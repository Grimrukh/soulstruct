import abc
import typing as tp
import logging
import struct
from io import BufferedReader, BytesIO

from soulstruct.maps.enums import MSBRegionSubtype
from soulstruct.maps.base.msb_entry import MSBEntryList, MSBEntryEntityCoordinates
from soulstruct.utilities import read_chars_from_buffer, pad_chars, unpack_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct
from soulstruct.utilities.maths import Vector3

_LOGGER = logging.getLogger(__name__)


class MSBRegion(MSBEntryEntityCoordinates, abc.ABC):

    REGION_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""  # type: str
    UNKNOWN_DATA_SIZE = -1  # type: int

    REGION_TYPE_DATA_STRUCT = ()

    FIELD_INFO = {
        "translate": (
            "Translate",
            Vector3,
            "3D coordinates of the region's position. Note that this is the middle of the bottom face for box "
            "regions.",
        ),
        "rotate": (
            "Rotate",
            Vector3,
            "Euler angles for region rotation around its local X, Y, and Z axes.",
        ),
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the region in other game files.",
        ),
    }

    ENTRY_SUBTYPE = None  # type: MSBRegionSubtype

    def __init__(self, msb_region_source=None):
        super().__init__()
        self._region_index = None  # Final automatic assignment done on `MSB.pack()`.

        if isinstance(msb_region_source, bytes):
            msb_region_source = BytesIO(msb_region_source)
        if isinstance(msb_region_source, (BufferedReader, BytesIO)):
            self.unpack(msb_region_source)
        elif msb_region_source is not None:
            raise TypeError("`msb_model_source` must be a buffer, `bytes`, or `None`.")

    def unpack(self, msb_buffer):
        region_offset = msb_buffer.tell()
        base_data = self.REGION_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=region_offset + base_data["name_offset"], encoding=self.NAME_ENCODING,
        )
        self._region_index = base_data["__region_index"]
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

    def pack(self, region_index=0):
        name_offset = self.REGION_STRUCT.size
        packed_name = pad_chars(self.get_name_to_pack(), encoding=self.NAME_ENCODING, pad_to_multiple_of=4)
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
            __region_index=region_index,
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

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.REGION_TYPE_DATA_STRUCT).unpack(msb_buffer)
        self.set(**data)

    def pack_type_data(self):
        return BinaryStruct(*self.REGION_TYPE_DATA_STRUCT).pack_from_object(self)

    def set_indices(self, region_index):
        self._region_index = region_index

    @classmethod
    def check_null_field(cls, msb_buffer, offset_to_null):
        msb_buffer.seek(offset_to_null)
        zero = msb_buffer.read(cls.UNKNOWN_DATA_SIZE)
        if zero != b"\0" * cls.UNKNOWN_DATA_SIZE:
            _LOGGER.warning(f"Null data entry in `{cls.__name__}` was not zero: {zero}.")


class MSBRegionPoint(MSBRegion, abc.ABC):
    """No shape attributes. Note that the rotate attribute is still meaningful for many uses (e.g. what way will the
    player be facing when they spawn?)."""

    REGION_TYPE_DATA_STRUCT = ()

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Point

    def __init__(self, msb_region_shape_source=None, **kwargs):
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        pass

    def pack_type_data(self):
        return b""


