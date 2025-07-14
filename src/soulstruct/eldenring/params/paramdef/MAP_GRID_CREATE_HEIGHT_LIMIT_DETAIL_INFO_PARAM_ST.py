from __future__ import annotations

__all__ = ["MAP_GRID_CREATE_HEIGHT_LIMIT_DETAIL_INFO_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_GRID_CREATE_HEIGHT_LIMIT_DETAIL_INFO_PARAM_ST(ParamRow):
    MapId: int = ParamField(
        int, "mapId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x4: int = ParamField(
        int, "unknown_0x4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x8: int = ParamField(
        int, "unknown_0x8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xc: int = ParamField(
        int, "unknown_0xc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x10: int = ParamField(
        int, "unknown_0x10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x14: int = ParamField(
        int, "unknown_0x14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x18: int = ParamField(
        int, "unknown_0x18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x1c: int = ParamField(
        int, "unknown_0x1c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x20: int = ParamField(
        int, "unknown_0x20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x24: int = ParamField(
        int, "unknown_0x24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x28: int = ParamField(
        int, "unknown_0x28", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2c: int = ParamField(
        byte, "unknown_0x2c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2d: int = ParamField(
        byte, "unknown_0x2d", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2e: int = ParamField(
        byte, "unknown_0x2e", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x2f: int = ParamField(
        byte, "unknown_0x2f", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x30: int = ParamField(
        byte, "unknown_0x30", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x31: int = ParamField(
        byte, "unknown_0x31", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x32: int = ParamField(
        ushort, "unknown_0x32", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x34: int = ParamField(
        int, "unknown_0x34", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x38: int = ParamField(
        int, "unknown_0x38", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x3c: int = ParamField(
        int, "unknown_0x3c", default=0,
        tooltip="TOOLTIP-TODO",
    )
