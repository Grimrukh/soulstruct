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
    RunCommonEvent(
        0,
        90005620,
        args=(1039500570, 1039501570, 1039501571, 0, 1039502571, 1039502572, 1039502573),
        arg_types="IIIIIIi",
    )
    Event_1039502580(
        0,
        flag=1039500800,
        flag_1=1039500805,
        flag_2=1039502800,
        character=1039500800,
        item_lot_param_id=1039500100,
        area_id=60,
        block_id=39,
        cc_id=50,
        dd_id=0,
        player_start=1039502805
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1039500800,
            1039500805,
            1039502800,
            1039500800,
            1039502806,
            1039505810,
            1039501800,
            1039500810,
            1039502810,
            904750520,
            -1,
            20012,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005885, args=(1039500800, 921100, 1039502806, 1039502807, 0, 1), arg_types="IiIIii")
    Event_1039502575(
        0,
        1039500800,
        1039500805,
        1039502801,
        1039502802,
        20300,
        1039501805,
        60,
        39,
        50,
        0,
        1039502805,
        1039500570,
    )
    Event_1039502576(0, 1039500800, 1039500805, 1039501805, 1039500570)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005251, args=(1039500400, 30.0, 1.0, 3022), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1039500450, 20.0, 0.0, 3020), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1039500451, 20.0, 0.0, 3020), arg_types="Iffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1039500307, 30000, 20000, 1039502300, 5.0, 0.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(1039500302, 30000, 20000, 1039502300, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1039500303, 30000, 20000, 1039502300, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1039502575)
def Event_1039502575(
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
    """Event 1039502575"""
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


@RestartOnRest(1039502576)
def Event_1039502576(_, flag: uint, flag_1: uint, entity: uint, flag_2: uint):
    """Event 1039502576"""
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


@RestartOnRest(1039502580)
def Event_1039502580(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    item_lot_param_id: int,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
):
    """Event 1039502580"""
    EndIfFlagEnabled(flag)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.Unknown)
    UnknownMap_12(unk_0_4=10.0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)
    Wait(5.0)
    AddSpecialEffect(20000, 8870)
    Wait(2.0)
    EnableFlag(flag_2)
    EnableFlag(9295)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
    End()
