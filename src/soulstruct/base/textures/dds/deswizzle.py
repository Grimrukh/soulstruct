"""Console DDS deswizzle methods, adapted from `DrSwizzler` by Shadowth117.

See:
    https://github.com/Shadowth117/DrSwizzler
"""
from __future__ import annotations

__all__ = [
    "DDSDeswizzleError",
    "deswizzle_dds_bytes_ps3",
    "deswizzle_dds_bytes_ps4",
]

from soulstruct.exceptions import SoulstructError
from .enums import *
from .utilities import *


class DDSDeswizzleError(SoulstructError):
    """Base DDS deswizzler error."""


def deswizzle_dds_bytes_ps3(swizzled: bytes, dxgi_format: DXGI_FORMAT, width: int, height: int) -> bytes:
    bits_per_pixel, pixel_block_size, dds_bytes_per_pixel_set = dxgi_format.get_format_info()
    print(f"Deswizzle PS3: {dxgi_format}, {width}, {height}")
    print(f"  bpp: {bits_per_pixel}, block size: {pixel_block_size}, bytes per pixel set: {dds_bytes_per_pixel_set}")
    if dds_bytes_per_pixel_set >= len(swizzled):
        raise DDSDeswizzleError(
            f"DDS texture is too small to contain a single pixel set (expected {dds_bytes_per_pixel_set} bytes)."
        )
    deswizzled_size = max((width * height * bits_per_pixel) // 8, dds_bytes_per_pixel_set)
    deswizzled = bytearray(b"\0" * deswizzled_size)
    sy = height // pixel_block_size
    sx = width // pixel_block_size
    for src_tile_i in range(sx * sy):
        dest_tile_i = morton(src_tile_i, sx, sy)
        swizzled_start = src_tile_i * dds_bytes_per_pixel_set
        swizzled_tile = swizzled[swizzled_start:swizzled_start + dds_bytes_per_pixel_set]
        deswizzled_start = dest_tile_i * dds_bytes_per_pixel_set
        deswizzled[deswizzled_start:deswizzled_start + dds_bytes_per_pixel_set] = swizzled_tile
    return bytes(deswizzled)


def deswizzle_dds_bytes_ps4(swizzled: bytes, dxgi_format: DXGI_FORMAT, width: int, height: int) -> bytes:
    bits_per_pixel, pixel_block_size, dds_bytes_per_pixel_set = dxgi_format.get_format_info()
    if dds_bytes_per_pixel_set >= len(swizzled):
        raise DDSDeswizzleError(
            f"DDS texture is too small to contain a single pixel set (expected {dds_bytes_per_pixel_set} bytes)."
        )

    deswizzled_size = max((width * height * bits_per_pixel) // 8, dds_bytes_per_pixel_set)
    deswizzled = bytearray(b"\0" * deswizzled_size)
    sy = height // pixel_block_size  # number of block rows
    sx = width // pixel_block_size  # number of block columns

    pos = 0
    for i in range((sy + 7) // 8):
        for j in range((sx + 7) // 8):
            for src_tile_i in range(64):
                dest_tile_i = morton(src_tile_i, 8, 8)
                dest_tile_row = dest_tile_i // 8
                dest_tile_col = dest_tile_i % 8
                if pos > len(swizzled) - dds_bytes_per_pixel_set:
                    # Can't read another tile.
                    return bytes(deswizzled)
                swizzled_tile = swizzled[pos:pos + dds_bytes_per_pixel_set]
                pos += dds_bytes_per_pixel_set
                if j * 8 + dest_tile_col >= sx or i * 8 + dest_tile_row >= sy:
                    continue  # invalid dest tile
                true_dest_tile_i = (i * 8 + dest_tile_row) * sx + j * 8 + dest_tile_col
                dest_tile_start = true_dest_tile_i * dds_bytes_per_pixel_set
                deswizzled[dest_tile_start:dest_tile_start + dds_bytes_per_pixel_set] = swizzled_tile

    return bytes(deswizzled)
