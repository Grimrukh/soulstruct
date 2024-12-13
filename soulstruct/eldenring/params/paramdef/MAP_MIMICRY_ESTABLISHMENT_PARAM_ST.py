from __future__ import annotations

__all__ = ["MAP_MIMICRY_ESTABLISHMENT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_MIMICRY_ESTABLISHMENT_PARAM_ST(ParamRow):
    MimicryEstablishment0: float = ParamField(
        float, "mimicryEstablishment0", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    MimicryEstablishment1: float = ParamField(
        float, "mimicryEstablishment1", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    MimicryEstablishment2: float = ParamField(
        float, "mimicryEstablishment2", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    MimicryBeginSfxId0: int = ParamField(
        int, "mimicryBeginSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicrySfxId0: int = ParamField(
        int, "mimicrySfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicryEndSfxId0: int = ParamField(
        int, "mimicryEndSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicryBeginSfxId1: int = ParamField(
        int, "mimicryBeginSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicrySfxId1: int = ParamField(
        int, "mimicrySfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicryEndSfxId1: int = ParamField(
        int, "mimicryEndSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicryBeginSfxId2: int = ParamField(
        int, "mimicryBeginSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicrySfxId2: int = ParamField(
        int, "mimicrySfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MimicryEndSfxId2: int = ParamField(
        int, "mimicryEndSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(16, "pad1[16]")
