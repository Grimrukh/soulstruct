from __future__ import annotations

__all__ = ["CHARACTER_INIT_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARACTER_INIT_PARAM(ParamRow):
    BaseRecmp: float = ParamField(
        float, "baseRec_mp", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseRecsp: float = ParamField(
        float, "baseRec_sp", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedFalldam: float = ParamField(
        float, "red_Falldam", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Soul: int = ParamField(
        int, "soul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipWepRight: int = ParamField(
        int, "equip_Wep_Right", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubwepRight: int = ParamField(
        int, "equip_Subwep_Right", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipWepLeft: int = ParamField(
        int, "equip_Wep_Left", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubwepLeft: int = ParamField(
        int, "equip_Subwep_Left", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipHelm: int = ParamField(
        int, "equip_Helm", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipArmer: int = ParamField(
        int, "equip_Armer", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipGaunt: int = ParamField(
        int, "equip_Gaunt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipLeg: int = ParamField(
        int, "equip_Leg", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipArrow: int = ParamField(
        int, "equip_Arrow", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipBolt: int = ParamField(
        int, "equip_Bolt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubArrow: int = ParamField(
        int, "equip_SubArrow", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubBolt: int = ParamField(
        int, "equip_SubBolt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipAccessory01: int = ParamField(
        int, "equip_Accessory01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipAccessory02: int = ParamField(
        int, "equip_Accessory02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipAccessory03: int = ParamField(
        int, "equip_Accessory03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipAccessory04: int = ParamField(
        int, "equip_Accessory04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad8[4]")
    Elixirmaterial00: int = ParamField(
        int, "elixir_material00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Elixirmaterial01: int = ParamField(
        int, "elixir_material01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Elixirmaterial02: int = ParamField(
        int, "elixir_material02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell01: int = ParamField(
        int, "equip_Spell_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell02: int = ParamField(
        int, "equip_Spell_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell03: int = ParamField(
        int, "equip_Spell_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell04: int = ParamField(
        int, "equip_Spell_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell05: int = ParamField(
        int, "equip_Spell_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell06: int = ParamField(
        int, "equip_Spell_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSpell07: int = ParamField(
        int, "equip_Spell_07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item01: int = ParamField(
        int, "item_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item02: int = ParamField(
        int, "item_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item03: int = ParamField(
        int, "item_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item04: int = ParamField(
        int, "item_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item05: int = ParamField(
        int, "item_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item06: int = ParamField(
        int, "item_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item07: int = ParamField(
        int, "item_07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item08: int = ParamField(
        int, "item_08", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item09: int = ParamField(
        int, "item_09", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Item10: int = ParamField(
        int, "item_10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerFaceGenId: int = ParamField(
        int, "npcPlayerFaceGenId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerThinkId: int = ParamField(
        int, "npcPlayerThinkId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseHp: int = ParamField(
        ushort, "baseHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMp: int = ParamField(
        ushort, "baseMp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseSp: int = ParamField(
        ushort, "baseSp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowNum: int = ParamField(
        ushort, "arrowNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BoltNum: int = ParamField(
        ushort, "boltNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubArrowNum: int = ParamField(
        ushort, "subArrowNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubBoltNum: int = ParamField(
        ushort, "subBoltNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(6, "pad4[6]")
    SoulLv: int = ParamField(
        short, "soulLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseVit: int = ParamField(
        byte, "baseVit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseWil: int = ParamField(
        byte, "baseWil", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseEnd: int = ParamField(
        byte, "baseEnd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseStr: int = ParamField(
        byte, "baseStr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDex: int = ParamField(
        byte, "baseDex", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMag: int = ParamField(
        byte, "baseMag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseFai: int = ParamField(
        byte, "baseFai", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseLuc: int = ParamField(
        byte, "baseLuc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseHeroPoint: int = ParamField(
        byte, "baseHeroPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseDurability: int = ParamField(
        byte, "baseDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum01: int = ParamField(
        byte, "itemNum_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum02: int = ParamField(
        byte, "itemNum_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum03: int = ParamField(
        byte, "itemNum_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum04: int = ParamField(
        byte, "itemNum_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum05: int = ParamField(
        byte, "itemNum_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum06: int = ParamField(
        byte, "itemNum_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum07: int = ParamField(
        byte, "itemNum_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum08: int = ParamField(
        byte, "itemNum_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum09: int = ParamField(
        byte, "itemNum_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum10: int = ParamField(
        byte, "itemNum_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(5, "pad5[5]")
    GestureId0: int = ParamField(
        sbyte, "gestureId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId1: int = ParamField(
        sbyte, "gestureId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId2: int = ParamField(
        sbyte, "gestureId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId3: int = ParamField(
        sbyte, "gestureId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId4: int = ParamField(
        sbyte, "gestureId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId5: int = ParamField(
        sbyte, "gestureId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GestureId6: int = ParamField(
        sbyte, "gestureId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerType: int = ParamField(
        byte, "npcPlayerType", NPC_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerDrawType: int = ParamField(
        sbyte, "npcPlayerDrawType", NPC_DRAW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerSex: int = ParamField(
        byte, "npcPlayerSex", CHARACTER_INIT_SEX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    VowType: int = ParamField(
        byte, "vowType:4", VOW_TYPE, bit_count=4, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSyncTarget: bool = ParamField(
        byte, "isSyncTarget:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad:3", bit_count=3)
    _Pad3: bytes = ParamPad(2, "pad6[2]")
    WepParamTypeRight1: int = ParamField(
        byte, "wepParamType_Right1", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeRight2: int = ParamField(
        byte, "wepParamType_Right2", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeRight3: int = ParamField(
        byte, "wepParamType_Right3", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft1: int = ParamField(
        byte, "wepParamType_Left1", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft2: int = ParamField(
        byte, "wepParamType_Left2", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft3: int = ParamField(
        byte, "wepParamType_Left3", CHARA_INIT_WEP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(26, "pad2[26]")
    EquipSubwepRight3: int = ParamField(
        int, "equip_Subwep_Right3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubwepLeft3: int = ParamField(
        int, "equip_Subwep_Left3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(4, "pad3[4]")
    SecondaryItem01: int = ParamField(
        int, "secondaryItem_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItem02: int = ParamField(
        int, "secondaryItem_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItem03: int = ParamField(
        int, "secondaryItem_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItem04: int = ParamField(
        int, "secondaryItem_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItem05: int = ParamField(
        int, "secondaryItem_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItem06: int = ParamField(
        int, "secondaryItem_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum01: int = ParamField(
        byte, "secondaryItemNum_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum02: int = ParamField(
        byte, "secondaryItemNum_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum03: int = ParamField(
        byte, "secondaryItemNum_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum04: int = ParamField(
        byte, "secondaryItemNum_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum05: int = ParamField(
        byte, "secondaryItemNum_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryItemNum06: int = ParamField(
        byte, "secondaryItemNum_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstMax: int = ParamField(
        sbyte, "HpEstMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MpEstMax: int = ParamField(
        sbyte, "MpEstMax", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(5, "pad7[5]")
    VoiceType: int = ParamField(
        byte, "voiceType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(6, "reserve[6]")
