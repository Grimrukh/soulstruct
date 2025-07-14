from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_WEP_LEFT_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class POSTURE_CONTROL_PARAM_WEP_LEFT_ST(ParamRow):
    A000leftArmFB: int = ParamField(
        int16, "a000_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWristFB: int = ParamField(
        int16, "a000_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWristIO: int = ParamField(
        int16, "a000_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWeaponRotation: int = ParamField(
        int16, "a000_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmFB: int = ParamField(
        int16, "a002_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWristFB: int = ParamField(
        int16, "a002_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWristIO: int = ParamField(
        int16, "a002_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWeaponRotation: int = ParamField(
        int16, "a002_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmFB: int = ParamField(
        int16, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad_old[14]")
    A003leftWristFB: int = ParamField(
        int16, "a003_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristIO: int = ParamField(
        int16, "a003_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWeaponRotation: int = ParamField(
        int16, "a003_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad[8]")
