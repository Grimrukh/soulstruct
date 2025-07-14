from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    SortIndex: int = ParamField(
        int32, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostArmorReplacement: int = ParamField(
        uint32, "wanderingEquipId", default=0,
        tooltip="Replacement equipment for network ghosts.",
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
    RepairCost: int = ParamField(
        int32, "fixPrice", default=0,
        tooltip="Amount of souls required to repair armor fully. Actual repair cost is this multiplied by current "
                "durability over max durability.",
    )
    BasicCost: int = ParamField(
        int32, "basicPrice", default=0,
        tooltip="Unsure when this is used. Possibly sets the default if the cost is not specified in Shop parameters. "
                "Always set to 200.",
    )
    FramptSellValue: int = ParamField(
        int32, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    Weight: float = ParamField(
        float32, "weight", default=1.0,
        tooltip="Weight of armor.",
    )
    WearerSpecialEffect1: int = ParamField(
        int32, "residentSpEffectId", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (first of three).",
    )
    WearerSpecialEffect2: int = ParamField(
        int32, "residentSpEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (second of three).",
    )
    WearerSpecialEffect3: int = ParamField(
        int32, "residentSpEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (third of three).",
    )
    UpgradeMaterialID: int = ParamField(
        int32, "materialSetId", game_type=UpgradeMaterialParam, default=-1,
        tooltip="Upgrade material set for reinforcement.",
    )
    SiteDamageMultiplier: float = ParamField(
        float32, "partsDamageRate", default=1.0,
        tooltip="Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, so is "
                "never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, 1.1 for gauntlets "
                "and leggings, and 1 for torso armor.",
    )
    PoiseRecoveryTimeModifier: float = ParamField(
        float32, "corectSARecover", default=0.0,
        tooltip="Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
                "otherwise.",
    )
    UpgradeOrigin0: int = ParamField(
        int32, "originEquipPro", default=-1,
        tooltip="Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin1: int = ParamField(
        int32, "originEquipPro1", default=-1,
        tooltip="Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin2: int = ParamField(
        int32, "originEquipPro2", default=-1,
        tooltip="Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin3: int = ParamField(
        int32, "originEquipPro3", default=-1,
        tooltip="Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin4: int = ParamField(
        int32, "originEquipPro4", default=-1,
        tooltip="Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin5: int = ParamField(
        int32, "originEquipPro5", default=-1,
        tooltip="Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin6: int = ParamField(
        int32, "originEquipPro6", default=-1,
        tooltip="Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin7: int = ParamField(
        int32, "originEquipPro7", default=-1,
        tooltip="Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin8: int = ParamField(
        int32, "originEquipPro8", default=-1,
        tooltip="Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin9: int = ParamField(
        int32, "originEquipPro9", default=-1,
        tooltip="Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin10: int = ParamField(
        int32, "originEquipPro10", default=-1,
        tooltip="Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin11: int = ParamField(
        int32, "originEquipPro11", default=-1,
        tooltip="Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin12: int = ParamField(
        int32, "originEquipPro12", default=-1,
        tooltip="Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin13: int = ParamField(
        int32, "originEquipPro13", default=-1,
        tooltip="Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin14: int = ParamField(
        int32, "originEquipPro14", default=-1,
        tooltip="Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin15: int = ParamField(
        int32, "originEquipPro15", default=-1,
        tooltip="Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    MaleFaceScaleX: float = ParamField(
        float32, "faceScaleM_ScaleX", default=1.0,
        tooltip="Scale factor applied to X dimension of male faces when worn.",
    )
    MaleFaceScaleZ: float = ParamField(
        float32, "faceScaleM_ScaleZ", default=1.0,
        tooltip="Scale factor applied to Z dimension of male faces when worn.",
    )
    MaleFaceMaxScaleX: float = ParamField(
        float32, "faceScaleM_MaxX", default=1.0,
        tooltip="Maximum scale permitted for X dimension of male faces when worn.",
    )
    MaleFaceMaxScaleZ: float = ParamField(
        float32, "faceScaleM_MaxZ", default=1.0,
        tooltip="Maximum scale permitted for Z dimension of male faces when worn.",
    )
    FemaleFaceScaleX: float = ParamField(
        float32, "faceScaleF_ScaleX", default=1.0,
        tooltip="Scale factor applied to X dimension of female faces when worn.",
    )
    FemaleFaceScaleZ: float = ParamField(
        float32, "faceScaleF_ScaleZ", default=1.0,
        tooltip="Scale factor applied to Z dimension of female faces when worn.",
    )
    FemaleFaceMaxScaleX: float = ParamField(
        float32, "faceScaleF_MaxX", default=1.0,
        tooltip="Maximum scale permitted for X dimension of female faces when worn.",
    )
    FemaleFaceMaxScaleZ: float = ParamField(
        float32, "faceScaleF_MaxZ", default=1.0,
        tooltip="Maximum scale permitted for Z dimension of female faces when worn.",
    )
    QWCID: int = ParamField(
        int32, "qwcId", default=-1,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        uint16, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Model ID of armor.",
    )
    MaleIcon: int = ParamField(
        uint16, "iconIdM", game_type=Icon, default=0,
        tooltip="Icon of male variant of armor in inventory.",
    )
    FemaleIcon: int = ParamField(
        uint16, "iconIdF", game_type=Icon, default=0,
        tooltip="Icon of female variant of armor in inventory.",
    )
    KnockbackPercentageReduction: int = ParamField(
        uint16, "knockBack", default=0,
        tooltip="Never used. Probably the percentage of knockback reduced (from 0 to 100) when wearing armor.",
    )
    KnockbackBouncePercentage: int = ParamField(
        uint16, "knockbackBounceRate", default=0,
        tooltip="Never used. Possibly affects knockback of incoming attacks.",
    )
    InitialDurability: int = ParamField(
        uint16, "durability", default=100,
        tooltip="Durability of armor when it is obtained. Always equal to max durability in vanilla game.",
    )
    MaxDurability: int = ParamField(
        uint16, "durabilityMax", default=100,
        tooltip="Maximum durability of armor.",
    )
    Poise: int = ParamField(
        int16, "saDurability", default=0,
        tooltip="Amount of poise added when wearing armor.",
    )
    RepelDefense: int = ParamField(
        uint16, "defFlickPower", default=0,
        tooltip="Determines when incoming attacks will bounce off.",
    )
    PhysicalDefense: int = ParamField(
        uint16, "defensePhysics", default=100,
        tooltip="Added defense against physical attack damage.",
    )
    MagicDefense: int = ParamField(
        uint16, "defenseMagic", default=100,
        tooltip="Added defense against magic attack damage.",
    )
    FireDefense: int = ParamField(
        uint16, "defenseFire", default=100,
        tooltip="Added defense against fire attack damage.",
    )
    LightningDefense: int = ParamField(
        uint16, "defenseThunder", default=100,
        tooltip="Added defense against lightning attack damage.",
    )
    SlashDefense: int = ParamField(
        int16, "defenseSlash", default=0,
        tooltip="Added defense against physical slash attack damage.",
    )
    StrikeDefense: int = ParamField(
        int16, "defenseBlow", default=0,
        tooltip="Added defense against physical strike attack damage.",
    )
    ThrustDefense: int = ParamField(
        int16, "defenseThrust", default=0,
        tooltip="Added defense against physical thrust attack damage.",
    )
    PoisonResistance: int = ParamField(
        uint16, "resistPoison", default=100,
        tooltip="Poison resistance added by armor.",
    )
    ToxicResistance: int = ParamField(
        uint16, "resistDisease", default=100,
        tooltip="Toxic resistance added by armor.",
    )
    BleedResistance: int = ParamField(
        uint16, "resistBlood", default=100,
        tooltip="Bleed resistance added by armor.",
    )
    CurseResistance: int = ParamField(
        uint16, "resistCurse", default=100,
        tooltip="Curse resistance added by armor.",
    )
    ArmorUpgradeID: int = ParamField(
        int16, "reinforceTypeId", game_type=ArmorUpgradeParam, default=0,
        tooltip="Effects applied at consecutive upgrade reinforcement levels.",
    )
    AchievementContributionID: int = ParamField(
        int16, "compTrophySedId", default=-1,
        tooltip="Index of armor as it contributes to certain multi-item achievements.",
    )
    ShopLevel: int = ParamField(
        int16, "shopLv", default=0,
        tooltip="Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
    )
    KnockbackID: int = ParamField(
        uint8, "knockbackParamId", game_type=KnockbackParam, default=0,
        tooltip="Knockback entry. Always 1.",
    )
    RepelDamagePercentageReduction: int = ParamField(
        uint8, "flickDamageCutRate", default=0,
        tooltip="Determines some aspect of attack deflection. Always set to 0 (for light armor) or 255 (for heavy "
                "armor).",
    )
    EquipmentModelCategory: int = ParamField(
        uint8, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=1,
        tooltip="Body part covered by armor model.",
    )
    EquipmentModelGender: int = ParamField(
        uint8, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Gender variant of armor.",
    )
    ArmorType: int = ParamField(
        uint8, "protectorCategory", PROTECTOR_CATEGORY, default=0,
        tooltip="Type of armor (equip slot).",
    )
    SoundEffectOnHit: int = ParamField(
        uint8, "defenseMaterial", WEP_MATERIAL_DEF, default=50,
        tooltip="Type of sound effect generated when this armor is hit.",
    )
    VisualEffectOnHit: int = ParamField(
        uint8, "defenseMaterialSfx", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="Type of visual effect generated when this armor is hit.",
    )
    PartsDamageType: int = ParamField(
        uint8, "partsDmgType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Always zero.",
    )
    SoundEffectOnWeakSpotHit: int = ParamField(
        uint8, "defenseMaterial_Weak", WEP_MATERIAL_DEF, default=50,
        tooltip="Sound effect for when damage is taken to weak spot (used for head armor).",
    )
    VisualEffectOnWeakSpotHit: int = ParamField(
        uint8, "defenseMaterialSfx_Weak", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="Visual effect for when damage is taken to weak spot (used for head armor).",
    )
    CanBeStored: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this armor can be stored in the Bottomless Box.",
    )
    EquippedToHead: bool = ParamField(
        uint8, "headEquip:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="This armor is equipped to the head.",
    )
    EquippedToBody: bool = ParamField(
        uint8, "bodyEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the body.",
    )
    EquippedToHands: bool = ParamField(
        uint8, "armEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the hands.",
    )
    EquippedToLegs: bool = ParamField(
        uint8, "legEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the legs.",
    )
    UseFaceScale: bool = ParamField(
        uint8, "useFaceScale:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the face-scaling parameters of this armor will be applied.",
    )
    HideFlag0: bool = ParamField(
        uint8, "invisibleFlag00:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag1HairFringe: bool = ParamField(
        uint8, "invisibleFlag01:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (hair fringe)",
    )
    HideFlag2Sideburns: bool = ParamField(
        uint8, "invisibleFlag02:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sideburns)",
    )
    HideFlag3TopOfHead: bool = ParamField(
        uint8, "invisibleFlag03:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (top of head)",
    )
    HideFlag4TopOfHead: bool = ParamField(
        uint8, "invisibleFlag04:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (top of head)",
    )
    HideFlag5BackHair: bool = ParamField(
        uint8, "invisibleFlag05:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (back hair)",
    )
    HideFlag6BackHairTip: bool = ParamField(
        uint8, "invisibleFlag06:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (back hair tip)",
    )
    HideFlag7: bool = ParamField(
        uint8, "invisibleFlag07:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag8: bool = ParamField(
        uint8, "invisibleFlag08:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag9: bool = ParamField(
        uint8, "invisibleFlag09:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag10Collar: bool = ParamField(
        uint8, "invisibleFlag10:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (collar)",
    )
    HideFlag11AroundCollar: bool = ParamField(
        uint8, "invisibleFlag11:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (around collar)",
    )
    HideFlag12: bool = ParamField(
        uint8, "invisibleFlag12:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag13: bool = ParamField(
        uint8, "invisibleFlag13:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag14: bool = ParamField(
        uint8, "invisibleFlag14:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag15HoodHem: bool = ParamField(
        uint8, "invisibleFlag15:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (hood hem)",
    )
    HideFlag16: bool = ParamField(
        uint8, "invisibleFlag16:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag17: bool = ParamField(
        uint8, "invisibleFlag17:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag18: bool = ParamField(
        uint8, "invisibleFlag18:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag19: bool = ParamField(
        uint8, "invisibleFlag19:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag20SleeveA: bool = ParamField(
        uint8, "invisibleFlag20:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sleeve A)",
    )
    HideFlag21SleeveB: bool = ParamField(
        uint8, "invisibleFlag21:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sleeve B)",
    )
    HideFlag22: bool = ParamField(
        uint8, "invisibleFlag22:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag23: bool = ParamField(
        uint8, "invisibleFlag23:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag24: bool = ParamField(
        uint8, "invisibleFlag24:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag25Arm: bool = ParamField(
        uint8, "invisibleFlag25:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (arm)",
    )
    HideFlag26: bool = ParamField(
        uint8, "invisibleFlag26:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag27: bool = ParamField(
        uint8, "invisibleFlag27:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag28: bool = ParamField(
        uint8, "invisibleFlag28:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag29: bool = ParamField(
        uint8, "invisibleFlag29:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag30Belt: bool = ParamField(
        uint8, "invisibleFlag30:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (belt)",
    )
    HideFlag31: bool = ParamField(
        uint8, "invisibleFlag31:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag32: bool = ParamField(
        uint8, "invisibleFlag32:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag33: bool = ParamField(
        uint8, "invisibleFlag33:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag34: bool = ParamField(
        uint8, "invisibleFlag34:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag35: bool = ParamField(
        uint8, "invisibleFlag35:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag36: bool = ParamField(
        uint8, "invisibleFlag36:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag37: bool = ParamField(
        uint8, "invisibleFlag37:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag38: bool = ParamField(
        uint8, "invisibleFlag38:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag39: bool = ParamField(
        uint8, "invisibleFlag39:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag40: bool = ParamField(
        uint8, "invisibleFlag40:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag41: bool = ParamField(
        uint8, "invisibleFlag41:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag42: bool = ParamField(
        uint8, "invisibleFlag42:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag43: bool = ParamField(
        uint8, "invisibleFlag43:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag44: bool = ParamField(
        uint8, "invisibleFlag44:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag45: bool = ParamField(
        uint8, "invisibleFlag45:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag46: bool = ParamField(
        uint8, "invisibleFlag46:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag47: bool = ParamField(
        uint8, "invisibleFlag47:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
    )
    SimpleDLCModelExists: bool = ParamField(
        uint8, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    CanDropToSummons: bool = ParamField(
        uint8, "isGuestDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    GunDamagePercentageReduction: float = ParamField(
        float32, "shotDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    SlashDamagePercentageReduction: float = ParamField(
        float32, "slashDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    BluntDamagePercentageReduction: float = ParamField(
        float32, "blowDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    ThrustDamagePercentageReduction: float = ParamField(
        float32, "thrustDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    MagicDamagePercentageReduction: float = ParamField(
        float32, "magicDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    FireDamagePercentageReduction: float = ParamField(
        float32, "fireDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    LightningDamagePercentageReduction: float = ParamField(
        float32, "thunderDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    ResistBeasts: int = ParamField(
        uint16, "resistTherianthrope", default=100,
        tooltip="TODO",
    )
    HideFlag48: bool = ParamField(
        uint8, "invisibleFlag48:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag49: bool = ParamField(
        uint8, "invisibleFlag49:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag50: bool = ParamField(
        uint8, "invisibleFlag50:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag51: bool = ParamField(
        uint8, "invisibleFlag51:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag52: bool = ParamField(
        uint8, "invisibleFlag52:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag53: bool = ParamField(
        uint8, "invisibleFlag53:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag54: bool = ParamField(
        uint8, "invisibleFlag54:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag55: bool = ParamField(
        uint8, "invisibleFlag55:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag56: bool = ParamField(
        uint8, "invisibleFlag56:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag57: bool = ParamField(
        uint8, "invisibleFlag57:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag58: bool = ParamField(
        uint8, "invisibleFlag58:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag59: bool = ParamField(
        uint8, "invisibleFlag59:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag60: bool = ParamField(
        uint8, "invisibleFlag60:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag61: bool = ParamField(
        uint8, "invisibleFlag61:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag62: bool = ParamField(
        uint8, "invisibleFlag62:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    StorageCategory: int = ParamField(
        uint8, "repositoryCategory", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    TrophyID: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad3[8]")
