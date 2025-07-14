from __future__ import annotations

__all__ = ["EQUIP_PARAM_WEAPON_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_WEAPON_ST(ParamRow):
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
        float32, "weight", default=0.0,
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
    BasicCost: int = ParamField(
        int32, "basicPrice", default=0,
        tooltip="Unknown purpose, and unused.",
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
    DamageAgainstDemonsMultiplier: float = ParamField(
        float32, "antiDemonDamageRate", default=1.0,
        tooltip="Multiplier applied to damage dealt against demons with this weapon.",
    )
    WeakToDivineDamageMultiplier: float = ParamField(
        float32, "antSaintDamageRate", default=1.0,
        tooltip="Multiplier applied to damage dealt against enemies weak to divine (e.g. skeletons) with this weapon.",
    )
    GodDamageMultiplier: float = ParamField(
        float32, "antWeakA_DamageRate", default=1.0,
        tooltip="Multiplier applied to damage dealt against Gods and Goddesses with this weapon.",
    )
    AbyssDamageMultiplier: float = ParamField(
        float32, "antWeakB_DamageRate", default=1.0,
        tooltip="Multiplier applied to damage dealt against enemies from the Abyss with this weapon.",
    )
    VagrantItemLot: int = ParamField(
        int32, "vagrantItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int32, "vagrantBonusEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
        int32, "vagrantItemEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
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
        uint16, "durability", default=0,
        tooltip="Durability of weapon when it is obtained. Always equal to max durability in vanilla game.",
    )
    MaxDurability: int = ParamField(
        uint16, "durabilityMax", default=0,
        tooltip="Maximum durability of weapon.",
    )
    ThrowEscapePower: int = ParamField(
        uint16, "attackThrowEscape", default=1,
        tooltip="Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement "
                "weapons.",
    )
    MaxParryWindowDuration: int = ParamField(
        int16, "parryDamageLife", default=10,
        tooltip="Maximum parry window duration (cannot exceed TAE duration). Always set to 10.",
    )
    BasePhysicalDamage: int = ParamField(
        uint16, "attackBasePhysics", default=0,
        tooltip="Base physical damage of weapon attacks.",
    )
    BaseMagicDamage: int = ParamField(
        uint16, "attackBaseMagic", default=0,
        tooltip="Base magic damage of weapon attacks.",
    )
    BaseFireDamage: int = ParamField(
        uint16, "attackBaseFire", default=0,
        tooltip="Base fire damage of weapon attacks.",
    )
    BaseLightningDamage: int = ParamField(
        uint16, "attackBaseThunder", default=0,
        tooltip="Base lightning damage of weapon attacks.",
    )
    BaseStaminaDamage: int = ParamField(
        uint16, "attackBaseStamina", default=0,
        tooltip="Base stamina damage of weapon attacks.",
    )
    BasePoiseDamage: int = ParamField(
        uint16, "saWeaponDamage", default=0,
        tooltip="Base poise damage of weapon attacks.",
    )
    AttackPoiseBonus: int = ParamField(
        int16, "saDurability", default=0,
        tooltip="Poise gained during attack animations with this weapon. Never used (probably done in TAE).",
    )
    EffectiveGuardAngle: int = ParamField(
        int16, "guardAngle", default=0,
        tooltip="Angle that can be guarded with this weapon. Never used.",
    )
    GuardStaminaDefense: int = ParamField(
        int16, "staminaGuardDef", default=0,
        tooltip="Defense against (i.e. value subtracted from) stamina attack damage while guarding.",
    )
    WeaponUpgradeID: int = ParamField(
        int16, "reinforceTypeId", game_type=WeaponUpgradeParam, default=0,
        tooltip="Weapon Upgrade parameter that specifies upgrade benefits.",
    )
    AllWeaponsAchievementIndex: int = ParamField(
        int16, "trophySGradeId", default=-1,
        tooltip="Index of weapon as it contributes to the Knight's Honor achievement.",
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
        int16, "bowDistRate", default=-1,
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
    VisualEffectsOnBlock: int = ParamField(
        uint8, "defMaterial", WEP_MATERIAL_DEF, default=0,
        tooltip="Determines the visual effects generated when this weapon blocks an attack.",
    )
    SoundEffectsOnBlock: int = ParamField(
        uint8, "defSfxMaterial", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="Determines the sound effects generated when this weapon blocks an attack.",
    )
    ScalingFormulaType: int = ParamField(
        uint8, "correctType", WEP_CORRECT_TYPE, default=0,
        tooltip="Determines how scaling changes with attribute level.",
    )
    ElementAttribute: int = ParamField(
        uint8, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="Element attached to hits with this weapon.",
    )
    SpecialAttackCategory: int = ParamField(
        uint8, "spAtkcategory", default=0,
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
        uint8, "overStrength", default=99,
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
    DurabilityDivergenceCategory: int = ParamField(
        uint8, "isDurabilityDivergence", DURABILITY_DIVERGENCE_CATEGORY, default=0,
        tooltip="Determines an alternate animation used if the player tries to use this weapon's special attack "
                "without having enough durability to use it. Exact enumeration is unknown, but existing usages are "
                "documented.",
    )
    RightHandAllowed: bool = ParamField(
        uint8, "rightHandEquipable:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this weapon can be equipped in the right hand.",
    )
    LeftHandAllowed: bool = ParamField(
        uint8, "leftHandEquipable:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this weapon can be equipped in the left hand.",
    )
    BothHandsAllowed: bool = ParamField(
        uint8, "bothHandEquipable:1", EQUIP_BOOL, bit_count=1, default=True,
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
        uint8, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TODO",
    )
    IsAffectedByLuck: bool = ParamField(
        uint8, "isLuckCorrect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsCustom: bool = ParamField(
        uint8, "isCustom:1", EQUIP_BOOL, bit_count=1, default=True,
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
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this weapon can be stored in the Bottomless Box. Always True for rings.",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this weapon cannot be given to other players by dropping it. Always False in vanilla.",
    )
    _Pad0: bytes = ParamPad(1, "pad_0[1]")
    OldSortIndex: int = ParamField(
        int16, "oldSortId", default=0,
        tooltip="Sorting index for an obsolete build of the game. No effect.",
    )
    _Pad1: bytes = ParamPad(8, "pad_1[8]")
