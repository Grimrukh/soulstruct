"""
Land of Shadow 12-09 SW NW

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
    RegisterGrace(grace_flag=2048370000, asset=2048371950)
    CommonFunc_900005580(0, flag=580600, asset=2048371502, flag_1=9146)
    CommonFunc_90005200(
        0,
        character=2048370200,
        animation_id=30014,
        animation_id_1=20014,
        region=2048372200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2048370203, region=2048372200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2048370204, region=2048372200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2048370205, region=2048372200, seconds=0.0, animation_id=-1)
    CommonFunc_90005748(0, entity=2048371700, action_button_id=206020, text=1030025, display_distance=30.0, flag=4915)
