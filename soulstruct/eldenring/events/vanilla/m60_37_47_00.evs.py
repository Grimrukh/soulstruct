"""
East Liurnia (NW) (NE)

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
from .enums.m60_37_47_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.AncestralFollower,
        region=1037472200,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.WildMouflon,
        animation_id=30005,
        animation_id_1=20021,
        radius=15.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Runebear,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.WildMouflon, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Runebear, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, dummy_id=800, right=0)
