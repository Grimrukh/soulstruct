"""
Stone Platform

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
from .enums.m19_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=19000800,
        grace_flag=19000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=8.0,
    )
    Event_19000100()
    Event_19000110()
    Event_19000120()
    Event_19002500()
    Event_19002502()
    Event_19002800()
    Event_19002810()
    Event_19002811()
    Event_19002812()
    Event_19002830()
    Event_19002849()
    Event_19002900()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_19000050()


@ContinueOnRest(19000100)
def Event_19000100():
    """Event 19000100"""
    GotoIfPlayerInOwnWorld(Label.L0)
    DisableAsset(Assets.AEG227_018_1000)
    DisableAsset(Assets.AEG227_017_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(120):
        return
    OR_15.Add(FlagEnabled(9400))
    OR_15.Add(FlagEnabled(9401))
    OR_15.Add(FlagEnabled(9402))
    OR_15.Add(FlagEnabled(9403))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    DisableAsset(Assets.AEG227_018_1000)
    DisableAsset(Assets.AEG227_017_1000)
    AND_1.Add(FlagEnabled(19001100))
    
    MAIN.Await(AND_1)
    
    EnableAsset(Assets.AEG227_018_1000)
    EnableAsset(Assets.AEG227_017_1000)
    DisableCharacter(Characters.Radagon)
    DisableAnimations(Characters.Radagon)
    DisableAsset(Assets.AEG301_240_1000)
    AND_2.Add(FlagDisabled(108))
    OR_4.Add(AND_2)
    AND_3.Add(FlagEnabled(108))
    AND_3.Add(FlagEnabled(116))
    OR_4.Add(AND_3)
    AND_5.Add(OR_4)
    OR_5.Add(FlagEnabled(9400))
    OR_5.Add(FlagEnabled(9401))
    OR_5.Add(FlagEnabled(9402))
    OR_5.Add(FlagEnabled(9403))
    AND_5.Add(OR_5)
    
    MAIN.Await(AND_5)
    
    AND_10.Add(PlayerGender(gender=Gender.Female))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 361000))
    AND_11.Add(PlayerGender(gender=Gender.Male))
    AND_11.Add(CharacterHasSpecialEffect(PLAYER, 361000))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    SkipLinesIfConditionTrue(3, OR_10)
    DisableFlag(780020)
    EnableFlag(780021)
    SkipLines(2)
    EnableFlag(780020)
    DisableFlag(780021)

    # --- Label 15 --- #
    DefineLabel(15)
    EnableFlag(19000100)
    EnableFlag(19002100)
    GotoIfFlagEnabled(Label.L13, flag=9403)
    GotoIfFlagEnabled(Label.L12, flag=9402)
    GotoIfFlagEnabled(Label.L11, flag=9401)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000010,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=10)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 11 --- #
    DefineLabel(11)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000060,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=20)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 12 --- #
    DefineLabel(12)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000070,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=30)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 13 --- #
    DefineLabel(13)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
        cutscene_id=19000080,
        cutscene_flags=CutsceneFlags.IsEndingCutscene,
        move_to_region=11712500,
        map_id=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_21=False,
        update_stable_position=False,
    )
    TriggerMultiplayerEvent(event_id=40)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)


@ContinueOnRest(19000110)
def Event_19000110():
    """Event 19000110"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(120):
        return
    OR_15.Add(FlagEnabled(9404))
    OR_15.Add(FlagEnabled(9405))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    AND_3.Add(FlagEnabled(19001100))
    AND_3.Add(FlagEnabled(1034509406))
    AND_1.Add(FlagDisabled(108))
    OR_3.Add(AND_1)
    AND_2.Add(FlagEnabled(108))
    AND_2.Add(FlagEnabled(116))
    OR_3.Add(AND_2)
    AND_3.Add(OR_3)
    
    MAIN.Await(AND_3)
    
    CreateAssetVFX(Assets.AEG099_090_9001, vfx_id=100, model_point=30070)
    AND_4.Add(ActionButtonParamActivated(action_button_id=9610, entity=Assets.AEG099_090_9001))
    AND_4.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_4)

    # --- Label 15 --- #
    DefineLabel(15)
    if FlagDisabled(1034509407):
        PlayCutscene(19000020, cutscene_flags=0, player_id=10000)
        EnableFlag(9404)
        TriggerMultiplayerEvent(event_id=50)
    else:
        PlayCutscene(19000021, cutscene_flags=0, player_id=10000)
        EnableFlag(9405)
        TriggerMultiplayerEvent(event_id=60)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(120)
    EnableFlag(6010)
    AwardAchievement(achievement_id=2)
    SetRespawnPoint(respawn_point=11102020)
    SaveRequest()
    EnableFlag(21)


