from __future__ import annotations

__all__ = ["AI_STANDARD_INFO_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class AI_STANDARD_INFO_BANK(ParamRow):
    RadarRange: int = ParamField(
        uint16, "RadarRange", default=20,
        tooltip="TOOLTIP-TODO",
    )
    RadarAngleX: int = ParamField(
        uint8, "RadarAngleX", default=30,
        tooltip="TOOLTIP-TODO",
    )
    RadarAngleY: int = ParamField(
        uint8, "RadarAngleY", default=60,
        tooltip="TOOLTIP-TODO",
    )
    TerritorySize: int = ParamField(
        uint16, "TerritorySize", default=20,
        tooltip="TOOLTIP-TODO",
    )
    ThreatBeforeAttackRate: int = ParamField(
        uint8, "ThreatBeforeAttackRate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    ForceThreatOnFirstLocked: int = ParamField(
        uint8, "ForceThreatOnFirstLocked", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(24, "reserve0[24]")
    Attack1Distance: int = ParamField(
        uint16, "Attack1_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1Margin: int = ParamField(
        uint16, "Attack1_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1Rate: int = ParamField(
        uint8, "Attack1_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack1ActionID: int = ParamField(
        uint8, "Attack1_ActionID", ACTION_PATTERN, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1DelayMin: int = ParamField(
        uint8, "Attack1_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1DelayMax: int = ParamField(
        uint8, "Attack1_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1ConeAngle: int = ParamField(
        uint8, "Attack1_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "reserve10[7]")
    Attack2Distance: int = ParamField(
        uint16, "Attack2_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2Margin: int = ParamField(
        uint16, "Attack2_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2Rate: int = ParamField(
        uint8, "Attack2_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack2ActionID: int = ParamField(
        uint8, "Attack2_ActionID", ACTION_PATTERN, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2DelayMin: int = ParamField(
        uint8, "Attack2_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2DelayMax: int = ParamField(
        uint8, "Attack2_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2ConeAngle: int = ParamField(
        uint8, "Attack2_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(7, "reserve11[7]")
    Attack3Distance: int = ParamField(
        uint16, "Attack3_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3Margin: int = ParamField(
        uint16, "Attack3_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3Rate: int = ParamField(
        uint8, "Attack3_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack3ActionID: int = ParamField(
        uint8, "Attack3_ActionID", ACTION_PATTERN, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3DelayMin: int = ParamField(
        uint8, "Attack3_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3DelayMax: int = ParamField(
        uint8, "Attack3_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3ConeAngle: int = ParamField(
        uint8, "Attack3_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(7, "reserve12[7]")
    Attack4Distance: int = ParamField(
        uint16, "Attack4_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4Margin: int = ParamField(
        uint16, "Attack4_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4Rate: int = ParamField(
        uint8, "Attack4_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack4ActionID: int = ParamField(
        uint8, "Attack4_ActionID", ACTION_PATTERN, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4DelayMin: int = ParamField(
        uint8, "Attack4_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4DelayMax: int = ParamField(
        uint8, "Attack4_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4ConeAngle: int = ParamField(
        uint8, "Attack4_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(7, "reserve13[7]")
    _Pad5: bytes = ParamPad(32, "reserve_last[32]")
