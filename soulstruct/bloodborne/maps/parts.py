from __future__ import annotations

__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBObject",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBDummyObject",
    "MSBDummyCharacter",
    "MSBNavmesh",
    "MSBConnectCollision",
    "MSBOtherPart",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.utils import GroupBitSet256
from soulstruct.bloodborne.game_types import *
from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import *
from .models import *
from .regions import MSBRegion

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList
    from .events import MSBEnvironmentEvent


@dataclass(slots=True)
class PartHeaderStruct(MSBHeaderStruct):
    description_offset: long  # only game with descriptions!
    name_offset: long
    instance_index: int
    _subtype_int: int
    subtype_index: int
    _model_index: int = field(**EntryRef("MODEL_PARAM_ST"))
    sib_path_offset: long
    translate: Vector3
    rotate: Vector3
    scale: Vector3
    draw_groups: GroupBitSet256 = field(**BinaryArray(8, uint))
    display_groups: GroupBitSet256 = field(**BinaryArray(8, uint))
    backread_groups: GroupBitSet256 = field(**BinaryArray(8, uint))
    _pad1: bytes = field(init=False, **BinaryPad(4))
    supertype_data_offset: long
    subtype_data_offset: long
    gparam_data_offset: long
    scene_gparam_data_offset: long

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(PartHeaderStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)
        kwargs["sib_path"] = reader.unpack_string(
            offset=entry_offset + kwargs.pop("sib_path_offset"), encoding=entry_type.NAME_ENCODING
        )
        kwargs["description"] = reader.unpack_string(
            offset=entry_offset + kwargs.pop("description_offset"), encoding=entry_type.NAME_ENCODING)
        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(PartHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs["sib_path_offset"] = RESERVED
        kwargs["description_offset"] = RESERVED

    @classmethod
    def post_write(
        cls,
        entry: MSBPart,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        """Trying to be as faithful to vanilla as possible with padding."""
        writer.fill("description_offset", writer.position - entry_offset, obj=entry)
        packed_description = entry.description.encode(entry.NAME_ENCODING) + b"\0\0"
        writer.append(packed_description)
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        packed_name = entry.name.encode(entry.NAME_ENCODING) + b"\0\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=entry)
        packed_sib_path = (entry.sib_path.encode(entry.NAME_ENCODING) + b"\0\0") if entry.sib_path else b"\0\0"
        strings_size = len(packed_description + packed_name + packed_sib_path)
        if strings_size <= 0x38:
            packed_sib_path += b"\0" * (0x3c - strings_size)
        else:
            packed_sib_path += b"\0" * 8
        while len(packed_description + packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"  # Not done in SoulsFormats, but makes sense to me.
        writer.append(packed_sib_path)


@dataclass(slots=True)
class PartDataStruct(MSBBinaryStruct):
    entity_id: int
    part_unk_x04_x05: sbyte
    part_unk_x05_x06: sbyte
    part_unk_x06_x07: sbyte
    part_unk_x07_x08: sbyte
    _pad1: bytes = field(**BinaryPad(4))
    lantern_id: byte
    lod_id: sbyte
    part_unk_x0e_x0f: byte
    part_unk_x0f_x10: byte


@dataclass(slots=True)
class GParamDataStruct(MSBBinaryStruct):
    light_set_id: int
    fog_id: int
    light_scattering_id: int
    environment_map_id: int
    _pad1: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True)
class SceneGParamDataStruct(MSBBinaryStruct):
    sg_unk_x00_x04: int
    sg_unk_x04_x08: int
    sg_unk_x08_x0c: int
    sg_unk_x0c_x10: int
    sg_unk_x10_x14: int
    sg_unk_x14_x18: int
    _pad1: bytes = field(init=False, **BinaryPad(36))
    event_ids: list[byte] = field(**BinaryArray(4))
    sg_unk_x40_x44: float
    _pad2: bytes = field(init=False, **BinaryPad(12))


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart, abc.ABC):

    HEADER_STRUCT = PartHeaderStruct
    STRUCTS = {
        "supertype_data": PartDataStruct,
    }

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\sib\\layout.SIB"
    GROUP_BIT_COUNT: tp.ClassVar[int] = 256

    # NOTE: `model` defined by subclasses.
    backread_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    part_unk_x04_x05: int = field(default=-1, **MapFieldInfo(
        "Unknown Parts Data [x04-x05]", "Unknown parts integer. Common values: -1, 0, 8"))
    part_unk_x05_x06: int = field(default=-1, **MapFieldInfo(
        "Unknown Parts Data [x05-x06]", "Unknown parts integer. Common values: -1, 0, 82"))
    part_unk_x06_x07: int = field(default=-1, **MapFieldInfo(
        "Unknown Parts Data [x06-x07]", "Unknown parts integer. Common values: -1, 0"))
    part_unk_x07_x08: int = field(default=-1, **MapFieldInfo(
        "Unknown Parts Data [x07-x08]", "Unknown parts integer. Common values: -1, 0"))
    lantern_id: int = field(default=0, **MapFieldInfo("Lantern ID", "Lantern param ID."))
    lod_id: int = field(default=-1, **MapFieldInfo("LoD ID", "LoD (level of detail) param ID."))
    part_unk_x0e_x0f: int = field(default=-1, **MapFieldInfo(
        "Unknown Parts Data [x0e-x0f]", "Unknown parts integer. Common values: 20, 22"))
    part_unk_x0f_x10: int = field(default=0, **MapFieldInfo(
        "Unknown Parts Data [x0f-x10]", "Unknown parts integer. Common values: 0"))


@dataclass(slots=True)
class MapPieceDataStruct(MSBBinaryStruct):
    _pad1: bytes = field(**BinaryPad(8))


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPiece(MSBPart):
    """No further fields beyond GParam."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapPiece
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": MapPieceDataStruct,
        "gparam_data": GParamDataStruct,
        "scene_gparam_data": None,
    }

    model: MSBMapPieceModel = None

    # GPARAM
    light_set_id: int = field(default=0, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=0, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))


@dataclass(slots=True)
class ObjectDataStruct(MSBBinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(4))
    _draw_parent_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    break_term: sbyte
    net_sync_type: sbyte
    collision_hit_filter: bool
    set_main_object_structure_bools: bool
    animation_ids: list[short] = field(**BinaryArray(4))
    model_vfx_param_id_offsets: list[short] = field(**BinaryArray(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBObject(MSBPart):
    """Interactable object. Note that Bloodborne has six-digit model IDs for Objects."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Object
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent"]
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": ObjectDataStruct,
        "gparam_data": GParamDataStruct,
        "scene_gparam_data": None,
    }

    HIDE_FIELDS: tp.ClassVar[str] = (
        "scale",
        "display_groups",
        "backread_groups",
    )

    model: MSBObjectModel = None

    draw_parent: MSBPart = None
    break_term: int = -1
    net_sync_type: int = -1
    collision_hit_filter: bool = False
    set_main_object_structure_bools: bool = False
    animation_ids: list[int] = field(default_factory=lambda: [0, 0, -1, -1])
    model_vfx_param_id_offsets: list[int] = field(default_factory=lambda: [-1, -1, 0, 0])

    # GPARAM
    light_set_id: int = field(default=0, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=0, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    _draw_parent_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBObject, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")


@dataclass(slots=True)
class CharacterDataStruct(MSBBinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(8))
    ai_id: int
    character_id: int
    talk_id: int
    player_id: int
    chr_unk_x18_x1c: int
    _draw_parent_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    chr_unk_x20_x22: short
    _pad2: bytes = field(init=False, **BinaryPad(6))
    _patrol_regions_indices: list[short] = field(**EntryRef("POINT_PARAM_ST", array_size=8))
    default_animation: int
    damage_animation: int


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacter(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_regions"]
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": CharacterDataStruct,
        "gparam_data": GParamDataStruct,
        "scene_gparam_data": None,
    }

    model: MSBCharacterModel = None

    ai_id: int = field(default=-1, **MapFieldInfo(game_type=AIParam))
    character_id: int = field(default=-1, **MapFieldInfo(game_type=CharacterParam))
    talk_id: int = field(default=0, **MapFieldInfo(game_type=TalkScript))
    player_id: int = field(default=0, **MapFieldInfo(game_type=PlayerParam))
    draw_parent: MSBPart = None
    patrol_regions: list[MSBRegion | None] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 8)))
    )
    default_animation: int = -1
    damage_animation: int = -1
    chr_unk_x18_x1c: int = field(default=-1, **MapFieldInfo(
        "Unknown Chr [18-1c]", "Unknown Character integer. Usually -1."))
    chr_unk_x20_x22: int = field(default=-1, **MapFieldInfo(
        "Unknown Chr [20-22]", "Unknown Character integer. Usually -1."))

    # GPARAM
    light_set_id: int = field(default=0, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=0, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    _draw_parent_index: int = None
    _patrol_regions_indices: list[int] = field(default=None, **BinaryArray(8))

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "display_groups",
    )

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBCharacter, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


