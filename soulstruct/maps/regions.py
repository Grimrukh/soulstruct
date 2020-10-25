import typing as tp
import logging
import struct
from io import BufferedReader, BytesIO

from soulstruct.maps.enums import MSBRegionSubtype
from soulstruct.maps.base import MSBEntryList, MSBEntryEntityCoordinates
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, pad_chars
from soulstruct.utilities.maths import Vector3

_LOGGER = logging.getLogger(__name__)


def MSBRegion(msb_buffer):
    """Detects the appropriate subclass of BaseMSBRegion to instantiate."""
    return BaseMSBRegion.auto_region_subclass(msb_buffer)


class BaseMSBRegion(MSBEntryEntityCoordinates):

    REGION_STRUCT = BinaryStruct(
        ("name_offset", "i"),
        "4x",
        ("region_index", "i"),
        ("region_type", "i"),
        ("translate", "3f"),
        ("rotate", "3f"),  # These are Euler angle rotations (and can therefore be gimbal-locked).
        ("unknown_offset_1", "i"),
        ("unknown_offset_2", "i"),
        ("type_data_offset", "i"),
        ("entity_id_offset", "i"),
        "4x",
    )

    FIELD_INFO = {
        "translate": (
            "Translate",
            True,
            Vector3,
            "3D coordinates of the region's position. Note that this is the middle of the bottom face for box "
            "regions.",
        ),
        "rotate": ("Rotate", True, Vector3, "Euler angles for region rotation around its local X, Y, and Z axes."),
        "entity_id": ("Entity ID", True, int, "Entity ID used to refer to the region in other game files."),
    }

    ENTRY_SUBTYPE = None  # type: MSBRegionSubtype

    def __init__(self, msb_region_source=None):
        super().__init__()
        self._region_index = None  # Final automatic assignment done on `MSB.pack()`.

        if isinstance(msb_region_source, bytes):
            msb_region_source = BytesIO(msb_region_source)
        if isinstance(msb_region_source, BufferedReader):
            self.unpack(msb_region_source)
        elif msb_region_source is not None:
            raise TypeError("`msb_model_source` must be a buffer, `bytes`, or `None`.")

    def unpack(self, msb_buffer):
        region_offset = msb_buffer.tell()
        base_data = self.REGION_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=region_offset + base_data["name_offset"], encoding="shift-jis"
        )
        self._region_index = base_data["region_index"]
        self.translate = Vector3(base_data["translate"])
        self.rotate = Vector3(base_data["rotate"])
        self.check_null_field(msb_buffer, region_offset + base_data["unknown_offset_1"])
        self.check_null_field(msb_buffer, region_offset + base_data["unknown_offset_2"])

        if base_data["type_data_offset"] != 0:
            msb_buffer.seek(region_offset + base_data["type_data_offset"])
            self.unpack_type_data(msb_buffer)

        msb_buffer.seek(region_offset + base_data["entity_id_offset"])
        self.entity_id = struct.unpack("i", msb_buffer.read(4))[0]

        return region_offset + base_data["entity_id_offset"]

    def unpack_type_data(self, msb_buffer):
        # TODO: Use type struct.
        raise NotImplementedError

    def pack(self):
        name_offset = self.REGION_STRUCT.size
        packed_name = pad_chars(self.get_name_to_pack(), encoding="shift-jis", pad_to_multiple_of=4)
        unknown_offset_1 = name_offset + len(packed_name)
        unknown_offset_2 = unknown_offset_1 + 4
        packed_type_data = self.pack_type_data()
        if packed_type_data:
            type_data_offset = unknown_offset_2 + 4
            entity_id_offset = type_data_offset + len(packed_type_data)
        else:
            type_data_offset = 0
            entity_id_offset = unknown_offset_2 + 4
        packed_base_data = self.REGION_STRUCT.pack(
            name_offset=name_offset,
            region_index=self._region_index,
            region_type=self.ENTRY_SUBTYPE,
            translate=list(self.translate),
            rotate=list(self.rotate),
            unknown_offset_1=unknown_offset_1,
            unknown_offset_2=unknown_offset_2,
            type_data_offset=type_data_offset,
            entity_id_offset=entity_id_offset,
        )
        packed_entity_id = struct.pack("i", self.entity_id)
        return packed_base_data + packed_name + b"\0\0\0\0" * 2 + packed_type_data + packed_entity_id

    def pack_type_data(self):
        raise NotImplementedError

    def set_indices(self, region_index):
        self._region_index = region_index

    @staticmethod
    def check_null_field(msb_buffer, offset_to_null):
        msb_buffer.seek(offset_to_null)
        zero = msb_buffer.read(4)
        if zero != b"\0\0\0\0":
            _LOGGER.warning(f"Null data entry in MSB region was not zero: {zero}.")

    @staticmethod
    def auto_region_subclass(msb_buffer):
        old_offset = msb_buffer.tell()
        msb_buffer.seek(old_offset + 12)
        try:
            region_type = MSBRegionSubtype(struct.unpack("i", msb_buffer.read(4))[0])
        except (ValueError, TypeError):
            raise ValueError("Could not detect region subtype from MSB data.")
        msb_buffer.seek(old_offset)
        return MSB_REGION_TYPE_CLASSES[region_type](msb_buffer)


