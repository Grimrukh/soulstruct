from __future__ import annotations

__all__ = ["REINFORCE_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REINFORCE_PARAM_WEAPON_ST(ParamRow):
    PhysicsAtkRate: float = ParamField(
        float, "physicsAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAtkRate: float = ParamField(
        float, "magicAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireAtkRate: float = ParamField(
        float, "fireAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderAtkRate: float = ParamField(
        float, "thunderAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAtkRate: float = ParamField(
        float, "staminaAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaWeaponAtkRate: float = ParamField(
        float, "saWeaponAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaDurabilityRate: float = ParamField(
        float, "saDurabilityRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectStrengthRate: float = ParamField(
        float, "correctStrengthRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectAgilityRate: float = ParamField(
        float, "correctAgilityRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectMagicRate: float = ParamField(
        float, "correctMagicRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectFaithRate: float = ParamField(
        float, "correctFaithRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicsGuardCutRate: float = ParamField(
        float, "physicsGuardCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicGuardCutRate: float = ParamField(
        float, "magicGuardCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRate: float = ParamField(
        float, "fireGuardCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderGuardCutRate: float = ParamField(
        float, "thunderGuardCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResistRate: float = ParamField(
        float, "poisonGuardResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseGuardResistRate: float = ParamField(
        float, "diseaseGuardResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodGuardResistRate: float = ParamField(
        float, "bloodGuardResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResistRate: float = ParamField(
        float, "curseGuardResistRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDefRate: float = ParamField(
        float, "staminaGuardDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        byte, "spEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        byte, "spEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId3: int = ParamField(
        byte, "spEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId1: int = ParamField(
        byte, "residentSpEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId2: int = ParamField(
        byte, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId3: int = ParamField(
        byte, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSetId: int = ParamField(
        byte, "materialSetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxReinforceLevel: int = ParamField(
        byte, "maxReinforceLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkAtkRate: float = ParamField(
        float, "darkAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float, "darkGuardCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectLuckRate: float = ParamField(
        float, "correctLuckRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardDefRate: float = ParamField(
        float, "freezeGuardDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforcePriceRate: float = ParamField(
        float, "reinforcePriceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangePriceRate: float = ParamField(
        float, "baseChangePriceRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableGemRank: int = ParamField(
        sbyte, "enableGemRank", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad2[3]")
    SleepGuardDefRate: float = ParamField(
        float, "sleepGuardDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardDefRate: float = ParamField(
        float, "madnessGuardDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseAtkRate: float = ParamField(
        float, "baseAtkRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
