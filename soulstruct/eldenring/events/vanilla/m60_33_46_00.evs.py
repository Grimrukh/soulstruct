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
    RegisterGrace(grace_flag=1033460000, obj=1033461950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76214, 76210, 1033461980, 77220, 0, 78220, 78221, 78222, 78223, 78224, 78225, 78226, 78227, 78228, 78229),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005251, args=(1033460200, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1033460201, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1033460203, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1033460204, 7.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(
        0,
        90005605,
        args=(1033461610, 13, 0, 0, 0, 13002509, 0, 1033462610, 1033462611, 1033462612, 1033460610, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    Event_1033462611(
        0,
        flag=1033460611,
        destination=1033461611,
        left_flag=1033462613,
        cancel_flag__right_flag=1033462614
    )
    Event_1033462612(0, 1033460611, 1033461612)


@RestartOnRest(1033462611)
def Event_1033462611(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint):
    """Event 1033462611"""
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
    EnableNetworkFlag(1033460610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1033462612)
def Event_1033462612(_, flag: uint, obj: uint):
    """Event 1033462612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    IfFlagEnabled(MAIN, flag)
    EnableObject(obj)
