from __future__ import annotations

__all__ = ["BEHAVIOR_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
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
        byte, "ezStateBehaviorType_old", default=0,
        tooltip="Unused remnant from Demon's Souls.",
    )
    ReferenceType: int = ParamField(
        byte, "refType", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Is the reference ID below an Attack or Bullet ID?",
    )
    _Pad0: bytes = ParamPad(2, "pad0[2]")
    ReferenceID: int = ParamField(
        int, "refId", default=-1, dynamic_callback=BehaviorReference(),
        tooltip="TODO",
    )
    VFXVariationID: int = ParamField(
        int, "sfxVariationId", default=-1,
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
    Category: int = ParamField(
        byte, "category", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
                "for thrown goods and 'No Category' otherwise.",
    )
    HumanityCost: int = ParamField(
        byte, "heroPoint", default=0,
        tooltip="Humanity cost of behavior. Never used.",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
