"""
East Weeping Peninsula (NW) (SE)

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
from .enums.m60_45_34_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RunEvent(1045342580, slot=0, args=(0,))
    Event_1045342250(0, character=1045340204)
    Event_1045342250(1, character=1045340250)
    Event_1045342250(2, character=1045340251)
    CommonFunc_90005201(
        0,
        character=Characters.GodrickSoldier0,
        animation_id=30028,
        animation_id_1=-1,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.GodrickSoldier1,
        animation_id=30028,
        animation_id_1=-1,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.GodrickSoldier2,
        animation_id=30029,
        animation_id_1=-1,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005461(0, character=1045340207)
    CommonFunc_90005462(1, character=1045340207)
    CommonFunc_90005460(0, character=1045340207)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, dummy_id=800, right=1045348540)
    CommonFunc_90005683(0, flag=62151, asset=Assets.AEG099_055_1000, vfx_id=208, flag_1=78198, flag_2=78198)
    CommonFunc_90005704(0, attacked_entity=Characters.IrinaofMorne0, flag=3381, flag_1=3380, flag_2=1045349201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.IrinaofMorne0,
        flag=3381,
        flag_1=3382,
        flag_2=1045349201,
        flag_3=3381,
        first_flag=3380,
        last_flag=3384,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.IrinaofMorne0, flag=3383, first_flag=3380, last_flag=3384)
    Event_1045340700(0, character=Characters.IrinaofMorne0)
    Event_1045340701(0, character=Characters.IrinaofMorne1, asset=Assets.AEG099_400_9000)
    CommonFunc_90005704(0, attacked_entity=Characters.Edgar, flag=3401, flag_1=3400, flag_2=1045349251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Edgar,
        flag=3401,
        flag_1=3402,
        flag_2=1045349251,
        flag_3=3401,
        first_flag=3400,
        last_flag=3403,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Edgar, flag=3403, first_flag=3400, last_flag=3403)
    Event_1045340705(0, character=Characters.Edgar)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=110620,
        first_flag=400061,
        last_flag=400061,
        flag=1045349258,
        dummy_id=0,
    )
    Event_1045340707(0, attacked_entity=Characters.Edgar)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.IrinaofMorne0)
    DisableBackread(Characters.IrinaofMorne1)
    DisableBackread(Characters.Edgar)
    Event_1045340706()
    CommonFunc_AITrigger_RegionOrHurt(0, character=1045340405, region=1045342405, seconds=0.0, animation_id=0)


@RestartOnRest(1045342250)
def Event_1045342250(_, character: uint):
    """Event 1045342250"""
    Kill(character)
    End()


@RestartOnRest(1045342680)
def Event_1045342680():
    """Event 1045342680"""
    MAIN.Await(FlagEnabled(1045348540))
    
    CreateAssetVFX(Assets.AEG099_090_9001, vfx_id=100, dummy_id=800)


@RestartOnRest(1045340700)
def Event_1045340700(_, character: uint):
    """Event 1045340700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3380):
        DisableFlag(1045349202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3385)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3385))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=1045342700, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=1045342700, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 90100)
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3385))
    
    Restart()


@RestartOnRest(1045340701)
def Event_1045340701(_, character: uint, asset: uint):
    """Event 1045340701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagRangeAnyEnabled(Label.L6, flag_range=(3386, 3397))
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3386, 3397)))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 90105)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3386, 3397)))
    
    Restart()


@RestartOnRest(1045340705)
def Event_1045340705(_, character: uint):
    """Event 1045340705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagDisabled(3400):
        DisableFlag(1043319202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L8, flag=3408)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3408))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagEnabled(Label.L0, flag=3400)
    GotoIfFlagEnabled(Label.L1, flag=3401)
    GotoIfFlagEnabled(Label.L2, flag=3402)
    GotoIfFlagEnabled(Label.L3, flag=3403)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    if PlayerInOwnWorld():
        EnableFlag(1045349258)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3408))
    
    Restart()


@RestartOnRest(1045340706)
def Event_1045340706():
    """Event 1045340706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045349256):
        return
    AND_1.Add(FlagEnabled(1043300800))
    AND_1.Add(FlagEnabled(1043319206))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1045342719)
    EnableFlag(3418)


@RestartOnRest(1045340707)
def Event_1045340707(_, attacked_entity: uint):
    """Event 1045340707"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1045349256):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity))
    
    EnableFlag(1045349256)
