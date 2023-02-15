from __future__ import annotations

__all__ = ["ESTUS_FLASK_RECOVERY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ESTUS_FLASK_RECOVERY_PARAM_ST(ParamRow):
    Host: int = ParamField(
        byte, "host", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbNone: int = ParamField(
        byte, "invadeOrb_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbUmbasa: int = ParamField(
        byte, "invadeOrb_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbBerserker: int = ParamField(
        byte, "invadeOrb_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbSinners: int = ParamField(
        byte, "invadeOrb_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignNone: int = ParamField(
        byte, "invadeSign_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignUmbasa: int = ParamField(
        byte, "invadeSign_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignBerserker: int = ParamField(
        byte, "invadeSign_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignSinners: int = ParamField(
        byte, "invadeSign_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingSinners: int = ParamField(
        byte, "invadeRing_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingRosalia: int = ParamField(
        byte, "invadeRing_Rosalia", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingForest: int = ParamField(
        byte, "invadeRing_Forest", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignNone: int = ParamField(
        byte, "coopSign_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignUmbasa: int = ParamField(
        byte, "coopSign_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignBerserker: int = ParamField(
        byte, "coopSign_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignSinners: int = ParamField(
        byte, "coopSign_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopRingRedHunter: int = ParamField(
        byte, "coopRing_RedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingAnor: int = ParamField(
        byte, "invadeRing_Anor", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParamReplaceRate: int = ParamField(
        ushort, "paramReplaceRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParamReplaceId: int = ParamField(
        int, "paramReplaceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
