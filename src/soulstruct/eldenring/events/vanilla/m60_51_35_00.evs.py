"""
Far South Caelid (NE) (NE)

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
from .enums.m60_51_35_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=1051350000, asset=1051351950, enemy_block_distance=10.0, character=1051350480)
    CommonFunc_90005300(0, flag=1051350290, character=Characters.Scarab, item_lot=40408, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=Characters.Bat0, region=1051352200, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Bat1, region=1051352200, radius=10.0, seconds=0.0, animation_id=0)
