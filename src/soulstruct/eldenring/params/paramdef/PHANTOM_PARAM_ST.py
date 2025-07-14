from __future__ import annotations

__all__ = ["PHANTOM_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PHANTOM_PARAM_ST(ParamRow):
    EdgeColorA: float = ParamField(
        float32, "edgeColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorA: float = ParamField(
        float32, "frontColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorA: float = ParamField(
        float32, "diffMulColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorA: float = ParamField(
        float32, "specMulColorA", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorA: float = ParamField(
        float32, "lightColorA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorR: int = ParamField(
        uint8, "edgeColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorG: int = ParamField(
        uint8, "edgeColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    EdgeColorB: int = ParamField(
        uint8, "edgeColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorR: int = ParamField(
        uint8, "frontColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorG: int = ParamField(
        uint8, "frontColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FrontColorB: int = ParamField(
        uint8, "frontColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorR: int = ParamField(
        uint8, "diffMulColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorG: int = ParamField(
        uint8, "diffMulColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    DiffMulColorB: int = ParamField(
        uint8, "diffMulColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorR: int = ParamField(
        uint8, "specMulColorR", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorG: int = ParamField(
        uint8, "specMulColorG", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpecMulColorB: int = ParamField(
        uint8, "specMulColorB", default=255,
        tooltip="TOOLTIP-TODO",
    )
    LightColorR: int = ParamField(
        uint8, "lightColorR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorG: int = ParamField(
        uint8, "lightColorG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightColorB: int = ParamField(
        uint8, "lightColorB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve[1]")
    Alpha: float = ParamField(
        float32, "alpha", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlendRate: float = ParamField(
        float32, "blendRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlendType: int = ParamField(
        uint8, "blendType", PHANTOM_BLEN_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEdgeSubtract: int = ParamField(
        uint8, "isEdgeSubtract", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFrontSubtract: int = ParamField(
        uint8, "isFrontSubtract", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNo2Pass: int = ParamField(
        uint8, "isNo2Pass", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EdgePower: float = ParamField(
        float32, "edgePower", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GlowScale: float = ParamField(
        float32, "glowScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
