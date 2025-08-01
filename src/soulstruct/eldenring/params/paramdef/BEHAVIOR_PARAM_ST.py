from __future__ import annotations

__all__ = ["BEHAVIOR_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import BehaviorReference


class BEHAVIOR_PARAM_ST(ParamRow):
    VariationID: int = ParamField(
        int32, "variationId", default=0,
        tooltip="TODO",
    )
    BehaviorJudgeID: int = ParamField(
        int32, "behaviorJudgeId", default=0,
        tooltip="This is the ID specified by TAE events that trigger behaviors.",
    )
    EzstateBehaviorType: int = ParamField(
        uint8, "ezStateBehaviorType_old", default=0,
        tooltip="Unused remnant from Demon's Souls.",
    )
    ReferenceType: int = ParamField(
        uint8, "refType", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Is the reference ID below an Attack or Bullet ID?",
    )
    _Pad0: bytes = ParamPad(2, "pad2[2]")
    ReferenceID: int = ParamField(
        int32, "refId", default=-1, dynamic_callback=BehaviorReference(),
        tooltip="TODO",
    )
    ConsumeSA: float = ParamField(
        float32, "consumeSA", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaCost: int = ParamField(
        int32, "stamina", default=0,
        tooltip="Stamina cost of behavior.",
    )
    ConsumeDurability: int = ParamField(
        int32, "consumeDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Category: int = ParamField(
        uint8, "category", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
                "for thrown goods and 'No Category' otherwise.",
    )
    HumanityCost: int = ParamField(
        uint8, "heroPoint", default=0,
        tooltip="Humanity cost of behavior. Never used.",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
