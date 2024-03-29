from __future__ import annotations

__all__ = ["Dummy"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.base.models.flver.version import Version


@dataclass(slots=True)
class DummyStruct(BinaryStruct):

    translate: Vector3
    _color: list[byte] = field(**BinaryArray(4))  # could be ARGB (Dark Souls 2 only) or BGRA
    forward: Vector3
    reference_id: short
    parent_bone_index: short
    upward: Vector3
    attach_bone_index: short
    flag_1: bool
    use_upward_vector: bool
    unk_x30: int  # only used in Sekiro
    unk_x34: int  # only used in Sekiro
    _pad1: bytes = field(init=False, **BinaryPad(8))


@dataclass(slots=True)
class Dummy:

    translate: Vector3 = field(default_factory=Vector3.zero)
    color_rgba: list[int] = field(default_factory=lambda: [255, 255, 255, 255])  # always stored as RGBA
    forward: Vector3 = field(default_factory=lambda: Vector3((0, 0, 1)))
    reference_id: short = 0
    parent_bone_index: short = -1
    upward: Vector3 = field(default_factory=lambda: Vector3((0, 1, 0)))
    attach_bone_index: short = -1
    flag_1: bool = True  # seems to be enabled more often than disabled
    use_upward_vector: bool = True  # seems more common
    unk_x30: int = 0  # only used in Sekiro+
    unk_x34: int = 0  # only used in Sekiro+

    @classmethod
    def from_flver_reader(cls, reader: BinaryReader, flver_version: Version) -> Dummy:
        """For consistency."""
        dummy_struct = DummyStruct.from_bytes(reader)
        _color = dummy_struct.pop("_color")
        color_rgba = list(reversed(_color)) if flver_version == Version.DarkSouls2 else list(_color)
        dummy = dummy_struct.to_object(cls, color_rgba=color_rgba)
        return dummy

    def to_flver_writer(self, writer: BinaryWriter, flver_version: Version):
        _color = tuple(self.color_rgba) if flver_version == Version.DarkSouls2 else tuple(reversed(self.color_rgba))
        dummy_struct = DummyStruct.from_object(self, _color=_color)
        dummy_struct.to_writer(writer)
