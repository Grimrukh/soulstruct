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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_45_38_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005704(0, attacked_entity=Characters.KennethHaight, flag=3581, flag_1=3580, flag_2=1045389201, right=3)
    CommonFunc_90005703(0, 1045380700, 3581, 3582, 1045389201, 3581, 3580, 3583, -1)
    CommonFunc_90005702(0, character=Characters.KennethHaight, flag=3583, first_flag=3580, last_flag=3583)
    Event_1045383700(0, 1045380700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.KennethHaight)


@RestartOnRest(1045382390)
def Event_1045382390():
    """Event 1045382390"""
    DisableAsset(1045381390)


@RestartOnRest(1045383700)
def Event_1045383700(_, asset__character: uint):
    """Event 1045383700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3580))
    AND_1.Add(FlagEnabled(1045389203))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1045389203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    OR_1.Add(FlagEnabled(3585))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3585))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3580)
    GotoIfFlagEnabled(Label.L2, flag=3581)
    GotoIfFlagEnabled(Label.L4, flag=3583)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 90100)
    SetCharacterTalkRange(character=asset__character, distance=100.0)
    if FlagEnabled(1045389205):
        ForceAnimation(asset__character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(asset__character)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAsset(asset__character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3585))
    
    MAIN.Await(not OR_15)
    
    Restart()
