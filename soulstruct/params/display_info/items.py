__all__ = [
    "EQUIP_PARAM_WEAPON_ST",
    "EQUIP_PARAM_PROTECTOR_ST",
    "EQUIP_PARAM_ACCESSORY_ST",
    "EQUIP_PARAM_GOODS_ST",
    "ITEMLOT_PARAM_ST",
    "EQUIP_MTRL_SET_PARAM_ST",
    "REINFORCE_PARAM_WEAPON_ST",
    "REINFORCE_PARAM_PROTECTOR_ST",
]

from soulstruct.game_types import *
from soulstruct.params.enums import *
from .base import FieldDisplayInfo, DynamicFieldDisplayInfo, pad_field

# Overrides for basic enum.
SP_EFFECT_SPCATEGORY = int


class DynamicGoodRef(DynamicFieldDisplayInfo):
    def __call__(self, entry):
        if entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Default:
            return FieldDisplayInfo(
                self.name,
                "NoReference",
                True,
                int,
                "This value should be -1 when 'Default' reference type is selected.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Bullet:
            return FieldDisplayInfo(
                self.name,
                "Bullet",
                True,
                BulletParam,
                "Bullet triggered by using good (which may simply be targeted at self).",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return FieldDisplayInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special effect triggered (on self) by using good.",
            )
        else:
            return (
                self.name,
                "UnknownReferenceID",
                True,
                int,
                "Could not determine reference ID type (usually Bullet or SpecialEffect).",
            )


class DynamicItemLotRef(DynamicFieldDisplayInfo):
    def __call__(self, entry):
        item_type = entry[self.type_field_name]
        item_lot_slot = int(self.type_field_name[-1])
        if item_type == ITEMLOT_ITEMCATEGORY.Weapon:
            return FieldDisplayInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                WeaponParam,
                f"Item slot {item_lot_slot} (Weapon).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Armor:
            return FieldDisplayInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                ArmorParam,
                f"Item slot {item_lot_slot} (Armor).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Ring:
            return FieldDisplayInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                RingParam,
                f"Item slot {item_lot_slot} (Ring).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Good:
            return FieldDisplayInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                GoodParam,
                f"Item slot {item_lot_slot} (Good).",
            )
        else:
            return FieldDisplayInfo(
                self.name,
                f"ItemSlot{item_lot_slot}",
                True,
                int,
                f"Item slot {item_lot_slot} (unknown item type {item_type}).",
            )


