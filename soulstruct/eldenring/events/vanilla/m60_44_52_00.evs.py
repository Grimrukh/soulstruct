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
    Event_1044523701(0, character=1044520700)
    Event_1044523702(0, character=1044520701, obj=1044521702, obj_1=1044521703)
    Event_1044523703(0, obj=1044521705, obj_1=1044521706)
    Event_1044523704(0, entity=1044520701)
    Event_1044523705()
    Event_1044523706()
    Event_1044523707(0, obj=1044521700, obj_1=1044521701)
    RunCommonEvent(0, 90005704, args=(1044520700, 4141, 4140, 1044529251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1044520700, 4141, 4142, 1044529251, 4141, 4140, 4144, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1044520700, 4143, 4140, 4144), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(1044520701, 4143, 4140, 4144), arg_types="IIII")
    RunCommonEvent(0, 90005750, args=(1044521704, 4350, 113010, 400308, 400309, 1044529272, 6101), arg_types="IiiIIIi")
    Event_1044523710()
    Event_1044523711()
    Event_1044523712()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1044523700(0, entity=1044521700)
    DisableBackread(1044520700)
    DisableBackread(1044520701)
    RunCommonEvent(0, 90005201, args=(1044520300, 30014, 20014, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1044520301, 30016, 20016, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")


@NeverRestart(1044523700)
def Event_1044523700(_, entity: uint):
    """Event 1044523700"""
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=PLAYER, radius=5.0)
    EndIfConditionFalse(input_condition=AND_1)
    EndIfFlagDisabled(4145)
    EnableFlag(1044522701)
    End()


@RestartOnRest(1044523701)
def Event_1044523701(_, character: uint):
    """Event 1044523701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4140)
    DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4146)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 4146)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4140)
    GotoIfFlagEnabled(Label.L2, flag=4141)
    GotoIfFlagEnabled(Label.L3, flag=4142)
    GotoIfFlagEnabled(Label.L4, flag=4143)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
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
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4146)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1044523702)
def Event_1044523702(_, character: uint, obj: uint, obj_1: uint):
    """Event 1044523702"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4140)
    DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4147)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    DisableObject(obj_1)
    IfFlagEnabled(OR_3, 4147)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(obj)
    EnableObject(obj_1)
    GotoIfFlagEnabled(Label.L1, flag=4140)
    GotoIfFlagEnabled(Label.L2, flag=4141)
    GotoIfFlagEnabled(Label.L3, flag=4142)
    GotoIfFlagEnabled(Label.L4, flag=4143)

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
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90102, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4147)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1044523703)
def Event_1044523703(_, obj: uint, obj_1: uint):
    """Event 1044523703"""
    WaitFrames(frames=1)
    DisableObject(obj)
    DisableObject(obj_1)
    EndIfFlagDisabled(35009315)
    IfFlagEnabled(AND_1, 4146)
    IfFlagEnabled(AND_1, 4143)
    IfFlagEnabled(OR_1, 4145)
    IfConditionTrue(OR_1, input_condition=AND_1)
    EndIfConditionFalse(input_condition=OR_1)
    EnableObject(obj)
    EnableObject(obj_1)
    End()


@RestartOnRest(1044523704)
def Event_1044523704(_, entity: uint):
    """Event 1044523704"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4143)
    EndIfFlagDisabled(4147)
    IfFlagEnabled(MAIN, 1044529271)
    DisableNetworkConnectedFlagRange(flag_range=(4140, 4144))
    EnableNetworkFlag(4143)
    SaveRequest()
    WaitFramesAfterCutscene(frames=2)
    ForceAnimation(entity, 90201, unknown2=1.0)
    End()


@RestartOnRest(1044523705)
def Event_1044523705():
    """Event 1044523705"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4145)
    EndIfFlagEnabled(1044529255)
    EnableFlag(1044529255)
    End()


@RestartOnRest(1044523706)
def Event_1044523706():
    """Event 1044523706"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4147)
    EndIfFlagEnabled(1044529272)
    GotoIfFlagEnabled(Label.L1, flag=4143)
    IfFlagEnabled(MAIN, 4143)
    Wait(1.5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(1044529272)
    End()


@RestartOnRest(1044523707)
def Event_1044523707(_, obj: uint, obj_1: uint):
    """Event 1044523707"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L5, flag=4146)
    GotoIfFlagEnabled(Label.L5, flag=4147)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteObjectVFX(obj_1)
    IfFlagEnabled(OR_3, 4146)
    IfFlagEnabled(OR_3, 4147)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(obj)
    EnableObject(obj_1)
    DeleteObjectVFX(obj_1)
    GotoIfFlagEnabled(Label.L20, flag=4143)
    GotoIfFlagEnabled(Label.L20, flag=4147)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=800291)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4146)
    IfFlagEnabled(OR_4, 4147)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1044523710)
def Event_1044523710():
    """Event 1044523710"""
    EndIfFlagDisabled(4240)
    AwaitFlagEnabled(flag=1045522181)
    Move(1045520705, destination=1044522700, destination_type=CoordEntityType.Region, set_draw_parent=0)
    ForceAnimation(1045520705, 63010, unknown2=1.0)
    End()


@RestartOnRest(1044523711)
def Event_1044523711():
    """Event 1044523711"""
    DisableObject(1045521705)
    DisableObject(1045521706)
    EndIfFlagDisabled(4240)
    EndIfFlagDisabled(4247)
    EndIfFlagRangeAnyEnabled(flag_range=(4146, 4147))
    EnableObject(1045521705)
    EnableObject(1045521706)
    EnableObjectInvulnerability(1045521705)
    EnableObjectInvulnerability(1045521706)
    EndOfAnimation(obj=1045521705, animation_id=201091)
    End()


@RestartOnRest(1044523712)
def Event_1044523712():
    """Event 1044523712"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    DisableNetworkFlag(35009315)
    EndIfFlagDisabled(4240)
    GotoIfFlagDisabled(Label.L19, flag=4247)
    GotoIfFlagDisabled(Label.L20, flag=4140)
    GotoIfFlagEnabled(Label.L20, flag=4145)
    EndIfFlagEnabled(4146)
    IfFlagEnabled(AND_1, 4147)
    IfFlagDisabled(AND_1, 4140)
    AwaitConditionTrue(AND_1)
    Goto(Label.L20)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_15, 4240)
    IfFlagEnabled(AND_15, 4247)
    AwaitConditionTrue(AND_15)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    EnableNetworkFlag(35009315)
    End()
