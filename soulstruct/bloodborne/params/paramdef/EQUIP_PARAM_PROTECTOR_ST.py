from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostArmorReplacement: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="Replacement equipment for network ghosts.",
    )
    VagrantItemLot: int = ParamField(
        int, "vagrantItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int, "vagrantBonusEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
        int, "vagrantItemEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    RepairCost: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="Amount of souls required to repair armor fully. Actual repair cost is this multiplied by current "
                "durability over max durability.",
    )
    BasicCost: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="Unsure when this is used. Possibly sets the default if the cost is not specified in Shop parameters. "
                "Always set to 200.",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="Weight of armor.",
    )
    WearerSpecialEffect1: int = ParamField(
        int, "residentSpEffectId", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (first of three).",
    )
    WearerSpecialEffect2: int = ParamField(
        int, "residentSpEffectId2", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (second of three).",
    )
    WearerSpecialEffect3: int = ParamField(
        int, "residentSpEffectId3", game_type=SpecialEffectParam, default=0,
        tooltip="Special effect granted to wearer (third of three).",
    )
    UpgradeMaterialID: int = ParamField(
        int, "materialSetId", game_type=UpgradeMaterialParam, default=-1,
        tooltip="Upgrade material set for reinforcement.",
    )
    SiteDamageMultiplier: float = ParamField(
        float, "partsDamageRate", default=1.0,
        tooltip="Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, so is "
                "never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, 1.1 for gauntlets "
                "and leggings, and 1 for torso armor.",
    )
    PoiseRecoveryTimeModifier: float = ParamField(
        float, "corectSARecover", default=0.0,
        tooltip="Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
                "otherwise.",
    )
    UpgradeOrigin0: int = ParamField(
        int, "originEquipPro", default=-1,
        tooltip="Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin1: int = ParamField(
        int, "originEquipPro1", default=-1,
        tooltip="Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin2: int = ParamField(
        int, "originEquipPro2", default=-1,
        tooltip="Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin3: int = ParamField(
        int, "originEquipPro3", default=-1,
        tooltip="Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin4: int = ParamField(
        int, "originEquipPro4", default=-1,
        tooltip="Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin5: int = ParamField(
        int, "originEquipPro5", default=-1,
        tooltip="Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin6: int = ParamField(
        int, "originEquipPro6", default=-1,
        tooltip="Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin7: int = ParamField(
        int, "originEquipPro7", default=-1,
        tooltip="Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin8: int = ParamField(
        int, "originEquipPro8", default=-1,
        tooltip="Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin9: int = ParamField(
        int, "originEquipPro9", default=-1,
        tooltip="Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin10: int = ParamField(
        int, "originEquipPro10", default=-1,
        tooltip="Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin11: int = ParamField(
        int, "originEquipPro11", default=-1,
        tooltip="Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin12: int = ParamField(
        int, "originEquipPro12", default=-1,
        tooltip="Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin13: int = ParamField(
        int, "originEquipPro13", default=-1,
        tooltip="Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin14: int = ParamField(
        int, "originEquipPro14", default=-1,
        tooltip="Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    UpgradeOrigin15: int = ParamField(
        int, "originEquipPro15", default=-1,
        tooltip="Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
                "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu.",
    )
    MaleFaceScaleX: float = ParamField(
        float, "faceScaleM_ScaleX", default=1.0,
        tooltip="Scale factor applied to X dimension of male faces when worn.",
    )
    MaleFaceScaleZ: float = ParamField(
        float, "faceScaleM_ScaleZ", default=1.0,
        tooltip="Scale factor applied to Z dimension of male faces when worn.",
    )
    MaleFaceMaxScaleX: float = ParamField(
        float, "faceScaleM_MaxX", default=1.0,
        tooltip="Maximum scale permitted for X dimension of male faces when worn.",
    )
    MaleFaceMaxScaleZ: float = ParamField(
        float, "faceScaleM_MaxZ", default=1.0,
        tooltip="Maximum scale permitted for Z dimension of male faces when worn.",
    )
    FemaleFaceScaleX: float = ParamField(
        float, "faceScaleF_ScaleX", default=1.0,
        tooltip="Scale factor applied to X dimension of female faces when worn.",
    )
    FemaleFaceScaleZ: float = ParamField(
        float, "faceScaleF_ScaleZ", default=1.0,
        tooltip="Scale factor applied to Z dimension of female faces when worn.",
    )
    FemaleFaceMaxScaleX: float = ParamField(
        float, "faceScaleF_MaxX", default=1.0,
        tooltip="Maximum scale permitted for X dimension of female faces when worn.",
    )
    FemaleFaceMaxScaleZ: float = ParamField(
        float, "faceScaleF_MaxZ", default=1.0,
        tooltip="Maximum scale permitted for Z dimension of female faces when worn.",
    )
    QWCID: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        ushort, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Model ID of armor.",
    )
    MaleIcon: int = ParamField(
        ushort, "iconIdM", game_type=Icon, default=0,
        tooltip="Icon of male variant of armor in inventory.",
    )
    FemaleIcon: int = ParamField(
        ushort, "iconIdF", game_type=Icon, default=0,
        tooltip="Icon of female variant of armor in inventory.",
    )
    KnockbackPercentageReduction: int = ParamField(
        ushort, "knockBack", default=0,
        tooltip="Never used. Probably the percentage of knockback reduced (from 0 to 100) when wearing armor.",
    )
    KnockbackBouncePercentage: int = ParamField(
        ushort, "knockbackBounceRate", default=0,
        tooltip="Never used. Possibly affects knockback of incoming attacks.",
    )
    InitialDurability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="Durability of armor when it is obtained. Always equal to max durability in vanilla game.",
    )
    MaxDurability: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="Maximum durability of armor.",
    )
    Poise: int = ParamField(
        short, "saDurability", default=0,
        tooltip="Amount of poise added when wearing armor.",
    )
    RepelDefense: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="Determines when incoming attacks will bounce off.",
    )
    PhysicalDefense: int = ParamField(
        ushort, "defensePhysics", default=100,
        tooltip="Added defense against physical attack damage.",
    )
    MagicDefense: int = ParamField(
        ushort, "defenseMagic", default=100,
        tooltip="Added defense against magic attack damage.",
    )
    FireDefense: int = ParamField(
        ushort, "defenseFire", default=100,
        tooltip="Added defense against fire attack damage.",
    )
    LightningDefense: int = ParamField(
        ushort, "defenseThunder", default=100,
        tooltip="Added defense against lightning attack damage.",
    )
    SlashDefense: int = ParamField(
        short, "defenseSlash", default=0,
        tooltip="Added defense against physical slash attack damage.",
    )
    StrikeDefense: int = ParamField(
        short, "defenseBlow", default=0,
        tooltip="Added defense against physical strike attack damage.",
    )
    ThrustDefense: int = ParamField(
        short, "defenseThrust", default=0,
        tooltip="Added defense against physical thrust attack damage.",
    )
    PoisonResistance: int = ParamField(
        ushort, "resistPoison", default=100,
        tooltip="Poison resistance added by armor.",
    )
    ToxicResistance: int = ParamField(
        ushort, "resistDisease", default=100,
        tooltip="Toxic resistance added by armor.",
    )
    BleedResistance: int = ParamField(
        ushort, "resistBlood", default=100,
        tooltip="Bleed resistance added by armor.",
    )
    CurseResistance: int = ParamField(
        ushort, "resistCurse", default=100,
        tooltip="Curse resistance added by armor.",
    )
    ArmorUpgradeID: int = ParamField(
        short, "reinforceTypeId", game_type=ArmorUpgradeParam, default=0,
        tooltip="Effects applied at consecutive upgrade reinforcement levels.",
    )
    AchievementContributionID: int = ParamField(
        short, "compTrophySedId", default=-1,
        tooltip="Index of armor as it contributes to certain multi-item achievements.",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
    )
    KnockbackID: int = ParamField(
        byte, "knockbackParamId", game_type=KnockbackParam, default=0,
        tooltip="Knockback entry. Always 1.",
    )
    RepelDamagePercentageReduction: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="Determines some aspect of attack deflection. Always set to 0 (for light armor) or 255 (for heavy "
                "armor).",
    )
    EquipmentModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=1,
        tooltip="Body part covered by armor model.",
    )
    EquipmentModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Gender variant of armor.",
    )
    ArmorType: int = ParamField(
        byte, "protectorCategory", PROTECTOR_CATEGORY, default=0,
        tooltip="Type of armor (equip slot).",
    )
    SoundEffectOnHit: int = ParamField(
        byte, "defenseMaterial", WEP_MATERIAL_DEF, default=50,
        tooltip="Type of sound effect generated when this armor is hit.",
    )
    VisualEffectOnHit: int = ParamField(
        byte, "defenseMaterialSfx", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="Type of visual effect generated when this armor is hit.",
    )
    PartsDamageType: int = ParamField(
        byte, "partsDmgType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Always zero.",
    )
    SoundEffectOnWeakSpotHit: int = ParamField(
        byte, "defenseMaterial_Weak", WEP_MATERIAL_DEF, default=50,
        tooltip="Sound effect for when damage is taken to weak spot (used for head armor).",
    )
    VisualEffectOnWeakSpotHit: int = ParamField(
        byte, "defenseMaterialSfx_Weak", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="Visual effect for when damage is taken to weak spot (used for head armor).",
    )
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this armor can be stored in the Bottomless Box.",
    )
    EquippedToHead: bool = ParamField(
        byte, "headEquip:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="This armor is equipped to the head.",
    )
    EquippedToBody: bool = ParamField(
        byte, "bodyEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the body.",
    )
    EquippedToHands: bool = ParamField(
        byte, "armEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the hands.",
    )
    EquippedToLegs: bool = ParamField(
        byte, "legEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="This armor is equipped to the legs.",
    )
    UseFaceScale: bool = ParamField(
        byte, "useFaceScale:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, the face-scaling parameters of this armor will be applied.",
    )
    HideFlag0: bool = ParamField(
        byte, "invisibleFlag00:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag1HairFringe: bool = ParamField(
        byte, "invisibleFlag01:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (hair fringe)",
    )
    HideFlag2Sideburns: bool = ParamField(
        byte, "invisibleFlag02:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sideburns)",
    )
    HideFlag3TopOfHead: bool = ParamField(
        byte, "invisibleFlag03:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (top of head)",
    )
    HideFlag4TopOfHead: bool = ParamField(
        byte, "invisibleFlag04:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (top of head)",
    )
    HideFlag5BackHair: bool = ParamField(
        byte, "invisibleFlag05:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (back hair)",
    )
    HideFlag6BackHairTip: bool = ParamField(
        byte, "invisibleFlag06:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (back hair tip)",
    )
    HideFlag7: bool = ParamField(
        byte, "invisibleFlag07:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag8: bool = ParamField(
        byte, "invisibleFlag08:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag9: bool = ParamField(
        byte, "invisibleFlag09:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag10Collar: bool = ParamField(
        byte, "invisibleFlag10:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (collar)",
    )
    HideFlag11AroundCollar: bool = ParamField(
        byte, "invisibleFlag11:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (around collar)",
    )
    HideFlag12: bool = ParamField(
        byte, "invisibleFlag12:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag13: bool = ParamField(
        byte, "invisibleFlag13:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag14: bool = ParamField(
        byte, "invisibleFlag14:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag15HoodHem: bool = ParamField(
        byte, "invisibleFlag15:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (hood hem)",
    )
    HideFlag16: bool = ParamField(
        byte, "invisibleFlag16:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag17: bool = ParamField(
        byte, "invisibleFlag17:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag18: bool = ParamField(
        byte, "invisibleFlag18:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag19: bool = ParamField(
        byte, "invisibleFlag19:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag20SleeveA: bool = ParamField(
        byte, "invisibleFlag20:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sleeve A)",
    )
    HideFlag21SleeveB: bool = ParamField(
        byte, "invisibleFlag21:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (sleeve B)",
    )
    HideFlag22: bool = ParamField(
        byte, "invisibleFlag22:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag23: bool = ParamField(
        byte, "invisibleFlag23:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag24: bool = ParamField(
        byte, "invisibleFlag24:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag25Arm: bool = ParamField(
        byte, "invisibleFlag25:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (arm)",
    )
    HideFlag26: bool = ParamField(
        byte, "invisibleFlag26:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag27: bool = ParamField(
        byte, "invisibleFlag27:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag28: bool = ParamField(
        byte, "invisibleFlag28:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag29: bool = ParamField(
        byte, "invisibleFlag29:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag30Belt: bool = ParamField(
        byte, "invisibleFlag30:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (belt)",
    )
    HideFlag31: bool = ParamField(
        byte, "invisibleFlag31:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag32: bool = ParamField(
        byte, "invisibleFlag32:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag33: bool = ParamField(
        byte, "invisibleFlag33:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag34: bool = ParamField(
        byte, "invisibleFlag34:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag35: bool = ParamField(
        byte, "invisibleFlag35:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag36: bool = ParamField(
        byte, "invisibleFlag36:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag37: bool = ParamField(
        byte, "invisibleFlag37:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag38: bool = ParamField(
        byte, "invisibleFlag38:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag39: bool = ParamField(
        byte, "invisibleFlag39:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag40: bool = ParamField(
        byte, "invisibleFlag40:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag41: bool = ParamField(
        byte, "invisibleFlag41:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag42: bool = ParamField(
        byte, "invisibleFlag42:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag43: bool = ParamField(
        byte, "invisibleFlag43:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag44: bool = ParamField(
        byte, "invisibleFlag44:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag45: bool = ParamField(
        byte, "invisibleFlag45:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag46: bool = ParamField(
        byte, "invisibleFlag46:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag47: bool = ParamField(
        byte, "invisibleFlag47:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
    )
    SimpleDLCModelExists: bool = ParamField(
        byte, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    CanDropToSummons: bool = ParamField(
        byte, "isGuestDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    GunDamagePercentageReduction: float = ParamField(
        float, "shotDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    SlashDamagePercentageReduction: float = ParamField(
        float, "slashDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    BluntDamagePercentageReduction: float = ParamField(
        float, "blowDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    ThrustDamagePercentageReduction: float = ParamField(
        float, "thrustDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    MagicDamagePercentageReduction: float = ParamField(
        float, "magicDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    FireDamagePercentageReduction: float = ParamField(
        float, "fireDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    LightningDamagePercentageReduction: float = ParamField(
        float, "thunderDamageCutRate", default=1.0,
        tooltip="TODO",
    )
    ResistBeasts: int = ParamField(
        ushort, "resistTherianthrope", default=100,
        tooltip="TODO",
    )
    HideFlag48: bool = ParamField(
        byte, "invisibleFlag48:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag49: bool = ParamField(
        byte, "invisibleFlag49:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag50: bool = ParamField(
        byte, "invisibleFlag50:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag51: bool = ParamField(
        byte, "invisibleFlag51:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag52: bool = ParamField(
        byte, "invisibleFlag52:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag53: bool = ParamField(
        byte, "invisibleFlag53:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag54: bool = ParamField(
        byte, "invisibleFlag54:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag55: bool = ParamField(
        byte, "invisibleFlag55:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag56: bool = ParamField(
        byte, "invisibleFlag56:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag57: bool = ParamField(
        byte, "invisibleFlag57:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag58: bool = ParamField(
        byte, "invisibleFlag58:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag59: bool = ParamField(
        byte, "invisibleFlag59:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag60: bool = ParamField(
        byte, "invisibleFlag60:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag61: bool = ParamField(
        byte, "invisibleFlag61:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    HideFlag62: bool = ParamField(
        byte, "invisibleFlag62:1", bit_count=1, default=False,
        tooltip="Hide part of the character model: (unknown)",
    )
    StorageCategory: int = ParamField(
        byte, "repositoryCategory", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    TrophyID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad3[8]")
