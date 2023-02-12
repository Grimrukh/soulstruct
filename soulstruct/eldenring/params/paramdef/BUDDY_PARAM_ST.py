from __future__ import annotations

__all__ = ["BUDDY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BUDDY_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
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
        byte, "appearOnAroundSekihi", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisablePCTargetShare: int = ParamField(
        byte, "disablePCTargetShare", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PcFollowType: int = ParamField(
        byte, "pcFollowType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "Reserve[1]")
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
    _Pad3: bytes = ParamPad(4, "Reserve2[4]")
