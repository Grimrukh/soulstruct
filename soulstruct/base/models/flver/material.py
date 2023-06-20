from __future__ import annotations

__all__ = ["MTDInfo", "GXItem", "GXList", "Material", "Texture"]

import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector2

from .version import Version


@dataclass(slots=True)
class MTDInfo:
    """Various booleans that indicate required textures for a specific MTD shader."""

    # g_Diffuse, g_Specular, g_Bumpmap, g_Height. These all appear in the same square brackets in the same order.
    MTD_DSB_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(D)?(S)?(B)?(H)?\].*")

    # Double DSB slots
    MTD_M_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(M|ML|LM)\].*")

    # g_Lightmap
    MTD_L_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(L|ML|LM)\].*")

    # Checked separately: [Dn] (g_Diffuse only), [We] (g_Bumpmap only)

    # TODO: Not sure if 'M_{n}*' is a general pattern for extra UV slots at n - 1, or if it's just a non-enforced hint.
    MTD_FOLIAGE_PREFIXES: tp.ClassVar[str, int] = {
        "M_2Foliage": 1,
        "M_3Ivy": 2,
    }  # MTD name prefixes that indicate two extra UV slots, and the required index of their first UV data.

    # TODO: Hardcoding a set of 'water' shader names I've encountered in DSR.
    WATER_NAMES: tp.ClassVar[set[str]] = {
        "A14_numa.mtd",  # Blighttown swamp
        "A12_DarkRiver.mtd",
        "A12_DarkWater.mtd",
    }

    mtd_name: str
    diffuse: bool = field(init=False, default=False)
    specular: bool = field(init=False, default=False)
    bumpmap: bool = field(init=False, default=False)
    height: bool = field(init=False, default=False)
    multiple: bool = field(init=False, default=False)
    lightmap: bool = field(init=False, default=False)
    alpha: bool = field(init=False, default=False)
    edge: bool = field(init=False, default=False)
    water: bool = field(init=False, default=False)
    no_tangents: bool = field(init=False, default=False)  # no tangent data in vertex buffer (in DS1)
    extra_uv_maps: None | tuple[int, int] = field(init=False, default=None)  # extra UV slots and first index of them

    def __post_init__(self):
        if dsbh_match := self.MTD_DSB_RE.match(self.mtd_name):
            self.diffuse = bool(dsbh_match.group(1))
            self.specular = bool(dsbh_match.group(2))
            self.bumpmap = bool(dsbh_match.group(3))
            self.height = bool(dsbh_match.group(4))

        self.multiple = bool(self.MTD_M_RE.match(self.mtd_name))
        self.lightmap = bool(self.MTD_L_RE.match(self.mtd_name))

        if "[Dn]" in self.mtd_name:
            self.diffuse = True
            self.no_tangents = True  # TODO: A few [D] shaders also don't use tangents...
        if "[We]" in self.mtd_name or self.mtd_name in self.WATER_NAMES:
            self.water = True
            self.bumpmap = True
        for prefix, first_uv_index in self.MTD_FOLIAGE_PREFIXES.items():
            if self.mtd_name.startswith(prefix):
                self.extra_uv_maps = (2, first_uv_index)
                break  # can't match more than one
        self.alpha = "_Alp" in self.mtd_name
        self.edge = "_Edge" in self.mtd_name


@dataclass(slots=True)
class GXItem(BinaryStruct):
    """Item that sets various material rendering properties."""

    gx_id: bytes = field(**BinaryString(4))
    unk_x04: int
    size: int
    data: bytes = field(init=False, metadata={"NOT_BINARY": True})  # `size - 12` bytes


@dataclass(slots=True)
class GXList:
    """List of `GXItem` instances, which set various material rendering properties.

    Literally just a sequence of packed `GXItem` structs jammed together, with a fairly useless terminator struct. The
    only reason this class exists is to track the exact form of the terminator struct for byte-perfect writes.

    Prior to Dark Souls 2 (version 0x20010), these lists only ever contained exactly one `GXItem`.
    """
    gx_items: list[GXItem]
    terminator_id: int = 2 ** 31 - 1
    terminator_null_count: int = 0

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, flver_version: Version):
        if flver_version <= Version.DarkSouls2:
            # Only one `GXItem`.
            gx_item = GXItem.from_bytes(reader)
            gx_item.data = reader.read(gx_item.size - 12)
            return cls([gx_item])
        gx_items = []
        while reader["i", reader.position] not in {2 ** 31 - 1, -1}:
            gx_item = GXItem.from_bytes(reader)
            gx_item.data = reader.read(gx_item.size - 12)
            gx_items.append(gx_item)
        terminator_id = reader["i"]  # either 2 ** 31 - 1 or -1
        reader.unpack_value("i", asserted=100)
        terminator_null_count = reader["i"] - 12
        terminator_nulls = reader.read(terminator_null_count)
        if terminator_nulls.strip(b"\0"):
            raise ValueError(f"Found non-null reader in `GXList` terminator: {terminator_nulls}")
        return cls(gx_items, terminator_id, terminator_null_count)

    def to_flver_writer(self, writer: BinaryWriter):
        for gx_item in self.gx_items:
            GXItem.object_to_writer(gx_item, writer, size=len(gx_item.data) + 12)
            writer.append(gx_item.data)
        writer.pack("iii", self.terminator_id, 100, self.terminator_null_count + 12)
        writer.pad(self.terminator_null_count)

    def __repr__(self):
        return f"GXList{repr(self.gx_items)}"


