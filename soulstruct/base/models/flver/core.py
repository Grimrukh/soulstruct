from __future__ import annotations

__all__ = ["FLVER"]

import io
import typing as tp
from enum import IntEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.maths import Vector2, Vector3, Vector4
from soulstruct.utilities import unpack_from_buffer, read_chars_from_buffer, Flags8
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject


class Version(IntEnum):
    Null = 0x0
    DarkSouls2_Armor9320 = 0x20009
    DarkSouls_PS3_o0700_o0701 = 0x2000B
    DarkSouls_A = 0x2000C
    DarkSouls_B = 0x2000D
    DarkSouls2_NT = 0x2000F
    DarkSouls2 = 0x20010  # includes SOTFS
    Bloodborne_DS3_A = 0x20013
    Bloodborne_DS3_B = 0x20014
    Sekiro_TestChr = 0x20016
    Sekiro = 0x2001A

    @classmethod
    def default(cls):
        return cls.Null


class Color:

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @classmethod
    def from_bgra(cls, blue, green, red, alpha):
        return cls(red, green, blue, alpha)

    @classmethod
    def from_argb(cls, alpha, red, green, blue):
        return cls(red, green, blue, alpha)

    @classmethod
    def black(cls):
        return cls(0, 0, 0, 1)

    default = black

    def __repr__(self):
        return f"Color(red={self.red}, green={self.green}, blue={self.blue}, alpha={self.alpha})"


class FLVERHeader(BinaryObject):

    STRUCT = BinaryStruct(
        ("file_type", "6s", "FLVER\0"),
        ("endian", "2s"),  # TODO: b"L\0" or b"B\0"
        ("version", "i"),  # `Version`
        ("data_offset", "i"),
        ("data_size", "i"),
        ("dummy_count", "i"),
        ("material_count", "i"),
        ("bone_count", "i"),
        ("mesh_count", "i"),
        ("vertex_buffer_count", "i"),
        ("bounding_box_min", "3f"),  # `Vector3`
        ("bounding_box_max", "3f"),  # `Vector3`
        ("raw_face_count", "i"),  # does not include motion blur meshes or degenerate faces
        ("total_face_count", "i"),  # all faces
        ("vertex_indices_size", "B"),  # 0, 8, 16, 32
        ("unicode", "?"),
        ("unk_x4a", "?"),
        "x",
        ("unk_x4c", "i"),
        ("face_set_count", "i"),
        ("buffer_layout_count", "i"),
        ("texture_count", "i"),
        ("unk_x5c", "B"),
        ("unk_x5d", "B"),
        "10x",
        ("unk_x68", "i"),
        "20x",
    )

    endian: bytes
    version: Version
    data_offset: int
    data_size: int
    dummy_count: int
    material_count: int
    bone_count: int
    mesh_count: int
    vertex_buffer_count: int
    bounding_box_min: Vector3
    bounding_box_max: Vector3
    raw_face_count: int
    total_face_count: int
    vertex_indices_size: int
    unicode: bool
    unk_x4a: bool
    unk_x4c: int
    face_set_count: int
    buffer_layout_count: int
    texture_count: int
    unk_x5c: int
    unk_x5d: int
    unk_x68: int


class Dummy(BinaryObject):

    STRUCT = BinaryStruct(
        ("position", "3f"),
        ("color", "4B"),
        ("forward", "3f"),
        ("reference_id", "h"),
        ("parent_bone_index", "h"),
        ("upward", "3f"),
        ("attach_bone_index", "h"),
        ("flag_1", "?"),
        ("use_upward_vector", "?"),
        ("unk_x30", "i"),
        ("unk_x34", "i"),
        "8x",
    )

    position: Vector3
    color: Color
    forward: Vector3
    reference_id: int
    parent_bone_index: int
    upward: Vector3
    attach_bone_index: int
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int
    unk_x34: int

    def unpack(self, buffer: io.BufferedIOBase, color_is_argb=None):
        if color_is_argb is None:
            raise ValueError
        data = self.STRUCT.unpack(buffer)
        self.color = (Color.from_argb if color_is_argb else Color.from_bgra)(data.pop("color"))
        self.set(**data)


