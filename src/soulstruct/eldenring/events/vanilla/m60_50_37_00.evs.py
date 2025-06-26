"""
South Caelid (SE) (NW)

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
from .enums.m60_50_37_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005251(0, character=Characters.Troll, radius=100.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(0, flag=1050370299, character=Characters.Troll, item_lot=0, seconds=0.0, left=0)
