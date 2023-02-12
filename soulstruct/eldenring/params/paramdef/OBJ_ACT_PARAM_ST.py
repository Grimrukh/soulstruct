from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class OBJ_ACT_PARAM_ST(ParamRowData):
    PromptMessage: int = ParamField(
        int, "actionEnableMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FailureMessage: int = ParamField(
        int, "actionFailedMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlagForAutomaticSuccess: int = ParamField(
        uint, "spQualifiedPassEventFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerActionAnimation: int = ParamField(
        uint, "playerAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NonPlayerActionAnimation: int = ParamField(
        uint, "chrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxActionDistance: int = ParamField(
        ushort, "validDist", default=150,
        tooltip="TOOLTIP-TODO",
    )
    spQualifiedId: int = ParamField(
        ushort, "spQualifiedId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    spQualifiedId2: int = ParamField(
        ushort, "spQualifiedId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjectActionModelPoint: int = ParamField(
        byte, "objDummyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEventKickSync: int = ParamField(
        byte, "isEventKickSync", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjectActionAnimation: int = ParamField(
        uint, "objAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxPlayerAngle: int = ParamField(
        byte, "validPlayerAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    SuccessCondition1Type: int = ParamField(
        byte, "spQualifiedType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SuccessCondition2Type: int = ParamField(
        byte, "spQualifiedType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxObjectAngle: int = ParamField(
        byte, "validObjAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    CharacterSnapType: int = ParamField(
        byte, "chrSorbType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventTriggerDelay: int = ParamField(
        byte, "eventKickTiming", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
    ActionButtonParamID: int = ParamField(
        int, "actionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnableTreasureDelaySec: float = ParamField(
        float, "enableTreasureDelaySec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PreActionSfxDmypolyId: int = ParamField(
        int, "preActionSfxDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PreActionSfxId: int = ParamField(
        int, "preActionSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(40, "pad2[40]")
