from __future__ import annotations

__all__ = ["GEM_CATEGORY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class GEM_CATEGORY_PARAM_ST(ParamRow):
    SortID: int = ParamField(
        int32, "sortNo", default=0,
        tooltip="TODO",
    )
    ManifestRate: float = ParamField(
        float32, "manifestRate", default=0.0,
        tooltip="TODO",
    )
    DirectionalID: int = ParamField(
        int32, "directionalId", default=0,
        tooltip="TODO",
    )
    CategoryGroupID: int = ParamField(
        int32, "cateGroupId", default=0,
        tooltip="TODO",
    )
    ExcludeGroupID: int = ParamField(
        int32, "excludeGroupId", default=0,
        tooltip="TODO",
    )
    IsNegative: bool = ParamField(
        uint32, "isNegative:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeA: bool = ParamField(
        uint32, "enableSlotTypeA:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeB: bool = ParamField(
        uint32, "enableSlotTypeB:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeC: bool = ParamField(
        uint32, "enableSlotTypeC:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeD: bool = ParamField(
        uint32, "enableSlotTypeD:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeE: bool = ParamField(
        uint32, "enableSlotTypeE:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableSlotTypeF: bool = ParamField(
        uint32, "enableSlotTypeF:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    ChaliceTypeGroup: int = ParamField(
        uint32, "holygrailTypeGroup:7", bit_count=7, default=0,
        tooltip="TODO",
    )
    AffinityCategoryID0: int = ParamField(
        int32, "affinityCateId_0", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate0: float = ParamField(
        float32, "affinityModifyRate_0", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID1: int = ParamField(
        int32, "affinityCateId_1", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate1: float = ParamField(
        float32, "affinityModifyRate_1", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID2: int = ParamField(
        int32, "affinityCateId_2", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate2: float = ParamField(
        float32, "affinityModifyRate_2", default=1.0,
        tooltip="TODO",
    )
    AffinityCategoryID3: int = ParamField(
        int32, "affinityCateId_3", default=-1,
        tooltip="TODO",
    )
    AffinityModifyRate3: float = ParamField(
        float32, "affinityModifyRate_3", default=1.0,
        tooltip="TODO",
    )
