"""
Far West Limgrave (NE) (NW)

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
from .enums.m60_38_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton0,
        animation_id=30018,
        animation_id_1=20018,
        region=1038392200,
        radius=7.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Skeleton1,
        animation_id=30018,
        animation_id_1=20018,
        region=1038392200,
        radius=7.0,
        seconds=3.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GraveSkeleton,
        region=1038392210,
        radius=7.0,
        seconds=0.0,
        animation_id=-1,
    )
