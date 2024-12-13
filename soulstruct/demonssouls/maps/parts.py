from __future__ import annotations

__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBObject",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBProtoboss",
    "MSBNavmesh",
    "MSBDummyObject",
    "MSBDummyCharacter",
    "MSBConnectCollision",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.utils import GroupBitSet128
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import *
from .models import *
from .regions import MSBRegion


class PartHeaderStruct(MSBHeaderStruct):
    # No description offset.
    name_offset: int
    # No supertype index.
    _subtype_int: int
    subtype_index: int
    _model_index: int = field(**EntryRef("MODEL_PARAM_ST"))
    sib_path_offset: int
    translate: Vector3
    rotate: Vector3
    scale: Vector3
    draw_groups: GroupBitSet128 = binary_array(4, uint)
    display_groups: GroupBitSet128 = binary_array(4, uint)
    supertype_data_offset: int
    subtype_data_offset: int
    # No other structs (Gparam, SceneGparam, etc.).
    _pad1: bytes = binary_pad(8)  # note that this is longer than in DS1

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
        strings_position = writer.position
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        packed_name = entry.name.encode(entry.NAME_ENCODING) + b"\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=entry)
        packed_sib_path = (entry.sib_path.encode(entry.NAME_ENCODING) + b"\0") if entry.sib_path else b"\0"
        writer.append(packed_sib_path)
        writer.pad_align(4)
        # Pad out to minimum combined length of name and SIB path.
        strings_size = writer.position - strings_position
        if strings_size < 0x10:
            writer.pad(0x10 - strings_size)


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
    unk_x0e: byte  # always zero in DS1
    is_shadow_source: bool
    is_shadow_destination: bool
    is_shadow_only: bool
    draw_by_reflect_cam: bool
    draw_only_reflect_cam: bool
    use_depth_bias_float: bool
    disable_point_light_effect: bool
    _pad2: bytes = binary_pad(2)


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart, abc.ABC):

    HEADER_STRUCT = PartHeaderStruct
    STRUCTS = {
        "supertype_data": PartSupertypeData,
        # Subtypes add their own struct or lack thereof (`None`).
    }

    NAME_ENCODING: tp.ClassVar[str] = "shift-jis"  # NOT `shift_jis_2004` (backslashes in SIB paths)
    GROUP_BIT_COUNT: tp.ClassVar[int] = 128  # 4 ints

    # NOTE: `model` type overridden by subclasses.
    # Subclasses may also use more appropriate defaults for convenience, as these Part supertype fields in DS1 are
    # really sporadic in which Part subtypes actually use each of them.
    draw_groups: GroupBitSet128 = field(default_factory=GroupBitSet128.all_off)
    display_groups: GroupBitSet128 = field(default_factory=GroupBitSet128.all_off)
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
    unk_x0e: int = 0  # TODO: default?
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
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\{name}.sib"
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
    # No draw parent in DeS.
    break_term: sbyte
    net_sync_type: sbyte
    _pad2: bytes = binary_pad(2, init=False)
    default_animation: short
    # NOTE: Offsets are wrong by -2, but better to keep synced with DS1 names.
    unk_x0e: short
    unk_x10: int
    _pad3: bytes = binary_pad(8, init=False)  # longer than in DS1


