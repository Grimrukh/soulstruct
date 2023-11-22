"""In Elden Ring (and possibly previous games), region subtypes are defined by actual functional usage (as though
they have built-in events) rather than just shapes.

Any given region subtype can have any given shape, which is given by an enum in the header.
"""
from __future__ import annotations

__all__ = [
    "MSBRegion",
    "MSBInvasionPointRegion",
    "MSBEnvironmentMapPointRegion",
    "MSBSoundRegion",
    "MSBVFXRegion",
    "MSBWindVFXRegion",
    "MSBSpawnPointRegion",
    "MSBMessageRegion",
    "MSBEnvironmentMapEffectBoxRegion",
    "MSBWindAreaRegion",
    "MSBConnectionRegion",
    "MSBPatrolRoute22Region",
    "MSBBuddySummonPointRegion",
    "MSBMufflingBoxRegion",
    "MSBMufflingPortalRegion",
    "MSBOtherSoundRegion",
    "MSBMufflingPlaneRegion",
    "MSBPatrolRouteRegion",
    "MSBMapPointRegion",
    "MSBWeatherOverrideRegion",
    "MSBAutoDrawGroupPointRegion",
    "MSBGroupDefeatRewardRegion",
    "MSBMapPointDiscoveryOverrideRegion",
    "MSBMapPointParticipationOverrideRegion",
    "MSBHitsetRegion",
    "MSBFastTravelRestrictionRegion",
    "MSBWeatherCreateAssetPointRegion",
    "MSBPlayAreaRegion",
    "MSBEnvironmentMapOutputRegion",
    "MSBMountJumpRegion",
    "MSBDummyRegion",
    "MSBFallPreventionRemovalRegion",
    "MSBNavmeshCuttingRegion",
    "MSBMapNameOverrideRegion",
    "MSBMountJumpFallRegion",
    "MSBHorseRideOverrideRegion",
    "MSBOtherRegion",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.regions import *
from soulstruct.eldenring.game_types import GameObjectIntSequence, Region, MapPart
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBRegionSubtype
from .region_shapes import *
from ...utilities.text import pad_chars

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb import MSBEntry
    from .parts import MSBPart

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBRegion"


@dataclass(slots=True)
class RegionHeader(BinaryStruct):
    name_offset: long
    _subtype_int: int
    _supertype_index: int
    _shape_int: int
    translate: Vector3
    rotate: Vector3  # Euler angles in radians
    region_unkh_2c: int
    unk_shorts_a_offset: long
    unk_shorts_b_offset: long
    region_unkh_40: int
    event_layer: int
    shape_data_offset: long
    supertype_data_offset: long
    subtype_data_offset: long
    extra_data_offset: long


@dataclass(slots=True)
class RegionSupertypeData(BinaryStruct):
    _attached_part_index: int
    entity_id: uint
    region_unkd_08: byte
    _pad1: bytes = field(init=False, **BinaryPad(7))


@dataclass(slots=True)
class RegionExtraData(BinaryStruct):
    map_id: int
    region_unkx_04: int
    _pad1: int = field(init=False, **BinaryPad(4))
    region_unkx_0c: int
    _pad2: int = field(init=False, **BinaryPad(16))


@dataclass(slots=True, eq=False, repr=False)
class MSBRegion(BaseMSBRegion, abc.ABC):

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[type[BinaryStruct]] = RegionHeader
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part"]
    SUPERTYPE_DATA_STRUCT: tp.ClassVar[type[BinaryStruct]] = RegionSupertypeData
    SUBTYPE_DATA_STRUCT: tp.ClassVar[type[BinaryStruct]] = None  # none by default

    shape: BaseShape = None
    region_unkh_2c: int = 0
    region_unkh_40: int = 0
    event_layer: int = -1
    unk_shorts_a: list[int] = field(default_factory=list)
    unk_shorts_b: list[int] = field(default_factory=list)
    region_unkd_08: int = 0
    map_id: int = 0
    region_unkx_04: int = 0
    region_unkx_0c: int = 0
    attached_part: MSBPart = None  # if given, region only works if this part is loaded (and drawn/enabled?)

    _attached_part_index: int = None

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Regions do not have 'supertype data'. Just a header (with some supertype data) and optional subtype data."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)

        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if cls.SUBTYPE_DATA_STRUCT is not None:
            if relative_subtype_data_offset == 0:
                raise ValueError(
                    f"Expected subtype data for `{cls.__name__}` with name '{kwargs['name']}' but found none."
                )
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)

        cls.SETATTR_CHECKS_DISABLED = True
        msb_region = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_region

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)

        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB region subtype index for `{cls.__name__}`: {header_subtype_int}")

        header_shape_int = header.pop("_shape_int")
        shape_class = SHAPE_TYPES[RegionShapeType(header_shape_int)]  # type: BaseShape
        reader.seek(entry_offset + header.pop("shape_data_offset"))
        shape = shape_class.from_msb_reader(reader)
        
        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        
        reader.seek(entry_offset + header.pop("unk_shorts_a_offset"))
        unk_shorts_a_len = reader["h"]
        unk_shorts_a = list(reader.unpack(f"{unk_shorts_a_len}h"))
        
        reader.seek(entry_offset + header.pop("unk_shorts_b_offset"))
        unk_shorts_b_len = reader["h"]
        unk_shorts_b = list(reader.unpack(f"{unk_shorts_b_len}h"))

        reader.seek(entry_offset + header.pop("supertype_data_offset"))
        supertype_data = cls.SUPERTYPE_DATA_STRUCT.from_bytes(reader)
        _attached_part_index = supertype_data.pop("_attached_part_index")
        data = supertype_data.to_dict(ignore_underscore_prefix=True)  # entity_id, region_unkd_08

        reader.seek(entry_offset + header.pop("extra_data_offset"))
        extra_data = RegionExtraData.from_bytes(reader)
        data |= extra_data.to_dict(ignore_underscore_prefix=True)  # map_id, region_unkx_04, region_unkx_0c

        return header.to_dict(ignore_underscore_prefix=True) | data | {
            "name": name,
            "_attached_part_index": _attached_part_index,
            "shape": shape,
            "unk_shorts_a": unk_shorts_a,
            "unk_shorts_b": unk_shorts_b,
        }

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "attached_part")
        self.shape.indices_to_objects(entry_lists)  # only does anything for Composite shapes

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        entry_offset = writer.position
        self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)

        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)  # can use base method (no indices to process)

        # Some subtypes pad here. The rest pad after the supertype data (above).
        if self.SUBTYPE_ENUM <= MSBRegionSubtype.BuddySummonPoint or self.SUBTYPE_ENUM == MSBRegionSubtype.OtherRegion:
            writer.pad_align(8)

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
            name_offset=RESERVED,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _supertype_index=supertype_index,
            # NOTE: No subtype index for regions.
            _shape_int=self.shape.SHAPE_TYPE.value,
            unk_shorts_a_offset=RESERVED,
            unk_shorts_b_offset=RESERVED,
            shape_data_offset=RESERVED,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
            extra_data_offset=RESERVED,
        )
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))
        
        writer.fill("unk_shorts_a_offset", writer.position - entry_offset, obj=self)
        writer.pack("h", len(self.unk_shorts_a))
        writer.pack(f"{len(self.unk_shorts_a)}h", *self.unk_shorts_a)
        writer.pad_align(4)
        
        writer.fill("unk_shorts_b_offset", writer.position - entry_offset, obj=self)
        writer.pack("h", len(self.unk_shorts_b))
        writer.pack(f"{len(self.unk_shorts_b)}h", *self.unk_shorts_b)
        writer.pad_align(8)

        shape_data_offset = writer.position - entry_offset if self.shape.DATA_STRUCT is not None else 0
        writer.fill("shape_data_offset", shape_data_offset, obj=self)
        self.shape.to_msb_writer(writer)

        writer.fill("supertype_data_offset", writer.position - entry_offset, obj=self)
        self.pack_supertype_data(writer, entry_offset, entry_lists)

        # Some subtypes pad here. The rest pad after the subtype data.
        if MSBRegionSubtype.BuddySummonPoint < self.SUBTYPE_ENUM != MSBRegionSubtype.OtherRegion:
            writer.pad_align(8)

    def pack_supertype_data(self, writer: BinaryWriter, entry_offset: int, entry_lists: dict[str, list[MSBEntry]]):
        self.SUPERTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _attached_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "attached_part"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBInvasionPointRegion(MSBRegion):
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.InvasionPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        priority: int

    priority: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapPointRegion(MSBRegion):
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: float
        unk_t04: int
        _minus_one: int = field(**Binary(asserted=-1))
        _zero: byte = field(**Binary(asserted=0))
        unk_t0d: bool
        unk_t0e: bool
        unk_t0f: bool
        unk_t10: float
        unk_t14: float
        map_id_2: int
        _pad1: bytes = field(**BinaryPad(4))
        unk_t20: int
        unk_t24: int
        unk_t28: int
        unk_t2c: byte
        unk_t2d: byte
        _pad2: bytes = field(**BinaryPad(2))

    unk_t00: float = 0.0
    unk_t04: int = 0
    unk_t0d: bool = False
    unk_t0e: bool = False
    unk_t0f: bool = False
    unk_t10: float = 0.0
    unk_t14: float = 0.0
    map_id_2: int = 0
    unk_t20: int = 0
    unk_t24: int = 0
    unk_t28: int = 0
    unk_t2c: int = 0
    unk_t2d: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBSoundRegion(MSBRegion):
    """Region where a sound can be heard.

    NOTE: Has built-in composite shape of up to 16 other regions (but as direct index references).
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Sound
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "child_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        sound_type: int
        sound_id: int
        _child_regions_indices: list[int] = field(**BinaryArray(16, int))
        _zero: byte = field(**Binary(asserted=0))
        unk_t49: bool
        _pad1: bytes = field(**BinaryPad(2))

    sound_type: int = 0
    sound_id: int = 0
    child_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 16, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 8)))
    )
    unk_t49: bool = False

    _child_regions_indices: list[int] = field(default=None, **BinaryArray(16))

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBSoundRegion, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "child_regions")


@dataclass(slots=True, eq=False, repr=False)
class MSBVFXRegion(MSBRegion):
    """Point where visual effects can play."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.VFX

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        effect_id: int
        unk_t04: int

    effect_id: int = 0
    unk_t04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBWindVFXRegion(MSBRegion):
    """Unknown. Likely to be procedural wind visual effects."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WindVFX
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "wind_area"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        effect_id: int
        _wind_area_index: int
        unk_t08: float

    effect_id: int = 0
    wind_area: MSBRegion = field(default=None, **MapFieldInfo(game_type=Region))
    unk_t08: float = 0.0

    _wind_area_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBWindVFXRegion, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "wind_area")


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnPointRegion(MSBRegion):
    """Point where the player can spawn in a map."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.SpawnPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _minus_one: int = field(**Binary(asserted=-1))
        _pad1: bytes = field(**BinaryPad(3))


