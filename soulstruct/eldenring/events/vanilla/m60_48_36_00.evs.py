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
    RegisterGrace(grace_flag=1048360000, obj=1048361950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76458, 76404, 1048361980, 77410, 1, 78410, 78411, 78412, 78413, 78414, 78415, 78416, 78417, 78418, 78419),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005250, args=(1048360201, 1048362201, 0.0, -1), arg_types="IIfi")
    Event_1048360700(0, character=1048360700)
    Event_1048360701()


@RestartOnRest(1048360700)
def Event_1048360700(_, character: uint):
    """Event 1048360700"""
    DisableGravity(character)
    DisableAnimations(character)


@RestartOnRest(1048360701)
def Event_1048360701():
    """Event 1048360701"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9611)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9612)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 60510, unknown2=1.0)
    Wait(0.20000000298023224)
    Restart()
