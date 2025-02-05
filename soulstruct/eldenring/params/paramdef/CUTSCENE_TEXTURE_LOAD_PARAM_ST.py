from __future__ import annotations

__all__ = ["CUTSCENE_TEXTURE_LOAD_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CUTSCENE_TEXTURE_LOAD_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        byte, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    TexName00: str = ParamField(
        str, "texName_00[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName01: str = ParamField(
        str, "texName_01[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName02: str = ParamField(
        str, "texName_02[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName03: str = ParamField(
        str, "texName_03[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName04: str = ParamField(
        str, "texName_04[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName05: str = ParamField(
        str, "texName_05[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName06: str = ParamField(
        str, "texName_06[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName07: str = ParamField(
        str, "texName_07[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName08: str = ParamField(
        str, "texName_08[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName09: str = ParamField(
        str, "texName_09[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName10: str = ParamField(
        str, "texName_10[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName11: str = ParamField(
        str, "texName_11[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName12: str = ParamField(
        str, "texName_12[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName13: str = ParamField(
        str, "texName_13[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName14: str = ParamField(
        str, "texName_14[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
    TexName15: str = ParamField(
        str, "texName_15[16]", encoding="shift_jis_2004", length=16, default='',
        tooltip="TOOLTIP-TODO",
    )