@dataclass(slots=True, eq=False, repr=False)
class MSBMessageRegion(MSBRegion):
    """Point where a developer message appears."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Message

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        message_id: short
        unk_t02: short
        hidden: bool = field(**Binary("i"))  # 32-bit bool
        unk_t08: int
        unk_t0c: int
        enable_event_flag_id: uint
        character_model_name: int
        character_id: int
        animation_id: int
        player_id: int

    message_id: int = 0
    unk_t02: int = 0
    hidden: bool = False
    unk_t08: int = 0
    unk_t0c: int = 0
    enable_event_flag_id: int = 0
    character_model_name: int = 0
    # TODO: param reference types
    character_id: int = 0
    animation_id: int = 0
    player_id: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapEffectBoxRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapEffectBox

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        enable_dist: float
        transition_dist: float
        unk_t08: byte
        unk_t09: byte
        unk_t0a: short
        _pad1: bytes = field(**BinaryPad(0x18))
        unk_t24: float
        unk_t28: float
        unk_t2c: short
        unk_t2e: bool
        unk_t2f: bool
        unk_t30: short
        _pad2: bytes = field(**BinaryPad(1))
        unk_t33: bool
        unk_t34: short
        unk_t36: short
        _pad3: bytes = field(**BinaryPad(4))

    enable_dist: float = 0.0
    transition_dist: float = 0.0
    unk_t08: int = 0
    unk_t09: int = 0
    unk_t0a: int = 0
    unk_t24: float = 0.0
    unk_t28: float = 0.0
    unk_t2c: int = 0
    unk_t2e: bool = False
    unk_t2f: bool = False
    unk_t30: int = 0
    unk_t33: bool = False
    unk_t34: int = 0
    unk_t36: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBWindAreaRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WindArea

    # No subtype data.


@dataclass(slots=True, eq=False, repr=False)
class MSBConnectionRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Connection

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        target_map_id: list[sbyte] = field(**BinaryArray(4))
        _pad1: bytes = field(**BinaryPad(12))

    # TODO: Map reference.
    target_map_id: list[int] = field(default_factory=lambda: [0, 0, 0, 0])


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRoute22Region(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PatrolRoute22

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _minus_one: int = field(**Binary(asserted=-1))
        _zero: int = field(**Binary(asserted=0))


@dataclass(slots=True, eq=False, repr=False)
class MSBBuddySummonPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.BuddySummonPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _pad1: bytes = field(**BinaryPad(16))


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingBoxRegion(MSBRegion):
    """Region in which a sound is muffled."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MufflingBox

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        _pad1: bytes = field(**BinaryPad(20))
        _unk: int = field(**Binary(asserted=32))
        _pad2: bytes = field(**BinaryPad(8))
        unk_t24: float
        _pad3: bytes = field(**BinaryPad(12))
        unk_t34: float
        _pad4: bytes = field(**BinaryPad(4))
        unk_t3c: float
        unk_t40: float
        unk_t44: float

    unk_t00: int = 0
    unk_t24: float = 0.0
    unk_t34: float = 0.0
    unk_t3c: float = 0.0
    unk_t40: float = 0.0
    unk_t44: float = 0.0


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingPortalRegion(MSBRegion):
    """Entrances to muffling box regions."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MufflingPortal

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        _pad1: bytes = field(**BinaryPad(20))
        _unk: int = field(**Binary(asserted=32))
        _pad2: bytes = field(**BinaryPad(24))
        _minus_one: int = field(**Binary(asserted=-1))

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherSoundRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.OtherSound

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: byte
        unk_t01: byte
        unk_t02: byte
        unk_t03: byte
        unk_t04: int
        unk_t08: short
        unk_t0a: short
        unk_t0c: byte
        _pad1: bytes = field(**BinaryPad(19))

    unk_t00: int = 0
    unk_t01: int = 0
    unk_t02: int = 0
    unk_t03: int = 0
    unk_t04: int = 0
    unk_t08: int = 0
    unk_t0a: int = 0
    unk_t0c: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingPlaneRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MufflingPlane

    # No subtype data.


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRouteRegion(MSBRegion):
    """Point that is part of a character's patrol path."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PatrolRoute

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        unk_t04: int
        unk_t08: float
        unk_t0c: float
        _minus_one: int = field(**Binary(asserted=-1))
        unk_t14: float
        unk_t18: float
        _zero: int = field(**Binary(asserted=0))

    unk_t00: int = 0
    unk_t04: int = 0
    unk_t08: float = 0.0
    unk_t0c: float = 0.0
    unk_t14: float = 0.0
    unk_t18: float = 0.0


