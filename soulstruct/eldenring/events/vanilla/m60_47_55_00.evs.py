"""
Northeast Altus Plateau (NE) (NE)

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
from .enums.m60_47_55_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=1047550209, region=1047552200, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1047550210, region=1047552200, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1047550220, region=1047552200, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Rat0, region=1047552211, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Rat7, region=1047552211, radius=1.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1047552300)
def Event_1047552300(_, character: uint):
    """Event 1047552300"""
    DisableAI(character)
    EnableImmortality(character)
    DisableHealthBar(character)
    ForceAnimation(character, 30019, loop=True)
