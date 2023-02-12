from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GhostArmorReplacement: int = ParamField(
        uint, "wanderingEquipId", default=0,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RepairCost: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BasicCost: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect1: int = ParamField(
        int, "residentSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect2: int = ParamField(
        int, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WearerSpecialEffect3: int = ParamField(
        int, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeMaterialID: int = ParamField(
        int, "materialSetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SiteDamageMultiplier: float = ParamField(
        float, "partsDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoiseRecoveryTimeModifier: float = ParamField(
        float, "corectSARecover", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin0: int = ParamField(
        int, "originEquipPro", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin1: int = ParamField(
        int, "originEquipPro1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin2: int = ParamField(
        int, "originEquipPro2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin3: int = ParamField(
        int, "originEquipPro3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin4: int = ParamField(
        int, "originEquipPro4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin5: int = ParamField(
        int, "originEquipPro5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin6: int = ParamField(
        int, "originEquipPro6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin7: int = ParamField(
        int, "originEquipPro7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin8: int = ParamField(
        int, "originEquipPro8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin9: int = ParamField(
        int, "originEquipPro9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin10: int = ParamField(
        int, "originEquipPro10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin11: int = ParamField(
        int, "originEquipPro11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin12: int = ParamField(
        int, "originEquipPro12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin13: int = ParamField(
        int, "originEquipPro13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin14: int = ParamField(
        int, "originEquipPro14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeOrigin15: int = ParamField(
        int, "originEquipPro15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaleFaceScaleX: float = ParamField(
        float, "faceScaleM_ScaleX", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaleFaceScaleZ: float = ParamField(
        float, "faceScaleM_ScaleZ", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaleFaceMaxScaleX: float = ParamField(
        float, "faceScaleM_MaxX", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaleFaceMaxScaleZ: float = ParamField(
        float, "faceScaleM_MaxZ", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FemaleFaceScaleX: float = ParamField(
        float, "faceScaleF_ScaleX", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FemaleFaceScaleZ: float = ParamField(
        float, "faceScaleF_ScaleZ", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FemaleFaceMaxScaleX: float = ParamField(
        float, "faceScaleF_MaxX", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FemaleFaceMaxScaleZ: float = ParamField(
        float, "faceScaleF_MaxZ", default=1,
        tooltip="TOOLTIP-TODO",
    )
    QWCID: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModel: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaleIcon: int = ParamField(
        ushort, "iconIdM", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FemaleIcon: int = ParamField(
        ushort, "iconIdF", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackPercentageReduction: int = ParamField(
        ushort, "knockBack", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackBouncePercentage: int = ParamField(
        ushort, "knockbackBounceRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    InitialDurability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="TOOLTIP-TODO",
    )
    MaxDurability: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad03[2]")
    RepelDefense: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalDefense: int = ParamField(
        ushort, "defensePhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefense: int = ParamField(
        ushort, "defenseMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    FireDefense: int = ParamField(
        ushort, "defenseFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    LightningDefense: int = ParamField(
        ushort, "defenseThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SlashDefense: int = ParamField(
        short, "defenseSlash", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StrikeDefense: int = ParamField(
        short, "defenseBlow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDefense: int = ParamField(
        short, "defenseThrust", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonResistance: int = ParamField(
        ushort, "resistPoison", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ToxicResistance: int = ParamField(
        ushort, "resistDisease", default=100,
        tooltip="TOOLTIP-TODO",
    )
    BleedResistance: int = ParamField(
        ushort, "resistBlood", default=100,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistance: int = ParamField(
        ushort, "resistCurse", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ArmorUpgradeID: int = ParamField(
        short, "reinforceTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackID: int = ParamField(
        byte, "knockbackParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepelDamagePercentageReduction: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModelCategory: int = ParamField(
        byte, "equipModelCategory", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModelGender: int = ParamField(
        byte, "equipModelGender", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArmorType: int = ParamField(
        byte, "protectorCategory", default=0,
        tooltip="TOOLTIP-TODO",
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
        byte, "partsDmgType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(2, "pad04[2]")
    CanBeStored: int = ParamField(
        byte, "isDeposit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedToHead: int = ParamField(
        byte, "headEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedToBody: int = ParamField(
        byte, "bodyEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedToHands: int = ParamField(
        byte, "armEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquippedToLegs: int = ParamField(
        byte, "legEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseFaceScale: int = ParamField(
        byte, "useFaceScale:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWeakDamageAnim: int = ParamField(
        byte, "isSkipWeakDamageAnim:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(1, "pad06:1")
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
    IsDiscard: int = ParamField(
        byte, "isDiscard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: int = ParamField(
        byte, "isDrop:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiplayerShare: int = ParamField(
        byte, "disableMultiDropShare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SimpleDLCModelExists: int = ParamField(
        byte, "simpleModelForDlc:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: int = ParamField(
        byte, "showLogCondType:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(1, "pad:1")
    NeutralDamageCutRate: float = ParamField(
        float, "neutralDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamagePercentageReduction: float = ParamField(
        float, "slashDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BluntDamagePercentageReduction: float = ParamField(
        float, "blowDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamagePercentageReduction: float = ParamField(
        float, "thrustDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamagePercentageReduction: float = ParamField(
        float, "magicDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireDamagePercentageReduction: float = ParamField(
        float, "fireDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LightningDamagePercentageReduction: float = ParamField(
        float, "thunderDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfx1: int = ParamField(
        ushort, "defenseMaterialSfx1", default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak1: int = ParamField(
        ushort, "defenseMaterialSfx_Weak1", default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterial1: int = ParamField(
        ushort, "defenseMaterial1", default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak1: int = ParamField(
        ushort, "defenseMaterial_Weak1", default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfx2: int = ParamField(
        ushort, "defenseMaterialSfx2", default=50,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialSfxWeak2: int = ParamField(
        ushort, "defenseMaterialSfx_Weak2", default=50,
        tooltip="TOOLTIP-TODO",
    )
    FootMaterialSe: int = ParamField(
        ushort, "footMaterialSe", default=139,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMaterialWeak2: int = ParamField(
        ushort, "defenseMaterial_Weak2", default=50,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId1: int = ParamField(
        int, "autoFootEffectDecalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessDamageCutRate: float = ParamField(
        float, "toughnessDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DefenseDark: int = ParamField(
        ushort, "defenseDark", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(1, "invisibleFlag48:1")
    _Pad7: bytes = ParamPad(1, "invisibleFlag49:1")
    _Pad8: bytes = ParamPad(1, "invisibleFlag50:1")
    _Pad9: bytes = ParamPad(1, "invisibleFlag51:1")
    _Pad10: bytes = ParamPad(1, "invisibleFlag52:1")
    _Pad11: bytes = ParamPad(1, "invisibleFlag53:1")
    _Pad12: bytes = ParamPad(1, "invisibleFlag54:1")
    _Pad13: bytes = ParamPad(1, "invisibleFlag55:1")
    _Pad14: bytes = ParamPad(1, "invisibleFlag56:1")
    _Pad15: bytes = ParamPad(1, "invisibleFlag57:1")
    _Pad16: bytes = ParamPad(1, "invisibleFlag58:1")
    _Pad17: bytes = ParamPad(1, "invisibleFlag59:1")
    _Pad18: bytes = ParamPad(1, "invisibleFlag60:1")
    _Pad19: bytes = ParamPad(1, "invisibleFlag61:1")
    _Pad20: bytes = ParamPad(1, "invisibleFlag62:1")
    _Pad21: bytes = ParamPad(1, "invisibleFlag63:1")
    _Pad22: bytes = ParamPad(1, "invisibleFlag64:1")
    _Pad23: bytes = ParamPad(1, "invisibleFlag65:1")
    _Pad24: bytes = ParamPad(1, "invisibleFlag66:1")
    _Pad25: bytes = ParamPad(1, "invisibleFlag67:1")
    _Pad26: bytes = ParamPad(1, "invisibleFlag68:1")
    _Pad27: bytes = ParamPad(1, "invisibleFlag69:1")
    _Pad28: bytes = ParamPad(1, "invisibleFlag70:1")
    _Pad29: bytes = ParamPad(1, "invisibleFlag71:1")
    _Pad30: bytes = ParamPad(1, "invisibleFlag72:1")
    _Pad31: bytes = ParamPad(1, "invisibleFlag73:1")
    _Pad32: bytes = ParamPad(1, "invisibleFlag74:1")
    _Pad33: bytes = ParamPad(1, "invisibleFlag75:1")
    _Pad34: bytes = ParamPad(1, "invisibleFlag76:1")
    _Pad35: bytes = ParamPad(1, "invisibleFlag77:1")
    _Pad36: bytes = ParamPad(1, "invisibleFlag78:1")
    _Pad37: bytes = ParamPad(1, "invisibleFlag79:1")
    _Pad38: bytes = ParamPad(1, "invisibleFlag80:1")
    _Pad39: bytes = ParamPad(1, "padbit:7")
    PostureControlId: int = ParamField(
        byte, "postureControlId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad40: bytes = ParamPad(4, "pad2[4]")
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
    _Pad41: bytes = ParamPad(14, "pad404[14]")
