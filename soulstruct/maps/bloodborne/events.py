__all__ = [
    "MSBEvent",
    "MSBSoundEvent",
    "MSBFXEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBMessageEvent",
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBWindFXEvent",
    "MSBPatrolRouteEvent",
    "MSBDarkLockEvent",
    "MSBPlatoonEvent",
    "MSBMultiSummonEvent",
    "MSBEventList",
]

import typing as tp

from soulstruct.game_types import *
from soulstruct.maps.base.events import (
    MSBEvent as _BaseMSBEvent,
    MSBEventList as _BaseMSBEventList,
    MSBSoundEvent as _BaseMSBSoundEvent,
    MSBFXEvent as _BaseMSBFXEvent,
    MSBMessageEvent as _BaseMSBMessageEvent,
    MSBTreasureEvent as _BaseMSBTreasureEvent,
    MSBSpawnerEvent as _BaseMSBSpawnerEvent,
    MSBObjActEvent as _BaseMSBObjActEvent,
    MSBSpawnPointEvent as _BaseMSBSpawnPointEvent,
    MSBMapOffsetEvent as _BaseMSBMapOffsetEvent,
    MSBNavigationEvent as _BaseMSBNavigationEvent,
    MSBEnvironmentEvent as _BaseMSBEnvironmentEvent,
)
from soulstruct.maps.enums import MSBEventSubtype
from soulstruct.utilities.binary_struct import BinaryStruct

from .msb_entry import MSBEntryList


class MSBEvent(_BaseMSBEvent):
    """MSB event entry in Bloodborne."""

    EVENT_HEADER_STRUCT = BinaryStruct(
        ("__name_offset", "q"),
        ("_event_index", "i"),
        ("__event_type", "i"),
        ("_local_event_index", "i"),
        "4x",
        ("__base_data_offset", "q"),
        ("__type_data_offset", "q"),
    )

    EVENT_TYPE_OFFSET = 12

    EVENT_BASE_DATA_STRUCT = BinaryStruct(
        ("_base_part_index", "i"),
        ("_base_region_index", "i"),
        ("entity_id", "i"),
        ("_unknowns", "4b"),
    )

    NAME_ENCODING = "utf-16-le"

    def __init__(self, msb_event_source=None):
        self._unknowns = [0, 0, 0, 0]
        super().__init__(msb_event_source)


class MSBSoundEvent(_BaseMSBSoundEvent, MSBEvent):
    pass


class MSBFXEvent(_BaseMSBFXEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("fx_id", "i"),
        ("_starts_disabled", "i"),  # 32-bit bool
    )

    FIELD_INFO = _BaseMSBFXEvent.FIELD_INFO | {
        "starts_disabled": (
            "Starts Disabled",
            bool,
            "FX will not be automatically created on map load (requires event script).",
        )
    }

    FIELD_NAMES = _BaseMSBFXEvent.FIELD_NAMES + (
        "starts_disabled",
    )

    def __init__(self, msb_event_source=None, **kwargs):
        self._starts_disabled = 0
        super().__init__(msb_event_source, **kwargs)

    @property
    def starts_disabled(self) -> bool:
        return bool(self._starts_disabled)

    @starts_disabled.setter
    def starts_disabled(self, value: tp.Union[bool, int]):
        if value in {True, False, 0, 1}:
            self._starts_disabled = int(value)
        else:
            raise ValueError(f"`MSBFX.starts_disabled` is boolean and cannot be set to {value}.")