@dataclass(slots=True, eq=False, repr=False)
class MSBObject(MSBPart):
    """Instance of a physical object."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Object
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\layout_obj.SIB"
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
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    break_term: int = 0
    net_sync_type: int = 0
    default_animation: int = -1
    unk_x0e: int = 0
    unk_x10: int = 0

    def set_all_lighting_fields(self, value: int):
        """Set all (Object-used) lighting fields to the same value."""
        self.ambient_light_id = value
        self.fog_id = value
        self.scattered_light_id = value


class CharacterDataStruct(MSBBinaryStruct):
    unk_x00: int
    unk_x04: int
    unk_x08: float  # note lack of Think param!
    character_id: int
    talk_id: int
    patrol_type: byte
    _pad2: bytes = binary_pad(1, init=False)
    platoon_id: ushort
    player_id: int
    _draw_parent_index: int = field(**EntryRef("PARTS_PARAM_ST"))  # still here, unlike Objects
    _pad3: bytes = binary_pad(8, init=False)
    _patrol_regions_indices: list[short] = field(**EntryRef("POINT_PARAM_ST", array_size=8))
    default_animation: int
    damage_animation: int


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacter(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\c_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_regions"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": CharacterDataStruct}

    # Override types/defaults.
    model: MSBCharacterModel | MSBPlayerModel = None
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    unk_x00: int = 0  # TODO: default?
    unk_x04: int = 0  # TODO: default?
    unk_x08: float = 0.0  # TODO: default?
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
    unk_x00: byte  # always zero in DS1
    _pad1: bytes = binary_pad(15, init=False)


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

    unk_x00: int = 0  # TODO: default?


class CollisionDataStruct(MSBBinaryStruct):
    hit_filter_id: byte
    sound_space_type: byte
    cubemap_index: short
    reflect_plane_height: float
    navmesh_groups: GroupBitSet128 = binary_array(4, uint)
    ref_tex_ids: list[short] = binary_array(16)
    unk_x38: short
    place_name_banner_id_: short  # -1 means use map area/block, and any negative value means banner is forced
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
        # TODO: Still true in DeS?
        internal_place_name_banner_id = kwargs.pop("place_name_banner_id_")
        if internal_place_name_banner_id != -1:
            kwargs["place_name_banner_id"] = abs(internal_place_name_banner_id)
        kwargs["force_place_name_banner"] = internal_place_name_banner_id < 0

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


# noinspection PyRedeclaration
@dataclass(slots=True, eq=False, repr=False)
class MSBCollision(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\h_layout.SIB"
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": CollisionDataStruct}

    # Internally managed. (It's important that these come before their wrapper fields!)
    _force_place_name_banner: bool = field(default=True, repr=False)

    # Field type overrides.
    model: MSBCollisionModel = None
    display_groups: GroupBitSet128 = field(default_factory=GroupBitSet128.all_on)  # all ON by default
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    hit_filter_id: int = field(default=CollisionHitFilter.Normal.value, **MapFieldInfo(game_type=CollisionHitFilter))
    sound_space_type: int = 0
    cubemap_index: int = 0  # TODO: No `MSBEnvironmentEvent` in DeS... maybe this doesn't actually index in DS1 either?
    reflect_plane_height: float = 0.0
    navmesh_groups: GroupBitSet128 = None  # defaults to being the same as `display_groups`
    ref_tex_ids: list[int] = field(default_factory=lambda: [0] * 16)  # TODO: default?
    unk_x38: int = 0  # TODO: default?
    place_name_banner_id: int = field(default=-1, **MapFieldInfo(game_type=PlaceName))
    force_place_name_banner: bool = True  # necessary default because `place_name_banner_id` defaults to -1

    HIDE_FIELDS = (
        "scale",
        "use_depth_bias_float",
    )

    def __post_init__(self):
        """`navmesh_groups` default (if `None`) to same as `display_groups`."""
        if self.navmesh_groups is None:
            self.navmesh_groups = self.display_groups.copy()

    def get_force_place_name_banner(self):
        return self._force_place_name_banner

    def set_force_place_name_banner(self, value: bool):
        if not value and self.place_name_banner_id == -1:
            raise InvalidFieldValueError(
                "Banner must appear when area name is set to default (-1).\n"
                "You must specify the area name manually to set this to False."
            )
        self._force_place_name_banner = bool(value)

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
MSBCollision.force_place_name_banner = property(
    lambda self: self.get_force_place_name_banner(),
    lambda self, value: self.set_force_place_name_banner(value),
)


class ProtobossDataStruct(MSBBinaryStruct):
    unk_x00: float
    unk_x04: float
    unk_x08: float
    unk_x0c: float
    unk_x10: int
    unk_x14: int
    unk_x18: float
    unk_x1c: float
    unk_x20: int
    unk_x24: int
    unk_x28: float
    unk_x2c: int
    unk_x30: int
    _pad1: bytes = binary_pad(12)


@dataclass(slots=True, eq=False, repr=False)
class MSBProtoboss(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Protoboss
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""  # empty
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": ProtobossDataStruct}

    # Type/default overrides.
    model: MSBCharacterModel = None  # TODO: Character model? Surely.

    # TODO: Defaults?
    unk_x00: float = 0.0
    unk_x04: float = 0.0
    unk_x08: float = 0.0
    unk_x0c: float = 0.0
    unk_x10: int = 0
    unk_x14: int = 0
    unk_x18: float = 0.0
    unk_x1c: float = 0.0
    unk_x20: int = 0
    unk_x24: int = 0
    unk_x28: float = 0.0
    unk_x2c: int = 0
    unk_x30: int = 0


class NavmeshDataStruct(MSBBinaryStruct):
    navmesh_groups: GroupBitSet128 = binary_array(4, uint)
    _pad1: bytes = binary_pad(16)


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmesh(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Navmesh
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\n_layout.SIB"
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": NavmeshDataStruct}

    # Type/default overrides.
    model: MSBNavmeshModel = None

    navmesh_groups: GroupBitSet128 = field(default_factory=GroupBitSet128.all_off)  # all OFF by default

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

    # Type override:
    model: MSBDummyObjectModel = None


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyCharacter(MSBCharacter):
    """Character not loaded in normal gameplay.

    May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`.
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.DummyCharacter
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""

    # Type override:
    model: MSBDummyCharacterModel = None


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
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\DemonsSoul\\data\\Model\\map\\{map_stem}\\sib\\h_layout_connect.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]
    STRUCTS = MSBPart.STRUCTS | {"subtype_data": ConnectCollisionDataStruct}

    model: MSBCollisionModel = None
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [1, 0, 0, 0], **BinaryArray(4))

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
