from __future__ import annotations

__all__ = ["HIT_EFFECT_SFX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class HIT_EFFECT_SFX_PARAM_ST(ParamRow):
    SlashNormal: int = ParamField(
        int32, "Slash_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashS: int = ParamField(
        int32, "Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashL: int = ParamField(
        int32, "Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashSpecific1: int = ParamField(
        int32, "Slash_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashSpecific2: int = ParamField(
        int32, "Slash_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowNormal: int = ParamField(
        int32, "Blow_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowS: int = ParamField(
        int32, "Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowL: int = ParamField(
        int32, "Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowSpecific1: int = ParamField(
        int32, "Blow_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowSpecific2: int = ParamField(
        int32, "Blow_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustNormal: int = ParamField(
        int32, "Thrust_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustS: int = ParamField(
        int32, "Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustL: int = ParamField(
        int32, "Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustSpecific1: int = ParamField(
        int32, "Thrust_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustSpecific2: int = ParamField(
        int32, "Thrust_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralNormal: int = ParamField(
        int32, "Neutral_Normal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralS: int = ParamField(
        int32, "Neutral_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralL: int = ParamField(
        int32, "Neutral_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralSpecific1: int = ParamField(
        int32, "Neutral_Specific1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralSpecific2: int = ParamField(
        int32, "Neutral_Specific2", default=0,
        tooltip="TOOLTIP-TODO",
    )
