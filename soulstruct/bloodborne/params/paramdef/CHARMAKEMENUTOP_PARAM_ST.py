from __future__ import annotations

__all__ = ["CHARMAKEMENUTOP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHARMAKEMENUTOP_PARAM_ST(ParamRow):
    CommandID: CHARMAKEMENU_CMD_TYPE = ParamField(
        int, "CommandID", default=0,
        tooltip="TODO",
    )
    CaptionID: int = ParamField(
        int, "CaptionID", default=0,
        tooltip="TODO",
    )
    FaceParamID: FACE_PARAM = ParamField(
        int, "FaceParamID", default=0,
        tooltip="TODO",
    )
    TableID: int = ParamField(
        int, "TableID", default=0,
        tooltip="TODO",
    )
    ViewCondition: CHARMAKEMENU_VIEW_CONDITION = ParamField(
        int, "ViewCondition", default=0,
        tooltip="TODO",
    )
    PreviewMode: CHARMAKEMENU_PREVIEW_MODE = ParamField(
        sbyte, "PreviewMode", default=0,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(11, "reserved[11]")
