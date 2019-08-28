from io import BufferedReader, BytesIO
from enum import IntEnum
import struct

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSB_REGION_TYPE(IntEnum):
    Point = 0
    Circle = 1
    Sphere = 2
    Cylinder = 4
    Rect = 5
    Box = 6


def MSBRegion(msb_buffer):
    """Detects the appropriate subclass of BaseMSBEvent to instantiate."""
    # TODO: support more types?
    return BaseMSBRegion.auto_region_subclass(msb_buffer)


class BaseMSBRegion(object):

    REGION_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        '4x',
        ('region_index', 'i'),
        ('shape_type', 'i'),
        ('translate_x', 'f'),
        ('translate_y', 'f'),
        ('translate_z', 'f'),
        ('rotate_x', 'f'),  # These are Euler angle rotations (and can therefore be gimbal-locked).
        ('rotate_y', 'f'),
        ('rotate_z', 'f'),
        ('unknown_offset_1', 'i'),
        ('unknown_offset_2', 'i'),
        ('shape_data_offset', 'i'),
        ('entity_id_offset', 'i'),
        '4x',
    )

    def __init__(self, msb_region_source):
        self.name = ''
        self.region_index = None  # TODO: identical to list index... important for anything? try scrambling it.
        self.entity_id = None

        if isinstance(msb_region_source, bytes):
            msb_region_source = BytesIO(msb_region_source)
        if isinstance(msb_region_source, BufferedReader):
            self.unpack(msb_region_source)
        else:
            raise TypeError("'msb_model_source' must be a buffer or bytes.")

    def unpack(self, msb_buffer):
        raise NotImplementedError

    def unpack_base(self, msb_buffer):
        region_offset = msb_buffer.tell()
        base_data = self.REGION_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=region_offset + base_data.name_offset, encoding='shift-jis')
        self.region_index = base_data.region_index
        self.check_null_field(msb_buffer, region_offset + base_data.unknown_offset_1)
        self.check_null_field(msb_buffer, region_offset + base_data.unknown_offset_2)

        msb_buffer.seek(region_offset + base_data.shape_data_offset)

        return region_offset + base_data.entity_id_offset

    @staticmethod
    def check_null_field(msb_buffer, offset_to_null):
        msb_buffer.seek(offset_to_null)
        zero = msb_buffer.read(4)
        if zero != b'\0\0\0\0':
            raise ValueError("Null data entry in MSB region was not zero.")

    @staticmethod
    def auto_region_subclass(msb_buffer):
        old_offset = msb_buffer.tell()
        msb_buffer.seek(old_offset + 12)
        try:
            region_type_int = struct.unpack('i', msb_buffer.read(4))[0]
            region_type = MSB_REGION_TYPE(region_type_int)
        except (ValueError, TypeError):
            region_type = None
        msb_buffer.seek(old_offset)
        return REGION_TYPE_CLASSES[region_type](msb_buffer)


class MSBRegionPoint(BaseMSBRegion):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way will the
    player be facing when they spawn?)."""
    REGION_TYPE = MSB_REGION_TYPE.Point

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


class MSBRegionCircle(BaseMSBRegion):
    """Almost never used (no volume)."""
    CIRCLE_STRUCT = (
        ('radius', 'f'),
    )

    REGION_TYPE = MSB_REGION_TYPE.Circle

    def __init__(self, msb_region_shape_source):
        self.radius = None
        super().__init__(msb_region_shape_source)

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        self.radius = BinaryStruct(*self.CIRCLE_STRUCT).unpack(msb_buffer).radius
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


class MSBRegionSphere(BaseMSBRegion):
    SPHERE_STRUCT = (
        ('radius', 'f'),
    )

    REGION_TYPE = MSB_REGION_TYPE.Sphere

    def __init__(self, msb_region_shape_source):
        self.radius = None
        super().__init__(msb_region_shape_source)

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        self.radius = BinaryStruct(*self.SPHERE_STRUCT).unpack(msb_buffer).radius
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


class MSBRegionCylinder(BaseMSBRegion):
    CYLINDER_STRUCT = (
        ('radius', 'f'),
        ('height', 'f'),
    )

    REGION_TYPE = MSB_REGION_TYPE.Cylinder

    def __init__(self, msb_region_shape_source):
        self.radius = None
        self.height = None
        super().__init__(msb_region_shape_source)

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.CYLINDER_STRUCT).unpack(msb_buffer)
        self.radius = data.radius
        self.height = data.height
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


class MSBRegionRect(BaseMSBRegion):
    """Almost never used (no volume)."""
    RECT_STRUCT = (
        ('width', 'f'),
        ('depth', 'f'),
    )

    REGION_TYPE = MSB_REGION_TYPE.Rect

    def __init__(self, msb_region_shape_source):
        self.width = None
        self.depth = None
        super().__init__(msb_region_shape_source)

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.RECT_STRUCT).unpack(msb_buffer)
        self.width = data.width
        self.depth = data.depth
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


class MSBRegionBox(BaseMSBRegion):
    SHAPE_STRUCT = (
        ('width', 'f'),
        ('depth', 'f'),
        ('height', 'f'),
    )

    REGION_TYPE = MSB_REGION_TYPE.Box

    def __init__(self, msb_region_shape_source):
        self.width = None
        self.depth = None
        self.height = None
        super().__init__(msb_region_shape_source)

    def unpack(self, msb_buffer):
        entity_id_offset = self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.SHAPE_STRUCT).unpack(msb_buffer)
        self.width = data.width
        self.depth = data.depth
        self.height = data.height
        msb_buffer.seek(entity_id_offset)
        self.entity_id = struct.unpack('i', msb_buffer.read(4))


REGION_TYPE_CLASSES = {
    MSB_REGION_TYPE.Point: MSBRegionPoint,
    MSB_REGION_TYPE.Circle: MSBRegionCircle,
    MSB_REGION_TYPE.Sphere: MSBRegionSphere,
    MSB_REGION_TYPE.Cylinder: MSBRegionCylinder,
    MSB_REGION_TYPE.Rect: MSBRegionRect,
    MSB_REGION_TYPE.Box: MSBRegionBox,
}
