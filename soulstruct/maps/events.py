from io import BufferedReader, BytesIO
from enum import IntEnum
import struct

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSB_EVENT_TYPE(IntEnum):  # TODO: better names for some of these?
    Light = 0
    Sound = 1
    FX = 2
    Wind = 3
    Treasure = 4
    Generator = 5
    Message = 6
    ObjAct = 7
    SpawnPoint = 8
    MapOffset = 9
    Navmesh = 10
    Environment = 11
    NPCInvasion = 12


def MSBEvent(msb_buffer):
    """Detects the appropriate subclass of BaseMSBEvent to instantiate."""
    # TODO: support more types?
    return BaseMSBEvent.auto_event_subclass(msb_buffer)


class BaseMSBEvent(object):
    EVENT_HEADER_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        ('event_index', 'i'),
        ('event_type', 'I'),
        ('event_index_2', 'i'),  # TODO: what is this? local vs. global index?
        ('base_data_offset', 'i'),
        ('type_data_offset', 'i'),
        '4x',
    )

    EVENT_BASE_DATA_STRUCT = BinaryStruct(
        ('part_index', 'i'),
        ('region_index', 'i'),
        ('entity_id', 'i'),
        '4x',
    )

    EVENT_TYPE = -1

    def __init__(self, msb_event_source):
        self.name = ''
        self.event_index = None  # TODO: index?
        self.event_index_2 = None
        self.entity_id = None
        self.base_part_index = None
        self.base_region_index = None

        if isinstance(msb_event_source, bytes):
            msb_event_source = BytesIO(msb_event_source)
        if isinstance(msb_event_source, BufferedReader):
            self.unpack(msb_event_source)
        else:
            raise TypeError("'msb_event_source' must be a buffer or bytes.")

    def unpack(self, msb_buffer):
        raise NotImplementedError

    def unpack_base(self, msb_buffer):
        event_offset = msb_buffer.tell()
        header = self.EVENT_HEADER_STRUCT.unpack(msb_buffer)
        if header.event_type != self.EVENT_TYPE:
            raise ValueError(f"Unexpected event type enum {header.event_type} for class {self.__class__.__name__}.")

        msb_buffer.seek(event_offset + header.base_data_offset)
        base_data = self.EVENT_BASE_DATA_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(msb_buffer, offset=event_offset + header.name_offset, encoding='shift-jis')
        self.event_index = header.event_index
        self.event_index_2 = header.event_index_2  # TODO
        self.entity_id = base_data.entity_id
        self.base_part_index = base_data.part_index
        self.base_region_index = base_data.region_index
        msb_buffer.seek(event_offset + header.type_data_offset)

    @staticmethod
    def auto_event_subclass(msb_buffer):
        old_offset = msb_buffer.tell()
        msb_buffer.seek(old_offset + 8)
        try:
            event_type_int = struct.unpack('i', msb_buffer.read(4))[0]
            event_type = MSB_EVENT_TYPE(event_type_int)
        except (ValueError, TypeError):
            event_type = None
        msb_buffer.seek(old_offset)
        return MSB_EVENT_TYPE_CLASSES[event_type](msb_buffer)


