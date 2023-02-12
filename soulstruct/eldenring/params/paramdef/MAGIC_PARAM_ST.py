from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MAGIC_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    ConfirmationMessage: int = ParamField(
        int, "yesNoDialogMessageId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LimitRemoveSpecialEffect: int = ParamField(
        int, "limitCancelSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortIndex: int = ParamField(
        short, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequirementLuck: int = ParamField(
        byte, "requirementLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiNotifyType: int = ParamField(
        byte, "aiNotifyType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MPCost: int = ParamField(
        short, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaCost: int = ParamField(
        short, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpellIcon: int = ParamField(
        short, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Behavior: int = ParamField(
        short, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredGood: int = ParamField(
        short, "mtrlItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceSpell: int = ParamField(
        short, "replaceMagicId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BaseCastCount: int = ParamField(
        short, "maxQuantity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory1: int = ParamField(
        byte, "refCategory1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory2: int = ParamField(
        byte, "refCategory2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttunementSlotsUsed: int = ParamField(
        byte, "slotLength", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredIntelligence: int = ParamField(
        byte, "requirementIntellect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredFaith: int = ParamField(
        byte, "requirementFaith", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMin: int = ParamField(
        byte, "analogDexterityMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMax: int = ParamField(
        byte, "analogDexterityMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpellCategory: int = ParamField(
        byte, "ezStateBehaviorType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory3: int = ParamField(
        byte, "refCategory3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimationType: int = ParamField(
        byte, "refType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuActivated: int = ParamField(
        byte, "opmeMenuType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory4: int = ParamField(
        byte, "refCategory4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HasSpecialEffectType: int = ParamField(
        ushort, "hasSpEffectType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LimitCategory: int = ParamField(
        byte, "useLimitCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByNoCovenant: int = ParamField(
        byte, "vowType0:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByWayOfWhite: int = ParamField(
        byte, "vowType1:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByPrincessGuard: int = ParamField(
        byte, "vowType2:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByWarriorsOfSunlight: int = ParamField(
        byte, "vowType3:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByDarkwraith: int = ParamField(
        byte, "vowType4:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByPathOfTheDragon: int = ParamField(
        byte, "vowType5:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByGravelordServant: int = ParamField(
        byte, "vowType6:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByForestHunter: int = ParamField(
        byte, "vowType7:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableInMultiplayer: int = ParamField(
        byte, "enable_multi:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisabledOutsideMultiplayer: int = ParamField(
        byte, "enable_multi_only:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWeaponBuff: int = ParamField(
        byte, "isEnchant:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsShieldBuff: int = ParamField(
        byte, "isShieldEnchant:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByHumans: int = ParamField(
        byte, "enable_live:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByHollows: int = ParamField(
        byte, "enable_gray:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByWhitePhantoms: int = ParamField(
        byte, "enable_white:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByBlackPhantoms: int = ParamField(
        byte, "enable_black:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisabledOffline: int = ParamField(
        byte, "disableOffline:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateResonanceRing: int = ParamField(
        byte, "castResonanceMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsValidToughProtSADmg: int = ParamField(
        byte, "isValidTough_ProtSADmg:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWarpMagic: int = ParamField(
        byte, "isWarpMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableRiding: int = ParamField(
        byte, "enableRiding:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableRiding: int = ParamField(
        byte, "disableRiding:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseNoAttackRegion: int = ParamField(
        byte, "isUseNoAttackRegion:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad_1:1")
    UseableByDarkmoonBlade: int = ParamField(
        byte, "vowType8:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByChaosServant: int = ParamField(
        byte, "vowType9:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant10: int = ParamField(
        byte, "vowType10:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant11: int = ParamField(
        byte, "vowType11:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant12: int = ParamField(
        byte, "vowType12:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant13: int = ParamField(
        byte, "vowType13:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant14: int = ParamField(
        byte, "vowType14:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByCovenant15: int = ParamField(
        byte, "vowType15:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CastSfxId: int = ParamField(
        int, "castSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FireSfxId: int = ParamField(
        int, "fireSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectSfxId: int = ParamField(
        int, "effectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatusType: int = ParamField(
        byte, "ReplacementStatusType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus1: int = ParamField(
        sbyte, "ReplacementStatus1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus2: int = ParamField(
        sbyte, "ReplacementStatus2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus3: int = ParamField(
        sbyte, "ReplacementStatus3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus4: int = ParamField(
        sbyte, "ReplacementStatus4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory5: int = ParamField(
        byte, "refCategory5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeSA: int = ParamField(
        short, "consumeSA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic1: int = ParamField(
        int, "ReplacementMagic1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic2: int = ParamField(
        int, "ReplacementMagic2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic3: int = ParamField(
        int, "ReplacementMagic3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic4: int = ParamField(
        int, "ReplacementMagic4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Mpcharge: int = ParamField(
        short, "mp_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Staminacharge: int = ParamField(
        short, "stamina_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        byte, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory6: int = ParamField(
        byte, "refCategory6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory1: int = ParamField(
        byte, "subCategory1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        byte, "subCategory2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory7: int = ParamField(
        byte, "refCategory7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory8: int = ParamField(
        byte, "refCategory8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory9: int = ParamField(
        byte, "refCategory9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory10: int = ParamField(
        byte, "refCategory10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefId1: int = ParamField(
        int, "refId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId2: int = ParamField(
        int, "refId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId3: int = ParamField(
        int, "refId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiUseJudgeId: int = ParamField(
        int, "aiUseJudgeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId4: int = ParamField(
        int, "refId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId5: int = ParamField(
        int, "refId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId6: int = ParamField(
        int, "refId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId7: int = ParamField(
        int, "refId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId8: int = ParamField(
        int, "refId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId9: int = ParamField(
        int, "refId9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId10: int = ParamField(
        int, "refId10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType1: int = ParamField(
        byte, "consumeType1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType2: int = ParamField(
        byte, "consumeType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType3: int = ParamField(
        byte, "consumeType3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType4: int = ParamField(
        byte, "consumeType4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType5: int = ParamField(
        byte, "consumeType5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType6: int = ParamField(
        byte, "consumeType6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType7: int = ParamField(
        byte, "consumeType7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType8: int = ParamField(
        byte, "consumeType8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType9: int = ParamField(
        byte, "consumeType9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType10: int = ParamField(
        byte, "consumeType10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeLoopMPforMenu: int = ParamField(
        short, "consumeLoopMP_forMenu", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad[8]")
