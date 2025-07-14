from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_WEP_RIGHT_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class POSTURE_CONTROL_PARAM_WEP_RIGHT_ST(ParamRow):
    A000rightArmFB: int = ParamField(
        int16, "a000_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightWristFB: int = ParamField(
        int16, "a000_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightWristIO: int = ParamField(
        int16, "a000_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightWeaponRotation: int = ParamField(
        int16, "a000_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
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
    A000lefttWeaponRotation: int = ParamField(
        int16, "a000_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightArmFB: int = ParamField(
        int16, "a002_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightWristFB: int = ParamField(
        int16, "a002_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightWristIO: int = ParamField(
        int16, "a002_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightWeaponRotation: int = ParamField(
        int16, "a002_rightWeaponRotation", default=0,
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
    A002lefttWeaponRotation: int = ParamField(
        int16, "a002_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightArmFB: int = ParamField(
        int16, "a003_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightWristFB: int = ParamField(
        int16, "a003_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightWristIO: int = ParamField(
        int16, "a003_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightWeaponRotation: int = ParamField(
        int16, "a003_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmFB: int = ParamField(
        int16, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristFB: int = ParamField(
        int16, "a003_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristIO: int = ParamField(
        int16, "a003_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003lefttWeaponRotation: int = ParamField(
        int16, "a003_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightArmFB: int = ParamField(
        int16, "a010_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightWristFB: int = ParamField(
        int16, "a010_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightWristIO: int = ParamField(
        int16, "a010_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightWeaponRotation: int = ParamField(
        int16, "a010_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmFB: int = ParamField(
        int16, "a010_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftWristFB: int = ParamField(
        int16, "a010_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftWristIO: int = ParamField(
        int16, "a010_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010lefttWeaponRotation: int = ParamField(
        int16, "a010_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmFB: int = ParamField(
        int16, "a012_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightWristFB: int = ParamField(
        int16, "a012_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightWristIO: int = ParamField(
        int16, "a012_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightWeaponRotation: int = ParamField(
        int16, "a012_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmFB: int = ParamField(
        int16, "a012_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftWristFB: int = ParamField(
        int16, "a012_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftWristIO: int = ParamField(
        int16, "a012_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012lefttWeaponRotation: int = ParamField(
        int16, "a012_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmFB: int = ParamField(
        int16, "a013_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightWristFB: int = ParamField(
        int16, "a013_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightWristIO: int = ParamField(
        int16, "a013_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightWeaponRotation: int = ParamField(
        int16, "a013_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmFB: int = ParamField(
        int16, "a013_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftWristFB: int = ParamField(
        int16, "a013_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftWristIO: int = ParamField(
        int16, "a013_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013lefttWeaponRotation: int = ParamField(
        int16, "a013_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmFB: int = ParamField(
        int16, "a014_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightWristFB: int = ParamField(
        int16, "a014_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightWristIO: int = ParamField(
        int16, "a014_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightWeaponRotation: int = ParamField(
        int16, "a014_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmFB: int = ParamField(
        int16, "a014_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftWristFB: int = ParamField(
        int16, "a014_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftWristIO: int = ParamField(
        int16, "a014_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014lefttWeaponRotation: int = ParamField(
        int16, "a014_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmFB: int = ParamField(
        int16, "a015_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightWristFB: int = ParamField(
        int16, "a015_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightWristIO: int = ParamField(
        int16, "a015_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightWeaponRotation: int = ParamField(
        int16, "a015_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmFB: int = ParamField(
        int16, "a015_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftWristFB: int = ParamField(
        int16, "a015_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftWristIO: int = ParamField(
        int16, "a015_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015lefttWeaponRotation: int = ParamField(
        int16, "a015_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmFB: int = ParamField(
        int16, "a016_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightWristFB: int = ParamField(
        int16, "a016_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightWristIO: int = ParamField(
        int16, "a016_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightWeaponRotation: int = ParamField(
        int16, "a016_rightWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmFB: int = ParamField(
        int16, "a016_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftWristFB: int = ParamField(
        int16, "a016_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftWristIO: int = ParamField(
        int16, "a016_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016lefttWeaponRotation: int = ParamField(
        int16, "a016_lefttWeaponRotation", default=0,
        tooltip="TOOLTIP-TODO",
    )
