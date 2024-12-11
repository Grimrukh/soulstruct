"""
Land of Shadow 12-09 NE SW

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
    RegisterGrace(grace_flag=2050380000, asset=2050381950)
    CommonFunc_90005250(0, character=2050380200, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005250(0, character=2050380201, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005250(0, character=2050380202, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005250(0, character=2050380203, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005250(0, character=2050380204, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005250(0, character=2050380250, region=2050382200, seconds=0.0, animation_id=1704)
    CommonFunc_90005200(
        0,
        character=2050380301,
        animation_id=30002,
        animation_id_1=20002,
        region=2050382301,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
