__all__ = ["CHARACTER_INIT_PARAM", "NPC_PARAM_ST", "CACL_CORRECT_GRAPH_ST"]

from soulstruct.game_types import *
from soulstruct.params.darksouls1ptde.enums import *
from soulstruct.params.core import FieldDisplayInfo, pad_field, bit_pad_field

CHARACTER_INIT_PARAM = {
    "internal_name": "CHARACTER_INIT_PARAM",
    "file_name": "CharaInitParam",
    "nickname": "Players",
    "fields": [
        FieldDisplayInfo("baseRec_mp", "BaseRecMP", False, float, "Unknown."),
        FieldDisplayInfo("baseRec_sp", "BaseRecSP", False, float, "Unknown."),
        FieldDisplayInfo("red_Falldam", "RedFallDamage", False, float, "Unknown."),
        FieldDisplayInfo("soul", "SoulCount", True, int, "Starting soul count of character."),
        FieldDisplayInfo(
            "equip_Wep_Right",
            "RightHandWeapon1",
            True,
            WeaponParam,
            "First (default) weapon/shield equipped in right hand.",
        ),
        FieldDisplayInfo(
            "equip_Subwep_Right",
            "RightHandWeapon2",
            True,
            WeaponParam,
            "Second weapon/shield equipped in right hand.",
        ),
        FieldDisplayInfo(
            "equip_Wep_Left",
            "LeftHandWeapon1",
            True,
            WeaponParam,
            "First (default) weapon/shield equipped in left hand.",
        ),
        FieldDisplayInfo(
            "equip_Subwep_Left",
            "LeftHandWeapon2",
            True,
            WeaponParam,
            "Second weapon/shield equipped in left hand.",
        ),
        FieldDisplayInfo("equip_Helm", "HeadArmor", True, ArmorParam, "Armor equipped to head."),
        FieldDisplayInfo("equip_Armer", "BodyArmor", True, ArmorParam, "Armor equipped to body."),
        FieldDisplayInfo("equip_Gaunt", "HandsArmor", True, ArmorParam, "Armor equipped to hands."),
        FieldDisplayInfo("equip_Leg", "LegsArmor", True, ArmorParam, "Armor equipped to legs."),
        FieldDisplayInfo("equip_Arrow", "ArrowSlot1", True, WeaponParam, "Arrows equipped in slot 1."),
        FieldDisplayInfo("equip_Bolt", "BoltSlot1", True, WeaponParam, "Bolts equipped in slot 1."),
        FieldDisplayInfo("equip_SubArrow", "ArrowSlot2", True, WeaponParam, "Arrows equipped in slot 2."),
        FieldDisplayInfo("equip_SubBolt", "BoltSlot2", True, WeaponParam, "Bolts equipped in slot 2."),
        FieldDisplayInfo(
            "equip_Accessory01",
            "RingSlot1",
            True,
            RingParam,
            "First ring equipped. Note that up to five rings can be equipped to human NPCs.",
        ),
        FieldDisplayInfo(
            "equip_Accessory02",
            "RingSlot2",
            True,
            RingParam,
            "Second ring equipped. Note that up to five rings can be equipped to human NPCs.",
        ),
        FieldDisplayInfo(
            "equip_Accessory03",
            "RingSlot3",
            True,
            RingParam,
            "Third ring equipped. Note that up to five rings can be equipped to human NPCs.",
        ),
        FieldDisplayInfo(
            "equip_Accessory04",
            "RingSlot4",
            True,
            RingParam,
            "Fourth ring equipped. Note that up to five rings can be equipped to human NPCs.",
        ),
        FieldDisplayInfo(
            "equip_Accessory05",
            "RingSlot5",
            True,
            RingParam,
            "Fifth ring equipped. Note that up to five rings can be equipped to human NPCs.",
        ),
        FieldDisplayInfo("equip_Skill_01", "SkillSlot1", False, int, ""),
        FieldDisplayInfo("equip_Skill_02", "SkillSlot2", False, int, ""),
        FieldDisplayInfo("equip_Skill_03", "SkillSlot3", False, int, ""),
        FieldDisplayInfo("equip_Spell_01", "SpellSlot1", True, SpellParam, "First spell equipped."),
        FieldDisplayInfo("equip_Spell_02", "SpellSlot2", True, SpellParam, "Second spell equipped."),
        FieldDisplayInfo("equip_Spell_03", "SpellSlot3", True, SpellParam, "Third spell equipped."),
        FieldDisplayInfo("equip_Spell_04", "SpellSlot4", True, SpellParam, "Fourth spell equipped."),
        FieldDisplayInfo("equip_Spell_05", "SpellSlot5", True, SpellParam, "Fifth spell equipped."),
        FieldDisplayInfo("equip_Spell_06", "SpellSlot6", True, SpellParam, "Sixth spell equipped."),
        FieldDisplayInfo("equip_Spell_07", "SpellSlot7", True, SpellParam, "Seventh spell equipped."),
        FieldDisplayInfo("item_01", "GoodSlot1", True, GoodParam, "Good (item) equipped in slot 1."),
        FieldDisplayInfo("item_02", "GoodSlot2", True, GoodParam, "Good (item) equipped in slot 2."),
        FieldDisplayInfo("item_03", "GoodSlot3", True, GoodParam, "Good (item) equipped in slot 3."),
        FieldDisplayInfo("item_04", "GoodSlot4", True, GoodParam, "Good (item) equipped in slot 4."),
        FieldDisplayInfo("item_05", "GoodSlot5", True, GoodParam, "Good (item) equipped in slot 5."),
        FieldDisplayInfo("item_06", "GoodSlot6", True, GoodParam, "Good (item) equipped in slot 6."),
        FieldDisplayInfo("item_07", "GoodSlot7", True, GoodParam, "Good (item) equipped in slot 7."),
        FieldDisplayInfo("item_08", "GoodSlot8", True, GoodParam, "Good (item) equipped in slot 8."),
        FieldDisplayInfo("item_09", "GoodSlot9", True, GoodParam, "Good (item) equipped in slot 9."),
        FieldDisplayInfo("item_10", "GoodSlot10", True, GoodParam, "Good (item) equipped in slot 10."),
        FieldDisplayInfo("npcPlayerFaceGenId", "FaceID", True, FaceParam, "Face parameter ID (NPCs only)."),
        FieldDisplayInfo("npcPlayerThinkId", "DefaultAI", True, AIParam, "Default AI (NPCs only)."),
        FieldDisplayInfo("baseHp", "BaseMaxHP", True, int, "Base amount of maximum HP (excluding effects of vitality)."),
        FieldDisplayInfo("baseMp", "BaseMaxMP", False, int, "Base amount of maximum MP (unused in Dark Souls)."),
        FieldDisplayInfo("baseSp", "BaseMaxStamina", True, int, "Base maximum stamina (excluding effects of endurance)."),
        FieldDisplayInfo("arrowNum", "ArrowSlot1Count", True, int, "Count of arrows equipped in slot 1."),
        FieldDisplayInfo("boltNum", "BoltSlot1Count", True, int, "Count of arrows equipped in slot 2."),
        FieldDisplayInfo("subArrowNum", "ArrowSlot2Count", True, int, "Count of bolts equipped in slot 1."),
        FieldDisplayInfo("subBoltNum", "BoltSlot2Count", True, int, "Count of bolts equipped in slot 2."),
        FieldDisplayInfo("QWC_sb", "QWC_SB", False, int, "Unknown. Likely to be unused world tendency effect."),
        FieldDisplayInfo("QWC_mw", "QWC_MW", False, int, "Unknown. Likely to be unused world tendency effect."),
        FieldDisplayInfo("QWC_cd", "QWC_CD", False, int, "Unknown. Likely to be unused world tendency effect."),
        FieldDisplayInfo(
            "soulLv",
            "SoulLevel",
            True,
            int,
            "Soul level, independent of actual stats. Determines amount of souls rewarded by human NPCs.",
        ),
        FieldDisplayInfo("baseVit", "Vitality", True, int, "Base vitality level. Determines maximum health."),
        FieldDisplayInfo(
            "baseWil", "Attunement", True, int, "Base attunement level. Determines spell slots and casting speed."
        ),
        FieldDisplayInfo(
            "baseEnd", "Endurance", True, int, "Base endurance level. Determines maximum stamina and equip load."
        ),
        FieldDisplayInfo(
            "baseStr", "Strength", True, int, "Base strength level. Affects strength-based weapons and damage."
        ),
        FieldDisplayInfo(
            "baseDex", "Dexterity", True, int, "Base dexterity level. Affects skill-based weapons and damage."
        ),
        FieldDisplayInfo(
            "baseMag",
            "Intelligence",
            True,
            int,
            "Base intelligence level. Affects magic usability and effectiveness.",
        ),
        FieldDisplayInfo("baseFai", "Faith", True, int, "Base faith level. Affects miracle usability and effectiveness."),
        FieldDisplayInfo("baseLuc", "Luck", True, int, "Base luck level. Improves chances of rare item drops."),
        FieldDisplayInfo("baseHeroPoint", "Humanity", True, int, "Base 'soft' humanity."),
        FieldDisplayInfo(
            "baseDurability",
            "Resistance",
            True,
            int,
            "Base resistance level. Improves resistances to status ailments.",
        ),
        FieldDisplayInfo("itemNum_01", "GoodSlot1Count", True, int, "Count of good equipped in slot 1."),
        FieldDisplayInfo("itemNum_02", "GoodSlot2Count", True, int, "Count of good equipped in slot 2."),
        FieldDisplayInfo("itemNum_03", "GoodSlot3Count", True, int, "Count of good equipped in slot 3."),
        FieldDisplayInfo("itemNum_04", "GoodSlot4Count", True, int, "Count of good equipped in slot 4."),
        FieldDisplayInfo("itemNum_05", "GoodSlot5Count", True, int, "Count of good equipped in slot 5."),
        FieldDisplayInfo("itemNum_06", "GoodSlot6Count", True, int, "Count of good equipped in slot 6."),
        FieldDisplayInfo("itemNum_07", "GoodSlot7Count", True, int, "Count of good equipped in slot 7."),
        FieldDisplayInfo("itemNum_08", "GoodSlot8Count", True, int, "Count of good equipped in slot 8."),
        FieldDisplayInfo("itemNum_09", "GoodSlot9Count", True, int, "Count of good equipped in slot 9."),
        FieldDisplayInfo("itemNum_10", "GoodSlot10Count", True, int, "Count of good equipped in slot 10."),
        FieldDisplayInfo("bodyScaleHead", "HeadScale", True, int, "Multiplier applied to head size."),
        FieldDisplayInfo("bodyScaleBreast", "ChestScale", True, int, "Multiplier applied to chest size."),
        FieldDisplayInfo("bodyScaleAbdomen", "AbdomenScale", True, int, "Multiplier applied to abdomen size."),
        FieldDisplayInfo("bodyScaleArm", "ArmScale", True, int, "Multiplier applied to arm size."),
        FieldDisplayInfo("bodyScaleLeg", "LegScale", True, int, "Multiplier applied to leg size."),
        FieldDisplayInfo("gestureId0", "Gesture1", True, int, "First equipped gesture."),
        FieldDisplayInfo("gestureId1", "Gesture2", True, int, "Second equipped gesture."),
        FieldDisplayInfo("gestureId2", "Gesture3", True, int, "Third equipped gesture."),
        FieldDisplayInfo("gestureId3", "Gesture4", True, int, "Fourth equipped gesture."),
        FieldDisplayInfo("gestureId4", "Gesture5", True, int, "Fifth equipped gesture."),
        FieldDisplayInfo("gestureId5", "Gesture6", True, int, "Sixth equipped gesture."),
        FieldDisplayInfo("gestureId6", "Gesture7", True, int, "Seventh equipped gesture."),
        FieldDisplayInfo("npcPlayerType", "CharacterType", True, NPC_TYPE, "Type of human NPC."),
        FieldDisplayInfo("npcPlayerDrawType", "DrawType", True, NPC_DRAW_TYPE, "Draw type of human NPC."),
        FieldDisplayInfo("npcPlayerSex", "Gender", True, CHARACTER_INIT_SEX, "Character gender."),
        FieldDisplayInfo("vowType:4", "Covenant", True, CHRINIT_VOW_TYPE, "Character covenant."),
        FieldDisplayInfo("pad:4", "Pad0", False, bit_pad_field(4), "Null padding."),
        FieldDisplayInfo("pad0[10]", "Pad1", False, pad_field(10), "Null padding."),
    ],
}

