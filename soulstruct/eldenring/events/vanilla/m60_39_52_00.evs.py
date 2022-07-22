"""
West Altus Plateau (SE) (SE)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_39_52_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1039522650()
    Event_1039522660()
    Event_1039522700()
    CommonFunc_90005790(
        0,
        right=0,
        flag=1039520180,
        summon_flag=1039522181,
        dismissal_flag=1039522182,
        character=Characters.EleonoraVioletBloodyFinger,
        sign_type=21,
        region=1039522180,
        region_1=1039522181,
        seconds=0.0,
        right_1=1039529206,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1039520180,
        flag_1=1039522181,
        flag_2=1039522182,
        character=Characters.EleonoraVioletBloodyFinger,
    )
    CommonFunc_90005792(
        0,
        flag=1039520180,
        flag_1=1039522181,
        flag_2=1039522182,
        character=Characters.EleonoraVioletBloodyFinger,
        item_lot=101620,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1039520180,
        flag_1=1039522181,
        flag_2=1039522182,
        character=Characters.EleonoraVioletBloodyFinger,
        other_entity=1039522180,
        region=1039522182,
        left=0,
    )
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61031)
    CommonFunc_90005300(0, flag=1039520500, character=Characters.Scarab, item_lot=40306, seconds=0.0, left=0)
    Event_1039523700(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1039523701(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1039523703(0, asset=Assets.AEG099_429_9000, asset_1=Assets.AEG099_429_9001, asset_2=Assets.AEG099_429_9002)
    Event_1039523702(0, flag=1039529206)
    Event_1039523704(0, character=Characters.YuraHunterofBloodyFingers)
    CommonFunc_90005750(0, 1039521703, 4350, 101630, 400163, 400163, 1039529205, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.YuraHunterofBloodyFingers)
    DisableBackread(Characters.EleonoraVioletBloodyFinger)
    CommonFunc_90005251(0, character=Characters.Scarab, radius=25.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.Scarab,
        animation_id=30001,
        animation_id_1=20004,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrab0,
        animation_id=30003,
        animation_id_1=20003,
        radius=6.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrab1,
        animation_id=30003,
        animation_id_1=20003,
        radius=6.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrab2,
        animation_id=30003,
        animation_id_1=20003,
        radius=6.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrab3,
        animation_id=30003,
        animation_id_1=20003,
        radius=6.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.RevenantFollower, radius=150.0, seconds=0.0, animation_id=0)
    Event_1039522220(0, character=Characters.Troll0)
    CommonFunc_90005423(0, character=Characters.Troll0)
    Event_1039522220(1, character=Characters.Troll1)
    CommonFunc_90005423(0, character=Characters.Troll1)
    CommonFunc_90005200(
        0,
        character=Characters.SanguineNoble,
        animation_id=30000,
        animation_id_1=20000,
        region=1039522400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1039522400()
    CommonFunc_90005300(0, 1039520400, 1039520400, 0, 0.0, 0)


@RestartOnRest(1039522220)
def Event_1039522220(_, character: uint):
    """Event 1039522220"""
    AddSpecialEffect(character, 5551)
    End()


@RestartOnRest(1039522400)
def Event_1039522400():
    """Event 1039522400"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(FlagEnabled(3630))
    AND_2.Add(FlagEnabled(3631))
    AND_2.Add(FlagDisabled(1039520180))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.SanguineNoble)
    DisableAnimations(Characters.SanguineNoble)
    End()


@RestartOnRest(1039522650)
def Event_1039522650():
    """Event 1039522650"""
    GotoIfFlagEnabled(Label.L0, flag=1039520655)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1039522650, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG003_316_9000)
    CreateVFX(1039522650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1039522650, erase_root_only=False)
    End()


