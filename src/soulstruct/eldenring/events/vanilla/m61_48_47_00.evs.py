"""
Land of Shadow 12-11 NW NW

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
    RegisterGrace(grace_flag=76912, asset=2048471950)
    CommonFunc_90005301(0, flag=2048470500, character=2048470500, item_lot__unk1=40910, seconds=0.0, unk1=0)
    CommonFunc_90005301(0, flag=2048470501, character=2048470501, item_lot__unk1=40912, seconds=0.0, unk1=0)
    CommonFunc_90005301(0, flag=2048470502, character=2048470502, item_lot__unk1=40914, seconds=0.0, unk1=0)


@RestartOnRest(2048470200)
def Event_2048470200(_, character: Character | int):
    """Event 2048470200"""
    Kill(character)
