from __future__ import annotations

__all__ = ["DEFAULT_KEY_ASSIGN"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class DEFAULT_KEY_ASSIGN(ParamRow):
    Priority0: bool = ParamField(
        byte, "priority0:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority1: bool = ParamField(
        byte, "priority1:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority2: bool = ParamField(
        byte, "priority2:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority3: bool = ParamField(
        byte, "priority3:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority4: bool = ParamField(
        byte, "priority4:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority5: bool = ParamField(
        byte, "priority5:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority6: bool = ParamField(
        byte, "priority6:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority7: bool = ParamField(
        byte, "priority7:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority8: bool = ParamField(
        byte, "priority8:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority9: bool = ParamField(
        byte, "priority9:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority10: bool = ParamField(
        byte, "priority10:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority11: bool = ParamField(
        byte, "priority11:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority12: bool = ParamField(
        byte, "priority12:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority13: bool = ParamField(
        byte, "priority13:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority14: bool = ParamField(
        byte, "priority14:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority15: bool = ParamField(
        byte, "priority15:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority16: bool = ParamField(
        byte, "priority16:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority17: bool = ParamField(
        byte, "priority17:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority18: bool = ParamField(
        byte, "priority18:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority19: bool = ParamField(
        byte, "priority19:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority20: bool = ParamField(
        byte, "priority20:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority21: bool = ParamField(
        byte, "priority21:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority22: bool = ParamField(
        byte, "priority22:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority23: bool = ParamField(
        byte, "priority23:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority24: bool = ParamField(
        byte, "priority24:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority25: bool = ParamField(
        byte, "priority25:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority26: bool = ParamField(
        byte, "priority26:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority27: bool = ParamField(
        byte, "priority27:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority28: bool = ParamField(
        byte, "priority28:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority29: bool = ParamField(
        byte, "priority29:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority30: bool = ParamField(
        byte, "priority30:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority31: bool = ParamField(
        byte, "priority31:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "dummy[12]")
    PhyisicalKey: int = ParamField(
        int, "phyisicalKey", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType: int = ParamField(
        byte, "traitsType", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator: int = ParamField(
        byte, "a2dOperator", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget: int = ParamField(
        byte, "applyTarget", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog: bool = ParamField(
        byte, "isAnalog:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin64: bool = ParamField(
        byte, "enableWin64:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS4: bool = ParamField(
        byte, "enablePS4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne: bool = ParamField(
        byte, "enableXboxOne:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
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
        float, "a2dThreshold", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
