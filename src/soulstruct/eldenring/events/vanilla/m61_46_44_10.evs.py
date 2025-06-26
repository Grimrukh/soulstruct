"""
Land of Shadow 11-11 (Alternate) SE SW

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
    RegisterGrace(grace_flag=2046440000, asset=2046441950, enemy_block_distance=0.0)
    CommonFunc_90005251(0, character=2046440301, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440341, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440307, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440337, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440343, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440310, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440344, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440335, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440342, region=2046442300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440250, region=2046442250, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440258, region=2046442250, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2046440259, region=2046442250, seconds=0.0, animation_id=-1)
    CommonFunc_90005556(0, asset=2046441692, flag=2046447900)
    CommonFunc_90005557(0, entity=2046441680)
    CommonFunc_90005557(0, entity=2046441681)
    CommonFunc_90005557(0, entity=2046441682)
    CommonFunc_90005557(0, entity=2046441683)
    CommonFunc_90005557(0, entity=2046441684)
    CommonFunc_90005557(0, entity=2046441685)
    CommonFunc_90005557(0, entity=2046441686)
    CommonFunc_90005557(0, entity=2046441687)
    CommonFunc_90005557(0, entity=2046441688)
    CommonFunc_90005557(0, entity=2046441689)
    CommonFunc_90005557(0, entity=2046441690)
    CommonFunc_90005557(0, entity=2046441691)
    CommonFunc_90005639(0, flag=2046440500, asset=2046441500, asset_1=2046441501, asset_2=2046441502, seconds=2.0)
    CommonFunc_90005706(0, character=2046440700, animation_id=30012, left=0)