class MSBLight(BaseMSBEvent):
    EVENT_LIGHT_STRUCT = (
        ('unk_x00_x04', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Light

    def __init__(self, msb_event_source):
        self.unk_x00_x04 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_LIGHT_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04


class MSBSound(BaseMSBEvent):
    EVENT_SOUND_STRUCT = (
        ('sound_type', 'i'),
        ('sound_id', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Sound

    def __init__(self, msb_event_source):
        self.sound_type = None
        self.sound_id = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_SOUND_STRUCT).unpack(msb_buffer)
        self.sound_type = data.sound_type
        self.sound_id = data.sound_id


class MSBFX(BaseMSBEvent):
    EVENT_FX_STRUCT = (
        ('fx_id', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.FX

    def __init__(self, msb_event_source):
        self.fx_id = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_FX_STRUCT).unpack(msb_buffer)
        self.fx_id = data.fx_id


class MSBWind(BaseMSBEvent):
    EVENT_WIND_STRUCT = (
        ('unk_x00_x04', 'f'),
        ('unk_x04_x08', 'f'),
        ('unk_x08_x0c', 'f'),
        ('unk_x0c_x10', 'f'),
        ('unk_x10_x14', 'f'),
        ('unk_x14_x18', 'f'),
        ('unk_x18_x1c', 'f'),
        ('unk_x1c_x20', 'f'),
        ('unk_x20_x24', 'f'),
        ('unk_x24_x28', 'f'),
        ('unk_x28_x2c', 'f'),
        ('unk_x2c_x30', 'f'),
        ('unk_x30_x34', 'f'),
        ('unk_x34_x38', 'f'),
        ('unk_x38_x3c', 'f'),
        ('unk_x3c_x40', 'f'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Wind

    def __init__(self, msb_event_source):
        """Data consists of 16 floats, which likely specify the transform parameters (e.g. position, direction) of wind
        effects in the map."""
        self.unk_x00_x04 = None
        self.unk_x04_x08 = None
        self.unk_x08_x0c = None
        self.unk_x0c_x10 = None
        self.unk_x10_x14 = None
        self.unk_x14_x18 = None
        self.unk_x18_x1c = None
        self.unk_x1c_x20 = None
        self.unk_x20_x24 = None
        self.unk_x24_x28 = None
        self.unk_x28_x2c = None
        self.unk_x2c_x30 = None
        self.unk_x30_x34 = None
        self.unk_x34_x38 = None
        self.unk_x38_x3c = None
        self.unk_x3c_x40 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_WIND_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04
        self.unk_x04_x08 = data.unk_x04_x08
        self.unk_x08_x0c = data.unk_x08_x0c
        self.unk_x0c_x10 = data.unk_x0c_x10
        self.unk_x10_x14 = data.unk_x10_x14
        self.unk_x14_x18 = data.unk_x14_x18
        self.unk_x18_x1c = data.unk_x18_x1c
        self.unk_x1c_x20 = data.unk_x1c_x20
        self.unk_x20_x24 = data.unk_x20_x24
        self.unk_x24_x28 = data.unk_x24_x28
        self.unk_x28_x2c = data.unk_x28_x2c
        self.unk_x2c_x30 = data.unk_x2c_x30
        self.unk_x30_x34 = data.unk_x30_x34
        self.unk_x34_x38 = data.unk_x34_x38
        self.unk_x38_x3c = data.unk_x38_x3c
        self.unk_x3c_x40 = data.unk_x3c_x40


class MSBTreasure(BaseMSBEvent):
    EVENT_TREASURE_STRUCT = (
        '4x',
        ('treasure_part_index', 'i'),
        ('item_lot_1', 'i'),
        ('minus_one_1', 'i', -1),
        ('item_lot_2', 'i'),
        ('minus_one_2', 'i', -1),
        ('item_lot_3', 'i'),
        ('minus_one_3', 'i', -1),
        ('item_lot_4', 'i'),
        ('minus_one_4', 'i', -1),
        ('item_lot_5', 'i'),
        ('minus_one_5', 'i', -1),
        ('in_chest', '?'),
        ('start_disabled', '?'),
        '2x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Treasure

    def __init__(self, msb_event_source):
        self.treasure_part_index = None
        self.item_lot_1 = None
        self.item_lot_2 = None
        self.item_lot_3 = None
        self.item_lot_4 = None
        self.item_lot_5 = None
        self.in_chest = None
        self.start_disabled = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_TREASURE_STRUCT).unpack(msb_buffer)
        self.treasure_part_index = data.treasure_part_index
        self.item_lot_1 = data.item_lot_1
        self.item_lot_2 = data.item_lot_2
        self.item_lot_3 = data.item_lot_3
        self.item_lot_4 = data.item_lot_4
        self.item_lot_5 = data.item_lot_5
        self.in_chest = data.in_chest
        self.start_disabled = data.start_disabled


class MSBGenerator(BaseMSBEvent):
    EVENT_GENERATOR_STRUCT = (
        ('max_count', 'h'),
        ('limit_count', 'h'),
        ('min_generator_count', 'h'),
        ('max_generator_count', 'h'),
        ('min_interval', 'f'),
        ('max_interval', 'f'),
        ('initial_spawn_count', 'i'),
        '28x',
        ('spawn_region_indices', '4i'),
        ('spawn_part_indices', '32i'),
        '64x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Generator

    def __init__(self, msb_event_source):
        self.max_count = None
        self.limit_count = None
        self.min_generator_count = None
        self.max_generator_count = None
        self.min_interval = None
        self.max_interval = None
        self.initial_spawn_count = None
        self.spawn_region_indices = None
        self.spawn_part_indices = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_GENERATOR_STRUCT).unpack(msb_buffer)
        self.max_count = data.max_count
        self.limit_count = data.limit_count
        self.min_generator_count = data.min_generator_count
        self.max_generator_count = data.max_generator_count
        self.min_interval = data.min_interval
        self.max_interval = data.max_interval
        self.initial_spawn_count = data.initial_spawn_count
        self.spawn_region_indices = data.spawn_region_indices
        self.spawn_part_indices = data.spawn_part_indices


class MSBMessage(BaseMSBEvent):
    EVENT_MESSAGE_STRUCT = (
        ('text_id', 'h'),
        ('unk_x02_x04', 'h'),
        ('is_hidden', '?'),
        '3x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Message

    def __init__(self, msb_event_source):
        self.text_id = None
        self.unk_x02_x04 = None
        self.is_hidden = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_MESSAGE_STRUCT).unpack(msb_buffer)
        self.text_id = data.text_id
        self.unk_x02_x04 = data.unk_x02_x04
        self.is_hidden = data.is_hidden


class MSBObjAct(BaseMSBEvent):
    EVENT_OBJ_ACT_STRUCT = (
        ('obj_act_entity_id', 'i'),
        ('obj_act_part_index', 'i'),
        ('obj_act_param_id', 'h'),
        ('unk_x0a_x0c', 'h'),
        ('obj_act_flag', 'i'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.ObjAct

    def __init__(self, msb_event_source):
        self.obj_act_entity_id = None
        self.obj_act_part_index = None
        self.obj_act_param_id = None
        self.unk_x0a_x0c = None
        self.obj_act_flag = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_OBJ_ACT_STRUCT).unpack(msb_buffer)
        self.obj_act_entity_id = data.obj_act_entity_id
        self.obj_act_part_index = data.obj_act_part_index
        self.obj_act_param_id = data.obj_act_param_id
        self.unk_x0a_x0c = data.unk_x0a_x0c
        self.obj_act_flag = data.obj_act_flag


class MSBSpawnPoint(BaseMSBEvent):
    EVENT_SPAWN_POINT_STRUCT = (
        ('spawn_point_region_index', 'i'),
        '12x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.SpawnPoint

    def __init__(self, msb_event_source):
        self.spawn_point_region_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_SPAWN_POINT_STRUCT).unpack(msb_buffer)
        self.spawn_point_region_index = data.spawn_point_region_index


class MSBMapOffset(BaseMSBEvent):
    EVENT_MAP_OFFSET_STRUCT = (
        ('translate_x', 'f'),
        ('translate_y', 'f'),
        ('translate_z', 'f'),
        ('rotate_y', 'f'),
    )

    EVENT_TYPE = MSB_EVENT_TYPE.MapOffset

    def __init__(self, msb_event_source):
        self.translate_x = None
        self.translate_y = None
        self.translate_z = None
        self.rotate_y = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_MAP_OFFSET_STRUCT).unpack(msb_buffer)
        self.translate_x = data.translate_x
        self.translate_y = data.translate_y
        self.translate_z = data.translate_z
        self.rotate_y = data.rotate_y


class MSBNavmesh(BaseMSBEvent):
    EVENT_NAVMESH_STRUCT = (
        ('navmesh_region_index', 'i'),
        '12x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Navmesh

    def __init__(self, msb_event_source):
        self.navmesh_region_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_NAVMESH_STRUCT).unpack(msb_buffer)
        self.navmesh_region_index = data.navmesh_region_index


class MSBEnvironment(BaseMSBEvent):
    EVENT_ENVIRONMENT_STRUCT = (
        ('unk_x00_x04', 'i'),
        ('unk_x04_x08', 'f'),
        ('unk_x08_x0c', 'f'),
        ('unk_x0c_x10', 'f'),
        ('unk_x10_x14', 'f'),
        ('unk_x14_x18', 'f'),
        '8x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.Environment

    def __init__(self, msb_event_source):
        self.unk_x00_x04 = None
        self.unk_x04_x08 = None
        self.unk_x08_x0c = None
        self.unk_x0c_x10 = None
        self.unk_x10_x14 = None
        self.unk_x14_x18 = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_ENVIRONMENT_STRUCT).unpack(msb_buffer)
        self.unk_x00_x04 = data.unk_x00_x04
        self.unk_x04_x08 = data.unk_x04_x08
        self.unk_x08_x0c = data.unk_x08_x0c
        self.unk_x0c_x10 = data.unk_x0c_x10
        self.unk_x10_x14 = data.unk_x10_x14
        self.unk_x14_x18 = data.unk_x14_x18


class MSBNPCInvasion(BaseMSBEvent):
    EVENT_NPC_INVASION_STRUCT = (
        ('host_entity_id', 'i'),
        ('invasion_flag_id', 'i'),
        ('spawn_point_index', 'i'),
        '4x',
    )

    EVENT_TYPE = MSB_EVENT_TYPE.NPCInvasion

    def __init__(self, msb_event_source):
        self.host_entity_id = None
        self.invasion_flag_id = None
        self.spawn_point_index = None
        super().__init__(msb_event_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.EVENT_NPC_INVASION_STRUCT).unpack(msb_buffer)
        self.host_entity_id = data.host_entity_id
        self.invasion_flag_id = data.invasion_flag_id
        self.spawn_point_index = data.spawn_point_index


MSB_EVENT_TYPE_CLASSES = {
    MSB_EVENT_TYPE.Light: MSBLight,
    MSB_EVENT_TYPE.Sound: MSBSound,
    MSB_EVENT_TYPE.FX: MSBFX,
    MSB_EVENT_TYPE.Wind: MSBWind,
    MSB_EVENT_TYPE.Treasure: MSBTreasure,
    MSB_EVENT_TYPE.Generator: MSBGenerator,
    MSB_EVENT_TYPE.Message: MSBMessage,
    MSB_EVENT_TYPE.ObjAct: MSBObjAct,
    MSB_EVENT_TYPE.SpawnPoint: MSBSpawnPoint,
    MSB_EVENT_TYPE.MapOffset: MSBMapOffset,
    MSB_EVENT_TYPE.Navmesh: MSBNavmesh,
    MSB_EVENT_TYPE.Environment: MSBEnvironment,
    MSB_EVENT_TYPE.NPCInvasion: MSBNPCInvasion,
}
