from __future__ import annotations

__all__ = ["HIT_EFFECT_SFX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class HIT_EFFECT_SFX_PARAM_ST(ParamRowData):
    SlashNormal: int = ParamField(
        int, "Slash_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashS: int = ParamField(
        int, "Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashL: int = ParamField(
        int, "Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashSpecific1: int = ParamField(
        int, "Slash_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashSpecific2: int = ParamField(
        int, "Slash_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowNormal: int = ParamField(
        int, "Blow_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowS: int = ParamField(
        int, "Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowL: int = ParamField(
        int, "Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowSpecific1: int = ParamField(
        int, "Blow_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowSpecific2: int = ParamField(
        int, "Blow_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustNormal: int = ParamField(
        int, "Thrust_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustS: int = ParamField(
        int, "Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustL: int = ParamField(
        int, "Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustSpecific1: int = ParamField(
        int, "Thrust_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustSpecific2: int = ParamField(
        int, "Thrust_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralNormal: int = ParamField(
        int, "Neutral_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralS: int = ParamField(
        int, "Neutral_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralL: int = ParamField(
        int, "Neutral_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralSpecific1: int = ParamField(
        int, "Neutral_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralSpecific2: int = ParamField(
        int, "Neutral_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
