from __future__ import annotations

__all__ = ["LOAD_BALANCER_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LOAD_BALANCER_PARAM_ST(ParamRow):
    LowerFpsThreshold: float = ParamField(
        float32, "lowerFpsThreshold", default=23.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperFpsThreshold: float = ParamField(
        float32, "upperFpsThreshold", default=27.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerFpsContinousCount: int = ParamField(
        uint32, "lowerFpsContinousCount", default=5,
        tooltip="TOOLTIP-TODO",
    )
    UpperFpsContinousCount: int = ParamField(
        uint32, "upperFpsContinousCount", default=20,
        tooltip="TOOLTIP-TODO",
    )
    DownAfterChangeSleep: int = ParamField(
        uint32, "downAfterChangeSleep", default=30,
        tooltip="TOOLTIP-TODO",
    )
    UpAfterChangeSleep: int = ParamField(
        uint32, "upAfterChangeSleep", default=10,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessLightShaft: int = ParamField(
        uint8, "postProcessLightShaft", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessBloom: int = ParamField(
        uint8, "postProcessBloom", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessGlow: int = ParamField(
        uint8, "postProcessGlow", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessAA: int = ParamField(
        uint8, "postProcessAA", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessSSAO: int = ParamField(
        uint8, "postProcessSSAO", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessDOF: int = ParamField(
        uint8, "postProcessDOF", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessMotionBlur: int = ParamField(
        uint8, "postProcessMotionBlur", default=20,
        tooltip="TOOLTIP-TODO",
    )
    PostProcessMotionBlurIteration: int = ParamField(
        uint8, "postProcessMotionBlurIteration", default=20,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "reserve0[1]")
    ShadowBlur: int = ParamField(
        uint8, "shadowBlur", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxParticleHalf: int = ParamField(
        uint8, "sfxParticleHalf", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxReflection: int = ParamField(
        uint8, "sfxReflection", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxWaterInteraction: int = ParamField(
        uint8, "sfxWaterInteraction", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxGlow: int = ParamField(
        uint8, "sfxGlow", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxDistortion: int = ParamField(
        uint8, "sfxDistortion", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SftSoftSprite: int = ParamField(
        uint8, "sftSoftSprite", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxLightShaft: int = ParamField(
        uint8, "sfxLightShaft", default=20,
        tooltip="TOOLTIP-TODO",
    )
    SfxScaleRenderDistanceScale: int = ParamField(
        uint8, "sfxScaleRenderDistanceScale", default=20,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolution: int = ParamField(
        uint8, "dynamicResolution", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShadowCascade0ResolutionHalf: int = ParamField(
        uint8, "shadowCascade0ResolutionHalf", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowCascade1ResolutionHalf: int = ParamField(
        uint8, "shadowCascade1ResolutionHalf", default=13,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisablePlayer: int = ParamField(
        uint8, "chrWetDisablePlayer", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisableRemotePlayer: int = ParamField(
        uint8, "chrWetDisableRemotePlayer", default=21,
        tooltip="TOOLTIP-TODO",
    )
    ChrWetDisableEnemy: int = ParamField(
        uint8, "chrWetDisableEnemy", default=21,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolutionPercentageMin: int = ParamField(
        uint8, "dynamicResolutionPercentageMin", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DynamicResolutionPercentageMax: int = ParamField(
        uint8, "dynamicResolutionPercentageMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(30, "reserve1[30]")
