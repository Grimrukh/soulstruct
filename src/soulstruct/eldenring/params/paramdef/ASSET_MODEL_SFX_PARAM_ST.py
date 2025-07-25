from __future__ import annotations

__all__ = ["ASSET_MODEL_SFX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class ASSET_MODEL_SFX_PARAM_ST(ParamRow):
    SfxId0: int = ParamField(
        int32, "sfxId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId0: int = ParamField(
        int32, "dmypolyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "reserve_0[8]")
    SfxId1: int = ParamField(
        int32, "sfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId1: int = ParamField(
        int32, "dmypolyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "reserve_1[8]")
    SfxId2: int = ParamField(
        int32, "sfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId2: int = ParamField(
        int32, "dmypolyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserve_2[8]")
    SfxId3: int = ParamField(
        int32, "sfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId3: int = ParamField(
        int32, "dmypolyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "reserve_3[8]")
    SfxId4: int = ParamField(
        int32, "sfxId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId4: int = ParamField(
        int32, "dmypolyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(8, "reserve_4[8]")
    SfxId5: int = ParamField(
        int32, "sfxId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId5: int = ParamField(
        int32, "dmypolyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "reserve_5[8]")
    SfxId6: int = ParamField(
        int32, "sfxId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId6: int = ParamField(
        int32, "dmypolyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(8, "reserve_6[8]")
    SfxId7: int = ParamField(
        int32, "sfxId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId7: int = ParamField(
        int32, "dmypolyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableIV: int = ParamField(
        uint8, "isDisableIV", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(7, "reserve_7[7]")
