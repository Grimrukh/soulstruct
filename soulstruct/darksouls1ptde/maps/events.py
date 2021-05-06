from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBEventList",
    "MSBLightEvent",
    "MSBSoundEvent",
    "MSBVFXEvent",
    "MSBWindEvent",
    "MSBMessageEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBNPCInvasionEvent",
]

import abc
import typing as tp

from soulstruct.game_types import *
from soulstruct.base.maps.msb.events import (
    MSBEvent as _BaseMSBEvent,
    MSBEventList as _BaseMSBEventList,
    MSBLightEvent as _BaseMSBLightEvent,
    MSBSoundEvent as _BaseMSBSoundEvent,
    MSBVFXEvent as _BaseMSBVFXEvent,
    MSBWindEvent as _BaseMSBWindEvent,
    MSBTreasureEvent as _BaseMSBTreasureEvent,
    MSBSpawnerEvent as _BaseMSBSpawnerEvent,
    MSBMessageEvent as _BaseMSBMessageEvent,
    MSBObjActEvent as _BaseMSBObjActEvent,
    MSBSpawnPointEvent as _BaseMSBSpawnPointEvent,
    MSBMapOffsetEvent as _BaseMSBMapOffsetEvent,
    MSBNavigationEvent as _BaseMSBNavigationEvent,
    MSBEnvironmentEvent as _BaseMSBEnvironmentEvent,
    MSBNPCInvasionEvent as _BaseMSBNPCInvasionEvent,
)
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.base.maps.msb.enums import MSBEventSubtype
from soulstruct.utilities.binary import BinaryStruct

from .msb_entry import MSBEntryList
from soulstruct.utilities.misc import partialmethod


class MSBEvent(_BaseMSBEvent, abc.ABC):

    EVENT_HEADER_STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("_event_index", "i"),
        ("__event_type", "i"),
        ("_local_event_index", "i"),
        ("__base_data_offset", "i"),
        ("__type_data_offset", "i"),
        "4x",
    )
    EVENT_BASE_DATA_STRUCT = BinaryStruct(
        ("_base_part_index", "i"),
        ("_base_region_index", "i"),
        ("entity_id", "i"),
        "4x",
    )
    NAME_ENCODING = "shift_jis_2004"


class MSBLightEvent(_BaseMSBLightEvent, MSBEvent):
    pass


class MSBSoundEvent(_BaseMSBSoundEvent, MSBEvent):
    pass


class MSBVFXEvent(_BaseMSBVFXEvent, MSBEvent):
    pass


class MSBWindEvent(_BaseMSBWindEvent, MSBEvent):
    pass


class MSBTreasureEvent(_BaseMSBTreasureEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        "4x",
        ("_treasure_part_index", "i"),
        ("item_lot_1", "i"),
        ("minus_one_1", "i", -1),
        ("item_lot_2", "i"),
        ("minus_one_2", "i", -1),
        ("item_lot_3", "i"),
        ("minus_one_3", "i", -1),
        ("item_lot_4", "i"),
        ("minus_one_4", "i", -1),
        ("item_lot_5", "i"),
        ("minus_one_5", "i", -1),
        ("is_in_chest", "?"),
        ("is_hidden", "?"),
        "2x",
    )

    FIELD_INFO = _BaseMSBTreasureEvent.FIELD_INFO | MSBEvent.FIELD_INFO | {
        # base_part, base_region, and entity_id are unused for Treasure.
        "item_lot_4": MapFieldInfo(
            "Item Lot 4",
            ItemLotParam,
            -1,
            "Fourth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_5": MapFieldInfo(
            "Item Lot 5",
            ItemLotParam,
            -1,
            "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
    }

    FIELD_ORDER = (
        "treasure_part_name",
        "item_lot_1",
        "item_lot_2",
        "item_lot_3",
        "item_lot_4",
        "item_lot_5",
        "is_in_chest",
        "is_hidden",
    )

    def __init__(self, source=None, **kwargs):
        self.item_lot_4 = -1
        self.item_lot_5 = -1
        super().__init__(source, **kwargs)


class MSBSpawnerEvent(_BaseMSBSpawnerEvent, MSBEvent):
    SPAWN_REGION_COUNT = 4

    FIELD_INFO = _BaseMSBSpawnerEvent.FIELD_INFO | {
        "spawn_region_names": MapFieldInfo(
            "Spawn Regions",
            GameObjectSequence((Region, SPAWN_REGION_COUNT)),
            [None] * SPAWN_REGION_COUNT,
            "Regions where entities will be spawned.",
        ),
    }


class MSBMessageEvent(_BaseMSBMessageEvent, MSBEvent):
    pass


class MSBObjActEvent(_BaseMSBObjActEvent, MSBEvent):
    pass


class MSBSpawnPointEvent(_BaseMSBSpawnPointEvent, MSBEvent):
    pass


class MSBMapOffsetEvent(_BaseMSBMapOffsetEvent, MSBEvent):
    pass


class MSBNavigationEvent(_BaseMSBNavigationEvent, MSBEvent):
    pass


class MSBEnvironmentEvent(_BaseMSBEnvironmentEvent, MSBEvent):
    pass


class MSBNPCInvasionEvent(_BaseMSBNPCInvasionEvent, MSBEvent):
    pass


class MSBEventList(_BaseMSBEventList, MSBEntryList):
    SUBTYPE_CLASSES = {
        MSBEventSubtype.Light: MSBLightEvent,
        MSBEventSubtype.Sound: MSBSoundEvent,
        MSBEventSubtype.VFX: MSBVFXEvent,
        MSBEventSubtype.Wind: MSBWindEvent,
        MSBEventSubtype.Treasure: MSBTreasureEvent,
        MSBEventSubtype.Spawner: MSBSpawnerEvent,
        MSBEventSubtype.Message: MSBMessageEvent,
        MSBEventSubtype.ObjAct: MSBObjActEvent,
        MSBEventSubtype.SpawnPoint: MSBSpawnPointEvent,
        MSBEventSubtype.MapOffset: MSBMapOffsetEvent,
        MSBEventSubtype.Navigation: MSBNavigationEvent,
        MSBEventSubtype.Environment: MSBEnvironmentEvent,
        MSBEventSubtype.NPCInvasion: MSBNPCInvasionEvent,
    }
    SUBTYPE_OFFSET = 8

    Lights: tp.Sequence[MSBLightEvent]
    Sounds: tp.Sequence[MSBSoundEvent]
    VFX: tp.Sequence[MSBVFXEvent]
    Wind: tp.Sequence[MSBWindEvent]
    Treasure: tp.Sequence[MSBTreasureEvent]
    Spawners: tp.Sequence[MSBSpawnerEvent]
    Messages: tp.Sequence[MSBMessageEvent]
    ObjActs: tp.Sequence[MSBObjActEvent]
    SpawnPoints: tp.Sequence[MSBSpawnPointEvent]
    MapOffsets: tp.Sequence[MSBMapOffsetEvent]
    Navigation: tp.Sequence[MSBNavigationEvent]
    Environment: tp.Sequence[MSBEnvironmentEvent]
    NPCInvasion: tp.Sequence[MSBNPCInvasionEvent]

    new = _BaseMSBEventList.new
    new_light: tp.Callable[..., MSBLightEvent] = partialmethod(new, MSBEventSubtype.Light)
    new_wind: tp.Callable[..., MSBWindEvent] = partialmethod(new, MSBEventSubtype.Wind)
    new_npc_invasion: tp.Callable[..., MSBNPCInvasionEvent] = partialmethod(new, MSBEventSubtype.NPCInvasion)