@dataclass(slots=True, eq=False, repr=False)
class MSBWeatherOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WeatherOverride

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        weather_lot_id: int
        _minus_one: int = field(**Binary(asserted=-1))
        _pad1: bytes = field(**BinaryPad(24))

    weather_lot_id: int = 0  # TODO: param ref


@dataclass(slots=True, eq=False, repr=False)
class MSBAutoDrawGroupPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.AutoDrawGroupPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        _pad1: bytes = field(**BinaryPad(28))

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBGroupDefeatRewardRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.GroupDefeatReward
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "parts"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        unk_t04: int
        unk_t08: int
        _minus_ones_0: int = field(**BinaryPad(8, b"\xFF"))
        _parts_indices: list[int] = field(**BinaryArray(8))
        unk_t34: int
        unk_t38: int
        _minus_ones_1: int = field(**BinaryPad(24, b"\xFF"))
        unk_t54: int
        _pad1: int = field(**BinaryPad(8))

    unk_t00: int = 0
    unk_t04: int = 0
    unk_t08: int = 0
    # TODO: Surely these are always Characters (accessed via part supertype index)?
    parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 16, **MapFieldInfo(game_type=GameObjectIntSequence((MapPart, 8)))
    )
    unk_t34: int = 0
    unk_t38: int = 0
    unk_t54: int = 0

    _parts_indices: list[int] = field(default=None, **BinaryArray(8))

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBGroupDefeatRewardRegion, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "parts")


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointDiscoveryOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPointDiscoveryOverride

    # No subtype data.


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointParticipationOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPointParticipationOverride

    # No subtype data.


