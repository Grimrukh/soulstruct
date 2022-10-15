from __future__ import annotations

__all__ = [
    "LayoutSemantic",
    "LayoutType",
    "LayoutMember",
    "BufferLayout",
    "Vertex",
    "VertexBufferSizeError",
    "VertexBuffer",
]

import logging
import struct
import typing as tp
from enum import IntEnum

from soulstruct.base.models.color import ColorRGBA
from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter
from soulstruct.utilities.maths import Vector3, Vector4

from .version import Version

_LOGGER = logging.getLogger(__name__)


class VertexBoneIndices:

    def __init__(self, a=0, b=0, c=0, d=0):
        if isinstance(a, (tuple, list)):
            a, b, c, d = a
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        elif index == 2:
            return self.c
        elif index == 3:
            return self.d
        raise IndexError(f"`VertexBoneIndices` index must range from 0 to 3, not {index}.")

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError(f"`VertexBoneIndices` values must be integers, not {type(value)}.")
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        elif index == 2:
            self.c = value
        elif index == 3:
            self.d = value
        raise IndexError(f"`VertexBoneIndices` index must range from 0 to 3, not {index}.")

    def __len__(self):
        return 4

    def __iter__(self):
        for i in range(4):
            yield self[i]

    def __eq__(self, other: VertexBoneIndices | tuple | list):
        if len(other) != 4:
            raise ValueError("Cannot only compare `VertexBoneIndices` for equality to a sequence of length 4.")
        return all(self[i] == other[i] for i in range(4))

    def __repr__(self):
        return f"VertexBoneIndices{tuple(self)}"


class VertexBoneWeights:

    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        elif index == 2:
            return self.c
        elif index == 3:
            return self.d
        raise IndexError(f"`VertexBoneWeights` index must range from 0 to 3, not {index}.")

    def __setitem__(self, index, value):
        if not isinstance(value, float):
            raise TypeError(f"`VertexBoneWeights` values must be floats, not {type(value)}.")
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        elif index == 2:
            self.c = value
        elif index == 3:
            self.d = value
        raise IndexError(f"`VertexBoneWeights` index must range from 0 to 3, not {index}.")

    def __len__(self):
        return 4

    def __iter__(self):
        for i in range(4):
            yield self[i]

    def __eq__(self, other: VertexBoneWeights | tuple | list):
        if len(other) != 4:
            raise ValueError("Cannot only compare `VertexBoneWeights` for equality to a sequence of length 4.")
        return all(self[i] == other[i] for i in range(4))

    def __repr__(self):
        return f"VertexBoneWeights{tuple(self)}"


class LayoutSemantic(IntEnum):
    """Vertex property."""
    Position = 0  # vertex position
    BoneWeights = 1  # weight of the attached bones
    BoneIndices = 2  # bones to which the vertex is attached (indices of the parent mesh's bone indices)
    Normal = 3  # orientation
    UV = 5  # texture coordinates
    Tangent = 6  # perpendicular to normal
    Bitangent = 7  # perpendicular to normal and tangent
    VertexColor = 10  # blending, alpha, etc.

    def unique(self):
        """If `True`, this `LayoutSemantic` only appears in one `LayoutMember` per `Mesh`."""
        return self in {self.BoneWeights, self.BoneIndices, self.Bitangent}


class LayoutType(IntEnum):
    """Format of a vertex property."""
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
        ("unk_x00", "i"),
        ("__struct_offset", "i"),  # validated, but not needed
        ("layout_type", "i"),
        ("semantic", "i"),
        ("index", "i"),
    )
    DEFAULTS = {
        "layout_type": LayoutType.Float3,
        "semantic": LayoutSemantic.Position,
    }

    unk_x00: int
    layout_type: LayoutType
    semantic: LayoutSemantic
    index: int

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

    def __repr__(self):
        return f"{self.semantic.name} | {self.layout_type.name} | {self.size}"

    @property
    def size(self) -> int:
        return self.layout_type.size()


# Layout types for which two short UV coordinates should be read.
TWO_SHORT_UV_TYPES = {
    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Short2toFloat2, LayoutType.Byte4C, LayoutType.UV
}
# Layout types for which a `Vector4` with quantized 8-bit floats in [-1, 1] range should be read.
SIGNED_8BIT_FLOAT_TYPES = {LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E}
TANGENT_SIGNED_8BIT_FLOAT_TYPES = SIGNED_8BIT_FLOAT_TYPES | {LayoutType.Short4ToFloat4A}  # one extra type
COLOR_UNSIGNED_8BIT_FLOAT_TYPES = {LayoutType.Byte4A, LayoutType.Byte4C}


