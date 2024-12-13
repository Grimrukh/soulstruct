from __future__ import annotations

__all__ = ["MISSILE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MISSILE_PARAM_ST(ParamRow):
    FFXID: int = ParamField(
        int, "FFXID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime: int = ParamField(
        ushort, "LifeTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitSphereRadius: int = ParamField(
        ushort, "HitSphereRadius", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitDamage: int = ParamField(
        ushort, "HitDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "reserve0[6]")
    InitVelocity: float = ParamField(
        float, "InitVelocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Distance: float = ParamField(
        float, "distance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityInRange: float = ParamField(
        float, "gravityInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GravityOutRange: float = ParamField(
        float, "gravityOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Mp: int = ParamField(
        int, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccelInRange: float = ParamField(
        float, "accelInRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccelOutRange: float = ParamField(
        float, "accelOutRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(20, "reserve1[20]")
    HitMissileID: int = ParamField(
        ushort, "HitMissileID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiedNaturaly: int = ParamField(
        byte, "DiedNaturaly", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExplosionDie: int = ParamField(
        byte, "ExplosionDie", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        int, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(56, "reserve_last[56]")
