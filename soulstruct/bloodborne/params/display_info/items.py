__all__ = [
    "EQUIP_PARAM_WEAPON_ST",
    "EQUIP_PARAM_PROTECTOR_ST",
    "EQUIP_PARAM_ACCESSORY_ST",
    "EQUIP_PARAM_GOODS_ST",
    "ITEMLOT_PARAM_ST",
    "ITEMLOT_LVDEP_PARAM_ST",
    "EQUIP_MTRL_SET_PARAM_ST",
    "REINFORCE_PARAM_WEAPON_ST",
    "REINFORCE_PARAM_PROTECTOR_ST",
    "PROTECTOR_GEN_PARAM_ST",
    "WEAPON_GEN_PARAM_ST",
]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field, bit_pad_field
from soulstruct.bloodborne.params.enums import *
from soulstruct.bloodborne.game_types import *


class DynamicGoodRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {BulletParam, SpecialEffectParam}

    def __call__(self, entry) -> ParamFieldInfo:
        if entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Default:
            return ParamFieldInfo(
                self.name,
                "NoReference",
                True,
                int,
                "This value should be -1 when 'Default' reference type is selected.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Bullet:
            return ParamFieldInfo(
                self.name,
                "Bullet",
                True,
                BulletParam,
                "Bullet triggered by using good (which may simply be targeted at self).",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return ParamFieldInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special effect triggered (on self) by using good.",
            )
        else:
            return ParamFieldInfo(
                self.name,
                "UnknownReferenceID",
                True,
                int,
                "Could not determine reference ID type (usually Bullet or SpecialEffect).",
            )


class DynamicItemLotRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {WeaponParam, ArmorParam, AccessoryParam, GoodParam}

    def __call__(self, entry) -> ParamFieldInfo:
        item_type = entry[self.type_field_name]
        item_lot_slot = int(self.type_field_name[-1])
        if item_type == ITEMLOT_ITEMCATEGORY.Weapon:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                WeaponParam,
                f"Item slot {item_lot_slot} (Weapon).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Armor:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                ArmorParam,
                f"Item slot {item_lot_slot} (Armor).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Good:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                GoodParam,
                f"Item slot {item_lot_slot} (Good).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.GemOrRune:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                GoodParam,
                f"Item slot {item_lot_slot} (Gem/Rune).",
            )
        else:
            return ParamFieldInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                int,
                f"Item slot {item_lot_slot} (unknown item type {item_type}).",
            )


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
            "compTrophySedId",
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
        ParamFieldInfo("isGuestDrop:1", "CanDropToSummons", True, EQUIP_BOOL, ""),
        ParamFieldInfo("shotDamageCutRate", "GunDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("slashDamageCutRate", "SlashDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("blowDamageCutRate", "BluntDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("thrustDamageCutRate", "ThrustDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("magicDamageCutRate", "MagicDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("fireDamageCutRate", "FireDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("thunderDamageCutRate", "LightningDamagePercentageReduction", True, float, ""),
        ParamFieldInfo("resistTherianthrope", "ResistBeasts", True, int, ""),
        ParamFieldInfo("invisibleFlag48:1", "HideFlag48", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag49:1", "HideFlag49", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag50:1", "HideFlag50", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag51:1", "HideFlag51", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag52:1", "HideFlag52", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag53:1", "HideFlag53", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag54:1", "HideFlag54", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag55:1", "HideFlag55", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag56:1", "HideFlag56", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag57:1", "HideFlag57", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag58:1", "HideFlag58", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag59:1", "HideFlag59", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag60:1", "HideFlag60", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag61:1", "HideFlag61", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("invisibleFlag62:1", "HideFlag62", False, bool, "Hide part of the character model: (unknown)"),
        ParamFieldInfo("repositoryCategory", "StorageCategory", True, int, ""),
        ParamFieldInfo("pad2[1]", "Pad", False, pad_field(1), ""),
        ParamFieldInfo("trophySeqId", "TrophyID", True, int, ""),
        ParamFieldInfo("pad3[8]", "Pad", False, pad_field(8), ""),
    ],
}


REINFORCE_PARAM_PROTECTOR_ST = {
    "param_type": "REINFORCE_PARAM_PROTECTOR_ST",
    "file_name": "ReinforceParamProtector",
    "nickname": "ArmorUpgrades",
    "fields": [
        ParamFieldInfo(
            "physicsDefRate",
            "PhysicalDefenseMultiplier",
            True,
            float,
            "Multiplier for physical defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "magicDefRate",
            "MagicDefenseMultiplier",
            True,
            float,
            "Multiplier for magic defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "fireDefRate",
            "FireDefenseMultiplier",
            True,
            float,
            "Multiplier for fire defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "thunderDefRate",
            "LightningDefenseMultiplier",
            True,
            float,
            "Multiplier for lightning defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "slashDefRate",
            "SlashDefenseMultiplier",
            True,
            float,
            "Multiplier for slash defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "blowDefRate",
            "StrikeDefenseMultiplier",
            True,
            float,
            "Multiplier for strike defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "thrustDefRate",
            "ThrustDefenseMultiplier",
            True,
            float,
            "Multiplier for thrust defense at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistPoisonRate",
            "PoisonResistanceMultiplier",
            True,
            float,
            "Multiplier for poison resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistDiseaseRate",
            "ToxicResistanceMultiplier",
            True,
            float,
            "Multiplier for toxic resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistBloodRate",
            "BleedResistanceMultiplier",
            True,
            float,
            "Multiplier for bleed resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "resistCurseRate",
            "CurseResistanceMultiplier",
            True,
            float,
            "Multiplier for curse resistance at this upgrade level.",
        ),
        ParamFieldInfo(
            "residentSpEffectId1",
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
    ],
}

EQUIP_PARAM_ACCESSORY_ST = {
    "param_type": "EQUIP_PARAM_ACCESSORY_ST",
    "file_name": "EquipParamAccessory",
    "nickname": "Rings",
    "fields": [
        ParamFieldInfo(
            "refId", "SpecialEffect", True, SpecialEffectParam, "Special effect applied when ring is equipped."
        ),
        ParamFieldInfo(
            "sfxVariationId",
            "SFXVariation",
            False,
            int,
            "SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
            "with unused Behavior parameter below.",
        ),
        ParamFieldInfo(
            "weight",
            "Weight",
            False,
            float,
            "Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other equipment.",
        ),
        ParamFieldInfo(
            "behaviorId",
            "Behavior",
            False,
            BehaviorParam,
            "Behavior of ring 'skill'. Always zero in the vanilla game.",
        ),
        ParamFieldInfo("basicPrice", "BasicCost", False, int, "Unknown purpose, and unused."),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        ParamFieldInfo(
            "equipModelId", "EquipmentModel", False, int, "Always zero. (Rings have no model, presumably.)"
        ),
        ParamFieldInfo("iconId", "MenuIcon", True, Texture, "Icon ID of ring in menu."),
        ParamFieldInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
            "level).",
        ),
        ParamFieldInfo(
            "trophySGradeId",
            "AchievementContributionID",
            False,
            int,
            "Index of ring as it contributes to certain multi-item achievements (none for rings).",
        ),
        ParamFieldInfo(
            "trophySeqId",
            "AchievementUnlockID",
            False,
            int,
            "Achievement unlocked when ring is acquired (Covenant of Artorias).",
        ),
        ParamFieldInfo("equipModelCategory", "EquipmentModelCategory", False, EQUIP_MODEL_CATEGORY, "Always zero."),
        ParamFieldInfo("equipModelGender", "EquipmentModelGender", False, EQUIP_MODEL_GENDER, "Always zero."),
        ParamFieldInfo("accessoryCategory", "AccessoryCategory", False, ACCESSORY_CATEGORY, "Always zero."),
        ParamFieldInfo(
            "refCategory",
            "ReferenceType",
            False,
            BEHAVIOR_REF_TYPE,
            "Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
        ),
        ParamFieldInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            False,
            SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this equipment. Unused for rings.",
        ),
        ParamFieldInfo("pad[1]", "Pad1", False, pad_field(1), "Null padding."),
        ParamFieldInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, ""),
        ParamFieldInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""
        ),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
        ParamFieldInfo(
            "isDeposit:1",
            "CanBeStored",
            False,
            bool,
            "If True, this ring can be stored in the Bottomless Box. Always True for rings.",
        ),
        ParamFieldInfo(
            "isEquipOutBrake:1",
            "BreaksWhenUnequipped",
            True,
            bool,
            "If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
        ),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        ParamFieldInfo("pad1[3]", "Pad2", False, pad_field(3), "Null padding."),
    ],
}

