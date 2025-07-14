from __future__ import annotations

__all__ = ["LEVELSYNC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LEVELSYNC_PARAM_ST(ParamRow):
    SCLUA: int = ParamField(
        int16, "SCLUA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SDCLUR: int = ParamField(
        int16, "SDCLUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SDCWLM: int = ParamField(
        int16, "SDCWLM", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLWSUR: int = ParamField(
        uint8, "MLWSUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLWSUA: int = ParamField(
        uint8, "MLWSUA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLRSUR: int = ParamField(
        uint8, "MLRSUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLRSUA: int = ParamField(
        uint8, "MLRSUA", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS0: int = ParamField(
        uint8, "MWLUWS0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS1: int = ParamField(
        uint8, "MWLUWS1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS2: int = ParamField(
        uint8, "MWLUWS2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS3: int = ParamField(
        uint8, "MWLUWS3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS4: int = ParamField(
        uint8, "MWLUWS4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS5: int = ParamField(
        uint8, "MWLUWS5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS6: int = ParamField(
        uint8, "MWLUWS6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS7: int = ParamField(
        uint8, "MWLUWS7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS8: int = ParamField(
        uint8, "MWLUWS8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS9: int = ParamField(
        uint8, "MWLUWS9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS10: int = ParamField(
        uint8, "MWLUWS10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS0: int = ParamField(
        uint8, "MWLURS0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS1: int = ParamField(
        uint8, "MWLURS1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS2: int = ParamField(
        uint8, "MWLURS2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS3: int = ParamField(
        uint8, "MWLURS3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS4: int = ParamField(
        uint8, "MWLURS4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS5: int = ParamField(
        uint8, "MWLURS5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS6: int = ParamField(
        uint8, "MWLURS6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS7: int = ParamField(
        uint8, "MWLURS7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS8: int = ParamField(
        uint8, "MWLURS8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS9: int = ParamField(
        uint8, "MWLURS9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS10: int = ParamField(
        uint8, "MWLURS10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA0: int = ParamField(
        uint8, "MWLUA0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA1: int = ParamField(
        uint8, "MWLUA1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA2: int = ParamField(
        uint8, "MWLUA2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA3: int = ParamField(
        uint8, "MWLUA3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA4: int = ParamField(
        uint8, "MWLUA4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA5: int = ParamField(
        uint8, "MWLUA5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA6: int = ParamField(
        uint8, "MWLUA6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA7: int = ParamField(
        uint8, "MWLUA7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA8: int = ParamField(
        uint8, "MWLUA8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA9: int = ParamField(
        uint8, "MWLUA9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA10: int = ParamField(
        uint8, "MWLUA10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MLASUR: int = ParamField(
        uint8, "MLASUR", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MLASUA: int = ParamField(
        uint8, "MLASUA", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "Pad[3]")
    summonTimeoutTime: float = ParamField(
        float32, "summonTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    singGetMax: int = ParamField(
        uint32, "singGetMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    signDownloadSpan: float = ParamField(
        float32, "signDownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    nitoSignDownloadSpan: float = ParamField(
        float32, "nitoSignDownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    signUpdateSpan: float = ParamField(
        float32, "signUpdateSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    maxBreakInTargetListCount: int = ParamField(
        uint32, "maxBreakInTargetListCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    breakInRequestIntervalTimeSec: float = ParamField(
        float32, "breakInRequestIntervalTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    breakInRequestTimeOutSec: float = ParamField(
        float32, "breakInRequestTimeOutSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignTotalCount_0: int = ParamField(
        uint32, "reloadSignTotalCount_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_0: float = ParamField(
        float32, "reloadSignIntervalTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_1: float = ParamField(
        float32, "reloadSignIntervalTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignTotalCount_1: int = ParamField(
        uint32, "reloadSignTotalCount_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignCellCount: int = ParamField(
        uint32, "reloadSignCellCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_2: float = ParamField(
        float32, "reloadSignIntervalTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostTotalCount: int = ParamField(
        uint32, "reloadGhostTotalCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostCellCount: int = ParamField(
        uint32, "reloadGhostCellCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    maxGhostTotalCount: int = ParamField(
        uint32, "maxGhostTotalCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    updateWanderGhostIntervalTime: float = ParamField(
        float32, "updateWanderGhostIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    minReplayIntervalTime: float = ParamField(
        float32, "minReplayIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    maxReplayIntervalTime: float = ParamField(
        float32, "maxReplayIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostIntervalTime: float = ParamField(
        float32, "reloadGhostIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    replayBonfireModeRange: float = ParamField(
        float32, "replayBonfireModeRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    wanderGhostIntervalLifeTime: float = ParamField(
        float32, "wanderGhostIntervalLifeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    summonMessageInterval: float = ParamField(
        float32, "summonMessageInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    hostRegisterUpdateTime: float = ParamField(
        float32, "hostRegisterUpdateTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    requestSearchQuickMatchLimit: int = ParamField(
        uint32, "requestSearchQuickMatchLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    myTeamInviteTimeoutTime: float = ParamField(
        float32, "myTeamInviteTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorListMax: int = ParamField(
        uint32, "VisitorListMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorTimeOutTime: float = ParamField(
        float32, "VisitorTimeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan: float = ParamField(
        float32, "DownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    bonfireLowerBoundCoolTime: float = ParamField(
        float32, "bonfireLowerBoundCoolTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    bonfireUpperBoundCoolTime: float = ParamField(
        float32, "bonfireUpperBoundCoolTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    resonanceMagicDbDistInterval: float = ParamField(
        float32, "resonanceMagicDbDistInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    inputTimeoutSec: float = ParamField(
        float32, "inputTimeoutSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam1: float = ParamField(
        float32, "generalPurposeParam1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam2: float = ParamField(
        float32, "generalPurposeParam2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam3: float = ParamField(
        float32, "generalPurposeParam3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam4: float = ParamField(
        float32, "generalPurposeParam4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam5: float = ParamField(
        float32, "generalPurposeParam5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_11: int = ParamField(
        uint8, "MWLUWS_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_12: int = ParamField(
        uint8, "MWLUWS_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_13: int = ParamField(
        uint8, "MWLUWS_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_14: int = ParamField(
        uint8, "MWLUWS_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_15: int = ParamField(
        uint8, "MWLUWS_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_11: int = ParamField(
        uint8, "MWLURS_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_12: int = ParamField(
        uint8, "MWLURS_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_13: int = ParamField(
        uint8, "MWLURS_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_14: int = ParamField(
        uint8, "MWLURS_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_15: int = ParamField(
        uint8, "MWLURS_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_11: int = ParamField(
        uint8, "MWLUAR_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_12: int = ParamField(
        uint8, "MWLUAR_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_13: int = ParamField(
        uint8, "MWLUAR_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_14: int = ParamField(
        uint8, "MWLUAR_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_15: int = ParamField(
        uint8, "MWLUAR_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam6: int = ParamField(
        uint8, "generalPurposeParam6", default=0,
        tooltip="TOOLTIP-TODO",
    )
