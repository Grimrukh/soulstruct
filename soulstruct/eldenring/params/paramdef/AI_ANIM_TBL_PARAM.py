from __future__ import annotations

__all__ = ["AI_ANIM_TBL_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_ANIM_TBL_PARAM(ParamRow):
    Atk0EzStateId: int = ParamField(
        ushort, "atk0_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1EzStateId: int = ParamField(
        ushort, "atk1_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2EzStateId: int = ParamField(
        ushort, "atk2_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3EzStateId: int = ParamField(
        ushort, "atk3_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4EzStateId: int = ParamField(
        ushort, "atk4_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5EzStateId: int = ParamField(
        ushort, "atk5_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6EzStateId: int = ParamField(
        ushort, "atk6_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7EzStateId: int = ParamField(
        ushort, "atk7_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8EzStateId: int = ParamField(
        ushort, "atk8_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9EzStateId: int = ParamField(
        ushort, "atk9_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10EzStateId: int = ParamField(
        ushort, "atk10_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11EzStateId: int = ParamField(
        ushort, "atk11_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12EzStateId: int = ParamField(
        ushort, "atk12_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13EzStateId: int = ParamField(
        ushort, "atk13_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14EzStateId: int = ParamField(
        ushort, "atk14_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15EzStateId: int = ParamField(
        ushort, "atk15_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16EzStateId: int = ParamField(
        ushort, "atk16_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17EzStateId: int = ParamField(
        ushort, "atk17_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18EzStateId: int = ParamField(
        ushort, "atk18_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19EzStateId: int = ParamField(
        ushort, "atk19_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20EzStateId: int = ParamField(
        ushort, "atk20_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21EzStateId: int = ParamField(
        ushort, "atk21_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22EzStateId: int = ParamField(
        ushort, "atk22_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23EzStateId: int = ParamField(
        ushort, "atk23_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24EzStateId: int = ParamField(
        ushort, "atk24_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25EzStateId: int = ParamField(
        ushort, "atk25_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26EzStateId: int = ParamField(
        ushort, "atk26_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27EzStateId: int = ParamField(
        ushort, "atk27_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28EzStateId: int = ParamField(
        ushort, "atk28_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29EzStateId: int = ParamField(
        ushort, "atk29_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0MinDist: int = ParamField(
        ushort, "atk0_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1MinDist: int = ParamField(
        ushort, "atk1_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2MinDist: int = ParamField(
        ushort, "atk2_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3MinDist: int = ParamField(
        ushort, "atk3_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4MinDist: int = ParamField(
        ushort, "atk4_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5MinDist: int = ParamField(
        ushort, "atk5_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6MinDist: int = ParamField(
        ushort, "atk6_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7MinDist: int = ParamField(
        ushort, "atk7_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8MinDist: int = ParamField(
        ushort, "atk8_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9MinDist: int = ParamField(
        ushort, "atk9_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10MinDist: int = ParamField(
        ushort, "atk10_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11MinDist: int = ParamField(
        ushort, "atk11_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12MinDist: int = ParamField(
        ushort, "atk12_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13MinDist: int = ParamField(
        ushort, "atk13_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14MinDist: int = ParamField(
        ushort, "atk14_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15MinDist: int = ParamField(
        ushort, "atk15_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16MinDist: int = ParamField(
        ushort, "atk16_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17MinDist: int = ParamField(
        ushort, "atk17_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18MinDist: int = ParamField(
        ushort, "atk18_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19MinDist: int = ParamField(
        ushort, "atk19_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20MinDist: int = ParamField(
        ushort, "atk20_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21MinDist: int = ParamField(
        ushort, "atk21_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22MinDist: int = ParamField(
        ushort, "atk22_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23MinDist: int = ParamField(
        ushort, "atk23_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24MinDist: int = ParamField(
        ushort, "atk24_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25MinDist: int = ParamField(
        ushort, "atk25_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26MinDist: int = ParamField(
        ushort, "atk26_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27MinDist: int = ParamField(
        ushort, "atk27_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28MinDist: int = ParamField(
        ushort, "atk28_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29MinDist: int = ParamField(
        ushort, "atk29_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0MaxDist: int = ParamField(
        ushort, "atk0_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1MaxDist: int = ParamField(
        ushort, "atk1_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2MaxDist: int = ParamField(
        ushort, "atk2_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3MaxDist: int = ParamField(
        ushort, "atk3_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4MaxDist: int = ParamField(
        ushort, "atk4_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5MaxDist: int = ParamField(
        ushort, "atk5_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6MaxDist: int = ParamField(
        ushort, "atk6_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7MaxDist: int = ParamField(
        ushort, "atk7_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8MaxDist: int = ParamField(
        ushort, "atk8_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9MaxDist: int = ParamField(
        ushort, "atk9_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10MaxDist: int = ParamField(
        ushort, "atk10_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11MaxDist: int = ParamField(
        ushort, "atk11_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12MaxDist: int = ParamField(
        ushort, "atk12_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13MaxDist: int = ParamField(
        ushort, "atk13_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14MaxDist: int = ParamField(
        ushort, "atk14_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15MaxDist: int = ParamField(
        ushort, "atk15_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16MaxDist: int = ParamField(
        ushort, "atk16_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17MaxDist: int = ParamField(
        ushort, "atk17_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18MaxDist: int = ParamField(
        ushort, "atk18_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19MaxDist: int = ParamField(
        ushort, "atk19_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20MaxDist: int = ParamField(
        ushort, "atk20_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21MaxDist: int = ParamField(
        ushort, "atk21_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22MaxDist: int = ParamField(
        ushort, "atk22_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23MaxDist: int = ParamField(
        ushort, "atk23_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24MaxDist: int = ParamField(
        ushort, "atk24_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25MaxDist: int = ParamField(
        ushort, "atk25_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26MaxDist: int = ParamField(
        ushort, "atk26_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27MaxDist: int = ParamField(
        ushort, "atk27_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28MaxDist: int = ParamField(
        ushort, "atk28_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29MaxDist: int = ParamField(
        ushort, "atk29_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0AtkDistType: int = ParamField(
        byte, "atk0_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1AtkDistType: int = ParamField(
        byte, "atk1_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2AtkDistType: int = ParamField(
        byte, "atk2_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3AtkDistType: int = ParamField(
        byte, "atk3_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4AtkDistType: int = ParamField(
        byte, "atk4_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5AtkDistType: int = ParamField(
        byte, "atk5_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6AtkDistType: int = ParamField(
        byte, "atk6_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7AtkDistType: int = ParamField(
        byte, "atk7_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8AtkDistType: int = ParamField(
        byte, "atk8_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9AtkDistType: int = ParamField(
        byte, "atk9_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10AtkDistType: int = ParamField(
        byte, "atk10_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11AtkDistType: int = ParamField(
        byte, "atk11_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12AtkDistType: int = ParamField(
        byte, "atk12_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13AtkDistType: int = ParamField(
        byte, "atk13_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14AtkDistType: int = ParamField(
        byte, "atk14_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15AtkDistType: int = ParamField(
        byte, "atk15_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16AtkDistType: int = ParamField(
        byte, "atk16_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17AtkDistType: int = ParamField(
        byte, "atk17_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18AtkDistType: int = ParamField(
        byte, "atk18_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19AtkDistType: int = ParamField(
        byte, "atk19_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20AtkDistType: int = ParamField(
        byte, "atk20_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21AtkDistType: int = ParamField(
        byte, "atk21_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22AtkDistType: int = ParamField(
        byte, "atk22_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23AtkDistType: int = ParamField(
        byte, "atk23_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24AtkDistType: int = ParamField(
        byte, "atk24_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25AtkDistType: int = ParamField(
        byte, "atk25_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26AtkDistType: int = ParamField(
        byte, "atk26_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27AtkDistType: int = ParamField(
        byte, "atk27_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28AtkDistType: int = ParamField(
        byte, "atk28_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29AtkDistType: int = ParamField(
        byte, "atk29_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(13, "pad0[13]")
