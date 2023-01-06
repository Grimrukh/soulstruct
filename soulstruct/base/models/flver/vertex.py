from __future__ import annotations

__all__ = [
    "MemberType",
    "MemberFormat",
    "LayoutMember",
    "BufferLayout",
    "Vertex",
    "VertexBufferSizeError",
    "VertexBuffer",
]

import logging
import struct
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter
from soulstruct.utilities.maths import Vector3

from .version import Version

_LOGGER = logging.getLogger(__name__)


class MemberType(IntEnum):
    """Data type of a `Vertex` property."""
    Position = 0  # vertex position
    BoneWeights = 1  # weight of the attached bones
    BoneIndices = 2  # bones to which the vertex is attached (indices of the parent mesh's bone indices)
    Normal = 3  # orientation
    UV = 5  # texture coordinates
    Tangent = 6  # perpendicular to normal
    Bitangent = 7  # perpendicular to normal and tangent
    VertexColor = 10  # blending, alpha, etc.

    def unique(self):
        """If `True`, this `LayoutFormat` must only appear in one `LayoutMember` per `Mesh`."""
        return self in {self.BoneWeights, self.BoneIndices, self.Bitangent}


class MemberFormat(IntEnum):
    """Data format of a `Vertex` property."""
    Float2 = 0x01
    Float3 = 0x02
    Float4 = 0x03
    Byte4A = 0x10
    Byte4B = 0x11
    Short2toFloat2 = 0x12
    Byte4C = 0x13
    UV = 0x15  # two shorts
    UVPair = 0x16
    ShortBoneIndices = 0x18
    Short4ToFloat4A = 0x1A
    Short4ToFloat4B = 0x2E
    Byte4E = 0x2F
    EdgeCompressed = 0xF0

    def size(self):
        if self == self.EdgeCompressed:
            return 1
        elif self.name.startswith("Byte") or self in {self.UV, self.Short2toFloat2}:
            return 4
        elif self.name.startswith("Short") or self in {self.Float2, self.UVPair}:
            return 8
        elif self == self.Float3:
            return 12
        elif self == self.Float4:
            return 16
        raise ValueError(f"Could not compute size of unknown `LayoutType`: {self.name}")


class LayoutMember(BinaryObject):

    STRUCT = BinaryStruct(
        ("unk_x00", "i"),  # always zero in DS1 at least
        ("__struct_offset", "i"),  # validated, but not needed
        ("member_format", "i"),
        ("member_type", "i"),
        ("index", "i"),  # instance index of this `type` in this `BufferLayout`
    )
    DEFAULTS = {
        "unk_x00": 0,
        "index": 0,
    }

    unk_x00: int
    member_format: MemberFormat
    member_type: MemberType
    index: int

    def __init__(
        self, reader: BinaryReader = None, **kwargs
    ):
        if reader is None:
            if "member_type" not in kwargs or "member_format" not in kwargs:
                raise ValueError(
                    "`member_type` and `member_format` must be given to `MemberLayout()` if `reader` not given."
                )
            self.member_type = kwargs.pop("member_type")
            self.member_format = kwargs.pop("member_format")
        super().__init__(reader, **kwargs)

    def unpack(self, reader: BinaryReader, struct_offset: int):
        layout_member = reader.unpack_struct(self.STRUCT)
        binary_struct_offset = layout_member.pop("__struct_offset")
        if struct_offset != binary_struct_offset:
            raise ValueError(
                f"`LayoutMember` binary struct offset ({binary_struct_offset}) does not match passed struct offset "
                f"({struct_offset})."
            )
        self.set(**layout_member)

    def pack(self, writer: BinaryWriter, struct_offset: int):
        writer.pack_struct(
            self.STRUCT,
            self,
            __struct_offset=struct_offset,
        )

    def __eq__(self, other: LayoutMember):
        return (
            self.unk_x00 == other.unk_x00
            and self.member_format == other.member_format
            and self.member_type == other.member_type
        )

    def __repr__(self):
        return f"{self.member_type.name}<{self.size}, {self.member_format.name}>"

    @property
    def size(self) -> int:
        return self.member_format.size()


