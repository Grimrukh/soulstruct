from __future__ import annotations

__all__ = ["MULTI_ESTUS_FLASK_BONUS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MULTI_ESTUS_FLASK_BONUS_PARAM_ST(ParamRow):
    Host: int = ParamField(
        uint8, "host", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostNone: int = ParamField(
        uint8, "WhiteGhost_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostUmbasa: int = ParamField(
        uint8, "WhiteGhost_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostBerserker: int = ParamField(
        uint8, "WhiteGhost_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneSign: int = ParamField(
        uint8, "BlackGhost_None_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaSign: int = ParamField(
        uint8, "BlackGhost_Umbasa_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerSign: int = ParamField(
        uint8, "BlackGhost_Berserker_Sign", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneInvade: int = ParamField(
        uint8, "BlackGhost_None_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaInvade: int = ParamField(
        uint8, "BlackGhost_Umbasa_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerInvade: int = ParamField(
        uint8, "BlackGhost_Berserker_Invade", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter1: int = ParamField(
        uint8, "RedHunter1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter2: int = ParamField(
        uint8, "RedHunter2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForest: int = ParamField(
        uint8, "GuardianOfForest", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnor: int = ParamField(
        uint8, "GuardianOfAnor", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: int = ParamField(
        uint8, "BattleRoyal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonk: int = ParamField(
        uint8, "YellowMonk", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(48, "pad1[48]")
