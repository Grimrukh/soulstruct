__all__ = ["Color"]

import io
import struct

from soulstruct.utilities import unpack_from_buffer


class Color:
    """Simple container for red, green, blue, and alpha channels, with unpacking methods for various channel orders."""

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @classmethod
    def from_rgba(cls, red, green, blue, alpha):
        return cls(red, green, blue, alpha)

    @classmethod
    def unpack_rgba(cls, buffer: io.BufferedIOBase):
        red, green, blue, alpha = unpack_from_buffer(buffer, "<4f")
        return cls(red, green, blue, alpha)

    def pack_rgba(self) -> bytes:
        return struct.pack("<4B", self.red, self.green, self.blue, self.alpha)

    @classmethod
    def from_bgra(cls, blue, green, red, alpha):
        return cls(red, green, blue, alpha)

    @classmethod
    def unpack_bgra(cls, buffer: io.BufferedIOBase):
        blue, green, red, alpha = unpack_from_buffer(buffer, "<4f")
        return cls(red, green, blue, alpha)

    def pack_bgra(self) -> bytes:
        return struct.pack("<4B", self.blue, self.green, self.red, self.alpha)

    @classmethod
    def from_argb(cls, alpha, red, green, blue):
        return cls(red, green, blue, alpha)

    @classmethod
    def unpack_argb(cls, buffer: io.BufferedIOBase):
        alpha, red, green, blue = unpack_from_buffer(buffer, "<4f")
        return cls(red, green, blue, alpha)

    def pack_argb(self) -> bytes:
        return struct.pack("<4B", self.alpha, self.red, self.green, self.blue)

    @classmethod
    def black(cls):
        return cls(0, 0, 0, 1)

    default = black

    def __repr__(self):
        return f"Color(red={self.red}, green={self.green}, blue={self.blue}, alpha={self.alpha})"
