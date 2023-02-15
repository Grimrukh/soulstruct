from __future__ import annotations

__all__ = ["EQUIP_PARAM_GEM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_GEM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rank: int = ParamField(
        sbyte, "rank", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemGetTutorialFlagId: int = ParamField(
        uint, "itemGetTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SwordArtsParamId: int = ParamField(
        int, "swordArtsParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MountValue: int = ParamField(
        int, "mountValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompTrophySedId: int = ParamField(
        short, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrophySeqId: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr00: bool = ParamField(
        byte, "configurableWepAttr00:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr01: bool = ParamField(
        byte, "configurableWepAttr01:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr02: bool = ParamField(
        byte, "configurableWepAttr02:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr03: bool = ParamField(
        byte, "configurableWepAttr03:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr04: bool = ParamField(
        byte, "configurableWepAttr04:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr05: bool = ParamField(
        byte, "configurableWepAttr05:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr06: bool = ParamField(
        byte, "configurableWepAttr06:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr07: bool = ParamField(
        byte, "configurableWepAttr07:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr08: bool = ParamField(
        byte, "configurableWepAttr08:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr09: bool = ParamField(
        byte, "configurableWepAttr09:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr10: bool = ParamField(
        byte, "configurableWepAttr10:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr11: bool = ParamField(
        byte, "configurableWepAttr11:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr12: bool = ParamField(
        byte, "configurableWepAttr12:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr13: bool = ParamField(
        byte, "configurableWepAttr13:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr14: bool = ParamField(
        byte, "configurableWepAttr14:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr15: bool = ParamField(
        byte, "configurableWepAttr15:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr16: bool = ParamField(
        byte, "configurableWepAttr16:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr17: bool = ParamField(
        byte, "configurableWepAttr17:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr18: bool = ParamField(
        byte, "configurableWepAttr18:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr19: bool = ParamField(
        byte, "configurableWepAttr19:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr20: bool = ParamField(
        byte, "configurableWepAttr20:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr21: bool = ParamField(
        byte, "configurableWepAttr21:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr22: bool = ParamField(
        byte, "configurableWepAttr22:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr23: bool = ParamField(
        byte, "configurableWepAttr23:1", EQUIP_BOOL, bit_count=1, default=False,
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
    IsDeposit: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        byte, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad:1", bit_count=1)
    DefaultWepAttr: int = ParamField(
        byte, "defaultWepAttr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    CanMountWepDagger: bool = ParamField(
        byte, "canMountWep_Dagger:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordNormal: bool = ParamField(
        byte, "canMountWep_SwordNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordLarge: bool = ParamField(
        byte, "canMountWep_SwordLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordGigantic: bool = ParamField(
        byte, "canMountWep_SwordGigantic:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberNormal: bool = ParamField(
        byte, "canMountWep_SaberNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberLarge: bool = ParamField(
        byte, "canMountWep_SaberLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepkatana: bool = ParamField(
        byte, "canMountWep_katana:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordDoubleEdge: bool = ParamField(
        byte, "canMountWep_SwordDoubleEdge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordPierce: bool = ParamField(
        byte, "canMountWep_SwordPierce:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepRapierHeavy: bool = ParamField(
        byte, "canMountWep_RapierHeavy:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeNormal: bool = ParamField(
        byte, "canMountWep_AxeNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeLarge: bool = ParamField(
        byte, "canMountWep_AxeLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerNormal: bool = ParamField(
        byte, "canMountWep_HammerNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerLarge: bool = ParamField(
        byte, "canMountWep_HammerLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepFlail: bool = ParamField(
        byte, "canMountWep_Flail:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearNormal: bool = ParamField(
        byte, "canMountWep_SpearNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearLarge: bool = ParamField(
        byte, "canMountWep_SpearLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearHeavy: bool = ParamField(
        byte, "canMountWep_SpearHeavy:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearAxe: bool = ParamField(
        byte, "canMountWep_SpearAxe:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSickle: bool = ParamField(
        byte, "canMountWep_Sickle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepKnuckle: bool = ParamField(
        byte, "canMountWep_Knuckle:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClaw: bool = ParamField(
        byte, "canMountWep_Claw:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepWhip: bool = ParamField(
        byte, "canMountWep_Whip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxhammerLarge: bool = ParamField(
        byte, "canMountWep_AxhammerLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowSmall: bool = ParamField(
        byte, "canMountWep_BowSmall:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowNormal: bool = ParamField(
        byte, "canMountWep_BowNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowLarge: bool = ParamField(
        byte, "canMountWep_BowLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClossBow: bool = ParamField(
        byte, "canMountWep_ClossBow:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBallista: bool = ParamField(
        byte, "canMountWep_Ballista:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepStaff: bool = ParamField(
        byte, "canMountWep_Staff:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSorcery: bool = ParamField(
        byte, "canMountWep_Sorcery:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTalisman: bool = ParamField(
        byte, "canMountWep_Talisman:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldSmall: bool = ParamField(
        byte, "canMountWep_ShieldSmall:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldNormal: bool = ParamField(
        byte, "canMountWep_ShieldNormal:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldLarge: bool = ParamField(
        byte, "canMountWep_ShieldLarge:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTorch: bool = ParamField(
        byte, "canMountWep_Torch:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(byte, "reserved_canMountWep:4", bit_count=4)
    _Pad2: bytes = ParamPad(3, "reserved2_canMountWep[3]")
    SpEffectMsgId0: int = ParamField(
        int, "spEffectMsgId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectMsgId1: int = ParamField(
        int, "spEffectMsgId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk0: int = ParamField(
        int, "spEffectId_forAtk0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk1: int = ParamField(
        int, "spEffectId_forAtk1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforAtk2: int = ParamField(
        int, "spEffectId_forAtk2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MountWepTextId: int = ParamField(
        int, "mountWepTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad6[8]")
