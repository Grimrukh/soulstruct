from __future__ import annotations

__all__ = ["NETWORK_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class NETWORK_PARAM_ST(ParamRow):
    SignVerticalOffset: float = ParamField(
        float32, "signVerticalOffset", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignPosCorrectionRange: float = ParamField(
        float32, "maxSignPosCorrectionRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SummonTimeoutTime: float = ParamField(
        float32, "summonTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad_0[4]")
    SignPuddleActiveMessageIntervalSec: float = ParamField(
        float32, "signPuddleActiveMessageIntervalSec", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeight0: float = ParamField(
        float32, "keyGuideHeight_0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime1: float = ParamField(
        float32, "reloadSignIntervalTime1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime2: float = ParamField(
        float32, "reloadSignIntervalTime2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignTotalCount0: int = ParamField(
        uint32, "reloadSignTotalCount_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignCellCount0: int = ParamField(
        uint32, "reloadSignCellCount_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    UpdateSignIntervalTime: float = ParamField(
        float32, "updateSignIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveRange0: float = ParamField(
        float32, "basicExclusiveRange_0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveHeight0: float = ParamField(
        float32, "basicExclusiveHeight_0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    PreviewChrWaitingTime: float = ParamField(
        float32, "previewChrWaitingTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignVisibleRange0: float = ParamField(
        float32, "signVisibleRange_0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupHorizontalRange0: int = ParamField(
        uint32, "cellGroupHorizontalRange_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupTopRange0: int = ParamField(
        uint32, "cellGroupTopRange_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupBottomRange0: int = ParamField(
        uint32, "cellGroupBottomRange_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MinWhitePhantomLimitTimeScale: float = ParamField(
        float32, "minWhitePhantomLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinSmallPhantomLimitTimeScale: float = ParamField(
        float32, "minSmallPhantomLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WhiteKeywordLimitTimeScale: float = ParamField(
        float32, "whiteKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SmallKeywordLimitTimeScale: float = ParamField(
        float32, "smallKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BlackKeywordLimitTimeScale: float = ParamField(
        float32, "blackKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DragonKeywordLimitTimeScale: float = ParamField(
        float32, "dragonKeywordLimitTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SingGetMax: int = ParamField(
        uint32, "singGetMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SignDownloadSpan: float = ParamField(
        float32, "signDownloadSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignUpdateSpan: float = ParamField(
        float32, "signUpdateSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "signPad[4]")
    MaxBreakInTargetListCount: int = ParamField(
        uint32, "maxBreakInTargetListCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BreakInRequestIntervalTimeSec: float = ParamField(
        float32, "breakInRequestIntervalTimeSec", default=4.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInRequestTimeOutSec: float = ParamField(
        float32, "breakInRequestTimeOutSec", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakInRequestAreaCount: int = ParamField(
        uint8, "breakInRequestAreaCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(3, "pad_1[3]")
    KeyGuideRange: float = ParamField(
        float32, "keyGuideRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeight1: float = ParamField(
        float32, "keyGuideHeight_1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignTotalCount1: int = ParamField(
        uint32, "reloadSignTotalCount_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadNewSignCellCount: int = ParamField(
        uint32, "reloadNewSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadRandomSignCellCount: int = ParamField(
        uint32, "reloadRandomSignCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignTotalCount0: int = ParamField(
        uint32, "maxSignTotalCount_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignCellCount0: int = ParamField(
        uint32, "maxSignCellCount_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveRange1: float = ParamField(
        float32, "basicExclusiveRange_1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveHeight1: float = ParamField(
        float32, "basicExclusiveHeight_1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignVisibleRange1: float = ParamField(
        float32, "signVisibleRange_1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxWriteSignCount: int = ParamField(
        uint32, "maxWriteSignCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxReadSignCount: int = ParamField(
        uint32, "maxReadSignCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime0: float = ParamField(
        float32, "reloadSignIntervalTime_0", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupHorizontalRange1: int = ParamField(
        uint32, "cellGroupHorizontalRange_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupTopRange1: int = ParamField(
        uint32, "cellGroupTopRange_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupBottomRange1: int = ParamField(
        uint32, "cellGroupBottomRange_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime0: int = ParamField(
        uint32, "lifeTime_0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan0: float = ParamField(
        float32, "downloadSpan_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadEvaluationSpan: float = ParamField(
        float32, "downloadEvaluationSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad_2[4]")
    DeadingGhostStartPosThreshold: float = ParamField(
        float32, "deadingGhostStartPosThreshold", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeight2: float = ParamField(
        float32, "keyGuideHeight_2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideRangePlayer: float = ParamField(
        float32, "keyGuideRangePlayer", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    KeyGuideHeightPlayer: float = ParamField(
        float32, "keyGuideHeightPlayer", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignTotalCount2: int = ParamField(
        uint32, "reloadSignTotalCount_2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignCellCount1: int = ParamField(
        uint32, "reloadSignCellCount_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignTotalCount1: int = ParamField(
        uint32, "maxSignTotalCount_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxSignCellCount1: int = ParamField(
        uint32, "maxSignCellCount_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSignIntervalTime1: float = ParamField(
        float32, "reloadSignIntervalTime_1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignVisibleRange2: float = ParamField(
        float32, "signVisibleRange_2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveRange2: float = ParamField(
        float32, "basicExclusiveRange_2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicExclusiveHeight2: float = ParamField(
        float32, "basicExclusiveHeight_2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupHorizontalRange2: int = ParamField(
        uint32, "cellGroupHorizontalRange_2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupTopRange2: int = ParamField(
        uint32, "cellGroupTopRange_2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupBottomRange2: int = ParamField(
        uint32, "cellGroupBottomRange_2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    LifeTime1: int = ParamField(
        uint32, "lifeTime_1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RecordDeadingGhostTotalTime: float = ParamField(
        float32, "recordDeadingGhostTotalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordDeadingGhostMinTime: float = ParamField(
        float32, "recordDeadingGhostMinTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan1: float = ParamField(
        float32, "downloadSpan_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StatueCreatableDistance: float = ParamField(
        float32, "statueCreatableDistance", default=80.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostTotalCount: int = ParamField(
        uint32, "reloadGhostTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostCellCount: int = ParamField(
        uint32, "reloadGhostCellCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxGhostTotalCount: int = ParamField(
        uint32, "maxGhostTotalCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    DistanceOfBeginRecordVersus: float = ParamField(
        float32, "distanceOfBeginRecordVersus", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistanceOfEndRecordVersus: float = ParamField(
        float32, "distanceOfEndRecordVersus", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateWanderGhostIntervalTime: float = ParamField(
        float32, "updateWanderGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateVersusGhostIntervalTime: float = ParamField(
        float32, "updateVersusGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordWanderingGhostTime: float = ParamField(
        float32, "recordWanderingGhostTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RecordWanderingGhostMinTime: float = ParamField(
        float32, "recordWanderingGhostMinTime", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    UpdateBonfireGhostIntervalTime: float = ParamField(
        float32, "updateBonfireGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayGhostRangeOnView: float = ParamField(
        float32, "replayGhostRangeOnView", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayGhostRangeOutView: float = ParamField(
        float32, "replayGhostRangeOutView", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfireGhostTime: float = ParamField(
        float32, "replayBonfireGhostTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinBonfireGhostValidRange: float = ParamField(
        float32, "minBonfireGhostValidRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxBonfireGhostValidRange: float = ParamField(
        float32, "maxBonfireGhostValidRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinReplayIntervalTime: float = ParamField(
        float32, "minReplayIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxReplayIntervalTime: float = ParamField(
        float32, "maxReplayIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadGhostIntervalTime: float = ParamField(
        float32, "reloadGhostIntervalTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupHorizontalRange3: int = ParamField(
        uint32, "cellGroupHorizontalRange_3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CellGroupTopRange3: int = ParamField(
        uint32, "cellGroupTopRange_3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfirePhantomParamIdForCodename: int = ParamField(
        int32, "replayBonfirePhantomParamIdForCodename", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfireModeRange: float = ParamField(
        float32, "replayBonfireModeRange", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplayBonfirePhantomParamId: int = ParamField(
        int32, "replayBonfirePhantomParamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(4, "ghostpad[4]")
    ReloadVisitListCoolTime: float = ParamField(
        float32, "reloadVisitListCoolTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxCoopBlueSummonCount: int = ParamField(
        uint32, "maxCoopBlueSummonCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxBellGuardSummonCount: int = ParamField(
        uint32, "maxBellGuardSummonCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MaxVisitListCount: int = ParamField(
        uint32, "maxVisitListCount", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchCoopBlueMin: float = ParamField(
        float32, "reloadSearch_CoopBlue_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchCoopBlueMax: float = ParamField(
        float32, "reloadSearch_CoopBlue_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchBellGuardMin: float = ParamField(
        float32, "reloadSearch_BellGuard_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchBellGuardMax: float = ParamField(
        float32, "reloadSearch_BellGuard_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchRatKingMin: float = ParamField(
        float32, "reloadSearch_RatKing_Min", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReloadSearchRatKingMax: float = ParamField(
        float32, "reloadSearch_RatKing_Max", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "visitpad00[8]")
    SrttMaxLimit: float = ParamField(
        float32, "srttMaxLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SrttMeanLimit: float = ParamField(
        float32, "srttMeanLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    SrttMeanDeviationLimit: float = ParamField(
        float32, "srttMeanDeviationLimit", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkPhantomLimitBoostTime: float = ParamField(
        float32, "darkPhantomLimitBoostTime", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    DarkPhantomLimitBoostScale: float = ParamField(
        float32, "darkPhantomLimitBoostScale", default=1000.0,
        tooltip="TOOLTIP-TODO",
    )
    MultiplayDisableLifeTime: float = ParamField(
        float32, "multiplayDisableLifeTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AbyssMultiplayLimit: int = ParamField(
        uint8, "abyssMultiplayLimit", default=10,
        tooltip="TOOLTIP-TODO",
    )
    PhantomWarpMinimumTime: int = ParamField(
        uint8, "phantomWarpMinimumTime", default=5,
        tooltip="TOOLTIP-TODO",
    )
    PhantomReturnDelayTime: int = ParamField(
        uint8, "phantomReturnDelayTime", default=5,
        tooltip="TOOLTIP-TODO",
    )
    TerminateTimeoutTime: int = ParamField(
        uint8, "terminateTimeoutTime", default=30,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointLanDisconnect: int = ParamField(
        uint16, "penaltyPointLanDisconnect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointSignout: int = ParamField(
        uint16, "penaltyPointSignout", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointReboot: int = ParamField(
        uint16, "penaltyPointReboot", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyPointBeginPenalize: int = ParamField(
        uint16, "penaltyPointBeginPenalize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenaltyForgiveItemLimitTime: float = ParamField(
        float32, "penaltyForgiveItemLimitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateCoopBlue: int = ParamField(
        uint8, "allAreaSearchRate_CoopBlue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateVsBlue: int = ParamField(
        uint8, "allAreaSearchRate_VsBlue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AllAreaSearchRateBellGuard: int = ParamField(
        uint8, "allAreaSearchRate_BellGuard", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BloodMessageEvalHealRate: int = ParamField(
        uint8, "bloodMessageEvalHealRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SmallGoldSuccessHostRewardId: int = ParamField(
        uint32, "smallGoldSuccessHostRewardId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DoorInvalidPlayAreaExtents: float = ParamField(
        float32, "doorInvalidPlayAreaExtents", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    SignDisplayMax: int = ParamField(
        uint8, "signDisplayMax", default=10,
        tooltip="TOOLTIP-TODO",
    )
    BloodStainDisplayMax: int = ParamField(
        uint8, "bloodStainDisplayMax", default=7,
        tooltip="TOOLTIP-TODO",
    )
    BloodMessageDisplayMax: int = ParamField(
        uint8, "bloodMessageDisplayMax", default=3,
        tooltip="TOOLTIP-TODO",
    )
    _Pad6: bytes = ParamPad(9, "pad00[9]")
    _Pad7: bytes = ParamPad(32, "pad10[32]")
    SummonMessageInterval: float = ParamField(
        float32, "summonMessageInterval", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostRegisterUpdateTime: float = ParamField(
        float32, "hostRegisterUpdateTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostTimeOutTime: float = ParamField(
        float32, "hostTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestUpdateTime: float = ParamField(
        float32, "guestUpdateTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    GuestPlayerNoTimeOutTime: float = ParamField(
        float32, "guestPlayerNoTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    HostPlayerNoTimeOutTime: float = ParamField(
        float32, "hostPlayerNoTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RequestSearchQuickMatchLimit: int = ParamField(
        uint32, "requestSearchQuickMatchLimit", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AvatarMatchSearchMax: int = ParamField(
        uint32, "AvatarMatchSearchMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyalMatchSearchMin: int = ParamField(
        uint32, "BattleRoyalMatchSearchMin", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyalMatchSearchMax: int = ParamField(
        uint32, "BattleRoyalMatchSearchMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad8: bytes = ParamPad(8, "pad11[8]")
    VisitorListMax: int = ParamField(
        uint32, "VisitorListMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    VisitorTimeOutTime: float = ParamField(
        float32, "VisitorTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan2: float = ParamField(
        float32, "DownloadSpan_2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorGuestRequestMessageIntervalSec: float = ParamField(
        float32, "VisitorGuestRequestMessageIntervalSec", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    WanderGhostIntervalLifeTime: float = ParamField(
        float32, "wanderGhostIntervalLifeTime", default=40.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad9: bytes = ParamPad(12, "pad13[12]")
    YellowMonkTimeOutTime: float = ParamField(
        float32, "YellowMonkTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonkDownloadSpan: float = ParamField(
        float32, "YellowMonkDownloadSpan", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    YellowMonkOverallFlowTimeOutTime: float = ParamField(
        float32, "YellowMonkOverallFlowTimeOutTime", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad10: bytes = ParamPad(4, "pad14_0[4]")
    _Pad11: bytes = ParamPad(8, "pad14_1[8]")
