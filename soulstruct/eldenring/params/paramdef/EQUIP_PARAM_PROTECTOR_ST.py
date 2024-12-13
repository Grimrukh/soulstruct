from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostArmorReplacement: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="Replacement equipment for network ghosts.",
    )
    ResistSleep: int = ParamField(
        ushort, "resistSleep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistMadness: int = ParamField(
        ushort, "resistMadness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Poise: float = ParamField(
        float, "saDurability", default=0.0,
        tooltip="Amount of poise added when wearing armor.",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
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
    _Pad1: bytes = ParamPad(2, "pad03[2]")
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
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
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
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageType: int = ParamField(
        byte, "partsDmgType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Always zero.",
    )
    _Pad2: bytes = ParamPad(2, "pad04[2]")
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor can be stored in storage.",
    )
    EquippedToHead: bool = ParamField(
        byte, "headEquip:1", EQUIP_BOOL, bit_count=1, default=False,
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
    IsSkipWeakDamageAnim: bool = ParamField(
        byte, "isSkipWeakDamageAnim:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad06:1", bit_count=1)
    DefenseMaterialVariationValueWeak: int = ParamField(
        byte, "defenseMaterialVariationValue_Weak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId2: int = ParamField(
        short, "autoFootEffectDecalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId3: int = ParamField(
        short, "autoFootEffectDecalBaseId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialVariationValue: int = ParamField(
        byte, "defenseMaterialVariationValue", default=0,
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
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
    )
    SimpleDLCModelExists: bool = ParamField(
        byte, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    ShowLogCondType: bool = ParamField(
        byte, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(byte, "pad:1", bit_count=1)
    NeutralDamageCutRate: float = ParamField(
        float, "neutralDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
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
    DefenseMaterialSfx1: int = ParamField(
        ushort, "defenseMaterialSfx1", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak1: int = ParamField(
        ushort, "defenseMaterialSfx_Weak1", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterial1: int = ParamField(
        ushort, "defenseMaterial1", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak1: int = ParamField(
        ushort, "defenseMaterial_Weak1", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfx2: int = ParamField(
        ushort, "defenseMaterialSfx2", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak2: int = ParamField(
        ushort, "defenseMaterialSfx_Weak2", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    FootMaterialSe: int = ParamField(
        ushort, "footMaterialSe", WEP_MATERIAL_DEF, default=139,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak2: int = ParamField(
        ushort, "defenseMaterial_Weak2", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId1: int = ParamField(
        int, "autoFootEffectDecalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessDamageCutRate: float = ParamField(
        float, "toughnessDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseDark: int = ParamField(
        ushort, "defenseDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad3: int = ParamBitPad(byte, "invisibleFlag48:1", bit_count=1)
    _BitPad4: int = ParamBitPad(byte, "invisibleFlag49:1", bit_count=1)
    _BitPad5: int = ParamBitPad(byte, "invisibleFlag50:1", bit_count=1)
    _BitPad6: int = ParamBitPad(byte, "invisibleFlag51:1", bit_count=1)
    _BitPad7: int = ParamBitPad(byte, "invisibleFlag52:1", bit_count=1)
    _BitPad8: int = ParamBitPad(byte, "invisibleFlag53:1", bit_count=1)
    _BitPad9: int = ParamBitPad(byte, "invisibleFlag54:1", bit_count=1)
    _BitPad10: int = ParamBitPad(byte, "invisibleFlag55:1", bit_count=1)
    _BitPad11: int = ParamBitPad(byte, "invisibleFlag56:1", bit_count=1)
    _BitPad12: int = ParamBitPad(byte, "invisibleFlag57:1", bit_count=1)
    _BitPad13: int = ParamBitPad(byte, "invisibleFlag58:1", bit_count=1)
    _BitPad14: int = ParamBitPad(byte, "invisibleFlag59:1", bit_count=1)
    _BitPad15: int = ParamBitPad(byte, "invisibleFlag60:1", bit_count=1)
    _BitPad16: int = ParamBitPad(byte, "invisibleFlag61:1", bit_count=1)
    _BitPad17: int = ParamBitPad(byte, "invisibleFlag62:1", bit_count=1)
    _BitPad18: int = ParamBitPad(byte, "invisibleFlag63:1", bit_count=1)
    _BitPad19: int = ParamBitPad(byte, "invisibleFlag64:1", bit_count=1)
    _BitPad20: int = ParamBitPad(byte, "invisibleFlag65:1", bit_count=1)
    _BitPad21: int = ParamBitPad(byte, "invisibleFlag66:1", bit_count=1)
    _BitPad22: int = ParamBitPad(byte, "invisibleFlag67:1", bit_count=1)
    _BitPad23: int = ParamBitPad(byte, "invisibleFlag68:1", bit_count=1)
    _BitPad24: int = ParamBitPad(byte, "invisibleFlag69:1", bit_count=1)
    _BitPad25: int = ParamBitPad(byte, "invisibleFlag70:1", bit_count=1)
    _BitPad26: int = ParamBitPad(byte, "invisibleFlag71:1", bit_count=1)
    _BitPad27: int = ParamBitPad(byte, "invisibleFlag72:1", bit_count=1)
    _BitPad28: int = ParamBitPad(byte, "invisibleFlag73:1", bit_count=1)
    _BitPad29: int = ParamBitPad(byte, "invisibleFlag74:1", bit_count=1)
    _BitPad30: int = ParamBitPad(byte, "invisibleFlag75:1", bit_count=1)
    _BitPad31: int = ParamBitPad(byte, "invisibleFlag76:1", bit_count=1)
    _BitPad32: int = ParamBitPad(byte, "invisibleFlag77:1", bit_count=1)
    _BitPad33: int = ParamBitPad(byte, "invisibleFlag78:1", bit_count=1)
    _BitPad34: int = ParamBitPad(byte, "invisibleFlag79:1", bit_count=1)
    _BitPad35: int = ParamBitPad(byte, "invisibleFlag80:1", bit_count=1)
    _BitPad36: int = ParamBitPad(byte, "padbit:7", bit_count=7)
    PostureControlId: int = ParamField(
        byte, "postureControlId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad2[4]")
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistFreeze: int = ParamField(
        ushort, "resistFreeze", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer00: int = ParamField(
        byte, "invisibleFlag_SexVer00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer01: int = ParamField(
        byte, "invisibleFlag_SexVer01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer02: int = ParamField(
        byte, "invisibleFlag_SexVer02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer03: int = ParamField(
        byte, "invisibleFlag_SexVer03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer04: int = ParamField(
        byte, "invisibleFlag_SexVer04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer05: int = ParamField(
        byte, "invisibleFlag_SexVer05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer06: int = ParamField(
        byte, "invisibleFlag_SexVer06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer07: int = ParamField(
        byte, "invisibleFlag_SexVer07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer08: int = ParamField(
        byte, "invisibleFlag_SexVer08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer09: int = ParamField(
        byte, "invisibleFlag_SexVer09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer10: int = ParamField(
        byte, "invisibleFlag_SexVer10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer11: int = ParamField(
        byte, "invisibleFlag_SexVer11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer12: int = ParamField(
        byte, "invisibleFlag_SexVer12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer13: int = ParamField(
        byte, "invisibleFlag_SexVer13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer14: int = ParamField(
        byte, "invisibleFlag_SexVer14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer15: int = ParamField(
        byte, "invisibleFlag_SexVer15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer16: int = ParamField(
        byte, "invisibleFlag_SexVer16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer17: int = ParamField(
        byte, "invisibleFlag_SexVer17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer18: int = ParamField(
        byte, "invisibleFlag_SexVer18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer19: int = ParamField(
        byte, "invisibleFlag_SexVer19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer20: int = ParamField(
        byte, "invisibleFlag_SexVer20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer21: int = ParamField(
        byte, "invisibleFlag_SexVer21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer22: int = ParamField(
        byte, "invisibleFlag_SexVer22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer23: int = ParamField(
        byte, "invisibleFlag_SexVer23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer24: int = ParamField(
        byte, "invisibleFlag_SexVer24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer25: int = ParamField(
        byte, "invisibleFlag_SexVer25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer26: int = ParamField(
        byte, "invisibleFlag_SexVer26", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer27: int = ParamField(
        byte, "invisibleFlag_SexVer27", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer28: int = ParamField(
        byte, "invisibleFlag_SexVer28", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer29: int = ParamField(
        byte, "invisibleFlag_SexVer29", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer30: int = ParamField(
        byte, "invisibleFlag_SexVer30", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer31: int = ParamField(
        byte, "invisibleFlag_SexVer31", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer32: int = ParamField(
        byte, "invisibleFlag_SexVer32", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer33: int = ParamField(
        byte, "invisibleFlag_SexVer33", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer34: int = ParamField(
        byte, "invisibleFlag_SexVer34", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer35: int = ParamField(
        byte, "invisibleFlag_SexVer35", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer36: int = ParamField(
        byte, "invisibleFlag_SexVer36", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer37: int = ParamField(
        byte, "invisibleFlag_SexVer37", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer38: int = ParamField(
        byte, "invisibleFlag_SexVer38", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer39: int = ParamField(
        byte, "invisibleFlag_SexVer39", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer40: int = ParamField(
        byte, "invisibleFlag_SexVer40", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer41: int = ParamField(
        byte, "invisibleFlag_SexVer41", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer42: int = ParamField(
        byte, "invisibleFlag_SexVer42", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer43: int = ParamField(
        byte, "invisibleFlag_SexVer43", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer44: int = ParamField(
        byte, "invisibleFlag_SexVer44", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer45: int = ParamField(
        byte, "invisibleFlag_SexVer45", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer46: int = ParamField(
        byte, "invisibleFlag_SexVer46", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer47: int = ParamField(
        byte, "invisibleFlag_SexVer47", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer48: int = ParamField(
        byte, "invisibleFlag_SexVer48", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer49: int = ParamField(
        byte, "invisibleFlag_SexVer49", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer50: int = ParamField(
        byte, "invisibleFlag_SexVer50", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer51: int = ParamField(
        byte, "invisibleFlag_SexVer51", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer52: int = ParamField(
        byte, "invisibleFlag_SexVer52", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer53: int = ParamField(
        byte, "invisibleFlag_SexVer53", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer54: int = ParamField(
        byte, "invisibleFlag_SexVer54", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer55: int = ParamField(
        byte, "invisibleFlag_SexVer55", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer56: int = ParamField(
        byte, "invisibleFlag_SexVer56", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer57: int = ParamField(
        byte, "invisibleFlag_SexVer57", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer58: int = ParamField(
        byte, "invisibleFlag_SexVer58", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer59: int = ParamField(
        byte, "invisibleFlag_SexVer59", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer60: int = ParamField(
        byte, "invisibleFlag_SexVer60", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer61: int = ParamField(
        byte, "invisibleFlag_SexVer61", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer62: int = ParamField(
        byte, "invisibleFlag_SexVer62", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer63: int = ParamField(
        byte, "invisibleFlag_SexVer63", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer64: int = ParamField(
        byte, "invisibleFlag_SexVer64", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer65: int = ParamField(
        byte, "invisibleFlag_SexVer65", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer66: int = ParamField(
        byte, "invisibleFlag_SexVer66", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer67: int = ParamField(
        byte, "invisibleFlag_SexVer67", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer68: int = ParamField(
        byte, "invisibleFlag_SexVer68", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer69: int = ParamField(
        byte, "invisibleFlag_SexVer69", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer70: int = ParamField(
        byte, "invisibleFlag_SexVer70", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer71: int = ParamField(
        byte, "invisibleFlag_SexVer71", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer72: int = ParamField(
        byte, "invisibleFlag_SexVer72", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer73: int = ParamField(
        byte, "invisibleFlag_SexVer73", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer74: int = ParamField(
        byte, "invisibleFlag_SexVer74", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer75: int = ParamField(
        byte, "invisibleFlag_SexVer75", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer76: int = ParamField(
        byte, "invisibleFlag_SexVer76", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer77: int = ParamField(
        byte, "invisibleFlag_SexVer77", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer78: int = ParamField(
        byte, "invisibleFlag_SexVer78", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer79: int = ParamField(
        byte, "invisibleFlag_SexVer79", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer80: int = ParamField(
        byte, "invisibleFlag_SexVer80", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer81: int = ParamField(
        byte, "invisibleFlag_SexVer81", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer82: int = ParamField(
        byte, "invisibleFlag_SexVer82", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer83: int = ParamField(
        byte, "invisibleFlag_SexVer83", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer84: int = ParamField(
        byte, "invisibleFlag_SexVer84", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer85: int = ParamField(
        byte, "invisibleFlag_SexVer85", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer86: int = ParamField(
        byte, "invisibleFlag_SexVer86", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer87: int = ParamField(
        byte, "invisibleFlag_SexVer87", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer88: int = ParamField(
        byte, "invisibleFlag_SexVer88", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer89: int = ParamField(
        byte, "invisibleFlag_SexVer89", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer90: int = ParamField(
        byte, "invisibleFlag_SexVer90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer91: int = ParamField(
        byte, "invisibleFlag_SexVer91", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer92: int = ParamField(
        byte, "invisibleFlag_SexVer92", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer93: int = ParamField(
        byte, "invisibleFlag_SexVer93", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer94: int = ParamField(
        byte, "invisibleFlag_SexVer94", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer95: int = ParamField(
        byte, "invisibleFlag_SexVer95", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(14, "pad404[14]")
