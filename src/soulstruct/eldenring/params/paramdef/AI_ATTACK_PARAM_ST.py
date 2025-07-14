from __future__ import annotations

__all__ = ["AI_ATTACK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class AI_ATTACK_PARAM_ST(ParamRow):
    AttackTableId: int = ParamField(
        int32, "attackTableId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackId: int = ParamField(
        int32, "attackId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SuccessDistance: float = ParamField(
        float32, "successDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TurnTimeBeforeAttack: float = ParamField(
        float32, "turnTimeBeforeAttack", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FrontAngleRange: int = ParamField(
        int16, "frontAngleRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UpAngleThreshold: int = ParamField(
        int16, "upAngleThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DownAngleThershold: int = ParamField(
        int16, "downAngleThershold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFirstAttack: int = ParamField(
        uint8, "isFirstAttack", AI_ATTACK_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnOutRange: int = ParamField(
        uint8, "doesSelectOnOutRange", AI_ATTACK_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MinOptimalDistance: float = ParamField(
        float32, "minOptimalDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxOptimalDistance: float = ParamField(
        float32, "maxOptimalDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDirectionForOptimalAngle1: int = ParamField(
        int16, "baseDirectionForOptimalAngle1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OptimalAttackAngleRange1: int = ParamField(
        int16, "optimalAttackAngleRange1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDirectionForOptimalAngle2: int = ParamField(
        int16, "baseDirectionForOptimalAngle2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OptimalAttackAngleRange2: int = ParamField(
        int16, "optimalAttackAngleRange2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalForExec: float = ParamField(
        float32, "intervalForExec", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SelectionTendency: float = ParamField(
        float32, "selectionTendency", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    ShortRangeTendency: float = ParamField(
        float32, "shortRangeTendency", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    MiddleRangeTendency: float = ParamField(
        float32, "middleRangeTendency", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    FarRangeTendency: float = ParamField(
        float32, "farRangeTendency", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    OutRangeTendency: float = ParamField(
        float32, "outRangeTendency", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId1: int = ParamField(
        int32, "deriveAttackId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId2: int = ParamField(
        int32, "deriveAttackId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId3: int = ParamField(
        int32, "deriveAttackId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId4: int = ParamField(
        int32, "deriveAttackId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId5: int = ParamField(
        int32, "deriveAttackId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId6: int = ParamField(
        int32, "deriveAttackId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId7: int = ParamField(
        int32, "deriveAttackId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId8: int = ParamField(
        int32, "deriveAttackId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId9: int = ParamField(
        int32, "deriveAttackId9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId10: int = ParamField(
        int32, "deriveAttackId10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId11: int = ParamField(
        int32, "deriveAttackId11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId12: int = ParamField(
        int32, "deriveAttackId12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId13: int = ParamField(
        int32, "deriveAttackId13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId14: int = ParamField(
        int32, "deriveAttackId14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId15: int = ParamField(
        int32, "deriveAttackId15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId16: int = ParamField(
        int32, "deriveAttackId16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoalLifeMin: float = ParamField(
        float32, "goalLifeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GoalLifeMax: float = ParamField(
        float32, "goalLifeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnInnerRange: int = ParamField(
        uint8, "doesSelectOnInnerRange", AI_ATTACK_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableAttackOnBattleStart: int = ParamField(
        uint8, "enableAttackOnBattleStart", AI_ATTACK_BOOL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnTargetDown: int = ParamField(
        uint8, "doesSelectOnTargetDown", AI_ATTACK_BOOL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1[1]")
    MinArriveDistance: float = ParamField(
        float32, "minArriveDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxArriveDistance: float = ParamField(
        float32, "maxArriveDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ComboExecDistance: float = ParamField(
        float32, "comboExecDistance", default=4.0,
        tooltip="TOOLTIP-TODO",
    )
    ComboExecRange: float = ParamField(
        float32, "comboExecRange", default=180.0,
        tooltip="TOOLTIP-TODO",
    )
