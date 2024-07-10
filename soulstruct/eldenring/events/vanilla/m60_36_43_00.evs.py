"""
Southeast Liurnia (NW) (NW)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_36_43_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036430000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1036430001, asset=Assets.AEG099_060_9001)
    Event_1036433700(0, character=Characters.Blackguard, asset=Assets.AEG099_316_1000)
    CommonFunc_90005704(0, attacked_entity=Characters.Blackguard, flag=4141, flag_1=4140, flag_2=1036439201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blackguard,
        flag=4141,
        flag_1=4142,
        flag_2=1036439201,
        flag_3=4141,
        first_flag=4140,
        last_flag=4144,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blackguard, flag=4143, first_flag=4140, last_flag=4144)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Blackguard)


@RestartOnRest(1036433700)
def Event_1036433700(_, character: uint, asset: Asset | int):
    """Event 1036433700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4140):
        DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4145)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(4145))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4140)
    GotoIfFlagEnabled(Label.L2, flag=4141)
    GotoIfFlagEnabled(Label.L3, flag=4142)
    GotoIfFlagEnabled(Label.L4, flag=4143)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAsset(asset)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableAsset(asset)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableAsset(asset)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4145))
    
    MAIN.Await(not OR_4)
    
    Restart()
