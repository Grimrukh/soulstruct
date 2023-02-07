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
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBNPCInvasionEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.bloodborne.events.emevd.enums import SoundType
from soulstruct.bloodborne.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb import MSBEntry
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBEventSubtype

if tp.TYPE_CHECKING:
    from .regions import MSBRegion
    from .parts import MSBPart


@dataclass(slots=True)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Bloodborne."""

    class SUPERTYPE_HEADER_STRUCT(NewBinaryStruct):
        name_offset: long
        _event_index: int
        event_type: int
        _local_event_index: int
        _pad1: bytes = field(**BinaryPad(4))
        supertype_data_offset: long
        subtype_data_offset: long

    class SUPERTYPE_DATA_STRUCT(NewBinaryStruct):
        _attached_part_index: int
        _attached_region_index: int
        entity_id: int
        unknowns: tuple[byte, byte, byte, byte]

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None

    unknowns: tuple[int, int, int, int] = (0, 0, 0, 0)


@dataclass(slots=True)
class MSBLightEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Light

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        point_light_id: int

    point_light_id: int = field(default=0, **MapFieldInfo(linked_type=PointLightParam))


@dataclass(slots=True)
class MSBSoundEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Sound

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        sound_type: SoundType = field(**Binary(int))
        sound_id: int

    sound_type: SoundType = SoundType.m_Music
    sound_id: int = -1


@dataclass(slots=True)
class MSBVFXEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.VFX

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        vfx_id: int

    vfx_id: int = 0


@dataclass(slots=True)
class MSBWindEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Wind

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        wind_vector_min: Vector3
        unk_x04_x08: float
        wind_vector_max: Vector3
        unk_x0c_x10: float
        wind_swing_cycles: tuple[float, float, float, float]
        wind_swing_powers: tuple[float, float, float, float]

    wind_vector_min: Vector3 = field(default_factory=lambda: Vector3.zero())
    unk_x04_x08: float = 0.0
    wind_vector_max: Vector3 = field(default_factory=lambda: Vector3.zero())
    unk_x0c_x10: float = 0.0
    wind_swing_cycles: list[int] = field(default_factory=lambda: [0.0] * 4)
    wind_swing_powers: list[int] = field(default_factory=lambda: [0.0] * 4)


@dataclass(slots=True)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        _pad1: bytes = field(**BinaryPad(4))
        _treasure_part_index: int
        item_lot_1: int
        _minus_one_1: int = field(**Binary(asserted=-1))
        item_lot_2: int
        _minus_one_2: int = field(**Binary(asserted=-1))
        item_lot_3: int
        _minus_one_3: int = field(**Binary(asserted=-1))
        item_lot_4: int
        _minus_one_4: int = field(**Binary(asserted=-1))
        item_lot_5: int
        _minus_one_5: int = field(**Binary(asserted=-1))
        is_in_chest: bool
        is_hidden: bool
        _pad2: bytes = field(**BinaryPad(2))

    treasure_part: MSBPart = None
    item_lot_1: int = field(default=-1, **MapFieldInfo(linked_type=ItemLotParam))
    item_lot_2: int = field(default=-1, **MapFieldInfo(linked_type=ItemLotParam))
    item_lot_3: int = field(default=-1, **MapFieldInfo(linked_type=ItemLotParam))
    item_lot_4: int = field(default=-1, **MapFieldInfo(linked_type=ItemLotParam))
    item_lot_5: int = field(default=-1, **MapFieldInfo(linked_type=ItemLotParam))
    is_in_chest: bool = False
    is_hidden: bool = False

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "treasures")


@dataclass(slots=True)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        max_count: byte
        spawner_type: sbyte
        limit_count: short
        min_spawner_count: short
        max_spawner_count: short
        min_interval: float
        max_interval: float
        initial_spawn_count: int
        _pad1: bytes = field(**BinaryPad(28))
        _spawn_region_indices: list[int] = field(**Binary(length=4))
        _spawn_part_indices: list[int] = field(**Binary(length=32))
        _pad2: bytes = field(**BinaryPad(64))

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(linked_type=GameObjectSequence((Character, 32)))
    )
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 4, **MapFieldInfo(GameObjectSequence((Region, 4)))
    )

    _spawn_parts_indices: list[int] | None = None
    _spawn_regions_indices: list[int] | None = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")


@dataclass(slots=True)
class MSBMessageEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Message

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        text_id: short
        unk_x02_x04: short
        is_hidden: bool
        _pad1: bytes = field(**BinaryPad(3))

    text_id: int = field(default=-1, **MapFieldInfo(linked_type=SoapstoneMessage))
    unk_x02_x04: int = 2
    is_hidden: bool = False


@dataclass(slots=True)
class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.ObjAct

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        obj_act_entity_id: int
        _obj_act_part_index: int
        obj_act_param_id: int
        obj_act_state: byte
        _pad1: bytes = field(**BinaryPad(1))
        obj_act_flag: int

    obj_act_entity_id: int = -1
    obj_act_part: MSBPart = None
    obj_act_param_id: int = field(default=-1, **MapFieldInfo(linked_type=ObjActParam))
    obj_act_state: int = 0
    obj_act_flag: int = field(default=0, **MapFieldInfo(linked_type=Flag))

    _obj_act_part_index: int | None = None
    _obj_act_part_name: int | None = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "obj_act_part")


@dataclass(slots=True)
class MSBSpawnPointEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.SpawnPoint

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        _spawn_point_region_index: int
        _pad1: bytes = field(**BinaryPad(12))

    spawn_point_region: MSBRegion = None

    _spawn_point_region_index: int | None = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "spawn_point_region")


@dataclass(slots=True)
class MSBMapOffsetEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.MapOffset

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        translate: Vector3
        rotate_y: float

    translate: Vector3 = field(default_factory=lambda: Vector3.zero())
    rotate: float = 0.0


@dataclass(slots=True)
class MSBNavigationEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Navigation

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        _navigation_region_index: int
        _pad1: bytes = field(**BinaryPad(12))

    navigation_region: MSBRegion = None

    _navigation_region_index: int | None = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "navigation_region")


@dataclass(slots=True)
class MSBEnvironmentEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Environment

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        unk_x00_x04: int
        unk_x04_x08: float
        unk_x08_x0c: float
        unk_x0c_x10: float
        unk_x10_x14: float
        unk_x14_x18: float
        _pad1: bytes = field(**BinaryPad(8))

    unk_x00_x04: int = 0
    unk_x04_x08: float = 1.0
    unk_x08_x0c: float = 1.0
    unk_x0c_x10: float = 1.0
    unk_x10_x14: float = 1.0
    unk_x14_x18: float = 1.0


@dataclass(slots=True)
class MSBNPCInvasionEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.NPCInvasion

    class SUBTYPE_DATA_STRUCT(NewBinaryStruct):
        host_entity_id: int
        invasion_flag_id: int
        _spawn_point_region_index: int
        _pad1: bytes = field(**BinaryPad(4))

    host_entity_id: int = -1
    invasion_flag_id: int = field(default=-1, **MapFieldInfo(linked_type=Flag))
    spawn_point_region: MSBRegion = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super().indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "spawn_point_region")
