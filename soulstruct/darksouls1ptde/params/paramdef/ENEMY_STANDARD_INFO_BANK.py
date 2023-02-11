from __future__ import annotations

__all__ = ["ENEMY_STANDARD_INFO_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ENEMY_STANDARD_INFO_BANK(ParamRowData):
    EnemyBehaviorID: int = ParamField(
        int, "EnemyBehaviorID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HP: int = ParamField(
        ushort, "HP", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AttackPower: int = ParamField(
        ushort, "AttackPower", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChrType: int = ParamField(
        int, "ChrType", default=5,
        tooltip="TOOLTIP-TODO",
    )
    HitHeight: float = ParamField(
        float, "HitHeight", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    HitRadius: float = ParamField(
        float, "HitRadius", default=0.4000000059604645,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "Weight", default=60.0,
        tooltip="TOOLTIP-TODO",
    )
    DynamicFriction: float = ParamField(
        float, "DynamicFriction", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaticFriction: float = ParamField(
        float, "StaticFriction", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperDefState: int = ParamField(
        int, "UpperDefState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActionDefState: int = ParamField(
        int, "ActionDefState", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RotY_per_Second: float = ParamField(
        float, "RotY_per_Second", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(20, "reserve0[20]")
    RotY_per_Second_old: int = ParamField(
        byte, "RotY_per_Second_old", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableSideStep: int = ParamField(
        byte, "EnableSideStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseRagdollHit: int = ParamField(
        byte, "UseRagdollHit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(5, "reserve_last[5]")
    stamina: int = ParamField(
        ushort, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    staminaRecover: int = ParamField(
        ushort, "staminaRecover", default=0,
        tooltip="TOOLTIP-TODO",
    )
    staminaConsumption: int = ParamField(
        ushort, "staminaConsumption", default=0,
        tooltip="TOOLTIP-TODO",
    )
    deffenct_Phys: int = ParamField(
        ushort, "deffenct_Phys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(48, "reserve_last2[48]")
