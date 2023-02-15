from __future__ import annotations

__all__ = ["NPC_AI_ACTION_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NPC_AI_ACTION_PARAM_ST(ParamRow):
    MoveDir: int = ParamField(
        byte, "moveDir", NPC_AI_ACTION_MOVE_DIR, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key1: int = ParamField(
        byte, "key1", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key2: int = ParamField(
        byte, "key2", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Key3: int = ParamField(
        byte, "key3", NPC_AI_ACTION_KEY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BMoveDirHold: int = ParamField(
        byte, "bMoveDirHold", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold1: int = ParamField(
        byte, "bKeyHold1", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold2: int = ParamField(
        byte, "bKeyHold2", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BKeyHold3: int = ParamField(
        byte, "bKeyHold3", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GestureId: int = ParamField(
        int, "gestureId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BLifeEndSuccess: int = ParamField(
        byte, "bLifeEndSuccess", ON_OFF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad1[3]")
