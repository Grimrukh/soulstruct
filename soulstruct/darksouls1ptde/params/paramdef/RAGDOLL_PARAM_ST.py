from __future__ import annotations

__all__ = ["RAGDOLL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RAGDOLL_PARAM_ST(ParamRow):
    hierarchyGain: float = ParamField(
        float, "hierarchyGain", default=0.17000000178813934,
        tooltip="TOOLTIP-TODO",
    )
    velocityDamping: float = ParamField(
        float, "velocityDamping", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    accelGain: float = ParamField(
        float, "accelGain", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    velocityGain: float = ParamField(
        float, "velocityGain", default=0.6000000238418579,
        tooltip="TOOLTIP-TODO",
    )
    positionGain: float = ParamField(
        float, "positionGain", default=0.05000000074505806,
        tooltip="TOOLTIP-TODO",
    )
    maxLinerVelocity: float = ParamField(
        float, "maxLinerVelocity", default=1.399999976158142,
        tooltip="TOOLTIP-TODO",
    )
    maxAngularVelocity: float = ParamField(
        float, "maxAngularVelocity", default=1.7999999523162842,
        tooltip="TOOLTIP-TODO",
    )
    snapGain: float = ParamField(
        float, "snapGain", default=0.10000000149011612,
        tooltip="TOOLTIP-TODO",
    )
    enable: int = ParamField(
        byte, "enable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    partsHitMaskNo: int = ParamField(
        sbyte, "partsHitMaskNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(14, "pad[14]")