@dataclass(slots=True)
class PlayerStartDataStruct(MSBBinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerStart(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.PlayerStart
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": PlayerStartDataStruct,
        "gparam_data": None,
        "scene_gparam_data": None,
    }

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "draw_groups",
        "display_groups",
    )

    model: MSBCharacterModel | MSBPlayerModel = None


@dataclass(slots=True)
class CollisionDataStruct(MSBBinaryStruct):
    hit_filter_id: byte
    sound_space_type: byte
    _environment_event_index: short = field(**EntryRef("environments"))
    reflect_plane_height: float
    _place_name_banner_id: short  # -1 means use map area/block, and any negative value means banner is forced
    starts_disabled: bool
    unk_x0b_x0c: byte
    attached_lantern: int
    _play_region_id: int  # -10 or greater is real play region ID, less than -10 is a negated stable footing flag
    camera_1_id: short
    camera_2_id: short

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(CollisionDataStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)

        # Negative area name means that banner will appear (-1 means get area name from map area/block).
        internal_place_name_banner_id = kwargs.pop("_place_name_banner_id")
        if internal_place_name_banner_id != -1:
            kwargs["place_name_banner_id"] = abs(internal_place_name_banner_id)
        kwargs["force_place_name_banner"] = internal_place_name_banner_id < 0

        # Play Region ID that is -10 or less is a stable footing flag (negated with 10 subtracted from it).
        internal_play_region_id = kwargs.pop("_play_region_id")
        if internal_play_region_id > -10:
            kwargs["play_region_id"] = internal_play_region_id
            kwargs["stable_footing_flag"] = 0
        else:
            kwargs["play_region_id"] = 0
            kwargs["stable_footing_flag"] = -internal_play_region_id - 10

        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBCollision,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:

        # Determine internal banner ID (negative if forced).
        if entry.place_name_banner_id == -1 and not entry._force_place_name_banner:
            raise InvalidFieldValueError(
                "`force_place_name_banner` must be enabled if `place_name_banner_id == -1` (default)."
            )
        place_name_sign = -1 if entry.place_name_banner_id >= 0 and entry._force_place_name_banner else 1
        kwargs["_place_name_banner_id"] = entry.place_name_banner_id * place_name_sign

        # Resolve play region ID or stable footing flag.
        if entry._stable_footing_flag != 0:
            kwargs["play_region_id"] = -entry._stable_footing_flag - 10
        else:
            kwargs["play_region_id"] = entry._play_region_id


