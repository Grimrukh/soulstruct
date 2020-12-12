import abc
import typing as tp
from io import BufferedReader, BytesIO

from soulstruct.events.darksouls1.enums import SoundType
from soulstruct.game_types import *
from soulstruct.maps.core import MapError
from soulstruct.maps.enums import MSBEventSubtype
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, pad_chars, unpack_from_buffer
from soulstruct.utilities.maths import Vector3

from .msb_entry import MSBEntryList, MSBEntryEntity


class MSBEvent(MSBEntryEntity, abc.ABC):
    """Parent class for MSB events, which describe various things that occur in maps (often attached to Regions)."""

    EVENT_HEADER_STRUCT = None  # type: BinaryStruct
    # Name is stored next.
    # Base data is stored next.
    # Type data is stored next.

    EVENT_BASE_DATA_STRUCT = None  # type: BinaryStruct

    EVENT_TYPE_DATA_STRUCT = ()

    ENTRY_SUBTYPE = None  # type: MSBEventSubtype

    def __init__(self, msb_event_source=None):
        super().__init__()
        self._event_index = None  # global index
        self._local_event_index = None  # local type index
        self.base_part_name = None
        self._base_part_index = None
        self.base_region_name = None
        self._base_region_index = None

        if isinstance(msb_event_source, bytes):
            msb_event_source = BytesIO(msb_event_source)
        if isinstance(msb_event_source, BufferedReader):
            self.unpack(msb_event_source)
        elif msb_event_source is not None:
            raise TypeError("`msb_event_source` must be a buffer, `bytes`, or `None`.")

    def unpack(self, msb_buffer):
        event_offset = msb_buffer.tell()
        header = self.EVENT_HEADER_STRUCT.unpack(msb_buffer)
        if header["__event_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected MSB event type value {header['__event_type']} for {self.__class__.__name__}.")
        msb_buffer.seek(event_offset + header["__base_data_offset"])
        base_data = self.EVENT_BASE_DATA_STRUCT.unpack(msb_buffer)
        name_offset = event_offset + header["__name_offset"]
        self.name = read_chars_from_buffer(msb_buffer, offset=name_offset, encoding="shift-jis")
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
        packed_name = pad_chars(self.get_name_to_pack(), encoding="shift-jis", pad_to_multiple_of=4)
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
        self.set(**BinaryStruct(*self.EVENT_TYPE_DATA_STRUCT).unpack(msb_buffer, include_asserted=False))

    def pack_type_data(self):
        return BinaryStruct(*self.EVENT_TYPE_DATA_STRUCT).pack_from_object(self)


class MSBLightEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("point_light", "i"),
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Light will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": (
            "Light Region",
            Region,
            "Region (usually a Point) at which Light appears.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the event in other game files. (Unused for Lights.)",
        ),
        "point_light": (
            "Point Light",
            PointLightParam,
            "Point Light lighting parameter ID to use for this light.",
        ),
    }

    FIELD_NAMES = (
        "base_part_name",
        "base_region_name",
        "point_light",
    )

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.Light

    def __init__(self, msb_event_source=None, **kwargs):
        self.point_light = 0
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBSoundEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("sound_type", "i"),
        ("sound_id", "i"),
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Sound is connected to this part (usually a Collision or Map Piece part), but this has an unknown effect.",
        ),
        "base_region_name": (
            "Sound Volume",
            Region,
            "Region in which Sound can be heard, if it's enabled.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the Sound in other game files.",
        ),
        "sound_type": (
            "Sound Type",
            SoundType,
            "Type of sound, which is used to find the sound data (sound name prefix letter).",
        ),
        "sound_id": (
            "Sound ID",
            Sound,
            "Sound data ID, which refers to an ID in loaded sound events.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "sound_type",
        "sound_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.Sound

    def __init__(self, msb_event_source=None, **kwargs):
        self.sound_type = SoundType.m_Music
        self.sound_id = -1
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBFXEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("fx_id", "i"),
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "FX will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": (
            "FX Region",
            Region,
            "Region (usually a Point) at which FX appears.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to this FX in other game files.",
        ),
        "fx_id": (
            "FX ID",
            int,
            "Visual effect ID, which refers to a loaded FX file.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "base_part_name",
        "base_region_name",
        "fx_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.FX

    def __init__(self, msb_event_source=None, **kwargs):
        self.fx_id = 0
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBWindEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("wind_vector_min", "f"),
        ("unk_x04_x08", "f"),
        ("wind_vector_max", "f"),
        ("unk_x0c_x10", "f"),
        ("_wind_swing_cycles", "ffff"),
        ("_wind_swing_powers", "ffff"),
    )

    FIELD_INFO = {
        "entity_id": (
            "Entity ID",
            int,
            "Unused for Wind events.",
        ),
        **MSBEvent.FIELD_INFO,
        "wind_vector_min": (
            "Wind Vector Min",
            float,
            "Wind vector minimum.",
        ),
        "unk_x04_x08": (
            "Unknown [04-08]",
            float,
            "Unknown Wind parameter (floating-point number).",
        ),
        "wind_vector_max": (
            "Wind Vector Max",
            float,
            "Wind vector maximum.",
        ),
        "unk_x0c_x10": (
            "Unknown [0c-10]",
            float,
            "Unknown Wind parameter (floating-point number).",
        ),
        "_wind_swing_cycles": (
            "Wind Swing Cycles",
            list,
            "Wind swing cycles (four values).",
        ),
        "_wind_swing_powers": (
            "Wind Swing Powers",
            list,
            "Wind swing powers (four values).",
        ),
    }

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.Wind

    def __init__(self, msb_event_source=None, **kwargs):
        """Data consists of 16 floats, which likely specify the transform parameters (e.g. position, direction) of wind
        effects in the map."""
        self.wind_vector_min = 0.0
        self.unk_x04_x08 = 0.0
        self.wind_vector_max = 0.0
        self.unk_x0c_x10 = 0.0
        self._wind_swing_cycles = [0.0, 0.0, 0.0, 0.0]
        self._wind_swing_powers = [0.0, 0.0, 0.0, 0.0]
        super().__init__(msb_event_source)
        self.set(**kwargs)

    @property
    def wind_swing_cycles(self):
        return self._wind_swing_cycles

    @property
    def wind_swing_powers(self):
        return self._wind_swing_powers


class MSBTreasureEvent(MSBEvent, abc.ABC):
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
        "entity_id": (
            "Entity ID",
            int,
            "Unused for Treasure events.",
        ),
        "treasure_part_name": (
            "Treasure Object",
            Object,
            "Object on which treasure will appear (usually a corpse or chest).",
        ),
        "item_lot_1": (
            "Item Lot 1",
            ItemLotParam,
            "First item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_2": (
            "Item Lot 2",
            ItemLotParam,
            "Second item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
        "item_lot_3": (
            "Item Lot 3",
            ItemLotParam,
            "Third item lot of treasure. (Note that the item lots that are +1 to +5 from this ID will also be "
            "awarded.)",
        ),
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
        "in_chest": (
            "Is In Chest",
            bool,
            "Indicates if this treasure is inside a chest (affects appearance).",  # TODO: effect?
        ),
        "is_hidden": (
            "Is Hidden",
            bool,
            "If True, this treasure will start disabled and will need to be enabled manually with an event script.",
        ),
    }

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.Treasure

    def __init__(self, msb_event_source=None, **kwargs):
        self.treasure_part_name = None
        self._treasure_part_index = None
        self.item_lot_1 = -1
        self.item_lot_2 = -1
        self.item_lot_3 = -1
        self.in_chest = False
        self.is_hidden = False
        super().__init__(msb_event_source)
        self.set(**kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._treasure_part_index = part_indices[self.treasure_part_name] if self.treasure_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.treasure_part_name = part_names[self._treasure_part_index] if self._treasure_part_index != -1 else None


class MSBSpawnerEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
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

    SPAWN_REGION_COUNT = 4

    FIELD_INFO = {
        # base_part and base_region are unused for Spawners.
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the Spawner in other game files.",
        ),
        "max_count": (
            "Max Count",
            int,
            "Unsure; I suspect this is the total number of entities this spawner can produce.",
        ),
        "spawner_type": (
            "Spawner Type",
            int,
            "Unsure what this enumeration is.",
        ),
        "limit_count": (
            "Limit Count",
            int,
            "Unsure; I suspect this is the number of spawned entities that can be alive at once.",
        ),
        "min_spawner_count": (
            "Min Spawner Count",
            int,
            "Unsure.",
        ),
        "max_spawner_count": (
            "Max Spawner Count",
            int,
            "Unsure.",
        ),
        "min_interval": (
            "Min Interval",
            float,
            "Minimum number of seconds between spawns.",
        ),
        "max_interval": (
            "Max Interval",
            float,
            "Maximum number of seconds between spawns.",
        ),
        "initial_spawn_count": (
            "Initial Spawn Count",
            int,
            "Unsure; I suspect this is the number of entities spawned immediately on map load.",
        ),
        "spawn_region_names": (
            "Spawn Regions",
            GameObjectSequence((Region, 4)),  # TODO: need a special pop-out window of entries for this.
            "Regions where entities will be spawned.",
        ),
        "spawn_part_names": (
            "Spawn Characters",
            GameObjectSequence((Character, 32)),  # TODO: ditto
            "Entities that will be spawned at given regions.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.Spawner

    def __init__(self, msb_event_source=None, **kwargs):
        self.max_count = 255
        self.limit_count = -1
        self.min_spawner_count = 1
        self.max_spawner_count = 1
        self.min_interval = 1.0
        self.max_interval = 1.0
        self.initial_spawn_count = 1
        self.spawn_region_names = [None] * self.SPAWN_REGION_COUNT
        self._spawn_region_indices = [-1] * self.SPAWN_REGION_COUNT
        self.spawn_part_names = [None] * 32
        self._spawn_part_indices = [-1] * 32
        super().__init__(msb_event_source)
        self.set(**kwargs)

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
    EVENT_TYPE_DATA_STRUCT = (
        ("text_id", "h"),
        ("unk_x02_x04", "h"),
        ("is_hidden", "?"),
        "3x",
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Message will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "base_region_name": (
            "Message Region",
            Region,
            "Region (usually a Point) at which Message appears.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the Message in other game files.",
        ),
        "text_id": (
            "Message Text",
            SoapstoneMessage,
            "Text shown when soapstone message is examined.",
        ),
        "unk_x02_x04": (
            "Unknown [02-04]",
            int,
            "Unknown. Often set to 2.",
        ),
        "is_hidden": (
            "Is Hidden",
            bool,
            "If True, the message must be manually enabled with an event script or by using Seek Guidance.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.Message

    def __init__(self, msb_event_source=None, **kwargs):
        self.text_id = -1
        self.unk_x02_x04 = 2
        self.is_hidden = False
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBObjActEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("obj_act_entity_id", "i"),
        ("_obj_act_part_index", "i"),
        ("obj_act_param_id", "h"),
        ("obj_act_state", "B"),
        "x",
        ("obj_act_flag", "i"),
    )

    FIELD_INFO = {
        # base_part, base_region, and entity_id are unused in ObjActs.
        "entity_id": (
            "Entity ID",
            int,
            "Unused for ObjAct events. Use ObjAct Entity ID instead."),
        "obj_act_entity_id": (
            "ObjAct Entity ID",
            int,
            "ID that identifies this object activation event in event scripts.",
        ),
        "obj_act_part_name": (
            "Object",
            Object,
            "Object to which this object activation event is attached.",
        ),
        "obj_act_param_id": (
            "ObjAct Param",
            ObjActParam,
            "Param entry containing information about this object activation event. If it is -1, it will "
            "default to the model ID of the object it is attached to.",
        ),
        "obj_act_state": (
            "ObjAct State",
            int,
            "State of object activation. Known values include Default (0), Door (1), and Loop (2).",
        ),
        "obj_act_flag": (
            "ObjAct Flag",
            Flag,
            "Flag that stores the persistent state (e.g. open/closed) of this object activation.",
        ),
    }

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.ObjAct

    def __init__(self, msb_event_source=None, **kwargs):
        self.obj_act_entity_id = -1
        self.obj_act_part_name = None
        self._obj_act_part_index = None
        self.obj_act_param_id = -1
        self.obj_act_state = 0
        self.obj_act_flag = 0
        super().__init__(msb_event_source)
        self.set(**kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._obj_act_part_index = part_indices[self.obj_act_part_name] if self.obj_act_part_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        self.obj_act_part_name = part_names[self._obj_act_part_index] if self._obj_act_part_index != -1 else None


class MSBSpawnPointEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("_spawn_point_region_index", "i"),
        "12x",
    )

    FIELD_INFO = {
        # base_region is unused in Spawn Points.
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Some Spawn Points use this; unclear what it does, but it is presumably the Collision of the Spawn Point.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the Spawn Point in other game files.",
        ),
        "spawn_point_region_name": (
            "Spawn Point Region",
            Region,
            "Region where player will spawn when registered to this spawn point.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.SpawnPoint

    def __init__(self, msb_event_source=None, **kwargs):
        self.spawn_point_region_name = None
        self._spawn_point_region_index = None
        super().__init__(msb_event_source)
        self.set(**kwargs)

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
    EVENT_TYPE_DATA_STRUCT = (
        ("translate", "3f"),
        ("rotate_y", "f"),
    )

    FIELD_INFO = {
        "entity_id": (
            "Entity ID",
            int,
            "Unused for MapOffset events.",
        ),
        "translate": (
            "Translate",
            Vector3,
            "Vector of (x, y, z) coordinates of map offset.",
        ),
        "rotate_y": (
            "Y Rotation",
            float,
            "Euler angle of rotation around the Y (vertical) axis.",
        ),
    }

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.MapOffset

    def __init__(self, msb_event_source, **kwargs):
        self.translate = [0, 0, 0]
        self.rotate_y = 0
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBNavigationEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("_navmesh_region_index", "i"),
        "12x",
    )

    FIELD_INFO = {
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the Navmesh in other game files.",
        ),
        "navmesh_region_name": (
            "Navmesh Region",
            Region,
            "Region to which navmesh event is attached.",
        ),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.Navigation

    def __init__(self, msb_event_source, **kwargs):
        self.navmesh_region_name = None
        self._navmesh_region_index = None
        super().__init__(msb_event_source)
        self.set(**kwargs)

    def set_indices(self, event_index, local_event_index, region_indices, part_indices):
        super().set_indices(event_index, local_event_index, region_indices, part_indices)
        self._navmesh_region_index = region_indices[self.navmesh_region_name] if self.navmesh_region_name else -1

    def set_names(self, region_names, part_names):
        super().set_names(region_names, part_names)
        if self._navmesh_region_index != -1:
            self.navmesh_region_name = region_names[self._navmesh_region_index]
        else:
            self.navmesh_region_name = None


class MSBEnvironmentEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("unk_x00_x04", "i"),
        ("unk_x04_x08", "f"),
        ("unk_x08_x0c", "f"),
        ("unk_x0c_x10", "f"),
        ("unk_x10_x14", "f"),
        ("unk_x14_x18", "f"),
        "8x",
    )

    FIELD_INFO = {
        "base_part_name": (
            "Draw Parent",
            MapPart,
            "Environment (or 'map spot') will be drawn whenever its parent is drawn.",
        ),
        "base_region_name": (
            "Environment Region",
            Region,
            "Region (usually a Point) at which Environment appears (whatever that means).",
        ),
        "entity_id": (
            "Environment ID",
            int,
            "Unknown index. Note that this replaces the Entity ID field (unlikely that it works as an Entity ID, as "
            "the same low-numbering values are used in multiple maps).",
        ),
        "unk_x00_x04": ("Unknown [00-04]", int, "Unknown Environment parameter (integer)."),
        "unk_x04_x08": ("Unknown [04-08]", float, "Unknown Environment parameter (floating-point number)."),
        "unk_x08_x0c": ("Unknown [08-0c]", float, "Unknown Environment parameter (floating-point number)."),
        "unk_x0c_x10": ("Unknown [0c-10]", float, "Unknown Environment parameter (floating-point number)."),
        "unk_x10_x14": ("Unknown [10-14]", float, "Unknown Environment parameter (floating-point number)."),
        "unk_x14_x18": ("Unknown [14-18]", float, "Unknown Environment parameter (floating-point number)."),
    }

    ENTRY_SUBTYPE = MSBEventSubtype.Environment

    def __init__(self, msb_event_source, **kwargs):
        self.unk_x00_x04 = 0
        self.unk_x04_x08 = 1.0
        self.unk_x08_x0c = 1.0
        self.unk_x0c_x10 = 1.0
        self.unk_x10_x14 = 1.0
        self.unk_x14_x18 = 1.0
        super().__init__(msb_event_source)
        self.set(**kwargs)


class MSBPseudoMultiplayerEvent(MSBEvent):
    EVENT_TYPE_DATA_STRUCT = (
        ("host_entity_id", "i"),
        ("invasion_flag_id", "i"),
        ("_spawn_point_region_index", "i"),
        "4x",
    )

    FIELD_INFO = {
        # base_part is unused for NPC Invasions.
        "base_region_name": (
            "Invasion Region",
            Region,
            "Region (a volume) in which NPC Invasion can be triggered (e.g. with Black Eye Orb).",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the NPC Invasion in other game files (unused).",
        ),
        "host_entity_id": (
            "Host Entity ID",
            int,
            "Entity ID of NPC character to be invaded.",
        ),
        "invasion_flag_id": (
            "Invasion Flag",
            Flag,
            "Flag that is enabled while the invasion is active, which should trigger changes to the world.",
        ),
        "spawn_point_region_name": (
            "Spawn Point Region",
            Region,
            "Region where player will spawn during invasion event.",
        ),
    }

    HIDDEN_FIELDS = (
        "entity_id",
    )

    ENTRY_SUBTYPE = MSBEventSubtype.PseudoMultiplayer

    def __init__(self, msb_event_source):
        self.host_entity_id = -1
        self.invasion_flag_id = -1
        self.spawn_point_region_name = None
        self._spawn_point_region_index = None
        super().__init__(msb_event_source)

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
    ENTRY_CLASS = staticmethod(MSBEvent)
    ENTRY_SUBTYPE_ENUM = MSBEventSubtype

    EVENT_SUBTYPE_CLASSES = {}  # type: dict[MSBEventSubtype, type]
    EVENT_SUBTYPE_OFFSET = None  # type: int

    _entries: tp.List[MSBEvent]

    Lights: tp.Sequence[MSBLightEvent]
    Sounds: tp.Sequence[MSBSoundEvent]
    FX: tp.Sequence[MSBFXEvent]
    Wind: tp.Sequence[MSBWindEvent]
    Treasure: tp.Sequence[MSBTreasureEvent]
    Spawners: tp.Sequence[MSBSpawnerEvent]
    Messages: tp.Sequence[MSBMessageEvent]
    ObjActs: tp.Sequence[MSBObjActEvent]
    SpawnPoints: tp.Sequence[MSBSpawnPointEvent]
    MapOffsets: tp.Sequence[MSBMapOffsetEvent]
    Navigation: tp.Sequence[MSBNavigationEvent]
    Environment: tp.Sequence[MSBEnvironmentEvent]
    NPCInvasions: tp.Sequence[MSBPseudoMultiplayerEvent]

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
                raise MapError(
                    f"Invalid map component name for {entry.ENTRY_SUBTYPE.name} event {entry.name}: {e}"
                )
            else:
                subtype_indices[entry.ENTRY_SUBTYPE] += 1

    def duplicate_light(
        self, light_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBLightEvent:
        return self.duplicate_entry(MSBEventSubtype.Light, light_name_or_index, insert_below_original, **kwargs)

    def duplicate_sound(
        self, sound_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBSoundEvent:
        return self.duplicate_entry(MSBEventSubtype.Sound, sound_name_or_index, insert_below_original, **kwargs)

    def duplicate_fx(
        self, fx_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBFXEvent:
        return self.duplicate_entry(MSBEventSubtype.FX, fx_name_or_index, insert_below_original, **kwargs)

    def duplicate_wind(
        self, wind_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBWindEvent:
        return self.duplicate_entry(MSBEventSubtype.Wind, wind_name_or_index, insert_below_original, **kwargs)

    def duplicate_treasure(
        self, treasure_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBTreasureEvent:
        return self.duplicate_entry(MSBEventSubtype.Treasure, treasure_name_or_index, insert_below_original, **kwargs)

    def duplicate_spawner(
        self, spawner_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBSpawnerEvent:
        return self.duplicate_entry(MSBEventSubtype.Spawner, spawner_name_or_index, insert_below_original, **kwargs)

    def duplicate_message(
        self, message_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBMessageEvent:
        return self.duplicate_entry(MSBEventSubtype.Message, message_name_or_index, insert_below_original, **kwargs)

    def duplicate_objact(
        self, objact_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBObjActEvent:
        return self.duplicate_entry(MSBEventSubtype.ObjAct, objact_name_or_index, insert_below_original, **kwargs)

    def duplicate_spawn_point(
        self, spawn_point_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBSpawnPointEvent:
        return self.duplicate_entry(
            MSBEventSubtype.SpawnPoint, spawn_point_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_map_offset(
        self, map_offset_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBMapOffsetEvent:
        return self.duplicate_entry(
            MSBEventSubtype.MapOffset, map_offset_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_navigation(
        self, navigation_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBNavigationEvent:
        return self.duplicate_entry(
            MSBEventSubtype.Navigation, navigation_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_environment(
        self, environment_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBEnvironmentEvent:
        return self.duplicate_entry(
            MSBEventSubtype.Environment, environment_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_npc_invasion(
        self, npc_invasion_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBPseudoMultiplayerEvent:
        return self.duplicate_entry(
            MSBEventSubtype.PseudoMultiplayer, npc_invasion_name_or_index, insert_below_original, **kwargs,
        )

    def get_subtype_instance(self, entry_subtype, **kwargs):
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        entry_class = self.EVENT_SUBTYPE_CLASSES[entry_subtype]
        return entry_class(msb_event_source=None, **kwargs)

    @classmethod
    def MSBEvent(cls, msb_buffer):
        """Detects the appropriate subclass of `MSBEvent` to instantiate, and does so."""
        event_type_int = unpack_from_buffer(msb_buffer, "i", offset=cls.EVENT_SUBTYPE_OFFSET, relative_offset=True)
        event_type = MSBEventSubtype(event_type_int)
        return cls.EVENT_SUBTYPE_CLASSES[event_type](msb_buffer)


for _entry_subtype in MSBEventList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBEventList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
