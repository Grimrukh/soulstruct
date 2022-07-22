"""
Northeast Altus Plateau (SW) (SW)

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
from .entities.m60_44_52_00_entities import *
from .entities.m60_45_52_00_entities import Characters as m60_45_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1044523701(0, character=Characters.Blackguard0)
    Event_1044523702(0, character=Characters.Blackguard1, asset=Assets.AEG099_058_9000, asset_1=Assets.AEG099_411_9000)
    Event_1044523703(0, asset=Assets.AEG099_620_9000, asset_1=Assets.AEG099_591_9000)
    Event_1044523704(0, entity=Characters.Blackguard1)
    Event_1044523705()
    Event_1044523706()
    Event_1044523707(0, asset=Assets.AEG099_315_9000, asset_1=Assets.AEG099_090_9000)
    CommonFunc_90005704(0, attacked_entity=Characters.Blackguard0, flag=4141, flag_1=4140, flag_2=1044529251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blackguard0,
        flag=4141,
        flag_1=4142,
        flag_2=1044529251,
        flag_3=4141,
        first_flag=4140,
        last_flag=4144,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blackguard0, flag=4143, first_flag=4140, last_flag=4144)
    CommonFunc_90005702(0, character=Characters.Blackguard1, flag=4143, first_flag=4140, last_flag=4144)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4350,
        item_lot_param_id=113010,
        first_flag=400308,
        last_flag=400309,
        flag=1044529272,
        model_point=6101,
    )
    Event_1044523710()
    Event_1044523711()
    Event_1044523712()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1044523700(0, entity=Assets.AEG099_315_9000)
    DisableBackread(Characters.Blackguard0)
    DisableBackread(Characters.Blackguard1)
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton0,
        animation_id=30014,
        animation_id_1=20014,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(0, 1044520301, 30016, 20016, 20.0, 0.0, 0, 0, 0, 0)


@ContinueOnRest(1044523700)
def Event_1044523700(_, entity: uint):
    """Event 1044523700"""
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=5.0))
    if not AND_1:
        return
    if FlagDisabled(4145):
        return
    EnableFlag(1044522701)
    End()


@RestartOnRest(1044523701)
def Event_1044523701(_, character: uint):
    """Event 1044523701"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4140):
        DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4146)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(4146))
    
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
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
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
    OR_4.Add(FlagEnabled(4146))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1044523702)
def Event_1044523702(_, character: uint, asset: uint, asset_1: uint):
    """Event 1044523702"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4140):
        DisableFlag(1036439203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4147)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    DisableAsset(asset_1)
    OR_3.Add(FlagEnabled(4147))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableAsset(asset)
    EnableAsset(asset_1)
    GotoIfFlagEnabled(Label.L1, flag=4140)
    GotoIfFlagEnabled(Label.L2, flag=4141)
    GotoIfFlagEnabled(Label.L3, flag=4142)
    GotoIfFlagEnabled(Label.L4, flag=4143)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90101)
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
    ForceAnimation(character, 90102)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4147))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1044523703)
def Event_1044523703(_, asset: uint, asset_1: uint):
    """Event 1044523703"""
    WaitFrames(frames=1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    if FlagDisabled(35009315):
        return
    AND_1.Add(FlagEnabled(4146))
    AND_1.Add(FlagEnabled(4143))
    OR_1.Add(FlagEnabled(4145))
    OR_1.Add(AND_1)
    if not OR_1:
        return
    EnableAsset(asset)
    EnableAsset(asset_1)
    End()


@RestartOnRest(1044523704)
def Event_1044523704(_, entity: uint):
    """Event 1044523704"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4143):
        return
    if FlagDisabled(4147):
        return
    
    MAIN.Await(FlagEnabled(1044529271))
    
    DisableNetworkConnectedFlagRange(flag_range=(4140, 4144))
    EnableNetworkFlag(4143)
    SaveRequest()
    WaitFramesAfterCutscene(frames=2)
    ForceAnimation(entity, 90201)
    End()


@RestartOnRest(1044523705)
def Event_1044523705():
    """Event 1044523705"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4145):
        return
    if FlagEnabled(1044529255):
        return
    EnableFlag(1044529255)
    End()


@RestartOnRest(1044523706)
def Event_1044523706():
    """Event 1044523706"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4147):
        return
    if FlagEnabled(1044529272):
        return
    GotoIfFlagEnabled(Label.L1, flag=4143)
    
    MAIN.Await(FlagEnabled(4143))
    
    Wait(1.5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(1044529272)
    End()


@RestartOnRest(1044523707)
def Event_1044523707(_, asset: uint, asset_1: uint):
    """Event 1044523707"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L5, flag=4146)
    GotoIfFlagEnabled(Label.L5, flag=4147)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DeleteAssetVFX(asset_1)
    OR_3.Add(FlagEnabled(4146))
    OR_3.Add(FlagEnabled(4147))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableAsset(asset)
    EnableAsset(asset_1)
    DeleteAssetVFX(asset_1)
    GotoIfFlagEnabled(Label.L20, flag=4143)
    GotoIfFlagEnabled(Label.L20, flag=4147)
    CreateAssetVFX(asset_1, vfx_id=90, model_point=800291)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4146))
    OR_4.Add(FlagEnabled(4147))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1044523710)
def Event_1044523710():
    """Event 1044523710"""
    if FlagDisabled(4240):
        return
    AwaitFlagEnabled(flag=1045522181)
    Move(
        m60_45_Characters.DungEater,
        destination=1044522700,
        destination_type=CoordEntityType.Region,
        set_draw_parent=0,
    )
    ForceAnimation(m60_45_Characters.DungEater, 63010)
    End()


@RestartOnRest(1044523711)
def Event_1044523711():
    """Event 1044523711"""
    DisableAsset(1045521705)
    DisableAsset(1045521706)
    if FlagDisabled(4240):
        return
    if FlagDisabled(4247):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(4146, 4147))
    EnableAsset(1045521705)
    EnableAsset(1045521706)
    EnableAssetInvulnerability(1045521705)
    EnableAssetInvulnerability(1045521706)
    EndOfAnimation(asset=1045521705, animation_id=201091)
    End()


@RestartOnRest(1044523712)
def Event_1044523712():
    """Event 1044523712"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    DisableNetworkFlag(35009315)
    if FlagDisabled(4240):
        return
    GotoIfFlagDisabled(Label.L19, flag=4247)
    GotoIfFlagDisabled(Label.L20, flag=4140)
    GotoIfFlagEnabled(Label.L20, flag=4145)
    if FlagEnabled(4146):
        return
    AND_1.Add(FlagEnabled(4147))
    AND_1.Add(FlagDisabled(4140))
    AwaitConditionTrue(AND_1)
    Goto(Label.L20)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_15.Add(FlagEnabled(4240))
    AND_15.Add(FlagEnabled(4247))
    AwaitConditionTrue(AND_15)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    EnableNetworkFlag(35009315)
    End()
