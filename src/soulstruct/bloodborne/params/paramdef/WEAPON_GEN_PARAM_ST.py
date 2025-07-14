from __future__ import annotations

__all__ = ["WEAPON_GEN_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class WEAPON_GEN_PARAM_ST(ParamRow):
    WeaponParamID: int = ParamField(
        int32, "wepParamId", game_type=WeaponParam, default=0,
        tooltip="TODO",
    )
    GemSlotType0: int = ParamField(
        uint32, "gemSlotType_0", GEM_SLOT_TYPE_MASK, default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID0: int = ParamField(
        int32, "gemGenId_0", default=-1,
        tooltip="TODO",
    )
    GemSlotType1: int = ParamField(
        uint32, "gemSlotType_1", GEM_SLOT_TYPE_MASK, default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID1: int = ParamField(
        int32, "gemGenId_1", default=-1,
        tooltip="TODO",
    )
    GemSlotType2: int = ParamField(
        uint32, "gemSlotType_2", GEM_SLOT_TYPE_MASK, default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID2: int = ParamField(
        int32, "gemGenId_2", default=-1,
        tooltip="TODO",
    )
    GemSlotType3: int = ParamField(
        uint32, "gemSlotType_3", GEM_SLOT_TYPE_MASK, default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID3: int = ParamField(
        int32, "gemGenId_3", default=-1,
        tooltip="TODO",
    )
    GemSlotType4: int = ParamField(
        uint32, "gemSlotType_4", GEM_SLOT_TYPE_MASK, default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID4: int = ParamField(
        int32, "gemGenId_4", default=-1,
        tooltip="TODO",
    )
    EquippableGemSegmentMask: int = ParamField(
        uint8, "equipableGemSegmentMask", GEM_SEGMENT_MASK, default=1,
        tooltip="TODO",
    )
    ReserveGemSlot0: int = ParamField(
        uint8, "reserveGemSlotNo_0", GEM_SLOT_TYPE_NO, default=0,
        tooltip="TODO",
    )
    ReserveGemSlot1: int = ParamField(
        uint8, "reserveGemSlotNo_1", GEM_SLOT_TYPE_NO, default=0,
        tooltip="TODO",
    )
    ReserveGemSlot2: int = ParamField(
        uint8, "reserveGemSlotNo_2", GEM_SLOT_TYPE_NO, default=0,
        tooltip="TODO",
    )
