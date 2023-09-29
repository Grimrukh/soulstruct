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

    def get_dtype(self) -> np.dtype:
        """Get decompressed NumPy dtype ONLY for this `BufferLayout`."""
        decompressed_field_types = []
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
                    decompressed_field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in decompressed_fields[:2]]
                    decompressed_field_types += [(f"{f[0]}_{uv_count + 1}", f[1]) for f in decompressed_fields[2:]]
                    uv_count += 2
                else:
                    decompressed_field_types += [(f"{f[0]}_{uv_count}", f[1]) for f in decompressed_fields]
                    uv_count += 1
            elif member.member_type == MemberType.VertexColor:
                # Add color indices to field names.
                decompressed_field_types += [(f"{f[0]}_{color_count}", f[1]) for f in decompressed_fields]
                color_count += 1
            else:
                decompressed_field_types += decompressed_fields

        return np.dtype(decompressed_field_types)

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
