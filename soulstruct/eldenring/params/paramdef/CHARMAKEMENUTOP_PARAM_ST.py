from __future__ import annotations

__all__ = ["CHARMAKEMENUTOP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARMAKEMENUTOP_PARAM_ST(ParamRow):
    CommandType: int = ParamField(
        int, "commandType", CHARMAKEMENU_CMD_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaptionId: int = ParamField(
        int, "captionId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FaceParamId: int = ParamField(
        int, "faceParamId", FACE_PARAM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TableId: int = ParamField(
        int, "tableId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ViewCondition: int = ParamField(
        int, "viewCondition", CHARMAKEMENU_VIEW_CONDITION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PreviewMode: int = ParamField(
        sbyte, "previewMode", CHARMAKEMENU_PREVIEW_MODE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "reserved2[3]")
    TableId2: int = ParamField(
        int, "tableId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefFaceParamId: int = ParamField(
        int, "refFaceParamId", FACE_PARAM, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefTextId: int = ParamField(
        int, "refTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HelpTextId: int = ParamField(
        int, "helpTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagId: int = ParamField(
        uint, "unlockEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "reserved[4]")
