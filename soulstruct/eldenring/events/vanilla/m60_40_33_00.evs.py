"""
West Weeping Peninsula (SW) (NW)

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=1040330200, region=1040332200, radius=5.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(0, character=1040330201, region=1040332200, radius=5.0, seconds=1.0, animation_id=1701)
    CommonFunc_90005261(0, character=1040330202, region=1040332200, radius=5.0, seconds=2.0, animation_id=1702)
    CommonFunc_90005261(0, character=1040330203, region=1040332200, radius=5.0, seconds=0.0, animation_id=1702)
    CommonFunc_90005261(0, character=1040330204, region=1040332200, radius=5.0, seconds=1.0, animation_id=1701)
    CommonFunc_90005261(0, character=1040330205, region=1040332200, radius=5.0, seconds=2.0, animation_id=1702)
    CommonFunc_90005261(0, character=1040330206, region=1040332200, radius=5.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(0, character=1040330207, region=1040332200, radius=5.0, seconds=1.0, animation_id=1702)
