from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBSoundEvent",
    "MSBVFXEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBMessageEvent",
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBWindVFXEvent",
    "MSBPatrolRouteEvent",
    "MSBDarkLockEvent",
    "MSBPlatoonEvent",
    "MSBMultiSummonEvent",
    "MSBOtherEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.bloodborne.events.enums import SoundType
from soulstruct.bloodborne.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBEventSubtype
from .regions import MSBRegion
from .parts import MSBPart, MSBCharacter

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


@dataclass(slots=True)
class EventHeaderStruct(MSBHeaderStruct):
    name_offset: long
    supertype_index: int
    _subtype_int: int
    subtype_index: int
    _pad1: bytes = field(**BinaryPad(4))
    supertype_data_offset: long
    subtype_data_offset: long


@dataclass(slots=True)
class EventDataStruct(MSBBinaryStruct):
    _attached_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _attached_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    entity_id: int
    unknowns: list[byte] = field(**BinaryArray(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Bloodborne."""

    HEADER_STRUCT = EventHeaderStruct
    STRUCTS = {
        "supertype_data_struct": EventDataStruct,
    }

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None

    unknowns: list[int] = field(default_factory=lambda: [0, 0, 0, 0], **BinaryArray(length=4))


@dataclass(slots=True)
class SoundEventDataStruct(MSBBinaryStruct):
    sound_type: int
    sound_id: int


@dataclass(slots=True, eq=False, repr=False)
class MSBSoundEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Sound
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": SoundEventDataStruct
    }

    sound_type: int = field(default=SoundType.m_Music.value, **MapFieldInfo(game_type=SoundType))
    sound_id: int = -1


@dataclass(slots=True)
class VFXEventDataStruct(MSBBinaryStruct):
    vfx_id: int
    starts_disabled: bool
    _pad1: bytes = field(**BinaryPad(3))


@dataclass(slots=True, eq=False, repr=False)
class MSBVFXEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.VFX
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": VFXEventDataStruct
    }
    vfx_id: int = 0
    starts_disabled: bool = False


@dataclass(slots=True)
class TreasureEventDataStruct(MSBBinaryStruct):
    _pad1: bytes = field(**BinaryPad(8))
    _treasure_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _pad2: bytes = field(**BinaryPad(4))
    item_lot_1: int
    item_lot_2: int
    item_lot_3: int
    unknown_x1c_x20: int
    unknown_x20_x24: int
    unknown_x24_x28: int
    unknown_x28_x2c: int
    unknown_x2c_x30: int
    unknown_x30_x34: int
    unknown_x34_x38: int
    unknown_x38_x3c: int
    unknown_x3c_x40: int
    is_in_chest: bool
    is_hidden: bool
    unknown_x42_x44: short
    unknown_x44_x48: int
    unknown_x48_x4c: int
    _pad3: bytes = field(**BinaryPad(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "treasure_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": TreasureEventDataStruct
    }

    treasure_part: MSBPart = None
    item_lot_1: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_2: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_3: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    is_in_chest: bool = False
    is_hidden: bool = False
    unknown_x1c_x20: int = -1
    unknown_x20_x24: int = -1
    unknown_x24_x28: int = -1
    unknown_x28_x2c: int = -1
    unknown_x2c_x30: int = -1
    unknown_x30_x34: int = -1
    unknown_x34_x38: int = -1
    unknown_x38_x3c: int = 0
    unknown_x3c_x40: int = -1
    unknown_x42_x44: int = 0
    unknown_x44_x48: int = -1
    unknown_x48_x4c: int = -1

    _treasure_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBTreasureEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "treasure_part")


@dataclass(slots=True)
class SpawnerEventDataStruct(MSBBinaryStruct):
    max_count: byte
    spawner_type: sbyte
    limit_count: short
    min_spawner_count: short
    max_spawner_count: short
    min_interval: float
    max_interval: float
    initial_spawn_count: byte
    _pad1: bytes = field(**BinaryPad(31))
    _spawn_regions_indices: list[int] = field(**EntryRef("POINT_PARAM_ST", array_size=8))
    _spawn_parts_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=32))
    _pad2: bytes = field(**BinaryPad(64))


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_parts", "spawn_regions"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": SpawnerEventDataStruct
    }

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 32))))
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(GameObjectIntSequence((Region, 8))))

    _spawn_parts_indices: list[int] = field(default=None, **BinaryArray(32))
    _spawn_regions_indices: list[int] = field(default=None, **BinaryArray(8))

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSpawnerEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")


@dataclass(slots=True)
class MessageEventDataStruct(MSBBinaryStruct):
    text_id: short
    unk_x02_x04: short
    is_hidden: bool
    _pad1: bytes = field(**BinaryPad(3))


@dataclass(slots=True, eq=False, repr=False)
class MSBMessageEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Message
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": MessageEventDataStruct
    }

    text_id: int = field(default=-1, **MapFieldInfo(game_type=SoapstoneMessage))
    unk_x02_x04: int = 2
    is_hidden: bool = False


@dataclass(slots=True)
class ObjActEventDataStruct(MSBBinaryStruct):
    obj_act_entity_id: int
    _obj_act_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    obj_act_param_id: int
    obj_act_state: byte
    _pad1: bytes = field(**BinaryPad(3))
    obj_act_flag: int
    _pad2: bytes = field(**BinaryPad(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.ObjAct
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "obj_act_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": ObjActEventDataStruct
    }

    obj_act_entity_id: int = -1
    obj_act_part: MSBPart = None
    obj_act_param_id: int = field(default=-1, **MapFieldInfo(game_type=ObjActParam))
    obj_act_state: int = 0
    obj_act_flag: int = field(default=0, **MapFieldInfo(game_type=Flag))

    _obj_act_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBObjActEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "obj_act_part")


@dataclass(slots=True)
class WindVFXEventDataStruct(MSBBinaryStruct):
    vfx_id: int
    _wind_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    unk_x08_x0c: float
    _pad1: bytes = field(**BinaryPad(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBWindVFXEvent(MSBEvent):
    
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.WindVFX
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "wind_region"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": WindVFXEventDataStruct
    }
        
    vfx_id: int = -1
    wind_region: MSBRegion = None
    unk_x08_x0c: float = 1.0

    _wind_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBWindVFXEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "wind_region")


@dataclass(slots=True)
class PatrolRouteEventDataStruct(MSBBinaryStruct):
    unk_x00_x04: int
    _pad1: bytes = field(**BinaryPad(12))
    _patrol_regions_indices: list[short] = field(**EntryRef("POINT_PARAM_ST", array_size=32))


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRouteEvent(MSBEvent):
    """Defines a patrol route through a sequence of up to 32 regions."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.PatrolRoute
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "patrol_regions"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": PatrolRouteEventDataStruct
    }

    unk_x00_x04: int = -1
    patrol_regions: list[MSBRegion | None] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 32))))

    _patrol_regions_indices: list[int] = field(default=None, **BinaryArray(32))

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBPatrolRouteEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


