from __future__ import annotations

__all__ = ["MULTI_ESTUS_FLASK_BONUS_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MULTI_ESTUS_FLASK_BONUS_PARAM_ST(ParamRow):
    Host: int = ParamField(
        byte, "host", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostNone: int = ParamField(
        byte, "WhiteGhost_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostUmbasa: int = ParamField(
        byte, "WhiteGhost_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostBerserker: int = ParamField(
        byte, "WhiteGhost_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneSign: int = ParamField(
        byte, "BlackGhost_None_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaSign: int = ParamField(
        byte, "BlackGhost_Umbasa_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerSign: int = ParamField(
        byte, "BlackGhost_Berserker_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneInvade: int = ParamField(
        byte, "BlackGhost_None_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaInvade: int = ParamField(
        byte, "BlackGhost_Umbasa_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerInvade: int = ParamField(
        byte, "BlackGhost_Berserker_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter1: int = ParamField(
        byte, "RedHunter1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter2: int = ParamField(
        byte, "RedHunter2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForest: int = ParamField(
        byte, "GuardianOfForest", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnor: int = ParamField(
        byte, "GuardianOfAnor", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: int = ParamField(
        byte, "BattleRoyal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonk: int = ParamField(
        byte, "YellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(48, "pad1[48]")
