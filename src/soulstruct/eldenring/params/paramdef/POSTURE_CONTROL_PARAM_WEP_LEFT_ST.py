from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_WEP_LEFT_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class POSTURE_CONTROL_PARAM_WEP_LEFT_ST(ParamRow):
    A000leftArmFB: int = ParamField(
        short, "a000_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWristFB: int = ParamField(
        short, "a000_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWristIO: int = ParamField(
        short, "a000_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftWeaponRotation: int = ParamField(
        short, "a000_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmFB: int = ParamField(
        short, "a002_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWristFB: int = ParamField(
        short, "a002_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWristIO: int = ParamField(
        short, "a002_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftWeaponRotation: int = ParamField(
        short, "a002_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmFB: int = ParamField(
        short, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad_old[14]")
    A003leftWristFB: int = ParamField(
        short, "a003_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristIO: int = ParamField(
        short, "a003_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWeaponRotation: int = ParamField(
        short, "a003_leftWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad[8]")
