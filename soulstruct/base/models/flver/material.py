"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

from __future__ import annotations

__all__ = ["GXItem", "GXList", "Material", "Texture"]

import typing as tp

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader, BinaryWriter
from soulstruct.utilities.maths import Vector2

from .version import Version


class GXItem(BinaryObject):
    """Item that sets various material rendering properties."""

    STRUCT = BinaryStruct(
        ("gx_id", "4s"),  # actually "i" prior to Dark Souls 2 (0x20010) but always stored as bytes here for consistency
        ("unk_x04", "i"),
        ("__size", "i"),  # includes header
    )

    gx_id: bytes
    unk_x04: int
    data: bytes

    def unpack(self, reader: BinaryReader):
        gx_item = reader.unpack_struct(self.STRUCT)
        self.data = reader.read(gx_item.pop("__size") - self.STRUCT.size)
        self.set(**gx_item)

    def pack(self, writer: BinaryWriter):
        writer.pack_struct(
            self.STRUCT,
            self,
            __size=len(self.data) + self.STRUCT.size,
        )
        writer.append(self.data)

    def __repr__(self):
        return f"GXItem(gx_id = {self.gx_id}, unk_x04 = {self.unk_x04}, data = {self.data})"


class GXList:
    """List of `GXItem` instances, which set various material rendering properties.

    Literally just a sequence of packed `GXItem` structs jammed together, with a fairly useless terminator struct. The
    only reason this class exists is to track the exact form of the terminator struct for byte-perfect writes.

    Prior to Dark Souls 2 (version 0x20010), these lists only ever contained exactly one `GXItem`.
    """

    gx_items: tp.List[GXItem]

    def __init__(self, source: tp.Union[BinaryReader, tp.List[GXItem], None], version: Version = None):
        self.gx_items = []
        self.terminator_id = 2 ** 31 - 1  # max value of signed int; sometimes also -1
        self.terminator_null_count = 0

        if isinstance(source, BinaryReader):
            if version is None:
                raise ValueError("`version` must be given to unpack `GXList` from binary reader.")
            if version <= Version.DarkSouls2:
                self.gx_items = [GXItem(source)]
            else:
                self.unpack(source)
        elif isinstance(source, list) and all(isinstance(item, GXItem) for item in source):
            self.gx_items = source
        elif source is None:
            self.gx_items = []
        else:
            raise TypeError(f"Invalid `source` for `GXList`: {type(source)}")

    def unpack(self, reader: BinaryReader):
        self.gx_items = []
        while reader.unpack_value("<i", offset=reader.position) not in {2 ** 31 - 1, -1}:
            self.gx_items.append(GXItem(reader))
        self.terminator_id = reader.unpack_value("<i")  # either 2 ** 31 - 1 or -1
        reader.unpack_value("<i", asserted=100)
        self.terminator_null_count = reader.unpack_value("<i") - 12
        terminator_nulls = reader.read(self.terminator_null_count)
        if terminator_nulls.strip(b"\0"):
            raise ValueError(f"Found non-null data in terminator: {terminator_nulls}")

    def pack(self, writer: BinaryWriter):
        for gx_item in self.gx_items:
            gx_item.pack(writer)
        writer.pack("iii", self.terminator_id, 100, self.terminator_null_count + 12)
        writer.pad(self.terminator_null_count)

    def get_terminator_struct(self, terminator_id: int = None) -> BinaryStruct:
        if terminator_id is None:
            if self.terminator_id is None:
                raise ValueError("`GXItem` terminator ID has not yet been determined from `unpack()`.")
            terminator_id = self.terminator_id
        return BinaryStruct(
            ("terminator_id", "i", terminator_id),
            ("one_hundred", "i", 100),
            ("terminator_size", "i"),
        )

    def __repr__(self):
        return repr(self.gx_items)


