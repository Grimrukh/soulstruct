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
    RegisterGrace(grace_flag=1033440000, obj=1033441950, unknown=5.0)
    RunCommonEvent(0, 90005460, args=(1033440200,))
    RunCommonEvent(0, 90005461, args=(1033440200,))
    RunCommonEvent(0, 90005462, args=(1033440200,))
    RunCommonEvent(0, 90005460, args=(1033440201,))
    RunCommonEvent(0, 90005461, args=(1033440201,))
    RunCommonEvent(0, 90005462, args=(1033440201,))
    RunCommonEvent(0, 90005460, args=(1033440204,))
    RunCommonEvent(0, 90005461, args=(1033440204,))
    RunCommonEvent(0, 90005462, args=(1033440204,))
    RunCommonEvent(0, 90005460, args=(1033440205,))
    RunCommonEvent(0, 90005461, args=(1033440205,))
    RunCommonEvent(0, 90005462, args=(1033440205,))
    RunCommonEvent(0, 90005460, args=(1033440206,))
    RunCommonEvent(0, 90005461, args=(1033440206,))
    RunCommonEvent(0, 90005462, args=(1033440206,))
    RunCommonEvent(0, 90005683, args=(62202, 1033441684, 209, 78292, 78292), arg_types="IIiII")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1033440180, 1033442181, 1033442182, 1033440700, 23, 1033442701, 1033442700, 0.0, 1045349259, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1033440180, 1033442181, 1033442182, 1033440700), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(1033440180, 1033442181, 1033442182, 1033440700, 100610, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005793,
        args=(1033440180, 1033442181, 1033442182, 1033440700, 1033442701, 0, 0),
        arg_types="IIIIIIi",
    )
    Event_1033440700(0, character=1033440701, animation_id=930027)
    Event_1033440700(1, character=1033440702, animation_id=930029)
    Event_1033440700(2, character=1033440703, animation_id=930028)
    Event_1033440705(0, obj=1033441700)
    Event_1033440705(1, obj=1033441701)
    Event_1033440705(2, obj=1033441702)
    Event_1033440705(3, obj=1033441703)
    Event_1033440705(4, obj=1033441704)
    Event_1033440710(0, obj=1033441710)
    Event_1033440710(1, obj=1033441711)
    Event_1033440710(2, obj=1033441715)
    Event_1033440710(3, 1033441713)


@RestartOnRest(1033440700)
def Event_1033440700(_, character: uint, animation_id: int):
    """Event 1033440700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3409)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3409)
    Restart()


@RestartOnRest(1033440705)
def Event_1033440705(_, obj: uint):
    """Event 1033440705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableObject(obj)
    DisableTreasure(obj=obj)
    IfFlagEnabled(MAIN, 3409)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableObject(obj)
    EnableTreasure(obj=obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3409)
    Restart()


@RestartOnRest(1033440710)
def Event_1033440710(_, obj: uint):
    """Event 1033440710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L9, flag=3409)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 3409)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3409)
    Restart()