@ContinueOnRest(19000120)
def Event_19000120():
    """Event 19000120"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(120):
        return
    OR_15.Add(FlagEnabled(9406))
    OR_15.Add(FlagEnabled(9407))
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    AND_1.Add(FlagEnabled(19001100))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_1.Add(FlagEnabled(108))
    AND_1.Add(FlagDisabled(116))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9620, entity=Assets.AEG099_090_9002))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 67070)
    Wait(10.0)

    # --- Label 15 --- #
    DefineLabel(15)
    if FlagDisabled(109):
        PlayCutscene(19000030, cutscene_flags=0, player_id=10000)
        EnableFlag(9406)
        TriggerMultiplayerEvent(event_id=70)
    else:
        PlayCutscene(19000031, cutscene_flags=0, player_id=10000)
        EnableFlag(9407)
        TriggerMultiplayerEvent(event_id=80)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(120)
    EnableFlag(6010)
    AwardAchievement(achievement_id=3)
    SetRespawnPoint(respawn_point=11102020)
    SaveRequest()
    EnableFlag(22)


@ContinueOnRest(19000050)
def Event_19000050():
    """Event 19000050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(19002500)
def Event_19002500():
    """Event 19002500"""
    GotoIfFlagDisabled(Label.L0, flag=19000800)
    CreateAssetVFX(Assets.AEG099_003_9000, vfx_id=101, model_point=1530)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerInOwnWorld(Label.L1)
    GotoIfFlagDisabled(Label.L1, flag=19002801)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=20000,
        destination_type=CoordEntityType.Region,
        destination=19002811,
        model_point=-1,
        copy_draw_parent=20000,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    CreateAssetVFX(Assets.AEG099_003_9000, vfx_id=101, model_point=1530)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=19002500)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(19000800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9501, entity=Assets.AEG099_003_9000))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=CharacterType.BlackPhantom))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=CharacterType.Unknown3))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=CharacterType.Unknown4))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=CharacterType.Unknown5))
    OR_9.Add(CharacterInvadeType(character=20000, invade_type=CharacterType.Unknown7))
    if OR_9:
        return
    ForceAnimation(PLAYER, 67080)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=19002500)
    Wait(2.4000000953674316)
    CreateAssetVFX(Assets.AEG099_003_9001, vfx_id=101, model_point=1531)
    if PlayerNotInOwnWorld():
        GotoIfFlagEnabled(Label.L2, flag=19002500)
    Wait(3.5999999046325684)
    EnableNetworkFlag(19002500)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000040,
            cutscene_flags=CutsceneFlags.Unknown32,
            move_to_region=19002810,
            map_id=19000000,
            player_id=10000,
            unk_20_24=19000,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000040,
            cutscene_flags=CutsceneFlags.Unknown32,
            move_to_region=19002811,
            map_id=19000000,
            player_id=10000,
            unk_20_24=19000,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if FlagDisabled(119):
        EnableFlag(119)
    DeleteAssetVFX(Assets.AEG099_003_9001, erase_root=False)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=13.0600004196167, y_angle=-63.06999969482422)