class MSBRegionCircle(MSBRegion, abc.ABC):
    """Almost never used (no volume)."""

    REGION_TYPE_DATA_STRUCT = (
        ("radius", "f"),
    )

    FIELD_INFO = {
        **MSBRegion.FIELD_INFO,
        "radius": (
            "Radius",
            float,
            "Radius (in xy-plane) of circular region.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Circle

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)


class MSBRegionSphere(MSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = (
        ("radius", "f"),
    )

    FIELD_INFO = {
        **MSBRegion.FIELD_INFO,
        "radius": (
            "Radius",
            float,
            "Radius of sphere-shaped region.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Sphere

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)


class MSBRegionCylinder(MSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = (
        ("radius", "f"),
        ("height", "f"),
    )

    FIELD_INFO = {
        **MSBRegion.FIELD_INFO,
        "radius": (
            "Radius",
            float,
            "Radius (in xz-plane) of cylinder-shaped region.",
        ),
        "height": (
            "Height",
            float,
            "Height (along y-axis) of cylinder-shaped region.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "radius",
        "height",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Cylinder

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.radius = 1.0
        self.height = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)


class MSBRegionRect(MSBRegion, abc.ABC):
    """Almost never used (no volume)."""

    REGION_TYPE_DATA_STRUCT = (
        ("width", "f"),
        ("depth", "f"),
    )

    FIELD_INFO = {
        **MSBRegion.FIELD_INFO,
        "width": (
            "Width",
            float,
            "Width (along x-axis) of rectangle-shaped region.",
        ),
        "height": (
            "Height",
            float,
            "Height (along y-axis) of rectangle-shaped region.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "width",
        "height",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Rect

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.width = 1.0
        self.depth = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)


class MSBRegionBox(MSBRegion, abc.ABC):
    REGION_TYPE_DATA_STRUCT = (
        ("width", "f"),
        ("depth", "f"),
        ("height", "f"),
    )

    FIELD_INFO = {
        **MSBRegion.FIELD_INFO,
        "width": (
            "Width",
            float,
            "Width (along x-axis) of box-shaped region.",
        ),
        "depth": (
            "Depth",
            float,
            "Depth (along z-axis) of box-shaped region.",
        ),
        "height": (
            "Height",
            float,
            "Height (along y-axis) of box-shaped region.",
        ),
    }

    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "width",
        "depth",
        "height",
    )

    ENTRY_SUBTYPE = MSBRegionSubtype.Box

    def __init__(self, msb_region_shape_source=None, **kwargs):
        self.width = 1.0
        self.depth = 1.0
        self.height = 1.0
        super().__init__(msb_region_shape_source)
        self.set(**kwargs)


class MSBRegionList(MSBEntryList[MSBRegion], abc.ABC):
    ENTRY_LIST_NAME = "Regions"
    ENTRY_SUBTYPE_ENUM = MSBRegionSubtype

    REGION_SUBTYPE_CLASSES = {}  # type: dict[MSBRegionSubtype, type]
    REGION_SUBTYPE_OFFSET = -1  # type: int

    _entries: tp.List[MSBRegion]

    Points: tp.Sequence[MSBRegionPoint]
    Circles: tp.Sequence[MSBRegionCircle]
    Spheres: tp.Sequence[MSBRegionSphere]
    Cylinders: tp.Sequence[MSBRegionCylinder]
    Rectangles: tp.Sequence[MSBRegionRect]
    Boxes: tp.Sequence[MSBRegionBox]

    def pack_entry(self, index: int, entry: MSBRegion):
        return entry.pack(index)

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
            self.REGION_SUBTYPE_CLASSES[region_type](**kwargs), append_to_entry_subtype=region_type,
        )

    def get_subtype_instance(self, entry_subtype, **kwargs):
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        entry_class = self.REGION_SUBTYPE_CLASSES[entry_subtype]
        return entry_class(msb_region_shape_source=None, **kwargs)

    def set_indices(self):
        """Global region index only."""
        for i, entry in enumerate(self._entries):
            entry.set_indices(region_index=i)

    @classmethod
    def MSBRegion(cls, msb_buffer):
        """Detects the appropriate subclass of `MSBRegion` to instantiate, and does so."""
        event_type_int = unpack_from_buffer(msb_buffer, "i", offset=cls.REGION_SUBTYPE_OFFSET, relative_offset=True)[0]
        event_type = MSBRegionSubtype(event_type_int)
        return cls.REGION_SUBTYPE_CLASSES[event_type](msb_buffer)

    ENTRY_CLASS = MSBRegion


for _entry_subtype in MSBRegionList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBRegionList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
