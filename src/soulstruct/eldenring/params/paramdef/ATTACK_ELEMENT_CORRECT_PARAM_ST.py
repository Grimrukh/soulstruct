from __future__ import annotations

__all__ = ["ATTACK_ELEMENT_CORRECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ATTACK_ELEMENT_CORRECT_PARAM_ST(ParamRow):
    IsStrengthCorrectbyPhysics: bool = ParamField(
        byte, "isStrengthCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyPhysics: bool = ParamField(
        byte, "isDexterityCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyPhysics: bool = ParamField(
        byte, "isMagicCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyPhysics: bool = ParamField(
        byte, "isFaithCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyPhysics: bool = ParamField(
        byte, "isLuckCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyMagic: bool = ParamField(
        byte, "isStrengthCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyMagic: bool = ParamField(
        byte, "isDexterityCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyMagic: bool = ParamField(
        byte, "isMagicCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyMagic: bool = ParamField(
        byte, "isFaithCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyMagic: bool = ParamField(
        byte, "isLuckCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyFire: bool = ParamField(
        byte, "isStrengthCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyFire: bool = ParamField(
        byte, "isDexterityCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyFire: bool = ParamField(
        byte, "isMagicCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyFire: bool = ParamField(
        byte, "isFaithCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyFire: bool = ParamField(
        byte, "isLuckCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyThunder: bool = ParamField(
        byte, "isStrengthCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyThunder: bool = ParamField(
        byte, "isDexterityCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyThunder: bool = ParamField(
        byte, "isMagicCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyThunder: bool = ParamField(
        byte, "isFaithCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyThunder: bool = ParamField(
        byte, "isLuckCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyDark: bool = ParamField(
        byte, "isStrengthCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyDark: bool = ParamField(
        byte, "isDexterityCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyDark: bool = ParamField(
        byte, "isMagicCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyDark: bool = ParamField(
        byte, "isFaithCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyDark: bool = ParamField(
        byte, "isLuckCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad1:7", bit_count=7)
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
    _Pad0: bytes = ParamPad(24, "pad2[24]")
