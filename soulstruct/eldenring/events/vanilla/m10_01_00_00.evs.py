"""
Chapel of Anticipation

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
from .entities.m10_01_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_10012682()
    Event_10012800()
    Event_10012810()
    Event_10012811()
    Event_10012849()
    Event_10012500()
    Event_10010790()
    Event_10010791()
    Event_10010792()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FingerMaiden)
    Event_10010020()
    Event_10010030()
    Event_10010031()
    Event_10012502()
    Event_10012560()
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(100):
        return
    if FlagEnabled(102):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetCurrentTime(
        time=(23, 45, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(10010020)
def Event_10010020():
    """Event 10010020"""
    if ThisEventSlotFlagEnabled():
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetAreaWelcomeMessageState(state=False)
    ForceAnimation(PLAYER, 0)
    SetWindVFX(wind_vfx_id=-1)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=0, face_param_id=-1)
    SetCharacterFaceParamOverride(character=PLAYER, override_slot=1, face_param_id=-1)
    PlayCutsceneToPlayerWithWeatherAndTime(
        cutscene_id=10000040,
        cutscene_flags=0,
        player_id=10000,
        weather_duration=0.0,
        change_time=True,
        time=(23, 45, 0),
    )
    WaitFramesAfterCutscene(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetRespawnPoint(respawn_point=10012020)
    SaveRequest()
    DisableThisSlotFlag()
    EnableFlag(100)


@NeverRestart(10010030)
def Event_10010030():
    """Event 10010030"""
    AND_15.Add(ThisEventSlotFlagEnabled())
    AND_15.Add(FlagEnabled(101))
    if AND_15:
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(10010801))
    AND_2.Add(HealthValue(Characters.GraftedScion) > 0)
    AND_2.Add(HealthValue(PLAYER) == 1)
    AND_3.Add(CharacterDead(PLAYER))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    DisableLoadingScreenText()
    EndIfFinishedConditionTrue(input_condition=AND_3)
    if ThisEventSlotFlagDisabled():
        Wait(1.0)
    AddSpecialEffect(PLAYER, 4790)
    EnableFlag(9021)
    SetBossMusic(bgm_boss_conv_param_id=920900, state=BossMusicState.Stop2)
    PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
        cutscene_id=10010000,
        cutscene_flags=0,
        move_to_region=18002020,
        map_id=18000000,
        player_id=10000,
        unk_20_24=10010,
        unk_24_25=False,
        change_weather=True,
        change_time=True,
        time=(10, 30, 0),
    )
    WaitFramesAfterCutscene(frames=1)


@NeverRestart(10010031)
def Event_10010031():
    """Event 10010031"""
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    if FlagEnabled(101):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(10012805))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(PLAYER)
    OR_2.Add(CharacterOutsideRegion(character=PLAYER, region=10012031))
    OR_2.Add(CharacterDead(Characters.GraftedScion))
    
    MAIN.Await(OR_2)
    
    DisableImmortality(PLAYER)


@RestartOnRest(10012500)
def Event_10012500():
    """Event 10012500"""
    GotoIfFlagDisabled(Label.L0, flag=10010500)
    DisableAsset(Assets.AEG210_451_0500)
    DisableAsset(10011501)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012500))
    
    MAIN.Await(AND_1)
    
    DestroyAsset(Assets.AEG210_451_0500)
    EnableFlag(10010500)


@RestartOnRest(10012501)
def Event_10012501():
    """Event 10012501"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(100):
        return
    if FlagEnabled(102):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetWindVFX(wind_vfx_id=808004)
    AddSpecialEffect(PLAYER, 4200)


