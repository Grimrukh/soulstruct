from __future__ import annotations

__all__ = ["CS_EFFECT_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_EFFECT_QUALITY_DETAIL(ParamRow):
    SoftParticleEnabled: int = ParamField(
        byte, "softParticleEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    GlowEnabled: int = ParamField(
        byte, "glowEnabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistortionEnable: int = ParamField(
        byte, "distortionEnable", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CsupScaleEnabledType: int = ParamField(
        byte, "cs_upScaleEnabledType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FNumOnceEmitsScale: float = ParamField(
        float, "fNumOnceEmitsScale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FEmitSpanScale: float = ParamField(
        float, "fEmitSpanScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance1Scale: float = ParamField(
        float, "fLodDistance1Scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance2Scale: float = ParamField(
        float, "fLodDistance2Scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance3Scale: float = ParamField(
        float, "fLodDistance3Scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FLodDistance4Scale: float = ParamField(
        float, "fLodDistance4Scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FScaleRenderDistanceScale: float = ParamField(
        float, "fScaleRenderDistanceScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "dmy[4]")
