from __future__ import annotations

__all__ = ["REINFORCE_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REINFORCE_PARAM_WEAPON_ST(ParamRow):
    PhysicalDamageMultiplier: float = ParamField(
        float, "physicsAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing physical damage (of any type).",
    )
    MagicDamageMultiplier: float = ParamField(
        float, "magicAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing magic damage.",
    )
    FireDamageMultiplier: float = ParamField(
        float, "fireAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing fire damage.",
    )
    LightningDamageMultiplier: float = ParamField(
        float, "thunderAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing lightning damage.",
    )
    StaminaDamageMultiplier: float = ParamField(
        float, "staminaAtkRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' stamina.",
    )
    PoiseDamageMultiplier: float = ParamField(
        float, "saWeaponAtkRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' poise. Never used.",
    )
    PoiseDefenseMultiplier: float = ParamField(
        float, "saDurabilityRate", default=1.0,
        tooltip="Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used.",
    )
    StrengthScalingMultiplier: float = ParamField(
        float, "correctStrengthRate", default=1.0,
        tooltip="Multiplier applied to strength scaling of this weapon.",
    )
    DexterityScalingMultiplier: float = ParamField(
        float, "correctAgilityRate", default=1.0,
        tooltip="Multiplier applied to dexterity scaling of this weapon.",
    )
    IntelligenceScalingMultiplier: float = ParamField(
        float, "correctMagicRate", default=1.0,
        tooltip="Multiplier applied to intelligence scaling of this weapon.",
    )
    FaithScalingMultiplier: float = ParamField(
        float, "correctFaithRate", default=1.0,
        tooltip="Multiplier applied to faith scaling of this weapon.",
    )
    PhysicalGuardReductionMultiplier: float = ParamField(
        float, "physicsGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of physical damage blocked by this weapon/shield.",
    )
    MagicGuardReductionMultiplier: float = ParamField(
        float, "magicGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of magic damage blocked by this weapon/shield.",
    )
    FireGuardReductionMultiplier: float = ParamField(
        float, "fireGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of fire damage blocked by this weapon/shield.",
    )
    LightningGuardReductionMultiplier: float = ParamField(
        float, "thunderGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of lightning damage blocked by this weapon/shield.",
    )
    PoisonGuardResistanceMultiplier: float = ParamField(
        float, "poisonGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of poison damage blocked by this weapon/shield.",
    )
    ToxicGuardResistanceMultiplier: float = ParamField(
        float, "diseaseGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of toxic damage blocked by this weapon/shield.",
    )
    BleedGuardResistanceMultiplier: float = ParamField(
        float, "bloodGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of bleed damage blocked by this weapon/shield.",
    )
    CurseGuardResistanceMultiplier: float = ParamField(
        float, "curseGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of curse damage blocked by this weapon/shield.",
    )
    StaminaGuardReductionMultiplier: float = ParamField(
        float, "staminaGuardDefRate", default=1.0,
        tooltip="Multiplier applied to the percentage of stamina damage blocked by this weapon/shield.",
    )
    SpecialEffectOnHit0: int = ParamField(
        byte, "spEffectId1", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters.",
    )
    SpecialEffectOnHit1: int = ParamField(
        byte, "spEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters.",
    )
    SpecialEffectOnHit2: int = ParamField(
        byte, "spEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters.",
    )
    EquippedSpecialEffect0: int = ParamField(
        byte, "residentSpEffectId1", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
                "parameters.",
    )
    EquippedSpecialEffect1: int = ParamField(
        byte, "residentSpEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
                "parameters.",
    )
    EquippedSpecialEffect2: int = ParamField(
        byte, "residentSpEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
                "parameters.",
    )
    UpgradeMaterialOffset: int = ParamField(
        byte, "materialSetId", game_type=UpgradeMaterialParam, default=0,
        tooltip="Value to be added to Upgrade Materials field in base weapon parameters.",
    )
    _Pad0: bytes = ParamPad(9, "pad[9]")
