from __future__ import annotations

__all__ = ["EQUIP_PARAM_WEAPON_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_WEAPON_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="Multiplied by 1000 and added to player behavior lookups (hitboxes, bullets) triggered by TAE.",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostWeaponReplacement: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="Weapon replacement for ghosts.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="Weight of weapon.",
    )
    WeightRatio: float = ParamField(
        float, "weaponWeightRate", default=0.0,
        tooltip="Unknown effect. Value is about evenly split between 0 and 1 across weapons, with no obvious pattern.",
    )
    RepairCost: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
                "durability over max durability.",
    )
    ReinforcePrice: int = ParamField(
        int, "reinforcePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    StrengthScaling: float = ParamField(
        float, "correctStrength", default=0.0,
        tooltip="Amount of attack power gained from strength. (I believe this is the percentage of the player's "
                "strength to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    DexterityScaling: float = ParamField(
        float, "correctAgility", default=0.0,
        tooltip="Amount of attack power gained from dexterity. (I believe this is the percentage of the player's "
                "dexterity to add to the weapon's attack power, but it also depends on ScalingFormulaType below.).",
    )
    IntelligenceScaling: float = ParamField(
        float, "correctMagic", default=0.0,
        tooltip="Amount of attack power gained from intelligence. (I believe this is the percentage of the player's "
                "intelligence to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    FaithScaling: float = ParamField(
        float, "correctFaith", default=0.0,
        tooltip="Amount of attack power gained from faith. (I believe this is the percentage of the player's faith to "
                "add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    PhysicalGuardPercentage: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="Percentage of physical damage prevented when guarding with this weapon.",
    )
    MagicGuardPercentage: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="Percentage of magic damage prevented when guarding with this weapon.",
    )
    FireGuardPercentage: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="Percentage of fire damage prevented when guarding with this weapon.",
    )
    LightningGuardPercentage: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="Percentage of lightning damage prevented when guarding with this weapon.",
    )
    SpecialEffectOnHit0: int = ParamField(
        int, "spEffectBehaviorId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 0).",
    )
    SpecialEffectOnHit1: int = ParamField(
        int, "spEffectBehaviorId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 1).",
    )
    SpecialEffectOnHit2: int = ParamField(
        int, "spEffectBehaviorId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 2).",
    )
    EquippedSpecialEffect0: int = ParamField(
        int, "residentSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 0).",
    )
    EquippedSpecialEffect1: int = ParamField(
        int, "residentSpEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 1).",
    )
    EquippedSpecialEffect2: int = ParamField(
        int, "residentSpEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 2).",
    )
    UpgradeMaterialID: int = ParamField(
        int, "materialSetId", game_type=UpgradeMaterialParam, default=-1,
        tooltip="Upgrade Material parameter that sets costs for weapon reinforcement.",
    )
    UpgradeOrigin0: int = ParamField(
        int, "originEquipWep", default=-1,
        tooltip="Origin armor for level 0 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin1: int = ParamField(
        int, "originEquipWep1", default=-1,
        tooltip="Origin armor for level 1 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin2: int = ParamField(
        int, "originEquipWep2", default=-1,
        tooltip="Origin armor for level 2 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin3: int = ParamField(
        int, "originEquipWep3", default=-1,
        tooltip="Origin armor for level 3 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin4: int = ParamField(
        int, "originEquipWep4", default=-1,
        tooltip="Origin armor for level 4 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin5: int = ParamField(
        int, "originEquipWep5", default=-1,
        tooltip="Origin armor for level 5 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin6: int = ParamField(
        int, "originEquipWep6", default=-1,
        tooltip="Origin armor for level 6 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin7: int = ParamField(
        int, "originEquipWep7", default=-1,
        tooltip="Origin armor for level 7 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin8: int = ParamField(
        int, "originEquipWep8", default=-1,
        tooltip="Origin armor for level 8 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin9: int = ParamField(
        int, "originEquipWep9", default=-1,
        tooltip="Origin armor for level 9 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin10: int = ParamField(
        int, "originEquipWep10", default=-1,
        tooltip="Origin armor for level 10 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin11: int = ParamField(
        int, "originEquipWep11", default=-1,
        tooltip="Origin armor for level 11 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin12: int = ParamField(
        int, "originEquipWep12", default=-1,
        tooltip="Origin armor for level 12 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin13: int = ParamField(
        int, "originEquipWep13", default=-1,
        tooltip="Origin armor for level 13 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin14: int = ParamField(
        int, "originEquipWep14", default=-1,
        tooltip="Origin armor for level 14 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin15: int = ParamField(
        int, "originEquipWep15", default=-1,
        tooltip="Origin armor for level 15 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
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
    BasePoiseDamage: float = ParamField(
        float, "saWeaponDamage", default=0.0,
        tooltip="Base poise damage of weapon attacks.",
    )
    WeaponModel: int = ParamField(
        ushort, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Weapon model ID.",
    )
    WeaponIcon: int = ParamField(
        ushort, "iconId", game_type=Icon, default=0,
        tooltip="Weapon icon texture ID.",
    )
    InitialDurability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="Durability of weapon when it is obtained. Always equal to max durability in vanilla game.",
    )
    MaxDurability: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="Maximum durability of weapon.",
    )
    ThrowEscapePower: int = ParamField(
        ushort, "attackThrowEscape", default=0,
        tooltip="Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement "
                "weapons.",
    )
    MaxParryWindowDuration: int = ParamField(
        short, "parryDamageLife", default=-1,
        tooltip="Maximum parry window duration (cannot exceed TAE duration). Always set to 10.",
    )
    BasePhysicalDamage: int = ParamField(
        ushort, "attackBasePhysics", default=100,
        tooltip="Base physical damage of weapon attacks.",
    )
    BaseMagicDamage: int = ParamField(
        ushort, "attackBaseMagic", default=100,
        tooltip="Base magic damage of weapon attacks.",
    )
    BaseFireDamage: int = ParamField(
        ushort, "attackBaseFire", default=100,
        tooltip="Base fire damage of weapon attacks.",
    )
    BaseLightningDamage: int = ParamField(
        ushort, "attackBaseThunder", default=100,
        tooltip="Base lightning damage of weapon attacks.",
    )
    BaseStaminaDamage: int = ParamField(
        ushort, "attackBaseStamina", default=100,
        tooltip="Base stamina damage of weapon attacks.",
    )
    EffectiveGuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="Angle that can be guarded with this weapon. Never used.",
    )
    AttackPoiseBonus: float = ParamField(
        float, "saDurability", default=0.0,
        tooltip="Poise gained during attack animations with this weapon. Never used (probably done in TAE).",
    )
    GuardStaminaDefense: int = ParamField(
        short, "staminaGuardDef", default=0,
        tooltip="Defense against (i.e. value subtracted from) stamina attack damage while guarding.",
    )
    WeaponUpgradeID: int = ParamField(
        short, "reinforceTypeId", game_type=WeaponUpgradeParam, default=0,
        tooltip="Weapon Upgrade parameter that specifies upgrade benefits.",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxUpgradeAchievementID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when weapon is upgraded to maximum level (one per upgrade path).",
    )
    ThrowDamageChangePercentage: int = ParamField(
        short, "throwAtkRate", default=0,
        tooltip="Percentage damage increase (if positive) or decrease (if negative) during backstabs and ripostes "
                "with this weapon.",
    )
    BowRangeChangePercentage: int = ParamField(
        short, "bowDistRate", default=0,
        tooltip="Percentage range increase (if positive) or decrease (if negative) with this bow.",
    )
    WeaponModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=7,
        tooltip="Model category for equipment. Only one option for weapons.",
    )
    WeaponModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Model gender variant. All weapons are genderless.",
    )
    WeaponCategory: int = ParamField(
        byte, "weaponCategory", WEAPON_CATEGORY, default=0,
        tooltip="Basic category of weapon. Many 'weapon types' you may be familiar with are merged here (e.g. whips "
                "are straight swords).",
    )
    AttackAnimationCategory: int = ParamField(
        byte, "wepmotionCategory", WEPMOTION_CATEGORY, default=0,
        tooltip="Basic weapon attack animation type. More diverse than WeaponCategory. This number is multiplied by "
                "10000 and used as an animation offset for all attacks, I believe.",
    )
    GuardAnimationCategory: int = ParamField(
        byte, "guardmotionCategory", GUARDMOTION_CATEGORY, default=0,
        tooltip="Basic weapon/shield block animation type.",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        byte, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="Determines the sounds and visual effects generated when this weapon hits.",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePhysics: int = ParamField(
        byte, "correctType_Physics", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Element attached to hits with this weapon.",
    )
    SpecialAttackCategory: int = ParamField(
        ushort, "spAtkcategory", default=0,
        tooltip="Overrides AttackAnimationCategory for some attacks. Ranges from 50 to 199 (or 0 for none). Often "
                "used to give weapons unique strong (R2) attacks, for example, but can override any attack animation.",
    )
    OneHandedAnimationCategory: int = ParamField(
        byte, "wepmotionOneHandId", default=0,
        tooltip="Animation category for one-handed non-attack animations (like walking).",
    )
    TwoHandedAnimationCategory: int = ParamField(
        byte, "wepmotionBothHandId", default=0,
        tooltip="Animation category for two-handed non-attack animations (like walking).",
    )
    RequiredStrength: int = ParamField(
        byte, "properStrength", default=0,
        tooltip="Required strength to wield weapon properly. (Reduced by one third if held two-handed.)",
    )
    RequiredDexterity: int = ParamField(
        byte, "properAgility", default=0,
        tooltip="Required dexterity to wield weapon properly.",
    )
    RequiredIntelligence: int = ParamField(
        byte, "properMagic", default=0,
        tooltip="Required intelligence to wield weapon properly.",
    )
    RequiredFaith: int = ParamField(
        byte, "properFaith", default=0,
        tooltip="Required faith to wield weapon properly.",
    )
    OverStrength: int = ParamField(
        byte, "overStrength", default=0,
        tooltip="Unknown. Always set to 99, except for arrows and bolts.",
    )
    AttackBaseParry: int = ParamField(
        byte, "attackBaseParry", default=0,
        tooltip="Unknown. Never used.",
    )
    DefenseBaseParry: int = ParamField(
        byte, "defenseBaseParry", default=0,
        tooltip="Unknown. Never used.",
    )
    DeflectOnBlock: int = ParamField(
        byte, "guardBaseRepel", default=0,
        tooltip="Determines if an enemy will be deflected when you block them with this weapon (by comparing it to "
                "their DeflectOnAttack).",
    )
    DeflectOnAttack: int = ParamField(
        byte, "attackBaseRepel", default=0,
        tooltip="Determines if this weapon will be deflected when attacking a blocking enemy (by comparing it to "
                "their DeflectOnBlock).",
    )
    IgnoreGuardPercentage: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
                "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in "
                "favor of the simple 'IgnoreGuard' boolean field.",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="Internal description: 'in which guard motion is the enemy attacked when guarded?' Exact effects are "
                "unclear, but this ranges from 0 to 4 in effectiveness of blocking in a predictable way (daggers are "
                "worse than swords, which are worse than greatswords, which are worse than all shields).",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        sbyte, "slashGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        sbyte, "blowGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        sbyte, "thrustGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    PoisonDamageReductionWhenGuarding: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="Percentage of incoming poison damage ignored when guarding.",
    )
    ToxicDamageReductionWhenGuarding: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="Percentage of incoming toxic damage ignored when guarding.",
    )
    BleedDamageReductionWhenGuarding: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="Percentage of incoming bleed damage ignored when guarding.",
    )
    CurseDamageReductionWhenGuarding: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="Percentage of incoming curse damage ignored when guarding.",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHandAllowed: bool = ParamField(
        byte, "rightHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be equipped in the right hand.",
    )
    LeftHandAllowed: bool = ParamField(
        byte, "leftHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be equipped in the left hand.",
    )
    BothHandsAllowed: bool = ParamField(
        byte, "bothHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be held in two-handed mode.",
    )
    UsesEquippedArrows: bool = ParamField(
        byte, "arrowSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon will use equipped arrow slot.",
    )
    UsesEquippedBolts: bool = ParamField(
        byte, "boltSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon will use equipped bolt slot.",
    )
    GuardEnabled: bool = ParamField(
        byte, "enableGuard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the player can guard with this weapon by holding L1.",
    )
    ParryEnabled: bool = ParamField(
        byte, "enableParry:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the player can parry with this weapon by pressing L2.",
    )
    CanCastSorceries: bool = ParamField(
        byte, "enableMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast sorceries.",
    )
    CanCastPyromancy: bool = ParamField(
        byte, "enableSorcery:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast pyromancy.",
    )
    CanCastMiracles: bool = ParamField(
        byte, "enableMiracle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast miracles.",
    )
    CanCastCovenantMagic: bool = ParamField(
        byte, "enableVowMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsNeutralDamage: bool = ParamField(
        byte, "isNormalAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsStrikeDamage: bool = ParamField(
        byte, "isBlowAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsSlashDamage: bool = ParamField(
        byte, "isSlashAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsThrustDamage: bool = ParamField(
        byte, "isThrustAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsUpgraded: bool = ParamField(
        byte, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsHeroPointCorrect: bool = ParamField(
        byte, "isHeroPointCorrect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCustom: bool = ParamField(
        byte, "isCustom:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableBaseChangeReset: bool = ParamField(
        byte, "disableBaseChangeReset:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableRepairs: bool = ParamField(
        byte, "disableRepair:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon cannot be repaired.",
    )
    IsDarkHand: bool = ParamField(
        byte, "isDarkHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Enabled only for the Dark Hand.",
    )
    SimpleDLCModelExists: bool = ParamField(
        byte, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    IsLantern: bool = ParamField(
        byte, "lanternWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanHitGhosts: bool = ParamField(
        byte, "isVersusGhostWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can hit ghosts without a Transient Curse active.",
    )
    BaseChangeCategory: int = ParamField(
        byte, "baseChangeCategory:6", WEP_BASE_CHANGE_CATEGORY, bit_count=6, default=0,
        tooltip="Never used. Likely Demon's Souls junk.",
    )
    IsDragonSlayer: bool = ParamField(
        byte, "isDragonSlayer:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be stored in storage. Always True for rings.",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon cannot be given to other players by dropping it. Always False in vanilla.",
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
    InvisibleInCutscenes: bool = ParamField(
        byte, "invisibleOnRemo:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
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
    LevelSyncCorrectID: int = ParamField(
        short, "levelSyncCorrectId", default=-1,
        tooltip="TODO",
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
    WeaponRegainHP: int = ParamField(
        ushort, "wepRegainHp", default=0,
        tooltip="TODO",
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