EQUIP_PARAM_GOODS_ST = {
    "param_type": "EQUIP_PARAM_GOODS_ST",
    "file_name": "EquipParamGoods",
    "nickname": "Goods",
    "fields": [
        DynamicGoodRef("refId", "refCategory"),
        ParamFieldInfo(
            "sfxVariationId",
            "AnimationVariationID",
            True,
            int,
            "Animation variation ID to combine with the base usage animation.",
        ),
        ParamFieldInfo("weight", "Weight", False, float, "Weight of good. Never used in vanilla Dark Souls."),
        ParamFieldInfo("fragmentNum", "FragmentCount", True, int, ""),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo("behaviorId", "Behavior", False, BehaviorParam, "Behavior triggered by good use. Never used."),
        ParamFieldInfo(
            "replaceItemId",
            "GoodToReplace",
            True,
            GoodParam,
            "Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        ParamFieldInfo(
            "yesNoDialogMessageId",
            "ConfirmationMessage",
            True,
            EventText,
            "Message displayed in yes/no dialog box to confirm use of good.",
        ),
        ParamFieldInfo(
            "magicId",
            "Spell",
            True,
            SpellParam,
            "Spell unlocked in attunement menu by possession of this good. (Usually matches the good ID.)",
        ),
        ParamFieldInfo("iconId", "GoodIcon", True, Texture, "Good icon texture ID."),
        ParamFieldInfo("modelId", "ModelID", False, int, "Model of good. Never used."),
        ParamFieldInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
        ),
        ParamFieldInfo(
            "compTrophySedId",
            "CollectionAchievementID",
            False,
            int,
            "Collection achievement (e.g. all spells) to which obtaining this good contributes.",
        ),
        ParamFieldInfo(
            "trophySeqId",
            "AchievementID",
            False,
            int,
            "Achievement unlocked when this good is first obtained (e.g. Estus Flask).",
        ),
        ParamFieldInfo("maxNum", "MaxHoldQuantity", True, int, "Maximum number of good that can be held at once."),
        ParamFieldInfo("consumeHeroPoint", "HumanityCost", False, int, "Humanity cost of using good. Always zero."),
        ParamFieldInfo(
            "overDexterity",
            "OverDexterity",
            False,
            int,
            "'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise.",
        ),
        ParamFieldInfo(
            "goodsType",
            "GoodType",
            True,
            GOODS_TYPE,
            "Determines if this is a basic good, upgrade material, key item, or spell.",
        ),
        ParamFieldInfo(
            "refCategory",
            "ReferenceType",
            True,
            BEHAVIOR_REF_TYPE,
            "Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)",
        ),
        ParamFieldInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            True,
            BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
            "for thrown goods and 'No Category' otherwise.",
        ),
        ParamFieldInfo("goodsCategory", "GoodCategory", False, GOODS_CATEGORY, "Never used. Only one value (0) used."),
        ParamFieldInfo(
            "goodsUseAnim",
            "UseAnimation",
            True,
            GOODS_USE_ANIM,
            "Points to basic animation used when good is used. Visual/sound effects are set by the variation ID.",
        ),
        ParamFieldInfo(
            "opmeMenuType",
            "MenuActivated",
            True,
            GOODS_OPEN_MENU,
            "Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be "
            "useful.",
        ),
        ParamFieldInfo(
            "useLimitCategory",
            "LimitCategory",
            True,
            SP_EFFECT_USELIMIT_CATEGORY,
            "Only one good-triggered special effect with this category can be active at once. Additional attempts "
            "to use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)",
        ),
        ParamFieldInfo(
            "replaceCategory",
            "ReplaceCategory",
            False,
            REPLACE_CATEGORY,
            "The special effect triggered by this good will replace any special effects in the same category as "
            "this one. Used only by Dragon Stones.",
        ),
        ParamFieldInfo(
            "vowType0:1",
            "UseableByNoCovenant",
            True,
            bool,
            "Determines if this good can be used by characters with no covenant.",
        ),
        ParamFieldInfo(
            "vowType1:1",
            "UseableByWayOfWhite",
            True,
            bool,
            "Determines if this good can be used by characters in the Way of White.",
        ),
        ParamFieldInfo(
            "vowType2:1",
            "UseableByPrincessGuard",
            True,
            bool,
            "Determines if this good can be used by characters in the Princess's Guard.",
        ),
        ParamFieldInfo(
            "vowType3:1",
            "UseableByWarriorsOfSunlight",
            True,
            bool,
            "Determines if this good can be used by characters in the Warriors of Sunlight.",
        ),
        ParamFieldInfo(
            "vowType4:1",
            "UseableByDarkwraith",
            True,
            bool,
            "Determines if this good can be used by characters in the Darkwraith covenant.",
        ),
        ParamFieldInfo(
            "vowType5:1",
            "UseableByPathOfTheDragon",
            True,
            bool,
            "Determines if this good can be used by characters in the Path of the Dragon.",
        ),
        ParamFieldInfo(
            "vowType6:1",
            "UseableByGravelordServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Gravelord Servants.",
        ),
        ParamFieldInfo(
            "vowType7:1",
            "UseableByForestHunter",
            True,
            bool,
            "Determines if this good can be used by characters in the Forest Hunters.",
        ),
        ParamFieldInfo(
            "vowType8:1",
            "UseableByDarkmoonBlade",
            True,
            bool,
            "Determines if this good can be used by characters in the Blades of the Darkmoon.",
        ),
        ParamFieldInfo(
            "vowType9:1",
            "UseableByChaosServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Chaos Servant covenant.",
        ),
        ParamFieldInfo(
            "vowType10:1",
            "UseableByCovenant10",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 10.",
        ),
        ParamFieldInfo(
            "vowType11:1",
            "UseableByCovenant11",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 11.",
        ),
        ParamFieldInfo(
            "vowType12:1",
            "UseableByCovenant12",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 12.",
        ),
        ParamFieldInfo(
            "vowType13:1",
            "UseableByCovenant13",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 13.",
        ),
        ParamFieldInfo(
            "vowType14:1",
            "UseableByCovenant14",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 14.",
        ),
        ParamFieldInfo(
            "vowType15:1",
            "UseableByCovenant15",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 15.",
        ),
        ParamFieldInfo(
            "enable_live:1",
            "UseableByHumans",
            True,
            bool,
            "Determines if this good can be used by characters who have revived to Human status.",
        ),
        ParamFieldInfo(
            "enable_gray:1",
            "UseableByHollows",
            True,
            bool,
            "Determines if this good can be used by characters who are Hollow.",
        ),
        ParamFieldInfo(
            "enable_white:1",
            "UseableByWhitePhantoms",
            True,
            bool,
            "Determines if this good can be used by White Phantoms (summons).",
        ),
        ParamFieldInfo(
            "enable_black:1",
            "UseableByBlackPhantoms",
            True,
            bool,
            "Determines if this good can be used by Black Phantoms (invaders).",
        ),
        ParamFieldInfo(
            "enable_multi:1",
            "UseableInMultiplayer",
            True,
            bool,
            "Determines if this good can be used while multiple players are together.",
        ),
        ParamFieldInfo(
            "disable_offline:1",
            "DisabledOffline",
            True,
            bool,
            "Determines if this good can be used while the game is disconnected from the network.",
        ),
        ParamFieldInfo(
            "isEquip:1",
            "CanBeEquipped",
            True,
            bool,
            "Determines if this good can be equipped in a quick item slot.",
        ),
        ParamFieldInfo(
            "isConsume:1",
            "ConsumedOnUse",
            True,
            bool,
            "Determines if this good is consumed (count decreases) when used.",
        ),
        ParamFieldInfo(
            "isAutoEquip:1",
            "AutomaticallyEquipped",
            True,
            bool,
            "Determines if this good will be equipped in an available quick slot when obtained.",
        ),
        ParamFieldInfo("isEstablishment:1", "IsStationary", True, bool, "Unknown; need to look at usage."),
        ParamFieldInfo("isOnlyOne:1", "IsUnique", True, bool, "Determines if only one of this good exists in the game."),
        ParamFieldInfo("isDrop:1", "CanBeDropped", True, bool, "Determines if this item can be dropped."),
        ParamFieldInfo("isDeposit:1", "CanBeStored", True, bool, "Determines if good can be stored in Bottomless Box."),
        ParamFieldInfo(
            "isDisableHand:1", "IsDisableHand?", True, bool, "Not sure. Could disable model hand when good is used?"
        ),
        ParamFieldInfo(
            "IsTravelItem:1", "IsTravelItem?", True, bool, "Not sure. Could flag items that warp the player."
        ),
        ParamFieldInfo(
            "isSuppleItem:1", "IsEmptyEstusFlask?", True, bool, "Not sure. Only enabled for empty Estus Flask."
        ),
        ParamFieldInfo(
            "isFullSuppleItem:1",
            "IsNonEmptyEstusFlask?",
            True,
            bool,
            "Not sure. Only enabled for non-empty Estus Flask.",
        ),
        ParamFieldInfo("isEnhance:1", "IsUpgradeMaterial", True, bool, "Determines if this is an upgrade material."),
        ParamFieldInfo("isFixItem:1", "IsFixItem?", True, bool, "Probably True for Repair Powder, etc."),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            True,
            bool,
            "If True, this good cannot be given to other players by dropping it.",
        ),
        ParamFieldInfo(
            "disableUseAtColiseum:1",
            "DisabledInArena",
            False,
            bool,
            "If True, this good cannot be used in the PvP Arena in Oolacile.",
        ),
        ParamFieldInfo(
            "disableUseAtOutOfColiseum:1",
            "DisabledOutsideArena",
            False,
            bool,
            "If True, this good cannot be used outside the PvP Arena in Oolacile.",
        ),
        ParamFieldInfo("useBulletMaxNum:1", "UseMaxBulletCount", True, EQUIP_BOOL, ""),
        ParamFieldInfo("useHpCureMaxNum:1", "UseHealingMaxCount", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isAutoReplenish:1", "AutoReplenishes", True, EQUIP_BOOL, ""),
        ParamFieldInfo("canMultiUse:1", "CanMultiUse", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isEnchantLeftHand:1", "EnchantsLeftHand", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isGuestDrop:1", "CanDropToSummons", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isApplySpecialEffect:1", "ApplySpecialEffect", True, EQUIP_BOOL, ""),
        ParamFieldInfo("pad0:3", "Pad", False, bit_pad_field(3), ""),
        ParamFieldInfo("maxRepositoryNum", "MaxStorageCount", True, int, ""),
        ParamFieldInfo("properStrength", "RequiredStrength", True, int, ""),
        ParamFieldInfo("properAgility", "RequiredDexterity", True, int, ""),
        ParamFieldInfo("properMagic", "RequiredBloodtinge", True, int, ""),
        ParamFieldInfo("properFaith", "RequiredArcane", True, int, ""),
        ParamFieldInfo("pad[2]", "Pad", False, pad_field(2), ""),
        ParamFieldInfo("vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
        ParamFieldInfo("refVirtualWepId", "VirtualWeaponID", True, int, ""),
        ParamFieldInfo("bulletConsumeNum", "BulletCost", True, int, ""),
        ParamFieldInfo("useLimitCategory2", "UseLimitCategory2", True, SP_EFFECT_USELIMIT_CATEGORY, ""),
        ParamFieldInfo("pad1[2]", "Pad", False, pad_field(2), ""),
        ParamFieldInfo("replaceItemId_bySpEffect", "ReplaceItemIDBySpecialEffect", True, int, ""),
        ParamFieldInfo("replaceTriggerSpEffectId", "ReplaceTriggerSpecialEffect", True, int, ""),
    ],
}


ITEMLOT_PARAM_ST = {
    "param_type": "ITEMLOT_PARAM_ST",
    "file_name": "ItemLotParam",
    "nickname": "ItemLots",
    "fields": [
        ParamFieldInfo(
            "getItemFlagId", "ItemFlag", True, Flag, "Flag enabled when any item from this item lot is picked up."
        ),
        ParamFieldInfo(
            "cumulateNumFlagId",
            "FirstCumulativeFlag",
            True,
            Flag,
            "First of eight consecutive flags used to store the cumulative points for this item lot.",
        ),
        ParamFieldInfo(
            "cumulateNumMax",
            "MaxCumulativeAdditions",
            True,
            int,
            "Maximum number of times that cumulative points will be added to the total. I suspect that the "
            "cumulative slot may be awarded automatically after this; if not, I don't know how the Symbol of "
            "Avarice always drops after all seven Mimics are killed.",
        ),
        ParamFieldInfo(
            "lotItem_Rarity",
            "ItemLotRarity",
            True,
            int,
            "Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set "
            "to 2 for all character drops except Crystal Lizards, who have 3.",
        ),
        ParamFieldInfo("lotItemCategory01", "Item1Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 1)."),
        DynamicItemLotRef("lotItemId01", "lotItemCategory01"),
        ParamFieldInfo("lotItemNum01", "Item1Count", True, int, "Count of item (slot 1)."),
        ParamFieldInfo(
            "lotItemBasePoint01",
            "Item1ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId01",
            "Item1Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck01:1",
            "Item1LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint01",
            "Item1CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset01:1",
            "Item1ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory02", "Item2Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 2)."),
        DynamicItemLotRef("lotItemId02", "lotItemCategory02"),
        ParamFieldInfo("lotItemNum02", "Item2Count", True, int, "Count of item (slot 2)."),
        ParamFieldInfo(
            "lotItemBasePoint02",
            "Item2ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId02",
            "Item2Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck02:1",
            "Item2LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint02",
            "Item2CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset02:1",
            "Item2ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory03", "Item3Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 3)."),
        DynamicItemLotRef("lotItemId03", "lotItemCategory03"),
        ParamFieldInfo("lotItemNum03", "Item3Count", True, int, "Count of item (slot 3)."),
        ParamFieldInfo(
            "lotItemBasePoint03",
            "Item3ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId03",
            "Item3Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck03:1",
            "Item3LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint03",
            "Item3CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset03:1",
            "Item3ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory04", "Item4Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 4)."),
        DynamicItemLotRef("lotItemId04", "lotItemCategory04"),
        ParamFieldInfo("lotItemNum04", "Item4Count", True, int, "Count of item (slot 4)."),
        ParamFieldInfo(
            "lotItemBasePoint04",
            "Item4ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId04",
            "Item4Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck04:1",
            "Item4LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint04",
            "Item4CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset04:1",
            "Item4ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory05", "Item5Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 5)."),
        DynamicItemLotRef("lotItemId05", "lotItemCategory05"),
        ParamFieldInfo("lotItemNum05", "Item5Count", True, int, "Count of item (slot 5)."),
        ParamFieldInfo(
            "lotItemBasePoint05",
            "Item5ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId05",
            "Item5Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck05:1",
            "Item5LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint05",
            "Item5CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset05:1",
            "Item5ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory06", "Item6Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 6)."),
        DynamicItemLotRef("lotItemId06", "lotItemCategory06"),
        ParamFieldInfo("lotItemNum06", "Item6Count", True, int, "Count of item (slot 6)."),
        ParamFieldInfo(
            "lotItemBasePoint06",
            "Item6ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId06",
            "Item6Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck06:1",
            "Item6LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint06",
            "Item6CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset06:1",
            "Item6ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory07", "Item7Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 7)."),
        DynamicItemLotRef("lotItemId07", "lotItemCategory07"),
        ParamFieldInfo("lotItemNum07", "Item7Count", True, int, "Count of item (slot 7)."),
        ParamFieldInfo(
            "lotItemBasePoint07",
            "Item7ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId07",
            "Item7Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck07:1",
            "Item7LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint07",
            "Item7CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset07:1",
            "Item7ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        ParamFieldInfo("lotItemCategory08", "Item8Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 8)."),
        DynamicItemLotRef("lotItemId08", "lotItemCategory08"),
        ParamFieldInfo("lotItemNum08", "Item8Count", True, int, "Count of item (slot 8)."),
        ParamFieldInfo(
            "lotItemBasePoint08",
            "Item8ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        ParamFieldInfo(
            "getItemFlagId08",
            "Item8Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        ParamFieldInfo(
            "enableLuck08:1",
            "Item8LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        ParamFieldInfo(
            "cumulateLotPoint08",
            "Item8CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        ParamFieldInfo(
            "cumulateReset08:1",
            "Item8ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
    ],
}


ITEMLOT_LVDEP_PARAM_ST = {
    "param_type": "ITEMLOT_LVDEP_PARAM_ST",
    "file_name": "ItemLotLvdepParam",
    "nickname": "ItemLotsWithScaling",
    "fields": [
        ParamFieldInfo("itemCategory", "", True, ITEMLOT_LVDEP_ITEMCATEGORY, ""),
        ParamFieldInfo("itemId", "", True, int, ""),  # TODO: dynamic item field
    ],
}


EQUIP_PARAM_WEAPON_ST = {
    "param_type": "EQUIP_PARAM_WEAPON_ST",
    "file_name": "EquipParamWeapon",
    "nickname": "Weapons",
    "fields": [
        ParamFieldInfo(
            "behaviorVariationId",
            "BehaviorVariationID",
            True,
            int,
            "Multiplied by 1000 and added to player behavior lookups (hitboxes, bullets) triggered by TAE.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo(
            "wanderingEquipId", "GhostWeaponReplacement", True, WeaponParam, "Weapon replacement for ghosts."
        ),
        ParamFieldInfo("weight", "Weight", True, float, "Weight of weapon."),
        ParamFieldInfo(
            "weaponWeightRate",
            "WeightRatio",
            True,
            float,
            "Unknown effect. Value is about evenly split between 0 and 1 across weapons, with no obvious pattern.",
        ),
        ParamFieldInfo(
            "fixPrice",
            "RepairCost",
            True,
            int,
            "Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
            "durability over max durability.", 
        ),
        ParamFieldInfo("basicPrice", "BasicCost", False, int, "Unknown purpose, and unused."),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo(
            "correctStrength",
            "StrengthScaling",
            True,
            float,
            "Amount of attack power gained from strength. (I believe this is the percentage of the player's "
            "strength to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)", 
        ),
        ParamFieldInfo(
            "correctAgility",
            "DexterityScaling",
            True,
            float,
            "Amount of attack power gained from dexterity. (I believe this is the percentage of the player's "
            "dexterity to add to the weapon's attack power, but it also depends on ScalingFormulaType below.).", 
        ),
        ParamFieldInfo(
            "correctMagic",
            "IntelligenceScaling",
            True,
            float,
            "Amount of attack power gained from intelligence. (I believe this is the percentage of the player's "
            "intelligence to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)", 
        ),
        ParamFieldInfo(
            "correctFaith",
            "FaithScaling",
            True,
            float,
            "Amount of attack power gained from faith. (I believe this is the percentage of the player's faith to "
            "add to the weapon's attack power, but it also depends on ScalingFormulaType below.)", 
        ),
        ParamFieldInfo(
            "physGuardCutRate",
            "PhysicalGuardPercentage",
            True,
            float,
            "Percentage of physical damage prevented when guarding with this weapon.",
        ),
        ParamFieldInfo(
            "magGuardCutRate",
            "MagicGuardPercentage",
            True,
            float,
            "Percentage of magic damage prevented when guarding with this weapon.",
        ),
        ParamFieldInfo(
            "fireGuardCutRate",
            "FireGuardPercentage",
            True,
            float,
            "Percentage of fire damage prevented when guarding with this weapon.",
        ),
        ParamFieldInfo(
            "thunGuardCutRate",
            "LightningGuardPercentage",
            True,
            float,
            "Percentage of lightning damage prevented when guarding with this weapon.",
        ),
        ParamFieldInfo(
            "spEffectBehaviorId0",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 0).",
        ),
        ParamFieldInfo(
            "spEffectBehaviorId1",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 1).",
        ),
        ParamFieldInfo(
            "spEffectBehaviorId2",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 2).",
        ),
        ParamFieldInfo(
            "residentSpEffectId",
            "EquippedSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 0).",
        ),
        ParamFieldInfo(
            "residentSpEffectId1",
            "EquippedSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 1).",
        ),
        ParamFieldInfo(
            "residentSpEffectId2",
            "EquippedSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 2).",
        ),
        ParamFieldInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade Material parameter that sets costs for weapon reinforcement.",
        ),
        ParamFieldInfo(
            "originEquipWep",
            "UpgradeOrigin0",
            True,
            WeaponParam,
            "Origin armor for level 0 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep1",
            "UpgradeOrigin1",
            True,
            WeaponParam,
            "Origin armor for level 1 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep2",
            "UpgradeOrigin2",
            True,
            WeaponParam,
            "Origin armor for level 2 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep3",
            "UpgradeOrigin3",
            True,
            WeaponParam,
            "Origin armor for level 3 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep4",
            "UpgradeOrigin4",
            True,
            WeaponParam,
            "Origin armor for level 4 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep5",
            "UpgradeOrigin5",
            True,
            WeaponParam,
            "Origin armor for level 5 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep6",
            "UpgradeOrigin6",
            True,
            WeaponParam,
            "Origin armor for level 6 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep7",
            "UpgradeOrigin7",
            True,
            WeaponParam,
            "Origin armor for level 7 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep8",
            "UpgradeOrigin8",
            True,
            WeaponParam,
            "Origin armor for level 8 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep9",
            "UpgradeOrigin9",
            True,
            WeaponParam,
            "Origin armor for level 9 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep10",
            "UpgradeOrigin10",
            True,
            WeaponParam,
            "Origin armor for level 10 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep11",
            "UpgradeOrigin11",
            True,
            WeaponParam,
            "Origin armor for level 11 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep12",
            "UpgradeOrigin12",
            True,
            WeaponParam,
            "Origin armor for level 12 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep13",
            "UpgradeOrigin13",
            True,
            WeaponParam,
            "Origin armor for level 13 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep14",
            "UpgradeOrigin14",
            True,
            WeaponParam,
            "Origin armor for level 14 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "originEquipWep15",
            "UpgradeOrigin15",
            True,
            WeaponParam,
            "Origin armor for level 15 of this weapon (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.", 
        ),
        ParamFieldInfo(
            "antiDemonDamageRate",
            "DamageAgainstDemonsMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against demons with this weapon.",
        ),
        ParamFieldInfo(
            "antSaintDamageRate",
            "WeakToDivineDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against enemies weak to divine (e.g. skeletons) with this weapon.",
        ),
        ParamFieldInfo(
            "antWeakA_DamageRate",
            "GodDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against Gods and Goddesses with this weapon.",
        ),
        ParamFieldInfo(
            "antWeakB_DamageRate",
            "AbyssDamageMultiplier",
            True,
            float,
            "Multiplier applied to damage dealt against enemies from the Abyss with this weapon.",
        ),
        ParamFieldInfo("levelSyncCorrectId", "LevelSyncCorrectID", True, int, ""),
        ParamFieldInfo("pad[2]", "Pad", False, pad_field(2), ""),
        ParamFieldInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""
        ),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
        ParamFieldInfo("equipModelId", "WeaponModel", True, int, "Weapon model ID."),
        ParamFieldInfo("iconId", "WeaponIcon", True, Texture, "Weapon icon texture ID."),
        ParamFieldInfo(
            "durability",
            "InitialDurability",
            True,
            int,
            "Durability of weapon when it is obtained. Always equal to max durability in vanilla game.",
        ),
        ParamFieldInfo("durabilityMax", "MaxDurability", True, int, "Maximum durability of weapon."),
        ParamFieldInfo(
            "attackThrowEscape",
            "ThrowEscapePower",
            False,
            int,
            "Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement "
            "weapons.", 
        ),
        ParamFieldInfo(
            "parryDamageLife",
            "MaxParryWindowDuration",
            False,
            int,
            "Maximum parry window duration (cannot exceed TAE duration). Always set to 10.",
        ),
        ParamFieldInfo("attackBasePhysics", "BasePhysicalDamage", True, int, "Base physical damage of weapon attacks."),
        ParamFieldInfo("attackBaseMagic", "BaseMagicDamage", True, int, "Base magic damage of weapon attacks."),
        ParamFieldInfo("attackBaseFire", "BaseFireDamage", True, int, "Base fire damage of weapon attacks."),
        ParamFieldInfo(
            "attackBaseThunder", "BaseLightningDamage", True, int, "Base lightning damage of weapon attacks."
        ),
        ParamFieldInfo("attackBaseStamina", "BaseStaminaDamage", True, int, "Base stamina damage of weapon attacks."),
        ParamFieldInfo("saWeaponDamage", "BasePoiseDamage", True, int, "Base poise damage of weapon attacks."),
        ParamFieldInfo(
            "saDurability",
            "AttackPoiseBonus",
            False,
            int,
            "Poise gained during attack animations with this weapon. Never used (probably done in TAE).",
        ),
        ParamFieldInfo(
            "guardAngle",
            "EffectiveGuardAngle",
            False,
            int,
            "Angle that can be guarded with this weapon. Never used.",
        ),
        ParamFieldInfo(
            "staminaGuardDef",
            "GuardStaminaDefense",
            True,
            int,
            "Defense against (i.e. value subtracted from) stamina attack damage while guarding.",
        ),
        ParamFieldInfo(
            "reinforceTypeId",
            "WeaponUpgradeID",
            True,
            WeaponUpgradeParam,
            "Weapon Upgrade parameter that specifies upgrade benefits.",
        ),
        ParamFieldInfo(
            "compTrophySedId",
            "AllWeaponsAchievementGroup",
            False,
            int,
            "Index of weapon as it contributes to the Knight's Honor achievement.",
        ),
        ParamFieldInfo(
            "trophySeqId",
            "MaxUpgradeAchievementID",
            False,
            int,
            "Achievement unlocked when weapon is upgraded to maximum level (one per upgrade path).",
        ),
        ParamFieldInfo(
            "throwAtkRate",
            "ThrowDamageChangePercentage",
            True,
            int,
            "Percentage damage increase (if positive) or decrease (if negative) during backstabs and ripostes "
            "with this weapon.", 
        ),
        ParamFieldInfo(
            "bowDistRate",
            "BowRangeChangePercentage",
            True,
            int,
            "Percentage range increase (if positive) or decrease (if negative) with this bow.",
        ),
        ParamFieldInfo(
            "equipModelCategory",
            "WeaponModelCategory",
            False,
            EQUIP_MODEL_CATEGORY,
            "Model category for equipment. Only one option for weapons.",
        ),
        ParamFieldInfo(
            "equipModelGender",
            "WeaponModelGender",
            False,
            EQUIP_MODEL_GENDER,
            "Model gender variant. All weapons are genderless.",
        ),
        ParamFieldInfo(
            "weaponCategory",
            "WeaponCategory",
            True,
            WEAPON_CATEGORY,
            "Basic category of weapon. Many 'weapon types' you may be familiar with are merged here (e.g. whips "
            "are straight swords).", 
        ),
        ParamFieldInfo(
            "wepmotionCategory",
            "AttackAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Basic weapon attack animation type. More diverse than WeaponCategory. This number is multiplied by "
            "10000 and used as an animation offset for all attacks, I believe.", 
        ),
        ParamFieldInfo(
            "guardmotionCategory",
            "GuardAnimationCategory",
            True,
            GUARDMOTION_CATEGORY,
            "Basic weapon/shield block animation type.",
        ),
        ParamFieldInfo(
            "atkMaterial",
            "VisualSoundEffectsOnHit",
            True,
            WEP_MATERIAL_ATK,
            "Determines the sounds and visual effects generated when this weapon hits.",
        ),
        ParamFieldInfo(
            "defMaterial",
            "VisualEffectsOnBlock",
            True,
            WEP_MATERIAL_DEF,
            "Determines the visual effects generated when this weapon blocks an attack.",
        ),
        ParamFieldInfo(
            "defSfxMaterial",
            "SoundEffectsOnBlock",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Determines the sound effects generated when this weapon blocks an attack.",
        ),
        ParamFieldInfo(
            "correctType",
            "ScalingFormulaType",
            True,
            WEP_CORRECT_TYPE,
            "Determines how scaling changes with attribute level.",
        ),
        ParamFieldInfo(
            "spAttribute",
            "ElementAttribute",
            True,
            ATKPARAM_SPATTR_TYPE,
            "Element attached to hits with this weapon.",
        ),
        ParamFieldInfo(
            "spAtkcategory",
            "SpecialAttackCategory",
            True,
            WEPMOTION_CATEGORY,
            "Overrides AttackAnimationCategory for some attacks. Ranges from 50 to 199 (or 0 for none). Often "
            "used to give weapons unique strong (R2) attacks, for example, but can override any attack animation.", 
        ),
        ParamFieldInfo(
            "wepmotionOneHandId",
            "OneHandedAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Animation category for one-handed non-attack animations (like walking).",
        ),
        ParamFieldInfo(
            "wepmotionBothHandId",
            "TwoHandedAnimationCategory",
            True,
            WEPMOTION_CATEGORY,
            "Animation category for two-handed non-attack animations (like walking).",
        ),
        ParamFieldInfo(
            "properStrength",
            "RequiredStrength",
            True,
            int,
            "Required strength to wield weapon properly. (Reduced by one third if held two-handed.)",
        ),
        ParamFieldInfo("properAgility", "RequiredDexterity", True, int, "Required dexterity to wield weapon properly."),
        ParamFieldInfo(
            "properMagic", "RequiredIntelligence", True, int, "Required intelligence to wield weapon properly."
        ),
        ParamFieldInfo("properFaith", "RequiredFaith", True, int, "Required faith to wield weapon properly."),
        ParamFieldInfo(
            "overStrength", "OverStrength", False, int, "Unknown. Always set to 99, except for arrows and bolts."
        ),
        ParamFieldInfo("attackBaseParry", "AttackBaseParry", False, int, "Unknown. Never used."),
        ParamFieldInfo("defenseBaseParry", "DefenseBaseParry", False, int, "Unknown. Never used."),
        ParamFieldInfo(
            "guardBaseRepel",
            "DeflectOnBlock",
            True,
            int,
            "Determines if an enemy will be deflected when you block them with this weapon (by comparing it to "
            "their DeflectOnAttack).", 
        ),
        ParamFieldInfo(
            "attackBaseRepel",
            "DeflectOnAttack",
            True,
            int,
            "Determines if this weapon will be deflected when attacking a blocking enemy (by comparing it to "
            "their DeflectOnBlock).", 
        ),
        ParamFieldInfo(
            "guardCutCancelRate",
            "IgnoreGuardPercentage",
            False,
            int,
            "Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
            "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, "
            "in favor of the simple 'IgnoreGuard' boolean field.", 
        ),
        ParamFieldInfo(
            "guardLevel",
            "GuardLevel",
            True,
            int,
            "Internal description: 'in which guard motion is the enemy attacked when guarded?' Exact effects are "
            "unclear, but this ranges from 0 to 4 in effectiveness of blocking in a predictable way (daggers are "
            "worse than swords, which are worse than greatswords, which are worse than all shields).", 
        ),
        ParamFieldInfo("slashGuardCutRate", "SlashDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo("blowGuardCutRate", "StrikeDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo("thrustGuardCutRate", "ThrustDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo(
            "poisonGuardResist",
            "PoisonDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming poison damage ignored when guarding.",
        ),
        ParamFieldInfo(
            "diseaseGuardResist",
            "ToxicDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming toxic damage ignored when guarding.",
        ),
        ParamFieldInfo(
            "bloodGuardResist",
            "BleedDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming bleed damage ignored when guarding.",
        ),
        ParamFieldInfo(
            "curseGuardResist",
            "CurseDamageReductionWhenGuarding",
            True,
            int,
            "Percentage of incoming curse damage ignored when guarding.",
        ),
        ParamFieldInfo(
            "isDurabilityDivergence",
            "DurabilityDivergenceCategory",
            True,
            DURABILITY_DIVERGENCE_CATEGORY,
            "Determines an alternate animation used if the player tries to use this weapon's special attack "
            "without having enough durability to use it. Exact enumeration is unknown, but existing usages are "
            "documented.", 
        ),
        ParamFieldInfo(
            "rightHandEquipable:1",
            "RightHandAllowed",
            True,
            bool,
            "If True, this weapon can be equipped in the right hand.",
        ),
        ParamFieldInfo(
            "leftHandEquipable:1",
            "LeftHandAllowed",
            True,
            bool,
            "If True, this weapon can be equipped in the left hand.",
        ),
        ParamFieldInfo(
            "bothHandEquipable:1",
            "BothHandsAllowed",
            True,
            bool,
            "If True, this weapon can be held in two-handed mode.",
        ),
        ParamFieldInfo(
            "arrowSlotEquipable:1",
            "UsesEquippedArrows",
            True,
            bool,
            "If True, this weapon will use equipped arrow slot.",
        ),
        ParamFieldInfo(
            "boltSlotEquipable:1",
            "UsesEquippedBolts",
            True,
            bool,
            "If True, this weapon will use equipped bolt slot.",
        ),
        ParamFieldInfo(
            "enableGuard:1",
            "GuardEnabled",
            True,
            bool,
            "If True, the player can guard with this weapon by holding L1.",
        ),
        ParamFieldInfo(
            "enableParry:1",
            "ParryEnabled",
            True,
            bool,
            "If True, the player can parry with this weapon by pressing L2.",
        ),
        ParamFieldInfo(
            "enableMagic:1", "CanCastSorceries", True, bool, "If True, this weapon can be used to cast sorceries."
        ),
        ParamFieldInfo(
            "enableSorcery:1", "CanCastPyromancy", True, bool, "If True, this weapon can be used to cast pyromancy."
        ),
        ParamFieldInfo(
            "enableMiracle:1", "CanCastMiracles", True, bool, "If True, this weapon can be used to cast miracles."
        ),
        ParamFieldInfo("enableVowMagic:1", "CanCastCovenantMagic", True, bool, ""),
        ParamFieldInfo("isNormalAttackType:1", "DealsNeutralDamage", True, bool, ""),
        ParamFieldInfo("isBlowAttackType:1", "DealsStrikeDamage", True, bool, ""),
        ParamFieldInfo("isSlashAttackType:1", "DealsSlashDamage", True, bool, ""),
        ParamFieldInfo("isThrustAttackType:1", "DealsThrustDamage", True, bool, ""),
        ParamFieldInfo("isEnhance:1", "IsUpgraded", True, bool, ""),
        ParamFieldInfo("isLuckCorrect:1", "IsAffectedByLuck", True, bool, ""),
        ParamFieldInfo("isCustom:1", "IsCustom?", True, bool, ""),
        ParamFieldInfo("disableBaseChangeReset:1", "DisableBaseChangeReset", True, bool, ""),
        ParamFieldInfo("disableRepair:1", "DisableRepairs", True, bool, "If True, this weapon cannot be repaired."),
        ParamFieldInfo("isDarkHand:1", "IsDarkHand", False, bool, "Enabled only for the Dark Hand."),
        ParamFieldInfo("simpleModelForDlc:1", "SimpleDLCModelExists", False, bool, "Unknown; always set to False."),
        ParamFieldInfo("lanternWep:1", "IsLantern?", True, bool, ""),
        ParamFieldInfo(
            "isVersusGhostWep:1",
            "CanHitGhosts",
            True,
            bool,
            "If True, this weapon can hit ghosts without a Transient Curse active.",
        ),
        ParamFieldInfo(
            "baseChangeCategory:6", "BaseChangeCategory", False, int, "Never used. Likely Demon's Souls junk."
        ),
        ParamFieldInfo("isDragonSlayer:1", "IsDragonSlayer", True, bool, ""),
        ParamFieldInfo(
            "isDeposit:1",
            "CanBeStored",
            True,
            bool,
            "If True, this weapon can be stored in the Bottomless Box. Always True for rings.",
        ),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this weapon cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        ParamFieldInfo("invisibleOnRemo:1", "InvisibleInCutscenes", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isAttributeWep:1", "IsAttributeWeapon", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isEnchantLeftHand:1", "EnchantsLeftHand", True, EQUIP_BOOL, ""),
        ParamFieldInfo("isGuestDrop:1", "CanDropToSummons", True, EQUIP_BOOL, ""),
        ParamFieldInfo("therianthropeGuardResist", "BeastResistanceOnGuard", True, int, ""),
        ParamFieldInfo("PhysAtkMenuDispType", "PhysicalAttackMenuDisplayType", True, PHYS_ATK_MENU_DISP_TYPE, ""),
        ParamFieldInfo("wepmotionHangType", "WeaponMotionHangType", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0RightHang", "Slot0RightHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0RightFormA", "Slot0RightFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0RightFormB", "Slot0RightFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0LeftHang", "Slot0LeftHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0LeftFormA", "Slot0LeftFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot0LeftFormB", "Slot0LeftFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1RightHang", "Slot1RightHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1RightFormA", "Slot1RightFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1RightFormB", "Slot1RightFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1LeftHang", "Slot1LeftHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1LeftFormA", "Slot1LeftFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot1LeftFormB", "Slot1LeftFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2RightHang", "Slot2RightHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2RightFormA", "Slot2RightFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2RightFormB", "Slot2RightFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2LeftHang", "Slot2LeftHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2LeftFormA", "Slot2LeftFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot2LeftFormB", "Slot2LeftFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3RightHang", "Slot3RightHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3RightFormA", "Slot3RightFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3RightFormB", "Slot3RightFormBModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3LeftHang", "Slot3LeftHangModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3LeftFormA", "Slot3LeftFormAModelPoint", True, int, ""),
        ParamFieldInfo("dmypolyId_Slot3LeftFormB", "Slot3LeftFormBModelPoint", True, int, ""),
        ParamFieldInfo("wepRegainHp", "WeaponRegainHP", True, int, ""),
        ParamFieldInfo("bulletConsumeNum", "BulletCost", True, int, ""),
        ParamFieldInfo("repositoryCategory", "StorageCategory", True, int, ""),
    ],
}


