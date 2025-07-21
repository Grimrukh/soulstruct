"""SIBCAM file, which defines a camera animation (movement and FoV changes), mainly for cutscenes.

Currently only made for Dark Souls Remastered. (PTDE is identical, but with 32-bit offsets, I believe.)
"""
from __future__ import annotations

__all__ = [
    "CameraFrameTransform",
    "FoVKeyframe",
    "SIBCAM",
]

import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

_LOGGER = logging.getLogger(__name__)


class FrameRef(BinaryStruct):
    t: int
    position_index: int
    position_diff_prev_index_1: int
    position_diff_prev_index_2: int  # TODO: what do these do?
    rotation_index: int
    rotation_diff_prev_index_1: int
    rotation_diff_prev_index_2: int  # TODO: what do these do?
    scale_index: int


@dataclass(slots=True)
class CameraFrameTransform:
    """Transform for a single frame during the SIBCAM camera animation.

    Not a binary struct, as vectors are hashed and re-used across frames.
    """
    t: int
    position: Vector3
    position_diff_prev: Vector3
    rotation: Vector3
    rotation_diff_prev: Vector3
    scale: Vector3

    def __repr__(self) -> str:
        return f"CameraFrameTransform({self.t}, {self.position}, {self.rotation}, {self.scale})"


class FoVKeyframe(BinaryStruct):
    """A single keyframe for SIBCAM Field of View. Note that `fov_t` can be on a different scale to transform `t`."""
    fov_t: int
    fov: float
    tan_in: float
    tan_out: float


class SIBCAMHeaderStruct(BinaryStruct):
    _one: int = binary(asserted=1)
    _unk_vec_x04: int = binary(asserted=8)
    _unk_vec_x08: int = binary(asserted=12)
    _unk_vec_x0C: int = binary(asserted=537202708)
    clip_start_t: int
    clip_end_t: int
    _camera_name_offset_offset: int = binary(asserted=132)  # fixed offset to `_camera_name_offset`
    _unk_vec_x1C: int = binary(asserted=1)
    vectors_start_offset: int
    vectors_end_offset_1: int  # before eight null bytes at EOF
    vector_count: int
    _unk_vec_x2C: int = binary(asserted=0)
    vectors_end_offset_2: int  # before eight null bytes at EOF
    _zeroes: bytes = binary_pad(80)
    _camera_name_offset: int = binary(asserted=376)  # fixed offset to end of this struct (last fixed offset)
    _unk_vec_x88: int = binary(asserted=3)
    # NOTE: Probably the wrong way to assert this (00 00 FF FF, then FF FF FF FF FF FF FF FF).
    _unk_vec_x8C: short = binary(asserted=0)
    _unk_vec_x8E: bytes = binary_pad(10, char=b"\xFF")
    initial_position: Vector3
    initial_rotation: Vector3
    initial_scale: Vector3
    frame_data_header_offset: int  # after camera name and align(4)
    _unk_vec_xC0: int = binary(asserted=0)
    _unk_vec_xC4: int = binary(asserted=0)
    fov_data_header_offset: int
    _pad1: bytes = binary_pad(172)
    # Null-terminated camera name here.


class SIBCAMFrameDataHeaderStruct(BinaryStruct):
    frame_refs_offset: int  # after this struct
    frame_count: int
    _unk_frame_x08: int = binary(asserted=3)
    initial_rotation_1: Vector3
    initial_rotation_2: Vector3
    _unk_frame_x20: int = binary(asserted=0)
    # `FrameRef` list here (indices into packed vectors).


class SIBCAMFoVDataHeaderStruct(BinaryStruct):
    initial_fov: float
    fov_keyframes_offset: int
    fov_keyframe_count: int
    _unk_fov_x0C: int = binary(asserted=0)


