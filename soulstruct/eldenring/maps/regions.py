"""In Elden Ring (and possibly previous games), region subtypes are defined by actual functional usage (as though
they have built-in events) rather than just shapes.
"""
from __future__ import annotations

__all__ = [
    "RegionShapeType",
    "RegionShape",
    "PointShape",
    "CircleShape",
    "SphereShape",
    "CylinderShape",
    "RectShape",
    "BoxShape",
    "CompositeShape",

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

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.regions import *
from soulstruct.base.maps.msb.region_shapes import *
from soulstruct.eldenring.game_types import GameObjectIntSequence, Region, MapPart
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBRegionSubtype

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb import MSBEntry
    from soulstruct.utilities.misc import IDList
    from .parts import MSBPart


class RegionHeaderStruct(MSBHeaderStruct):
    name_offset: long
    _subtype_int: int
    subtype_index: int
    shape_type_int: int
    translate: Vector3
    rotate: Vector3  # Euler angles in radians
    supertype_index: int
    unk_shorts_a_offset: long
    unk_shorts_b_offset: long
    region_unkh_40: int
    event_layer: int
    shape_data_offset: long
    supertype_data_offset: long
    subtype_data_offset: long
    extra_data_offset: long

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBRegion],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(RegionHeaderStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)

        reader.seek(entry_offset + kwargs.pop("unk_shorts_a_offset"))
        unk_shorts_a_len = reader["h"]
        kwargs["unk_shorts_a"] = list(reader.unpack(f"{unk_shorts_a_len}h"))

        reader.seek(entry_offset + kwargs.pop("unk_shorts_b_offset"))
        unk_shorts_b_len = reader["h"]
        kwargs["unk_shorts_b"] = list(reader.unpack(f"{unk_shorts_b_len}h"))

        # TODO: Should treat as an initial struct?
        reader.seek(entry_offset + kwargs.pop("extra_data_offset"))
        extra_data = RegionExtraData.from_bytes(reader)
        kwargs |= extra_data.to_dict(ignore_underscore_prefix=True)  # map_id, region_unkx_04, region_unkx_0c

        # Read shape struct.
        shape_type_int = kwargs.pop("shape_type_int")
        try:
            shape_class = entry_type.SHAPE_CLASSES[shape_type_int]  # type: type[RegionShape]
        except KeyError:
            if shape_type_int == 6:
                raise ValueError("Composite Region shape type (6) is not supported in older games.")
            raise ValueError(f"Invalid MSB region shape type value: {shape_type_int}")
        reader.seek(entry_offset + kwargs.pop("shape_data_offset"))
        kwargs["shape"] = shape_class.from_msb_reader(reader)

        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBRegion,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(RegionHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs["shape_type_int"] = entry.shape_type_int
        kwargs["unk_shorts_a_offset"] = RESERVED
        kwargs["unk_shorts_b_offset"] = RESERVED
        kwargs["shape_data_offset"] = RESERVED
        kwargs["supertype_data_offset"] = RESERVED
        kwargs["subtype_data_offset"] = RESERVED
        kwargs["extra_data_offset"] = RESERVED

    @classmethod
    def post_write(
        cls,
        entry: MSBRegion,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        super(RegionHeaderStruct, cls).post_write(entry, writer, entry_offset, entry_lists)
        writer.fill("unk_shorts_a_offset", writer.position - entry_offset, obj=entry)
        writer.pack("h", len(entry.unk_shorts_a))
        writer.pack(f"{len(entry.unk_shorts_a)}h", *entry.unk_shorts_a)
        writer.pad_align(4)

        writer.fill("unk_shorts_b_offset", writer.position - entry_offset, obj=entry)
        writer.pack("h", len(entry.unk_shorts_b))
        writer.pack(f"{len(entry.unk_shorts_b)}h", *entry.unk_shorts_b)
        writer.pad_align(8)

        if isinstance(entry.shape, CompositeShape):
            entry.shape.regions_to_indices(entry_lists, owner_region_name=entry.name)
        shape_offset = writer.position - entry_offset
        writer.fill("shape_data_offset", shape_offset, obj=entry)
        entry.shape.to_msb_writer(writer)


class RegionSupertypeDataStruct(MSBBinaryStruct):
    _attached_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    entity_id: uint
    region_unkd_08: byte
    _pad1: bytes = binary_pad(7, init=False)


class RegionExtraData(MSBBinaryStruct):
    map_id: int
    region_unkx_04: int
    _pad1: int = binary_pad(4, init=False)
    region_unkx_0c: int
    _pad2: int = binary_pad(16, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBRegion(BaseMSBRegion, abc.ABC):

    HEADER_STRUCT = RegionHeaderStruct
    MSB_ENTRY_REFERENCES = ["attached_part"]
    STRUCTS = {
        "supertype_data": RegionSupertypeDataStruct,
        "subtype_data": None,  # no subtype data by default
    }

    NAME_ENCODING = "utf-16-le"

    # Composite shape type added.
    SHAPE_CLASSES: tp.ClassVar[dict[int, type[RegionShape]]] = BaseMSBRegion.SHAPE_CLASSES | {
        6: CompositeShape
    }

    # HEADER DATA
    region_unkh_40: int = 0
    event_layer: int = -1
    unk_shorts_a: list[int] = field(default_factory=list)
    unk_shorts_b: list[int] = field(default_factory=list)

    # REGION DATA
    attached_part: MSBPart = None  # if given, region only works if this part is loaded (and drawn/enabled?)
    region_unkd_08: int = 0
    # `entity_id` already on parent.

    # EXTRA DATA
    map_id: int = 0
    region_unkx_04: int = 0
    region_unkx_0c: int = 0

    _attached_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "attached_part")
        if isinstance(self.shape, CompositeShape):
            self.shape.indices_to_regions(entry_lists, owner_region_name=self.name)

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, IDList[MSBEntry]]
    ):
        """More complicated between-struct padding."""
        entry_offset = writer.position
        self.HEADER_STRUCT.kwargs_to_msb_writer(
            self,
            writer,
            entry_offset,
            entry_lists,
            supertype_index=supertype_index,
            subtype_index=subtype_index,
        )

        aligned = False
        for struct_name, struct_type in self.STRUCTS.items():
            struct_offset = writer.position - entry_offset
            writer.fill(f"{struct_name}_offset", struct_offset, obj=self)
            struct_type.kwargs_to_msb_writer(
                self,
                writer,
                entry_offset,
                entry_lists,
                supertype_index=supertype_index,
                subtype_index=subtype_index,
            )

            if struct_name == "supertype_data" and MSBRegionSubtype.MufflingBox <= self.SUBTYPE_ENUM:
                # Some subtypes align here. The rest align after the remaining structs.
                writer.pad_align(8)
                aligned = True

        if not aligned:
            writer.pad_align(8)


