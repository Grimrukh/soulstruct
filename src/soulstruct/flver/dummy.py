from __future__ import annotations

__all__ = ["ColorRGBA", "Dummy"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from .version import FLVERVersion


class ColorRGBA:
    __slots__ = ('_r', '_g', '_b', '_a')

    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @staticmethod
    def _validate(value: int) -> int:
        if not isinstance(value, int) or not (0 <= value <= 255):
            raise ValueError(f"Color values must be integers in range [0, 255], not: {value}")
        return value

    @property
    def r(self) -> int:
        return self._r

    @r.setter
    def r(self, value: int):
        self._r = self._validate(value)

    @property
    def g(self) -> int:
        return self._g

    @g.setter
    def g(self, value: int):
        self._g = self._validate(value)

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    def b(self, value: int):
        self._b = self._validate(value)

    @property
    def a(self) -> int:
        return self._a

    @a.setter
    def a(self, value):
        self._a = self._validate(value)

    def __getitem__(self, index):
        if index == 0:
            return self.r
        elif index == 1:
            return self.g
        elif index == 2:
            return self.b
        elif index == 3:
            return self.a
        else:
            raise IndexError("Index must be in range 0-3 for RGBA components.")

    def __setitem__(self, index, value):
        if index == 0:
            self.r = value
        elif index == 1:
            self.g = value
        elif index == 2:
            self.b = value
        elif index == 3:
            self.a = value
        else:
            raise IndexError("Index must be in range 0-3 for RGBA components.")

    def __repr__(self) -> str:
        return f"ColorRGBA(r={self.r}, g={self.g}, b={self.b}, a={self.a})"

    @classmethod
    def default(cls) -> ColorRGBA:
        return cls(255, 255, 255, 255)

    def __iter__(self):
        return iter((self._r, self._g, self._b, self._a))

    def __len__(self) -> int:
        return 4


@dataclass(slots=True)
class Dummy:

    class STRUCT(BinaryStruct):
        translate: Vector3
        _color: list[byte] = binary_array(4)  # could be ARGB (Dark Souls 2 only) or BGRA
        forward: Vector3
        reference_id: short
        parent_bone_index: short
        upward: Vector3
        attach_bone_index: short
        follows_attach_bone: bool
        use_upward_vector: bool
        unk_x30: int  # only used in Sekiro
        unk_x34: int  # only used in Sekiro
        _pad1: bytes = binary_pad(8, init=False)

    translate: Vector3 = field(default_factory=Vector3.zero)
    color_rgba: ColorRGBA = field(default_factory=ColorRGBA.default)  # white
    forward: Vector3 = field(default_factory=lambda: Vector3((0, 0, 1)))
    reference_id: short = 0
    parent_bone_index: short = -1
    upward: Vector3 = field(default_factory=lambda: Vector3((0, 1, 0)))
    attach_bone_index: short = -1
    follows_attach_bone: bool = True  # not sure what the attach bone does if this is disabled
    use_upward_vector: bool = True  # seems more common
    unk_x30: int = 0  # only used in Sekiro+
    unk_x34: int = 0  # only used in Sekiro+

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, flver_version: FLVERVersion) -> Dummy:
        dummy_struct = cls.STRUCT.from_bytes(reader)
        _color = dummy_struct.pop("_color")
        color_rgba = ColorRGBA(*reversed(_color)) if flver_version == FLVERVersion.DarkSouls2 else ColorRGBA(*_color)
        dummy = dummy_struct.to_object(cls, color_rgba=color_rgba)
        return dummy

    def to_flver_writer(self, writer: BinaryWriter, flver_version: FLVERVersion):
        _color = tuple(self.color_rgba if flver_version == FLVERVersion.DarkSouls2 else reversed(self.color_rgba))
        dummy_struct = self.STRUCT.from_object(self, _color=_color)
        dummy_struct.to_writer(writer)
