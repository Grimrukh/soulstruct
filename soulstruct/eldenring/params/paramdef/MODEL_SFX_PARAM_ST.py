from __future__ import annotations

__all__ = ["MODEL_SFX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MODEL_SFX_PARAM_ST(ParamRowData):
    SfxId0: int = ParamField(
        int, "sfxId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId0: int = ParamField(
        int, "dmypolyId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "reserve_0[8]")
    SfxId1: int = ParamField(
        int, "sfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId1: int = ParamField(
        int, "dmypolyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "reserve_1[8]")
    SfxId2: int = ParamField(
        int, "sfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId2: int = ParamField(
        int, "dmypolyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserve_2[8]")
    SfxId3: int = ParamField(
        int, "sfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId3: int = ParamField(
        int, "dmypolyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "reserve_3[8]")
    SfxId4: int = ParamField(
        int, "sfxId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId4: int = ParamField(
        int, "dmypolyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(8, "reserve_4[8]")
    SfxId5: int = ParamField(
        int, "sfxId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId5: int = ParamField(
        int, "dmypolyId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "reserve_5[8]")
    SfxId6: int = ParamField(
        int, "sfxId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId6: int = ParamField(
        int, "dmypolyId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(8, "reserve_6[8]")
    SfxId7: int = ParamField(
        int, "sfxId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DmypolyId7: int = ParamField(
        int, "dmypolyId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(8, "reserve_7[8]")
