from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_WEP_RIGHT_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class POSTURE_CONTROL_PARAM_WEP_RIGHT_ST(ParamRow):
    A000rightArmFB: int = ParamField(
        short, "a000_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightWristFB: int = ParamField(
        short, "a000_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightWristIO: int = ParamField(
        short, "a000_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
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
    A002rightArmFB: int = ParamField(
        short, "a002_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightWristFB: int = ParamField(
        short, "a002_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightWristIO: int = ParamField(
        short, "a002_rightWristIO", default=0,
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
    A003rightArmFB: int = ParamField(
        short, "a003_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightWristFB: int = ParamField(
        short, "a003_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightWristIO: int = ParamField(
        short, "a003_rightWristIO", default=0,
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
    A010rightArmFB: int = ParamField(
        short, "a010_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightWristFB: int = ParamField(
        short, "a010_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightWristIO: int = ParamField(
        short, "a010_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmFB: int = ParamField(
        short, "a010_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftWristFB: int = ParamField(
        short, "a010_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftWristIO: int = ParamField(
        short, "a010_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmFB: int = ParamField(
        short, "a012_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightWristFB: int = ParamField(
        short, "a012_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightWristIO: int = ParamField(
        short, "a012_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmFB: int = ParamField(
        short, "a012_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftWristFB: int = ParamField(
        short, "a012_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftWristIO: int = ParamField(
        short, "a012_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmFB: int = ParamField(
        short, "a013_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightWristFB: int = ParamField(
        short, "a013_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightWristIO: int = ParamField(
        short, "a013_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmFB: int = ParamField(
        short, "a013_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftWristFB: int = ParamField(
        short, "a013_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftWristIO: int = ParamField(
        short, "a013_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmFB: int = ParamField(
        short, "a014_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightWristFB: int = ParamField(
        short, "a014_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightWristIO: int = ParamField(
        short, "a014_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmFB: int = ParamField(
        short, "a014_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftWristFB: int = ParamField(
        short, "a014_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftWristIO: int = ParamField(
        short, "a014_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmFB: int = ParamField(
        short, "a015_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightWristFB: int = ParamField(
        short, "a015_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightWristIO: int = ParamField(
        short, "a015_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmFB: int = ParamField(
        short, "a015_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftWristFB: int = ParamField(
        short, "a015_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftWristIO: int = ParamField(
        short, "a015_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmFB: int = ParamField(
        short, "a016_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightWristFB: int = ParamField(
        short, "a016_rightWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightWristIO: int = ParamField(
        short, "a016_rightWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmFB: int = ParamField(
        short, "a016_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftWristFB: int = ParamField(
        short, "a016_leftWristFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftWristIO: int = ParamField(
        short, "a016_leftWristIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
