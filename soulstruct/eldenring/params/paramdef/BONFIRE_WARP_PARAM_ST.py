from __future__ import annotations

__all__ = ["BONFIRE_WARP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class BONFIRE_WARP_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    EventflagId: int = ParamField(
        uint, "eventflagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireEntityId: int = ParamField(
        uint, "bonfireEntityId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad4[2]")
    BonfireSubCategorySortId: int = ParamField(
        ushort, "bonfireSubCategorySortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForbiddenIconId: int = ParamField(
        ushort, "forbiddenIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispMinZoomStep: int = ParamField(
        byte, "dispMinZoomStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SelectMinZoomStep: int = ParamField(
        byte, "selectMinZoomStep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BonfireSubCategoryId: int = ParamField(
        int, "bonfireSubCategoryId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ClearedEventFlagId: int = ParamField(
        uint, "clearedEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispMask00: bool = ParamField(
        byte, "dispMask00:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DispMask01: bool = ParamField(
        byte, "dispMask01:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad1:6", bit_count=6)
    _Pad2: bytes = ParamPad(1, "pad2[1]")
    AreaNo: int = ParamField(
        byte, "areaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNo: int = ParamField(
        byte, "gridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNo: int = ParamField(
        byte, "gridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad3[1]")
    PosX: float = ParamField(
        float, "posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosY: float = ParamField(
        float, "posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZ: float = ParamField(
        float, "posZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TextId1: int = ParamField(
        int, "textId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId1: int = ParamField(
        uint, "textEnableFlagId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId1: int = ParamField(
        uint, "textDisableFlagId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId2: int = ParamField(
        int, "textId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId2: int = ParamField(
        uint, "textEnableFlagId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId2: int = ParamField(
        uint, "textDisableFlagId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId3: int = ParamField(
        int, "textId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId3: int = ParamField(
        uint, "textEnableFlagId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId3: int = ParamField(
        uint, "textDisableFlagId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId4: int = ParamField(
        int, "textId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId4: int = ParamField(
        uint, "textEnableFlagId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId4: int = ParamField(
        uint, "textDisableFlagId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId5: int = ParamField(
        int, "textId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId5: int = ParamField(
        uint, "textEnableFlagId5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId5: int = ParamField(
        uint, "textDisableFlagId5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId6: int = ParamField(
        int, "textId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId6: int = ParamField(
        uint, "textEnableFlagId6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId6: int = ParamField(
        uint, "textDisableFlagId6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId7: int = ParamField(
        int, "textId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId7: int = ParamField(
        uint, "textEnableFlagId7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId7: int = ParamField(
        uint, "textDisableFlagId7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextId8: int = ParamField(
        int, "textId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlagId8: int = ParamField(
        uint, "textEnableFlagId8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlagId8: int = ParamField(
        uint, "textDisableFlagId8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType1: int = ParamField(
        byte, "textType1", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType2: int = ParamField(
        byte, "textType2", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType3: int = ParamField(
        byte, "textType3", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType4: int = ParamField(
        byte, "textType4", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType5: int = ParamField(
        byte, "textType5", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType6: int = ParamField(
        byte, "textType6", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType7: int = ParamField(
        byte, "textType7", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType8: int = ParamField(
        byte, "textType8", WORLD_MAP_POINT_TEXT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxDmypolyId0: int = ParamField(
        int, "noIgnitionSfxDmypolyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxId0: int = ParamField(
        int, "noIgnitionSfxId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxDmypolyId1: int = ParamField(
        int, "noIgnitionSfxDmypolyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoIgnitionSfxId1: int = ParamField(
        int, "noIgnitionSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UnkA8: int = ParamField(
        int, "unkA8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkAC: int = ParamField(
        int, "unkAC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkB0: int = ParamField(
        int, "unkB0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkB4: int = ParamField(
        int, "unkB4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkB8: int = ParamField(
        int, "unkB8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkBC: int = ParamField(
        int, "unkBC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkC0: int = ParamField(
        int, "unkC0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkC4: int = ParamField(
        int, "unkC4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkC8: int = ParamField(
        int, "unkC8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkCC: int = ParamField(
        int, "unkCC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkD0: int = ParamField(
        int, "unkD0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkD4: int = ParamField(
        int, "unkD4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkD8: int = ParamField(
        int, "unkD8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkDC: int = ParamField(
        int, "unkDC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkE0: int = ParamField(
        int, "unkE0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkE4: int = ParamField(
        int, "unkE4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkE8: int = ParamField(
        int, "unkE8", default=0,
        tooltip="TOOLTIP-TODO",
    )
