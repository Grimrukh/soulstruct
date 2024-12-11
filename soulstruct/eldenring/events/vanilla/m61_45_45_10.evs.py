"""
Land of Shadow 11-11 (Alternate) SW NE

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
    RegisterGrace(grace_flag=76942, asset=2045451951)
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=76942,
        asset=2045451981,
        source_flag=77900,
        value=4,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
