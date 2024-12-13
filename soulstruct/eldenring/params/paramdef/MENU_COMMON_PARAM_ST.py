from __future__ import annotations

__all__ = ["MENU_COMMON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MENU_COMMON_PARAM_ST(ParamRow):
    SoloPlayDeathToFadeOutTime: float = ParamField(
        float, "soloPlayDeath_ToFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PartyGhostDeathToFadeOutTime: float = ParamField(
        float, "partyGhostDeath_ToFadeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxHpLimit: int = ParamField(
        int, "playerMaxHpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxMpLimit: int = ParamField(
        int, "playerMaxMpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxSpLimit: int = ParamField(
        int, "playerMaxSpLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ActionPanelChangeThresholdVel: float = ParamField(
        float, "actionPanelChangeThreshold_Vel", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ActionPanelChangeThresholdPassTime: float = ParamField(
        float, "actionPanelChangeThreshold_PassTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspace: int = ParamField(
        int, "kgIconVspace", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSelectRadius: float = ParamField(
        float, "worldMapCursorSelectRadius", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "reserved8[4]")
    DecalPosOffsetX: int = ParamField(
        int, "decalPosOffsetX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalPosOffsetY: int = ParamField(
        int, "decalPosOffsetY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TargetStateSearchDurationTime: float = ParamField(
        float, "targetStateSearchDurationTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    TargetStateBattleDurationTime: float = ParamField(
        float, "targetStateBattleDurationTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSpeed: float = ParamField(
        float, "worldMapCursorSpeed", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorFirstDistance: float = ParamField(
        float, "worldMapCursorFirstDistance", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorFirstDelay: float = ParamField(
        float, "worldMapCursorFirstDelay", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorWaitTime: float = ParamField(
        float, "worldMapCursorWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSnapRadius: float = ParamField(
        float, "worldMapCursorSnapRadius", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapCursorSnapTime: float = ParamField(
        float, "worldMapCursorSnapTime", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    ItemGetLogAliveTime: float = ParamField(
        float, "itemGetLogAliveTime", default=0.01,
        tooltip="TOOLTIP-TODO",
    )
    PlayerMaxSaLimit: int = ParamField(
        int, "playerMaxSaLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapIsChangeableLayerEventFlagId: int = ParamField(
        uint, "worldMap_IsChangeableLayerEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapTravelMargin: float = ParamField(
        float, "worldMap_TravelMargin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollBufferTime: float = ParamField(
        float, "systemAnnounceScrollBufferTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollSpeed: int = ParamField(
        int, "systemAnnounceScrollSpeed", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceNoScrollWaitTime: float = ParamField(
        float, "systemAnnounceNoScrollWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SystemAnnounceScrollCount: int = ParamField(
        byte, "systemAnnounceScrollCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(3, "reserved17[3]")
    CompassMemoDispDistance: float = ParamField(
        float, "compassMemoDispDistance", default=50.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassBonfireDispDistance: float = ParamField(
        float, "compassBonfireDispDistance", default=50.0,
        tooltip="TOOLTIP-TODO",
    )
    MarkerGoalThreshold: float = ParamField(
        float, "markerGoalThreshold", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SvSliderStep: float = ParamField(
        float, "svSliderStep", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    PreOpeningMovieWaitSec: float = ParamField(
        float, "preOpeningMovie_WaitSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScale: float = ParamField(
        float, "kgIconScale", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScaleforTable: float = ParamField(
        float, "kgIconScale_forTable", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspaceforTable: int = ParamField(
        int, "kgIconVspace_forTable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconScaleforConfig: float = ParamField(
        float, "kgIconScale_forConfig", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    KgIconVspaceforConfig: int = ParamField(
        int, "kgIconVspace_forConfig", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapSearchRadius: float = ParamField(
        float, "worldMap_SearchRadius", default=256.0,
        tooltip="TOOLTIP-TODO",
    )
    TutorialDisplayTime: float = ParamField(
        float, "tutorialDisplayTime", default=3.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassFriendHostInnerDistance: float = ParamField(
        float, "compassFriendHostInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassEnemyHostInnerDistance: float = ParamField(
        float, "compassEnemyHostInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CompassFriendGuestInnerDistance: float = ParamField(
        float, "compassFriendGuestInnerDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CutsceneKeyGuideAliveTime: float = ParamField(
        float, "cutsceneKeyGuideAliveTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideHpThresholdRatio: float = ParamField(
        float, "autoHideHpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideHpThresholdValue: int = ParamField(
        int, "autoHideHpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideMpThresholdRatio: float = ParamField(
        float, "autoHideMpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideMpThresholdValue: int = ParamField(
        int, "autoHideMpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideSpThresholdRatio: float = ParamField(
        float, "autoHideSpThresholdRatio", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    AutoHideSpThresholdValue: int = ParamField(
        int, "autoHideSpThresholdValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapZoomAnimationTime: float = ParamField(
        float, "worldMapZoomAnimationTime", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapIconScaleMin: float = ParamField(
        float, "worldMapIconScaleMin", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WorldMapTravelMarginPoint: float = ParamField(
        float, "worldMap_TravelMargin_Point", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeLeft: int = ParamField(
        ushort, "enemyTagSafeLeft", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeRight: int = ParamField(
        ushort, "enemyTagSafeRight", default=1920,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeTop: int = ParamField(
        ushort, "enemyTagSafeTop", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnemyTagSafeBottom: int = ParamField(
        ushort, "enemyTagSafeBottom", default=1080,
        tooltip="TOOLTIP-TODO",
    )
    PcHorseHpRecoverDispThreshold: int = ParamField(
        uint, "pcHorseHpRecoverDispThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(32, "reserved33[32]")
