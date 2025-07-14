from __future__ import annotations

__all__ = ["LOCK_CAM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LOCK_CAM_PARAM_ST(ParamRow):
    CameraDistanceFromTarget: float = ParamField(
        float32, "camDistTarget", default=4.0,
        tooltip="Distance maintained from target by camera in meters. (Default value is 4.)",
    )
    MinRotationElevation: float = ParamField(
        float32, "rotRangeMinX", default=-40.0,
        tooltip="Minimum angle of elevation (X-axis rotation) permitted for camera.",
    )
    LockElevationShiftRatio: float = ParamField(
        float32, "lockRotXShiftRatio", default=0.6,
        tooltip="'Lock X-rotation shift ratio (0.0 to 1.0).' Unclear effect. Default value is 0.6.",
    )
    CharacterVerticalOffset: float = ParamField(
        float32, "chrOrgOffset_Y", default=1.42,
        tooltip="Vertical offset of camera target from character's base. Default value is 1.42.",
    )
    MaxDistanceFromCharacter: float = ParamField(
        float32, "chrLockRangeMaxRadius", default=15.0,
        tooltip="Maximum distance ('radius') of camera from character in meters. Default value is 15; only other "
                "value used is 7.",
    )
    VerticalFieldOfView: float = ParamField(
        float32, "camFovY", default=43.0,
        tooltip="Vertical field of view of camera in degrees. Default value is 43. Never goes above 48 (Lost "
                "Izalith).",
    )
    CharacterLockRangeMaxRadiusD: float = ParamField(
        float32, "chrLockRangeMaxRadius_forD", default=-1.0,
        tooltip="TODO",
    )
    CharacterLockRangeMaxRadiusPD: float = ParamField(
        float32, "chrLockRangeMaxRadius_forPD", default=-1.0,
        tooltip="TODO",
    )
    CloseMaxHeight: float = ParamField(
        float32, "closeMaxHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMinHeight: float = ParamField(
        float32, "closeMinHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseAngRange: float = ParamField(
        float32, "closeAngRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadius: float = ParamField(
        float32, "closeMaxRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadiusforD: float = ParamField(
        float32, "closeMaxRadius_forD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadiusforPD: float = ParamField(
        float32, "closeMaxRadius_forPD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadius: float = ParamField(
        float32, "bulletMaxRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadiusforD: float = ParamField(
        float32, "bulletMaxRadius_forD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadiusforPD: float = ParamField(
        float32, "bulletMaxRadius_forPD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletAngRange: float = ParamField(
        float32, "bulletAngRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LockTgtKeepTime: float = ParamField(
        float32, "lockTgtKeepTime", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrTransChaseRateForNormal: float = ParamField(
        float32, "chrTransChaseRateForNormal", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(48, "pad[48]")
