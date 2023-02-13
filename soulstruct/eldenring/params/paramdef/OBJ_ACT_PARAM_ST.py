from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class OBJ_ACT_PARAM_ST(ParamRow):
    ActionEnableMsgId: int = ParamField(
        int, "actionEnableMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ActionFailedMsgId: int = ParamField(
        int, "actionFailedMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedPassEventFlag: int = ParamField(
        uint, "spQualifiedPassEventFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PlayerAnimId: int = ParamField(
        uint, "playerAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrAnimId: int = ParamField(
        uint, "chrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ValidDist: int = ParamField(
        ushort, "validDist", default=150,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedId: int = ParamField(
        ushort, "spQualifiedId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedId2: int = ParamField(
        ushort, "spQualifiedId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjDummyId: int = ParamField(
        byte, "objDummyId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEventKickSync: int = ParamField(
        byte, "isEventKickSync", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjAnimId: int = ParamField(
        uint, "objAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ValidPlayerAngle: int = ParamField(
        byte, "validPlayerAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedType: int = ParamField(
        byte, "spQualifiedType", OBJACT_SP_QUALIFIED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedType2: int = ParamField(
        byte, "spQualifiedType2", OBJACT_SP_QUALIFIED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ValidObjAngle: int = ParamField(
        byte, "validObjAngle", default=30,
        tooltip="TOOLTIP-TODO",
    )
    ChrSorbType: int = ParamField(
        byte, "chrSorbType", OBJACT_CHR_SORB_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventKickTiming: int = ParamField(
        byte, "eventKickTiming", OBJACT_EVENT_KICK_TIMING, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
    ActionButtonParamId: int = ParamField(
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
