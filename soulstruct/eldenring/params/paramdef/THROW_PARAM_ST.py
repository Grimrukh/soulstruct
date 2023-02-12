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
        float, "upperYRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRange: float = ParamField(
        float, "lowerYRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDef: float = ParamField(
        float, "diffAngMyToDef", default=60,
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
        byte, "PadType", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AtkEnableState: int = ParamField(
        byte, "AtkEnableState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingType: int = ParamField(
        byte, "throwFollowingType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    ThrowType: int = ParamField(
        byte, "throwType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelfEscCycleCnt: int = ParamField(
        byte, "selfEscCycleCnt", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmyHasChrDirType: int = ParamField(
        byte, "dmyHasChrDirType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsTurnAtker: int = ParamField(
        byte, "isTurnAtker:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWepCate: int = ParamField(
        byte, "isSkipWepCate:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipSphereCast: int = ParamField(
        byte, "isSkipSphereCast:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableCorrectPosforThrowAdjust: int = ParamField(
        byte, "isEnableCorrectPos_forThrowAdjust:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFallAssist: int = ParamField(
        byte, "isEnableThrowFollowingFallAssist:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableThrowFollowingFeedback: int = ParamField(
        byte, "isEnableThrowFollowingFeedback:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad0:2")
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
        float, "adsrobModelPosInterpolationTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFollowingEndEasingTime: float = ParamField(
        float, "throwFollowingEndEasingTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(24, "pad1[24]")
