"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

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
import typing as tp
from enum import IntEnum

from soulstruct.base.models.color import ColorRGBA
from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter
from soulstruct.utilities.maths import Vector3, Vector4

from .version import Version

_LOGGER = logging.getLogger(__name__)


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


class BufferLayout:

    STRUCT = BinaryStruct(
        ("__member_count", "i"),
        "8x",
        ("__member_offset", "i"),
    )

    members: tp.List[LayoutMember]

    def __init__(self, source: tp.Union[BinaryReader, tp.List[LayoutMember]]):
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


class VertexBoneIndices:

    def __init__(self, a=0, b=0, c=0, d=0):
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

    def __repr__(self):
        return f"VertexBoneWeights{tuple(self)}"


class Vertex:

    VertexBoneWeights = VertexBoneWeights
    VertexBoneIndices = VertexBoneIndices

    def __init__(self):
        self.position = Vector3.zero()
        self.bone_weights = VertexBoneWeights()
        self.bone_indices = VertexBoneIndices()
        self.normal = Vector3.zero()
        self.normal_w = 0
        self.uvs = []  # type: tp.List[Vector3]
        self.tangents = []  # type: tp.List[Vector4]
        self.bitangent = Vector4.zero()
        self.colors = []  # type: tp.List[ColorRGBA]

        self.raw = b""

        self.uv_queue = []  # type: tp.List[Vector3]
        self.tangent_queue = []  # type: tp.List[Vector4]
        self.color_queue = []  # type: tp.List[ColorRGBA]

    def read(self, reader: BinaryReader, layout: BufferLayout, uv_factor: float):
        self.uvs = []
        self.tangents = []
        self.colors = []

        with reader.temp_offset(reader.position):
            self.raw = reader.read(layout.get_total_size())

        for member in layout:

            not_implemented = False

            if member.semantic == LayoutSemantic.Position:
                if member.layout_type == LayoutType.Float3:
                    self.position = Vector3(reader.unpack("<3f"))
                elif member.layout_type == LayoutType.Float4:
                    self.position = Vector3(reader.unpack("<3f"))[:3]
                elif member.layout_type == LayoutType.EdgeCompressed:
                    raise NotImplementedError("Soulstruct cannot load FLVERs with edge-compressed vertex positions.")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneWeights:
                if member.layout_type == LayoutType.Byte4A:
                    self.bone_weights = VertexBoneWeights(*[w / 127.0 for w in reader.unpack("<4b")])
                elif member.layout_type == LayoutType.Byte4C:
                    self.bone_weights = VertexBoneWeights(*[w / 255.0 for w in reader.unpack("<4B")])
                elif member.layout_type in {LayoutType.UVPair, LayoutType.Short4ToFloat4A}:
                    self.bone_weights = VertexBoneWeights(*[w / 32767.0 for w in reader.unpack("<4h")])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneIndices:
                if member.layout_type in {LayoutType.Byte4B, LayoutType.Byte4E}:
                    self.bone_indices = VertexBoneIndices(*reader.unpack("<4B"))
                elif member.layout_type == LayoutType.ShortBoneIndices:
                    self.bone_indices = VertexBoneIndices(*reader.unpack("<4h"))
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Normal:
                if member.layout_type == LayoutType.Float3:
                    self.normal = Vector3(reader.unpack("<3f"))
                elif member.layout_type == LayoutType.Float4:
                    self.normal = Vector3(reader.unpack("<3f"))
                    float_normal_w = reader.unpack_value("<f")
                    self.normal_w = int(float_normal_w)
                    if self.normal_w != float_normal_w:
                        raise ValueError(f"`normal_w` float was not a whole number.")
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E}:
                    self.normal = Vector3([(x - 127) / 127.0 for x in reader.unpack("<3B")])
                    self.normal_w = reader.unpack_value("<B")
                elif member.layout_type == LayoutType.Short2toFloat2:
                    self.normal_w = reader.unpack_value("<B")
                    self.normal = Vector3([x / 127.0 for x in reader.unpack("<3b")])
                elif member.layout_type == LayoutType.Short4ToFloat4A:
                    self.normal = Vector3([x / 32767.0 for x in reader.unpack("<3h")])
                    self.normal_w = reader.unpack_value("<h")
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    self.normal = Vector3([(x - 32767) / 32767.0 for x in reader.unpack("<3H")])
                    self.normal_w = reader.unpack_value("<h")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.UV:
                if member.layout_type == LayoutType.Float2:
                    self.uvs.append(Vector3(*reader.unpack("<2f"), 0.0))
                elif member.layout_type == LayoutType.Float3:
                    self.uvs.append(Vector3(*reader.unpack("<3f")))
                elif member.layout_type == LayoutType.Float4:
                    self.uvs.append(Vector3(*reader.unpack("<2f"), 0.0))
                    self.uvs.append(Vector3(*reader.unpack("<2f"), 0.0))
                elif member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Short2toFloat2, LayoutType.Byte4C, LayoutType.UV
                }:
                    self.uvs.append(Vector3(*reader.unpack("<2h"), 0) / uv_factor)
                elif member.layout_type == LayoutType.UVPair:
                    self.uvs.append(Vector3(*reader.unpack("<2h"), 0) / uv_factor)
                    self.uvs.append(Vector3(*reader.unpack("<2h"), 0) / uv_factor)
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    self.uvs.append(Vector3(*reader.unpack("<3h")) / uv_factor)
                    if reader.unpack_value("<h") != 0:
                        raise ValueError("Expected zero short after reading UV | Short4ToFloat4B vertex member.")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Tangent:
                if member.layout_type == LayoutType.Float4:
                    self.tangents.append(Vector4(*reader.unpack("<4f")))
                elif member.layout_type in {
                    LayoutType.Byte4A,
                    LayoutType.Byte4B,
                    LayoutType.Byte4C,
                    LayoutType.Short4ToFloat4A,
                    LayoutType.Byte4E,
                }:
                    tangent = Vector4([(x - 127) / 127.0 for x in reader.unpack("<4B")])
                    self.tangents.append(tangent)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Bitangent:
                if member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E
                }:
                    self.bitangent = Vector4([(x - 127) / 127.0 for x in reader.unpack("<4B")])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.VertexColor:
                if member.layout_type == LayoutType.Float4:
                    self.colors.append(ColorRGBA(*reader.unpack("<4f")))
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4C}:
                    # Convert byte channnels [0-255] to float channels [0-1].
                    self.colors.append(ColorRGBA(*[b / 255.0 for b in reader.unpack("<4B")]))
                else:
                    not_implemented = True
            else:
                not_implemented = True

            if not_implemented:
                raise NotImplementedError(
                    f"Unsupported vertex member semantic/type combination: "
                    f"{member.semantic.name} | {member.layout_type.name}"
                )

    def prepare_pack(self):
        """Queue list types so they can be properly split across buffers."""
        self.uv_queue = list(reversed(self.uvs))
        self.tangent_queue = list(reversed(self.tangents))
        self.color_queue = list(reversed(self.colors))

    def pack(self, writer: BinaryWriter, layout: BufferLayout, uv_factor: float):
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
                uv = self.uv_queue.pop() * uv_factor
                if member.layout_type == LayoutType.Float2:
                    writer.pack("2f", uv.x, uv.y)
                elif member.layout_type == LayoutType.Float3:
                    writer.pack("3f", uv.x, uv.y, uv.z)
                elif member.layout_type == LayoutType.Float4:
                    writer.pack("2f", uv.x, uv.y)
                    uv = self.uv_queue.pop() * uv_factor
                    writer.pack("2f", uv.x, uv.y)
                elif member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Short2toFloat2, LayoutType.Byte4C, LayoutType.UV
                }:
                    writer.pack("2h", int(uv.x), int(uv.y))
                elif member.layout_type == LayoutType.UVPair:
                    writer.pack("2h", int(uv.x), int(uv.y))
                    uv = self.uv_queue.pop() * uv_factor
                    writer.pack("2h", int(uv.x), int(uv.y))
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    writer.pack("4h", int(uv.x), int(uv.y), int(uv.z), 0)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Tangent:
                tangent = self.tangent_queue.pop()
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
                color = self.color_queue.pop()
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
        return (
            f"Vertex(\n"
            f"    position = {self.position}\n"
            f"    bone_weights = {self.bone_weights}\n"
            f"    bone_indices = {self.bone_indices}\n"
            f"    normal = {self.normal}\n"
            f"    normal_w = {self.normal_w}\n"
            f"    uvs = {self.uvs}\n"
            f"    tangents = {self.tangents}\n"
            f"    bitangent = {self.bitangent}\n"
            f"    colors = {self.colors}\n"
            f")"
        )


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
        layouts: tp.List[BufferLayout],
        vertices: tp.List[Vertex],
        vertex_data_offset: int,
        uv_factor: int,
    ):
        layout = layouts[self.layout_index]
        layout_size = layout.get_total_size()
        if self._vertex_size != self._buffer_length / self.vertex_count:
            raise ValueError(
                f"Vertex buffer size ({self._vertex_size}) != buffer length / vertex count "
                f"({self._buffer_length / self.vertex_count})."
            )
        if self._vertex_size != layout_size:
            # This happens for a few vanilla meshes; we ignore such meshes.
            # TODO: I've looked at the buffer data for mesh 0 of m8000B2A10, and it appears very abnormal. In fact,
            #  some of the 28-byte data clusters appear to just be counting upward as integers; there definitely does
            #  not seem to be any position float data in there. Later on, they appear to change into random shorts.
            raise VertexBufferSizeError(self._vertex_size, layout_size)

        with reader.temp_offset(vertex_data_offset + self._buffer_offset):
            for vertex in vertices:
                vertex.read(reader, layout, uv_factor)

    def pack(
        self,
        writer: BinaryWriter,
        version: Version,
        mesh_vertex_buffer_index: int,
        buffer_layouts: tp.List[BufferLayout],
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
        buffer_layouts: tp.List[BufferLayout],
        vertices: tp.List[Vertex],
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