class InvasionPointRegionDataStruct(MSBBinaryStruct):
    priority: int


@dataclass(slots=True, eq=False, repr=False)
class MSBInvasionPointRegion(MSBRegion):
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.InvasionPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": InvasionPointRegionDataStruct,
    }

    priority: int = 0


class EnvironmentMapPointRegionDataStruct(MSBBinaryStruct):
    unk_t00: float
    unk_t04: int
    _minus_one: int = binary(asserted=-1)
    _zero: byte = binary(asserted=0)
    unk_t0d: bool
    unk_t0e: bool
    unk_t0f: bool
    unk_t10: float
    unk_t14: float
    map_id_2: int
    _pad1: bytes = binary_pad(4)
    unk_t20: int
    unk_t24: int
    unk_t28: int
    unk_t2c: byte
    unk_t2d: byte
    _pad2: bytes = binary_pad(2)


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapPointRegion(MSBRegion):
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": EnvironmentMapPointRegionDataStruct,
    }

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


class SoundRegionDataStruct(MSBBinaryStruct):
    sound_type: int
    sound_id: int
    _child_regions_indices: list[int] = binary_array(16, int)
    _zero: byte = binary(asserted=0)
    unk_t49: bool
    _pad1: bytes = binary_pad(2)


@dataclass(slots=True, eq=False, repr=False)
class MSBSoundRegion(MSBRegion):
    """Region where a sound can be heard.

    NOTE: Has built-in composite shape of up to 16 other regions (but as direct index references).
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Sound
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "child_regions"]
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": SoundRegionDataStruct,
    }
    sound_type: int = 0
    sound_id: int = 0
    child_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 16, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 16)))
    )
    unk_t49: bool = False

    _child_regions_indices: list[int] = binary_array(16, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSoundRegion, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "child_regions")


class VFXRegionDataStruct(MSBBinaryStruct):
    effect_id: int
    unk_t04: int


@dataclass(slots=True, eq=False, repr=False)
class MSBVFXRegion(MSBRegion):
    """Point where visual effects can play."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.VFX
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": VFXRegionDataStruct,
    }

    effect_id: int = 0
    unk_t04: int = 0


class WindVFXRegionDataStruct(MSBBinaryStruct):
    effect_id: int
    _wind_area_index: int = field(**EntryRef("POINT_PARAM_ST"))
    unk_t08: float


