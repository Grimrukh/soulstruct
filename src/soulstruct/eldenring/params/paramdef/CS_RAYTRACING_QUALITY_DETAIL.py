from __future__ import annotations

__all__ = ["CS_RAYTRACING_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_RAYTRACING_QUALITY_DETAIL(ParamRow):
    EnableRaytraceAO: int = ParamField(
        byte, "enableRaytraceAO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableRaytraceShadows: int = ParamField(
        byte, "enableRaytraceShadows", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x02: int = ParamField(
        byte, "Unk0x02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x03: int = ParamField(
        byte, "Unk0x03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkFloat0x04: float = ParamField(
        float, "UnkFloat0x04", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x08: int = ParamField(
        int, "Unk0x08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkFloat0x0C: float = ParamField(
        float, "UnkFloat0x0C", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x10: int = ParamField(
        int, "Unk0x10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenumbraSize: float = ParamField(
        float, "penumbraSize", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RenderDistance: float = ParamField(
        float, "renderDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
