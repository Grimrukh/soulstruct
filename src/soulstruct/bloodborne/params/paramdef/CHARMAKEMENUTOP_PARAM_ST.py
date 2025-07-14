from __future__ import annotations

__all__ = ["CHARMAKEMENUTOP_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class CHARMAKEMENUTOP_PARAM_ST(ParamRow):
    CommandID: int = ParamField(
        int32, "CommandID", CHARMAKEMENU_CMD_TYPE, default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int32, "CaptionID", default=0,
        tooltip="TODO",
    )
    FaceParamID: int = ParamField(
        int32, "FaceParamID", FACE_PARAM, default=0,
        tooltip="TODO",
    )
    TableID: int = ParamField(
        int32, "TableID", default=0,
        tooltip="TODO",
    )
    ViewCondition: int = ParamField(
        int32, "ViewCondition", CHARMAKEMENU_VIEW_CONDITION, default=0,
        tooltip="TODO",
    )
    PreviewMode: int = ParamField(
        int8, "PreviewMode", CHARMAKEMENU_PREVIEW_MODE, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(11, "reserved[11]")
