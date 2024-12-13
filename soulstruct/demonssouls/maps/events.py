from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBLightEvent",
    "MSBSoundEvent",
    "MSBVFXEvent",
    "MSBWindEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBMessageEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.demonssouls.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBEventSubtype
from .regions import MSBRegion
from .parts import MSBPart

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


class EventHeaderStruct(MSBHeaderStruct):
    name_offset: int
    supertype_index: int
    _subtype_int: int
    subtype_index: int
    supertype_data_offset: int
    subtype_data_offset: int
    _pad1: bytes = binary_pad(8)  # extra 4 bytes compared to DS1


class EventDataStruct(MSBBinaryStruct):
    _attached_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _attached_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    entity_id: int
    _pad1: bytes = binary_pad(4)  # always zero, unlike `unknowns` bytes in DS1


@dataclass(slots=True, eq=False, repr=False)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Dark Souls 1."""

    HEADER_STRUCT = EventHeaderStruct
    STRUCTS = {"supertype_data": EventDataStruct}

    NAME_ENCODING = "shift-jis"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None


class LightEventDataStruct(MSBBinaryStruct):
    point_light_id: int
    unk_x04: int


@dataclass(slots=True, eq=False, repr=False)
class MSBLightEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Light
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": LightEventDataStruct}

    point_light_id: int = field(default=0, **MapFieldInfo(game_type=PointLightParam))
    unk_x04: int = 0


class SoundEventDataStruct(MSBBinaryStruct):
    unk_x00: int
    sound_type: int
    sound_id: int


@dataclass(slots=True, eq=False, repr=False)
class MSBSoundEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Sound
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": SoundEventDataStruct}

    unk_x00: int = 0
    sound_type: int = field(default=SoundType.m_Music.value, **MapFieldInfo(game_type=SoundType))
    sound_id: int = -1


class VFXEventDataStruct(MSBBinaryStruct):
    unk_x00: int
    vfx_id: int


@dataclass(slots=True, eq=False, repr=False)
class MSBVFXEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.VFX
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": VFXEventDataStruct}

    unk_x00: int = 0
    vfx_id: int = 0


class WindEventDataStruct(MSBBinaryStruct):
    wind_vector_min: Vector3
    unk_x0c: float
    wind_vector_max: Vector3
    unk_x1c: float
    wind_swing_cycles: list[float] = binary_array(4)
    wind_swing_powers: list[float] = binary_array(4)


@dataclass(slots=True, eq=False, repr=False)
class MSBWindEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Wind
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": WindEventDataStruct}

    wind_vector_min: Vector3 = field(default_factory=Vector3.zero)
    unk_x0c: float = 0.0
    wind_vector_max: Vector3 = field(default_factory=Vector3.zero)
    unk_x1c: float = 0.0
    wind_swing_cycles: list[float] = field(default_factory=lambda: [0.0] * 4, **BinaryArray(4))
    wind_swing_powers: list[float] = field(default_factory=lambda: [0.0] * 4, **BinaryArray(4))


class TreasureEventDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(4)
    _treasure_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    item_lot_1: int
    _minus_one_1: int = binary(asserted=-1)
    item_lot_2: int
    _minus_one_2: int = binary(asserted=-1)
    item_lot_3: int
    _minus_one_3: int = binary(asserted=-1)
    item_lot_4: int
    _minus_one_4: int = binary(asserted=-1)
    item_lot_5: int
    _minus_one_5: int = binary(asserted=-1)
    # No extra bools, unlike DS1.


@dataclass(slots=True, eq=False, repr=False)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "treasure_part"]
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": TreasureEventDataStruct}

    treasure_part: MSBPart = None
    item_lot_1: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_2: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_3: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_4: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_5: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))

    _treasure_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "treasure_part")


class SpawnerEventDataStruct(MSBBinaryStruct):
    max_count: byte
    spawner_type: sbyte
    limit_count: short
    min_spawner_count: short
    max_spawner_count: short
    min_interval: float
    max_interval: float
    initial_spawn_count: byte
    _pad1: bytes = binary_pad(0x1F, init=False)
    _spawn_regions_indices: list[int] = field(**EntryRef("POINT_PARAM_ST", array_size=4))
    _spawn_parts_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=32))  # should be Characters
    _pad2: bytes = binary_pad(0x40, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_parts", "spawn_regions"]
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": SpawnerEventDataStruct}

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 32)))
    )
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 4, **MapFieldInfo(GameObjectIntSequence((Region, 4)))
    )

    _spawn_parts_indices: list[int] = binary_array(32, default=None)
    _spawn_regions_indices: list[int] = binary_array(4, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSpawnerEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")


class MessageEventDataStruct(MSBBinaryStruct):
    unk_x00: short
    text_id: short
    # TODO: Not just `is_hidden` and three pad bytes?
    text_param: int


@dataclass(slots=True, eq=False, repr=False)
class MSBMessageEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Message
    STRUCTS = MSBEvent.STRUCTS | {"subtype_data": MessageEventDataStruct}

    unk_x00: int = 0  # TODO: default?
    text_id: int = field(default=-1, **MapFieldInfo(game_type=SoapstoneMessage))
    text_param: int = 0  # TODO: default?
