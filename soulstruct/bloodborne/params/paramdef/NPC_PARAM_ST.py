from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_PARAM_ST(ParamRow):
    BehaviorVariationID: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="Multiplied by 1000 and added to non-player behavior lookups (hitboxes, bullets) triggered by TAE.",
    )
    DefaultAI: int = ParamField(
        int, "aiThinkId", game_type=AIParam, default=0,
        tooltip="Default AI ID. Overridden by AI ID field in Maps entry.",
    )
    NameID: int = ParamField(
        int, "nameId", default=-1,
        tooltip="Text ID for NPC name that appears attached to NPCs. Only works for invaders and summons.",
    )
    TurnVelocity: float = ParamField(
        float, "turnVellocity", default=0.0,
        tooltip="Turning velocity of NPC. (Exact effect needs testing.)",
    )
    HitHeight: float = ParamField(
        float, "hitHeight", default=0.0,
        tooltip="Height of NPC hitbox for collision.",
    )
    HitRadius: float = ParamField(
        float, "hitRadius", default=0.0,
        tooltip="Radius of NPC hitbox for collision.",
    )
    Weight: int = ParamField(
        uint, "weight", default=0,
        tooltip="Weight of NPC. Probably has no effect (generall 100).",
    )
    HitYOffset: float = ParamField(
        float, "hitYOffset", default=0.0,
        tooltip="Vertical offset of NPC hitbox for collision.",
    )
    MaximumHP: int = ParamField(
        uint, "hp", default=0,
        tooltip="Maximum HP of NPC.",
    )
    MaximumMP: int = ParamField(
        uint, "mp", default=0,
        tooltip="Maximum MP of NPC. Not used in Dark Souls (generally zero).",
    )
    SoulReward: int = ParamField(
        uint, "getSoul", default=0,
        tooltip="Amount of souls (before NG+ scaling) rewarded when NPC is killed.",
    )
    ItemLotID1: int = ParamField(
        int, "itemLotId_1", game_type=ItemLotParam, default=-1,
        tooltip="First item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    ItemLotID2: int = ParamField(
        int, "itemLotId_2", game_type=ItemLotParam, default=-1,
        tooltip="Second item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    ItemLotID3: int = ParamField(
        int, "itemLotId_3", game_type=ItemLotParam, default=-1,
        tooltip="Third item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    ItemLotID4: int = ParamField(
        int, "itemLotId_4", game_type=ItemLotParam, default=-1,
        tooltip="Fourth item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    ItemLotID5: int = ParamField(
        int, "itemLotId_5", game_type=ItemLotParam, default=-1,
        tooltip="Fifth item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    ItemLotID6: int = ParamField(
        int, "itemLotId_6", game_type=ItemLotParam, default=-1,
        tooltip="Sixth item lot triggered when NPC dies (set to -1 for no item lot).",
    )
    HumanityLotID: int = ParamField(
        int, "humanityLotId", default=-1,
        tooltip="Starting flag of counter for awarding random humanity (I think). Only used by a few enemies, such as "
                "Hollows and Mass of Souls.",
    )
    SpecialEffectID0: int = ParamField(
        int, "spEffectID0", game_type=SpecialEffectParam, default=-1,
        tooltip="First passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 5300-5337 range, which modify enemy damage animations (e.g. so bosses stagger less).",
    )
    SpecialEffectID1: int = ParamField(
        int, "spEffectID1", game_type=SpecialEffectParam, default=-1,
        tooltip="Second passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 5360-5364 range, which further modify enemy damage animations based on poise.",
    )
    SpecialEffectID2: int = ParamField(
        int, "spEffectID2", game_type=SpecialEffectParam, default=-1,
        tooltip="Third passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 90000-91111 range, which determine status effect immunities. From left to right, the four binary "
                "digits represent poison, toxic, bleed, and curse. 0 means the NPC is immune to that status, and 1 "
                "means they are not immune (though their resistance could be any value).",
    )
    SpecialEffectID3: int = ParamField(
        int, "spEffectID3", game_type=SpecialEffectParam, default=-1,
        tooltip="Fourth passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 80000-81111 range, which determine immunities to effects that apparently never made it into the "
                "game ('remnant', 'absorption', 'fascination', and 'ineffective').",
    )
    SpecialEffectID4: int = ParamField(
        int, "spEffectID4", game_type=SpecialEffectParam, default=-1,
        tooltip="Fifth passive special effect that is active on NPC.  This slot is generally reserved for 'levelling' "
                "effects in the 7000-7015 range, which scale enemy stats according to the map they are found in.",
    )
    SpecialEffectID5: int = ParamField(
        int, "spEffectID5", game_type=SpecialEffectParam, default=-1,
        tooltip="Sixth passive special effect that is active on NPC.  Used for miscellaneous effects, such as "
                "elemental resistance or immunity, animation offset effects, the black phantom effect (7100), etc.",
    )
    SpecialEffectID6: int = ParamField(
        int, "spEffectID6", game_type=SpecialEffectParam, default=-1,
        tooltip="Seventh passive special effect that is active on NPC.  Used for miscellaneous effects, such as "
                "elemental resistance or immunity, animation offset effects, the black phantom effect (7100), etc.",
    )
    SpecialEffectID7: int = ParamField(
        int, "spEffectID7", game_type=SpecialEffectParam, default=-1,
        tooltip="Eighth passive special effect that is active on NPC.  This slot is generally reserved for effect "
                "71100, 71110, or 71111. The fourth binary digit determines if the NPC uses the 'immortal system'; "
                "the third binary digit is unknown. Darkwraiths, Hollows, Humanity Phantoms, and Armored Tusks are "
                "some examples of the few NPCs that use 71111; most others use 71110, except bosses.",
    )
    NewGamePlusSpecialEffect: int = ParamField(
        int, "GameClearSpEffectID", game_type=SpecialEffectParam, default=-1,
        tooltip="Passive special effect that is only applied to the NPC in NG+ and beyond, which are taken from the "
                "range 7401-7415.",
    )
    PhysicalGuardCutRate: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="Percentage reduction in physical damage taken while NPC is guarding.",
    )
    MagicGuardCutRate: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="Percentage reduction in magic damage taken while NPC is guarding.",
    )
    FireGuardCutRate: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="Percentage reduction in fire damage taken while NPC is guarding.",
    )
    LightningGuardCutRate: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="Percentage reduction in lightning damage taken while NPC is guarding.",
    )
    AnimationIDOffset: int = ParamField(
        int, "animIdOffset", default=0,
        tooltip="Offset added to animation requests (e.g. from AI script or event script). If the offset animation is "
                "missing, the original will be used.",
    )
    MoveAnimationID: int = ParamField(
        int, "moveAnimId", game_type=Animation, default=0,
        tooltip="TODO",
    )
    SpecialMoveAnimationID1: int = ParamField(
        int, "spMoveAnimId1", game_type=Animation, default=0,
        tooltip="TODO",
    )
    SpecialMoveAnimationID2: int = ParamField(
        int, "spMoveAnimId2", game_type=Animation, default=0,
        tooltip="TODO",
    )
    NetworkWarpDistance: float = ParamField(
        float, "networkWarpDist", default=0.0,
        tooltip="TODO",
    )
    DebugBehaviorR1: int = ParamField(
        int, "dbgBehaviorR1", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorL1: int = ParamField(
        int, "dbgBehaviorL1", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorR2: int = ParamField(
        int, "dbgBehaviorR2", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorL2: int = ParamField(
        int, "dbgBehaviorL2", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRL: int = ParamField(
        int, "dbgBehaviorRL", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRR: int = ParamField(
        int, "dbgBehaviorRR", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRD: int = ParamField(
        int, "dbgBehaviorRD", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRU: int = ParamField(
        int, "dbgBehaviorRU", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLL: int = ParamField(
        int, "dbgBehaviorLL", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLR: int = ParamField(
        int, "dbgBehaviorLR", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLD: int = ParamField(
        int, "dbgBehaviorLD", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLU: int = ParamField(
        int, "dbgBehaviorLU", default=-1,
        tooltip="TODO",
    )
    AnimationIDOffset2: int = ParamField(
        int, "animIdOffset2", game_type=Animation, default=0,
        tooltip="TODO",
    )
    Part1DamageMultiplier: float = ParamField(
        float, "partsDamageRate1", default=1.0,
        tooltip="Multiplier for damage taken by part 1 of NPC model.",
    )
    Part2DamageMultiplier: float = ParamField(
        float, "partsDamageRate2", default=1.0,
        tooltip="Multiplier for damage taken by part 2 of NPC model.",
    )
    Part3DamageMultiplier: float = ParamField(
        float, "partsDamageRate3", default=1.0,
        tooltip="Multiplier for damage taken by part 3 of NPC model.",
    )
    Part4DamageMultiplier: float = ParamField(
        float, "partsDamageRate4", default=1.0,
        tooltip="Multiplier for damage taken by part 4 of NPC model.",
    )
    Part5DamageMultiplier: float = ParamField(
        float, "partsDamageRate5", default=1.0,
        tooltip="Multiplier for damage taken by part 5 of NPC model.",
    )
    Part6DamageMultiplier: float = ParamField(
        float, "partsDamageRate6", default=1.0,
        tooltip="Multiplier for damage taken by part 6 of NPC model.",
    )
    Part7DamageMultiplier: float = ParamField(
        float, "partsDamageRate7", default=1.0,
        tooltip="Multiplier for damage taken by part 7 of NPC model.",
    )
    Part8DamageMultiplier: float = ParamField(
        float, "partsDamageRate8", default=1.0,
        tooltip="Multiplier for damage taken by part 8 of NPC model.",
    )
    WeakPartsDamageMultiplier: float = ParamField(
        float, "weakPartsDamageRate", default=1.0,
        tooltip="Multiplier for damage taken by weak parts of NPC model.",
    )
    PoiseRecoveryCorrection: float = ParamField(
        float, "superArmorRecoverCorrection", default=0.0,
        tooltip="Change to poise recovery rate. Only the Chained Prisoner uses a non-zero value in vanilla(-0.2).",
    )
    StaggerKnockbackDistance: float = ParamField(
        float, "superArmorBrakeKnockbackDist", default=0.0,
        tooltip="Stagger knockback distance when NPC's poise is broken.",
    )
    MaxStamina: int = ParamField(
        ushort, "stamina", default=0,
        tooltip="Maximum stamina of NPC.",
    )
    StaminaRecoveryBaseSpeed: int = ParamField(
        ushort, "staminaRecoverBaseVel", default=0,
        tooltip="Base speed of NPC's stamina recovery.",
    )
    PhysicalDefense: int = ParamField(
        ushort, "def_phys", default=0,
        tooltip="Base defense applied to all physical attacks.",
    )
    SlashDefense: int = ParamField(
        short, "def_slash", default=0,
        tooltip="Base defense added against slashing physical attacks.",
    )
    StrikeDefense: int = ParamField(
        short, "def_blow", default=0,
        tooltip="Base defense added against striking physical attacks.",
    )
    ThrustDefense: int = ParamField(
        short, "def_thrust", default=0,
        tooltip="Base defense added against thrusting physical attacks.",
    )
    MagicDefense: int = ParamField(
        ushort, "def_mag", default=0,
        tooltip="Base defense added against magic attacks.",
    )
    FireDefense: int = ParamField(
        ushort, "def_fire", default=0,
        tooltip="Base defense added against fire attacks.",
    )
    LightningDefense: int = ParamField(
        ushort, "def_thunder", default=0,
        tooltip="Base defense added against lightning attacks.",
    )
    DefenseRepelPower: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="Determines how severely an attacker is repelled when they fail to break this NPC's poise. The "
                "Armored Tusk and Chained Prisoner have very high values (50-60), but most NPCs have 0.",
    )
    PoisonResistance: int = ParamField(
        ushort, "resist_poison", default=0,
        tooltip="Base poison resistance.",
    )
    ToxicResistance: int = ParamField(
        ushort, "resist_desease", default=0,
        tooltip="Base toxic resistance.",
    )
    BleedResistance: int = ParamField(
        ushort, "resist_blood", default=0,
        tooltip="Base bleed resistance.",
    )
    CurseResistance: int = ParamField(
        ushort, "resist_curse", default=0,
        tooltip="Base curse resistance.",
    )
    GhostModelID: int = ParamField(
        short, "ghostModelId", game_type=EquipmentModel, default=-1,
        tooltip="Model to be used when this quest-related NPC appears as a ghost to other players. Defaults to -1 for "
                "almost all standard enemies, which means they do not appear as a ghost to others.",
    )
    NormalChangeResourceID: int = ParamField(
        short, "normalChangeResouceId", default=-1,
        tooltip="Unknown. Always -1.",
    )
    GuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="Zero for every NPC except the Phalanx Hollow (20).",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        short, "slashGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        short, "blowGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        short, "thrustGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    MaxPoise: int = ParamField(
        short, "superArmorDurability", default=0,
        tooltip="Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, "
                "the character will be staggered.",
    )
    NormalChangeTextureChrID: int = ParamField(
        short, "normalChangeTexChrId", default=-1,
        tooltip="Unknown. Used for only some NPCs, where it is generally set to a number close to the NPC's character "
                "model ID.",
    )
    ItemDropAppearance: int = ParamField(
        ushort, "dropType", NPC_ITEMDROP_TYPE, default=0,
        tooltip="Determines appearance of dropped items. 0 means the item appears to glow faintly from inside the "
                "NPC's body (e.g. Rat, Mushroom Child/Parent, Ent) and 1 means the item is a clear white orb just "
                "like regular treasure on corpses (most NPCs).",
    )
    KnockbackRate: int = ParamField(
        byte, "knockbackRate", default=0,
        tooltip="TODO",
    )
    KnockbackID: int = ParamField(
        byte, "knockbackParamId", game_type=KnockbackParam, default=0,
        tooltip="Knockback parameters were abandoned after Demons' Souls. A param table for Knockback is still "
                "present but is not accessible in the GUI.",
    )
    FallDamageReduction: int = ParamField(
        byte, "fallDamageDump", default=0,
        tooltip="Percentage of fall damage to ignore.",
    )
    StaminaGuardDefense: int = ParamField(
        byte, "staminaGuardDef", default=0,
        tooltip="Always set to zero in the game, but presumably, increasing it will reduce the amount of stamina lost "
                "when this NPC blocks an attack.",
    )
    PCAttrB: int = ParamField(
        byte, "pcAttrB", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    PCAttrW: int = ParamField(
        byte, "pcAttrW", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    PCAttrL: int = ParamField(
        byte, "pcAttrL", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    PCAttrR: int = ParamField(
        byte, "pcAttrR", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    AreaAttrB: int = ParamField(
        byte, "areaAttrB", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    AreaAttrW: int = ParamField(
        byte, "areaAttrW", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    AreaAttrL: int = ParamField(
        byte, "areaAttrL", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    AreaAttrR: int = ParamField(
        byte, "areaAttrR", default=0,
        tooltip="Like a remnant of World Tendency. Always set to zero.",
    )
    MPRecoveryBaseSpeed: int = ParamField(
        byte, "mpRecoverBaseVel", default=0,
        tooltip="Unknown effect, likely none. Set to zero for NPC parts (tails and Hydra heads) and 10 for everyone "
                "else.",
    )
    RepelDamageCutRate: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="Unknown effect, but it is set to zero for most enemies, 50 for very heavy enemies like Great Stone "
                "Knights and Titanite Demons, and 100 for Mimics.",
    )
    DefaultLightingParamID: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="Default lighting (Lod) parameter entry ID.",
    )
    DrawType: int = ParamField(
        byte, "drawType", NPC_DRAW_TYPE, default=0,
        tooltip="TODO",
    )
    CharacterType: int = ParamField(
        byte, "npcType", NPC_TYPE, default=0,
        tooltip="TODO",
    )
    TeamType: int = ParamField(
        byte, "teamType", NPC_TEAM_TYPE, default=0,
        tooltip="0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom",
    )
    MoveType: int = ParamField(
        byte, "moveType", NPC_MOVE_TYPE, default=0,
        tooltip="TODO",
    )
    LockOnDistance: int = ParamField(
        byte, "lockDist", default=0,
        tooltip="TODO",
    )
    Material: int = ParamField(
        byte, "material", WEP_MATERIAL_DEF, default=0,
        tooltip="TODO",
    )
    MaterialSFX: int = ParamField(
        byte, "materialSfx", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TODO",
    )
    MaterialWeak: int = ParamField(
        byte, "material_Weak", WEP_MATERIAL_DEF, default=0,
        tooltip="TODO",
    )
    MaterialWeakSFX: int = ParamField(
        byte, "materialSfx_Weak", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TODO",
    )
    PartsDamageType: int = ParamField(
        byte, "partsDamageType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, Seath, "
                "Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise.",
    )
    MaxUndurationAngle: int = ParamField(
        byte, "maxUndurationAng", default=0,
        tooltip="Unknown effect, but it is generally set to 30 for all four-legged enemies, and 0 for all others.",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="Set to 4 for enemies who can guard (including Manus), except Giant Skeletons, who have a value of 3. "
                "All other NPCs have zero.",
    )
    BurnSFXType: int = ParamField(
        byte, "burnSfxType", NPC_BURN_TYPE, default=0,
        tooltip="Set to 1 for Slimes and Undead Dragons, and 0 for everyone else.",
    )
    PoisonGuardResistance: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="Added poison resistance while guarding.",
    )
    ToxicGuardResistance: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="Added toxic resistance while guarding.",
    )
    BleedGuardResistance: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="Added bleed resistance while guarding.",
    )
    CurseGuardResistance: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="Added curse resistance while guarding.",
    )
    ParryAttack: int = ParamField(
        byte, "parryAttack", default=0,
        tooltip="Always zero.",
    )
    ParryDefense: int = ParamField(
        byte, "parryDefence", default=0,
        tooltip="Always zero.",
    )
    SFXSize: int = ParamField(
        byte, "sfxSize", NPC_SFX_SIZE, default=0,
        tooltip="Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise.",
    )
    PushOutCameraRegionRadius: int = ParamField(
        byte, "pushOutCamRegionRadius", default=12,
        tooltip="Always zero.",
    )
    HitStopType: int = ParamField(
        byte, "hitStopType", NPC_HITSTOP_TYPE, default=0,
        tooltip="Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely related to AI triggers.",
    )
    LadderEndCheckOffsetTop: int = ParamField(
        byte, "ladderEndChkOffsetTop", default=15,
        tooltip="Not something you want to mess with.",
    )
    LadderEndCheckOffsetBottom: int = ParamField(
        byte, "ladderEndChkOffsetLow", default=8,
        tooltip="Not something you want to mess with.",
    )
    UseRagdollCameraHit: bool = ParamField(
        byte, "useRagdollCamHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableClothRigidHit: bool = ParamField(
        byte, "disableClothRigidHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    UseRagdoll: bool = ParamField(
        byte, "useRagdoll:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsDemon: bool = ParamField(
        byte, "isDemon:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsGhost: bool = ParamField(
        byte, "isGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsNoDamageMotion: bool = ParamField(
        byte, "isNoDamageMotion:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsUnduration: bool = ParamField(
        byte, "isUnduration:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsChangeWanderGhost: bool = ParamField(
        byte, "isChangeWanderGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="Always false.",
    )
    ModelDisplayMask0: bool = ParamField(
        byte, "modelDispMask0:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask1: bool = ParamField(
        byte, "modelDispMask1:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask2: bool = ParamField(
        byte, "modelDispMask2:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask3: bool = ParamField(
        byte, "modelDispMask3:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask4: bool = ParamField(
        byte, "modelDispMask4:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask5: bool = ParamField(
        byte, "modelDispMask5:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask6: bool = ParamField(
        byte, "modelDispMask6:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask7: bool = ParamField(
        byte, "modelDispMask7:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask8: bool = ParamField(
        byte, "modelDispMask8:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask9: bool = ParamField(
        byte, "modelDispMask9:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask10: bool = ParamField(
        byte, "modelDispMask10:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask11: bool = ParamField(
        byte, "modelDispMask11:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask12: bool = ParamField(
        byte, "modelDispMask12:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask13: bool = ParamField(
        byte, "modelDispMask13:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask14: bool = ParamField(
        byte, "modelDispMask14:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask15: bool = ParamField(
        byte, "modelDispMask15:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableNeckTurn: bool = ParamField(
        byte, "isEnableNeckTurn:1", bit_count=1, default=False,
        tooltip="Character can turn their neck.",
    )
    DisableRespawnOnRest: bool = ParamField(
        byte, "disableRespawn:1", bit_count=1, default=False,
        tooltip="Prevents character from respawning when you rest at a bonfire, though they will still respawn when "
                "you die or the map is de-loaded unless they are disabled by an event script.",
    )
    IsMoveAnimationWait: bool = ParamField(
        byte, "isMoveAnimWait:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    IsCrowd: bool = ParamField(
        byte, "isCrowd:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="Always false.",
    )
    IsWeakToDivine: bool = ParamField(
        byte, "isWeakSaint:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for skeletons and friends, but not sure how it is actually used to disable their reanimation by "
                "Necromancers.",
    )
    IsWeakToOccult: bool = ParamField(
        byte, "isWeakA:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for all Gods and most NPCs in Anor Londo.",
    )
    IsAbyssal: bool = ParamField(
        byte, "isWeakB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus.",
    )
    CanStealBloodEchoes: bool = ParamField(
        byte, "isEnableDropSoulCapture:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    VowType: int = ParamField(
        byte, "vowType:3", bit_count=3, default=0,
        tooltip="Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone else.",
    )
    DisableInitializeDead: bool = ParamField(
        byte, "disableInitializeDead:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for bosses and non-respawning enemies that are disabled in event scripts, but its effects are "
                "unknown.",
    )
    IsSoulsGetByBoss: bool = ParamField(
        byte, "isSoulGetByBoss:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsMultilingual: bool = ParamField(
        byte, "isMultilingual:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad3:2", bit_count=2)
    ModelDisplayMask16: bool = ParamField(
        byte, "modelDispMask16:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask17: bool = ParamField(
        byte, "modelDispMask17:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask18: bool = ParamField(
        byte, "modelDispMask18:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask19: bool = ParamField(
        byte, "modelDispMask19:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask20: bool = ParamField(
        byte, "modelDispMask20:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask21: bool = ParamField(
        byte, "modelDispMask21:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask22: bool = ParamField(
        byte, "modelDispMask22:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask23: bool = ParamField(
        byte, "modelDispMask23:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask24: bool = ParamField(
        byte, "modelDispMask24:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask25: bool = ParamField(
        byte, "modelDispMask25:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask26: bool = ParamField(
        byte, "modelDispMask26:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask27: bool = ParamField(
        byte, "modelDispMask27:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask28: bool = ParamField(
        byte, "modelDispMask28:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask29: bool = ParamField(
        byte, "modelDispMask29:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask30: bool = ParamField(
        byte, "modelDispMask30:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask31: bool = ParamField(
        byte, "modelDispMask31:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ItemSearchRadius: float = ParamField(
        float, "itemSearchRadius", default=0.0,
        tooltip="TODO",
    )
    NormalChangeModelID: int = ParamField(
        short, "normalChangeModelId", game_type=EquipmentModel, default=-1,
        tooltip="TODO",
    )
    ClothUpdateOffset: int = ParamField(
        sbyte, "clothUpdateOffset", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad4")
    SubHitOffset: float = ParamField(
        float, "subHitOffset", default=0.0,
        tooltip="TODO",
    )
    SubHitHeight: float = ParamField(
        float, "subHitHeight", default=0.0,
        tooltip="TODO",
    )
    SubHitRadius: float = ParamField(
        float, "subHitRadius", default=0.0,
        tooltip="TODO",
    )
    PaintRenderTargetSize: int = ParamField(
        ushort, "paintRenderTargetSize", default=256,
        tooltip="TODO",
    )
    NormalChangeAnimChrID: int = ParamField(
        short, "normalChangeAnimChrId", default=-1,
        tooltip="TODO",
    )
    NeutralPhysicalRegainRate: float = ParamField(
        float, "regainRate_PhysNeutral", default=1.0,
        tooltip="TODO",
    )
    SlashPhysicalRegainRate: float = ParamField(
        float, "regainRate_PhysSlash", default=1.0,
        tooltip="TODO",
    )
    BlowPhysicalRegainRate: float = ParamField(
        float, "regainRate_PhysBlow", default=1.0,
        tooltip="TODO",
    )
    ThrustPhysicalRegainRate: float = ParamField(
        float, "regainRate_PhysThrust", default=1.0,
        tooltip="TODO",
    )
    MagicRegainRate: float = ParamField(
        float, "regainRate_Magic", default=1.0,
        tooltip="TODO",
    )
    FireRegainRate: float = ParamField(
        float, "regainRate_Fire", default=1.0,
        tooltip="TODO",
    )
    LightingRegainRate: float = ParamField(
        float, "regainRate_Thunder", default=1.0,
        tooltip="TODO",
    )
    MaxAnkleAngle: float = ParamField(
        float, "maxAnkleAngle", default=-1.0,
        tooltip="TODO",
    )
