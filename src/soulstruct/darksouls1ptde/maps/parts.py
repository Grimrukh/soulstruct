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
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.utils import BitSet128
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import EulerDeg, Vector3

from .enums import *
from .models import *
from .regions import MSBRegion

if tp.TYPE_CHECKING:
    from .events import MSBEnvironmentEvent


class PartHeaderStruct(MSBHeaderStruct):
    # No description offset.
    name_offset: int
    # No supertype index.
    _subtype_int: int
    subtype_index: int
    _model_index: int = field(**EntryRef("MODEL_PARAM_ST"))
    sib_path_offset: int
    translate: Vector3
    rotate: EulerDeg
    scale: Vector3
    draw_groups: BitSet128 = binary_array(4, uint)
    display_groups: BitSet128 = binary_array(4, uint)
    supertype_data_offset: int
    subtype_data_offset: int
    # No other structs (Gparam, SceneGparam, etc.).
    _pad1: bytes = binary_pad(4)

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
        kwargs.pop("supertype_index")

    @classmethod
    def post_write(
        cls,
        entry: MSBPart,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        """Trying to be as faithful to vanilla as possible with padding."""
        strings_position = writer.position - entry_offset
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        packed_name = entry.name.encode(entry.NAME_ENCODING) + b"\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=entry)
        packed_sib_path = (entry.sib_path.encode(entry.NAME_ENCODING) + b"\0") if entry.sib_path else b"\0"
        writer.append(packed_sib_path)
        writer.pad_align(4)
        # Minimum combined length of name and SIB path is 20 bytes, so pad if necessary.
        if writer.position - strings_position < 20:
            writer.pad(0x14 - (writer.position - strings_position))


class PartSupertypeData(MSBBinaryStruct):
    """Uses old `DrawParam` fields here, rather than separate Gparam/SceneGparam structs."""
    entity_id: int
    ambient_light_id: sbyte
    fog_id: sbyte
    scattered_light_id: sbyte
    lens_flare_id: sbyte
    shadow_id: sbyte
    dof_id: sbyte
    tone_map_id: sbyte
    tone_correction_id: sbyte
    point_light_id: sbyte
    lod_id: sbyte
    _pad1: bytes = binary_pad(1)
    is_shadow_source: bool
    is_shadow_destination: bool
    is_shadow_only: bool
    draw_by_reflect_cam: bool
    draw_only_reflect_cam: bool
    use_depth_bias_float: bool
    disable_point_light_effect: bool
    _pad2: bytes = binary_pad(2)


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart[BitSet128], abc.ABC):

    HEADER_STRUCT = PartHeaderStruct
    STRUCTS = {
        "supertype_data": PartSupertypeData,
        # Subtypes add their own struct or lack thereof (`None`).
    }

    NAME_ENCODING: tp.ClassVar[str] = "shift-jis"  # NOT `shift_jis_2004` (backslashes in SIB paths)
    BIT_SET_TYPE: tp.ClassVar = BitSet128

    # NOTE: `model` type overridden by subclasses.
    # Subclasses may also use more appropriate defaults for convenience, as these Part supertype fields in DS1 are
    # really sporadic in which Part subtypes actually use each of them.
    draw_groups: BitSet128 = field(default_factory=BitSet128.all_off)
    display_groups: BitSet128 = field(default_factory=BitSet128.all_off)
    ambient_light_id: int = field(default=-1, **MapFieldInfo(game_type=BakedLightParam))
    fog_id: int = field(default=-1, **MapFieldInfo(game_type=FogParam))
    scattered_light_id: int = field(default=-1, **MapFieldInfo(game_type=ScatteredLightParam))
    lens_flare_id: int = field(default=-1, **MapFieldInfo(game_type=LensFlareSourceParam))
    shadow_id: int = field(default=-1, **MapFieldInfo(game_type=ShadowParam))
    dof_id: int = field(default=-1, **MapFieldInfo(game_type=DepthOfFieldParam))
    tone_map_id: int = field(default=-1, **MapFieldInfo(game_type=ToneMappingParam))
    point_light_id: int = field(default=-1, **MapFieldInfo(game_type=PointLightParam))
    tone_correction_id: int = field(default=-1, **MapFieldInfo(game_type=ToneCorrectionParam))
    lod_id: int = -1
    is_shadow_source: bool = False
    is_shadow_destination: bool = False
    is_shadow_only: bool = False
    draw_by_reflect_cam: bool = False
    draw_only_reflect_cam: bool = False
    use_depth_bias_float: bool = False
    disable_point_light_effect: bool = False


class MapPieceDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPiece(MSBPart):
    """Just a textured, visible mesh asset. Does not include any collision."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapPiece
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\layout.SIB"
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": MapPieceDataStruct}

    model: MSBMapPieceModel = None

    HIDE_FIELDS = (
        "scale",
        "display_groups",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "is_shadow_source",
        "is_shadow_only",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    def set_all_lighting_fields(self, value: int):
        """Set all (Map Piece-used) lighting fields to the same value."""
        self.ambient_light_id = value
        self.fog_id = value
        self.scattered_light_id = value


class ObjectDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(4, init=False)
    _draw_parent_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    break_term: sbyte
    net_sync_type: sbyte
    _pad2: bytes = binary_pad(2, init=False)
    default_animation: short
    unk_x0e: short
    unk_x10: int
    _pad3: bytes = binary_pad(4, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBObject(MSBPart):
    """Instance of a physical object."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Object
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\o_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": ObjectDataStruct}

    HIDE_FIELDS: tp.ClassVar[tuple] = (
        "scale",  # NOTE: works, but only object visual FLVER will be scaled (not HKX collision or animations)
        "display_groups",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "lod_id",
        "unk_x0e",
        "unk_x10",
        "use_depth_bias_float",
    )

    # Replace types/defaults.
    model: MSBObjectModel = None
    draw_parent: MSBPart = None
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    break_term: int = 0
    net_sync_type: int = 0
    default_animation: int = -1
    unk_x0e: int = 0
    unk_x10: int = 0

    _draw_parent_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBObject, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")

    def set_all_lighting_fields(self, value: int):
        """Set all (Object-used) lighting fields to the same value."""
        self.ambient_light_id = value
        self.fog_id = value
        self.scattered_light_id = value


class CharacterDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(8, init=False)
    ai_id: int
    character_id: int
    talk_id: int
    patrol_type: byte
    _pad2: bytes = binary_pad(1, init=False)
    platoon_id: ushort
    player_id: int
    _draw_parent_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _pad3: bytes = binary_pad(8, init=False)
    _patrol_regions_indices: list[short] = field(**EntryRef("POINT_PARAM_ST", array_size=8))
    default_animation: int
    damage_animation: int


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacter(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""  # empty
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_regions"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": CharacterDataStruct}

    # Override types/defaults.
    model: MSBCharacterModel | MSBPlayerModel = None
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    ai_id: int = field(default=-1, **MapFieldInfo(game_type=AIParam))
    character_id: int = field(default=-1, **MapFieldInfo(game_type=CharacterParam))
    talk_id: int = field(default=0, **MapFieldInfo(game_type=TalkScript))
    platoon_id: int = 0
    patrol_type: int = 0
    player_id: int = field(default=-1, **MapFieldInfo(game_type=PlayerParam))
    draw_parent: MSBPart = None
    patrol_regions: list[MSBRegion | None] = field(
        default_factory=lambda: [None] * 8,
        **MapFieldInfo(game_type=GameObjectIntSequence((Region, 8))),
    )
    default_animation: int = -1
    damage_animation: int = -1

    _draw_parent_index: int = None
    _patrol_regions_indices: list[int] = binary_array(8, default=None)

    HIDE_FIELDS = (
        "scale",
        "display_groups",
        "platoon_id",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "lod_id",
        "use_depth_bias_float",
    )

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBCharacter, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


class PlayerStartDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(16, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerStart(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.PlayerStart
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": PlayerStartDataStruct}

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "sib_path",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    # Override types/defaults.
    model: MSBCharacterModel | MSBPlayerModel = None
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True


class CollisionDataStruct(MSBBinaryStruct):
    hit_filter_id: byte
    sound_space_type: byte
    _environment_event_index: short = field(**EntryRef("environments"))
    reflect_plane_height: float
    navmesh_groups: BitSet128 = binary_array(4, uint)
    vagrant_entity_ids: list[int] = binary_array(3)
    place_name_banner_id_: short  # -1 means use map area/block, and any negative value means banner is forced
    starts_disabled: bool
    unk_x27_x28: byte
    attached_bonfire: int
    _minus_ones: list[int] = binary_array(3, asserted=[-1, -1, -1])  # never used
    play_region_id_: int  # -10 or greater is real play region ID, less than -10 is a negated stable footing flag
    camera_1_id: short
    camera_2_id: short
    _pad1: bytes = binary_pad(16)

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(CollisionDataStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)

        # Negative area name means that banner will appear (-1 means get area name from map area/block).
        internal_place_name_banner_id = kwargs.pop("place_name_banner_id_")
        if internal_place_name_banner_id != -1:
            kwargs["place_name_banner_id"] = abs(internal_place_name_banner_id)
        kwargs["force_place_name_banner"] = internal_place_name_banner_id < 0

        # Play Region ID that is -10 or less is a stable footing flag (negated with 10 subtracted from it).
        internal_play_region_id = kwargs.pop("play_region_id_")
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
        super(CollisionDataStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)

        # Determine internal banner ID (negative if forced).
        if entry.place_name_banner_id == -1 and not entry._force_place_name_banner:
            raise InvalidFieldValueError(
                "`force_place_name_banner` must be enabled if `place_name_banner_id == -1` (default)."
            )
        place_name_sign = -1 if entry.place_name_banner_id >= 0 and entry._force_place_name_banner else 1
        kwargs["place_name_banner_id_"] = entry.place_name_banner_id * place_name_sign

        # Resolve play region ID or stable footing flag.
        if entry._stable_footing_flag != 0:
            kwargs["play_region_id_"] = -entry._stable_footing_flag - 10
        else:
            kwargs["play_region_id_"] = entry._play_region_id


# noinspection PyRedeclaration
@dataclass(slots=True, eq=False, repr=False)
class MSBCollision(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\h_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "environment_event"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": CollisionDataStruct}

    # Internally managed. (It's important that these come before their wrapper fields!)
    _force_place_name_banner: bool = field(default=True, repr=False)
    _play_region_id: int = field(default=0, repr=False)
    _stable_footing_flag: int = field(default=0, repr=False)

    # Field type/default overrides.
    model: MSBCollisionModel = None
    display_groups: BitSet128 = field(default_factory=BitSet128.all_on)  # all ON by default
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    hit_filter_id: int = field(default=CollisionHitFilter.Normal.value, **MapFieldInfo(game_type=CollisionHitFilter))
    sound_space_type: int = 0
    # NOTE: imported under TYPE_CHECKING to avoid circular import.
    # I recommend ignoring this field and calling `MSB.set_collision_environment_references()` before exporting.
    environment_event: MSBEnvironmentEvent = None
    reflect_plane_height: float = 0.0
    navmesh_groups: BitSet128 = None  # defaults to being the same as `display_groups`
    vagrant_entity_ids: list[int] = field(default_factory=lambda: [-1, -1, -1])
    place_name_banner_id: int = field(default=-1, **MapFieldInfo(game_type=PlaceName))
    force_place_name_banner: bool = True  # necessary default because `place_name_banner_id` defaults to -1
    starts_disabled: bool = False
    play_region_id: int = 0
    stable_footing_flag: int = 0  # TODO: event flag type
    camera_1_id: int = field(default=-1, **MapFieldInfo(game_type=CameraParam))
    camera_2_id: int = field(default=-1, **MapFieldInfo(game_type=CameraParam))
    unk_x27_x28: int = field(default=0, **MapFieldInfo("Unknown [x27-x28]", "Unknown Collision byte."))
    attached_bonfire: int = 0

    _environment_event_index: int = None

    HIDE_FIELDS = (
        "scale",
        # "unk_x27_x28",  # TODO: Not hiding this, as some rare collisions do use it, e.g. Anor Londo spinning tower.
        "use_depth_bias_float",
    )

    def __post_init__(self):
        """`navmesh_groups` default (if `None`) to same as `display_groups`."""
        if self.navmesh_groups is None:
            self.navmesh_groups = self.display_groups.copy()

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

    def set_all_lighting_fields(self, value: int):
        """Set all lighting fields to the same value."""
        self.ambient_light_id = value
        self.fog_id = value
        self.scattered_light_id = value
        self.lens_flare_id = value
        self.shadow_id = value
        self.dof_id = value
        self.tone_map_id = value
        self.point_light_id = value
        self.tone_correction_id = value


# Still slightly awkward to get dataclasses, properties, and `__init__` to interact well. This is the workaround.
# noinspection PyTypeChecker
MSBCollision.force_place_name_banner = property(
    lambda self: self.get_force_place_name_banner(),
    lambda self, value: self.set_force_place_name_banner(value),
)
# noinspection PyTypeChecker
MSBCollision.stable_footing_flag = property(
    lambda self: self.get_stable_footing_flag(),
    lambda self, value: self.set_stable_footing_flag(value),
)
# noinspection PyTypeChecker
MSBCollision.play_region_id = property(
    lambda self: self.get_play_region_id(),
    lambda self, value: self.set_play_region_id(value),
)


class NavmeshDataStruct(MSBBinaryStruct):
    navmesh_groups: BitSet128 = binary_array(4, uint)
    _pad1: bytes = binary_pad(16)


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmesh(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Navmesh
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\n_layout.SIB"
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": NavmeshDataStruct}

    # Type/default overrides.
    model: MSBNavmeshModel = None

    navmesh_groups: BitSet128 = field(default_factory=BitSet128.all_off)  # all OFF by default

    HIDE_FIELDS = (
        "scale",
        "sib_path",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyObject(MSBObject):
    """Object not loaded in normal gameplay.

    May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`.
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.DummyObject
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""  # no SIB path, unlike real objects


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyCharacter(MSBCharacter):
    """Character not loaded in normal gameplay.

    May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`.
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.DummyCharacter
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""


class ConnectCollisionDataStruct(MSBBinaryStruct):
    _collision_index: int = field(**EntryRef("collisions"))
    connected_map_id: list[sbyte] = binary_array(4)
    _pad1: bytes = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBConnectCollision(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.ConnectCollision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": ConnectCollisionDataStruct}

    model: MSBCollisionModel = None
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [10, 0, 0, 0], **BinaryArray(4))

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
