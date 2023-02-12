from __future__ import annotations

__all__ = ["GEM_DROP_MODIFY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GEM_DROP_MODIFY_PARAM_ST(ParamRow):
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
    AffinityCategoryID0: int = ParamField(
        int, "affinityCateId_0", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate0: float = ParamField(
        float, "affinityModifyRate_0", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID1: int = ParamField(
        int, "affinityCateId_1", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate1: float = ParamField(
        float, "affinityModifyRate_1", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID2: int = ParamField(
        int, "affinityCateId_2", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate2: float = ParamField(
        float, "affinityModifyRate_2", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID3: int = ParamField(
        int, "affinityCateId_3", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate3: float = ParamField(
        float, "affinityModifyRate_3", default=1.0,
        tooltip="TODO",
    )
    ManifestRate0: float = ParamField(
        float, "manifestRate_0", default=0.0,
        tooltip="TODO",
    )
    ManifestRate1: float = ParamField(
        float, "manifestRate_1", default=0.0,
        tooltip="TODO",
    )
    ManifestRate2: float = ParamField(
        float, "manifestRate_2", default=0.0,
        tooltip="TODO",
    )
    ManifestRate3: float = ParamField(
        float, "manifestRate_3", default=0.0,
        tooltip="TODO",
    )
    ManifestRate4: float = ParamField(
        float, "manifestRate_4", default=0.0,
        tooltip="TODO",
    )
    ManifestRate5: float = ParamField(
        float, "manifestRate_5", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate0: float = ParamField(
        float, "negativizeRate_0", default=0.0,
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
