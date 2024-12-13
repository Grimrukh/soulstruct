from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBObjActEvent",
    "MSBNavigationEvent",
    "MSBNPCInvasionEvent",
    "MSBPlatoonEvent",
    "MSBPatrolRouteEvent",
    "MSBMountEvent",
    "MSBSignPoolEvent",
    "MSBRetryPointEvent",
    "MSBOtherEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.bloodborne.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.utilities.binary import *

from .enums import MSBEventSubtype
from .regions import MSBRegion
from .parts import MSBPart

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


class EventHeaderStruct(MSBHeaderStruct):
    name_offset: long
    supertype_index: int
    _subtype_int: int
    subtype_index: int
    event_unkh_14: int = binary(asserted=(0, 1))
    supertype_data_offset: long
    subtype_data_offset: long
    extra_data_offset: long


class EventDataStruct(MSBBinaryStruct):
    _attached_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _attached_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    entity_id: int
    event_unkd_0c: byte
    _pad1: bytes = binary_pad(3, init=False)


class EventExtraDataStruct(MSBBinaryStruct):
    map_id: int
    unk_04: int
    unk_08: int
    unk_0c: int
    _pad1: bytes = binary_pad(16, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Bloodborne."""
    
    HEADER_STRUCT = EventHeaderStruct
    STRUCTS = {
        "supertype_data": EventDataStruct,
        "subtype_data": None,
        "extra_data": EventExtraDataStruct,
    }

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None

    event_unkh_14: int = 0
    event_unkd_0c: int = 0

    map_id: int = 0
    unk_04: int = 0
    unk_08: int = 0
    unk_0c: int = 0


class TreasureEventDataStruct(MSBBinaryStruct):
    _pad1: bytes = binary_pad(8)
    _treasure_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _pad2: bytes = binary_pad(4)
    item_lot: int
    _pad3: bytes = binary_pad(0x24, b"\xFF", init=False)
    action_button_id: int
    pickup_animation_id: int
    is_in_chest: bool
    starts_disabled: bool
    _pad4: bytes = binary_pad(14)


@dataclass(slots=True, eq=False, repr=False)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "treasure_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": TreasureEventDataStruct,
    }

    treasure_part: MSBPart = None
    item_lot: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    action_button_id: int = 0
    pickup_animation_id: int = 0
    is_in_chest: bool = False
    starts_disabled: bool = False
    
    _treasure_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBTreasureEvent, self).indices_to_objects(entry_lists)
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
    _pad1: bytes = binary_pad(3)
    spawner_unk_14: float
    spawner_unk_18: float
    _pad2: bytes = binary_pad(0x14, init=False)
    _spawn_regions_indices: list[int] = field(**EntryRef("POINT_PARAM_ST", array_size=8))
    _pad3: bytes = binary_pad(0x10, init=False)
    _spawn_parts_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=32))
    _pad4: bytes = binary_pad(0x20, init=False)


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_parts", "spawn_regions"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": SpawnerEventDataStruct,
    }

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawner_unk_14: float = 0.0
    spawner_unk_18: float = 0.0
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 32)))
    )
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(GameObjectIntSequence((Region, 8)))
    )

    _spawn_parts_indices: list[int] = binary_array(32, default=None)
    _spawn_regions_indices: list[int] = binary_array(8, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSpawnerEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")


class ObjActEventDataStruct(MSBBinaryStruct):
    obj_act_entity_id: int
    _obj_act_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    obj_act_param_id: int
    obj_act_state: byte
    _pad1: bytes = binary_pad(3)
    obj_act_flag: int
    _pad2: bytes = binary_pad(12)


@dataclass(slots=True, eq=False, repr=False)
class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.ObjAct
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "obj_act_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": ObjActEventDataStruct,
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


class NavigationEventDataStruct(MSBBinaryStruct):
    _navigation_region_index: int = field(**EntryRef("POINT_PARAM_ST"))
    _pad1: bytes = binary_pad(12)


@dataclass(slots=True, eq=False, repr=False)
class MSBNavigationEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Navigation
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "navigation_region"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": NavigationEventDataStruct,
    }

    navigation_region: MSBRegion = None

    _navigation_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBNavigationEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "navigation_region")


class NPCInvasionEventDataStruct(MSBBinaryStruct):
    host_entity_id: int
    invasion_flag_id: int
    activate_good_id: int
    npc_invasion_unk_0c: int
    npc_invasion_unk_10: int
    npc_invasion_unk_14: int
    npc_invasion_unk_18: int
    npc_invasion_unk_1c: int
    _minus_one: int = binary(asserted=-1)


@dataclass(slots=True, eq=False, repr=False)
class MSBNPCInvasionEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.NPCInvasion
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": NPCInvasionEventDataStruct,
    }

    host_entity_id: int = -1
    invasion_flag_id: int = field(default=-1, **MapFieldInfo(game_type=Flag))
    activate_good_id: int = field(default=-1, **MapFieldInfo(game_type=GoodParam))
    npc_invasion_unk_0c: int = 0
    npc_invasion_unk_10: int = 0
    npc_invasion_unk_14: int = 0
    npc_invasion_unk_18: int = 0
    npc_invasion_unk_1c: int = 0


class PlatoonEventDataStruct(MSBBinaryStruct):
    platoon_id_script_activate: int
    state: int
    _pad1: bytes = binary_pad(8)
    _platoon_parts_indices: list[int] = field(**EntryRef("PARTS_PARAM_ST", array_size=32))


@dataclass(slots=True, eq=False, repr=False)
class MSBPlatoonEvent(MSBEvent):
    """Defines a group (platoon) of enemies."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Platoon
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = [
        "attached_part", "attached_region", "platoon_parts"
    ]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": PlatoonEventDataStruct,
    }

    platoon_id_script_activate: int = -1
    state: int = -1
    platoon_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((MapPart, 32)))
    )

    _platoon_parts_indices: list[int] = binary_array(32, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBPlatoonEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "platoon_parts")


