"""Weapon Param in DSR has additional fields."""
from soulstruct.base.params.utils import FieldDisplayInfo, pad_field
from soulstruct.darksouls1r.game_types import *
from ..enums import *


EQUIP_PARAM_WEAPON_ST = {
    "paramdef_name": "EQUIP_PARAM_WEAPON_ST",
    "file_name": "EquipParamWeapon",
    "nickname": "Weapons",
    "fields": [
        FieldDisplayInfo(
            "behaviorVariationId",
            "BehaviorVariationID",
            True,
            int,
            "Multiplied by 1000 and added to player behavior lookups (hitboxes, bullets) triggered by TAE.",
        ),
        FieldDisplayInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        FieldDisplayInfo(
            "wanderingEquipId", "GhostWeaponReplacement", True, WeaponParam, "Weapon replacement for ghosts."
        ),
        FieldDisplayInfo("weight", "Weight", True, float, "Weight of weapon."),
        FieldDisplayInfo(
            "weaponWeightRate",
            "WeightRatio",
            True,
            float,
            "Unknown effect. Value is about evenly split between 0 and 1 across weapons, with no obvious pattern.",
        ),
        FieldDisplayInfo(
            "fixPrice",
            "RepairCost",
            True,
            int,
            "Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
            "durability over max durability.",
        ),
        FieldDisplayInfo("basicPrice", "BasicCost", False, int, "Unknown purpose, and unused."),
        FieldDisplayInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        FieldDisplayInfo(
            "correctStrength",
            "StrengthScaling",
            True,
            float,
            "Amount of attack power gained from strength. (I believe this is the percentage of the player's "
            "strength to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
        ),
        FieldDisplayInfo(
            "correctAgility",
            "DexterityScaling",
            True,
            float,
            "Amount of attack power gained from dexterity. (I believe this is the percentage of the player's "
            "dexterity to add to the weapon's attack power, but it also depends on ScalingFormulaType below.).",
        ),
        FieldDisplayInfo(
            "correctMagic",
            "IntelligenceScaling",
            True,
            float,
            "Amount of attack power gained from intelligence. (I believe this is the percentage of the player's "
            "intelligence to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
        ),
        FieldDisplayInfo(
            "correctFaith",
            "FaithScaling",
            True,
            float,
            "Amount of attack power gained from faith. (I believe this is the percentage of the player's faith to "
            "add to the weapon's attack power, but it also depends on ScalingFormulaType below.)",
        ),
        FieldDisplayInfo(
            "physGuardCutRate",
            "PhysicalGuardPercentage",
            True,
            float,
            "Percentage of physical damage prevented when guarding with this weapon.",
        ),
        FieldDisplayInfo(
            "magGuardCutRate",
            "MagicGuardPercentage",
            True,
            float,
            "Percentage of magic damage prevented when guarding with this weapon.",
        ),
        FieldDisplayInfo(
            "fireGuardCutRate",
            "FireGuardPercentage",
            True,
            float,
            "Percentage of fire damage prevented when guarding with this weapon.",
        ),
        FieldDisplayInfo(
            "thunGuardCutRate",
            "LightningGuardPercentage",
            True,
            float,
            "Percentage of lightning damage prevented when guarding with this weapon.",
        ),
        FieldDisplayInfo(
            "spEffectBehaviorId0",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 0).",
        ),
        FieldDisplayInfo(
            "spEffectBehaviorId1",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 1).",
        ),
        FieldDisplayInfo(
            "spEffectBehaviorId2",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 2).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId",
            "EquippedSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 0).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId1",
            "EquippedSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 1).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId2",
            "EquippedSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 2).",
        ),
        FieldDisplayInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade Material parameter that sets costs for weapon reinforcement.",
        ),
        FieldDisplayInfo(
            "originEquipWep",
            "UpgradeOrigin0",
            True,
            WeaponParam,
            "Origin armor for level 0 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep1",
            "UpgradeOrigin1",
            True,
            WeaponParam,
            "Origin armor for level 1 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep2",
            "UpgradeOrigin2",
            True,
            WeaponParam,
            "Origin armor for level 2 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep3",
            "UpgradeOrigin3",
            True,
            WeaponParam,
            "Origin armor for level 3 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep4",
            "UpgradeOrigin4",
            True,
            WeaponParam,
            "Origin armor for level 4 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep5",
            "UpgradeOrigin5",
            True,
            WeaponParam,
            "Origin armor for level 5 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep6",
            "UpgradeOrigin6",
            True,
            WeaponParam,
            "Origin armor for level 6 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep7",
            "UpgradeOrigin7",
            True,
            WeaponParam,
            "Origin armor for level 7 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep8",
            "UpgradeOrigin8",
            True,
            WeaponParam,
            "Origin armor for level 8 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep9",
            "UpgradeOrigin9",
            True,
            WeaponParam,
            "Origin armor for level 9 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep10",
            "UpgradeOrigin10",
            True,
            WeaponParam,
            "Origin armor for level 10 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep11",
            "UpgradeOrigin11",
            True,
            WeaponParam,
            "Origin armor for level 11 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep12",
            "UpgradeOrigin12",
            True,
            WeaponParam,
            "Origin armor for level 12 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep13",
            "UpgradeOrigin13",
            True,
            WeaponParam,
            "Origin armor for level 13 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep14",
            "UpgradeOrigin14",
            True,
            WeaponParam,
            "Origin armor for level 14 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipWep15",
            "UpgradeOrigin15",
            True,
            WeaponParam,
            "Origin armor for level 15 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "antiDemonDamageRate",
            "DamageAgainstDemonsMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against demons with this weapon.",
        ),
        FieldDisplayInfo(
            "antSaintDamageRate",
            "WeakToDivineDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against enemies weak to divine (e.g. skeletons) with this weapon.",
        ),
        FieldDisplayInfo(
            "antWeakA_DamageRate",
            "GodDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against Gods and Goddesses with this weapon.",
        ),
        FieldDisplayInfo(
            "antWeakB_DamageRate",
            "AbyssDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against enemies from the Abyss with this weapon.",
        ),
        FieldDisplayInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, ""),
        FieldDisplayInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""
        ),
        FieldDisplayInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
        FieldDisplayInfo("equipModelId", "WeaponModel", True, int, "Weapon model ID."),
        FieldDisplayInfo("iconId", "WeaponIcon", True, Texture, "Weapon icon texture ID."),
        FieldDisplayInfo(
            "durability",
            "InitialDurability",
            True,
            int,
            "Durability of weapon when it is obtained. Always equal to max durability in vanilla game.",
        ),
        FieldDisplayInfo("durabilityMax", "MaxDurability", True, int, "Maximum durability of weapon."),
        FieldDisplayInfo(
            "attackThrowEscape",
            "ThrowEscapePower",
            False,
            int,
            "Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement "
            "weapons.",
        ),
        FieldDisplayInfo(
            "parryDamageLife",
            "MaxParryWindowDuration",
            False,
            int,
            "Maximum parry window duration (cannot exceed TAE duration). Always set to 10.",
        ),
        FieldDisplayInfo("attackBasePhysics", "BasePhysicalDamage", True, int, "Base physical damage of weapon attacks."),
        FieldDisplayInfo("attackBaseMagic", "BaseMagicDamage", True, int, "Base magic damage of weapon attacks."),
        FieldDisplayInfo("attackBaseFire", "BaseFireDamage", True, int, "Base fire damage of weapon attacks."),
        FieldDisplayInfo(
            "attackBaseThunder", "BaseLightningDamage", True, int, "Base lightning damage of weapon attacks."
        ),
        FieldDisplayInfo("attackBaseStamina", "BaseStaminaDamage", True, int, "Base stamina damage of weapon attacks."),
        FieldDisplayInfo("saWeaponDamage", "BasePoiseDamage", True, int, "Base poise damage of weapon attacks."),
        FieldDisplayInfo(
            "saDurability",
            "AttackPoiseBonus",
            False,
            int,
            "Poise gained during attack animations with this weapon. Never used (probably done in TAE).",
        ),
        FieldDisplayInfo(
            "guardAngle",
            "EffectiveGuardAngle",
            False,
            int,
            "Angle that can be guarded with this weapon. Never used.",
        ),
        FieldDisplayInfo(
            "staminaGuardDef",
            "GuardStaminaDefense",
            True,
            int,
            "Defense against (i.e. value subtracted from) stamina attack damage while guarding.",
        ),
        FieldDisplayInfo(
            "reinforceTypeId",
            "WeaponUpgradeID",
            True,
            WeaponUpgradeParam,
            "Weapon Upgrade parameter that specifies upgrade benefits.",
        ),
        FieldDisplayInfo(
            "trophySGradeId",
            "AllWeaponsAchievementIndex",
            False,
            int,
            "Index of weapon as it contributes to the Knight's Honor achievement.",
        ),
        FieldDisplayInfo(
            "trophySeqId",
            "MaxUpgradeAchievementID",
            False,
            int,
            "Achievement unlocked when weapon is upgraded to maximum level (one per upgrade path).",
        ),
        FieldDisplayInfo(
            "throwAtkRate",
            "ThrowDamageChangePercentage",
            True,
            int,
            "Percentage damage increase (if positive) or decrease (if negative) during backstabs and ripostes "
            "with this weapon.",
        ),
        FieldDisplayInfo(
            "bowDistRate",
            "BowRangeChangePercentage",
            True,
            int,
            "Percentage range increase (if positive) or decrease (if negative) with this bow.",
        ),
        FieldDisplayInfo(
            "equipModelCategory",
            "WeaponModelCategory",
            False,
            EQUIP_MODEL_CATEGORY,
            "Model category for equipment. Only one option for weapons.",
        ),
        FieldDisplayInfo(
            "equipModelGender",
            "WeaponModelGender",
            False,
            EQUIP_MODEL_GENDER,
            "Model gender variant. All weapons are genderless.",
        ),
        FieldDisplayInfo(
            "weaponCategory",
            "WeaponCategory",
            True,
            WEAPON_CATEGORY,
            "Basic category of weapon. Many 'weapon types' you may be familiar with are merged here (e.g. whips "
            "are straight swords).",
        ),
        FieldDisplayInfo(
            "wepmotionCategory",
            "AttackAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Basic weapon attack animation type. More diverse than WeaponCategory. This number is multiplied by "
            "10000 and used as an animation offset for all attacks, I believe.",
        ),
        FieldDisplayInfo(
            "guardmotionCategory",
            "GuardAnimationCategory",
            True,
            GUARDMOTION_CATEGORY,
            "Basic weapon/shield block animation type.",
        ),
        FieldDisplayInfo(
            "atkMaterial",
            "VisualSoundEffectsOnHit",
            True,
            WEP_MATERIAL_ATK,
            "Determines the sounds and visual effects generated when this weapon hits.",
        ),
        FieldDisplayInfo(
            "defMaterial",
            "VisualEffectsOnBlock",
            True,
            WEP_MATERIAL_DEF,
            "Determines the visual effects generated when this weapon blocks an attack.",
        ),
        FieldDisplayInfo(
            "defSfxMaterial",
            "SoundEffectsOnBlock",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Determines the sound effects generated when this weapon blocks an attack.",
        ),
        FieldDisplayInfo(
            "correctType",
            "ScalingFormulaType",
            True,
            WEP_CORRECT_TYPE,
            "Determines how scaling changes with attribute level.",
        ),
        FieldDisplayInfo(
            "spAttribute",
            "ElementAttribute",
            True,
            ATKPARAM_SPATTR_TYPE,
            "Element attached to hits with this weapon.",
        ),
        FieldDisplayInfo(
            "spAtkcategory",
            "SpecialAttackCategory",
            True,
            WEPMOTION_CATEGORY,
            "Overrides AttackAnimationCategory for some attacks. Ranges from 50 to 199 (or 0 for none). Often "
            "used to give weapons unique strong (R2) attacks, for example, but can override any attack animation.",
        ),
        FieldDisplayInfo(
            "wepmotionOneHandId",
            "OneHandedAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Animation category for one-handed non-attack animations (like walking).",
        ),
        FieldDisplayInfo(
            "wepmotionBothHandId",
            "TwoHandedAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Animation category for two-handed non-attack animations (like walking).",
        ),
        FieldDisplayInfo(
            "properStrength",
            "RequiredStrength",
            True,
            int,
            "Required strength to wield weapon properly. (Reduced by one third if held two-handed.)",
        ),
        FieldDisplayInfo("properAgility", "RequiredDexterity", True, int, "Required dexterity to wield weapon properly."),
        FieldDisplayInfo(
            "properMagic", "RequiredIntelligence", True, int, "Required intelligence to wield weapon properly."
        ),
        FieldDisplayInfo("properFaith", "RequiredFaith", True, int, "Required faith to wield weapon properly."),
        FieldDisplayInfo(
            "overStrength", "OverStrength", False, int, "Unknown. Always set to 99, except for arrows and bolts."
        ),
        FieldDisplayInfo("attackBaseParry", "AttackBaseParry", False, int, "Unknown. Never used."),
        FieldDisplayInfo("defenseBaseParry", "DefenseBaseParry", False, int, "Unknown. Never used."),
        FieldDisplayInfo(
            "guardBaseRepel",
            "DeflectOnBlock",
            True,
            int,
            "Determines if an enemy will be deflected when you block them with this weapon (by comparing it to "
            "their DeflectOnAttack).",
        ),
        FieldDisplayInfo(
            "attackBaseRepel",
            "DeflectOnAttack",
            True,
            int,
            "Determines if this weapon will be deflected when attacking a blocking enemy (by comparing it to "
            "their DeflectOnBlock).",
        ),
        FieldDisplayInfo(
            "guardCutCancelRate",
            "IgnoreGuardPercentage",
            False,
            int,
            "Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
            "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, "
            "in favor of the simple 'IgnoreGuard' boolean field.",
        ),
        FieldDisplayInfo(
            "guardLevel",
            "GuardLevel",
            True,
            int,
            "Internal description: 'in which guard motion is the enemy attacked when guarded?' Exact effects are "
            "unclear, but this ranges from 0 to 4 in effectiveness of blocking in a predictable way (daggers are "
            "worse than swords, which are worse than greatswords, which are worse than all shields).",
        ),
        FieldDisplayInfo("slashGuardCutRate", "SlashDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo("blowGuardCutRate", "StrikeDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo("thrustGuardCutRate", "ThrustDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo(
            "poisonGuardResist",
            "PoisonDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming poison damage ignored when guarding.",
        ),
        FieldDisplayInfo(
            "diseaseGuardResist",
            "ToxicDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming toxic damage ignored when guarding.",
        ),
        FieldDisplayInfo(
            "bloodGuardResist",
            "BleedDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming bleed damage ignored when guarding.",
        ),
        FieldDisplayInfo(
            "curseGuardResist",
            "CurseDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming curse damage ignored when guarding.",
        ),
        FieldDisplayInfo(
            "isDurabilityDivergence",
            "DurabilityDivergenceCategory",
            True,
            DURABILITY_DIVERGENCE_CATEGORY,
            "Determines an alternate animation used if the player tries to use this weapon's special attack "
            "without having enough durability to use it. Exact enumeration is unknown, but existing usages are "
            "documented.",
        ),
        FieldDisplayInfo(
            "rightHandEquipable:1",
            "RightHandAllowed",
            True,
            bool,
            "If True, this weapon can be equipped in the right hand.",
        ),
        FieldDisplayInfo(
            "leftHandEquipable:1",
            "LeftHandAllowed",
            True,
            bool,
            "If True, this weapon can be equipped in the left hand.",
        ),
        FieldDisplayInfo(
            "bothHandEquipable:1",
            "BothHandsAllowed",
            True,
            bool,
            "If True, this weapon can be held in two-handed mode.",
        ),
        FieldDisplayInfo(
            "arrowSlotEquipable:1",
            "UsesEquippedArrows",
            True,
            bool,
            "If True, this weapon will use equipped arrow slot.",
        ),
        FieldDisplayInfo(
            "boltSlotEquipable:1",
            "UsesEquippedBolts",
            True,
            bool,
            "If True, this weapon will use equipped bolt slot.",
        ),
        FieldDisplayInfo(
            "enableGuard:1",
            "GuardEnabled",
            True,
            bool,
            "If True, the player can guard with this weapon by holding L1.",
        ),
        FieldDisplayInfo(
            "enableParry:1",
            "ParryEnabled",
            True,
            bool,
            "If True, the player can parry with this weapon by pressing L2.",
        ),
        FieldDisplayInfo(
            "enableMagic:1", "CanCastSorceries", True, bool, "If True, this weapon can be used to cast sorceries."
        ),
        FieldDisplayInfo(
            "enableSorcery:1", "CanCastPyromancy", True, bool, "If True, this weapon can be used to cast pyromancy."
        ),
        FieldDisplayInfo(
            "enableMiracle:1", "CanCastMiracles", True, bool, "If True, this weapon can be used to cast miracles."
        ),
        FieldDisplayInfo("enableVowMagic:1", "CanCastCovenantMagic", True, bool, ""),
        FieldDisplayInfo("isNormalAttackType:1", "DealsNeutralDamage", True, bool, ""),
        FieldDisplayInfo("isBlowAttackType:1", "DealsStrikeDamage", True, bool, ""),
        FieldDisplayInfo("isSlashAttackType:1", "DealsSlashDamage", True, bool, ""),
        FieldDisplayInfo("isThrustAttackType:1", "DealsThrustDamage", True, bool, ""),
        FieldDisplayInfo("isEnhance:1", "IsUpgraded", True, bool, ""),
        FieldDisplayInfo("isLuckCorrect:1", "IsAffectedByLuck", True, bool, ""),
        FieldDisplayInfo("isCustom:1", "IsCustom?", True, bool, ""),
        FieldDisplayInfo("disableBaseChangeReset:1", "DisableBaseChangeReset", True, bool, ""),
        FieldDisplayInfo("disableRepair:1", "DisableRepairs", True, bool, "If True, this weapon cannot be repaired."),
        FieldDisplayInfo("isDarkHand:1", "IsDarkHand", False, bool, "Enabled only for the Dark Hand."),
        FieldDisplayInfo("simpleModelForDlc:1", "SimpleDLCModelExists", False, bool, "Unknown; always set to False."),
        FieldDisplayInfo("lanternWep:1", "IsLantern?", True, bool, ""),
        FieldDisplayInfo(
            "isVersusGhostWep:1",
            "CanHitGhosts",
            True,
            bool,
            "If True, this weapon can hit ghosts without a Transient Curse active.",
        ),
        FieldDisplayInfo(
            "baseChangeCategory:6", "BaseChangeCategory", False, int, "Never used. Likely Demon's Souls junk."
        ),
        FieldDisplayInfo("isDragonSlayer:1", "IsDragonSlayer", True, bool, ""),
        FieldDisplayInfo(
            "isDeposit:1",
            "CanBeStored",
            True,
            bool,
            "If True, this weapon can be stored in the Bottomless Box. Always True for rings.",
        ),
        FieldDisplayInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this weapon cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        FieldDisplayInfo("pad_0[1]", "Pad2", False, pad_field(1), "Null padding."),
        FieldDisplayInfo(
            "oldSortId", "OldSortIndex", False, int, "Sorting index for an obsolete build of the game. No effect."
        ),
        FieldDisplayInfo("levelSyncCorrectID", "LevelSyncCorrectID", False, int, "Level sync ID for DSR."),
        FieldDisplayInfo("pad_1[6]", "Pad3", False, pad_field(6), "Null padding."),
    ],
}
