"""SIBCAM file, which defines a camera animation (movement and FoV changes), mainly for cutscenes.

Currently only made for Dark Souls Remastered. (PTDE is identical, but with 32-bit offsets, I believe.)
"""
from __future__ import annotations

__all__ = [
    "CameraFrameTransform",
    "FoVKeyframe",
    "SIBCAM",
]

from dataclasses import dataclass

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, ByteOrder
from soulstruct.utilities.maths import Vector3


@dataclass(slots=True)
class FrameRef:
    index: int
    position_index: int
    position_diff_prev_index_1: int
    position_diff_prev_index_2: int  # TODO: what do these do?
    rotation_index: int
    rotation_diff_prev_index_1: int
    rotation_diff_prev_index_2: int  # TODO: what do these do?
    scale_index: int


@dataclass(slots=True)
class CameraFrameTransform:
    """Transform for a single frame during the SIBCAM camera animation."""
    index: int
    position: Vector3
    position_diff_prev: Vector3
    rotation: Vector3
    rotation_diff_prev: Vector3
    scale: Vector3


@dataclass(slots=True)
class FoVKeyframe:
    """A single keyframe for SIBCAM Field of View, corresponding to the transform at `frame_index`."""
    frame_index: int
    fov: float
    tan_in: float
    tan_out: float


class SIBCAM(GameFile):

    big_endian: bool
    camera_name: str
    fov_keyframe_count: int
    initial_fov: float
    camera_animation: list[CameraFrameTransform]
    fov_keyframes: list[FoVKeyframe]

    # TODO: Unknown chunks of data. Check it for counts and offsets...?
    unk_pre_vector_count: bytes
    unk_post_vector_count: bytes
    unk_pre_frame_count: bytes
    unk_post_frame_count: bytes
    unk_pre_fov_count: bytes
    unk_post_fov_count: bytes

    def unpack(self, reader: BinaryReader, **kwargs):
        self.big_endian = reader.read(4) == b"\00\00\00\01"
        reader.default_byte_order = ByteOrder.big_endian_bool(self.big_endian)

        self.unk_pre_vector_count = reader.read(0x24)
        vector_count = reader.unpack_value("I")
        self.unk_post_vector_count = reader.read(0x14C)

        self.camera_name = reader.unpack_string(encoding="ASCII")
        reader.align(4)

        self.unk_pre_frame_count = reader.read(0x4)
        frame_count = reader.unpack_value("I")  # TODO: equal to length of `self.camera_animation`
        self.unk_post_frame_count = reader.read(0x20)

        frame_refs = [FrameRef(*reader.unpack("8I")) for _ in range(frame_count)]

        self.initial_fov = reader.unpack_value("f")

        self.unk_pre_fov_count = reader.read(4)  # 'i'?
        self.fov_keyframe_count = reader.unpack_value("I")
        self.unk_post_fov_count = reader.read(4)  # 'i'?

        self.fov_keyframes = [FoVKeyframe(*reader.unpack("I3f")) for _ in range(self.fov_keyframe_count)]

        # Position, rotation, and scale vectors indexed by `FrameRef`.
        vectors = [Vector3(reader.unpack_value("3f")) for _ in range(vector_count)]

        # Done reading the file; now resolve into `CameraFrameTransform` list.
        self.camera_animation = [
            CameraFrameTransform(
                index=frame_ref.index,
                position=vectors[frame_ref.position_index],
                position_diff_prev=vectors[frame_ref.position_diff_prev_index_1],
                rotation=vectors[frame_ref.rotation_index],
                rotation_diff_prev=vectors[frame_ref.rotation_diff_prev_index_1],
                scale=vectors[frame_ref.scale_index],
            )
            for frame_ref in frame_refs
        ]

    def pack(self, **kwargs) -> bytes:
        """TODO: Not implemented by Meow. Would need to figure out the 'skipped' bytes first?
            (Or just store them and only support editing the other data, rather than writing from scratch.)
        """
        writer = BinaryWriter(byte_order=ByteOrder.big_endian_bool(self.big_endian))

        # TODO

        return writer.finish()

    @property
    def frame_count(self):
        return len(self.camera_animation)
