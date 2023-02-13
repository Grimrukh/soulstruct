from __future__ import annotations

__all__ = ["NPC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    BehaviorVariationId: int = ParamField(
        int, "behaviorVariationId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResistCorrectIdpoison: int = ParamField(
        int, "resistCorrectId_poison", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NameId: int = ParamField(
        int, "nameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnVellocity: float = ParamField(
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
    Hp: int = ParamField(
        uint, "hp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Mp: int = ParamField(
        uint, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GetSoul: int = ParamField(
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
    HumanityLotId: int = ParamField(
        int, "humanityLotId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID0: int = ParamField(
        int, "spEffectID0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID1: int = ParamField(
        int, "spEffectID1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID2: int = ParamField(
        int, "spEffectID2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID3: int = ParamField(
        int, "spEffectID3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID4: int = ParamField(
        int, "spEffectID4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID5: int = ParamField(
        int, "spEffectID5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID6: int = ParamField(
        int, "spEffectID6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID7: int = ParamField(
        int, "spEffectID7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GameClearSpEffectID: int = ParamField(
        int, "GameClearSpEffectID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhysGuardCutRate: float = ParamField(
        float, "physGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MagGuardCutRate: float = ParamField(
        float, "magGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FireGuardCutRate: float = ParamField(
        float, "fireGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ThunGuardCutRate: float = ParamField(
        float, "thunGuardCutRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AnimIdOffset: int = ParamField(
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
    NetworkWarpDist: float = ParamField(
        float, "networkWarpDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorR1: int = ParamField(
        int, "dbgBehaviorR1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorL1: int = ParamField(
        int, "dbgBehaviorL1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorR2: int = ParamField(
        int, "dbgBehaviorR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorL2: int = ParamField(
        int, "dbgBehaviorL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorRL: int = ParamField(
        int, "dbgBehaviorRL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorRR: int = ParamField(
        int, "dbgBehaviorRR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorRD: int = ParamField(
        int, "dbgBehaviorRD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorRU: int = ParamField(
        int, "dbgBehaviorRU", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorLL: int = ParamField(
        int, "dbgBehaviorLL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorLR: int = ParamField(
        int, "dbgBehaviorLR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorLD: int = ParamField(
        int, "dbgBehaviorLD", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DbgBehaviorLU: int = ParamField(
        int, "dbgBehaviorLU", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimIdOffset2: int = ParamField(
        int, "animIdOffset2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate1: float = ParamField(
        float, "partsDamageRate1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate2: float = ParamField(
        float, "partsDamageRate2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate3: float = ParamField(
        float, "partsDamageRate3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate4: float = ParamField(
        float, "partsDamageRate4", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate5: float = ParamField(
        float, "partsDamageRate5", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate6: float = ParamField(
        float, "partsDamageRate6", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate7: float = ParamField(
        float, "partsDamageRate7", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PartsDamageRate8: float = ParamField(
        float, "partsDamageRate8", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WeakPartsDamageRate: float = ParamField(
        float, "weakPartsDamageRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SuperArmorRecoverCorrection: float = ParamField(
        float, "superArmorRecoverCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SuperArmorBrakeKnockbackDist: float = ParamField(
        float, "superArmorBrakeKnockbackDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Stamina: int = ParamField(
        ushort, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaRecoverBaseVel: int = ParamField(
        ushort, "staminaRecoverBaseVel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defphys: int = ParamField(
        ushort, "def_phys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defslash: int = ParamField(
        short, "def_slash", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defblow: int = ParamField(
        short, "def_blow", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defthrust: int = ParamField(
        short, "def_thrust", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defmag: int = ParamField(
        ushort, "def_mag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Deffire: int = ParamField(
        ushort, "def_fire", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Defthunder: int = ParamField(
        ushort, "def_thunder", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefFlickPower: int = ParamField(
        ushort, "defFlickPower", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistpoison: int = ParamField(
        ushort, "resist_poison", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistdesease: int = ParamField(
        ushort, "resist_desease", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistblood: int = ParamField(
        ushort, "resist_blood", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Resistcurse: int = ParamField(
        ushort, "resist_curse", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GhostModelId: int = ParamField(
        short, "ghostModelId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeResouceId: int = ParamField(
        short, "normalChangeResouceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardAngle: int = ParamField(
        short, "guardAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlashGuardCutRate: int = ParamField(
        short, "slashGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowGuardCutRate: int = ParamField(
        short, "blowGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrustGuardCutRate: int = ParamField(
        short, "thrustGuardCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockGazePoint6: int = ParamField(
        short, "lockGazePoint6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeTexChrId: int = ParamField(
        short, "normalChangeTexChrId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DropType: int = ParamField(
        ushort, "dropType", NPC_ITEMDROP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackRate: int = ParamField(
        byte, "knockbackRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackParamId: int = ParamField(
        byte, "knockbackParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FallDamageDump: int = ParamField(
        byte, "fallDamageDump", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaGuardDef: int = ParamField(
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
    MpRecoverBaseVel: int = ParamField(
        byte, "mpRecoverBaseVel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FlickDamageCutRate: int = ParamField(
        byte, "flickDamageCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefaultLodParamId: int = ParamField(
        sbyte, "defaultLodParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DrawType: int = ParamField(
        sbyte, "drawType", NPC_DRAW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NpcType: int = ParamField(
        byte, "npcType", NPC_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TeamType: int = ParamField(
        byte, "teamType", TEAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MoveType: int = ParamField(
        byte, "moveType", NPC_MOVE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LockDist: int = ParamField(
        byte, "lockDist", default=0,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    VowType: int = ParamField(
        byte, "vowType", VOW_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardLevel: int = ParamField(
        sbyte, "guardLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxType: int = ParamField(
        byte, "burnSfxType", NPC_BURN_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoisonGuardResist: int = ParamField(
        sbyte, "poisonGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DiseaseGuardResist: int = ParamField(
        sbyte, "diseaseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodGuardResist: int = ParamField(
        sbyte, "bloodGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CurseGuardResist: int = ParamField(
        sbyte, "curseGuardResist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryAttack: int = ParamField(
        byte, "parryAttack", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryDefence: int = ParamField(
        byte, "parryDefence", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SfxSize: int = ParamField(
        byte, "sfxSize", NPC_SFX_SIZE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PushOutCamRegionRadius: int = ParamField(
        byte, "pushOutCamRegionRadius", default=12,
        tooltip="TOOLTIP-TODO",
    )
    HitStopType: int = ParamField(
        byte, "hitStopType", NPC_HITSTOP_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LadderEndChkOffsetTop: int = ParamField(
        byte, "ladderEndChkOffsetTop", default=15,
        tooltip="TOOLTIP-TODO",
    )
    LadderEndChkOffsetLow: int = ParamField(
        byte, "ladderEndChkOffsetLow", default=8,
        tooltip="TOOLTIP-TODO",
    )
    UseRagdollCamHit: bool = ParamField(
        byte, "useRagdollCamHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableClothRigidHit: bool = ParamField(
        byte, "disableClothRigidHit:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    UseUndulationAddAnimFB: bool = ParamField(
        byte, "useUndulationAddAnimFB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakA: bool = ParamField(
        byte, "isWeakA:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGhost: bool = ParamField(
        byte, "isGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsNoDamageMotion: bool = ParamField(
        byte, "isNoDamageMotion:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUnduration: bool = ParamField(
        byte, "isUnduration:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsChangeWanderGhost: bool = ParamField(
        byte, "isChangeWanderGhost:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask0: bool = ParamField(
        byte, "modelDispMask0:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask1: bool = ParamField(
        byte, "modelDispMask1:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask2: bool = ParamField(
        byte, "modelDispMask2:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask3: bool = ParamField(
        byte, "modelDispMask3:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask4: bool = ParamField(
        byte, "modelDispMask4:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask5: bool = ParamField(
        byte, "modelDispMask5:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask6: bool = ParamField(
        byte, "modelDispMask6:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask7: bool = ParamField(
        byte, "modelDispMask7:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask8: bool = ParamField(
        byte, "modelDispMask8:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask9: bool = ParamField(
        byte, "modelDispMask9:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask10: bool = ParamField(
        byte, "modelDispMask10:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask11: bool = ParamField(
        byte, "modelDispMask11:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask12: bool = ParamField(
        byte, "modelDispMask12:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask13: bool = ParamField(
        byte, "modelDispMask13:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask14: bool = ParamField(
        byte, "modelDispMask14:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask15: bool = ParamField(
        byte, "modelDispMask15:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableNeckTurn: bool = ParamField(
        byte, "isEnableNeckTurn:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableRespawn: bool = ParamField(
        byte, "disableRespawn:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveAnimWait: bool = ParamField(
        byte, "isMoveAnimWait:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCrowd: bool = ParamField(
        byte, "isCrowd:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWeakB: bool = ParamField(
        byte, "isWeakB:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
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
    ModelDispMask16: bool = ParamField(
        byte, "modelDispMask16:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask17: bool = ParamField(
        byte, "modelDispMask17:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask18: bool = ParamField(
        byte, "modelDispMask18:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask19: bool = ParamField(
        byte, "modelDispMask19:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask20: bool = ParamField(
        byte, "modelDispMask20:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask21: bool = ParamField(
        byte, "modelDispMask21:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask22: bool = ParamField(
        byte, "modelDispMask22:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask23: bool = ParamField(
        byte, "modelDispMask23:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask24: bool = ParamField(
        byte, "modelDispMask24:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask25: bool = ParamField(
        byte, "modelDispMask25:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask26: bool = ParamField(
        byte, "modelDispMask26:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask27: bool = ParamField(
        byte, "modelDispMask27:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask28: bool = ParamField(
        byte, "modelDispMask28:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask29: bool = ParamField(
        byte, "modelDispMask29:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask30: bool = ParamField(
        byte, "modelDispMask30:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ModelDispMask31: bool = ParamField(
        byte, "modelDispMask31:1", bit_count=1, default=False,
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
        byte, "specialTurnType", NPC_SPECIAL_TURN_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSoulGetByBoss: bool = ParamField(
        byte, "isSoulGetByBoss:1", NPC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
        tooltip="TOOLTIP-TODO",
    )
    NpcPlayerWeightType: int = ParamField(
        byte, "npcPlayerWeightType", NPC_WEIGHT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeModelId: int = ParamField(
        short, "normalChangeModelId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalChangeAnimChrId: int = ParamField(
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
    SuperArmorDurability: float = ParamField(
        float, "superArmorDurability", default=0.0,
        tooltip="TOOLTIP-TODO",
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
    _Pad3: bytes = ParamPad(8, "pad12[8]")
