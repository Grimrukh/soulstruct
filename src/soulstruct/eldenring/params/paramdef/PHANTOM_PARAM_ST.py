from __future__ import annotations

__all__ = ["PHANTOM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PHANTOM_PARAM_ST(ParamRow):
    EdgeColorA: float = ParamField(
        float, "edgeColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorA: float = ParamField(
        float, "frontColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorA: float = ParamField(
        float, "diffMulColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorA: float = ParamField(
        float, "specMulColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorA: float = ParamField(
        float, "lightColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorR: int = ParamField(
        byte, "edgeColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorG: int = ParamField(
        byte, "edgeColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorB: int = ParamField(
        byte, "edgeColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorR: int = ParamField(
        byte, "frontColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorG: int = ParamField(
        byte, "frontColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorB: int = ParamField(
        byte, "frontColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorR: int = ParamField(
        byte, "diffMulColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorG: int = ParamField(
        byte, "diffMulColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorB: int = ParamField(
        byte, "diffMulColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorR: int = ParamField(
        byte, "specMulColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorG: int = ParamField(
        byte, "specMulColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorB: int = ParamField(
        byte, "specMulColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    LightColorR: int = ParamField(
        byte, "lightColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorG: int = ParamField(
        byte, "lightColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorB: int = ParamField(
        byte, "lightColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve[1]")
    Alpha: float = ParamField(
        float, "alpha", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlendRate: float = ParamField(
        float, "blendRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlendType: int = ParamField(
        byte, "blendType", PHANTOM_BLEN_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEdgeSubtract: int = ParamField(
        byte, "isEdgeSubtract", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFrontSubtract: int = ParamField(
        byte, "isFrontSubtract", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNo2Pass: int = ParamField(
        byte, "isNo2Pass", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EdgePower: float = ParamField(
        float, "edgePower", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GlowScale: float = ParamField(
        float, "glowScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
