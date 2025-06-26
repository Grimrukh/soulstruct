from __future__ import annotations

__all__ = ["GEM_DROP_DOPING_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class GEM_DROP_DOPING_PARAM_ST(ParamRow):
    MinimumRank: int = ParamField(
        int, "rankMin", default=0,
        tooltip="TODO",
    )
    MaximumRank: int = ParamField(
        int, "rankMax", default=0,
        tooltip="TODO",
    )
    NormalDistributionMean: int = ParamField(
        int, "normalDistributionAve", default=0,
        tooltip="TODO",
    )
    NormalDistributionSigma: int = ParamField(
        int, "normalDistributionSigma", default=1,
        tooltip="TODO",
    )
    SlotTypeRateA: float = ParamField(
        float, "slotTypeRateA", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateB: float = ParamField(
        float, "slotTypeRateB", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateC: float = ParamField(
        float, "slotTypeRateC", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateD: float = ParamField(
        float, "slotTypeRateD", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateE: float = ParamField(
        float, "slotTypeRateE", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateF: float = ParamField(
        float, "slotTypeRateF", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate0: float = ParamField(
        float, "directionalIdRate_0", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate1: float = ParamField(
        float, "directionalIdRate_1", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate2: float = ParamField(
        float, "directionalIdRate_2", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate3: float = ParamField(
        float, "directionalIdRate_3", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate4: float = ParamField(
        float, "directionalIdRate_4", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate5: float = ParamField(
        float, "directionalIdRate_5", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate6: float = ParamField(
        float, "directionalIdRate_6", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate7: float = ParamField(
        float, "directionalIdRate_7", default=1.0,
        tooltip="TODO",
    )
