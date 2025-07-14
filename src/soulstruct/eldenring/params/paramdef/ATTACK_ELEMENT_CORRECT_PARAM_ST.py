from __future__ import annotations

__all__ = ["ATTACK_ELEMENT_CORRECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ATTACK_ELEMENT_CORRECT_PARAM_ST(ParamRow):
    IsStrengthCorrectbyPhysics: bool = ParamField(
        uint8, "isStrengthCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyPhysics: bool = ParamField(
        uint8, "isDexterityCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyPhysics: bool = ParamField(
        uint8, "isMagicCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyPhysics: bool = ParamField(
        uint8, "isFaithCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyPhysics: bool = ParamField(
        uint8, "isLuckCorrect_byPhysics:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyMagic: bool = ParamField(
        uint8, "isStrengthCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyMagic: bool = ParamField(
        uint8, "isDexterityCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyMagic: bool = ParamField(
        uint8, "isMagicCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyMagic: bool = ParamField(
        uint8, "isFaithCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyMagic: bool = ParamField(
        uint8, "isLuckCorrect_byMagic:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyFire: bool = ParamField(
        uint8, "isStrengthCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyFire: bool = ParamField(
        uint8, "isDexterityCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyFire: bool = ParamField(
        uint8, "isMagicCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyFire: bool = ParamField(
        uint8, "isFaithCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyFire: bool = ParamField(
        uint8, "isLuckCorrect_byFire:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyThunder: bool = ParamField(
        uint8, "isStrengthCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyThunder: bool = ParamField(
        uint8, "isDexterityCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyThunder: bool = ParamField(
        uint8, "isMagicCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyThunder: bool = ParamField(
        uint8, "isFaithCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyThunder: bool = ParamField(
        uint8, "isLuckCorrect_byThunder:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStrengthCorrectbyDark: bool = ParamField(
        uint8, "isStrengthCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDexterityCorrectbyDark: bool = ParamField(
        uint8, "isDexterityCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMagicCorrectbyDark: bool = ParamField(
        uint8, "isMagicCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFaithCorrectbyDark: bool = ParamField(
        uint8, "isFaithCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLuckCorrectbyDark: bool = ParamField(
        uint8, "isLuckCorrect_byDark:1", BOOL_YESNO_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad1:7", bit_count=7)
    OverwriteStrengthCorrectRatebyPhysics: int = ParamField(
        int16, "overwriteStrengthCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyPhysics: int = ParamField(
        int16, "overwriteDexterityCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyPhysics: int = ParamField(
        int16, "overwriteMagicCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyPhysics: int = ParamField(
        int16, "overwriteFaithCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyPhysics: int = ParamField(
        int16, "overwriteLuckCorrectRate_byPhysics", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyMagic: int = ParamField(
        int16, "overwriteStrengthCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyMagic: int = ParamField(
        int16, "overwriteDexterityCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyMagic: int = ParamField(
        int16, "overwriteMagicCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyMagic: int = ParamField(
        int16, "overwriteFaithCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyMagic: int = ParamField(
        int16, "overwriteLuckCorrectRate_byMagic", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyFire: int = ParamField(
        int16, "overwriteStrengthCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyFire: int = ParamField(
        int16, "overwriteDexterityCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyFire: int = ParamField(
        int16, "overwriteMagicCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyFire: int = ParamField(
        int16, "overwriteFaithCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyFire: int = ParamField(
        int16, "overwriteLuckCorrectRate_byFire", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyThunder: int = ParamField(
        int16, "overwriteStrengthCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyThunder: int = ParamField(
        int16, "overwriteDexterityCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyThunder: int = ParamField(
        int16, "overwriteMagicCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyThunder: int = ParamField(
        int16, "overwriteFaithCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyThunder: int = ParamField(
        int16, "overwriteLuckCorrectRate_byThunder", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteStrengthCorrectRatebyDark: int = ParamField(
        int16, "overwriteStrengthCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteDexterityCorrectRatebyDark: int = ParamField(
        int16, "overwriteDexterityCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteMagicCorrectRatebyDark: int = ParamField(
        int16, "overwriteMagicCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteFaithCorrectRatebyDark: int = ParamField(
        int16, "overwriteFaithCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteLuckCorrectRatebyDark: int = ParamField(
        int16, "overwriteLuckCorrectRate_byDark", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyPhysics: int = ParamField(
        int16, "InfluenceStrengthCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyPhysics: int = ParamField(
        int16, "InfluenceDexterityCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyPhysics: int = ParamField(
        int16, "InfluenceMagicCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyPhysics: int = ParamField(
        int16, "InfluenceFaithCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyPhysics: int = ParamField(
        int16, "InfluenceLuckCorrectRate_byPhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyMagic: int = ParamField(
        int16, "InfluenceStrengthCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyMagic: int = ParamField(
        int16, "InfluenceDexterityCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyMagic: int = ParamField(
        int16, "InfluenceMagicCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyMagic: int = ParamField(
        int16, "InfluenceFaithCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyMagic: int = ParamField(
        int16, "InfluenceLuckCorrectRate_byMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyFire: int = ParamField(
        int16, "InfluenceStrengthCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyFire: int = ParamField(
        int16, "InfluenceDexterityCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyFire: int = ParamField(
        int16, "InfluenceMagicCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyFire: int = ParamField(
        int16, "InfluenceFaithCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyFire: int = ParamField(
        int16, "InfluenceLuckCorrectRate_byFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyThunder: int = ParamField(
        int16, "InfluenceStrengthCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyThunder: int = ParamField(
        int16, "InfluenceDexterityCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyThunder: int = ParamField(
        int16, "InfluenceMagicCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyThunder: int = ParamField(
        int16, "InfluenceFaithCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyThunder: int = ParamField(
        int16, "InfluenceLuckCorrectRate_byThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceStrengthCorrectRatebyDark: int = ParamField(
        int16, "InfluenceStrengthCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceDexterityCorrectRatebyDark: int = ParamField(
        int16, "InfluenceDexterityCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceMagicCorrectRatebyDark: int = ParamField(
        int16, "InfluenceMagicCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceFaithCorrectRatebyDark: int = ParamField(
        int16, "InfluenceFaithCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    InfluenceLuckCorrectRatebyDark: int = ParamField(
        int16, "InfluenceLuckCorrectRate_byDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(24, "pad2[24]")
