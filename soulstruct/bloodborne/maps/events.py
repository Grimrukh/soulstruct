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
    "MSBEventList",
]

import typing as tp

from soulstruct.game_types import *
from soulstruct.base.maps.msb.events import (
    MSBEvent as _BaseMSBEvent,
    MSBEventList as _BaseMSBEventList,
    MSBSoundEvent as _BaseMSBSoundEvent,
    MSBVFXEvent as _BaseMSBVFXEvent,
    MSBMessageEvent as _BaseMSBMessageEvent,
    MSBTreasureEvent as _BaseMSBTreasureEvent,
    MSBSpawnerEvent as _BaseMSBSpawnerEvent,
    MSBObjActEvent as _BaseMSBObjActEvent,
    MSBSpawnPointEvent as _BaseMSBSpawnPointEvent,
    MSBMapOffsetEvent as _BaseMSBMapOffsetEvent,
    MSBNavigationEvent as _BaseMSBNavigationEvent,
    MSBEnvironmentEvent as _BaseMSBEnvironmentEvent,
)
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.base.maps.msb.enums import MSBEventSubtype
from soulstruct.utilities.binary_struct import BinaryStruct

from .msb_entry import MSBEntryList
from soulstruct.utilities import partialmethod


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

    def __init__(self, source=None, **kwargs):
        self._unknowns = [0, 0, 0, 0]
        super().__init__(source=source, **kwargs)


class MSBSoundEvent(_BaseMSBSoundEvent, MSBEvent):
    pass


class MSBVFXEvent(_BaseMSBVFXEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("vfx_id", "i"),
        ("starts_disabled", "i"),  # 32-bit bool
    )

    FIELD_INFO = _BaseMSBVFXEvent.FIELD_INFO | {
        "starts_disabled": MapFieldInfo(
            "Starts Disabled",
            bool,
            False,
            "VFX will not be automatically created on map load (requires event script).",
        )
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "vfx_id",
        "starts_disabled",
    )