@RestartOnRest(1039522660)
def Event_1039522660():
    """Event 1039522660"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1039520655):
        return
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1039522651))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9521, entity=Assets.AEG003_316_9000))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039520655)
    DisableAsset(Assets.AEG003_316_9000)
    RotateToFaceEntity(PLAYER, Assets.AEG003_316_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.0)
    PlaySoundEffect(1039522650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1039522650)
    End()


@RestartOnRest(1039522700)
def Event_1039522700():
    """Event 1039522700"""
    AND_15.Add(FlagEnabled(1039520655))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    if FlagEnabled(1039520502):
        Kill(Characters.Imp0)
        Kill(Characters.Imp1)
    if FlagDisabled(1039520502):
        EnableFlag(1039520502)
        Kill(Characters.Imp0, award_runes=True)
        Kill(Characters.Imp1, award_runes=True)
    if AND_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1039523200)
    GotoIfFlagEnabled(Label.L1, flag=1039522701)
    DisableSpawner(entity=1039523200)
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1039522260))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=1039523200)
    ClearTargetList(Characters.Imp0)
    MakeEnemyAppear(character=1039523200)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    ClearTargetList(Characters.Imp1)
    MakeEnemyAppear(character=1039523200)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterDead(Characters.Imp0))
    SkipLinesIfConditionFalse(3, AND_2)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    EnableSpawner(entity=1039523200)
    ClearTargetList(Characters.Imp0)
    MakeEnemyAppear(character=1039523200)
    AND_3.Add(CharacterDead(Characters.Imp1))
    SkipLinesIfConditionFalse(3, AND_3)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=5.0)
    EnableSpawner(entity=1039523200)
    ClearTargetList(Characters.Imp1)
    MakeEnemyAppear(character=1039523200)
    if FlagEnabled(1039520655):
        Wait(5.0)
    DisableSpawner(entity=1039523200)
    EnableFlag(1039522701)
    Restart()


@RestartOnRest(1039523700)
def Event_1039523700(_, character: uint):
    """Event 1039523700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3620):
        DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3630)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3630))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

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
    if FlagDisabled(1039529205):
        DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3630))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1039523701)
def Event_1039523701(_, character: uint):
    """Event 1039523701"""
    WaitFrames(frames=1)
    MoveAssetToCharacter(Assets.AEG099_090_9000, character=character)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3620):
        return
    if FlagEnabled(3631):
        return
    OR_1.Add(FlagEnabled(1039529205))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableFlag(1039529209)
    DisableAnimations(character)
    if FlagEnabled(1039529205):
        ForceAnimation(character, 90201)
        End()
        EnableFlag(1039529207)
    End()


@RestartOnRest(1039523702)
def Event_1039523702(_, flag: uint):
    """Event 1039523702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1039520180):
        return
    if FlagEnabled(1039529205):
        EnableFlag(flag)
        End()
    if FlagEnabled(1039529207):
        EnableFlag(flag)
        End()
    OR_1.Add(FlagEnabled(1039529209))
    OR_1.Add(FlagEnabled(3631))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    End()


@RestartOnRest(1039523703)
def Event_1039523703(_, asset: uint, asset_1: uint, asset_2: uint):
    """Event 1039523703"""
    GotoIfFlagEnabled(Label.L1, flag=1039529208)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableAsset(asset_2)
    WaitFrames(frames=1)
    if FlagDisabled(3630):
        return
    EnableNetworkFlag(1039529208)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAsset(asset)
    EnableAsset(asset_1)
    EnableAsset(asset_2)
    End()


@RestartOnRest(1039523704)
def Event_1039523704(_, character: uint):
    """Event 1039523704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043359259):
        return
    if FlagEnabled(1044389209):
        return
    if FlagEnabled(1035469209):
        return
    GotoIfFlagEnabled(Label.L1, flag=1039529209)
    
    MAIN.Await(FlagEnabled(1039529209))
    
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1039529205):
        return
    WaitFrames(frames=1)
    if FlagEnabled(3630):
        return
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()
