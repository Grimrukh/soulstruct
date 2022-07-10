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
    RegisterGrace(grace_flag=1042330000, obj=1042331950, unknown=5.0)
    RunCommonEvent(0, 90005300, args=(1042330220, 1042330220, 40132, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(1042330405, 1042332400, 5.0, 0.0, 3006), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005620,
        args=(1042330570, 1042331570, 1042331571, 0, 1042332570, 1042332571, 1042332572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005880,
        args=(1042330800, 1042330805, 1042332800, 1042330800, 1042330100, 60, 42, 33, 0, 1042332805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1042330800,
            1042330805,
            1042332800,
            1042330800,
            1042332806,
            1042335810,
            1042331800,
            1042330810,
            1042332810,
            907100520,
            -1,
            20002,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005885, args=(1042330800, 0, 1042332806, 1042332807, 0, 1), arg_types="IiIIii")
    Event_1042332575(
        0,
        1042330800,
        1042330805,
        1042332801,
        1042332802,
        20300,
        1042331805,
        60,
        42,
        33,
        0,
        1042332805,
        1042330570,
    )
    Event_1042332576(0, flag=1042330800, flag_1=1042330805, entity=1042331805, flag_2=1042330570)
    RunCommonEvent(0, 90005400, args=(1042330230, 0, 0.0, 0.0, 0), arg_types="IiffI")
    RunCommonEvent(0, 90005401, args=(0, 1042330230), arg_types="II")
    Event_1042332200(0, 1042330200, 0.0)
    Event_1042332200(1, 1042330201, 2.0)
    Event_1042332200(2, 1042330202, 1.0)
    Event_1042332200(3, 1042330203, 0.5)
    Event_1042332200(4, 1042330204, 1.5)
    Event_1042332200(5, 1042330205, 2.0)
    Event_1042332200(6, 1042330206, 0.0)
    Event_1042332200(7, 1042330207, 2.5)
    Event_1042332200(8, 1042330208, 3.0)
    Event_1042332200(9, 1042330209, 0.5)
    Event_1042332200(10, 1042330210, 0.0)
    Event_1042332200(11, 1042330212, 0.0)
    Event_1042332200(12, 1042330213, 2.5)
    Event_1042332200(13, 1042330214, 3.0)


@RestartOnRest(1042332200)
def Event_1042332200(_, character: uint, seconds: float):
    """Event 1042332200"""
    GotoIfFlagDisabled(Label.L0, flag=1242330400)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, 1242330400)
    IfConditionTrue(MAIN, input_condition=MAIN)
    Wait(seconds)
    Kill(character)


@RestartOnRest(1042332575)
def Event_1042332575(
    _,
    flag: uint,
    flag_1: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    message: int,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start__region: uint,
    flag_2: uint,
):
    """Event 1042332575"""
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfLeavingSession(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9230, entity=anchor_entity)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    RestartIfFlagEnabled(cancel_flag__right_flag)
    IfTryingToCreateSession(OR_3)
    IfTryingToJoinSession(OR_3)
    RestartIfConditionTrue(input_condition=OR_3)
    SkipLinesIfFlagEnabled(4, flag_2)
    Wait(0.5)
    DisplayDialog(text=20510, anchor_entity=anchor_entity, display_distance=5.0)
    Wait(3.0)
    Restart()
    EnableNetworkFlag(flag_1)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450, unknown2=1.0)
    Wait(1.5)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=player_start__region,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=1,
        unknown4=1,
    )
    EnableFlag(9021)
    End()
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start__region)


@RestartOnRest(1042332576)
def Event_1042332576(_, flag: uint, flag_1: uint, entity: uint, flag_2: uint):
    """Event 1042332576"""
    ForceAnimation(entity, 0, loop=True, unknown2=1.0)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    IfLeavingSession(AND_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True, unknown2=1.0)
    IfLeavingSession(AND_11)
    IfTryingToJoinSession(AND_12)
    IfConditionFalse(AND_11, input_condition=AND_12)
    IfConditionFalse(MAIN, input_condition=AND_11)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042330700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005451, args=(1042330400, 1042336420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1042330400, 1242330400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1042330400, 1242332400, 1242330400), arg_types="III")
    RunCommonEvent(0, 90005458, args=(1042330400, 1042331401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331420, 101, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1042330400, 1042331421, 102, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331422, 103, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331423, 104, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331424, 105, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331425, 106, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331426, 107, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331427, 108, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331428, 109, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331429, 110, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331430, 111, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331436, 117, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331437, 118, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331438, 119, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331439, 120, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331440, 121, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331441, 122, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331442, 123, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331443, 124, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331444, 125, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331445, 126, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331446, 127, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331447, 128, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331452, 133, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331453, 134, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331454, 135, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331455, 136, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331456, 137, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331457, 138, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331458, 139, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331459, 140, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331460, 141, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331461, 142, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331468, 149, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331469, 150, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331470, 151, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331471, 152, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331472, 153, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331473, 154, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331474, 155, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331475, 156, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331476, 157, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331477, 158, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1042330400, 1042331478, 159, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005456, args=(1042330400, 1042331410, 1042331418, 1042330400), arg_types="IIII")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1042330400, 1042331400, 1042331410, 1042331418), arg_types="IIII")


@RestartOnRest(1042332800)
def Event_1042332800():
    """Event 1042332800"""
    IfFlagEnabled(OR_1, 1042332800)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableCharacter(1042335800)
    DisableAnimations(1042335800)
    DisableObject(1042335801)
    IfFlagEnabled(AND_1, 1042330800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(7.0)
    EnableCharacter(1042335800)
    EnableAnimations(1042335800)
    EnableObject(1042335801)
