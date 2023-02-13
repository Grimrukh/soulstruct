from __future__ import annotations

__all__ = ["LOAD_BALANCER_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LOAD_BALANCER_PARAM_ST(ParamRow):
    LowerFpsThreshold: float = ParamField(
        float, "lowerFpsThreshold", default=23.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperFpsThreshold: float = ParamField(
        float, "upperFpsThreshold", default=27.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerFpsContinousCount: int = ParamField(
        uint, "lowerFpsContinousCount", default=5,
        tooltip="TOOLTIP-TODO",
    )
    UpperFpsContinousCount: int = ParamField(
        uint, "upperFpsContinousCount", default=20,
        tooltip="TOOLTIP-TODO",
    )
    DownAfterChangeSleep: int = ParamField(
        uint, "downAfterChangeSleep", default=30,
        tooltip="TOOLTIP-TODO",
    )
    UpAfterChangeSleep: int = ParamField(
        uint, "upAfterChangeSleep", default=10,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessLightShaft: int = ParamField(
        byte, "postProcessLightShaft", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessBloom: int = ParamField(
        byte, "postProcessBloom", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessGlow: int = ParamField(
        byte, "postProcessGlow", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessAA: int = ParamField(
        byte, "postProcessAA", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessSSAO: int = ParamField(
        byte, "postProcessSSAO", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessDOF: int = ParamField(
        byte, "postProcessDOF", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessMotionBlur: int = ParamField(
        byte, "postProcessMotionBlur", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessMotionBlurIteration: int = ParamField(
        byte, "postProcessMotionBlurIteration", default=20,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve0[1]")
    ShadowBlur: int = ParamField(
        byte, "shadowBlur", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxParticleHalf: int = ParamField(
        byte, "sfxParticleHalf", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxReflection: int = ParamField(
        byte, "sfxReflection", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxWaterInteraction: int = ParamField(
        byte, "sfxWaterInteraction", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxGlow: int = ParamField(
        byte, "sfxGlow", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxDistortion: int = ParamField(
        byte, "sfxDistortion", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SftSoftSprite: int = ParamField(
        byte, "sftSoftSprite", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxLightShaft: int = ParamField(
        byte, "sfxLightShaft", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxScaleRenderDistanceScale: int = ParamField(
        byte, "sfxScaleRenderDistanceScale", default=20,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolution: int = ParamField(
        byte, "dynamicResolution", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShadowCascade0ResolutionHalf: int = ParamField(
        byte, "shadowCascade0ResolutionHalf", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowCascade1ResolutionHalf: int = ParamField(
        byte, "shadowCascade1ResolutionHalf", default=13,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisablePlayer: int = ParamField(
        byte, "chrWetDisablePlayer", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisableRemotePlayer: int = ParamField(
        byte, "chrWetDisableRemotePlayer", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisableEnemy: int = ParamField(
        byte, "chrWetDisableEnemy", default=21,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolutionPercentageMin: int = ParamField(
        byte, "dynamicResolutionPercentageMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolutionPercentageMax: int = ParamField(
        byte, "dynamicResolutionPercentageMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(30, "reserve1[30]")
