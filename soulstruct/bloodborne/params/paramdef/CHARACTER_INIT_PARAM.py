from __future__ import annotations

__all__ = ["CHARACTER_INIT_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARACTER_INIT_PARAM(ParamRow):
    BaseRecMP: float = ParamField(
        float, "baseRec_mp", default=0.0, hide=True,
        tooltip="Unknown.",
    )
    BaseRecSP: float = ParamField(
        float, "baseRec_sp", default=0.0, hide=True,
        tooltip="Unknown.",
    )
    RedFallDamage: float = ParamField(
        float, "red_Falldam", default=0.0, hide=True,
        tooltip="Unknown.",
    )
    SoulCount: int = ParamField(
        int, "soul", default=0,
        tooltip="Starting soul count of character.",
    )
    RightHandWeapon1: WeaponParam = ParamField(
        int, "equip_Wep_Right", default=-1,
        tooltip="First (default) weapon/shield equipped in right hand.",
    )
    RightHandWeapon2: WeaponParam = ParamField(
        int, "equip_Subwep_Right", default=-1,
        tooltip="Second weapon/shield equipped in right hand.",
    )
    LeftHandWeapon1: WeaponParam = ParamField(
        int, "equip_Wep_Left", default=-1,
        tooltip="First (default) weapon/shield equipped in left hand.",
    )
    LeftHandWeapon2: WeaponParam = ParamField(
        int, "equip_Subwep_Left", default=-1,
        tooltip="Second weapon/shield equipped in left hand.",
    )
    HeadArmor: ArmorParam = ParamField(
        int, "equip_Helm", default=-1,
        tooltip="Armor equipped to head.",
    )
    BodyArmor: ArmorParam = ParamField(
        int, "equip_Armer", default=-1,
        tooltip="Armor equipped to body.",
    )
    HandsArmor: ArmorParam = ParamField(
        int, "equip_Gaunt", default=-1,
        tooltip="Armor equipped to hands.",
    )
    LegsArmor: ArmorParam = ParamField(
        int, "equip_Leg", default=-1,
        tooltip="Armor equipped to legs.",
    )
    ArrowSlot1: WeaponParam = ParamField(
        int, "equip_Arrow", default=-1,
        tooltip="Arrows equipped in slot 1.",
    )
    BoltSlot1: WeaponParam = ParamField(
        int, "equip_Bolt", default=-1,
        tooltip="Bolts equipped in slot 1.",
    )
    ArrowSlot2: WeaponParam = ParamField(
        int, "equip_SubArrow", default=-1,
        tooltip="Arrows equipped in slot 2.",
    )
    BoltSlot2: WeaponParam = ParamField(
        int, "equip_SubBolt", default=-1,
        tooltip="Bolts equipped in slot 2.",
    )
    RingSlot1: AccessoryParam = ParamField(
        int, "equip_Accessory01", default=-1,
        tooltip="First ring equipped. Note that up to five rings can be equipped to human NPCs.",
    )
    RingSlot2: AccessoryParam = ParamField(
        int, "equip_Accessory02", default=-1,
        tooltip="Second ring equipped. Note that up to five rings can be equipped to human NPCs.",
    )
    RingSlot3: AccessoryParam = ParamField(
        int, "equip_Accessory03", default=-1,
        tooltip="Third ring equipped. Note that up to five rings can be equipped to human NPCs.",
    )
    RingSlot4: AccessoryParam = ParamField(
        int, "equip_Accessory04", default=-1,
        tooltip="Fourth ring equipped. Note that up to five rings can be equipped to human NPCs.",
    )
    RingSlot5: AccessoryParam = ParamField(
        int, "equip_Accessory05", default=-1,
        tooltip="Fifth ring equipped. Note that up to five rings can be equipped to human NPCs.",
    )
    SkillSlot1: int = ParamField(
        int, "equip_Skill_01", default=-1, hide=True,
        tooltip="TODO",
    )
    SkillSlot2: int = ParamField(
        int, "equip_Skill_02", default=-1, hide=True,
        tooltip="TODO",
    )
    SkillSlot3: int = ParamField(
        int, "equip_Skill_03", default=-1, hide=True,
        tooltip="TODO",
    )
    SpellSlot1: SpellParam = ParamField(
        int, "equip_Spell_01", default=-1,
        tooltip="First spell equipped.",
    )
    SpellSlot2: SpellParam = ParamField(
        int, "equip_Spell_02", default=-1,
        tooltip="Second spell equipped.",
    )
    SpellSlot3: SpellParam = ParamField(
        int, "equip_Spell_03", default=-1,
        tooltip="Third spell equipped.",
    )
    SpellSlot4: SpellParam = ParamField(
        int, "equip_Spell_04", default=-1,
        tooltip="Fourth spell equipped.",
    )
    SpellSlot5: SpellParam = ParamField(
        int, "equip_Spell_05", default=-1,
        tooltip="Fifth spell equipped.",
    )
    SpellSlot6: SpellParam = ParamField(
        int, "equip_Spell_06", default=-1,
        tooltip="Sixth spell equipped.",
    )
    SpellSlot7: SpellParam = ParamField(
        int, "equip_Spell_07", default=-1,
        tooltip="Seventh spell equipped.",
    )
    GoodSlot1: GoodParam = ParamField(
        int, "item_01", default=-1,
        tooltip="Good (item) equipped in slot 1.",
    )
    GoodSlot2: GoodParam = ParamField(
        int, "item_02", default=-1,
        tooltip="Good (item) equipped in slot 2.",
    )
    GoodSlot3: GoodParam = ParamField(
        int, "item_03", default=-1,
        tooltip="Good (item) equipped in slot 3.",
    )
    GoodSlot4: GoodParam = ParamField(
        int, "item_04", default=-1,
        tooltip="Good (item) equipped in slot 4.",
    )
    GoodSlot5: GoodParam = ParamField(
        int, "item_05", default=-1,
        tooltip="Good (item) equipped in slot 5.",
    )
    GoodSlot6: GoodParam = ParamField(
        int, "item_06", default=-1,
        tooltip="Good (item) equipped in slot 6.",
    )
    GoodSlot7: GoodParam = ParamField(
        int, "item_07", default=-1,
        tooltip="Good (item) equipped in slot 7.",
    )
    GoodSlot8: GoodParam = ParamField(
        int, "item_08", default=-1,
        tooltip="Good (item) equipped in slot 8.",
    )
    GoodSlot9: GoodParam = ParamField(
        int, "item_09", default=-1,
        tooltip="Good (item) equipped in slot 9.",
    )
    GoodSlot10: GoodParam = ParamField(
        int, "item_10", default=-1,
        tooltip="Good (item) equipped in slot 10.",
    )
    FaceID: FaceParam = ParamField(
        int, "npcPlayerFaceGenId", default=0,
        tooltip="Face parameter ID (NPCs only).",
    )
    DefaultAI: AIParam = ParamField(
        int, "npcPlayerThinkId", default=0,
        tooltip="Default AI (NPCs only).",
    )
    BaseMaxHP: int = ParamField(
        ushort, "baseHp", default=0,
        tooltip="Base amount of maximum HP (excluding effects of vitality).",
    )
    BaseMaxMP: int = ParamField(
        ushort, "baseMp", default=0, hide=True,
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
    QWC_SB: int = ParamField(
        short, "QWC_sb", default=0, hide=True,
        tooltip="Unknown. Likely to be unused world tendency effect.",
    )
    QWC_MW: int = ParamField(
        short, "QWC_mw", default=0, hide=True,
        tooltip="Unknown. Likely to be unused world tendency effect.",
    )
    QWC_CD: int = ParamField(
        short, "QWC_cd", default=0, hide=True,
        tooltip="Unknown. Likely to be unused world tendency effect.",
    )
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
    HeadScale: int = ParamField(
        sbyte, "bodyScaleHead", default=0,
        tooltip="Multiplier applied to head size.",
    )
    ChestScale: int = ParamField(
        sbyte, "bodyScaleBreast", default=0,
        tooltip="Multiplier applied to chest size.",
    )
    AbdomenScale: int = ParamField(
        sbyte, "bodyScaleAbdomen", default=0,
        tooltip="Multiplier applied to abdomen size.",
    )
    ArmScale: int = ParamField(
        sbyte, "bodyScaleArm", default=0,
        tooltip="Multiplier applied to arm size.",
    )
    LegScale: int = ParamField(
        sbyte, "bodyScaleLeg", default=0,
        tooltip="Multiplier applied to leg size.",
    )
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
    CharacterType: NPC_TYPE = ParamField(
        byte, "npcPlayerType", default=0,
        tooltip="Type of human NPC.",
    )
    DrawType: NPC_DRAW_TYPE = ParamField(
        byte, "npcPlayerDrawType", default=0,
        tooltip="Draw type of human NPC.",
    )
    Gender: CHARACTER_INIT_SEX = ParamField(
        byte, "npcPlayerSex", default=0,
        tooltip="Character gender.",
    )
    Covenant: CHRINIT_VOW_TYPE = ParamField(
        byte, "vowType:4", bit_count=4, default=0,
        tooltip="Character covenant.",
    )
    _BitPad0: int = ParamBitPad(byte, "pad:4", bit_count=4)
    VoiceType: int = ParamField(
        byte, "voiceType", default=0,
        tooltip="Voice type.",
    )
    _Pad0: bytes = ParamPad(1, "pad0[1]")
    RightHandWeapon1GenID: int = ParamField(
        int, "equip_Wep_Right_GenId", default=-1,
        tooltip="TODO",
    )
    RightHandWeapon2GenID: int = ParamField(
        int, "equip_Subwep_Right_GenId", default=-1,
        tooltip="TODO",
    )
    LeftHandWeapon1GenID: int = ParamField(
        int, "equip_Wep_Left_GenId", default=-1,
        tooltip="TODO",
    )
    LeftHandWeapon2GenID: int = ParamField(
        int, "equip_Subwep_Left_GenId", default=-1,
        tooltip="TODO",
    )
    HeadArmorGenID: int = ParamField(
        int, "equip_Helm_GenId", default=-1,
        tooltip="TODO",
    )
    BodyArmorGenID: int = ParamField(
        int, "equip_Armer_GenId", default=-1,
        tooltip="TODO",
    )
    HandsArmorGenID: int = ParamField(
        int, "equip_Gaunt_GenId", default=-1,
        tooltip="TODO",
    )
    LegsArmorGenID: int = ParamField(
        int, "equip_Leg_GenId", default=-1,
        tooltip="TODO",
    )
    BodyWeaponGenID: int = ParamField(
        int, "equip_Wep_Body_GenId", default=-1,
        tooltip="TODO",
    )
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
    _Pad1: bytes = ParamPad(2, "pad1[2]")
