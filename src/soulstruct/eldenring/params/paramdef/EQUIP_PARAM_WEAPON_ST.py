from __future__ import annotations

__all__ = ["EQUIP_PARAM_WEAPON_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_WEAPON_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int32, "behaviorVariationId", default=0,
        tooltip="Multiplied by 1000 and added to player behavior lookups (hitboxes, bullets) triggered by TAE.",
    )
    SortIndex: int = ParamField(
        int32, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostWeaponReplacement: int = ParamField(
        uint32, "wanderingEquipId", default=0,
        tooltip="Weapon replacement for ghosts.",
    )
    Weight: float = ParamField(
        float32, "weight", default=1.0,
        tooltip="Weight of weapon.",
    )
    WeightRatio: float = ParamField(
        float32, "weaponWeightRate", default=0.0,
        tooltip="Unknown effect. Value is about evenly split between 0 and 1 across weapons, with no obvious pattern.",
    )
    RepairCost: int = ParamField(
        int32, "fixPrice", default=0,
        tooltip="Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
                "durability over max durability.",
    )
    ReinforcePrice: int = ParamField(
        int32, "reinforcePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int32, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    StrengthScaling: float = ParamField(
        float32, "correctStrength", default=0.0,
        tooltip="Amount of attack power gained from strength. (I believe this is the percentage of the player's "
                "strength to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    DexterityScaling: float = ParamField(
        float32, "correctAgility", default=0.0,
        tooltip="Amount of attack power gained from dexterity. (I believe this is the percentage of the player's "
                "dexterity to add to the weapon's attack power, but it also depends on ScalingFormulaType below.).",
    )
    IntelligenceScaling: float = ParamField(
        float32, "correctMagic", default=0.0,
        tooltip="Amount of attack power gained from intelligence. (I believe this is the percentage of the player's "
                "intelligence to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    FaithScaling: float = ParamField(
        float32, "correctFaith", default=0.0,
        tooltip="Amount of attack power gained from faith. (I believe this is the percentage of the player's faith to "
                "add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
    )
    PhysicalGuardPercentage: float = ParamField(
        float32, "physGuardCutRate", default=0.0,
        tooltip="Percentage of physical damage prevented when guarding with this weapon.",
    )
    MagicGuardPercentage: float = ParamField(
        float32, "magGuardCutRate", default=0.0,
        tooltip="Percentage of magic damage prevented when guarding with this weapon.",
    )
    FireGuardPercentage: float = ParamField(
        float32, "fireGuardCutRate", default=0.0,
        tooltip="Percentage of fire damage prevented when guarding with this weapon.",
    )
    LightningGuardPercentage: float = ParamField(
        float32, "thunGuardCutRate", default=0.0,
        tooltip="Percentage of lightning damage prevented when guarding with this weapon.",
    )
    SpecialEffectOnHit0: int = ParamField(
        int32, "spEffectBehaviorId0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 0).",
    )
    SpecialEffectOnHit1: int = ParamField(
        int32, "spEffectBehaviorId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 1).",
    )
    SpecialEffectOnHit2: int = ParamField(
        int32, "spEffectBehaviorId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to struck target (slot 2).",
    )
    EquippedSpecialEffect0: int = ParamField(
        int32, "residentSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 0).",
    )
    EquippedSpecialEffect1: int = ParamField(
        int32, "residentSpEffectId1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 1).",
    )
    EquippedSpecialEffect2: int = ParamField(
        int32, "residentSpEffectId2", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect granted to character with weapon equipped (slot 2).",
    )
    UpgradeMaterialID: int = ParamField(
        int32, "materialSetId", game_type=UpgradeMaterialParam, default=-1,
        tooltip="Upgrade Material parameter that sets costs for weapon reinforcement.",
    )
    UpgradeOrigin0: int = ParamField(
        int32, "originEquipWep", default=-1,
        tooltip="Origin armor for level 0 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin1: int = ParamField(
        int32, "originEquipWep1", default=-1,
        tooltip="Origin armor for level 1 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin2: int = ParamField(
        int32, "originEquipWep2", default=-1,
        tooltip="Origin armor for level 2 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin3: int = ParamField(
        int32, "originEquipWep3", default=-1,
        tooltip="Origin armor for level 3 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin4: int = ParamField(
        int32, "originEquipWep4", default=-1,
        tooltip="Origin armor for level 4 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin5: int = ParamField(
        int32, "originEquipWep5", default=-1,
        tooltip="Origin armor for level 5 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin6: int = ParamField(
        int32, "originEquipWep6", default=-1,
        tooltip="Origin armor for level 6 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin7: int = ParamField(
        int32, "originEquipWep7", default=-1,
        tooltip="Origin armor for level 7 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin8: int = ParamField(
        int32, "originEquipWep8", default=-1,
        tooltip="Origin armor for level 8 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin9: int = ParamField(
        int32, "originEquipWep9", default=-1,
        tooltip="Origin armor for level 9 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin10: int = ParamField(
        int32, "originEquipWep10", default=-1,
        tooltip="Origin armor for level 10 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin11: int = ParamField(
        int32, "originEquipWep11", default=-1,
        tooltip="Origin armor for level 11 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin12: int = ParamField(
        int32, "originEquipWep12", default=-1,
        tooltip="Origin armor for level 12 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin13: int = ParamField(
        int32, "originEquipWep13", default=-1,
        tooltip="Origin armor for level 13 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin14: int = ParamField(
        int32, "originEquipWep14", default=-1,
        tooltip="Origin armor for level 14 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin15: int = ParamField(
        int32, "originEquipWep15", default=-1,
        tooltip="Origin armor for level 15 of this weapon (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    WeakADamageRate: float = ParamField(
        float32, "weakA_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakBDamageRate: float = ParamField(
        float32, "weakB_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakCDamageRate: float = ParamField(
        float32, "weakC_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakDDamageRate: float = ParamField(
        float32, "weakD_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResistMaxCorrect: float = ParamField(
        float32, "sleepGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResistMaxCorrect: float = ParamField(
        float32, "madnessGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BasePoiseDamage: float = ParamField(
        float32, "saWeaponDamage", default=0.0,
        tooltip="Base poise damage of weapon attacks.",
    )
    WeaponModel: int = ParamField(
        uint16, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Weapon model ID.",
    )
    WeaponIcon: int = ParamField(
        uint16, "iconId", game_type=Icon, default=0,
        tooltip="Weapon icon texture ID.",
    )
    InitialDurability: int = ParamField(
        uint16, "durability", default=100,
        tooltip="Durability of weapon when it is obtained. Always equal to max durability in vanilla game.",
    )
    MaxDurability: int = ParamField(
        uint16, "durabilityMax", default=100,
        tooltip="Maximum durability of weapon.",
    )
    ThrowEscapePower: int = ParamField(
        uint16, "attackThrowEscape", default=0,
        tooltip="Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement "
                "weapons.",
    )
    MaxParryWindowDuration: int = ParamField(
        int16, "parryDamageLife", default=-1,
        tooltip="Maximum parry window duration (cannot exceed TAE duration). Always set to 10.",
    )
    BasePhysicalDamage: int = ParamField(
        uint16, "attackBasePhysics", default=100,
        tooltip="Base physical damage of weapon attacks.",
    )
    BaseMagicDamage: int = ParamField(
        uint16, "attackBaseMagic", default=100,
        tooltip="Base magic damage of weapon attacks.",
    )
    BaseFireDamage: int = ParamField(
        uint16, "attackBaseFire", default=100,
        tooltip="Base fire damage of weapon attacks.",
    )
    BaseLightningDamage: int = ParamField(
        uint16, "attackBaseThunder", default=100,
        tooltip="Base lightning damage of weapon attacks.",
    )
    BaseStaminaDamage: int = ParamField(
        uint16, "attackBaseStamina", default=100,
        tooltip="Base stamina damage of weapon attacks.",
    )
    EffectiveGuardAngle: int = ParamField(
        int16, "guardAngle", default=0,
        tooltip="Angle that can be guarded with this weapon. Never used.",
    )
    AttackPoiseBonus: float = ParamField(
        float32, "saDurability", default=0.0,
        tooltip="Poise gained during attack animations with this weapon. Never used (probably done in TAE).",
    )
    GuardStaminaDefense: int = ParamField(
        int16, "staminaGuardDef", default=0,
        tooltip="Defense against (i.e. value subtracted from) stamina attack damage while guarding.",
    )
    WeaponUpgradeID: int = ParamField(
        int16, "reinforceTypeId", game_type=WeaponUpgradeParam, default=0,
        tooltip="Weapon Upgrade parameter that specifies upgrade benefits.",
    )
    TrophySGradeId: int = ParamField(
        int16, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxUpgradeAchievementID: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when weapon is upgraded to maximum level (one per upgrade path).",
    )
    ThrowDamageChangePercentage: int = ParamField(
        int16, "throwAtkRate", default=0,
        tooltip="Percentage damage increase (if positive) or decrease (if negative) during backstabs and ripostes "
                "with this weapon.",
    )
    BowRangeChangePercentage: int = ParamField(
        int16, "bowDistRate", default=0,
        tooltip="Percentage range increase (if positive) or decrease (if negative) with this bow.",
    )
    WeaponModelCategory: int = ParamField(
        uint8, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=7,
        tooltip="Model category for equipment. Only one option for weapons.",
    )
    WeaponModelGender: int = ParamField(
        uint8, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Model gender variant. All weapons are genderless.",
    )
    WeaponCategory: int = ParamField(
        uint8, "weaponCategory", WEAPON_CATEGORY, default=0,
        tooltip="Basic category of weapon. Many 'weapon types' you may be familiar with are merged here (e.g. whips "
                "are straight swords).",
    )
    AttackAnimationCategory: int = ParamField(
        uint8, "wepmotionCategory", WEPMOTION_CATEGORY, default=0,
        tooltip="Basic weapon attack animation type. More diverse than WeaponCategory. This number is multiplied by "
                "10000 and used as an animation offset for all attacks, I believe.",
    )
    GuardAnimationCategory: int = ParamField(
        uint8, "guardmotionCategory", GUARDMOTION_CATEGORY, default=0,
        tooltip="Basic weapon/shield block animation type.",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        uint8, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="Determines the sounds and visual effects generated when this weapon hits.",
    )
    DefSeMaterial1: int = ParamField(
        uint16, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePhysics: int = ParamField(
        uint8, "correctType_Physics", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Element attached to hits with this weapon.",
    )
    SpecialAttackCategory: int = ParamField(
        uint16, "spAtkcategory", default=0,
        tooltip="Overrides AttackAnimationCategory for some attacks. Ranges from 50 to 199 (or 0 for none). Often "
                "used to give weapons unique strong (R2) attacks, for example, but can override any attack animation.",
    )
    OneHandedAnimationCategory: int = ParamField(
        uint8, "wepmotionOneHandId", default=0,
        tooltip="Animation category for one-handed non-attack animations (like walking).",
    )
    TwoHandedAnimationCategory: int = ParamField(
        uint8, "wepmotionBothHandId", default=0,
        tooltip="Animation category for two-handed non-attack animations (like walking).",
    )
    RequiredStrength: int = ParamField(
        uint8, "properStrength", default=0,
        tooltip="Required strength to wield weapon properly. (Reduced by one third if held two-handed.)",
    )
    RequiredDexterity: int = ParamField(
        uint8, "properAgility", default=0,
        tooltip="Required dexterity to wield weapon properly.",
    )
    RequiredIntelligence: int = ParamField(
        uint8, "properMagic", default=0,
        tooltip="Required intelligence to wield weapon properly.",
    )
    RequiredFaith: int = ParamField(
        uint8, "properFaith", default=0,
        tooltip="Required faith to wield weapon properly.",
    )
    OverStrength: int = ParamField(
        uint8, "overStrength", default=0,
        tooltip="Unknown. Always set to 99, except for arrows and bolts.",
    )
    AttackBaseParry: int = ParamField(
        uint8, "attackBaseParry", default=0,
        tooltip="Unknown. Never used.",
    )
    DefenseBaseParry: int = ParamField(
        uint8, "defenseBaseParry", default=0,
        tooltip="Unknown. Never used.",
    )
    DeflectOnBlock: int = ParamField(
        uint8, "guardBaseRepel", default=0,
        tooltip="Determines if an enemy will be deflected when you block them with this weapon (by comparing it to "
                "their DeflectOnAttack).",
    )
    DeflectOnAttack: int = ParamField(
        uint8, "attackBaseRepel", default=0,
        tooltip="Determines if this weapon will be deflected when attacking a blocking enemy (by comparing it to "
                "their DeflectOnBlock).",
    )
    IgnoreGuardPercentage: int = ParamField(
        int8, "guardCutCancelRate", default=0,
        tooltip="Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
                "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in "
                "favor of the simple 'IgnoreGuard' boolean field.",
    )
    GuardLevel: int = ParamField(
        int8, "guardLevel", default=0,
        tooltip="Internal description: 'in which guard motion is the enemy attacked when guarded?' Exact effects are "
                "unclear, but this ranges from 0 to 4 in effectiveness of blocking in a predictable way (daggers are "
                "worse than swords, which are worse than greatswords, which are worse than all shields).",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        int8, "slashGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        int8, "blowGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        int8, "thrustGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    PoisonDamageReductionWhenGuarding: int = ParamField(
        int8, "poisonGuardResist", default=0,
        tooltip="Percentage of incoming poison damage ignored when guarding.",
    )
    ToxicDamageReductionWhenGuarding: int = ParamField(
        int8, "diseaseGuardResist", default=0,
        tooltip="Percentage of incoming toxic damage ignored when guarding.",
    )
    BleedDamageReductionWhenGuarding: int = ParamField(
        int8, "bloodGuardResist", default=0,
        tooltip="Percentage of incoming bleed damage ignored when guarding.",
    )
    CurseDamageReductionWhenGuarding: int = ParamField(
        int8, "curseGuardResist", default=0,
        tooltip="Percentage of incoming curse damage ignored when guarding.",
    )
    AtkAttribute: int = ParamField(
        uint8, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHandAllowed: bool = ParamField(
        uint8, "rightHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be equipped in the right hand.",
    )
    LeftHandAllowed: bool = ParamField(
        uint8, "leftHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be equipped in the left hand.",
    )
    BothHandsAllowed: bool = ParamField(
        uint8, "bothHandEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be held in two-handed mode.",
    )
    UsesEquippedArrows: bool = ParamField(
        uint8, "arrowSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon will use equipped arrow slot.",
    )
    UsesEquippedBolts: bool = ParamField(
        uint8, "boltSlotEquipable:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon will use equipped bolt slot.",
    )
    GuardEnabled: bool = ParamField(
        uint8, "enableGuard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the player can guard with this weapon by holding L1.",
    )
    ParryEnabled: bool = ParamField(
        uint8, "enableParry:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the player can parry with this weapon by pressing L2.",
    )
    CanCastSorceries: bool = ParamField(
        uint8, "enableMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast sorceries.",
    )
    CanCastPyromancy: bool = ParamField(
        uint8, "enableSorcery:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast pyromancy.",
    )
    CanCastMiracles: bool = ParamField(
        uint8, "enableMiracle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be used to cast miracles.",
    )
    CanCastCovenantMagic: bool = ParamField(
        uint8, "enableVowMagic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsNeutralDamage: bool = ParamField(
        uint8, "isNormalAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsStrikeDamage: bool = ParamField(
        uint8, "isBlowAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsSlashDamage: bool = ParamField(
        uint8, "isSlashAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DealsThrustDamage: bool = ParamField(
        uint8, "isThrustAttackType:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsUpgraded: bool = ParamField(
        uint8, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsHeroPointCorrect: bool = ParamField(
        uint8, "isHeroPointCorrect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCustom: bool = ParamField(
        uint8, "isCustom:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableBaseChangeReset: bool = ParamField(
        uint8, "disableBaseChangeReset:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableRepairs: bool = ParamField(
        uint8, "disableRepair:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon cannot be repaired.",
    )
    IsDarkHand: bool = ParamField(
        uint8, "isDarkHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Enabled only for the Dark Hand.",
    )
    SimpleDLCModelExists: bool = ParamField(
        uint8, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    IsLantern: bool = ParamField(
        uint8, "lanternWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanHitGhosts: bool = ParamField(
        uint8, "isVersusGhostWep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can hit ghosts without a Transient Curse active.",
    )
    BaseChangeCategory: int = ParamField(
        uint8, "baseChangeCategory:6", WEP_BASE_CHANGE_CATEGORY, bit_count=6, default=0,
        tooltip="Never used. Likely Demon's Souls junk.",
    )
    IsDragonSlayer: bool = ParamField(
        uint8, "isDragonSlayer:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    CanBeStored: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon can be stored in storage. Always True for rings.",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon cannot be given to other players by dropping it. Always False in vanilla.",
    )
    IsDiscard: bool = ParamField(
        uint8, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: bool = ParamField(
        uint8, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        uint8, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableThrow: bool = ParamField(
        uint8, "enableThrow:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        uint8, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    DisableGemAttr: bool = ParamField(
        uint8, "disableGemAttr:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        uint16, "defSfxMaterial1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType0: int = ParamField(
        uint8, "wepCollidableType0", WEP_COLLIDABLE_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    WepCollidableType1: int = ParamField(
        uint8, "wepCollidableType1", WEP_COLLIDABLE_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    PostureControlIdRight: int = ParamField(
        uint8, "postureControlId_Right", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PostureControlIdLeft: int = ParamField(
        uint8, "postureControlId_Left", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId0: int = ParamField(
        int32, "traceSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead0: int = ParamField(
        int32, "traceDmyIdHead0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail0: int = ParamField(
        int32, "traceDmyIdTail0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId1: int = ParamField(
        int32, "traceSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead1: int = ParamField(
        int32, "traceDmyIdHead1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail1: int = ParamField(
        int32, "traceDmyIdTail1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId2: int = ParamField(
        int32, "traceSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead2: int = ParamField(
        int32, "traceDmyIdHead2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail2: int = ParamField(
        int32, "traceDmyIdTail2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId3: int = ParamField(
        int32, "traceSfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead3: int = ParamField(
        int32, "traceDmyIdHead3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail3: int = ParamField(
        int32, "traceDmyIdTail3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId4: int = ParamField(
        int32, "traceSfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead4: int = ParamField(
        int32, "traceDmyIdHead4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail4: int = ParamField(
        int32, "traceDmyIdTail4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId5: int = ParamField(
        int32, "traceSfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead5: int = ParamField(
        int32, "traceDmyIdHead5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail5: int = ParamField(
        int32, "traceDmyIdTail5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId6: int = ParamField(
        int32, "traceSfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead6: int = ParamField(
        int32, "traceDmyIdHead6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail6: int = ParamField(
        int32, "traceDmyIdTail6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId7: int = ParamField(
        int32, "traceSfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead7: int = ParamField(
        int32, "traceDmyIdHead7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail7: int = ParamField(
        int32, "traceDmyIdTail7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        uint16, "defSfxMaterial2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        uint16, "defSeMaterial2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AbsorpParamId: int = ParamField(
        int32, "absorpParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float32, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IsValidToughProtSADmg: bool = ParamField(
        uint8, "isValidTough_ProtSADmg:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDualBlade: bool = ParamField(
        uint8, "isDualBlade:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoEquip: bool = ParamField(
        uint8, "isAutoEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableEmergencyStep: bool = ParamField(
        uint8, "isEnableEmergencyStep:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleInCutscenes: bool = ParamField(
        uint8, "invisibleOnRemo:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    Unknown0x17c5: bool = ParamField(
        uint8, "unknown_0x17c_5:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    QuickMatchReplenish: bool = ParamField(
        uint8, "quickMatchReplenish:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeaponCatalyst: bool = ParamField(
        uint8, "isWeaponCatalyst:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeMagic: int = ParamField(
        uint8, "correctType_Magic", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeFire: int = ParamField(
        uint8, "correctType_Fire", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeThunder: int = ParamField(
        uint8, "correctType_Thunder", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeakEDamageRate: float = ParamField(
        float32, "weakE_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakFDamageRate: float = ParamField(
        float32, "weakF_DamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float32, "darkGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AttackBaseDark: int = ParamField(
        uint16, "attackBaseDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeDark: int = ParamField(
        uint8, "correctType_Dark", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypePoison: int = ParamField(
        uint8, "correctType_Poison", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        uint8, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute2: int = ParamField(
        uint8, "atkAttribute2", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResist: int = ParamField(
        int8, "sleepGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResist: int = ParamField(
        int8, "madnessGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeBlood: int = ParamField(
        uint8, "correctType_Blood", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProperLuck: int = ParamField(
        uint8, "properLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResist: int = ParamField(
        int8, "freezeGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoReplenishType: int = ParamField(
        uint8, "autoReplenishType", AUTO_REPLENISH_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SwordArtsParamId: int = ParamField(
        int32, "swordArtsParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectLuck: float = ParamField(
        float32, "correctLuck", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowBoltEquipId: int = ParamField(
        uint32, "arrowBoltEquipId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DerivationLevelType: int = ParamField(
        uint8, "DerivationLevelType", WEAPON_DERIVATION_LEVEL_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnchantSfxSize: int = ParamField(
        uint8, "enchantSfxSize", WEP_ENCHANT_SFX_SIZE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepType: int = ParamField(
        uint16, "wepType", WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysGuardCutRateMaxCorrect: float = ParamField(
        float32, "physGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagGuardCutRateMaxCorrect: float = ParamField(
        float32, "magGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRateMaxCorrect: float = ParamField(
        float32, "fireGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunGuardCutRateMaxCorrect: float = ParamField(
        float32, "thunGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRateMaxCorrect: float = ParamField(
        float32, "darkGuardCutRate_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResistMaxCorrect: float = ParamField(
        float32, "poisonGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseGuardResistMaxCorrect: float = ParamField(
        float32, "diseaseGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BloodGuardResistMaxCorrect: float = ParamField(
        float32, "bloodGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResistMaxCorrect: float = ParamField(
        float32, "curseGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResistMaxCorrect: float = ParamField(
        float32, "freezeGuardResist_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDefMaxCorrect: float = ParamField(
        float32, "staminaGuardDef_MaxCorrect", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId1: int = ParamField(
        int32, "residentSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId2: int = ParamField(
        int32, "residentSfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId3: int = ParamField(
        int32, "residentSfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxId4: int = ParamField(
        int32, "residentSfxId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId1: int = ParamField(
        int32, "residentSfx_DmyId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId2: int = ParamField(
        int32, "residentSfx_DmyId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId3: int = ParamField(
        int32, "residentSfx_DmyId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfxDmyId4: int = ParamField(
        int32, "residentSfx_DmyId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StaminaConsumptionRate: float = ParamField(
        float32, "staminaConsumptionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePhysics: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Physics", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMagic: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Magic", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFire: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Fire", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateThunder: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Thunder", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateDark: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Dark", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRatePoison: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Poison", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateBlood: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Blood", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateFreeze: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Freeze", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusStr: int = ParamField(
        int32, "attainmentWepStatusStr", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusDex: int = ParamField(
        int32, "attainmentWepStatusDex", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusMag: int = ParamField(
        int32, "attainmentWepStatusMag", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusFai: int = ParamField(
        int32, "attainmentWepStatusFai", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttainmentWepStatusLuc: int = ParamField(
        int32, "attainmentWepStatusLuc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AttackElementCorrectId: int = ParamField(
        int32, "attackElementCorrectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaleValue: int = ParamField(
        int32, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceShopCategory: int = ParamField(
        uint8, "reinforceShopCategory", REINFORCE_SHOP_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxArrowQuantity: int = ParamField(
        uint8, "maxArrowQuantity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx1IsVisibleForHang: bool = ParamField(
        uint8, "residentSfx_1_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx2IsVisibleForHang: bool = ParamField(
        uint8, "residentSfx_2_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx3IsVisibleForHang: bool = ParamField(
        uint8, "residentSfx_3_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSfx4IsVisibleForHang: bool = ParamField(
        uint8, "residentSfx_4_IsVisibleForHang:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel0: bool = ParamField(
        uint8, "isSoulParamIdChange_model0:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel1: bool = ParamField(
        uint8, "isSoulParamIdChange_model1:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel2: bool = ParamField(
        uint8, "isSoulParamIdChange_model2:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulParamIdChangemodel3: bool = ParamField(
        uint8, "isSoulParamIdChange_model3:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    WepSeIdOffset: int = ParamField(
        int8, "wepSeIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseChangePrice: int = ParamField(
        int32, "baseChangePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LevelSyncCorrectID: int = ParamField(
        int16, "levelSyncCorrectId", default=-1,
        tooltip="TODO",
    )
    CorrectTypeSleep: int = ParamField(
        uint8, "correctType_Sleep", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CorrectTypeMadness: int = ParamField(
        uint8, "correctType_Madness", WEP_CORRECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        uint8, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GemMountType: int = ParamField(
        uint8, "gemMountType", GEM_MOUNT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WeaponRegainHP: int = ParamField(
        uint16, "wepRegainHp", default=0,
        tooltip="TODO",
    )
    SpEffectMsgId0: int = ParamField(
        int32, "spEffectMsgId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId1: int = ParamField(
        int32, "spEffectMsgId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId2: int = ParamField(
        int32, "spEffectMsgId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep16: int = ParamField(
        int32, "originEquipWep16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep17: int = ParamField(
        int32, "originEquipWep17", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep18: int = ParamField(
        int32, "originEquipWep18", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep19: int = ParamField(
        int32, "originEquipWep19", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep20: int = ParamField(
        int32, "originEquipWep20", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep21: int = ParamField(
        int32, "originEquipWep21", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep22: int = ParamField(
        int32, "originEquipWep22", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep23: int = ParamField(
        int32, "originEquipWep23", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep24: int = ParamField(
        int32, "originEquipWep24", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipWep25: int = ParamField(
        int32, "originEquipWep25", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateSleep: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Sleep", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateMadness: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Madness", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaGuardCutRate: float = ParamField(
        float32, "saGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefMaterialVariationValue: int = ParamField(
        uint8, "defMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        uint8, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StealthAtkRate: int = ParamField(
        int16, "stealthAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateDisease: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Disease", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VsPlayerDmgCorrectRateCurse: float = ParamField(
        float32, "vsPlayerDmgCorrectRate_Curse", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RestrictSpecialSwordArt: int = ParamField(
        uint8, "restrictSpecialSwordArt", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(7, "pad[7]")
