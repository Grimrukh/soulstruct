from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *

EQUIP_PARAM_PROTECTOR_ST = {
    "param_type": "EQUIP_PARAM_PROTECTOR_ST",
    "file_name": "EquipParamProtector",
    "nickname": "Armor",
    "fields": [
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo(
            "wanderingEquipId",
            "GhostArmorReplacement",
            True,
            ArmorParam,
            "Replacement equipment for network ghosts.",
        ),
        ParamFieldInfo("vagrantItemLotId", "VagrantItemLot", True, ItemLotParam, ""),
        ParamFieldInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", True, ItemLotParam, ""
        ),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", True, ItemLotParam, ""),
        ParamFieldInfo(
            "fixPrice",
            "RepairCost",
            True,
            int,
            "Amount of souls required to repair armor fully. Actual repair cost is this multiplied by "
            "current durability over max durability.",
        ),
        ParamFieldInfo(
            "basicPrice",
            "BasicCost",
            False,
            int,
            "Unsure when this is used. Possibly sets the default if the cost is not specified in Shop "
            "parameters. Always set to 200.",
        ),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo("weight", "Weight", True, float, "Weight of armor."),
        ParamFieldInfo(
            "residentSpEffectId",
            "WearerSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (first of three).",
        ),
        ParamFieldInfo(
            "residentSpEffectId2",
            "WearerSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (second of three).",
        ),
        ParamFieldInfo(
            "residentSpEffectId3",
            "WearerSpecialEffect3",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (third of three).",
        ),
        ParamFieldInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade material set for reinforcement.",
        ),
        ParamFieldInfo(
            "partsDamageRate",
            "SiteDamageMultiplier",
            True,
            float,
            "Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, "
            "so is never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, "
            "1.1 for gauntlets and leggings, and 1 for torso armor.",
        ),
        ParamFieldInfo(
            "corectSARecover",
            "PoiseRecoveryTimeModifier",
            True,
            float,
            "Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
            "otherwise.",
        ),
        ParamFieldInfo(
            "originEquipPro",
            "UpgradeOrigin0",
            True,
            ArmorParam,
            "Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro1",
            "UpgradeOrigin1",
            True,
            ArmorParam,
            "Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro2",
            "UpgradeOrigin2",
            True,
            ArmorParam,
            "Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro3",
            "UpgradeOrigin3",
            True,
            ArmorParam,
            "Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro4",
            "UpgradeOrigin4",
            True,
            ArmorParam,
            "Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro5",
            "UpgradeOrigin5",
            True,
            ArmorParam,
            "Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro6",
            "UpgradeOrigin6",
            True,
            ArmorParam,
            "Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro7",
            "UpgradeOrigin7",
            True,
            ArmorParam,
            "Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro8",
            "UpgradeOrigin8",
            True,
            ArmorParam,
            "Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro9",
            "UpgradeOrigin9",
            True,
            ArmorParam,
            "Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro10",
            "UpgradeOrigin10",
            True,
            ArmorParam,
            "Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro11",
            "UpgradeOrigin11",
            True,
            ArmorParam,
            "Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro12",
            "UpgradeOrigin12",
            True,
            ArmorParam,
            "Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro13",
            "UpgradeOrigin13",
            True,
            ArmorParam,
            "Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro14",
            "UpgradeOrigin14",
            True,
            ArmorParam,
            "Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "originEquipPro15",
            "UpgradeOrigin15",
            True,
            ArmorParam,
            "Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        ParamFieldInfo(
            "faceScaleM_ScaleX",
            "MaleFaceScaleX",
            True,
            float,
            "Scale factor applied to X dimension of male faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleM_ScaleZ",
            "MaleFaceScaleZ",
            True,
            float,
            "Scale factor applied to Z dimension of male faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleM_MaxX",
            "MaleFaceMaxScaleX",
            True,
            float,
            "Maximum scale permitted for X dimension of male faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleM_MaxZ",
            "MaleFaceMaxScaleZ",
            True,
            float,
            "Maximum scale permitted for Z dimension of male faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleF_ScaleX",
            "FemaleFaceScaleX",
            True,
            float,
            "Scale factor applied to X dimension of female faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleF_ScaleZ",
            "FemaleFaceScaleZ",
            True,
            float,
            "Scale factor applied to Z dimension of female faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleF_MaxX",
            "FemaleFaceMaxScaleX",
            True,
            float,
            "Maximum scale permitted for X dimension of female faces when worn.",
        ),
        ParamFieldInfo(
            "faceScaleF_MaxZ",
            "FemaleFaceMaxScaleZ",
            True,
            float,
            "Maximum scale permitted for Z dimension of female faces when worn.",
        ),
        ParamFieldInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        ParamFieldInfo("equipModelId", "EquipmentModel", True, int, "Model ID of armor."),
        ParamFieldInfo("iconIdM", "MaleIcon", True, Texture, "Icon of male variant of armor in inventory."),
        ParamFieldInfo("iconIdF", "FemaleIcon", True, Texture, "Icon of female variant of armor in inventory."),
        ParamFieldInfo(
            "knockBack",
            "KnockbackPercentageReduction",
            False,
            int,
            "Never used. Probably the percentage of knockback reduced (from 0 to 100) when wearing armor.",
        ),
        ParamFieldInfo(
            "knockbackBounceRate",
            "KnockbackBouncePercentage",
            False,
            int,
            "Never used. Possibly affects knockback of incoming attacks.",
        ),
        ParamFieldInfo(
            "durability",
            "InitialDurability",
            True,
            int,
            "Durability of armor when it is obtained. Always equal to max durability in vanilla game.",
        ),
        ParamFieldInfo("durabilityMax", "MaxDurability", True, int, "Maximum durability of armor."),
        ParamFieldInfo("saDurability", "Poise", True, int, "Amount of poise added when wearing armor."),
        ParamFieldInfo(
            "defFlickPower", "RepelDefense", True, int, "Determines when incoming attacks will bounce off."),
        ParamFieldInfo(
            "defensePhysics", "PhysicalDefense", True, int, "Added defense against physical attack damage."),
        ParamFieldInfo("defenseMagic", "MagicDefense", True, int, "Added defense against magic attack damage."),
        ParamFieldInfo("defenseFire", "FireDefense", True, int, "Added defense against fire attack damage."),
        ParamFieldInfo(
            "defenseThunder", "LightningDefense", True, int, "Added defense against lightning attack damage."
        ),
        ParamFieldInfo(
            "defenseSlash", "SlashDefense", True, int, "Added defense against physical slash attack damage."),
        ParamFieldInfo(
            "defenseBlow", "StrikeDefense", True, int, "Added defense against physical strike attack damage."
        ),
        ParamFieldInfo(
            "defenseThrust", "ThrustDefense", True, int, "Added defense against physical thrust attack damage."
        ),
        ParamFieldInfo("resistPoison", "PoisonResistance", True, int, "Poison resistance added by armor."),
        ParamFieldInfo("resistDisease", "ToxicResistance", True, int, "Toxic resistance added by armor."),
        ParamFieldInfo("resistBlood", "BleedResistance", True, int, "Bleed resistance added by armor."),
        ParamFieldInfo("resistCurse", "CurseResistance", True, int, "Curse resistance added by armor."),
        ParamFieldInfo(
            "reinforceTypeId",
            "ArmorUpgradeID",
            True,
            ArmorUpgradeParam,
            "Effects applied at consecutive upgrade reinforcement levels.",
        ),
        ParamFieldInfo(
            "trophySGradeId",
            "AchievementContributionID",
            False,
            int,
            "Index of armor as it contributes to certain multi-item achievements.",
        ),
        ParamFieldInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
        ),
        ParamFieldInfo("knockbackParamId", "KnockbackID", False, int, "Knockback entry. Always 1."),
        ParamFieldInfo(
            "flickDamageCutRate",
            "RepelDamagePercentageReduction",
            True,
            int,
            "Determines some aspect of attack deflection. Always set to 0 (for light armor) or 255 (for heavy "
            "armor).",
        ),
        ParamFieldInfo(
            "equipModelCategory",
            "EquipmentModelCategory",
            True,
            EQUIP_MODEL_CATEGORY,
            "Body part covered by armor model.",
        ),
        ParamFieldInfo(
            "equipModelGender", "EquipmentModelGender", True, EQUIP_MODEL_GENDER, "Gender variant of armor."),
        ParamFieldInfo("protectorCategory", "ArmorType", True, PROTECTOR_CATEGORY, "Type of armor (equip slot)."),
        ParamFieldInfo(
            "defenseMaterial",
            "SoundEffectOnHit",
            True,
            WEP_MATERIAL_DEF,
            "Type of sound effect generated when this armor is hit.",
        ),
        ParamFieldInfo(
            "defenseMaterialSfx",
            "VisualEffectOnHit",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Type of visual effect generated when this armor is hit.",
        ),
        ParamFieldInfo("partsDmgType", "PartsDamageType", False, ATK_PARAM_PARTSDMGTYPE, "Always zero."),
        ParamFieldInfo(
            "defenseMaterial_Weak",
            "SoundEffectOnWeakSpotHit",
            True,
            WEP_MATERIAL_DEF,
            "Sound effect for when damage is taken to weak spot (used for head armor).",
        ),
        ParamFieldInfo(
            "defenseMaterialSfx_Weak",
            "VisualEffectOnWeakSpotHit",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Visual effect for when damage is taken to weak spot (used for head armor).",
        ),
        ParamFieldInfo(
            "isDeposit:1", "CanBeStored", True, bool, "If True, this armor can be stored in the Bottomless Box."
        ),
        ParamFieldInfo("headEquip:1", "EquippedToHead", True, bool, "This armor is equipped to the head."),
        ParamFieldInfo("bodyEquip:1", "EquippedToBody", True, bool, "This armor is equipped to the body."),
        ParamFieldInfo("armEquip:1", "EquippedToHands", True, bool, "This armor is equipped to the hands."),
        ParamFieldInfo("legEquip:1", "EquippedToLegs", True, bool, "This armor is equipped to the legs."),
        ParamFieldInfo(
            "useFaceScale:1",
            "UseFaceScale",
            False,
            bool,
            "If True, the face-scaling parameters of this armor will be applied.",
        ),
        ParamFieldInfo("invisibleFlag00:1", "HideFlag0", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag01:1", "HideFlag1HairFringe", True, bool, "Hide part of the character model: (hair fringe)"),
        ParamFieldInfo(
            "invisibleFlag02:1", "HideFlag2Sideburns", True, bool, "Hide part of the character model: (sideburns)"),
        ParamFieldInfo(
            "invisibleFlag03:1", "HideFlag3TopOfHead", True, bool, "Hide part of the character model: (top of head)"),
        ParamFieldInfo(
            "invisibleFlag04:1", "HideFlag4TopOfHead", True, bool, "Hide part of the character model: (top of head)"),
        ParamFieldInfo(
            "invisibleFlag05:1", "HideFlag5BackHair", True, bool, "Hide part of the character model: (back hair)"),
        ParamFieldInfo(
            "invisibleFlag06:1",
            "HideFlag6BackHairTip",
            True,
            bool,
            "Hide part of the character model: (back hair tip)",
        ),
        ParamFieldInfo("invisibleFlag07:1", "HideFlag7", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag08:1", "HideFlag8", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag09:1", "HideFlag9", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag10:1", "HideFlag10Collar", True, bool, "Hide part of the character model: (collar)"
        ),
        ParamFieldInfo(
            "invisibleFlag11:1",
            "HideFlag11AroundCollar",
            True,
            bool,
            "Hide part of the character model: (around collar)",
        ),
        ParamFieldInfo("invisibleFlag12:1", "HideFlag12", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag13:1", "HideFlag13", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag14:1", "HideFlag14", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag15:1", "HideFlag15HoodHem", True, bool, "Hide part of the character model: (hood hem)"
        ),
        ParamFieldInfo("invisibleFlag16:1", "HideFlag16", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag17:1", "HideFlag17", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag18:1", "HideFlag18", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag19:1", "HideFlag19", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag20:1", "HideFlag20SleeveA", True, bool, "Hide part of the character model: (sleeve A)"
        ),
        ParamFieldInfo(
            "invisibleFlag21:1", "HideFlag21SleeveB", True, bool, "Hide part of the character model: (sleeve B)"
        ),
        ParamFieldInfo("invisibleFlag22:1", "HideFlag22", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag23:1", "HideFlag23", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag24:1", "HideFlag24", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag25:1", "HideFlag25Arm", True, bool, "Hide part of the character model: (arm)"
        ),
        ParamFieldInfo("invisibleFlag26:1", "HideFlag26", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag27:1", "HideFlag27", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag28:1", "HideFlag28", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag29:1", "HideFlag29", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "invisibleFlag30:1", "HideFlag30Belt", True, bool, "Hide part of the character model: (belt)"
        ),
        ParamFieldInfo("invisibleFlag31:1", "HideFlag31", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag32:1", "HideFlag32", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag33:1", "HideFlag33", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag34:1", "HideFlag34", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag35:1", "HideFlag35", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag36:1", "HideFlag36", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag37:1", "HideFlag37", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag38:1", "HideFlag38", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag39:1", "HideFlag39", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag40:1", "HideFlag40", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag41:1", "HideFlag41", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag42:1", "HideFlag42", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag43:1", "HideFlag43", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag44:1", "HideFlag44", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag45:1", "HideFlag45", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag46:1", "HideFlag46", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag47:1", "HideFlag47", True, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        ParamFieldInfo("simpleModelForDlc:1", "SimpleDLCModelExists", False, bool, "Unknown; always set to False."),
        ParamFieldInfo("pad_0[1]", "Pad0", False, pad_field(1), "Null padding."),
        ParamFieldInfo(
            "oldSortId", "OldSortIndex", False, int, "Sorting index for an obsolete build of the game. No effect."
        ),
        ParamFieldInfo("pad_1[6]", "Pad1", False, pad_field(6), "Null padding."),
    ],
}
