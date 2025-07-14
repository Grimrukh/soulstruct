from __future__ import annotations

__all__ = ["ENV_LIGHT_TEX_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class ENV_LIGHT_TEX_BANK(ParamRow):
    isUse: int = ParamField(
        int8, "isUse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    autoUpdate: int = ParamField(
        int8, "autoUpdate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad_0[12]")
    invMulCol: int = ParamField(
        int16, "invMulCol", default=100,
        tooltip="TOOLTIP-TODO",
    )
    resNameId_Dif0: int = ParamField(
        int16, "resNameId_Dif0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Dif0: int = ParamField(
        int16, "invMulCol_Dif0", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Dif0: float = ParamField(
        float32, "sepcPow_Dif0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad_Dif0[8]")
    resNameId_Spc0: int = ParamField(
        int16, "resNameId_Spc0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc0: int = ParamField(
        int16, "invMulCol_Spc0", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc0: float = ParamField(
        float32, "sepcPow_Spc0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "pad_Spc0[8]")
    resNameId_Spc1: int = ParamField(
        int16, "resNameId_Spc1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc1: int = ParamField(
        int16, "invMulCol_Spc1", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc1: float = ParamField(
        float32, "sepcPow_Spc1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad_Spc1[8]")
    resNameId_Spc2: int = ParamField(
        int16, "resNameId_Spc2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc2: int = ParamField(
        int16, "invMulCol_Spc2", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc2: float = ParamField(
        float32, "sepcPow_Spc2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(8, "pad_Spc2[8]")
    resNameId_Spc3: int = ParamField(
        int16, "resNameId_Spc3", default=3,
        tooltip="TOOLTIP-TODO",
    )
    invMulCol_Spc3: int = ParamField(
        int16, "invMulCol_Spc3", default=100,
        tooltip="TOOLTIP-TODO",
    )
    sepcPow_Spc3: float = ParamField(
        float32, "sepcPow_Spc3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "pad_Spc3[8]")
    degRotX_00: int = ParamField(
        int16, "degRotX_00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_00: int = ParamField(
        int16, "degRotY_00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_00: int = ParamField(
        int16, "colR_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_00: int = ParamField(
        int16, "colG_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_00: int = ParamField(
        int16, "colB_00", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_00: int = ParamField(
        int16, "colA_00", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(4, "pad_00[4]")
    degRotX_01: int = ParamField(
        int16, "degRotX_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_01: int = ParamField(
        int16, "degRotY_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_01: int = ParamField(
        int16, "colR_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_01: int = ParamField(
        int16, "colG_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_01: int = ParamField(
        int16, "colB_01", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_01: int = ParamField(
        int16, "colA_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(4, "pad_01[4]")
    degRotX_02: int = ParamField(
        int16, "degRotX_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_02: int = ParamField(
        int16, "degRotY_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_02: int = ParamField(
        int16, "colR_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_02: int = ParamField(
        int16, "colG_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_02: int = ParamField(
        int16, "colB_02", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_02: int = ParamField(
        int16, "colA_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad8: bytes = ParamPad(4, "pad_02[4]")
    degRotX_03: int = ParamField(
        int16, "degRotX_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_03: int = ParamField(
        int16, "degRotY_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_03: int = ParamField(
        int16, "colR_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_03: int = ParamField(
        int16, "colG_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_03: int = ParamField(
        int16, "colB_03", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_03: int = ParamField(
        int16, "colA_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad9: bytes = ParamPad(4, "pad_03[4]")
    degRotX_04: int = ParamField(
        int16, "degRotX_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_04: int = ParamField(
        int16, "degRotY_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_04: int = ParamField(
        int16, "colR_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_04: int = ParamField(
        int16, "colG_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_04: int = ParamField(
        int16, "colB_04", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_04: int = ParamField(
        int16, "colA_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad10: bytes = ParamPad(4, "pad_04[4]")
    degRotX_05: int = ParamField(
        int16, "degRotX_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_05: int = ParamField(
        int16, "degRotY_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_05: int = ParamField(
        int16, "colR_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_05: int = ParamField(
        int16, "colG_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_05: int = ParamField(
        int16, "colB_05", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_05: int = ParamField(
        int16, "colA_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad11: bytes = ParamPad(4, "pad_05[4]")
    degRotX_06: int = ParamField(
        int16, "degRotX_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_06: int = ParamField(
        int16, "degRotY_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_06: int = ParamField(
        int16, "colR_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_06: int = ParamField(
        int16, "colG_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_06: int = ParamField(
        int16, "colB_06", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_06: int = ParamField(
        int16, "colA_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad12: bytes = ParamPad(4, "pad_06[4]")
    degRotX_07: int = ParamField(
        int16, "degRotX_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_07: int = ParamField(
        int16, "degRotY_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_07: int = ParamField(
        int16, "colR_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_07: int = ParamField(
        int16, "colG_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_07: int = ParamField(
        int16, "colB_07", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_07: int = ParamField(
        int16, "colA_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad13: bytes = ParamPad(4, "pad_07[4]")
    degRotX_08: int = ParamField(
        int16, "degRotX_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_08: int = ParamField(
        int16, "degRotY_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_08: int = ParamField(
        int16, "colR_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_08: int = ParamField(
        int16, "colG_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_08: int = ParamField(
        int16, "colB_08", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_08: int = ParamField(
        int16, "colA_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad14: bytes = ParamPad(4, "pad_08[4]")
    degRotX_09: int = ParamField(
        int16, "degRotX_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    degRotY_09: int = ParamField(
        int16, "degRotY_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    colR_09: int = ParamField(
        int16, "colR_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colG_09: int = ParamField(
        int16, "colG_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colB_09: int = ParamField(
        int16, "colB_09", default=255,
        tooltip="TOOLTIP-TODO",
    )
    colA_09: int = ParamField(
        int16, "colA_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad15: bytes = ParamPad(4, "pad_09[4]")