@dataclass(slots=True)
class TextureStruct(BinaryStruct):

    _path_offset: int
    _texture_type_offset: int
    scale: Vector2
    unk_x10: byte = field(**Binary(asserted=[0, 1, 2]))
    unk_x11: bool
    _pad1: bytes = field(init=False, **BinaryPad(2))
    unk_x14: float
    unk_x18: float
    unk_x1C: float


@dataclass(slots=True)
class Texture:

    path: str = ""
    texture_type: str = ""
    scale: Vector2 = field(default_factory=Vector2.one)
    unk_x10: int = 1
    unk_x11: bool = True  # TODO: possibly 'has_texture'? seems to correlate with non-empty path
    unk_x14: float = 0.0
    unk_x18: float = 0.0
    unk_x1C: float = 0.0

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, encoding: str):
        texture_struct = TextureStruct.from_bytes(reader)
        path = reader.unpack_string(offset=texture_struct.pop("_path_offset"), encoding=encoding)
        texture_type = reader.unpack_string(offset=texture_struct.pop("_texture_type_offset"), encoding=encoding)
        texture = texture_struct.to_object(cls, path=path, texture_type=texture_type)
        return texture

    def to_flver_writer(self, writer: BinaryWriter):
        TextureStruct.object_to_writer(self, writer, _path_offset=None, _texture_type_offset=None)

    def pack_strings(self, writer: BinaryWriter, encoding: str):
        writer.fill_with_position("_path_offset", obj=self)
        writer.pack_z_string(self.path, encoding=encoding)
        writer.fill_with_position("_texture_type_offset", obj=self)
        writer.pack_z_string(self.texture_type, encoding=encoding)

    def set_name(self, name: str):
        """Set `path` to '{name}.tga'.

        Any existing '.tga' or '.tpf' extension in `name` will be removed and replaced with '.tga'.
        """
        name = name.removesuffix(".tga").removesuffix(".tpf") + ".tga"
        self.path = str(Path(self.path).with_name(name))

    @property
    def path_parent(self) -> str:
        """Directory part of FLVER texture path, as a string. Includes (exactly one) trailing backslash."""
        return str(Path(self.path).parent).rstrip("\\") + "\\"

    @property
    def stem(self) -> str:
        """Typically just removes '.tga' extension from FLVER texture path."""
        return Path(self.path).stem

    def __hash__(self) -> int:
        """Used mostly by `Material` hash."""
        return hash((
            self.path, self.texture_type, self.scale.x, self.scale.y, self.unk_x10, self.unk_x11, self.unk_x14,
            self.unk_x18, self.unk_x1C
        ))


