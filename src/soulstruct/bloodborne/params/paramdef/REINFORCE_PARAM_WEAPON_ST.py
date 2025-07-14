from __future__ import annotations

__all__ = ["REINFORCE_PARAM_WEAPON_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class REINFORCE_PARAM_WEAPON_ST(ParamRow):
    PhysicalDamageMultiplier: float = ParamField(
        float32, "physicsAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing physical damage (of any type).",
    )
    MagicDamageMultiplier: float = ParamField(
        float32, "magicAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing magic damage.",
    )
    FireDamageMultiplier: float = ParamField(
        float32, "fireAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing fire damage.",
    )
    LightningDamageMultiplier: float = ParamField(
        float32, "thunderAtkRate", default=1.0,
        tooltip="Multiplier applied to outgoing lightning damage.",
    )
    StaminaDamageMultiplier: float = ParamField(
        float32, "staminaAtkRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' stamina.",
    )
    PoiseDamageMultiplier: float = ParamField(
        float32, "saWeaponAtkRate", default=1.0,
        tooltip="Multiplier applied to the amount of damage dealt to targets' poise. Never used.",
    )
    PoiseDefenseMultiplier: float = ParamField(
        float32, "saDurabilityRate", default=1.0,
        tooltip="Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used.",
    )
    StrengthScalingMultiplier: float = ParamField(
        float32, "correctStrengthRate", default=1.0,
        tooltip="Multiplier applied to strength scaling of this weapon.",
    )
    DexterityScalingMultiplier: float = ParamField(
        float32, "correctAgilityRate", default=1.0,
        tooltip="Multiplier applied to dexterity scaling of this weapon.",
    )
    IntelligenceScalingMultiplier: float = ParamField(
        float32, "correctMagicRate", default=1.0,
        tooltip="Multiplier applied to intelligence scaling of this weapon.",
    )
    FaithScalingMultiplier: float = ParamField(
        float32, "correctFaithRate", default=1.0,
        tooltip="Multiplier applied to faith scaling of this weapon.",
    )
    PhysicalGuardReductionMultiplier: float = ParamField(
        float32, "physicsGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of physical damage blocked by this weapon/shield.",
    )
    MagicGuardReductionMultiplier: float = ParamField(
        float32, "magicGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of magic damage blocked by this weapon/shield.",
    )
    FireGuardReductionMultiplier: float = ParamField(
        float32, "fireGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of fire damage blocked by this weapon/shield.",
    )
    LightningGuardReductionMultiplier: float = ParamField(
        float32, "thunderGuardCutRate", default=1.0,
        tooltip="Multiplier applied to the percentage of lightning damage blocked by this weapon/shield.",
    )
    PoisonGuardResistanceMultiplier: float = ParamField(
        float32, "poisonGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of poison damage blocked by this weapon/shield.",
    )
    ToxicGuardResistanceMultiplier: float = ParamField(
        float32, "diseaseGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of toxic damage blocked by this weapon/shield.",
    )
    BleedGuardResistanceMultiplier: float = ParamField(
        float32, "bloodGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of bleed damage blocked by this weapon/shield.",
    )
    CurseGuardResistanceMultiplier: float = ParamField(
        float32, "curseGuardResistRate", default=1.0,
        tooltip="Multiplier applied to the percentage of curse damage blocked by this weapon/shield.",
    )
    StaminaGuardReductionMultiplier: float = ParamField(
        float32, "staminaGuardDefRate", default=1.0,
        tooltip="Multiplier applied to the percentage of stamina damage blocked by this weapon/shield.",
    )
    SpecialEffectOnHit0: int = ParamField(
        uint8, "spEffectId1", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters.",
    )
    SpecialEffectOnHit1: int = ParamField(
        uint8, "spEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters.",
    )
    SpecialEffectOnHit2: int = ParamField(
        uint8, "spEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters.",
    )
    EquippedSpecialEffect0: int = ParamField(
        uint8, "residentSpEffectId1", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
                "parameters.",
    )
    EquippedSpecialEffect1: int = ParamField(
        uint8, "residentSpEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
                "parameters.",
    )
    EquippedSpecialEffect2: int = ParamField(
        uint8, "residentSpEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
                "parameters.",
    )
    UpgradeMaterialOffset: int = ParamField(
        uint8, "materialSetId", default=0,
        tooltip="Value to be added to Upgrade Materials field in base weapon parameters.",
    )
    _Pad0: bytes = ParamPad(9, "pad[9]")
