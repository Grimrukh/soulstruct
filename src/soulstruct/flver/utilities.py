"""Utilities designed to work with both pure Python and C++ FLVER."""

from __future__ import annotations

__all__ = [
    "get_all_texture_paths",
    "hash_texture",
    "hash_gx_item",
    "hash_material",
]

import typing as tp
from pathlib import Path

if tp.TYPE_CHECKING:
    from . import *


def get_all_texture_paths(flver: FLVER) -> set[Path]:
    """Get set of all texture paths from all materials, which typically end in '.tga' or '.tif'.

    Ignores textures with empty `path`.
    """
    return {
        Path(texture.path)
        for mesh in flver.meshes
        for texture in mesh.material.textures
    }


def hash_texture(texture: Texture) -> int:
    return hash((
        texture.path, texture.texture_type, texture.scale[0], texture.scale[1], texture.f2_unk_x10, texture.f2_unk_x11,
        texture.f2_unk_x14, texture.f2_unk_x18, texture.f2_unk_x1c
    ))


def hash_gx_item(gx_item: GXItem) -> int:
    return hash((gx_item.category, gx_item.index, gx_item.data))


def hash_material(material: Material) -> int:
    """Straightforward hashing of fields, Textures, and GXItems.

    Note that `name` is included in the hash, despite only being functional in some (known!) cases, so users can
    use material names as a way to keep them separate.
    """
    texture_hashes = tuple(hash_texture(tex) for tex in material.textures)
    gx_item_hashes = tuple(hash_gx_item(item) for item in material.gx_items)
    return hash((
        material.name, material.mat_def_path, material.flags, gx_item_hashes, material.f2_unk_x18, texture_hashes
    ))
