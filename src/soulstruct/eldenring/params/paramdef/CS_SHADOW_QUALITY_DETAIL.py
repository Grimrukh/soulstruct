from __future__ import annotations

__all__ = ["CS_SHADOW_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_SHADOW_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        uint8, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxFilterLevel: int = ParamField(
        uint8, "maxFilterLevel", GX_SHADOW_FILTER_LEVEL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "dmy[2]")
    TextureSizeScaler: int = ParamField(
        uint32, "textureSizeScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TextureSizeDivider: int = ParamField(
        uint32, "textureSizeDivider", default=2,
        tooltip="TOOLTIP-TODO",
    )
    TextureMinSize: int = ParamField(
        uint32, "textureMinSize", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureMaxSize: int = ParamField(
        uint32, "textureMaxSize", default=1024,
        tooltip="TOOLTIP-TODO",
    )
    BlurCountBias: int = ParamField(
        int32, "blurCountBias", default=-1,
        tooltip="TOOLTIP-TODO",
    )
