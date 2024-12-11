"""
Land of Shadow 11-10 SE NE

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
    RegisterGrace(grace_flag=2047410000, asset=2047411950, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=2047410001, asset=2047411951, enemy_block_distance=0.0)
    CommonFunc_90005221(0, character=2047410207, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410212, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410217, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410229, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410235, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410221, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410222, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2047410223, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005250(0, character=2047410233, region=2047412233, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047410236, region=2047412233, seconds=0.0, animation_id=0)
    CommonFunc_90005639(0, flag=2047410500, asset=2047411500, asset_1=2047411501, asset_2=2047411502, seconds=4.0)
    CommonFunc_90005639(0, flag=2047410510, asset=2047411510, asset_1=2047411511, asset_2=2047411512, seconds=2.0)
    CommonFunc_90005706(0, character=2047410700, animation_id=30013, left=0)
    CommonFunc_90005706(0, character=2047410720, animation_id=30015, left=0)
    CommonFunc_90005706(0, character=2047410710, animation_id=30016, left=2047412710)