@dataclass(slots=True, eq=False, repr=False)
class MSBCollision(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\sib\\h_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "environment_event"]
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": CollisionDataStruct,
        "gparam_data": GParamDataStruct,
        "scene_gparam_data": SceneGParamDataStruct,
    }

    # Internally managed. (It's important that these come before their wrapper fields!)
    _force_place_name_banner: bool = field(default=True, repr=False)
    _play_region_id: int = field(default=0, repr=False)
    _stable_footing_flag: int = field(default=0, repr=False)

    # Field type overrides.
    model: MSBCollisionModel = None
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)

    hit_filter_id: int = field(default=CollisionHitFilter.Normal.value, **MapFieldInfo(game_type=CollisionHitFilter))
    sound_space_type: int = 0
    environment_event: MSBEnvironmentEvent = None  # NOTE: imported under TYPE_CHECKING to avoid circular import
    reflect_plane_height: float = 0.0
    place_name_banner_id: int = field(default=-1, **MapFieldInfo(game_type=PlaceName))
    force_place_name_banner: bool = True  # necessary default because `place_name_banner_id` defaults to -1
    starts_disabled: bool = False
    # TODO: Confirm Bloodborne uses the same signed combined field as DS1 for play region and stable footing.
    play_region_id: int = 0
    stable_footing_flag: int = 0  # TODO: event flag type
    camera_1_id: int = field(default=-1, **MapFieldInfo(game_type=CameraParam))
    camera_2_id: int = field(default=-1, **MapFieldInfo(game_type=CameraParam))
    unk_x0b_x0c: int = field(default=0, **MapFieldInfo("Unknown [x0b-x0c]", "Unknown Collision integer.")),
    attached_lantern: int = 0

    # GPARAM
    light_set_id: int = field(default=0, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=0, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # SCENE GPARAM
    sg_unk_x00_x04: int = field(default=0, **MapFieldInfo("Unk SceneG [x00-x04]", "Unknown SceneGparam integer."))
    sg_unk_x04_x08: int = field(default=0, **MapFieldInfo("Unk SceneG [x04-x08]", "Unknown SceneGparam integer."))
    sg_unk_x08_x0c: int = field(default=0, **MapFieldInfo("Unk SceneG [x08-x0c]", "Unknown SceneGparam integer."))
    sg_unk_x0c_x10: int = field(default=0, **MapFieldInfo("Unk SceneG [x0c-x10]", "Unknown SceneGparam integer."))
    sg_unk_x10_x14: int = field(default=0, **MapFieldInfo("Unk SceneG [x10-x14]", "Unknown SceneGparam integer."))
    sg_unk_x14_x18: int = field(default=0, **MapFieldInfo("Unk SceneG [x14-x18]", "Unknown SceneGparam integer."))
    event_ids: list[int] = field(default_factory=lambda: [-1] * 4, **MapFieldInfo("Event IDs", "Gparam Event IDs."))
    sg_unk_x40_x44: float = field(default=0.0, **MapFieldInfo("Unk SceneG [x40-x44]", "Unknown SceneGparam float."))

    _environment_event_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBCollision, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "environments", "environment_event")

    def get_force_place_name_banner(self):
        return self._force_place_name_banner

    def set_force_place_name_banner(self, value: bool):
        if not value and self.place_name_banner_id == -1:
            raise InvalidFieldValueError(
                "Banner must appear when area name is set to default (-1).\n"
                "You must specify the area name manually to set this to False."
            )
        self._force_place_name_banner = bool(value)

    def get_play_region_id(self):
        return self._play_region_id

    def set_play_region_id(self, value):
        if value != 0 and self._stable_footing_flag != 0:
            raise InvalidFieldValueError(
                f"Cannot set 'play_region_id' to a non-zero value ({value}) while `stable_footing_flag` is non-zero."
            )
        if not isinstance(value, int) or value <= -10:
            raise InvalidFieldValueError("'play_region_id' must be an integer greater than or equal to -9.")
        self._play_region_id = value

    def get_stable_footing_flag(self):
        return self._stable_footing_flag

    def set_stable_footing_flag(self, value):
        if not isinstance(value, int) or value < -1:
            raise InvalidFieldValueError(
                f"`stable_footing_flag` must be an integer no less than -1 (Collision '{self.name}')."
            )
        if value != 0 and self._play_region_id != 0:
            raise InvalidFieldValueError(
                f"Cannot set `stable_footing_flag` to a non-zero value while 'play_region_id' is not zero, even if it "
                f"is just -1: {self._play_region_id} (Collision '{self.name}')."
            )
        self._stable_footing_flag = value


