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
    Event_1035472602()
    RunCommonEvent(0, 90005300, args=(1046390210, 1046390210, 40118, 0.0, 0), arg_types="IIifi")
    Event_1035472200(0, 1046391600, 60, 51, 43, 0, 1051430600, 0, 1051432650, 1051432651, 1051432652, 0, 0, 0.0, 0.0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1046390340, 1046392340, 30.0, 0.0, 0), arg_types="IIffi")


@NeverRestart(1035472200)
def Event_1035472200(
    _,
    obj: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    unknown1: int,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    left: uint,
    text: int,
    seconds: float,
    seconds_1: float,
):
    """Event 1035472200"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    SkipLinesIfThisEventSlotFlagEnabled(3)
    DeleteObjectVFX(obj)
    DisableFlag(flag)
    WaitFrames(frames=1)
    IfTryingToCreateSession(OR_10)
    IfTryingToJoinSession(OR_10)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_10, left)
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=806870)
    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    SkipLinesIfUnsignedEqual(3, left=left, right=0)
    SkipLinesIfValueNotEqual(2, left=text, right=0)
    IfFlagEnabled(AND_1, left)
    IfFlagEnabled(AND_1, flag)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=obj)
    IfTryingToCreateSession(OR_4)
    IfTryingToJoinSession(OR_4)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_4, left)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfFlagEnabled(AND_4, flag)
    IfTryingToCreateSession(OR_7)
    IfTryingToJoinSession(OR_7)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagDisabled(OR_7, left)
    IfConditionFalse(AND_7, input_condition=OR_7)
    IfFlagDisabled(AND_7, flag)
    IfFlagState(AND_9, FlagSetting.Change, FlagType.Absolute, left)
    IfConditionTrue(OR_14, input_condition=AND_1)
    IfConditionTrue(OR_14, input_condition=AND_4)
    IfConditionTrue(OR_14, input_condition=AND_7)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfConditionTrue(OR_14, input_condition=AND_9)
    IfConditionTrue(MAIN, input_condition=OR_14)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_4)
    DeleteObjectVFX(obj)
    DisableFlag(flag)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    IfUnsignedEqual(OR_13, left=left, right=0)
    IfValueEqual(OR_13, left=text, right=0)
    GotoIfConditionTrue(Label.L4, input_condition=OR_13)
    GotoIfFlagEnabled(Label.L4, flag=left)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=obj,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfTryingToCreateSession(OR_15)
    IfTryingToJoinSession(OR_15)
    RestartIfConditionTrue(input_condition=OR_15)
    EnableFlag(1051430210)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unknown1=unknown1)
    Restart()
    Wait(seconds)
    Wait(seconds_1)


@RestartOnRest(1035472602)
def Event_1035472602():
    """Event 1035472602"""
    AddSpecialEffect(1046390340, 8090)
