from __future__ import annotations

__all__ = ["CHARMAKEMENUTOP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARMAKEMENUTOP_PARAM_ST(ParamRow):
    CommandID: int = ParamField(
        int, "CommandID", CHARMAKEMENU_CMD_TYPE, default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int, "CaptionID", default=0,
        tooltip="TODO",
    )
    FaceParamID: int = ParamField(
        int, "FaceParamID", FACE_PARAM, default=0,
        tooltip="TODO",
    )
    TableID: int = ParamField(
        int, "TableID", default=0,
        tooltip="TODO",
    )
    ViewCondition: int = ParamField(
        int, "ViewCondition", CHARMAKEMENU_VIEW_CONDITION, default=0,
        tooltip="TODO",
    )
    PreviewMode: int = ParamField(
        sbyte, "PreviewMode", CHARMAKEMENU_PREVIEW_MODE, default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(11, "reserved[11]")
