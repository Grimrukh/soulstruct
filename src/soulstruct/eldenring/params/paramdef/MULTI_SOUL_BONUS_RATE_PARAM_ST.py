from __future__ import annotations

__all__ = ["MULTI_SOUL_BONUS_RATE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MULTI_SOUL_BONUS_RATE_PARAM_ST(ParamRow):
    Host: float = ParamField(
        float32, "host", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostNone: float = ParamField(
        float32, "WhiteGhost_None", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostUmbasa: float = ParamField(
        float32, "WhiteGhost_Umbasa", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteGhostBerserker: float = ParamField(
        float32, "WhiteGhost_Berserker", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneSign: float = ParamField(
        float32, "BlackGhost_None_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaSign: float = ParamField(
        float32, "BlackGhost_Umbasa_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerSign: float = ParamField(
        float32, "BlackGhost_Berserker_Sign", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostNoneInvade: float = ParamField(
        float32, "BlackGhost_None_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostUmbasaInvade: float = ParamField(
        float32, "BlackGhost_Umbasa_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackGhostBerserkerInvade: float = ParamField(
        float32, "BlackGhost_Berserker_Invade", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter1: float = ParamField(
        float32, "RedHunter1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedHunter2: float = ParamField(
        float32, "RedHunter2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForest: float = ParamField(
        float32, "GuardianOfForest", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnor: float = ParamField(
        float32, "GuardianOfAnor", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: float = ParamField(
        float32, "BattleRoyal", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonk: float = ParamField(
        float32, "YellowMonk", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(64, "pad1[64]")
