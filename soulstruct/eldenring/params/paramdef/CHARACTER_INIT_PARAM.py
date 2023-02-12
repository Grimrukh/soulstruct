from __future__ import annotations

__all__ = ["CHARACTER_INIT_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARACTER_INIT_PARAM(ParamRow):
    BaseRecMP: float = ParamField(
        float, "baseRec_mp", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BaseRecSP: float = ParamField(
        float, "baseRec_sp", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RedFallDamage: float = ParamField(
        float, "red_Falldam", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SoulCount: int = ParamField(
        int, "soul", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RightHandWeapon1: int = ParamField(
        int, "equip_Wep_Right", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RightHandWeapon2: int = ParamField(
        int, "equip_Subwep_Right", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LeftHandWeapon1: int = ParamField(
        int, "equip_Wep_Left", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LeftHandWeapon2: int = ParamField(
        int, "equip_Subwep_Left", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HeadArmor: int = ParamField(
        int, "equip_Helm", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BodyArmor: int = ParamField(
        int, "equip_Armer", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HandsArmor: int = ParamField(
        int, "equip_Gaunt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LegsArmor: int = ParamField(
        int, "equip_Leg", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ArrowSlot1: int = ParamField(
        int, "equip_Arrow", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BoltSlot1: int = ParamField(
        int, "equip_Bolt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ArrowSlot2: int = ParamField(
        int, "equip_SubArrow", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BoltSlot2: int = ParamField(
        int, "equip_SubBolt", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RingSlot1: int = ParamField(
        int, "equip_Accessory01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RingSlot2: int = ParamField(
        int, "equip_Accessory02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RingSlot3: int = ParamField(
        int, "equip_Accessory03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RingSlot4: int = ParamField(
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
    SpellSlot1: int = ParamField(
        int, "equip_Spell_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot2: int = ParamField(
        int, "equip_Spell_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot3: int = ParamField(
        int, "equip_Spell_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot4: int = ParamField(
        int, "equip_Spell_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot5: int = ParamField(
        int, "equip_Spell_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot6: int = ParamField(
        int, "equip_Spell_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpellSlot7: int = ParamField(
        int, "equip_Spell_07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot1: int = ParamField(
        int, "item_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot2: int = ParamField(
        int, "item_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot3: int = ParamField(
        int, "item_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot4: int = ParamField(
        int, "item_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot5: int = ParamField(
        int, "item_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot6: int = ParamField(
        int, "item_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot7: int = ParamField(
        int, "item_07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot8: int = ParamField(
        int, "item_08", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot9: int = ParamField(
        int, "item_09", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot10: int = ParamField(
        int, "item_10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FaceID: int = ParamField(
        int, "npcPlayerFaceGenId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefaultAI: int = ParamField(
        int, "npcPlayerThinkId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMaxHP: int = ParamField(
        ushort, "baseHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMaxMP: int = ParamField(
        ushort, "baseMp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BaseMaxStamina: int = ParamField(
        ushort, "baseSp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowSlot1Count: int = ParamField(
        ushort, "arrowNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BoltSlot1Count: int = ParamField(
        ushort, "boltNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ArrowSlot2Count: int = ParamField(
        ushort, "subArrowNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BoltSlot2Count: int = ParamField(
        ushort, "subBoltNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(6, "pad4[6]")
    Level: int = ParamField(
        short, "soulLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Vitality: int = ParamField(
        byte, "baseVit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Attunement: int = ParamField(
        byte, "baseWil", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Endurance: int = ParamField(
        byte, "baseEnd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Strength: int = ParamField(
        byte, "baseStr", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dexterity: int = ParamField(
        byte, "baseDex", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Intelligence: int = ParamField(
        byte, "baseMag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Faith: int = ParamField(
        byte, "baseFai", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Luck: int = ParamField(
        byte, "baseLuc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Humanity: int = ParamField(
        byte, "baseHeroPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistance: int = ParamField(
        byte, "baseDurability", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot1Count: int = ParamField(
        byte, "itemNum_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot2Count: int = ParamField(
        byte, "itemNum_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot3Count: int = ParamField(
        byte, "itemNum_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot4Count: int = ParamField(
        byte, "itemNum_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot5Count: int = ParamField(
        byte, "itemNum_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot6Count: int = ParamField(
        byte, "itemNum_06", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot7Count: int = ParamField(
        byte, "itemNum_07", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot8Count: int = ParamField(
        byte, "itemNum_08", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot9Count: int = ParamField(
        byte, "itemNum_09", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodSlot10Count: int = ParamField(
        byte, "itemNum_10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(5, "pad5[5]")
    Gesture1: int = ParamField(
        sbyte, "gestureId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture2: int = ParamField(
        sbyte, "gestureId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture3: int = ParamField(
        sbyte, "gestureId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture4: int = ParamField(
        sbyte, "gestureId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture5: int = ParamField(
        sbyte, "gestureId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture6: int = ParamField(
        sbyte, "gestureId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Gesture7: int = ParamField(
        sbyte, "gestureId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CharacterType: int = ParamField(
        byte, "npcPlayerType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DrawType: int = ParamField(
        sbyte, "npcPlayerDrawType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Gender: int = ParamField(
        byte, "npcPlayerSex", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Covenant: int = ParamField(
        byte, "vowType:4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSyncTarget: int = ParamField(
        byte, "isSyncTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad:3")
    _Pad4: bytes = ParamPad(2, "pad6[2]")
    WepParamTypeRight1: int = ParamField(
        byte, "wepParamType_Right1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeRight2: int = ParamField(
        byte, "wepParamType_Right2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeRight3: int = ParamField(
        byte, "wepParamType_Right3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft1: int = ParamField(
        byte, "wepParamType_Left1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft2: int = ParamField(
        byte, "wepParamType_Left2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WepParamTypeLeft3: int = ParamField(
        byte, "wepParamType_Left3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(26, "pad2[26]")
    EquipSubwepRight3: int = ParamField(
        int, "equip_Subwep_Right3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubwepLeft3: int = ParamField(
        int, "equip_Subwep_Left3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(4, "pad3[4]")
    SecondaryGoodSlot1: int = ParamField(
        int, "secondaryItem_01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot2: int = ParamField(
        int, "secondaryItem_02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot3: int = ParamField(
        int, "secondaryItem_03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot4: int = ParamField(
        int, "secondaryItem_04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot5: int = ParamField(
        int, "secondaryItem_05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot6: int = ParamField(
        int, "secondaryItem_06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count1: int = ParamField(
        byte, "secondaryItemNum_01", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count2: int = ParamField(
        byte, "secondaryItemNum_02", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count3: int = ParamField(
        byte, "secondaryItemNum_03", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count4: int = ParamField(
        byte, "secondaryItemNum_04", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count5: int = ParamField(
        byte, "secondaryItemNum_05", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SecondaryGoodSlot1Count6: int = ParamField(
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
    _Pad7: bytes = ParamPad(5, "pad7[5]")
    VoiceType: int = ParamField(
        byte, "voiceType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad8: bytes = ParamPad(6, "reserve[6]")
