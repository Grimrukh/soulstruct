"""
Southeast Liurnia (SE) (SW)

linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_38_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038400000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76201,
        asset=Assets.AEG099_090_9001,
        source_flag=77200,
        value=1,
        flag_2=78200,
        flag_3=78201,
        flag_4=78202,
        flag_5=78203,
        flag_6=78204,
        flag_7=78205,
        flag_8=78206,
        flag_9=78207,
        flag_10=78208,
        flag_11=78209,
    )
    CommonFunc_90005251(0, character=1038400210, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005630(0, far_view_id=61384000, asset=1038401500, model_point=122)
