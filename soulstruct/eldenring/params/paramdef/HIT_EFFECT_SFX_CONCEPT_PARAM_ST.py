from __future__ import annotations

__all__ = ["HIT_EFFECT_SFX_CONCEPT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class HIT_EFFECT_SFX_CONCEPT_PARAM_ST(ParamRow):
    AtkIron1: int = ParamField(
        short, "atkIron_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkIron2: int = ParamField(
        short, "atkIron_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkLeather1: int = ParamField(
        short, "atkLeather_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkLeather2: int = ParamField(
        short, "atkLeather_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkWood1: int = ParamField(
        short, "atkWood_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkWood2: int = ParamField(
        short, "atkWood_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkBody1: int = ParamField(
        short, "atkBody_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkBody2: int = ParamField(
        short, "atkBody_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStone1: int = ParamField(
        short, "atkStone_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStone2: int = ParamField(
        short, "atkStone_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
    AtkNone1: int = ParamField(
        short, "atkNone_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkNone2: int = ParamField(
        short, "atkNone_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(52, "reserve[52]")
