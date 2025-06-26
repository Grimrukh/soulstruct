"""
North Altus Plateau (NW) (NW)

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
from .enums.m60_40_55_00_enums import *


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Rat0, region=1040552301, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Rat1, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat2, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat3, region=1040552302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.GiantRat, region=1040552250, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse,
        animation_id=30000,
        animation_id_1=20000,
        region=1040552403,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse,
        animation_id=30000,
        animation_id_1=20000,
        region=1040552403,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse,
        animation_id=30000,
        animation_id_1=20000,
        region=1040552403,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
