from __future__ import annotations

__all__ = ["CS_SHADOW_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_SHADOW_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxFilterLevel: int = ParamField(
        byte, "maxFilterLevel", GX_SHADOW_FILTER_LEVEL, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "dmy[2]")
    TextureSizeScaler: int = ParamField(
        uint, "textureSizeScaler", default=1,
        tooltip="TOOLTIP-TODO",
    )
    TextureSizeDivider: int = ParamField(
        uint, "textureSizeDivider", default=2,
        tooltip="TOOLTIP-TODO",
    )
    TextureMinSize: int = ParamField(
        uint, "textureMinSize", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureMaxSize: int = ParamField(
        uint, "textureMaxSize", default=1024,
        tooltip="TOOLTIP-TODO",
    )
    BlurCountBias: int = ParamField(
        int, "blurCountBias", default=-1,
        tooltip="TOOLTIP-TODO",
    )
