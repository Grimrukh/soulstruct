from __future__ import annotations

__all__ = ["EQUIP_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_WEAPON_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GhostWeaponReplacement: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeightRatio: float = ParamField(
        float, "weaponWeightRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RepairCost: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforcePrice: int = ParamField(
        int, "reinforcePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StrengthScaling: float = ParamField(
        float, "correctStrength", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DexterityScaling: float = ParamField(
        float, "correctAgility", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IntelligenceScaling: float = ParamField(
        float, "correctMagic", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaithScaling: float = ParamField(
        float, "correctFaith", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalGuardPercentage: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicGuardPercentage: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardPercentage: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LightningGuardPercentage: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit0: int = ParamField(
        int, "spEffectBehaviorId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit1: int = ParamField(
        int, "spEffectBehaviorId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit2: int = ParamField(
        int, "spEffectBehaviorId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect0: int = ParamField(
        int, "residentSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect1: int = ParamField(
        int, "residentSpEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquippedSpecialEffect2: int = ParamField(
        int, "residentSpEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeMaterialID: int = ParamField(
        int, "materialSetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin0: int = ParamField(
        int, "originEquipWep", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin1: int = ParamField(
        int, "originEquipWep1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin2: int = ParamField(
        int, "originEquipWep2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin3: int = ParamField(
        int, "originEquipWep3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin4: int = ParamField(
        int, "originEquipWep4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin5: int = ParamField(
        int, "originEquipWep5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin6: int = ParamField(
        int, "originEquipWep6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin7: int = ParamField(
        int, "originEquipWep7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin8: int = ParamField(
        int, "originEquipWep8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin9: int = ParamField(
        int, "originEquipWep9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin10: int = ParamField(
        int, "originEquipWep10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin11: int = ParamField(
        int, "originEquipWep11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin12: int = ParamField(
        int, "originEquipWep12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin13: int = ParamField(
        int, "originEquipWep13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin14: int = ParamField(
        int, "originEquipWep14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin15: int = ParamField(
        int, "originEquipWep15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeakADamageRate: float = ParamField(
        float, "weakA_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakBDamageRate: float = ParamField(
        float, "weakB_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakCDamageRate: float = ParamField(
        float, "weakC_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakDDamageRate: float = ParamField(
        float, "weakD_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResistMaxCorrect: float = ParamField(
        float, "sleepGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResistMaxCorrect: float = ParamField(
        float, "madnessGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BasePoiseDamage: float = ParamField(
        float, "saWeaponDamage", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponModel: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponIcon: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InitialDurability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="TOOLTIP-TODO",
    )
    MaxDurability: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ThrowEscapePower: int = ParamField(
        ushort, "attackThrowEscape", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxParryWindowDuration: int = ParamField(
        short, "parryDamageLife", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BasePhysicalDamage: int = ParamField(
        ushort, "attackBasePhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    BaseMagicDamage: int = ParamField(
        ushort, "attackBaseMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    BaseFireDamage: int = ParamField(
        ushort, "attackBaseFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    BaseLightningDamage: int = ParamField(
        ushort, "attackBaseThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    BaseStaminaDamage: int = ParamField(
        ushort, "attackBaseStamina", default=100,
        tooltip="TOOLTIP-TODO",
    )
    EffectiveGuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackPoiseBonus: float = ParamField(
        float, "saDurability", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaDefense: int = ParamField(
        short, "staminaGuardDef", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponUpgradeID: int = ParamField(
        short, "reinforceTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxUpgradeAchievementID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ThrowDamageChangePercentage: int = ParamField(
        short, "throwAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BowRangeChangePercentage: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponModelCategory: int = ParamField(
        byte, "equipModelCategory", default=7,
        tooltip="TOOLTIP-TODO",
    )
    WeaponModelGender: int = ParamField(
        byte, "equipModelGender", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponCategory: int = ParamField(
        byte, "weaponCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackAnimationCategory: int = ParamField(
        byte, "wepmotionCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardAnimationCategory: int = ParamField(
        byte, "guardmotionCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        byte, "atkMaterial", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePhysics: int = ParamField(
        byte, "correctType_Physics", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialAttackCategory: int = ParamField(
        ushort, "spAtkcategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OneHandedAnimationCategory: int = ParamField(
        byte, "wepmotionOneHandId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TwoHandedAnimationCategory: int = ParamField(
        byte, "wepmotionBothHandId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredStrength: int = ParamField(
        byte, "properStrength", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredDexterity: int = ParamField(
        byte, "properAgility", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredIntelligence: int = ParamField(
        byte, "properMagic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequiredFaith: int = ParamField(
        byte, "properFaith", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverStrength: int = ParamField(
        byte, "overStrength", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseParry: int = ParamField(
        byte, "attackBaseParry", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseBaseParry: int = ParamField(
        byte, "defenseBaseParry", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeflectOnBlock: int = ParamField(
        byte, "guardBaseRepel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeflectOnAttack: int = ParamField(
        byte, "attackBaseRepel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreGuardPercentage: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        sbyte, "slashGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        sbyte, "blowGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        sbyte, "thrustGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonDamageReductionWhenGuarding: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToxicDamageReductionWhenGuarding: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BleedDamageReductionWhenGuarding: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseDamageReductionWhenGuarding: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHandAllowed: int = ParamField(
        byte, "rightHandEquipable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LeftHandAllowed: int = ParamField(
        byte, "leftHandEquipable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BothHandsAllowed: int = ParamField(
        byte, "bothHandEquipable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsesEquippedArrows: int = ParamField(
        byte, "arrowSlotEquipable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UsesEquippedBolts: int = ParamField(
        byte, "boltSlotEquipable:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardEnabled: int = ParamField(
        byte, "enableGuard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryEnabled: int = ParamField(
        byte, "enableParry:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanCastSorceries: int = ParamField(
        byte, "enableMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanCastPyromancy: int = ParamField(
        byte, "enableSorcery:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanCastMiracles: int = ParamField(
        byte, "enableMiracle:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanCastCovenantMagic: int = ParamField(
        byte, "enableVowMagic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DealsNeutralDamage: int = ParamField(
        byte, "isNormalAttackType:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DealsStrikeDamage: int = ParamField(
        byte, "isBlowAttackType:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DealsSlashDamage: int = ParamField(
        byte, "isSlashAttackType:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DealsThrustDamage: int = ParamField(
        byte, "isThrustAttackType:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUpgraded: int = ParamField(
        byte, "isEnhance:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHeroPointCorrect: int = ParamField(
        byte, "isHeroPointCorrect:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCustom: int = ParamField(
        byte, "isCustom:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableBaseChangeReset: int = ParamField(
        byte, "disableBaseChangeReset:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableRepairs: int = ParamField(
        byte, "disableRepair:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDarkHand: int = ParamField(
        byte, "isDarkHand:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SimpleDLCModelExists: int = ParamField(
        byte, "simpleModelForDlc:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsLantern: int = ParamField(
        byte, "lanternWep:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanHitGhosts: int = ParamField(
        byte, "isVersusGhostWep:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangeCategory: int = ParamField(
        byte, "baseChangeCategory:6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDragonSlayer: int = ParamField(
        byte, "isDragonSlayer:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeStored: int = ParamField(
        byte, "isDeposit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiplayerShare: int = ParamField(
        byte, "disableMultiDropShare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: int = ParamField(
        byte, "isDiscard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: int = ParamField(
        byte, "isDrop:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: int = ParamField(
        byte, "showLogCondType:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableThrow: int = ParamField(
        byte, "enableThrow:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    DisableGemAttr: int = ParamField(
        byte, "disableGemAttr:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        ushort, "defSfxMaterial1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType0: int = ParamField(
        byte, "wepCollidableType0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType1: int = ParamField(
        byte, "wepCollidableType1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PostureControlIdRight: int = ParamField(
        byte, "postureControlId_Right", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostureControlIdLeft: int = ParamField(
        byte, "postureControlId_Left", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId0: int = ParamField(
        int, "traceSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead0: int = ParamField(
        int, "traceDmyIdHead0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail0: int = ParamField(
        int, "traceDmyIdTail0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId1: int = ParamField(
        int, "traceSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead1: int = ParamField(
        int, "traceDmyIdHead1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail1: int = ParamField(
        int, "traceDmyIdTail1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId2: int = ParamField(
        int, "traceSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead2: int = ParamField(
        int, "traceDmyIdHead2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail2: int = ParamField(
        int, "traceDmyIdTail2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId3: int = ParamField(
        int, "traceSfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead3: int = ParamField(
        int, "traceDmyIdHead3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail3: int = ParamField(
        int, "traceDmyIdTail3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId4: int = ParamField(
        int, "traceSfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead4: int = ParamField(
        int, "traceDmyIdHead4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail4: int = ParamField(
        int, "traceDmyIdTail4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId5: int = ParamField(
        int, "traceSfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead5: int = ParamField(
        int, "traceDmyIdHead5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail5: int = ParamField(
        int, "traceDmyIdTail5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId6: int = ParamField(
        int, "traceSfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead6: int = ParamField(
        int, "traceDmyIdHead6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail6: int = ParamField(
        int, "traceDmyIdTail6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId7: int = ParamField(
        int, "traceSfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead7: int = ParamField(
        int, "traceDmyIdHead7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail7: int = ParamField(
        int, "traceDmyIdTail7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        ushort, "defSfxMaterial2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        ushort, "defSeMaterial2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AbsorpParamId: int = ParamField(
        int, "absorpParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IsValidToughProtSADmg: int = ParamField(
        byte, "isValidTough_ProtSADmg:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDualBlade: int = ParamField(
        byte, "isDualBlade:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoEquip: int = ParamField(
        byte, "isAutoEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableEmergencyStep: int = ParamField(
        byte, "isEnableEmergencyStep:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleInCutscenes: int = ParamField(
        byte, "invisibleOnRemo:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad2:3")
    CorrectTypeMagic: int = ParamField(
        byte, "correctType_Magic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeFire: int = ParamField(
        byte, "correctType_Fire", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeThunder: int = ParamField(
        byte, "correctType_Thunder", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeakEDamageRate: float = ParamField(
        float, "weakE_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakFDamageRate: float = ParamField(
        float, "weakF_DamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float, "darkGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseDark: int = ParamField(
        ushort, "attackBaseDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeDark: int = ParamField(
        byte, "correctType_Dark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePoison: int = ParamField(
        byte, "correctType_Poison", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute2: int = ParamField(
        byte, "atkAttribute2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResist: int = ParamField(
        sbyte, "sleepGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResist: int = ParamField(
        sbyte, "madnessGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeBlood: int = ParamField(
        byte, "correctType_Blood", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperLuck: int = ParamField(
        byte, "properLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResist: int = ParamField(
        sbyte, "freezeGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoReplenishType: int = ParamField(
        byte, "autoReplenishType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SwordArtsParamId: int = ParamField(
        int, "swordArtsParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectLuck: float = ParamField(
        float, "correctLuck", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltEquipId: int = ParamField(
        uint, "arrowBoltEquipId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DerivationLevelType: int = ParamField(
        byte, "DerivationLevelType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnchantSfxSize: int = ParamField(
        byte, "enchantSfxSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepType: int = ParamField(
        ushort, "wepType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysGuardCutRateMaxCorrect: float = ParamField(
        float, "physGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagGuardCutRateMaxCorrect: float = ParamField(
        float, "magGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRateMaxCorrect: float = ParamField(
        float, "fireGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunGuardCutRateMaxCorrect: float = ParamField(
        float, "thunGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRateMaxCorrect: float = ParamField(
        float, "darkGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResistMaxCorrect: float = ParamField(
        float, "poisonGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseGuardResistMaxCorrect: float = ParamField(
        float, "diseaseGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodGuardResistMaxCorrect: float = ParamField(
        float, "bloodGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResistMaxCorrect: float = ParamField(
        float, "curseGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResistMaxCorrect: float = ParamField(
        float, "freezeGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDefMaxCorrect: float = ParamField(
        float, "staminaGuardDef_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId1: int = ParamField(
        int, "residentSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId2: int = ParamField(
        int, "residentSfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId3: int = ParamField(
        int, "residentSfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId4: int = ParamField(
        int, "residentSfxId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId1: int = ParamField(
        int, "residentSfx_DmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId2: int = ParamField(
        int, "residentSfx_DmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId3: int = ParamField(
        int, "residentSfx_DmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId4: int = ParamField(
        int, "residentSfx_DmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StaminaConsumptionRate: float = ParamField(
        float, "staminaConsumptionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Physics", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMagic: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Magic", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFire: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Fire", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateThunder: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Thunder", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateDark: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Dark", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePoison: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Poison", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateBlood: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Blood", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFreeze: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Freeze", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusStr: int = ParamField(
        int, "attainmentWepStatusStr", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusDex: int = ParamField(
        int, "attainmentWepStatusDex", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusMag: int = ParamField(
        int, "attainmentWepStatusMag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusFai: int = ParamField(
        int, "attainmentWepStatusFai", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusLuc: int = ParamField(
        int, "attainmentWepStatusLuc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttackElementCorrectId: int = ParamField(
        int, "attackElementCorrectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceShopCategory: int = ParamField(
        byte, "reinforceShopCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxArrowQuantity: int = ParamField(
        byte, "maxArrowQuantity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx1IsVisibleForHang: int = ParamField(
        byte, "residentSfx_1_IsVisibleForHang:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx2IsVisibleForHang: int = ParamField(
        byte, "residentSfx_2_IsVisibleForHang:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx3IsVisibleForHang: int = ParamField(
        byte, "residentSfx_3_IsVisibleForHang:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx4IsVisibleForHang: int = ParamField(
        byte, "residentSfx_4_IsVisibleForHang:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel0: int = ParamField(
        byte, "isSoulParamIdChange_model0:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel1: int = ParamField(
        byte, "isSoulParamIdChange_model1:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel2: int = ParamField(
        byte, "isSoulParamIdChange_model2:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel3: int = ParamField(
        byte, "isSoulParamIdChange_model3:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WepSeIdOffset: int = ParamField(
        sbyte, "wepSeIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangePrice: int = ParamField(
        int, "baseChangePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LevelSyncCorrectID: int = ParamField(
        short, "levelSyncCorrectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeSleep: int = ParamField(
        byte, "correctType_Sleep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeMadness: int = ParamField(
        byte, "correctType_Madness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GemMountType: int = ParamField(
        byte, "gemMountType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponRegainHP: int = ParamField(
        ushort, "wepRegainHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId0: int = ParamField(
        int, "spEffectMsgId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId1: int = ParamField(
        int, "spEffectMsgId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId2: int = ParamField(
        int, "spEffectMsgId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep16: int = ParamField(
        int, "originEquipWep16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep17: int = ParamField(
        int, "originEquipWep17", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep18: int = ParamField(
        int, "originEquipWep18", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep19: int = ParamField(
        int, "originEquipWep19", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep20: int = ParamField(
        int, "originEquipWep20", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep21: int = ParamField(
        int, "originEquipWep21", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep22: int = ParamField(
        int, "originEquipWep22", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep23: int = ParamField(
        int, "originEquipWep23", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep24: int = ParamField(
        int, "originEquipWep24", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep25: int = ParamField(
        int, "originEquipWep25", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateSleep: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Sleep", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMadness: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Madness", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SaGuardCutRate: float = ParamField(
        float, "saGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefMaterialVariationValue: int = ParamField(
        byte, "defMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        byte, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StealthAtkRate: int = ParamField(
        short, "stealthAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateDisease: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Disease", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateCurse: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Curse", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad[8]")