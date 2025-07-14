from __future__ import annotations

__all__ = ["WORLD_MAP_POINT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WORLD_MAP_POINT_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    EventFlagId: int = ParamField(
        uint, "eventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistViewEventFlagId: int = ParamField(
        uint, "distViewEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BgmPlaceType: int = ParamField(
        short, "bgmPlaceType", SOUND_BGM_MAP_PLACE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAreaIcon: bool = ParamField(
        byte, "isAreaIcon:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsOverrideDistViewMarkPos: bool = ParamField(
        byte, "isOverrideDistViewMarkPos:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableNoText: bool = ParamField(
        byte, "isEnableNoText:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad3:5", bit_count=5)
    AreaNoforDistViewMark: int = ParamField(
        byte, "areaNo_forDistViewMark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNoforDistViewMark: int = ParamField(
        byte, "gridXNo_forDistViewMark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNoforDistViewMark: int = ParamField(
        byte, "gridZNo_forDistViewMark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ClearedEventFlagId: int = ParamField(
        uint, "clearedEventFlagId", default=0,
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
    _BitPad2: int = ParamBitPad(byte, "pad2_0:6", bit_count=6)
    DispMask02: bool = ParamField(
        byte, "dispMask02:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad3: int = ParamBitPad(byte, "pad2_0:5", bit_count=5)
    _Pad1: bytes = ParamPad(1, "pad2[1]")
    DistViewIconId: int = ParamField(
        ushort, "distViewIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Angle: float = ParamField(
        float, "angle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
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
    _Pad2: bytes = ParamPad(1, "pad[1]")
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
    DistViewId: int = ParamField(
        int, "distViewId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PosXforDistViewMark: float = ParamField(
        float, "posX_forDistViewMark", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosYforDistViewMark: float = ParamField(
        float, "posY_forDistViewMark", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZforDistViewMark: float = ParamField(
        float, "posZ_forDistViewMark", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DistViewId1: int = ParamField(
        int, "distViewId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DistViewId2: int = ParamField(
        int, "distViewId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DistViewId3: int = ParamField(
        int, "distViewId3", default=-1,
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
    EntryFEType: int = ParamField(
        byte, "entryFEType", WORLD_MAP_ENTRY_FE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(9, "pad4_old[9]")
    Unknown0xb7: int = ParamField(
        byte, "unknown_0xb7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AltIconId: int = ParamField(
        ushort, "altIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(6, "pad4[6]")
    TextEnableFlag2Id1: int = ParamField(
        int, "textEnableFlag2Id1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id2: int = ParamField(
        int, "textEnableFlag2Id2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id3: int = ParamField(
        int, "textEnableFlag2Id3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id4: int = ParamField(
        int, "textEnableFlag2Id4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id5: int = ParamField(
        int, "textEnableFlag2Id5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id6: int = ParamField(
        int, "textEnableFlag2Id6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id7: int = ParamField(
        int, "textEnableFlag2Id7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextEnableFlag2Id8: int = ParamField(
        int, "textEnableFlag2Id8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id1: int = ParamField(
        int, "textDisableFlag2Id1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id2: int = ParamField(
        int, "textDisableFlag2Id2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id3: int = ParamField(
        int, "textDisableFlag2Id3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id4: int = ParamField(
        int, "textDisableFlag2Id4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id5: int = ParamField(
        int, "textDisableFlag2Id5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id6: int = ParamField(
        int, "textDisableFlag2Id6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id7: int = ParamField(
        int, "textDisableFlag2Id7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextDisableFlag2Id8: int = ParamField(
        int, "textDisableFlag2Id8", default=0,
        tooltip="TOOLTIP-TODO",
    )
