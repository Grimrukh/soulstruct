from __future__ import annotations

__all__ = ["NPC_AI_ACTION_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NPC_AI_ACTION_PARAM_ST(ParamRow):
    MoveDir: int = ParamField(
        uint8, "moveDir", NPC_AI_ACTION_MOVE_DIR, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key1: int = ParamField(
        uint8, "key1", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key2: int = ParamField(
        uint8, "key2", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key3: int = ParamField(
        uint8, "key3", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BMoveDirHold: int = ParamField(
        uint8, "bMoveDirHold", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold1: int = ParamField(
        uint8, "bKeyHold1", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold2: int = ParamField(
        uint8, "bKeyHold2", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold3: int = ParamField(
        uint8, "bKeyHold3", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GestureId: int = ParamField(
        int32, "gestureId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BLifeEndSuccess: int = ParamField(
        uint8, "bLifeEndSuccess", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad1[3]")
