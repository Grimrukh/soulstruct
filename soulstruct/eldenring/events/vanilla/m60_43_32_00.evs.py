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
    RunCommonEvent(0, 9005910, args=(1043321940, 1043320101, 1043320101, 1), arg_types="IIIi")
    RunCommonEvent(0, 9005911, args=(1043321941,))
    RunCommonEvent(0, 9005912, args=(1043320100, 605055), arg_types="Ii")
    RunCommonEvent(0, 90005550, args=(1043320500, 1043321500, 43323500), arg_types="III")
    Event_1043322215(0, 1043320215, 1043322215)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1043320200, 1043322200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1043320201, 1043322200, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1043320202, 5.0, 0.0, 3005), arg_types="Iffi")


@RestartOnRest(1043322215)
def Event_1043322215(_, character: uint, region: uint):
    """Event 1043322215"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(character, 8080)