@dataclass(slots=True)
class MaterialStruct(BinaryStruct):

    _name_offset: int
    _mtd_path_offset: int
    _texture_count: int
    _first_texture_index: int
    flags: int
    _gx_offset: int
    unk_x18: int
    _pad1: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class Material:

    Texture: tp.ClassVar[tp.Type[Texture]] = Texture

    name: str = ""
    mtd_path: str = ""
    flags: int = 0
    unk_x18: int = 0
    gx_index: int = -1
    textures: list[Texture] = field(default_factory=list)

    # Held temporarily before FLVER textures are assigned.
    _texture_count: int | None = None
    _first_texture_index: int | None = None

    @classmethod
    def from_flver_reader(
        cls,
        reader: BinaryReader,
        encoding: str,
        version: Version,
        gx_lists: list[GXList],
        gx_list_indices: dict[int, int],
    ):
        material_struct = MaterialStruct.from_bytes(reader)
        name = reader.unpack_string(offset=material_struct.pop("_name_offset"), encoding=encoding)
        mtd_path = reader.unpack_string(offset=material_struct.pop("_mtd_path_offset"), encoding=encoding)
        gx_offset = material_struct.pop("_gx_offset")
        if gx_offset == 0:
            gx_index = -1
        elif gx_offset in gx_list_indices:
            # Reuses a `GXList` first used by a prior `Material`.
            gx_index = gx_list_indices[gx_offset]
        else:
            gx_index = gx_list_indices[gx_offset] = len(gx_lists)
            with reader.temp_offset(gx_offset):
                gx_lists.append(GXList.from_flver_reader(reader, version))
        material = material_struct.to_object(
            cls,
            name=name,
            mtd_path=mtd_path,
            gx_index=gx_index,
            _texture_count=material_struct.pop("_texture_count"),
            _first_texture_index=material_struct.pop("_first_texture_index"),
        )
        return material

    def assign_textures(self, textures: dict[int, Texture]):
        """Pop and assign textures from dictionary by index."""
        if self._texture_count == -1 or self._first_texture_index == -1:
            raise ValueError(f"Tried to call `assign_textures()` on `Material` {self.name} more than once.")
        for i in range(self._first_texture_index, self._first_texture_index + self._texture_count):
            if i not in textures:
                raise KeyError(
                    f"Tried to assign `Texture` with index {i} to `Material` {self.name}, but the `Texture` has "
                    "already been assigned to another `Material` (or does not exist)."
                )
            self.textures.append(textures.pop(i))
        self._texture_count = None
        self._first_texture_index = None

    def to_flver_writer(self, writer: BinaryWriter):
        MaterialStruct.object_to_writer(self, writer, _texture_count=len(self.textures))

    def pack_textures(self, flver_writer: BinaryWriter, first_texture_index: int):
        """Pack material's textures at this position."""
        flver_writer.fill("_first_texture_index", first_texture_index, obj=self)
        for texture in self.textures:
            texture.to_flver_writer(flver_writer)

    def fill_gx_offset(self, flver_writer: BinaryWriter, gx_offsets: list[int]):
        gx_offset = 0 if self.gx_index == -1 else gx_offsets[self.gx_index]
        flver_writer.fill("_gx_offset", gx_offset, obj=self)

    def pack_strings(self, flver_writer: BinaryWriter, encoding: str):
        flver_writer.fill_with_position("_name_offset", obj=self)
        flver_writer.pack_z_string(self.name, encoding=encoding)
        flver_writer.fill_with_position("_mtd_path_offset", obj=self)
        flver_writer.pack_z_string(self.mtd_path, encoding=encoding)

    def get_texture_dict(self) -> dict[str, Texture]:
        """Get a dictionary mapping texture types to `Texture` instances.

        Will raise a `KeyError` if any texture type is repeated.
        """
        textures = {}
        for texture in self.textures:
            if texture.texture_type in textures:
                raise KeyError(f"Texture type {texture.texture_type} appeared more than once in Material {self.name}.")
            textures[texture.texture_type] = texture
        return textures

    def find_texture_type(self, texture_type: str) -> Texture | None:
        for texture in self.textures:
            if texture.texture_type == texture_type:
                return texture
        return None

    def get_shared_texture_path_prefix(self, exclude_names=True, exclude_empty_paths=True) -> str:
        shared_texture_prefix = ""
        for texture in self.textures:
            if exclude_empty_paths and not texture.path:
                continue  # empty paths do not count
            path_part = texture.path_parent if exclude_names else texture.path
            if shared_texture_prefix == "":
                shared_texture_prefix = path_part
                continue
            for i, (a, b) in enumerate(zip(shared_texture_prefix, path_part)):
                if a != b:
                    shared_texture_prefix = shared_texture_prefix[:i]
                    break
        return shared_texture_prefix

    @property
    def mtd_name(self):
        return Path(self.mtd_path).name

    @mtd_name.setter
    def mtd_name(self, name: str):
        """Set '.mtd' name of `mtd_path`."""
        name = name.removesuffix(".mtd") + ".mtd"
        self.mtd_path = str(Path(self.mtd_path).with_name(name))

    def get_mtd_info(self) -> MTDInfo:
        return MTDInfo(self.mtd_name)

    def replace_in_all_texture_names(self, old_string: str, new_string: str):
        """Replace all occurrences of `old_string` in all texture names (at end of paths) with `new_string`."""
        for tex in self.textures:
            if tex.path:
                tex_path = Path(tex.path)
                tex_name = tex_path.name.replace(old_string, new_string)
                tex.path = str(tex_path.with_name(tex_name))

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

    def __hash__(self) -> int:
        """Game FLVERs reuse identical `Material` instances across multiple meshes.

        You can hash each material to check if any two materials are identical.
        """
        texture_hashes = tuple(hash(tex) for tex in self.textures)
        return hash((self.name, self.mtd_path, self.flags, self.gx_index, self.unk_x18, texture_hashes))
