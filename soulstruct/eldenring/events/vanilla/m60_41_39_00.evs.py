"""
West Limgrave (NW) (NE)

linked:
0
82
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_41_39_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1041392340(0, character=1041390705)
    Event_1041392340(1, character=1041390706)
    Event_1041392340(2, character=1041390707)
    Event_1041392340(3, character=1041390708)
    CommonFunc_90005705(0, character=Characters.FingerReader)
    CommonFunc_90005706(0, 1041390720, 30023, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FingerReader)
    DisableBackread(1041390720)
    CommonFunc_90005261(0, character=Characters.Bat0, region=1041382200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Bat1, region=1041382200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, 1041390202, 1041382200, 10.0, 0.0, -1)


@RestartOnRest(1041392340)
def Event_1041392340(_, character: uint):
    """Event 1041392340"""
    Kill(character, award_runes=True)
