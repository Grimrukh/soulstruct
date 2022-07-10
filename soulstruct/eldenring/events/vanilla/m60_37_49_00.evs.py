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
    RegisterGrace(grace_flag=1037490000, obj=1037491950, unknown=5.0)
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1037490180, 1037492181, 1037492182, 1038480700, 23, 1037492180, 1037492181, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1037490180, 1037492181, 1037492182, 1038480700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1037490180, 1037492181, 1037492182, 1038480700, 1037490300, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1037490180, 1037492181, 1037492182, 1038480700, 1037492180, 0, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005631, args=(1037491640, 61023), arg_types="Ii")
    RunCommonEvent(0, 90005201, args=(1037490401, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1037490403, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1037490405, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1037493700(0, 1037490700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037490700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005490, args=(1037490400, 1037490401, 1037491400, 0, 0, 1037492400, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1037490402, 1037490403, 1037491402, 0, 0, 1037492402, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1037490404, 1037490405, 1037491404, 0, 0, 1037492404, 1), arg_types="IIIIIII")


@RestartOnRest(1037493700)
def Event_1037493700(_, character: uint):
    """Event 1037493700"""
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    DisableAnimations(character)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(400033)
    EndIfFlagDisabled(400031)
    IfActionButtonParamActivated(MAIN, action_button_id=6472, entity=character)
    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()
