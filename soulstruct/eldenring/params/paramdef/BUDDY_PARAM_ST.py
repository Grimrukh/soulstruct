from __future__ import annotations

__all__ = ["BUDDY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BUDDY_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    TriggerSpEffectId: int = ParamField(
        int, "triggerSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcParamId: int = ParamField(
        int, "npcParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcThinkParamId: int = ParamField(
        int, "npcThinkParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcParamIdridden: int = ParamField(
        int, "npcParamId_ridden", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcThinkParamIdridden: int = ParamField(
        int, "npcThinkParamId_ridden", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Xoffset: float = ParamField(
        float, "x_offset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Zoffset: float = ParamField(
        float, "z_offset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Yangle: float = ParamField(
        float, "y_angle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AppearOnAroundSekihi: int = ParamField(
        byte, "appearOnAroundSekihi", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisablePCTargetShare: int = ParamField(
        byte, "disablePCTargetShare", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcFollowType: int = ParamField(
        byte, "pcFollowType", BUDDY_PC_FOLLOW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "Reserve[1]")
    DopingSpEffectlv0: int = ParamField(
        int, "dopingSpEffect_lv0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv1: int = ParamField(
        int, "dopingSpEffect_lv1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv2: int = ParamField(
        int, "dopingSpEffect_lv2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv3: int = ParamField(
        int, "dopingSpEffect_lv3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv4: int = ParamField(
        int, "dopingSpEffect_lv4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv5: int = ParamField(
        int, "dopingSpEffect_lv5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv6: int = ParamField(
        int, "dopingSpEffect_lv6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv7: int = ParamField(
        int, "dopingSpEffect_lv7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv8: int = ParamField(
        int, "dopingSpEffect_lv8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv9: int = ParamField(
        int, "dopingSpEffect_lv9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DopingSpEffectlv10: int = ParamField(
        int, "dopingSpEffect_lv10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerInitParamId: int = ParamField(
        int, "npcPlayerInitParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GenerateAnimId: int = ParamField(
        int, "generateAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Unk1: int = ParamField(
        uint, "Unk1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk2: int = ParamField(
        uint, "Unk2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk3: int = ParamField(
        int, "Unk3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk4: int = ParamField(
        int, "Unk4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk5: int = ParamField(
        int, "Unk5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk6: int = ParamField(
        int, "Unk6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk7: int = ParamField(
        int, "Unk7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk8: int = ParamField(
        int, "Unk8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk9: int = ParamField(
        int, "Unk9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk10: int = ParamField(
        int, "Unk10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk11: int = ParamField(
        uint, "Unk11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk12: int = ParamField(
        int, "Unk12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk13: int = ParamField(
        int, "Unk13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk14: int = ParamField(
        int, "Unk14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk15: int = ParamField(
        int, "Unk15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk16: int = ParamField(
        int, "Unk16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk17: int = ParamField(
        uint, "Unk17", default=0,
        tooltip="TOOLTIP-TODO",
    )
