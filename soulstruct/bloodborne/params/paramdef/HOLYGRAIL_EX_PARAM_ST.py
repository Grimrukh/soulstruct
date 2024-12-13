from __future__ import annotations

__all__ = ["HOLYGRAIL_EX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class HOLYGRAIL_EX_PARAM_ST(ParamRow):
    RitualLevel: int = ParamField(
        byte, "ritualLv", default=0,
        tooltip="TODO",
    )
    AttributeID: int = ParamField(
        byte, "attributeId", default=0,
        tooltip="TODO",
    )
    MapBaseID: int = ParamField(
        ushort, "mapBaseId", default=0,
        tooltip="TODO",
    )
    ChaliceTypeID: int = ParamField(
        byte, "holygrailTypeId", default=0,
        tooltip="TODO",
    )
    Variation: int = ParamField(
        byte, "variationNum", default=1,
        tooltip="TODO",
    )
    MainFeature1: int = ParamField(
        sbyte, "mainFeature_1", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad_0")
    DungeonNameBaseID: int = ParamField(
        uint, "dungeonNameBaseId", default=0,
        tooltip="TODO",
    )
    UniqueBaseFlagID: int = ParamField(
        uint, "uniqueBaseFlagId", game_type=Flag, default=0,
        tooltip="TODO",
    )
    UniqueItem0Head: int = ParamField(
        byte, "uniqueItem00_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem0Tail: int = ParamField(
        byte, "uniqueItem00_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem1Head: int = ParamField(
        byte, "uniqueItem01_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem1Tail: int = ParamField(
        byte, "uniqueItem01_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem2Head: int = ParamField(
        byte, "uniqueItem02_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem2Tail: int = ParamField(
        byte, "uniqueItem02_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem3Head: int = ParamField(
        byte, "uniqueItem03_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem3Tail: int = ParamField(
        byte, "uniqueItem03_tail", default=-1,
        tooltip="TODO",
    )
    DirectMapUID: int = ParamField(
        int, "directMapUid", default=-1,
        tooltip="TODO",
    )
    RequiredMaterialID: int = ParamField(
        uint, "requiredMaterialId", default=0,
        tooltip="TODO",
    )
    GroupFrameNameID: int = ParamField(
        uint, "groupFrameNameId", default=0,
        tooltip="TODO",
    )
    UniqueItem4Head: int = ParamField(
        byte, "uniqueItem04_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem4Tail: int = ParamField(
        byte, "uniqueItem04_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem5Head: int = ParamField(
        byte, "uniqueItem05_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem5Tail: int = ParamField(
        byte, "uniqueItem05_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem6Head: int = ParamField(
        byte, "uniqueItem06_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem6Tail: int = ParamField(
        byte, "uniqueItem06_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem7Head: int = ParamField(
        byte, "uniqueItem07_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem7Tail: int = ParamField(
        byte, "uniqueItem07_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem8Head: int = ParamField(
        byte, "uniqueItem08_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem8Tail: int = ParamField(
        byte, "uniqueItem08_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem9Head: int = ParamField(
        byte, "uniqueItem09_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem9Tail: int = ParamField(
        byte, "uniqueItem09_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem10Head: int = ParamField(
        byte, "uniqueItem10_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem10Tail: int = ParamField(
        byte, "uniqueItem10_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem11Head: int = ParamField(
        byte, "uniqueItem11_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem11Tail: int = ParamField(
        byte, "uniqueItem11_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem12Head: int = ParamField(
        byte, "uniqueItem12_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem12Tail: int = ParamField(
        byte, "uniqueItem12_tail", default=-1,
        tooltip="TODO",
    )
    UniqueItem13Head: int = ParamField(
        byte, "uniqueItem13_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem13Tail: int = ParamField(
        byte, "uniqueItem13_tail", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID1: int = ParamField(
        int, "fixedSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID2: int = ParamField(
        int, "fixedSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID3: int = ParamField(
        int, "fixedSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID4: int = ParamField(
        int, "fixedSf_4_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FixedSubFeatureLotID5: int = ParamField(
        int, "fixedSf_5_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID1: int = ParamField(
        int, "freeSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID2: int = ParamField(
        int, "freeSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    FreeSubFeatureLotID3: int = ParamField(
        int, "freeSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    UniqueItem14Head: int = ParamField(
        byte, "uniqueItem14_head", default=-1,
        tooltip="TODO",
    )
    UniqueItem14Tail: int = ParamField(
        byte, "uniqueItem14_tail", default=-1,
        tooltip="TODO",
    )
    IsGenericChalice: int = ParamField(
        byte, "isGenericHolygrail", default=0,
        tooltip="TODO",
    )
    ReleaseFlagIDOffset: int = ParamField(
        byte, "releaseFlagIdOffset", default=-1,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad_3[24]")
    GroupSubFeatureLotID1: int = ParamField(
        int, "groupSf_1_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID2: int = ParamField(
        int, "groupSf_2_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID3: int = ParamField(
        int, "groupSf_3_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID4: int = ParamField(
        int, "groupSf_4_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
    GroupSubFeatureLotID5: int = ParamField(
        int, "groupSf_5_subFeatureLotId", default=-1,
        tooltip="TODO",
    )
