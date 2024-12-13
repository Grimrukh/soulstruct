from __future__ import annotations

__all__ = ["CLEAR_COUNT_CORRECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CLEAR_COUNT_CORRECT_PARAM_ST(ParamRow):
    MaxHpRate: float = ParamField(
        float, "MaxHpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxMpRate: float = ParamField(
        float, "MaxMpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxStaminaRate: float = ParamField(
        float, "MaxStaminaRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsAttackRate: float = ParamField(
        float, "PhysicsAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float, "SlashAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowAttackRate: float = ParamField(
        float, "BlowAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackRate: float = ParamField(
        float, "ThrustAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NeturalAttackRate: float = ParamField(
        float, "NeturalAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackRate: float = ParamField(
        float, "MagicAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackRate: float = ParamField(
        float, "FireAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAttackRate: float = ParamField(
        float, "ThunderAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackRate: float = ParamField(
        float, "DarkAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsDefenseRate: float = ParamField(
        float, "PhysicsDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefenseRate: float = ParamField(
        float, "MagicDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDefenseRate: float = ParamField(
        float, "FireDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDefenseRate: float = ParamField(
        float, "ThunderDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDefenseRate: float = ParamField(
        float, "DarkDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAttackRate: float = ParamField(
        float, "StaminaAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulRate: float = ParamField(
        float, "SoulRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisionResistRate: float = ParamField(
        float, "PoisionResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseResistRate: float = ParamField(
        float, "DiseaseResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodResistRate: float = ParamField(
        float, "BloodResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistRate: float = ParamField(
        float, "CurseResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeResistRate: float = ParamField(
        float, "FreezeResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodDamageRate: float = ParamField(
        float, "BloodDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SuperArmorDamageRate: float = ParamField(
        float, "SuperArmorDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDamageRate: float = ParamField(
        float, "FreezeDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepResistRate: float = ParamField(
        float, "SleepResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessResistRate: float = ParamField(
        float, "MadnessResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDamageRate: float = ParamField(
        float, "SleepDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDamageRate: float = ParamField(
        float, "MadnessDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad1[4]")
