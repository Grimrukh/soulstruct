import abc
import typing as tp

from soulstruct.base.events.emevd.enums import SoundType
from soulstruct.game_types import *
from soulstruct.utilities import read_chars_from_buffer, pad_chars, partialmethod
from soulstruct.utilities.binary_struct import BinaryStruct
from soulstruct.utilities.maths import Vector3

from .enums import MSBEventSubtype
from .exceptions import MapEventError
from .msb_entry import MSBEntryList, MSBEntryEntity
from .utils import MapFieldInfo


class MSBEvent(MSBEntryEntity, abc.ABC):
    """Parent class for MSB events, which describe various things that occur in maps (often attached to Regions)."""

    ENTRY_SUBTYPE: MSBEventSubtype = None
    EVENT_HEADER_STRUCT: BinaryStruct = None
    EVENT_BASE_DATA_STRUCT: BinaryStruct = None
    EVENT_TYPE_DATA_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""

    FIELD_INFO = MSBEntryEntity.FIELD_INFO | {
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

    base_part_name: tp.Optional[str]
    base_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._event_index = None  # global index
        self._local_event_index = None  # local type index
        self._base_part_index = None
        self._base_region_index = None
        super().__init__(source=source, **kwargs)

    def unpack(self, msb_buffer):
        event_offset = msb_buffer.tell()
        header = self.EVENT_HEADER_STRUCT.unpack(msb_buffer)
        if header["__event_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected MSB event type value {header['__event_type']} for {self.__class__.__name__}.")
        msb_buffer.seek(event_offset + header["__base_data_offset"])
        base_data = self.EVENT_BASE_DATA_STRUCT.unpack(msb_buffer)
        name_offset = event_offset + header["__name_offset"]
        self.name = read_chars_from_buffer(msb_buffer, offset=name_offset, encoding=self.NAME_ENCODING)
        self.set(**header)
        self.set(**base_data)
        msb_buffer.seek(event_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_buffer)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        self._event_index = event_index  # TODO: confirm this can safely be handled automatically.
        self._local_event_index = local_event_index
        self._base_part_index = part_indices[self.base_part_name] if self.base_part_name else -1
        self._base_region_index = region_indices[self.base_region_name] if self.base_region_name else -1

    def set_names(self, region_names, part_names):
        self.base_part_name = part_names[self._base_part_index] if self._base_part_index != -1 else None
        self.base_region_name = region_names[self._base_region_index] if self._base_region_index != -1 else None

    def pack(self):
        name_offset = self.EVENT_HEADER_STRUCT.size
        packed_name = pad_chars(self.get_name_to_pack(), encoding=self.NAME_ENCODING, pad_to_multiple_of=4)
        base_data_offset = name_offset + len(packed_name)
        packed_base_data = self.EVENT_BASE_DATA_STRUCT.pack_from_object(self)
        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()
        packed_header = self.EVENT_HEADER_STRUCT.pack(
            __name_offset=name_offset,
            _event_index=self._event_index,
            __event_type=self.ENTRY_SUBTYPE,
            _local_event_index=self._local_event_index,
            __base_data_offset=base_data_offset,
            __type_data_offset=type_data_offset,
        )
        return packed_header + packed_name + packed_base_data + packed_type_data

    def unpack_type_data(self, msb_buffer):
        self.set(**self.EVENT_TYPE_DATA_STRUCT.unpack(msb_buffer, include_asserted=False))

    def pack_type_data(self):
        return self.EVENT_TYPE_DATA_STRUCT.pack_from_object(self)


class MSBLightEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Light
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("point_light_id", "i"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_part_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Light will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": MapFieldInfo(
            "Light Region",
            Region,
            None,
            "Region (usually a Point) at which Light appears.",
        ),
        "point_light_id": MapFieldInfo(
            "Point Light",
            PointLightParam,
            0,
            "Point Light lighting parameter ID to use for this light.",
        ),
    }

    FIELD_ORDER = (
        "base_part_name",
        "base_region_name",
        "point_light_id",
    )


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
            Sound,
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
    }

    FIELD_ORDER = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "vfx_id",
    )

    vfx_id: int


class MSBWindEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Wind
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("wind_vector_min", "3f"),
        ("unk_x04_x08", "f"),
        ("wind_vector_max", "3f"),
        ("unk_x0c_x10", "f"),
        ("wind_swing_cycles", "4f"),
        ("wind_swing_powers", "4f"),
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "wind_vector_min": MapFieldInfo(
            "Wind Vector Min",
            Vector3,
            Vector3.zero(),
            "Wind vector minimum.",
        ),
        "unk_x04_x08": MapFieldInfo(
            "Unknown [04-08]",
            float,
            0.0,
            "Unknown Wind parameter (floating-point number).",
        ),
        "wind_vector_max": MapFieldInfo(
            "Wind Vector Max",
            Vector3,
            Vector3.zero(),
            "Wind vector maximum.",
        ),
        "unk_x0c_x10": MapFieldInfo(
            "Unknown [0c-10]",
            float,
            0.0,
            "Unknown Wind parameter (floating-point number).",
        ),
        "wind_swing_cycles": MapFieldInfo(
            "Wind Swing Cycles",
            list,
            [0.0, 0.0, 0.0, 0.0],
            "Wind swing cycles (four values).",
        ),
        "wind_swing_powers": MapFieldInfo(
            "Wind Swing Powers",
            list,
            [0.0, 0.0, 0.0, 0.0],
            "Wind swing powers (four values).",
        ),
    }

    FIELD_ORDER = (
        "wind_vector_min",
        "unk_x04_x08",
        "wind_vector_max",
        "unk_x0c_x10",
        "wind_swing_cycles",
        "wind_swing_powers",
    )

    unk_x04_x08: float
    unk_x0c_x10: float

    def __init__(self, source=None, **kwargs):
        """Most of these floats have been mapped out."""
        self._wind_vector_min = Vector3.zero()
        self._wind_vector_max = Vector3.zero()
        self._wind_swing_cycles = [0.0, 0.0, 0.0, 0.0]
        self._wind_swing_powers = [0.0, 0.0, 0.0, 0.0]
        super().__init__(source=source, **kwargs)

    @property
    def wind_vector_min(self):
        return self._wind_vector_min

    @wind_vector_min.setter
    def wind_vector_min(self, value):
        self._wind_vector_min = Vector3(value)

    @property
    def wind_vector_max(self):
        return self._wind_vector_max

    @wind_vector_max.setter
    def wind_vector_max(self, value):
        self._wind_vector_max = Vector3(value)

    @property
    def wind_swing_cycles(self):
        return self._wind_swing_cycles

    @wind_swing_cycles.setter
    def wind_swing_cycles(self, value):
        try:
            value = list(value)
            if not len(value) == 4 or not all(isinstance(v, (int, float)) for v in value):
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError(f"`wind_swing_cycles` must be a sequence of four numbers.")
        self._wind_swing_cycles = value

    @property
    def wind_swing_powers(self):
        return self._wind_swing_powers

    @wind_swing_powers.setter
    def wind_swing_powers(self, value):
        try:
            value = list(value)
            if not len(value) == 4 or not all(isinstance(v, (int, float)) for v in value):
                raise ValueError
        except (TypeError, ValueError):
            raise ValueError(f"`wind_swing_powers` must be a sequence of four numbers.")
        self._wind_swing_powers = value


class MSBTreasureEvent(MSBEvent, abc.ABC):
    ENTRY_SUBTYPE = MSBEventSubtype.Treasure
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

    FIELD_INFO = MSBEvent.FIELD_INFO | {
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
    }

    FIELD_ORDER = (
        "treasure_part_name",
        "item_lot_1",
        "item_lot_2",
        "item_lot_3",
        "is_in_chest",
        "is_hidden",
    )

    treasure_part_name: tp.Optional[str]
    item_lot_1: int
    item_lot_2: int
    item_lot_3: int
    is_in_chest: bool
    is_hidden: bool

    def __init__(self, source=None, **kwargs):
        self._treasure_part_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._treasure_part_index = part_indices[self.treasure_part_name] if self.treasure_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.treasure_part_name = part_names[self._treasure_part_index] if self._treasure_part_index != -1 else None


class MSBSpawnerEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.Spawner
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("max_count", "B"),
        ("spawner_type", "b"),
        ("limit_count", "h"),
        ("min_spawner_count", "h"),
        ("max_spawner_count", "h"),
        ("min_interval", "f"),
        ("max_interval", "f"),
        ("initial_spawn_count", "i"),
        "28x",
        ("_spawn_region_indices", "4i"),
        ("_spawn_part_indices", "32i"),
        "64x",
    )
    SPAWN_REGION_COUNT: int = None

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
        # 'spawn_region_names' defined in subclass.
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

    def __init__(self, source=None, **kwargs):
        self._spawn_region_indices = [-1] * self.SPAWN_REGION_COUNT
        self._spawn_part_indices = [-1] * 32
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._spawn_region_indices = [region_indices[n] if n else -1 for n in self.spawn_region_names]
        while len(self._spawn_region_indices) < self.SPAWN_REGION_COUNT:
            self._spawn_part_indices.append(-1)
        self._spawn_part_indices = [part_indices[n] if n else -1 for n in self.spawn_part_names]
        while len(self._spawn_part_indices) < 32:
            self._spawn_part_indices.append(-1)

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.spawn_region_names = [region_names[i] if i != -1 else None for i in self._spawn_region_indices]
        while len(self.spawn_region_names) < self.SPAWN_REGION_COUNT:
            self.spawn_region_names.append(None)
        self.spawn_part_names = [part_names[i] if i != -1 else None for i in self._spawn_part_indices]
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
    ENTRY_SUBTYPE = MSBEventSubtype.ObjAct
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("obj_act_entity_id", "i"),
        ("_obj_act_part_index", "i"),
        ("obj_act_param_id", "h"),
        ("obj_act_state", "B"),
        "x",
        ("obj_act_flag", "i"),
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

    obj_act_entity_id: int
    obj_act_part_name: tp.Optional[str]
    obj_act_param_id: int
    obj_act_state: int
    obj_act_flag: int

    def __init__(self, source=None, **kwargs):
        self._obj_act_part_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._obj_act_part_index = part_indices[self.obj_act_part_name] if self.obj_act_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.obj_act_part_name = part_names[self._obj_act_part_index] if self._obj_act_part_index != -1 else None


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

    spawn_point_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._spawn_point_region_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        if self.spawn_point_region_name:
            self._spawn_point_region_index = region_indices[self.spawn_point_region_name]
        else:
            self._spawn_point_region_index = -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._spawn_point_region_index != -1:
            self.spawn_point_region_name = region_names[self._spawn_point_region_index]
        else:
            self.spawn_point_region_name = None


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
            "Region to which Navigation event is attached, which encloses parts of one or more Navmesh parts.",
        ),
    }

    FIELD_ORDER = (
        "entity_id",
        "navigation_region_name",
    )

    navigation_region_name: tp.Optional[str]

    def __init__(self, source, **kwargs):
        self._navigation_region_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        if self.navigation_region_name:
            self._navigation_region_index = region_indices[self.navigation_region_name]
        else:
            self._navigation_region_index = -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._navigation_region_index != -1:
            self.navigation_region_name = region_names[self._navigation_region_index]
        else:
            self.navigation_region_name = None


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


class MSBNPCInvasionEvent(MSBEvent):
    ENTRY_SUBTYPE = MSBEventSubtype.NPCInvasion
    EVENT_TYPE_DATA_STRUCT = BinaryStruct(
        ("host_entity_id", "i"),
        ("invasion_flag_id", "i"),
        ("_spawn_point_region_index", "i"),
        "4x",
    )

    FIELD_INFO = MSBEvent.FIELD_INFO | {
        "base_region_name": MapFieldInfo(
            "Invasion Region",
            Region,
            None,
            "Region in which NPC Invasion event can be triggered (e.g. with Black Eye Orb).",
        ),
        "host_entity_id": MapFieldInfo(
            "Host Entity ID",
            int,
            -1,
            "Entity ID of NPC character to be invaded.",
        ),
        "invasion_flag_id": MapFieldInfo(
            "Invasion Flag",
            Flag,
            -1,
            "Flag that is enabled while the invasion is active, which should trigger changes to the world.",
        ),
        "spawn_point_region_name": MapFieldInfo(
            "Spawn Point Region",
            Region,
            None,
            "Region where player will spawn during invasion event.",
        ),
    }

    FIELD_ORDER = (
        "base_region_name",
        "host_entity_id",
        "invasion_flag_id",
        "spawn_point_region_name",
    )

    host_entity_id: int
    invasion_flag_id: int
    spawn_point_region_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._spawn_point_region_index = None
        super().__init__(source=source, **kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        if self.spawn_point_region_name:
            self._spawn_point_region_index = region_indices[self.spawn_point_region_name]
        else:
            self._spawn_point_region_index = -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._spawn_point_region_index != -1:
            self.spawn_point_region_name = region_names[self._spawn_point_region_index]
        else:
            self.spawn_point_region_name = None


class MSBEventList(MSBEntryList[MSBEvent]):
    ENTRY_LIST_NAME = "Events"
    ENTRY_SUBTYPE_ENUM = MSBEventSubtype
    SUBTYPE_CLASSES = {}  # type: dict[MSBEventSubtype, type]
    SUBTYPE_OFFSET = None  # type: int

    _entries: list[MSBEvent]

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

    def pack_entry(self, index: int, entry: MSBEvent):
        return entry.pack()

    def set_names(self, region_names, part_names):
        for entry in self._entries:
            entry.set_names(region_names, part_names)

    def set_indices(self, region_indices, part_indices):
        """Global and subtype-specific indices both set. (Unclear if either of them do anything.)"""
        subtype_indices = {}
        for i, entry in enumerate(self._entries):
            try:
                entry.set_indices(
                    event_index=i,
                    local_event_index=subtype_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    region_indices=region_indices,
                    part_indices=part_indices,
                )
            except KeyError as e:
                raise MapEventError(
                    f"Invalid map component name for {entry.ENTRY_SUBTYPE.name} event '{entry.name}': {e}"
                )
            else:
                subtype_indices[entry.ENTRY_SUBTYPE] += 1


for _entry_subtype in MSBEventList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBEventList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
