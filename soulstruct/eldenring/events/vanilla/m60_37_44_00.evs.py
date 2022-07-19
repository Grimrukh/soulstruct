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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_44_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037440000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76204,
        asset=Assets.AEG099_090_9001,
        source_flag=77200,
        value=4,
        flag_2=78200,
        flag_3=78201,
        flag_4=78202,
        flag_5=78203,
        flag_6=78204,
        flag_7=78205,
        flag_8=78206,
        flag_9=78207,
        flag_10=78208,
        flag_11=78209,
    )
    CommonFunc_90005300(0, flag=1037440210, character=Characters.Scarab, item_lot_param_id=40262, seconds=0.0, left=0)
    CommonFunc_90005920(0, flag=1037440600, asset=1037441600, obj_act_id=1037443600)
    Event_1037442610(0, asset=1037441610, entity=1037441611, flag=82021)
    Event_1037443700(0, character=Characters.KnightDiallos, character_1=Characters.Human)
    Event_1037443701(0, flag=1037449206, flag_1=1037449200)
    CommonFunc_90005704(0, attacked_entity=Characters.KnightDiallos, flag=3441, flag_1=3440, flag_2=1037449201, right=3)
    CommonFunc_90005703(0, 1037440700, 3441, 3442, 1037449201, 3441, 3440, 3444, -1)
    CommonFunc_90005702(0, 1037440700, 3443, 3440, 3444)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.KnightDiallos)
    DisableBackread(Characters.Human)
    CommonFunc_90005201(
        0,
        character=1037440220,
        animation_id=30001,
        animation_id_1=20001,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1037440220, 15.0, 0.0, -1)
    CommonFunc_90005261(0, 1037440200, 1037442200, 1.0, 0.5, -1)
    CommonFunc_90005261(0, 1037440201, 1037442200, 1.0, 1.0, -1)
    CommonFunc_90005261(0, 1037440202, 1037442200, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 1037440203, 1037442200, 1.0, 1.5, -1)


@RestartOnRest(1037442610)
def Event_1037442610(_, asset: uint, entity: uint, flag: uint):
    """Event 1037442610"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1037443700)
def Event_1037443700(_, character: uint, character_1: uint):
    """Event 1037443700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3440))
    AND_1.Add(FlagEnabled(11109405))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(Assets.AEG099_401_9000)
    OR_1.Add(FlagEnabled(3446))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3446))
    
    MAIN.Await(OR_2)
    
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
    EnableAsset(Assets.AEG099_401_9000)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character, 90105)
    ForceAnimation(character_1, 90100)
    DisableAnimations(character_1)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableAsset(Assets.AEG099_401_9000)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character_1, 90100)
    DisableAnimations(character_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableAsset(Assets.AEG099_401_9000)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ForceAnimation(character_1, 90100)
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
    OR_15.Add(FlagEnabled(3446))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1037443701)
def Event_1037443701(_, flag: uint, flag_1: uint):
    """Event 1037443701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3445):
        return
    EnableFlag(flag)
    EnableNetworkFlag(1037442701)
    EnableNetworkFlag(3458)
    WaitFrames(frames=1)
    EnableNetworkFlag(flag_1)
    End()
