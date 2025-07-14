from __future__ import annotations

__all__ = ["MISSILE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MISSILE_PARAM_ST(ParamRow):
    FFXID: int = ParamField(
        int32, "FFXID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime: int = ParamField(
        uint16, "LifeTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitSphereRadius: int = ParamField(
        uint16, "HitSphereRadius", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitDamage: int = ParamField(
        uint16, "HitDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "reserve0[6]")
    InitVelocity: float = ParamField(
        float32, "InitVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Distance: float = ParamField(
        float32, "distance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityInRange: float = ParamField(
        float32, "gravityInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityOutRange: float = ParamField(
        float32, "gravityOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Mp: int = ParamField(
        int32, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccelInRange: float = ParamField(
        float32, "accelInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelOutRange: float = ParamField(
        float32, "accelOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(20, "reserve1[20]")
    HitMissileID: int = ParamField(
        uint16, "HitMissileID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiedNaturaly: int = ParamField(
        uint8, "DiedNaturaly", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExplosionDie: int = ParamField(
        uint8, "ExplosionDie", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        int32, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(56, "reserve_last[56]")
