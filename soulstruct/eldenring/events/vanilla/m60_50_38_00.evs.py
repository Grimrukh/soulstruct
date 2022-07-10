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
    RegisterGrace(grace_flag=1050380000, obj=1050381950, unknown=5.0)
    RunCommonEvent(0, 90005200, args=(1050380200, 30000, 20000, 1050382200, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1050383700(0, character=1050380700, character_1=1050380702)
    RunCommonEvent(0, 90005702, args=(1050380700, 4163, 4160, 4163), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(1050380702, 4163, 4160, 4163), arg_types="IIII")
    Event_1050383701()
    Event_1050383702()
    Event_1050383703(0, character=1050380701)
    Event_1050383704(0, character=1050380700, obj=1050381702, character_1=1050380702)
    RunCommonEvent(0, 90005750, args=(1050381703, 4110, 103120, 400312, 400312, 7611, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(1050381703, 4110, 103120, 400312, 400312, 1050389238, 0), arg_types="IiiIIIi")
    Event_1050383710(0, character=1050380705)
    RunCommonEvent(0, 90005704, args=(1050380705, 4181, 4180, 1050389251, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1050380705, 4181, 4182, 1050389251, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1050380705, 4183, 4180, 4184), arg_types="IIII")
    Event_1050383711(0, character=1050380710)
    RunCommonEvent(0, 90005704, args=(1050380710, 4181, 4180, 1050389251, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1050380710, 4181, 4182, 1050389251, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1050380710, 4183, 4180, 4184), arg_types="IIII")
    Event_1050383712(0, character=1050380706)
    RunCommonEvent(0, 90005704, args=(1050380706, 4181, 4180, 1050389261, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1050380706, 4181, 4182, 1050389261, 1059481190, 4180, 4184, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005702, args=(1050380706, 4183, 4180, 4184), arg_types="IIII")
    Event_1050383713()
    Event_1050383714()
    RunCommonEvent(0, 90005752, args=(1050381700, 200, 120, 3.0), arg_types="Iiif")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1050380700)
    DisableBackread(1050380701)
    DisableBackread(1050380702)
    DisableBackread(1050380705)
    DisableBackread(1050380706)
    DisableObject(1050381700)


@RestartOnRest(1050383700)
def Event_1050383700(_, character: uint, character_1: uint):
    """Event 1050383700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 4165)
    IfFlagEnabled(OR_1, 4166)
    IfFlagEnabled(OR_1, 4167)
    IfFlagEnabled(OR_1, 4168)
    IfFlagEnabled(OR_1, 4169)
    IfFlagEnabled(OR_1, 4170)
    IfFlagEnabled(OR_1, 4171)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(1050381702)
    IfFlagEnabled(OR_1, 4165)
    IfFlagEnabled(OR_1, 4166)
    IfFlagEnabled(OR_1, 4167)
    IfFlagEnabled(OR_1, 4168)
    IfFlagEnabled(OR_1, 4169)
    IfFlagEnabled(OR_1, 4170)
    IfFlagEnabled(OR_1, 4171)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L3, flag=4171)
    GotoIfFlagEnabled(Label.L1, flag=4160)
    GotoIfFlagEnabled(Label.L2, flag=4161)
    GotoIfFlagEnabled(Label.L4, flag=4163)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableObject(1050381702)
    RestoreObject(1050381702)
    EnableObjectInvulnerability(1050381702)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 90102, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(1050381702)
    IfFlagDisabled(AND_1, 1050389266)
    IfFlagDisabled(AND_1, 4183)
    IfFlagEnabled(AND_1, 4187)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    EnableObject(1050381702)
    RestoreObject(1050381702)
    EnableObjectInvulnerability(1050381702)
    SkipLinesIfFlagRangeAllDisabled(4, (4165, 4168))
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    SkipLines(4)
    SkipLinesIfFlagRangeAllDisabled(3, (4169, 4170))
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 90100, unknown2=1.0)
    IfFlagEnabled(AND_3, 4168)
    IfFlagDisabled(AND_3, 1050389230)
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 90101, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(1, (4169, 4170))
    ForceAnimation(character_1, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    DisableObject(1050381702)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 4165)
    IfFlagEnabled(OR_15, 4166)
    IfFlagEnabled(OR_15, 4167)
    IfFlagEnabled(OR_15, 4168)
    IfFlagEnabled(OR_15, 4169)
    IfFlagEnabled(OR_15, 4170)
    IfFlagEnabled(OR_15, 4171)
    AwaitConditionFalse(OR_15)
    Restart()


@RestartOnRest(1050383701)
def Event_1050383701():
    """Event 1050383701"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 4166)
    IfFlagEnabled(AND_1, 1050389255)
    AwaitConditionTrue(AND_1)
    EnableFlag(4178)
    End()


@RestartOnRest(1050383702)
def Event_1050383702():
    """Event 1050383702"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 1050389228)
    IfFlagEnabled(AND_1, 1050389217)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    AwaitFlagEnabled(flag=110850)
    EnableNetworkFlag(1050389228)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1050383703)
def Event_1050383703(_, character: uint):
    """Event 1050383703"""
    DisableCharacter(character)
    DisableBackread(character)
    EndIfPlayerNotInOwnWorld()
    IfHealthValueEqual(OR_1, 1050380700, value=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050380700, attacker=0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterBackreadEnabled(AND_1, 1050380700)
    IfHealthValueEqual(OR_2, 1050380702, value=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1050380702, attacker=0)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterBackreadEnabled(AND_2, 1050380702)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    AwaitConditionTrue(OR_3)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    Kill(1050380700, award_souls=True)
    SkipLines(1)
    Kill(1050380702, award_souls=True)
    Wait(5.0)
    IfFlagEnabled(OR_4, 4169)
    IfFlagEnabled(OR_4, 4170)
    GotoIfConditionTrue(Label.L2, input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    Move(
        character,
        destination=1050380700,
        destination_type=CoordEntityType.Character,
        model_point=900,
        short_move=True,
    )
    EnableAnimations(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4163)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
    EnableNetworkFlag(4163)
    EnableNetworkFlag(1050389238)
    End()


@RestartOnRest(1050383704)
def Event_1050383704(_, character: uint, obj: uint, character_1: uint):
    """Event 1050383704"""
    EnableObjectInvulnerability(obj)
    IfHealthValueEqual(OR_1, character, value=0)
    IfHealthValueEqual(OR_1, character_1, value=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableObjectInvulnerability(obj)
    DestroyObject(obj, request_slot=0)
    End()


@RestartOnRest(1050383710)
def Event_1050383710(_, character: uint):
    """Event 1050383710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 4185)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(1050381700)
    IfFlagEnabled(OR_2, 4185)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableObject(1050381700)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(1050381700)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(1050381700)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_1, 4185)
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(1050383711)
def Event_1050383711(_, character: uint):
    """Event 1050383711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(OR_1, 4186)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_2, 4186)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    DisableObject(1050381700)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_1, 4186)
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(1050383712)
def Event_1050383712(_, character: uint):
    """Event 1050383712"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4180)
    DisableFlag(1050389253)
    DisableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 4187)
    IfFlagDisabled(AND_1, 1050389266)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    SkipLinesIfPlayerInOwnWorld(3)
    IfFlagEnabled(AND_3, 4187)
    IfFlagDisabled(AND_3, 4197)
    GotoIfConditionTrue(Label.L6, input_condition=AND_3)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 4187)
    IfFlagDisabled(AND_2, 1050389266)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableNetworkFlag(1050389265)
    DisableNetworkFlag(1038519255)
    DisableNetworkFlag(4197)
    GotoIfFlagEnabled(Label.L1, flag=4180)
    GotoIfFlagEnabled(Label.L2, flag=4181)
    GotoIfFlagEnabled(Label.L4, flag=4183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4187)
    Restart()


@RestartOnRest(1050383713)
def Event_1050383713():
    """Event 1050383713"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4185)
    IfFlagDisabled(MAIN, 1050389255)
    IfFlagEnabled(MAIN, 1050382716)
    WaitFrames(frames=2)
    PlayCutscene(60500000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(1050382717)
    ForceAnimation(1050380705, 90102, unknown2=1.0)
    WaitFramesAfterCutscene(frames=1)
    End()


@RestartOnRest(1050383714)
def Event_1050383714():
    """Event 1050383714"""
    EndIfPlayerNotInOwnWorld()
    SetCharacterTalkRange(character=1050380705, distance=17.0)
    EndIfFlagEnabled(1050389255)
    SetCharacterTalkRange(character=1050380705, distance=50.0)
    IfFlagDisabled(AND_1, 1050389255)
    IfFlagDisabled(AND_1, 1050382713)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1050382710)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1050382713)
    End()
