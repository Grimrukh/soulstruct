"""
West Altus Plateau (SE) (NW)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_38_53_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(0, grace_flag=1038530000, asset=1038531950, enemy_block_distance=5.0, character=1038530480)
    Event_1038532200(0, character=1038530200)
    Event_1038532200(1, character=1038530201)
    Event_1038532200(2, character=1038530202)
    Event_1038532200(3, character=1038530203)
    Event_1038532200(4, character=1038530204)
    Event_1038532200(5, character=1038530205)
    Event_1038532200(6, character=1038530206)
    Event_1038532200(7, character=1038530207)
    Event_1038532200(8, character=1038530208)
    Event_1038532580()
    CommonFunc_90005620(
        0,
        flag=1038530570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1038532570,
        cancel_flag__right_flag=1038532571,
        right=1038532572,
    )
    CommonFunc_90005621(0, flag=1038530570, asset=Assets.AEG099_272_9000)


@RestartOnRest(1038532580)
def Event_1038532580():
    """Event 1038532580"""
    RegisterLadder(start_climbing_flag=38531580, stop_climbing_flag=38531851, asset=1038531582)


@RestartOnRest(1038532200)
def Event_1038532200(_, character: Character | int):
    """Event 1038532200"""
    Kill(character)
    End()
