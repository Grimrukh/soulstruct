from __future__ import annotations

__all__ = ["CS_EFFECT_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_EFFECT_QUALITY_DETAIL(ParamRow):
    SoftParticleEnabled: int = ParamField(
        uint8, "softParticleEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    GlowEnabled: int = ParamField(
        uint8, "glowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistortionEnable: int = ParamField(
        uint8, "distortionEnable", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CsupScaleEnabledType: int = ParamField(
        uint8, "cs_upScaleEnabledType", CS_GCONFIG_ENABLED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FNumOnceEmitsScale: float = ParamField(
        float32, "fNumOnceEmitsScale", default=0.9,
        tooltip="TOOLTIP-TODO",
    )
    FEmitSpanScale: float = ParamField(
        float32, "fEmitSpanScale", default=1.1,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance1Scale: float = ParamField(
        float32, "fLodDistance1Scale", default=0.9,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance2Scale: float = ParamField(
        float32, "fLodDistance2Scale", default=0.9,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance3Scale: float = ParamField(
        float32, "fLodDistance3Scale", default=0.9,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance4Scale: float = ParamField(
        float32, "fLodDistance4Scale", default=0.9,
        tooltip="TOOLTIP-TODO",
    )
    FScaleRenderDistanceScale: float = ParamField(
        float32, "fScaleRenderDistanceScale", default=1.2,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "dmy[4]")