class GXItem(BinaryObject):
    """Item that sets various material rendering properties."""

    STRUCT = BinaryStruct(
        ("gx_id", "4s"),  # actually "i" prior to Dark Souls 2 (0x20010) but always stored as bytes here for consistency
        ("unk_x04", "i"),
        ("size", "i"),  # includes header
    )

    gx_id: bytes
    unk_x04: int
    data: bytes

    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        data = self.STRUCT.unpack(buffer)
        self.gx_id = data["gx_id"]
        self.unk_x04 = data["unk_x04"]
        self.data = buffer.read(data["length"] - self.STRUCT.size)

    def pack(self):
        """TODO"""


class GXList:
    """List of `GXItem` instances, which set various material rendering properties.

    Literally just a sequence of packed `GXItem` structs jammed together, with a fairly useless terminator struct. The
    only reason this class exists is to track the exact form of the terminator struct for byte-perfect writes.

    Prior to Dark Souls 2 (version 0x20010), these lists only ever contained exactly one `GXItem`.
    """

    def __init__(self, source: tp.Union[io.BufferedIOBase, list[GXItem], None], version: Version = None):
        self.gx_items = []
        self.terminator_id = 2 ** 31 - 1  # max value of signed int; sometimes also -1
        self.terminator_null_count = 0

        if isinstance(source, io.BufferedIOBase):
            if version is None:
                raise ValueError("`version` must be given to unpack `GXList` from binary buffer.")
            if version <= Version.DarkSouls2:
                self.gx_items = [GXItem(source)]
            else:
                self.unpack(source)
        elif isinstance(source, list) and all(isinstance(item, GXItem) for item in source):
            self.gx_items = source
        elif source is None:
            self.gx_items = []

        raise TypeError(f"Invalid `source` for `GXList`: {type(source)}. Must be a buffer, list of `GXItem`s, or None.")

    def unpack(self, buffer):
        self.gx_items = []
        while (gx_id := unpack_from_buffer(buffer, "<i", offset=buffer.tell())) not in {2 ** 31 - 1, -1}:
            self.gx_items.append(GXItem(buffer))
        self.terminator_id = gx_id
        terminator_data = BinaryStruct(
            ("terminator_id", "i", gx_id),
            ("one_hundred", "i", 100),
            ("terminator_size", "i"),
        )
        terminator = terminator_data.unpack(buffer)
        self.terminator_id = terminator["terminator_id"]
        self.terminator_null_count = terminator["terminator_size"] - terminator_data.size
        if (terminator_nulls := buffer.read(self.terminator_null_count)).strip(b"\0"):
            raise ValueError(f"Found non-null data in terminator: {terminator_nulls}")


class Material(BinaryObject):

    STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("__mtd_path_offset", "i"),
        ("_texture_count", "i"),
        ("_first_texture_index", "i"),
        ("flags", "i"),
        ("__gx_offset", "i"),
        ("unk_x18", "i"),
        "4x",
    )

    name: str
    mtd_path: str
    flags: int
    gx_index: int
    unk_x18: int
    textures: list[Texture]

    _texture_count: int
    _first_texture_index: int

    def __init__(self, source, unpack_kwargs, **kwargs):
        self.textures = []
        super().__init__(source, unpack_kwargs, **kwargs)

    def unpack(
        self,
        buffer: io.BufferedIOBase,
        unicode: bool = None,
        version: Version = None,
        gx_lists: list[GXList] = None,
        gx_list_indices: dict[int, int] = None,
    ):
        if any(var is None for var in (unicode, version, gx_lists, gx_list_indices)):
            raise ValueError("Not all required keywords were passed to `Material.unpack()`.")

        data = self.STRUCT.unpack(buffer)
        encoding = "utf-16-le" if unicode else "shift_jis_2004"
        self.name = read_chars_from_buffer(buffer, offset=data.pop("__name_offset"), encoding=encoding)
        self.mtd_path = read_chars_from_buffer(buffer, offset=data.pop("__mtd_path_offset"), encoding=encoding)
        gx_offset = data.pop("__gx_offset")
        if gx_offset == 0:
            self.gx_index = -1
        elif gx_offset in gx_list_indices:
            self.gx_index = gx_list_indices[gx_offset]
        else:
            gx_list_indices[gx_offset] = len(gx_lists)
            material_offset = buffer.tell()
            buffer.seek(gx_offset)
            gx_lists.append(GXList(buffer, version))
            buffer.seek(material_offset)
        self.set(**data)

    def pack(self):
        """TODO"""

    def assign_textures(self, textures: dict[int, Texture]):
        if self._texture_count == -1 or self._first_texture_index == -1:
            raise ValueError(f"Tried to call `assign_textures()` on `Material` {self.name} more than once.")
        for i in range(self._first_texture_index, self._first_texture_index + self._texture_count):
            if i not in textures:
                raise KeyError(
                    f"Tried to assign `Texture` with index {i} to `Material` {self.name}, but the `Texture` has "
                    "already been assigned to another `Material` (or does not exist)."
                )
            self.textures.append(textures.pop(i))
        self._texture_count = -1
        self._first_texture_index = -1

    def __repr__(self):
        textures = ",\n".join([
            "    " + "\n    ".join(repr(tex).split("\n")) for tex in self.textures
        ])
        return (
            f"Material(\n"
            f"  name = {repr(self.name)}\n"
            f"  mtd_path = {repr(self.mtd_path)}\n"
            f"  flags = {self.flags}\n"
            f"  gx_index = {self.gx_index}\n"
            f"  unk_x18 = {self.unk_x18}\n"
            f"  textures = [\n"
            f"{textures}\n"
            f"  ]\n"
            f")"
        )


