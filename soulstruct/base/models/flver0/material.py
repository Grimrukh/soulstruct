from __future__ import annotations

__all__ = ["Material", "Texture"]

import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *
from soulstruct.utilities.text import indent_lines
from soulstruct.base.models.base.material import BaseMaterial
from .vertex_array_layout import VertexArrayLayout
from .texture import Texture

if tp.TYPE_CHECKING:
    from soulstruct.base.models.base.version import FLVERVersion
    from .core import FLVER0
    from .submesh import Submesh


@dataclass(slots=True)
class Material(BaseMaterial[Texture]):
    """Information about a FLVER material used by any number of submeshes.

    Unlike modern `FLVER`, `Texture` instances are stored on the `Material` and not passed in to it from the root FLVER.

    TODO: Confirm that same mask name rule applies to old FLVER.
    NOTE: The `name` of the material is usually junk, but if it is formatted as a number between two hashes, e.g.
    '#01#', then any submesh using the materia will ONLY be rendered if the corresponding 'Model Display Mask' bit flag
    in `NPC_PARAM` is enabled. We carefully preserve these names and have properties that wrap name getting/setting
    based on a desired mask value. Multiple `Material` instances may use the same display mask value, but typically only
    one of them will.
    """

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        _name_offset: int
        _mat_def_path_offset: int
        _textures_offset: int
        _layouts_offset: int
        _size: int  # from name offset to end of layouts
        _layout_header_offset: int
        _pad0: bytes = field(init=False, **BinaryPad(8))

    # Exactly one or two digits required between hashes (two usually used), with optional trimmable spaces. Any suffix.
    DISPLAY_MASK_RE: tp.ClassVar[re.Pattern] = re.compile(r"^# *(\d|\d\d) *# *(.*)$")

    name: str = ""
    mat_def_path: str = ""  # '.mtd' (MTD) file name (MATBIN too new)
    textures: list[Texture] = field(default_factory=list)

    # Stored by `FLVER0` just after reading (before reassining to array users).
    _layouts: list[VertexArrayLayout] | None = None

    @classmethod
    def from_flver_reader(
        cls,
        reader: BinaryReader,
        encoding: str,
        version: FLVERVersion,
    ):
        """Unpack a `Material`. `version` is unused here."""
        material_struct = cls.STRUCT.from_bytes(reader)

        name_offset = material_struct.pop("_name_offset")
        mat_def_path_offset = material_struct.pop("_mat_def_path_offset")
        textures_offset = material_struct.pop("_textures_offset")

        name = reader.unpack_string(offset=name_offset, encoding=encoding)
        mat_def_path = reader.unpack_string(offset=mat_def_path_offset, encoding=encoding)

        with reader.temp_offset(textures_offset):
            texture_count = reader["B"]
            reader.assert_pad(3)  # align
            reader.assert_pad(12)
            textures = [Texture.from_flver_reader(reader, encoding) for _ in range(texture_count)]

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
                        layout = VertexArrayLayout.from_flver_reader(reader)
                    layouts.append(layout)
        else:
            # Read single layout.
            with reader.temp_offset(layouts_offset):
                layouts = [VertexArrayLayout.from_flver_reader(reader)]

        material = material_struct.to_object(
            cls,
            name=name,
            mat_def_path=mat_def_path,
            textures=textures,
            _layouts=layouts,
        )
        return material

    def to_flver_writer(self, writer: BinaryWriter):
        self.STRUCT.object_to_writer(self, writer)  # everything reserved!

    def pack_data(self, flver_writer: BinaryWriter, layouts: list[VertexArrayLayout], encoding: str):
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
            texture.to_flver_writer(flver_writer)
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
            layout.to_flver_writer(flver_writer)  # data written here as well

        size = flver_writer.position - start
        flver_writer.fill("_size", size, obj=self)

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

    def get_submesh_users(self, flver: FLVER0) -> list[Submesh]:
        """Get all submeshes that use this material (by equality, not exact instance)."""
        return [submesh for submesh in flver.submeshes if submesh.material == self]

    def __repr__(self):
        textures = ",\n".join(["    " + indent_lines(repr(texture)) for texture in self.textures])
        if textures:
            textures = "\n" + textures + ",\n  "
        lines = [
            f"Material(",
            f"  name = {repr(self.name)},",
            f"  mat_def_path = {repr(self.mat_def_path)},",
            f"  textures = [{textures}],",
            f")",
        ]
        return "\n".join(lines)

    def __hash__(self) -> int:
        """Straightforward hashing of fields and textures.

        Note that `name` is included in the hash, despite only being functional in some (known!) cases, so users can
        use material names as a way to keep them separate.
        """
        texture_hashes = tuple(hash(tex) for tex in self.textures)
        return hash((self.name, self.mat_def_path, texture_hashes))

    def __eq__(self, other: Material):
        """Check for equality by hash."""
        if not isinstance(other, Material):
            return False
        return hash(self) == hash(other)