# region Buffer Parser Callbacks
def _int_to_float(scale: float, make_signed=False) -> (tp.Callable, tp.Callable):
    if make_signed:
        def read_func(v: tuple[int, ...]):
            return [(x - scale) / scale for x in v]

        def write_func(d: list[float]):
            return [int(x * scale + scale) for x in d]
    else:
        def read_func(v: tuple[int, ...]):
            return [x / scale for x in v]

        def write_func(d: list[float]):
            return [int(x * scale) for x in d]
    return read_func, write_func


def _int_to_float_normal(v: tuple[int, int, int, int]) -> list[float, float, float, float]:
    """Does not un-quantize fourth element."""
    return [(x - 127) / 127.0 for x in v[:3]] + [float(v[3])]


def _float_to_int_normal(d: list[float, float, float, float]) -> list[int, int, int, int]:
    """Does not quantize fourth element."""
    return [int(d[0] * 127 + 127), int(d[1] * 127 + 127), int(d[2] * 127 + 127), int(d[3])]


def _two_shorts_to_one_uv(v: tuple[int, int]) -> list[list[float]]:
    return [[float(v[0]), float(v[1]), 0.0]]


def _one_uv_to_two_shorts(d: list[float]) -> list[int, int]:
    return [int(d[0]), int(d[1])]


def _four_shorts_to_one_uv(v: tuple[int, int, int, int]) -> list[list[float]]:
    if v[3] != 0:
        raise ValueError("Expected fourth short to be zero in reading UV | Short4ToFloat4B vertex member.")
    return [[float(v[0]), float(v[1]), float(v[2])]]


def _one_uv_to_four_shorts(d: list[float]) -> list[int, int, int, int]:
    return [int(d[0]), int(d[1]), int(d[2]), 0]


def _four_shorts_to_two_uvs(v: tuple[int, int, int, int]) -> list[list[float], list[float]]:
    return [[float(v[0]), float(v[1]), 0.0], [float(v[2]), float(v[3]), 0.0]]


def _four_floats_to_two_uvs(v: tuple[float, float, float, float]) -> list[list[float], list[float]]:
    return [[v[0], v[1], 0.0], [v[2], v[3], 0.0]]


def _one_uv_to_two_floats(d: list[float]) -> list[float, float]:
    return [d[0], d[1]]
# endregion


class LayoutMemberInfo(tp.NamedTuple):
    attr: str
    fmt: str
    size: int
    read_callback: tp.Callable = None  # converts `struct.unpack` output tuples to attribute lists (default is `list()`)
    write_callback: tp.Callable = None  # converts attribute lists to `v` as in `struct.pack(fmt, *v)` (default skipped)
    has_two_uvs: bool = False