NPC_PARAM_ST = {
    "paramdef_name": "NPC_PARAM_ST",
    "file_name": "NpcParam",
    "nickname": "Characters",
    "fields": [
        FieldDisplayInfo(
            "behaviorVariationId",
            "BehaviorVariationID",
            True,
            int,
            "Multiplied by 1000 and added to non-player behavior lookups (hitboxes, bullets) triggered by TAE.",
        ),
        FieldDisplayInfo(
            "aiThinkId", "DefaultAI", True, AIParam, "Default AI ID. Overridden by AI ID field in Maps entry."
        ),
        FieldDisplayInfo(
            "nameId",
            "NameID",
            True,
            NPCName,
            "Text ID for NPC name that appears attached to NPCs. Only works for invaders and summons.",
        ),
        FieldDisplayInfo(
            "turnVellocity", "TurnVelocity", True, float, "Turning velocity of NPC. (Exact effect needs testing.)"
        ),
        FieldDisplayInfo("hitHeight", "HitHeight", True, float, "Height of NPC hitbox for collision."),
        FieldDisplayInfo("hitRadius", "HitRadius", True, float, "Radius of NPC hitbox for collision."),
        FieldDisplayInfo("weight", "Weight", False, int, "Weight of NPC. Probably has no effect (generall 100)."),
        FieldDisplayInfo("hitYOffset", "HitYOffset", False, float, "Vertical offset of NPC hitbox for collision."),
        FieldDisplayInfo("hp", "MaximumHP", True, int, "Maximum HP of NPC."),
        FieldDisplayInfo("mp", "MaximumMP", False, int, "Maximum MP of NPC. Not used in Dark Souls (generally zero)."),
        FieldDisplayInfo(
            "getSoul", "SoulReward", True, int, "Amount of souls (before NG+ scaling) rewarded when NPC is killed."
        ),
        FieldDisplayInfo(
            "itemLotId_1",
            "ItemLotID1",
            True,
            ItemLotParam,
            "First item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "itemLotId_2",
            "ItemLotID2",
            True,
            ItemLotParam,
            "Second item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "itemLotId_3",
            "ItemLotID3",
            True,
            ItemLotParam,
            "Third item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "itemLotId_4",
            "ItemLotID4",
            True,
            ItemLotParam,
            "Fourth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "itemLotId_5",
            "ItemLotID5",
            True,
            ItemLotParam,
            "Fifth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "itemLotId_6",
            "ItemLotID6",
            True,
            ItemLotParam,
            "Sixth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        FieldDisplayInfo(
            "humanityLotId",
            "HumanityLotID",
            True,
            Flag,
            "Starting flag of counter for awarding random humanity (I think). Only used by a few enemies, "
            "such as Hollows and Mass of Souls.",
        ),
        FieldDisplayInfo(
            "spEffectID0",
            "SpecialEffectID0",
            True,
            SpecialEffectParam,
            "First passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 5300-5337 range, which modify enemy damage animations (e.g. so bosses stagger less).",
        ),
        FieldDisplayInfo(
            "spEffectID1",
            "SpecialEffectID1",
            True,
            SpecialEffectParam,
            "Second passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 5360-5364 range, which further modify enemy damage animations based on poise.",
        ),
        FieldDisplayInfo(
            "spEffectID2",
            "SpecialEffectID2",
            True,
            SpecialEffectParam,
            "Third passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 90000-91111 range, which determine status effect immunities. From left to right, "
            "the four binary digits represent poison, toxic, bleed, and curse. 0 means the NPC is immune to that "
            "status, and 1 means they are not immune (though their resistance could be any value).",
        ),
        FieldDisplayInfo(
            "spEffectID3",
            "SpecialEffectID3",
            True,
            SpecialEffectParam,
            "Fourth passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 80000-81111 range, which determine immunities to effects that apparently never made it into "
            "the game ('remnant', 'absorption', 'fascination', and 'ineffective').",
        ),
        FieldDisplayInfo(
            "spEffectID4",
            "SpecialEffectID4",
            True,
            SpecialEffectParam,
            "Fifth passive special effect that is active on NPC.\n\nThis slot is generally reserved for "
            "'levelling' effects in the 7000-7015 range, which scale enemy stats according to the map they are "
            "found in.",
        ),
        FieldDisplayInfo(
            "spEffectID5",
            "SpecialEffectID5",
            True,
            SpecialEffectParam,
            "Sixth passive special effect that is active on NPC.\n\nUsed for miscellaneous effects, "
            "such as elemental resistance or immunity, animation offset effects, the black phantom effect (7100), "
            "etc.",
        ),
        FieldDisplayInfo(
            "spEffectID6",
            "SpecialEffectID6",
            True,
            SpecialEffectParam,
            "Seventh passive special effect that is active on NPC.\n\nUsed for miscellaneous effects, "
            "such as elemental resistance or immunity, animation offset effects, the black phantom effect (7100), "
            "etc.",
        ),
        FieldDisplayInfo(
            "spEffectID7",
            "SpecialEffectID7",
            True,
            SpecialEffectParam,
            "Eighth passive special effect that is active on NPC.\n\nThis slot is generally reserved for effect "
            "71100, 71110, or 71111. The fourth binary digit determines if the NPC uses the 'immortal system'; "
            "the third binary digit is unknown. Darkwraiths, Hollows, Humanity Phantoms, and Armored Tusks are "
            "some examples of the few NPCs that use 71111; most others use 71110, except bosses.",
        ),
        FieldDisplayInfo(
            "GameClearSpEffectID",
            "NewGamePlusSpecialEffect",
            True,
            SpecialEffectParam,
            "Passive special effect that is only applied to the NPC in NG+ and beyond, which are taken from the "
            "range 7401-7415.",
        ),
        FieldDisplayInfo(
            "physGuardCutRate",
            "PhysicalGuardCutRate",
            True,
            float,
            "Percentage reduction in physical damage taken while NPC is guarding.",
        ),
        FieldDisplayInfo(
            "magGuardCutRate",
            "MagicGuardCutRate",
            True,
            float,
            "Percentage reduction in magic damage taken while NPC is guarding.",
        ),
        FieldDisplayInfo(
            "fireGuardCutRate",
            "FireGuardCutRate",
            True,
            float,
            "Percentage reduction in fire damage taken while NPC is guarding.",
        ),
        FieldDisplayInfo(
            "thunGuardCutRate",
            "LightningGuardCutRate",
            True,
            float,
            "Percentage reduction in lightning damage taken while NPC is guarding.",
        ),
        FieldDisplayInfo(
            "animIdOffset",
            "AnimationIDOffset",
            True,
            int,
            "Offset added to animation requests (e.g. from AI script or event script). If the offset animation is "
            "missing, the original will be used.",
        ),
        # TODO: Animation types.
        FieldDisplayInfo("moveAnimId", "MoveAnimationID", False, int, ""),
        FieldDisplayInfo("spMoveAnimId1", "SpecialMoveAnimationID1", False, int, ""),
        FieldDisplayInfo("spMoveAnimId2", "SpecialMoveAnimationID2", False, int, ""),
        FieldDisplayInfo("networkWarpDist", "NetworkWarpDistance", False, float, ""),
        FieldDisplayInfo("dbgBehaviorR1", "DebugBehaviorR1", False, int, ""),
        FieldDisplayInfo("dbgBehaviorL1", "DebugBehaviorL1", False, int, ""),
        FieldDisplayInfo("dbgBehaviorR2", "DebugBehaviorR2", False, int, ""),
        FieldDisplayInfo("dbgBehaviorL2", "DebugBehaviorL2", False, int, ""),
        FieldDisplayInfo("dbgBehaviorRL", "DebugBehaviorRL", False, int, ""),
        FieldDisplayInfo("dbgBehaviorRR", "DebugBehaviorRR", False, int, ""),
        FieldDisplayInfo("dbgBehaviorRD", "DebugBehaviorRD", False, int, ""),
        FieldDisplayInfo("dbgBehaviorRU", "DebugBehaviorRU", False, int, ""),
        FieldDisplayInfo("dbgBehaviorLL", "DebugBehaviorLL", False, int, ""),
        FieldDisplayInfo("dbgBehaviorLR", "DebugBehaviorLR", False, int, ""),
        FieldDisplayInfo("dbgBehaviorLD", "DebugBehaviorLD", False, int, ""),
        FieldDisplayInfo("dbgBehaviorLU", "DebugBehaviorLU", False, int, ""),
        FieldDisplayInfo("animIdOffset2", "AnimationIDOffset2", False, int, ""),
        FieldDisplayInfo(
            "partsDamageRate1",
            "Part1DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 1 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate2",
            "Part2DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 2 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate3",
            "Part3DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 3 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate4",
            "Part4DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 4 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate5",
            "Part5DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 5 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate6",
            "Part6DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 6 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate7",
            "Part7DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 7 of NPC model.",
        ),
        FieldDisplayInfo(
            "partsDamageRate8",
            "Part8DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 8 of NPC model.",
        ),
        FieldDisplayInfo(
            "weakPartsDamageRate",
            "WeakPartsDamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by weak parts of NPC model.",
        ),
        FieldDisplayInfo(
            "superArmorRecoverCorrection",
            "PoiseRecoveryCorrection",
            True,
            float,
            "Change to poise recovery rate. Only the Chained Prisoner uses a non-zero value in vanilla(-0.2).",
        ),
        FieldDisplayInfo(
            "superArmorBrakeKnockbackDist",
            "StaggerKnockbackDistance",
            True,
            float,
            "Stagger knockback distance when NPC's poise is broken.",
        ),
        FieldDisplayInfo("stamina", "MaxStamina", True, int, "Maximum stamina of NPC."),
        FieldDisplayInfo(
            "staminaRecoverBaseVel", "StaminaRecoveryBaseSpeed", True, int, "Base speed of NPC's stamina recovery."
        ),
        FieldDisplayInfo("def_phys", "PhysicalDefense", True, int, "Base defense applied to all physical attacks."),
        FieldDisplayInfo("def_slash", "SlashDefense", True, int, "Base defense added against slashing physical attacks."),
        FieldDisplayInfo("def_blow", "StrikeDefense", True, int, "Base defense added against striking physical attacks."),
        FieldDisplayInfo(
            "def_thrust", "ThrustDefense", True, int, "Base defense added against thrusting physical attacks."
        ),
        FieldDisplayInfo("def_mag", "MagicDefense", True, int, "Base defense added against magic attacks."),
        FieldDisplayInfo("def_fire", "FireDefense", True, int, "Base defense added against fire attacks."),
        FieldDisplayInfo("def_thunder", "LightningDefense", True, int, "Base defense added against lightning attacks."),
        FieldDisplayInfo(
            "defFlickPower",
            "DefenseRepelPower",
            False,
            int,
            "Determines how severely an attacker is repelled when they fail to break this NPC's poise. The "
            "Armored Tusk and Chained Prisoner have very high values (50-60), but most NPCs have 0.",
        ),
        FieldDisplayInfo("resist_poison", "PoisonResistance", True, int, "Base poison resistance."),
        FieldDisplayInfo("resist_desease", "ToxicResistance", True, int, "Base toxic resistance."),
        FieldDisplayInfo("resist_blood", "BleedResistance", True, int, "Base bleed resistance."),
        FieldDisplayInfo("resist_curse", "CurseResistance", True, int, "Base curse resistance."),
        FieldDisplayInfo(
            "ghostModelId",
            "GhostModelID",
            False,
            int,
            "Model to be used when this quest-related NPC appears as a ghost to other players. Defaults to -1 for "
            "almost all standard enemies, which means they do not appear as a ghost to others.",
        ),
        FieldDisplayInfo("normalChangeResouceId", "NormalChangeResourceID", False, int, "Unknown. Always -1."),
        FieldDisplayInfo("guardAngle", "GuardAngle", False, int, "Zero for every NPC except the Phalanx Hollow (20)."),
        FieldDisplayInfo("slashGuardCutRate", "SlashDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo("blowGuardCutRate", "StrikeDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo("thrustGuardCutRate", "ThrustDamageReductionWhenGuarding", False, int, "Always zero."),
        FieldDisplayInfo(
            "superArmorDurability",
            "MaxPoise",
            True,
            int,
            "Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, "
            "the character will be staggered.",
        ),
        FieldDisplayInfo(
            "normalChangeTexChrId",
            "NormalChangeTextureChrID",
            False,
            int,
            "Unknown. Used for only some NPCs, where it is generally set to a number close to the NPC's character "
            "model ID.",
        ),
        FieldDisplayInfo(
            "dropType",
            "ItemDropAppearance",
            True,
            NPC_ITEMDROP_TYPE,
            "Determines appearance of dropped items. 0 means the item appears to glow faintly from inside the "
            "NPC's body (e.g. Rat, Mushroom Child/Parent, Ent) and 1 means the item is a clear white orb just "
            "like regular treasure on corpses (most NPCs).",
        ),
        FieldDisplayInfo("knockbackRate", "KnockbackRate", True, int, ""),
        FieldDisplayInfo(
            "knockbackParamId",
            "KnockbackID",
            True,
            int,
            "Knockback parameters were abandoned after Demons' Souls. A param table for Knockback is still present "
            "but is not accessible in the GUI.",
        ),
        FieldDisplayInfo("fallDamageDump", "FallDamageReduction", True, int, "Percentage of fall damage to ignore."),
        FieldDisplayInfo(
            "staminaGuardDef",
            "StaminaGuardDefense",
            True,
            int,
            "Always set to zero in the game, but presumably, increasing it will reduce the amount of stamina lost "
            "when this NPC blocks an attack.",
        ),
        FieldDisplayInfo("pcAttrB", "PCAttrB", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("pcAttrW", "PCAttrW", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("pcAttrL", "PCAttrL", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("pcAttrR", "PCAttrR", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("areaAttrB", "AreaAttrB", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("areaAttrW", "AreaAttrW", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("areaAttrL", "AreaAttrL", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo("areaAttrR", "AreaAttrR", False, int, "Like a remnant of World Tendency. Always set to zero."),
        FieldDisplayInfo(
            "mpRecoverBaseVel",
            "MPRecoveryBaseSpeed",
            False,
            int,
            "Unknown effect, likely none. Set to zero for NPC parts (tails and Hydra heads) and 10 for everyone "
            "else.",
        ),
        FieldDisplayInfo(
            "flickDamageCutRate",
            "RepelDamageCutRate",
            False,
            int,
            "Unknown effect, but it is set to zero for most enemies, 50 for very heavy enemies like Great Stone "
            "Knights and Titanite Demons, and 100 for Mimics.",
        ),
        FieldDisplayInfo(
            "defaultLodParamId", "DefaultLightingParamID", False, int, "Default lighting (Lod) parameter entry ID."
        ),
        FieldDisplayInfo("drawType", "DrawType", True, NPC_DRAW_TYPE, ""),
        FieldDisplayInfo("npcType", "CharacterType", True, NPC_TYPE, ""),
        FieldDisplayInfo(
            "teamType", "TeamType", True, NPC_TEMA_TYPE, "0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom"
        ),
        FieldDisplayInfo("moveType", "MoveType", True, NPC_MOVE_TYPE, ""),
        FieldDisplayInfo("lockDist", "LockOnDistance", True, int, ""),
        FieldDisplayInfo("material", "Material", False, int, ""),
        FieldDisplayInfo("materialSfx", "MaterialSFX", False, int, ""),
        FieldDisplayInfo("material_Weak", "MaterialWeak", False, int, ""),
        FieldDisplayInfo("materialSfx_Weak", "MaterialWeakSFX", False, int, ""),
        FieldDisplayInfo(
            "partsDamageType",
            "PartsDamageType",
            False,
            int,
            "Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, Seath, "
            "Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise.",
        ),
        FieldDisplayInfo(
            "maxUndurationAng",
            "MaxUndurationAngle",
            False,
            int,
            "Unknown effect, but it is generally set to 30 for all four-legged enemies, and 0 for all others.",
        ),
        FieldDisplayInfo(
            "guardLevel",
            "GuardLevel",
            False,
            GUARDMOTION_CATEGORY,
            "Set to 4 for enemies who can guard (including Manus), except Giant Skeletons, who have a value of 3. "
            "All other NPCs have zero.",
        ),
        FieldDisplayInfo(
            "burnSfxType",
            "BurnSFXType",
            False,
            NPC_BURN_TYPE,
            "Set to 1 for Slimes and Undead Dragons, and 0 for everyone else.",
        ),
        FieldDisplayInfo(
            "poisonGuardResist", "PoisonGuardResistance", True, int, "Added poison resistance while guarding."
        ),
        FieldDisplayInfo(
            "diseaseGuardResist", "ToxicGuardResistance", True, int, "Added toxic resistance while guarding."
        ),
        FieldDisplayInfo("bloodGuardResist", "BleedGuardResistance", True, int, "Added bleed resistance while guarding."),
        FieldDisplayInfo("curseGuardResist", "CurseGuardResistance", True, int, "Added curse resistance while guarding."),
        FieldDisplayInfo("parryAttack", "ParryAttack", False, int, "Always zero."),
        FieldDisplayInfo("parryDefence", "ParryDefense", False, int, "Always zero."),
        FieldDisplayInfo(
            "sfxSize",
            "SFXSize",
            False,
            NPC_SFX_SIZE,
            "Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise.",
        ),
        FieldDisplayInfo("pushOutCamRegionRadius", "PushOutCameraRegionRadius", False, int, "Always zero."),
        FieldDisplayInfo(
            "hitStopType",
            "HitStopType",
            False,
            NPC_HITSTOP_TYPE,
            "Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely related to AI triggers.",
        ),
        FieldDisplayInfo(
            "ladderEndChkOffsetTop", "LadderEndCheckOffsetTop", False, int, "Not something you want to mess with."
        ),
        FieldDisplayInfo(
            "ladderEndChkOffsetLow",
            "LadderEndCheckOffsetBottom",
            False,
            int,
            "Not something you want to mess with.",
        ),
        FieldDisplayInfo("useRagdollCamHit:1", "UseRagdollCameraHit", False, bool, ""),
        FieldDisplayInfo("disableClothRigidHit:1", "DisableClothRigidHit", False, bool, ""),
        FieldDisplayInfo("useRagdoll:1", "UseRagdoll", False, bool, ""),
        FieldDisplayInfo("isDemon:1", "IsDemon", True, bool, ""),
        FieldDisplayInfo("isGhost:1", "IsGhost", True, bool, ""),
        FieldDisplayInfo("isNoDamageMotion:1", "IsNoDamageMotion", True, bool, ""),
        FieldDisplayInfo("isUnduration:1", "IsUnduration", False, bool, ""),
        FieldDisplayInfo("isChangeWanderGhost:1", "IsChangeWanderGhost", False, bool, "Always false."),
        FieldDisplayInfo("modelDispMask0:1", "ModelDisplayMask0", False, bool, ""),
        FieldDisplayInfo("modelDispMask1:1", "ModelDisplayMask1", False, bool, ""),
        FieldDisplayInfo("modelDispMask2:1", "ModelDisplayMask2", False, bool, ""),
        FieldDisplayInfo("modelDispMask3:1", "ModelDisplayMask3", False, bool, ""),
        FieldDisplayInfo("modelDispMask4:1", "ModelDisplayMask4", False, bool, ""),
        FieldDisplayInfo("modelDispMask5:1", "ModelDisplayMask5", False, bool, ""),
        FieldDisplayInfo("modelDispMask6:1", "ModelDisplayMask6", False, bool, ""),
        FieldDisplayInfo("modelDispMask7:1", "ModelDisplayMask7", False, bool, ""),
        FieldDisplayInfo("modelDispMask8:1", "ModelDisplayMask8", False, bool, ""),
        FieldDisplayInfo("modelDispMask9:1", "ModelDisplayMask9", False, bool, ""),
        FieldDisplayInfo("modelDispMask10:1", "ModelDisplayMask10", False, bool, ""),
        FieldDisplayInfo("modelDispMask11:1", "ModelDisplayMask11", False, bool, ""),
        FieldDisplayInfo("modelDispMask12:1", "ModelDisplayMask12", False, bool, ""),
        FieldDisplayInfo("modelDispMask13:1", "ModelDisplayMask13", False, bool, ""),
        FieldDisplayInfo("modelDispMask14:1", "ModelDisplayMask14", False, bool, ""),
        FieldDisplayInfo("modelDispMask15:1", "ModelDisplayMask15", False, bool, ""),
        FieldDisplayInfo("isEnableNeckTurn:1", "EnableNeckTurn", True, bool, "Character can turn their neck."),
        FieldDisplayInfo(
            "disableRespawn:1",
            "DisableRespawnOnRest",
            True,
            bool,
            "Prevents character from respawning when you rest at a bonfire, though they will still respawn when you "
            "die or the map is de-loaded unless they are disabled by an event script.",
        ),
        FieldDisplayInfo("isMoveAnimWait:1", "IsMoveAnimationWait", False, bool, ""),
        FieldDisplayInfo("isCrowd:1", "IsCrowd", False, bool, "Always false."),
        FieldDisplayInfo(
            "isWeakSaint:1",
            "IsWeakToDivine",
            True,
            bool,
            "True for skeletons and friends, but not sure how it is actually used to disable their reanimation by "
            "Necromancers.",
        ),
        FieldDisplayInfo("isWeakA:1", "IsWeakToOccult", True, bool, "True for all Gods and most NPCs in Anor Londo."),
        FieldDisplayInfo(
            "isWeakB:1",
            "IsAbyssal",
            True,
            bool,
            "True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus.",
        ),
        FieldDisplayInfo("pad1:1", "Pad1", False, bit_pad_field(1), ""),
        FieldDisplayInfo(
            "vowType:3",
            "VowType",
            False,
            int,
            "Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone else.",
        ),
        FieldDisplayInfo(
            "disableInitializeDead:1",
            "DisableInitializeDead",
            False,
            bool,
            "True for bosses and non-respawning enemies that are disabled in event scripts, but its effects are "
            "unknown.",
        ),
        FieldDisplayInfo("pad3:4", "Pad2", False, bit_pad_field(4), ""),
        FieldDisplayInfo("pad2[6]", "Pad3", False, pad_field(6), ""),
    ],
}

CACL_CORRECT_GRAPH_ST = {
    "paramdef_name": "CACL_CORRECT_GRAPH_ST",  # note typo in name
    "file_name": "CalcCorrectGraph",
    "nickname": "GrowthCurves",
    "fields": [
        FieldDisplayInfo(
            "stageMaxVal0", "StageMaxIntercept0", True, float, "Y-intercept in equation of 'stage max' line 0."
        ),
        FieldDisplayInfo(
            "stageMaxVal1", "StageMaxIntercept1", True, float, "Y-intercept in equation of 'stage max' line 1."
        ),
        FieldDisplayInfo(
            "stageMaxVal2", "StageMaxIntercept2", True, float, "Y-intercept in equation of 'stage max' line 2."
        ),
        FieldDisplayInfo(
            "stageMaxVal3", "StageMaxIntercept3", True, float, "Y-intercept in equation of 'stage max' line 3."
        ),
        FieldDisplayInfo(
            "stageMaxVal4", "StageMaxIntercept4", True, float, "Y-intercept in equation of 'stage max' line 4."
        ),
        FieldDisplayInfo("stageMaxGrowVal0", "StageMaxSlope0", True, float, "Slope in equation of 'stage max' line 0."),
        FieldDisplayInfo("stageMaxGrowVal1", "StageMaxSlope1", True, float, "Slope in equation of 'stage max' line 1."),
        FieldDisplayInfo("stageMaxGrowVal2", "StageMaxSlope2", True, float, "Slope in equation of 'stage max' line 2."),
        FieldDisplayInfo("stageMaxGrowVal3", "StageMaxSlope3", True, float, "Slope in equation of 'stage max' line 3."),
        FieldDisplayInfo("stageMaxGrowVal4", "StageMaxSlope4", True, float, "Slope in equation of 'stage max' line 4."),
        FieldDisplayInfo(
            "adjPt_maxGrowVal0",
            "AdjustmentMaxSlope0",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 0.",
        ),
        FieldDisplayInfo(
            "adjPt_maxGrowVal1",
            "AdjustmentMaxSlope1",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 1.",
        ),
        FieldDisplayInfo(
            "adjPt_maxGrowVal2",
            "AdjustmentMaxSlope2",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 2.",
        ),
        FieldDisplayInfo(
            "adjPt_maxGrowVal3",
            "AdjustmentMaxSlope3",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 3.",
        ),
        FieldDisplayInfo(
            "adjPt_maxGrowVal4",
            "AdjustmentMaxSlope4",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 4.",
        ),
        FieldDisplayInfo(
            "init_inclination_soul",
            "InitialLevellingCostSlope",
            True,
            float,
            "Initial slope of equation determining levelling costs (α1).",
        ),
        FieldDisplayInfo(
            "adjustment_value",
            "LevellingCostEarlyAdjustment",
            True,
            float,
            "'Early' adjustment value of equation determining levelling costs (α2).",
        ),
        FieldDisplayInfo(
            "boundry_inclination_soul",  # (sic)
            "LateLevellingCostSlope",
            True,
            float,
            "Slope of equation determining required levelling souls after 'LateLevellingCostThreshold' value (α3).",
        ),
        FieldDisplayInfo(
            "boundry_value",  # (sic)
            "LateLevellingCostThreshold",
            True,
            float,
            "Threshold at which 'LateLevellingCostSlope' takes over for levelling (t).",
        ),
        FieldDisplayInfo("pad[4]", "Pad0", False, pad_field(4), "Null padding."),
    ],
}
