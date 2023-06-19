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
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb import MSBEntry
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

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBPart"

if tp.TYPE_CHECKING:
    from .events import MSBEnvironmentEvent


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart, abc.ABC):

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        # No description offset.
        name_offset: int
        # No instance index.
        _subtype_int: int
        _subtype_index: int
        model_index: int
        sib_path_offset: int
        translate: Vector3
        rotate: Vector3
        scale: Vector3
        draw_groups: GroupBitSet128 = field(**BinaryArray(4, uint))
        display_groups: GroupBitSet128 = field(**BinaryArray(4, uint))
        # No backread groups.
        supertype_data_offset: int
        subtype_data_offset: int
        # No Gparam or SceneGparam structs.
        _pad1: bytes = field(**BinaryPad(4))

    @dataclass(slots=True)
    class SUPERTYPE_DATA_STRUCT(BinaryStruct):
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
        _pad1: bytes = field(**BinaryPad(1))
        is_shadow_source: bool
        is_shadow_destination: bool
        is_shadow_only: bool
        draw_by_reflect_cam: bool
        draw_only_reflect_cam: bool
        use_depth_bias_float: bool
        disable_point_light_effect: bool
        _pad2: bytes = field(**BinaryPad(2))

    NAME_ENCODING: tp.ClassVar[str] = "shift-jis"  # NOT `shift_jis_2004` (backslashes in SIB paths)
    GROUP_BIT_COUNT: tp.ClassVar[int] = 128  # 4 ints

    # NOTE: `model` type overridden by subclasses.
    # Subclasses may also use more appropriate defaults for convenience, as these Part supertype fields in DS1 are
    # really sporadic in which Part subtypes actually use each of them.
    sib_path: str = ""
    draw_groups: GroupBitSet128 = field(default_factory=set)
    display_groups: GroupBitSet128 = field(default_factory=set)
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

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")

        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        sib_path = reader.unpack_string(offset=entry_offset + header.pop("sib_path_offset"), encoding=cls.NAME_ENCODING)
        kwargs = dict(
            name=name,
            description="",  # no packed description in DS1 (but user/JSON descriptions are still supported)
            sib_path=sib_path,
            _model_index=header.pop("model_index"),
        )
        return header.to_dict(ignore_underscore_prefix=True) | kwargs

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
            name_offset=RESERVED,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            model_index=self.try_index(entry_lists["MODEL_PARAM_ST"], "model"),
            sib_path_offset=RESERVED,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
        )
        strings_position = writer.position - entry_offset
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        packed_name = self.name.encode(self.NAME_ENCODING) + b"\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=self)
        packed_sib_path = (self.sib_path.encode(self.NAME_ENCODING) + b"\0") if self.sib_path else b"\0"
        writer.append(packed_sib_path)
        writer.pad_align(4)
        # Minimum combined length of name and SIB path is 20 bytes, so pad if necessary.
        if writer.position - strings_position < 20:
            writer.pad(0x14 - (writer.position - strings_position))


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPiece(MSBPart):
    """Just a textured, visible mesh asset. Does not include any collision."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapPiece
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\layout.SIB"

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(**BinaryPad(8))

    model: MSBMapPieceModel = None

    HIDE_FIELDS = (
        "scale",
        "display_groups",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        "is_shadow_source",
        "is_shadow_only",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )


@dataclass(slots=True, eq=False, repr=False)
class MSBObject(MSBPart):
    """Instance of a physical object."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Object
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\o_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(4))
        _draw_parent_index: int
        break_term: sbyte
        net_sync_type: sbyte
        _pad2: bytes = field(init=False, **BinaryPad(2))
        default_animation: short
        unk_x0e_x10: short
        unk_x10_x14: int
        _pad3: bytes = field(init=False, **BinaryPad(4))

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
        "unk_x0e_x10",
        "unk_x10_x14",
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
    unk_x0e_x10: int = 0
    unk_x10_x14: int = 0

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
class MSBCharacter(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""  # empty
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(8))
        ai_id: int
        character_id: int
        talk_id: int
        patrol_type: byte
        _pad2: bytes = field(init=False, **BinaryPad(1))
        platoon_id: ushort
        player_id: int
        _draw_parent_index: int
        _pad3: bytes = field(init=False, **BinaryPad(8))
        _patrol_regions_indices: list[short] = field(**BinaryArray(8))
        default_animation: int
        damage_animation: int

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
    patrol_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 8)))
    )
    default_animation: int = -1
    damage_animation: int = -1

    _draw_parent_index: int = None
    _patrol_regions_indices: list[int] = field(default=None, **BinaryArray(8))

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
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(16))

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


