from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NPC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int32, "behaviorVariationId", default=0,
        tooltip="Multiplied by 1000 and added to non-player behavior lookups (hitboxes, bullets) triggered by TAE.",
    )
    ResistCorrectIdpoison: int = ParamField(
        int32, "resistCorrectId_poison", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NameID: int = ParamField(
        int32, "nameId", default=-1,
        tooltip="Text ID for NPC name that appears attached to NPCs. Only works for invaders and summons.",
    )
    TurnVelocity: float = ParamField(
        float32, "turnVellocity", default=0.0,
        tooltip="Turning velocity of NPC. (Exact effect needs testing.)",
    )
    HitHeight: float = ParamField(
        float32, "hitHeight", default=0.0,
        tooltip="Height of NPC hitbox for collision.",
    )
    HitRadius: float = ParamField(
        float32, "hitRadius", default=0.0,
        tooltip="Radius of NPC hitbox for collision.",
    )
    Weight: int = ParamField(
        uint32, "weight", default=0,
        tooltip="Weight of NPC. Probably has no effect (generall 100).",
    )
    HitYOffset: float = ParamField(
        float32, "hitYOffset", default=0.0,
        tooltip="Vertical offset of NPC hitbox for collision.",
    )
    MaximumHP: int = ParamField(
        uint32, "hp", default=0,
        tooltip="Maximum HP of NPC.",
    )
    MaximumMP: int = ParamField(
        uint32, "mp", default=0,
        tooltip="Maximum MP of NPC. Not used in Dark Souls (generally zero).",
    )
    SoulReward: int = ParamField(
        uint32, "getSoul", default=0,
        tooltip="Amount of souls (before NG+ scaling) rewarded when NPC is killed.",
    )
    ItemLotIdenemy: int = ParamField(
        int32, "itemLotId_enemy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemLotIdmap: int = ParamField(
        int32, "itemLotId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnkleRollAngle: float = ParamField(
        float32, "maxAnkleRollAngle", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrHitGroupAndNavimesh: int = ParamField(
        uint8, "chrHitGroupAndNavimesh", CHR_HIT_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FaceIconId: int = ParamField(
        uint8, "faceIconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeactivateDist: int = ParamField(
        int16, "deactivateDist", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrActivateConditionParamId: int = ParamField(
        uint32, "chrActivateConditionParamId", CHR_ACTIVATE_CONDITION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorHeightLimit: float = ParamField(
        float32, "footIkErrorHeightLimit", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityLotID: int = ParamField(
        int32, "humanityLotId", default=-1,
        tooltip="Starting flag of counter for awarding random humanity (I think). Only used by a few enemies, such as "
                "Hollows and Mass of Souls.",
    )
    SpecialEffectID0: int = ParamField(
        int32, "spEffectID0", game_type=SpecialEffectParam, default=-1,
        tooltip="First passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 5300-5337 range, which modify enemy damage animations (e.g. so bosses stagger less).",
    )
    SpecialEffectID1: int = ParamField(
        int32, "spEffectID1", game_type=SpecialEffectParam, default=-1,
        tooltip="Second passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 5360-5364 range, which further modify enemy damage animations based on poise.",
    )
    SpecialEffectID2: int = ParamField(
        int32, "spEffectID2", game_type=SpecialEffectParam, default=-1,
        tooltip="Third passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 90000-91111 range, which determine status effect immunities. From left to right, the four binary "
                "digits represent poison, toxic, bleed, and curse. 0 means the NPC is immune to that status, and 1 "
                "means they are not immune (though their resistance could be any value).",
    )
    SpecialEffectID3: int = ParamField(
        int32, "spEffectID3", game_type=SpecialEffectParam, default=-1,
        tooltip="Fourth passive special effect that is active on NPC.  This slot is generally reserved for effects in "
                "the 80000-81111 range, which determine immunities to effects that apparently never made it into the "
                "game ('remnant', 'absorption', 'fascination', and 'ineffective').",
    )
    SpecialEffectID4: int = ParamField(
        int32, "spEffectID4", game_type=SpecialEffectParam, default=-1,
        tooltip="Fifth passive special effect that is active on NPC.  This slot is generally reserved for 'levelling' "
                "effects in the 7000-7015 range, which scale enemy stats according to the map they are found in.",
    )
    SpecialEffectID5: int = ParamField(
        int32, "spEffectID5", game_type=SpecialEffectParam, default=-1,
        tooltip="Sixth passive special effect that is active on NPC.  Used for miscellaneous effects, such as "
                "elemental resistance or immunity, animation offset effects, the black phantom effect (7100), etc.",
    )
    SpecialEffectID6: int = ParamField(
        int32, "spEffectID6", game_type=SpecialEffectParam, default=-1,
        tooltip="Seventh passive special effect that is active on NPC.  Used for miscellaneous effects, such as "
                "elemental resistance or immunity, animation offset effects, the black phantom effect (7100), etc.",
    )
    SpecialEffectID7: int = ParamField(
        int32, "spEffectID7", game_type=SpecialEffectParam, default=-1,
        tooltip="Eighth passive special effect that is active on NPC.  This slot is generally reserved for effect "
                "71100, 71110, or 71111. The fourth binary digit determines if the NPC uses the 'immortal system'; "
                "the third binary digit is unknown. Darkwraiths, Hollows, Humanity Phantoms, and Armored Tusks are "
                "some examples of the few NPCs that use 71111; most others use 71110, except bosses.",
    )
    NewGamePlusSpecialEffect: int = ParamField(
        int32, "GameClearSpEffectID", game_type=SpecialEffectParam, default=-1,
        tooltip="Passive special effect that is only applied to the NPC in NG+ and beyond, which are taken from the "
                "range 7401-7415.",
    )
    PhysicalGuardCutRate: float = ParamField(
        float32, "physGuardCutRate", default=0.0,
        tooltip="Percentage reduction in physical damage taken while NPC is guarding.",
    )
    MagicGuardCutRate: float = ParamField(
        float32, "magGuardCutRate", default=0.0,
        tooltip="Percentage reduction in magic damage taken while NPC is guarding.",
    )
    FireGuardCutRate: float = ParamField(
        float32, "fireGuardCutRate", default=0.0,
        tooltip="Percentage reduction in fire damage taken while NPC is guarding.",
    )
    LightningGuardCutRate: float = ParamField(
        float32, "thunGuardCutRate", default=0.0,
        tooltip="Percentage reduction in lightning damage taken while NPC is guarding.",
    )
    AnimationIDOffset: int = ParamField(
        int32, "animIdOffset", default=0,
        tooltip="Offset added to animation requests (e.g. from AI script or event script). If the offset animation is "
                "missing, the original will be used.",
    )
    LockGazePoint0: int = ParamField(
        int16, "lockGazePoint0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint1: int = ParamField(
        int16, "lockGazePoint1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint2: int = ParamField(
        int16, "lockGazePoint2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint3: int = ParamField(
        int16, "lockGazePoint3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint4: int = ParamField(
        int16, "lockGazePoint4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint5: int = ParamField(
        int16, "lockGazePoint5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NetworkWarpDistance: float = ParamField(
        float32, "networkWarpDist", default=0.0,
        tooltip="TODO",
    )
    DebugBehaviorR1: int = ParamField(
        int32, "dbgBehaviorR1", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorL1: int = ParamField(
        int32, "dbgBehaviorL1", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorR2: int = ParamField(
        int32, "dbgBehaviorR2", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorL2: int = ParamField(
        int32, "dbgBehaviorL2", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRL: int = ParamField(
        int32, "dbgBehaviorRL", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRR: int = ParamField(
        int32, "dbgBehaviorRR", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRD: int = ParamField(
        int32, "dbgBehaviorRD", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorRU: int = ParamField(
        int32, "dbgBehaviorRU", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLL: int = ParamField(
        int32, "dbgBehaviorLL", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLR: int = ParamField(
        int32, "dbgBehaviorLR", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLD: int = ParamField(
        int32, "dbgBehaviorLD", default=-1,
        tooltip="TODO",
    )
    DebugBehaviorLU: int = ParamField(
        int32, "dbgBehaviorLU", default=-1,
        tooltip="TODO",
    )
    AnimationIDOffset2: int = ParamField(
        int32, "animIdOffset2", game_type=Animation, default=0,
        tooltip="TODO",
    )
    Part1DamageMultiplier: float = ParamField(
        float32, "partsDamageRate1", default=1.0,
        tooltip="Multiplier for damage taken by part 1 of NPC model.",
    )
    Part2DamageMultiplier: float = ParamField(
        float32, "partsDamageRate2", default=1.0,
        tooltip="Multiplier for damage taken by part 2 of NPC model.",
    )
    Part3DamageMultiplier: float = ParamField(
        float32, "partsDamageRate3", default=1.0,
        tooltip="Multiplier for damage taken by part 3 of NPC model.",
    )
    Part4DamageMultiplier: float = ParamField(
        float32, "partsDamageRate4", default=1.0,
        tooltip="Multiplier for damage taken by part 4 of NPC model.",
    )
    Part5DamageMultiplier: float = ParamField(
        float32, "partsDamageRate5", default=1.0,
        tooltip="Multiplier for damage taken by part 5 of NPC model.",
    )
    Part6DamageMultiplier: float = ParamField(
        float32, "partsDamageRate6", default=1.0,
        tooltip="Multiplier for damage taken by part 6 of NPC model.",
    )
    Part7DamageMultiplier: float = ParamField(
        float32, "partsDamageRate7", default=1.0,
        tooltip="Multiplier for damage taken by part 7 of NPC model.",
    )
    Part8DamageMultiplier: float = ParamField(
        float32, "partsDamageRate8", default=1.0,
        tooltip="Multiplier for damage taken by part 8 of NPC model.",
    )
    WeakPartsDamageMultiplier: float = ParamField(
        float32, "weakPartsDamageRate", default=1.0,
        tooltip="Multiplier for damage taken by weak parts of NPC model.",
    )
    PoiseRecoveryCorrection: float = ParamField(
        float32, "superArmorRecoverCorrection", default=0.0,
        tooltip="Change to poise recovery rate. Only the Chained Prisoner uses a non-zero value in vanilla(-0.2).",
    )
    StaggerKnockbackDistance: float = ParamField(
        float32, "superArmorBrakeKnockbackDist", default=0.0,
        tooltip="Stagger knockback distance when NPC's poise is broken.",
    )
    MaxStamina: int = ParamField(
        uint16, "stamina", default=0,
        tooltip="Maximum stamina of NPC.",
    )
    StaminaRecoveryBaseSpeed: int = ParamField(
        uint16, "staminaRecoverBaseVel", default=0,
        tooltip="Base speed of NPC's stamina recovery.",
    )
    PhysicalDefense: int = ParamField(
        uint16, "def_phys", default=0,
        tooltip="Base defense applied to all physical attacks.",
    )
    SlashDefense: int = ParamField(
        int16, "def_slash", default=0,
        tooltip="Base defense added against slashing physical attacks.",
    )
    StrikeDefense: int = ParamField(
        int16, "def_blow", default=0,
        tooltip="Base defense added against striking physical attacks.",
    )
    ThrustDefense: int = ParamField(
        int16, "def_thrust", default=0,
        tooltip="Base defense added against thrusting physical attacks.",
    )
    MagicDefense: int = ParamField(
        uint16, "def_mag", default=0,
        tooltip="Base defense added against magic attacks.",
    )
    FireDefense: int = ParamField(
        uint16, "def_fire", default=0,
        tooltip="Base defense added against fire attacks.",
    )
    LightningDefense: int = ParamField(
        uint16, "def_thunder", default=0,
        tooltip="Base defense added against lightning attacks.",
    )
    DefenseRepelPower: int = ParamField(
        uint16, "defFlickPower", default=0,
        tooltip="Determines how severely an attacker is repelled when they fail to break this NPC's poise. The "
                "Armored Tusk and Chained Prisoner have very high values (50-60), but most NPCs have 0.",
    )
    PoisonResistance: int = ParamField(
        uint16, "resist_poison", default=0,
        tooltip="Base poison resistance.",
    )
    ToxicResistance: int = ParamField(
        uint16, "resist_desease", default=0,
        tooltip="Base toxic resistance.",
    )
    BleedResistance: int = ParamField(
        uint16, "resist_blood", default=0,
        tooltip="Base bleed resistance.",
    )
    CurseResistance: int = ParamField(
        uint16, "resist_curse", default=0,
        tooltip="Base curse resistance.",
    )
    GhostModelID: int = ParamField(
        int16, "ghostModelId", game_type=EquipmentModel, default=-1,
        tooltip="Model to be used when this quest-related NPC appears as a ghost to other players. Defaults to -1 for "
                "almost all standard enemies, which means they do not appear as a ghost to others.",
    )
    NormalChangeResourceID: int = ParamField(
        int16, "normalChangeResouceId", default=-1,
        tooltip="Unknown. Always -1.",
    )
    GuardAngle: int = ParamField(
        int16, "guardAngle", default=0,
        tooltip="Zero for every NPC except the Phalanx Hollow (20).",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        int16, "slashGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        int16, "blowGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        int16, "thrustGuardCutRate", default=0,
        tooltip="Always zero.",
    )
    LockGazePoint6: int = ParamField(
        int16, "lockGazePoint6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeTextureChrID: int = ParamField(
        int16, "normalChangeTexChrId", default=-1,
        tooltip="Unknown. Used for only some NPCs, where it is generally set to a number close to the NPC's character "
                "model ID.",
    )
    ItemDropAppearance: int = ParamField(
        uint16, "dropType", NPC_ITEMDROP_TYPE, default=0,
        tooltip="Determines appearance of dropped items. 0 means the item appears to glow faintly from inside the "
                "NPC's body (e.g. Rat, Mushroom Child/Parent, Ent) and 1 means the item is a clear white orb just "
                "like regular treasure on corpses (most NPCs).",
    )
    KnockbackRate: int = ParamField(
        uint8, "knockbackRate", default=0,
        tooltip="TODO",
    )
    KnockbackID: int = ParamField(
        uint8, "knockbackParamId", game_type=KnockbackParam, default=0,
        tooltip="Knockback parameters were abandoned after Demons' Souls. A param table for Knockback is still "
                "present but is not accessible in the GUI.",
    )
    FallDamageReduction: int = ParamField(
        uint8, "fallDamageDump", default=0,
        tooltip="Percentage of fall damage to ignore.",
    )
    StaminaGuardDefense: int = ParamField(
        uint8, "staminaGuardDef", default=0,
        tooltip="Always set to zero in the game, but presumably, increasing it will reduce the amount of stamina lost "
                "when this NPC blocks an attack.",
    )
    Resistsleep: int = ParamField(
        uint16, "resist_sleep", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistmadness: int = ParamField(
        uint16, "resist_madness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SleepGuardResist: int = ParamField(
        int8, "sleepGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MadnessGuardResist: int = ParamField(
        int8, "madnessGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint7: int = ParamField(
        int16, "lockGazePoint7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MPRecoveryBaseSpeed: int = ParamField(
        uint8, "mpRecoverBaseVel", default=0,
        tooltip="Unknown effect, likely none. Set to zero for NPC parts (tails and Hydra heads) and 10 for everyone "
                "else.",
    )
    RepelDamageCutRate: int = ParamField(
        uint8, "flickDamageCutRate", default=0,
        tooltip="Unknown effect, but it is set to zero for most enemies, 50 for very heavy enemies like Great Stone "
                "Knights and Titanite Demons, and 100 for Mimics.",
    )
    DefaultLightingParamID: int = ParamField(
        int8, "defaultLodParamId", default=-1,
        tooltip="Default lighting (Lod) parameter entry ID.",
    )
    DrawType: int = ParamField(
        int8, "drawType", NPC_DRAW_TYPE, default=0,
        tooltip="TODO",
    )
    CharacterType: int = ParamField(
        uint8, "npcType", NPC_TYPE, default=0,
        tooltip="TODO",
    )
    TeamType: int = ParamField(
        uint8, "teamType", TEAM_TYPE, default=0,
        tooltip="0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom",
    )
    MoveType: int = ParamField(
        uint8, "moveType", NPC_MOVE_TYPE, default=0,
        tooltip="TODO",
    )
    LockOnDistance: int = ParamField(
        uint8, "lockDist", default=0,
        tooltip="TODO",
    )
    MaterialSeWeak1: int = ParamField(
        uint16, "materialSe_Weak1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak1: int = ParamField(
        uint16, "materialSfx_Weak1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageType: int = ParamField(
        uint8, "partsDamageType", ATK_PARAM_PARTSDMGTYPE, default=0,
        tooltip="Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, Seath, "
                "Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise.",
    )
    VowType: int = ParamField(
        uint8, "vowType", VOW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLevel: int = ParamField(
        int8, "guardLevel", default=0,
        tooltip="Set to 4 for enemies who can guard (including Manus), except Giant Skeletons, who have a value of 3. "
                "All other NPCs have zero.",
    )
    BurnSFXType: int = ParamField(
        uint8, "burnSfxType", NPC_BURN_TYPE, default=0,
        tooltip="Set to 1 for Slimes and Undead Dragons, and 0 for everyone else.",
    )
    PoisonGuardResistance: int = ParamField(
        int8, "poisonGuardResist", default=0,
        tooltip="Added poison resistance while guarding.",
    )
    ToxicGuardResistance: int = ParamField(
        int8, "diseaseGuardResist", default=0,
        tooltip="Added toxic resistance while guarding.",
    )
    BleedGuardResistance: int = ParamField(
        int8, "bloodGuardResist", default=0,
        tooltip="Added bleed resistance while guarding.",
    )
    CurseGuardResistance: int = ParamField(
        int8, "curseGuardResist", default=0,
        tooltip="Added curse resistance while guarding.",
    )
    ParryAttack: int = ParamField(
        uint8, "parryAttack", default=0,
        tooltip="Always zero.",
    )
    ParryDefense: int = ParamField(
        uint8, "parryDefence", default=0,
        tooltip="Always zero.",
    )
    SFXSize: int = ParamField(
        uint8, "sfxSize", NPC_SFX_SIZE, default=0,
        tooltip="Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise.",
    )
    PushOutCameraRegionRadius: int = ParamField(
        uint8, "pushOutCamRegionRadius", default=12,
        tooltip="Always zero.",
    )
    HitStopType: int = ParamField(
        uint8, "hitStopType", NPC_HITSTOP_TYPE, default=0,
        tooltip="Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely related to AI triggers.",
    )
    LadderEndCheckOffsetTop: int = ParamField(
        uint8, "ladderEndChkOffsetTop", default=15,
        tooltip="Not something you want to mess with.",
    )
    LadderEndCheckOffsetBottom: int = ParamField(
        uint8, "ladderEndChkOffsetLow", default=8,
        tooltip="Not something you want to mess with.",
    )
    UseRagdollCameraHit: bool = ParamField(
        uint8, "useRagdollCamHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    DisableClothRigidHit: bool = ParamField(
        uint8, "disableClothRigidHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    UseUndulationAddAnimFB: bool = ParamField(
        uint8, "useUndulationAddAnimFB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakToOccult: bool = ParamField(
        uint8, "isWeakA:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for all Gods and most NPCs in Anor Londo.",
    )
    IsGhost: bool = ParamField(
        uint8, "isGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsNoDamageMotion: bool = ParamField(
        uint8, "isNoDamageMotion:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsUnduration: bool = ParamField(
        uint8, "isUnduration:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsChangeWanderGhost: bool = ParamField(
        uint8, "isChangeWanderGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="Always false.",
    )
    ModelDisplayMask0: bool = ParamField(
        uint8, "modelDispMask0:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask1: bool = ParamField(
        uint8, "modelDispMask1:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask2: bool = ParamField(
        uint8, "modelDispMask2:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask3: bool = ParamField(
        uint8, "modelDispMask3:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask4: bool = ParamField(
        uint8, "modelDispMask4:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask5: bool = ParamField(
        uint8, "modelDispMask5:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask6: bool = ParamField(
        uint8, "modelDispMask6:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask7: bool = ParamField(
        uint8, "modelDispMask7:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask8: bool = ParamField(
        uint8, "modelDispMask8:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask9: bool = ParamField(
        uint8, "modelDispMask9:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask10: bool = ParamField(
        uint8, "modelDispMask10:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask11: bool = ParamField(
        uint8, "modelDispMask11:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask12: bool = ParamField(
        uint8, "modelDispMask12:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask13: bool = ParamField(
        uint8, "modelDispMask13:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask14: bool = ParamField(
        uint8, "modelDispMask14:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask15: bool = ParamField(
        uint8, "modelDispMask15:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    EnableNeckTurn: bool = ParamField(
        uint8, "isEnableNeckTurn:1", bit_count=1, default=False,
        tooltip="Character can turn their neck.",
    )
    DisableRespawnOnRest: bool = ParamField(
        uint8, "disableRespawn:1", bit_count=1, default=False,
        tooltip="Prevents character from respawning when you rest at a bonfire, though they will still respawn when "
                "you die or the map is de-loaded unless they are disabled by an event script.",
    )
    IsMoveAnimationWait: bool = ParamField(
        uint8, "isMoveAnimWait:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    IsCrowd: bool = ParamField(
        uint8, "isCrowd:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="Always false.",
    )
    IsAbyssal: bool = ParamField(
        uint8, "isWeakB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus.",
    )
    IsWeakC: bool = ParamField(
        uint8, "isWeakC:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakD: bool = ParamField(
        uint8, "isWeakD:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DoesAlwaysUseSpecialTurn: bool = ParamField(
        uint8, "doesAlwaysUseSpecialTurn:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsRideAtkTarget: bool = ParamField(
        uint8, "isRideAtkTarget:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableStepDispInterpolate: bool = ParamField(
        uint8, "isEnableStepDispInterpolate:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsStealthTarget: bool = ParamField(
        uint8, "isStealthTarget:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DisableInitializeDead: bool = ParamField(
        uint8, "disableInitializeDead:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="True for bosses and non-respawning enemies that are disabled in event scripts, but its effects are "
                "unknown.",
    )
    IsHitRumble: bool = ParamField(
        uint8, "isHitRumble:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSmoothTurn: bool = ParamField(
        uint8, "isSmoothTurn:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakE: bool = ParamField(
        uint8, "isWeakE:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakF: bool = ParamField(
        uint8, "isWeakF:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask16: bool = ParamField(
        uint8, "modelDispMask16:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask17: bool = ParamField(
        uint8, "modelDispMask17:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask18: bool = ParamField(
        uint8, "modelDispMask18:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask19: bool = ParamField(
        uint8, "modelDispMask19:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask20: bool = ParamField(
        uint8, "modelDispMask20:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask21: bool = ParamField(
        uint8, "modelDispMask21:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask22: bool = ParamField(
        uint8, "modelDispMask22:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask23: bool = ParamField(
        uint8, "modelDispMask23:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask24: bool = ParamField(
        uint8, "modelDispMask24:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask25: bool = ParamField(
        uint8, "modelDispMask25:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask26: bool = ParamField(
        uint8, "modelDispMask26:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask27: bool = ParamField(
        uint8, "modelDispMask27:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask28: bool = ParamField(
        uint8, "modelDispMask28:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask29: bool = ParamField(
        uint8, "modelDispMask29:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask30: bool = ParamField(
        uint8, "modelDispMask30:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ModelDisplayMask31: bool = ParamField(
        uint8, "modelDispMask31:1", bit_count=1, default=False,
        tooltip="TODO",
    )
    ItemSearchRadius: float = ParamField(
        float32, "itemSearchRadius", default=0.0,
        tooltip="TODO",
    )
    ChrHitHeight: float = ParamField(
        float32, "chrHitHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrHitRadius: float = ParamField(
        float32, "chrHitRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialTurnType: int = ParamField(
        uint8, "specialTurnType", NPC_SPECIAL_TURN_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulsGetByBoss: bool = ParamField(
        uint8, "isSoulGetByBoss:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TODO",
    )
    IsBulletOwnerbyObject: bool = ParamField(
        uint8, "isBulletOwner_byObject:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseLowHitFootIk: bool = ParamField(
        uint8, "isUseLowHitFootIk:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCalculatePvPDamage: bool = ParamField(
        uint8, "isCalculatePvPDamage:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHostSyncChr: bool = ParamField(
        uint8, "isHostSyncChr:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWeakDamageAnim: bool = ParamField(
        uint8, "isSkipWeakDamageAnim:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsKeepHitOnRide: bool = ParamField(
        uint8, "isKeepHitOnRide:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSpCollide: bool = ParamField(
        uint8, "isSpCollide:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Defdark: int = ParamField(
        uint16, "def_dark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThreatLv: int = ParamField(
        uint32, "threatLv", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialTurnDistanceThreshold: float = ParamField(
        float32, "specialTurnDistanceThreshold", default=4.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectSfxId: int = ParamField(
        int32, "autoFootEffectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe1: int = ParamField(
        uint16, "materialSe1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx1: int = ParamField(
        uint16, "materialSfx1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSeWeak2: int = ParamField(
        uint16, "materialSe_Weak2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak2: int = ParamField(
        uint16, "materialSfx_Weak2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe2: int = ParamField(
        uint16, "materialSe2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx2: int = ParamField(
        uint16, "materialSfx2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID8: int = ParamField(
        int32, "spEffectID8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID9: int = ParamField(
        int32, "spEffectID9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID10: int = ParamField(
        int32, "spEffectID10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID11: int = ParamField(
        int32, "spEffectID11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID12: int = ParamField(
        int32, "spEffectID12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID13: int = ParamField(
        int32, "spEffectID13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID14: int = ParamField(
        int32, "spEffectID14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID15: int = ParamField(
        int32, "spEffectID15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId1: int = ParamField(
        int32, "autoFootEffectDecalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Toughness: int = ParamField(
        uint32, "toughness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessRecoverCorrection: float = ParamField(
        float32, "toughnessRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    NeutralDamageCutRate: float = ParamField(
        float32, "neutralDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageCutRate: float = ParamField(
        float32, "slashDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlowDamageCutRate: float = ParamField(
        float32, "blowDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageCutRate: float = ParamField(
        float32, "thrustDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageCutRate: float = ParamField(
        float32, "magicDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageCutRate: float = ParamField(
        float32, "fireDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageCutRate: float = ParamField(
        float32, "thunderDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float32, "darkDamageCutRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float32, "darkGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateOffset: int = ParamField(
        int8, "clothUpdateOffset", default=0,
        tooltip="TODO",
    )
    NpcPlayerWeightType: int = ParamField(
        uint8, "npcPlayerWeightType", NPC_WEIGHT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeModelID: int = ParamField(
        int16, "normalChangeModelId", game_type=EquipmentModel, default=-1,
        tooltip="TODO",
    )
    NormalChangeAnimChrID: int = ParamField(
        int16, "normalChangeAnimChrId", default=-1,
        tooltip="TODO",
    )
    PaintRenderTargetSize: int = ParamField(
        uint16, "paintRenderTargetSize", default=256,
        tooltip="TODO",
    )
    ResistCorrectIddisease: int = ParamField(
        int32, "resistCorrectId_disease", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhantomShaderId: int = ParamField(
        int32, "phantomShaderId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayCorrectionParamId: int = ParamField(
        int32, "multiPlayCorrectionParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxAnklePitchAngle: float = ParamField(
        float32, "maxAnklePitchAngle", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    Resistfreeze: int = ParamField(
        uint16, "resist_freeze", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FreezeGuardResist: int = ParamField(
        int8, "freezeGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpBurnDamageRate: int = ParamField(
        uint8, "hpBurnDamageRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockCameraParamId: int = ParamField(
        int32, "lockCameraParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID16: int = ParamField(
        int32, "spEffectID16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID17: int = ParamField(
        int32, "spEffectID17", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID18: int = ParamField(
        int32, "spEffectID18", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID19: int = ParamField(
        int32, "spEffectID19", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID20: int = ParamField(
        int32, "spEffectID20", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID21: int = ParamField(
        int32, "spEffectID21", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID22: int = ParamField(
        int32, "spEffectID22", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID23: int = ParamField(
        int32, "spEffectID23", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID24: int = ParamField(
        int32, "spEffectID24", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID25: int = ParamField(
        int32, "spEffectID25", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID26: int = ParamField(
        int32, "spEffectID26", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID27: int = ParamField(
        int32, "spEffectID27", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID28: int = ParamField(
        int32, "spEffectID28", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID29: int = ParamField(
        int32, "spEffectID29", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID30: int = ParamField(
        int32, "spEffectID30", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID31: int = ParamField(
        int32, "spEffectID31", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DisableLockOnAng: float = ParamField(
        float32, "disableLockOnAng", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothOffLodLevel: int = ParamField(
        int8, "clothOffLodLevel", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsUseFootIKNormalByUnduration: bool = ParamField(
        uint8, "isUseFootIKNormalByUnduration:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AttachHitInitializeDead: bool = ParamField(
        uint8, "attachHitInitializeDead:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeGroupRewardCheck: bool = ParamField(
        uint8, "excludeGroupRewardCheck:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly212: bool = ParamField(
        uint8, "enableAILockDmyPoly_212:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly213: bool = ParamField(
        uint8, "enableAILockDmyPoly_213:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly214: bool = ParamField(
        uint8, "enableAILockDmyPoly_214:1", NPC_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateOpenxb1: bool = ParamField(
        uint8, "disableActivateOpen_xb1:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateLegacyxb1: bool = ParamField(
        uint8, "disableActivateLegacy_xb1:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryParamId: int = ParamField(
        int16, "estusFlaskRecoveryParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RoleNameId: int = ParamField(
        int32, "roleNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskLotPoint: int = ParamField(
        uint16, "estusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskLotPoint: int = ParamField(
        uint16, "hpEstusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskLotPoint: int = ParamField(
        uint16, "mpEstusFlaskLotPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        uint16, "estusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HpEstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        uint16, "hpEstusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MpEstusFlaskRecoveryfailedLotPointAdd: int = ParamField(
        uint16, "mpEstusFlaskRecovery_failedLotPointAdd", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WanderGhostPhantomId: int = ParamField(
        int32, "WanderGhostPhantomId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HearingHeadSize: float = ParamField(
        float32, "hearingHeadSize", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    SoundBankId: int = ParamField(
        int16, "SoundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForwardUndulationLimit: int = ParamField(
        uint8, "forwardUndulationLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SideUndulationLimit: int = ParamField(
        uint8, "sideUndulationLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DeactiveMoveSpeed: float = ParamField(
        float32, "deactiveMoveSpeed", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DeactiveMoveDist: float = ParamField(
        float32, "deactiveMoveDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableSoundObjDist: float = ParamField(
        float32, "enableSoundObjDist", default=48.0,
        tooltip="TOOLTIP-TODO",
    )
    UndulationCorrectGain: float = ParamField(
        float32, "undulationCorrectGain", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId2: int = ParamField(
        int16, "autoFootEffectDecalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectDecalBaseId3: int = ParamField(
        int16, "autoFootEffectDecalBaseId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RetargetReferenceChrId: int = ParamField(
        int16, "RetargetReferenceChrId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxResBankId: int = ParamField(
        int16, "SfxResBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpdateActivatePriolity: float = ParamField(
        float32, "updateActivatePriolity", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagAlive: int = ParamField(
        uint8, "chrNavimeshFlag_Alive", NPC_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagDead: int = ParamField(
        uint8, "chrNavimeshFlag_Dead", NPC_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsConsideredUndead: int = ParamField(
        uint8, "isConsideredUndead", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WheelRotType: int = ParamField(
        uint8, "wheelRotType", NPC_WHEEL_ROT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WheelRotRadius: float = ParamField(
        float32, "wheelRotRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetargetMoveRate: float = ParamField(
        float32, "retargetMoveRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    LadderWarpOffset: float = ParamField(
        float32, "ladderWarpOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LoadAssetId: int = ParamField(
        int32, "loadAssetId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    OverlapCameraDmypolyId: int = ParamField(
        int32, "overlapCameraDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId00: int = ParamField(
        int32, "residentMaterialExParamId00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId01: int = ParamField(
        int32, "residentMaterialExParamId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId02: int = ParamField(
        int32, "residentMaterialExParamId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId03: int = ParamField(
        int32, "residentMaterialExParamId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentMaterialExParamId04: int = ParamField(
        int32, "residentMaterialExParamId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemLotIdenemy: int = ParamField(
        int32, "sleepCollectorItemLotId_enemy", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SleepCollectorItemLotIdmap: int = ParamField(
        int32, "sleepCollectorItemLotId_map", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorOnGain: float = ParamField(
        float32, "footIkErrorOnGain", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorOffGain: float = ParamField(
        float32, "footIkErrorOffGain", default=0.4,
        tooltip="TOOLTIP-TODO",
    )
    SoundAddBankId: int = ParamField(
        int16, "SoundAddBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialVariationValue: int = ParamField(
        uint8, "materialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialVariationValueWeak: int = ParamField(
        uint8, "materialVariationValue_Weak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxPoise: float = ParamField(
        float32, "superArmorDurability", default=0.0,
        tooltip="Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, "
                "the character will be staggered.",
    )
    SaRecoveryRate: float = ParamField(
        float32, "saRecoveryRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SaGuardCutRate: float = ParamField(
        float32, "saGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdblood: int = ParamField(
        int32, "resistCorrectId_blood", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdcurse: int = ParamField(
        int32, "resistCorrectId_curse", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdfreeze: int = ParamField(
        int32, "resistCorrectId_freeze", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdsleep: int = ParamField(
        int32, "resistCorrectId_sleep", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdmadness: int = ParamField(
        int32, "resistCorrectId_madness", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrDeadTutorialFlagId: int = ParamField(
        uint32, "chrDeadTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StepDispInterpolateTime: float = ParamField(
        float32, "stepDispInterpolateTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    StepDispInterpolateTriggerValue: float = ParamField(
        float32, "stepDispInterpolateTriggerValue", default=0.6,
        tooltip="TOOLTIP-TODO",
    )
    LockScoreOffset: float = ParamField(
        float32, "lockScoreOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DlcGameClearSpEffectID: int = ParamField(
        int32, "dlcGameClearSpEffectID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "pad12[4]")
