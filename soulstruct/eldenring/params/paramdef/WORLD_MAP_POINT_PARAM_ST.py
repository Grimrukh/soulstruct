from __future__ import annotations

__all__ = ["WORLD_MAP_POINT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WORLD_MAP_POINT_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
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
        short, "bgmPlaceType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAreaIcon: int = ParamField(
        byte, "isAreaIcon:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsOverrideDistViewMarkPos: int = ParamField(
        byte, "isOverrideDistViewMarkPos:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableNoText: int = ParamField(
        byte, "isEnableNoText:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3:5")
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
    DispMask00: int = ParamField(
        byte, "dispMask00:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DispMask01: int = ParamField(
        byte, "dispMask01:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad2_0:6")
    _Pad4: bytes = ParamPad(1, "pad2[1]")
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
    _Pad5: bytes = ParamPad(1, "pad[1]")
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
        byte, "textType1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType2: int = ParamField(
        byte, "textType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType3: int = ParamField(
        byte, "textType3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType4: int = ParamField(
        byte, "textType4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType5: int = ParamField(
        byte, "textType5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType6: int = ParamField(
        byte, "textType6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType7: int = ParamField(
        byte, "textType7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TextType8: int = ParamField(
        byte, "textType8", default=0,
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
        byte, "entryFEType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(9, "pad4[9]")
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
    UnkEC: int = ParamField(
        int, "unkEC", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkF0: int = ParamField(
        int, "unkF0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkF4: int = ParamField(
        int, "unkF4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkF8: int = ParamField(
        int, "unkF8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkFC: int = ParamField(
        int, "unkFC", default=0,
        tooltip="TOOLTIP-TODO",
    )
