"""
Far West Limgrave (NE) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_39_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005704(0, attacked_entity=Characters.SorcererThops, flag=3801, flag_1=3800, flag_2=1039399201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.SorcererThops,
        flag=3801,
        flag_1=3802,
        flag_2=1039399201,
        flag_3=3801,
        first_flag=3800,
        last_flag=3803,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.SorcererThops, flag=3803, first_flag=3800, last_flag=3803)
    Event_1039393700(0, asset__character=Characters.SorcererThops)
    Event_1039393701()
    Event_1039393702(0, character=Characters.SorcererThops, asset=Assets.AEG003_061_9000)
    CommonFunc_90005300(0, flag=1039390200, character=Characters.Scarab, item_lot=40206, seconds=0.0, left=0)
    Event_1039392200()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SorcererThops)


@RestartOnRest(1039392200)
def Event_1039392200():
    """Event 1039392200"""
    if FlagEnabled(3803):
        return
    DisableCharacter(Characters.Scarab)
    DisableAnimations(Characters.Scarab)


@RestartOnRest(1039393700)
def Event_1039393700(_, asset__character: uint):
    """Event 1039393700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3800))
    AND_1.Add(FlagEnabled(1039399203))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1039399203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    OR_1.Add(FlagEnabled(3805))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3805))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3800)
    GotoIfFlagEnabled(Label.L2, flag=3801)
    GotoIfFlagEnabled(Label.L4, flag=3803)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 90100)
    Move(asset__character, destination=1039392700, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(asset__character)
    EnableAssetInvulnerability(Assets.AEG003_061_9000)
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
    OR_15.Add(FlagEnabled(3805))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1039393701)
def Event_1039393701():
    """Event 1039393701"""
    AND_1.Add(FlagEnabled(1039399213))
    AND_1.Add(FlagEnabled(1039399218))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(120500, 120749)) >= 3)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1039399218)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039393702)
def Event_1039393702(_, character: Character | int, asset: Asset | int):
    """Event 1039393702"""
    AND_1.Add(FlagEnabled(3801))
    AwaitConditionTrue(AND_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 9624))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(PlayerInOwnWorld())
    AwaitConditionTrue(AND_1)
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset, request_slot=0)
    EnableGravity(character)
    End()
