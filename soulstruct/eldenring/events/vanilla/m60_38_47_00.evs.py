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
    RegisterGrace(grace_flag=1038470000, obj=1038471950, unknown=5.0)
    RunCommonEvent(0, 90005400, args=(1038470340, 0, 0.0, 0.0, 0), arg_types="IiffI")
    RunCommonEvent(0, 90005401, args=(0, 1038470340), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038470700)
    RunCommonEvent(0, 90005251, args=(1038470250, 30.0, 0.0, 1700), arg_types="Iffi")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005451, args=(1038470400, 1038476420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1038470400, 1238470400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1038470400, 1238472400, 1238470400), arg_types="III")
    RunCommonEvent(0, 90005458, args=(1038470400, 1038471401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471420, 101, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1038470400, 1038471421, 102, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471422, 103, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471423, 104, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471424, 105, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471425, 106, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471426, 107, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471427, 108, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471428, 109, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471429, 110, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471430, 111, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471436, 117, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471437, 118, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471438, 119, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471439, 120, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471440, 121, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471441, 122, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471442, 123, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471443, 124, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471444, 125, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471445, 126, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471446, 127, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471447, 128, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471452, 133, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471453, 134, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471454, 135, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471455, 136, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471456, 137, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471457, 138, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471458, 139, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471459, 140, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471460, 141, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471461, 142, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471468, 149, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471469, 150, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471470, 151, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471471, 152, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471472, 153, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471473, 154, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471474, 155, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471475, 156, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471476, 157, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471477, 158, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1038470400, 1038471478, 159, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005456, args=(1038470400, 1038471410, 1038471418, 1238470400), arg_types="IIII")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1038470400, 1038471400, 1038471410, 1038471418), arg_types="IIII")