def _UV_4H_CALLBACK(v: tuple[int, int, int, int]) -> list[Vector3]:
    if v[3] != 0:
        raise ValueError("Expected fourth short to be zero in reading UV | Short4ToFloat4B vertex member.")
    return [Vector3(v[:3])]


# Maps `(LayoutSemantic, LayoutType)` key pairs (nested) to `(name, fmt, size, callback)` quadruples.
# Note that the layout is aware that `uvs`, `tangents`, and `colors` attributes are lists; `+=` will be used on the
# callback result in these cases.
LAYOUT_PARSER = {
    LayoutSemantic.Position: {
        LayoutType.Float3: ("position", "3f", 3, Vector3),
        LayoutType.Float4: ("position", "4f", 4, lambda v: Vector3(v[:3])),
        # LayoutType.EdgeCompressed is explicitly not supported.
    },
    LayoutSemantic.BoneWeights: {
        LayoutType.Byte4A: ("bone_weights", "4b", 4, lambda v: VertexBoneWeights(*[x / 127.0 for x in v])),
        LayoutType.Byte4C: ("bone_weights", "4B", 4, lambda v: VertexBoneWeights(*[x / 255.0 for x in v])),
        LayoutType.UVPair: ("bone_weights", "4h", 4, lambda v: VertexBoneWeights(*[x / 32767.0 for x in v])),
        LayoutType.Short4ToFloat4A: ("bone_weights", "4h", 4, lambda v: VertexBoneWeights(*[x / 32767.0 for x in v])),
    },
    LayoutSemantic.BoneIndices: {
        LayoutType.Byte4B: ("bone_indices", "4B", 4, VertexBoneIndices),
        LayoutType.Byte4E: ("bone_indices", "4B", 4, VertexBoneIndices),
        LayoutType.ShortBoneIndices: ("bone_indices", "4h", 4, VertexBoneIndices),
    },
    LayoutSemantic.Normal: {
        LayoutType.Float3: ("normal", "3f", 3, Vector4),
        LayoutType.Float4: ("normal", "4f", 4, Vector4),
        # Note that we don't modify `w` in any of these quantization cases.
        LayoutType.Byte4A: ("normal", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v[:3]] + [v[3]])),
        LayoutType.Byte4B: ("normal", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v[:3]] + [v[3]])),
        LayoutType.Byte4C: ("normal", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v[:3]] + [v[3]])),
        LayoutType.Byte4E: ("normal", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v[:3]] + [v[3]])),
        LayoutType.Short2toFloat2:
            ("normal", "B3b", 4, lambda v: Vector4([v[3]] + [x / 127.0 for x in v[1:]])),
        LayoutType.Short4ToFloat4A:
            ("normal", "4h", 4, lambda v: Vector4([x / 32767.0 for x in v[:3]] + [v[3]])),
        LayoutType.Short4ToFloat4B:
            ("normal", "3Hh", 4, lambda v: Vector4([(x - 32767) / 32767.0 for x in v[:3]] + [v[3]])),
    },
    LayoutSemantic.UV: {
        LayoutType.Float2: ("uvs", "2f", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.Float3: ("uvs", "3f", 3, lambda v: [Vector3(v)]),
        LayoutType.Float4: ("uvs", "4f", 4, lambda v: [Vector3(v[0], v[1], 0.0), Vector3(v[2], v[3], 0.0)]),
        # All types below this will have their UVs divided by local `uv_factor`.
        LayoutType.Byte4A: ("uvs", "2h", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.Byte4B: ("uvs", "2h", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.Short2toFloat2: ("uvs", "2h", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.Byte4C: ("uvs", "2h", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.UV: ("uvs", "2h", 2, lambda v: [Vector3(*v, 0.0)]),
        LayoutType.UVPair: ("uvs", "4h", 4, lambda v: [Vector3(v[0], v[1], 0.0), Vector3(v[2], v[3], 0.0)]),
        LayoutType.Short4ToFloat4B: ("uvs", "4h", 4, _UV_4H_CALLBACK),  # asserts fourth short is zero
    },
    LayoutSemantic.Tangent: {
        LayoutType.Float4: ("tangents", "4f", 4, lambda v: [Vector4(v)]),
        LayoutType.Byte4A: ("tangents", "4B", 4, lambda v: [Vector4([(x - 127) / 127.0 for x in v])]),
        LayoutType.Byte4B: ("tangents", "4B", 4, lambda v: [Vector4([(x - 127) / 127.0 for x in v])]),
        LayoutType.Byte4C: ("tangents", "4B", 4, lambda v: [Vector4([(x - 127) / 127.0 for x in v])]),
        LayoutType.Byte4E: ("tangents", "4B", 4, lambda v: [Vector4([(x - 127) / 127.0 for x in v])]),
        LayoutType.Short4ToFloat4A: ("tangents", "4B", 4, lambda v: [Vector4([(x - 127) / 127.0 for x in v])]),
    },
    LayoutSemantic.Bitangent: {
        LayoutType.Byte4A: ("bitangent", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v])),
        LayoutType.Byte4B: ("bitangent", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v])),
        LayoutType.Byte4C: ("bitangent", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v])),
        LayoutType.Byte4E: ("bitangent", "4B", 4, lambda v: Vector4([(x - 127) / 127.0 for x in v])),
    },
    LayoutSemantic.VertexColor: {
        LayoutType.Float4: ("colors", "4f", 4, lambda v: [ColorRGBA(*v)]),
        LayoutType.Byte4A: ("colors", "4B", 4, lambda v: [ColorRGBA(*[x / 255.0 for x in v])]),
        LayoutType.Byte4C: ("colors", "4B", 4, lambda v: [ColorRGBA(*[x / 255.0 for x in v])]),
    },
}

