"""Console DDS swizzle methods, adapted from `DrSwizzler` by Shadowth117.

The swizzle/deswizzle algorithms (for all consoles supported thus far) are identical, i.e. self-inverse.

See:
    https://github.com/Shadowth117/DrSwizzler
"""
from __future__ import annotations

__all__ = [
    "DDSSwizzleError",
    "swizzle_dds_bytes_ps3",
    "swizzle_dds_bytes_ps4",
]

from soulstruct.exceptions import SoulstructError
from .enums import *
from .utilities import *


class DDSSwizzleError(SoulstructError):
    """Base DDS swizzler error."""


def swizzle_dds_bytes_ps3(
    deswizzled: bytes, dxgi_format: DXGI_FORMAT, width: int, height: int, min_data_size: int = 0
) -> bytes:
    bits_per_pixel, pixel_block_size, dds_bytes_per_pixel_set = dxgi_format.get_format_info()
    if dds_bytes_per_pixel_set >= len(deswizzled):
        raise DDSSwizzleError(
            f"DDS texture is too small to contain a single pixel set (expected {dds_bytes_per_pixel_set} bytes)."
        )
    # Pad deswizzled data to minimum size if necessary.
    deswizzled += b"\0" * (min_data_size - len(deswizzled))
    swizzled_size = max((width * height * bits_per_pixel) // 8, min_data_size)
    swizzled = bytearray(b"\0" * swizzled_size)
    sy = height // pixel_block_size
    sx = width // pixel_block_size
    for src_tile_i in range(sx * sy):
        # Identical to PS3 deswizzling.
        dest_tile_i = morton(src_tile_i, sx, sy)
        deswizzled_start = src_tile_i * dds_bytes_per_pixel_set
        deswizzled_tile = deswizzled[deswizzled_start:deswizzled_start + dds_bytes_per_pixel_set]
        swizzled_start = dest_tile_i * dds_bytes_per_pixel_set
        swizzled[swizzled_start:swizzled_start + dds_bytes_per_pixel_set] = deswizzled_tile
    return bytes(swizzled)


def swizzle_dds_bytes_ps4(
    deswizzled: bytes, dxgi_format: DXGI_FORMAT, width: int, height: int, min_data_size: int = 0
) -> bytes:
    bits_per_pixel, pixel_block_size, dds_bytes_per_pixel_set = dxgi_format.get_format_info()
    if dds_bytes_per_pixel_set >= len(deswizzled):
        raise DDSSwizzleError(
            f"DDS texture is too small to contain a single pixel set (expected {dds_bytes_per_pixel_set} bytes)."
        )
    # Pad deswizzled data to minimum size if necessary.
    deswizzled += b"\0" * (min_data_size - len(deswizzled))
    swizzled_size = max((width * height * bits_per_pixel) // 8, min_data_size)
    swizzled = bytearray(b"\0" * swizzled_size)
    sy = height // pixel_block_size  # number of block rows
    sx = width // pixel_block_size  # number of block columns

    pos = 0
    for i in range((sy + 7) // 8):
        for j in range((sx + 7) // 8):
            for src_tile_i in range(64):
                dest_tile_i = morton(src_tile_i, 8, 8)
                dest_tile_row = dest_tile_i // 8
                dest_tile_col = dest_tile_i % 8
                if pos > len(deswizzled) - dds_bytes_per_pixel_set:
                    # Can't read another tile.
                    return bytes(swizzled)
                deswizzled_tile = deswizzled[pos:pos + dds_bytes_per_pixel_set]
                pos += dds_bytes_per_pixel_set
                swizzled_start = (dest_tile_row * 8 * sx + dest_tile_col * 8) * dds_bytes_per_pixel_set
                swizzled[swizzled_start:swizzled_start + dds_bytes_per_pixel_set] = deswizzled_tile
    return bytes(swizzled)
