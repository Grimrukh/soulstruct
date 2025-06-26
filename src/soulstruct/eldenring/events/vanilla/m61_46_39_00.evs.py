"""
Land of Shadow 11-09 NE NW

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
    RegisterGrace(grace_flag=2046390000, asset=2046391950)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005431(0, character=2246390200)
    CommonFunc_90005432(0, character=2246390200, flag=2246392200)
    CommonFunc_90005435(
        0,
        character=2246390200,
        flag=2246392201,
        flag_1=2246392202,
        flag_2=2246392203,
        flag_3=2246392204,
    )
    CommonFunc_90005437(0, character=2246390200, flag=2246392208, flag_1=2046392209)
    CommonFunc_90005436(0, character=2246390200, region=2046392201, region_1=2046392202)
    CommonFunc_90005301(0, flag=2046390200, character=2246390200, item_lot__unk1=2046390060, seconds=4.0, unk1=0)
