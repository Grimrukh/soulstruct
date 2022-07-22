"""
Southeast Liurnia (NW) (NE)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_43_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005251(0, character=Characters.GiantLobster0, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantLobster1, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantLobster2, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1037430204, radius=12.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=1037430210, radius=12.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=1037430211, radius=12.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, 1037430212, 12.0, 0.0, 1701)
