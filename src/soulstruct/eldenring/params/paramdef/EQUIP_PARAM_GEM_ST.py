from __future__ import annotations

__all__ = ["EQUIP_PARAM_GEM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_GEM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    IconId: int = ParamField(
        uint16, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rank: int = ParamField(
        int8, "rank", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        uint8, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId0: int = ParamField(
        int32, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        int32, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int32, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemGetTutorialFlagId: int = ParamField(
        uint32, "itemGetTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SwordArtsParamId: int = ParamField(
        int32, "swordArtsParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MountValue: int = ParamField(
        int32, "mountValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int32, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaleValue: int = ParamField(
        int32, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int32, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompTrophySedId: int = ParamField(
        int16, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrophySeqId: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr00: bool = ParamField(
        uint8, "configurableWepAttr00:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr01: bool = ParamField(
        uint8, "configurableWepAttr01:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr02: bool = ParamField(
        uint8, "configurableWepAttr02:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr03: bool = ParamField(
        uint8, "configurableWepAttr03:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr04: bool = ParamField(
        uint8, "configurableWepAttr04:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr05: bool = ParamField(
        uint8, "configurableWepAttr05:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr06: bool = ParamField(
        uint8, "configurableWepAttr06:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr07: bool = ParamField(
        uint8, "configurableWepAttr07:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr08: bool = ParamField(
        uint8, "configurableWepAttr08:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr09: bool = ParamField(
        uint8, "configurableWepAttr09:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr10: bool = ParamField(
        uint8, "configurableWepAttr10:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr11: bool = ParamField(
        uint8, "configurableWepAttr11:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr12: bool = ParamField(
        uint8, "configurableWepAttr12:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr13: bool = ParamField(
        uint8, "configurableWepAttr13:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr14: bool = ParamField(
        uint8, "configurableWepAttr14:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr15: bool = ParamField(
        uint8, "configurableWepAttr15:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        uint8, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr16: bool = ParamField(
        uint8, "configurableWepAttr16:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr17: bool = ParamField(
        uint8, "configurableWepAttr17:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr18: bool = ParamField(
        uint8, "configurableWepAttr18:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr19: bool = ParamField(
        uint8, "configurableWepAttr19:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr20: bool = ParamField(
        uint8, "configurableWepAttr20:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr21: bool = ParamField(
        uint8, "configurableWepAttr21:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr22: bool = ParamField(
        uint8, "configurableWepAttr22:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr23: bool = ParamField(
        uint8, "configurableWepAttr23:1", EQUIP_BOOL, bit_count=1, default=False,
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
    IsDeposit: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        uint8, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        uint8, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad:1", bit_count=1)
    DefaultWepAttr: int = ParamField(
        uint8, "defaultWepAttr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSpecialSwordArt: int = ParamField(
        uint8, "isSpecialSwordArt", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad2[1]")
    CanMountWepDagger: bool = ParamField(
        uint8, "canMountWep_Dagger:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordNormal: bool = ParamField(
        uint8, "canMountWep_SwordNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordLarge: bool = ParamField(
        uint8, "canMountWep_SwordLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordGigantic: bool = ParamField(
        uint8, "canMountWep_SwordGigantic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberNormal: bool = ParamField(
        uint8, "canMountWep_SaberNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberLarge: bool = ParamField(
        uint8, "canMountWep_SaberLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepkatana: bool = ParamField(
        uint8, "canMountWep_katana:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordDoubleEdge: bool = ParamField(
        uint8, "canMountWep_SwordDoubleEdge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordPierce: bool = ParamField(
        uint8, "canMountWep_SwordPierce:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepRapierHeavy: bool = ParamField(
        uint8, "canMountWep_RapierHeavy:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeNormal: bool = ParamField(
        uint8, "canMountWep_AxeNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeLarge: bool = ParamField(
        uint8, "canMountWep_AxeLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerNormal: bool = ParamField(
        uint8, "canMountWep_HammerNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerLarge: bool = ParamField(
        uint8, "canMountWep_HammerLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepFlail: bool = ParamField(
        uint8, "canMountWep_Flail:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearNormal: bool = ParamField(
        uint8, "canMountWep_SpearNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearLarge: bool = ParamField(
        uint8, "canMountWep_SpearLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearHeavy: bool = ParamField(
        uint8, "canMountWep_SpearHeavy:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearAxe: bool = ParamField(
        uint8, "canMountWep_SpearAxe:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSickle: bool = ParamField(
        uint8, "canMountWep_Sickle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepKnuckle: bool = ParamField(
        uint8, "canMountWep_Knuckle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClaw: bool = ParamField(
        uint8, "canMountWep_Claw:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepWhip: bool = ParamField(
        uint8, "canMountWep_Whip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxhammerLarge: bool = ParamField(
        uint8, "canMountWep_AxhammerLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowSmall: bool = ParamField(
        uint8, "canMountWep_BowSmall:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowNormal: bool = ParamField(
        uint8, "canMountWep_BowNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowLarge: bool = ParamField(
        uint8, "canMountWep_BowLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClossBow: bool = ParamField(
        uint8, "canMountWep_ClossBow:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBallista: bool = ParamField(
        uint8, "canMountWep_Ballista:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepStaff: bool = ParamField(
        uint8, "canMountWep_Staff:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSorcery: bool = ParamField(
        uint8, "canMountWep_Sorcery:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTalisman: bool = ParamField(
        uint8, "canMountWep_Talisman:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldSmall: bool = ParamField(
        uint8, "canMountWep_ShieldSmall:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldNormal: bool = ParamField(
        uint8, "canMountWep_ShieldNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldLarge: bool = ParamField(
        uint8, "canMountWep_ShieldLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTorch: bool = ParamField(
        uint8, "canMountWep_Torch:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHandToHand: bool = ParamField(
        uint8, "canMountWep_HandToHand:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepPerfumeBottle: bool = ParamField(
        uint8, "canMountWep_PerfumeBottle:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepThrustingShield: bool = ParamField(
        uint8, "canMountWep_ThrustingShield:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepThrowingWeapon: bool = ParamField(
        uint8, "canMountWep_ThrowingWeapon:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepReverseHandSword: bool = ParamField(
        uint8, "canMountWep_ReverseHandSword:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepLightGreatsword: bool = ParamField(
        uint8, "canMountWep_LightGreatsword:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepGreatKatana: bool = ParamField(
        uint8, "canMountWep_GreatKatana:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBeastClaw: bool = ParamField(
        uint8, "canMountWep_BeastClaw:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(uint8, "reserved_canMountWep_0x3d_4:4", bit_count=4)
    _Pad2: bytes = ParamPad(2, "reserved2_canMountWep[2]")
    SpEffectMsgId0: int = ParamField(
        int32, "spEffectMsgId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId1: int = ParamField(
        int32, "spEffectMsgId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk0: int = ParamField(
        int32, "spEffectId_forAtk0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk1: int = ParamField(
        int32, "spEffectId_forAtk1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk2: int = ParamField(
        int32, "spEffectId_forAtk2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MountWepTextId: int = ParamField(
        int32, "mountWepTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad6[8]")
