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
    RegisterGrace(grace_flag=1038480000, obj=1038481950, unknown=5.0)
    RunCommonEvent(0, 90005870, args=(1038480800, 904810601, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1038480800, 0, 1038480800, 0, 30200, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1038480800, 18, 0), arg_types="III")
    Event_1038482580()
    RunCommonEvent(0, 90005683, args=(62201, 1038481684, 209, 78290, 78290), arg_types="IIiII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038480700)
    RunCommonEvent(0, 90005261, args=(1038480200, 1038482200, 0.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480201, 1038482200, 0.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480202, 1038482200, 0.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480203, 1038482200, 0.0, 1.399999976158142, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480204, 1038482200, 0.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480205, 1038482200, 0.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480206, 1038482200, 0.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480207, 1038482200, 0.0, 1.399999976158142, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480208, 1038482200, 0.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480209, 1038482200, 0.0, 0.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480210, 1038482200, 0.0, 1.399999976158142, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1038480211, 1038482200, 0.0, 1.0, 1705), arg_types="IIffi")


@NeverRestart(1038482580)
def Event_1038482580():
    """Event 1038482580"""
    RegisterLadder(start_climbing_flag=1038480580, stop_climbing_flag=1038480581, obj=1038481580)
    RegisterLadder(start_climbing_flag=1038480582, stop_climbing_flag=1038480583, obj=1038481582)
    RegisterLadder(start_climbing_flag=1038480584, stop_climbing_flag=1038480585, obj=1038481584)
