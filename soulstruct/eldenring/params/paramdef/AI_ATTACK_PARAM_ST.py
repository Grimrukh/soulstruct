from __future__ import annotations

__all__ = ["AI_ATTACK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_ATTACK_PARAM_ST(ParamRowData):
    AttackTableId: int = ParamField(
        int, "attackTableId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackId: int = ParamField(
        int, "attackId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SuccessDistance: float = ParamField(
        float, "successDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TurnTimeBeforeAttack: float = ParamField(
        float, "turnTimeBeforeAttack", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FrontAngleRange: int = ParamField(
        short, "frontAngleRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UpAngleThreshold: int = ParamField(
        short, "upAngleThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DownAngleThershold: int = ParamField(
        short, "downAngleThershold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFirstAttack: int = ParamField(
        byte, "isFirstAttack", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnOutRange: int = ParamField(
        byte, "doesSelectOnOutRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MinOptimalDistance: float = ParamField(
        float, "minOptimalDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxOptimalDistance: float = ParamField(
        float, "maxOptimalDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDirectionForOptimalAngle1: int = ParamField(
        short, "baseDirectionForOptimalAngle1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OptimalAttackAngleRange1: int = ParamField(
        short, "optimalAttackAngleRange1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDirectionForOptimalAngle2: int = ParamField(
        short, "baseDirectionForOptimalAngle2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OptimalAttackAngleRange2: int = ParamField(
        short, "optimalAttackAngleRange2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IntervalForExec: float = ParamField(
        float, "intervalForExec", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SelectionTendency: float = ParamField(
        float, "selectionTendency", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ShortRangeTendency: float = ParamField(
        float, "shortRangeTendency", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MiddleRangeTendency: float = ParamField(
        float, "middleRangeTendency", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FarRangeTendency: float = ParamField(
        float, "farRangeTendency", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OutRangeTendency: float = ParamField(
        float, "outRangeTendency", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId1: int = ParamField(
        int, "deriveAttackId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId2: int = ParamField(
        int, "deriveAttackId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId3: int = ParamField(
        int, "deriveAttackId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId4: int = ParamField(
        int, "deriveAttackId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId5: int = ParamField(
        int, "deriveAttackId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId6: int = ParamField(
        int, "deriveAttackId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId7: int = ParamField(
        int, "deriveAttackId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId8: int = ParamField(
        int, "deriveAttackId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId9: int = ParamField(
        int, "deriveAttackId9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId10: int = ParamField(
        int, "deriveAttackId10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId11: int = ParamField(
        int, "deriveAttackId11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId12: int = ParamField(
        int, "deriveAttackId12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId13: int = ParamField(
        int, "deriveAttackId13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId14: int = ParamField(
        int, "deriveAttackId14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId15: int = ParamField(
        int, "deriveAttackId15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DeriveAttackId16: int = ParamField(
        int, "deriveAttackId16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoalLifeMin: float = ParamField(
        float, "goalLifeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GoalLifeMax: float = ParamField(
        float, "goalLifeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnInnerRange: int = ParamField(
        byte, "doesSelectOnInnerRange", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableAttackOnBattleStart: int = ParamField(
        byte, "enableAttackOnBattleStart", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DoesSelectOnTargetDown: int = ParamField(
        byte, "doesSelectOnTargetDown", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1[1]")
    MinArriveDistance: float = ParamField(
        float, "minArriveDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxArriveDistance: float = ParamField(
        float, "maxArriveDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ComboExecDistance: float = ParamField(
        float, "comboExecDistance", default=4,
        tooltip="TOOLTIP-TODO",
    )
    ComboExecRange: float = ParamField(
        float, "comboExecRange", default=180,
        tooltip="TOOLTIP-TODO",
    )
