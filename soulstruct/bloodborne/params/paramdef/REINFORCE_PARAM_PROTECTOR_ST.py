from __future__ import annotations

__all__ = ["REINFORCE_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class REINFORCE_PARAM_PROTECTOR_ST(ParamRow):
    PhysicalDefenseMultiplier: float = ParamField(
        float, "physicsDefRate", default=1.0,
        tooltip="Multiplier for physical defense at this upgrade level.",
    )
    MagicDefenseMultiplier: float = ParamField(
        float, "magicDefRate", default=1.0,
        tooltip="Multiplier for magic defense at this upgrade level.",
    )
    FireDefenseMultiplier: float = ParamField(
        float, "fireDefRate", default=1.0,
        tooltip="Multiplier for fire defense at this upgrade level.",
    )
    LightningDefenseMultiplier: float = ParamField(
        float, "thunderDefRate", default=1.0,
        tooltip="Multiplier for lightning defense at this upgrade level.",
    )
    SlashDefenseMultiplier: float = ParamField(
        float, "slashDefRate", default=1.0,
        tooltip="Multiplier for slash defense at this upgrade level.",
    )
    StrikeDefenseMultiplier: float = ParamField(
        float, "blowDefRate", default=1.0,
        tooltip="Multiplier for strike defense at this upgrade level.",
    )
    ThrustDefenseMultiplier: float = ParamField(
        float, "thrustDefRate", default=1.0,
        tooltip="Multiplier for thrust defense at this upgrade level.",
    )
    PoisonResistanceMultiplier: float = ParamField(
        float, "resistPoisonRate", default=1.0,
        tooltip="Multiplier for poison resistance at this upgrade level.",
    )
    ToxicResistanceMultiplier: float = ParamField(
        float, "resistDiseaseRate", default=1.0,
        tooltip="Multiplier for toxic resistance at this upgrade level.",
    )
    BleedResistanceMultiplier: float = ParamField(
        float, "resistBloodRate", default=1.0,
        tooltip="Multiplier for bleed resistance at this upgrade level.",
    )
    CurseResistanceMultiplier: float = ParamField(
        float, "resistCurseRate", default=1.0,
        tooltip="Multiplier for curse resistance at this upgrade level.",
    )
    WearerSpecialEffect1: int = ParamField(
        byte, "residentSpEffectId1", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (first of three).",
    )
    WearerSpecialEffect2: int = ParamField(
        byte, "residentSpEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (second of three).",
    )
    WearerSpecialEffect3: int = ParamField(
        byte, "residentSpEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (third of three).",
    )
    UpgradeMaterialID: int = ParamField(
        byte, "materialSetId", game_type=UpgradeMaterialParam, default=0,
        tooltip="Upgrade material set for reinforcement.",
    )
