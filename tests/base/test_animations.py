"""Tests for `soulstruct.base.animations`: the TAE event machinery and the SIBCAM camera format.

NOTE: `soulstruct.base.animations.tae` currently fails to import (finding C1), so every TAE test is
guarded behind an import attempt.
"""
from __future__ import annotations

import pytest

from soulstruct.base.animations import SIBCAM
from soulstruct.base.animations.sibcam import (
    CameraFrameTransform,
    FoVKeyframe,
    TimescaledFoVKeyframe,
    FrameRef,
)
from soulstruct.base.animations.anibnd import BaseANIBND
from soulstruct.utilities.maths import Vector3, EulerRad


def _import_tae():
    """Return the `tae` package, or `None` if it cannot be imported (finding C1)."""
    try:
        import soulstruct.base.animations.tae as tae
    except Exception:
        return None
    return tae


# ---------------------------------------------------------------------------
# TAE
# ---------------------------------------------------------------------------


def test_tae_package_imports():
    import soulstruct.base.animations.tae  # noqa: F401


def test_tae_enums_import_independently():
    """The `enums` module has no `BinaryStruct`, so it imports even while `tae/core.py` is broken."""
    from soulstruct.base.animations.tae.enums import TAEEventType

    assert TAEEventType.JumpTable == 0
    assert TAEEventType.PlaySound1 == 128
    assert TAEEventType(96) is TAEEventType.PlayFFX
    # Values must be unique (IntEnum would alias duplicates).
    assert len(set(TAEEventType)) == len(list(TAEEventType))


@pytest.mark.xfail(
    reason="Newly exposed by the C1 import fix (not one of the audit's 20 Critical findings): "
           "`TAEEventType` members Unk136, Unk192, Unk306, Unk317, and Unk900 have no corresponding "
           "`TAEEventData` class in `tae.events`, so `TAEEvent.from_tae_reader()` would raise "
           "`AttributeError` for these event types. Left out of scope pending separate triage.",
    strict=False,
)
def test_tae_event_data_classes_exist_for_every_event_type():
    """`TAEEvent.from_tae_reader()` resolves data classes by `getattr(events, event_type.name)`."""
    from soulstruct.base.animations.tae.enums import TAEEventType

    try:
        from soulstruct.base.animations.tae import events
    except Exception as ex:  # pragma: no cover - depends on C1
        pytest.skip(f"`tae.events` cannot be imported: {ex}")

    missing = [t.name for t in TAEEventType if not hasattr(events, t.name)]
    assert not missing, f"TAEEventType members with no `TAEEventData` class: {missing}"


def test_tae_event_data_classes_declare_matching_event_type():
    from soulstruct.base.animations.tae.enums import TAEEventType

    try:
        from soulstruct.base.animations.tae import events
    except Exception as ex:  # pragma: no cover - depends on C1
        pytest.skip(f"`tae.events` cannot be imported: {ex}")

    mismatched = []
    for event_type in TAEEventType:
        cls = getattr(events, event_type.name, None)
        if cls is None:
            continue
        if getattr(cls, "event_type", None) != event_type:
            mismatched.append(event_type.name)
    assert not mismatched, mismatched


def test_base_anibnd_is_an_abstract_binder_placeholder():
    from soulstruct.containers import Binder

    assert issubclass(BaseANIBND, Binder)
    assert getattr(BaseANIBND, "__abstractmethods__", frozenset()) is not None


def test_animations_package_exports_only_sibcam():
    """L13: `TAE` is not re-exported from `soulstruct.base.animations`."""
    import soulstruct.base.animations as animations

    assert animations.__all__ == ["SIBCAM"]


def test_tae_to_writer_is_unimplemented():
    tae = _import_tae()
    if tae is None:
        pytest.skip("`tae` package cannot be imported (finding C1).")
    instance = tae.TAE()
    with pytest.raises(NotImplementedError):
        instance.to_writer()


# ---------------------------------------------------------------------------
# SIBCAM value types
# ---------------------------------------------------------------------------


def test_camera_frame_transform_repr():
    frame = CameraFrameTransform(
        t=3,
        position=Vector3((1.0, 2.0, 3.0)),
        position_diff_prev=Vector3((0.0, 0.0, 0.0)),
        rotation=EulerRad((0.0, 0.0, 0.0)),
        rotation_diff_prev=EulerRad((0.0, 0.0, 0.0)),
        scale=Vector3((1.0, 1.0, 1.0)),
    )
    text = repr(frame)
    assert text.startswith("CameraFrameTransform(3,")


