from __future__ import annotations

__all__ = ["BONFIRE_WARP_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BONFIRE_WARP_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    EventflagId: int = ParamField(
        uint32, "eventflagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireEntityId: int = ParamField(
        uint32, "bonfireEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad4[2]")
    BonfireSubCategorySortId: int = ParamField(
        uint16, "bonfireSubCategorySortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForbiddenIconId: int = ParamField(
        uint16, "forbiddenIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispMinZoomStep: int = ParamField(
        uint8, "dispMinZoomStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelectMinZoomStep: int = ParamField(
        uint8, "selectMinZoomStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireSubCategoryId: int = ParamField(
        int32, "bonfireSubCategoryId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ClearedEventFlagId: int = ParamField(
        uint32, "clearedEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        uint16, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispMask00: bool = ParamField(
        uint8, "dispMask00:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispMask01: bool = ParamField(
        uint8, "dispMask01:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispMask02: bool = ParamField(
        uint8, "dispMask02:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad1:5", bit_count=5)
    _Pad2: bytes = ParamPad(1, "pad2[1]")
    AreaNo: int = ParamField(
        uint8, "areaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNo: int = ParamField(
        uint8, "gridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNo: int = ParamField(
        uint8, "gridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad3[1]")
    PosX: float = ParamField(
        float32, "posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosY: float = ParamField(
        float32, "posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZ: float = ParamField(
        float32, "posZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TextId1: int = ParamField(
        int32, "textId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId1: int = ParamField(
        uint32, "textEnableFlagId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId1: int = ParamField(
        uint32, "textDisableFlagId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId2: int = ParamField(
        int32, "textId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId2: int = ParamField(
        uint32, "textEnableFlagId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId2: int = ParamField(
        uint32, "textDisableFlagId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId3: int = ParamField(
        int32, "textId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId3: int = ParamField(
        uint32, "textEnableFlagId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId3: int = ParamField(
        uint32, "textDisableFlagId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId4: int = ParamField(
        int32, "textId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId4: int = ParamField(
        uint32, "textEnableFlagId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId4: int = ParamField(
        uint32, "textDisableFlagId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId5: int = ParamField(
        int32, "textId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId5: int = ParamField(
        uint32, "textEnableFlagId5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId5: int = ParamField(
        uint32, "textDisableFlagId5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId6: int = ParamField(
        int32, "textId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId6: int = ParamField(
        uint32, "textEnableFlagId6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId6: int = ParamField(
        uint32, "textDisableFlagId6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId7: int = ParamField(
        int32, "textId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId7: int = ParamField(
        uint32, "textEnableFlagId7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId7: int = ParamField(
        uint32, "textDisableFlagId7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId8: int = ParamField(
        int32, "textId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId8: int = ParamField(
        uint32, "textEnableFlagId8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId8: int = ParamField(
        uint32, "textDisableFlagId8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType1: int = ParamField(
        uint8, "textType1", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType2: int = ParamField(
        uint8, "textType2", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType3: int = ParamField(
        uint8, "textType3", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType4: int = ParamField(
        uint8, "textType4", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType5: int = ParamField(
        uint8, "textType5", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType6: int = ParamField(
        uint8, "textType6", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType7: int = ParamField(
        uint8, "textType7", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType8: int = ParamField(
        uint8, "textType8", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxDmypolyId0: int = ParamField(
        int32, "noIgnitionSfxDmypolyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxId0: int = ParamField(
        int32, "noIgnitionSfxId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxDmypolyId1: int = ParamField(
        int32, "noIgnitionSfxDmypolyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxId1: int = ParamField(
        int32, "noIgnitionSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id1: int = ParamField(
        int32, "textEnableFlag2Id1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id2: int = ParamField(
        int32, "textEnableFlag2Id2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id3: int = ParamField(
        int32, "textEnableFlag2Id3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id4: int = ParamField(
        int32, "textEnableFlag2Id4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id5: int = ParamField(
        int32, "textEnableFlag2Id5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id6: int = ParamField(
        int32, "textEnableFlag2Id6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id7: int = ParamField(
        int32, "textEnableFlag2Id7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id8: int = ParamField(
        int32, "textEnableFlag2Id8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id1: int = ParamField(
        int32, "textDisableFlag2Id1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id2: int = ParamField(
        int32, "textDisableFlag2Id2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id3: int = ParamField(
        int32, "textDisableFlag2Id3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id4: int = ParamField(
        int32, "textDisableFlag2Id4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id5: int = ParamField(
        int32, "textDisableFlag2Id5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id6: int = ParamField(
        int32, "textDisableFlag2Id6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id7: int = ParamField(
        int32, "textDisableFlag2Id7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id8: int = ParamField(
        int32, "textDisableFlag2Id8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AltIconId: int = ParamField(
        uint16, "altIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AltForbiddenIconId: int = ParamField(
        uint16, "altForbiddenIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
