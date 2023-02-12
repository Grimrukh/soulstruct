from __future__ import annotations

__all__ = ["REINFORCE_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REINFORCE_PARAM_PROTECTOR_ST(ParamRowData):
    PhysicalDefenseMultiplier: float = ParamField(
        float, "physicsDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefenseMultiplier: float = ParamField(
        float, "magicDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireDefenseMultiplier: float = ParamField(
        float, "fireDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningDefenseMultiplier: float = ParamField(
        float, "thunderDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SlashDefenseMultiplier: float = ParamField(
        float, "slashDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    StrikeDefenseMultiplier: float = ParamField(
        float, "blowDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDefenseMultiplier: float = ParamField(
        float, "thrustDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoisonResistanceMultiplier: float = ParamField(
        float, "resistPoisonRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ToxicResistanceMultiplier: float = ParamField(
        float, "resistDiseaseRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BleedResistanceMultiplier: float = ParamField(
        float, "resistBloodRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistanceMultiplier: float = ParamField(
        float, "resistCurseRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect1: int = ParamField(
        byte, "residentSpEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect2: int = ParamField(
        byte, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect3: int = ParamField(
        byte, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeMaterialID: int = ParamField(
        byte, "materialSetId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDefRate: float = ParamField(
        float, "darkDefRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResistFreezeRate: float = ParamField(
        float, "resistFreezeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResistSleepRate: float = ParamField(
        float, "resistSleepRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResistMadnessRate: float = ParamField(
        float, "resistMadnessRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