USES_UV_FACTOR = {
    LayoutType.Byte4A,
    LayoutType.Byte4B,
    LayoutType.Short2toFloat2,
    LayoutType.Byte4C,
    LayoutType.UV,
    LayoutType.UVPair,
    LayoutType.Short4ToFloat4B,
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
                struct_offset += member.layout_type.size()

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

    def get_vertex_read_function(self, uv_factor: int) -> tp.Callable[[BinaryReader, Vertex], None]:
        """Construct a relatively efficient function that can be used to read data for each `Vertex` whose data lies
        in a `VertexBuffer` with this layout."""

        attr_names = []  # attributes of `Vertex` to assign from unpacked `struct.unpack(fmt)` (maybe with func below)
        full_fmt = ""  # fmt of data to read
        attr_sizes = []  # number of elements in `struct.unpack(fmt)` result to eat for corresponding attr name above
        attr_funcs = []  # callbacks (or `None`) to process tuples of elements above

        for member in self.members:

            if member.semantic == LayoutSemantic.Position and member.layout_type == LayoutType.EdgeCompressed:
                # Explicitly not supported.
                raise NotImplementedError("Cannot read FLVERs with edge-compressed vertex positions.")
            if member.semantic not in LAYOUT_PARSER:
                raise ValueError(f"Invalid vertex buffer layout member semantic: {member.semantic}")

            semantic_parser = LAYOUT_PARSER[member.semantic]
            if member.layout_type not in semantic_parser:
                raise NotImplementedError(
                    f"Unsupported vertex buffer layout member semantic/type combination: "
                    f"{member.semantic.name} | {member.layout_type.name}"
                )
            attr_name, fmt, attr_size, attr_func = semantic_parser[member.layout_type]

            attr_names.append(attr_name)
            full_fmt += fmt
            attr_sizes.append(attr_size)

            if member.semantic == LayoutSemantic.UV and member.layout_type in USES_UV_FACTOR:
                def uv_attr_func(v) -> list[Vector3]:
                    return [vec / uv_factor for vec in attr_func(v)]
                attr_funcs.append(uv_attr_func)
            else:
                attr_funcs.append(attr_func)

        def read_vertex_data(reader: BinaryReader, vertex: Vertex):
            vertex.raw = reader.read(struct.calcsize("<" + full_fmt))
            data = struct.unpack("<" + full_fmt, vertex.raw)
            index = 0
            for name, size, func in zip(attr_names, attr_sizes, attr_funcs, strict=True):
                raw_value = data[index:index + size]  # raw tuple
                value = func(raw_value)
                if isinstance(value, list):  # extend list
                    getattr(vertex, name).extend(value)
                else:
                    setattr(vertex, name, value)
                index += size

        return read_vertex_data

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index):
        return self.members[index]

    def __len__(self):
        return len(self.members)

    def get_total_size(self):
        return sum(member.layout_type.size() for member in self.members)

    def __repr__(self):
        members = "\n        ".join(repr(m) for m in self.members)
        return (
            f"BufferLayout(\n"
            f"    size = {self.get_total_size()}\n"
            f"    members = [\n        {members}\n    ]\n"
            f")"
        )


