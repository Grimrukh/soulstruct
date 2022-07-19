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
from .entities.m60_41_34_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, 1041340200)
