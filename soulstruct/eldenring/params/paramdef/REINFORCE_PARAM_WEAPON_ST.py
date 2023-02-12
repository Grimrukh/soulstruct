from __future__ import annotations

__all__ = ["REINFORCE_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REINFORCE_PARAM_WEAPON_ST(ParamRowData):
    PhysicalDamageMultiplier: float = ParamField(
        float, "physicsAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageMultiplier: float = ParamField(
        float, "magicAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageMultiplier: float = ParamField(
        float, "fireAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningDamageMultiplier: float = ParamField(
        float, "thunderAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    StaminaDamageMultiplier: float = ParamField(
        float, "staminaAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoiseDamageMultiplier: float = ParamField(
        float, "saWeaponAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoiseDefenseMultiplier: float = ParamField(
        float, "saDurabilityRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    StrengthScalingMultiplier: float = ParamField(
        float, "correctStrengthRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DexterityScalingMultiplier: float = ParamField(
        float, "correctAgilityRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IntelligenceScalingMultiplier: float = ParamField(
        float, "correctMagicRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FaithScalingMultiplier: float = ParamField(
        float, "correctFaithRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalGuardReductionMultiplier: float = ParamField(
        float, "physicsGuardCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicGuardReductionMultiplier: float = ParamField(
        float, "magicGuardCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardReductionMultiplier: float = ParamField(
        float, "fireGuardCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningGuardReductionMultiplier: float = ParamField(
        float, "thunderGuardCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResistanceMultiplier: float = ParamField(
        float, "poisonGuardResistRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ToxicGuardResistanceMultiplier: float = ParamField(
        float, "diseaseGuardResistRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BleedGuardResistanceMultiplier: float = ParamField(
        float, "bloodGuardResistRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResistanceMultiplier: float = ParamField(
        float, "curseGuardResistRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardReductionMultiplier: float = ParamField(
        float, "staminaGuardDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit0: int = ParamField(
        byte, "spEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit1: int = ParamField(
        byte, "spEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit2: int = ParamField(
        byte, "spEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect0: int = ParamField(
        byte, "residentSpEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect1: int = ParamField(
        byte, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect2: int = ParamField(
        byte, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeMaterialOffset: int = ParamField(
        byte, "materialSetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxReinforceLevel: int = ParamField(
        byte, "maxReinforceLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAtkRate: float = ParamField(
        float, "darkAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float, "darkGuardCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CorrectLuckRate: float = ParamField(
        float, "correctLuckRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardDefRate: float = ParamField(
        float, "freezeGuardDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforcePriceRate: float = ParamField(
        float, "reinforcePriceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangePriceRate: float = ParamField(
        float, "baseChangePriceRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableGemRank: int = ParamField(
        sbyte, "enableGemRank", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad2[3]")
    SleepGuardDefRate: float = ParamField(
        float, "sleepGuardDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardDefRate: float = ParamField(
        float, "madnessGuardDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BaseAtkRate: float = ParamField(
        float, "baseAtkRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
