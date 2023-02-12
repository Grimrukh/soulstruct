from __future__ import annotations

__all__ = ["ATTACK_ELEMENT_CORRECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ATTACK_ELEMENT_CORRECT_PARAM_ST(ParamRow):
    IsStrengthCorrectbyPhysics: int = ParamField(
        byte, "isStrengthCorrect_byPhysics:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyPhysics: int = ParamField(
        byte, "isDexterityCorrect_byPhysics:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyPhysics: int = ParamField(
        byte, "isMagicCorrect_byPhysics:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyPhysics: int = ParamField(
        byte, "isFaithCorrect_byPhysics:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyPhysics: int = ParamField(
        byte, "isLuckCorrect_byPhysics:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyMagic: int = ParamField(
        byte, "isStrengthCorrect_byMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyMagic: int = ParamField(
        byte, "isDexterityCorrect_byMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyMagic: int = ParamField(
        byte, "isMagicCorrect_byMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyMagic: int = ParamField(
        byte, "isFaithCorrect_byMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyMagic: int = ParamField(
        byte, "isLuckCorrect_byMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyFire: int = ParamField(
        byte, "isStrengthCorrect_byFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyFire: int = ParamField(
        byte, "isDexterityCorrect_byFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyFire: int = ParamField(
        byte, "isMagicCorrect_byFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyFire: int = ParamField(
        byte, "isFaithCorrect_byFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyFire: int = ParamField(
        byte, "isLuckCorrect_byFire:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyThunder: int = ParamField(
        byte, "isStrengthCorrect_byThunder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyThunder: int = ParamField(
        byte, "isDexterityCorrect_byThunder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyThunder: int = ParamField(
        byte, "isMagicCorrect_byThunder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyThunder: int = ParamField(
        byte, "isFaithCorrect_byThunder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyThunder: int = ParamField(
        byte, "isLuckCorrect_byThunder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyDark: int = ParamField(
        byte, "isStrengthCorrect_byDark:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyDark: int = ParamField(
        byte, "isDexterityCorrect_byDark:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyDark: int = ParamField(
        byte, "isMagicCorrect_byDark:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyDark: int = ParamField(
        byte, "isFaithCorrect_byDark:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyDark: int = ParamField(
        byte, "isLuckCorrect_byDark:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1:7")
    OverwriteStrengthCorrectRatebyPhysics: int = ParamField(
        short, "overwriteStrengthCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyPhysics: int = ParamField(
        short, "overwriteDexterityCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyPhysics: int = ParamField(
        short, "overwriteMagicCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyPhysics: int = ParamField(
        short, "overwriteFaithCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyPhysics: int = ParamField(
        short, "overwriteLuckCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyMagic: int = ParamField(
        short, "overwriteStrengthCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyMagic: int = ParamField(
        short, "overwriteDexterityCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyMagic: int = ParamField(
        short, "overwriteMagicCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyMagic: int = ParamField(
        short, "overwriteFaithCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyMagic: int = ParamField(
        short, "overwriteLuckCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyFire: int = ParamField(
        short, "overwriteStrengthCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyFire: int = ParamField(
        short, "overwriteDexterityCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyFire: int = ParamField(
        short, "overwriteMagicCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyFire: int = ParamField(
        short, "overwriteFaithCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyFire: int = ParamField(
        short, "overwriteLuckCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyThunder: int = ParamField(
        short, "overwriteStrengthCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyThunder: int = ParamField(
        short, "overwriteDexterityCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyThunder: int = ParamField(
        short, "overwriteMagicCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyThunder: int = ParamField(
        short, "overwriteFaithCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyThunder: int = ParamField(
        short, "overwriteLuckCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyDark: int = ParamField(
        short, "overwriteStrengthCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyDark: int = ParamField(
        short, "overwriteDexterityCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyDark: int = ParamField(
        short, "overwriteMagicCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyDark: int = ParamField(
        short, "overwriteFaithCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyDark: int = ParamField(
        short, "overwriteLuckCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyPhysics: int = ParamField(
        short, "InfluenceStrengthCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyPhysics: int = ParamField(
        short, "InfluenceDexterityCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyPhysics: int = ParamField(
        short, "InfluenceMagicCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyPhysics: int = ParamField(
        short, "InfluenceFaithCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyPhysics: int = ParamField(
        short, "InfluenceLuckCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyMagic: int = ParamField(
        short, "InfluenceStrengthCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyMagic: int = ParamField(
        short, "InfluenceDexterityCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyMagic: int = ParamField(
        short, "InfluenceMagicCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyMagic: int = ParamField(
        short, "InfluenceFaithCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyMagic: int = ParamField(
        short, "InfluenceLuckCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyFire: int = ParamField(
        short, "InfluenceStrengthCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyFire: int = ParamField(
        short, "InfluenceDexterityCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyFire: int = ParamField(
        short, "InfluenceMagicCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyFire: int = ParamField(
        short, "InfluenceFaithCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyFire: int = ParamField(
        short, "InfluenceLuckCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyThunder: int = ParamField(
        short, "InfluenceStrengthCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyThunder: int = ParamField(
        short, "InfluenceDexterityCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyThunder: int = ParamField(
        short, "InfluenceMagicCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyThunder: int = ParamField(
        short, "InfluenceFaithCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyThunder: int = ParamField(
        short, "InfluenceLuckCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyDark: int = ParamField(
        short, "InfluenceStrengthCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyDark: int = ParamField(
        short, "InfluenceDexterityCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyDark: int = ParamField(
        short, "InfluenceMagicCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyDark: int = ParamField(
        short, "InfluenceFaithCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyDark: int = ParamField(
        short, "InfluenceLuckCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad2[24]")
