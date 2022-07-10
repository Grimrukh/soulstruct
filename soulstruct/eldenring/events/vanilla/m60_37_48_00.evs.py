"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037480000, obj=1037481950, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1037480200, 1037480200, 40236, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1037480210, 1037480210, 40254, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037480700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005451, args=(1037480400, 1037486420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1037480400, 1237480400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1037480400, 1237482400, 1237480400), arg_types="III")
    RunCommonEvent(0, 90005458, args=(1037480400, 1037481401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481420, 101, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1037480400, 1037481421, 102, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481422, 103, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481423, 104, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481424, 105, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481425, 106, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481426, 107, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481427, 108, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481428, 109, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481429, 110, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481430, 111, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481436, 117, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481437, 118, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481438, 119, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481439, 120, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481440, 121, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481441, 122, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481442, 123, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481443, 124, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481444, 125, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481445, 126, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481446, 127, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481447, 128, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481452, 133, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481453, 134, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481454, 135, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481455, 136, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481456, 137, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481457, 138, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481458, 139, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481459, 140, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481460, 141, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481461, 142, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481468, 149, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481469, 150, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481470, 151, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481471, 152, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481472, 153, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481473, 154, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481474, 155, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481475, 156, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481476, 157, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481477, 158, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1037480400, 1037481478, 159, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005456, args=(1037480400, 1037481410, 1037481418, 1037480400), arg_types="IIII")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1037480400, 1037481400, 1037481410, 1037481418), arg_types="IIII")
