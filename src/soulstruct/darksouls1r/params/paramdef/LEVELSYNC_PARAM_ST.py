from __future__ import annotations

__all__ = ["LEVELSYNC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1r.game_types import *
from soulstruct.darksouls1r.params.enums import *
from soulstruct.utilities.binary import *


class LEVELSYNC_PARAM_ST(ParamRow):
    SCLUA: int = ParamField(
        short, "SCLUA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SDCLUR: int = ParamField(
        short, "SDCLUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SDCWLM: int = ParamField(
        short, "SDCWLM", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLWSUR: int = ParamField(
        byte, "MLWSUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLWSUA: int = ParamField(
        byte, "MLWSUA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLRSUR: int = ParamField(
        byte, "MLRSUR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MLRSUA: int = ParamField(
        byte, "MLRSUA", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS0: int = ParamField(
        byte, "MWLUWS0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS1: int = ParamField(
        byte, "MWLUWS1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS2: int = ParamField(
        byte, "MWLUWS2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS3: int = ParamField(
        byte, "MWLUWS3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS4: int = ParamField(
        byte, "MWLUWS4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS5: int = ParamField(
        byte, "MWLUWS5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS6: int = ParamField(
        byte, "MWLUWS6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS7: int = ParamField(
        byte, "MWLUWS7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS8: int = ParamField(
        byte, "MWLUWS8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS9: int = ParamField(
        byte, "MWLUWS9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS10: int = ParamField(
        byte, "MWLUWS10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS0: int = ParamField(
        byte, "MWLURS0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS1: int = ParamField(
        byte, "MWLURS1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS2: int = ParamField(
        byte, "MWLURS2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS3: int = ParamField(
        byte, "MWLURS3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS4: int = ParamField(
        byte, "MWLURS4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS5: int = ParamField(
        byte, "MWLURS5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS6: int = ParamField(
        byte, "MWLURS6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS7: int = ParamField(
        byte, "MWLURS7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS8: int = ParamField(
        byte, "MWLURS8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS9: int = ParamField(
        byte, "MWLURS9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS10: int = ParamField(
        byte, "MWLURS10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA0: int = ParamField(
        byte, "MWLUA0", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA1: int = ParamField(
        byte, "MWLUA1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA2: int = ParamField(
        byte, "MWLUA2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA3: int = ParamField(
        byte, "MWLUA3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA4: int = ParamField(
        byte, "MWLUA4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA5: int = ParamField(
        byte, "MWLUA5", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA6: int = ParamField(
        byte, "MWLUA6", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA7: int = ParamField(
        byte, "MWLUA7", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA8: int = ParamField(
        byte, "MWLUA8", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA9: int = ParamField(
        byte, "MWLUA9", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MWLUA10: int = ParamField(
        byte, "MWLUA10", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MLASUR: int = ParamField(
        byte, "MLASUR", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MLASUA: int = ParamField(
        byte, "MLASUA", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "Pad[3]")
    summonTimeoutTime: float = ParamField(
        float, "summonTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    singGetMax: int = ParamField(
        uint, "singGetMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    signDownloadSpan: float = ParamField(
        float, "signDownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    nitoSignDownloadSpan: float = ParamField(
        float, "nitoSignDownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    signUpdateSpan: float = ParamField(
        float, "signUpdateSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    maxBreakInTargetListCount: int = ParamField(
        uint, "maxBreakInTargetListCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    breakInRequestIntervalTimeSec: float = ParamField(
        float, "breakInRequestIntervalTimeSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    breakInRequestTimeOutSec: float = ParamField(
        float, "breakInRequestTimeOutSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignTotalCount_0: int = ParamField(
        uint, "reloadSignTotalCount_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_0: float = ParamField(
        float, "reloadSignIntervalTime_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_1: float = ParamField(
        float, "reloadSignIntervalTime_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignTotalCount_1: int = ParamField(
        uint, "reloadSignTotalCount_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignCellCount: int = ParamField(
        uint, "reloadSignCellCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadSignIntervalTime_2: float = ParamField(
        float, "reloadSignIntervalTime_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostTotalCount: int = ParamField(
        uint, "reloadGhostTotalCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostCellCount: int = ParamField(
        uint, "reloadGhostCellCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    maxGhostTotalCount: int = ParamField(
        uint, "maxGhostTotalCount", default=0,
        tooltip="TOOLTIP-TODO",
    )
    updateWanderGhostIntervalTime: float = ParamField(
        float, "updateWanderGhostIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    minReplayIntervalTime: float = ParamField(
        float, "minReplayIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    maxReplayIntervalTime: float = ParamField(
        float, "maxReplayIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    reloadGhostIntervalTime: float = ParamField(
        float, "reloadGhostIntervalTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    replayBonfireModeRange: float = ParamField(
        float, "replayBonfireModeRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    wanderGhostIntervalLifeTime: float = ParamField(
        float, "wanderGhostIntervalLifeTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    summonMessageInterval: float = ParamField(
        float, "summonMessageInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    hostRegisterUpdateTime: float = ParamField(
        float, "hostRegisterUpdateTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    requestSearchQuickMatchLimit: int = ParamField(
        uint, "requestSearchQuickMatchLimit", default=0,
        tooltip="TOOLTIP-TODO",
    )
    myTeamInviteTimeoutTime: float = ParamField(
        float, "myTeamInviteTimeoutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorListMax: int = ParamField(
        uint, "VisitorListMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VisitorTimeOutTime: float = ParamField(
        float, "VisitorTimeOutTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DownloadSpan: float = ParamField(
        float, "DownloadSpan", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    bonfireLowerBoundCoolTime: float = ParamField(
        float, "bonfireLowerBoundCoolTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    bonfireUpperBoundCoolTime: float = ParamField(
        float, "bonfireUpperBoundCoolTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    resonanceMagicDbDistInterval: float = ParamField(
        float, "resonanceMagicDbDistInterval", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    inputTimeoutSec: float = ParamField(
        float, "inputTimeoutSec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam1: float = ParamField(
        float, "generalPurposeParam1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam2: float = ParamField(
        float, "generalPurposeParam2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam3: float = ParamField(
        float, "generalPurposeParam3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam4: float = ParamField(
        float, "generalPurposeParam4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam5: float = ParamField(
        float, "generalPurposeParam5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_11: int = ParamField(
        byte, "MWLUWS_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_12: int = ParamField(
        byte, "MWLUWS_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_13: int = ParamField(
        byte, "MWLUWS_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_14: int = ParamField(
        byte, "MWLUWS_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUWS_15: int = ParamField(
        byte, "MWLUWS_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_11: int = ParamField(
        byte, "MWLURS_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_12: int = ParamField(
        byte, "MWLURS_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_13: int = ParamField(
        byte, "MWLURS_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_14: int = ParamField(
        byte, "MWLURS_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLURS_15: int = ParamField(
        byte, "MWLURS_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_11: int = ParamField(
        byte, "MWLUAR_11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_12: int = ParamField(
        byte, "MWLUAR_12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_13: int = ParamField(
        byte, "MWLUAR_13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_14: int = ParamField(
        byte, "MWLUAR_14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MWLUAR_15: int = ParamField(
        byte, "MWLUAR_15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    generalPurposeParam6: int = ParamField(
        byte, "generalPurposeParam6", default=0,
        tooltip="TOOLTIP-TODO",
    )
