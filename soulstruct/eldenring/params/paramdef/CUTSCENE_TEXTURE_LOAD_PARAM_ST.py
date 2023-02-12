from __future__ import annotations

__all__ = ["CUTSCENE_TEXTURE_LOAD_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_TEXTURE_LOAD_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: int = ParamField(
        byte, "disableParam_Debug:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:6")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    TexName00: bytes = ParamField(
        bytes, "texName_00[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName01: bytes = ParamField(
        bytes, "texName_01[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName02: bytes = ParamField(
        bytes, "texName_02[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName03: bytes = ParamField(
        bytes, "texName_03[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName04: bytes = ParamField(
        bytes, "texName_04[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName05: bytes = ParamField(
        bytes, "texName_05[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName06: bytes = ParamField(
        bytes, "texName_06[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName07: bytes = ParamField(
        bytes, "texName_07[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName08: bytes = ParamField(
        bytes, "texName_08[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName09: bytes = ParamField(
        bytes, "texName_09[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName10: bytes = ParamField(
        bytes, "texName_10[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName11: bytes = ParamField(
        bytes, "texName_11[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName12: bytes = ParamField(
        bytes, "texName_12[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName13: bytes = ParamField(
        bytes, "texName_13[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName14: bytes = ParamField(
        bytes, "texName_14[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName15: bytes = ParamField(
        bytes, "texName_15[16]", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