EQUIP_PARAM_PROTECTOR_ST = {
    "paramdef_name": "EQUIP_PARAM_PROTECTOR_ST",
    "file_name": "EquipParamProtector",
    "nickname": "Armor",
    "fields": [
        FieldDisplayInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        FieldDisplayInfo(
            "wanderingEquipId",
            "GhostArmorReplacement",
            True,
            ArmorParam,
            "Replacement equipment for network ghosts.",
        ),
        FieldDisplayInfo("vagrantItemLotId", "VagrantItemLot", True, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", True, ItemLotParam, "DOC-TODO"
        ),
        FieldDisplayInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", True, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "fixPrice",
            "RepairCost",
            True,
            int,
            "Amount of souls required to repair armor fully. Actual repair cost is this multiplied by "
            "current durability over max durability.",
        ),
        FieldDisplayInfo(
            "basicPrice",
            "BasicCost",
            False,
            int,
            "Unsure when this is used. Possibly sets the default if the cost is not specified in Shop "
            "parameters. Always set to 200.",
        ),
        FieldDisplayInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        FieldDisplayInfo("weight", "Weight", True, float, "Weight of armor."),
        FieldDisplayInfo(
            "residentSpEffectId",
            "WearerSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (first of three).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId2",
            "WearerSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (second of three).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId3",
            "WearerSpecialEffect3",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (third of three).",
        ),
        FieldDisplayInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade material set for reinforcement.",
        ),
        FieldDisplayInfo(
            "partsDamageRate",
            "SiteDamageMultiplier",
            True,
            float,
            "Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, "
            "so is never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, "
            "1.1 for gauntlets and leggings, and 1 for torso armor.",
        ),
        FieldDisplayInfo(
            "corectSARecover",
            "PoiseRecoveryTimeModifier",
            True,
            float,
            "Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
            "otherwise.",
        ),
        FieldDisplayInfo(
            "originEquipPro",
            "UpgradeOrigin0",
            True,
            ArmorParam,
            "Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro1",
            "UpgradeOrigin1",
            True,
            ArmorParam,
            "Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro2",
            "UpgradeOrigin2",
            True,
            ArmorParam,
            "Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro3",
            "UpgradeOrigin3",
            True,
            ArmorParam,
            "Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro4",
            "UpgradeOrigin4",
            True,
            ArmorParam,
            "Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro5",
            "UpgradeOrigin5",
            True,
            ArmorParam,
            "Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro6",
            "UpgradeOrigin6",
            True,
            ArmorParam,
            "Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro7",
            "UpgradeOrigin7",
            True,
            ArmorParam,
            "Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro8",
            "UpgradeOrigin8",
            True,
            ArmorParam,
            "Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro9",
            "UpgradeOrigin9",
            True,
            ArmorParam,
            "Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades). If "
            "-1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro10",
            "UpgradeOrigin10",
            True,
            ArmorParam,
            "Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro11",
            "UpgradeOrigin11",
            True,
            ArmorParam,
            "Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro12",
            "UpgradeOrigin12",
            True,
            ArmorParam,
            "Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro13",
            "UpgradeOrigin13",
            True,
            ArmorParam,
            "Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro14",
            "UpgradeOrigin14",
            True,
            ArmorParam,
            "Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "originEquipPro15",
            "UpgradeOrigin15",
            True,
            ArmorParam,
            "Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes "
            "upgrades). If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's "
            "reversion menu.",
        ),
        FieldDisplayInfo(
            "faceScaleM_ScaleX",
            "MaleFaceScaleX",
            True,
            float,
            "Scale factor applied to X dimension of male faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleM_ScaleZ",
            "MaleFaceScaleZ",
            True,
            float,
            "Scale factor applied to Z dimension of male faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleM_MaxX",
            "MaleFaceMaxScaleX",
            True,
            float,
            "Maximum scale permitted for X dimension of male faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleM_MaxZ",
            "MaleFaceMaxScaleZ",
            True,
            float,
            "Maximum scale permitted for Z dimension of male faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleF_ScaleX",
            "FemaleFaceScaleX",
            True,
            float,
            "Scale factor applied to X dimension of female faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleF_ScaleZ",
            "FemaleFaceScaleZ",
            True,
            float,
            "Scale factor applied to Z dimension of female faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleF_MaxX",
            "FemaleFaceMaxScaleX",
            True,
            float,
            "Maximum scale permitted for X dimension of female faces when worn.",
        ),
        FieldDisplayInfo(
            "faceScaleF_MaxZ",
            "FemaleFaceMaxScaleZ",
            True,
            float,
            "Maximum scale permitted for Z dimension of female faces when worn.",
        ),
        FieldDisplayInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        FieldDisplayInfo("equipModelId", "EquipmentModel", True, int, "Model ID of armor."),
        FieldDisplayInfo("iconIdM", "MaleIcon", True, Texture, "Icon of male variant of armor in inventory."),
        FieldDisplayInfo("iconIdF", "FemaleIcon", True, Texture, "Icon of female variant of armor in inventory."),
        FieldDisplayInfo(
            "knockBack",
            "KnockbackPercentageReduction",
            False,
            int,
            "Never used. Probably the percentage of knockback reduced (from 0 to 100) when wearing armor.",
        ),
        FieldDisplayInfo(
            "knockbackBounceRate",
            "KnockbackBouncePercentage",
            False,
            int,
            "Never used. Possibly affects knockback of incoming attacks.",
        ),
        FieldDisplayInfo(
            "durability",
            "InitialDurability",
            True,
            int,
            "Durability of armor when it is obtained. Always equal to max durability in vanilla game.",
        ),
        FieldDisplayInfo("durabilityMax", "MaxDurability", True, int, "Maximum durability of armor."),
        FieldDisplayInfo("saDurability", "Poise", True, int, "Amount of poise added when wearing armor."),
        FieldDisplayInfo(
            "defFlickPower", "RepelDefense", True, int, "Determines when incoming attacks will bounce off."),
        FieldDisplayInfo(
            "defensePhysics", "PhysicalDefense", True, int, "Added defense against physical attack damage."),
        FieldDisplayInfo("defenseMagic", "MagicDefense", True, int, "Added defense against magic attack damage."),
        FieldDisplayInfo("defenseFire", "FireDefense", True, int, "Added defense against fire attack damage."),
        FieldDisplayInfo(
            "defenseThunder", "LightningDefense", True, int, "Added defense against lightning attack damage."
        ),
        FieldDisplayInfo(
            "defenseSlash", "SlashDefense", True, int, "Added defense against physical slash attack damage."),
        FieldDisplayInfo(
            "defenseBlow", "StrikeDefense", True, int, "Added defense against physical strike attack damage."
        ),
        FieldDisplayInfo(
            "defenseThrust", "ThrustDefense", True, int, "Added defense against physical thrust attack damage."
        ),
        FieldDisplayInfo("resistPoison", "PoisonResistance", True, int, "Poison resistance added by armor."),
        FieldDisplayInfo("resistDisease", "ToxicResistance", True, int, "Toxic resistance added by armor."),
        FieldDisplayInfo("resistBlood", "BleedResistance", True, int, "Bleed resistance added by armor."),
        FieldDisplayInfo("resistCurse", "CurseResistance", True, int, "Curse resistance added by armor."),
        FieldDisplayInfo(
            "reinforceTypeId",
            "ArmorUpgradeID",
            True,
            ArmorUpgradeParam,
            "Effects applied at consecutive upgrade reinforcement levels.",
        ),
        FieldDisplayInfo(
            "trophySGradeId",
            "AchievementContributionID",
            False,
            int,
            "Index of armor as it contributes to certain multi-item achievements.",
        ),
        FieldDisplayInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
        ),
        FieldDisplayInfo("knockbackParamId", "KnockbackID", False, KnockbackParam, "Knockback entry. Always 1."),
        FieldDisplayInfo(
            "flickDamageCutRate",
            "RepelDamagePercentageReduction",
            True,
            int,
            "Determines some aspect of attack deflection. Always set to 0 (for light armor) or 255 (for heavy "
            "armor).",
        ),
        FieldDisplayInfo(
            "equipModelCategory",
            "EquipmentModelCategory",
            True,
            EQUIP_MODEL_CATEGORY,
            "Body part covered by armor model.",
        ),
        FieldDisplayInfo(
            "equipModelGender", "EquipmentModelGender", True, EQUIP_MODEL_GENDER, "Gender variant of armor."),
        FieldDisplayInfo("protectorCategory", "ArmorType", True, PROTECTOR_CATEGORY, "Type of armor (equip slot)."),
        FieldDisplayInfo(
            "defenseMaterial",
            "SoundEffectOnHit",
            True,
            WEP_MATERIAL_DEF,
            "Type of sound effect generated when this armor is hit.",
        ),
        FieldDisplayInfo(
            "defenseMaterialSfx",
            "VisualEffectOnHit",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Type of visual effect generated when this armor is hit.",
        ),
        FieldDisplayInfo("partsDmgType", "PartsDamageType", False, ATK_PARAM_PARTSDMGTYPE, "Always zero."),
        FieldDisplayInfo(
            "defenseMaterial_Weak",
            "SoundEffectOnWeakSpotHit",
            True,
            WEP_MATERIAL_DEF,
            "Sound effect for when damage is taken to weak spot (used for head armor).",
        ),
        FieldDisplayInfo(
            "defenseMaterialSfx_Weak",
            "VisualEffectOnWeakSpotHit",
            True,
            WEP_MATERIAL_DEF_SFX,
            "Visual effect for when damage is taken to weak spot (used for head armor).",
        ),
        FieldDisplayInfo(
            "isDeposit:1", "CanBeStored", True, bool, "If True, this armor can be stored in the Bottomless Box."
        ),
        FieldDisplayInfo("headEquip:1", "EquippedToHead", True, bool, "This armor is equipped to the head."),
        FieldDisplayInfo("bodyEquip:1", "EquippedToBody", True, bool, "This armor is equipped to the body."),
        FieldDisplayInfo("armEquip:1", "EquippedToHands", True, bool, "This armor is equipped to the hands."),
        FieldDisplayInfo("legEquip:1", "EquippedToLegs", True, bool, "This armor is equipped to the legs."),
        FieldDisplayInfo(
            "useFaceScale:1",
            "UseFaceScale",
            False,
            bool,
            "If True, the face-scaling parameters of this armor will be applied.",
        ),
        FieldDisplayInfo("invisibleFlag00:1", "HideFlag0", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo(
            "invisibleFlag01:1", "HideFlag1", False, bool, "Hide part of the character model: (hair fringe)"),
        FieldDisplayInfo(
            "invisibleFlag02:1", "HideFlag2", False, bool, "Hide part of the character model: (sideburns)"),
        FieldDisplayInfo(
            "invisibleFlag03:1", "HideFlag3", False, bool, "Hide part of the character model: (top of head)"),
        FieldDisplayInfo(
            "invisibleFlag04:1", "HideFlag4", False, bool, "Hide part of the character model: (top of head)"),
        FieldDisplayInfo(
            "invisibleFlag05:1", "HideFlag5", False, bool, "Hide part of the character model: (back hair)"),
        FieldDisplayInfo(
            "invisibleFlag06:1", "HideFlag6", False, bool, "Hide part of the character model: (back hair tip)"
        ),
        FieldDisplayInfo("invisibleFlag07:1", "HideFlag7", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag08:1", "HideFlag8", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag09:1", "HideFlag9", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag10:1", "HideFlag10", False, bool, "Hide part of the character model: (collar)"),
        FieldDisplayInfo(
            "invisibleFlag11:1", "HideFlag11", False, bool, "Hide part of the character model: (around collar)"
        ),
        FieldDisplayInfo("invisibleFlag12:1", "HideFlag12", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag13:1", "HideFlag13", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag14:1", "HideFlag14", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag15:1", "HideFlag15", False, bool, "Hide part of the character model: (hood hem)"),
        FieldDisplayInfo("invisibleFlag16:1", "HideFlag16", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag17:1", "HideFlag17", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag18:1", "HideFlag18", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag19:1", "HideFlag19", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag20:1", "HideFlag20", False, bool, "Hide part of the character model: (sleeve A)"),
        FieldDisplayInfo("invisibleFlag21:1", "HideFlag21", False, bool, "Hide part of the character model: (sleeve B)"),
        FieldDisplayInfo("invisibleFlag22:1", "HideFlag22", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag23:1", "HideFlag23", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag24:1", "HideFlag24", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag25:1", "HideFlag25", False, bool, "Hide part of the character model: (arm)"),
        FieldDisplayInfo("invisibleFlag26:1", "HideFlag26", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag27:1", "HideFlag27", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag28:1", "HideFlag28", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag29:1", "HideFlag29", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag30:1", "HideFlag30", False, bool, "Hide part of the character model: (belt)"),
        FieldDisplayInfo("invisibleFlag31:1", "HideFlag31", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag32:1", "HideFlag32", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag33:1", "HideFlag33", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag34:1", "HideFlag34", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag35:1", "HideFlag35", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag36:1", "HideFlag36", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag37:1", "HideFlag37", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag38:1", "HideFlag38", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag39:1", "HideFlag39", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag40:1", "HideFlag40", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag41:1", "HideFlag41", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag42:1", "HideFlag42", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag43:1", "HideFlag43", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag44:1", "HideFlag44", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag45:1", "HideFlag45", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag46:1", "HideFlag46", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo("invisibleFlag47:1", "HideFlag47", False, bool, "Hide part of the character model: (unknown)"),
        FieldDisplayInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        FieldDisplayInfo("simpleModelForDlc:1", "SimpleDLCModelExists", False, bool, "Unknown; always set to False."),
        FieldDisplayInfo("pad_0[1]", "Pad0", False, pad_field(1), "Null padding."),
        FieldDisplayInfo(
            "oldSortId", "OldSortIndex", False, int, "Sorting index for an obsolete build of the game. No effect."
        ),
        FieldDisplayInfo("pad_1[6]", "Pad1", False, pad_field(6), "Null padding."),
    ],
}


REINFORCE_PARAM_PROTECTOR_ST = {
    "paramdef_name": "REINFORCE_PARAM_PROTECTOR_ST",
    "file_name": "ReinforceParamProtector",
    "nickname": "ArmorUpgrades",
    "fields": [
        FieldDisplayInfo(
            "physicsDefRate",
            "PhysicalDefenseMultiplier",
            True,
            float,
            "Multiplier for physical defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "magicDefRate",
            "MagicDefenseMultiplier",
            True,
            float,
            "Multiplier for magic defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "fireDefRate",
            "FireDefenseMultiplier",
            True,
            float,
            "Multiplier for fire defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "thunderDefRate",
            "LightningDefenseMultiplier",
            True,
            float,
            "Multiplier for lightning defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "slashDefRate",
            "SlashDefenseMultiplier",
            True,
            float,
            "Multiplier for slash defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "blowDefRate",
            "StrikeDefenseMultiplier",
            True,
            float,
            "Multiplier for strike defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "thrustDefRate",
            "ThrustDefenseMultiplier",
            True,
            float,
            "Multiplier for thrust defense at this upgrade level.",
        ),
        FieldDisplayInfo(
            "resistPoisonRate",
            "PoisonResistanceMultiplier",
            True,
            float,
            "Multiplier for poison resistance at this upgrade level.",
        ),
        FieldDisplayInfo(
            "resistDiseaseRate",
            "ToxicResistanceMultiplier",
            True,
            float,
            "Multiplier for toxic resistance at this upgrade level.",
        ),
        FieldDisplayInfo(
            "resistBloodRate",
            "BleedResistanceMultiplier",
            True,
            float,
            "Multiplier for bleed resistance at this upgrade level.",
        ),
        FieldDisplayInfo(
            "resistCurseRate",
            "CurseResistanceMultiplier",
            True,
            float,
            "Multiplier for curse resistance at this upgrade level.",
        ),
        FieldDisplayInfo(
            "residentSpEffectId1",
            "WearerSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (first of three).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId2",
            "WearerSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (second of three).",
        ),
        FieldDisplayInfo(
            "residentSpEffectId3",
            "WearerSpecialEffect3",
            True,
            SpecialEffectParam,
            "Special effect granted to wearer (third of three).",
        ),
        FieldDisplayInfo(
            "materialSetId",
            "UpgradeMaterialID",
            True,
            UpgradeMaterialParam,
            "Upgrade material set for reinforcement.",
        ),
    ],
}

EQUIP_PARAM_ACCESSORY_ST = {
    "paramdef_name": "EQUIP_PARAM_ACCESSORY_ST",
    "file_name": "EquipParamAccessory",
    "nickname": "Rings",
    "fields": [
        FieldDisplayInfo(
            "refId", "SpecialEffect", True, SpecialEffectParam, "Special effect applied when ring is equipped."
        ),
        FieldDisplayInfo(
            "sfxVariationId",
            "SFXVariation",
            False,
            int,
            "SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
            "with unused Behavior parameter below.",
        ),
        FieldDisplayInfo(
            "weight",
            "Weight",
            False,
            float,
            "Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other equipment.",
        ),
        FieldDisplayInfo(
            "behaviorId",
            "Behavior",
            False,
            BehaviorParam,
            "Behavior of ring 'skill'. Always zero in the vanilla game.",
        ),
        FieldDisplayInfo("basicPrice", "BasicCost", False, int, "Unknown purpose, and unused."),
        FieldDisplayInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        FieldDisplayInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        FieldDisplayInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        FieldDisplayInfo(
            "equipModelId", "EquipmentModel", False, int, "Always zero. (Rings have no model, presumably.)"
        ),
        FieldDisplayInfo("iconId", "MenuIcon", True, Texture, "Icon ID of ring in menu."),
        FieldDisplayInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
            "level).",
        ),
        FieldDisplayInfo(
            "trophySGradeId",
            "AchievementContributionID",
            False,
            int,
            "Index of ring as it contributes to certain multi-item achievements (none for rings).",
        ),
        FieldDisplayInfo(
            "trophySeqId",
            "AchievementUnlockID",
            False,
            int,
            "Achievement unlocked when ring is acquired (Covenant of Artorias).",
        ),
        FieldDisplayInfo("equipModelCategory", "EquipmentModelCategory", False, EQUIP_MODEL_CATEGORY, "Always zero."),
        FieldDisplayInfo("equipModelGender", "EquipmentModelGender", False, EQUIP_MODEL_GENDER, "Always zero."),
        FieldDisplayInfo("accessoryCategory", "AccessoryCategory", False, ACCESSORY_CATEGORY, "Always zero."),
        FieldDisplayInfo(
            "refCategory",
            "ReferenceType",
            False,
            BEHAVIOR_REF_TYPE,
            "Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
        ),
        FieldDisplayInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            False,
            SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this equipment. Unused for rings.",
        ),
        FieldDisplayInfo("pad[1]", "Pad1", False, pad_field(1), "Null padding."),
        FieldDisplayInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"
        ),
        FieldDisplayInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "isDeposit:1",
            "CanBeStored",
            False,
            bool,
            "If True, this ring can be stored in the Bottomless Box. Always True for rings.",
        ),
        FieldDisplayInfo(
            "isEquipOutBrake:1",
            "BreaksWhenUnequipped",
            True,
            bool,
            "If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
        ),
        FieldDisplayInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        FieldDisplayInfo("pad1[3]", "Pad2", False, pad_field(3), "Null padding."),
    ],
}

