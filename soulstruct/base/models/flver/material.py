from __future__ import annotations

__all__ = ["GXItem", "read_gx_item_list", "Material", "Texture"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector2

from .version import Version

if tp.TYPE_CHECKING:
    from .core import FLVER
    from .submesh import Submesh

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class GXItem:
    """Item that sets various material rendering properties.

    Doesn't use `BinaryStruct` due to the way its header `size` and `data` interact.
    """
    # List of GXItems should end with a 'dummy' item that has one of these categories.
    DUMMY_CATEGORIES: tp.ClassVar[set[bytes]] = {b'\xff\xff\xff\x7f', b'\xff\xff\xff\xff'}
    HEADER_SIZE: tp.ClassVar[int] = 12  # category, index, size (all four bytes each)

    category: bytes  # typically ASCII, but not decoded as it may be one of the 'dummy' values above
    index: int  # index of `GXItem` 'subtype' (e.g. 100), NOT just its index in a FLVER list
    # `size` appears here in header (`len(data) + 12`).
    data: bytes  # packed 'argument' data; usage varies by category/index and is not managed here

    @classmethod
    def from_bytes(cls, reader: bytes | BinaryReader):
        if isinstance(reader, bytes):
            reader = BinaryReader(reader)
        category = reader.unpack_value("4s")
        index = reader.unpack_value("i")
        size = reader.unpack_value("i")  # total size of struct (12) and raw `data`
        data = reader.read(size - cls.HEADER_SIZE)
        return cls(category, index, data)

    def to_writer(self, writer: BinaryWriter):
        if len(self.category) != 4:
            raise ValueError(f"`GXItem.category` must be 4 bytes long, not {len(self.category)} bytes: {self.category}")
        writer.append(self.category)
        writer.pack("i", self.index)
        writer.pack("i", len(self.data) + self.HEADER_SIZE)
        writer.append(self.data)

    def __hash__(self):
        """For identifying unique lists of `GXItem`s."""
        return hash((self.category, self.index, self.data))

    @property
    def is_dummy(self):
        return self.category in self.DUMMY_CATEGORIES

    @classmethod
    def new_dummy(cls):
        """
        TODO: This is valid for Bloodborne, DS3, Sekiro, and Elden Ring.
         I think dummy items may have appeared somewhere (DS2? Other FLVERs?) with:
            category = b"\xff\xff\xff\xff"
            data     = b"\x00\x00\x00\x00"
         But I can't find those FLVERs. And this dummy may work in those FLVERs anyway.
        """
        return cls(b"\xff\xff\xff\x7f", 100, b"")


def read_gx_item_list(flver_reader: BinaryReader, flver_version: Version) -> list[GXItem]:
    """Read a list of `GXItem` instances from FLVER, including the final dummy `GXItem` (which no `Material` should
    ever use).

    The `FLVER` instance will maintain the final dummy item for byte-perfect rewrites.
    """
    if flver_version <= Version.DarkSouls2:
        # Only one `GXItem` with no dummy item. TODO: Definitely no dummy item?
        gx_item = GXItem.from_bytes(flver_reader)
        return [gx_item]

    # Keep unpacking `GXItem`s until we unpack one with a dummy category.
    # The dummy item is still appended to the list, as its exact category and data may vary.
    gx_items = []
    while True:
        gx_item = GXItem.from_bytes(flver_reader)
        gx_items.append(gx_item)
        if gx_item.is_dummy:
            # Warn user if contents of dummy `GXItem` are not as expected.
            if gx_item.index != 100:
                _LOGGER.warning(f"Dummy `GXItem` at end of list should have `index == 100`, not: {gx_item.index}")
            if gx_item.data.strip(b"\0"):
                _LOGGER.warning(f"Dummy `GXItem` at end of list has non-null `data`: {gx_item.data}")
            break  # final dummy item found
    return gx_items  # including dummy item


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
    texture_type: str = ""  # MTD or MATBIN sampler name (e.g. 'g_Diffuse', 'C_DetailBlend__snp_Texture2D_7_AlbedoMap')
    scale: Vector2 = field(default_factory=Vector2.one)
    unk_x10: int = 1  # always 0 when `path` is empty, and *very rarely* 2 (for three total materials in DS1)
    unk_x11: bool = True  # seems exactly `bool(path)` in DS1
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
    def name(self) -> str:
        return Path(self.path).name if self.path else ""

    @property
    def stem(self) -> str:
        """Typically just removes '.tga' extension from FLVER texture path."""
        return Path(self.path).stem if self.path else ""

    def __hash__(self) -> int:
        """Used mostly by `Material` hash."""
        return hash((
            self.path, self.texture_type, self.scale.x, self.scale.y, self.unk_x10, self.unk_x11, self.unk_x14,
            self.unk_x18, self.unk_x1C
        ))

    def __repr__(self):
        s = f"Texture(\"{self.path}\", \"{self.texture_type}\""
        if self.scale[0] != 1.0 or self.scale[1] != 1.0:
            s += f", scale={self.scale}"
        if self.unk_x10 != 1:
            s += f", unk_x10={self.unk_x10}"
        if not self.unk_x11:
            s += f", unk_x11={self.unk_x11}"
        if self.unk_x14 != 0.0:
            s += f", unk_x14={self.unk_x14}"
        if self.unk_x18 != 0.0:
            s += f", unk_x18={self.unk_x18}"
        if self.unk_x1C != 0.0:
            s += f", unk_x1C={self.unk_x1C}"
        s += ")"
        return s


@dataclass(slots=True)
class MaterialStruct(BinaryStruct):

    _name_offset: int
    _mat_def_path_offset: int
    _texture_count: int
    _first_texture_index: int
    flags: int
    _gx_offset: int
    unk_x18: int
    _pad1: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class Material:
    """Information about a FLVER material used by any number of submeshes.

    NOTE: The `name` of the material is usually junk, but if it is formatted as a number between two hashes, e.g.
    '#01#', then any submesh using the materia will ONLY be rendered if the corresponding 'Model Display Mask' bit flag
    in `NPC_PARAM` is enabled. We carefully preserve these names and have properties that wrap name getting/setting
    based on a desired mask value. Multiple `Material` instances may use the same display mask value, but typically only
    one of them will.
    """

    # Exactly one or two digits required between hashes (two usually used), with optional trimmable spaces. Any suffix.
    DISPLAY_MASK_RE: tp.ClassVar[re.Pattern] = re.compile(r"^# *(\d|\d\d) *# *(.*)$")

    name: str = ""
    mat_def_path: str = ""  # could be a '.mtd' (MTD) file name or '.matxml' (MATBIN) file name
    flags: int = 0
    unk_x18: int = 0
    gx_items: list[GXItem] = field(default_factory=list)
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
        gx_item_lists: dict[int, list[GXItem]],
    ):
        """Unpack a `Material`.

        Each packed material may contain an offset to a list of `GXItem`s, but these lists (NOT the individual items)
        can also be shared between materials. The `gx_item_lists` dictionary maps these offsets to `GXItem` lists that
        have already been unpacked due to usage by a previous `Material`. If the offset is new, the list is unpacked and
        added to this dictionary in-place for future materials.

        NOTE: The Python lists that represent the `GXItem` lists are shallow-copied when reused, so that modifying the
        list for one material does NOT affect any others (by default). Upon export, any lists that turn out to be
        identical will be written to the same shared offset in the FLVER file.
        """
        material_struct = MaterialStruct.from_bytes(reader)
        name = reader.unpack_string(offset=material_struct.pop("_name_offset"), encoding=encoding)
        mat_def_path = reader.unpack_string(offset=material_struct.pop("_mat_def_path_offset"), encoding=encoding)
        gx_offset = material_struct.pop("_gx_offset")
        if gx_offset <= 0:
            gx_item_list = []  # no `GXItem`s (older games)
        elif gx_offset in gx_item_lists:
            # Reuses a `GXItem` list first used by a prior `Material`.
            gx_item_list = gx_item_lists[gx_offset].copy()  # shallow copy
        else:
            # Unpack first-time use of `GXItem` list.
            # Final 'dummy' `GXItem` is NOT removed here. Management of it is up to the user. If absent on FLVER export,
            # a default dummy item will be created and written.
            with reader.temp_offset(gx_offset):
                gx_item_list = read_gx_item_list(reader, version)
                gx_item_lists[gx_offset] = gx_item_list

        material = material_struct.to_object(
            cls,
            name=name,
            mat_def_path=mat_def_path,
            gx_items=gx_item_list,
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
        MaterialStruct.object_to_writer(
            self,
            writer,
            _texture_count=len(self.textures),
            _gx_offset=RESERVED if self.gx_items else 0,
        )

    def pack_textures(self, flver_writer: BinaryWriter, first_texture_index: int):
        """Pack material's textures at this position."""
        flver_writer.fill("_first_texture_index", first_texture_index, obj=self)
        for texture in self.textures:
            texture.to_flver_writer(flver_writer)

    def fill_gx_offset(self, flver_writer: BinaryWriter, gx_offset: int):
        """NOTE: Material only reserves this field if it has any GX items. Otherwise, it already wrote offset 0."""
        flver_writer.fill("_gx_offset", gx_offset, obj=self)

    def pack_strings(self, flver_writer: BinaryWriter, encoding: str):
        flver_writer.fill_with_position("_name_offset", obj=self)
        flver_writer.pack_z_string(self.name, encoding=encoding)
        flver_writer.fill_with_position("_mat_def_path_offset", obj=self)
        flver_writer.pack_z_string(self.mat_def_path, encoding=encoding)

    def get_texture_dict(self) -> dict[str, Texture]:
        """Get a dictionary mapping texture types to like 'g_Diffuse' to `Texture` instances.

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
    def mat_def_stem(self) -> str:
        return Path(self.mat_def_path).stem

    @property
    def mat_def_name(self) -> str:
        """Extension can vary: '.mtd' or '.matxml'."""
        return Path(self.mat_def_path).name

    @mat_def_name.setter
    def mat_def_name(self, name: str):
        """Replaces name component of current `mat_def_path`. If extension is missing, current suffix will be used."""
        if name.endswith(".mtd") or name.endswith(".matxml"):
            # Use name as-is.
            pass
        elif "." in name:
            raise ValueError(f"Material definition name {name} should have no suffix, or '.mtd' or '.matxml'.")
        else:
            # Keep current suffix.
            new_suffix = Path(self.mat_def_path).suffix
            name += new_suffix
        self.mat_def_path = str(Path(self.mat_def_path).with_name(name))

    @property
    def display_mask(self) -> int | None:
        """Parse `name` of material to check if it is a display mask material, and return the mask value if so.

        Returns `None` if the material is not a display mask material, which means it will always be rendered.
        """
        if match := self.DISPLAY_MASK_RE.match(self.name):
            return int(match.group(1))
        return None

    @display_mask.setter
    def display_mask(self, value: int):
        """Sets `name` to the appropriate formatted, hash-enclosed string: `#{value:02d}#`.

        Since suffixes in mask names are supported, any existing suffix will be copied. If the name is not currently a
        mask name, the existing name will be moved to a suffix.
        """
        if value is None:
            raise ValueError("Model display mask value cannot be `None`. Just change the name to a non-mask name.")
        if not 0 <= value < 32:
            # TODO: Earlier games only allow 16 masks, not 32.
            raise ValueError(f"Model display mask value must be between 0 and 31, not {value}.")
        if match := self.DISPLAY_MASK_RE.match(self.name):
            self.name = f"#{value:02d}# {match.group(2)}"  # keep existing mask name suffix
        else:
            self.name = f"#{value:02d}# {self.name}"  # no existing mask name suffix

    @property
    def name_without_display_mask(self) -> str:
        """Return material name after display mask prefix, if present.

        May be empty if there's nothing after the mask.
        """
        if match := self.DISPLAY_MASK_RE.match(self.name):
            return match.group(2)
        return self.name

    def replace_in_all_texture_names(self, old_string: str, new_string: str):
        """Replace all occurrences of `old_string` in all texture names (at end of paths) with `new_string`."""
        for tex in self.textures:
            if tex.path:
                tex_path = Path(tex.path)
                tex_name = tex_path.name.replace(old_string, new_string)
                tex.path = str(tex_path.with_name(tex_name))

    def get_submesh_users(self, flver: FLVER) -> list[Submesh]:
        """Get all submeshes that use this material (by equality, not exact instance)."""
        return [submesh for submesh in flver.submeshes if submesh.material == self]

    def get_non_dummy_gx_items(self) -> list[GXItem]:
        """Return only the non-dummy (non-final) `GXItem`s in list.

        Raises a `ValueError` if a dummy item appears anywhere except as the last element, but doesn't care if no dummy
        item exists at all (as one can be created automatically on FLVER export).
        """
        non_dummy_gx_items = []
        for i, gx_item in enumerate(self.gx_items):
            if gx_item.is_dummy:
                if i != len(self.gx_items) - 1:
                    raise ValueError("Dummy `GXItem` found in non-final position in `Material`.")
                break  # do not append this final dummy item
            non_dummy_gx_items.append(gx_item)
        return non_dummy_gx_items

    def __repr__(self):
        textures = ",\n".join(["    " + indent_lines(repr(texture)) for texture in self.textures])
        if textures:
            textures = "\n" + textures + ",\n  "
        lines = [
            f"Material(",
            f"  name = {repr(self.name)},",
            f"  mat_def_path = {repr(self.mat_def_path)},",
            f"  flags = 0b{self.flags:032b},  # {self.flags}",
        ]
        if self.gx_items:
            items = ",\n".join(["    " + indent_lines(repr(item)) for item in self.gx_items if item.category])
            lines.append(f"  gx_items = [\n{items}\n  ],")
        if self.unk_x18 != 0:
            lines.append(f"  unk_x18 = {self.unk_x18},")
        lines.append(f"  textures = [{textures}],")
        lines.append(")")
        return "\n".join(lines)

    def __hash__(self) -> int:
        """Straightforward hashing of fields and textures.

        Note that `name` is included in the hash, despite only being functional in some (known!) cases, so users can
        use material names as a way to keep them separate.
        """
        texture_hashes = tuple(hash(tex) for tex in self.textures)
        gx_item_hashes = tuple(hash(item) for item in self.gx_items)
        return hash((self.name, self.mat_def_path, self.flags, gx_item_hashes, self.unk_x18, texture_hashes))

    def __eq__(self, other: Material):
        """Check for equality by hash."""
        if not isinstance(other, Material):
            return False
        return hash(self) == hash(other)
