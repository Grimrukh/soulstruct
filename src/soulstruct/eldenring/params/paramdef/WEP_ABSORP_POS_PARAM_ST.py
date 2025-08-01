from __future__ import annotations

__all__ = ["WEP_ABSORP_POS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WEP_ABSORP_POS_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    HangPosType: int = ParamField(
        uint8, "hangPosType", WEP_HANG_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkeletonBind: int = ParamField(
        uint8, "isSkeletonBind", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad0[2]")
    Right0: int = ParamField(
        int16, "right_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Left0: int = ParamField(
        int16, "left_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Both0: int = ParamField(
        int16, "both_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftHang0: int = ParamField(
        int16, "leftHang_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHang0: int = ParamField(
        int16, "rightHang_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Right1: int = ParamField(
        int16, "right_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Left1: int = ParamField(
        int16, "left_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Both1: int = ParamField(
        int16, "both_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftHang1: int = ParamField(
        int16, "leftHang_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHang1: int = ParamField(
        int16, "rightHang_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Right2: int = ParamField(
        int16, "right_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Left2: int = ParamField(
        int16, "left_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Both2: int = ParamField(
        int16, "both_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftHang2: int = ParamField(
        int16, "leftHang_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHang2: int = ParamField(
        int16, "rightHang_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Right3: int = ParamField(
        int16, "right_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Left3: int = ParamField(
        int16, "left_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Both3: int = ParamField(
        int16, "both_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftHang3: int = ParamField(
        int16, "leftHang_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHang3: int = ParamField(
        int16, "rightHang_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepInvisibleType0: int = ParamField(
        uint8, "wepInvisibleType_0", WEP_INVISIBLE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepInvisibleType1: int = ParamField(
        uint8, "wepInvisibleType_1", WEP_INVISIBLE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepInvisibleType2: int = ParamField(
        uint8, "wepInvisibleType_2", WEP_INVISIBLE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepInvisibleType3: int = ParamField(
        uint8, "wepInvisibleType_3", WEP_INVISIBLE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftBoth0: int = ParamField(
        int16, "leftBoth_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftBoth1: int = ParamField(
        int16, "leftBoth_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftBoth2: int = ParamField(
        int16, "leftBoth_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftBoth3: int = ParamField(
        int16, "leftBoth_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperight0: int = ParamField(
        uint8, "dispPosType_right_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleft0: int = ParamField(
        uint8, "dispPosType_left_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightBoth0: int = ParamField(
        uint8, "dispPosType_rightBoth_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftBoth0: int = ParamField(
        uint8, "dispPosType_leftBoth_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightHang0: int = ParamField(
        uint8, "dispPosType_rightHang_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftHang0: int = ParamField(
        uint8, "dispPosType_leftHang_0", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperight1: int = ParamField(
        uint8, "dispPosType_right_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleft1: int = ParamField(
        uint8, "dispPosType_left_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightBoth1: int = ParamField(
        uint8, "dispPosType_rightBoth_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftBoth1: int = ParamField(
        uint8, "dispPosType_leftBoth_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightHang1: int = ParamField(
        uint8, "dispPosType_rightHang_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftHang1: int = ParamField(
        uint8, "dispPosType_leftHang_1", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperight2: int = ParamField(
        uint8, "dispPosType_right_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleft2: int = ParamField(
        uint8, "dispPosType_left_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightBoth2: int = ParamField(
        uint8, "dispPosType_rightBoth_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftBoth2: int = ParamField(
        uint8, "dispPosType_leftBoth_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightHang2: int = ParamField(
        uint8, "dispPosType_rightHang_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftHang2: int = ParamField(
        uint8, "dispPosType_leftHang_2", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperight3: int = ParamField(
        uint8, "dispPosType_right_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleft3: int = ParamField(
        uint8, "dispPosType_left_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightBoth3: int = ParamField(
        uint8, "dispPosType_rightBoth_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftBoth3: int = ParamField(
        uint8, "dispPosType_leftBoth_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTyperightHang3: int = ParamField(
        uint8, "dispPosType_rightHang_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispPosTypeleftHang3: int = ParamField(
        uint8, "dispPosType_leftHang_3", WEP_DISP_POS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x54: int = ParamField(
        int8, "unknown_0x54", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x55: int = ParamField(
        int8, "unknown_0x55", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x56: int = ParamField(
        int8, "unknown_0x56", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x57: int = ParamField(
        int8, "unknown_0x57", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserve[8]")