@RestartOnRest(19002502)
def Event_19002502():
    """Event 19002502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(71900):
        return
    if FlagEnabled(121):
        return
    AND_1.Add(InsideMap(game_map=STONE_PLATFORM))
    AND_1.Add(FlagEnabled(9123))
    AND_1.Add(FlagDisabled(71900))
    AND_1.Add(FlagDisabled(121))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(FlagEnabled(71900))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(19002800)
def Event_19002800():
    """Event 19002800"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=19002815))
    AND_1.Add(FlagEnabled(19000804))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    if FlagEnabled(19000804):
        return
    GotoIfFlagEnabled(Label.L0, flag=19000800)
    
    MAIN.Await(HealthValue(Characters.EldenBeast) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(19008000, 888880000, sound_type=SoundType.s_SFX)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    
    MAIN.Await(CharacterDead(Characters.EldenBeast))
    
    Wait(4.5)
    KillBossAndDisplayBanner(character=Characters.EldenBeast, banner_type=BannerType.GodSlain)
    EnableFlag(19000800)
    EnableFlag(19001100)
    EnableFlag(9123)
    if PlayerNotInOwnWorld():
        return
    EnableFlag(61123)
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    Wait(7.5)
    AND_2.Add(HealthRatio(PLAYER) == 0.0)
    if AND_2:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=19000050,
        cutscene_flags=0,
        move_to_region=19002814,
        map_id=19000000,
        player_id=10000,
        unk_20_24=19000,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    SetCameraAngle(x_angle=20.899999618530273, y_angle=-51.560001373291016)
    SetPlayerPositionDisplay(
        state=True,
        aboveground=True,
        game_map=STONE_PLATFORM,
        x=181.10000610351562,
        y=102.3499984741211,
        z=-607.0599975585938,
    )
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    EnableFlag(19000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)


@RestartOnRest(19002810)
def Event_19002810():
    """Event 19002810"""
    GotoIfFlagDisabled(Label.L0, flag=19000800)
    DisableCharacter(19005800)
    DisableAnimations(19005800)
    Kill(19005800)
    DisableCharacter(19000811)
    DisableAnimations(19000811)
    DisableAsset(Assets.AEG301_240_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(19005800)
    DisableCharacter(Characters.Radagon)
    DisableAnimations(Characters.Radagon)
    SetCharacterFadeOnEnable(character=Characters.Radagon, state=False)
    DisableAsset(Assets.AEG301_240_1000)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.Radagon, radius=20.0))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=14.600000381469727, y_angle=-72.33000183105469)
    EnableNetworkFlag(19000801)
    EnableNetworkFlag(19002801)
    EnableNetworkFlag(19002806)
    DisableAsset(Assets.AEG301_240_1000)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.Radagon)
    EnableAnimations(Characters.Radagon)
    ForceAnimation(Characters.Radagon, 20010)
    EnableAI(Characters.Radagon)
    SetNetworkUpdateRate(Characters.Radagon, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Radagon, name=902190000)


@RestartOnRest(19002811)
def Event_19002811():
    """Event 19002811"""
    if FlagEnabled(19000800):
        return
    AND_1.Add(CharacterDead(Characters.Radagon))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    EnableFlag(19002802)
    EnableFlag(19000802)


@RestartOnRest(19002812)
def Event_19002812():
    """Event 19002812"""
    if FlagEnabled(19000800):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableHealthBar(Characters.EldenBeast)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(19002802))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.EldenBeast, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=STONE_PLATFORM,
        x=181.10000610351562,
        y=102.3499984741211,
        z=-607.0599975585938,
    )
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000000,
            cutscene_flags=0,
            move_to_region=19002812,
            map_id=19000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=19000000,
            cutscene_flags=0,
            move_to_region=19002813,
            map_id=19000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-11.329999923706055, y_angle=-25.829999923706055)
    if PlayerInOwnWorld():
        EnableThisNetworkSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    Move(35000, destination=19002813, destination_type=CoordEntityType.Region, copy_draw_parent=Characters.EldenBeast)
    Move(
        Characters.TalkDummy3,
        destination=19002813,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.EldenBeast,
    )
    SetCharacterTalkRange(character=Characters.TalkDummy3, distance=200.0)
    EnableCharacter(Characters.EldenBeast)
    EnableAnimations(Characters.EldenBeast)
    EnableAI(19005800)
    ForceAnimation(Characters.EldenBeast, 20000)
    EnableBossHealthBar(Characters.EldenBeast, name=902200000)
    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    WaitFramesAfterCutscene(frames=1)
    AttachAssetToCharacter(character=Characters.TalkDummy3, model_point=10, asset=Assets.AEG099_052_9000)


