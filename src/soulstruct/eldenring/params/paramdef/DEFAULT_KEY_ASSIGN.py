from __future__ import annotations

__all__ = ["DEFAULT_KEY_ASSIGN"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class DEFAULT_KEY_ASSIGN(ParamRow):
    Priority0: bool = ParamField(
        uint8, "priority0:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority1: bool = ParamField(
        uint8, "priority1:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority2: bool = ParamField(
        uint8, "priority2:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority3: bool = ParamField(
        uint8, "priority3:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority4: bool = ParamField(
        uint8, "priority4:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority5: bool = ParamField(
        uint8, "priority5:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority6: bool = ParamField(
        uint8, "priority6:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority7: bool = ParamField(
        uint8, "priority7:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority8: bool = ParamField(
        uint8, "priority8:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority9: bool = ParamField(
        uint8, "priority9:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority10: bool = ParamField(
        uint8, "priority10:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority11: bool = ParamField(
        uint8, "priority11:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority12: bool = ParamField(
        uint8, "priority12:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority13: bool = ParamField(
        uint8, "priority13:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority14: bool = ParamField(
        uint8, "priority14:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority15: bool = ParamField(
        uint8, "priority15:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority16: bool = ParamField(
        uint8, "priority16:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority17: bool = ParamField(
        uint8, "priority17:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority18: bool = ParamField(
        uint8, "priority18:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority19: bool = ParamField(
        uint8, "priority19:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority20: bool = ParamField(
        uint8, "priority20:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority21: bool = ParamField(
        uint8, "priority21:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority22: bool = ParamField(
        uint8, "priority22:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority23: bool = ParamField(
        uint8, "priority23:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority24: bool = ParamField(
        uint8, "priority24:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority25: bool = ParamField(
        uint8, "priority25:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority26: bool = ParamField(
        uint8, "priority26:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority27: bool = ParamField(
        uint8, "priority27:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority28: bool = ParamField(
        uint8, "priority28:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority29: bool = ParamField(
        uint8, "priority29:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority30: bool = ParamField(
        uint8, "priority30:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Priority31: bool = ParamField(
        uint8, "priority31:1", DefaultKeyAssignPrioritySuppression, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "dummy[12]")
    PhyisicalKey0: int = ParamField(
        int32, "phyisicalKey_0", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType0: int = ParamField(
        uint8, "traitsType_0", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator0: int = ParamField(
        uint8, "a2dOperator_0", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget0: int = ParamField(
        uint8, "applyTarget_0", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog0: bool = ParamField(
        uint8, "isAnalog_0:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin640: bool = ParamField(
        uint8, "enableWin64_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS40: bool = ParamField(
        uint8, "enablePS4_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne0: bool = ParamField(
        uint8, "enableXboxOne_0:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time10: float = ParamField(
        float32, "time1_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time20: float = ParamField(
        float32, "time2_0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold0: float = ParamField(
        float32, "a2dThreshold_0", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey1: int = ParamField(
        int32, "phyisicalKey_1", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType1: int = ParamField(
        uint8, "traitsType_1", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator1: int = ParamField(
        uint8, "a2dOperator_1", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget1: int = ParamField(
        uint8, "applyTarget_1", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog1: bool = ParamField(
        uint8, "isAnalog_1:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin641: bool = ParamField(
        uint8, "enableWin64_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS41: bool = ParamField(
        uint8, "enablePS4_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne1: bool = ParamField(
        uint8, "enableXboxOne_1:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time11: float = ParamField(
        float32, "time1_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time21: float = ParamField(
        float32, "time2_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold1: float = ParamField(
        float32, "a2dThreshold_1", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey2: int = ParamField(
        int32, "phyisicalKey_2", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType2: int = ParamField(
        uint8, "traitsType_2", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator2: int = ParamField(
        uint8, "a2dOperator_2", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget2: int = ParamField(
        uint8, "applyTarget_2", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog2: bool = ParamField(
        uint8, "isAnalog_2:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin642: bool = ParamField(
        uint8, "enableWin64_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS42: bool = ParamField(
        uint8, "enablePS4_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne2: bool = ParamField(
        uint8, "enableXboxOne_2:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time12: float = ParamField(
        float32, "time1_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time22: float = ParamField(
        float32, "time2_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold2: float = ParamField(
        float32, "a2dThreshold_2", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey3: int = ParamField(
        int32, "phyisicalKey_3", DefaultKeyAssignPadKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType3: int = ParamField(
        uint8, "traitsType_3", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator3: int = ParamField(
        uint8, "a2dOperator_3", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget3: int = ParamField(
        uint8, "applyTarget_3", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog3: bool = ParamField(
        uint8, "isAnalog_3:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin643: bool = ParamField(
        uint8, "enableWin64_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS43: bool = ParamField(
        uint8, "enablePS4_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne3: bool = ParamField(
        uint8, "enableXboxOne_3:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time13: float = ParamField(
        float32, "time1_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time23: float = ParamField(
        float32, "time2_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold3: float = ParamField(
        float32, "a2dThreshold_3", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey4: int = ParamField(
        int32, "phyisicalKey_4", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType4: int = ParamField(
        uint8, "traitsType_4", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator4: int = ParamField(
        uint8, "a2dOperator_4", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget4: int = ParamField(
        uint8, "applyTarget_4", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog4: bool = ParamField(
        uint8, "isAnalog_4:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin644: bool = ParamField(
        uint8, "enableWin64_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS44: bool = ParamField(
        uint8, "enablePS4_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne4: bool = ParamField(
        uint8, "enableXboxOne_4:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time14: float = ParamField(
        float32, "time1_4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time24: float = ParamField(
        float32, "time2_4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold4: float = ParamField(
        float32, "a2dThreshold_4", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey5: int = ParamField(
        int32, "phyisicalKey_5", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType5: int = ParamField(
        uint8, "traitsType_5", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator5: int = ParamField(
        uint8, "a2dOperator_5", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget5: int = ParamField(
        uint8, "applyTarget_5", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog5: bool = ParamField(
        uint8, "isAnalog_5:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin645: bool = ParamField(
        uint8, "enableWin64_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS45: bool = ParamField(
        uint8, "enablePS4_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne5: bool = ParamField(
        uint8, "enableXboxOne_5:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time15: float = ParamField(
        float32, "time1_5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time25: float = ParamField(
        float32, "time2_5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold5: float = ParamField(
        float32, "a2dThreshold_5", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey6: int = ParamField(
        int32, "phyisicalKey_6", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType6: int = ParamField(
        uint8, "traitsType_6", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator6: int = ParamField(
        uint8, "a2dOperator_6", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget6: int = ParamField(
        uint8, "applyTarget_6", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog6: bool = ParamField(
        uint8, "isAnalog_6:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin646: bool = ParamField(
        uint8, "enableWin64_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS46: bool = ParamField(
        uint8, "enablePS4_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne6: bool = ParamField(
        uint8, "enableXboxOne_6:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time16: float = ParamField(
        float32, "time1_6", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time26: float = ParamField(
        float32, "time2_6", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold6: float = ParamField(
        float32, "a2dThreshold_6", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    PhyisicalKey7: int = ParamField(
        int32, "phyisicalKey_7", DefaultKeyAssignPcKey, default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraitsType7: int = ParamField(
        uint8, "traitsType_7", DefaultKeyAssignTraits, default=0,
        tooltip="TOOLTIP-TODO",
    )
    A2dOperator7: int = ParamField(
        uint8, "a2dOperator_7", DefaultKeyAssignA2DOperator, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplyTarget7: int = ParamField(
        uint8, "applyTarget_7", DefaultKeyAssignApplyTarget, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnalog7: bool = ParamField(
        uint8, "isAnalog_7:1", DefaultKeyAssignDigitalAnalog, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableWin647: bool = ParamField(
        uint8, "enableWin64_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnablePS47: bool = ParamField(
        uint8, "enablePS4_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    EnableXboxOne7: bool = ParamField(
        uint8, "enableXboxOne_7:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    Time17: float = ParamField(
        float32, "time1_7", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Time27: float = ParamField(
        float32, "time2_7", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    A2dThreshold7: float = ParamField(
        float32, "a2dThreshold_7", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
