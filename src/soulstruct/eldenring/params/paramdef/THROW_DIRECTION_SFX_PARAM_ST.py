from __future__ import annotations

__all__ = ["THROW_DIRECTION_SFX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class THROW_DIRECTION_SFX_PARAM_ST(ParamRow):
    SfxId00: int = ParamField(
        int, "sfxId_00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId01: int = ParamField(
        int, "sfxId_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId02: int = ParamField(
        int, "sfxId_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId03: int = ParamField(
        int, "sfxId_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId04: int = ParamField(
        int, "sfxId_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId05: int = ParamField(
        int, "sfxId_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId06: int = ParamField(
        int, "sfxId_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId07: int = ParamField(
        int, "sfxId_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId08: int = ParamField(
        int, "sfxId_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId09: int = ParamField(
        int, "sfxId_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId10: int = ParamField(
        int, "sfxId_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId11: int = ParamField(
        int, "sfxId_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId12: int = ParamField(
        int, "sfxId_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId13: int = ParamField(
        int, "sfxId_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId14: int = ParamField(
        int, "sfxId_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId15: int = ParamField(
        int, "sfxId_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId16: int = ParamField(
        int, "sfxId_16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId17: int = ParamField(
        int, "sfxId_17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId18: int = ParamField(
        int, "sfxId_18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId19: int = ParamField(
        int, "sfxId_19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId20: int = ParamField(
        int, "sfxId_20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId21: int = ParamField(
        int, "sfxId_21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId22: int = ParamField(
        int, "sfxId_22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId23: int = ParamField(
        int, "sfxId_23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId24: int = ParamField(
        int, "sfxId_24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId25: int = ParamField(
        int, "sfxId_25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId26: int = ParamField(
        int, "sfxId_26", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId27: int = ParamField(
        int, "sfxId_27", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId28: int = ParamField(
        int, "sfxId_28", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId29: int = ParamField(
        int, "sfxId_29", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxId30: int = ParamField(
        int, "sfxId_30", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(20, "pad1[20]")
