from __future__ import annotations

__all__ = ["RAGDOLL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class RAGDOLL_PARAM_ST(ParamRow):
    HierarchyGain: float = ParamField(
        float, "hierarchyGain", default=0.17000000178813934,
        tooltip="TOOLTIP-TODO",
    )
    VelocityDamping: float = ParamField(
        float, "velocityDamping", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelGain: float = ParamField(
        float, "accelGain", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VelocityGain: float = ParamField(
        float, "velocityGain", default=0.6000000238418579,
        tooltip="TOOLTIP-TODO",
    )
    PositionGain: float = ParamField(
        float, "positionGain", default=0.05000000074505806,
        tooltip="TOOLTIP-TODO",
    )
    MaxLinerVelocity: float = ParamField(
        float, "maxLinerVelocity", default=1.399999976158142,
        tooltip="TOOLTIP-TODO",
    )
    MaxAngularVelocity: float = ParamField(
        float, "maxAngularVelocity", default=1.7999999523162842,
        tooltip="TOOLTIP-TODO",
    )
    SnapGain: float = ParamField(
        float, "snapGain", default=0.10000000149011612,
        tooltip="TOOLTIP-TODO",
    )
    Enable: int = ParamField(
        byte, "enable", RAGDOLL_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PartsHitMaskNo: int = ParamField(
        sbyte, "partsHitMaskNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad[14]")
