"""
linked:
0
72
138
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\m60.emevd
138: N:\\GR\\data\\Param\\event\\common_func.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_36_41_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036410000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005570(0, flag=60824, gesture_param_id=54, asset=Assets.AEG099_990_9000, left=2, left_1=1, right=0)
    Event_1036413700(0, character=Characters.AlbinauricArcher, character_1=Characters.BigWolf)
    Event_1036413701(0, character=Characters.AlbinauricArcher)
    Event_1036413702(0, character=Characters.AlbinauricArcher)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.AlbinauricArcher,
        flag=4101,
        flag_1=4100,
        flag_2=1036419201,
        right=3,
    )
    CommonFunc_90005703(0, 1036410700, 4101, 4102, 1036419201, 4101, 4100, 4104, -1)
    CommonFunc_90005702(0, character=Characters.AlbinauricArcher, flag=4103, first_flag=4100, last_flag=4104)
    CommonFunc_90005750(0, 1036411700, 4350, 104100, 400410, 400410, 1036419215, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.AlbinauricArcher)
    DisableBackread(Characters.BigWolf)


@RestartOnRest(1036413700)
def Event_1036413700(_, character: uint, character_1: uint):
    """Event 1036413700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4100):
        DisableFlag(1036419203)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 30020)
    GotoIfFlagEnabled(Label.L5, flag=4105)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(4105))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagEnabled(1051587800):
        DisableCharacter(character)
        DisableBackread(character)
        EnableFlag(1036419215)
        Goto(Label.L20)
    GotoIfFlagEnabled(Label.L1, flag=4100)
    GotoIfFlagEnabled(Label.L2, flag=4101)
    GotoIfFlagEnabled(Label.L3, flag=4102)
    GotoIfFlagEnabled(Label.L4, flag=4103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 30020)
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
    OR_4.Add(FlagEnabled(4105))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1036413701)
def Event_1036413701(_, character: uint):
    """Event 1036413701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4100):
        return
    if FlagDisabled(4105):
        return
    
    MAIN.Await(FlagEnabled(1036419209))
    
    DisableAnimations(character)
    Wait(30.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1036413702)
def Event_1036413702(_, character: uint):
    """Event 1036413702"""
    if FlagEnabled(4101):
        return
    if FlagEnabled(4103):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 9644))
    OR_1.Add(FlagEnabled(4101))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterHasSpecialEffect(character, 9644))
    AND_1.Add(FlagDisabled(4101))
    if AND_1:
        return
    ForceAnimation(character, 20022)
    End()
