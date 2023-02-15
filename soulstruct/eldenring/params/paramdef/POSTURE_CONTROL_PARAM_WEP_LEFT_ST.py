from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_WEP_LEFT_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
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
    A003leftArmFB: int = ParamField(
        short, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristFB: int = ParamField(
        short, "a003_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftWristIO: int = ParamField(
        short, "a003_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad[14]")
