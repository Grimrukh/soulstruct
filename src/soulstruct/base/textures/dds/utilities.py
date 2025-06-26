from __future__ import annotations

__all__ = [
    "morton",
    "extract_tile",
]


def morton(t: int, sx: int, sy: int) -> int:
    """Find index of output texel that input texel `t` maps to.

    Morton order is a way of interleaving the bits of two numbers to create a single number that can be used to index
    a 2D array in a way that is more cache-friendly than simply using the row and column indices directly. By
    interleaving the bits of the X and Y coordinates, texels that are spatially close are likely to have more similar
    Morton codes -- which, when used as offsets, take better advantage of GPU caching.
    """
    params = [1, 1, t, sx, sy, 0, 0]
    while params[3] > 1 or params[4] > 1:
        if params[3] > 1:
            params[5] += params[1] * (params[2] & 1)
            params[1] *= 2
            params[2] >>= 1
            params[3] >>= 1
        if params[4] > 1:
            params[6] += params[0] * (params[2] & 1)
            params[0] *= 2
            params[2] >>= 1
            params[4] >>= 1
    return params[6] * sx + params[5]


def extract_tile(
    tex_buffer: bytes,
    tex_buffer_total_width: int,
    tile_leftmost_pixel: int,
    tile_topmost_pixel: int,
    tile_width: int,
    tile_height: int,
    bits_per_pixel: int,
    pixel_block_size: int,
    bytes_per_pixel_set: int,
) -> bytes:
    tile_buffer = bytearray((bits_per_pixel * tile_width * tile_height) // 8)

    if pixel_block_size == 4:
        tile_height //= 4
        tile_topmost_pixel //= 4
        tile_leftmost_pixel //= 4
        tex_buffer_total_width //= 4
        tile_width //= 4

    for i in range(tile_topmost_pixel, tile_height):
        row_start = (tile_leftmost_pixel * bytes_per_pixel_set) + (i * tex_buffer_total_width * bytes_per_pixel_set)
        write_start = i * (bytes_per_pixel_set * tile_width)
        tile_buffer[write_start:] = tex_buffer[row_start:row_start + bytes_per_pixel_set * tile_width]

    return bytes(tile_buffer)
