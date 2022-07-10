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
    Event_1039522650()
    Event_1039522660()
    Event_1039522700()
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1039520180, 1039522181, 1039522182, 1039520710, 21, 1039522180, 1039522181, 0.0, 1039529206, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1039520180, 1039522181, 1039522182, 1039520710), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(1039520180, 1039522181, 1039522182, 1039520710, 101620, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005793,
        args=(1039520180, 1039522181, 1039522182, 1039520710, 1039522180, 1039522182, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005631, args=(1039521400, 61031), arg_types="Ii")
    RunCommonEvent(0, 90005300, args=(1039520500, 1039520500, 40306, 0.0, 0), arg_types="IIifi")
    Event_1039523700(0, character=1039520701)
    Event_1039523701(0, character=1039520701)
    Event_1039523703(0, obj=1039521700, obj_1=1039521701, obj_2=1039521702)
    Event_1039523702(0, flag=1039529206)
    Event_1039523704(0, character=1039520701)
    RunCommonEvent(0, 90005750, args=(1039521703, 4350, 101630, 400163, 400163, 1039529205, 0), arg_types="IiiIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039520701)
    DisableBackread(1039520710)
    RunCommonEvent(0, 90005251, args=(1039520500, 25.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1039520500, 30001, 20004, 25.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039520300, 30003, 20003, 6.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039520301, 30003, 20003, 6.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039520302, 30003, 20003, 6.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1039520303, 30003, 20003, 6.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1039520350, 150.0, 0.0, 0), arg_types="Iffi")
    Event_1039522220(0, character=1039520360)
    RunCommonEvent(0, 90005423, args=(1039520360,))
    Event_1039522220(1, character=1039520361)
    RunCommonEvent(0, 90005423, args=(1039520361,))
    RunCommonEvent(0, 90005200, args=(1039520400, 30000, 20000, 1039522400, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1039522400()
    RunCommonEvent(0, 90005300, args=(1039520400, 1039520400, 0, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1039522220)
def Event_1039522220(_, character: uint):
    """Event 1039522220"""
    AddSpecialEffect(character, 5551)
    End()


@RestartOnRest(1039522400)
def Event_1039522400():
    """Event 1039522400"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(OR_1, 3630)
    IfFlagEnabled(AND_2, 3631)
    IfFlagDisabled(AND_2, 1039520180)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(1039520400)
    DisableAnimations(1039520400)
    End()


@RestartOnRest(1039522650)
def Event_1039522650():
    """Event 1039522650"""
    GotoIfFlagEnabled(Label.L0, flag=1039520655)
    DisableObject(1039521650)
    DeleteVFX(1039522650, erase_root_only=False)
    IfFlagEnabled(MAIN, 1039530505)
    EnableObject(1039521650)
    CreateVFX(1039522650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(1039521650)
    DeleteVFX(1039522650, erase_root_only=False)
    End()


@RestartOnRest(1039522660)
def Event_1039522660():
    """Event 1039522660"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1039520655)
    IfFlagEnabled(AND_1, 1039530505)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1039522651)
    IfActionButtonParamActivated(AND_1, action_button_id=9521, entity=1039521650)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039520655)
    DisableObject(1039521650)
    RotateToFaceEntity(PLAYER, 1039521650, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.0)
    PlaySoundEffect(1039522650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1039522650)
    End()


@RestartOnRest(1039522700)
def Event_1039522700():
    """Event 1039522700"""
    IfFlagEnabled(AND_15, 1039520655)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    SkipLinesIfFlagDisabled(2, 1039520502)
    Kill(1039520600)
    Kill(1039520601)
    SkipLinesIfFlagEnabled(3, 1039520502)
    EnableFlag(1039520502)
    Kill(1039520600, award_souls=True)
    Kill(1039520601, award_souls=True)
    EndIfConditionTrue(input_condition=AND_15)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1039523200)
    GotoIfFlagEnabled(Label.L1, flag=1039522701)
    DisableSpawner(entity=1039523200)
    IfFlagEnabled(AND_1, 1039530505)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1039522260)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableSpawner(entity=1039523200)
    ClearTargetList(1039520600)
    MakeEnemyAppear(character=1039523200)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    ClearTargetList(1039520601)
    MakeEnemyAppear(character=1039523200)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterDead(AND_2, 1039520600)
    SkipLinesIfConditionFalse(3, AND_2)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    EnableSpawner(entity=1039523200)
    ClearTargetList(1039520600)
    MakeEnemyAppear(character=1039523200)
    IfCharacterDead(AND_3, 1039520601)
    SkipLinesIfConditionFalse(3, AND_3)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    EnableSpawner(entity=1039523200)
    ClearTargetList(1039520601)
    MakeEnemyAppear(character=1039523200)
    SkipLinesIfFlagDisabled(1, 1039520655)
    Wait(5.0)
    DisableSpawner(entity=1039523200)
    EnableFlag(1039522701)
    Restart()


@RestartOnRest(1039523700)
def Event_1039523700(_, character: uint):
    """Event 1039523700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3620)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3630)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3630)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagEnabled(1, 1039529205)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3630)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1039523701)
def Event_1039523701(_, character: uint):
    """Event 1039523701"""
    WaitFrames(frames=1)
    MoveObjectToCharacter(1039521703, character=character)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3620)
    EndIfFlagEnabled(3631)
    IfFlagEnabled(OR_1, 1039529205)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(1039529209)
    DisableAnimations(character)
    SkipLinesIfFlagDisabled(3, 1039529205)
    ForceAnimation(character, 90201, unknown2=1.0)
    End()
    EnableFlag(1039529207)
    End()


@RestartOnRest(1039523702)
def Event_1039523702(_, flag: uint):
    """Event 1039523702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1039520180)
    SkipLinesIfFlagDisabled(2, 1039529205)
    EnableFlag(flag)
    End()
    SkipLinesIfFlagDisabled(2, 1039529207)
    EnableFlag(flag)
    End()
    IfFlagEnabled(OR_1, 1039529209)
    IfFlagEnabled(OR_1, 3631)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(flag)
    End()


@RestartOnRest(1039523703)
def Event_1039523703(_, obj: uint, obj_1: uint, obj_2: uint):
    """Event 1039523703"""
    GotoIfFlagEnabled(Label.L1, flag=1039529208)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableObject(obj_2)
    WaitFrames(frames=1)
    EndIfFlagDisabled(3630)
    EnableNetworkFlag(1039529208)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableObject(obj_2)
    End()


@RestartOnRest(1039523704)
def Event_1039523704(_, character: uint):
    """Event 1039523704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043359259)
    EndIfFlagEnabled(1044389209)
    EndIfFlagEnabled(1035469209)
    GotoIfFlagEnabled(Label.L1, flag=1039529209)
    IfFlagEnabled(MAIN, 1039529209)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(1039529205)
    WaitFrames(frames=1)
    EndIfFlagEnabled(3630)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()
