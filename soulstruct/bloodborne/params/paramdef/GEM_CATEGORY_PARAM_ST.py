from __future__ import annotations

__all__ = ["GEM_CATEGORY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GEM_CATEGORY_PARAM_ST(ParamRow):
    SortID: int = ParamField(
        int, "sortNo", default=0,
        tooltip="TODO",
    )
    ManifestRate: float = ParamField(
        float, "manifestRate", default=0.0,
        tooltip="TODO",
    )
    DirectionalID: int = ParamField(
        int, "directionalId", default=0,
        tooltip="TODO",
    )
    CategoryGroupID: int = ParamField(
        int, "cateGroupId", default=0,
        tooltip="TODO",
    )
    ExcludeGroupID: int = ParamField(
        int, "excludeGroupId", default=0,
        tooltip="TODO",
    )
    IsNegative: bool = ParamField(
        uint, "isNegative:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeA: bool = ParamField(
        uint, "enableSlotTypeA:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeB: bool = ParamField(
        uint, "enableSlotTypeB:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeC: bool = ParamField(
        uint, "enableSlotTypeC:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeD: bool = ParamField(
        uint, "enableSlotTypeD:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeE: bool = ParamField(
        uint, "enableSlotTypeE:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeF: bool = ParamField(
        uint, "enableSlotTypeF:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    ChaliceTypeGroup: int = ParamField(
        uint, "holygrailTypeGroup:7", bit_count=7, default=0,
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
