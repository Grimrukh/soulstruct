"""
Liurnia to Altus Plateau (NW) (SE)

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005221(0, character=1037500200, animation_id=30005, animation_id_1=20020, seconds=0.0, left=0)
