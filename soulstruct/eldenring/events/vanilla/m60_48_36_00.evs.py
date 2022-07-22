"""
South Caelid (SW) (SW)

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
from .entities.m60_48_36_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1048360000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76458,
        flag_1=76404,
        asset=Assets.AEG099_090_9000,
        source_flag=77410,
        value=1,
        flag_2=78410,
        flag_3=78411,
        flag_4=78412,
        flag_5=78413,
        flag_6=78414,
        flag_7=78415,
        flag_8=78416,
        flag_9=78417,
        flag_10=78418,
        flag_11=78419,
    )
    CommonFunc_90005250(0, character=Characters.BanishedKnight, region=1048362201, seconds=0.0, animation_id=-1)
    Event_1048360700(0, character=Characters.Dummy)
    Event_1048360701()


@RestartOnRest(1048360700)
def Event_1048360700(_, character: uint):
    """Event 1048360700"""
    DisableGravity(character)
    DisableAnimations(character)


@RestartOnRest(1048360701)
def Event_1048360701():
    """Event 1048360701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9611))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9612))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60510)
    Wait(0.20000000298023224)
    Restart()