EQUIP_MTRL_SET_PARAM_ST = {
    "param_type": "EQUIP_MTRL_SET_PARAM_ST",
    "file_name": "EquipMtrlSetParam",
    "nickname": "UpgradeMaterials",
    "fields": [
        ParamFieldInfo("materialId01", "UpgradeGood", True, GoodParam, "Good required to upgrade weapon."),
        ParamFieldInfo(
            "materialId02",
            "UpgradeGood2",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "materialId03",
            "UpgradeGood3",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "materialId04",
            "UpgradeGood4",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "materialId05",
            "UpgradeGood5",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        ParamFieldInfo("itemNum01", "UpgradeQuantity", True, int, "Amount of Upgrade Good required for reinforcement."),
        ParamFieldInfo(
            "itemNum02",
            "UpgradeQuantity2",
            False,
            int,
            "Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "itemNum03",
            "UpgradeQuantity3",
            False,
            int,
            "Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "itemNum04",
            "UpgradeQuantity4",
            False,
            int,
            "Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "itemNum05",
            "UpgradeQuantity5",
            False,
            int,
            "Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        ParamFieldInfo(
            "isDisableDispNum01:1",
            "DisableQuantityIndicator",
            True,
            bool,
            "If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is "
            "needed.", 
        ),
        ParamFieldInfo(
            "isDisableDispNum02:1",
            "DisableQuantityIndicator2",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        ParamFieldInfo(
            "isDisableDispNum03:1",
            "DisableQuantityIndicator3",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        ParamFieldInfo(
            "isDisableDispNum04:1",
            "DisableQuantityIndicator4",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        ParamFieldInfo(
            "isDisableDispNum05:1",
            "DisableQuantityIndicator5",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        ParamFieldInfo("pad[6]", "Pad1", False, pad_field(6), "Null padding."),
    ],
}


REINFORCE_PARAM_WEAPON_ST = {
    "param_type": "REINFORCE_PARAM_WEAPON_ST",
    "file_name": "ReinforceParamWeapon",
    "nickname": "WeaponUpgrades",
    "fields": [
        ParamFieldInfo(
            "physicsAtkRate",
            "PhysicalDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing physical damage (of any type).",
        ),
        ParamFieldInfo(
            "magicAtkRate", "MagicDamageMultiplier", True, float, "Multiplier applied to outgoing magic damage."
        ),
        ParamFieldInfo(
            "fireAtkRate", "FireDamageMultiplier", True, float, "Multiplier applied to outgoing fire damage."
        ),
        ParamFieldInfo(
            "thunderAtkRate",
            "LightningDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing lightning damage.",
        ),
        ParamFieldInfo(
            "staminaAtkRate",
            "StaminaDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' stamina.",
        ),
        ParamFieldInfo(
            "saWeaponAtkRate",
            "PoiseDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' poise. Never used.",
        ),
        ParamFieldInfo(
            "saDurabilityRate",
            "PoiseDefenseMultiplier",
            True,
            float,
            "Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used.",
        ),
        ParamFieldInfo(
            "correctStrengthRate",
            "StrengthScalingMultiplier",
            True,
            float,
            "Multiplier applied to strength scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctAgilityRate",
            "DexterityScalingMultiplier",
            True,
            float,
            "Multiplier applied to dexterity scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctMagicRate",
            "IntelligenceScalingMultiplier",
            True,
            float,
            "Multiplier applied to intelligence scaling of this weapon.",
        ),
        ParamFieldInfo(
            "correctFaithRate",
            "FaithScalingMultiplier",
            True,
            float,
            "Multiplier applied to faith scaling of this weapon.",
        ),
        ParamFieldInfo(
            "physicsGuardCutRate",
            "PhysicalGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of physical damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "magicGuardCutRate",
            "MagicGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of magic damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "fireGuardCutRate",
            "FireGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of fire damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "thunderGuardCutRate",
            "LightningGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of lightning damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "poisonGuardResistRate",
            "PoisonGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of poison damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "diseaseGuardResistRate",
            "ToxicGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of toxic damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "bloodGuardResistRate",
            "BleedGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of bleed damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "curseGuardResistRate",
            "CurseGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of curse damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "staminaGuardDefRate",
            "StaminaGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of stamina damage blocked by this weapon/shield.",
        ),
        ParamFieldInfo(
            "spEffectId1",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "spEffectId2",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "spEffectId3",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters.",
        ),
        ParamFieldInfo(
            "residentSpEffectId1",
            "EquippedSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
            "parameters.", 
        ),
        ParamFieldInfo(
            "residentSpEffectId2",
            "EquippedSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
            "parameters.", 
        ),
        ParamFieldInfo(
            "residentSpEffectId3",
            "EquippedSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
            "parameters.", 
        ),
        ParamFieldInfo(
            "materialSetId",
            "UpgradeMaterialOffset",
            True,
            int,
            "Value to be added to Upgrade Materials field in base weapon parameters.",
        ),
        ParamFieldInfo("pad[9]", "Pad", False, pad_field(9), ""),
    ],
}


PROTECTOR_GEN_PARAM_ST = {
    "param_type": "PROTECTOR_GEN_PARAM_ST",
    "file_name": "ProtectorGenParam",
    "nickname": "ArmorGenerators",
    "fields": [
        ParamFieldInfo("proParamId", "ArmorParamID", True, ArmorParam, ""),
        ParamFieldInfo("gemSlotType_0", "GemSlotType0", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_0", "GemGeneratorID0", True, int, ""),  # TODO: Gem Generator param type
        ParamFieldInfo("gemSlotType_1", "GemSlotType1", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_1", "GemGeneratorID1", True, int, ""),
        ParamFieldInfo("gemSlotType_2", "GemSlotType2", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_2", "GemGeneratorID2", True, int, ""),
        ParamFieldInfo("gemSlotType_3", "GemSlotType3", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_3", "GemGeneratorID3", True, int, ""),
        ParamFieldInfo("gemSlotType_4", "GemSlotType4", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_4", "GemGeneratorID4", True, int, ""),
    ],
}


WEAPON_GEN_PARAM_ST = {
    "param_type": "WEAPON_GEN_PARAM_ST",
    "file_name": "WeaponGenParam",
    "nickname": "WeaponGenerators",
    "fields": [
        ParamFieldInfo("wepParamId", "WeaponParamID", True, WeaponParam, ""),
        ParamFieldInfo("gemSlotType_0", "GemSlotType0", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_0", "GemGeneratorID0", True, int, ""),
        ParamFieldInfo("gemSlotType_1", "GemSlotType1", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_1", "GemGeneratorID1", True, int, ""),
        ParamFieldInfo("gemSlotType_2", "GemSlotType2", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_2", "GemGeneratorID2", True, int, ""),
        ParamFieldInfo("gemSlotType_3", "GemSlotType3", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_3", "GemGeneratorID3", True, int, ""),
        ParamFieldInfo("gemSlotType_4", "GemSlotType4", True, GEM_SLOT_TYPE_MASK, ""),
        ParamFieldInfo("gemGenId_4", "GemGeneratorID4", True, int, ""),
        ParamFieldInfo("equipableGemSegmentMask", "EquippableGemSegmentMask", True, GEM_SEGMENT_MASK, ""),
        ParamFieldInfo("reserveGemSlotNo_0", "ReserveGemSlot0", True, GEM_SLOT_TYPE_NO, ""),
        ParamFieldInfo("reserveGemSlotNo_1", "ReserveGemSlot1", True, GEM_SLOT_TYPE_NO, ""),
        ParamFieldInfo("reserveGemSlotNo_2", "ReserveGemSlot2", True, GEM_SLOT_TYPE_NO, ""),
    ],
}
