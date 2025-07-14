from __future__ import annotations

__all__ = ["ENEMY_STANDARD_INFO_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class ENEMY_STANDARD_INFO_BANK(ParamRow):
    EnemyBehaviorID: int = ParamField(
        int32, "EnemyBehaviorID", ENEMY_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HP: int = ParamField(
        uint16, "HP", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AttackPower: int = ParamField(
        uint16, "AttackPower", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChrType: int = ParamField(
        int32, "ChrType", ChrType, default=5,
        tooltip="TOOLTIP-TODO",
    )
    HitHeight: float = ParamField(
        float32, "HitHeight", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    HitRadius: float = ParamField(
        float32, "HitRadius", default=0.4000000059604645,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float32, "Weight", default=60.0,
        tooltip="TOOLTIP-TODO",
    )
    DynamicFriction: float = ParamField(
        float32, "DynamicFriction", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaticFriction: float = ParamField(
        float32, "StaticFriction", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperDefState: int = ParamField(
        int32, "UpperDefState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActionDefState: int = ParamField(
        int32, "ActionDefState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RotYperSecond: float = ParamField(
        float32, "RotY_per_Second", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(20, "reserve0[20]")
    RotYperSecondold: int = ParamField(
        uint8, "RotY_per_Second_old", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableSideStep: int = ParamField(
        uint8, "EnableSideStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseRagdollHit: int = ParamField(
        uint8, "UseRagdollHit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(5, "reserve_last[5]")
    Stamina: int = ParamField(
        uint16, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRecover: int = ParamField(
        uint16, "staminaRecover", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaConsumption: int = ParamField(
        uint16, "staminaConsumption", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeffenctPhys: int = ParamField(
        uint16, "deffenct_Phys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(48, "reserve_last2[48]")
