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
    RegisterGrace(grace_flag=1033470000, obj=1033471950, unknown=5.0)
    RunCommonEvent(
        0,
        90005605,
        args=(1033471610, 12, 2, 0, 0, 12022210, 0, 1033472610, 1033472611, 1033472612, 1033470610, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1033472611(
        0,
        flag=1033470611,
        destination=1033471611,
        left_flag=1033472613,
        cancel_flag__right_flag=1033472614
    )
    Event_1033472612(0, 1033470611, 1033471612)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1033470200, 1033472200, 0.0, 1.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1033470201, 1033472200, 0.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1033470202, 1033472200, 0.0, 2.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1033470203, 1033472200, 0.0, 1.5, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1033470204, 1033472200, 0.0, 0.0, 1705), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1033470205, 1033472200, 0.0, 1.0, 1705), arg_types="IIffi")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005421, args=(1033470300, 1033471301, 1033478301), arg_types="III")
    RunCommonEvent(0, 90005422, args=(1033478301, 1033471300, 1033473301), arg_types="III")
    RunCommonEvent(0, 90005424, args=(1033471300, 1033470302, 1033470303, 1033470300, 1033471301), arg_types="IIIII")
    RunCommonEvent(0, 90005423, args=(1033470302,))
    RunCommonEvent(0, 90005423, args=(1033470303,))


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(
        0,
        90005420,
        args=(1033470300, 1033471300, 1033471301, 1033470301, 1033470302, 1033470303, 0.0),
        arg_types="IIIIIIf",
    )


@RestartOnRest(1033472610)
def Event_1033472610(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 1033472610"""
    EndIfTryingToCreateSession()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L5, flag=1033470610)
    DisplayDialogAndSetFlags(
        message=108186,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerHasGood(AND_5, 8186)
    SkipLinesIfConditionTrue(3, AND_5)
    DisplayDialogAndSetFlags(
        message=308186,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=0,
        right_flag=0,
        cancel_flag=0,
    )
    Wait(1.0)
    Restart()
    EnableFlag(1033470610)
    DisplayDialogAndSetFlags(
        message=208186,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
        anchor_entity=anchor_entity,
        display_distance=2.0,
        left_flag=0,
        right_flag=0,
        cancel_flag=0,
    )
    RemoveGoodFromPlayer(item=8186, quantity=1)

    # --- Label 5 --- #
    DefineLabel(5)
    RotateToFaceEntity(PLAYER, anchor_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1033472611)
def Event_1033472611(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint):
    """Event 1033472611"""
    IfFlagEnabled(OR_1, flag)
    IfPlayerNotInOwnWorld(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfActionButtonParamActivated(MAIN, action_button_id=9523, entity=destination)
    DisplayDialogAndSetFlags(
        message=108186,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerHasGood(AND_2, 8186)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050, unknown2=1.0)
    Wait(1.5)
    DisplayDialog(text=308186, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810, unknown2=1.0)
    Wait(2.5)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(1033470610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1033472612)
def Event_1033472612(_, flag: uint, obj: uint):
    """Event 1033472612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    IfFlagEnabled(MAIN, flag)
    EnableObject(obj)
