from __future__ import annotations

__all__ = ["WEAPON_GEN_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WEAPON_GEN_PARAM_ST(ParamRowData):
    WeaponParamID: WeaponParam = ParamField(
        int, "wepParamId", default=0,
        tooltip="TODO",
    )
    GemSlotType0: GEM_SLOT_TYPE_MASK = ParamField(
        uint, "gemSlotType_0", default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID0: int = ParamField(
        int, "gemGenId_0", default=-1,
        tooltip="TODO",
    )
    GemSlotType1: GEM_SLOT_TYPE_MASK = ParamField(
        uint, "gemSlotType_1", default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID1: int = ParamField(
        int, "gemGenId_1", default=-1,
        tooltip="TODO",
    )
    GemSlotType2: GEM_SLOT_TYPE_MASK = ParamField(
        uint, "gemSlotType_2", default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID2: int = ParamField(
        int, "gemGenId_2", default=-1,
        tooltip="TODO",
    )
    GemSlotType3: GEM_SLOT_TYPE_MASK = ParamField(
        uint, "gemSlotType_3", default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID3: int = ParamField(
        int, "gemGenId_3", default=-1,
        tooltip="TODO",
    )
    GemSlotType4: GEM_SLOT_TYPE_MASK = ParamField(
        uint, "gemSlotType_4", default=2147483648,
        tooltip="TODO",
    )
    GemGeneratorID4: int = ParamField(
        int, "gemGenId_4", default=-1,
        tooltip="TODO",
    )
    EquippableGemSegmentMask: GEM_SEGMENT_MASK = ParamField(
        byte, "equipableGemSegmentMask", default=1,
        tooltip="TODO",
    )
    ReserveGemSlot0: GEM_SLOT_TYPE_NO = ParamField(
        byte, "reserveGemSlotNo_0", default=0,
        tooltip="TODO",
    )
    ReserveGemSlot1: GEM_SLOT_TYPE_NO = ParamField(
        byte, "reserveGemSlotNo_1", default=0,
        tooltip="TODO",
    )
    ReserveGemSlot2: GEM_SLOT_TYPE_NO = ParamField(
        byte, "reserveGemSlotNo_2", default=0,
        tooltip="TODO",
    )
