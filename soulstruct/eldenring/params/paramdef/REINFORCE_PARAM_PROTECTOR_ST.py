from __future__ import annotations

__all__ = ["REINFORCE_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class REINFORCE_PARAM_PROTECTOR_ST(ParamRow):
    PhysicsDefRate: float = ParamField(
        float, "physicsDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefRate: float = ParamField(
        float, "magicDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDefRate: float = ParamField(
        float, "fireDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDefRate: float = ParamField(
        float, "thunderDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDefRate: float = ParamField(
        float, "slashDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowDefRate: float = ParamField(
        float, "blowDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDefRate: float = ParamField(
        float, "thrustDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistPoisonRate: float = ParamField(
        float, "resistPoisonRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistDiseaseRate: float = ParamField(
        float, "resistDiseaseRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistBloodRate: float = ParamField(
        float, "resistBloodRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurseRate: float = ParamField(
        float, "resistCurseRate", default=1.0,
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
    DarkDefRate: float = ParamField(
        float, "darkDefRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistFreezeRate: float = ParamField(
        float, "resistFreezeRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistSleepRate: float = ParamField(
        float, "resistSleepRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistMadnessRate: float = ParamField(
        float, "resistMadnessRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
