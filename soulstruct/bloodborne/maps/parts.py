from __future__ import annotations

__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBObject",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBUnusedObject",
    "MSBUnusedCharacter",
    "MSBNavmesh",
    "MSBMapConnection",
    "MSBOtherPart",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb import MSBEntry
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.utils import GroupBitSet256
from soulstruct.bloodborne.game_types import *
from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import *
from .models import *
from .regions import MSBRegion

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBPart"

if tp.TYPE_CHECKING:
    from .events import MSBEnvironmentEvent


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart, abc.ABC):

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\sib\\layout.SIB"

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        description_offset: long
        name_offset: long
        _instance_index: int  # TK says "Unknown; appears to count up with each instance of a model added."
        _subtype_int: int
        _subtype_index: int
        model_index: int
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

    @dataclass(slots=True)
    class SUPERTYPE_DATA_STRUCT(BinaryStruct):
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

    # Set by further abstract subclasses.
    GPARAM_STRUCT: tp.ClassVar[BinaryStruct] = None
    SCENE_GPARAM_STRUCT: tp.ClassVar[BinaryStruct] = None

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
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

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        reader.seek(entry_offset + kwargs.pop("supertype_data_offset"))
        kwargs |= cls.SUPERTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)

        relative_gparam_data_offset = kwargs.pop("gparam_data_offset")
        if relative_gparam_data_offset > 0:
            if cls.GPARAM_STRUCT is None:
                raise ValueError(f"Found invalid non-zero Gparam offset in `{cls.__name__}` '{kwargs['name']}.")
            reader.seek(entry_offset + relative_gparam_data_offset)
            kwargs |= cls.GPARAM_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        relative_scene_gparam_data_offset = kwargs.pop("scene_gparam_data_offset")
        if relative_scene_gparam_data_offset > 0:
            if cls.SCENE_GPARAM_STRUCT is None:
                raise ValueError(f"Found invalid non-zero SceneGparam offset in `{cls.__name__}` '{kwargs['name']}.")
            reader.seek(entry_offset + relative_scene_gparam_data_offset)
            kwargs |= cls.SCENE_GPARAM_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        cls.SETATTR_CHECKS_DISABLED = True  # will be re-enabled in `__post_init__`
        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")

        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        description = reader.unpack_string(
            offset=entry_offset + header.pop("description_offset"), encoding=cls.NAME_ENCODING
        )
        sib_path = reader.unpack_string(offset=entry_offset + header.pop("sib_path_offset"), encoding=cls.NAME_ENCODING)
        kwargs = dict(
            name=name,
            description=description,
            sib_path=sib_path,
            _model_index=header.pop("model_index"),
        )
        return header.to_dict(ignore_underscore_prefix=True) | kwargs

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)
        supertype_data_offset = writer.position - entry_offset if self.SUPERTYPE_DATA_STRUCT is not None else 0
        writer.fill("supertype_data_offset", supertype_data_offset, obj=self)
        self.pack_supertype_data(writer, entry_offset, entry_lists)
        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)

        if self.GPARAM_STRUCT is not None:
            writer.fill("gparam_data_offset", writer.position - entry_offset, obj=self)
            self.GPARAM_STRUCT.object_to_writer(self, writer)
        else:
            writer.fill("gparam_data_offset", 0, obj=self)

        if self.SCENE_GPARAM_STRUCT is not None:
            writer.fill("scene_gparam_data_offset", writer.position - entry_offset, obj=self)
            self.SCENE_GPARAM_STRUCT.object_to_writer(self, writer)
        else:
            writer.fill("scene_gparam_data_offset", 0, obj=self)

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            description_offset=RESERVED,  # NOTE: Only Parts have descriptions.
            name_offset=RESERVED,
            _instance_index=0,  # TODO: Need to pass in...
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            model_index=self.try_index(entry_lists["MODEL_PARAM_ST"], "model"),
            sib_path_offset=RESERVED,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
            gparam_data_offset=RESERVED,
            scene_gparam_data_offset=RESERVED,
        )
        writer.fill("description_offset", writer.position - entry_offset, obj=self)
        packed_description = self.description.encode(self.NAME_ENCODING) + b"\0\0"
        writer.append(packed_description)
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        packed_name = self.name.encode(self.NAME_ENCODING) + b"\0\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=self)
        packed_sib_path = (self.sib_path.encode(self.NAME_ENCODING) + b"\0\0") if self.sib_path else b"\0\0"
        strings_size = len(packed_description + packed_name + packed_sib_path)
        if strings_size <= 0x38:
            packed_sib_path += b"\0" * (0x3c - strings_size)
        else:
            packed_sib_path += b"\0" * 8
        while len(packed_description + packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"  # Not done in SoulsFormats, but makes sense to me.
        writer.append(packed_sib_path)


@dataclass(slots=True, eq=False, repr=False)
class MSBPartWithGParam(MSBPart, abc.ABC):
    """Subclass of `MSBPart` that includes GParam fields."""

    @dataclass(slots=True)
    class GPARAM_STRUCT(BinaryStruct):
        light_set_id: int
        fog_id: int
        light_scattering_id: int
        environment_map_id: int
        _pad1: bytes = field(init=False, **BinaryPad(16))

    light_set_id: int = field(default=0, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=0, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))


