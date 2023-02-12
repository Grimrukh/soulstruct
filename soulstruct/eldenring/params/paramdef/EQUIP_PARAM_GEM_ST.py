from __future__ import annotations

__all__ = ["EQUIP_PARAM_GEM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_GEM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
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
    ConfigurableWepAttr00: int = ParamField(
        byte, "configurableWepAttr00:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr01: int = ParamField(
        byte, "configurableWepAttr01:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr02: int = ParamField(
        byte, "configurableWepAttr02:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr03: int = ParamField(
        byte, "configurableWepAttr03:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr04: int = ParamField(
        byte, "configurableWepAttr04:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr05: int = ParamField(
        byte, "configurableWepAttr05:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr06: int = ParamField(
        byte, "configurableWepAttr06:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr07: int = ParamField(
        byte, "configurableWepAttr07:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr08: int = ParamField(
        byte, "configurableWepAttr08:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr09: int = ParamField(
        byte, "configurableWepAttr09:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr10: int = ParamField(
        byte, "configurableWepAttr10:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr11: int = ParamField(
        byte, "configurableWepAttr11:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr12: int = ParamField(
        byte, "configurableWepAttr12:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr13: int = ParamField(
        byte, "configurableWepAttr13:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr14: int = ParamField(
        byte, "configurableWepAttr14:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr15: int = ParamField(
        byte, "configurableWepAttr15:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr16: int = ParamField(
        byte, "configurableWepAttr16:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr17: int = ParamField(
        byte, "configurableWepAttr17:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr18: int = ParamField(
        byte, "configurableWepAttr18:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr19: int = ParamField(
        byte, "configurableWepAttr19:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr20: int = ParamField(
        byte, "configurableWepAttr20:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr21: int = ParamField(
        byte, "configurableWepAttr21:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr22: int = ParamField(
        byte, "configurableWepAttr22:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConfigurableWepAttr23: int = ParamField(
        byte, "configurableWepAttr23:1", default=0,
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
    IsDeposit: int = ParamField(
        byte, "isDeposit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: int = ParamField(
        byte, "disableMultiDropShare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: int = ParamField(
        byte, "showLogCondType:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad:1")
    DefaultWepAttr: int = ParamField(
        byte, "defaultWepAttr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(2, "pad2[2]")
    CanMountWepDagger: int = ParamField(
        byte, "canMountWep_Dagger:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordNormal: int = ParamField(
        byte, "canMountWep_SwordNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordLarge: int = ParamField(
        byte, "canMountWep_SwordLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordGigantic: int = ParamField(
        byte, "canMountWep_SwordGigantic:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberNormal: int = ParamField(
        byte, "canMountWep_SaberNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSaberLarge: int = ParamField(
        byte, "canMountWep_SaberLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepkatana: int = ParamField(
        byte, "canMountWep_katana:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordDoubleEdge: int = ParamField(
        byte, "canMountWep_SwordDoubleEdge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSwordPierce: int = ParamField(
        byte, "canMountWep_SwordPierce:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepRapierHeavy: int = ParamField(
        byte, "canMountWep_RapierHeavy:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeNormal: int = ParamField(
        byte, "canMountWep_AxeNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxeLarge: int = ParamField(
        byte, "canMountWep_AxeLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerNormal: int = ParamField(
        byte, "canMountWep_HammerNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepHammerLarge: int = ParamField(
        byte, "canMountWep_HammerLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepFlail: int = ParamField(
        byte, "canMountWep_Flail:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearNormal: int = ParamField(
        byte, "canMountWep_SpearNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearLarge: int = ParamField(
        byte, "canMountWep_SpearLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearHeavy: int = ParamField(
        byte, "canMountWep_SpearHeavy:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSpearAxe: int = ParamField(
        byte, "canMountWep_SpearAxe:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSickle: int = ParamField(
        byte, "canMountWep_Sickle:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepKnuckle: int = ParamField(
        byte, "canMountWep_Knuckle:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClaw: int = ParamField(
        byte, "canMountWep_Claw:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepWhip: int = ParamField(
        byte, "canMountWep_Whip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepAxhammerLarge: int = ParamField(
        byte, "canMountWep_AxhammerLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowSmall: int = ParamField(
        byte, "canMountWep_BowSmall:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowNormal: int = ParamField(
        byte, "canMountWep_BowNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBowLarge: int = ParamField(
        byte, "canMountWep_BowLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepClossBow: int = ParamField(
        byte, "canMountWep_ClossBow:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepBallista: int = ParamField(
        byte, "canMountWep_Ballista:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepStaff: int = ParamField(
        byte, "canMountWep_Staff:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepSorcery: int = ParamField(
        byte, "canMountWep_Sorcery:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTalisman: int = ParamField(
        byte, "canMountWep_Talisman:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldSmall: int = ParamField(
        byte, "canMountWep_ShieldSmall:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldNormal: int = ParamField(
        byte, "canMountWep_ShieldNormal:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepShieldLarge: int = ParamField(
        byte, "canMountWep_ShieldLarge:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMountWepTorch: int = ParamField(
        byte, "canMountWep_Torch:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(1, "reserved_canMountWep:4")
    _Pad5: bytes = ParamPad(3, "reserved2_canMountWep[3]")
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
    _Pad6: bytes = ParamPad(8, "pad6[8]")
