from __future__ import annotations

__all__ = ["MENU_OFFSCR_REND_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENU_OFFSCR_REND_PARAM_ST(ParamRow):
    CamAtPosX: float = ParamField(
        float, "camAtPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamAtPosY: float = ParamField(
        float, "camAtPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamAtPosZ: float = ParamField(
        float, "camAtPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamDist: float = ParamField(
        float, "camDist", default=10,
        tooltip="TOOLTIP-TODO",
    )
    CamRotX: float = ParamField(
        float, "camRotX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamRotY: float = ParamField(
        float, "camRotY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamFov: float = ParamField(
        float, "camFov", default=49,
        tooltip="TOOLTIP-TODO",
    )
    CamDistMin: float = ParamField(
        float, "camDistMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamDistMax: float = ParamField(
        float, "camDistMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    CamRotXMin: float = ParamField(
        float, "camRotXMin", default=-89,
        tooltip="TOOLTIP-TODO",
    )
    CamRotXMax: float = ParamField(
        float, "camRotXMax", default=89,
        tooltip="TOOLTIP-TODO",
    )
    GparamID: int = ParamField(
        uint, "GparamID", default=10,
        tooltip="TOOLTIP-TODO",
    )
    EnvTexId: int = ParamField(
        uint, "envTexId", default=10,
        tooltip="TOOLTIP-TODO",
    )
    GrapmIDforPS4: int = ParamField(
        uint, "Grapm_ID_forPS4", default=10,
        tooltip="TOOLTIP-TODO",
    )
    GrapmIDforXB1: int = ParamField(
        uint, "Grapm_ID_forXB1", default=10,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
