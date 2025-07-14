from __future__ import annotations

__all__ = ["SOUND_CHR_PHYSICS_SE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_CHR_PHYSICS_SE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ContactLandSeId: int = ParamField(
        int32, "ContactLandSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandAddSeId: int = ParamField(
        int32, "ContactLandAddSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandPlayNum: int = ParamField(
        int32, "ContactLandPlayNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnablePlayCountPerRigid: int = ParamField(
        uint8, "IsEnablePlayCountPerRigid", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad[3]")
    ContactLandMinImpuse: float = ParamField(
        float32, "ContactLandMinImpuse", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandMinSpeed: float = ParamField(
        float32, "ContactLandMinSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerSeId: int = ParamField(
        int32, "ContactPlayerSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerMinImpuse: float = ParamField(
        float32, "ContactPlayerMinImpuse", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerMinSpeed: float = ParamField(
        float32, "ContactPlayerMinSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx0: int = ParamField(
        int8, "ContactCheckRigidIdx0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx1: int = ParamField(
        int8, "ContactCheckRigidIdx1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx2: int = ParamField(
        int8, "ContactCheckRigidIdx2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx3: int = ParamField(
        int8, "ContactCheckRigidIdx3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx4: int = ParamField(
        int8, "ContactCheckRigidIdx4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx5: int = ParamField(
        int8, "ContactCheckRigidIdx5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx6: int = ParamField(
        int8, "ContactCheckRigidIdx6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx7: int = ParamField(
        int8, "ContactCheckRigidIdx7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx8: int = ParamField(
        int8, "ContactCheckRigidIdx8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx9: int = ParamField(
        int8, "ContactCheckRigidIdx9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx10: int = ParamField(
        int8, "ContactCheckRigidIdx10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx11: int = ParamField(
        int8, "ContactCheckRigidIdx11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx12: int = ParamField(
        int8, "ContactCheckRigidIdx12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx13: int = ParamField(
        int8, "ContactCheckRigidIdx13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx14: int = ParamField(
        int8, "ContactCheckRigidIdx14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx15: int = ParamField(
        int8, "ContactCheckRigidIdx15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
