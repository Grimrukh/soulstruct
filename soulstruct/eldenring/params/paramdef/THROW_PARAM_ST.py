from __future__ import annotations

__all__ = ["THROW_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class THROW_PARAM_ST(ParamRow):
    AtkChrId: int = ParamField(
        int, "AtkChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrId: int = ParamField(
        int, "DefChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dist: float = ParamField(
        float, "Dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMin: float = ParamField(
        float, "DiffAngMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMax: float = ParamField(
        float, "DiffAngMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRange: float = ParamField(
        float, "upperYRange", default=0.2,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRange: float = ParamField(
        float, "lowerYRange", default=0.2,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDef: float = ParamField(
        float, "diffAngMyToDef", default=60.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowTypeId: int = ParamField(
        int, "throwTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAnimId: int = ParamField(
        int, "atkAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefAnimId: int = ParamField(
        int, "defAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EscHp: int = ParamField(
        ushort, "escHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfEscCycleTime: int = ParamField(
        ushort, "selfEscCycleTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SphereCastRadiusRateTop: int = ParamField(
        ushort, "sphereCastRadiusRateTop", default=80,
        tooltip="TOOLTIP-TODO",
    )
    SphereCastRadiusRateLow: int = ParamField(
        ushort, "sphereCastRadiusRateLow", default=80,
        tooltip="TOOLTIP-TODO",
    )
    PadType: int = ParamField(
        byte, "PadType", THROW_PAD_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnableState: int = ParamField(
        byte, "AtkEnableState", THROW_ENABLE_STATE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingType: int = ParamField(
        byte, "throwFollowingType", THROW_FOLLOWING_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    ThrowType: int = ParamField(
        byte, "throwType", THROW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfEscCycleCnt: int = ParamField(
        byte, "selfEscCycleCnt", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmyHasChrDirType: int = ParamField(
        byte, "dmyHasChrDirType", THROW_DMY_CHR_DIR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsTurnAtker: bool = ParamField(
        byte, "isTurnAtker:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWepCate: bool = ParamField(
        byte, "isSkipWepCate:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipSphereCast: bool = ParamField(
        byte, "isSkipSphereCast:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableCorrectPosforThrowAdjust: bool = ParamField(
        byte, "isEnableCorrectPos_forThrowAdjust:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFallAssist: bool = ParamField(
        byte, "isEnableThrowFollowingFallAssist:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFeedback: bool = ParamField(
        byte, "isEnableThrowFollowingFeedback:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad0:2", bit_count=2)
    AtkSorbDmyId: int = ParamField(
        short, "atkSorbDmyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSorbDmyId: int = ParamField(
        short, "defSorbDmyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Diststart: float = ParamField(
        float, "Dist_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMinstart: float = ParamField(
        float, "DiffAngMin_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMaxstart: float = ParamField(
        float, "DiffAngMax_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRangestart: float = ParamField(
        float, "upperYRange_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRangestart: float = ParamField(
        float, "lowerYRange_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDefstart: float = ParamField(
        float, "diffAngMyToDef_start", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    JudgeRangeBasePosDmyId1: int = ParamField(
        int, "judgeRangeBasePosDmyId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    JudgeRangeBasePosDmyId2: int = ParamField(
        int, "judgeRangeBasePosDmyId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AdsrobModelPosInterpolationTime: float = ParamField(
        float, "adsrobModelPosInterpolationTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingEndEasingTime: float = ParamField(
        float, "throwFollowingEndEasingTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad1[24]")
