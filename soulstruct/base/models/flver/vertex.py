from __future__ import annotations

__all__ = [
    "MemberType",
    "MemberFormat",
    "LayoutMember",
    "BufferLayout",
    "VertexBufferSizeError",
    "VertexBuffer",
]

import logging
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import *

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

    def is_unique(self):
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


@dataclass(slots=True)
class LayoutMemberStruct(BinaryStruct):

    unk_x00: int
    _struct_offset: int  # just the offset of this `LayoutMember` struct instance
    member_format: MemberFormat = field(**Binary(int))
    member_type: MemberType = field(**Binary(int))
    index: int  # instance index of this member in its `BufferLayout`


@dataclass(slots=True)
class LayoutMember:

    member_format: MemberFormat
    member_type: MemberType
    unk_x00: int = 0
    index: int = 0  # instance index of this `MemberType` in its `BufferLayout`

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, asserted_struct_offset: int):
        layout_member_struct = LayoutMemberStruct.from_bytes(reader)
        # TODO: Do we really have to raise an exception here? SS re-export can easily fix this.
        if asserted_struct_offset != layout_member_struct.pop("_struct_offset"):
            raise ValueError("`LayoutMember` recorded binary struct offset does not match its actual struct offset.")
        return layout_member_struct.to_object(cls)

    def to_flver_writer(self, writer: BinaryWriter, struct_offset: int):
        LayoutMemberStruct.object_to_writer(self, writer, _struct_offset=struct_offset)

    def __eq__(self, other: LayoutMember):
        return (
            self.unk_x00 == other.unk_x00
            and self.member_format == other.member_format
            and self.member_type == other.member_type
        )

    def __repr__(self):
        suffix = f" (unk_x00 = {self.unk_x00})" if self.unk_x00 != 0 else ""
        if self.index > 0:
            return f"{self.member_type.name}({self.index})<{self.size}, {self.member_format.name}>{suffix}"
        return f"{self.member_type.name}<{self.size}, {self.member_format.name}>{suffix}"

    @property
    def size(self) -> int:
        return self.member_format.size()


_INT_TO_FLOAT_127 = (
    lambda i: i / 127.0,
    lambda f: f * 127,
)
_INT_TO_FLOAT_255 = (
    lambda i: i / 255.0,
    lambda f: f * 255,
)
_INT_TO_FLOAT_32767 = (
    lambda i: i / 32767.0,
    lambda f: f * 32767,
)
_INT_TO_FLOAT_127_SIGNED = (
    lambda i: (i - 127.0) / 127.0,
    lambda f: f * 127 + 127,
)
_INT_TO_FLOAT_255_SIGNED = (
    lambda i: (i - 255.0) / 255.0,
    lambda f: f * 255 + 255,
)
_INT_TO_FLOAT_32767_SIGNED = (
    lambda i: (i - 32767.0) / 32767.0,
    lambda f: f * 32767 + 32767,
)


