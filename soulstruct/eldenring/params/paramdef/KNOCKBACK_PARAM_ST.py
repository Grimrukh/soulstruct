from __future__ import annotations

__all__ = ["KNOCKBACK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class KNOCKBACK_PARAM_ST(ParamRowData):
    DamageMinContTime: float = ParamField(
        float, "damage_Min_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageSContTime: float = ParamField(
        float, "damage_S_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageMContTime: float = ParamField(
        float, "damage_M_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageLContTime: float = ParamField(
        float, "damage_L_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBlowSContTime: float = ParamField(
        float, "damage_BlowS_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBlowMContTime: float = ParamField(
        float, "damage_BlowM_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageStrikeContTime: float = ParamField(
        float, "damage_Strike_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageUppercutContTime: float = ParamField(
        float, "damage_Uppercut_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamagePushContTime: float = ParamField(
        float, "damage_Push_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBreathContTime: float = ParamField(
        float, "damage_Breath_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageHeadShotContTime: float = ParamField(
        float, "damage_HeadShot_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardSContTime: float = ParamField(
        float, "guard_S_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLContTime: float = ParamField(
        float, "guard_L_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLLContTime: float = ParamField(
        float, "guard_LL_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBrakeContTime: float = ParamField(
        float, "guardBrake_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageMinDecTime: float = ParamField(
        float, "damage_Min_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageSDecTime: float = ParamField(
        float, "damage_S_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageMDecTime: float = ParamField(
        float, "damage_M_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageLDecTime: float = ParamField(
        float, "damage_L_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBlowSDecTime: float = ParamField(
        float, "damage_BlowS_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBlowMDecTime: float = ParamField(
        float, "damage_BlowM_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageStrikeDecTime: float = ParamField(
        float, "damage_Strike_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageUppercutDecTime: float = ParamField(
        float, "damage_Uppercut_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamagePushDecTime: float = ParamField(
        float, "damage_Push_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageBreathDecTime: float = ParamField(
        float, "damage_Breath_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DamageHeadShotDecTime: float = ParamField(
        float, "damage_HeadShot_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardSDecTime: float = ParamField(
        float, "guard_S_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLDecTime: float = ParamField(
        float, "guard_L_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLLDecTime: float = ParamField(
        float, "guard_LL_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBrakeDecTime: float = ParamField(
        float, "guardBrake_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
