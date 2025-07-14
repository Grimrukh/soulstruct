from __future__ import annotations

__all__ = ["CLEAR_COUNT_CORRECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CLEAR_COUNT_CORRECT_PARAM_ST(ParamRow):
    MaxHpRate: float = ParamField(
        float32, "MaxHpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxMpRate: float = ParamField(
        float32, "MaxMpRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxStaminaRate: float = ParamField(
        float32, "MaxStaminaRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsAttackRate: float = ParamField(
        float32, "PhysicsAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashAttackRate: float = ParamField(
        float32, "SlashAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowAttackRate: float = ParamField(
        float32, "BlowAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustAttackRate: float = ParamField(
        float32, "ThrustAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    NeturalAttackRate: float = ParamField(
        float32, "NeturalAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackRate: float = ParamField(
        float32, "MagicAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackRate: float = ParamField(
        float32, "FireAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAttackRate: float = ParamField(
        float32, "ThunderAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAttackRate: float = ParamField(
        float32, "DarkAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsDefenseRate: float = ParamField(
        float32, "PhysicsDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefenseRate: float = ParamField(
        float32, "MagicDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDefenseRate: float = ParamField(
        float32, "FireDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDefenseRate: float = ParamField(
        float32, "ThunderDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDefenseRate: float = ParamField(
        float32, "DarkDefenseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAttackRate: float = ParamField(
        float32, "StaminaAttackRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulRate: float = ParamField(
        float32, "SoulRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisionResistRate: float = ParamField(
        float32, "PoisionResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseResistRate: float = ParamField(
        float32, "DiseaseResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodResistRate: float = ParamField(
        float32, "BloodResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistRate: float = ParamField(
        float32, "CurseResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeResistRate: float = ParamField(
        float32, "FreezeResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodDamageRate: float = ParamField(
        float32, "BloodDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SuperArmorDamageRate: float = ParamField(
        float32, "SuperArmorDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeDamageRate: float = ParamField(
        float32, "FreezeDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepResistRate: float = ParamField(
        float32, "SleepResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessResistRate: float = ParamField(
        float32, "MadnessResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepDamageRate: float = ParamField(
        float32, "SleepDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessDamageRate: float = ParamField(
        float32, "MadnessDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad1[4]")
