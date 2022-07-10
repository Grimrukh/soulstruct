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
    RegisterGrace(grace_flag=1035450000, obj=1035451950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76205, 1035451980, 77200, 5, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005725,
        args=(4750, 4751, 4753, 1035459205, 1035450700, 1035450701, 1035456700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1035450700, 4751, 4752, 1035459206, 4751, 4750, 4754, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1035450700, 4751, 4750, 1035459206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1035450700, 4753, 4750, 4754), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1035450701, 4751, 4752, 1035459207, 4751, 4750, 4754, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1035450701, 4751, 4750, 1035459207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1035450701, 1035452706, 1035452707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4751, 1035450700, 1035450701, 4750, 4753), arg_types="IIIII")
    Event_1035452500()
    Event_1035452600(
        0,
        anchor_entity=1035451600,
        area_id=60,
        block_id=35,
        cc_id=46,
        dd_id=0,
        player_start=1035462610,
        flag=1035460605,
        target_entity=1035452611,
        animation_id=60470,
        action_button_id=9522
    )
    Event_1035452605(0, 1035450605, 1035452601, 60471)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1035450700)
    DisableBackread(1035450701)
    RunCommonEvent(0, 90005251, args=(1035450200, 10.0, 0.0, 3011), arg_types="Iffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1035450210, 30002, 20002, 1035452210, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1035452500)
def Event_1035452500():
    """Event 1035452500"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1035457100)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 1035457100)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(2.0)
    DisplayDialog(text=30100, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)


@NeverRestart(1035452600)
def Event_1035452600(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag: uint,
    target_entity: uint,
    animation_id: int,
    action_button_id: int,
):
    """Event 1035452600"""
    EndIfPlayerNotInOwnWorld()
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    SkipLinesIfConditionTrue(7, OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=action_button_id, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfPlayerHasGood(AND_9, 8109)
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    DisplayDialog(text=20030, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(PLAYER, target_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id, unknown2=1.0)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1035452605)
def Event_1035452605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1035452605"""
    EndIfFlagDisabled(flag)
    IfFlagEnabled(MAIN, flag)
    WaitFrames(frames=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)
