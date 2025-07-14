from __future__ import annotations

__all__ = ["DEFAULT_KEY_ASSIGN"]

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
    PhyisicalKey0: int = ParamField(
        int, "phyisicalKey_0", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType0: int = ParamField(
        byte, "traitsType_0", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator0: int = ParamField(
        byte, "a2dOperator_0", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget0: int = ParamField(
        byte, "applyTarget_0", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog0: bool = ParamField(
        byte, "isAnalog_0:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin640: bool = ParamField(
        byte, "enableWin64_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS40: bool = ParamField(
        byte, "enablePS4_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne0: bool = ParamField(
        byte, "enableXboxOne_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time10: float = ParamField(
        float, "time1_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time20: float = ParamField(
        float, "time2_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold0: float = ParamField(
        float, "a2dThreshold_0", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey1: int = ParamField(
        int, "phyisicalKey_1", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType1: int = ParamField(
        byte, "traitsType_1", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator1: int = ParamField(
        byte, "a2dOperator_1", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget1: int = ParamField(
        byte, "applyTarget_1", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog1: bool = ParamField(
        byte, "isAnalog_1:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin641: bool = ParamField(
        byte, "enableWin64_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS41: bool = ParamField(
        byte, "enablePS4_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne1: bool = ParamField(
        byte, "enableXboxOne_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time11: float = ParamField(
        float, "time1_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time21: float = ParamField(
        float, "time2_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold1: float = ParamField(
        float, "a2dThreshold_1", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey2: int = ParamField(
        int, "phyisicalKey_2", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType2: int = ParamField(
        byte, "traitsType_2", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator2: int = ParamField(
        byte, "a2dOperator_2", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget2: int = ParamField(
        byte, "applyTarget_2", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog2: bool = ParamField(
        byte, "isAnalog_2:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin642: bool = ParamField(
        byte, "enableWin64_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS42: bool = ParamField(
        byte, "enablePS4_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne2: bool = ParamField(
        byte, "enableXboxOne_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time12: float = ParamField(
        float, "time1_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time22: float = ParamField(
        float, "time2_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold2: float = ParamField(
        float, "a2dThreshold_2", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey3: int = ParamField(
        int, "phyisicalKey_3", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType3: int = ParamField(
        byte, "traitsType_3", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator3: int = ParamField(
        byte, "a2dOperator_3", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget3: int = ParamField(
        byte, "applyTarget_3", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog3: bool = ParamField(
        byte, "isAnalog_3:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin643: bool = ParamField(
        byte, "enableWin64_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS43: bool = ParamField(
        byte, "enablePS4_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne3: bool = ParamField(
        byte, "enableXboxOne_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time13: float = ParamField(
        float, "time1_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time23: float = ParamField(
        float, "time2_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold3: float = ParamField(
        float, "a2dThreshold_3", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey4: int = ParamField(
        int, "phyisicalKey_4", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType4: int = ParamField(
        byte, "traitsType_4", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator4: int = ParamField(
        byte, "a2dOperator_4", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget4: int = ParamField(
        byte, "applyTarget_4", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog4: bool = ParamField(
        byte, "isAnalog_4:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin644: bool = ParamField(
        byte, "enableWin64_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS44: bool = ParamField(
        byte, "enablePS4_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne4: bool = ParamField(
        byte, "enableXboxOne_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time14: float = ParamField(
        float, "time1_4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time24: float = ParamField(
        float, "time2_4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold4: float = ParamField(
        float, "a2dThreshold_4", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey5: int = ParamField(
        int, "phyisicalKey_5", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType5: int = ParamField(
        byte, "traitsType_5", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator5: int = ParamField(
        byte, "a2dOperator_5", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget5: int = ParamField(
        byte, "applyTarget_5", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog5: bool = ParamField(
        byte, "isAnalog_5:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin645: bool = ParamField(
        byte, "enableWin64_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS45: bool = ParamField(
        byte, "enablePS4_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne5: bool = ParamField(
        byte, "enableXboxOne_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time15: float = ParamField(
        float, "time1_5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time25: float = ParamField(
        float, "time2_5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold5: float = ParamField(
        float, "a2dThreshold_5", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey6: int = ParamField(
        int, "phyisicalKey_6", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType6: int = ParamField(
        byte, "traitsType_6", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator6: int = ParamField(
        byte, "a2dOperator_6", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget6: int = ParamField(
        byte, "applyTarget_6", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog6: bool = ParamField(
        byte, "isAnalog_6:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin646: bool = ParamField(
        byte, "enableWin64_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS46: bool = ParamField(
        byte, "enablePS4_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne6: bool = ParamField(
        byte, "enableXboxOne_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time16: float = ParamField(
        float, "time1_6", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time26: float = ParamField(
        float, "time2_6", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold6: float = ParamField(
        float, "a2dThreshold_6", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey7: int = ParamField(
        int, "phyisicalKey_7", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType7: int = ParamField(
        byte, "traitsType_7", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator7: int = ParamField(
        byte, "a2dOperator_7", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget7: int = ParamField(
        byte, "applyTarget_7", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog7: bool = ParamField(
        byte, "isAnalog_7:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin647: bool = ParamField(
        byte, "enableWin64_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS47: bool = ParamField(
        byte, "enablePS4_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne7: bool = ParamField(
        byte, "enableXboxOne_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time17: float = ParamField(
        float, "time1_7", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time27: float = ParamField(
        float, "time2_7", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold7: float = ParamField(
        float, "a2dThreshold_7", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
