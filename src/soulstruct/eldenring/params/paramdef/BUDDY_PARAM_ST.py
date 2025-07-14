from __future__ import annotations

__all__ = ["BUDDY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BUDDY_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    TriggerSpEffectId: int = ParamField(
        int32, "triggerSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcParamId: int = ParamField(
        int32, "npcParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcThinkParamId: int = ParamField(
        int32, "npcThinkParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcParamIdridden: int = ParamField(
        int32, "npcParamId_ridden", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcThinkParamIdridden: int = ParamField(
        int32, "npcThinkParamId_ridden", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Xoffset: float = ParamField(
        float32, "x_offset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Zoffset: float = ParamField(
        float32, "z_offset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Yangle: float = ParamField(
        float32, "y_angle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AppearOnAroundSekihi: int = ParamField(
        uint8, "appearOnAroundSekihi", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisablePCTargetShare: int = ParamField(
        uint8, "disablePCTargetShare", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcFollowType: int = ParamField(
        uint8, "pcFollowType", BUDDY_PC_FOLLOW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "Reserve[1]")
    DopingSpEffectlv0: int = ParamField(
        int32, "dopingSpEffect_lv0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv1: int = ParamField(
        int32, "dopingSpEffect_lv1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv2: int = ParamField(
        int32, "dopingSpEffect_lv2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv3: int = ParamField(
        int32, "dopingSpEffect_lv3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv4: int = ParamField(
        int32, "dopingSpEffect_lv4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv5: int = ParamField(
        int32, "dopingSpEffect_lv5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv6: int = ParamField(
        int32, "dopingSpEffect_lv6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv7: int = ParamField(
        int32, "dopingSpEffect_lv7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv8: int = ParamField(
        int32, "dopingSpEffect_lv8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv9: int = ParamField(
        int32, "dopingSpEffect_lv9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv10: int = ParamField(
        int32, "dopingSpEffect_lv10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerInitParamId: int = ParamField(
        int32, "npcPlayerInitParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GenerateAnimId: int = ParamField(
        int32, "generateAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "Reserve2[4]")
    Unknown0x5c: int = ParamField(
        uint32, "unknown_0x5c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x60: int = ParamField(
        uint32, "unknown_0x60", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x64: int = ParamField(
        int32, "unknown_0x64", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x68: int = ParamField(
        int32, "unknown_0x68", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x6c: int = ParamField(
        int32, "unknown_0x6c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x70: int = ParamField(
        int32, "unknown_0x70", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x74: int = ParamField(
        int32, "unknown_0x74", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x78: int = ParamField(
        int32, "unknown_0x78", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x7c: int = ParamField(
        int32, "unknown_0x7c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x80: int = ParamField(
        int32, "unknown_0x80", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x84: int = ParamField(
        uint32, "unknown_0x84", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x88: int = ParamField(
        int32, "unknown_0x88", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x8c: int = ParamField(
        int32, "unknown_0x8c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x90: int = ParamField(
        int32, "unknown_0x90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x94: int = ParamField(
        int32, "unknown_0x94", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x98: int = ParamField(
        int32, "unknown_0x98", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x9c: int = ParamField(
        uint32, "unknown_0x9c", default=0,
        tooltip="TOOLTIP-TODO",
    )