@dataclass(slots=True)
class DarkLockEventDataStruct(MSBBinaryStruct):
    """No data."""
    _pad1: bytes = field(**BinaryPad(32))


@dataclass(slots=True, eq=False, repr=False)
class MSBDarkLockEvent(MSBEvent):
    """Unknown purpose. Has no event-specific data."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.DarkLock
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": DarkLockEventDataStruct
    }


@dataclass(slots=True)
class PlatoonEventDataStruct(MSBBinaryStruct):
    platoon_id_script_activate: int
    state: int
    _pad1: bytes = field(**BinaryPad(16))
    # TODO: Confirm these are actually Character subtype indices.
    _platoon_character_indices: list[int] = field(**EntryRef("characters", array_size=30))
    _platoon_parent_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=2))


@dataclass(slots=True, eq=False, repr=False)
class MSBPlatoonEvent(MSBEvent):
    """Defines a group (platoon) of enemies."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Platoon
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = [
        "attached_part", "attached_region", "platoon_characters", "platoon_parents"
    ]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": PlatoonEventDataStruct
    }
 
    platoon_characters: list[MSBCharacter] = field(
        default_factory=lambda: [None] * 30, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 30))))
    platoon_parents: list[MSBPart] = field(
        default_factory=lambda: [None] * 2, **MapFieldInfo(game_type=GameObjectIntSequence((MapPart, 2))))
    platoon_id_script_activate: int = -1
    state: int = -1

    _platoon_characters_indices: list[int] = field(default=None, **BinaryArray(30))
    _platoon_parents_indices: list[int] = field(default=None, **BinaryArray(2))

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBPlatoonEvent, self).indices_to_objects(entry_lists)
        # TODO: Confirm these are actually Character subtype indices.
        self._consume_indices(entry_lists, "characters", "platoon_characters")
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "platoon_parents")


@dataclass(slots=True)
class MultiSummonEventDataStruct(MSBBinaryStruct):
    unk_x00_x04: int
    unk_x04_x06: short
    unk_x06_x08: short
    unk_x08_x0a: short
    unk_x0a_x0c: short
    _pad1: bytes = field(**BinaryPad(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBMultiSummonEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.MultiSummon
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": MultiSummonEventDataStruct
    }

    unk_x00_x04: int = 1
    unk_x04_x06: int = 1
    unk_x06_x08: int = 1
    unk_x08_x0a: int = 1
    unk_x0a_x0c: int = 1


@dataclass(slots=True)
class SpawnPointEventDataStruct(MSBBinaryStruct):
    _spawn_point_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    _pad1: bytes = field(**BinaryPad(12))


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnPointEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.SpawnPoint
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_point_region"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": SpawnPointEventDataStruct
    }

    spawn_point_region: MSBRegion = None

    _spawn_point_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSpawnPointEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "spawn_point_region")


@dataclass(slots=True)
class MapOffsetEventDataStruct(MSBBinaryStruct):
    translate: Vector3
    rotate_y: float


@dataclass(slots=True, eq=False, repr=False)
class MSBMapOffsetEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.MapOffset
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": MapOffsetEventDataStruct
    }

    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate_y: float = 0.0


@dataclass(slots=True)
class NavigationEventDataStruct(MSBBinaryStruct):
    _navigation_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    _pad1: bytes = field(**BinaryPad(12))


@dataclass(slots=True, eq=False, repr=False)
class MSBNavigationEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Navigation
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "navigation_region"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": NavigationEventDataStruct
    }

    navigation_region: MSBRegion = None

    _navigation_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBNavigationEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "navigation_region")


@dataclass(slots=True)
class EnvironmentEventDataStruct(MSBBinaryStruct):
    unk_x00_x04: int
    unk_x04_x08: float
    unk_x08_x0c: float
    unk_x0c_x10: float
    unk_x10_x14: float
    unk_x14_x18: float
    _pad1: bytes = field(**BinaryPad(8))


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Environment
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": EnvironmentEventDataStruct
    }

    unk_x00_x04: int = 0
    unk_x04_x08: float = 1.0
    unk_x08_x0c: float = 1.0
    unk_x0c_x10: float = 1.0
    unk_x10_x14: float = 1.0
    unk_x14_x18: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.OtherEvent
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": None
    }
