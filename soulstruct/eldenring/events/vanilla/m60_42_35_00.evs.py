"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1042352222(0, character=1042350222, region=1042352222)
    Event_1042352222(1, character=1042350223, region=1042352223)
    Event_1042352222(2, character=1042350224, region=1042352223)
    RunCommonEvent(
        0,
        90005633,
        args=(580340, 580040, 1042350600, 30017, 20017, 1042351600, 1042351610),
        arg_types="IIIiiII",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005250, args=(1042350210, 1042352210, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1042350200, 30016, 20016, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1042350200, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1042350201, 30016, 20016, 20.0, 1.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1042350201, 20.0, 1.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1042350202, 30016, 20016, 20.0, 1.5, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1042350202, 20.0, 1.5, -1), arg_types="Iffi")


@RestartOnRest(1042352222)
def Event_1042352222(_, character: uint, region: uint):
    """Event 1042352222"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(character, 8080)
