"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037440000, obj=1037441950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76206, 76204, 1037441980, 77200, 4, 78200, 78201, 78202, 78203, 78204, 78205, 78206, 78207, 78208, 78209),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1037440210, 1037440210, 40262, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005920, args=(1037440600, 1037441600, 1037443600), arg_types="III")
    Event_1037442610(0, obj=1037441610, entity=1037441611, flag=82021)
    Event_1037443700(0, character=1037440700, character_1=1037440710)
    Event_1037443701(0, flag=1037449206, flag_1=1037449200)
    RunCommonEvent(0, 90005704, args=(1037440700, 3441, 3440, 1037449201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1037440700, 3441, 3442, 1037449201, 3441, 3440, 3444, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1037440700, 3443, 3440, 3444), arg_types="IIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037440700)
    DisableBackread(1037440710)
    RunCommonEvent(0, 90005201, args=(1037440220, 30001, 20001, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1037440220, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1037440200, 1037442200, 1.0, 0.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037440201, 1037442200, 1.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037440202, 1037442200, 1.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037440203, 1037442200, 1.0, 1.5, -1), arg_types="IIffi")


@RestartOnRest(1037442610)
def Event_1037442610(_, obj: uint, entity: uint, flag: uint):
    """Event 1037442610"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1037443700)
def Event_1037443700(_, character: uint, character_1: uint):
    """Event 1037443700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3440)
    IfFlagEnabled(AND_1, 11109405)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableObject(1037441700)
    IfFlagEnabled(OR_1, 3446)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3446)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableObject(1037441700)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character, 90105, unknown2=1.0)
    ForceAnimation(character_1, 90100, unknown2=1.0)
    DisableAnimations(character_1)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableObject(1037441700)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character_1, 90100, unknown2=1.0)
    DisableAnimations(character_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableObject(1037441700)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character_1, 90100, unknown2=1.0)
    DisableAnimations(character_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3446)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1037443701)
def Event_1037443701(_, flag: uint, flag_1: uint):
    """Event 1037443701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3445)
    EnableFlag(flag)
    EnableNetworkFlag(1037442701)
    EnableNetworkFlag(3458)
    WaitFrames(frames=1)
    EnableNetworkFlag(flag_1)
    End()
