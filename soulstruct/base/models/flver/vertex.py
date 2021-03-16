__all__ = ["LayoutSemantic", "LayoutType", "LayoutMember", "BufferLayout", "Vertex", "VertexBuffer"]

import io
import typing as tp
from enum import IntEnum

from soulstruct.utilities import unpack_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject
from soulstruct.utilities.maths import Vector3, Vector4

from .color import Color
from .version import Version


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
        ("__struct_offset", "i"),  # ignored
        ("layout_type", "i"),
        ("semantic", "i"),
        ("index", "i"),
    )

    unk_x00: int
    layout_type: LayoutType
    semantic: LayoutSemantic
    index: int

    def unpack(self, buffer: io.BufferedIOBase, struct_offset: int = None):
        data = self.STRUCT.unpack(buffer)
        if struct_offset != (binary_struct_offset := data.pop("__struct_offset")):
            raise ValueError(
                f"`LayoutMember` binary struct offset ({binary_struct_offset}) does not match passed struct offset "
                f"({struct_offset})."
            )
        self.set(**data)

    def __repr__(self):
        return f"{self.semantic.name} | {self.layout_type.name}"


class BufferLayout:

    STRUCT = BinaryStruct(
        ("__member_count", "i"),
        "8x",
        ("__member_offset", "i"),
    )

    members: list[LayoutMember]

    def __init__(self, source: tp.Union[io.BufferedIOBase, list[LayoutMember]]):
        self.members = []

        if isinstance(source, io.BufferedIOBase):
            self.unpack(source)
        elif isinstance(source, (list, tuple)) and all(isinstance(e, LayoutMember) for e in source):
            self.members = source
        else:
            raise TypeError(f"`BufferLayout` source must be a binary buffer or list of `LayoutMember`s, not {source}.")

    def unpack(self, buffer: io.BufferedIOBase):
        data = self.STRUCT.unpack(buffer)
        layout_offset = buffer.tell()

        buffer.seek(data.pop("__member_offset"))
        struct_offset = 0
        self.members = []
        for _ in range(data.pop("__member_count")):
            member = LayoutMember(buffer, dict(struct_offset=struct_offset))
            self.members.append(member)
            struct_offset += member.layout_type.size()
        buffer.seek(layout_offset)

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index):
        return self.members[index]

    def __len__(self):
        return len(self.members)

    def get_total_size(self):
        return sum(member.layout_type.size() for member in self.members)


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

    def __init__(self):
        self.position = Vector3.zero()
        self.bone_weights = VertexBoneWeights()
        self.bone_indices = VertexBoneIndices()
        self.normal = Vector3.zero()
        self.normal_w = 0
        self.uvs = []  # type: list[Vector3]
        self.tangents = []  # type: list[Vector4]
        self.bitangent = Vector4.zero()
        self.colors = []  # type: list[Color]

    def read(self, buffer: io.BufferedIOBase, layout: BufferLayout, uv_factor: float):
        self.uvs = []
        self.tangents = []
        self.colors = []
        for member in layout:

            not_implemented = False

            if member.semantic == LayoutSemantic.Position:
                if member.layout_type == LayoutType.Float3:
                    self.position = Vector3(unpack_from_buffer(buffer, "<3f"))
                elif member.layout_type == LayoutType.Float4:
                    self.position = Vector3(unpack_from_buffer(buffer, "<3f"))[:3]
                elif member.layout_type == LayoutType.EdgeCompressed:
                    raise NotImplementedError("Soulstruct cannot load FLVERs with edge-compressed vertex positions.")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneWeights:
                if member.layout_type == LayoutType.Byte4A:
                    self.bone_weights = VertexBoneWeights(*[w / 127.0 for w in unpack_from_buffer(buffer, "<4b")])
                elif member.layout_type == LayoutType.Byte4C:
                    self.bone_weights = VertexBoneWeights(*[w / 255.0 for w in unpack_from_buffer(buffer, "<4B")])
                elif member.layout_type == LayoutType.UVPair:
                    self.bone_weights = VertexBoneWeights(*[w / 32767.0 for w in unpack_from_buffer(buffer, "<4h")])
                elif member.layout_type == LayoutType.Short4ToFloat4A:
                    self.bone_weights = VertexBoneWeights(*[w / 32767.0 for w in unpack_from_buffer(buffer, "<4h")])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.BoneIndices:
                if member.layout_type == LayoutType.Byte4B:
                    self.bone_indices = VertexBoneIndices(*unpack_from_buffer(buffer, "<4B"))
                elif member.layout_type == LayoutType.ShortBoneIndices:
                    self.bone_indices = VertexBoneIndices(*unpack_from_buffer(buffer, "<4h"))
                elif member.layout_type == LayoutType.Byte4E:
                    self.bone_indices = VertexBoneIndices(*unpack_from_buffer(buffer, "<4B"))
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Normal:
                if member.layout_type == LayoutType.Float3:
                    self.normal = Vector3(unpack_from_buffer(buffer, "<3f"))
                elif member.layout_type == LayoutType.Float4:
                    self.normal = Vector3(unpack_from_buffer(buffer, "<3f"))
                    float_normal_w = unpack_from_buffer(buffer, "<f")[0]
                    self.normal_w = int(float_normal_w)
                    if self.normal_w != float_normal_w:
                        raise ValueError(f"`normal_w` float was not a whole number.")
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E}:
                    self.normal = Vector3([(x - 127) / 127.0 for x in unpack_from_buffer(buffer, "<3B")])
                    self.normal_w = unpack_from_buffer(buffer, "<B")[0]
                elif member.layout_type == LayoutType.Short2toFloat2:
                    self.normal_w = unpack_from_buffer(buffer, "<B")[0]
                    self.normal = Vector3([x / 127.0 for x in unpack_from_buffer(buffer, "<3b")])
                elif member.layout_type == LayoutType.Short4ToFloat4A:
                    self.normal = Vector3([x / 32767.0 for x in unpack_from_buffer(buffer, "<3h")])
                    self.normal_w = unpack_from_buffer(buffer, "<h")[0]
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    self.normal = Vector3([(x - 32767) / 32767.0 for x in unpack_from_buffer(buffer, "<3H")])
                    self.normal_w = unpack_from_buffer(buffer, "<h")[0]
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.UV:
                if member.layout_type == LayoutType.Float2:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2f"), 0.0))
                elif member.layout_type == LayoutType.Float3:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<3f")))
                elif member.layout_type == LayoutType.Float4:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2f"), 0.0))
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2f"), 0.0))
                elif member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Short2toFloat2, LayoutType.Byte4C, LayoutType.UV
                }:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2h"), 0) / uv_factor)
                elif member.layout_type == LayoutType.UVPair:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2h"), 0) / uv_factor)
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<2h"), 0) / uv_factor)
                elif member.layout_type == LayoutType.Short4ToFloat4B:
                    self.uvs.append(Vector3(*unpack_from_buffer(buffer, "<3h")) / uv_factor)
                    if unpack_from_buffer(buffer, "<h") != 0:
                        raise ValueError("Expected null byte after reading UV | Short4ToFloat4B vertex member.")
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Tangent:
                if member.layout_type == LayoutType.Float4:
                    self.tangents.append(Vector4(*unpack_from_buffer(buffer, "<4f")))
                elif member.layout_type in {
                    LayoutType.Byte4A,
                    LayoutType.Byte4B,
                    LayoutType.Byte4C,
                    LayoutType.Short4ToFloat4A,
                    LayoutType.Byte4E,
                }:
                    tangent = Vector4([(x - 127) / 127.0 for x in unpack_from_buffer(buffer, "<4B")])
                    self.tangents.append(tangent)
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.Bitangent:
                if member.layout_type in {
                    LayoutType.Byte4A, LayoutType.Byte4B, LayoutType.Byte4C, LayoutType.Byte4E
                }:
                    self.bitangent = Vector4([(x - 127) / 127.0 for x in unpack_from_buffer(buffer, "<4B")])
                else:
                    not_implemented = True
            elif member.semantic == LayoutSemantic.VertexColor:
                if member.layout_type == LayoutType.Float4:
                    self.colors.append(Color(*unpack_from_buffer(buffer, "<4f")))
                elif member.layout_type in {LayoutType.Byte4A, LayoutType.Byte4C}:
                    self.colors.append(Color(*[b / 255.0 for b in unpack_from_buffer(buffer, "<4B")]))
                else:
                    not_implemented = True
            else:
                not_implemented = True

            if not_implemented:
                raise NotImplementedError(
                    f"Unsupported vertex member semantic/type combination: "
                    f"{member.semantic.name} | {member.layout_type.name}"
                )

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


class VertexBuffer(BinaryObject):

    STRUCT = BinaryStruct(
        ("_buffer_index", "i"),
        ("layout_index", "i"),
        ("_vertex_size", "i"),
        ("vertex_count", "i"),
        "8x",
        ("__buffer_length", "i"),
        ("_buffer_offset", "i"),
    )

    layout_index: int
    vertex_count: int

    _buffer_index: int
    _vertex_size: int
    _buffer_offset: int

    def read_buffer(
        self,
        buffer: io.BufferedIOBase,
        layouts: list[BufferLayout],
        vertices: list[Vertex],
        data_offset: int,
        version: Version,
    ):
        layout = layouts[self.layout_index]
        if self._vertex_size != (layout_size := layout.get_total_size()):
            raise ValueError(f"Vertex buffer size ({self._vertex_size}) does not match layout size ({layout_size}).")
        uv_factor = 2048 if version >= Version.DarkSouls2_NT else 1024

        old_offset = buffer.tell()
        buffer.seek(data_offset + self._buffer_offset)
        for vertex in vertices:
            vertex.read(buffer, layout, uv_factor)
        buffer.seek(old_offset)

        self._buffer_index = -1
        self._vertex_size = -1
        self.vertex_count = -1
        self._buffer_offset = -1