# noinspection PyRedeclaration
@dataclass(slots=True, eq=False, repr=False)
class MSBCollision(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\h_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "environment_event"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        hit_filter_id: byte
        sound_space_type: byte
        _environment_event_index: short
        reflect_plane_height: float
        navmesh_groups: GroupBitSet128 = field(**BinaryArray(4, uint))
        vagrant_entity_ids: list[int] = field(**BinaryArray(3))
        _place_name_banner_id: short  # -1 means use map area/block, and any negative value means banner is forced
        starts_disabled: bool
        unk_x27_x28: byte
        attached_bonfire: int
        _minus_ones: list[int] = field(**BinaryArray(3, asserted=[-1, -1, -1]))  # never used
        _play_region_id: int  # -10 or greater is real play region ID, less than -10 is a negated stable footing flag
        camera_1_id: short
        camera_2_id: short
        _pad1: bytes = field(**BinaryPad(16))

    # Internally managed. (It's important that these come before their wrapper fields!)
    _force_place_name_banner: bool = field(default=True, repr=False)
    _play_region_id: int = field(default=0, repr=False)
    _stable_footing_flag: int = field(default=0, repr=False)

    # Field type overrides.
    model: MSBCollisionModel = None
    display_groups: GroupBitSet128 = field(default_factory=GroupBitSet128.all_on)  # all ON by default
    is_shadow_source: bool = True
    is_shadow_destination: bool = True
    draw_by_reflect_cam: bool = True

    hit_filter_id: int = field(default=CollisionHitFilter.Normal.value, **MapFieldInfo(game_type=CollisionHitFilter))
    sound_space_type: int = 0
    environment_event: MSBEnvironmentEvent = None  # NOTE: imported under TYPE_CHECKING to avoid circular import
    reflect_plane_height: float = 0.0
    navmesh_groups: GroupBitSet128 = None  # defaults to being the same as `display_groups`
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

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        data = cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        # Negative area name means that banner will appear (-1 means get area name from map area/block).
        internal_place_name_banner_id = data.pop("_place_name_banner_id")
        if internal_place_name_banner_id != -1:
            data["place_name_banner_id"] = abs(internal_place_name_banner_id)
        data["force_place_name_banner"] = internal_place_name_banner_id < 0

        # Play Region ID that is -10 or less is a stable footing flag (negated with 10 subtracted from it).
        internal_play_region_id = data.pop("_play_region_id")
        if internal_play_region_id > -10:
            data["play_region_id"] = internal_play_region_id
            data["stable_footing_flag"] = 0
        else:
            data["play_region_id"] = 0
            data["stable_footing_flag"] = -internal_play_region_id - 10

        return data

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):

        # Determine internal banner ID (negative if forced).
        if self.place_name_banner_id == -1 and not self._force_place_name_banner:
            raise InvalidFieldValueError(
                "`force_place_name_banner` must be enabled if `place_name_banner_id == -1` (default)."
            )
        place_name_sign = -1 if self.place_name_banner_id >= 0 and self._force_place_name_banner else 1
        internal_place_name_banner_id = self.place_name_banner_id * place_name_sign

        # Resolve play region ID or stable footing flag.
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


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmesh(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Navmesh
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\n_layout.SIB"

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        navmesh_groups: GroupBitSet128 = field(**BinaryArray(4, uint))
        _pad1: bytes = field(**BinaryPad(16))

    # Type/default overrides.
    model: MSBNavmeshModel = None
    is_shadow_source: bool = True

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
class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedObject
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""  # no SIB path, unlike real objects


@dataclass(slots=True, eq=False, repr=False)
class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedCharacter
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""


@dataclass(slots=True, eq=False, repr=False)
class MSBMapConnection(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapConnection
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _collision_index: int
        connected_map_id: list[sbyte] = field(**BinaryArray(4))
        _pad1: bytes = field(**BinaryPad(8))

    model: MSBCollisionModel = None
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [10, 0, 0, 0], **BinaryArray(4))

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