EQUIP_PARAM_GOODS_ST = {
    "paramdef_name": "EQUIP_PARAM_GOODS_ST",
    "file_name": "EquipParamGoods",
    "nickname": "Goods",
    "fields": [
        DynamicGoodRef("refId", "refCategory"),
        FieldDisplayInfo(
            "sfxVariationId",
            "AnimationVariationID",
            True,
            int,
            "Animation variation ID to combine with the base usage animation.",
        ),
        FieldDisplayInfo("weight", "Weight", False, float, "Weight of good. Never used in vanilla Dark Souls."),
        FieldDisplayInfo("basicPrice", "BasicCost", False, int, "Unsure. Does not appear to be used."),
        FieldDisplayInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        FieldDisplayInfo("behaviorId", "Behavior", False, BehaviorParam, "Behavior triggered by good use. Never used."),
        FieldDisplayInfo(
            "replaceItemId",
            "GoodToReplace",
            True,
            GoodParam,
            "Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange.",
        ),
        FieldDisplayInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        FieldDisplayInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        FieldDisplayInfo(
            "yesNoDialogMessageId",
            "ConfirmationMessage",
            True,
            EventText,
            "Message displayed in yes/no dialog box to confirm use of good.",
        ),
        FieldDisplayInfo(
            "magicId",
            "Spell",
            True,
            SpellParam,
            "Spell unlocked in attunement menu by possession of this good. (Usually matches the good ID.)",
        ),
        FieldDisplayInfo("iconId", "GoodIcon", True, Texture, "Good icon texture ID."),
        FieldDisplayInfo("modelId", "ModelID", False, int, "Model of good. Never used."),
        FieldDisplayInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
        ),
        FieldDisplayInfo(
            "compTrophySedId",
            "CollectionAchievementID",
            False,
            int,
            "Collection achievement (e.g. all spells) to which obtaining this good contributes.",
        ),
        FieldDisplayInfo(
            "trophySeqId",
            "AchievementID",
            False,
            int,
            "Achievement unlocked when this good is first obtained (e.g. Estus Flask).",
        ),
        FieldDisplayInfo("maxNum", "MaxHoldQuantity", True, int, "Maximum number of good that can be held at once."),
        FieldDisplayInfo("consumeHeroPoint", "HumanityCost", False, int, "Humanity cost of using good. Always zero."),
        FieldDisplayInfo(
            "overDexterity",
            "OverDexterity",
            False,
            int,
            "'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise.",
        ),
        FieldDisplayInfo(
            "goodsType",
            "GoodType",
            True,
            GOODS_TYPE,
            "Determines if this is a basic good, upgrade material, key item, or spell.",
        ),
        FieldDisplayInfo(
            "refCategory",
            "ReferenceType",
            True,
            BEHAVIOR_REF_TYPE,
            "Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)",
        ),
        FieldDisplayInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            True,
            BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
            "for thrown goods and 'No Category' otherwise.",
        ),
        FieldDisplayInfo("goodsCategory", "GoodCategory", False, GOODS_CATEGORY, "Never used. Only one value (0) used."),
        FieldDisplayInfo(
            "goodsUseAnim",
            "UseAnimation",
            True,
            GOODS_USE_ANIM,
            "Points to basic animation used when good is used. Visual/sound effects are set by the variation ID.",
        ),
        FieldDisplayInfo(
            "opmeMenuType",
            "MenuActivated",
            True,
            GOODS_OPEN_MENU,
            "Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be "
            "useful.",
        ),
        FieldDisplayInfo(
            "useLimitCategory",
            "LimitCategory",
            True,
            SP_EFFECT_USELIMIT_CATEGORY,
            "Only one good-triggered special effect with this category can be active at once. Additional attempts "
            "to use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)",
        ),
        FieldDisplayInfo(
            "replaceCategory",
            "ReplaceCategory",
            False,
            REPLACE_CATEGORY,
            "The special effect triggered by this good will replace any special effects in the same category as "
            "this one. Used only by Dragon Stones.",
        ),
        FieldDisplayInfo(
            "vowType0:1",
            "UseableByNoCovenant",
            True,
            bool,
            "Determines if this good can be used by characters with no covenant.",
        ),
        FieldDisplayInfo(
            "vowType1:1",
            "UseableByWayOfWhite",
            True,
            bool,
            "Determines if this good can be used by characters in the Way of White.",
        ),
        FieldDisplayInfo(
            "vowType2:1",
            "UseableByPrincessGuard",
            True,
            bool,
            "Determines if this good can be used by characters in the Princess's Guard.",
        ),
        FieldDisplayInfo(
            "vowType3:1",
            "UseableByWarriorsOfSunlight",
            True,
            bool,
            "Determines if this good can be used by characters in the Warriors of Sunlight.",
        ),
        FieldDisplayInfo(
            "vowType4:1",
            "UseableByDarkwraith",
            True,
            bool,
            "Determines if this good can be used by characters in the Darkwraith covenant.",
        ),
        FieldDisplayInfo(
            "vowType5:1",
            "UseableByPathOfTheDragon",
            True,
            bool,
            "Determines if this good can be used by characters in the Path of the Dragon.",
        ),
        FieldDisplayInfo(
            "vowType6:1",
            "UseableByGravelordServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Gravelord Servants.",
        ),
        FieldDisplayInfo(
            "vowType7:1",
            "UseableByForestHunter",
            True,
            bool,
            "Determines if this good can be used by characters in the Forest Hunters.",
        ),
        FieldDisplayInfo(
            "vowType8:1",
            "UseableByDarkmoonBlade",
            True,
            bool,
            "Determines if this good can be used by characters in the Blades of the Darkmoon.",
        ),
        FieldDisplayInfo(
            "vowType9:1",
            "UseableByChaosServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Chaos Servant covenant.",
        ),
        FieldDisplayInfo(
            "vowType10:1",
            "UseableByCovenant10",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 10.",
        ),
        FieldDisplayInfo(
            "vowType11:1",
            "UseableByCovenant11",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 11.",
        ),
        FieldDisplayInfo(
            "vowType12:1",
            "UseableByCovenant12",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 12.",
        ),
        FieldDisplayInfo(
            "vowType13:1",
            "UseableByCovenant13",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 13.",
        ),
        FieldDisplayInfo(
            "vowType14:1",
            "UseableByCovenant14",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 14.",
        ),
        FieldDisplayInfo(
            "vowType15:1",
            "UseableByCovenant15",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 15.",
        ),
        FieldDisplayInfo(
            "enable_live:1",
            "UseableByHumans",
            True,
            bool,
            "Determines if this good can be used by characters who have revived to Human status.",
        ),
        FieldDisplayInfo(
            "enable_gray:1",
            "UseableByHollows",
            True,
            bool,
            "Determines if this good can be used by characters who are Hollow.",
        ),
        FieldDisplayInfo(
            "enable_white:1",
            "UseableByWhitePhantoms",
            True,
            bool,
            "Determines if this good can be used by White Phantoms (summons).",
        ),
        FieldDisplayInfo(
            "enable_black:1",
            "UseableByBlackPhantoms",
            True,
            bool,
            "Determines if this good can be used by Black Phantoms (invaders).",
        ),
        FieldDisplayInfo(
            "enable_multi:1",
            "UseableInMultiplayer",
            True,
            bool,
            "Determines if this good can be used while multiple players are together.",
            dsr_only=True,
        ),
        FieldDisplayInfo(
            "enable_pvp:1",
            "UseableInPVP",
            True,
            bool,
            "<DSR> Determines if this good can be used in 'PVP' multiplayer. Not sure exactly what that refers to.",
        ),
        FieldDisplayInfo(
            "disable_offline:1",
            "DisabledOffline",
            True,
            bool,
            "Determines if this good can be used while the game is disconnected from the network.",
        ),
        FieldDisplayInfo(
            "isEquip:1",
            "CanBeEquipped",
            True,
            bool,
            "Determines if this good can be equipped in a quick item slot.",
        ),
        FieldDisplayInfo(
            "isConsume:1",
            "ConsumedOnUse",
            True,
            bool,
            "Determines if this good is consumed (count decreases) when used.",
        ),
        FieldDisplayInfo(
            "isAutoEquip:1",
            "AutomaticallyEquipped",
            True,
            bool,
            "Determines if this good will be equipped in an available quick slot when obtained.",
        ),
        FieldDisplayInfo("isEstablishment:1", "IsStationary", True, bool, "Unknown; need to look at usage."),
        FieldDisplayInfo("isOnlyOne:1", "IsUnique", True, bool, "Determines if only one of this good exists in the game."),
        FieldDisplayInfo("isDrop:1", "CanBeDropped", True, bool, "Determines if this item can be dropped."),
        FieldDisplayInfo("isDeposit:1", "CanBeStored", True, bool, "Determines if good can be stored in Bottomless Box."),
        FieldDisplayInfo(
            "isDisableHand:1", "IsDisableHand?", True, bool, "Not sure. Could disable model hand when good is used?"
        ),
        FieldDisplayInfo(
            "IsTravelItem:1", "IsTravelItem?", True, bool, "Not sure. Could flag items that warp the player."
        ),
        FieldDisplayInfo(
            "isSuppleItem:1", "IsEmptyEstusFlask?", True, bool, "Not sure. Only enabled for empty Estus Flask."
        ),
        FieldDisplayInfo(
            "isFullSuppleItem:1",
            "IsNonEmptyEstusFlask?",
            True,
            bool,
            "Not sure. Only enabled for non-empty Estus Flask.",
        ),
        FieldDisplayInfo("isEnhance:1", "IsUpgradeMaterial", True, bool, "Determines if this is an upgrade material."),
        FieldDisplayInfo("isFixItem:1", "IsFixItem?", True, bool, "Probably True for Repair Powder, etc."),
        FieldDisplayInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            True,
            bool,
            "If True, this good cannot be given to other players by dropping it.",
        ),
        FieldDisplayInfo(
            "disableUseAtColiseum:1",
            "DisabledInArena",
            False,
            bool,
            "If True, this good cannot be used in the PvP Arena in Oolacile.",
        ),
        FieldDisplayInfo(
            "disableUseAtOutOfColiseum:1",
            "DisabledOutsideArena",
            False,
            bool,
            "If True, this good cannot be used outside the PvP Arena in Oolacile.",
        ),
        FieldDisplayInfo("pad[9]", "Pad1", False, pad_field(9), "Null padding."),
        FieldDisplayInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"
        ),
        FieldDisplayInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"),
    ],
}

