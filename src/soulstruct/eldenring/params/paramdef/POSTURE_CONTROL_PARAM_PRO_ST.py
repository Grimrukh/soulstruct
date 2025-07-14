from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_PRO_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class POSTURE_CONTROL_PARAM_PRO_ST(ParamRow):
    A000rightArmIO: int = ParamField(
        int16, "a000_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightArmFB: int = ParamField(
        int16, "a000_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftArmIO: int = ParamField(
        int16, "a000_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftArmFB: int = ParamField(
        int16, "a000_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightArmIO: int = ParamField(
        int16, "a002_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightArmFB: int = ParamField(
        int16, "a002_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmIO: int = ParamField(
        int16, "a002_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmFB: int = ParamField(
        int16, "a002_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightArmIO: int = ParamField(
        int16, "a003_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightArmFB: int = ParamField(
        int16, "a003_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmIO: int = ParamField(
        int16, "a003_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmFB: int = ParamField(
        int16, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightArmIO: int = ParamField(
        int16, "a010_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightArmFB: int = ParamField(
        int16, "a010_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmIO: int = ParamField(
        int16, "a010_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmFB: int = ParamField(
        int16, "a010_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmIO: int = ParamField(
        int16, "a012_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmFB: int = ParamField(
        int16, "a012_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmIO: int = ParamField(
        int16, "a012_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmFB: int = ParamField(
        int16, "a012_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmIO: int = ParamField(
        int16, "a013_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmFB: int = ParamField(
        int16, "a013_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmIO: int = ParamField(
        int16, "a013_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmFB: int = ParamField(
        int16, "a013_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmIO: int = ParamField(
        int16, "a014_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmFB: int = ParamField(
        int16, "a014_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmIO: int = ParamField(
        int16, "a014_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmFB: int = ParamField(
        int16, "a014_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmIO: int = ParamField(
        int16, "a015_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmFB: int = ParamField(
        int16, "a015_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmIO: int = ParamField(
        int16, "a015_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmFB: int = ParamField(
        int16, "a015_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmIO: int = ParamField(
        int16, "a016_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmFB: int = ParamField(
        int16, "a016_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmIO: int = ParamField(
        int16, "a016_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmFB: int = ParamField(
        int16, "a016_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