# Maps `(LayoutFormat, LayoutType)` key pairs (nested) to `(name, fmt, size, callback)` quadruples.
# Note that the layout is aware that `uvs`, `tangents`, and `colors` attributes are lists; `+=` will be used on the
# callback result in these cases.
LAYOUT_PARSER = {
    MemberType.Position: {
        MemberFormat.Float3: LayoutMemberInfo("position", "3f", 3),
        MemberFormat.Float4: LayoutMemberInfo(
            "position", "4f", 4,
            lambda v: [v[0], v[1], v[2]],
            lambda d: (d[0], d[1], d[2], 0.0),
        ),
        # LayoutType.EdgeCompressed is explicitly not supported.
    },
    MemberType.BoneWeights: {
        MemberFormat.Byte4A: LayoutMemberInfo("bone_weights", "4b", 4, *_int_to_float(127.0)),
        MemberFormat.Byte4C: LayoutMemberInfo("bone_weights", "4B", 4, *_int_to_float(255.0)),
        MemberFormat.UVPair: LayoutMemberInfo("bone_weights", "4h", 4, *_int_to_float(32767.0)),
        MemberFormat.Short4ToFloat4A: LayoutMemberInfo("bone_weights", "4h", 4, *_int_to_float(32767.0)),
    },
    MemberType.BoneIndices: {
        MemberFormat.Byte4B: LayoutMemberInfo("bone_indices", "4B", 4),
        MemberFormat.Byte4E: LayoutMemberInfo("bone_indices", "4B", 4),
        MemberFormat.ShortBoneIndices: LayoutMemberInfo("bone_indices", "4h", 4),
    },
    MemberType.Normal: {
        MemberFormat.Float3: LayoutMemberInfo(
            "normal", "3f", 3,
            lambda v: [v[0], v[1], v[2], -1.0],
            lambda d: [d[0], d[1], d[2]],
        ),
        MemberFormat.Float4: LayoutMemberInfo("normal", "4f", 4),
        # Note that we don't modify `w` in any of these quantization cases, except to make it a `float`.
        MemberFormat.Byte4A: LayoutMemberInfo("normal", "4B", 4, _int_to_float_normal, _float_to_int_normal),
        MemberFormat.Byte4B: LayoutMemberInfo("normal", "4B", 4, _int_to_float_normal, _float_to_int_normal),
        MemberFormat.Byte4C: LayoutMemberInfo("normal", "4B", 4, _int_to_float_normal, _float_to_int_normal),
        MemberFormat.Byte4E: LayoutMemberInfo("normal", "4B", 4, _int_to_float_normal, _float_to_int_normal),
        MemberFormat.Short2toFloat2: LayoutMemberInfo(
            "normal", "B3b", 4,
            lambda v: [v[1] / 127.0, v[2] / 127.0, v[3] / 127.0, v[0]],  # packed in `wxyz` order
            lambda d: [d[3], int(d[0] * 127), int(d[1] * 127), int(d[2] * 127)],
        ),
        MemberFormat.Short4ToFloat4A: LayoutMemberInfo(
            "normal", "4h", 4,
            lambda v: [v[0] / 32767.0, v[1] / 32767.0, v[2] / 32767.0, float(v[3])],
            lambda d: [int(d[0] * 32767), int(d[1] * 32767), int(d[2] * 32767), int(d[3])],
        ),
        MemberFormat.Short4ToFloat4B: LayoutMemberInfo(
            "normal", "3Hh", 4,
            lambda v: [(v[0] - 32767) / 32767.0, (v[1] - 32767) / 32767.0, (v[2] - 32767) / 32767.0, float(v[3])],
            lambda d: [int(d[0] * 32767 + 32767), int(d[1] * 32767 + 32767), int(d[2] * 32767 + 32767), int(d[3])],
        ),
    },
    MemberType.UV: {
        # UV read callbacks return a list of 1-2 UV lists, but write callbacks still process one UV list at a time.
        # Writer will detect `Float4` and `UVPair` types are write two queued UVs (in reverse order) as needed.
        MemberFormat.Float2: LayoutMemberInfo("uvs", "2f", 2, lambda v: [[*v, 0.0]], lambda d: [d[0], d[1]]),
        MemberFormat.Float3: LayoutMemberInfo("uvs", "3f", 3, lambda v: [list(v)]),
        MemberFormat.Float4: LayoutMemberInfo(
            "uvs", "4f", 4, _four_floats_to_two_uvs, _one_uv_to_two_floats, has_two_uvs=True
        ),
        # All types below this will have their UVs divided by local `uv_factor` by the unpacker.
        MemberFormat.Byte4A: LayoutMemberInfo("uvs", "2h", 2, _two_shorts_to_one_uv, _one_uv_to_two_shorts),
        MemberFormat.Byte4B: LayoutMemberInfo("uvs", "2h", 2, _two_shorts_to_one_uv, _one_uv_to_two_shorts),
        MemberFormat.Short2toFloat2: LayoutMemberInfo("uvs", "2h", 2, _two_shorts_to_one_uv, _one_uv_to_two_shorts),
        MemberFormat.Byte4C: LayoutMemberInfo("uvs", "2h", 2, _two_shorts_to_one_uv, _one_uv_to_two_shorts),
        MemberFormat.UV: LayoutMemberInfo("uvs", "2h", 2, _two_shorts_to_one_uv, _one_uv_to_two_shorts),
        MemberFormat.UVPair: LayoutMemberInfo(
            "uvs", "4h", 4, _four_shorts_to_two_uvs, _one_uv_to_two_shorts, has_two_uvs=True
        ),
        MemberFormat.Short4ToFloat4B: LayoutMemberInfo("uvs", "4h", 4, _four_shorts_to_one_uv, _one_uv_to_four_shorts),
    },
    MemberType.Tangent: {
        MemberFormat.Float4: LayoutMemberInfo("tangents", "4f", 4),
        MemberFormat.Byte4A: LayoutMemberInfo("tangents", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4B: LayoutMemberInfo("tangents", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4C: LayoutMemberInfo("tangents", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4E: LayoutMemberInfo("tangents", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Short4ToFloat4A: LayoutMemberInfo("tangents", "4B", 4, *_int_to_float(127.0, make_signed=True)),
    },
    MemberType.Bitangent: {
        MemberFormat.Byte4A: LayoutMemberInfo("bitangent", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4B: LayoutMemberInfo("bitangent", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4C: LayoutMemberInfo("bitangent", "4B", 4, *_int_to_float(127.0, make_signed=True)),
        MemberFormat.Byte4E: LayoutMemberInfo("bitangent", "4B", 4, *_int_to_float(127.0, make_signed=True)),
    },
    MemberType.VertexColor: {
        MemberFormat.Float4: LayoutMemberInfo("colors", "4f", 4),
        MemberFormat.Byte4A: LayoutMemberInfo("colors", "4B", 4, *_int_to_float(255.0)),
        MemberFormat.Byte4C: LayoutMemberInfo("colors", "4B", 4, *_int_to_float(255.0)),
    },
}


USES_UV_FACTOR = {
    MemberFormat.Byte4A,
    MemberFormat.Byte4B,
    MemberFormat.Short2toFloat2,
    MemberFormat.Byte4C,
    MemberFormat.UV,
    MemberFormat.UVPair,
    MemberFormat.Short4ToFloat4B,
}


class BufferLayout:

    STRUCT = BinaryStruct(
        ("__member_count", "i"),
        "8x",
        ("__member_offset", "i"),
    )

    members: list[LayoutMember]

    def __init__(self, source: BinaryReader | list[LayoutMember]):
        self.members = []

        if isinstance(source, BinaryReader):
            self.unpack(source)
        elif isinstance(source, (list, tuple)) and all(isinstance(e, LayoutMember) for e in source):
            self.members = source
        else:
            raise TypeError(f"`BufferLayout` source must be a binary reader or list of `LayoutMember`s, not {source}.")

    def unpack(self, reader: BinaryReader):
        buffer_layout = reader.unpack_struct(self.STRUCT)

        with reader.temp_offset(buffer_layout.pop("__member_offset")):
            struct_offset = 0
            self.members = []
            for _ in range(buffer_layout.pop("__member_count")):
                member = LayoutMember(reader, struct_offset=struct_offset)
                self.members.append(member)
                struct_offset += member.member_format.size()

    def pack(self, writer: BinaryWriter):
        writer.pack_struct(
            self.STRUCT,
            self,
            __member_count=len(self.members),
            __member_offset=writer.AUTO_RESERVE,
        )

    def pack_members(self, writer: BinaryWriter):
        writer.fill("__member_offset", writer.position, obj=self)
        struct_offset = 0
        for member in self.members:
            member.pack(writer, struct_offset)
            struct_offset += member.size

    def has_member_type(self, member_type: MemberType) -> bool:
        return any(member.member_type == member_type for member in self.members)

    def get_uv_count(self):
        """Return total number of UV slots."""
        count = 0
        for member in self.members:
            if member.member_type == MemberType.UV:
                if member.member_format == MemberFormat.UV:
                    count += 1
                elif member.member_format == MemberFormat.UVPair:
                    count += 2
        return count

    def get_vertex_read_function(self, uv_factor: int) -> tp.Callable[[BinaryReader, Vertex], None]:
        """Construct a relatively efficient function that can be used to read data for each `Vertex` whose data lies
        in a `VertexBuffer` with this layout."""

        member_infos = []  # type: list[LayoutMemberInfo]
        full_fmt = ""  # fmt of data to read

        for member in self.members:

            if member.member_type == MemberType.Position and member.member_format == MemberFormat.EdgeCompressed:
                # Explicitly not supported.
                raise NotImplementedError("Cannot read FLVERs with edge-compressed vertex positions.")
            if member.member_type not in LAYOUT_PARSER:
                raise ValueError(f"Invalid vertex buffer layout member type: {member.member_type}")

            type_parser = LAYOUT_PARSER[member.member_type]
            if member.member_format not in type_parser:
                raise NotImplementedError(f"Unsupported vertex buffer layout member type/format: {member}")

            member_info = type_parser[member.member_format]

            # Modify UV callbacks with scale factor, if appropriate.
            if member.member_type == MemberType.UV and member.member_format in USES_UV_FACTOR:
                def scaled_uv_callback(v, info=member_info):  # this `member_info` baked in
                    return [[x / uv_factor for x in uv_list] for uv_list in info.read_callback(v)]

                member_info = LayoutMemberInfo(
                    member_info.attr, member_info.fmt, member_info.size, read_callback=scaled_uv_callback
                )

            member_infos.append(member_info)
            full_fmt += member_info.fmt

        def read_vertex_data(reader: BinaryReader, vertex: Vertex):
            vertex.raw = reader.read(struct.calcsize("<" + full_fmt))
            data = struct.unpack("<" + full_fmt, vertex.raw)
            index = 0
            for info in member_infos:
                raw_value = data[index:index + info.size]  # raw tuple
                value = info.read_callback(raw_value) if info.read_callback is not None else list(raw_value)
                if info.attr == "uvs":
                    vertex.uvs += value  # extend with list of one/two UV lists
                elif info.attr == "tangents":
                    vertex.tangents.append(value)
                elif info.attr == "colors":
                    vertex.colors.append(value)
                else:
                    setattr(vertex, info.attr, value)
                index += info.size

        return read_vertex_data

    def get_vertex_write_function(self, uv_factor: int) -> tp.Callable[[BinaryWriter, Vertex], None]:
        """Construct a relatively efficient function that can be used to write data for each `Vertex` into a packed
        `VertexBuffer` with this layout."""

        member_infos = []  # type: list[LayoutMemberInfo]
        full_fmt = ""  # fmt of data to read

        for member in self.members:

            if member.member_type == MemberType.Position and member.member_format == MemberFormat.EdgeCompressed:
                # Explicitly not supported.
                raise NotImplementedError("Cannot write FLVERs with edge-compressed vertex positions.")
            if member.member_type not in LAYOUT_PARSER:
                raise ValueError(f"Invalid vertex buffer layout member type: {member.member_type}")

            type_parser = LAYOUT_PARSER[member.member_type]
            if member.member_format not in type_parser:
                raise NotImplementedError(f"Unsupported vertex buffer layout member type/format: {member}")

            member_info = type_parser[member.member_format]

            # Modify UV callbacks with scale factor, if appropriate.
            if member.member_type == MemberType.UV and member.member_format in USES_UV_FACTOR:
                def scaled_uv_callback(d, info=member_info):  # this `member_info` baked in
                    return info.write_callback([x * uv_factor for x in d])

                member_info = LayoutMemberInfo(
                    member_info.attr, member_info.fmt, member_info.size,
                    write_callback=scaled_uv_callback,
                    has_two_uvs=member_info.has_two_uvs,
                )

            member_infos.append(member_info)
            full_fmt += member_info.fmt

        def write_vertex_data(writer: BinaryWriter, vertex: Vertex):

            # TODO: Change write callbacks to return lists for faster extending here.
            values = []
            for info in member_infos:

                if info.attr == "uvs":
                    try:
                        uv1 = vertex.uv_queue.pop()
                    except IndexError:
                        raise IndexError("Ran out of vertex UVs to buffer.")
                    values += info.write_callback(uv1) if info.write_callback else uv1
                    if info.has_two_uvs:
                        try:
                            uv2 = vertex.uv_queue.pop()
                        except IndexError:
                            raise IndexError("Ran out of vertex UVs to buffer.")
                        values += info.write_callback(uv2) if info.write_callback else uv2
                elif info.attr == "tangents":
                    try:
                        tangent = vertex.tangent_queue.pop()
                    except IndexError:
                        raise IndexError("Ran out of vertex tangents to buffer.")
                    values += info.write_callback(tangent) if info.write_callback else tangent
                elif info.attr == "colors":
                    try:
                        color = vertex.color_queue.pop()
                    except IndexError:
                        raise IndexError("Ran out of vertex colors to buffer.")
                    values += info.write_callback(color) if info.write_callback else color
                else:
                    value = getattr(vertex, info.attr)
                    values += info.write_callback(value) if info.write_callback else value

            try:
                writer.pack("<" + full_fmt, *values)
            except struct.error:
                raise ValueError(
                    f"Could not pack vertex data.\n"
                    f"    Info: {member_infos}\n"
                    f"    Format: {full_fmt}\n"
                    f"    Values: {values}"
                )

        return write_vertex_data

    def __hash__(self):
        return hash(", ".join(str(m) for m in self.members))

    def __eq__(self, other: BufferLayout):
        return self.members == other.members

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index):
        return self.members[index]

    def __len__(self):
        return len(self.members)

    def get_total_size(self):
        return sum(member.member_format.size() for member in self.members)

    def __repr__(self):
        members = "\n        ".join(repr(m) for m in self.members)
        return (
            f"BufferLayout(\n"
            f"    size = {self.get_total_size()}\n"
            f"    members = [\n        {members}\n    ]\n"
            f")"
        )


@dataclass(slots=True)
class Vertex:
    """A single mesh vertex.

    This class used to store its data in `Vector` and `Color` classes, but in Python, all that instantiation gets real
    expensive real quick for large meshes. All data is now stored as lists of floats (ints for `bone_indices`). If you
    assign a `Vector` to them, it will work fine, as long as it supports sequence iteration and has the right length.

    Note that multiple values (lists of floats) are supported for `uvs`, `tangents`, and `colors`, though most buffer
    layouts will only have one of each.

    Also note that the fourth element of `normal` is used as an (integer) index for binding to a single bone in some
    cases. It is not part of the actual 3D normal vector.
    """
    DEFAULT_NORMAL_W = 127.0

    position: list[float] = field(default_factory=lambda: [0.0] * 3)
    bone_weights: list[float] = field(default_factory=lambda: [0.0] * 4)
    bone_indices: list[int] = field(default_factory=lambda: [0] * 4)
    # NOTE: `normal[3]` can be used to bind to a single bone (as an `int`).
    normal: list[float] = field(default_factory=lambda: [0.0] * 4)
    # NOTE: proportion of 1024 (pre-`DarkSouls2_NT`) or 2048
    uvs: list[list[float]] = field(default_factory=list)
    tangents: list[list[float]] = field(default_factory=list)
    bitangent: list[float] = field(default_factory=lambda: [0.0] * 4)
    colors: list[list[float]] = field(default_factory=list)

    raw: bytes = field(default=b"", init=False, repr=False)
    uv_queue: list[list[float]] = field(default_factory=list, init=False, repr=False)
    tangent_queue: list[list[float]] = field(default_factory=list, init=False, repr=False)
    color_queue: list[list[float]] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self):
        if len(self.normal) == 3:
            self.normal = [*self.normal, self.DEFAULT_NORMAL_W]

    @property
    def normal_xyz(self) -> list[float]:
        """Get XYZ of `_normal` as a three-float list, which is suitable for most uses."""
        return self.normal[:3]

    @normal_xyz.setter
    def normal_xyz(self, value: Vector3 | tuple | list):
        """Set XYZ of `normal`."""
        if len(value) == 3:
            self.normal = [*value, self.normal[3]]  # keep current `w`
        else:
            raise TypeError(f"`Vertex.normal_xyz` can only be set to a 3-length sequence/vector, not: {value}")

    @property
    def normal_w(self) -> int:
        """Get `_normal[3]` as an `int`, which is sometimes used to bind the `Vertex` to a single bone."""
        return int(self.normal[3])

    @normal_w.setter
    def normal_w(self, value: float | int):
        self.normal[3] = float(value)

    def clear_lists(self):
        self.uvs = []
        self.tangents = []
        self.colors = []

    def prepare_pack(self):
        """Queue list types so they can be properly split across buffers."""
        self.uv_queue = list(reversed(self.uvs))
        self.tangent_queue = list(reversed(self.tangents))
        self.color_queue = list(reversed(self.colors))

    def finish_pack(self):
        """Check queues are empty."""
        if self.uv_queue:
            raise ValueError(f"{len(self.uv_queue)} UVs left in vertex queue after it was packed.")
        if self.tangent_queue:
            raise ValueError(f"{len(self.tangent_queue)} tangents left in vertex queue after it was packed.")
        if self.color_queue:
            raise ValueError(f"{len(self.color_queue)} vertex colors left in vertex queue after it was packed.")

    def repr_position_only(self):
        return f"Vertex({self.position[0]}, {self.position[1]}, {self.position[2]})"

    def __repr__(self):
        """Omits default/empty values."""
        lines = [f"    position = {self.position},"]
        if any(self.bone_weights):
            lines += [f"    bone_weights = {self.bone_weights},"]
        if any(self.bone_indices) or any(self.bone_weights):
            lines += [f"    bone_indices = {self.bone_indices},"]
        lines += [f"    normal = {self.normal},"]
        if self.normal_w != 127:
            lines += [f"    normal_w = {self.normal_w},"]
        lines += [f"    uvs = {self.uvs},"]
        lines += [f"    tangents = {self.tangents},"]
        if any(self.bitangent):
            lines += [f"    bitangent = {self.bitangent},"]
        if any(c != 1.0 for v in self.colors for c in v):
            lines += [f"    colors = {self.colors},"]
        return "Vertex(\n" + "\n".join(lines) + "\n)"


class VertexBufferSizeError(SoulstructError):
    """Raised by some vanilla meshes."""

    def __init__(self, vertex_size: int, layout_size: int):
        self.vertex_size = vertex_size
        self.layout_size = layout_size
        super().__init__(
            f"Vertex buffer vertex size {vertex_size} not equal to size calculated from layout: {layout_size}."
        )


class VertexBuffer(BinaryObject):
    """Header for a block of vertex data for one mesh.

    The structure of each vertex's data is defined by the indexed `BufferLayout`.
    """

    STRUCT = BinaryStruct(
        ("_buffer_index", "i"),
        ("layout_index", "i"),
        ("_vertex_size", "i"),
        ("vertex_count", "i"),
        "8x",
        ("_buffer_length", "i"),
        ("_buffer_offset", "i"),
    )

    layout_index: int
    vertex_count: int

    _buffer_index: int
    _vertex_size: int
    _buffer_length: int
    _buffer_offset: int

    unpack = BinaryObject.default_unpack

    def read_buffer(
        self,
        reader: BinaryReader,
        layouts: list[BufferLayout],
        vertices: list[Vertex],
        vertex_data_offset: int,
        uv_factor: int,
    ):
        layout = layouts[self.layout_index]
        layout_size = layout.get_total_size()
        expected_vertex_size = self._buffer_length / self.vertex_count
        if self._vertex_size != expected_vertex_size:
            raise ValueError(
                f"Vertex buffer size ({self._vertex_size}) != buffer length / vertex count ({expected_vertex_size})."
            )
        if self._vertex_size != layout_size:
            # This happens for a few vanilla meshes; we ignore such meshes.
            # TODO: I've looked at the buffer data for mesh 0 of m8000B2A10, and it appears very abnormal. In fact,
            #  some of the 28-byte data clusters appear to just be counting upward as integers; there definitely does
            #  not seem to be any position float data in there. Later on, they appear to change into random shorts.
            raise VertexBufferSizeError(self._vertex_size, layout_size)

        read_func = layout.get_vertex_read_function(uv_factor)

        with reader.temp_offset(vertex_data_offset + self._buffer_offset):
            for vertex in vertices:
                read_func(reader, vertex)

    def pack(
        self,
        writer: BinaryWriter,
        version: Version,
        mesh_vertex_buffer_index: int,
        buffer_layouts: list[BufferLayout],
        mesh_vertex_count: int,
    ):
        layout_size = buffer_layouts[self.layout_index].get_total_size()
        writer.pack_struct(
            self.STRUCT,
            self,
            _buffer_index=mesh_vertex_buffer_index,
            _vertex_size=layout_size,
            vertex_count=mesh_vertex_count,
            _buffer_length=layout_size * mesh_vertex_count if version >= 0x20005 else 0,
            _buffer_offset=writer.AUTO_RESERVE,
        )

    def pack_buffer(
        self,
        writer: BinaryWriter,
        buffer_layouts: list[BufferLayout],
        vertices: list[Vertex],
        buffer_offset: int,
        uv_factor: int,
    ):
        layout = buffer_layouts[self.layout_index]
        self.fill(writer, _buffer_offset=buffer_offset)

        write_func = layout.get_vertex_write_function(uv_factor)

        for vertex in vertices:
            write_func(writer, vertex)

    def __repr__(self):
        return (
            f"VertexBuffer(\n"
            f"    layout_index = {self.layout_index}\n"
            f"    vertex_count = {self.vertex_count}\n"
            f"    buffer_length = {self._buffer_length}\n"
            f"    vertex_size = {self._vertex_size}\n"
            ")"
        )
