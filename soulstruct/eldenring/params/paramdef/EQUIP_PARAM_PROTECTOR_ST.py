from __future__ import annotations

__all__ = ["EQUIP_PARAM_PROTECTOR_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_PROTECTOR_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WanderingEquipId: int = ParamField(
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
    SaDurability: float = ParamField(
        float, "saDurability", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FixPrice: int = ParamField(
        int, "fixPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BasicPrice: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId: int = ParamField(
        int, "residentSpEffectId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId2: int = ParamField(
        int, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId3: int = ParamField(
        int, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSetId: int = ParamField(
        int, "materialSetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate: float = ParamField(
        float, "partsDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CorectSARecover: float = ParamField(
        float, "corectSARecover", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro: int = ParamField(
        int, "originEquipPro", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro1: int = ParamField(
        int, "originEquipPro1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro2: int = ParamField(
        int, "originEquipPro2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro3: int = ParamField(
        int, "originEquipPro3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro4: int = ParamField(
        int, "originEquipPro4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro5: int = ParamField(
        int, "originEquipPro5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro6: int = ParamField(
        int, "originEquipPro6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro7: int = ParamField(
        int, "originEquipPro7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro8: int = ParamField(
        int, "originEquipPro8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro9: int = ParamField(
        int, "originEquipPro9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro10: int = ParamField(
        int, "originEquipPro10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro11: int = ParamField(
        int, "originEquipPro11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro12: int = ParamField(
        int, "originEquipPro12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro13: int = ParamField(
        int, "originEquipPro13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro14: int = ParamField(
        int, "originEquipPro14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OriginEquipPro15: int = ParamField(
        int, "originEquipPro15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleMScaleX: float = ParamField(
        float, "faceScaleM_ScaleX", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleMScaleZ: float = ParamField(
        float, "faceScaleM_ScaleZ", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleMMaxX: float = ParamField(
        float, "faceScaleM_MaxX", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleMMaxZ: float = ParamField(
        float, "faceScaleM_MaxZ", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleFScaleX: float = ParamField(
        float, "faceScaleF_ScaleX", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleFScaleZ: float = ParamField(
        float, "faceScaleF_ScaleZ", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleFMaxX: float = ParamField(
        float, "faceScaleF_MaxX", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceScaleFMaxZ: float = ParamField(
        float, "faceScaleF_MaxZ", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    QwcId: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelId: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconIdM: int = ParamField(
        ushort, "iconIdM", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconIdF: int = ParamField(
        ushort, "iconIdF", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockBack: int = ParamField(
        ushort, "knockBack", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackBounceRate: int = ParamField(
        ushort, "knockbackBounceRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Durability: int = ParamField(
        ushort, "durability", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DurabilityMax: int = ParamField(
        ushort, "durabilityMax", default=100,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad03[2]")
    DefFlickPower: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefensePhysics: int = ParamField(
        ushort, "defensePhysics", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DefenseMagic: int = ParamField(
        ushort, "defenseMagic", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DefenseFire: int = ParamField(
        ushort, "defenseFire", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DefenseThunder: int = ParamField(
        ushort, "defenseThunder", default=100,
        tooltip="TOOLTIP-TODO",
    )
    DefenseSlash: int = ParamField(
        short, "defenseSlash", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseBlow: int = ParamField(
        short, "defenseBlow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseThrust: int = ParamField(
        short, "defenseThrust", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistPoison: int = ParamField(
        ushort, "resistPoison", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ResistDisease: int = ParamField(
        ushort, "resistDisease", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ResistBlood: int = ParamField(
        ushort, "resistBlood", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ResistCurse: int = ParamField(
        ushort, "resistCurse", default=100,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceTypeId: int = ParamField(
        short, "reinforceTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ShopLv: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackParamId: int = ParamField(
        byte, "knockbackParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageCutRate: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=1,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ProtectorCategory: int = ParamField(
        byte, "protectorCategory", PROTECTOR_CATEGORY, default=0,
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
    PartsDmgType: int = ParamField(
        byte, "partsDmgType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad04[2]")
    IsDeposit: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HeadEquip: bool = ParamField(
        byte, "headEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    BodyEquip: bool = ParamField(
        byte, "bodyEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ArmEquip: bool = ParamField(
        byte, "armEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    LegEquip: bool = ParamField(
        byte, "legEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UseFaceScale: bool = ParamField(
        byte, "useFaceScale:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
    DisableMultiDropShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SimpleModelForDlc: bool = ParamField(
        byte, "simpleModelForDlc:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
    SlashDamageCutRate: float = ParamField(
        float, "slashDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowDamageCutRate: float = ParamField(
        float, "blowDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageCutRate: float = ParamField(
        float, "thrustDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageCutRate: float = ParamField(
        float, "magicDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageCutRate: float = ParamField(
        float, "fireDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageCutRate: float = ParamField(
        float, "thunderDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
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
