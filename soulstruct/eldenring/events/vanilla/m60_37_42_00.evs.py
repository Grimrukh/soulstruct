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
    RunCommonEvent(0, 90005860, args=(1037420800, 0, 1037420340, 0, 1037420400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1037420340, 904980603, 24), arg_types="IiI")
    RegisterGrace(grace_flag=1037420000, obj=1037421950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76203, 1037421980, 77200, 3, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005605,
        args=(1037421610, 60, 35, 45, 0, 1035452630, 0, 1037422610, 1037422611, 1037422612, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunEvent(1037422600, slot=0, args=(0,))
    RunCommonEvent(0, 90005630, args=(61374200, 1037421500, 123), arg_types="IIi")
    Event_1037423700(0, character=1037420700, obj=1037421700)
    Event_1037423702(0, 1037422704, 1037422703, 1037429207, 20.0)
    Event_1037423703(0, attacked_entity=1037421700, other_entity=1037420700)
    RunCommonEvent(0, 90005752, args=(1037421700, 200, 120, 3.0), arg_types="Iiif")
    Event_1037423710(0, character=1037420720, obj=1037421720)
    Event_1037423711(0, character=1037420720, flag=1037422731, flag_1=1038419251)
    Event_1037423712()
    RunCommonEvent(0, 90005704, args=(1037420720, 3681, 3680, 1038419251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1037420720, 3681, 3682, 1038419251, 3681, 3680, 3684, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1037420720, 3683, 3680, 3684), arg_types="IIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037420700)
    DisableBackread(1037420705)
    DisableObject(1037421700)
    RunCommonEvent(0, 90005261, args=(1037420200, 1037422200, 2.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1037420201, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037420207, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037420203, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037420204, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037420205, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1037420206, 10.0, 0.0, 1705), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1037420221, 1037422200, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037420222, 1037422200, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037420223, 1037422200, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037420224, 1037422200, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037420225, 1037422200, 2.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1037420213, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1037420340, 1037422340, 10.0, 0.0, 1700), arg_types="IIffi")


@RestartOnRest(1037422610)
def Event_1037422610(
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
    """Event 1037422610"""
    EndIfTryingToCreateSession()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfActionButtonParamActivated(AND_1, action_button_id=9140, entity=anchor_entity)
    IfLeavingSession(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayDialogAndSetFlags(
        message=4300,
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
    RotateToFaceEntity(PLAYER, anchor_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490, unknown2=1.0)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1037423700)
def Event_1037423700(_, character: uint, obj: uint):
    """Event 1037423700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3420)
    DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3425)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 3425)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    MoveObjectToCharacter(obj, character=character)
    DisableObject(obj)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3425)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1037423702)
def Event_1037423702(_, flag: uint, flag_1: uint, flag_2: uint, seconds: float):
    """Event 1037423702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3420)
    EndIfFlagDisabled(3425)
    EndIfFlagEnabled(flag_2)
    SetCharacterTalkRange(character=1037420700, distance=30.0)
    IfFlagEnabled(MAIN, flag_1)
    Wait(seconds)
    EnableFlag(flag)
    End()


@RestartOnRest(1037423703)
def Event_1037423703(_, attacked_entity: uint, other_entity: uint):
    """Event 1037423703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3425)
    EndIfFlagEnabled(1037422708)
    GotoIfFlagDisabled(Label.L1, flag=1037422701)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(AND_1, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(0.10000000149011612)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=20000)
    IfTimeElapsed(OR_2, seconds=7.0)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(OR_3, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionFalse(Label.L7, input_condition=AND_2)
    Wait(0.10000000149011612)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L5, flag=1037422701)
    GotoIfFlagDisabled(Label.L6, flag=1037422707)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    IfEntityWithinDistance(AND_5, entity=20000, other_entity=other_entity, radius=10.0)
    SkipLinesIfConditionFalse(1, AND_5)
    EnableFlag(1037422702)
    IfFlagEnabled(MAIN, 1037422701)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    IfEntityWithinDistance(AND_6, entity=20000, other_entity=other_entity, radius=10.0)
    SkipLinesIfConditionFalse(1, AND_6)
    EnableFlag(1037422706)
    IfFlagEnabled(MAIN, 1037422707)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1037422708)
    End()


@RestartOnRest(1037423710)
def Event_1037423710(_, character: uint, obj: uint):
    """Event 1037423710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3687)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 3687)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    EnableObject(obj)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3687)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1037423711)
def Event_1037423711(_, character: uint, flag: uint, flag_1: uint):
    """Event 1037423711"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3683)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 3681)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfCharacterHasSpecialEffect(AND_2, PLAYER, 9700)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    End()


@RestartOnRest(1037423712)
def Event_1037423712():
    """Event 1037423712"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(31009206)
    EndIfFlagEnabled(1038419254)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    EndIfConditionTrue(input_condition=AND_1)
    EnableFlag(1038419254)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()
