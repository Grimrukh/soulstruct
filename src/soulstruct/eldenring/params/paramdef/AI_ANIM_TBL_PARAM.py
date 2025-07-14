from __future__ import annotations

__all__ = ["AI_ANIM_TBL_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class AI_ANIM_TBL_PARAM(ParamRow):
    Atk0EzStateId: int = ParamField(
        uint16, "atk0_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1EzStateId: int = ParamField(
        uint16, "atk1_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2EzStateId: int = ParamField(
        uint16, "atk2_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3EzStateId: int = ParamField(
        uint16, "atk3_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4EzStateId: int = ParamField(
        uint16, "atk4_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5EzStateId: int = ParamField(
        uint16, "atk5_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6EzStateId: int = ParamField(
        uint16, "atk6_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7EzStateId: int = ParamField(
        uint16, "atk7_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8EzStateId: int = ParamField(
        uint16, "atk8_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9EzStateId: int = ParamField(
        uint16, "atk9_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10EzStateId: int = ParamField(
        uint16, "atk10_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11EzStateId: int = ParamField(
        uint16, "atk11_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12EzStateId: int = ParamField(
        uint16, "atk12_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13EzStateId: int = ParamField(
        uint16, "atk13_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14EzStateId: int = ParamField(
        uint16, "atk14_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15EzStateId: int = ParamField(
        uint16, "atk15_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16EzStateId: int = ParamField(
        uint16, "atk16_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17EzStateId: int = ParamField(
        uint16, "atk17_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18EzStateId: int = ParamField(
        uint16, "atk18_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19EzStateId: int = ParamField(
        uint16, "atk19_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20EzStateId: int = ParamField(
        uint16, "atk20_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21EzStateId: int = ParamField(
        uint16, "atk21_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22EzStateId: int = ParamField(
        uint16, "atk22_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23EzStateId: int = ParamField(
        uint16, "atk23_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24EzStateId: int = ParamField(
        uint16, "atk24_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25EzStateId: int = ParamField(
        uint16, "atk25_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26EzStateId: int = ParamField(
        uint16, "atk26_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27EzStateId: int = ParamField(
        uint16, "atk27_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28EzStateId: int = ParamField(
        uint16, "atk28_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29EzStateId: int = ParamField(
        uint16, "atk29_EzStateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0MinDist: int = ParamField(
        uint16, "atk0_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1MinDist: int = ParamField(
        uint16, "atk1_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2MinDist: int = ParamField(
        uint16, "atk2_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3MinDist: int = ParamField(
        uint16, "atk3_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4MinDist: int = ParamField(
        uint16, "atk4_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5MinDist: int = ParamField(
        uint16, "atk5_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6MinDist: int = ParamField(
        uint16, "atk6_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7MinDist: int = ParamField(
        uint16, "atk7_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8MinDist: int = ParamField(
        uint16, "atk8_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9MinDist: int = ParamField(
        uint16, "atk9_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10MinDist: int = ParamField(
        uint16, "atk10_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11MinDist: int = ParamField(
        uint16, "atk11_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12MinDist: int = ParamField(
        uint16, "atk12_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13MinDist: int = ParamField(
        uint16, "atk13_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14MinDist: int = ParamField(
        uint16, "atk14_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15MinDist: int = ParamField(
        uint16, "atk15_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16MinDist: int = ParamField(
        uint16, "atk16_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17MinDist: int = ParamField(
        uint16, "atk17_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18MinDist: int = ParamField(
        uint16, "atk18_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19MinDist: int = ParamField(
        uint16, "atk19_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20MinDist: int = ParamField(
        uint16, "atk20_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21MinDist: int = ParamField(
        uint16, "atk21_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22MinDist: int = ParamField(
        uint16, "atk22_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23MinDist: int = ParamField(
        uint16, "atk23_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24MinDist: int = ParamField(
        uint16, "atk24_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25MinDist: int = ParamField(
        uint16, "atk25_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26MinDist: int = ParamField(
        uint16, "atk26_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27MinDist: int = ParamField(
        uint16, "atk27_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28MinDist: int = ParamField(
        uint16, "atk28_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29MinDist: int = ParamField(
        uint16, "atk29_MinDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0MaxDist: int = ParamField(
        uint16, "atk0_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1MaxDist: int = ParamField(
        uint16, "atk1_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2MaxDist: int = ParamField(
        uint16, "atk2_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3MaxDist: int = ParamField(
        uint16, "atk3_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4MaxDist: int = ParamField(
        uint16, "atk4_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5MaxDist: int = ParamField(
        uint16, "atk5_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6MaxDist: int = ParamField(
        uint16, "atk6_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7MaxDist: int = ParamField(
        uint16, "atk7_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8MaxDist: int = ParamField(
        uint16, "atk8_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9MaxDist: int = ParamField(
        uint16, "atk9_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10MaxDist: int = ParamField(
        uint16, "atk10_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11MaxDist: int = ParamField(
        uint16, "atk11_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12MaxDist: int = ParamField(
        uint16, "atk12_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13MaxDist: int = ParamField(
        uint16, "atk13_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14MaxDist: int = ParamField(
        uint16, "atk14_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15MaxDist: int = ParamField(
        uint16, "atk15_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16MaxDist: int = ParamField(
        uint16, "atk16_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17MaxDist: int = ParamField(
        uint16, "atk17_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18MaxDist: int = ParamField(
        uint16, "atk18_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19MaxDist: int = ParamField(
        uint16, "atk19_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20MaxDist: int = ParamField(
        uint16, "atk20_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21MaxDist: int = ParamField(
        uint16, "atk21_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22MaxDist: int = ParamField(
        uint16, "atk22_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23MaxDist: int = ParamField(
        uint16, "atk23_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24MaxDist: int = ParamField(
        uint16, "atk24_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25MaxDist: int = ParamField(
        uint16, "atk25_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26MaxDist: int = ParamField(
        uint16, "atk26_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27MaxDist: int = ParamField(
        uint16, "atk27_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28MaxDist: int = ParamField(
        uint16, "atk28_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29MaxDist: int = ParamField(
        uint16, "atk29_MaxDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk0AtkDistType: int = ParamField(
        uint8, "atk0_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk1AtkDistType: int = ParamField(
        uint8, "atk1_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk2AtkDistType: int = ParamField(
        uint8, "atk2_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk3AtkDistType: int = ParamField(
        uint8, "atk3_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk4AtkDistType: int = ParamField(
        uint8, "atk4_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk5AtkDistType: int = ParamField(
        uint8, "atk5_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk6AtkDistType: int = ParamField(
        uint8, "atk6_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk7AtkDistType: int = ParamField(
        uint8, "atk7_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk8AtkDistType: int = ParamField(
        uint8, "atk8_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk9AtkDistType: int = ParamField(
        uint8, "atk9_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk10AtkDistType: int = ParamField(
        uint8, "atk10_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk11AtkDistType: int = ParamField(
        uint8, "atk11_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk12AtkDistType: int = ParamField(
        uint8, "atk12_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk13AtkDistType: int = ParamField(
        uint8, "atk13_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk14AtkDistType: int = ParamField(
        uint8, "atk14_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk15AtkDistType: int = ParamField(
        uint8, "atk15_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk16AtkDistType: int = ParamField(
        uint8, "atk16_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk17AtkDistType: int = ParamField(
        uint8, "atk17_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk18AtkDistType: int = ParamField(
        uint8, "atk18_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk19AtkDistType: int = ParamField(
        uint8, "atk19_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk20AtkDistType: int = ParamField(
        uint8, "atk20_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk21AtkDistType: int = ParamField(
        uint8, "atk21_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk22AtkDistType: int = ParamField(
        uint8, "atk22_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk23AtkDistType: int = ParamField(
        uint8, "atk23_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk24AtkDistType: int = ParamField(
        uint8, "atk24_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk25AtkDistType: int = ParamField(
        uint8, "atk25_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk26AtkDistType: int = ParamField(
        uint8, "atk26_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk27AtkDistType: int = ParamField(
        uint8, "atk27_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk28AtkDistType: int = ParamField(
        uint8, "atk28_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Atk29AtkDistType: int = ParamField(
        uint8, "atk29_AtkDistType:4", AI_ATK_DIST_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(13, "pad0[13]")
