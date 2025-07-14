from __future__ import annotations

__all__ = ["CS_RAYTRACING_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CS_RAYTRACING_QUALITY_DETAIL(ParamRow):
    EnableRaytraceAO: int = ParamField(
        uint8, "enableRaytraceAO", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableRaytraceShadows: int = ParamField(
        uint8, "enableRaytraceShadows", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x02: int = ParamField(
        uint8, "Unk0x02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x03: int = ParamField(
        uint8, "Unk0x03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkFloat0x04: float = ParamField(
        float32, "UnkFloat0x04", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x08: int = ParamField(
        int32, "Unk0x08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkFloat0x0C: float = ParamField(
        float32, "UnkFloat0x0C", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk0x10: int = ParamField(
        int32, "Unk0x10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenumbraSize: float = ParamField(
        float32, "penumbraSize", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RenderDistance: float = ParamField(
        float32, "renderDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