class MSBRegionPoint(BaseMSBRegion):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way will the
    player be facing when they spawn?)."""

    ENTRY_SUBTYPE = MSBRegionSubtype.Point

    def __init__(self, msb_region_shape_source=None, **kwargs):
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        """No data to unpack."""
        pass

    def pack_type_data(self):
        return b""


class MSBRegionCircle(BaseMSBRegion):
    """Almost never used (no volume)."""

    CIRCLE_STRUCT = (("radius", "f"),)

    FIELD_INFO = {
        **BaseMSBRegion.FIELD_INFO,
        "radius": ("Radius", True, float, "Radius (in xy-plane) of circular region.",),
    }

    ENTRY_SUBTYPE = MSBRegionSubtype.Circle

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        self.radius = BinaryStruct(*self.CIRCLE_STRUCT).unpack(msb_buffer)["radius"]

    def pack_type_data(self):
        return BinaryStruct(*self.CIRCLE_STRUCT).pack(radius=self.radius,)


class MSBRegionSphere(BaseMSBRegion):
    SPHERE_STRUCT = (("radius", "f"),)

    FIELD_INFO = {**BaseMSBRegion.FIELD_INFO, "radius": ("Radius", True, float, "Radius of sphere-shaped region.",)}

    ENTRY_SUBTYPE = MSBRegionSubtype.Sphere

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        self.radius = BinaryStruct(*self.SPHERE_STRUCT).unpack(msb_buffer)["radius"]

    def pack_type_data(self):
        return BinaryStruct(*self.SPHERE_STRUCT).pack(radius=self.radius,)


class MSBRegionCylinder(BaseMSBRegion):
    CYLINDER_STRUCT = (
        ("radius", "f"),
        ("height", "f"),
    )

    FIELD_INFO = {
        **BaseMSBRegion.FIELD_INFO,
        "radius": ("Radius", True, float, "Radius (in xz-plane) of cylinder-shaped region."),
        "height": ("Height", True, float, "Height (along y-axis) of cylinder-shaped region."),
    }

    ENTRY_SUBTYPE = MSBRegionSubtype.Cylinder

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        self.height = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.CYLINDER_STRUCT).unpack(msb_buffer)
        self.radius = data["radius"]
        self.height = data["height"]

    def pack_type_data(self):
        return BinaryStruct(*self.CYLINDER_STRUCT).pack(radius=self.radius, height=self.height,)


class MSBRegionRect(BaseMSBRegion):
    """Almost never used (no volume)."""

    RECT_STRUCT = (
        ("width", "f"),
        ("depth", "f"),
    )

    FIELD_INFO = {
        **BaseMSBRegion.FIELD_INFO,
        "width": ("Width", True, float, "Width (along x-axis) of rectangle-shaped region."),
        "height": ("Height", True, float, "Height (along y-axis) of rectangle-shaped region."),
    }

    ENTRY_SUBTYPE = MSBRegionSubtype.Rect

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.width = 1.0
        self.depth = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.RECT_STRUCT).unpack(msb_buffer)
        self.width = data["width"]
        self.depth = data["depth"]

    def pack_type_data(self):
        return BinaryStruct(*self.RECT_STRUCT).pack(width=self.width, depth=self.depth,)


class MSBRegionBox(BaseMSBRegion):
    BOX_STRUCT = (
        ("width", "f"),
        ("depth", "f"),
        ("height", "f"),
    )

    FIELD_INFO = {
        **BaseMSBRegion.FIELD_INFO,
        "width": ("Width", True, float, "Width (along x-axis) of box-shaped region."),
        "depth": ("Depth", True, float, "Depth (along z-axis) of box-shaped region."),
        "height": ("Height", True, float, "Height (along y-axis) of box-shaped region."),
    }

    ENTRY_SUBTYPE = MSBRegionSubtype.Box

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.width = 1.0
        self.depth = 1.0
        self.height = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.BOX_STRUCT).unpack(msb_buffer)
        self.width = data["width"]
        self.depth = data["depth"]
        self.height = data["height"]

    def pack_type_data(self):
        return BinaryStruct(*self.BOX_STRUCT).pack(
            width=float(self.width), depth=float(self.depth), height=float(self.height)
        )


MSB_REGION_TYPE_CLASSES = {
    MSBRegionSubtype.Point: MSBRegionPoint,
    MSBRegionSubtype.Circle: MSBRegionCircle,
    MSBRegionSubtype.Sphere: MSBRegionSphere,
    MSBRegionSubtype.Cylinder: MSBRegionCylinder,
    MSBRegionSubtype.Rect: MSBRegionRect,
    MSBRegionSubtype.Box: MSBRegionBox,
}


class MSBRegionList(MSBEntryList[BaseMSBRegion]):
    ENTRY_LIST_NAME = "Regions"
    ENTRY_CLASS = staticmethod(MSBRegion)
    ENTRY_SUBTYPE_ENUM = MSBRegionSubtype

    _entries: tp.List[BaseMSBRegion]

    Points: tp.Sequence[MSBRegionPoint]
    Circles: tp.Sequence[MSBRegionCircle]
    Spheres: tp.Sequence[MSBRegionSphere]
    Cylinders: tp.Sequence[MSBRegionCylinder]
    Rectangles: tp.Sequence[MSBRegionRect]
    Boxes: tp.Sequence[MSBRegionBox]

    def add_region(self, region_type, dimensions=None, **kwargs):
        region_type = self.resolve_entry_subtype(region_type)
        if dimensions is not None:
            if region_type == MSBRegionSubtype.Box:
                if "width" in kwargs or "depth" in kwargs or "height" in kwargs:
                    raise ValueError("Cannot use `dimensions` argument in addition to `width`, `depth`, or `height`.")
                try:
                    kwargs["width"], kwargs["depth"], kwargs["height"] = dimensions
                except ValueError:
                    raise ValueError(f"`dimensions` argument for Box must be (width, depth, height) sequence.")
            elif region_type == MSBRegionSubtype.Cylinder:
                if "radius" in kwargs or "height" in kwargs:
                    raise ValueError("Cannot use `dimensions` argument in addition to `radius` or `height`.")
                try:
                    kwargs["radius"], kwargs["height"] = dimensions
                except ValueError:
                    raise ValueError(f"`dimensions` argument for Cylinder must be (radius, height) sequence.")
            else:
                raise ValueError("Can only use `dimensions` argument for Box or Cylinder region.")
        self.add_entry(
            MSB_REGION_TYPE_CLASSES[region_type](**kwargs), append_to_entry_subtype=region_type,
        )

    def get_subtype_instance(self, entry_subtype, **kwargs):
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        entry_class = MSB_REGION_TYPE_CLASSES[entry_subtype]
        return entry_class(msb_region_shape_source=None, **kwargs)

    def set_indices(self):
        """Global region index only."""
        for i, entry in enumerate(self._entries):
            entry.set_indices(region_index=i)
