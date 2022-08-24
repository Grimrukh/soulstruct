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

import abc
import typing as tp

from soulstruct.bloodborne.events.emevd.enums import SoundType
from soulstruct.bloodborne.game_types import *
from soulstruct.base.maps.msb.events import *
from soulstruct.base.maps.msb.exceptions import MapEventError
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.utilities.binary import BinaryStruct
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import partialmethod

from .enums import MSBEventSubtype
from .msb_entry import MSBEntryList


class MSBEvent(BaseMSBEvent, abc.ABC):
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

    FIELD_INFO = BaseMSBEvent.FIELD_INFO | {
        "entity_id": MapFieldInfo(  # definition overridden when used
            "Entity ID",
            int,
            -1,
            "Entity ID for event. Unused for this event type.",
        ),
        "base_part_name": MapFieldInfo(  # definition overridden when used
            "Base Part Name",
            MapPart,
            None,
            "Map Part name related to event. Unused for this event type.",
        ),
        "base_region_name": MapFieldInfo(  # definition overridden when used
            "Base Region Name",
            Region,
            None,
            "Map Region name related to event. Unused for this event type.",
        ),
    }

    def __init__(self, source=None, **kwargs):
        self._unknowns = [0, 0, 0, 0]
        super().__init__(source=source, **kwargs)


class MSBSoundEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Sound
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("sound_type", "i"),
        ("sound_id", "i"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Sound is connected to this part (usually a Collision or Map Piece part), but this has an unknown effect.",
        ),
        "base_region_name": MapFieldInfo(
            "Sound Volume",
            Region,
            None,
            "Region in which Sound can be heard, if it's enabled.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to the Sound in other game files.",
        ),
        "sound_type": MapFieldInfo(
            "Sound Type",
            SoundType,
            SoundType.m_Music,
            "Type of sound, which is used to find the sound data (sound name prefix letter).",
        ),
        "sound_id": MapFieldInfo(
            "Sound ID",
            int,
            -1,
            "Sound data ID, which refers to an ID in loaded sound events.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "sound_type",
        "sound_id",
    )


class MSBVFXEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.VFX

    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("vfx_id", "i"),
        ("starts_disabled", "i"),  # 32-bit bool
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "VFX will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": MapFieldInfo(
            "VFX Region",
            Region,
            None,
            "Region (usually a Point) at which VFX appears.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to this VFX in other game files.",
        ),
        "vfx_id": MapFieldInfo(
            "VFX ID",
            int,
            0,
            "Visual effect ID, which refers to a loaded VFX file.",
        ),
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

    vfx_id: int
    starts_disabled: bool


class MSBTreasureEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Treasure
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

    FIELD_INFO = {
        "treasure_part_name": MapFieldInfo(
            "Treasure Object",
            Object,
            None,
            "Object on which treasure will appear (usually a corpse or chest).",
        ),
        "item_lot_1": MapFieldInfo(
            "Item Lot 1",
            ItemLotParam,
            -1,
            "First item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_2": MapFieldInfo(
            "Item Lot 2",
            ItemLotParam,
            -1,
            "Second item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_3": MapFieldInfo(
            "Item Lot 3",
            ItemLotParam,
            -1,
            "Third item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "is_in_chest": MapFieldInfo(
            "Is In Chest",
            bool,
            False,
            "Indicates if this treasure is inside a chest (affects appearance).",  # TODO: effect?
        ),
        "is_hidden": MapFieldInfo(
            "Is Hidden",
            bool,
            False,
            "If True, this treasure will start disabled and will need to be enabled manually with an event script.",
        ),
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

    REFERENCE_FIELDS = {"parts": ["base_part_name", "treasure_part_name"], "regions": ["base_region_name"]}

    treasure_part_name: tp.Optional[str]
    item_lot_1: int
    item_lot_2: int
    item_lot_3: int
    is_in_chest: bool
    is_hidden: bool
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

    def __init__(self, source=None, **kwargs):
        self._treasure_part_index = None
        self._treasure_part_name = None
        self.item_lot_1 = -1
        self.item_lot_2 = -1
        self.item_lot_3 = -1
        self.unknown_x1c_x20 = -1
        self.unknown_x20_x24 = -1
        self.unknown_x24_x28 = -1
        self.unknown_x28_x2c = -1
        self.unknown_x2c_x30 = -1
        self.unknown_x30_x34 = -1
        self.unknown_x34_x38 = -1
        self.unknown_x38_x3c = -1
        self.unknown_x3c_x40 = -1
        self.unknown_x42_x44 = -1
        self.unknown_x44_x48 = -1
        self.unknown_x48_x4c = -1
        super().__init__(source=source, **kwargs)

    @property
    def treasure_part_name(self):
        return self._treasure_part_name

    @treasure_part_name.setter
    def treasure_part_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._treasure_part_name = value if value else None
        elif value is None:
            self._treasure_part_name = None
        else:
            raise TypeError(f"`treasure_part_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._treasure_part_index = indices.part_indices[self._treasure_part_name] if self.treasure_part_name else -1

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self._treasure_part_name = (
            names.part_names[self._treasure_part_index] if self._treasure_part_index != -1 else None
        )


class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    ENTRY_SUBTYPE = MSBEventSubtype.Spawner

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

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to the Spawner in other game files.",
        ),
        "max_count": MapFieldInfo(
            "Max Count",
            int,
            255,
            "Unsure; I suspect this is the total number of entities this spawner can produce.",
        ),
        "spawner_type": MapFieldInfo(
            "Spawner Type",
            int,
            0,
            "Unsure what this enumeration is.",
        ),
        "limit_count": MapFieldInfo(
            "Limit Count",
            int,
            -1,
            "Unsure; I suspect this is the number of spawned entities that can be alive at once.",
        ),
        "min_spawner_count": MapFieldInfo(
            "Min Spawner Count",
            int,
            1,
            "Unsure.",
        ),
        "max_spawner_count": MapFieldInfo(
            "Max Spawner Count",
            int,
            1,
            "Unsure.",
        ),
        "min_interval": MapFieldInfo(
            "Min Interval",
            float,
            1.0,
            "Minimum number of seconds between spawns.",
        ),
        "max_interval": MapFieldInfo(
            "Max Interval",
            float,
            1.0,
            "Maximum number of seconds between spawns.",
        ),
        "initial_spawn_count": MapFieldInfo(
            "Initial Spawn Count",
            int,
            1,
            "Unsure; I suspect this is the number of entities spawned immediately on map load.",
        ),
        "spawn_part_names": MapFieldInfo(
            "Spawn Characters",
            GameObjectSequence((Character, 32)),  # TODO: ditto
            [None] * 32,
            "Entities that will be spawned at given regions.",
        ),
        "spawn_region_names": MapFieldInfo(
            "Spawn Regions",
            GameObjectSequence((Region, SPAWN_REGION_COUNT)),
            [None] * SPAWN_REGION_COUNT,
            "Regions where entities will be spawned.",
        ),
    }

    REFERENCE_FIELDS = {
        "parts": ["base_part_name", "spawn_part_names"],
        "regions": ["base_region_name", "spawn_region_names"]
    }

    FIELD_ORDER = (
        "entity_id",
        "max_count",
        "spawner_type",
        "limit_count",
        "min_spawner_count",
        "max_spawner_count",
        "min_interval",
        "max_interval",
        "initial_spawn_count",
        "spawn_part_names",
        "spawn_region_names",
    )

    spawn_region_names: list[tp.Union[str, None]]
    spawn_part_names: list[tp.Union[str, None]]

    def __init__(self, source=None, **kwargs):
        self._spawn_region_indices = [-1] * self.SPAWN_REGION_COUNT
        self._spawn_part_indices = [-1] * 32
        super().__init__(source=source, **kwargs)

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._spawn_region_indices = [indices.region_indices[n] if n else -1 for n in self.spawn_region_names]
        while len(self._spawn_region_indices) < self.SPAWN_REGION_COUNT:
            self._spawn_part_indices.append(-1)
        self._spawn_part_indices = [indices.part_indices[n] if n else -1 for n in self.spawn_part_names]
        while len(self._spawn_part_indices) < 32:
            self._spawn_part_indices.append(-1)

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self.spawn_region_names = [names.region_names[i] if i != -1 else None for i in self._spawn_region_indices]
        while len(self.spawn_region_names) < self.SPAWN_REGION_COUNT:
            self.spawn_region_names.append(None)
        self.spawn_part_names = [names.part_names[i] if i != -1 else None for i in self._spawn_part_indices]
        while len(self.spawn_part_names) < 32:
            self.spawn_part_names.append(None)


class MSBMessageEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Message
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("text_id", "h"),
        ("unk_x02_x04", "h"),
        ("is_hidden", "?"),
        "3x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Message will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": MapFieldInfo(
            "Message Region",
            Region,
            None,
            "Region (usually a Point) at which Message appears.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to the Message in other game files.",
        ),
        "text_id": MapFieldInfo(
            "Message Text ID",
            SoapstoneMessage,
            -1,
            "Soapstone Messages text ID shown when soapstone message is examined.",
        ),
        "unk_x02_x04": MapFieldInfo(
            "Unknown [02-04]",
            int,
            2,
            "Unknown. Often set to 2.",
        ),
        "is_hidden": MapFieldInfo(
            "Is Hidden",
            bool,
            False,
            "If True, the message must be manually enabled with an event script or by using Seek Guidance.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "text_id",
        "unk_x02_x04",
        "is_hidden",
    )

    text_id: int
    unk_x02_x04: int
    is_hidden: bool


class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    ENTRY_SUBTYPE = MSBEventSubtype.ObjAct
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("obj_act_entity_id", "i"),
        ("_obj_act_part_index", "i"),
        ("obj_act_param_id", "i"),
        ("obj_act_state", "B"),
        "3x",
        ("obj_act_flag", "i"),
        "4x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "obj_act_entity_id": MapFieldInfo(
            "ObjAct Entity ID",
            int,
            -1,
            "ID that identifies this object activation event in event scripts.",
        ),
        "obj_act_part_name": MapFieldInfo(
            "Object",
            Object,
            None,
            "Object to which this object activation event is attached.",
        ),
        "obj_act_param_id": MapFieldInfo(
            "ObjAct Param",
            ObjActParam,
            -1,
            "Param entry containing information about this object activation event. If it is -1, it will "
            "default to the model ID of the object it is attached to.",
        ),
        "obj_act_state": MapFieldInfo(
            "ObjAct State",
            int,
            0,
            "State of object activation. Known values include Default (0), Door (1), and Loop (2).",
        ),
        "obj_act_flag": MapFieldInfo(
            "ObjAct Flag",
            Flag,
            0,
            "Flag that stores the persistent state (e.g. open/closed) of this object activation.",
        ),
    }

    FIELD_ORDER = (
        "obj_act_entity_id",
        "obj_act_part_name",
        "obj_act_param_id",
        "obj_act_state",
        "obj_act_flag",
    )

    REFERENCE_FIELDS = {"parts": ["base_part_name", "obj_act_part_name"], "regions": ["base_region_name"]}

    obj_act_entity_id: int
    obj_act_part_name: tp.Optional[str]
    obj_act_param_id: int
    obj_act_state: int
    obj_act_flag: int

    def __init__(self, source=None, **kwargs):
        self._obj_act_part_index = None
        self._obj_act_part_name = None
        super().__init__(source=source, **kwargs)

    @property
    def obj_act_part_name(self):
        return self._obj_act_part_name

    @obj_act_part_name.setter
    def obj_act_part_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._obj_act_part_name = value if value else None
        elif value is None:
            self._obj_act_part_name = None
        else:
            raise TypeError(f"`obj_act_part_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._obj_act_part_index = indices.part_indices[self._obj_act_part_name] if self.obj_act_part_name else -1

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self._obj_act_part_name = names.part_names[self._obj_act_part_index] if self._obj_act_part_index != -1 else None


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

    REFERENCE_FIELDS = {"parts": ["base_part_name"], "regions": ["base_region_name", "wind_region_name"]}

    wind_region_name: tp.Optional[str]
    vfx_id: int
    unk_x08_x0c: float

    def __init__(self, source, **kwargs):
        self._wind_region_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._wind_region_index = indices.part_indices[self.wind_region_name] if self.wind_region_name else -1

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self.wind_region_name = names.part_names[self._wind_region_index] if self._wind_region_index != -1 else None


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

    REFERENCE_FIELDS = {"parts": ["base_part_name"], "regions": ["base_region_name", "patrol_region_names"]}

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

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._patrol_region_indices = [indices.region_indices[n] if n else -1 for n in self._patrol_region_names]
        while len(self._patrol_region_indices) < 32:
            self._patrol_region_indices.append(-1)

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self._patrol_region_names = [names.region_names[i] if i != -1 else None for i in self._patrol_region_indices]
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

    REFERENCE_FIELDS = {
        "parts": ["base_part_name", "platoon_character_names", "platoon_parent_names"],
        "regions": ["base_region_name"]
    }

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

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        self._platoon_character_indices = [indices.part_indices[n] if n else -1 for n in self._platoon_character_names]
        while len(self._platoon_character_indices) < 30:
            self._platoon_character_indices.append(-1)
        self._platoon_parent_indices = [indices.part_indices[n] if n else -1 for n in self._platoon_parent_names]
        while len(self._platoon_parent_indices) < 2:
            self._platoon_parent_indices.append(-1)

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        self._platoon_character_names = [
            names.part_names[i] if i != -1 else None for i in self._platoon_character_indices
        ]
        while len(self._platoon_character_names) < 30:
            self._platoon_character_names.append(None)
        self._platoon_parent_names = [names.part_names[i] if i != -1 else None for i in self._platoon_parent_indices]
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


class MSBSpawnPointEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.SpawnPoint
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("_spawn_point_region_index", "i"),
        "12x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Some Spawn Points use this; unclear what it does, but it is presumably the Collision of the Spawn Point.",
        ),
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to the Spawn Point in other game files.",
        ),
        "spawn_point_region_name": MapFieldInfo(
            "Spawn Point Region",
            Region,
            None,
            "Region where player will spawn when registered to this spawn point.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "spawn_point_region_name",
    )

    REFERENCE_FIELDS = {"parts": ["base_part_name"], "regions": ["base_region_name", "spawn_point_region_name"]}

    spawn_point_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._spawn_point_region_index = None
        self._spawn_point_region_name = None
        super().__init__(source=source, **kwargs)

    @property
    def spawn_point_region_name(self):
        return self._spawn_point_region_name

    @spawn_point_region_name.setter
    def spawn_point_region_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._spawn_point_region_name = value if value else None
        elif value is None:
            self._spawn_point_region_name = None
        else:
            raise TypeError(f"`spawn_point_region_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        if self.spawn_point_region_name:
            self._spawn_point_region_index = indices.region_indices[self._spawn_point_region_name]
        else:
            self._spawn_point_region_index = -1

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        if self._spawn_point_region_index != -1:
            self._spawn_point_region_name = names.region_names[self._spawn_point_region_index]
        else:
            self._spawn_point_region_name = None


class MSBMapOffsetEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.MapOffset
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("translate", "3f"),
        ("rotate_y", "f"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "translate": MapFieldInfo(
            "Translate",
            Vector3,
            Vector3.zero(),
            "Vector of (x, y, z) coordinates of map offset.",
        ),
        "rotate_y": MapFieldInfo(
            "Y Rotation",
            float,
            0.0,
            "Euler angle of rotation around the Y (vertical) axis.",
        ),
    }

    FIELD_ORDER = (
        "translate",
        "rotate_y",
    )

    translate: Vector3
    rotate_y: float

    def __init__(self, source=None, **kwargs):
        self._translate = Vector3.zero()
        super().__init__(source=source, **kwargs)

    @property
    def translate(self):
        return self._translate

    @translate.setter
    def translate(self, value):
        self._translate = Vector3(value)


class MSBNavigationEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Navigation
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("_navigation_region_index", "i"),
        "12x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to the Navigation event in other game files.",
        ),
        "navigation_region_name": MapFieldInfo(
            "Navmesh Region",
            Region,
            None,
            "Region to which Navigation event is attached, which encloses faces of one or more Navmesh parts.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "navigation_region_name",
    )

    REFERENCE_FIELDS = {"parts": ["base_part_name"], "regions": ["base_region_name", "navigation_region_name"]}

    navigation_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._navigation_region_index = None
        self._navigation_region_name = None
        super().__init__(source=source, **kwargs)

    @property
    def navigation_region_name(self):
        return self._navigation_region_name

    @navigation_region_name.setter
    def navigation_region_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._navigation_region_name = value if value else None
        elif value is None:
            self._navigation_region_name = None
        else:
            raise TypeError(f"`navigation_region_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: EventsIndicesData):
        super().set_indices(indices)
        if self.navigation_region_name:
            self._navigation_region_index = indices.region_indices[self._navigation_region_name]
        else:
            self._navigation_region_index = -1

    def set_names(self, names: EventsNamesData):
        super().set_names(names)
        if self._navigation_region_index != -1:
            self._navigation_region_name = names.region_names[self._navigation_region_index]
        else:
            self._navigation_region_name = None


class MSBEnvironmentEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Environment
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("unk_x00_x04", "i"),
        ("unk_x04_x08", "f"),
        ("unk_x08_x0c", "f"),
        ("unk_x0c_x10", "f"),
        ("unk_x10_x14", "f"),
        ("unk_x14_x18", "f"),
        "8x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Environment (or 'map spot') will be drawn whenever its parent is drawn.",
        ),
        "base_region_name": MapFieldInfo(
            "Environment Region",
            Region,
            None,
            "Region (usually a Point) at which Environment appears (whatever that means).",
        ),
        "entity_id": MapFieldInfo(
            "Environment ID",
            int,
            -1,
            "Unknown index. Note that this replaces the usual Entity ID field.",
        ),
        "unk_x00_x04": MapFieldInfo(
            "Unknown [00-04]",
            int,
            0,
            "Unknown Environment parameter (integer).",
        ),
        "unk_x04_x08": MapFieldInfo(
            "Unknown [04-08]",
            float,
            1.0,
            "Unknown Environment parameter (floating-point number).",
        ),
        "unk_x08_x0c": MapFieldInfo(
            "Unknown [08-0c]",
            float,
            1.0,
            "Unknown Environment parameter (floating-point number).",
        ),
        "unk_x0c_x10": MapFieldInfo(
            "Unknown [0c-10]",
            float,
            1.0,
            "Unknown Environment parameter (floating-point number).",
        ),
        "unk_x10_x14": MapFieldInfo(
            "Unknown [10-14]",
            float,
            1.0,
            "Unknown Environment parameter (floating-point number).",
        ),
        "unk_x14_x18": MapFieldInfo(
            "Unknown [14-18]",
            float,
            1.0,
            "Unknown Environment parameter (floating-point number).",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "unk_x00_x04",
        "unk_x04_x08",
        "unk_x08_x0c",
        "unk_x0c_x10",
        "unk_x10_x14",
        "unk_x14_x18",
    )

    unk_x00_x04: int
    unk_x04_x08: float
    unk_x08_x0c: float
    unk_x0c_x10: float
    unk_x10_x14: float
    unk_x14_x18: float


class MSBOtherEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = BinaryStruct()
    ENTRY_SUBTYPE = MSBEventSubtype.Other


class MSBEventList(BaseMSBEventList, MSBEntryList[MSBEvent]):
    INTERNAL_NAME = "EVENT_PARAM_ST"
    ENTRY_LIST_NAME = "Events"
    ENTRY_SUBTYPE_ENUM = MSBEventSubtype

    SUBTYPE_CLASSES = {
        MSBEventSubtype.Sound: MSBSoundEvent,
        MSBEventSubtype.VFX: MSBVFXEvent,
        MSBEventSubtype.Treasure: MSBTreasureEvent,
        MSBEventSubtype.Spawner: MSBSpawnerEvent,
        MSBEventSubtype.Message: MSBMessageEvent,
        MSBEventSubtype.ObjAct: MSBObjActEvent,
        MSBEventSubtype.SpawnPoint: MSBSpawnPointEvent,
        MSBEventSubtype.MapOffset: MSBMapOffsetEvent,
        MSBEventSubtype.Navigation: MSBNavigationEvent,
        MSBEventSubtype.Environment: MSBEnvironmentEvent,
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

    _entries: list[MSBEvent]

    new = MSBEntryList.new
    new_sound: tp.Callable[..., MSBSoundEvent] = partialmethod(new, MSBEventSubtype.Sound)
    new_vfx: tp.Callable[..., MSBVFXEvent] = partialmethod(new, MSBEventSubtype.VFX)
    new_treasure: tp.Callable[..., MSBTreasureEvent] = partialmethod(new, MSBEventSubtype.Treasure)
    new_spawner: tp.Callable[..., MSBSpawnerEvent] = partialmethod(new, MSBEventSubtype.Spawner)
    new_message: tp.Callable[..., MSBMessageEvent] = partialmethod(new, MSBEventSubtype.Message)
    new_obj_act: tp.Callable[..., MSBObjActEvent] = partialmethod(new, MSBEventSubtype.ObjAct)
    new_spawn_point: tp.Callable[..., MSBSpawnPointEvent] = partialmethod(new, MSBEventSubtype.SpawnPoint)
    new_map_offset: tp.Callable[..., MSBMapOffsetEvent] = partialmethod(new, MSBEventSubtype.MapOffset)
    new_navigation: tp.Callable[..., MSBNavigationEvent] = partialmethod(new, MSBEventSubtype.Navigation)
    new_environment: tp.Callable[..., MSBEnvironmentEvent] = partialmethod(new, MSBEventSubtype.Environment)
    new_wind_vfx: tp.Callable[..., MSBWindVFXEvent] = partialmethod(new, MSBEventSubtype.WindVFX)
    new_patrol_route: tp.Callable[..., MSBPatrolRouteEvent] = partialmethod(new, MSBEventSubtype.PatrolRoute)
    new_dark_lock: tp.Callable[..., MSBDarkLockEvent] = partialmethod(new, MSBEventSubtype.DarkLock)
    new_multi_summon: tp.Callable[..., MSBMultiSummonEvent] = partialmethod(new, MSBEventSubtype.MultiSummon)
    new_other: tp.Callable[..., MSBOtherEvent] = partialmethod(new, MSBEventSubtype.Other)

    def pack_entry(self, index: int, entry: MSBEvent):
        return entry.pack()

    def set_indices(self, region_indices, part_indices):
        """Global and subtype-specific indices both set. (Unclear if either of them do anything.)"""
        subtype_indices = {}
        for i, entry in enumerate(self._entries):
            try:
                indices = EventsIndicesData(
                    event_index=i,
                    local_event_index=subtype_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    region_indices=region_indices,
                    part_indices=part_indices,
                )
                entry.set_indices(indices)
            except KeyError as e:
                raise MapEventError(
                    f"Invalid map component name for {entry.ENTRY_SUBTYPE.name} event '{entry.name}': {e}"
                )
            else:
                subtype_indices[entry.ENTRY_SUBTYPE] += 1

    def set_names(self, region_names, part_names):
        for entry in self._entries:
            names = EventsNamesData(region_names, part_names)
            entry.set_names(names)


for _entry_subtype in iter(MSBEventList.ENTRY_SUBTYPE_ENUM):
    setattr(
        MSBEventList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