ITEMLOT_PARAM_ST = {
    "paramdef_name": "ITEMLOT_PARAM_ST",
    "file_name": "ItemLotParam",
    "nickname": "ItemLots",
    "fields": [
        FieldDisplayInfo(
            "getItemFlagId", "ItemFlag", True, Flag, "Flag enabled when any item from this item lot is picked up."
        ),
        FieldDisplayInfo(
            "cumulateNumFlagId",
            "FirstCumulativeFlag",
            True,
            Flag,
            "First of eight consecutive flags used to store the cumulative points for this item lot.",
        ),
        FieldDisplayInfo(
            "cumulateNumMax",
            "MaxCumulativeAdditions",
            True,
            int,
            "Maximum number of times that cumulative points will be added to the total. I suspect that the "
            "cumulative slot may be awarded automatically after this; if not, I don't know how the Symbol of "
            "Avarice always drops after all seven Mimics are killed.",
        ),
        FieldDisplayInfo(
            "lotItem_Rarity",
            "ItemLotRarity",
            True,
            int,
            "Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set "
            "to 2 for all character drops except Crystal Lizards, who have 3.",
        ),
        FieldDisplayInfo("lotItemCategory01", "Item1Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 1)."),
        DynamicItemLotRef("lotItemId01", "lotItemCategory01"),
        FieldDisplayInfo("lotItemNum01", "Item1Count", True, int, "Count of item (slot 1)."),
        FieldDisplayInfo(
            "lotItemBasePoint01",
            "Item1ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId01",
            "Item1Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck01:1",
            "Item1LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint01",
            "Item1CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset01:1",
            "Item1ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory02", "Item2Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 2)."),
        DynamicItemLotRef("lotItemId02", "lotItemCategory02"),
        FieldDisplayInfo("lotItemNum02", "Item2Count", True, int, "Count of item (slot 2)."),
        FieldDisplayInfo(
            "lotItemBasePoint02",
            "Item2ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId02",
            "Item2Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck02:1",
            "Item2LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint02",
            "Item2CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset02:1",
            "Item2ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory03", "Item3Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 3)."),
        DynamicItemLotRef("lotItemId03", "lotItemCategory03"),
        FieldDisplayInfo("lotItemNum03", "Item3Count", True, int, "Count of item (slot 3)."),
        FieldDisplayInfo(
            "lotItemBasePoint03",
            "Item3ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId03",
            "Item3Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck03:1",
            "Item3LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint03",
            "Item3CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset03:1",
            "Item3ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory04", "Item4Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 4)."),
        DynamicItemLotRef("lotItemId04", "lotItemCategory04"),
        FieldDisplayInfo("lotItemNum04", "Item4Count", True, int, "Count of item (slot 4)."),
        FieldDisplayInfo(
            "lotItemBasePoint04",
            "Item4ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId04",
            "Item4Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck04:1",
            "Item4LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint04",
            "Item4CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset04:1",
            "Item4ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory05", "Item5Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 5)."),
        DynamicItemLotRef("lotItemId05", "lotItemCategory05"),
        FieldDisplayInfo("lotItemNum05", "Item5Count", True, int, "Count of item (slot 5)."),
        FieldDisplayInfo(
            "lotItemBasePoint05",
            "Item5ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId05",
            "Item5Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck05:1",
            "Item5LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint05",
            "Item5CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset05:1",
            "Item5ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory06", "Item6Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 6)."),
        DynamicItemLotRef("lotItemId06", "lotItemCategory06"),
        FieldDisplayInfo("lotItemNum06", "Item6Count", True, int, "Count of item (slot 6)."),
        FieldDisplayInfo(
            "lotItemBasePoint06",
            "Item6ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId06",
            "Item6Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck06:1",
            "Item6LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint06",
            "Item6CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset06:1",
            "Item6ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory07", "Item7Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 7)."),
        DynamicItemLotRef("lotItemId07", "lotItemCategory07"),
        FieldDisplayInfo("lotItemNum07", "Item7Count", True, int, "Count of item (slot 7)."),
        FieldDisplayInfo(
            "lotItemBasePoint07",
            "Item7ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId07",
            "Item7Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck07:1",
            "Item7LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint07",
            "Item7CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset07:1",
            "Item7ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
        FieldDisplayInfo("lotItemCategory08", "Item8Category", True, ITEMLOT_ITEMCATEGORY, "Type of item (slot 8)."),
        DynamicItemLotRef("lotItemId08", "lotItemCategory08"),
        FieldDisplayInfo("lotItemNum08", "Item8Count", True, int, "Count of item (slot 8)."),
        FieldDisplayInfo(
            "lotItemBasePoint08",
            "Item8ChancePoints",
            True,
            int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be "
            "dropped.",
        ),
        FieldDisplayInfo(
            "getItemFlagId08",
            "Item8Flag",
            False,
            Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never "
            "used.",
        ),
        FieldDisplayInfo(
            "enableLuck08:1",
            "Item8LuckEnabled",
            True,
            bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the "
            "empty item slot so that rarer items have a relatively better chance of dropping.",
        ),
        FieldDisplayInfo(
            "cumulateLotPoint08",
            "Item8CumulativePoints",
            True,
            int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is "
            "rolled. This ",
        ),
        FieldDisplayInfo(
            "cumulateReset08:1",
            "Item8ResetCumulativePointsOnDrop",
            True,
            bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped.",
        ),
    ],
}


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
        FieldDisplayInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, "DOC-TODO"),
        FieldDisplayInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"
        ),
        FieldDisplayInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, "DOC-TODO"),
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
            "KnightHonorIndex",
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
        FieldDisplayInfo(
            "levelSyncCorrectID",
            "LevelSyncCorrection",
            False,
            int,
            "Level sync correction (DSR only). Probably not useful.",
        ),
        FieldDisplayInfo("pad_1[6]", "Pad3", False, pad_field(6), "Null padding."),
    ],
}


