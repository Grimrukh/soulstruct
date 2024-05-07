"""
Southeast Mountaintops (NW) (NE)

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_53_55_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.MonstrousDog2,
        region=1053552202,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1053552200(0, character=1053555200)


@RestartOnRest(1053552200)
def Event_1053552200(_, character: uint):
    """Event 1053552200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()
