from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NPC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="Multiplied by 1000 and added to non-player behavior lookups (hitboxes, bullets) triggered by TAE.",
    )
    ResistCorrectIdpoison: int = ParamField(
        int, "resistCorrectId_poison", default=-1,
        tooltip="TOOLTIP-TODO",
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
    ItemLotIdenemy: int = ParamField(
        int, "itemLotId_enemy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemLotIdmap: int = ParamField(
        int, "itemLotId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnkleRollAngle: float = ParamField(
        float, "maxAnkleRollAngle", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrHitGroupAndNavimesh: int = ParamField(
        byte, "chrHitGroupAndNavimesh", CHR_HIT_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FaceIconId: int = ParamField(
        byte, "faceIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeactivateDist: int = ParamField(
        short, "deactivateDist", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrActivateConditionParamId: int = ParamField(
        uint, "chrActivateConditionParamId", CHR_ACTIVATE_CONDITION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorHeightLimit: float = ParamField(
        float, "footIkErrorHeightLimit", default=0.0,
        tooltip="TOOLTIP-TODO",
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
    LockGazePoint0: int = ParamField(
        short, "lockGazePoint0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint1: int = ParamField(
        short, "lockGazePoint1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint2: int = ParamField(
        short, "lockGazePoint2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint3: int = ParamField(
        short, "lockGazePoint3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint4: int = ParamField(
        short, "lockGazePoint4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint5: int = ParamField(
        short, "lockGazePoint5", default=-1,
        tooltip="TOOLTIP-TODO",
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
    LockGazePoint6: int = ParamField(
        short, "lockGazePoint6", default=-1,
        tooltip="TOOLTIP-TODO",
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
    Resistsleep: int = ParamField(
        ushort, "resist_sleep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistmadness: int = ParamField(
        ushort, "resist_madness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResist: int = ParamField(
        sbyte, "sleepGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResist: int = ParamField(
        sbyte, "madnessGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint7: int = ParamField(
        short, "lockGazePoint7", default=-1,
        tooltip="TOOLTIP-TODO",
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
        sbyte, "drawType", NPC_DRAW_TYPE, default=0,
        tooltip="TODO",
    )
    CharacterType: int = ParamField(
        byte, "npcType", NPC_TYPE, default=0,
        tooltip="TODO",
    )
    TeamType: int = ParamField(
        byte, "teamType", TEAM_TYPE, default=0,
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
    MaterialSeWeak1: int = ParamField(
        ushort, "materialSe_Weak1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak1: int = ParamField(
        ushort, "materialSfx_Weak1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageType: int = ParamField(
        byte, "partsDamageType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, Seath, "
                "Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise.",
    )
    VowType: int = ParamField(
        byte, "vowType", VOW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
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
    UseUndulationAddAnimFB: bool = ParamField(
        byte, "useUndulationAddAnimFB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakToOccult: bool = ParamField(
        byte, "isWeakA:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for all Gods and most NPCs in Anor Londo.",
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
    IsAbyssal: bool = ParamField(
        byte, "isWeakB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus.",
    )
    IsWeakC: bool = ParamField(
        byte, "isWeakC:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakD: bool = ParamField(
        byte, "isWeakD:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DoesAlwaysUseSpecialTurn: bool = ParamField(
        byte, "doesAlwaysUseSpecialTurn:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsRideAtkTarget: bool = ParamField(
        byte, "isRideAtkTarget:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableStepDispInterpolate: bool = ParamField(
        byte, "isEnableStepDispInterpolate:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStealthTarget: bool = ParamField(
        byte, "isStealthTarget:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DisableInitializeDead: bool = ParamField(
        byte, "disableInitializeDead:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for bosses and non-respawning enemies that are disabled in event scripts, but its effects are "
                "unknown.",
    )
    IsHitRumble: bool = ParamField(
        byte, "isHitRumble:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSmoothTurn: bool = ParamField(
        byte, "isSmoothTurn:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakE: bool = ParamField(
        byte, "isWeakE:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakF: bool = ParamField(
        byte, "isWeakF:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
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
    ChrHitHeight: float = ParamField(
        float, "chrHitHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrHitRadius: float = ParamField(
        float, "chrHitRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialTurnType: int = ParamField(
        byte, "specialTurnType", NPC_SPECIAL_TURN_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulsGetByBoss: bool = ParamField(
        byte, "isSoulGetByBoss:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsBulletOwnerbyObject: bool = ParamField(
        byte, "isBulletOwner_byObject:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseLowHitFootIk: bool = ParamField(
        byte, "isUseLowHitFootIk:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCalculatePvPDamage: bool = ParamField(
        byte, "isCalculatePvPDamage:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHostSyncChr: bool = ParamField(
        byte, "isHostSyncChr:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWeakDamageAnim: bool = ParamField(
        byte, "isSkipWeakDamageAnim:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsKeepHitOnRide: bool = ParamField(
        byte, "isKeepHitOnRide:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSpCollide: bool = ParamField(
        byte, "isSpCollide:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Defdark: int = ParamField(
        ushort, "def_dark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThreatLv: int = ParamField(
        uint, "threatLv", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialTurnDistanceThreshold: float = ParamField(
        float, "specialTurnDistanceThreshold", default=4.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectSfxId: int = ParamField(
        int, "autoFootEffectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe1: int = ParamField(
        ushort, "materialSe1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx1: int = ParamField(
        ushort, "materialSfx1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSeWeak2: int = ParamField(
        ushort, "materialSe_Weak2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak2: int = ParamField(
        ushort, "materialSfx_Weak2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe2: int = ParamField(
        ushort, "materialSe2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx2: int = ParamField(
        ushort, "materialSfx2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID8: int = ParamField(
        int, "spEffectID8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID9: int = ParamField(
        int, "spEffectID9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID10: int = ParamField(
        int, "spEffectID10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID11: int = ParamField(
        int, "spEffectID11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID12: int = ParamField(
        int, "spEffectID12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID13: int = ParamField(
        int, "spEffectID13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID14: int = ParamField(
        int, "spEffectID14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID15: int = ParamField(
        int, "spEffectID15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId1: int = ParamField(
        int, "autoFootEffectDecalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Toughness: int = ParamField(
        uint, "toughness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralDamageCutRate: float = ParamField(
        float, "neutralDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageCutRate: float = ParamField(
        float, "slashDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowDamageCutRate: float = ParamField(
        float, "blowDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageCutRate: float = ParamField(
        float, "thrustDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageCutRate: float = ParamField(
        float, "magicDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageCutRate: float = ParamField(
        float, "fireDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageCutRate: float = ParamField(
        float, "thunderDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float, "darkGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateOffset: int = ParamField(
        sbyte, "clothUpdateOffset", default=0,
        tooltip="TODO",
    )
    NpcPlayerWeightType: int = ParamField(
        byte, "npcPlayerWeightType", NPC_WEIGHT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeModelID: int = ParamField(
        short, "normalChangeModelId", game_type=EquipmentModel, default=-1,
        tooltip="TODO",
    )
    NormalChangeAnimChrID: int = ParamField(
        short, "normalChangeAnimChrId", default=-1,
        tooltip="TODO",
    )
    PaintRenderTargetSize: int = ParamField(
        ushort, "paintRenderTargetSize", default=256,
        tooltip="TODO",
    )
    ResistCorrectIddisease: int = ParamField(
        int, "resistCorrectId_disease", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhantomShaderId: int = ParamField(
        int, "phantomShaderId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayCorrectionParamId: int = ParamField(
        int, "multiPlayCorrectionParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnklePitchAngle: float = ParamField(
        float, "maxAnklePitchAngle", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Resistfreeze: int = ParamField(
        ushort, "resist_freeze", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResist: int = ParamField(
        sbyte, "freezeGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    HpBurnDamageRate: int = ParamField(
        byte, "hpBurnDamageRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockCameraParamId: int = ParamField(
        int, "lockCameraParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID16: int = ParamField(
        int, "spEffectID16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID17: int = ParamField(
        int, "spEffectID17", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID18: int = ParamField(
        int, "spEffectID18", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID19: int = ParamField(
        int, "spEffectID19", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID20: int = ParamField(
        int, "spEffectID20", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID21: int = ParamField(
        int, "spEffectID21", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID22: int = ParamField(
        int, "spEffectID22", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID23: int = ParamField(
        int, "spEffectID23", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID24: int = ParamField(
        int, "spEffectID24", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID25: int = ParamField(
        int, "spEffectID25", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID26: int = ParamField(
        int, "spEffectID26", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID27: int = ParamField(
        int, "spEffectID27", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID28: int = ParamField(
        int, "spEffectID28", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID29: int = ParamField(
        int, "spEffectID29", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID30: int = ParamField(
        int, "spEffectID30", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID31: int = ParamField(
        int, "spEffectID31", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DisableLockOnAng: float = ParamField(
        float, "disableLockOnAng", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothOffLodLevel: int = ParamField(
        sbyte, "clothOffLodLevel", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsUseFootIKNormalByUnduration: bool = ParamField(
        byte, "isUseFootIKNormalByUnduration:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AttachHitInitializeDead: bool = ParamField(
        byte, "attachHitInitializeDead:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeGroupRewardCheck: bool = ParamField(
        byte, "excludeGroupRewardCheck:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly212: bool = ParamField(
        byte, "enableAILockDmyPoly_212:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly213: bool = ParamField(
        byte, "enableAILockDmyPoly_213:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly214: bool = ParamField(
        byte, "enableAILockDmyPoly_214:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateOpenxb1: bool = ParamField(
        byte, "disableActivateOpen_xb1:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateLegacyxb1: bool = ParamField(
        byte, "disableActivateLegacy_xb1:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryParamId: int = ParamField(
        short, "estusFlaskRecoveryParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RoleNameId: int = ParamField(
        int, "roleNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskLotPoint: int = ParamField(
        ushort, "estusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskLotPoint: int = ParamField(
        ushort, "hpEstusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskLotPoint: int = ParamField(
        ushort, "mpEstusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        ushort, "estusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        ushort, "hpEstusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        ushort, "mpEstusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WanderGhostPhantomId: int = ParamField(
        int, "WanderGhostPhantomId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HearingHeadSize: float = ParamField(
        float, "hearingHeadSize", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    SoundBankId: int = ParamField(
        short, "SoundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForwardUndulationLimit: int = ParamField(
        byte, "forwardUndulationLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SideUndulationLimit: int = ParamField(
        byte, "sideUndulationLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeactiveMoveSpeed: float = ParamField(
        float, "deactiveMoveSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DeactiveMoveDist: float = ParamField(
        float, "deactiveMoveDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableSoundObjDist: float = ParamField(
        float, "enableSoundObjDist", default=48.0,
        tooltip="TOOLTIP-TODO",
    )
    UndulationCorrectGain: float = ParamField(
        float, "undulationCorrectGain", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId2: int = ParamField(
        short, "autoFootEffectDecalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId3: int = ParamField(
        short, "autoFootEffectDecalBaseId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RetargetReferenceChrId: int = ParamField(
        short, "RetargetReferenceChrId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxResBankId: int = ParamField(
        short, "SfxResBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpdateActivatePriolity: float = ParamField(
        float, "updateActivatePriolity", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagAlive: int = ParamField(
        byte, "chrNavimeshFlag_Alive", NPC_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagDead: int = ParamField(
        byte, "chrNavimeshFlag_Dead", NPC_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad7[1]")
    IsConsideredUndead: int = ParamField(
        byte, "isConsideredUndead", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WheelRotType: int = ParamField(
        byte, "wheelRotType", NPC_WHEEL_ROT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WheelRotRadius: float = ParamField(
        float, "wheelRotRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetargetMoveRate: float = ParamField(
        float, "retargetMoveRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LadderWarpOffset: float = ParamField(
        float, "ladderWarpOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LoadAssetId: int = ParamField(
        int, "loadAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverlapCameraDmypolyId: int = ParamField(
        int, "overlapCameraDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId00: int = ParamField(
        int, "residentMaterialExParamId00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId01: int = ParamField(
        int, "residentMaterialExParamId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId02: int = ParamField(
        int, "residentMaterialExParamId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId03: int = ParamField(
        int, "residentMaterialExParamId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId04: int = ParamField(
        int, "residentMaterialExParamId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemLotIdenemy: int = ParamField(
        int, "sleepCollectorItemLotId_enemy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemLotIdmap: int = ParamField(
        int, "sleepCollectorItemLotId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorOnGain: float = ParamField(
        float, "footIkErrorOnGain", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorOffGain: float = ParamField(
        float, "footIkErrorOffGain", default=0.4,
        tooltip="TOOLTIP-TODO",
    )
    SoundAddBankId: int = ParamField(
        short, "SoundAddBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialVariationValue: int = ParamField(
        byte, "materialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialVariationValueWeak: int = ParamField(
        byte, "materialVariationValue_Weak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxPoise: float = ParamField(
        float, "superArmorDurability", default=0.0,
        tooltip="Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, "
                "the character will be staggered.",
    )
    SaRecoveryRate: float = ParamField(
        float, "saRecoveryRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaGuardCutRate: float = ParamField(
        float, "saGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdblood: int = ParamField(
        int, "resistCorrectId_blood", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdcurse: int = ParamField(
        int, "resistCorrectId_curse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdfreeze: int = ParamField(
        int, "resistCorrectId_freeze", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdsleep: int = ParamField(
        int, "resistCorrectId_sleep", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdmadness: int = ParamField(
        int, "resistCorrectId_madness", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrDeadTutorialFlagId: int = ParamField(
        uint, "chrDeadTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StepDispInterpolateTime: float = ParamField(
        float, "stepDispInterpolateTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    StepDispInterpolateTriggerValue: float = ParamField(
        float, "stepDispInterpolateTriggerValue", default=0.6,
        tooltip="TOOLTIP-TODO",
    )
    LockScoreOffset: float = ParamField(
        float, "lockScoreOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(8, "pad12_old[8]")
    DlcGameClearSpEffectID: int = ParamField(
        int, "dlcGameClearSpEffectID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(4, "pad12[4]")