@dataclass(slots=True, eq=False, repr=False)
class MSBPartWithSceneGParam(MSBPartWithGParam, abc.ABC):
    """Subclass of `MSBPart` that includes SceneGParam (and GParam) fields."""

    @dataclass(slots=True)
    class SCENE_GPARAM_STRUCT(BinaryStruct):
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

    sg_unk_x00_x04: int = field(default=0, **MapFieldInfo("Unk SceneG [x00-x04]", "Unknown SceneGparam integer."))
    sg_unk_x04_x08: int = field(default=0, **MapFieldInfo("Unk SceneG [x04-x08]", "Unknown SceneGparam integer."))
    sg_unk_x08_x0c: int = field(default=0, **MapFieldInfo("Unk SceneG [x08-x0c]", "Unknown SceneGparam integer."))
    sg_unk_x0c_x10: int = field(default=0, **MapFieldInfo("Unk SceneG [x0c-x10]", "Unknown SceneGparam integer."))
    sg_unk_x10_x14: int = field(default=0, **MapFieldInfo("Unk SceneG [x10-x14]", "Unknown SceneGparam integer."))
    sg_unk_x14_x18: int = field(default=0, **MapFieldInfo("Unk SceneG [x14-x18]", "Unknown SceneGparam integer."))
    event_ids: list[int] = field(default_factory=lambda: [-1] * 4, **MapFieldInfo("Event IDs", "Gparam Event IDs."))
    sg_unk_x40_x44: float = field(default=0.0, **MapFieldInfo("Unk SceneG [x40-x44]", "Unknown SceneGparam float."))


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPiece(MSBPartWithGParam):
    """No further fields beyond GParam."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapPiece

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(**BinaryPad(8))

    model: MSBMapPieceModel = None


@dataclass(slots=True, eq=False, repr=False)
class MSBObject(MSBPartWithGParam):
    """Interactable object. Note that Bloodborne has six-digit model IDs for Objects."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Object
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(4))
        _draw_parent_index: int
        break_term: sbyte
        net_sync_type: sbyte
        collision_hit_filter: bool
        set_main_object_structure_bools: bool
        animation_ids: list[short] = field(**BinaryArray(4))
        model_vfx_param_id_offsets: list[short] = field(**BinaryArray(4))

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

    _draw_parent_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _draw_parent_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "draw_parent"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBObject, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacter(MSBPartWithGParam):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(8))
        ai_id: int
        character_id: int
        talk_id: int
        player_id: int
        chr_unk_x18_x1c: int
        _draw_parent_index: int
        chr_unk_x20_x22: short
        _pad2: bytes = field(init=False, **BinaryPad(6))
        _patrol_regions_indices: list[short] = field(**BinaryArray(8))
        default_animation: int
        damage_animation: int

    model: MSBCharacterModel = None
    ai_id: int = field(default=-1, **MapFieldInfo(game_type=AIParam))
    character_id: int = field(default=-1, **MapFieldInfo(game_type=CharacterParam))
    talk_id: int = field(default=0, **MapFieldInfo(game_type=TalkScript))
    player_id: int = field(default=0, **MapFieldInfo(game_type=PlayerParam))
    draw_parent: MSBPart = None
    patrol_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 8)))
    )
    default_animation: int = -1
    damage_animation: int = -1
    chr_unk_x18_x1c: int = field(default=-1, **MapFieldInfo(
        "Unknown Chr [18-1c]", "Unknown Character integer. Usually -1."))
    chr_unk_x20_x22: int = field(default=-1, **MapFieldInfo(
        "Unknown Chr [20-22]", "Unknown Character integer. Usually -1."))

    _draw_parent_index: int = None
    _patrol_regions_indices: list[int] = field(default=None, **BinaryArray(8))

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "display_groups",
    )

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _draw_parent_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "draw_parent"),
            _patrol_regions_indices=self.try_index(entry_lists["POINT_PARAM_ST"], "patrol_regions"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBCharacter, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerStart(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.PlayerStart

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(16))

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "draw_groups",
        "display_groups",
    )

    model: MSBCharacterModel | MSBPlayerModel = None


