from __future__ import annotations

__all__ = ["Dummy"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from .version import FLVERVersion


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
    color_rgba: list[int] = field(default_factory=lambda: [255, 255, 255, 255])  # always stored as RGBA
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
        color_rgba = list(reversed(_color)) if flver_version == FLVERVersion.DarkSouls2 else list(_color)
        dummy = dummy_struct.to_object(cls, color_rgba=color_rgba)
        return dummy

    def to_flver_writer(self, writer: BinaryWriter, flver_version: FLVERVersion):
        _color = tuple(self.color_rgba) if flver_version == FLVERVersion.DarkSouls2 else tuple(reversed(self.color_rgba))
        dummy_struct = self.STRUCT.from_object(self, _color=_color)
        dummy_struct.to_writer(writer)