# Still slightly awkward to get dataclasses, properties, and `__init__` to interact well. This is the workaround.
MSBCollision.force_place_name_banner = property(
    lambda self: self.get_force_place_name_banner(),
    lambda self, value: self.set_force_place_name_banner(value),
)
MSBCollision.stable_footing_flag = property(
    lambda self: self.get_stable_footing_flag(),
    lambda self, value: self.set_stable_footing_flag(value),
)
MSBCollision.play_region_id = property(
    lambda self: self.get_play_region_id(),
    lambda self, value: self.set_play_region_id(value),
)


@dataclass(slots=True)
class NavmeshDataStruct(MSBBinaryStruct):
    # No 'navmesh_groups' anymore.
    _pad1: bytes = field(**BinaryPad(8))


class MSBNavmesh(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Navmesh
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": NavmeshDataStruct,
        "gparam_data": None,
        "scene_gparam_data": None,
    }

    model: MSBNavmeshModel = None


class MSBDummyObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.DummyObject


class MSBDummyCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.DummyCharacter


@dataclass(slots=True)
class ConnectCollisionDataStruct(MSBBinaryStruct):
    _collision_index: int = field(**EntryRef("collisions"))
    connected_map_id: list[sbyte] = field(**BinaryArray(4))
    _pad1: bytes = field(**BinaryPad(8))


@dataclass(slots=True, eq=False, repr=False)
class MSBConnectCollision(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.ConnectCollision
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": ConnectCollisionDataStruct,
        "gparam_data": None,
        "scene_gparam_data": None,
    }

    model: MSBCollisionModel = None
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [21, 0, 0, 0], **BinaryArray(4))

    _collision_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBConnectCollision, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "collisions", "collision")

    @property
    def connected_map_stem(self) -> str:
        aa, bb, cc, dd = self.connected_map_id
        return f"m{aa:02d}_{bb:02d}_{cc:02d}_{dd:02d}"

    @connected_map_stem.setter
    def connected_map_stem(self, value: str):
        if not value.startswith("m"):
            raise ValueError(f"Connected map stem must start with 'm'.")
        aa, bb, cc, dd = value[1:].split("_")
        self.connected_map_id = [int(aa), int(bb), int(cc), int(dd)]

    def get_connected_map(self, get_map_func: tp.Callable):
        return get_map_func(self.connected_map_id)


class MSBOtherPart(MSBPart):
    """Unknown part (enum -1). No data."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.OtherPart
    STRUCTS = MSBPart.STRUCTS | {
        "subtype_data": None,
        "gparam_data": None,
        "scene_gparam_data": None,
    }

    model: MSBOtherModel = None
