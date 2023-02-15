from __future__ import annotations

__all__ = ["ENV_LIGHT_TEX_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ENV_LIGHT_TEX_BANK(ParamRow):
    isUse: int = ParamField(
        sbyte, "isUse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    autoUpdate: int = ParamField(
        sbyte, "autoUpdate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad_0[12]")
    invMulCol: int = ParamField(
        short, "invMulCol", default=100,
        tooltip="TOOLTIP-TODO",
    )
    resNameId_Dif0: int = ParamField(
        short, "resNameId_Dif0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Dif0: int = ParamField(
        short, "invMulCol_Dif0", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Dif0: float = ParamField(
        float, "sepcPow_Dif0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad_Dif0[8]")
    resNameId_Spc0: int = ParamField(
        short, "resNameId_Spc0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc0: int = ParamField(
        short, "invMulCol_Spc0", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc0: float = ParamField(
        float, "sepcPow_Spc0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "pad_Spc0[8]")
    resNameId_Spc1: int = ParamField(
        short, "resNameId_Spc1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc1: int = ParamField(
        short, "invMulCol_Spc1", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc1: float = ParamField(
        float, "sepcPow_Spc1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad_Spc1[8]")
    resNameId_Spc2: int = ParamField(
        short, "resNameId_Spc2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc2: int = ParamField(
        short, "invMulCol_Spc2", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc2: float = ParamField(
        float, "sepcPow_Spc2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(8, "pad_Spc2[8]")
    resNameId_Spc3: int = ParamField(
        short, "resNameId_Spc3", default=3,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc3: int = ParamField(
        short, "invMulCol_Spc3", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc3: float = ParamField(
        float, "sepcPow_Spc3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "pad_Spc3[8]")
    degRotX_00: int = ParamField(
        short, "degRotX_00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_00: int = ParamField(
        short, "degRotY_00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_00: int = ParamField(
        short, "colR_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_00: int = ParamField(
        short, "colG_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_00: int = ParamField(
        short, "colB_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_00: int = ParamField(
        short, "colA_00", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(4, "pad_00[4]")
    degRotX_01: int = ParamField(
        short, "degRotX_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_01: int = ParamField(
        short, "degRotY_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_01: int = ParamField(
        short, "colR_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_01: int = ParamField(
        short, "colG_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_01: int = ParamField(
        short, "colB_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_01: int = ParamField(
        short, "colA_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(4, "pad_01[4]")
    degRotX_02: int = ParamField(
        short, "degRotX_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_02: int = ParamField(
        short, "degRotY_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_02: int = ParamField(
        short, "colR_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_02: int = ParamField(
        short, "colG_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_02: int = ParamField(
        short, "colB_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_02: int = ParamField(
        short, "colA_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad8: bytes = ParamPad(4, "pad_02[4]")
    degRotX_03: int = ParamField(
        short, "degRotX_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_03: int = ParamField(
        short, "degRotY_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_03: int = ParamField(
        short, "colR_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_03: int = ParamField(
        short, "colG_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_03: int = ParamField(
        short, "colB_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_03: int = ParamField(
        short, "colA_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad9: bytes = ParamPad(4, "pad_03[4]")
    degRotX_04: int = ParamField(
        short, "degRotX_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_04: int = ParamField(
        short, "degRotY_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_04: int = ParamField(
        short, "colR_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_04: int = ParamField(
        short, "colG_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_04: int = ParamField(
        short, "colB_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_04: int = ParamField(
        short, "colA_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad10: bytes = ParamPad(4, "pad_04[4]")
    degRotX_05: int = ParamField(
        short, "degRotX_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_05: int = ParamField(
        short, "degRotY_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_05: int = ParamField(
        short, "colR_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_05: int = ParamField(
        short, "colG_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_05: int = ParamField(
        short, "colB_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_05: int = ParamField(
        short, "colA_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad11: bytes = ParamPad(4, "pad_05[4]")
    degRotX_06: int = ParamField(
        short, "degRotX_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_06: int = ParamField(
        short, "degRotY_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_06: int = ParamField(
        short, "colR_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_06: int = ParamField(
        short, "colG_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_06: int = ParamField(
        short, "colB_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_06: int = ParamField(
        short, "colA_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad12: bytes = ParamPad(4, "pad_06[4]")
    degRotX_07: int = ParamField(
        short, "degRotX_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_07: int = ParamField(
        short, "degRotY_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_07: int = ParamField(
        short, "colR_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_07: int = ParamField(
        short, "colG_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_07: int = ParamField(
        short, "colB_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_07: int = ParamField(
        short, "colA_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad13: bytes = ParamPad(4, "pad_07[4]")
    degRotX_08: int = ParamField(
        short, "degRotX_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_08: int = ParamField(
        short, "degRotY_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_08: int = ParamField(
        short, "colR_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_08: int = ParamField(
        short, "colG_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_08: int = ParamField(
        short, "colB_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_08: int = ParamField(
        short, "colA_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad14: bytes = ParamPad(4, "pad_08[4]")
    degRotX_09: int = ParamField(
        short, "degRotX_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_09: int = ParamField(
        short, "degRotY_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_09: int = ParamField(
        short, "colR_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_09: int = ParamField(
        short, "colG_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_09: int = ParamField(
        short, "colB_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_09: int = ParamField(
        short, "colA_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad15: bytes = ParamPad(4, "pad_09[4]")
