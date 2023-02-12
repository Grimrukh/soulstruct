from __future__ import annotations

__all__ = ["AI_ODDS_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class AI_ODDS_PARAM(ParamRowData):
    Act0: int = ParamField(
        byte, "act0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act1: int = ParamField(
        byte, "act1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act2: int = ParamField(
        byte, "act2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act3: int = ParamField(
        byte, "act3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act4: int = ParamField(
        byte, "act4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act5: int = ParamField(
        byte, "act5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act6: int = ParamField(
        byte, "act6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act7: int = ParamField(
        byte, "act7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act8: int = ParamField(
        byte, "act8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act9: int = ParamField(
        byte, "act9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act10: int = ParamField(
        byte, "act10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act11: int = ParamField(
        byte, "act11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act12: int = ParamField(
        byte, "act12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act13: int = ParamField(
        byte, "act13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act14: int = ParamField(
        byte, "act14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act15: int = ParamField(
        byte, "act15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act16: int = ParamField(
        byte, "act16", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act17: int = ParamField(
        byte, "act17", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act18: int = ParamField(
        byte, "act18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act19: int = ParamField(
        byte, "act19", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act20: int = ParamField(
        byte, "act20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act21: int = ParamField(
        byte, "act21", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act22: int = ParamField(
        byte, "act22", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act23: int = ParamField(
        byte, "act23", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act24: int = ParamField(
        byte, "act24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act25: int = ParamField(
        byte, "act25", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act26: int = ParamField(
        byte, "act26", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act27: int = ParamField(
        byte, "act27", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act28: int = ParamField(
        byte, "act28", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act29: int = ParamField(
        byte, "act29", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act30: int = ParamField(
        byte, "act30", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act31: int = ParamField(
        byte, "act31", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act32: int = ParamField(
        byte, "act32", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act33: int = ParamField(
        byte, "act33", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act34: int = ParamField(
        byte, "act34", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act35: int = ParamField(
        byte, "act35", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act36: int = ParamField(
        byte, "act36", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act37: int = ParamField(
        byte, "act37", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act38: int = ParamField(
        byte, "act38", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act39: int = ParamField(
        byte, "act39", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act40: int = ParamField(
        byte, "act40", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act41: int = ParamField(
        byte, "act41", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act42: int = ParamField(
        byte, "act42", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act43: int = ParamField(
        byte, "act43", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act44: int = ParamField(
        byte, "act44", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act45: int = ParamField(
        byte, "act45", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act46: int = ParamField(
        byte, "act46", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act47: int = ParamField(
        byte, "act47", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act48: int = ParamField(
        byte, "act48", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act49: int = ParamField(
        byte, "act49", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act50: int = ParamField(
        byte, "act50", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act51: int = ParamField(
        byte, "act51", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act52: int = ParamField(
        byte, "act52", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act53: int = ParamField(
        byte, "act53", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act54: int = ParamField(
        byte, "act54", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act55: int = ParamField(
        byte, "act55", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act56: int = ParamField(
        byte, "act56", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act57: int = ParamField(
        byte, "act57", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act58: int = ParamField(
        byte, "act58", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act59: int = ParamField(
        byte, "act59", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act60: int = ParamField(
        byte, "act60", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act61: int = ParamField(
        byte, "act61", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act62: int = ParamField(
        byte, "act62", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act63: int = ParamField(
        byte, "act63", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act64: int = ParamField(
        byte, "act64", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act65: int = ParamField(
        byte, "act65", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act66: int = ParamField(
        byte, "act66", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act67: int = ParamField(
        byte, "act67", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act68: int = ParamField(
        byte, "act68", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act69: int = ParamField(
        byte, "act69", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act70: int = ParamField(
        byte, "act70", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act71: int = ParamField(
        byte, "act71", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act72: int = ParamField(
        byte, "act72", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act73: int = ParamField(
        byte, "act73", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act74: int = ParamField(
        byte, "act74", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act75: int = ParamField(
        byte, "act75", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act76: int = ParamField(
        byte, "act76", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act77: int = ParamField(
        byte, "act77", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act78: int = ParamField(
        byte, "act78", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act79: int = ParamField(
        byte, "act79", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act80: int = ParamField(
        byte, "act80", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act81: int = ParamField(
        byte, "act81", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act82: int = ParamField(
        byte, "act82", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act83: int = ParamField(
        byte, "act83", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act84: int = ParamField(
        byte, "act84", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act85: int = ParamField(
        byte, "act85", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act86: int = ParamField(
        byte, "act86", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act87: int = ParamField(
        byte, "act87", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act88: int = ParamField(
        byte, "act88", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act89: int = ParamField(
        byte, "act89", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act90: int = ParamField(
        byte, "act90", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act91: int = ParamField(
        byte, "act91", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act92: int = ParamField(
        byte, "act92", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act93: int = ParamField(
        byte, "act93", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act94: int = ParamField(
        byte, "act94", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act95: int = ParamField(
        byte, "act95", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act96: int = ParamField(
        byte, "act96", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act97: int = ParamField(
        byte, "act97", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act98: int = ParamField(
        byte, "act98", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Act99: int = ParamField(
        byte, "act99", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad0[12]")