EQUIP_MTRL_SET_PARAM_ST = {
    "paramdef_name": "EQUIP_MTRL_SET_PARAM_ST",
    "file_name": "EquipMtrlSetParam",
    "nickname": "UpgradeMaterials",
    "fields": [
        FieldDisplayInfo("materialId01", "UpgradeGood", True, GoodParam, "Good required to upgrade weapon."),
        FieldDisplayInfo(
            "materialId02",
            "UpgradeGood2",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "materialId03",
            "UpgradeGood3",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "materialId04",
            "UpgradeGood4",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "materialId05",
            "UpgradeGood5",
            False,
            GoodParam,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it "
            "may still work as a requirement).", 
        ),
        FieldDisplayInfo("itemNum01", "UpgradeQuantity", True, int, "Amount of Upgrade Good required for reinforcement."),
        FieldDisplayInfo(
            "itemNum02",
            "UpgradeQuantity2",
            False,
            int,
            "Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "itemNum03",
            "UpgradeQuantity3",
            False,
            int,
            "Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "itemNum04",
            "UpgradeQuantity4",
            False,
            int,
            "Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "itemNum05",
            "UpgradeQuantity5",
            False,
            int,
            "Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it ("
            "though it may still work as a requirement).", 
        ),
        FieldDisplayInfo(
            "isDisableDispNum01:1",
            "DisableQuantityIndicator",
            True,
            bool,
            "If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is "
            "needed.", 
        ),
        FieldDisplayInfo(
            "isDisableDispNum02:1",
            "DisableQuantityIndicator2",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        FieldDisplayInfo(
            "isDisableDispNum03:1",
            "DisableQuantityIndicator3",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        FieldDisplayInfo(
            "isDisableDispNum04:1",
            "DisableQuantityIndicator4",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        FieldDisplayInfo(
            "isDisableDispNum05:1",
            "DisableQuantityIndicator5",
            False,
            bool,
            "If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used).", 
        ),
        FieldDisplayInfo("pad[6]", "Pad1", False, pad_field(6), "Null padding."),
    ],
}


REINFORCE_PARAM_WEAPON_ST = {
    "paramdef_name": "REINFORCE_PARAM_WEAPON_ST",
    "file_name": "ReinforceParamWeapon",
    "nickname": "WeaponUpgrades",
    "fields": [
        FieldDisplayInfo(
            "physicsAtkRate",
            "PhysicalDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing physical damage (of any type).",
        ),
        FieldDisplayInfo(
            "magicAtkRate", "MagicDamageMultiplier", True, float, "Multiplier applied to outgoing magic damage."
        ),
        FieldDisplayInfo(
            "fireAtkRate", "FireDamageMultiplier", True, float, "Multiplier applied to outgoing fire damage."
        ),
        FieldDisplayInfo(
            "thunderAtkRate",
            "LightningDamageMultiplier",
            True,
            float,
            "Multiplier applied to outgoing lightning damage.",
        ),
        FieldDisplayInfo(
            "staminaAtkRate",
            "StaminaDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' stamina.",
        ),
        FieldDisplayInfo(
            "saWeaponAtkRate",
            "PoiseDamageMultiplier",
            True,
            float,
            "Multiplier applied to the amount of damage dealt to targets' poise. Never used.",
        ),
        FieldDisplayInfo(
            "saDurabilityRate",
            "PoiseDefenseMultiplier",
            True,
            float,
            "Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used.",
        ),
        FieldDisplayInfo(
            "correctStrengthRate",
            "StrengthScalingMultiplier",
            True,
            float,
            "Multiplier applied to strength scaling of this weapon.",
        ),
        FieldDisplayInfo(
            "correctAgilityRate",
            "DexterityScalingMultiplier",
            True,
            float,
            "Multiplier applied to dexterity scaling of this weapon.",
        ),
        FieldDisplayInfo(
            "correctMagicRate",
            "IntelligenceScalingMultiplier",
            True,
            float,
            "Multiplier applied to intelligence scaling of this weapon.",
        ),
        FieldDisplayInfo(
            "correctFaithRate",
            "FaithScalingMultiplier",
            True,
            float,
            "Multiplier applied to faith scaling of this weapon.",
        ),
        FieldDisplayInfo(
            "physicsGuardCutRate",
            "PhysicalGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of physical damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "magicGuardCutRate",
            "MagicGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of magic damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "fireGuardCutRate",
            "FireGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of fire damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "thunderGuardCutRate",
            "LightningGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of lightning damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "poisonGuardResistRate",
            "PoisonGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of poison damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "diseaseGuardResistRate",
            "ToxicGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of toxic damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "bloodGuardResistRate",
            "BleedGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of bleed damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "curseGuardResistRate",
            "CurseGuardResistanceMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of curse damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "staminaGuardDefRate",
            "StaminaGuardReductionMultiplier",
            True,
            float,
            "Multiplier applied to the percentage of stamina damage blocked by this weapon/shield.",
        ),
        FieldDisplayInfo(
            "spEffectId1",
            "SpecialEffectOnHit0",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters.",
        ),
        FieldDisplayInfo(
            "spEffectId2",
            "SpecialEffectOnHit1",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters.",
        ),
        FieldDisplayInfo(
            "spEffectId3",
            "SpecialEffectOnHit2",
            True,
            SpecialEffectParam,
            "Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters.",
        ),
        FieldDisplayInfo(
            "residentSpEffectId1",
            "EquippedSpecialEffect0",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
            "parameters.", 
        ),
        FieldDisplayInfo(
            "residentSpEffectId2",
            "EquippedSpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
            "parameters.", 
        ),
        FieldDisplayInfo(
            "residentSpEffectId3",
            "EquippedSpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
            "parameters.", 
        ),
        FieldDisplayInfo(
            "materialSetId",
            "UpgradeMaterialOffset",
            True,
            int,
            "Value to be added to Upgrade Materials field in base weapon parameters.",
        ),
        FieldDisplayInfo("pad[9]", "Pad1", False, pad_field(9), "Null padding."),
        FieldDisplayInfo(
            "reinforcementLevel",
            "ReinforcementLevel",
            True,
            int,
            "Reinforcement level. Not sure where this is used; it could be used to calculate the final "
            "weapon ID (e.g. 100005 for Dagger+5).",
            dsr_only=True,
        ),
    ],
}