class SIBCAM(GameFile):
    """Holds camera animation data for cutscenes, including lens FoV."""

    big_endian: bool = False
    camera_name: str = ""
    clip_start_t: int = 0
    clip_end_t: int = 0
    fov_keyframe_count: int = 0
    initial_fov: float = 0.0
    full_camera_animation: list[CameraFrameTransform] = field(default_factory=list)
    fov_keyframes: list[FoVKeyframe] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        """NOTE: File contains a null-terminated `camera_name` string early on and is hence not amenable to structs.

        (It's also full of unknown chunks of data, so a struct may be premature.)
        """
        big_endian = reader.peek(4) == b"\00\00\00\01"
        reader.byte_order = ByteOrder.big_endian_bool(big_endian)

        header = SIBCAMHeaderStruct.from_bytes(reader)
        camera_name = reader.unpack_string(encoding="ASCII")
        reader.align(4)

        if header.frame_data_header_offset != reader.position:
            raise ValueError(
                f"SIBCAM header's frame data header offset is incorrect:\n"
                f"    {header.frame_data_header_offset} != {reader.position}"
            )

        frame_data_header = SIBCAMFrameDataHeaderStruct.from_bytes(reader)
        frame_refs = [FrameRef.from_bytes(reader) for _ in range(frame_data_header.frame_count)]

        if header.fov_data_header_offset != reader.position:
            raise ValueError(
                f"SIBCAM header's FoV data header offset is incorrect:\n"
                f"    {header.fov_data_header_offset} != {reader.position}"
            )

        fov_data_header = SIBCAMFoVDataHeaderStruct.from_bytes(reader)

        if fov_data_header.fov_keyframes_offset != reader.position:
            raise ValueError(
                f"SIBCAM FoV header's keyframes offset is incorrect:\n"
                f"    {fov_data_header.fov_keyframes_offset} != {reader.position}"
            )

        fov_keyframes = [FoVKeyframe.from_bytes(reader) for _ in range(fov_data_header.fov_keyframe_count)]

        if header.vectors_start_offset != reader.position:
            raise ValueError(
                f"SIBCAM header's vectors start offset is incorrect:\n"
                f"    {header.vectors_start_offset} != {reader.position}"
            )

        # Position, rotation, and scale vectors indexed by `FrameRef`.
        vectors = [Vector3(reader.unpack("3f")) for _ in range(header.vector_count)]
        # Note that there are eight empty bytes at EOF, after the vector data.

        if header.vectors_end_offset_1 != reader.position:
            raise ValueError(
                f"SIBCAM header's vectors end offset (first occurrence) is incorrect:\n"
                f"    {header.vectors_end_offset_1} != {reader.position}"
            )
        if header.vectors_end_offset_2 != reader.position:
            raise ValueError(
                f"SIBCAM header's vectors end offset (second occurrence) is incorrect:\n"
                f"    {header.vectors_end_offset_1} != {reader.position}"
            )

        # Done reading the file; now resolve into `CameraFrameTransform` list.
        full_camera_animation = [
            CameraFrameTransform(
                t=frame_ref.t,  # NOTE: does NOT need to start at 0
                position=vectors[frame_ref.position_index],
                position_diff_prev=vectors[frame_ref.position_diff_prev_index_1],
                rotation=vectors[frame_ref.rotation_index],
                rotation_diff_prev=vectors[frame_ref.rotation_diff_prev_index_1],
                scale=vectors[frame_ref.scale_index],
            )
            for frame_ref in frame_refs
        ]

        # Null bytes pad out the end of the file.
        reader.align(16)

        if full_camera_animation:
            # Check for incorrect initial values in header.
            # Unlike offset errors above, we tolerate these and just log warnings.
            first_position = full_camera_animation[0].position
            first_rotation = full_camera_animation[0].rotation
            first_scale = full_camera_animation[0].scale
            
            if not first_position.allclose(header.initial_position):
                _LOGGER.warning(
                    f"Initial camera position in SIBCAM does not match header:\n"
                    f"    {first_position} != {header.initial_position}"
                )
            if not first_rotation.allclose(header.initial_rotation):
                _LOGGER.warning(
                    f"Initial camera rotation in SIBCAM does not match header:\n"
                    f"    {first_rotation} != {header.initial_rotation}"
                )
            if not first_scale.allclose(header.initial_scale):
                _LOGGER.warning(
                    f"Initial camera scale in SIBCAM does not match header:\n"
                    f"    {first_scale} != {header.initial_scale}"
                )

            # For the initial rotation values in the frame data header, we check them against the header, not data.
            if not header.initial_rotation.allclose(frame_data_header.initial_rotation_1):
                _LOGGER.warning(
                    f"SIBCAM header initial rotation does not match frame data header (first occurrence):\n"
                    f"    {first_rotation} != {frame_data_header.initial_rotation_1}"
                )
            if not header.initial_rotation.allclose(frame_data_header.initial_rotation_2):
                _LOGGER.warning(
                    f"SIBCAM header initial rotation does not match frame data header (second occurrence):\n"
                    f"    {first_rotation} != {frame_data_header.initial_rotation_2}"
                )

        return cls(
            big_endian=big_endian,
            camera_name=camera_name,
            clip_start_t=header.clip_start_t,
            clip_end_t=header.clip_end_t,
            fov_keyframe_count=fov_data_header.fov_keyframe_count,
            initial_fov=fov_data_header.initial_fov,
            full_camera_animation=full_camera_animation,
            fov_keyframes=fov_keyframes,
        )

    def to_writer(self) -> BinaryWriter:
        """Pack SIBCAM to binary format.

        TODO: Implement. Only slightly tough part is vector compression (by caching and re-using).
         Should probably use a hash map for this.
        """

        if not self.full_camera_animation:
            raise ValueError("Cannot write SIBCAM with no camera animation data.")
        if not self.fov_keyframes:
            raise ValueError("Cannot write SIBCAM with no FoV keyframes.")

        writer = BinaryWriter(byte_order=ByteOrder.big_endian_bool(self.big_endian))

        hashed_vector_indices = {}
        vectors = []
        frame_refs = []
        for frame in self.full_camera_animation:
            # TODO: Do we enforce that `frame.index == i` here?
            frame_ref_kwargs = {}
            for vec_name in ("position", "position_diff_prev", "rotation", "rotation_diff_prev", "scale"):
                vec = getattr(frame, vec_name)
                vec_hsh = hash(vec)
                if vec_hsh in hashed_vector_indices:
                    vec_index = hashed_vector_indices[vec_hsh]
                else:
                    vec_index = len(vectors)
                    vectors.append(vec)
                    hashed_vector_indices[vec_hsh] = vec_index
                if "diff" in vec_name:
                    # Two copies of each 'diff' vector, for some reason.
                    frame_ref_kwargs[f"{vec_name}_index_1"] = vec_index
                    frame_ref_kwargs[f"{vec_name}_index_2"] = vec_index
                else:
                    frame_ref_kwargs[f"{vec_name}_index"] = vec_index
            frame_refs.append(FrameRef(t=frame.t, **frame_ref_kwargs))

        header = SIBCAMHeaderStruct(
            clip_start_t=self.clip_start_t,
            clip_end_t=self.clip_end_t,
            vectors_start_offset=RESERVED,
            vectors_end_offset_1=RESERVED,
            vector_count=len(vectors),
            vectors_end_offset_2=RESERVED,
            initial_position=self.full_camera_animation[0].position,
            initial_rotation=self.full_camera_animation[0].rotation,
            initial_scale=self.full_camera_animation[0].scale,
            frame_data_header_offset=RESERVED,
            fov_data_header_offset=RESERVED,
        )
        header.to_writer(writer)
        writer.pack_z_string(self.camera_name, encoding="ASCII")
        writer.pad_align(4)
        writer.fill_with_position("frame_data_header_offset", header)

        frame_data_header = SIBCAMFrameDataHeaderStruct(
            frame_refs_offset=RESERVED,
            frame_count=len(frame_refs),
            initial_rotation_1=self.full_camera_animation[0].rotation,
            initial_rotation_2=self.full_camera_animation[0].rotation,
        )
        frame_data_header.to_writer(writer)
        writer.fill_with_position("frame_refs_offset", frame_data_header)
        for frame_ref in frame_refs:
            frame_ref.to_writer(writer)

        writer.fill_with_position("fov_data_header_offset", header)
        fov_data_header = SIBCAMFoVDataHeaderStruct(
            initial_fov=self.initial_fov,
            fov_keyframes_offset=RESERVED,
            fov_keyframe_count=len(self.fov_keyframes),
        )
        fov_data_header.to_writer(writer)
        writer.fill_with_position("fov_keyframes_offset", fov_data_header)
        for keyframe in self.fov_keyframes:
            keyframe.to_writer(writer)

        writer.fill_with_position("vectors_start_offset", header)
        for vec in vectors:
            writer.pack("3f", *vec)

        writer.fill_with_position("vectors_end_offset_1", header)
        writer.fill_with_position("vectors_end_offset_2", header)

        writer.pad(16)  # align finished file to 16 bytes

        return writer

    def get_clipped_camera_animation(self) -> list[CameraFrameTransform]:
        """Get camera animation between clipped start and end times. Note end frame index is inclusive."""
        return [
            frame for frame in self.full_camera_animation
            if self.clip_start_t <= frame.t <= self.clip_end_t  # note inclusive
        ]

    def get_fov_keyframes_scaled_to_clip(self) -> list[tuple[float, float]]:
        """Get a list of `(t, fov)` tuples where `t` is scaled to the clip transform frame count.

        NOTE: The returned `t` values match the scale of the transform frame counts, but do NOT match any offset from
        zero the first frame may have.

        Useful for Blender animation. Returned `t` values are floats to limit loss of precision from integer rounding.
        If only one keyframe is present, its `t` value will be zero. If two are present, their `t` values will be
        zero and `clip_frame_count`. And so on.
        """
        if len(self.fov_keyframes) == 1:
            return [(0.0, self.fov_keyframes[0].fov)]
        # TODO: Wondering if numerator here is off by 1?
        t_interval = self.clip_frame_count / len(self.fov_keyframes)
        return [
            (i * t_interval, frame.fov)
            for i, frame in enumerate(self.fov_keyframes)
        ]

    @property
    def full_frame_count(self):
        return len(self.full_camera_animation)

    @property
    def clip_frame_count(self):
        return len(self.get_clipped_camera_animation())
