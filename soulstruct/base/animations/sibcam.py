"""SIBCAM file, which defines a camera animation (movement and FoV changes), mainly for cutscenes.

Currently only made for Dark Souls Remastered. (PTDE is identical, but with 32-bit offsets, I believe.)
"""
from __future__ import annotations

__all__ = [
    "CameraFrameTransform",
    "FoVKeyframe",
    "SIBCAMUnknownBytes",
    "SIBCAM",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

try:
    Self = tp.Self
except AttributeError:
    Self = "SIBCAM"


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


@dataclass(slots=True)
class SIBCAMUnknownBytes:
    """Unified place to put the six unknown chunks of data in the SIBCAM file."""
    unk_pre_vector_count: bytes  # 0x24
    unk_post_vector_count: bytes  # 0x14C
    unk_pre_frame_count: bytes  # 0x4
    unk_post_frame_count: bytes  # 0x20
    unk_pre_fov_count: bytes  # 0x4
    unk_post_fov_count: bytes  # 0x4


@dataclass(slots=True)
class SIBCAM(GameFile):

    big_endian: bool = False
    camera_name: str = ""
    fov_keyframe_count: int = 0
    initial_fov: float = 0.0
    camera_animation: list[CameraFrameTransform] = field(default_factory=list)
    fov_keyframes: list[FoVKeyframe] = field(default_factory=list)

    unknowns: SIBCAMUnknownBytes = None

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        """NOTE: File contains a null-terminated `camera_name` string early on and is hence not amenable to structs.

        (It's also full of unknown chunks of data, so a struct may be premature.)
        """
        big_endian = reader.read(4) == b"\00\00\00\01"
        reader.default_byte_order = ByteOrder.big_endian_bool(big_endian)

        unk_pre_vector_count = reader.read(0x24)
        vector_count = reader["I"]
        unk_post_vector_count = reader.read(0x14C)

        camera_name = reader.unpack_string(encoding="ASCII")
        reader.align(4)

        unk_pre_frame_count = reader.read(0x4)
        frame_count = reader["I"]  # TODO: equal to length of `self.camera_animation`
        unk_post_frame_count = reader.read(0x20)

        frame_refs = [FrameRef(*reader.unpack("8I")) for _ in range(frame_count)]

        initial_fov = reader["f"]

        unk_pre_fov_count = reader.read(4)  # 'i'?
        fov_keyframe_count = reader["I"]
        unk_post_fov_count = reader.read(4)  # 'i'?

        fov_keyframes = [FoVKeyframe(*reader.unpack("I3f")) for _ in range(fov_keyframe_count)]

        # Position, rotation, and scale vectors indexed by `FrameRef`.
        vectors = [Vector3(reader.unpack("3f")) for _ in range(vector_count)]

        # Done reading the file; now resolve into `CameraFrameTransform` list.
        camera_animation = [
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

        unknowns = SIBCAMUnknownBytes(
            unk_pre_vector_count=unk_pre_vector_count,
            unk_post_vector_count=unk_post_vector_count,
            unk_pre_frame_count=unk_pre_frame_count,
            unk_post_frame_count=unk_post_frame_count,
            unk_pre_fov_count=unk_pre_fov_count,
            unk_post_fov_count=unk_post_fov_count,
        )

        return cls(
            big_endian=big_endian,
            camera_name=camera_name,
            fov_keyframe_count=fov_keyframe_count,
            initial_fov=initial_fov,
            camera_animation=camera_animation,
            fov_keyframes=fov_keyframes,
            unknowns=unknowns,
        )

    def to_writer(self) -> BinaryWriter:
        """TODO: Not implemented by Meow. Would need to figure out the 'skipped' bytes first?
            (Or just store them and only support editing the other data, rather than writing from scratch.)
        """
        if not self.unknowns:
            raise ValueError(
                "Cannot write SIBCAM without all the unknown chunks of data. (This means all SIBCAM instances should "
                "be loaded from existing files.)"
            )

        writer = BinaryWriter(byte_order=ByteOrder.big_endian_bool(self.big_endian))

        raise NotImplementedError("SIBCAM files cannot be written yet.")

    @property
    def frame_count(self):
        return len(self.camera_animation)
