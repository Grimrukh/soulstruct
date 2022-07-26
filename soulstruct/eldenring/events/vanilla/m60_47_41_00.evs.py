"""
Northwest Caelid (SE) (NE)

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
from .entities.m60_47_41_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1047412300()
    Event_1047412301()
    Event_1047412302()
    Event_1047412306()
    Event_1047412305()
    Event_1047412400()
    CommonFunc_90005793(
        0,
        flag=1047419201,
        flag_1=1047412220,
        flag_2=1047410230,
        character=Characters.KnightoftheGreatJar0,
        other_entity=1047412200,
        region=0,
        left=0,
    )
    CommonFunc_90005793(
        0,
        flag=1047419201,
        flag_1=1047412221,
        flag_2=1047410231,
        character=Characters.KnightoftheGreatJar1,
        other_entity=1047412201,
        region=0,
        left=0,
    )
    CommonFunc_90005793(
        0,
        flag=1047419201,
        flag_1=1047412222,
        flag_2=1047410232,
        character=Characters.KnightoftheGreatJar2,
        other_entity=1047412202,
        region=0,
        left=0,
    )


@ContinueOnRest(100)
def Event_100():
    """Event 100"""
    Event_1047412304(0, character=Characters.LargeLivingPot)
    Event_1047410700()
    Event_1047410701()
    Event_1047410702()


@ContinueOnRest(150)
def Event_150():
    """Event 150"""
    Event_1047412303(0, character=Characters.LargeLivingPot)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005485(0, character=Characters.GuardianGolem)


@RestartOnRest(1047412300)
def Event_1047412300():
    """Event 1047412300"""
    if PlayerInOwnWorld():
        GotoIfFlagEnabled(Label.L0, flag=1047412350)
    DisableCharacter(Characters.KnightoftheGreatJar0)
    DisableCharacter(Characters.KnightoftheGreatJar1)
    DisableCharacter(Characters.KnightoftheGreatJar2)
    if FlagEnabled(1047419201):
        return
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(FlagEnabled(1047419200))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1047412310))
    
    MAIN.Await(AND_1)
    
    AND_5.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(4, AND_5)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23731,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23741,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23751,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(4, AND_6)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23732,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23742,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23752,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(4, AND_7)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23733,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23743,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23753,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(4, AND_8)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23734,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23744,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23754,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_9.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(4, AND_9)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23735,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23745,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23755,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_10.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(4, AND_10)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23736,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23746,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23756,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    AND_11.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(4, AND_11)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23737,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23747,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23757,
        target_character=Characters.KnightoftheGreatJar2,
    )
    Goto(Label.L0)
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23738,
        target_character=Characters.KnightoftheGreatJar0,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23748,
        target_character=Characters.KnightoftheGreatJar1,
    )
    CopyPlayerCharacterDataFromOnlinePlayers(
        pool_type=1,
        failcase_player_param_id=23758,
        target_character=Characters.KnightoftheGreatJar2,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(1047412350)
    AND_2.Add(CharacterDead(Characters.KnightoftheGreatJar0))
    SkipLinesIfConditionTrue(2, AND_2)
    PlaceSummonSign(
        sign_type=SummonSignType.RedSign,
        character=Characters.KnightoftheGreatJar0,
        region=1047412200,
        summon_flag=1047412220,
        dismissal_flag=1047410230,
        unknown=0,
    )
    CreateAssetVFX(Assets.AEG099_090_9000, vfx_id=100, model_point=30090)
    AND_3.Add(CharacterDead(Characters.KnightoftheGreatJar1))
    SkipLinesIfConditionTrue(2, AND_3)
    PlaceSummonSign(
        sign_type=SummonSignType.RedSign,
        character=Characters.KnightoftheGreatJar1,
        region=1047412201,
        summon_flag=1047412221,
        dismissal_flag=1047410231,
        unknown=0,
    )
    CreateAssetVFX(Assets.AEG099_090_9001, vfx_id=100, model_point=30090)
    AND_4.Add(CharacterDead(Characters.KnightoftheGreatJar2))
    SkipLinesIfConditionTrue(2, AND_4)
    PlaceSummonSign(
        sign_type=SummonSignType.RedSign,
        character=Characters.KnightoftheGreatJar2,
        region=1047412202,
        summon_flag=1047412222,
        dismissal_flag=1047410232,
        unknown=0,
    )
    CreateAssetVFX(Assets.AEG099_090_9002, vfx_id=100, model_point=30090)
    
    MAIN.Await(MultiplayerPending())
    
    EraseNPCSummonSign(character=Characters.KnightoftheGreatJar0)
    EraseNPCSummonSign(character=Characters.KnightoftheGreatJar1)
    EraseNPCSummonSign(character=Characters.KnightoftheGreatJar2)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    DeleteAssetVFX(Assets.AEG099_090_9001)
    DeleteAssetVFX(Assets.AEG099_090_9002)
    Wait(1.0)
    Restart()


@RestartOnRest(1047412301)
def Event_1047412301():
    """Event 1047412301"""
    if FlagEnabled(1047419201):
        return
    AND_1.Add(FlagEnabled(1047419200))
    AND_1.Add(CharacterDead(Characters.KnightoftheGreatJar0))
    AND_1.Add(CharacterDead(Characters.KnightoftheGreatJar1))
    AND_1.Add(CharacterDead(Characters.KnightoftheGreatJar2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1047419201)


@RestartOnRest(1047412302)
def Event_1047412302():
    """Event 1047412302"""
    if FlagEnabled(1047419201):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1047412300))
    
    RequestPlayerCharacterDataFromOnlinePlayers(pool_type=1, data_count=3)


@RestartOnRest(1047412303)
def Event_1047412303(_, character: uint):
    """Event 1047412303"""
    DisableNetworkSync()
    SetBackreadStateAlternate(character, True)
    SetCharacterEnableDistance(character=character, distance=430.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)


@RestartOnRest(1047412304)
def Event_1047412304(_, character: uint):
    """Event 1047412304"""
    DisableNetworkSync()
    DisableGravity(character)
    
    MAIN.Await(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=200.0))
    
    EnableGravity(character)
    
    MAIN.Await(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=220.0))
    
    Restart()


@RestartOnRest(1047412305)
def Event_1047412305():
    """Event 1047412305"""
    GotoIfFlagEnabled(Label.L2, flag=1047419201)
    AND_15.Add(CharacterInsideRegion(character=PLAYER, region=1047412400))
    AND_15.Add(FlagEnabled(1047419200))
    
    MAIN.Await(AND_15)
    
    AND_5.Add(InvasionPending())
    OR_1.Add(Invasion())
    AND_5.Add(not OR_1)
    AND_1.Add(AND_5)
    AND_2.Add(FlagEnabled(1047412220))
    AND_2.Add(CharacterAlive(Characters.KnightoftheGreatJar0))
    AND_2.Add(Invasion())
    AND_3.Add(FlagEnabled(1047412221))
    AND_3.Add(CharacterAlive(Characters.KnightoftheGreatJar1))
    AND_3.Add(Invasion())
    AND_4.Add(FlagEnabled(1047412222))
    AND_4.Add(CharacterAlive(Characters.KnightoftheGreatJar2))
    AND_4.Add(Invasion())
    OR_15.Add(AND_1)
    OR_15.Add(AND_2)
    OR_15.Add(AND_3)
    OR_15.Add(AND_4)
    GotoIfConditionTrue(Label.L0, input_condition=OR_15)
    GotoIfConditionFalse(Label.L1, input_condition=OR_15)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(Assets.AEG099_028_1001)
    EnableAsset(Assets.AEG099_029_1001)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(Assets.AEG099_028_1001)
    DisableAsset(Assets.AEG099_029_1001)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAsset(Assets.AEG099_028_1001)
    DisableAsset(Assets.AEG099_029_1001)
    End()


@RestartOnRest(1047412306)
def Event_1047412306():
    """Event 1047412306"""
    if FlagEnabled(1047419200):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(1047419200))
    
    Wait(0.30000001192092896)
    DisplayDialog(text=30110, anchor_entity=Assets.AEG099_090_9000)


@RestartOnRest(1047412400)
def Event_1047412400():
    """Event 1047412400"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=20000, region=1047412400))
    
    AddSpecialEffect(20000, 514)
    Wait(1.0)
    
    MAIN.Await(CharacterOutsideRegion(character=20000, region=1047412401))
    
    RemoveSpecialEffect(20000, 514)
    Restart()


@RestartOnRest(1047410700)
def Event_1047410700():
    """Event 1047410700"""
    ForceAnimation(Characters.LargeLivingPot, 30003)
    DisableHealthBar(Characters.LargeLivingPot)
    EnableImmortality(Characters.LargeLivingPot)


@RestartOnRest(1047410701)
def Event_1047410701():
    """Event 1047410701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400470):
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(400470))
    
    SendPlayerCharacterDataToOnlinePlayers(pool_type=1)


@RestartOnRest(1047410702)
def Event_1047410702():
    """Event 1047410702"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=Characters.LargeLivingPot, distance=50.0)
    End()