@dataclass(slots=True, eq=False, repr=False)
class MSBHitsetRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Hitset

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBFastTravelRestrictionRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.FastTravelRestriction

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        event_flag_id: uint
        _zero: int = field(**Binary(asserted=0))

    event_flag_id: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBWeatherCreateAssetPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WeatherCreateAssetPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _zero: int = field(**Binary(asserted=0))


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayAreaRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PlayArea

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        unk_t04: int

    unk_t00: int = 0
    unk_t04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapOutputRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapOutput

    # No subtype data.


@dataclass(slots=True, eq=False, repr=False)
class MSBMountJumpRegion(MSBRegion):
    """Unknown. TODO: Wellspring, surely?"""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MountJump

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        jump_height: float
        unk_t04: int

    jump_height: float = 0.0
    unk_t04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Dummy

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int
        _zero: int = field(**Binary(asserted=0))

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBFallPreventionRemovalRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.FallPreventionRemoval

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _pad1: bytes = field(**BinaryPad(8))


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmeshCuttingRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.NavmeshCutting

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _pad1: bytes = field(**BinaryPad(8))


@dataclass(slots=True, eq=False, repr=False)
class MSBMapNameOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapNameOverride

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_t00: int  # TODO: surely a text ID for desired map name?
        _zero: int = field(**Binary(asserted=0))

    unk_t00: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBMountJumpFallRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MountJumpFall

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        """No actual data."""
        _minus_one: int = field(**Binary(asserted=-1))
        _zero: int = field(**Binary(asserted=0))


@dataclass(slots=True, eq=False, repr=False)
class MSBHorseRideOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.HorseRideOverride

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        override_type: int  # TODO: 1 is Prevent, 2 is Allow
        _zero: int = field(**Binary(asserted=0))

    override_type: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherRegion(MSBRegion):
    """Unknown. Probably holds unused regions."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.OtherRegion

    # No subtype data.
