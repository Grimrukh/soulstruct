from __future__ import annotations

__all__ = ["Material"]

import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.text import indent_lines
from soulstruct.utilities.binary import *
from soulstruct.base.models.base.material import BaseMaterial
from soulstruct.base.models.base.version import FLVERVersion
from .gx_item import GXItem
from .texture import Texture

if tp.TYPE_CHECKING:
    from .core import FLVER
    from .submesh import Submesh

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Material(BaseMaterial[Texture]):
    """Information about a FLVER material used by any number of submeshes.

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
        _texture_count: int
        _first_texture_index: int
        flags: int
        _gx_offset: int
        unk_x18: int
        _pad1: bytes = field(init=False, **BinaryPad(4))

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

        material_struct = cls.STRUCT.from_bytes(reader)
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
        self.STRUCT.object_to_writer(
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
