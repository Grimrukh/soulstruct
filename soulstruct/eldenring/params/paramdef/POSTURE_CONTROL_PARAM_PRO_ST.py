from __future__ import annotations

__all__ = ["POSTURE_CONTROL_PARAM_PRO_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class POSTURE_CONTROL_PARAM_PRO_ST(ParamRow):
    A000rightArmIO: int = ParamField(
        short, "a000_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000rightArmFB: int = ParamField(
        short, "a000_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftArmIO: int = ParamField(
        short, "a000_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A000leftArmFB: int = ParamField(
        short, "a000_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightArmIO: int = ParamField(
        short, "a002_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002rightArmFB: int = ParamField(
        short, "a002_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmIO: int = ParamField(
        short, "a002_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A002leftArmFB: int = ParamField(
        short, "a002_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightArmIO: int = ParamField(
        short, "a003_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003rightArmFB: int = ParamField(
        short, "a003_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmIO: int = ParamField(
        short, "a003_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A003leftArmFB: int = ParamField(
        short, "a003_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightArmIO: int = ParamField(
        short, "a010_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010rightArmFB: int = ParamField(
        short, "a010_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmIO: int = ParamField(
        short, "a010_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A010leftArmFB: int = ParamField(
        short, "a010_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmIO: int = ParamField(
        short, "a012_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012rightArmFB: int = ParamField(
        short, "a012_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmIO: int = ParamField(
        short, "a012_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A012leftArmFB: int = ParamField(
        short, "a012_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmIO: int = ParamField(
        short, "a013_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013rightArmFB: int = ParamField(
        short, "a013_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmIO: int = ParamField(
        short, "a013_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A013leftArmFB: int = ParamField(
        short, "a013_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmIO: int = ParamField(
        short, "a014_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014rightArmFB: int = ParamField(
        short, "a014_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmIO: int = ParamField(
        short, "a014_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A014leftArmFB: int = ParamField(
        short, "a014_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmIO: int = ParamField(
        short, "a015_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015rightArmFB: int = ParamField(
        short, "a015_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmIO: int = ParamField(
        short, "a015_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A015leftArmFB: int = ParamField(
        short, "a015_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmIO: int = ParamField(
        short, "a016_rightArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016rightArmFB: int = ParamField(
        short, "a016_rightArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmIO: int = ParamField(
        short, "a016_leftArmIO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A016leftArmFB: int = ParamField(
        short, "a016_leftArmFB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
