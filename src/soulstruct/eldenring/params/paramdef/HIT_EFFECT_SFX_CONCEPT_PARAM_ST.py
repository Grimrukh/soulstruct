from __future__ import annotations

__all__ = ["HIT_EFFECT_SFX_CONCEPT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class HIT_EFFECT_SFX_CONCEPT_PARAM_ST(ParamRow):
    AtkIron1: int = ParamField(
        int16, "atkIron_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkIron2: int = ParamField(
        int16, "atkIron_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkLeather1: int = ParamField(
        int16, "atkLeather_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkLeather2: int = ParamField(
        int16, "atkLeather_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkWood1: int = ParamField(
        int16, "atkWood_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkWood2: int = ParamField(
        int16, "atkWood_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkBody1: int = ParamField(
        int16, "atkBody_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkBody2: int = ParamField(
        int16, "atkBody_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStone1: int = ParamField(
        int16, "atkStone_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStone2: int = ParamField(
        int16, "atkStone_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
    AtkNone1: int = ParamField(
        int16, "atkNone_1", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkNone2: int = ParamField(
        int16, "atkNone_2", HIT_EFFECT_SFX_CONCEPT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(52, "reserve[52]")
