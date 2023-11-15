"""Console DDS deswizzler methods, adapted from DSMapStudio (Horkrux, I believe)."""
from __future__ import annotations

__all__ = ["DDSDeswizzler", "DDSDeswizzlerError"]

from dataclasses import dataclass, field

from soulstruct.exceptions import SoulstructError
from .enums import *


class DDSDeswizzlerError(SoulstructError):
    """Base DDS deswizzler error."""


@dataclass(slots=True)
class DDSDeswizzler:
    """Deswizzles console DDS textures.

    Uses a recursive call structure, so the input and output bytes are stored in the instance.
    """

    block_size: int
    dxgi_format: DXGI_FORMAT
    pitch_or_linear_size: int
    swizzled: bytes

    deswizzled: bytearray | None = None
    write_offset: int = field(init=False, default=0)

    def _finish(self) -> bytes:
        deswizzled = bytes(self.deswizzled)
        self.deswizzled = None
        self.write_offset = 0
        return deswizzled

    def deswizzle_dds_bytes_ps4(self, width: int, height: int) -> bytes:
        self.deswizzled = bytearray(b"\0" * len(self.swizzled))

        match self.dxgi_format:
            case DXGI_FORMAT.X32_TYPELESS_G8X24_UINT:
                # blocks_h = (width + 7) // 8
                # blocks_v = (height + 7) // 8
                # swizzle_block_size = 8
                self._deswizzle_dds_bytes_ps4_rgba(width, height, 0, 2, is_8bit=False)
                return self._finish()
            case DXGI_FORMAT.P016:
                blocks_h = (width + 15) // 16
                blocks_v = (height + 15) // 16
                swizzle_block_size = 16
            case _:
                blocks_h = (width + 31) // 32
                blocks_v = (height + 31) // 32
                swizzle_block_size = 32

        try:
            v = 0
            for i in range(blocks_v):
                h = 0
                for j in range(blocks_h):
                    offset = h + v

                    if self.dxgi_format == DXGI_FORMAT.P016:
                        self._deswizzle_dds_bytes_ps4_rgba(16, 16, offset, 2, is_8bit=True)
                    else:
                        self._deswizzle_dds_bytes_ps4(32, 32, offset, 2)

                    h += (swizzle_block_size // 4) * self.block_size

                if self.dxgi_format == DXGI_FORMAT.P016:
                    v += swizzle_block_size ** 2
                elif self.block_size == 8:
                    v += swizzle_block_size * (width // 2)
                else:
                    v += swizzle_block_size * width
        except Exception as ex:
            raise DDSDeswizzlerError(
                f"Failed to deswizzle PS4 texture with DXGI format {self.dxgi_format}. Error: {ex}"
            )

        return self._finish()

    def deswizzle_dds_bytes_switch(self, width: int, height: int):
        self.deswizzled = bytearray(b"\0" * len(self.swizzled))

        stripe_count = width // 32
        blocks_per_stripe = height // 32
        dds_block_size = 8
        stripe_width = dds_block_size * 8
        stripe_block_size = stripe_width * 8
        width_stride = stripe_width // 2
        height_stride = (stripe_count * stripe_block_size) // 2
        self.pitch_or_linear_size = 256

        try:
            for i in range(stripe_count):
                for j in range(blocks_per_stripe):
                    offset = (i * stripe_width) + (j * stripe_count * stripe_block_size)

                    # Left:
                    self._deswizzle_dds_bytes_ps4(16, 16, offset, 2)
                    self._deswizzle_dds_bytes_ps4(16, 16, offset + height_stride, 2)

                    # Right:
                    self._deswizzle_dds_bytes_ps4(16, 16, offset + width_stride, 2)
                    self._deswizzle_dds_bytes_ps4(16, 16, offset + width_stride + height_stride, 2)
        except Exception as ex:
            raise DDSDeswizzlerError(f"Failed to deswizzle Switch texture. Error: {ex}")

        return self._finish()

    def _deswizzle_dds_bytes_ps3(self, width: int, height: int, offset: int, offset_factor: int):
        """Recursively deswizzles PS3 DDS bytes. TODO: Base call?"""

        if width * height > 4:
            # Four quadrant sub-calls.
            new_offset_factor = offset_factor * 2
            half_width = width_stride = width // 2
            half_height = height // 2
            height_stride = (half_width * half_height * offset_factor)
            new_offsets = (
                offset,
                offset + width_stride,
                offset + height_stride,
                offset + width_stride + height_stride,
            )
            for new_offset in new_offsets:
                self._deswizzle_dds_bytes_ps3(half_width, half_height, new_offset, new_offset_factor)
            return

        # Otherwise, we have zoomed in to a base block of 2x2 or less pixels.
        offset *= 3
        for i, write_offset in enumerate((3, 2, 1, 7, 6, 5)):
            self.deswizzled[offset + i] = self.swizzled[self.write_offset + write_offset]
        offset += self.pitch_or_linear_size * 3
        for i, write_offset in enumerate((11, 10, 9, 15, 14, 13)):
            self.deswizzled[offset + i] = self.swizzled[self.write_offset + write_offset]
        self.write_offset += 16

    def _deswizzle_dds_bytes_ps4(self, width: int, height: int, offset: int, offset_factor: int):
        """Recursively deswizzles PS4 DDS bytes."""

        if width * height > 16:
            # Four quadrant calls.
            new_offset_factor = offset_factor * 2
            half_width = width // 2
            half_height = height // 2
            width_stride = (width // 8 * self.block_size)
            height_stride = (self.pitch_or_linear_size // 8 * (height // 8) * self.block_size)
            new_offsets = (
                offset,
                offset + width_stride,
                offset + height_stride,
                offset + width_stride + height_stride,
            )
            for new_offset in new_offsets:
                self._deswizzle_dds_bytes_ps4(half_width, half_height, new_offset, new_offset_factor)
            return

        # Otherwise, we have zoomed in to a base block of 4x4 or less pixels.
        for i in range(self.block_size):
            self.deswizzled[offset + i] = self.swizzled[self.write_offset + i]
        self.write_offset += self.block_size

    def _deswizzle_dds_bytes_ps4_rgba(self, width: int, height: int, offset: int, offset_factor: int, is_8bit: bool):
        """Recursively deswizzles PS4 DDS bytes (RGBA version)."""

        if width * height > 4:
            # Four quadrant calls.
            new_offset_factor = offset_factor * 2
            half_width = width_stride = width // 2
            half_height = height // 2
            height_stride = (half_width * half_height * offset_factor)
            new_offsets = (
                offset,
                offset + width_stride,
                offset + height_stride,
                offset + width_stride + height_stride,
            )
            for new_offset in new_offsets:
                self._deswizzle_dds_bytes_ps4_rgba(half_width, half_height, new_offset, new_offset_factor, is_8bit)
            return

        # Otherwise, we have zoomed in to a base block of 4x4 or less pixels.
        offset *= 4 if is_8bit else 8
        for i in range(8 if is_8bit else 16):
            self.deswizzled[offset + i] = self.swizzled[self.write_offset + i]
        self.write_offset += 8 if is_8bit else 16

        offset += self.pitch_or_linear_size * (4 if is_8bit else 8)
        for i in range(8 if is_8bit else 16):
            self.deswizzled[offset + i] = self.swizzled[self.write_offset + i]
        self.write_offset += 8 if is_8bit else 16
