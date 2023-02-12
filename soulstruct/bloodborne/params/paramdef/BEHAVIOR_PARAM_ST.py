from __future__ import annotations

__all__ = ["BEHAVIOR_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import BehaviorReference


# noinspection PyDataclass
@dataclass(slots=True)
class BEHAVIOR_PARAM_ST(ParamRow):
    VariationID: int = ParamField(
        int, "variationId", default=0,
        tooltip="TODO",
    )
    BehaviorJudgeID: int = ParamField(
        int, "behaviorJudgeId", default=0,
        tooltip="This is the ID specified by TAE events that trigger behaviors.",
    )
    EzstateBehaviorType: int = ParamField(
        byte, "ezStateBehaviorType_old", default=0, hide=True,
        tooltip="Unused remnant from Demon's Souls.",
    )
    ReferenceType: BEHAVIOR_REF_TYPE = ParamField(
        byte, "refType", default=0,
        tooltip="Is the reference ID below an Attack or Bullet ID?",
    )
    _Pad0: bytes = ParamPad(2, "pad0[2]")
    refId: int = ParamField(
        int, "refId", default=-1, dynamic_callback=BehaviorReference(),
        tooltip="TODO",
    )
    VFXVariationID: int = ParamField(
        int, "sfxVariationId", default=0,
        tooltip="Visual effect ID.",
    )
    StaminaCost: int = ParamField(
        int, "stamina", default=0,
        tooltip="Stamina cost of behavior.",
    )
    DurabilityCost: int = ParamField(
        int, "mp", default=0,
        tooltip="Weapon/shield durability cost of behavior.",
    )
    Category: BEHAVIOR_CATEGORY = ParamField(
        byte, "category", default=0,
        tooltip="Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
                "for thrown goods and 'No Category' otherwise.",
    )
    HumanityCost: int = ParamField(
        byte, "heroPoint", default=0, hide=True,
        tooltip="Humanity cost of behavior. Never used.",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
