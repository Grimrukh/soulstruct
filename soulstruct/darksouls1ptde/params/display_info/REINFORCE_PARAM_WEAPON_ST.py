from __future__ import annotations

__all__ = ["REINFORCE_PARAM_WEAPON_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *

REINFORCE_PARAM_WEAPON_ST = {
    "param_type": "REINFORCE_PARAM_WEAPON_ST",
    "file_name": "ReinforceParamWeapon",
    "nickname": "WeaponUpgrades",
    "fields": [
        ParamFieldInfo(
            "physicsAtkRate",
            "PhysicalDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing physical damage (of any type).",
        ),
        ParamFieldInfo(
            "magicAtkRate", "MagicDamageMultiplier", True, float, "Multiplier applied to outgoing magic damage."
        ),
        ParamFieldInfo(
            "fireAtkRate", "FireDamageMultiplier", True, float, "Multiplier applied to outgoing fire damage."
        ),
        ParamFieldInfo(
            "thunderAtkRate",
            "LightningDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing lightning damage.",
        ),
        ParamFieldInfo(
            "staminaAtkRate",
            "StaminaDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' stamina.",
        ),
        ParamFieldInfo(
            "saWeaponAtkRate",
            "PoiseDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' poise. Never used.",
        ),
        ParamFieldInfo(
            "saDurabilityRate",
            "PoiseDefenseMultiplier",
            True,
            float,
            "Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used.",
        ),
        ParamFieldInfo(
            "correctStrengthRate",
            "StrengthScalingMultiplier",
            True,
            float,
            "Multiplier applied to strength scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctAgilityRate",
            "DexterityScalingMultiplier",
            True,
            float,
            "Multiplier applied to dexterity scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctMagicRate",
            "IntelligenceScalingMultiplier",
            True,
            float,
            "Multiplier applied to intelligence scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctFaithRate",
            "FaithScalingMultiplier",
            True,
            float,
            "Multiplier applied to faith scaling of this weapon.",
        ),
        ParamFieldInfo(
            "physicsGuardCutRate",
            "PhysicalGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of physical damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "magicGuardCutRate",
            "MagicGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of magic damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "fireGuardCutRate",
            "FireGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of fire damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "thunderGuardCutRate",
            "LightningGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of lightning damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "poisonGuardResistRate",
            "PoisonGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of poison damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "diseaseGuardResistRate",
            "ToxicGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of toxic damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "bloodGuardResistRate",
            "BleedGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of bleed damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "curseGuardResistRate",
            "CurseGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of curse damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "staminaGuardDefRate",
            "StaminaGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of stamina damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "spEffectId1",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "spEffectId2",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "spEffectId3",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "residentSpEffectId1",
            "EquippedSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
            "parameters.",
        ),
        ParamFieldInfo(
            "residentSpEffectId2",
            "EquippedSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
            "parameters.",
        ),
        ParamFieldInfo(
            "residentSpEffectId3",
            "EquippedSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
            "parameters.",
        ),
        ParamFieldInfo(
            "materialSetId",
            "UpgradeMaterialOffset",
            True,
            int,
            "Value to be added to Upgrade Materials field in base weapon parameters.",
        ),
        ParamFieldInfo("pad[9]", "Pad1", False, pad_field(9), "Null padding."),
    ],
}
