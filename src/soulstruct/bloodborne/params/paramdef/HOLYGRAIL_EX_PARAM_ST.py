from __future__ import annotations

__all__ = ["HOLYGRAIL_EX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class HOLYGRAIL_EX_PARAM_ST(ParamRow):
    RitualLevel: int = ParamField(
        uint8, "ritualLv", default=0,
        tooltip="TODO",
    )
    AttributeID: int = ParamField(
        uint8, "attributeId", default=0,
        tooltip="TODO",
    )
    MapBaseID: int = ParamField(
        uint16, "mapBaseId", default=0,
        tooltip="TODO",
    )
    ChaliceTypeID: int = ParamField(
        uint8, "holygrailTypeId", default=0,
        tooltip="TODO",
    )
    Variation: int = ParamField(
        uint8, "variationNum", default=1,
        tooltip="TODO",
    )
    MainFeature1: int = ParamField(
        int8, "mainFeature_1", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad_0")
    DungeonNameBaseID: int = ParamField(
        uint32, "dungeonNameBaseId", default=0,
        tooltip="TODO",
    )
    UniqueBaseFlagID: int = ParamField(
        uint32, "uniqueBaseFlagId", game_type=Flag, default=0,
        tooltip="TODO",
    )
    UniqueItem0Head: int = ParamField(
        uint8, "uniqueItem00_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem0Tail: int = ParamField(
        uint8, "uniqueItem00_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem1Head: int = ParamField(
        uint8, "uniqueItem01_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem1Tail: int = ParamField(
        uint8, "uniqueItem01_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem2Head: int = ParamField(
        uint8, "uniqueItem02_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem2Tail: int = ParamField(
        uint8, "uniqueItem02_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem3Head: int = ParamField(
        uint8, "uniqueItem03_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem3Tail: int = ParamField(
        uint8, "uniqueItem03_tail", default=-1,
        tooltip="TODO",
    )
    DirectMapUID: int = ParamField(
        int32, "directMapUid", default=-1,
        tooltip="TODO",
    )
    RequiredMaterialID: int = ParamField(
        uint32, "requiredMaterialId", default=0,
        tooltip="TODO",
    )
    GroupFrameNameID: int = ParamField(
        uint32, "groupFrameNameId", default=0,
        tooltip="TODO",
    )
    UniqueItem4Head: int = ParamField(
        uint8, "uniqueItem04_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem4Tail: int = ParamField(
        uint8, "uniqueItem04_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem5Head: int = ParamField(
        uint8, "uniqueItem05_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem5Tail: int = ParamField(
        uint8, "uniqueItem05_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem6Head: int = ParamField(
        uint8, "uniqueItem06_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem6Tail: int = ParamField(
        uint8, "uniqueItem06_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem7Head: int = ParamField(
        uint8, "uniqueItem07_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem7Tail: int = ParamField(
        uint8, "uniqueItem07_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem8Head: int = ParamField(
        uint8, "uniqueItem08_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem8Tail: int = ParamField(
        uint8, "uniqueItem08_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem9Head: int = ParamField(
        uint8, "uniqueItem09_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem9Tail: int = ParamField(
        uint8, "uniqueItem09_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem10Head: int = ParamField(
        uint8, "uniqueItem10_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem10Tail: int = ParamField(
        uint8, "uniqueItem10_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem11Head: int = ParamField(
        uint8, "uniqueItem11_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem11Tail: int = ParamField(
        uint8, "uniqueItem11_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem12Head: int = ParamField(
        uint8, "uniqueItem12_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem12Tail: int = ParamField(
        uint8, "uniqueItem12_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem13Head: int = ParamField(
        uint8, "uniqueItem13_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem13Tail: int = ParamField(
        uint8, "uniqueItem13_tail", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID1: int = ParamField(
        int32, "fixedSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID2: int = ParamField(
        int32, "fixedSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID3: int = ParamField(
        int32, "fixedSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID4: int = ParamField(
        int32, "fixedSf_4_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID5: int = ParamField(
        int32, "fixedSf_5_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID1: int = ParamField(
        int32, "freeSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID2: int = ParamField(
        int32, "freeSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID3: int = ParamField(
        int32, "freeSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    UniqueItem14Head: int = ParamField(
        uint8, "uniqueItem14_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem14Tail: int = ParamField(
        uint8, "uniqueItem14_tail", default=-1,
        tooltip="TODO",
    )
    IsGenericChalice: int = ParamField(
        uint8, "isGenericHolygrail", default=0,
        tooltip="TODO",
    )
    ReleaseFlagIDOffset: int = ParamField(
        uint8, "releaseFlagIdOffset", default=-1,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad_3[24]")
    GroupSubFeatureLotID1: int = ParamField(
        int32, "groupSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID2: int = ParamField(
        int32, "groupSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID3: int = ParamField(
        int32, "groupSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID4: int = ParamField(
        int32, "groupSf_4_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID5: int = ParamField(
        int32, "groupSf_5_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