class Texture(BinaryObject):

    STRUCT = BinaryStruct(
        ("__path__z", "i"),
        ("__texture_type__z", "i"),
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
        "scale": Vector2.ones(),
    }

    unpack = BinaryObject.default_unpack
    pack = BinaryObject.default_pack

    def __repr__(self):
        lines = [
            f"Texture(",
            f"  path = {repr(self.path)}",
            f"  texture_type = {repr(self.texture_type)}",
        ]
        if self.scale != (1.0, 1.0):
            lines.append(f"  scale = {self.scale}")
        if self.unk_x10 != 1:
            lines.append(f"  unk_x10 = {self.unk_x10}")
        if not self.unk_x11:
            lines.append(f"  unk_x11 = {self.unk_x11}")
        if self.unk_x14 != 0.0:
            lines.append(f"  unk_x14 = {self.unk_x14}")
        if self.unk_x18 != 0.0:
            lines.append(f"  unk_x18 = {self.unk_x18}")
        if self.unk_x1C != 0.0:
            lines.append(f"  unk_x1C = {self.unk_x1C}")
        lines.append(")")
        return "\n".join(lines)


class Material(BinaryObject):

    Texture = Texture

    STRUCT = BinaryStruct(
        ("__name__z", "i"),
        ("__mtd_path__z", "i"),
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

    textures: tp.List[Texture]

    _texture_count: int
    _first_texture_index: int

    def __init__(self, reader: BinaryReader, **kwargs):
        self.textures = []
        super().__init__(reader, **kwargs)

    def unpack(
        self,
        reader: BinaryReader,
        encoding: str,
        version: Version,
        gx_lists: tp.List[GXList],
        gx_list_indices: tp.Dict[int, int],
    ):
        material = reader.unpack_struct(self.STRUCT)
        self.name = reader.unpack_string(offset=material.pop("__name__z"), encoding=encoding)
        self.mtd_path = reader.unpack_string(offset=material.pop("__mtd_path__z"), encoding=encoding)
        gx_offset = material.pop("__gx_offset")
        if gx_offset == 0:
            self.gx_index = -1
        elif gx_offset in gx_list_indices:
            self.gx_index = gx_list_indices[gx_offset]
        else:
            self.gx_index = gx_list_indices[gx_offset] = len(gx_lists)
            with reader.temp_offset(gx_offset):
                gx_lists.append(GXList(reader, version))
        self.set(**material)

    def assign_textures(self, textures: tp.Dict[int, Texture]):
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

    def pack(self, writer: BinaryWriter):
        writer.pack_struct(
            self.STRUCT,
            self,
            __name__z=writer.AUTO_RESERVE,
            __mtd_path__z=writer.AUTO_RESERVE,
            _first_texture_index=writer.AUTO_RESERVE,
            __gx_offset=writer.AUTO_RESERVE,
            _texture_count=len(self.textures),
        )

    def pack_textures(self, writer: BinaryWriter, first_texture_index: int):
        writer.fill("_first_texture_index", first_texture_index, obj=self)
        for texture in self.textures:
            texture.pack(writer)

    def fill_gx_offset(self, writer: BinaryWriter, gx_offsets: tp.List[int]):
        writer.fill("__gx_offset", 0 if self.gx_index == -1 else gx_offsets[self.gx_index], obj=self)

    def pack_strings(self, writer: BinaryWriter, encoding: str):
        self.pack_zstring(writer, "name", encoding=encoding)
        self.pack_zstring(writer, "mtd_path", encoding=encoding)

    def get_texture_dict(self) -> tp.Dict[str, Texture]:
        """Get a dictionary mapping texture types to `Texture` instances.

        Will raise a KeyError if any texture type is repeated.
        """
        textures = {}
        for texture in self.textures:
            if texture.texture_type in textures:
                raise KeyError(f"Texture type {texture.texture_type} appeared more than once in Material {self.name}.")
            textures[texture.texture_type] = texture
        return textures

    def __repr__(self):
        textures = ",\n".join(["    " + indent_lines(repr(texture)) for texture in self.textures])
        lines = [
            f"Material(",
            f"  name = {repr(self.name)}",
            f"  mtd_path = {repr(self.mtd_path)}",
            f"  flags = {self.flags:032b}",
        ]
        if self.gx_index != -1:
            lines.append(f"  gx_index = {self.gx_index}")
        if self.unk_x18 != 0:
            lines.append(f"  unk_x18 = {self.unk_x18}")
        lines.append(f"  textures = [\n{textures}\n  ]")
        lines.append(")")
        return "\n".join(lines)