class PatrolRouteEventDataStruct(MSBBinaryStruct):
    patrol_type: byte
    _pad1: bytes = binary_pad(2)
    _one: byte = binary(asserted=1)
    _minus_one: int = binary(asserted=-1)
    _pad2: bytes = binary_pad(8)
    _patrol_regions_indices: list[short] = field(**EntryRef("POINT_PARAM_ST", array_size=64))


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRouteEvent(MSBEvent):
    """Defines a patrol route through a sequence of up to 32 regions."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.PatrolRouteEvent
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "patrol_regions"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": PatrolRouteEventDataStruct,
    }

    patrol_type: int = 0
    patrol_regions: list[MSBRegion | None] = field(
        default_factory=lambda: [None] * 64, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 64)))
    )

    _patrol_regions_indices: list[int] = binary_array(64, default=None)

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBPatrolRouteEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


class MountEventDataStruct(MSBBinaryStruct):
    _rider_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    _mount_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))


@dataclass(slots=True, eq=False, repr=False)
class MSBMountEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Mount
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "rider_part", "mount_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": MountEventDataStruct,
    }

    rider_part: MSBPart = None
    mount_part: MSBPart = None

    _rider_part_index: int = None
    _mount_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBMountEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "rider_part")
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "mount_part")


class SignPoolEventDataStruct(MSBBinaryStruct):
    _sign_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    sign_pool_unk_04: int
    _pad1: bytes = binary_pad(8)


@dataclass(slots=True, eq=False, repr=False)
class MSBSignPoolEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.SignPool
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "sign_part"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": SignPoolEventDataStruct,
    }
    sign_part: MSBPart = None
    sign_pool_unk_04: int = 0

    _sign_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBSignPoolEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "sign_part")


class RetryPointEventDataStruct(MSBBinaryStruct):
    _retry_part_index: int = field(**EntryRef("PARTS_PARAM_ST"))
    event_flag_id: uint
    retry_point_unk_08: float
    _retry_region_index: short = field(**EntryRef("POINT_PARAM_ST"))
    _zero: short = binary(asserted=0)


@dataclass(slots=True, eq=False, repr=False)
class MSBRetryPointEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.RetryPoint
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "retry_part", "retry_region"]
    STRUCTS = MSBEvent.STRUCTS | {
        "subtype_data": RetryPointEventDataStruct,
    }

    retry_part: MSBPart = None
    event_flag_id: int = field(default=0, **MapFieldInfo(game_type=Flag))
    retry_point_unk_08: float = 0.0
    retry_region: MSBRegion = None

    _retry_part_index: int = None
    _retry_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        super(MSBRetryPointEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "retry_part")
        self._consume_index(entry_lists, "POINT_PARAM_ST", "retry_region")


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.OtherEvent
