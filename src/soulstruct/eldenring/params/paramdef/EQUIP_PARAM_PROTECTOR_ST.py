from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SortIndex: int = ParamField(
        int32, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    GhostArmorReplacement: int = ParamField(
        uint32, "wanderingEquipId", default=0,
        tooltip="Replacement equipment for network ghosts.",
    )
    ResistSleep: int = ParamField(
        uint16, "resistSleep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistMadness: int = ParamField(
        uint16, "resistMadness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Poise: float = ParamField(
        float32, "saDurability", default=0.0,
        tooltip="Amount of poise added when wearing armor.",
    )
    ToughnessCorrectRate: float = ParamField(
        float32, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
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
    _Pad1: bytes = ParamPad(2, "pad03[2]")
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
    TrophySGradeId: int = ParamField(
        int16, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
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
    Rarity: int = ParamField(
        uint8, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        uint8, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageType: int = ParamField(
        uint8, "partsDmgType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Always zero.",
    )
    _Pad2: bytes = ParamPad(2, "pad04[2]")
    CanBeStored: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor can be stored in storage.",
    )
    EquippedToHead: bool = ParamField(
        uint8, "headEquip:1", EQUIP_BOOL, bit_count=1, default=False,
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
    IsSkipWeakDamageAnim: bool = ParamField(
        uint8, "isSkipWeakDamageAnim:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad06:1", bit_count=1)
    DefenseMaterialVariationValueWeak: int = ParamField(
        uint8, "defenseMaterialVariationValue_Weak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId2: int = ParamField(
        int16, "autoFootEffectDecalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId3: int = ParamField(
        int16, "autoFootEffectDecalBaseId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialVariationValue: int = ParamField(
        uint8, "defenseMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: bool = ParamField(
        uint8, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: bool = ParamField(
        uint8, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this armor cannot be given to other players by dropping it. Always False in vanilla.",
    )
    SimpleDLCModelExists: bool = ParamField(
        uint8, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; always set to False.",
    )
    ShowLogCondType: bool = ParamField(
        uint8, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        uint8, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(uint8, "pad:1", bit_count=1)
    NeutralDamageCutRate: float = ParamField(
        float32, "neutralDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
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
    DefenseMaterialSfx1: int = ParamField(
        uint16, "defenseMaterialSfx1", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak1: int = ParamField(
        uint16, "defenseMaterialSfx_Weak1", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterial1: int = ParamField(
        uint16, "defenseMaterial1", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak1: int = ParamField(
        uint16, "defenseMaterial_Weak1", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfx2: int = ParamField(
        uint16, "defenseMaterialSfx2", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak2: int = ParamField(
        uint16, "defenseMaterialSfx_Weak2", WEP_MATERIAL_DEF_SFX, default=50,
        tooltip="TOOLTIP-TODO",
    )
    FootMaterialSe: int = ParamField(
        uint16, "footMaterialSe", WEP_MATERIAL_DEF, default=139,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak2: int = ParamField(
        uint16, "defenseMaterial_Weak2", WEP_MATERIAL_DEF, default=50,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId1: int = ParamField(
        int32, "autoFootEffectDecalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessDamageCutRate: float = ParamField(
        float32, "toughnessDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float32, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float32, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseDark: int = ParamField(
        uint16, "defenseDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad3: int = ParamBitPad(uint8, "invisibleFlag48:1", bit_count=1)
    _BitPad4: int = ParamBitPad(uint8, "invisibleFlag49:1", bit_count=1)
    _BitPad5: int = ParamBitPad(uint8, "invisibleFlag50:1", bit_count=1)
    _BitPad6: int = ParamBitPad(uint8, "invisibleFlag51:1", bit_count=1)
    _BitPad7: int = ParamBitPad(uint8, "invisibleFlag52:1", bit_count=1)
    _BitPad8: int = ParamBitPad(uint8, "invisibleFlag53:1", bit_count=1)
    _BitPad9: int = ParamBitPad(uint8, "invisibleFlag54:1", bit_count=1)
    _BitPad10: int = ParamBitPad(uint8, "invisibleFlag55:1", bit_count=1)
    _BitPad11: int = ParamBitPad(uint8, "invisibleFlag56:1", bit_count=1)
    _BitPad12: int = ParamBitPad(uint8, "invisibleFlag57:1", bit_count=1)
    _BitPad13: int = ParamBitPad(uint8, "invisibleFlag58:1", bit_count=1)
    _BitPad14: int = ParamBitPad(uint8, "invisibleFlag59:1", bit_count=1)
    _BitPad15: int = ParamBitPad(uint8, "invisibleFlag60:1", bit_count=1)
    _BitPad16: int = ParamBitPad(uint8, "invisibleFlag61:1", bit_count=1)
    _BitPad17: int = ParamBitPad(uint8, "invisibleFlag62:1", bit_count=1)
    _BitPad18: int = ParamBitPad(uint8, "invisibleFlag63:1", bit_count=1)
    _BitPad19: int = ParamBitPad(uint8, "invisibleFlag64:1", bit_count=1)
    _BitPad20: int = ParamBitPad(uint8, "invisibleFlag65:1", bit_count=1)
    _BitPad21: int = ParamBitPad(uint8, "invisibleFlag66:1", bit_count=1)
    _BitPad22: int = ParamBitPad(uint8, "invisibleFlag67:1", bit_count=1)
    _BitPad23: int = ParamBitPad(uint8, "invisibleFlag68:1", bit_count=1)
    _BitPad24: int = ParamBitPad(uint8, "invisibleFlag69:1", bit_count=1)
    _BitPad25: int = ParamBitPad(uint8, "invisibleFlag70:1", bit_count=1)
    _BitPad26: int = ParamBitPad(uint8, "invisibleFlag71:1", bit_count=1)
    _BitPad27: int = ParamBitPad(uint8, "invisibleFlag72:1", bit_count=1)
    _BitPad28: int = ParamBitPad(uint8, "invisibleFlag73:1", bit_count=1)
    _BitPad29: int = ParamBitPad(uint8, "invisibleFlag74:1", bit_count=1)
    _BitPad30: int = ParamBitPad(uint8, "invisibleFlag75:1", bit_count=1)
    _BitPad31: int = ParamBitPad(uint8, "invisibleFlag76:1", bit_count=1)
    _BitPad32: int = ParamBitPad(uint8, "invisibleFlag77:1", bit_count=1)
    _BitPad33: int = ParamBitPad(uint8, "invisibleFlag78:1", bit_count=1)
    _BitPad34: int = ParamBitPad(uint8, "invisibleFlag79:1", bit_count=1)
    _BitPad35: int = ParamBitPad(uint8, "invisibleFlag80:1", bit_count=1)
    _BitPad36: int = ParamBitPad(uint8, "padbit:7", bit_count=7)
    PostureControlId: int = ParamField(
        uint8, "postureControlId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad2[4]")
    SaleValue: int = ParamField(
        int32, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistFreeze: int = ParamField(
        uint16, "resistFreeze", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer00: int = ParamField(
        uint8, "invisibleFlag_SexVer00", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer01: int = ParamField(
        uint8, "invisibleFlag_SexVer01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer02: int = ParamField(
        uint8, "invisibleFlag_SexVer02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer03: int = ParamField(
        uint8, "invisibleFlag_SexVer03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer04: int = ParamField(
        uint8, "invisibleFlag_SexVer04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer05: int = ParamField(
        uint8, "invisibleFlag_SexVer05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer06: int = ParamField(
        uint8, "invisibleFlag_SexVer06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer07: int = ParamField(
        uint8, "invisibleFlag_SexVer07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer08: int = ParamField(
        uint8, "invisibleFlag_SexVer08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer09: int = ParamField(
        uint8, "invisibleFlag_SexVer09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer10: int = ParamField(
        uint8, "invisibleFlag_SexVer10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer11: int = ParamField(
        uint8, "invisibleFlag_SexVer11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer12: int = ParamField(
        uint8, "invisibleFlag_SexVer12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer13: int = ParamField(
        uint8, "invisibleFlag_SexVer13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer14: int = ParamField(
        uint8, "invisibleFlag_SexVer14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer15: int = ParamField(
        uint8, "invisibleFlag_SexVer15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer16: int = ParamField(
        uint8, "invisibleFlag_SexVer16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer17: int = ParamField(
        uint8, "invisibleFlag_SexVer17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer18: int = ParamField(
        uint8, "invisibleFlag_SexVer18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer19: int = ParamField(
        uint8, "invisibleFlag_SexVer19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer20: int = ParamField(
        uint8, "invisibleFlag_SexVer20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer21: int = ParamField(
        uint8, "invisibleFlag_SexVer21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer22: int = ParamField(
        uint8, "invisibleFlag_SexVer22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer23: int = ParamField(
        uint8, "invisibleFlag_SexVer23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer24: int = ParamField(
        uint8, "invisibleFlag_SexVer24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer25: int = ParamField(
        uint8, "invisibleFlag_SexVer25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer26: int = ParamField(
        uint8, "invisibleFlag_SexVer26", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer27: int = ParamField(
        uint8, "invisibleFlag_SexVer27", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer28: int = ParamField(
        uint8, "invisibleFlag_SexVer28", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer29: int = ParamField(
        uint8, "invisibleFlag_SexVer29", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer30: int = ParamField(
        uint8, "invisibleFlag_SexVer30", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer31: int = ParamField(
        uint8, "invisibleFlag_SexVer31", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer32: int = ParamField(
        uint8, "invisibleFlag_SexVer32", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer33: int = ParamField(
        uint8, "invisibleFlag_SexVer33", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer34: int = ParamField(
        uint8, "invisibleFlag_SexVer34", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer35: int = ParamField(
        uint8, "invisibleFlag_SexVer35", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer36: int = ParamField(
        uint8, "invisibleFlag_SexVer36", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer37: int = ParamField(
        uint8, "invisibleFlag_SexVer37", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer38: int = ParamField(
        uint8, "invisibleFlag_SexVer38", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer39: int = ParamField(
        uint8, "invisibleFlag_SexVer39", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer40: int = ParamField(
        uint8, "invisibleFlag_SexVer40", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer41: int = ParamField(
        uint8, "invisibleFlag_SexVer41", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer42: int = ParamField(
        uint8, "invisibleFlag_SexVer42", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer43: int = ParamField(
        uint8, "invisibleFlag_SexVer43", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer44: int = ParamField(
        uint8, "invisibleFlag_SexVer44", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer45: int = ParamField(
        uint8, "invisibleFlag_SexVer45", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer46: int = ParamField(
        uint8, "invisibleFlag_SexVer46", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer47: int = ParamField(
        uint8, "invisibleFlag_SexVer47", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer48: int = ParamField(
        uint8, "invisibleFlag_SexVer48", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer49: int = ParamField(
        uint8, "invisibleFlag_SexVer49", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer50: int = ParamField(
        uint8, "invisibleFlag_SexVer50", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer51: int = ParamField(
        uint8, "invisibleFlag_SexVer51", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer52: int = ParamField(
        uint8, "invisibleFlag_SexVer52", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer53: int = ParamField(
        uint8, "invisibleFlag_SexVer53", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer54: int = ParamField(
        uint8, "invisibleFlag_SexVer54", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer55: int = ParamField(
        uint8, "invisibleFlag_SexVer55", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer56: int = ParamField(
        uint8, "invisibleFlag_SexVer56", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer57: int = ParamField(
        uint8, "invisibleFlag_SexVer57", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer58: int = ParamField(
        uint8, "invisibleFlag_SexVer58", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer59: int = ParamField(
        uint8, "invisibleFlag_SexVer59", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer60: int = ParamField(
        uint8, "invisibleFlag_SexVer60", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer61: int = ParamField(
        uint8, "invisibleFlag_SexVer61", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer62: int = ParamField(
        uint8, "invisibleFlag_SexVer62", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer63: int = ParamField(
        uint8, "invisibleFlag_SexVer63", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer64: int = ParamField(
        uint8, "invisibleFlag_SexVer64", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer65: int = ParamField(
        uint8, "invisibleFlag_SexVer65", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer66: int = ParamField(
        uint8, "invisibleFlag_SexVer66", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer67: int = ParamField(
        uint8, "invisibleFlag_SexVer67", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer68: int = ParamField(
        uint8, "invisibleFlag_SexVer68", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer69: int = ParamField(
        uint8, "invisibleFlag_SexVer69", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer70: int = ParamField(
        uint8, "invisibleFlag_SexVer70", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer71: int = ParamField(
        uint8, "invisibleFlag_SexVer71", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer72: int = ParamField(
        uint8, "invisibleFlag_SexVer72", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer73: int = ParamField(
        uint8, "invisibleFlag_SexVer73", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer74: int = ParamField(
        uint8, "invisibleFlag_SexVer74", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer75: int = ParamField(
        uint8, "invisibleFlag_SexVer75", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer76: int = ParamField(
        uint8, "invisibleFlag_SexVer76", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer77: int = ParamField(
        uint8, "invisibleFlag_SexVer77", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer78: int = ParamField(
        uint8, "invisibleFlag_SexVer78", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer79: int = ParamField(
        uint8, "invisibleFlag_SexVer79", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer80: int = ParamField(
        uint8, "invisibleFlag_SexVer80", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer81: int = ParamField(
        uint8, "invisibleFlag_SexVer81", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer82: int = ParamField(
        uint8, "invisibleFlag_SexVer82", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer83: int = ParamField(
        uint8, "invisibleFlag_SexVer83", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer84: int = ParamField(
        uint8, "invisibleFlag_SexVer84", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer85: int = ParamField(
        uint8, "invisibleFlag_SexVer85", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer86: int = ParamField(
        uint8, "invisibleFlag_SexVer86", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer87: int = ParamField(
        uint8, "invisibleFlag_SexVer87", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer88: int = ParamField(
        uint8, "invisibleFlag_SexVer88", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer89: int = ParamField(
        uint8, "invisibleFlag_SexVer89", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer90: int = ParamField(
        uint8, "invisibleFlag_SexVer90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer91: int = ParamField(
        uint8, "invisibleFlag_SexVer91", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer92: int = ParamField(
        uint8, "invisibleFlag_SexVer92", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer93: int = ParamField(
        uint8, "invisibleFlag_SexVer93", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer94: int = ParamField(
        uint8, "invisibleFlag_SexVer94", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InvisibleFlagSexVer95: int = ParamField(
        uint8, "invisibleFlag_SexVer95", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(14, "pad404[14]")
