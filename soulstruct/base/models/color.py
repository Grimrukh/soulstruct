"""NOTE: This file is Python 3.9 compatible for Blender 3.X use."""

__all__ = ["ColorRGB", "ColorRGBA", "ColorRGBA8"]

import abc

from soulstruct.utilities.maths import Vector, Vector3, Vector4


class ColorBase(Vector, abc.ABC):

    @property
    def red(self):
        return self[0]

    @red.setter
    def red(self, value: float):
        self[0] = value

    @property
    def green(self):
        return self[1]

    @green.setter
    def green(self, value: float):
        self[1] = value

    @property
    def blue(self):
        return self[2]

    @blue.setter
    def blue(self, value: float):
        self[2] = value


class ColorRGB(ColorBase, Vector3):
    """Color channels are permitted to go outside [0.0, 1.0] range, as they sometimes do in FromSoft files."""

    black = Vector3.zero
    white = Vector3.ones


class ColorRGBA(ColorBase, Vector4):

    @property
    def alpha(self):
        return self[3]

    @alpha.setter
    def alpha(self, value: float):
        self[3] = value

    @classmethod
    def black(cls):
        return cls(0.0, 0.0, 0.0, 1.0)

    white = Vector4.ones


class ColorRGBA8:
    """Simple container for red, green, blue, and alpha channels.

    Color channels should be bytes in [0, 255] range. This is enforced by the property wrappers.

    Does not support any arithmetic natively.
    """

    def __init__(self, red: int, green: int, blue: int, alpha: int):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value: int):
        if not 0 <= value <= 255:
            raise ValueError(f"Color value {value} is outside 8-bit range [0-255].")
        self._red = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value: int):
        if not 0 <= value <= 255:
            raise ValueError(f"Color value {value} is outside 8-bit range [0-255].")
        self._green = value

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value: int):
        if not 0 <= value <= 255:
            raise ValueError(f"Color value {value} is outside 8-bit range [0-255].")
        self._blue = value

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value: int):
        if not 0 <= value <= 255:
            raise ValueError(f"Color value {value} is outside 8-bit range [0-255].")
        self._alpha = value

    @classmethod
    def black(cls):
        return cls(0, 0, 0, 255)

    @classmethod
    def white(cls):
        return cls(255, 255, 255, 255)

    default = black

    def __repr__(self):
        return f"ColorRGBA8({self.red}, {self.green}, {self.blue}, {self.alpha})"
