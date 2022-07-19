"""
Southeast Mountaintops (NE) (NW)

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
from .entities.m60_54_55_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1054550000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76505,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=4,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    Event_1054552200(0, character=1054555200)
    CommonFunc_90005630(0, far_view_id=65545500, asset=1054551500, model_point=119)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy, flag=1054552700)
    CommonFunc_90005771(0, 1054550950, 1054552701)


@RestartOnRest(1054552200)
def Event_1054552200(_, character: uint):
    """Event 1054552200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