class MSBTreasureEvent(_BaseMSBTreasureEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        "8x",
        ("_treasure_part_index", "i"),
        "4x",
        ("item_lot_1", "i"),
        ("item_lot_2", "i"),
        ("item_lot_3", "i"),
        ("unknown_x1c_x20", "i"),
        ("unknown_x20_x24", "i"),
        ("unknown_x24_x28", "i"),
        ("unknown_x28_x2c", "i"),
        ("unknown_x2c_x30", "i"),
        ("unknown_x30_x34", "i"),
        ("unknown_x34_x38", "i"),
        ("unknown_x38_x3c", "i"),
        ("unknown_x3c_x40", "i"),
        ("in_chest", "?"),
        ("is_hidden", "?"),
        ("unknown_x42_x44", "h"),
        ("unknown_x44_x48", "i"),
        ("unknown_x48_x4c", "i"),
        "4x",
    )

    FIELD_INFO = {
        # base_part, base_region, and entity_id are unused for Treasure.
        "entity_id": _BaseMSBTreasureEvent.FIELD_INFO["entity_id"],
        "treasure_part_name": _BaseMSBTreasureEvent.FIELD_INFO["treasure_part_name"],
        "item_lot_1": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_1"],
        "item_lot_2": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_2"],
        "item_lot_3": _BaseMSBTreasureEvent.FIELD_INFO["item_lot_3"],
        "unknown_x1c_x20": (
            "Unknown [1c-20]",
            int,
            "Unknown integer.",
        ),
        "unknown_x20_x24": (
            "Unknown [20-24]",
            int,
            "Unknown integer.",
        ),
        "unknown_x24_x28": (
            "Unknown [24-28]",
            int,
            "Unknown integer.",
        ),
        "unknown_x28_x2c": (
            "Unknown [28-2c]",
            int,
            "Unknown integer.",
        ),
        "unknown_x2c_x30": (
            "Unknown [2c-30]",
            int,
            "Unknown integer.",
        ),
        "unknown_x30_x34": (
            "Unknown [30-34]",
            int,
            "Unknown integer.",
        ),
        "unknown_x34_x38": (
            "Unknown [34-38]",
            int,
            "Unknown integer.",
        ),
        "unknown_x38_x3c": (
            "Unknown [38-3c]",
            int,
            "Unknown integer.",
        ),
        "unknown_x3c_x40": (
            "Unknown [3c-40]",
            int,
            "Unknown integer.",
        ),
        "in_chest": _BaseMSBTreasureEvent.FIELD_INFO["in_chest"],
        "is_hidden": _BaseMSBTreasureEvent.FIELD_INFO["is_hidden"],
        "unknown_x42_x44": (
            "Unknown [42-44]",
            int,
            "Unknown short.",
        ),
        "unknown_x44_x48": (
            "Unknown [44-48]",
            int,
            "Unknown integer.",
        ),
        "unknown_x48_x4c": (
            "Unknown [48-4c]",
            int,
            "Unknown integer.",
        ),
    }

    def __init__(self, msb_event_source=None, **kwargs):
        self.unknown_x1c_x20 = 0
        self.unknown_x20_x24 = 0
        self.unknown_x24_x28 = 0
        self.unknown_x28_x2c = 0
        self.unknown_x2c_x30 = 0
        self.unknown_x30_x34 = 0
        self.unknown_x34_x38 = 0
        self.unknown_x38_x3c = 0
        self.unknown_x3c_x40 = 0
        self.unknown_x42_x44 = 0
        self.unknown_x44_x48 = 0
        self.unknown_x48_x4c = 0
        super().__init__(msb_event_source, **kwargs)


