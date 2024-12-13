from __future__ import annotations

__all__ = ["GEM_GEN_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class GEM_GEN_PARAM_ST(ParamRow):
    IsUnique: bool = ParamField(
        uint, "isUnique:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad_0[4]")
    GemNameIDOffset: int = ParamField(
        uint, "gemNameIdOffset", default=0,
        tooltip="TODO",
    )
    DisableSlotModifyRate: bool = ParamField(
        uint, "disableSlotRateModify:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    SlotTypeRateA: float = ParamField(
        float, "slotTypeRateA", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateB: float = ParamField(
        float, "slotTypeRateB", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateC: float = ParamField(
        float, "slotTypeRateC", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateD: float = ParamField(
        float, "slotTypeRateD", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateE: float = ParamField(
        float, "slotTypeRateE", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateF: float = ParamField(
        float, "slotTypeRateF", default=0.0,
        tooltip="TODO",
    )
    GemRankDoping: int = ParamField(
        sbyte, "gemRankDoping", default=0,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad_1[3]")
    GemEffectGenParamType0: int = ParamField(
        uint, "gemeffectGenParamType_0", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam0: int = ParamField(
        int, "gemeffectGenParam_0", default=-1,
        tooltip="TODO",
    )
    ManifestRate0: float = ParamField(
        float, "manifestRate_0", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate0: float = ParamField(
        float, "negativizeRate_0", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType1: int = ParamField(
        uint, "gemeffectGenParamType_1", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam1: int = ParamField(
        int, "gemeffectGenParam_1", default=-1,
        tooltip="TODO",
    )
    ManifestRate1: float = ParamField(
        float, "manifestRate_1", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate1: float = ParamField(
        float, "negativizeRate_1", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType2: int = ParamField(
        uint, "gemeffectGenParamType_2", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam2: int = ParamField(
        int, "gemeffectGenParam_2", default=-1,
        tooltip="TODO",
    )
    ManifestRate2: float = ParamField(
        float, "manifestRate_2", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate2: float = ParamField(
        float, "negativizeRate_2", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType3: int = ParamField(
        uint, "gemeffectGenParamType_3", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam3: int = ParamField(
        int, "gemeffectGenParam_3", default=-1,
        tooltip="TODO",
    )
    ManifestRate3: float = ParamField(
        float, "manifestRate_3", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate3: float = ParamField(
        float, "negativizeRate_3", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType4: int = ParamField(
        uint, "gemeffectGenParamType_4", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam4: int = ParamField(
        int, "gemeffectGenParam_4", default=-1,
        tooltip="TODO",
    )
    ManifestRate4: float = ParamField(
        float, "manifestRate_4", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate4: float = ParamField(
        float, "negativizeRate_4", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType5: int = ParamField(
        uint, "gemeffectGenParamType_5", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam5: int = ParamField(
        int, "gemeffectGenParam_5", default=-1,
        tooltip="TODO",
    )
    ManifestRate5: float = ParamField(
        float, "manifestRate_5", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate5: float = ParamField(
        float, "negativizeRate_5", default=0.0,
        tooltip="TODO",
    )
    IsRune: bool = ParamField(
        uint, "equipableSegmentBody:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsBloodGem: bool = ParamField(
        uint, "equipableSegmentWeapon:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    CannotRemove: bool = ParamField(
        uint, "unremovable:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanDropToSummons: bool = ParamField(
        uint, "isGuestDrop:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