class Bone(BinaryObject):

    STRUCT = BinaryStruct(
        ("translate", "3f"),
        ("__name_offset", "i"),
        ("rotate", "3f"),
        ("parent_index", "h"),
        ("child_index", "h"),
        ("scale", "3f"),
        ("next_sibling_index", "h"),
        ("previous_sibling_index", "h"),
        ("bounding_box_min", "3f"),
        ("unk_x3c", "i"),
        ("bounding_box_max", "3f"),
        "52x",
    )

    translate: Vector3
    name: str
    rotate: Vector3
    parent_index: int
    child_index: int
    scale: Vector3
    next_sibling_index: int
    previous_sibling_index: int
    bounding_box_min: Vector3
    unk_x3c: int
    bounding_box_max: Vector3

    def unpack(self, buffer: io.BufferedIOBase, unicode=None):
        data = self.STRUCT.unpack(buffer)
        encoding = "utf-16-le" if unicode else "shift_jis_2004"
        self.name = read_chars_from_buffer(buffer, offset=data.pop("__name_offset"), encoding=encoding)
        self.set(**data)


class BoundingBox(BinaryObject):

    STRUCT = BinaryStruct(
        ("minimum", "3f"),
        ("maximum", "3f"),
    )

    minimum: Vector3
    maximum: Vector3

    def __repr__(self):
        return f"BoundingBox(minimum={tuple(self.minimum)}, maximum={tuple(self.maximum)})"


class BoundingBoxWithUnknown(BoundingBox):
    STRUCT = BinaryStruct(
        ("minimum", "3f"),
        ("maximum", "3f"),
        ("unknown", "3f"),
    )

    minimum: Vector3
    maximum: Vector3
    unknown: Vector3

    def __repr__(self):
        return (
            f"BoundingBoxWithUnknown("
            f"minimum={tuple(self.minimum)}, maximum={tuple(self.maximum)}, unknown={tuple(self.unknown)}"
            f")"
        )


