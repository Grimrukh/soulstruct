from __future__ import annotations

__all__ = ["MULTI_SOUL_BONUS_RATE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MULTI_SOUL_BONUS_RATE_PARAM_ST(ParamRow):
    Host: float = ParamField(
        float, "host", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostNone: float = ParamField(
        float, "WhiteGhost_None", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostUmbasa: float = ParamField(
        float, "WhiteGhost_Umbasa", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostBerserker: float = ParamField(
        float, "WhiteGhost_Berserker", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneSign: float = ParamField(
        float, "BlackGhost_None_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaSign: float = ParamField(
        float, "BlackGhost_Umbasa_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerSign: float = ParamField(
        float, "BlackGhost_Berserker_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneInvade: float = ParamField(
        float, "BlackGhost_None_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaInvade: float = ParamField(
        float, "BlackGhost_Umbasa_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerInvade: float = ParamField(
        float, "BlackGhost_Berserker_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter1: float = ParamField(
        float, "RedHunter1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter2: float = ParamField(
        float, "RedHunter2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForest: float = ParamField(
        float, "GuardianOfForest", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnor: float = ParamField(
        float, "GuardianOfAnor", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: float = ParamField(
        float, "BattleRoyal", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonk: float = ParamField(
        float, "YellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(64, "pad1[64]")
