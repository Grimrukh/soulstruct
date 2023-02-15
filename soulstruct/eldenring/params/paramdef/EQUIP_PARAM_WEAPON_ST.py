from __future__ import annotations

__all__ = ["EQUIP_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_WEAPON_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationId: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WanderingEquipId: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponWeightRate: float = ParamField(
        float, "weaponWeightRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FixPrice: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforcePrice: int = ParamField(
        int, "reinforcePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectStrength: float = ParamField(
        float, "correctStrength", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectAgility: float = ParamField(
        float, "correctAgility", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectMagic: float = ParamField(
        float, "correctMagic", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectFaith: float = ParamField(
        float, "correctFaith", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PhysGuardCutRate: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagGuardCutRate: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRate: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunGuardCutRate: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectBehaviorId0: int = ParamField(
        int, "spEffectBehaviorId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectBehaviorId1: int = ParamField(
        int, "spEffectBehaviorId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectBehaviorId2: int = ParamField(
        int, "spEffectBehaviorId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId: int = ParamField(
        int, "residentSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId1: int = ParamField(
        int, "residentSpEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId2: int = ParamField(
        int, "residentSpEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSetId: int = ParamField(
        int, "materialSetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep: int = ParamField(
        int, "originEquipWep", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep1: int = ParamField(
        int, "originEquipWep1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep2: int = ParamField(
        int, "originEquipWep2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep3: int = ParamField(
        int, "originEquipWep3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep4: int = ParamField(
        int, "originEquipWep4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep5: int = ParamField(
        int, "originEquipWep5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep6: int = ParamField(
        int, "originEquipWep6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep7: int = ParamField(
        int, "originEquipWep7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep8: int = ParamField(
        int, "originEquipWep8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep9: int = ParamField(
        int, "originEquipWep9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep10: int = ParamField(
        int, "originEquipWep10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep11: int = ParamField(
        int, "originEquipWep11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep12: int = ParamField(
        int, "originEquipWep12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep13: int = ParamField(
        int, "originEquipWep13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep14: int = ParamField(
        int, "originEquipWep14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep15: int = ParamField(
        int, "originEquipWep15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeakADamageRate: float = ParamField(
        float, "weakA_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakBDamageRate: float = ParamField(
        float, "weakB_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakCDamageRate: float = ParamField(
        float, "weakC_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDDamageRate: float = ParamField(
        float, "weakD_DamageRate", default=1.0,
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
    SaWeaponDamage: float = ParamField(
        float, "saWeaponDamage", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelId: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Durability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DurabilityMax: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackThrowEscape: int = ParamField(
        ushort, "attackThrowEscape", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryDamageLife: int = ParamField(
        short, "parryDamageLife", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttackBasePhysics: int = ParamField(
        ushort, "attackBasePhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseMagic: int = ParamField(
        ushort, "attackBaseMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseFire: int = ParamField(
        ushort, "attackBaseFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseThunder: int = ParamField(
        ushort, "attackBaseThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseStamina: int = ParamField(
        ushort, "attackBaseStamina", default=100,
        tooltip="TOOLTIP-TODO",
    )
    GuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaDurability: float = ParamField(
        float, "saDurability", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDef: int = ParamField(
        short, "staminaGuardDef", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceTypeId: int = ParamField(
        short, "reinforceTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrophySeqId: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ThrowAtkRate: int = ParamField(
        short, "throwAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BowDistRate: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=7,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponCategory: int = ParamField(
        byte, "weaponCategory", WEAPON_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepmotionCategory: int = ParamField(
        byte, "wepmotionCategory", WEPMOTION_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardmotionCategory: int = ParamField(
        byte, "guardmotionCategory", GUARDMOTION_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkMaterial: int = ParamField(
        byte, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePhysics: int = ParamField(
        byte, "correctType_Physics", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAtkcategory: int = ParamField(
        ushort, "spAtkcategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepmotionOneHandId: int = ParamField(
        byte, "wepmotionOneHandId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepmotionBothHandId: int = ParamField(
        byte, "wepmotionBothHandId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperStrength: int = ParamField(
        byte, "properStrength", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperAgility: int = ParamField(
        byte, "properAgility", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperMagic: int = ParamField(
        byte, "properMagic", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperFaith: int = ParamField(
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
    GuardBaseRepel: int = ParamField(
        byte, "guardBaseRepel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseRepel: int = ParamField(
        byte, "attackBaseRepel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardCutCancelRate: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashGuardCutRate: int = ParamField(
        sbyte, "slashGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowGuardCutRate: int = ParamField(
        sbyte, "blowGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustGuardCutRate: int = ParamField(
        sbyte, "thrustGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResist: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseGuardResist: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodGuardResist: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResist: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHandEquipable: bool = ParamField(
        byte, "rightHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    LeftHandEquipable: bool = ParamField(
        byte, "leftHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BothHandEquipable: bool = ParamField(
        byte, "bothHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ArrowSlotEquipable: bool = ParamField(
        byte, "arrowSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BoltSlotEquipable: bool = ParamField(
        byte, "boltSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableGuard: bool = ParamField(
        byte, "enableGuard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableParry: bool = ParamField(
        byte, "enableParry:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableMagic: bool = ParamField(
        byte, "enableMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableSorcery: bool = ParamField(
        byte, "enableSorcery:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableMiracle: bool = ParamField(
        byte, "enableMiracle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableVowMagic: bool = ParamField(
        byte, "enableVowMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsNormalAttackType: bool = ParamField(
        byte, "isNormalAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBlowAttackType: bool = ParamField(
        byte, "isBlowAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSlashAttackType: bool = ParamField(
        byte, "isSlashAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsThrustAttackType: bool = ParamField(
        byte, "isThrustAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnhance: bool = ParamField(
        byte, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHeroPointCorrect: bool = ParamField(
        byte, "isHeroPointCorrect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCustom: bool = ParamField(
        byte, "isCustom:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableBaseChangeReset: bool = ParamField(
        byte, "disableBaseChangeReset:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableRepair: bool = ParamField(
        byte, "disableRepair:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDarkHand: bool = ParamField(
        byte, "isDarkHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SimpleModelForDlc: bool = ParamField(
        byte, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    LanternWep: bool = ParamField(
        byte, "lanternWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVersusGhostWep: bool = ParamField(
        byte, "isVersusGhostWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangeCategory: int = ParamField(
        byte, "baseChangeCategory:6", WEP_BASE_CHANGE_CATEGORY, bit_count=6, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDragonSlayer: bool = ParamField(
        byte, "isDragonSlayer:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDeposit: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: bool = ParamField(
        byte, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: bool = ParamField(
        byte, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        byte, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableThrow: bool = ParamField(
        byte, "enableThrow:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    DisableGemAttr: bool = ParamField(
        byte, "disableGemAttr:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        ushort, "defSfxMaterial1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType0: int = ParamField(
        byte, "wepCollidableType0", WEP_COLLIDABLE_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType1: int = ParamField(
        byte, "wepCollidableType1", WEP_COLLIDABLE_TYPE, default=1,
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
        ushort, "defSfxMaterial2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        ushort, "defSeMaterial2", WEP_MATERIAL_DEF, default=0,
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
    IsValidToughProtSADmg: bool = ParamField(
        byte, "isValidTough_ProtSADmg:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDualBlade: bool = ParamField(
        byte, "isDualBlade:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoEquip: bool = ParamField(
        byte, "isAutoEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableEmergencyStep: bool = ParamField(
        byte, "isEnableEmergencyStep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleOnRemo: bool = ParamField(
        byte, "invisibleOnRemo:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad2:3", bit_count=3)
    CorrectTypeMagic: int = ParamField(
        byte, "correctType_Magic", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeFire: int = ParamField(
        byte, "correctType_Fire", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeThunder: int = ParamField(
        byte, "correctType_Thunder", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeakEDamageRate: float = ParamField(
        float, "weakE_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakFDamageRate: float = ParamField(
        float, "weakF_DamageRate", default=1.0,
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
        byte, "correctType_Dark", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePoison: int = ParamField(
        byte, "correctType_Poison", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute2: int = ParamField(
        byte, "atkAttribute2", ATKPARAM_ATKATTR_TYPE, default=0,
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
        byte, "correctType_Blood", WEP_CORRECT_TYPE, default=0,
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
        byte, "autoReplenishType", AUTO_REPLENISH_TYPE, default=0,
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
        byte, "DerivationLevelType", WEAPON_DERIVATION_LEVEL_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnchantSfxSize: int = ParamField(
        byte, "enchantSfxSize", WEP_ENCHANT_SFX_SIZE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepType: int = ParamField(
        ushort, "wepType", WEP_TYPE, default=0,
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
        float, "staminaConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePhysics: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMagic: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFire: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateThunder: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateDark: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePoison: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Poison", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateBlood: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Blood", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFreeze: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Freeze", default=1.0,
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
        byte, "reinforceShopCategory", REINFORCE_SHOP_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxArrowQuantity: int = ParamField(
        byte, "maxArrowQuantity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx1IsVisibleForHang: bool = ParamField(
        byte, "residentSfx_1_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx2IsVisibleForHang: bool = ParamField(
        byte, "residentSfx_2_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx3IsVisibleForHang: bool = ParamField(
        byte, "residentSfx_3_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx4IsVisibleForHang: bool = ParamField(
        byte, "residentSfx_4_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel0: bool = ParamField(
        byte, "isSoulParamIdChange_model0:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel1: bool = ParamField(
        byte, "isSoulParamIdChange_model1:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel2: bool = ParamField(
        byte, "isSoulParamIdChange_model2:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel3: bool = ParamField(
        byte, "isSoulParamIdChange_model3:1", EQUIP_BOOL, bit_count=1, default=True,
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
    LevelSyncCorrectId: int = ParamField(
        short, "levelSyncCorrectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeSleep: int = ParamField(
        byte, "correctType_Sleep", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeMadness: int = ParamField(
        byte, "correctType_Madness", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GemMountType: int = ParamField(
        byte, "gemMountType", GEM_MOUNT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepRegainHp: int = ParamField(
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
        float, "vsPlayerDmgCorrectRate_Sleep", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMadness: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Madness", default=1.0,
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
        float, "vsPlayerDmgCorrectRate_Disease", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateCurse: float = ParamField(
        float, "vsPlayerDmgCorrectRate_Curse", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad[8]")
