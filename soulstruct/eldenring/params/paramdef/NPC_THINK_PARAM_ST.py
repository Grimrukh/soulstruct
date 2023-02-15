from __future__ import annotations

__all__ = ["NPC_THINK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_THINK_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    LogicId: int = ParamField(
        int, "logicId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BattleGoalID: int = ParamField(
        int, "battleGoalID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SearchEyedist: int = ParamField(
        ushort, "searchEye_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SearchEyeangY: int = ParamField(
        byte, "searchEye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNoAvoidHugeEnemy: bool = ParamField(
        byte, "isNoAvoidHugeEnemy:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWeaponOnOff: bool = ParamField(
        byte, "enableWeaponOnOff:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    TargetAILockDmyPoly: bool = ParamField(
        byte, "targetAILockDmyPoly:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad8:5", bit_count=5)
    SpEffectIdRangedAttack: int = ParamField(
        int, "spEffectId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv1ForgetTime: float = ParamField(
        float, "searchTargetLv1ForgetTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv2ForgetTime: float = ParamField(
        float, "searchTargetLv2ForgetTime", default=8.0,
        tooltip="TOOLTIP-TODO",
    )
    BackHomeLifeOnHitEneWal: float = ParamField(
        float, "BackHomeLife_OnHitEneWal", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    SightTargetForgetTime: float = ParamField(
        float, "SightTargetForgetTime", default=600.0,
        tooltip="TOOLTIP-TODO",
    )
    IdAttackCannotMove: int = ParamField(
        int, "idAttackCannotMove", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Eardist: float = ParamField(
        float, "ear_dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpActionAnimId: int = ParamField(
        int, "callHelp_ActionAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpCallActionId: int = ParamField(
        int, "callHelp_CallActionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Eyedist: int = ParamField(
        ushort, "eye_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGuardAct: int = ParamField(
        byte, "isGuard_Act", BOOL_DODONT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad6[1]")
    Earsoundcutdist: int = ParamField(
        ushort, "ear_soundcut_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Nosedist: int = ParamField(
        ushort, "nose_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxBackhomeDist: int = ParamField(
        ushort, "maxBackhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackhomeDist: int = ParamField(
        ushort, "backhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackhomeBattleDist: int = ParamField(
        ushort, "backhomeBattleDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NonBattleActLife: int = ParamField(
        ushort, "nonBattleActLife", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackHomeLookTargetTime: int = ParamField(
        ushort, "BackHome_LookTargetTime", default=3,
        tooltip="TOOLTIP-TODO",
    )
    BackHomeLookTargetDist: int = ParamField(
        ushort, "BackHome_LookTargetDist", default=10,
        tooltip="TOOLTIP-TODO",
    )
    SoundTargetForgetTime: float = ParamField(
        float, "SoundTargetForgetTime", default=3.0,
        tooltip="TOOLTIP-TODO",
    )
    BattleStartDist: int = ParamField(
        ushort, "BattleStartDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpMyPeerId: int = ParamField(
        ushort, "callHelp_MyPeerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpCallPeerId: int = ParamField(
        ushort, "callHelp_CallPeerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetSysDmgEffectRate: int = ParamField(
        ushort, "targetSys_DmgEffectRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    TeamAttackEffectivity: int = ParamField(
        byte, "TeamAttackEffectivity", default=25,
        tooltip="TOOLTIP-TODO",
    )
    EyeangX: int = ParamField(
        byte, "eye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeangY: int = ParamField(
        byte, "eye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableDark: int = ParamField(
        byte, "disableDark", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaravanRole: int = ParamField(
        byte, "caravanRole", NPC_THINK_CARAVAN_ROLE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpCallValidMinDistTarget: int = ParamField(
        byte, "callHelp_CallValidMinDistTarget", default=5,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpCallValidRange: int = ParamField(
        byte, "callHelp_CallValidRange", default=15,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpForgetTimeByArrival: int = ParamField(
        byte, "callHelp_ForgetTimeByArrival", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpMinWaitTime: int = ParamField(
        byte, "callHelp_MinWaitTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpMaxWaitTime: int = ParamField(
        byte, "callHelp_MaxWaitTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToCaution: int = ParamField(
        byte, "goalAction_ToCaution", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EarlistenLevel: int = ParamField(
        byte, "ear_listenLevel", default=128,
        tooltip="TOOLTIP-TODO",
    )
    CallHelpReplyBehaviorType: int = ParamField(
        byte, "callHelp_ReplyBehaviorType", NPC_THINK_REPLY_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisablePathMove: int = ParamField(
        byte, "disablePathMove", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SkipArrivalVisibleCheck: int = ParamField(
        byte, "skipArrivalVisibleCheck", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThinkAttrdoAdmirer: int = ParamField(
        byte, "thinkAttr_doAdmirer", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgEdge: bool = ParamField(
        byte, "enableNaviFlg_Edge:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgLargeSpace: bool = ParamField(
        byte, "enableNaviFlg_LargeSpace:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgLadder: bool = ParamField(
        byte, "enableNaviFlg_Ladder:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgHole: bool = ParamField(
        byte, "enableNaviFlg_Hole:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgDoor: bool = ParamField(
        byte, "enableNaviFlg_Door:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgInSideWall: bool = ParamField(
        byte, "enableNaviFlg_InSideWall:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgLava: bool = ParamField(
        byte, "enableNaviFlg_Lava:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgEdgeOrdinary: bool = ParamField(
        byte, "enableNaviFlg_Edge_Ordinary:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "enableNaviFlg_reserve1[3]")
    SearchThresholdLv0toLv1: int = ParamField(
        int, "searchThreshold_Lv0toLv1", default=10,
        tooltip="TOOLTIP-TODO",
    )
    SearchThresholdLv1toLv2: int = ParamField(
        int, "searchThreshold_Lv1toLv2", default=70,
        tooltip="TOOLTIP-TODO",
    )
    PlatoonReplyTime: float = ParamField(
        float, "platoonReplyTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PlatoonReplyAddRandomTime: float = ParamField(
        float, "platoonReplyAddRandomTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SearchEyeangX: int = ParamField(
        byte, "searchEye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUpdateBattleSight: int = ParamField(
        byte, "isUpdateBattleSight", BOOL_DODONT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateDist: int = ParamField(
        ushort, "battleEye_updateDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateAngX: int = ParamField(
        byte, "battleEye_updateAngX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleEyeupdateAngY: int = ParamField(
        byte, "battleEye_updateAngY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(16, "pad4[16]")
    EyeBackOffsetDist: int = ParamField(
        ushort, "eye_BackOffsetDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeBeginDist: int = ParamField(
        ushort, "eye_BeginDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActTypeOnFailedPath: int = ParamField(
        byte, "actTypeOnFailedPath", NPC_THINK_ACTTYPE_ON_FAILEDPATH, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToCautionImportant: int = ParamField(
        byte, "goalAction_ToCautionImportant", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShiftAnimeIdRangedAttack: int = ParamField(
        int, "shiftAnimeId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActTypeOnNonBtlFailedPath: int = ParamField(
        byte, "actTypeOnNonBtlFailedPath", NPC_THINK_ACTTYPE_ON_NONBTL_FAILEDPATH, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBuddyAI: int = ParamField(
        byte, "isBuddyAI", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv1: int = ParamField(
        byte, "goalAction_ToSearchLv1", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv2: int = ParamField(
        byte, "goalAction_ToSearchLv2", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMove: int = ParamField(
        byte, "enableJumpMove", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableLocalSteering: int = ParamField(
        byte, "disableLocalSteering", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToDisappear: int = ParamField(
        byte, "goalAction_ToDisappear", NPC_THINK_GOAL_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeStateActionToNormal: int = ParamField(
        byte, "changeStateAction_ToNormal", NPC_THINK_CHANGE_STATE_ACTION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MemoryTargetForgetTime: float = ParamField(
        float, "MemoryTargetForgetTime", default=150.0,
        tooltip="TOOLTIP-TODO",
    )
    RangedAttackId: int = ParamField(
        int, "rangedAttackId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonNormalCaution: int = ParamField(
        byte, "useFall_onNormalCaution", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=2,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonSearchBattle: int = ParamField(
        byte, "useFall_onSearchBattle", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=2,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMoveonBattle: int = ParamField(
        byte, "enableJumpMove_onBattle", NPC_THINK_JUMPUSEREDGE_USE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackToHomeStuckAct: int = ParamField(
        byte, "backToHomeStuckAct", NPC_THINK_BackToHomeStuckAct, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(4, "pad3[4]")
    SoundBehaviorId01: int = ParamField(
        int, "soundBehaviorId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId02: int = ParamField(
        int, "soundBehaviorId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId03: int = ParamField(
        int, "soundBehaviorId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId04: int = ParamField(
        int, "soundBehaviorId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId05: int = ParamField(
        int, "soundBehaviorId05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId06: int = ParamField(
        int, "soundBehaviorId06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId07: int = ParamField(
        int, "soundBehaviorId07", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBehaviorId08: int = ParamField(
        int, "soundBehaviorId08", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOffSpecialEffectId: int = ParamField(
        int, "weaponOffSpecialEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOnSpecialEffectId: int = ParamField(
        int, "weaponOnSpecialEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOffAnimId: int = ParamField(
        int, "weaponOffAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WeaponOnAnimId: int = ParamField(
        int, "weaponOnAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SurpriseAnimId: int = ParamField(
        int, "surpriseAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
