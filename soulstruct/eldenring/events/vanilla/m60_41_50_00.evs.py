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
    RunCommonEvent(0, 90005870, args=(1041500800, 904680602, 19), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1041500800, 0, 1041500800, 0, 30310, 0.0), arg_types="IIIIif")
    Event_1041502200()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005201, args=(1041500800, 30009, 20009, 30.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")


@RestartOnRest(1041502200)
def Event_1041502200():
    """Event 1041502200"""
    GotoIfFlagEnabled(Label.L0, flag=1041500800)
    IfUnknownCharacterCondition_35(MAIN, character=1041500800, unk_8_12=1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(1041502200, erase_root_only=False)
    End()