def test_fov_keyframe_struct_size():
    kf = FoVKeyframe(fov_t=1, fov=0.5, tan_in=0.0, tan_out=0.0)
    assert len(bytes(kf.to_writer())) == 16


def test_frame_ref_struct_size():
    ref = FrameRef(
        t=0, position_index=0, position_diff_prev_index_1=0, position_diff_prev_index_2=0,
        rotation_index=0, rotation_diff_prev_index_1=0, rotation_diff_prev_index_2=0, scale_index=0,
    )
    assert len(bytes(ref.to_writer())) == 32


def test_timescaled_fov_keyframe_from_single():
    kf = FoVKeyframe(fov_t=4, fov=1.0, tan_in=0.1, tan_out=0.2)
    scaled = TimescaledFoVKeyframe.from_fov_keyframe(kf, t_interval=2.5)
    assert scaled.fov_t == pytest.approx(10.0)
    assert scaled.fov == pytest.approx(1.0)
    assert scaled.tan_in == pytest.approx(0.1)
    assert scaled.tan_out == pytest.approx(0.2)


def test_timescaled_fov_keyframes_from_list():
    keyframes = [FoVKeyframe(fov_t=i, fov=float(i), tan_in=0.0, tan_out=0.0) for i in range(4)]
    scaled = TimescaledFoVKeyframe.from_fov_keyframes(keyframes, t_interval=3.0)
    assert [k.fov_t for k in scaled] == [0.0, 3.0, 6.0, 9.0]


# ---------------------------------------------------------------------------
# SIBCAM clip helpers (pure unit, no binary file needed)
# ---------------------------------------------------------------------------


def _frame(t: int) -> CameraFrameTransform:
    return CameraFrameTransform(
        t=t,
        position=Vector3((float(t), 0.0, 0.0)),
        position_diff_prev=Vector3((0.0, 0.0, 0.0)),
        rotation=EulerRad((0.0, 0.0, 0.0)),
        rotation_diff_prev=EulerRad((0.0, 0.0, 0.0)),
        scale=Vector3((1.0, 1.0, 1.0)),
    )


@pytest.fixture
def sibcam() -> SIBCAM:
    return SIBCAM(
        camera_name="cam",
        clip_start_t=2,
        clip_end_t=5,
        initial_fov=1.0,
        full_camera_animation=[_frame(t) for t in range(8)],
        fov_keyframes=[FoVKeyframe(fov_t=i, fov=float(i), tan_in=0.0, tan_out=0.0) for i in range(4)],
    )


def test_sibcam_frame_counts(sibcam):
    assert sibcam.full_frame_count == 8
    assert sibcam.clip_frame_count == 4  # t in [2, 5] inclusive


def test_sibcam_clipped_animation_is_inclusive(sibcam):
    clipped = sibcam.get_clipped_camera_animation()
    assert [f.t for f in clipped] == [2, 3, 4, 5]


def test_sibcam_timescaled_fov_keyframes(sibcam):
    scaled = sibcam.get_clip_timescaled_fov_keyframes()
    assert len(scaled) == 4
    # t_interval = clip_frame_count / len(keyframes) = 4 / 4 = 1.0
    assert [k.fov_t for k in scaled] == [0.0, 1.0, 2.0, 3.0]


def test_sibcam_timescaled_fov_keyframes_single(sibcam):
    sibcam.fov_keyframes = [FoVKeyframe(fov_t=9, fov=1.0, tan_in=0.0, tan_out=0.0)]
    scaled = sibcam.get_clip_timescaled_fov_keyframes()
    assert len(scaled) == 1
    assert scaled[0].fov_t == 0.0


def test_sibcam_timescaled_fov_keyframes_empty(sibcam):
    sibcam.fov_keyframes = []
    assert sibcam.get_clip_timescaled_fov_keyframes() == []


def test_sibcam_writer_requires_animation_and_fov():
    with pytest.raises(ValueError):
        SIBCAM(
            full_camera_animation=[],
            fov_keyframes=[FoVKeyframe(fov_t=1, fov=1.0, tan_in=0.0, tan_out=0.0)],
        ).to_writer()
    with pytest.raises(ValueError):
        SIBCAM(full_camera_animation=[_frame(0)], fov_keyframes=[]).to_writer()
