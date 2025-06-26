"""
Southwest Mountaintops (NE) (SE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_51_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.LesserFingercreeper,
        region=1051542245,
        radius=0.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1051542200(0, character=1049535200)
    CommonFunc_90005300(0, flag=1051540210, character=1051540210, item_lot=40512, seconds=0.0, left=0)


@RestartOnRest(1051542200)
def Event_1051542200(_, character: uint):
    """Event 1051542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()
