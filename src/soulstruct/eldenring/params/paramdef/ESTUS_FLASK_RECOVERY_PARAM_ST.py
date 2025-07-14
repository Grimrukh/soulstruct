from __future__ import annotations

__all__ = ["ESTUS_FLASK_RECOVERY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class ESTUS_FLASK_RECOVERY_PARAM_ST(ParamRow):
    Host: int = ParamField(
        uint8, "host", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbNone: int = ParamField(
        uint8, "invadeOrb_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbUmbasa: int = ParamField(
        uint8, "invadeOrb_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbBerserker: int = ParamField(
        uint8, "invadeOrb_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeOrbSinners: int = ParamField(
        uint8, "invadeOrb_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignNone: int = ParamField(
        uint8, "invadeSign_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignUmbasa: int = ParamField(
        uint8, "invadeSign_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignBerserker: int = ParamField(
        uint8, "invadeSign_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeSignSinners: int = ParamField(
        uint8, "invadeSign_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingSinners: int = ParamField(
        uint8, "invadeRing_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingRosalia: int = ParamField(
        uint8, "invadeRing_Rosalia", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingForest: int = ParamField(
        uint8, "invadeRing_Forest", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignNone: int = ParamField(
        uint8, "coopSign_None", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignUmbasa: int = ParamField(
        uint8, "coopSign_Umbasa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignBerserker: int = ParamField(
        uint8, "coopSign_Berserker", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopSignSinners: int = ParamField(
        uint8, "coopSign_Sinners", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CoopRingRedHunter: int = ParamField(
        uint8, "coopRing_RedHunter", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvadeRingAnor: int = ParamField(
        uint8, "invadeRing_Anor", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParamReplaceRate: int = ParamField(
        uint16, "paramReplaceRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParamReplaceId: int = ParamField(
        int32, "paramReplaceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