class Mesh(BinaryObject):

    STRUCT = BinaryStruct(
        ("is_bind_pose", "?"),
        "3x",
        ("material_index", "i"),
        "8x",
        ("default_bone_index", "i"),
        ("__bone_count", "i"),
        ("__bounding_box_offset", "i"),
        ("__bone_offset", "i"),
        ("__face_set_count", "i"),
        ("__face_set_offset", "i"),
        ("__vertex_buffer_count", "i"),  # 1, 2, or 3
        ("__vertex_buffer_offset", "i"),
    )

    is_bind_pose: bool
    material_index: int
    default_bone_index: int
    bone_indices: list[int]
    bounding_box: tp.Optional[BoundingBox]

    face_sets: list[FaceSet]
    vertex_buffers: list[VertexBuffer]
    vertices: list[Vertex]

    _face_set_indices: tp.Optional[list[int]]
    _vertex_buffer_indices: tp.Optional[list[int]]

    DEFAULTS = {
        "default_bone_index": -1,
    }

    def __init__(self, source, unpack_kwargs, **kwargs):
        self.face_sets = []
        self.vertex_buffers = []
        self.vertices = []
        super().__init__(source, unpack_kwargs, **kwargs)

    def assign_face_sets(self, face_sets: dict[int, FaceSet]):
        self.face_sets = []
        if self._face_set_indices is None:
            raise ValueError("Tried to call `assign_face_sets()` on a `Mesh` more than once.")
        for i in self._face_set_indices:
            if i not in face_sets:
                raise KeyError(
                    f"Tried to assign `FaceSet` with index {i} to `Mesh`, but the `FaceSet` has "
                    "already been assigned to another `Mesh` (or does not exist)."
                )
            self.face_sets.append(face_sets.pop(i))
        self._face_set_indices = None

    def unpack(self, buffer: io.BufferedIOBase, bounding_box_has_unknown: bool = None):
        data = self.STRUCT.unpack(buffer)
        mesh_offset = buffer.tell()

        bounding_box_offset = data.pop("__bounding_box_offset")
        if bounding_box_offset != 0:
            buffer.seek(bounding_box_offset)
            self.bounding_box = BoundingBoxWithUnknown(buffer) if bounding_box_has_unknown else BoundingBox(buffer)
        else:
            self.bounding_box = None

        buffer.seek(data.pop("__bone_offset"))
        bone_count = data.pop("__bone_count")
        self.bone_indices = list(unpack_from_buffer(buffer, f"<{bone_count}i",))

        buffer.seek(data.pop("__face_set_offset"))
        face_set_count = data.pop("__face_set_count")
        self._face_set_indices = list(unpack_from_buffer(buffer, f"<{face_set_count}i"))

        buffer.seek(data.pop("__vertex_buffer_offset"))
        vertex_count = data.pop("__vertex_buffer_count")
        self._vertex_buffer_indices = list(unpack_from_buffer(buffer, f"<{vertex_count}i"))

        buffer.seek(mesh_offset)
        self.set(**data)

    def assign_vertex_buffers(self, vertex_buffers: dict[int, VertexBuffer], layouts: list[BufferLayout]):
        self.vertex_buffers = []
        if self._vertex_buffer_indices is None:
            raise ValueError("Tried to call `assign_vertex_buffers()` on a `Mesh` more than once.")
        for i in self._vertex_buffer_indices:
            if i not in vertex_buffers:
                raise KeyError(
                    f"Tried to assign `VertexBuffer` with index {i} to `Mesh`, but the `VertexBuffer` has "
                    "already been assigned to another `Mesh` (or does not exist)."
                )
            self.vertex_buffers.append(vertex_buffers.pop(i))
        self._vertex_buffer_indices = None

        # Check that unique `LayoutSemantic` types do not occur more than once among all `BufferLayout` members.
        existing_semantics = set()
        for vertex_buffer in self.vertex_buffers:
            for member in layouts[vertex_buffer.layout_index]:
                if member.semantic.unique():
                    if member.semantic in existing_semantics:
                        raise ValueError(
                            f"Unique `LayoutSemantic` {member.semantic} found more than once in `BufferLayouts` "
                            f"of `Mesh`."
                        )
                    existing_semantics.add(member.semantic)

        # TODO: TKGP does an extra check here for edge-compressed vertex buffers, which are not supported.

    def read_vertices(self, buffer: io.BufferedIOBase, data_offset: int, layouts: list[BufferLayout], version: Version):
        all_members = [member for layout in layouts for member in layout]
        max_uv_count = len([member for member in all_members if member.semantic == LayoutSemantic.UV])
        max_tangent_count = len([[member for member in all_members if member.semantic == LayoutSemantic.Tangent]])
        max_color_count = len([[member for member in all_members if member.semantic == LayoutSemantic.VertexColor]])

        self.vertices = [
            Vertex(max_uv_count, max_tangent_count, max_color_count)
            for _ in range(self.vertex_buffers[0].vertex_count)
        ]

        for vertex_buffer in self.vertex_buffers:
            vertex_buffer.read_buffer(buffer, layouts, self.vertices, data_offset, version)

    def __repr__(self):
        vertices = ",\n".join([
            f"    {v.repr_position_only()}" for v in self.vertices
        ])
        face_sets = ",\n".join([
            "    " + "\n    ".join(repr(f).split("\n")) for f in self.face_sets
        ])
        return (
            f"Mesh(\n"
            f"  is_bind_pose={self.is_bind_pose}\n"
            f"  material_index={self.material_index}\n"
            f"  default_bone_index={self.default_bone_index}\n"
            f"  bone_indices={self.bone_indices}\n"
            f"  bounding_box={self.bounding_box}\n"
            f"  vertices = [\n"
            f"{vertices}\n"
            f"  ]\n"
            f"  face_sets = [\n"
            f"{face_sets}\n"
            f"  ]\n"
            f")"
        )