DTYPE_PARSER = {
    MemberType.Position: {
        MemberFormat.Float3: (
            [("position_x", "f"), ("position_y", "f"), ("position_z", "f")],
            [("position_x", "f"), ("position_y", "f"), ("position_z", "f")],
            [None, None, None],
        ),
        MemberFormat.Float4: (
            [("position_x", "f"), ("position_y", "f"), ("position_z", "f"), ("position_w", "f")],
            [("position_x", "f"), ("position_y", "f"), ("position_z", "f"), ("position_w", "f")],
            [None, None, None, None],
        ),
        # LayoutType.EdgeCompressed is explicitly not supported.
    },
    MemberType.BoneWeights: {
        MemberFormat.Byte4A: (
            [(f"bone_weight_{c}", "b") for c in "abcd"],
            [(f"bone_weight_{c}", "f") for c in "abcd"],
            [_INT_TO_FLOAT_127] * 4,
        ),
        MemberFormat.Byte4C: (
            [(f"bone_weight_{c}", "B") for c in "abcd"],
            [(f"bone_weight_{c}", "f") for c in "abcd"],
            [_INT_TO_FLOAT_255] * 4,
        ),
        MemberFormat.UVPair: (
            [(f"bone_weight_{c}", "h") for c in "abcd"],
            [(f"bone_weight_{c}", "f") for c in "abcd"],
            [_INT_TO_FLOAT_32767] * 4,
        ),
        MemberFormat.Short4ToFloat4A: (
            [(f"bone_weight_{c}", "h") for c in "abcd"],
            [(f"bone_weight_{c}", "f") for c in "abcd"],
            [_INT_TO_FLOAT_32767] * 4,
        ),
    },
    MemberType.BoneIndices: {
        MemberFormat.Byte4B: (
            [(f"bone_index_{c}", "B") for c in "abcd"],
            [(f"bone_index_{c}", "B") for c in "abcd"],
            [None, None, None, None],
        ),
        MemberFormat.Byte4E: (
            [(f"bone_index_{c}", "B") for c in "abcd"],
            [(f"bone_index_{c}", "B") for c in "abcd"],
            [None, None, None, None],
        ),
        MemberFormat.ShortBoneIndices: (
            [(f"bone_index_{c}", "h") for c in "abcd"],
            [(f"bone_index_{c}", "h") for c in "abcd"],
            [None, None, None, None],
        ),
    },
    MemberType.Normal: {
        MemberFormat.Float3: (
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f")],
            [None, None, None],
        ),
        MemberFormat.Float4: (
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "i4")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "i4")],
            [None, None, None, None],
        ),
        # Note that we don't modify `w` in any of these quantization cases.
        MemberFormat.Byte4A: (
            [("normal_x", "B"), ("normal_y", "B"), ("normal_z", "B"), ("normal_w", "B")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "B")],
            [_INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, None],
        ),
        MemberFormat.Byte4B: (
            [("normal_x", "B"), ("normal_y", "B"), ("normal_z", "B"), ("normal_w", "B")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "B")],
            [_INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, None],
        ),
        MemberFormat.Byte4C: (
            [("normal_x", "B"), ("normal_y", "B"), ("normal_z", "B"), ("normal_w", "B")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "B")],
            [_INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, None],
        ),
        MemberFormat.Byte4E: (
            [("normal_x", "B"), ("normal_y", "B"), ("normal_z", "B"), ("normal_w", "B")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "B")],
            [_INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, None],
        ),
        MemberFormat.Short2toFloat2: (
            [("normal_w", "B"), ("normal_x", "b"), ("normal_y", "b"), ("normal_z", "b")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "B")],
            [None, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED, _INT_TO_FLOAT_127_SIGNED],
        ),
        MemberFormat.Short4ToFloat4A: (
            [("normal_x", "h"), ("normal_y", "h"), ("normal_z", "h"), ("normal_w", "h")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "h")],
            [_INT_TO_FLOAT_32767_SIGNED] * 3 + [None],
        ),
        MemberFormat.Short4ToFloat4B: (
            [("normal_x", "H"), ("normal_y", "H"), ("normal_z", "H"), ("normal_w", "h")],
            [("normal_x", "f"), ("normal_y", "f"), ("normal_z", "f"), ("normal_w", "h")],
            [_INT_TO_FLOAT_32767_SIGNED] * 3 + [None],
        ),
    },
    MemberType.UV: {
        # UV read callbacks return a list of 1-2 UV lists, but write callbacks still process one UV list at a time.
        # Writer will detect `Float4` and `UVPair` types are write two queued UVs (in reverse order) as needed.
        MemberFormat.Float2: (
            [("uv_u", "f"), ("uv_v", "f")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.Float3: (
            [("uv_u", "f"), ("uv_v", "f"), ("uv_w", "f")],
            [("uv_u", "f"), ("uv_v", "f"), ("uv_w", "f")],
            [None, None, None],
        ),
        MemberFormat.Float4: (
            [("uv_u", "f"), ("uv_v", "f"), ("uv_u", "f"), ("uv_v", "f")],
            [("uv_u", "f"), ("uv_v", "f"), ("uv_u", "f"), ("uv_v", "f")],
            [None, None, None, None],
        ),
        # All types below this will have their UVs divided by local `uv_factor` by the unpacker.
        MemberFormat.Byte4A: (
            [("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.Byte4B: (
            [("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.Short2toFloat2: (
            [("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.Byte4C: (
            [("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.UV: (
            [("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f")],
            [None, None],
        ),
        MemberFormat.UVPair: (
            [("uv_u", "h"), ("uv_v", "h"), ("uv_u", "h"), ("uv_v", "h")],
            [("uv_u", "f"), ("uv_v", "f"), ("uv_u", "f"), ("uv_v", "f")],
            [None, None, None, None],
        ),
        MemberFormat.Short4ToFloat4A: (
            [("uv_u", "h"), ("uv_v", "h"), ("uv_w", "h"), ("uv_zero", "h")],
            [("uv_u", "f"), ("uv_v", "f"), ("uv_w", "f"), ("uv_zero", "f")],
            [None, None, None, None],
        ),
    },
    MemberType.Tangent: {
        MemberFormat.Float4: (
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4A: (
            [("tangent_x", "B"), ("tangent_y", "B"), ("tangent_z", "B"), ("tangent_w", "B")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4B: (
            [("tangent_x", "B"), ("tangent_y", "B"), ("tangent_z", "B"), ("tangent_w", "B")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4C: (
            [("tangent_x", "B"), ("tangent_y", "B"), ("tangent_z", "B"), ("tangent_w", "B")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4E: (
            [("tangent_x", "B"), ("tangent_y", "B"), ("tangent_z", "B"), ("tangent_w", "B")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Short4ToFloat4A: (
            [("tangent_x", "B"), ("tangent_y", "B"), ("tangent_z", "B"), ("tangent_w", "B")],
            [("tangent_x", "f"), ("tangent_y", "f"), ("tangent_z", "f"), ("tangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
    },
    MemberType.Bitangent: {
        MemberFormat.Byte4A: (
            [("bitangent_x", "B"), ("bitangent_y", "B"), ("bitangent_z", "B"), ("bitangent_w", "B")],
            [("bitangent_x", "f"), ("bitangent_y", "f"), ("bitangent_z", "f"), ("bitangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4B: (
            [("bitangent_x", "B"), ("bitangent_y", "B"), ("bitangent_z", "B"), ("bitangent_w", "B")],
            [("bitangent_x", "f"), ("bitangent_y", "f"), ("bitangent_z", "f"), ("bitangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4C: (
            [("bitangent_x", "B"), ("bitangent_y", "B"), ("bitangent_z", "B"), ("bitangent_w", "B")],
            [("bitangent_x", "f"), ("bitangent_y", "f"), ("bitangent_z", "f"), ("bitangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
        MemberFormat.Byte4E: (
            [("bitangent_x", "B"), ("bitangent_y", "B"), ("bitangent_z", "B"), ("bitangent_w", "B")],
            [("bitangent_x", "f"), ("bitangent_y", "f"), ("bitangent_z", "f"), ("bitangent_w", "f")],
            [_INT_TO_FLOAT_127_SIGNED] * 4,
        ),
    },
    MemberType.VertexColor: {
        MemberFormat.Float4: (
            [("color_r", "f"), ("color_g", "f"), ("color_b", "f"), ("color_a", "f")],
            [("color_r", "f"), ("color_g", "f"), ("color_b", "f"), ("color_a", "f")],
            [None] * 4,
        ),
        MemberFormat.Byte4A: (
            [("color_r", "B"), ("color_g", "B"), ("color_b", "B"), ("color_a", "B")],
            [("color_r", "f"), ("color_g", "f"), ("color_b", "f"), ("color_a", "f")],
            [_INT_TO_FLOAT_255] * 4,
        ),
        MemberFormat.Byte4C: (
            [("color_r", "B"), ("color_g", "B"), ("color_b", "B"), ("color_a", "B")],
            [("color_r", "f"), ("color_g", "f"), ("color_b", "f"), ("color_a", "f")],
            [_INT_TO_FLOAT_255] * 4,
        ),
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


@dataclass(slots=True)
class BufferLayoutStruct(BinaryStruct):

    _members_count: int
    _pad1: bytes = field(init=False, **BinaryPad(8))
    _members_offset: int


@dataclass(slots=True)
class BufferLayout:
    """Layout that describes the binary structure of a single vertex in a `VertexBuffer`.

    In Python, corresponds to a structured `np.dtype` and optioanl compression/decompression methods for each field.
    """

    members: list[LayoutMember] = field(default_factory=list)

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader):
        buffer_layout_struct = BufferLayoutStruct.from_bytes(reader)

        _members_count = buffer_layout_struct.pop("_members_count")
        _members_offset = buffer_layout_struct.pop("_members_offset")

        with reader.temp_offset(_members_offset):
            struct_offset = 0
            members = []
            for _ in range(_members_count):
                member = LayoutMember.from_flver_reader(reader, asserted_struct_offset=struct_offset)
                members.append(member)
                struct_offset += member.member_format.size()
        return buffer_layout_struct.to_object(cls, members=members)

    def to_flver_writer(self, writer: BinaryWriter):
        BufferLayoutStruct.object_to_writer(self, writer, _members_count=len(self.members))

    def pack_members(self, writer: BinaryWriter):
        writer.fill_with_position("_members_offset", obj=self)
        struct_offset = 0
        for member in self.members:
            member.to_flver_writer(writer, struct_offset)
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

    def get_vertex_colors_count(self):
        """Return total number of vertex color slots."""
        return sum(member.member_type == MemberType.VertexColor for member in self.members)

    def get_numpy_dtype_and_codecs(
        self, uv_factor: int
    ) -> tuple[np.dtype, np.dtype, list[tp.Callable], list[tp.Callable]]:
        """Construct a NumPy compound `dtype` corresponding to a single vertex's data.

        Also returns decompression and compression functions intended to be applied to the corresponding NumPy columns.

        NOTE: Does not perform any compression or decompression of data. Strictly corresponds to the buffer layout.
        """
        field_types = []
        decompressed_field_types = []
        decompress_funcs = []
        compress_funcs = []
        uv_count = 0
        color_count = 0
        for member in self.members:
            if member.member_type == MemberType.Position and member.member_format == MemberFormat.EdgeCompressed:
                # Explicitly not supported.
                raise NotImplementedError("Cannot read FLVERs with edge-compressed vertex positions.")
            if member.member_type not in DTYPE_PARSER:
                raise ValueError(f"Invalid vertex buffer layout member type: {member.member_type}")

            type_parser = DTYPE_PARSER[member.member_type]
            if member.member_format not in type_parser:
                raise NotImplementedError(f"Unsupported vertex buffer layout member type/format: {member}")

            fields, decompressed_fields, codecs = type_parser[member.member_format]
            if member.member_type == MemberType.UV:
                # Add UV indices to field names.
                if member.member_format in {MemberFormat.Float4, MemberFormat.UVPair}:
                    # Member contains TWO UVs.
                    field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in fields[:2]]
                    field_types += [(f"{f[0]}_{uv_count + 1}", f[1]) for f in fields[2:]]
                    decompressed_field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in decompressed_fields[:2]]
                    decompressed_field_types += [(f"{f[0]}_{uv_count + 1}", f[1]) for f in decompressed_fields[2:]]
                    uv_count += 2
                else:
                    field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in fields]
                    decompressed_field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in decompressed_fields]
                    uv_count += 1
            elif member.member_type == MemberType.VertexColor:
                # Add color indices to field names.
                field_types += [(f"{f[0]}_{color_count}", f[1]) for f in fields]
                decompressed_field_types += [(f"{f[0]}_{color_count}", f[1]) for f in decompressed_fields]
                color_count += 1
            else:
                field_types += fields
                decompressed_field_types += decompressed_fields

            codecs: list[None | tuple[tp.Callable, tp.Callable]]
            for codec in codecs:
                if codec is None:
                    decompress, compress = lambda x: x, lambda x: x
                else:
                    decompress, compress = codec
                if member.member_type == MemberType.UV and not member.member_format.name.startswith("Float"):
                    # Bake in UV factor.
                    decompress_funcs.append(lambda x, f=decompress: f(x / uv_factor))
                    compress_funcs.append(lambda x, f=compress: f(x) * uv_factor)
                else:
                    decompress_funcs.append(decompress)
                    compress_funcs.append(compress)

        return np.dtype(field_types), np.dtype(decompressed_field_types), decompress_funcs, compress_funcs

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


class VertexBufferSizeError(SoulstructError):
    """Raised by some vanilla meshes."""

    def __init__(self, vertex_size: int, layout_size: int):
        self.vertex_size = vertex_size
        self.layout_size = layout_size
        super().__init__(
            f"Vertex buffer vertex size {vertex_size} not equal to size calculated from layout: {layout_size}."
        )


@dataclass(slots=True)
class VertexBufferStruct(BinaryStruct):
    buffer_index: int
    layout_index: int
    vertex_size: int
    vertex_count: int
    _pad1: bytes = field(init=False, **BinaryPad(8))
    buffer_length: int
    buffer_offset: int


@dataclass(slots=True)
class VertexBuffer:
    """Header for a block of vertex data for one mesh.

    The structure of each vertex's data is defined by the indexed `BufferLayout`.
    """

    layout_index: int

    # Held temporarily.
    _struct: VertexBufferStruct | None = None

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader):
        vertex_buffer_struct = VertexBufferStruct.from_bytes(reader)
        return vertex_buffer_struct.to_object(cls, _struct=vertex_buffer_struct)

    def read_buffer(
        self,
        reader: BinaryReader,
        layouts: list[BufferLayout],
        vertex_data_offset: int,
        uv_factor: int,
    ) -> np.ndarray:
        layout = layouts[self.layout_index]
        layout_size = layout.get_total_size()
        expected_size = self._struct.buffer_length / self._struct.vertex_count
        if self._struct.vertex_size != expected_size:
            raise ValueError(
                f"Vertex buffer size ({self._struct.vertex_size}) != buffer length / vertex count ({expected_size})."
            )
        if self._struct.vertex_size != layout_size:
            # Layout could not be fixed in `FLVER` binary file reader. Mark mesh as invalid for user inspection.

            # TODO: Printing bytes.
            with reader.temp_offset(vertex_data_offset + self._struct.buffer_offset):
                first_vertex_bytes = reader.read(self._struct.vertex_size)
            # Decode as floats.
            first_vertex_floats = np.frombuffer(first_vertex_bytes, dtype=np.float32)
            # Decode as bytes.
            first_vertex_bytes = np.frombuffer(first_vertex_bytes, dtype=np.uint8)
            # Decode as shorts.
            first_vertex_shorts = np.frombuffer(first_vertex_bytes, dtype=np.uint16)
            # Print all.
            print(f"\nFLOATS: {first_vertex_floats}")
            print(f"BYTES: {first_vertex_bytes}")
            print(f"SHORTS: {first_vertex_shorts}")
            # Print 'bad' layout.
            print(f"BAD LAYOUT: {layout}")

            raise VertexBufferSizeError(self._struct.vertex_size, layout_size)

        with reader.temp_offset(vertex_data_offset + self._struct.buffer_offset):
            buffer_data = reader.read(self._struct.buffer_length)
            return get_vertex_array(buffer_data, layout, uv_factor)

    def get_vertex_count(self) -> int:
        if self._struct is None:
            raise ValueError("Cannot get `VertexBuffer` vertex count after struct has been consumed.")
        return self._struct.vertex_count

    def to_flver_writer(
        self,
        writer: BinaryWriter,
        version: Version,
        mesh_vertex_buffer_index: int,
        buffer_layouts: list[BufferLayout],
        mesh_vertex_count: int,
    ):
        layout_size = buffer_layouts[self.layout_index].get_total_size()
        VertexBufferStruct.object_to_writer(
            self,
            writer,
            buffer_index=mesh_vertex_buffer_index,
            vertex_size=layout_size,
            vertex_count=mesh_vertex_count,
            buffer_length=layout_size * mesh_vertex_count if version >= 0x20005 else 0,
            buffer_offset=RESERVED,
        )

    def pack_buffer(
        self,
        writer: BinaryWriter,
        buffer_layouts: list[BufferLayout],
        vertex_array: np.ndarray,
        buffer_offset: int,
        uv_factor: int,
    ):
        layout = buffer_layouts[self.layout_index]
        writer.fill("buffer_offset", buffer_offset, obj=self)
        writer.append(get_vertex_buffer(vertex_array, layout, uv_factor))

    def __repr__(self):
        return f"VertexBuffer(layout_index={self.layout_index})"


def get_vertex_array(buffer_data: bytes, layout: BufferLayout, uv_factor: int) -> np.ndarray:
    """Convert FLVER vertex buffer to NumPy array 'record' with named columns."""
    compressed_dtype, decompressed_dtype, dec_funcs, co_funcs = layout.get_numpy_dtype_and_codecs(uv_factor)
    buffer_array = np.frombuffer(buffer_data, dtype=compressed_dtype)
    decompressed_array = np.empty(len(buffer_array), dtype=decompressed_dtype)
    # Iterate over decompressed dtype and func.
    for decompress, (name, dtype) in zip(dec_funcs, decompressed_dtype.fields.items()):
        decompressed_array[name] = decompress(buffer_array[name].astype(dtype[0]))
    return decompressed_array


def get_vertex_buffer(vertex_array: np.ndarray, layout: BufferLayout, uv_factor: int) -> bytes:
    """Convert FLVER vertex buffer to NumPy array 'record' with named columns."""
    compressed_dtype, decompressed_dtype, dec_funcs, co_funcs = layout.get_numpy_dtype_and_codecs(uv_factor)
    compressed_array = np.empty(len(vertex_array), dtype=compressed_dtype)
    # Iterate over compressed dtype and func.
    for compress, (name, dtype) in zip(co_funcs, compressed_dtype.fields.items()):
        compressed_array[name] = compress(vertex_array[name].astype(dtype[0]))
    return compressed_array.tobytes()
