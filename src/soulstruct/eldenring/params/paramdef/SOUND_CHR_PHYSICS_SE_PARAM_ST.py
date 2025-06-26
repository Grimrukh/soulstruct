from __future__ import annotations

__all__ = ["SOUND_CHR_PHYSICS_SE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_CHR_PHYSICS_SE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ContactLandSeId: int = ParamField(
        int, "ContactLandSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandAddSeId: int = ParamField(
        int, "ContactLandAddSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandPlayNum: int = ParamField(
        int, "ContactLandPlayNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnablePlayCountPerRigid: int = ParamField(
        byte, "IsEnablePlayCountPerRigid", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "pad[3]")
    ContactLandMinImpuse: float = ParamField(
        float, "ContactLandMinImpuse", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactLandMinSpeed: float = ParamField(
        float, "ContactLandMinSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerSeId: int = ParamField(
        int, "ContactPlayerSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerMinImpuse: float = ParamField(
        float, "ContactPlayerMinImpuse", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactPlayerMinSpeed: float = ParamField(
        float, "ContactPlayerMinSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx0: int = ParamField(
        sbyte, "ContactCheckRigidIdx0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx1: int = ParamField(
        sbyte, "ContactCheckRigidIdx1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx2: int = ParamField(
        sbyte, "ContactCheckRigidIdx2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx3: int = ParamField(
        sbyte, "ContactCheckRigidIdx3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx4: int = ParamField(
        sbyte, "ContactCheckRigidIdx4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx5: int = ParamField(
        sbyte, "ContactCheckRigidIdx5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx6: int = ParamField(
        sbyte, "ContactCheckRigidIdx6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx7: int = ParamField(
        sbyte, "ContactCheckRigidIdx7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx8: int = ParamField(
        sbyte, "ContactCheckRigidIdx8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx9: int = ParamField(
        sbyte, "ContactCheckRigidIdx9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx10: int = ParamField(
        sbyte, "ContactCheckRigidIdx10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx11: int = ParamField(
        sbyte, "ContactCheckRigidIdx11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx12: int = ParamField(
        sbyte, "ContactCheckRigidIdx12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx13: int = ParamField(
        sbyte, "ContactCheckRigidIdx13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx14: int = ParamField(
        sbyte, "ContactCheckRigidIdx14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ContactCheckRigidIdx15: int = ParamField(
        sbyte, "ContactCheckRigidIdx15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
