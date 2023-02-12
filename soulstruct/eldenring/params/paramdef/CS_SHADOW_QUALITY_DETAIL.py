from __future__ import annotations

__all__ = ["CS_SHADOW_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_SHADOW_QUALITY_DETAIL(ParamRowData):
    Enabled: int = ParamField(
        byte, "enabled", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxFilterLevel: int = ParamField(
        byte, "maxFilterLevel", default=1,
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
