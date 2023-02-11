from __future__ import annotations

__all__ = ["KNOCKBACK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class KNOCKBACK_PARAM_ST(ParamRowData):
    damage_Min_ContTime: float = ParamField(
        float, "damage_Min_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_S_ContTime: float = ParamField(
        float, "damage_S_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_M_ContTime: float = ParamField(
        float, "damage_M_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_L_ContTime: float = ParamField(
        float, "damage_L_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_BlowS_ContTime: float = ParamField(
        float, "damage_BlowS_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_BlowM_ContTime: float = ParamField(
        float, "damage_BlowM_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Strike_ContTime: float = ParamField(
        float, "damage_Strike_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Uppercut_ContTime: float = ParamField(
        float, "damage_Uppercut_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Push_ContTime: float = ParamField(
        float, "damage_Push_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Breath_ContTime: float = ParamField(
        float, "damage_Breath_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_HeadShot_ContTime: float = ParamField(
        float, "damage_HeadShot_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_S_ContTime: float = ParamField(
        float, "guard_S_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_L_ContTime: float = ParamField(
        float, "guard_L_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_LL_ContTime: float = ParamField(
        float, "guard_LL_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guardBrake_ContTime: float = ParamField(
        float, "guardBrake_ContTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Min_DecTime: float = ParamField(
        float, "damage_Min_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_S_DecTime: float = ParamField(
        float, "damage_S_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_M_DecTime: float = ParamField(
        float, "damage_M_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_L_DecTime: float = ParamField(
        float, "damage_L_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_BlowS_DecTime: float = ParamField(
        float, "damage_BlowS_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_BlowM_DecTime: float = ParamField(
        float, "damage_BlowM_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Strike_DecTime: float = ParamField(
        float, "damage_Strike_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Uppercut_DecTime: float = ParamField(
        float, "damage_Uppercut_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Push_DecTime: float = ParamField(
        float, "damage_Push_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_Breath_DecTime: float = ParamField(
        float, "damage_Breath_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    damage_HeadShot_DecTime: float = ParamField(
        float, "damage_HeadShot_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_S_DecTime: float = ParamField(
        float, "guard_S_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_L_DecTime: float = ParamField(
        float, "guard_L_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guard_LL_DecTime: float = ParamField(
        float, "guard_LL_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    guardBrake_DecTime: float = ParamField(
        float, "guardBrake_DecTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
