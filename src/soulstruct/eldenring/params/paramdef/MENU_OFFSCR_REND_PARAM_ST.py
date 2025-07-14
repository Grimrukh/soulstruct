from __future__ import annotations

__all__ = ["MENU_OFFSCR_REND_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MENU_OFFSCR_REND_PARAM_ST(ParamRow):
    CamAtPosX: float = ParamField(
        float32, "camAtPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamAtPosY: float = ParamField(
        float32, "camAtPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamAtPosZ: float = ParamField(
        float32, "camAtPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamDist: float = ParamField(
        float32, "camDist", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    CamRotX: float = ParamField(
        float32, "camRotX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamRotY: float = ParamField(
        float32, "camRotY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamFov: float = ParamField(
        float32, "camFov", default=49.0,
        tooltip="TOOLTIP-TODO",
    )
    CamDistMin: float = ParamField(
        float32, "camDistMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CamDistMax: float = ParamField(
        float32, "camDistMax", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    CamRotXMin: float = ParamField(
        float32, "camRotXMin", default=-89.0,
        tooltip="TOOLTIP-TODO",
    )
    CamRotXMax: float = ParamField(
        float32, "camRotXMax", default=89.0,
        tooltip="TOOLTIP-TODO",
    )
    GparamID: int = ParamField(
        uint32, "GparamID", default=10,
        tooltip="TOOLTIP-TODO",
    )
    EnvTexId: int = ParamField(
        uint32, "envTexId", default=10,
        tooltip="TOOLTIP-TODO",
    )
    GrapmIDforPS4: int = ParamField(
        uint32, "Grapm_ID_forPS4", default=10,
        tooltip="TOOLTIP-TODO",
    )
    GrapmIDforXB1: int = ParamField(
        uint32, "Grapm_ID_forXB1", default=10,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
