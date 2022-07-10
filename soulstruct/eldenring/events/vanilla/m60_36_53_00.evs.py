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
    RunCommonEvent(0, 90005261, args=(1036530200, 1036532200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1036530200, 30001, 20001, 1036532200, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1036530201, 1036532200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1036530201, 30001, 20001, 1036532200, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    Event_1036532300()
    Event_1036532500()
    Event_1036532450(0, obj=1036531400)
    Event_1036532450(1, obj=1036531401)
    Event_1036532450(2, obj=1036531402)
    Event_1036533700()


@RestartOnRest(1036532300)
def Event_1036532300():
    """Event 1036532300"""
    CancelSpecialEffect(1036530300, 5070)
    CancelSpecialEffect(1036530301, 5070)
    CancelSpecialEffect(1036530302, 5070)
    CancelSpecialEffect(1036530303, 5070)
    CancelSpecialEffect(1036530304, 5070)
    CancelSpecialEffect(1036530305, 5070)
    CancelSpecialEffect(1036530306, 5070)
    CancelSpecialEffect(1036530307, 5070)


@RestartOnRest(1036532450)
def Event_1036532450(_, obj: uint):
    """Event 1036532450"""
    DisableObject(obj)
    End()


@NeverRestart(1036532500)
def Event_1036532500():
    """Event 1036532500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036532200, 1036531200, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036532201, 1036531201, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036532202, 1036531202, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")


@RestartOnRest(1036533700)
def Event_1036533700():
    """Event 1036533700"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3670)
    EndIfFlagEnabled(400179)
    IfFlagEnabled(AND_1, 400179)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1035539204)
    End()