class MSBTreasureEvent(_BaseMSBTreasureEvent, MSBEvent):
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
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
        ("is_in_chest", "?"),
        ("is_hidden", "?"),
        ("unknown_x42_x44", "h"),
        ("unknown_x44_x48", "i"),
        ("unknown_x48_x4c", "i"),
        "4x",
    )

    FIELD_INFO = _BaseMSBTreasureEvent.FIELD_INFO | {
        "unknown_x1c_x20": MapFieldInfo(
            "Unknown [1c-20]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x20_x24": MapFieldInfo(
            "Unknown [20-24]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x24_x28": MapFieldInfo(
            "Unknown [24-28]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x28_x2c": MapFieldInfo(
            "Unknown [28-2c]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x2c_x30": MapFieldInfo(
            "Unknown [2c-30]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x30_x34": MapFieldInfo(
            "Unknown [30-34]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x34_x38": MapFieldInfo(
            "Unknown [34-38]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x38_x3c": MapFieldInfo(
            "Unknown [38-3c]",
            int,
            0,
            "Unknown integer.",
        ),
        "unknown_x3c_x40": MapFieldInfo(
            "Unknown [3c-40]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x42_x44": MapFieldInfo(
            "Unknown [42-44]",
            int,
            0,
            "Unknown short.",
        ),
        "unknown_x44_x48": MapFieldInfo(
            "Unknown [44-48]",
            int,
            -1,
            "Unknown integer.",
        ),
        "unknown_x48_x4c": MapFieldInfo(
            "Unknown [48-4c]",
            int,
            -1,
            "Unknown integer.",
        ),
    }

    FIELD_ORDER = (
        "treasure_part_name",
        "item_lot_1",
        "item_lot_2",
        "item_lot_3",
        "is_in_chest",
        "is_hidden",
        "unknown_x1c_x20",
        "unknown_x20_x24",
        "unknown_x24_x28",
        "unknown_x28_x2c",
        "unknown_x2c_x30",
        "unknown_x30_x34",
        "unknown_x34_x38",
        "unknown_x38_x3c",
        "unknown_x3c_x40",
        "unknown_x42_x44",
        "unknown_x44_x48",
        "unknown_x48_x4c",
    )

    unknown_x1c_x20: int
    unknown_x20_x24: int
    unknown_x24_x28: int
    unknown_x28_x2c: int
    unknown_x2c_x30: int
    unknown_x30_x34: int
    unknown_x34_x38: int
    unknown_x38_x3c: int
    unknown_x3c_x40: int
    unknown_x42_x44: int
    unknown_x44_x48: int
    unknown_x48_x4c: int


class MSBSpawnerEvent(_BaseMSBSpawnerEvent, MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
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
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("obj_act_entity_id", "i"),
        ("_obj_act_part_index", "i"),
        ("obj_act_param_id", "i"),
        ("obj_act_state", "B"),
        "3x",
        ("obj_act_flag", "i"),
        "4x",
    )


class MSBWindVFXEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.WindVFX
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("vfx_id", "i"),
        ("_wind_region_index", "i"),
        ("unk_x08_x0c", "f"),
        "4x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "VFX will be drawn if this parent (usually a Collision or Map Piece part) is drawn. Possibly unused.",
        ),
        "base_region_name": MapFieldInfo(
            "Base Region",
            Region,
            None,
            "Base event region. Probably unused with WindVFX (see Wind Region Name instead).",
        ),
        "wind_region_name": MapFieldInfo(
            "VFX Region",
            Region,
            None,
            "Region at or in which WindVFX appears.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to this VFX in other game files. Possibly unused with WindVFX.",
        ),
        "vfx_id": MapFieldInfo(
            "VFX ID",
            int,
            -1,
            "Visual effect ID, which refers to a loaded VFX file.",
        ),
        "unk_x08_x0c": MapFieldInfo(
            "Unknown [08-0c]",
            float,
            1.0,
            "Unknown floating-point number.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "vfx_id",
        "unk_x08_x0c",
    )

    wind_region_name: tp.Optional[str]
    vfx_id: int
    unk_x08_x0c: float

    def __init__(self, source, **kwargs):
        self._wind_region_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._wind_region_index = part_indices[self.wind_region_name] if self.wind_region_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.wind_region_name = part_names[self._wind_region_index] if self._wind_region_index != -1 else None


class MSBPatrolRouteEvent(MSBEvent):
    """Defines a patrol route through a sequence of up to 32 regions."""

    ENTRY_SUBTYPE = MSBEventSubtype.PatrolRoute
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("unk_x00_x04", "i"),
        "12x",
        ("_patrol_region_indices", "32h"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Probably unused for Patrol Route.",
        ),
        "base_region_name": MapFieldInfo(
            "Base Region",
            Region,
            None,
            "Probably unused for Patrol Route.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Probably unused for Patrol Route.",
        ),
        "unk_x00_x04": MapFieldInfo(
            "Unknown [00-04]",
            int,
            1,
            "Unknown integer.",
        ),
        "patrol_region_names": MapFieldInfo(
            "Patrol Regions",
            GameObjectSequence((Region, 32)),
            [None] * 32,
            "List of regions that define this Patrol Route."
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "unk_x00_x04",
        "patrol_region_names",
    )

    unk_x00_x04: int

    def __init__(self, source, **kwargs):
        self._patrol_region_names = [None] * 32
        self._patrol_region_indices = [-1] * 32
        super().__init__(source=source, **kwargs)

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

    ENTRY_SUBTYPE = MSBEventSubtype.DarkLock
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        "32x",  # no data
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Probably unused for Dark Lock.",
        ),
        "base_region_name": MapFieldInfo(
            "Base Region",
            Region,
            None,
            "Probably unused for Dark Lock.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Probably unused for Dark Lock.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
    )


class MSBPlatoonEvent(MSBEvent):
    """Defines a group (platoon) of enemies."""

    ENTRY_SUBTYPE = MSBEventSubtype.Platoon
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("platoon_id_script_active", "i"),
        ("state", "i"),
        "16x",
        ("_platoon_character_indices", "30i"),
        ("_platoon_parent_indices", "2i"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Probably unused for Platoon.",
        ),
        "base_region_name": MapFieldInfo(
            "Base Region",
            Region,
            None,
            "Probably unused for Platoon.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Probably unused for Platoon.",
        ),
        "platoon_character_names": MapFieldInfo(
            "Platoon Character Names",
            GameObjectSequence((Character, 30)),
            [None] * 30,
            "Characters in this Platoon.",
        ),
        "platoon_parent_names": MapFieldInfo(
            "Platoon Parent Names",
            GameObjectSequence((MapPart, 2)),
            [None] * 2,
            "Parent parts of this Platoon.",
        ),
        "platoon_id_script_active": MapFieldInfo(
            "Platoon Active Script ID",
            int,
            -1,
            "Unknown. Possibly an AI param ID.",
        ),
        "state": MapFieldInfo(
            "Platoon State",
            int,
            -1,
            "Unknown.",
        )
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "platoon_character_names",
        "platoon_parent_names",
        "platoon_id_script_active",
        "state",
    )

    def __init__(self, source, **kwargs):
        self._platoon_character_names = [None] * 30
        self._platoon_character_indices = [-1] * 30
        self._platoon_parent_names = [None] * 2
        self._platoon_parent_indices = [-1] * 2
        super().__init__(source=source, **kwargs)

    @property
    def platoon_character_names(self):
        return self._platoon_character_names

    @platoon_character_names.setter
    def platoon_character_names(self, value):
        """Pads out to 30 names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Platoon character names must be strings or `None`.")
            names.append(v if v else None)
        self._platoon_character_names = value
        while len(self._platoon_character_names) < 30:
            self._platoon_character_names.append(None)

    @property
    def platoon_parent_names(self):
        return self._platoon_parent_names

    @platoon_parent_names.setter
    def platoon_parent_names(self, value):
        """Pads out to 2 names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Platoon parent names must be strings or `None`.")
            names.append(v if v else None)
        self._platoon_parent_names = value
        while len(self._platoon_parent_names) < 2:
            self._platoon_parent_names.append(None)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._platoon_character_indices = [part_indices[n] if n else -1 for n in self._platoon_character_names]
        while len(self._platoon_character_indices) < 30:
            self._platoon_character_indices.append(-1)
        self._platoon_parent_indices = [part_indices[n] if n else -1 for n in self._platoon_parent_names]
        while len(self._platoon_parent_indices) < 2:
            self._platoon_parent_indices.append(-1)

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self._platoon_character_names = [part_names[i] if i != -1 else None for i in self._platoon_character_indices]
        while len(self._platoon_character_names) < 30:
            self._platoon_character_names.append(None)
        self._platoon_parent_names = [part_names[i] if i != -1 else None for i in self._platoon_parent_indices]
        while len(self._platoon_parent_names) < 2:
            self._platoon_parent_names.append(None)


class MSBMultiSummonEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.MultiSummon
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("unk_x00_x04", "i"),
        ("unk_x04_x06", "h"),
        ("unk_x06_x08", "h"),
        ("unk_x08_x0a", "h"),
        ("unk_x0a_x0c", "h"),
        "4x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Probably unused for Multi Summon.",
        ),
        "base_region_name": MapFieldInfo(
            "Base Region",
            Region,
            None,
            "Probably unused for Multi Summon.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Probably unused for Multi Summon.",
        ),
        "unk_x00_x04": MapFieldInfo(
            "Unknown [00-04]",
            int,
            1,
            "Unknown integer.",
        ),
        "unk_x04_x06": MapFieldInfo(
            "Unknown [04-06]",
            int,
            1,
            "Unknown 16-bit integer.",
        ),
        "unk_x06_x08": MapFieldInfo(
            "Unknown [06-08]",
            int,
            1,
            "Unknown 16-bit integer.",
        ),
        "unk_x08_x0a": MapFieldInfo(
            "Unknown [08-0a]",
            int,
            1,
            "Unknown 16-bit integer.",
        ),
        "unk_x0a_x0c": MapFieldInfo(
            "Unknown [0a-0c]",
            int,
            1,
            "Unknown 16-bit integer.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "unk_x00_x04",
        "unk_x04_x06",
        "unk_x06_x08",
        "unk_x08_x0a",
        "unk_x0a_x0c",
    )

    unk_x00_x04: int
    unk_x04_x06: int
    unk_x06_x08: int
    unk_x08_x0a: int
    unk_x0a_x0c: int


class MSBSpawnPointEvent(_BaseMSBSpawnPointEvent, MSBEvent):
    pass


class MSBMapOffsetEvent(_BaseMSBMapOffsetEvent, MSBEvent):
    pass


class MSBNavigationEvent(_BaseMSBNavigationEvent, MSBEvent):
    pass


class MSBEnvironmentEvent(_BaseMSBEnvironmentEvent, MSBEvent):
    pass


class MSBOtherEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = BinaryStruct()
    ENTRY_SUBTYPE = MSBEventSubtype.Other


class MSBEventList(_BaseMSBEventList, MSBEntryList):
    SUBTYPE_CLASSES = {
        # MSBEventSubtype.Light: MSBLightEvent,
        MSBEventSubtype.Sound: MSBSoundEvent,
        MSBEventSubtype.VFX: MSBVFXEvent,
        # MSBEventSubtype.Wind: MSBWindEvent,
        MSBEventSubtype.Treasure: MSBTreasureEvent,
        MSBEventSubtype.Spawner: MSBSpawnerEvent,
        MSBEventSubtype.Message: MSBMessageEvent,
        MSBEventSubtype.ObjAct: MSBObjActEvent,
        MSBEventSubtype.SpawnPoint: MSBSpawnPointEvent,
        MSBEventSubtype.MapOffset: MSBMapOffsetEvent,
        MSBEventSubtype.Navigation: MSBNavigationEvent,
        MSBEventSubtype.Environment: MSBEnvironmentEvent,
        # MSBEventSubtype.NPCInvasion: MSBNPCInvasionEvent,
        MSBEventSubtype.WindVFX: MSBWindVFXEvent,
        MSBEventSubtype.PatrolRoute: MSBPatrolRouteEvent,
        MSBEventSubtype.DarkLock: MSBDarkLockEvent,
        MSBEventSubtype.Platoon: MSBPlatoonEvent,
        MSBEventSubtype.MultiSummon: MSBMultiSummonEvent,
        MSBEventSubtype.Other: MSBOtherEvent,
    }
    SUBTYPE_OFFSET = 12

    Sounds: tp.Sequence[MSBSoundEvent]
    VFX: tp.Sequence[MSBVFXEvent]
    Treasure: tp.Sequence[MSBTreasureEvent]
    Spawners: tp.Sequence[MSBSpawnerEvent]
    Messages: tp.Sequence[MSBMessageEvent]
    ObjActs: tp.Sequence[MSBObjActEvent]
    SpawnPoints: tp.Sequence[MSBSpawnPointEvent]
    MapOffsets: tp.Sequence[MSBMapOffsetEvent]
    Navigation: tp.Sequence[MSBNavigationEvent]
    Environment: tp.Sequence[MSBEnvironmentEvent]
    WindVFX: tp.Sequence[MSBWindVFXEvent]
    PatrolRoutes: tp.Sequence[MSBPatrolRouteEvent]
    DarkLocks: tp.Sequence[MSBDarkLockEvent]
    MultiSummons: tp.Sequence[MSBMultiSummonEvent]
    Other: tp.Sequence[MSBOtherEvent]

    new = _BaseMSBEventList.new
    new_sound: tp.Callable[..., MSBSoundEvent]
    new_vfx: tp.Callable[..., MSBVFXEvent]
    new_treasure: tp.Callable[..., MSBTreasureEvent]
    new_spawner: tp.Callable[..., MSBSpawnerEvent]
    new_message: tp.Callable[..., MSBMessageEvent]
    new_obj_act: tp.Callable[..., MSBObjActEvent]
    new_spawn_point: tp.Callable[..., MSBSpawnPointEvent]
    new_map_offset: tp.Callable[..., MSBMapOffsetEvent]
    new_navigation: tp.Callable[..., MSBNavigationEvent]
    new_environment: tp.Callable[..., MSBEnvironmentEvent]
    new_wind_vfx: tp.Callable[..., MSBWindVFXEvent] = partialmethod(new, MSBEventSubtype.WindVFX)
    new_patrol_route: tp.Callable[..., MSBPatrolRouteEvent] = partialmethod(new, MSBEventSubtype.PatrolRoute)
    new_dark_lock: tp.Callable[..., MSBDarkLockEvent] = partialmethod(new, MSBEventSubtype.DarkLock)
    new_multi_summon: tp.Callable[..., MSBMultiSummonEvent] = partialmethod(new, MSBEventSubtype.MultiSummon)
    new_other: tp.Callable[..., MSBOtherEvent] = partialmethod(new, MSBEventSubtype.Other)
