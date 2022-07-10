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
    Event_1036472600(
        0,
        anchor_entity=1036471600,
        area_id=60,
        block_id=35,
        cc_id=46,
        dd_id=0,
        player_start=1035462611,
        flag=1035460615,
        target_entity=1036472601,
        animation=60470,
        action_button_id=9522
    )
    Event_1036472605(0, flag=1036470605, target_entity=1036472606, animation=60471)
    RunCommonEvent(0, 90005637, args=(32020691, 1036470620, 1036471620), arg_types="III")
    RunCommonEvent(
        0,
        90005636,
        args=(32020691, 1036470620, 1036471620, 4470, 1036472620, 1036472621, 1036472620, 1036473620, -1),
        arg_types="IIIiIIIIi",
    )


@NeverRestart(1036472600)
def Event_1036472600(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag: uint,
    target_entity: uint,
    animation: int,
    action_button_id: int,
):
    """Event 1036472600"""
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
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1036472605)
def Event_1036472605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1036472605"""
    EndIfFlagDisabled(flag)
    IfFlagEnabled(MAIN, flag)
    WaitFrames(frames=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036470700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005451, args=(1036470400, 1036476420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1036470400, 1236470400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1036470400, 1236472400, 1236470400), arg_types="III")
    RunCommonEvent(0, 90005456, args=(1036470400, 1036471410, 1036471418, 1236470400), arg_types="IIII")
    RunCommonEvent(0, 90005458, args=(1036470400, 1036471401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471420, 60, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1036470400, 1036471421, 61, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471422, 62, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471423, 63, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471424, 64, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471425, 65, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471426, 66, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471427, 67, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471428, 68, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471429, 69, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471430, 70, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471431, 71, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471432, 72, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471433, 73, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471434, 74, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1036470400, 1036471435, 75, 0.5), arg_types="IIif")
    Event_1036472340()
    Event_1036472490()


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1036470400, 1036471400, 1036471410, 1036471418), arg_types="IIII")


@RestartOnRest(1036472340)
def Event_1036472340():
    """Event 1036472340"""
    EndIfFlagEnabled(1036470400)
    IfCharacterInsideRegion(MAIN, character=1036470400, region=1036472340)
    ChangePatrolBehavior(1036470400, patrol_information_id=1036473340)


@RestartOnRest(1036472490)
def Event_1036472490():
    """Event 1036472490"""
    EndIfFlagDisabled(1036470400)
    DisableObject(1036471420)
    DisableObject(1036471421)
    DisableObject(1036471422)
    DisableObject(1036471423)
    DisableObject(1036471424)
    DisableObject(1036471425)
    DisableObject(1036471426)
    DisableObject(1036471427)
    DisableObject(1036471428)
    DisableObject(1036471429)
    DisableObject(1036471430)
    DisableObject(1036471431)
    DisableObject(1036471432)
    DisableObject(1036471433)
    DisableObject(1036471434)
    DisableObject(1036471435)