class MSBSpawnerEvent(_BaseMSBSpawnerEvent, MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    EVENT_TYPE_DATA_STRUCT = (
        ("max_count", "B"),
        ("spawner_type", "b"),
        ("limit_count", "h"),
        ("min_spawner_count", "h"),
        ("max_spawner_count", "h"),
        ("min_interval", "f"),
        ("max_interval", "f"),
        ("initial_spawn_count", "B"),
        "31x",
        ("_spawn_region_indices", "8i"),
        ("_spawn_part_indices", "32i"),
        "64x",
    )

    SPAWN_REGION_COUNT = 8


class MSBMessageEvent(_BaseMSBMessageEvent, MSBEvent):
    pass


class MSBObjActEvent(_BaseMSBObjActEvent, MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    EVENT_TYPE_DATA_STRUCT = (
        ("obj_act_entity_id", "i"),
        ("_obj_act_part_index", "i"),
        ("obj_act_param_id", "i"),
        ("obj_act_state", "B"),
        "3x",
        ("obj_act_flag", "i"),
        "4x",
    )


class MSBWindFXEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("fx_id", "i"),
        ("_wind_region_index", "i"),
        ("unk_x08_x0c", "f"),
        "4x",
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "FX will be drawn if this parent (usually a Collision or Map Piece part) is drawn. Possibly unused.",
        ),
        "base_region_name": (
            "Base Region",
            Region,
            "Base event region. Possibly unused with WindFX (see Wind Region Name instead).",
        ),
        "wind_region_name": (
            "FX Region",
            str,
            "Region at or in which wind FX appears.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to this FX in other game files. Possibly unused with WindFX.",
        ),
        "fx_id": (
            "FX ID",
            int,
            "Visual effect ID, which refers to a loaded FX file.",
        ),
        "unk_x08_x0c": (
            "Unknown [08-0c]",
            float,
            "Unknown floating-point number.",
        )
    }

    ENTRY_SUBTYPE = MSBEventSubtype.WindFX

    def __init__(self, msb_event_source, **kwargs):
        self._wind_region_index = None
        self.wind_region_name = None
        self.fx_id = -1
        self.unk_x08_x0c = 1.0
        super().__init__(msb_event_source)
        self.set(**kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._wind_region_index = part_indices[self.wind_region_name] if self.wind_region_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.wind_region_name = part_names[self._wind_region_index] if self._wind_region_index != -1 else None


class MSBPatrolRouteEvent(MSBEvent):
    """Defines a patrol route through a sequence of up to 32 regions."""

    EVENT_TYPE_DATA_STRUCT = (
        ("unk_x00_x04", "i"),
        "12x",
        ("_patrol_region_indices", "32h"),
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Probably unused for Patrol Route.",
        ),
        "base_region_name": (
            "Base Region",
            Region,
            "Probably unused for Patrol Route.",
        ),
        "unk_x00_x04": (
            "Unknown [00-04]",
            int,
            "Unknown integer.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Probably unused for Patrol Route.",
        ),
        "patrol_region_names": (
            "Patrol Regions",
            GameObjectSequence((Region, 32)),
            "List of regions that define this Patrol Route."
        )
    }

    ENTRY_SUBTYPE = MSBEventSubtype.PatrolRoute

    def __init__(self, msb_event_source, **kwargs):
        self.unk_x00_x04 = 1.0
        self._patrol_region_names = [None] * 32
        self._patrol_region_indices = [-1] * 32
        super().__init__(msb_event_source)
        self.set(**kwargs)

    @property
    def patrol_region_names(self):
        return self._patrol_region_names

    @patrol_region_names.setter
    def patrol_region_names(self, value):
        """Pads out to 32 names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Patrol point names must be strings or `None`.")
            names.append(v if v else None)
        self._patrol_region_names = value
        while len(self._patrol_region_names) < 32:
            self._patrol_region_names.append(None)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._patrol_region_indices = [region_indices[n] if n else -1 for n in self._patrol_region_names]
        while len(self._patrol_region_indices) < 32:
            self._patrol_region_indices.append(-1)

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self._patrol_region_names = [region_names[i] if i != -1 else None for i in self._patrol_region_indices]
        while len(self._patrol_region_names) < 32:
            self._patrol_region_names.append(None)


class MSBDarkLockEvent(MSBEvent):
    """Unknown purpose. Has no event-specific data."""

    EVENT_TYPE_DATA_STRUCT = (
        "32x",  # no data
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Probably unused for Dark Lock.",
        ),
        "base_region_name": (
            "Base Region",
            Region,
            "Probably unused for Dark Lock.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Probably unused for Dark Lock.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.DarkLock


class MSBPlatoonEvent(MSBEvent):
    """Defines a group (platoon) of enemies."""

    EVENT_TYPE_DATA_STRUCT = (
        ("platoon_id_script_active", "i"),
        ("state", "i"),
        "16x",
        ("_platoon_part_indices", "32i"),
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Probably unused for Dark Lock.",
        ),
        "base_region_name": (
            "Base Region",
            Region,
            "Probably unused for Dark Lock.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Probably unused for Dark Lock.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.Platoon

    def __init__(self, msb_event_source, **kwargs):
        self.platoon_id_script_active = 0
        self.state = 0
        self._platoon_part_names = [None] * 32
        self._platoon_part_indices = [-1] * 32
        super().__init__(msb_event_source)
        self.set(**kwargs)

    @property
    def platoon_part_names(self):
        return self._platoon_part_names

    @platoon_part_names.setter
    def platoon_part_names(self, value):
        """Pads out to 32 names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Patrol point names must be strings or `None`.")
            names.append(v if v else None)
        self._platoon_part_names = value
        while len(self._platoon_part_names) < 32:
            self._platoon_part_names.append(None)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._platoon_part_indices = [part_indices[n] if n else -1 for n in self._platoon_part_names]
        while len(self._platoon_part_indices) < 32:
            self._platoon_part_indices.append(-1)

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self._platoon_part_names = [part_names[i] if i != -1 else None for i in self._platoon_part_indices]
        while len(self._platoon_part_names) < 32:
            self._platoon_part_names.append(None)


class MSBMultiSummonEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("unk_x00_x04", "i"),
        ("unk_x04_x06", "h"),
        ("unk_x06_x08", "h"),
        ("unk_x08_x0a", "h"),
        ("unk_x0a_x0c", "h"),
        "4x",
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Probably unused for Dark Lock.",
        ),
        "base_region_name": (
            "Base Region",
            Region,
            "Probably unused for Dark Lock.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Probably unused for Dark Lock.",
        ),
        "unk_x00_x04": (
            "Unknown [00-04]",
            int,
            "Unknown floating-point number.",
        ),
        "unk_x04_x06": (
            "Unknown [04-06]",
            int,
            "Unknown floating-point number.",
        ),
        "unk_x06_x08": (
            "Unknown [06-08]",
            int,
            "Unknown floating-point number.",
        ),
        "unk_x08_x0a": (
            "Unknown [08-0a]",
            int,
            "Unknown floating-point number.",
        ),
        "unk_x0a_x0c": (
            "Unknown [0a-0c]",
            int,
            "Unknown floating-point number.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.MultiSummon

    def __init__(self, msb_event_source, **kwargs):
        self.unk_x00_x04 = 1.0
        self.unk_x04_x06 = 1.0
        self.unk_x06_x08 = 1.0
        self.unk_x08_x0a = 1.0
        self.unk_x0a_x0c = 1.0
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBSpawnPointEvent(_BaseMSBSpawnPointEvent, MSBEvent):
    pass


class MSBMapOffsetEvent(_BaseMSBMapOffsetEvent, MSBEvent):
    pass


class MSBNavigationEvent(_BaseMSBNavigationEvent, MSBEvent):
    pass


class MSBEnvironmentEvent(_BaseMSBEnvironmentEvent, MSBEvent):
    pass


class MSBOtherEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Other


class MSBEventList(_BaseMSBEventList, MSBEntryList):
    EVENT_SUBTYPE_CLASSES = {
        # MSBEventSubtype.Light: MSBLightEvent,
        MSBEventSubtype.Sound: MSBSoundEvent,
        MSBEventSubtype.FX: MSBFXEvent,
        # MSBEventSubtype.Wind: MSBWindEvent,
        MSBEventSubtype.Treasure: MSBTreasureEvent,
        MSBEventSubtype.Spawner: MSBSpawnerEvent,
        MSBEventSubtype.Message: MSBMessageEvent,
        MSBEventSubtype.ObjAct: MSBObjActEvent,
        MSBEventSubtype.SpawnPoint: MSBSpawnPointEvent,
        MSBEventSubtype.MapOffset: MSBMapOffsetEvent,
        MSBEventSubtype.Navigation: MSBNavigationEvent,
        MSBEventSubtype.Environment: MSBEnvironmentEvent,
        # MSBEventSubtype.PseudoMultiplayer: MSBPseudoMultiplayerEvent,
        MSBEventSubtype.WindFX: MSBWindFXEvent,
        MSBEventSubtype.PatrolRoute: MSBPatrolRouteEvent,
        MSBEventSubtype.DarkLock: MSBDarkLockEvent,
        MSBEventSubtype.Platoon: MSBPlatoonEvent,
        MSBEventSubtype.MultiSummon: MSBMultiSummonEvent,
        MSBEventSubtype.Other: MSBOtherEvent,
    }
    EVENT_SUBTYPE_OFFSET = 12
