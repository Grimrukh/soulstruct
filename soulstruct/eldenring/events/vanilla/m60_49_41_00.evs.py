"""
North Caelid (SW) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_49_41_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, flag=1049410299, character=Characters.Scarab, item_lot=40426, seconds=0.0, left=0)
    Event_1049412580()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(1049412580)
def Event_1049412580():
    """Event 1049412580"""
    RegisterLadder(start_climbing_flag=1049410580, stop_climbing_flag=1049410581, asset=Assets.AEG005_100_1000)
    RegisterLadder(start_climbing_flag=1049410582, stop_climbing_flag=1049410583, asset=Assets.AEG005_101_1000)
    RegisterLadder(start_climbing_flag=1049410584, stop_climbing_flag=1049410585, asset=Assets.AEG005_101_1001)
    RegisterLadder(start_climbing_flag=1049410586, stop_climbing_flag=1049410587, asset=Assets.AEG005_101_1002)
    RegisterLadder(start_climbing_flag=1049410588, stop_climbing_flag=1049410589, asset=Assets.AEG005_102_1000)
    RegisterLadder(start_climbing_flag=1049410590, stop_climbing_flag=1049410591, asset=1049411590)
    RegisterLadder(start_climbing_flag=1049410592, stop_climbing_flag=1049410593, asset=1049411592)
    RegisterLadder(start_climbing_flag=1049410594, stop_climbing_flag=1049410595, asset=1049411594)
    RegisterLadder(start_climbing_flag=1049410596, stop_climbing_flag=1049410597, asset=1049411596)
