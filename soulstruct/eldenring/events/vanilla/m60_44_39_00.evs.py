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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_44_39_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044390000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005726(
        0,
        flag=4720,
        flag_1=4721,
        flag_2=4723,
        flag_3=1044399255,
        character=Characters.Merchant,
        asset=1044396700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4721,
        flag_1=4722,
        flag_2=1044399256,
        flag_3=4721,
        first_flag=4720,
        last_flag=4724,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4721, flag_1=4720, flag_2=1044399256, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4723, first_flag=4720, last_flag=4724)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DHunteroftheDead,
        flag=4041,
        flag_1=4040,
        flag_2=1044399201,
        right=3,
    )
    CommonFunc_90005703(0, 1044390700, 4041, 4042, 1044399201, 4041, 4040, 4043, -1)
    CommonFunc_90005702(0, character=Characters.DHunteroftheDead, flag=4043, first_flag=4040, last_flag=4043)
    Event_1044390715(
        0,
        character=Characters.DHunteroftheDead,
        character_1=Characters.Human,
        asset=Assets.AEG099_412_9000,
    )
    CommonFunc_90005730(
        0,
        flag=1044399210,
        seconds=20.0,
        flag_1=1044399214,
        flag_2=4045,
        flag_3=1044399213,
        flag_4=1044399212,
    )
    CommonFunc_90005731(0, 1044399214, 1044390700, 10.0, 12.0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DHunteroftheDead)
    DisableBackread(Characters.Human)
    DisableBackread(Characters.Merchant)
    DisableBackread(1044390711)
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton0,
        region=1044392200,
        radius=1.0,
        seconds=1.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton1,
        region=1044392200,
        radius=1.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton2,
        region=1044392202,
        radius=1.0,
        seconds=1.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton3,
        region=1044392202,
        radius=1.0,
        seconds=1.5,
        animation_id=1700,
    )
    CommonFunc_90005261(0, 1044390204, 1044392202, 1.0, 0.0, 1700)


@NeverRestart(1044393710)
def Event_1044393710(_, asset__character: uint):
    """Event 1044393710"""
    WaitFrames(frames=1)
    DisableFlag(1044399250)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(4000))
    AND_1.Add(FlagEnabled(1044392710))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1044392710)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=4000)
    GotoIfFlagEnabled(Label.L2, flag=4001)
    GotoIfFlagEnabled(Label.L4, flag=4003)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 30003)
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
    
    MAIN.Await(FlagEnabled(1044399250))
    
    Restart()


@RestartOnRest(1044390715)
def Event_1044390715(_, character: uint, character_1: uint, asset: uint):
    """Event 1044390715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 90004)
    EnableAsset(asset)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(4040):
        DisableFlag(1044399202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=4045)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4045))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=4040)
    GotoIfFlagEnabled(Label.L1, flag=4041)
    GotoIfFlagEnabled(Label.L3, flag=4043)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4045))
    
    Restart()
