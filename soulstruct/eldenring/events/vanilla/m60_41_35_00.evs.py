"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1041350000, obj=1041351950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(1041351680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005300, args=(1041350210, 1041350210, 40144, 0.0, 0), arg_types="IIifi")
    Event_1041350700(0, character=1041350700)
    Event_1041350701()
    RunCommonEvent(0, 90005708, args=(1041350700, 6001, 0), arg_types="III")
    Event_1041353702()


@RestartOnRest(1041352680)
def Event_1041352680():
    """Event 1041352680"""
    CreateObjectVFX(1041351680, vfx_id=100, model_point=800)


@RestartOnRest(1041350700)
def Event_1041350700(_, character: uint):
    """Event 1041350700"""
    DisableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(1041350701)
def Event_1041350701():
    """Event 1041350701"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9611)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9612)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 60510, unknown2=1.0)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(1041353702)
def Event_1041353702():
    """Event 1041353702"""
    DisableFlag(1041359950)
    EndIfPlayerNotInOwnWorld()
    EnableFlag(1041359950)
    End()
