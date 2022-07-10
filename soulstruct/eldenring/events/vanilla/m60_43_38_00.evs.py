"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043380000, obj=1043381950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(1043381680, 100, 800, 1043388540), arg_types="IiiI")
    RunCommonEvent(0, 90005683, args=(62105, 1043381684, 208, 78194, 78194), arg_types="IIiII")
    RunCommonEvent(0, 90005251, args=(1043380260, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005460, args=(1043380280,))
    RunCommonEvent(0, 90005461, args=(1043380280,))
    RunCommonEvent(0, 90005462, args=(1043380280,))
    Event_1043382270()
    Event_1043382270(slot=1)
    Event_1043383700(0, character=1043380700, attacker=1043370740)
    Event_1043383701(
        0,
        character=1043380700,
        character_1=1043380701,
        region=1043372703,
        region_1=1043382701,
        destination=1043372705,
        destination_1=1043382702,
        destination_2=1043372708
    )
    Event_1043383702(0, character=1043380700)
    Event_1043383703(0, 1043380700, 1043372712, 160.0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043380700)


@RestartOnRest(1043382270)
def Event_1043382270():
    """Event 1043382270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1043380270)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1043382270)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1043380270,
        source_entity=1043382271,
        model_point=900,
        behavior_id=802101070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1043382650)
def Event_1043382650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1043382650"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfPlayerHasGood(OR_1, 215000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 240000, including_storage=True)
    IfPlayerHasGood(OR_1, 243000, including_storage=True)
    IfPlayerHasGood(OR_1, 234000, including_storage=True)
    IfPlayerHasGood(OR_1, 244000, including_storage=True)
    IfPlayerHasGood(OR_1, 236000, including_storage=True)
    IfPlayerHasGood(OR_1, 232000, including_storage=True)
    IfPlayerHasGood(OR_1, 212000, including_storage=True)
    IfPlayerHasGood(OR_1, 241000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 233000, including_storage=True)
    IfPlayerHasGood(OR_1, 245000, including_storage=True)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9530)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NE_SE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1043383700)
def Event_1043383700(_, character: uint, attacker: uint):
    """Event 1043383700"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfFlagDisabled(AND_1, 3625)
    IfFlagDisabled(AND_1, 3626)
    IfFlagDisabled(OR_1, 3620)
    IfConditionTrue(OR_1, input_condition=AND_1)
    EndIfConditionTrue(input_condition=OR_1)
    GotoIfFlagDisabled(Label.L1, flag=1043372714)
    GotoIfFlagEnabled(Label.L2, flag=1043372714)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=PLAYER, attacker=attacker)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(10.0)
    EndIfFlagDisabled(1043372714)
    IfFlagDisabled(AND_2, 3625)
    IfFlagDisabled(AND_2, 3626)
    IfFlagDisabled(OR_2, 3620)
    IfConditionTrue(OR_2, input_condition=AND_2)
    EndIfConditionTrue(input_condition=OR_2)
    EnableFlag(1043372717)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfFlagDisabled(OR_3, 1043372714)
    IfCharacterDead(OR_3, character)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableFlag(1043372718)
    End()


@RestartOnRest(1043383701)
def Event_1043383701(
    _,
    character: uint,
    character_1: uint,
    region: uint,
    region_1: uint,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
):
    """Event 1043383701"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfFlagDisabled(AND_1, 3625)
    IfFlagDisabled(AND_1, 3626)
    IfFlagDisabled(OR_1, 3620)
    IfConditionTrue(OR_1, input_condition=AND_1)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(MAIN, 1043372717)
    EnableBackread(character)
    EnableBackread(character_1)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_1)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character_1)
    EnableCharacter(character)
    ForceAnimation(character, 63010, unknown2=1.0)
    AddSpecialEffect(character, 9651)
    SetTeamType(character, TeamType.WhitePhantom)
    DisplayUnknownMessage_12(text=80000, unknown1=0)
    End()


@RestartOnRest(1043383702)
def Event_1043383702(_, character: uint):
    """Event 1043383702"""
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfFlagDisabled(AND_1, 3625)
    IfFlagDisabled(AND_1, 3626)
    IfFlagDisabled(OR_1, 3620)
    IfConditionTrue(OR_1, input_condition=AND_1)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(MAIN, 1043372718)
    WaitFrames(frames=1)
    IfCharacterDead(AND_2, character)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L2, flag=1043379262)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    DisplayUnknownMessage_12(text=80002, unknown1=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 18677)
    ClearTargetList(character)
    ReplanAI(character)
    DisplayUnknownMessage_12(text=80001, unknown1=0)
    Wait(10.0)
    DisableBackread(character)
    DisableCharacter(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    SetTeamType(character, TeamType.NoTeam)
    ClearTargetList(character)
    ReplanAI(character)
    Wait(1.0)
    AddSpecialEffect(character, 18677)
    DisplayUnknownMessage_12(text=80003, unknown1=0)
    Wait(10.0)
    DisableBackread(character)
    DisableCharacter(character)
    End()


@RestartOnRest(1043383703)
def Event_1043383703(_, character: uint, flag: uint, distance: float):
    """Event 1043383703"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=character, distance=17.0)
    WaitFramesAfterCutscene(frames=1)
    EndIfFlagDisabled(3620)
    IfFlagDisabled(AND_1, 3625)
    IfFlagDisabled(AND_1, 3626)
    EndIfConditionTrue(input_condition=AND_1)
    EndIfFlagEnabled(1043379262)
    EndIfFlagEnabled(1043372716)
    IfFlagDisabled(AND_2, 1043372713)
    IfFlagEnabled(AND_2, 1043372717)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableNetworkFlag(flag)
    End()
