from __future__ import annotations

__all__ = ["Material"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *
from soulstruct.utilities.text import indent_lines
from .gx_item import GXItem
from .texture import Texture
from .version import FLVERVersion
from .vertex_array_layout import VertexArrayLayout

if tp.TYPE_CHECKING:
    from .core import FLVER
    from .mesh import FLVERMesh

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Material:
    """Information about a FLVER material used by any number of meshes.

    NOTE: The `name` of the material is usually junk, but if it is formatted as a number between two hashes, e.g.
    '#01#', then any mesh using the materia will ONLY be rendered if the corresponding 'Model Display Mask' bit flag
    in `NPC_PARAM` is enabled. We carefully preserve these names and have properties that wrap name getting/setting
    based on a desired mask value. Multiple `Material` instances may use the same display mask value, but typically only
    one of them will.
    """

    # Exactly one or two digits required between hashes (two usually used), with optional trimmable spaces. Any suffix.
    DISPLAY_MASK_RE: tp.ClassVar[re.Pattern] = re.compile(r"^# *(\d|\d\d) *# *(.*)$")

    class STRUCT0(BinaryStruct):
        _name_offset: int
        _mat_def_path_offset: int
        _textures_offset: int
        _layouts_offset: int
        _size: int  # from name offset to end of layouts
        _layout_header_offset: int
        _pad0: bytes = binary_pad(8, init=False)

    class STRUCT2(BinaryStruct):
        _name_offset: int
        _mat_def_path_offset: int
        _texture_count: int
        _first_texture_index: int
        flags: int
        _gx_offset: int
        f2_unk_x18: int
        _pad1: bytes = binary_pad(4, init=False)

    name: str = ""
    mat_def_path: str = ""  # could be a '.mtd' (MTD) file name or '.matxml' (MATBIN) file name
    textures: list[Texture] = field(default_factory=list)

    # Written to FLVER2 versions only:
    flags: int = 0
    f2_unk_x18: int = 0
    gx_items: list[GXItem] = field(default_factory=list)

    # Held temporarily before FLVER textures are assigned.
    _texture_count: int | None = None
    _first_texture_index: int | None = None

    # Stored by `FLVER0` just after reading (before reassigning to array users).
    _layouts: list[VertexArrayLayout] | None = None

    @classmethod
    def from_flver0_reader(
        cls,
        reader: BinaryReader,
        encoding: str,
    ):
        """Unpack a `Material`. `version` is unused here."""
        material_struct = cls.STRUCT0.from_bytes(reader)

        name_offset = material_struct.pop("_name_offset")
        mat_def_path_offset = material_struct.pop("_mat_def_path_offset")
        textures_offset = material_struct.pop("_textures_offset")

        name = reader.unpack_string(offset=name_offset, encoding=encoding)
        mat_def_path = reader.unpack_string(offset=mat_def_path_offset, encoding=encoding)

        with reader.temp_offset(textures_offset):
            texture_count = reader["B"]
            reader.assert_pad(3)  # align
            reader.assert_pad(12)
            textures = [Texture.from_flver0_reader(reader, encoding) for _ in range(texture_count)]

        layouts_offset = material_struct.pop("_layouts_offset")
        layouts_header_offset = material_struct.pop("_layout_header_offset")
        if layouts_header_offset != 0:
            with reader.temp_offset(layouts_header_offset):
                layout_count = reader["i"]
                reader.unpack_value("i", asserted=reader.position + 0xC)  # layout data offset
                reader.assert_pad(8)
                if layouts_offset != reader.position + 4:
                    raise ValueError(
                        f"Material layouts offset {layouts_offset} != post-header offset {reader.position + 4}."
                    )
                layouts = []
                for _ in range(layout_count):
                    layout_offset = reader["i"]
                    with reader.temp_offset(layout_offset):
                        layout = VertexArrayLayout.from_flver0_reader(reader)
                    layouts.append(layout)
        else:
            # Read single layout.
            with reader.temp_offset(layouts_offset):
                layouts = [VertexArrayLayout.from_flver0_reader(reader)]

        material = material_struct.to_object(
            cls,
            name=name,
            mat_def_path=mat_def_path,
            textures=textures,
            _layouts=layouts,
        )
        return material

    @classmethod
    def from_flver2_reader(
        cls,
        reader: BinaryReader,
        encoding: str,
        version: FLVERVersion,
        gx_item_lists: dict[int, list[GXItem]] = None,
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
        if gx_item_lists is None:
            raise ValueError("`gx_item_lists` must be provided to `Material.from_flver_reader()`.")

        material_struct = cls.STRUCT2.from_bytes(reader)
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
            # Final terminator `GXItem` is NOT removed here. Management of it is up to the user. If absent on FLVER
            # export, a default terminator item will be created and written.
            with reader.temp_offset(gx_offset):
                gx_item_list = GXItem.read_list(reader, version)
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

    def assign_flver2_textures(self, textures: dict[int, Texture]):
        """FLVER2 verions store textures in root FLVER. This pops and assign textures to Material by index key."""
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

    def to_flver0_writer(self, writer: BinaryWriter):
        self.STRUCT0.object_to_writer(self, writer)  # everything reserved!

    def pack_flver0_data(self, flver_writer: BinaryWriter, layouts: list[VertexArrayLayout], encoding: str):
        start = flver_writer.position
        flver_writer.fill_with_position("_name_offset", obj=self)
        flver_writer.pack_z_string(self.name, encoding=encoding)
        flver_writer.fill_with_position("_mat_def_path_offset", obj=self)
        flver_writer.pack_z_string(self.mat_def_path, encoding=encoding)

        flver_writer.fill_with_position("_textures_offset", obj=self)
        flver_writer.pack("B", len(self.textures))
        flver_writer.pad(3)  # align
        flver_writer.pad(12)

        for texture in self.textures:
            texture.to_flver0_writer(flver_writer)
        for texture in self.textures:
            texture.pack_strings(flver_writer, encoding=encoding)

        # We always write the layout header, even if it was absent on import.
        flver_writer.fill_with_position("_layout_header_offset", obj=self)
        flver_writer.pack("i", len(layouts))
        flver_writer.pack("i", flver_writer.position + 0xC)
        flver_writer.pad(8)
        for layout in layouts:
            flver_writer.reserve("layout_offset", "i", obj=layout)

        flver_writer.fill_with_position("_layouts_offset", obj=self)
        for layout in layouts:
            flver_writer.fill_with_position("layout_offset", obj=layout)
            layout.to_flver0_writer(flver_writer)  # data written here as well

        size = flver_writer.position - start
        flver_writer.fill("_size", size, obj=self)

    def to_flver2_writer(self, writer: BinaryWriter):
        self.STRUCT2.object_to_writer(
            self,
            writer,
            _texture_count=len(self.textures),
            _gx_offset=RESERVED if self.gx_items else 0,
        )

    def pack_flver2_strings(self, flver_writer: BinaryWriter, encoding: str):
        """FLVER2 material data only contains these strings. Textures and layouts are stored in root FLVER."""
        flver_writer.fill_with_position("_name_offset", obj=self)
        flver_writer.pack_z_string(self.name, encoding=encoding)
        flver_writer.fill_with_position("_mat_def_path_offset", obj=self)
        flver_writer.pack_z_string(self.mat_def_path, encoding=encoding)

    def pack_flver2_textures(self, flver_writer: BinaryWriter, first_texture_index: int):
        """Pack material's textures at this position."""
        flver_writer.fill("_first_texture_index", first_texture_index, obj=self)
        for texture in self.textures:
            texture.to_flver2_writer(flver_writer)

    def fill_flver2_gx_offset(self, flver_writer: BinaryWriter, gx_offset: int):
        """NOTE: Material only reserves this field if it has any GX items. Otherwise, it already wrote offset 0."""
        flver_writer.fill("_gx_offset", gx_offset, obj=self)

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

    def get_mesh_users(self, flver: FLVER) -> list[FLVERMesh]:
        """Get all meshes that use this material (by equality, not exact instance)."""
        return [mesh for mesh in flver.meshes if mesh.material == self]

    def get_non_terminator_gx_items(self) -> list[GXItem]:
        """Return only the non-terminator `GXItem`s in list.

        Raises a `ValueError` if a terminator item appears anywhere except as the last element, but doesn't care if no
        terminator item exists at all (as one can be created automatically on FLVER export).
        """
        non_term_gx_items = []
        for i, gx_item in enumerate(self.gx_items):
            if gx_item.is_terminator:
                if i != len(self.gx_items) - 1:
                    raise ValueError("Terminator `GXItem` found in non-final position in `Material`.")
                break  # do not append this final terminator item
            non_term_gx_items.append(gx_item)
        return non_term_gx_items

    def __hash__(self) -> int:
        """Straightforward hashing of fields, Textures, and GXItems.

        Note that `name` is included in the hash, despite only being functional in some (known!) cases, so users can
        use material names as a way to keep them separate.
        """
        texture_hashes = tuple(hash(tex) for tex in self.textures)
        gx_item_hashes = tuple(hash(item) for item in self.gx_items)
        return hash((self.name, self.mat_def_path, self.flags, gx_item_hashes, self.f2_unk_x18, texture_hashes))

    def __eq__(self, other: tp.Self):
        """Check for equality by hash."""
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

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
        if self.f2_unk_x18 != 0:
            lines.append(f"  f2_unk_x18 = {self.f2_unk_x18},")
        lines.append(f"  textures = [{textures}],")
        lines.append(")")
        return "\n".join(lines)
