from io import BufferedReader, BytesIO
from enum import IntEnum

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, pad_chars


class MODEL_TYPE(IntEnum):
    MapPiece = 0
    Object = 1
    Enemy = 2
    Player = 4
    Collision = 5
    Navmesh = 6


class MSBModel(object):

    MODEL_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        ('model_type', 'i'),
        ('model_type_index', 'i'),
        ('sib_offset', 'i'),
        ('instance_count', 'i'),
        '12x',
    )

    def __init__(self, msb_model_source):
        self.model_type = -1
        self.name = ''
        self._model_type_index = None  # not sure if this matters.
        self.sib_path = ''
        self._instance_count = None

        if isinstance(msb_model_source, bytes):
            msb_model_source = BytesIO(msb_model_source)
        if isinstance(msb_model_source, BufferedReader):
            self.unpack(msb_model_source)
        else:
            raise TypeError(f"'msb_model_source' must be a buffer or bytes, not {type(msb_model_source)}")

    def unpack(self, msb_buffer):
        model_offset = msb_buffer.tell()
        model_data = self.MODEL_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data.name_offset, encoding='shift-jis')
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data.sib_offset, encoding='shift-jis')
        self.model_type = MODEL_TYPE(model_data.model_type)
        self._model_type_index = model_data.model_type_index
        self._instance_count = model_data.instance_count

    def pack(self):
        packed_name = pad_chars(self.name, encoding='shift-jis', pad_to_multiple_of=4)
        packed_sib_path = pad_chars(self.sib_path, encoding='shift-jis', pad_to_multiple_of=4)
        packed_model_data = self.MODEL_STRUCT.pack(
            name_offset=self.MODEL_STRUCT.size,
            model_type=MODEL_TYPE(self.model_type).value,
            model_type_index=self._model_type_index,
            sib_offset=self.MODEL_STRUCT.size + len(packed_name),
            instance_count=self._instance_count,
        )
        return packed_model_data + packed_name + packed_sib_path

    def set_indices(self, model_type_index, instance_count):
        self._model_type_index = model_type_index
        self._instance_count = instance_count
