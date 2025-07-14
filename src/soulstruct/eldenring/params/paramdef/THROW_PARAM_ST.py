from __future__ import annotations

__all__ = ["THROW_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class THROW_PARAM_ST(ParamRow):
    AtkChrId: int = ParamField(
        int32, "AtkChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrId: int = ParamField(
        int32, "DefChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dist: float = ParamField(
        float32, "Dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMin: float = ParamField(
        float32, "DiffAngMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMax: float = ParamField(
        float32, "DiffAngMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRange: float = ParamField(
        float32, "upperYRange", default=0.2,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRange: float = ParamField(
        float32, "lowerYRange", default=0.2,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDef: float = ParamField(
        float32, "diffAngMyToDef", default=60.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowTypeId: int = ParamField(
        int32, "throwTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAnimId: int = ParamField(
        int32, "atkAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefAnimId: int = ParamField(
        int32, "defAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EscHp: int = ParamField(
        uint16, "escHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfEscCycleTime: int = ParamField(
        uint16, "selfEscCycleTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SphereCastRadiusRateTop: int = ParamField(
        uint16, "sphereCastRadiusRateTop", default=80,
        tooltip="TOOLTIP-TODO",
    )
    SphereCastRadiusRateLow: int = ParamField(
        uint16, "sphereCastRadiusRateLow", default=80,
        tooltip="TOOLTIP-TODO",
    )
    PadType: int = ParamField(
        uint8, "PadType", THROW_PAD_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnableState: int = ParamField(
        uint8, "AtkEnableState", THROW_ENABLE_STATE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingType: int = ParamField(
        uint8, "throwFollowingType", THROW_FOLLOWING_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    ThrowType: int = ParamField(
        uint8, "throwType", THROW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfEscCycleCnt: int = ParamField(
        uint8, "selfEscCycleCnt", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmyHasChrDirType: int = ParamField(
        uint8, "dmyHasChrDirType", THROW_DMY_CHR_DIR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsTurnAtker: bool = ParamField(
        uint8, "isTurnAtker:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWepCate: bool = ParamField(
        uint8, "isSkipWepCate:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipSphereCast: bool = ParamField(
        uint8, "isSkipSphereCast:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableCorrectPosforThrowAdjust: bool = ParamField(
        uint8, "isEnableCorrectPos_forThrowAdjust:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFallAssist: bool = ParamField(
        uint8, "isEnableThrowFollowingFallAssist:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFeedback: bool = ParamField(
        uint8, "isEnableThrowFollowingFeedback:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad0:2", bit_count=2)
    AtkSorbDmyId: int = ParamField(
        int16, "atkSorbDmyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSorbDmyId: int = ParamField(
        int16, "defSorbDmyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Diststart: float = ParamField(
        float32, "Dist_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMinstart: float = ParamField(
        float32, "DiffAngMin_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMaxstart: float = ParamField(
        float32, "DiffAngMax_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRangestart: float = ParamField(
        float32, "upperYRange_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRangestart: float = ParamField(
        float32, "lowerYRange_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDefstart: float = ParamField(
        float32, "diffAngMyToDef_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    JudgeRangeBasePosDmyId1: int = ParamField(
        int32, "judgeRangeBasePosDmyId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    JudgeRangeBasePosDmyId2: int = ParamField(
        int32, "judgeRangeBasePosDmyId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AdsrobModelPosInterpolationTime: float = ParamField(
        float32, "adsrobModelPosInterpolationTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingEndEasingTime: float = ParamField(
        float32, "throwFollowingEndEasingTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad1[24]")
