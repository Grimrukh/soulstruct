from __future__ import annotations

__all__ = ["GXItem", "GXList", "Material", "Texture"]

import io
import typing as tp

from soulstruct.utilities import read_chars_from_buffer, unpack_from_buffer, indent_lines
from soulstruct.utilities.binary_struct import BinaryStruct, BinaryObject
from soulstruct.utilities.maths import Vector2

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary_struct import BinaryWriter
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

    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        data = self.STRUCT.unpack(buffer)
        self.data = buffer.read(data.pop("__size") - self.STRUCT.size)
        self.set(**data)

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
        else:
            raise TypeError(f"Invalid `source` for `GXList`: {type(source)}. Must be a buffer, list of `GXItem`s, or None.")

    def unpack(self, buffer):
        self.gx_items = []
        while (gx_id := unpack_from_buffer(buffer, "<i", offset=buffer.tell())):
            (gx_id,) = gx_id
            if gx_id in [2 ** 31 - 1, -1]:
                break
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
        "scale": Vector2.ones(),
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

    def pack(
        self,
        name_offset: int = None,
        mtd_path_offset: int = None,
        first_texture_index: int = None,
        gx_offset: int = None,
    ) -> bytes:
        """Pack with all offsets known."""
        if any(kwarg is None for kwarg in (name_offset, mtd_path_offset, first_texture_index, gx_offset)):
            raise ValueError("`Material.pack()` did not receive all necessary keyword arguments.")
        return self.STRUCT.pack(
            self,
            __name_offset=name_offset,
            __mtd_path_offset=mtd_path_offset,
            _texture_count=len(self.textures),
            _first_texture_index=first_texture_index,
            __gx_offset=gx_offset,
        )

    def pack_writer(self, writer: BinaryWriter, material_index: int):
        writer.pack_struct(
            self.STRUCT,
            self,
            __name_offset=writer.Reserved(f"MaterialNameOffset{material_index}"),
            __mtd_path_offset=writer.Reserved(f"MaterialMTDPathOffset{material_index}"),
            _first_texture_index=writer.Reserved(f"MaterialFirstTextureIndex{material_index}"),
            __gx_offset=writer.Reserved(f"MaterialGXOffset{material_index}"),
            _texture_count=len(self.textures),
        )

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
        textures = ",\n".join(["    " + indent_lines(repr(texture)) for texture in self.textures])
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
