from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_GENDER_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class POSTURE_CONTROL_PARAM_GENDER_ST(ParamRow):
    A000rightElbowIO: int = ParamField(
        int16, "a000_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftElbowIO: int = ParamField(
        int16, "a000_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000bothLegsIO: int = ParamField(
        int16, "a000_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightElbowIO: int = ParamField(
        int16, "a002_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftElbowIO: int = ParamField(
        int16, "a002_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002bothLegsIO: int = ParamField(
        int16, "a002_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightElbowIO: int = ParamField(
        int16, "a003_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftElbowIO: int = ParamField(
        int16, "a003_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003bothLegsIO: int = ParamField(
        int16, "a003_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightElbowIO: int = ParamField(
        int16, "a010_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftElbowIO: int = ParamField(
        int16, "a010_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010bothLegsIO: int = ParamField(
        int16, "a010_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightElbowIO: int = ParamField(
        int16, "a012_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftElbowIO: int = ParamField(
        int16, "a012_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012bothLegsIO: int = ParamField(
        int16, "a012_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightElbowIO: int = ParamField(
        int16, "a013_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftElbowIO: int = ParamField(
        int16, "a013_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013bothLegsIO: int = ParamField(
        int16, "a013_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightElbowIO: int = ParamField(
        int16, "a014_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftElbowIO: int = ParamField(
        int16, "a014_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014bothLegsIO: int = ParamField(
        int16, "a014_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightElbowIO: int = ParamField(
        int16, "a015_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftElbowIO: int = ParamField(
        int16, "a015_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015bothLegsIO: int = ParamField(
        int16, "a015_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightElbowIO: int = ParamField(
        int16, "a016_rightElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftElbowIO: int = ParamField(
        int16, "a016_leftElbowIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016bothLegsIO: int = ParamField(
        int16, "a016_bothLegsIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(10, "pad[10]")
