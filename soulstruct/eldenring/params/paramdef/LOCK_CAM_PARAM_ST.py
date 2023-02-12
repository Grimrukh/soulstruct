from __future__ import annotations

__all__ = ["LOCK_CAM_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOCK_CAM_PARAM_ST(ParamRow):
    CameraDistanceFromTarget: float = ParamField(
        float, "camDistTarget", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MinRotationElevation: float = ParamField(
        float, "rotRangeMinX", default=-40,
        tooltip="TOOLTIP-TODO",
    )
    LockElevationShiftRatio: float = ParamField(
        float, "lockRotXShiftRatio", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CharacterVerticalOffset: float = ParamField(
        float, "chrOrgOffset_Y", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxDistanceFromCharacter: float = ParamField(
        float, "chrLockRangeMaxRadius", default=15,
        tooltip="TOOLTIP-TODO",
    )
    VerticalFieldOfView: float = ParamField(
        float, "camFovY", default=43,
        tooltip="TOOLTIP-TODO",
    )
    CharacterLockRangeMaxRadiusD: float = ParamField(
        float, "chrLockRangeMaxRadius_forD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CharacterLockRangeMaxRadiusPD: float = ParamField(
        float, "chrLockRangeMaxRadius_forPD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxHeight: float = ParamField(
        float, "closeMaxHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMinHeight: float = ParamField(
        float, "closeMinHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseAngRange: float = ParamField(
        float, "closeAngRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadius: float = ParamField(
        float, "closeMaxRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadiusforD: float = ParamField(
        float, "closeMaxRadius_forD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CloseMaxRadiusforPD: float = ParamField(
        float, "closeMaxRadius_forPD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadius: float = ParamField(
        float, "bulletMaxRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadiusforD: float = ParamField(
        float, "bulletMaxRadius_forD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletMaxRadiusforPD: float = ParamField(
        float, "bulletMaxRadius_forPD", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BulletAngRange: float = ParamField(
        float, "bulletAngRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LockTgtKeepTime: float = ParamField(
        float, "lockTgtKeepTime", default=2,
        tooltip="TOOLTIP-TODO",
    )
    ChrTransChaseRateForNormal: float = ParamField(
        float, "chrTransChaseRateForNormal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(48, "pad[48]")
