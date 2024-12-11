"""
Land of Shadow 12-11 SW NE

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=2049450800, name=905820601, npc_threat_level=16)
    CommonFunc_90005860(0, flag=2049450800, left=0, character=2049450800, left_1=0, item_lot=30930, seconds=0.0)
    CommonFunc_90005251(0, character=2049450300, radius=35.0, seconds=0.0, animation_id=-1)
