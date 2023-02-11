from __future__ import annotations

__all__ = ["AI_STANDARD_INFO_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_STANDARD_INFO_BANK(ParamRowData):
    RadarRange: int = ParamField(
        ushort, "RadarRange", default=20,
        tooltip="TOOLTIP-TODO",
    )
    RadarAngleX: int = ParamField(
        byte, "RadarAngleX", default=30,
        tooltip="TOOLTIP-TODO",
    )
    RadarAngleY: int = ParamField(
        byte, "RadarAngleY", default=60,
        tooltip="TOOLTIP-TODO",
    )
    TerritorySize: int = ParamField(
        ushort, "TerritorySize", default=20,
        tooltip="TOOLTIP-TODO",
    )
    ThreatBeforeAttackRate: int = ParamField(
        byte, "ThreatBeforeAttackRate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    ForceThreatOnFirstLocked: int = ParamField(
        byte, "ForceThreatOnFirstLocked", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(24, "reserve0[24]")
    Attack1_Distance: int = ParamField(
        ushort, "Attack1_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_Margin: int = ParamField(
        ushort, "Attack1_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_Rate: int = ParamField(
        byte, "Attack1_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_ActionID: int = ParamField(
        byte, "Attack1_ActionID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_DelayMin: int = ParamField(
        byte, "Attack1_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_DelayMax: int = ParamField(
        byte, "Attack1_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack1_ConeAngle: int = ParamField(
        byte, "Attack1_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "reserve10[7]")
    Attack2_Distance: int = ParamField(
        ushort, "Attack2_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_Margin: int = ParamField(
        ushort, "Attack2_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_Rate: int = ParamField(
        byte, "Attack2_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_ActionID: int = ParamField(
        byte, "Attack2_ActionID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_DelayMin: int = ParamField(
        byte, "Attack2_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_DelayMax: int = ParamField(
        byte, "Attack2_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack2_ConeAngle: int = ParamField(
        byte, "Attack2_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(7, "reserve11[7]")
    Attack3_Distance: int = ParamField(
        ushort, "Attack3_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_Margin: int = ParamField(
        ushort, "Attack3_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_Rate: int = ParamField(
        byte, "Attack3_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_ActionID: int = ParamField(
        byte, "Attack3_ActionID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_DelayMin: int = ParamField(
        byte, "Attack3_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_DelayMax: int = ParamField(
        byte, "Attack3_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack3_ConeAngle: int = ParamField(
        byte, "Attack3_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(7, "reserve12[7]")
    Attack4_Distance: int = ParamField(
        ushort, "Attack4_Distance", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_Margin: int = ParamField(
        ushort, "Attack4_Margin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_Rate: int = ParamField(
        byte, "Attack4_Rate", default=50,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_ActionID: int = ParamField(
        byte, "Attack4_ActionID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_DelayMin: int = ParamField(
        byte, "Attack4_DelayMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_DelayMax: int = ParamField(
        byte, "Attack4_DelayMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attack4_ConeAngle: int = ParamField(
        byte, "Attack4_ConeAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(7, "reserve13[7]")
    _Pad5: bytes = ParamPad(32, "reserve_last[32]")
