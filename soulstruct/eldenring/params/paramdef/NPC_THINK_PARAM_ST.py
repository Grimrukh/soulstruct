from __future__ import annotations

__all__ = ["NPC_THINK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_THINK_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    LogicID: int = ParamField(
        int, "logicId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BattleID: int = ParamField(
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
    IsNoAvoidHugeEnemy: int = ParamField(
        byte, "isNoAvoidHugeEnemy:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableWeaponOnOff: int = ParamField(
        byte, "enableWeaponOnOff:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetAILockDmyPoly: int = ParamField(
        byte, "targetAILockDmyPoly:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad8:5")
    SpEffectIdRangedAttack: int = ParamField(
        int, "spEffectId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv1ForgetTime: float = ParamField(
        float, "searchTargetLv1ForgetTime", default=5,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetLv2ForgetTime: float = ParamField(
        float, "searchTargetLv2ForgetTime", default=8,
        tooltip="TOOLTIP-TODO",
    )
    RetreatTimeAfterHittingEnemyWall: float = ParamField(
        float, "BackHomeLife_OnHitEneWal", default=5,
        tooltip="TOOLTIP-TODO",
    )
    SightForgetTime: float = ParamField(
        float, "SightTargetForgetTime", default=600,
        tooltip="TOOLTIP-TODO",
    )
    StuckAnimationID: int = ParamField(
        int, "idAttackCannotMove", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HearingDistance: float = ParamField(
        float, "ear_dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallResponseAnimation: int = ParamField(
        int, "callHelp_ActionAnimId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallSendAnimation: int = ParamField(
        int, "callHelp_CallActionId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SightDistance: int = ParamField(
        ushort, "eye_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsGuardAct: int = ParamField(
        byte, "isGuard_Act", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad6[1]")
    HearingCutDistance: int = ParamField(
        ushort, "ear_soundcut_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SmellDistance: int = ParamField(
        ushort, "nose_dist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxRetreatDistance: int = ParamField(
        ushort, "maxBackhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BattleRetreatDistance: int = ParamField(
        ushort, "backhomeDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RetreatBattleStartDistance: int = ParamField(
        ushort, "backhomeBattleDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NonBattleActLife: int = ParamField(
        ushort, "nonBattleActLife", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SearchTimeBeforeRetreat: int = ParamField(
        ushort, "BackHome_LookTargetTime", default=3,
        tooltip="TOOLTIP-TODO",
    )
    SearchDistanceBeforeRetreat: int = ParamField(
        ushort, "BackHome_LookTargetDist", default=10,
        tooltip="TOOLTIP-TODO",
    )
    HearingForgetTime: float = ParamField(
        float, "SoundTargetForgetTime", default=3,
        tooltip="TOOLTIP-TODO",
    )
    BattleStartDistance: int = ParamField(
        ushort, "BattleStartDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpGroupID: int = ParamField(
        ushort, "callHelp_MyPeerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallGroupID: int = ParamField(
        ushort, "callHelp_CallPeerId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetSysDamageRate: int = ParamField(
        ushort, "targetSys_DmgEffectRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    TeamAttackEffectivity: int = ParamField(
        byte, "TeamAttackEffectivity", default=25,
        tooltip="TOOLTIP-TODO",
    )
    SightRangeHeight: int = ParamField(
        byte, "eye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightRangeWidth: int = ParamField(
        byte, "eye_angY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableDark: int = ParamField(
        byte, "disableDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaravanRole: int = ParamField(
        byte, "caravanRole", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallTargetMinDistance: int = ParamField(
        byte, "callHelp_CallValidMinDistTarget", default=5,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallFriendMaxDistance: int = ParamField(
        byte, "callHelp_CallValidRange", default=15,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallForgetTime: int = ParamField(
        byte, "callHelp_ForgetTimeByArrival", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallMinWaitTime: int = ParamField(
        byte, "callHelp_MinWaitTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallMaxWaitTime: int = ParamField(
        byte, "callHelp_MaxWaitTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CautionGoalAction: int = ParamField(
        byte, "goalAction_ToCaution", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EarlistenLevel: int = ParamField(
        byte, "ear_listenLevel", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HelpCallReplyType: int = ParamField(
        byte, "callHelp_ReplyBehaviorType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreNavmesh: int = ParamField(
        byte, "disablePathMove", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SkipArrivalVisibleCheck: int = ParamField(
        byte, "skipArrivalVisibleCheck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AdmirerAttribute: int = ParamField(
        byte, "thinkAttr_doAdmirer", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanFallOffEdges: int = ParamField(
        byte, "enableNaviFlg_Edge:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateWideSpaces: int = ParamField(
        byte, "enableNaviFlg_LargeSpace:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateLadders: int = ParamField(
        byte, "enableNaviFlg_Ladder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateHoles: int = ParamField(
        byte, "enableNaviFlg_Hole:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateDoors: int = ParamField(
        byte, "enableNaviFlg_Door:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateInsideWalls: int = ParamField(
        byte, "enableNaviFlg_InSideWall:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableNaviFlgLava: int = ParamField(
        byte, "enableNaviFlg_Lava:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanNavigateOrdinaryEdges: int = ParamField(
        byte, "enableNaviFlg_Edge_Ordinary:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(3, "enableNaviFlg_reserve1[3]")
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
    PlatoonReplyRandomExtraTime: float = ParamField(
        float, "platoonReplyAddRandomTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SearchEyeangX: int = ParamField(
        byte, "searchEye_angX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUpdateBattleSight: int = ParamField(
        byte, "isUpdateBattleSight", default=0,
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
    _Pad5: bytes = ParamPad(16, "pad4[16]")
    SightBackOffsetDistance: int = ParamField(
        ushort, "eye_BackOffsetDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SightBeginDistance: int = ParamField(
        ushort, "eye_BeginDist", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActTypeOnFailedPath: int = ParamField(
        byte, "actTypeOnFailedPath", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToCautionImportant: int = ParamField(
        byte, "goalAction_ToCautionImportant", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShiftAnimeIdRangedAttack: int = ParamField(
        int, "shiftAnimeId_RangedAttack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActTypeOnNonBtlFailedPath: int = ParamField(
        byte, "actTypeOnNonBtlFailedPath", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBuddyAI: int = ParamField(
        byte, "isBuddyAI", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv1: int = ParamField(
        byte, "goalAction_ToSearchLv1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoalActionToSearchLv2: int = ParamField(
        byte, "goalAction_ToSearchLv2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMove: int = ParamField(
        byte, "enableJumpMove", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableLocalSteering: int = ParamField(
        byte, "disableLocalSteering", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisappearGoalAction: int = ParamField(
        byte, "goalAction_ToDisappear", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChangeStateActionToNormal: int = ParamField(
        byte, "changeStateAction_ToNormal", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MemoryTargetForgetTime: float = ParamField(
        float, "MemoryTargetForgetTime", default=150,
        tooltip="TOOLTIP-TODO",
    )
    RangedAttackId: int = ParamField(
        int, "rangedAttackId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonNormalCaution: int = ParamField(
        byte, "useFall_onNormalCaution", default=2,
        tooltip="TOOLTIP-TODO",
    )
    UseFallonSearchBattle: int = ParamField(
        byte, "useFall_onSearchBattle", default=2,
        tooltip="TOOLTIP-TODO",
    )
    EnableJumpMoveonBattle: int = ParamField(
        byte, "enableJumpMove_onBattle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BackToHomeStuckAct: int = ParamField(
        byte, "backToHomeStuckAct", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(4, "pad3[4]")
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
