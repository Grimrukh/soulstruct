from __future__ import annotations

__all__ = ["BEHAVIOR_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BEHAVIOR_PARAM_ST(ParamRow):
    VariationID: int = ParamField(
        int, "variationId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorJudgeID: int = ParamField(
        int, "behaviorJudgeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EzstateBehaviorType: int = ParamField(
        byte, "ezStateBehaviorType_old", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReferenceType: int = ParamField(
        byte, "refType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad2[2]")
    refId: int = ParamField(
        int, "refId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeSA: float = ParamField(
        float, "consumeSA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaCost: int = ParamField(
        int, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeDurability: int = ParamField(
        int, "consumeDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Category: int = ParamField(
        byte, "category", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityCost: int = ParamField(
        byte, "heroPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
