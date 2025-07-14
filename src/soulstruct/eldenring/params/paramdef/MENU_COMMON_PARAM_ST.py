from __future__ import annotations

__all__ = ["MENU_COMMON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MENU_COMMON_PARAM_ST(ParamRow):
    SoloPlayDeathToFadeOutTime: float = ParamField(
        float32, "soloPlayDeath_ToFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PartyGhostDeathToFadeOutTime: float = ParamField(
        float32, "partyGhostDeath_ToFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxHpLimit: int = ParamField(
        int32, "playerMaxHpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxMpLimit: int = ParamField(
        int32, "playerMaxMpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxSpLimit: int = ParamField(
        int32, "playerMaxSpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActionPanelChangeThresholdVel: float = ParamField(
        float32, "actionPanelChangeThreshold_Vel", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ActionPanelChangeThresholdPassTime: float = ParamField(
        float32, "actionPanelChangeThreshold_PassTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspace: int = ParamField(
        int32, "kgIconVspace", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSelectRadius: float = ParamField(
        float32, "worldMapCursorSelectRadius", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserved8[4]")
    DecalPosOffsetX: int = ParamField(
        int32, "decalPosOffsetX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalPosOffsetY: int = ParamField(
        int32, "decalPosOffsetY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetStateSearchDurationTime: float = ParamField(
        float32, "targetStateSearchDurationTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TargetStateBattleDurationTime: float = ParamField(
        float32, "targetStateBattleDurationTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSpeed: float = ParamField(
        float32, "worldMapCursorSpeed", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorFirstDistance: float = ParamField(
        float32, "worldMapCursorFirstDistance", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorFirstDelay: float = ParamField(
        float32, "worldMapCursorFirstDelay", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorWaitTime: float = ParamField(
        float32, "worldMapCursorWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSnapRadius: float = ParamField(
        float32, "worldMapCursorSnapRadius", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSnapTime: float = ParamField(
        float32, "worldMapCursorSnapTime", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    ItemGetLogAliveTime: float = ParamField(
        float32, "itemGetLogAliveTime", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxSaLimit: int = ParamField(
        int32, "playerMaxSaLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapIsChangeableLayerEventFlagId: int = ParamField(
        uint32, "worldMap_IsChangeableLayerEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapTravelMargin: float = ParamField(
        float32, "worldMap_TravelMargin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollBufferTime: float = ParamField(
        float32, "systemAnnounceScrollBufferTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollSpeed: int = ParamField(
        int32, "systemAnnounceScrollSpeed", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceNoScrollWaitTime: float = ParamField(
        float32, "systemAnnounceNoScrollWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollCount: int = ParamField(
        uint8, "systemAnnounceScrollCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "reserved17[3]")
    CompassMemoDispDistance: float = ParamField(
        float32, "compassMemoDispDistance", default=50.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassBonfireDispDistance: float = ParamField(
        float32, "compassBonfireDispDistance", default=50.0,
        tooltip="TOOLTIP-TODO",
    )
    MarkerGoalThreshold: float = ParamField(
        float32, "markerGoalThreshold", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SvSliderStep: float = ParamField(
        float32, "svSliderStep", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    PreOpeningMovieWaitSec: float = ParamField(
        float32, "preOpeningMovie_WaitSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScale: float = ParamField(
        float32, "kgIconScale", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScaleforTable: float = ParamField(
        float32, "kgIconScale_forTable", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspaceforTable: int = ParamField(
        int32, "kgIconVspace_forTable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScaleforConfig: float = ParamField(
        float32, "kgIconScale_forConfig", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspaceforConfig: int = ParamField(
        int32, "kgIconVspace_forConfig", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapSearchRadius: float = ParamField(
        float32, "worldMap_SearchRadius", default=256.0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialDisplayTime: float = ParamField(
        float32, "tutorialDisplayTime", default=3.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassFriendHostInnerDistance: float = ParamField(
        float32, "compassFriendHostInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassEnemyHostInnerDistance: float = ParamField(
        float32, "compassEnemyHostInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassFriendGuestInnerDistance: float = ParamField(
        float32, "compassFriendGuestInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CutsceneKeyGuideAliveTime: float = ParamField(
        float32, "cutsceneKeyGuideAliveTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideHpThresholdRatio: float = ParamField(
        float32, "autoHideHpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideHpThresholdValue: int = ParamField(
        int32, "autoHideHpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideMpThresholdRatio: float = ParamField(
        float32, "autoHideMpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideMpThresholdValue: int = ParamField(
        int32, "autoHideMpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideSpThresholdRatio: float = ParamField(
        float32, "autoHideSpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideSpThresholdValue: int = ParamField(
        int32, "autoHideSpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapZoomAnimationTime: float = ParamField(
        float32, "worldMapZoomAnimationTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapIconScaleMin: float = ParamField(
        float32, "worldMapIconScaleMin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapTravelMarginPoint: float = ParamField(
        float32, "worldMap_TravelMargin_Point", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeLeft: int = ParamField(
        uint16, "enemyTagSafeLeft", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeRight: int = ParamField(
        uint16, "enemyTagSafeRight", default=1920,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeTop: int = ParamField(
        uint16, "enemyTagSafeTop", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeBottom: int = ParamField(
        uint16, "enemyTagSafeBottom", default=1080,
        tooltip="TOOLTIP-TODO",
    )
    PcHorseHpRecoverDispThreshold: int = ParamField(
        uint32, "pcHorseHpRecoverDispThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe0: int = ParamField(
        uint8, "unknown_0xe0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe1: int = ParamField(
        uint8, "unknown_0xe1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe2: int = ParamField(
        uint8, "unknown_0xe2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe3: int = ParamField(
        uint8, "unknown_0xe3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe4: int = ParamField(
        uint8, "unknown_0xe4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe5: int = ParamField(
        uint8, "unknown_0xe5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe6: int = ParamField(
        uint8, "unknown_0xe6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe7: int = ParamField(
        uint8, "unknown_0xe7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe8: int = ParamField(
        uint8, "unknown_0xe8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xe9: int = ParamField(
        uint8, "unknown_0xe9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xea: int = ParamField(
        uint8, "unknown_0xea", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xeb: int = ParamField(
        uint8, "unknown_0xeb", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xec: int = ParamField(
        uint8, "unknown_0xec", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xed: int = ParamField(
        uint8, "unknown_0xed", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xee: int = ParamField(
        uint8, "unknown_0xee", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(17, "reserved33[17]")