@dataclass(slots=True, eq=False, repr=False, init=False)
class MSBCollision(MSBPartWithSceneGParam):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\sib\\h_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "environment_event"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        hit_filter_id: byte
        sound_space_type: byte
        _environment_event_index: short
        reflect_plane_height: float
        _place_name_banner_id: short  # -1 means use map area/block, and any negative value means banner is forced
        starts_disabled: bool
        unk_x0b_x0c: byte
        attached_lantern: int
        _play_region_id: int  # -10 or greater is real play region ID, less than -10 is a negated stable footing flag
        camera_1_id: short
        camera_2_id: short

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

    _environment_event_index: int = None

    # Internally managed.
    _force_place_name_banner: bool = field(default=True, repr=False)
    _play_region_id: int = field(default=0, repr=False)
    _stable_footing_flag: int = field(default=0, repr=False)

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        data = cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        # Negative area name means that banner will appear (-1 means get area name from map area/block).
        internal_place_name_banner_id = data.pop("_place_name_banner_id")
        if internal_place_name_banner_id != -1:
            data["place_name_banner_id"] = abs(internal_place_name_banner_id)
        data["_force_place_name_banner"] = internal_place_name_banner_id < 0
        
        internal_play_region_id = data.pop("_play_region_id")
        if internal_play_region_id > -10:
            data["_play_region_id"] = internal_play_region_id
            data["_stable_footing_flag"] = 0
        else:
            data["_play_region_id"] = 0
            data["_stable_footing_flag"] = -internal_play_region_id - 10
        
        return data

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        if self.place_name_banner_id == -1 and not self._force_place_name_banner:
            raise InvalidFieldValueError(
                "`force_place_name_banner` must be enabled if `place_name_banner_id == -1` (default)."
            )
        place_name_sign = -1 if self.place_name_banner_id >= 0 and self._force_place_name_banner else 1
        internal_place_name_banner_id = self.place_name_banner_id * place_name_sign
        if self._stable_footing_flag != 0:
            play_region_id = -self._stable_footing_flag - 10
        else:
            play_region_id = self._play_region_id
        return self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _environment_event_index=self.try_index(entry_lists["environments"], "environment_event"),
            _place_name_banner_id=internal_place_name_banner_id,
            _play_region_id=play_region_id,
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
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


MSBCollision.force_place_name_banner = property(
    MSBCollision.get_force_place_name_banner, MSBCollision.set_force_place_name_banner
)
MSBCollision.stable_footing_flag = property(
    MSBCollision.get_stable_footing_flag, MSBCollision.set_stable_footing_flag
)
MSBCollision.play_region_id = property(
    MSBCollision.get_play_region_id, MSBCollision.set_play_region_id
)


class MSBNavmesh(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Navmesh

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        # No 'navmesh_groups' anymore.
        _pad1: bytes = field(**BinaryPad(8))

    model: MSBNavmeshModel = None


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedCharacter


@dataclass(slots=True, eq=False, repr=False)
class MSBMapConnection(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapConnection
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _collision_index: int
        connected_map_id: list[sbyte] = field(**BinaryArray(4))
        _pad1: bytes = field(**BinaryPad(8))

    model: MSBCollisionModel = None
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [21, 0, 0, 0], **BinaryArray(4))

    _collision_index: int = None

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        data = cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)
        return data

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _collision_index=self.try_index(entry_lists["collisions"], "collision"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBMapConnection, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "collisions", "collision")

    def get_connected_map(self, get_map_func: tp.Callable):
        return get_map_func(self.connected_map_id)


class MSBOtherPart(MSBPart):
    """Unknown part (enum -1). No data."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.OtherPart
    SUBTYPE_DATA_STRUCT: tp.ClassVar = None

    model: MSBOtherModel = None
