from __future__ import annotations

__all__ = ["DEFAULT_KEY_ASSIGN"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DEFAULT_KEY_ASSIGN(ParamRowData):
    Priority0: int = ParamField(
        byte, "priority0:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority1: int = ParamField(
        byte, "priority1:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority2: int = ParamField(
        byte, "priority2:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority3: int = ParamField(
        byte, "priority3:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority4: int = ParamField(
        byte, "priority4:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority5: int = ParamField(
        byte, "priority5:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority6: int = ParamField(
        byte, "priority6:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority7: int = ParamField(
        byte, "priority7:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority8: int = ParamField(
        byte, "priority8:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority9: int = ParamField(
        byte, "priority9:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority10: int = ParamField(
        byte, "priority10:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority11: int = ParamField(
        byte, "priority11:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority12: int = ParamField(
        byte, "priority12:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority13: int = ParamField(
        byte, "priority13:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority14: int = ParamField(
        byte, "priority14:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority15: int = ParamField(
        byte, "priority15:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority16: int = ParamField(
        byte, "priority16:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority17: int = ParamField(
        byte, "priority17:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority18: int = ParamField(
        byte, "priority18:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority19: int = ParamField(
        byte, "priority19:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority20: int = ParamField(
        byte, "priority20:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority21: int = ParamField(
        byte, "priority21:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority22: int = ParamField(
        byte, "priority22:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority23: int = ParamField(
        byte, "priority23:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority24: int = ParamField(
        byte, "priority24:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority25: int = ParamField(
        byte, "priority25:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority26: int = ParamField(
        byte, "priority26:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority27: int = ParamField(
        byte, "priority27:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority28: int = ParamField(
        byte, "priority28:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority29: int = ParamField(
        byte, "priority29:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority30: int = ParamField(
        byte, "priority30:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Priority31: int = ParamField(
        byte, "priority31:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "dummy[12]")
    PhyisicalKey: int = ParamField(
        int, "phyisicalKey", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType: int = ParamField(
        byte, "traitsType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator: int = ParamField(
        byte, "a2dOperator", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget: int = ParamField(
        byte, "applyTarget", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog: int = ParamField(
        byte, "isAnalog:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin64: int = ParamField(
        byte, "enableWin64:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS4: int = ParamField(
        byte, "enablePS4:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne: int = ParamField(
        byte, "enableXboxOne:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Time1: float = ParamField(
        float, "time1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time2: float = ParamField(
        float, "time2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold: float = ParamField(
        float, "a2dThreshold", default=0,
        tooltip="TOOLTIP-TODO",
    )
