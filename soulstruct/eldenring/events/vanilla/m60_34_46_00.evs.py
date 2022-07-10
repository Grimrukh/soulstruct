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
    RegisterGrace(grace_flag=1034460000, obj=1034461950, unknown=5.0)
    RunCommonEvent(0, 90005920, args=(1034460600, 1034461600, 1034463600), arg_types="III")


@RestartOnRest(1034462210)
def Event_1034462210(_, entity: uint):
    """Event 1034462210"""
    ForceAnimation(entity, 30000, unknown2=1.0)
    DisableObject(1038461210)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1034462210)
    EnableObject(1038461210)
    Wait(3.0)
    ForceAnimation(entity, 20000, unknown2=1.0)
    Wait(6.0)
    DisableObject(1038461210)
    End()
