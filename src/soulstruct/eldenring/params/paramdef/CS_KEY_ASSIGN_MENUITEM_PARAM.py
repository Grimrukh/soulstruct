from __future__ import annotations

__all__ = ["CS_KEY_ASSIGN_MENUITEM_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_KEY_ASSIGN_MENUITEM_PARAM(ParamRow):
    TextID: int = ParamField(
        int32, "textID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key: int = ParamField(
        int32, "key", CS_USER_INPUT_KEY, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnableUnassign: int = ParamField(
        uint8, "enableUnassign", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnablePadConfig: int = ParamField(
        uint8, "enablePadConfig", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableMouseConfig: int = ParamField(
        uint8, "enableMouseConfig", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    Group: int = ParamField(
        uint8, "group", CS_KEY_ASSIGN_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MappingTextID: int = ParamField(
        int32, "mappingTextID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ViewPad: int = ParamField(
        uint8, "viewPad", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    ViewKeyboardMouse: int = ParamField(
        uint8, "viewKeyboardMouse", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "padding[6]")