@RestartOnRest(19002820)
def Event_19002820():
    """Event 19002820"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(19000800):
        return
    AND_1.Add(FlagRangeAllDisabled(flag_range=(19002830, 19002834)))
    AND_1.Add(CharacterHasSpecialEffect(Characters.EldenBeast, 18600))
    
    MAIN.Await(AND_1)
    
    EnableRandomFlagInRange(flag_range=(19002830, 19002834))
    Wait(3.0)
    Restart()


@RestartOnRest(19002821)
def Event_19002821():
    """Event 19002821"""
    if FlagEnabled(19000800):
        return
    Event_19002822(0, flag=19002830, model_point=110, model_point_1=111, model_point_2=112, model_point_3=113)
    Event_19002822(1, flag=19002831, model_point=111, model_point_1=112, model_point_2=113, model_point_3=114)
    Event_19002822(2, flag=19002832, model_point=112, model_point_1=113, model_point_2=114, model_point_3=115)
    Event_19002822(3, flag=19002833, model_point=113, model_point_1=114, model_point_2=115, model_point_3=116)
    Event_19002822(4, flag=19002834, model_point=114, model_point_1=115, model_point_2=116, model_point_3=117)


@RestartOnRest(19002822)
def Event_19002822(_, flag: uint, model_point: int, model_point_1: int, model_point_2: int, model_point_3: int):
    """Event 19002822"""
    if FlagEnabled(19000800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Move(
        19000801,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    Move(
        19000802,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_1,
        short_move=True,
    )
    Move(
        19000803,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_2,
        short_move=True,
    )
    Move(
        19000804,
        destination=Characters.EldenBeast,
        destination_type=CoordEntityType.Character,
        model_point=model_point_3,
        short_move=True,
    )
    ForceAnimation(Characters.EldenBeast, 3023, skip_transition=True)
    ForceAnimation(19000801, 3000, skip_transition=True)
    ForceAnimation(19000802, 3000, skip_transition=True)
    ForceAnimation(19000803, 3000, skip_transition=True)
    ForceAnimation(19000804, 3000, skip_transition=True)
    Wait(2.0)
    DisableFlag(flag)
    Restart()


@RestartOnRest(19002830)
def Event_19002830():
    """Event 19002830"""
    DisableNetworkSync()
    if FlagEnabled(19000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.EldenBeast, 18606))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=2201, locked_camera_id=2201)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.EldenBeast, 18606))
    
    MAIN.Await(AND_2)
    
    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    Restart()


@RestartOnRest(19002849)
def Event_19002849():
    """Event 19002849"""
    CommonFunc_9005800(
        0,
        flag=19000800,
        entity=Assets.AEG099_001_9000,
        region=19002800,
        flag_1=19002805,
        character=19005800,
        action_button_id=10000,
        left=19002801,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=19000800,
        entity=Assets.AEG099_001_9000,
        region=19002800,
        flag_1=19002805,
        flag_2=19002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=19000800, asset=Assets.AEG099_001_9000, model_point=5, right=19002801)
    CommonFunc_9005822(
        0,
        flag=19000800,
        bgm_boss_conv_param_id=219000,
        flag_1=19002805,
        flag_2=19002806,
        right=0,
        flag_3=19002802,
        left=0,
        left_1=1,
    )


@RestartOnRest(19002900)
def Event_19002900():
    """Event 19002900"""
    CreateAssetVFX(Assets.AEG099_090_9000, vfx_id=100, model_point=1300)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9000, entity=Assets.AEG099_090_9000))
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=19002900,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=False,
    )