@dataclass(slots=True, eq=False, repr=False)
class MSBWindVFXRegion(MSBRegion):
    """Unknown. Likely to be procedural wind visual effects."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WindVFX
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "wind_area"]
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": WindVFXRegionDataStruct,
    }
    effect_id: int = 0
    wind_area: MSBRegion = field(default=None, **MapFieldInfo(game_type=Region))
    unk_t08: float = 0.0

    _wind_area_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBWindVFXRegion, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "wind_area")


class SpawnPointRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _minus_one: int = binary(asserted=-1)
    _pad1: bytes = binary_pad(3)


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnPointRegion(MSBRegion):
    """Point where the player can spawn in a map."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.SpawnPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": SpawnPointRegionDataStruct,
    }


class MessageRegionDataStruct(MSBBinaryStruct):
    message_id: short
    unk_t02: short
    hidden: bool = binary(int)  # 32-bit bool
    unk_t08: int
    unk_t0c: int
    enable_event_flag_id: uint
    character_model_name: int
    character_id: int
    animation_id: int
    player_id: int


@dataclass(slots=True, eq=False, repr=False)
class MSBMessageRegion(MSBRegion):
    """Point where a developer message appears."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Message
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MessageRegionDataStruct,
    }
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


class EnvironmentMapEffectBoxRegionDataStruct(MSBBinaryStruct):
    enable_dist: float
    transition_dist: float
    unk_t08: byte
    unk_t09: byte
    unk_t0a: short
    _pad1: bytes = binary_pad(0x18, init=False)
    unk_t24: float
    unk_t28: float
    unk_t2c: short
    unk_t2e: bool
    unk_t2f: bool
    unk_t30: short
    _pad2: bytes = binary_pad(1)
    unk_t33: bool
    unk_t34: short
    unk_t36: short
    _pad3: bytes = binary_pad(4)


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapEffectBoxRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapEffectBox
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": EnvironmentMapEffectBoxRegionDataStruct,
    }

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


class ConnectionRegionDataStruct(MSBBinaryStruct):
    target_map_id: list[sbyte] = binary_array(4)
    _pad1: bytes = binary_pad(12)


@dataclass(slots=True, eq=False, repr=False)
class MSBConnectionRegion(MSBRegion):
    """Unknown. New ConnectCollision?"""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Connection
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": ConnectionRegionDataStruct,
    }

    # TODO: Map reference.
    target_map_id: list[int] = field(default_factory=lambda: [0, 0, 0, 0])


class PatrolRoute22RegionSUBTYPE_DataStruct(MSBBinaryStruct):
    """No actual data."""
    _minus_one: int = binary(asserted=-1)
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRoute22Region(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PatrolRoute22
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": PatrolRoute22RegionSUBTYPE_DataStruct,
    }


class BuddySummonPointRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _pad1: bytes = binary_pad(16)


@dataclass(slots=True, eq=False, repr=False)
class MSBBuddySummonPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.BuddySummonPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": BuddySummonPointRegionDataStruct,
    }


class MufflingBoxRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    _pad1: bytes = binary_pad(20)
    _unk: int = binary(asserted=32)
    _pad2: bytes = binary_pad(8)
    unk_t24: float
    _pad3: bytes = binary_pad(12)
    unk_t34: float
    _pad4: bytes = binary_pad(4)
    unk_t3c: float
    unk_t40: float
    unk_t44: float


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingBoxRegion(MSBRegion):
    """Region in which a sound is muffled."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MufflingBox
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MufflingBoxRegionDataStruct,
    }

    unk_t00: int = 0
    unk_t24: float = 0.0
    unk_t34: float = 0.0
    unk_t3c: float = 0.0
    unk_t40: float = 0.0
    unk_t44: float = 0.0


class MufflingPortalRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    _pad1: bytes = binary_pad(20)
    _unk: int = binary(asserted=32)
    _pad2: bytes = binary_pad(24)
    _minus_one: int = binary(asserted=-1)


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingPortalRegion(MSBRegion):
    """Entrances to muffling box regions."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MufflingPortal
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MufflingPortalRegionDataStruct,
    }

    unk_t00: int = 0


class OtherSoundRegionDataStruct(MSBBinaryStruct):
    unk_t00: byte
    unk_t01: byte
    unk_t02: byte
    unk_t03: byte
    unk_t04: int
    unk_t08: short
    unk_t0a: short
    unk_t0c: byte
    _pad1: bytes = binary_pad(19)


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherSoundRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.OtherSound
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": OtherSoundRegionDataStruct,
    }
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


class PatrolRouteRegionDataStruct(MSBBinaryStruct):
    unk_t00: int


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRouteRegion(MSBRegion):
    """Point that is part of a character's patrol path."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PatrolRoute
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": PatrolRouteRegionDataStruct,
    }
    unk_t00: int = 0


class MapPointRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    unk_t04: int
    unk_t08: float
    unk_t0c: float
    _minus_one: int = binary(asserted=-1)
    unk_t14: float
    unk_t18: float
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MapPointRegionDataStruct,
    }

    unk_t00: int = 0
    unk_t04: int = 0
    unk_t08: float = 0.0
    unk_t0c: float = 0.0
    unk_t14: float = 0.0
    unk_t18: float = 0.0


class WeatherOverrideRegionDataStruct(MSBBinaryStruct):
    weather_lot_id: int
    _minus_one: int = binary(asserted=-1)
    _pad1: bytes = binary_pad(24)


@dataclass(slots=True, eq=False, repr=False)
class MSBWeatherOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WeatherOverride
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": WeatherOverrideRegionDataStruct,
    }

    weather_lot_id: int = 0  # TODO: param ref


class AutoDrawGroupPointRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    _pad1: bytes = binary_pad(28)


@dataclass(slots=True, eq=False, repr=False)
class MSBAutoDrawGroupPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.AutoDrawGroupPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": AutoDrawGroupPointRegionDataStruct,
    }
    unk_t00: int = 0


class GroupDefeatRewardRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    unk_t04: int
    unk_t08: int
    _minus_ones_0: int = binary_pad(8, b"\xFF", init=False)
    _parts_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=8))
    unk_t34: int
    unk_t38: int
    _minus_ones_1: int = binary_pad(24, b"\xFF", init=False)
    unk_t54: int
    _pad1: int = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBGroupDefeatRewardRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.GroupDefeatReward
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "parts"]
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": GroupDefeatRewardRegionDataStruct,
    }

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

    _parts_indices: list[int] = binary_array(8, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBGroupDefeatRewardRegion, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "parts")


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointDiscoveryOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPointDiscoveryOverride


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPointParticipationOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapPointParticipationOverride


class HitsetRegionDataStruct(MSBBinaryStruct):
    unk_t00: int


@dataclass(slots=True, eq=False, repr=False)
class MSBHitsetRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Hitset
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": HitsetRegionDataStruct,
    }

    unk_t00: int = 0


class FastTravelRestrictionRegionDataStruct(MSBBinaryStruct):
    event_flag_id: uint
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBFastTravelRestrictionRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.FastTravelRestriction
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": FastTravelRestrictionRegionDataStruct,
    }

    event_flag_id: int = 0


class WeatherCreateAssetPointRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBWeatherCreateAssetPointRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.WeatherCreateAssetPoint
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": WeatherCreateAssetPointRegionDataStruct,
    }


class PlayAreaRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    unk_t04: int


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayAreaRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.PlayArea
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": PlayAreaRegionDataStruct,
    }

    unk_t00: int = 0
    unk_t04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentMapOutputRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.EnvironmentMapOutput


class MountJumpRegionDataStruct(MSBBinaryStruct):
    jump_height: float
    unk_t04: int


@dataclass(slots=True, eq=False, repr=False)
class MSBMountJumpRegion(MSBRegion):
    """Unknown. TODO: Wellspring, surely?"""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MountJump
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MountJumpRegionDataStruct,
    }

    jump_height: float = 0.0
    unk_t04: int = 0


class DummyRegionDataStruct(MSBBinaryStruct):
    unk_t00: int
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBDummyRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.Dummy
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": DummyRegionDataStruct,
    }

    unk_t00: int = 0


class FallPreventionRemovalRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _pad1: bytes = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBFallPreventionRemovalRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.FallPreventionRemoval
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": FallPreventionRemovalRegionDataStruct,
    }


class NavmeshCuttingRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _pad1: bytes = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmeshCuttingRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.NavmeshCutting
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": NavmeshCuttingRegionDataStruct,
    }


class MapNameOverrideRegionDataStruct(MSBBinaryStruct):
    unk_t00: int  # TODO: surely a text ID for desired map name?
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBMapNameOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MapNameOverride
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MapNameOverrideRegionDataStruct,
    }

    unk_t00: int = 0


class MountJumpFallRegionDataStruct(MSBBinaryStruct):
    """No actual data."""
    _minus_one: int = binary(asserted=-1)
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBMountJumpFallRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.MountJumpFall
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": MountJumpFallRegionDataStruct,
    }


class HorseRideOverrideRegionDataStruct(MSBBinaryStruct):
    override_type: int  # TODO: 1 is Prevent, 2 is Allow
    _zero: int = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBHorseRideOverrideRegion(MSBRegion):
    """Unknown."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.HorseRideOverride
    STRUCTS = MSBRegion.STRUCTS | {
        "subtype_data": HorseRideOverrideRegionDataStruct,
    }

    override_type: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherRegion(MSBRegion):
    """Unknown. Probably holds unused regions."""
    SUBTYPE_ENUM: tp.ClassVar[MSBRegionSubtype] = MSBRegionSubtype.OtherRegion
