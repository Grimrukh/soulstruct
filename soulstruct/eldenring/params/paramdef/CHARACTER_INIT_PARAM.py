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
    BaseRecMP: float = ParamField(
        float, "baseRec_mp", default=0.0,
        tooltip="Unknown.",
    )
    BaseRecSP: float = ParamField(
        float, "baseRec_sp", default=0.0,
        tooltip="Unknown.",
    )
    RedFallDamage: float = ParamField(
        float, "red_Falldam", default=0.0,
        tooltip="Unknown.",
    )
    SoulCount: int = ParamField(
        int, "soul", default=0,
        tooltip="Starting soul count of character.",
    )
    RightHandWeapon1: int = ParamField(
        int, "equip_Wep_Right", game_type=WeaponParam, default=-1,
        tooltip="First (default) weapon/shield equipped in right hand.",
    )
    RightHandWeapon2: int = ParamField(
        int, "equip_Subwep_Right", game_type=WeaponParam, default=-1,
        tooltip="Second weapon/shield equipped in right hand.",
    )
    LeftHandWeapon1: int = ParamField(
        int, "equip_Wep_Left", game_type=WeaponParam, default=-1,
        tooltip="First (default) weapon/shield equipped in left hand.",
    )
    LeftHandWeapon2: int = ParamField(
        int, "equip_Subwep_Left", game_type=WeaponParam, default=-1,
        tooltip="Second weapon/shield equipped in left hand.",
    )
    HeadArmor: int = ParamField(
        int, "equip_Helm", game_type=ArmorParam, default=-1,
        tooltip="Armor equipped to head.",
    )
    BodyArmor: int = ParamField(
        int, "equip_Armer", game_type=ArmorParam, default=-1,
        tooltip="Armor equipped to body.",
    )
    HandsArmor: int = ParamField(
        int, "equip_Gaunt", game_type=ArmorParam, default=-1,
        tooltip="Armor equipped to hands.",
    )
    LegsArmor: int = ParamField(
        int, "equip_Leg", game_type=ArmorParam, default=-1,
        tooltip="Armor equipped to legs.",
    )
    ArrowSlot1: int = ParamField(
        int, "equip_Arrow", game_type=WeaponParam, default=-1,
        tooltip="Arrows equipped in slot 1.",
    )
    BoltSlot1: int = ParamField(
        int, "equip_Bolt", game_type=WeaponParam, default=-1,
        tooltip="Bolts equipped in slot 1.",
    )
    ArrowSlot2: int = ParamField(
        int, "equip_SubArrow", game_type=WeaponParam, default=-1,
        tooltip="Arrows equipped in slot 2.",
    )
    BoltSlot2: int = ParamField(
        int, "equip_SubBolt", game_type=WeaponParam, default=-1,
        tooltip="Bolts equipped in slot 2.",
    )
    TalismanSlot1: int = ParamField(
        int, "equip_Accessory01", game_type=AccessoryParam, default=-1,
        tooltip="First talisman equipped.",
    )
    TalismanSlot2: int = ParamField(
        int, "equip_Accessory02", game_type=AccessoryParam, default=-1,
        tooltip="Second talisman equipped.",
    )
    TalismanSlot3: int = ParamField(
        int, "equip_Accessory03", game_type=AccessoryParam, default=-1,
        tooltip="Third talisman equipped.",
    )
    TalismanSlot4: int = ParamField(
        int, "equip_Accessory04", game_type=AccessoryParam, default=-1,
        tooltip="Fourth talisman equipped.",
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
        int, "equip_Spell_01", game_type=SpellParam, default=-1,
        tooltip="First spell equipped.",
    )
    SpellSlot2: int = ParamField(
        int, "equip_Spell_02", game_type=SpellParam, default=-1,
        tooltip="Second spell equipped.",
    )
    SpellSlot3: int = ParamField(
        int, "equip_Spell_03", game_type=SpellParam, default=-1,
        tooltip="Third spell equipped.",
    )
    SpellSlot4: int = ParamField(
        int, "equip_Spell_04", game_type=SpellParam, default=-1,
        tooltip="Fourth spell equipped.",
    )
    SpellSlot5: int = ParamField(
        int, "equip_Spell_05", game_type=SpellParam, default=-1,
        tooltip="Fifth spell equipped.",
    )
    SpellSlot6: int = ParamField(
        int, "equip_Spell_06", game_type=SpellParam, default=-1,
        tooltip="Sixth spell equipped.",
    )
    SpellSlot7: int = ParamField(
        int, "equip_Spell_07", game_type=SpellParam, default=-1,
        tooltip="Seventh spell equipped.",
    )
    GoodSlot1: int = ParamField(
        int, "item_01", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 1.",
    )
    GoodSlot2: int = ParamField(
        int, "item_02", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 2.",
    )
    GoodSlot3: int = ParamField(
        int, "item_03", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 3.",
    )
    GoodSlot4: int = ParamField(
        int, "item_04", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 4.",
    )
    GoodSlot5: int = ParamField(
        int, "item_05", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 5.",
    )
    GoodSlot6: int = ParamField(
        int, "item_06", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 6.",
    )
    GoodSlot7: int = ParamField(
        int, "item_07", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 7.",
    )
    GoodSlot8: int = ParamField(
        int, "item_08", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 8.",
    )
    GoodSlot9: int = ParamField(
        int, "item_09", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 9.",
    )
    GoodSlot10: int = ParamField(
        int, "item_10", game_type=GoodParam, default=-1,
        tooltip="Good (item) equipped in slot 10.",
    )
    FaceID: int = ParamField(
        int, "npcPlayerFaceGenId", game_type=FaceGenParam, default=0,
        tooltip="Face parameter ID (NPCs only).",
    )
    DefaultAI: int = ParamField(
        int, "npcPlayerThinkId", game_type=AIParam, default=0,
        tooltip="Default AI (NPCs only).",
    )
    BaseMaxHP: int = ParamField(
        ushort, "baseHp", default=0,
        tooltip="Base amount of maximum HP (excluding effects of vitality).",
    )
    BaseMaxMP: int = ParamField(
        ushort, "baseMp", default=0,
        tooltip="Base amount of maximum MP (unused in Dark Souls).",
    )
    BaseMaxStamina: int = ParamField(
        ushort, "baseSp", default=0,
        tooltip="Base maximum stamina (excluding effects of endurance).",
    )
    ArrowSlot1Count: int = ParamField(
        ushort, "arrowNum", default=0,
        tooltip="Count of arrows equipped in slot 1.",
    )
    BoltSlot1Count: int = ParamField(
        ushort, "boltNum", default=0,
        tooltip="Count of arrows equipped in slot 2.",
    )
    ArrowSlot2Count: int = ParamField(
        ushort, "subArrowNum", default=0,
        tooltip="Count of bolts equipped in slot 1.",
    )
    BoltSlot2Count: int = ParamField(
        ushort, "subBoltNum", default=0,
        tooltip="Count of bolts equipped in slot 2.",
    )
    _Pad1: bytes = ParamPad(6, "pad4[6]")
    Level: int = ParamField(
        short, "soulLv", default=0,
        tooltip="Soul level, independent of actual stats. Determines amount of souls rewarded by human NPCs.",
    )
    Vitality: int = ParamField(
        byte, "baseVit", default=0,
        tooltip="Base vitality level. Determines maximum health.",
    )
    Attunement: int = ParamField(
        byte, "baseWil", default=0,
        tooltip="Base attunement level. Determines spell slots and casting speed.",
    )
    Endurance: int = ParamField(
        byte, "baseEnd", default=0,
        tooltip="Base endurance level. Determines maximum stamina and equip load.",
    )
    Strength: int = ParamField(
        byte, "baseStr", default=0,
        tooltip="Base strength level. Affects strength-based weapons and damage.",
    )
    Dexterity: int = ParamField(
        byte, "baseDex", default=0,
        tooltip="Base dexterity level. Affects skill-based weapons and damage.",
    )
    Intelligence: int = ParamField(
        byte, "baseMag", default=0,
        tooltip="Base intelligence level. Affects magic usability and effectiveness.",
    )
    Faith: int = ParamField(
        byte, "baseFai", default=0,
        tooltip="Base faith level. Affects miracle usability and effectiveness.",
    )
    Luck: int = ParamField(
        byte, "baseLuc", default=0,
        tooltip="Base luck level. Improves chances of rare item drops.",
    )
    Humanity: int = ParamField(
        byte, "baseHeroPoint", default=0,
        tooltip="Base 'soft' humanity.",
    )
    Resistance: int = ParamField(
        byte, "baseDurability", default=0,
        tooltip="Base resistance level. Improves resistances to status ailments.",
    )
    GoodSlot1Count: int = ParamField(
        byte, "itemNum_01", default=0,
        tooltip="Count of good equipped in slot 1.",
    )
    GoodSlot2Count: int = ParamField(
        byte, "itemNum_02", default=0,
        tooltip="Count of good equipped in slot 2.",
    )
    GoodSlot3Count: int = ParamField(
        byte, "itemNum_03", default=0,
        tooltip="Count of good equipped in slot 3.",
    )
    GoodSlot4Count: int = ParamField(
        byte, "itemNum_04", default=0,
        tooltip="Count of good equipped in slot 4.",
    )
    GoodSlot5Count: int = ParamField(
        byte, "itemNum_05", default=0,
        tooltip="Count of good equipped in slot 5.",
    )
    GoodSlot6Count: int = ParamField(
        byte, "itemNum_06", default=0,
        tooltip="Count of good equipped in slot 6.",
    )
    GoodSlot7Count: int = ParamField(
        byte, "itemNum_07", default=0,
        tooltip="Count of good equipped in slot 7.",
    )
    GoodSlot8Count: int = ParamField(
        byte, "itemNum_08", default=0,
        tooltip="Count of good equipped in slot 8.",
    )
    GoodSlot9Count: int = ParamField(
        byte, "itemNum_09", default=0,
        tooltip="Count of good equipped in slot 9.",
    )
    GoodSlot10Count: int = ParamField(
        byte, "itemNum_10", default=0,
        tooltip="Count of good equipped in slot 10.",
    )
    _Pad2: bytes = ParamPad(5, "pad5[5]")
    Gesture1: int = ParamField(
        sbyte, "gestureId0", default=-1,
        tooltip="First equipped gesture.",
    )
    Gesture2: int = ParamField(
        sbyte, "gestureId1", default=-1,
        tooltip="Second equipped gesture.",
    )
    Gesture3: int = ParamField(
        sbyte, "gestureId2", default=-1,
        tooltip="Third equipped gesture.",
    )
    Gesture4: int = ParamField(
        sbyte, "gestureId3", default=-1,
        tooltip="Fourth equipped gesture.",
    )
    Gesture5: int = ParamField(
        sbyte, "gestureId4", default=-1,
        tooltip="Fifth equipped gesture.",
    )
    Gesture6: int = ParamField(
        sbyte, "gestureId5", default=-1,
        tooltip="Sixth equipped gesture.",
    )
    Gesture7: int = ParamField(
        sbyte, "gestureId6", default=-1,
        tooltip="Seventh equipped gesture.",
    )
    CharacterType: int = ParamField(
        byte, "npcPlayerType", NPC_TYPE, default=0,
        tooltip="Type of human NPC.",
    )
    DrawType: int = ParamField(
        sbyte, "npcPlayerDrawType", NPC_DRAW_TYPE, default=0,
        tooltip="Draw type of human NPC.",
    )
    Gender: int = ParamField(
        byte, "npcPlayerSex", CHARACTER_INIT_SEX, default=0,
        tooltip="Character gender.",
    )
    Covenant: int = ParamField(
        byte, "vowType:4", VOW_TYPE, bit_count=4, default=0,
        tooltip="Character covenant.",
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
        int, "equip_Subwep_Right3", game_type=WeaponParam, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipSubwepLeft3: int = ParamField(
        int, "equip_Subwep_Left3", game_type=WeaponParam, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(4, "pad3[4]")
    SecondaryGoodSlot1: int = ParamField(
        int, "secondaryItem_01", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot2: int = ParamField(
        int, "secondaryItem_02", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot3: int = ParamField(
        int, "secondaryItem_03", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot4: int = ParamField(
        int, "secondaryItem_04", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot5: int = ParamField(
        int, "secondaryItem_05", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot6: int = ParamField(
        int, "secondaryItem_06", default=-1,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count1: int = ParamField(
        byte, "secondaryItemNum_01", default=0,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count2: int = ParamField(
        byte, "secondaryItemNum_02", default=0,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count3: int = ParamField(
        byte, "secondaryItemNum_03", default=0,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count4: int = ParamField(
        byte, "secondaryItemNum_04", default=0,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count5: int = ParamField(
        byte, "secondaryItemNum_05", default=0,
        tooltip="TODO",
    )
    SecondaryGoodSlot1Count6: int = ParamField(
        byte, "secondaryItemNum_06", default=0,
        tooltip="TODO",
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
        tooltip="Voice type.",
    )
    _Pad7: bytes = ParamPad(6, "reserve[6]")
