from __future__ import annotations

__all__ = ["CHARMAKEMENUTOP_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHARMAKEMENUTOP_PARAM_ST(ParamRow):
    CommandType: int = ParamField(
        int32, "commandType", CHARMAKEMENU_CMD_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CaptionId: int = ParamField(
        int32, "captionId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FaceParamId: int = ParamField(
        int32, "faceParamId", FACE_PARAM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TableId: int = ParamField(
        int32, "tableId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ViewCondition: int = ParamField(
        int32, "viewCondition", CHARMAKEMENU_VIEW_CONDITION, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PreviewMode: int = ParamField(
        int8, "previewMode", CHARMAKEMENU_PREVIEW_MODE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "reserved2[3]")
    TableId2: int = ParamField(
        int32, "tableId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefFaceParamId: int = ParamField(
        int32, "refFaceParamId", FACE_PARAM, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefTextId: int = ParamField(
        int32, "refTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HelpTextId: int = ParamField(
        int32, "helpTextId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UnlockEventFlagId: int = ParamField(
        uint32, "unlockEventFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "reserved[4]")
