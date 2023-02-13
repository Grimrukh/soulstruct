from __future__ import annotations

__all__ = ["CS_KEY_ASSIGN_MENUITEM_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CS_KEY_ASSIGN_MENUITEM_PARAM(ParamRow):
    TextID: int = ParamField(
        int, "textID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key: int = ParamField(
        int, "key", CS_USER_INPUT_KEY, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EnableUnassign: int = ParamField(
        byte, "enableUnassign", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnablePadConfig: int = ParamField(
        byte, "enablePadConfig", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableMouseConfig: int = ParamField(
        byte, "enableMouseConfig", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    Group: int = ParamField(
        byte, "group", CS_KEY_ASSIGN_GROUP, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MappingTextID: int = ParamField(
        int, "mappingTextID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ViewPad: int = ParamField(
        byte, "viewPad", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    ViewKeyboardMouse: int = ParamField(
        byte, "viewKeyboardMouse", BOOL_CIRCLECROSS_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "padding[6]")