class FaceSetFlags(Flags8):
    @property
    def LodLevel1(self):
        return self.flags[0]

    @property
    def LodLevel2(self):
        return self.flags[1]

    @property
    def EdgeCompressed(self):
        return self.flags[6]

    @property
    def MotionBlur(self):
        return self.flags[7]


class FaceSet(BinaryObject):

    STRUCT = BinaryStruct(
        ("flags", "B"),
        "3x",
        ("triangle_strip", "?"),
        ("cull_back_faces", "?"),
        ("unk_x06", "h"),
        ("__indices_count", "i"),
        ("__indices_offset", "i"),  # header stops here for versions < 0x20005, which are not supported by Soulstruct
        ("__indices_length", "i"),
        "4x",
        ("__index_size", "i"),  # 0 (header), 16, or 32
        "4x",
    )

    flags: FaceSetFlags
    triangle_strip: bool
    cull_back_faces: bool
    unk_x06: int
    indices: list[int]

    def unpack(self, buffer: io.BufferedIOBase, header_index_size: int = None, data_offset: int = None):
        data = self.STRUCT.unpack(buffer)

        if (index_size := data.pop("__index_size")) == 0:
            index_size = header_index_size

        if index_size == 8:
            raise NotImplementedError("Soulstruct cannot support edge-compressed FLVER face sets.")
        elif index_size in {16, 32}:
            face_set_offset = buffer.tell()
            indices_count = data.pop("__indices_count")
            indices_offset = data.pop("__indices_offset")
            buffer.seek(data_offset + indices_offset)
            if index_size == 16:
                self.indices = list(unpack_from_buffer(buffer, f"<{indices_count}H"))
            elif index_size == 32:
                self.indices = list(unpack_from_buffer(buffer, f"<{indices_count}H"))
            buffer.seek(face_set_offset)
        else:
            raise ValueError(f"Unsupported face set index size: {index_size}")

        self.set(**data)

    def __repr__(self):
        return (
            f"FaceSet(\n"
            f"  flags = {self.flags}\n"
            f"  triangle_strip = {self.triangle_strip}\n"
            f"  cull_back_faces = {self.cull_back_faces}\n"
            f"  unk_x06 = {self.unk_x06}\n"
            f"  indices = {self.indices}\n"
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


class Texture(BinaryObject):

    STRUCT = BinaryStruct(
        ("__path_offset", "i"),
        ("__texture_type_offset", "i"),
        ("scale", "2f"),
        ("unk_x10", "B"),  # 0, 1, or 2
        ("unk_x11", "?"),
        "2x",
        ("unk_x14", "f"),
        ("unk_x18", "f"),
        ("unk_x1C", "f"),
    )

    path: str
    texture_type: str
    scale: Vector2
    unk_x10: int
    unk_x11: bool
    unk_x14: float
    unk_x18: float
    unk_x1C: float

    DEFAULTS = {
        "scale": Vector2.ones,
    }

    def unpack(self, buffer: io.BufferedIOBase, unicode: bool = None):
        data = self.STRUCT.unpack(buffer)
        encoding = "utf-16-le" if unicode else "shift_jis_2004"
        self.path = read_chars_from_buffer(buffer, offset=data.pop("__path_offset"), encoding=encoding)
        self.texture_type = read_chars_from_buffer(buffer, offset=data.pop("__texture_type_offset"), encoding=encoding)
        self.set(**data)

    def __repr__(self):
        return (
            f"Texture(\n"
            f"  path = {repr(self.path)}\n"
            f"  texture_type = {repr(self.texture_type)}\n"
            f"  scale = {self.scale}\n"
            f"  unk_x10 = {self.unk_x10}\n"
            f"  unk_x11 = {self.unk_x11}\n"
            f"  unk_x14 = {self.unk_x14}\n"
            f"  unk_x18 = {self.unk_x18}\n"
            f"  unk_x1C = {self.unk_x1C}\n"
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

    def __init__(self, max_uv_count=0, max_tangent_count=0, max_color_count=0):
        self._max_uv_count = max_uv_count
        self._max_tangent_count = max_tangent_count
        self._max_color_count = max_color_count

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
            elif len(self.uvs) > self._max_uv_count:
                raise ValueError(
                    f"Vertex UV count ({len(self.uvs)}) exceeded maximum ({self._max_uv_count})."
                )
            elif len(self.tangents) > self._max_tangent_count:
                raise ValueError(
                    f"Vertex tangent count ({len(self.tangents)}) exceeded maximum ({self._max_tangent_count})."
                )
            elif len(self.colors) > self._max_color_count:
                raise ValueError(
                    f"Vertex color count ({len(self.colors)}) exceeded maximum ({self._max_color_count})."
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


class FLVER(GameFile):
    """Model format used since Dark Souls PTDE.

    Technically, this format is FLVER2. Demon's Souls used a different format, FLVER0, which is not supported here.
    """

    def __init__(
        self,
        file_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase] = None,
        dcx_magic: tuple[int, int] = (),
        **kwargs,
    ):
        self.header = FLVERHeader()
        self.dummies = []  # type: list[Dummy]
        self.gx_lists = []  # type: list[GXList]
        self.materials = []  # type: list[Material]
        self.bones = []  # type: list[Bone]
        self.meshes = []  # type: list[Mesh]
        self.buffer_layouts = []  # type: list[BufferLayout]
        # TODO

        super().__init__(file_source, dcx_magic, **kwargs)

    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        self.header = FLVERHeader(buffer)

        self.dummies = [
            Dummy(buffer, dict(is_argb=self.header.version == Version.DarkSouls2))
            for _ in range(self.header.dummy_count)
        ]

        gx_list_indices = {}  # type: dict[int, int]  # maps `_gx_offset` in `Material` to `self.gx_lists` index
        self.gx_lists = []
        self.materials = [
            Material(
                buffer,
                dict(
                    unicode=self.header.unicode,
                    version=self.header.version,
                    gx_lists=self.gx_lists,
                    gx_list_indices=gx_list_indices,
                )
            )
            for _ in range(self.header.material_count)
        ]

        self.bones = [
            Bone(buffer, dict(unicode=self.header.unicode))
            for _ in range(self.header.bone_count)
        ]

        self.meshes = [
            Mesh(buffer, dict(bounding_box_has_unknown=self.header.version == Version.Sekiro))
            for _ in range(self.header.mesh_count)
        ]

        face_sets = {
            i: FaceSet(
                buffer,
                dict(
                    header_index_size=self.header.vertex_indices_size,
                    data_offset=self.header.data_offset,
                )
            )
            for i in range(self.header.face_set_count)
        }

        vertex_buffers = {i: VertexBuffer(buffer) for i in range(self.header.vertex_buffer_count)}

        self.buffer_layouts = [BufferLayout(buffer) for _ in range(self.header.buffer_layout_count)]

        textures = {i: Texture(buffer, dict(unicode=self.header.unicode)) for i in range(self.header.texture_count)}

        # TODO: Sekiro has an additional unknown structure here.

        for material in self.materials:
            # Each texture is only assigned to ONE material. Texture is popped from `textures` after first assignment.
            material.assign_textures(textures)
        if textures:
            raise ValueError(f"{len(textures)} `Texture`s were left over after assignment to `Material`s.")

        for mesh in self.meshes:
            mesh.assign_face_sets(face_sets)
            mesh.assign_vertex_buffers(vertex_buffers, self.buffer_layouts)
            mesh.read_vertices(buffer, self.header.data_offset, self.buffer_layouts, self.header.version)
        if face_sets:
            raise ValueError(f"{len(face_sets)} `FaceSet`s were left over after assignment to `Mesh`es.")
        if vertex_buffers:
            raise ValueError(f"{len(vertex_buffers)} `VertexBuffer`s were left over after assignment to `Mesh`es.")

    def pack(self):
        """TODO"""
        raise NotImplementedError("Pack not implemented yet.")


if __name__ == '__main__':
    from soulstruct import DSR_PATH
    flver = FLVER(DSR_PATH + "/map/m10_00_00_00/m2080B0.flver.dcx")
    print(flver.materials)
    # print(flver.meshes)
