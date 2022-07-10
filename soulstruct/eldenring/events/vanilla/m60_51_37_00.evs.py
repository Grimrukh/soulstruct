"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1051372598(
        0,
        obj=1051371600,
        area_id=60,
        block_id=51,
        cc_id=37,
        dd_id=0,
        player_start__region=1051382300,
        unknown1=0,
        flag=0,
        left_flag=1052382610,
        cancel_flag__right_flag=1052382611
    )
    Event_1051372599()


@RestartOnRest(1051372598)
def Event_1051372598(
    _,
    obj: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start__region: uint,
    unknown1: int,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 1051372598"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=806870)
    IfPlayerInOwnWorld(AND_1)
    IfTryingToJoinSession(AND_2)
    IfConditionFalse(AND_1, input_condition=AND_2)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=obj)
    IfTryingToJoinSession(AND_4)
    IfTryingToCreateSession(AND_5)
    IfConditionFalse(AND_4, input_condition=AND_5)
    IfPlayerInOwnWorld(AND_7)
    IfTryingToJoinSession(AND_7)
    IfTryingToCreateSession(AND_7)
    IfActionButtonParamActivated(AND_7, action_button_id=9140, entity=obj)
    IfMultiplayerState(OR_2, state=MultiplayerState.Unknown6)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(AND_8, input_condition=OR_2)
    IfConditionTrue(OR_14, input_condition=AND_1)
    IfConditionTrue(OR_14, input_condition=AND_4)
    IfConditionTrue(OR_14, input_condition=AND_7)
    IfConditionTrue(OR_14, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_14)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_7)
    DeleteObjectVFX(obj)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
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
    IfTryingToJoinSession(AND_10)
    IfTryingToCreateSession(AND_10)
    IfConditionTrue(OR_15, input_condition=AND_10)
    IfTryingToJoinSession(AND_11)
    IfConditionFalse(AND_12, input_condition=AND_11)
    IfTryingToCreateSession(AND_13)
    IfConditionFalse(AND_12, input_condition=AND_13)
    IfConditionTrue(OR_15, input_condition=AND_12)
    SkipLinesIfConditionTrue(1, OR_15)
    Restart()
    IfMultiplayerState(OR_4, state=MultiplayerState.Unknown6)
    IfFailedToCreateSession(OR_4)
    RestartIfConditionTrue(input_condition=OR_4)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    EnableNetworkFlag(1052382602)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=player_start__region,
        unknown2=10,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    DisableInvincibility(PLAYER)
    GotoIfFlagEnabled(Label.L4, flag=1252380800)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(1052385800)
    BanishInvaders(unknown=0)
    EnableNetworkFlag(1052382805)

    # --- Label 4 --- #
    DefineLabel(4)
    Restart()
    SkipLines(1)
    DisableFlag(flag)
    SkipLines(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start__region, unknown1=unknown1)


@RestartOnRest(1051372599)
def Event_1051372599():
    """Event 1051372599"""
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    IfFlagEnabled(MAIN, 1052382602)
    Unknown_2004_74(
        character=20000,
        unknown1=1,
        region=1051382302,
        unknown2=10,
        character_2=20000,
        unknown3=0,
        unknown4=1,
    )
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    ActivateMultiplayerBuffs(1052385800)
    EnableNetworkFlag(1052382806)

    # --- Label 1 --- #
    DefineLabel(1)
    End()
