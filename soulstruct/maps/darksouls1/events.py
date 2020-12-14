__all__ = [
    "MSBEvent",
    "MSBEventList",
    "MSBLightEvent",
    "MSBSoundEvent",
    "MSBFXEvent",
    "MSBWindEvent",
    "MSBMessageEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBPseudoMultiplayerEvent",
]

from soulstruct.game_types import *
from soulstruct.maps.base.events import (
    MSBEvent as _BaseMSBEvent,
    MSBEventList as _BaseMSBEventList,
    MSBLightEvent as _BaseMSBLightEvent,
    MSBSoundEvent as _BaseMSBSoundEvent,
    MSBFXEvent as _BaseMSBFXEvent,
    MSBWindEvent as _BaseMSBWindEvent,
    MSBTreasureEvent as _BaseMSBTreasureEvent,
    MSBSpawnerEvent as _BaseMSBSpawnerEvent,
    MSBMessageEvent as _BaseMSBMessageEvent,
    MSBObjActEvent as _BaseMSBObjActEvent,
    MSBSpawnPointEvent as _BaseMSBSpawnPointEvent,
    MSBMapOffsetEvent as _BaseMSBMapOffsetEvent,
    MSBNavigationEvent as _BaseMSBNavigationEvent,
    MSBEnvironmentEvent as _BaseMSBEnvironmentEvent,
    MSBPseudoMultiplayerEvent as _BaseMSBPseudoMultiplayerEvent,
)
from soulstruct.maps.enums import MSBEventSubtype
from soulstruct.utilities import BinaryStruct

from .msb_entry import MSBEntryList


class MSBEvent(_BaseMSBEvent):

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


class MSBFXEvent(_BaseMSBFXEvent, MSBEvent):
    pass


class MSBWindEvent(_BaseMSBWindEvent, MSBEvent):
    pass


class MSBTreasureEvent(_BaseMSBTreasureEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
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
        ("in_chest", "?"),
        ("is_hidden", "?"),
        "2x",
    )

    FIELD_INFO = {
        # base_part, base_region, and entity_id are unused for Treasure.
        "entity_id": _BaseMSBTreasureEvent.FIELD_INFO["entity_id"],
        "treasure_part_name": _BaseMSBTreasureEvent.FIELD_INFO["treasure_part_name"],
        "item_lot_1": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_1"],
        "item_lot_2": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_2"],
        "item_lot_3": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_3"],
        "item_lot_4": (
            "Item Lot 4",
            ItemLotParam,
            "Fourth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_5": (
            "Item Lot 5",
            ItemLotParam,
            "Fifth item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "in_chest": _BaseMSBTreasureEvent.FIELD_INFO["in_chest"],
        "is_hidden": _BaseMSBTreasureEvent.FIELD_INFO["is_hidden"],
    }

    def __init__(self, msb_event_source=None, **kwargs):
        self.item_lot_4 = -1
        self.item_lot_5 = -1
        super().__init__(msb_event_source, **kwargs)


class MSBSpawnerEvent(_BaseMSBSpawnerEvent, MSBEvent):
    pass


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


class MSBPseudoMultiplayerEvent(_BaseMSBPseudoMultiplayerEvent, MSBEvent):
    pass


class MSBEventList(_BaseMSBEventList, MSBEntryList):
    EVENT_SUBTYPE_CLASSES = {
        MSBEventSubtype.Light: MSBLightEvent,
        MSBEventSubtype.Sound: MSBSoundEvent,
        MSBEventSubtype.FX: MSBFXEvent,
        MSBEventSubtype.Wind: MSBWindEvent,
        MSBEventSubtype.Treasure: MSBTreasureEvent,
        MSBEventSubtype.Spawner: MSBSpawnerEvent,
        MSBEventSubtype.Message: MSBMessageEvent,
        MSBEventSubtype.ObjAct: MSBObjActEvent,
        MSBEventSubtype.SpawnPoint: MSBSpawnPointEvent,
        MSBEventSubtype.MapOffset: MSBMapOffsetEvent,
        MSBEventSubtype.Navigation: MSBNavigationEvent,
        MSBEventSubtype.Environment: MSBEnvironmentEvent,
        MSBEventSubtype.PseudoMultiplayer: MSBPseudoMultiplayerEvent,
    }
    EVENT_SUBTYPE_OFFSET = 8