@RestartOnRest(10012502)
def Event_10012502():
    """Event 10012502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(10010502):
        return
    if OutsideMap(game_map=CHAPEL_OF_ANTICIPATION):
        return
    SetAreaWelcomeMessageState(state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=10012502))
    
    MAIN.Await(AND_1)
    
    SetAreaWelcomeMessageState(state=True)
    DisplayAreaWelcomeMessage(text=10010)
    EnableFlag(10010502)


@RestartOnRest(10012504)
def Event_10012504():
    """Event 10012504"""
    if FlagEnabled(10018540):
        return
    if FlagEnabled(60210):
        return
    DisableAssetActivation(Assets.AEG219_002_0500, obj_act_id=-1)
    AND_1.Add(FlagEnabled(60210))
    
    MAIN.Await(AND_1)
    
    EnableAssetActivation(Assets.AEG219_002_0500, obj_act_id=-1)


@RestartOnRest(10012560)
def Event_10012560():
    """Event 10012560"""
    GotoIfFlagEnabled(Label.L0, flag=10018560)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(102))
    
    MAIN.Await(AND_1)
    
    EnableFlag(10018560)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=0)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=1)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=2)
    DisableAssetActivation(Assets.AEG219_000_0500, obj_act_id=2219000, relative_index=3)


@RestartOnRest(10012680)
def Event_10012680():
    """Event 10012680"""
    DisableNetworkSync()
    if FlagEnabled(18000020):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(10010020))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012680))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=10012680))
    
    MAIN.Await(AND_2)
    
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=False, unk_5_6=True)


@RestartOnRest(10012682)
def Event_10012682():
    """Event 10012682"""
    DisableNetworkSync()
    if FlagEnabled(18000020):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012682))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710000)
    DisplayTutorialMessage(tutorial_param_id=1000, unk_4_5=True, unk_5_6=True)


@RestartOnRest(10012800)
def Event_10012800():
    """Event 10012800"""
    if FlagEnabled(10010800):
        return
    
    MAIN.Await(HealthValue(Characters.GraftedScion) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(10018000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GraftedScion))
    
    KillBossAndDisplayBanner(character=Characters.GraftedScion, banner_type=BannerType.EnemyFelled)
    EnableFlag(10010800)
    EnableFlag(9103)
    if PlayerInOwnWorld():
        EnableFlag(61103)


@RestartOnRest(10012810)
def Event_10012810():
    """Event 10012810"""
    GotoIfFlagDisabled(Label.L0, flag=10010800)
    DisableCharacter(Characters.GraftedScion)
    DisableAnimations(Characters.GraftedScion)
    Kill(Characters.GraftedScion)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GraftedScion)
    GotoIfFlagEnabled(Label.L1, flag=10010801)
    ForceAnimation(Characters.GraftedScion, 30003)
    DisableHealthBar(Characters.GraftedScion)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=10012801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GraftedScion, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(10010801)
    SetNetworkUpdateRate(Characters.GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.GraftedScion, 20003)
    Wait(4.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAnimations(Characters.GraftedScion)
    Move(Characters.GraftedScion, destination=10012810, destination_type=CoordEntityType.Region, short_move=True)
    AND_2.Add(FlagEnabled(10012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=10012800))
    
    MAIN.Await(AND_2)
    
    EnableAnimations(Characters.GraftedScion)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.GraftedScion, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(Characters.GraftedScion)
    EnableBossHealthBar(Characters.GraftedScion, name=904690000)
    if FlagEnabled(10010030):
        return
    AddSpecialEffect(PLAYER, 4290)


@RestartOnRest(10012811)
def Event_10012811():
    """Event 10012811"""
    if FlagEnabled(10010800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.GraftedScion, 16265))
    
    MAIN.Await(AND_1)
    
    EnableFlag(10012802)


@RestartOnRest(10012849)
def Event_10012849():
    """Event 10012849"""
    if FlagDisabled(101):
        CommonFunc_9005800(
            0,
            flag=10010800,
            entity=Assets.AEG099_001_9000,
            region=10012800,
            flag_1=10012805,
            character=10015800,
            action_button_id=10000,
            left=10010801,
            region_1=10012801,
        )
    else:
        CommonFunc_9005800(
            0,
            flag=10010800,
            entity=Assets.AEG099_001_9001,
            region=10012800,
            flag_1=10012805,
            character=10015800,
            action_button_id=10000,
            left=10010801,
            region_1=10012801,
        )
    CommonFunc_9005801(
        0,
        flag=10010800,
        entity=Assets.AEG099_001_9001,
        region=10012800,
        flag_1=10012805,
        flag_2=10012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=10010800, asset=Assets.AEG099_001_9000, model_point=16, right=10010801)
    CommonFunc_9005811(0, flag=10010800, asset=Assets.AEG099_001_9001, model_point=16, right=0)
    CommonFunc_9005822(0, 10010800, 920900, 10012805, 10012806, 0, 10012802, 0, 0)


@RestartOnRest(10010790)
def Event_10010790():
    """Event 10010790"""
    EnableBackread(Characters.FingerMaiden)
    EnableCharacter(Characters.FingerMaiden)
    ForceAnimation(Characters.FingerMaiden, 90100)
    DisableAnimations(Characters.FingerMaiden)


@RestartOnRest(10010791)
def Event_10010791():
    """Event 10010791"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400033):
        return
    if FlagDisabled(400031):
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6471, entity=Characters.FingerMaiden))
    
    RemoveGoodFromPlayer(item=8154, quantity=1)
    AwardItemLot(100330, host_only=False)
    End()


@RestartOnRest(10010792)
def Event_10010792():
    """Event 10010792"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(50):
        return
    if FlagEnabled(10019200):
        return
    OR_1.Add(PlayerHasGood(9500))
    OR_2.Add(TimeElapsed(seconds=5.0))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    WaitFrames(frames=1)
    OR_5.Add(PlayerHasGood(9500))
    SkipLinesIfConditionFalse(3, OR_5)
    EnableFlag(66150)
    EnableFlag(66170)
    EnableFlag(66180)
    EnableFlag(10019200)
    End()


@NeverRestart(10012900)
def Event_10012900():
    """Event 10012900"""
    MAIN.Await(FlagEnabled(10010900))
    
    IncrementEventValue(10010910, bit_count=32, max_value=999999999)
    Restart()
