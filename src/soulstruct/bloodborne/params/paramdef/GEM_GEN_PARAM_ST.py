from __future__ import annotations

__all__ = ["GEM_GEN_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class GEM_GEN_PARAM_ST(ParamRow):
    IsUnique: bool = ParamField(
        uint32, "isUnique:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad_0[4]")
    GemNameIDOffset: int = ParamField(
        uint32, "gemNameIdOffset", default=0,
        tooltip="TODO",
    )
    DisableSlotModifyRate: bool = ParamField(
        uint32, "disableSlotRateModify:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    SlotTypeRateA: float = ParamField(
        float32, "slotTypeRateA", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateB: float = ParamField(
        float32, "slotTypeRateB", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateC: float = ParamField(
        float32, "slotTypeRateC", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateD: float = ParamField(
        float32, "slotTypeRateD", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateE: float = ParamField(
        float32, "slotTypeRateE", default=0.0,
        tooltip="TODO",
    )
    SlotTypeRateF: float = ParamField(
        float32, "slotTypeRateF", default=0.0,
        tooltip="TODO",
    )
    GemRankDoping: int = ParamField(
        int8, "gemRankDoping", default=0,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad_1[3]")
    GemEffectGenParamType0: int = ParamField(
        uint32, "gemeffectGenParamType_0", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam0: int = ParamField(
        int32, "gemeffectGenParam_0", default=-1,
        tooltip="TODO",
    )
    ManifestRate0: float = ParamField(
        float32, "manifestRate_0", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate0: float = ParamField(
        float32, "negativizeRate_0", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType1: int = ParamField(
        uint32, "gemeffectGenParamType_1", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam1: int = ParamField(
        int32, "gemeffectGenParam_1", default=-1,
        tooltip="TODO",
    )
    ManifestRate1: float = ParamField(
        float32, "manifestRate_1", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate1: float = ParamField(
        float32, "negativizeRate_1", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType2: int = ParamField(
        uint32, "gemeffectGenParamType_2", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam2: int = ParamField(
        int32, "gemeffectGenParam_2", default=-1,
        tooltip="TODO",
    )
    ManifestRate2: float = ParamField(
        float32, "manifestRate_2", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate2: float = ParamField(
        float32, "negativizeRate_2", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType3: int = ParamField(
        uint32, "gemeffectGenParamType_3", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam3: int = ParamField(
        int32, "gemeffectGenParam_3", default=-1,
        tooltip="TODO",
    )
    ManifestRate3: float = ParamField(
        float32, "manifestRate_3", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate3: float = ParamField(
        float32, "negativizeRate_3", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType4: int = ParamField(
        uint32, "gemeffectGenParamType_4", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam4: int = ParamField(
        int32, "gemeffectGenParam_4", default=-1,
        tooltip="TODO",
    )
    ManifestRate4: float = ParamField(
        float32, "manifestRate_4", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate4: float = ParamField(
        float32, "negativizeRate_4", default=0.0,
        tooltip="TODO",
    )
    GemEffectGenParamType5: int = ParamField(
        uint32, "gemeffectGenParamType_5", GEMEFFECT_GEN_PT, default=0,
        tooltip="TODO",
    )
    GemEffectGenParam5: int = ParamField(
        int32, "gemeffectGenParam_5", default=-1,
        tooltip="TODO",
    )
    ManifestRate5: float = ParamField(
        float32, "manifestRate_5", default=0.0,
        tooltip="TODO",
    )
    NegativizeRate5: float = ParamField(
        float32, "negativizeRate_5", default=0.0,
        tooltip="TODO",
    )
    IsRune: bool = ParamField(
        uint32, "equipableSegmentBody:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsBloodGem: bool = ParamField(
        uint32, "equipableSegmentWeapon:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    CannotRemove: bool = ParamField(
        uint32, "unremovable:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanDropToSummons: bool = ParamField(
        uint32, "isGuestDrop:1", EQUIP_GEN_PARAM_BOOL32, bit_count=1, default=False,
        tooltip="TODO",
    )
