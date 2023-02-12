from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationID: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdpoison: int = ParamField(
        int, "resistCorrectId_poison", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NameID: int = ParamField(
        int, "nameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnVelocity: float = ParamField(
        float, "turnVellocity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitHeight: float = ParamField(
        float, "hitHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitRadius: float = ParamField(
        float, "hitRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Weight: int = ParamField(
        uint, "weight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitYOffset: float = ParamField(
        float, "hitYOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaximumHP: int = ParamField(
        uint, "hp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaximumMP: int = ParamField(
        uint, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SoulReward: int = ParamField(
        uint, "getSoul", default=0,
        tooltip="TOOLTIP-TODO",
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
        float, "maxAnkleRollAngle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ChrHitGroupAndNavimesh: int = ParamField(
        byte, "chrHitGroupAndNavimesh", default=0,
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
        uint, "chrActivateConditionParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorHeightLimit: float = ParamField(
        float, "footIkErrorHeightLimit", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityLotID: int = ParamField(
        int, "humanityLotId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID0: int = ParamField(
        int, "spEffectID0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID1: int = ParamField(
        int, "spEffectID1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID2: int = ParamField(
        int, "spEffectID2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID3: int = ParamField(
        int, "spEffectID3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID4: int = ParamField(
        int, "spEffectID4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID5: int = ParamField(
        int, "spEffectID5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID6: int = ParamField(
        int, "spEffectID6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectID7: int = ParamField(
        int, "spEffectID7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NewGamePlusSpecialEffect: int = ParamField(
        int, "GameClearSpEffectID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalGuardCutRate: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagicGuardCutRate: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRate: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LightningGuardCutRate: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimationIDOffset: int = ParamField(
        int, "animIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorR1: int = ParamField(
        int, "dbgBehaviorR1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorL1: int = ParamField(
        int, "dbgBehaviorL1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorR2: int = ParamField(
        int, "dbgBehaviorR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorL2: int = ParamField(
        int, "dbgBehaviorL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorRL: int = ParamField(
        int, "dbgBehaviorRL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorRR: int = ParamField(
        int, "dbgBehaviorRR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorRD: int = ParamField(
        int, "dbgBehaviorRD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorRU: int = ParamField(
        int, "dbgBehaviorRU", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorLL: int = ParamField(
        int, "dbgBehaviorLL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorLR: int = ParamField(
        int, "dbgBehaviorLR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorLD: int = ParamField(
        int, "dbgBehaviorLD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugBehaviorLU: int = ParamField(
        int, "dbgBehaviorLU", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimationIDOffset2: int = ParamField(
        int, "animIdOffset2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Part1DamageMultiplier: float = ParamField(
        float, "partsDamageRate1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part2DamageMultiplier: float = ParamField(
        float, "partsDamageRate2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part3DamageMultiplier: float = ParamField(
        float, "partsDamageRate3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part4DamageMultiplier: float = ParamField(
        float, "partsDamageRate4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part5DamageMultiplier: float = ParamField(
        float, "partsDamageRate5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part6DamageMultiplier: float = ParamField(
        float, "partsDamageRate6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part7DamageMultiplier: float = ParamField(
        float, "partsDamageRate7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Part8DamageMultiplier: float = ParamField(
        float, "partsDamageRate8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    WeakPartsDamageMultiplier: float = ParamField(
        float, "weakPartsDamageRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    PoiseRecoveryCorrection: float = ParamField(
        float, "superArmorRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StaggerKnockbackDistance: float = ParamField(
        float, "superArmorBrakeKnockbackDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxStamina: int = ParamField(
        ushort, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRecoveryBaseSpeed: int = ParamField(
        ushort, "staminaRecoverBaseVel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalDefense: int = ParamField(
        ushort, "def_phys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDefense: int = ParamField(
        short, "def_slash", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StrikeDefense: int = ParamField(
        short, "def_blow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDefense: int = ParamField(
        short, "def_thrust", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicDefense: int = ParamField(
        ushort, "def_mag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireDefense: int = ParamField(
        ushort, "def_fire", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningDefense: int = ParamField(
        ushort, "def_thunder", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefenseRepelPower: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonResistance: int = ParamField(
        ushort, "resist_poison", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToxicResistance: int = ParamField(
        ushort, "resist_desease", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BleedResistance: int = ParamField(
        ushort, "resist_blood", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseResistance: int = ParamField(
        ushort, "resist_curse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GhostModelID: int = ParamField(
        short, "ghostModelId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeResourceID: int = ParamField(
        short, "normalChangeResouceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageReductionWhenGuarding: int = ParamField(
        short, "slashGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StrikeDamageReductionWhenGuarding: int = ParamField(
        short, "blowGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageReductionWhenGuarding: int = ParamField(
        short, "thrustGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint6: int = ParamField(
        short, "lockGazePoint6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeTextureChrID: int = ParamField(
        short, "normalChangeTexChrId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemDropAppearance: int = ParamField(
        ushort, "dropType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackRate: int = ParamField(
        byte, "knockbackRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackID: int = ParamField(
        byte, "knockbackParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageReduction: int = ParamField(
        byte, "fallDamageDump", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDefense: int = ParamField(
        byte, "staminaGuardDef", default=0,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    RepelDamageCutRate: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefaultLightingParamID: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DrawType: int = ParamField(
        sbyte, "drawType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CharacterType: int = ParamField(
        byte, "npcType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TeamType: int = ParamField(
        byte, "teamType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MoveType: int = ParamField(
        byte, "moveType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockOnDistance: int = ParamField(
        byte, "lockDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSeWeak1: int = ParamField(
        ushort, "materialSe_Weak1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak1: int = ParamField(
        ushort, "materialSfx_Weak1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageType: int = ParamField(
        byte, "partsDamageType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VowType: int = ParamField(
        byte, "vowType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSFXType: int = ParamField(
        byte, "burnSfxType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResistance: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ToxicGuardResistance: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BleedGuardResistance: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResistance: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryAttack: int = ParamField(
        byte, "parryAttack", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryDefense: int = ParamField(
        byte, "parryDefence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SFXSize: int = ParamField(
        byte, "sfxSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PushOutCameraRegionRadius: int = ParamField(
        byte, "pushOutCamRegionRadius", default=12,
        tooltip="TOOLTIP-TODO",
    )
    HitStopType: int = ParamField(
        byte, "hitStopType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LadderEndCheckOffsetTop: int = ParamField(
        byte, "ladderEndChkOffsetTop", default=15,
        tooltip="TOOLTIP-TODO",
    )
    LadderEndCheckOffsetBottom: int = ParamField(
        byte, "ladderEndChkOffsetLow", default=8,
        tooltip="TOOLTIP-TODO",
    )
    UseRagdollCameraHit: int = ParamField(
        byte, "useRagdollCamHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableClothRigidHit: int = ParamField(
        byte, "disableClothRigidHit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseUndulationAddAnimFB: int = ParamField(
        byte, "useUndulationAddAnimFB:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakToOccult: int = ParamField(
        byte, "isWeakA:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGhost: int = ParamField(
        byte, "isGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNoDamageMotion: int = ParamField(
        byte, "isNoDamageMotion:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUnduration: int = ParamField(
        byte, "isUnduration:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsChangeWanderGhost: int = ParamField(
        byte, "isChangeWanderGhost:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask0: int = ParamField(
        byte, "modelDispMask0:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask1: int = ParamField(
        byte, "modelDispMask1:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask2: int = ParamField(
        byte, "modelDispMask2:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask3: int = ParamField(
        byte, "modelDispMask3:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask4: int = ParamField(
        byte, "modelDispMask4:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask5: int = ParamField(
        byte, "modelDispMask5:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask6: int = ParamField(
        byte, "modelDispMask6:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask7: int = ParamField(
        byte, "modelDispMask7:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask8: int = ParamField(
        byte, "modelDispMask8:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask9: int = ParamField(
        byte, "modelDispMask9:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask10: int = ParamField(
        byte, "modelDispMask10:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask11: int = ParamField(
        byte, "modelDispMask11:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask12: int = ParamField(
        byte, "modelDispMask12:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask13: int = ParamField(
        byte, "modelDispMask13:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask14: int = ParamField(
        byte, "modelDispMask14:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask15: int = ParamField(
        byte, "modelDispMask15:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableNeckTurn: int = ParamField(
        byte, "isEnableNeckTurn:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableRespawnOnRest: int = ParamField(
        byte, "disableRespawn:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveAnimationWait: int = ParamField(
        byte, "isMoveAnimWait:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCrowd: int = ParamField(
        byte, "isCrowd:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAbyssal: int = ParamField(
        byte, "isWeakB:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakC: int = ParamField(
        byte, "isWeakC:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakD: int = ParamField(
        byte, "isWeakD:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DoesAlwaysUseSpecialTurn: int = ParamField(
        byte, "doesAlwaysUseSpecialTurn:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRideAtkTarget: int = ParamField(
        byte, "isRideAtkTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableStepDispInterpolate: int = ParamField(
        byte, "isEnableStepDispInterpolate:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStealthTarget: int = ParamField(
        byte, "isStealthTarget:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DisableInitializeDead: int = ParamField(
        byte, "disableInitializeDead:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHitRumble: int = ParamField(
        byte, "isHitRumble:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSmoothTurn: int = ParamField(
        byte, "isSmoothTurn:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakE: int = ParamField(
        byte, "isWeakE:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakF: int = ParamField(
        byte, "isWeakF:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask16: int = ParamField(
        byte, "modelDispMask16:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask17: int = ParamField(
        byte, "modelDispMask17:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask18: int = ParamField(
        byte, "modelDispMask18:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask19: int = ParamField(
        byte, "modelDispMask19:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask20: int = ParamField(
        byte, "modelDispMask20:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask21: int = ParamField(
        byte, "modelDispMask21:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask22: int = ParamField(
        byte, "modelDispMask22:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask23: int = ParamField(
        byte, "modelDispMask23:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask24: int = ParamField(
        byte, "modelDispMask24:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask25: int = ParamField(
        byte, "modelDispMask25:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask26: int = ParamField(
        byte, "modelDispMask26:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask27: int = ParamField(
        byte, "modelDispMask27:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask28: int = ParamField(
        byte, "modelDispMask28:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask29: int = ParamField(
        byte, "modelDispMask29:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask30: int = ParamField(
        byte, "modelDispMask30:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelDisplayMask31: int = ParamField(
        byte, "modelDispMask31:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemSearchRadius: float = ParamField(
        float, "itemSearchRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
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
        byte, "specialTurnType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulsGetByBoss: int = ParamField(
        byte, "isSoulGetByBoss:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBulletOwnerbyObject: int = ParamField(
        byte, "isBulletOwner_byObject:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseLowHitFootIk: int = ParamField(
        byte, "isUseLowHitFootIk:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCalculatePvPDamage: int = ParamField(
        byte, "isCalculatePvPDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHostSyncChr: int = ParamField(
        byte, "isHostSyncChr:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkipWeakDamageAnim: int = ParamField(
        byte, "isSkipWeakDamageAnim:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsKeepHitOnRide: int = ParamField(
        byte, "isKeepHitOnRide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSpCollide: int = ParamField(
        byte, "isSpCollide:1", default=0,
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
        float, "specialTurnDistanceThreshold", default=4,
        tooltip="TOOLTIP-TODO",
    )
    AutoFootEffectSfxId: int = ParamField(
        int, "autoFootEffectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe1: int = ParamField(
        ushort, "materialSe1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx1: int = ParamField(
        ushort, "materialSfx1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSeWeak2: int = ParamField(
        ushort, "materialSe_Weak2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfxWeak2: int = ParamField(
        ushort, "materialSfx_Weak2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSe2: int = ParamField(
        ushort, "materialSe2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialSfx2: int = ParamField(
        ushort, "materialSfx2", default=0,
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
        float, "neutralDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SlashDamageCutRate: float = ParamField(
        float, "slashDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BlowDamageCutRate: float = ParamField(
        float, "blowDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThrustDamageCutRate: float = ParamField(
        float, "thrustDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MagicDamageCutRate: float = ParamField(
        float, "magicDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    FireDamageCutRate: float = ParamField(
        float, "fireDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ThunderDamageCutRate: float = ParamField(
        float, "thunderDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkDamageCutRate: float = ParamField(
        float, "darkDamageCutRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DarkGuardCutRate: float = ParamField(
        float, "darkGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateOffset: int = ParamField(
        sbyte, "clothUpdateOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerWeightType: int = ParamField(
        byte, "npcPlayerWeightType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeModelID: int = ParamField(
        short, "normalChangeModelId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeAnimChrID: int = ParamField(
        short, "normalChangeAnimChrId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PaintRenderTargetSize: int = ParamField(
        ushort, "paintRenderTargetSize", default=256,
        tooltip="TOOLTIP-TODO",
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
        float, "maxAnklePitchAngle", default=-1,
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
    _Pad2: bytes = ParamPad(1, "pad1[1]")
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
    IsUseFootIKNormalByUnduration: int = ParamField(
        byte, "isUseFootIKNormalByUnduration:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttachHitInitializeDead: int = ParamField(
        byte, "attachHitInitializeDead:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeGroupRewardCheck: int = ParamField(
        byte, "excludeGroupRewardCheck:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly212: int = ParamField(
        byte, "enableAILockDmyPoly_212:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly213: int = ParamField(
        byte, "enableAILockDmyPoly_213:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableAILockDmyPoly214: int = ParamField(
        byte, "enableAILockDmyPoly_214:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateOpenxb1: int = ParamField(
        byte, "disableActivateOpen_xb1:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableActivateLegacyxb1: int = ParamField(
        byte, "disableActivateLegacy_xb1:1", default=0,
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
        float, "hearingHeadSize", default=-1,
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
        float, "enableSoundObjDist", default=48,
        tooltip="TOOLTIP-TODO",
    )
    UndulationCorrectGain: float = ParamField(
        float, "undulationCorrectGain", default=0,
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
        float, "updateActivatePriolity", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagAlive: int = ParamField(
        byte, "chrNavimeshFlag_Alive", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrNavimeshFlagDead: int = ParamField(
        byte, "chrNavimeshFlag_Dead", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad7[1]")
    WheelRotType: int = ParamField(
        byte, "wheelRotType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WheelRotRadius: float = ParamField(
        float, "wheelRotRadius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RetargetMoveRate: float = ParamField(
        float, "retargetMoveRate", default=1,
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
        float, "footIkErrorOnGain", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootIkErrorOffGain: float = ParamField(
        float, "footIkErrorOffGain", default=0,
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
        tooltip="TOOLTIP-TODO",
    )
    SaRecoveryRate: float = ParamField(
        float, "saRecoveryRate", default=1,
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
        float, "stepDispInterpolateTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StepDispInterpolateTriggerValue: float = ParamField(
        float, "stepDispInterpolateTriggerValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockScoreOffset: float = ParamField(
        float, "lockScoreOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(8, "pad12[8]")