class Vertex:

    VertexBoneWeights = VertexBoneWeights
    VertexBoneIndices = VertexBoneIndices

    def __init__(
        self,
        position: Vector3 = None,
        bone_weights: VertexBoneWeights = None,
        bone_indices: VertexBoneIndices = None,
        normal: Vector3 | Vector4 = None,  # NOTE: `w` element can be used to bind to a single bone (as an `int`)
        uvs: list[Vector3] = None,
        tangents: list[Vector4] = None,
        bitangent: Vector4 = None,
        colors: list[ColorRGBA] = None,
    ):
        self.position = Vector3.zero() if position is None else position
        self.bone_weights = VertexBoneWeights() if bone_weights is None else bone_weights
        self.bone_indices = VertexBoneIndices() if bone_indices is None else bone_indices
        if isinstance(normal, Vector4):
            self._normal = Vector4.zero()
        elif isinstance(normal, Vector3):
            self._normal = Vector4(*normal, 0.0)
        else:
            self._normal = Vector4.zero()  # default
        self.uvs = [] if uvs is None else uvs
        self.tangents = [] if tangents is None else tangents
        self.bitangent = Vector4.zero() if bitangent is None else bitangent
        self.colors = [] if colors is None else colors

        self.raw = b""

        self.uv_queue = []  # type: list[Vector3]
        self.tangent_queue = []  # type: list[Vector4]
        self.color_queue = []  # type: list[ColorRGBA]

    @property
    def normal(self) -> Vector3:
        """Get XYZ of `_normal` as a `Vector3`, which is suitable for most uses."""
        return Vector3(self._normal[:3])

    @normal.setter
    def normal(self, value: Vector3 | Vector4 | tuple | list):
        """Set XYZ or full XYZW of `_normal`."""
        if len(value) == 3:
            self._normal = Vector4(*value, self._normal.w)  # keep current `w`
        elif len(value) == 4:
            self._normal = Vector4(*value)
        else:
            raise TypeError(f"`Vertex.normal` can only be set to a 3 or 4 length sequence/vector, not: {value}")

    @property
    def normal_w(self) -> int:
        """Get `_normal.w` as an `int`, which is sometimes used to bind the `Vertex` to a single bone."""
        return int(self._normal.w)

    @normal_w.setter
    def normal_w(self, value: float | int):
        self._normal.w = float(value)

    def clear_lists(self):
        self.uvs = []
        self.tangents = []
        self.colors = []

    def prepare_pack(self):
        """Queue list types so they can be properly split across buffers."""
        self.uv_queue = list(reversed(self.uvs))
        self.tangent_queue = list(reversed(self.tangents))
        self.color_queue = list(reversed(self.colors))

    def pack(self, writer: BinaryWriter, layout: BufferLayout, uv_factor: float):

        # TODO: Speed up in the same way as reading parser.

        for member in layout:

            not_implemented = False

            if member.semantic == LayoutSemantic.Position:
                if member.layout_type == LayoutType.Float3:
                    writer.pack("3f", *self.position)
                elif member.layout_type == LayoutType.Float4:
                    writer.pack("4f", *self.position, 0.0)
                elif member.layout_type == LayoutType.EdgeCompressed:
                    raise NotImplementedError("Soulstruct cannot load FLVERs with edge-compressed vertex positions.")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneWeights:
                if member.layout_type == LayoutType.Byte4A:
                    writer.pack("4b", *[int(w * 127) for w in self.bone_weights])
                elif member.layout_type == LayoutType.Byte4C:
                    writer.pack("4B", *[int(w * 255) for w in self.bone_weights])
                elif member.layout_type in {LayoutType.UVPair, LayoutType.Short4ToFloat4A}:
                    writer.pack("4h", *[int(w * 32767) for w in self.bone_weights])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneIndices:
                if member.layout_type in {LayoutType.Byte4B, LayoutType.Byte4E}:
                    writer.pack("4B", *self.bone_indices)
                elif member.layout_type == LayoutType.ShortBoneIndices:
                    writer.pack("4h", *self.bone_indices)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Normal:
                if member.layout_type == LayoutType.Float3:
                    writer.pack("3f", *self.normal)
                elif member.layout_type == LayoutType.Float4:
                    writer.pack("4f", *self.normal, self.normal_w)
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E}:
                    writer.pack("4B", *[int(x * 127 + 127) for x in self.normal], self.normal_w)
                elif member.layout_type == LayoutType.Short2toFloat2:
                    writer.pack("B3b", self.normal_w, *[int(x * 127) for x in self.normal])
                elif member.layout_type == LayoutType.Short4ToFloat4A:
                    writer.pack("4h", *[int(x * 32767) for x in self.normal], self.normal_w)
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    writer.pack("4H", *[int(x * 32767 + 32767) for x in self.normal], self.normal_w)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.UV:
                try:
                    uv = self.uv_queue.pop() * uv_factor
                except IndexError:
                    print(layout)
                    print(member)
                    print(f"{len(self.uvs)} UVS, {len(self.tangents)} tangents, {len(self.colors)} colors")
                    raise IndexError("Ran out of vertex UVs to buffer.")
                if member.layout_type == LayoutType.Float2:
                    writer.pack("2f", uv.x, uv.y)
                elif member.layout_type == LayoutType.Float3:
                    writer.pack("3f", uv.x, uv.y, uv.z)
                elif member.layout_type == LayoutType.Float4:
                    writer.pack("2f", uv.x, uv.y)
                    try:
                        uv = self.uv_queue.pop() * uv_factor
                    except IndexError:
                        print(layout)
                        print(member)
                        print(f"{len(self.uvs)} UVS, {len(self.tangents)} tangents, {len(self.colors)} colors")
                        raise IndexError("Ran out of vertex UVs to buffer.")
                    writer.pack("2f", uv.x, uv.y)
                elif member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Short2toFloat2, LayoutType.Byte4C, LayoutType.UV
                }:
                    writer.pack("2h", int(uv.x), int(uv.y))
                elif member.layout_type == LayoutType.UVPair:
                    writer.pack("2h", int(uv.x), int(uv.y))
                    try:
                        uv = self.uv_queue.pop() * uv_factor
                    except IndexError:
                        print(layout)
                        print(member)
                        print(f"{len(self.uvs)} UVS, {len(self.tangents)} tangents, {len(self.colors)} colors")
                        raise IndexError("Ran out of vertex UVs to buffer.")
                    writer.pack("2h", int(uv.x), int(uv.y))
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    writer.pack("4h", int(uv.x), int(uv.y), int(uv.z), 0)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Tangent:
                try:
                    tangent = self.tangent_queue.pop()
                except IndexError:
                    print(layout)
                    print(member)
                    print(f"{len(self.uvs)} UVS, {len(self.tangents)} tangents, {len(self.colors)} colors")
                    raise IndexError("Ran out of vertex tangents to buffer.")
                if member.layout_type == LayoutType.Float4:
                    writer.pack("4f", *tangent)
                elif member.layout_type in {
                    LayoutType.Byte4A,
                    LayoutType.Byte4B,
                    LayoutType.Byte4C,
                    LayoutType.Short4ToFloat4A,
                    LayoutType.Byte4E,
                }:
                    writer.pack("4B", *[int(x * 127 + 127) for x in tangent])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Bitangent:
                if member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E
                }:
                    writer.pack("4B", *[int(x * 127 + 127) for x in self.bitangent])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.VertexColor:
                try:
                    color = self.color_queue.pop()
                except IndexError:
                    print(layout)
                    print(member)
                    print(f"{len(self.uvs)} UVS, {len(self.tangents)} tangents, {len(self.colors)} colors")
                    raise IndexError("Ran out of vertex colors to buffer.")
                if member.layout_type == LayoutType.Float4:
                    writer.pack("4f", *color)
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4C}:
                    writer.pack("4B", *[int(c * 255) for c in color])
                else:
                    not_implemented = True
            else:
                not_implemented = True

            if not_implemented:
                raise NotImplementedError(
                    f"Unsupported vertex member semantic/type combination: "
                    f"{member.semantic.name} | {member.layout_type.name}"
                )

    def finish_pack(self):
        """Check queues are empty."""
        if self.uv_queue:
            raise ValueError(f"{len(self.uv_queue)} UVs left in vertex queue after it was packed.")
        if self.tangent_queue:
            raise ValueError(f"{len(self.tangent_queue)} tangents left in vertex queue after it was packed.")
        if self.color_queue:
            raise ValueError(f"{len(self.color_queue)} vertex colors left in vertex queue after it was packed.")

    def repr_position_only(self):
        return f"Vertex{repr(self.position)[7:]}"

    def __repr__(self):
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
        for vertex in vertices:
            vertex.pack(writer, layout, uv_factor)

    def __repr__(self):
        return (
            f"VertexBuffer(\n"
            f"    layout_index = {self.layout_index}\n"
            f"    vertex_count = {self.vertex_count}\n"
            f"    buffer_length = {self._buffer_length}\n"
            f"    vertex_size = {self._vertex_size}\n"
            ")"
        )
