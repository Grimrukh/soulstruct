from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


NPC_PARAM_ST = {
    "param_type": "NPC_PARAM_ST",
    "file_name": "NpcParam",
    "nickname": "Characters",
    "fields": [
        ParamFieldInfo(
            "behaviorVariationId",
            "BehaviorVariationID",
            True,
            int,
            "Multiplied by 1000 and added to non-player behavior lookups (hitboxes, bullets) triggered by TAE.",
        ),
        ParamFieldInfo(
            "aiThinkId", "DefaultAI", True, AIParam, "Default AI ID. Overridden by AI ID field in Maps entry."
        ),
        ParamFieldInfo(
            "nameId",
            "NameID",
            True,
            NPCName,
            "Text ID for NPC name that appears attached to NPCs. Only works for invaders and summons.",
        ),
        ParamFieldInfo(
            "turnVellocity", "TurnVelocity", True, float, "Turning velocity of NPC. (Exact effect needs testing.)"
        ),
        ParamFieldInfo("hitHeight", "HitHeight", True, float, "Height of NPC hitbox for collision."),
        ParamFieldInfo("hitRadius", "HitRadius", True, float, "Radius of NPC hitbox for collision."),
        ParamFieldInfo("weight", "Weight", False, int, "Weight of NPC. Probably has no effect (generall 100)."),
        ParamFieldInfo("hitYOffset", "HitYOffset", False, float, "Vertical offset of NPC hitbox for collision."),
        ParamFieldInfo("hp", "MaximumHP", True, int, "Maximum HP of NPC."),
        ParamFieldInfo("mp", "MaximumMP", False, int, "Maximum MP of NPC. Not used in Dark Souls (generally zero)."),
        ParamFieldInfo(
            "getSoul", "SoulReward", True, int, "Amount of souls (before NG+ scaling) rewarded when NPC is killed."
        ),
        ParamFieldInfo(
            "itemLotId_1",
            "ItemLotID1",
            True,
            ItemLotParam,
            "First item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "itemLotId_2",
            "ItemLotID2",
            True,
            ItemLotParam,
            "Second item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "itemLotId_3",
            "ItemLotID3",
            True,
            ItemLotParam,
            "Third item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "itemLotId_4",
            "ItemLotID4",
            True,
            ItemLotParam,
            "Fourth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "itemLotId_5",
            "ItemLotID5",
            True,
            ItemLotParam,
            "Fifth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "itemLotId_6",
            "ItemLotID6",
            True,
            ItemLotParam,
            "Sixth item lot triggered when NPC dies (set to -1 for no item lot).",
        ),
        ParamFieldInfo(
            "humanityLotId",
            "HumanityLotID",
            True,
            Flag,
            "Starting flag of counter for awarding random humanity (I think). Only used by a few enemies, "
            "such as Hollows and Mass of Souls.",
        ),
        ParamFieldInfo(
            "spEffectID0",
            "SpecialEffectID0",
            True,
            SpecialEffectParam,
            "First passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 5300-5337 range, which modify enemy damage animations (e.g. so bosses stagger less).",
        ),
        ParamFieldInfo(
            "spEffectID1",
            "SpecialEffectID1",
            True,
            SpecialEffectParam,
            "Second passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 5360-5364 range, which further modify enemy damage animations based on poise.",
        ),
        ParamFieldInfo(
            "spEffectID2",
            "SpecialEffectID2",
            True,
            SpecialEffectParam,
            "Third passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 90000-91111 range, which determine status effect immunities. From left to right, "
            "the four binary digits represent poison, toxic, bleed, and curse. 0 means the NPC is immune to that "
            "status, and 1 means they are not immune (though their resistance could be any value).",
        ),
        ParamFieldInfo(
            "spEffectID3",
            "SpecialEffectID3",
            True,
            SpecialEffectParam,
            "Fourth passive special effect that is active on NPC.\n\nThis slot is generally reserved for effects "
            "in the 80000-81111 range, which determine immunities to effects that apparently never made it into "
            "the game ('remnant', 'absorption', 'fascination', and 'ineffective').",
        ),
        ParamFieldInfo(
            "spEffectID4",
            "SpecialEffectID4",
            True,
            SpecialEffectParam,
            "Fifth passive special effect that is active on NPC.\n\nThis slot is generally reserved for "
            "'levelling' effects in the 7000-7015 range, which scale enemy stats according to the map they are "
            "found in.",
        ),
        ParamFieldInfo(
            "spEffectID5",
            "SpecialEffectID5",
            True,
            SpecialEffectParam,
            "Sixth passive special effect that is active on NPC.\n\nUsed for miscellaneous effects, "
            "such as elemental resistance or immunity, animation offset effects, the black phantom effect (7100), "
            "etc.",
        ),
        ParamFieldInfo(
            "spEffectID6",
            "SpecialEffectID6",
            True,
            SpecialEffectParam,
            "Seventh passive special effect that is active on NPC.\n\nUsed for miscellaneous effects, "
            "such as elemental resistance or immunity, animation offset effects, the black phantom effect (7100), "
            "etc.",
        ),
        ParamFieldInfo(
            "spEffectID7",
            "SpecialEffectID7",
            True,
            SpecialEffectParam,
            "Eighth passive special effect that is active on NPC.\n\nThis slot is generally reserved for effect "
            "71100, 71110, or 71111. The fourth binary digit determines if the NPC uses the 'immortal system'; "
            "the third binary digit is unknown. Darkwraiths, Hollows, Humanity Phantoms, and Armored Tusks are "
            "some examples of the few NPCs that use 71111; most others use 71110, except bosses.",
        ),
        ParamFieldInfo(
            "GameClearSpEffectID",
            "NewGamePlusSpecialEffect",
            True,
            SpecialEffectParam,
            "Passive special effect that is only applied to the NPC in NG+ and beyond, which are taken from the "
            "range 7401-7415.",
        ),
        ParamFieldInfo(
            "physGuardCutRate",
            "PhysicalGuardCutRate",
            True,
            float,
            "Percentage reduction in physical damage taken while NPC is guarding.",
        ),
        ParamFieldInfo(
            "magGuardCutRate",
            "MagicGuardCutRate",
            True,
            float,
            "Percentage reduction in magic damage taken while NPC is guarding.",
        ),
        ParamFieldInfo(
            "fireGuardCutRate",
            "FireGuardCutRate",
            True,
            float,
            "Percentage reduction in fire damage taken while NPC is guarding.",
        ),
        ParamFieldInfo(
            "thunGuardCutRate",
            "LightningGuardCutRate",
            True,
            float,
            "Percentage reduction in lightning damage taken while NPC is guarding.",
        ),
        ParamFieldInfo(
            "animIdOffset",
            "AnimationIDOffset",
            True,
            int,
            "Offset added to animation requests (e.g. from AI script or event script). If the offset animation is "
            "missing, the original will be used.",
        ),
        # TODO: Animation types.
        ParamFieldInfo("moveAnimId", "MoveAnimationID", False, int, ""),
        ParamFieldInfo("spMoveAnimId1", "SpecialMoveAnimationID1", False, int, ""),
        ParamFieldInfo("spMoveAnimId2", "SpecialMoveAnimationID2", False, int, ""),
        ParamFieldInfo("networkWarpDist", "NetworkWarpDistance", False, float, ""),
        ParamFieldInfo("dbgBehaviorR1", "DebugBehaviorR1", False, int, ""),
        ParamFieldInfo("dbgBehaviorL1", "DebugBehaviorL1", False, int, ""),
        ParamFieldInfo("dbgBehaviorR2", "DebugBehaviorR2", False, int, ""),
        ParamFieldInfo("dbgBehaviorL2", "DebugBehaviorL2", False, int, ""),
        ParamFieldInfo("dbgBehaviorRL", "DebugBehaviorRL", False, int, ""),
        ParamFieldInfo("dbgBehaviorRR", "DebugBehaviorRR", False, int, ""),
        ParamFieldInfo("dbgBehaviorRD", "DebugBehaviorRD", False, int, ""),
        ParamFieldInfo("dbgBehaviorRU", "DebugBehaviorRU", False, int, ""),
        ParamFieldInfo("dbgBehaviorLL", "DebugBehaviorLL", False, int, ""),
        ParamFieldInfo("dbgBehaviorLR", "DebugBehaviorLR", False, int, ""),
        ParamFieldInfo("dbgBehaviorLD", "DebugBehaviorLD", False, int, ""),
        ParamFieldInfo("dbgBehaviorLU", "DebugBehaviorLU", False, int, ""),
        ParamFieldInfo("animIdOffset2", "AnimationIDOffset2", False, int, ""),
        ParamFieldInfo(
            "partsDamageRate1",
            "Part1DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 1 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate2",
            "Part2DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 2 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate3",
            "Part3DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 3 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate4",
            "Part4DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 4 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate5",
            "Part5DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 5 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate6",
            "Part6DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 6 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate7",
            "Part7DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 7 of NPC model.",
        ),
        ParamFieldInfo(
            "partsDamageRate8",
            "Part8DamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by part 8 of NPC model.",
        ),
        ParamFieldInfo(
            "weakPartsDamageRate",
            "WeakPartsDamageMultiplier",
            True,
            float,
            "Multiplier for damage taken by weak parts of NPC model.",
        ),
        ParamFieldInfo(
            "superArmorRecoverCorrection",
            "PoiseRecoveryCorrection",
            True,
            float,
            "Change to poise recovery rate. Only the Chained Prisoner uses a non-zero value in vanilla(-0.2).",
        ),
        ParamFieldInfo(
            "superArmorBrakeKnockbackDist",
            "StaggerKnockbackDistance",
            True,
            float,
            "Stagger knockback distance when NPC's poise is broken.",
        ),
        ParamFieldInfo("stamina", "MaxStamina", True, int, "Maximum stamina of NPC."),
        ParamFieldInfo(
            "staminaRecoverBaseVel", "StaminaRecoveryBaseSpeed", True, int, "Base speed of NPC's stamina recovery."
        ),
        ParamFieldInfo("def_phys", "PhysicalDefense", True, int, "Base defense applied to all physical attacks."),
        ParamFieldInfo("def_slash", "SlashDefense", True, int, "Base defense added against slashing physical attacks."),
        ParamFieldInfo("def_blow", "StrikeDefense", True, int, "Base defense added against striking physical attacks."),
        ParamFieldInfo(
            "def_thrust", "ThrustDefense", True, int, "Base defense added against thrusting physical attacks."
        ),
        ParamFieldInfo("def_mag", "MagicDefense", True, int, "Base defense added against magic attacks."),
        ParamFieldInfo("def_fire", "FireDefense", True, int, "Base defense added against fire attacks."),
        ParamFieldInfo("def_thunder", "LightningDefense", True, int, "Base defense added against lightning attacks."),
        ParamFieldInfo(
            "defFlickPower",
            "DefenseRepelPower",
            False,
            int,
            "Determines how severely an attacker is repelled when they fail to break this NPC's poise. The "
            "Armored Tusk and Chained Prisoner have very high values (50-60), but most NPCs have 0.",
        ),
        ParamFieldInfo("resist_poison", "PoisonResistance", True, int, "Base poison resistance."),
        ParamFieldInfo("resist_desease", "ToxicResistance", True, int, "Base toxic resistance."),
        ParamFieldInfo("resist_blood", "BleedResistance", True, int, "Base bleed resistance."),
        ParamFieldInfo("resist_curse", "CurseResistance", True, int, "Base curse resistance."),
        ParamFieldInfo(
            "ghostModelId",
            "GhostModelID",
            False,
            int,
            "Model to be used when this quest-related NPC appears as a ghost to other players. Defaults to -1 for "
            "almost all standard enemies, which means they do not appear as a ghost to others.",
        ),
        ParamFieldInfo("normalChangeResouceId", "NormalChangeResourceID", False, int, "Unknown. Always -1."),
        ParamFieldInfo("guardAngle", "GuardAngle", False, int, "Zero for every NPC except the Phalanx Hollow (20)."),
        ParamFieldInfo("slashGuardCutRate", "SlashDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo("blowGuardCutRate", "StrikeDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo("thrustGuardCutRate", "ThrustDamageReductionWhenGuarding", False, int, "Always zero."),
        ParamFieldInfo(
            "superArmorDurability",
            "MaxPoise",
            True,
            int,
            "Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, "
            "the character will be staggered.",
        ),
        ParamFieldInfo(
            "normalChangeTexChrId",
            "NormalChangeTextureChrID",
            False,
            int,
            "Unknown. Used for only some NPCs, where it is generally set to a number close to the NPC's character "
            "model ID.",
        ),
        ParamFieldInfo(
            "dropType",
            "ItemDropAppearance",
            True,
            NPC_ITEMDROP_TYPE,
            "Determines appearance of dropped items. 0 means the item appears to glow faintly from inside the "
            "NPC's body (e.g. Rat, Mushroom Child/Parent, Ent) and 1 means the item is a clear white orb just "
            "like regular treasure on corpses (most NPCs).",
        ),
        ParamFieldInfo("knockbackRate", "KnockbackRate", True, int, ""),
        ParamFieldInfo(
            "knockbackParamId",
            "KnockbackID",
            True,
            int,
            "Knockback parameters were abandoned after Demons' Souls. A param table for Knockback is still present "
            "but is not accessible in the GUI.",
        ),
        ParamFieldInfo("fallDamageDump", "FallDamageReduction", True, int, "Percentage of fall damage to ignore."),
        ParamFieldInfo(
            "staminaGuardDef",
            "StaminaGuardDefense",
            True,
            int,
            "Always set to zero in the game, but presumably, increasing it will reduce the amount of stamina lost "
            "when this NPC blocks an attack.",
        ),
        ParamFieldInfo("pcAttrB", "PCAttrB", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("pcAttrW", "PCAttrW", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("pcAttrL", "PCAttrL", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("pcAttrR", "PCAttrR", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("areaAttrB", "AreaAttrB", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("areaAttrW", "AreaAttrW", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("areaAttrL", "AreaAttrL", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo("areaAttrR", "AreaAttrR", False, int, "Like a remnant of World Tendency. Always set to zero."),
        ParamFieldInfo(
            "mpRecoverBaseVel",
            "MPRecoveryBaseSpeed",
            False,
            int,
            "Unknown effect, likely none. Set to zero for NPC parts (tails and Hydra heads) and 10 for everyone "
            "else.",
        ),
        ParamFieldInfo(
            "flickDamageCutRate",
            "RepelDamageCutRate",
            False,
            int,
            "Unknown effect, but it is set to zero for most enemies, 50 for very heavy enemies like Great Stone "
            "Knights and Titanite Demons, and 100 for Mimics.",
        ),
        ParamFieldInfo(
            "defaultLodParamId", "DefaultLightingParamID", False, int, "Default lighting (Lod) parameter entry ID."
        ),
        ParamFieldInfo("drawType", "DrawType", True, NPC_DRAW_TYPE, ""),
        ParamFieldInfo("npcType", "CharacterType", True, NPC_TYPE, ""),
        ParamFieldInfo(
            "teamType", "TeamType", True, NPC_TEMA_TYPE, "0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom"
        ),
        ParamFieldInfo("moveType", "MoveType", True, NPC_MOVE_TYPE, ""),
        ParamFieldInfo("lockDist", "LockOnDistance", True, int, ""),
        ParamFieldInfo("material", "Material", False, int, ""),
        ParamFieldInfo("materialSfx", "MaterialSFX", False, int, ""),
        ParamFieldInfo("material_Weak", "MaterialWeak", False, int, ""),
        ParamFieldInfo("materialSfx_Weak", "MaterialWeakSFX", False, int, ""),
        ParamFieldInfo(
            "partsDamageType",
            "PartsDamageType",
            False,
            int,
            "Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, Seath, "
            "Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise.",
        ),
        ParamFieldInfo(
            "maxUndurationAng",
            "MaxUndurationAngle",
            False,
            int,
            "Unknown effect, but it is generally set to 30 for all four-legged enemies, and 0 for all others.",
        ),
        ParamFieldInfo(
            "guardLevel",
            "GuardLevel",
            False,
            GUARDMOTION_CATEGORY,
            "Set to 4 for enemies who can guard (including Manus), except Giant Skeletons, who have a value of 3. "
            "All other NPCs have zero.",
        ),
        ParamFieldInfo(
            "burnSfxType",
            "BurnSFXType",
            False,
            NPC_BURN_TYPE,
            "Set to 1 for Slimes and Undead Dragons, and 0 for everyone else.",
        ),
        ParamFieldInfo(
            "poisonGuardResist", "PoisonGuardResistance", True, int, "Added poison resistance while guarding."
        ),
        ParamFieldInfo(
            "diseaseGuardResist", "ToxicGuardResistance", True, int, "Added toxic resistance while guarding."
        ),
        ParamFieldInfo("bloodGuardResist", "BleedGuardResistance", True, int, "Added bleed resistance while guarding."),
        ParamFieldInfo("curseGuardResist", "CurseGuardResistance", True, int, "Added curse resistance while guarding."),
        ParamFieldInfo("parryAttack", "ParryAttack", False, int, "Always zero."),
        ParamFieldInfo("parryDefence", "ParryDefense", False, int, "Always zero."),
        ParamFieldInfo(
            "sfxSize",
            "SFXSize",
            False,
            NPC_SFX_SIZE,
            "Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise.",
        ),
        ParamFieldInfo("pushOutCamRegionRadius", "PushOutCameraRegionRadius", False, int, "Always zero."),
        ParamFieldInfo(
            "hitStopType",
            "HitStopType",
            False,
            NPC_HITSTOP_TYPE,
            "Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely related to AI triggers.",
        ),
        ParamFieldInfo(
            "ladderEndChkOffsetTop", "LadderEndCheckOffsetTop", False, int, "Not something you want to mess with."
        ),
        ParamFieldInfo(
            "ladderEndChkOffsetLow",
            "LadderEndCheckOffsetBottom",
            False,
            int,
            "Not something you want to mess with.",
        ),
        ParamFieldInfo("useRagdollCamHit:1", "UseRagdollCameraHit", False, bool, ""),
        ParamFieldInfo("disableClothRigidHit:1", "DisableClothRigidHit", False, bool, ""),
        ParamFieldInfo("useRagdoll:1", "UseRagdoll", False, bool, ""),
        ParamFieldInfo("isDemon:1", "IsDemon", True, bool, ""),
        ParamFieldInfo("isGhost:1", "IsGhost", True, bool, ""),
        ParamFieldInfo("isNoDamageMotion:1", "IsNoDamageMotion", True, bool, ""),
        ParamFieldInfo("isUnduration:1", "IsUnduration", False, bool, ""),
        ParamFieldInfo("isChangeWanderGhost:1", "IsChangeWanderGhost", False, bool, "Always false."),
        ParamFieldInfo("modelDispMask0:1", "ModelDisplayMask0", False, bool, ""),
        ParamFieldInfo("modelDispMask1:1", "ModelDisplayMask1", False, bool, ""),
        ParamFieldInfo("modelDispMask2:1", "ModelDisplayMask2", False, bool, ""),
        ParamFieldInfo("modelDispMask3:1", "ModelDisplayMask3", False, bool, ""),
        ParamFieldInfo("modelDispMask4:1", "ModelDisplayMask4", False, bool, ""),
        ParamFieldInfo("modelDispMask5:1", "ModelDisplayMask5", False, bool, ""),
        ParamFieldInfo("modelDispMask6:1", "ModelDisplayMask6", False, bool, ""),
        ParamFieldInfo("modelDispMask7:1", "ModelDisplayMask7", False, bool, ""),
        ParamFieldInfo("modelDispMask8:1", "ModelDisplayMask8", False, bool, ""),
        ParamFieldInfo("modelDispMask9:1", "ModelDisplayMask9", False, bool, ""),
        ParamFieldInfo("modelDispMask10:1", "ModelDisplayMask10", False, bool, ""),
        ParamFieldInfo("modelDispMask11:1", "ModelDisplayMask11", False, bool, ""),
        ParamFieldInfo("modelDispMask12:1", "ModelDisplayMask12", False, bool, ""),
        ParamFieldInfo("modelDispMask13:1", "ModelDisplayMask13", False, bool, ""),
        ParamFieldInfo("modelDispMask14:1", "ModelDisplayMask14", False, bool, ""),
        ParamFieldInfo("modelDispMask15:1", "ModelDisplayMask15", False, bool, ""),
        ParamFieldInfo("isEnableNeckTurn:1", "EnableNeckTurn", True, bool, "Character can turn their neck."),
        ParamFieldInfo(
            "disableRespawn:1",
            "DisableRespawnOnRest",
            True,
            bool,
            "Prevents character from respawning when you rest at a bonfire, though they will still respawn when you "
            "die or the map is de-loaded unless they are disabled by an event script.",
        ),
        ParamFieldInfo("isMoveAnimWait:1", "IsMoveAnimationWait", False, bool, ""),
        ParamFieldInfo("isCrowd:1", "IsCrowd", False, bool, "Always false."),
        ParamFieldInfo(
            "isWeakSaint:1",
            "IsWeakToDivine",
            True,
            bool,
            "True for skeletons and friends, but not sure how it is actually used to disable their reanimation by "
            "Necromancers.",
        ),
        ParamFieldInfo("isWeakA:1", "IsWeakToOccult", True, bool, "True for all Gods and most NPCs in Anor Londo."),
        ParamFieldInfo(
            "isWeakB:1",
            "IsAbyssal",
            True,
            bool,
            "True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus.",
        ),
        ParamFieldInfo("pad1:1", "Pad1", False, bit_pad_field(1), ""),
        ParamFieldInfo(
            "vowType:3",
            "VowType",
            False,
            int,
            "Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone else.",
        ),
        ParamFieldInfo(
            "disableInitializeDead:1",
            "DisableInitializeDead",
            False,
            bool,
            "True for bosses and non-respawning enemies that are disabled in event scripts, but its effects are "
            "unknown.",
        ),
        ParamFieldInfo("pad3:4", "Pad2", False, bit_pad_field(4), ""),
        ParamFieldInfo("pad2[6]", "Pad3", False, pad_field(6), ""),
    ],
}
