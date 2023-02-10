from __future__ import annotations

__all__ = ["REINFORCE_PARAM_PROTECTOR_ST"]

from soulstruct.base.params.utils import ParamFieldInfo
from soulstruct.darksouls1ptde.game_types import *


REINFORCE_PARAM_PROTECTOR_ST = {
    "param_type": "REINFORCE_PARAM_PROTECTOR_ST",
    "file_name": "ReinforceParamProtector",
    "nickname": "ArmorUpgrades",
    "fields": [
        ParamFieldInfo(
            "physicsDefRate",
            "PhysicalDefenseMultiplier",
            True,
            float,
            "Multiplier for physical defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "magicDefRate",
            "MagicDefenseMultiplier",
            True,
            float,
            "Multiplier for magic defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "fireDefRate",
            "FireDefenseMultiplier",
            True,
            float,
            "Multiplier for fire defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "thunderDefRate",
            "LightningDefenseMultiplier",
            True,
            float,
            "Multiplier for lightning defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "slashDefRate",
            "SlashDefenseMultiplier",
            True,
            float,
            "Multiplier for slash defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "blowDefRate",
            "StrikeDefenseMultiplier",
            True,
            float,
            "Multiplier for strike defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "thrustDefRate",
            "ThrustDefenseMultiplier",
            True,
            float,
            "Multiplier for thrust defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistPoisonRate",
            "PoisonResistanceMultiplier",
            True,
            float,
            "Multiplier for poison resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistDiseaseRate",
            "ToxicResistanceMultiplier",
            True,
            float,
            "Multiplier for toxic resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistBloodRate",
            "BleedResistanceMultiplier",
            True,
            float,
            "Multiplier for bleed resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistCurseRate",
            "CurseResistanceMultiplier",
            True,
            float,
            "Multiplier for curse resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "residentSpEffectId1",
            "WearerSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (first of three).",
        ),
        ParamFieldInfo(
            "residentSpEffectId2",
            "WearerSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (second of three).",
        ),
        ParamFieldInfo(
            "residentSpEffectId3",
            "WearerSpecialEffect3",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (third of three).",
        ),
        ParamFieldInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade material set for reinforcement.",
        ),
    ],
}
