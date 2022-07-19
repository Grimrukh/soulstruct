"""
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


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, 1047550209, 1047552200, 2.0, 0.0, -1)
    CommonFunc_90005261(0, 1047550210, 1047552200, 2.0, 0.0, -1)
    CommonFunc_90005261(0, 1047550220, 1047552200, 2.0, 0.0, -1)
    CommonFunc_90005261(0, 1047550200, 1047552211, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 1047550211, 1047552211, 1.0, 0.0, -1)


@RestartOnRest(1047552300)
def Event_1047552300(_, character: uint):
    """Event 1047552300"""
    DisableAI(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    ForceAnimation(character, 30019, loop=True)
