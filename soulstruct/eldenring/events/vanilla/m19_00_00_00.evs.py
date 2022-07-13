"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 9005810, args=(19000800, 19000000, 19000950, 19001950, 8.0), arg_types="IIIIf")
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


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_19000050()


@NeverRestart(19000100)
def Event_19000100():
    """Event 19000100"""
    GotoIfPlayerInOwnWorld(Label.L0)
    DisableObject(19001100)
    DisableObject(19001101)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(120)
    IfFlagEnabled(OR_15, 9400)
    IfFlagEnabled(OR_15, 9401)
    IfFlagEnabled(OR_15, 9402)
    IfFlagEnabled(OR_15, 9403)
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    DisableObject(19001100)
    DisableObject(19001101)
    IfFlagEnabled(AND_1, 19001100)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableObject(19001100)
    EnableObject(19001101)
    DisableCharacter(19000810)
    DisableAnimations(19000810)
    DisableObject(19001810)
    IfFlagDisabled(AND_2, 108)
    IfConditionTrue(OR_4, input_condition=AND_2)
    IfFlagEnabled(AND_3, 108)
    IfFlagEnabled(AND_3, 116)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(AND_5, input_condition=OR_4)
    IfFlagEnabled(OR_5, 9400)
    IfFlagEnabled(OR_5, 9401)
    IfFlagEnabled(OR_5, 9402)
    IfFlagEnabled(OR_5, 9403)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfConditionTrue(MAIN, input_condition=AND_5)
    IfSteamConnectionState(AND_10, is_disconnected=True)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, PLAYER, 361000)
    IfSteamConnectionState(AND_11, is_disconnected=False)
    IfCharacterHasSpecialEffect(AND_11, PLAYER, 361000)
    IfConditionTrue(OR_10, input_condition=AND_10)
    IfConditionTrue(OR_10, input_condition=AND_11)
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
    UnknownCutscene_13(
        cutscene_id=19000010,
        cutscene_flags=CutsceneFlags.Unknown64,
        respawn_point=11712500,
        move_to_region=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_24=0,
    )
    TriggerMultiplayerEvent(event_id=10)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 11 --- #
    DefineLabel(11)
    UnknownCutscene_13(
        cutscene_id=19000060,
        cutscene_flags=CutsceneFlags.Unknown64,
        respawn_point=11712500,
        move_to_region=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_24=0,
    )
    TriggerMultiplayerEvent(event_id=20)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 12 --- #
    DefineLabel(12)
    UnknownCutscene_13(
        cutscene_id=19000070,
        cutscene_flags=CutsceneFlags.Unknown64,
        respawn_point=11712500,
        move_to_region=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_24=0,
    )
    TriggerMultiplayerEvent(event_id=30)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 13 --- #
    DefineLabel(13)
    UnknownCutscene_13(
        cutscene_id=19000080,
        cutscene_flags=CutsceneFlags.Unknown64,
        respawn_point=11712500,
        move_to_region=11710000,
        player_id=10000,
        unk_16_20=19000,
        unk_20_24=0,
    )
    TriggerMultiplayerEvent(event_id=40)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L15)

    # --- Label 15 --- #
    DefineLabel(15)


@NeverRestart(19000110)
def Event_19000110():
    """Event 19000110"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(120)
    IfFlagEnabled(OR_15, 9404)
    IfFlagEnabled(OR_15, 9405)
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    IfFlagEnabled(AND_3, 19001100)
    IfFlagEnabled(AND_3, 1034509406)
    IfFlagDisabled(AND_1, 108)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfFlagEnabled(AND_2, 108)
    IfFlagEnabled(AND_2, 116)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_3)
    CreateObjectVFX(19001110, vfx_id=100, model_point=30070)
    IfActionButtonParamActivated(AND_4, action_button_id=9610, entity=19001110)
    IfPlayerInOwnWorld(AND_4)
    IfConditionTrue(MAIN, input_condition=AND_4)

    # --- Label 15 --- #
    DefineLabel(15)
    SkipLinesIfFlagEnabled(4, 1034509407)
    PlayCutscene(19000020, cutscene_flags=0, player_id=10000)
    EnableFlag(9404)
    TriggerMultiplayerEvent(event_id=50)
    SkipLines(3)
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


@NeverRestart(19000120)
def Event_19000120():
    """Event 19000120"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(120)
    IfFlagEnabled(OR_15, 9406)
    IfFlagEnabled(OR_15, 9407)
    GotoIfConditionTrue(Label.L15, input_condition=OR_15)
    IfFlagEnabled(AND_1, 19001100)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitFrames(frames=1)
    IfFlagEnabled(AND_1, 108)
    IfFlagDisabled(AND_1, 116)
    IfActionButtonParamActivated(AND_1, action_button_id=9620, entity=19001120)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 67070, unknown2=1.0)
    Wait(10.0)

    # --- Label 15 --- #
    DefineLabel(15)
    SkipLinesIfFlagEnabled(4, 109)
    PlayCutscene(19000030, cutscene_flags=0, player_id=10000)
    EnableFlag(9406)
    TriggerMultiplayerEvent(event_id=70)
    SkipLines(3)
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


@NeverRestart(19000050)
def Event_19000050():
    """Event 19000050"""
    EndIfThisEventSlotFlagEnabled()


@NeverRestart(19002500)
def Event_19002500():
    """Event 19002500"""
    GotoIfFlagDisabled(Label.L0, flag=19000800)
    CreateObjectVFX(19001500, vfx_id=101, model_point=1530)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerInOwnWorld(Label.L1)
    GotoIfFlagDisabled(Label.L1, flag=19002801)
    Unknown_2004_74(
        character=20000,
        unknown1=1,
        region=19002811,
        unknown2=-1,
        character_2=20000,
        unknown3=0,
        unknown4=1,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    CreateObjectVFX(19001500, vfx_id=101, model_point=1530)
    SkipLinesIfPlayerInOwnWorld(1)
    GotoIfFlagEnabled(Label.L2, flag=19002500)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 19000800)
    IfActionButtonParamActivated(AND_1, action_button_id=9501, entity=19001500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    IfUnknownCharacterCondition_31(OR_9, character=20000, unk_4_8=2, unk_8_12=1.0)
    IfUnknownCharacterCondition_31(OR_9, character=20000, unk_4_8=3, unk_8_12=1.0)
    IfUnknownCharacterCondition_31(OR_9, character=20000, unk_4_8=4, unk_8_12=1.0)
    IfUnknownCharacterCondition_31(OR_9, character=20000, unk_4_8=5, unk_8_12=1.0)
    IfUnknownCharacterCondition_31(OR_9, character=20000, unk_4_8=7, unk_8_12=1.0)
    EndIfConditionTrue(input_condition=OR_9)
    ForceAnimation(PLAYER, 67080, unknown2=1.0)
    SkipLinesIfPlayerInOwnWorld(1)
    GotoIfFlagEnabled(Label.L2, flag=19002500)
    Wait(2.4000000953674316)
    CreateObjectVFX(19001501, vfx_id=101, model_point=1531)
    SkipLinesIfPlayerInOwnWorld(1)
    GotoIfFlagEnabled(Label.L2, flag=19002500)
    Wait(3.5999999046325684)
    EnableNetworkFlag(19002500)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=19000040,
        cutscene_flags=CutsceneFlags.Unknown32,
        move_to_region=19002810,
        map_base_id=19000000,
        player_id=10000,
        unknown2=19000,
        unknown3=0,
    )
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=19000040,
        cutscene_flags=CutsceneFlags.Unknown32,
        move_to_region=19002811,
        map_base_id=19000000,
        player_id=10000,
        unknown2=19000,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfFlagEnabled(1, 119)
    EnableFlag(119)
    DeleteObjectVFX(19001501, erase_root=False)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=13.0600004196167, unknown2=-63.06999969482422)


@RestartOnRest(19002502)
def Event_19002502():
    """Event 19002502"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(71900)
    EndIfFlagEnabled(121)
    IfInsideMap(AND_1, game_map=STONE_PLATFORM)
    IfFlagEnabled(AND_1, 9123)
    IfFlagDisabled(AND_1, 71900)
    IfFlagDisabled(AND_1, 121)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    IfFlagEnabled(AND_2, 71900)
    IfConditionTrue(MAIN, input_condition=AND_2)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(19002800)
def Event_19002800():
    """Event 19002800"""
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=19002815)
    IfFlagEnabled(AND_1, 19000804)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    EndIfFlagEnabled(19000804)
    GotoIfFlagEnabled(Label.L0, flag=19000800)
    IfHealthValueLessThanOrEqual(MAIN, 19000800, value=0)
    Wait(4.0)
    PlaySoundEffect(19008000, 888880000, sound_type=SoundType.s_SFX)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    IfCharacterDead(MAIN, 19000800)
    Wait(4.5)
    KillBossAndDisplayBanner(character=19000800, banner_type=BannerType.Unknown27)
    EnableFlag(19000800)
    EnableFlag(19001100)
    EnableFlag(9123)
    EndIfPlayerNotInOwnWorld()
    EnableFlag(61123)
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    Wait(7.5)
    IfHealthRatioEqual(AND_2, PLAYER, value=0.0)
    EndIfConditionTrue(input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9021)
    UnknownCutscene_11(
        cutscene_id=19000050,
        cutscene_flags=0,
        move_to_region=19002814,
        map_base_id=19000000,
        player_id=10000,
        unknown2=19000,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    UnknownCamera_4(unknown1=20.899999618530273, unknown2=-51.560001373291016)
    Unknown_2003_76(
        unk_0_4=1245441,
        unk_4_8=0,
        unk_8_12=181.10000610351562,
        unk_12_16=102.3499984741211,
        unk_16_20=-607.0599975585938,
    )
    SetRespawnPoint(respawn_point=19002814)
    SaveRequest()
    EnableFlag(19000804)
    SetBackreadStateAlternate(35000, False)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)


@RestartOnRest(19002810)
def Event_19002810():
    """Event 19002810"""
    GotoIfFlagDisabled(Label.L0, flag=19000800)
    DisableCharacter(19005800)
    DisableAnimations(19005800)
    Kill(19005800)
    DisableCharacter(19000811)
    DisableAnimations(19000811)
    DisableObject(19001810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(19005800)
    DisableCharacter(19000810)
    DisableAnimations(19000810)
    Unknown_2004_73(entity=19000810, unk_4_8=0)
    DisableObject(19001810)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=19000810, radius=20.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=14.600000381469727, unknown2=-72.33000183105469)
    EnableNetworkFlag(19000801)
    EnableNetworkFlag(19002801)
    EnableNetworkFlag(19002806)
    DisableObject(19001810)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(19000810)
    EnableAnimations(19000810)
    ForceAnimation(19000810, 20010, unknown2=1.0)
    EnableAI(19000810)
    SetNetworkUpdateRate(19000810, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(19000810, name=902190000)


@RestartOnRest(19002811)
def Event_19002811():
    """Event 19002811"""
    EndIfFlagEnabled(19000800)
    IfCharacterDead(AND_1, 19000810)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(3.0)
    EnableFlag(19002802)
    EnableFlag(19000802)


@RestartOnRest(19002812)
def Event_19002812():
    """Event 19002812"""
    EndIfFlagEnabled(19000800)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableHealthBar(19000800)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 19002802)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=19000800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Unknown_2003_76(
        unk_0_4=1245440,
        unk_4_8=0,
        unk_8_12=181.10000610351562,
        unk_12_16=102.3499984741211,
        unk_16_20=-607.0599975585938,
    )
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_11(
        cutscene_id=19000000,
        cutscene_flags=0,
        move_to_region=19002812,
        map_base_id=19000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    SkipLines(1)
    UnknownCutscene_11(
        cutscene_id=19000000,
        cutscene_flags=0,
        move_to_region=19002813,
        map_base_id=19000000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=-11.329999923706055, unknown2=-25.829999923706055)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    SetBackreadStateAlternate(35000, True)
    SetNetworkUpdateRate(35000, is_fixed=True, update_rate=CharacterUpdateRate.Unknown105)
    Move(35000, destination=19002813, destination_type=CoordEntityType.Region, copy_draw_parent=19000800)
    Move(19000130, destination=19002813, destination_type=CoordEntityType.Region, copy_draw_parent=19000800)
    SetCharacterTalkRange(character=19000130, distance=200.0)
    EnableCharacter(19000800)
    EnableAnimations(19000800)
    EnableAI(19005800)
    ForceAnimation(19000800, 20000, unknown2=1.0)
    EnableBossHealthBar(19000800, name=902200000)
    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    WaitFramesAfterCutscene(frames=1)
    AttachObjectToCharacter(character=19000130, model_point=10, obj=19001130)


@RestartOnRest(19002820)
def Event_19002820():
    """Event 19002820"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(19000800)
    IfFlagRangeAllDisabled(AND_1, flag_range=(19002830, 19002834))
    IfCharacterHasSpecialEffect(AND_1, 19000800, 18600)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableRandomFlagInRange(flag_range=(19002830, 19002834))
    Wait(3.0)
    Restart()


@RestartOnRest(19002821)
def Event_19002821():
    """Event 19002821"""
    EndIfFlagEnabled(19000800)
    Event_19002822(0, flag=19002830, model_point=110, model_point_1=111, model_point_2=112, model_point_3=113)
    Event_19002822(1, flag=19002831, model_point=111, model_point_1=112, model_point_2=113, model_point_3=114)
    Event_19002822(2, flag=19002832, model_point=112, model_point_1=113, model_point_2=114, model_point_3=115)
    Event_19002822(3, flag=19002833, model_point=113, model_point_1=114, model_point_2=115, model_point_3=116)
    Event_19002822(4, 19002834, 114, 115, 116, 117)


@RestartOnRest(19002822)
def Event_19002822(_, flag: uint, model_point: int, model_point_1: int, model_point_2: int, model_point_3: int):
    """Event 19002822"""
    EndIfFlagEnabled(19000800)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Move(
        19000801,
        destination=19000800,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    Move(
        19000802,
        destination=19000800,
        destination_type=CoordEntityType.Character,
        model_point=model_point_1,
        short_move=True,
    )
    Move(
        19000803,
        destination=19000800,
        destination_type=CoordEntityType.Character,
        model_point=model_point_2,
        short_move=True,
    )
    Move(
        19000804,
        destination=19000800,
        destination_type=CoordEntityType.Character,
        model_point=model_point_3,
        short_move=True,
    )
    ForceAnimation(19000800, 3023, skip_transition=True, unknown2=1.0)
    ForceAnimation(19000801, 3000, skip_transition=True, unknown2=1.0)
    ForceAnimation(19000802, 3000, skip_transition=True, unknown2=1.0)
    ForceAnimation(19000803, 3000, skip_transition=True, unknown2=1.0)
    ForceAnimation(19000804, 3000, skip_transition=True, unknown2=1.0)
    Wait(2.0)
    DisableFlag(flag)
    Restart()


@RestartOnRest(19002830)
def Event_19002830():
    """Event 19002830"""
    DisableNetworkSync()
    EndIfFlagEnabled(19000800)
    IfCharacterHasSpecialEffect(AND_1, 19000800, 18606)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=2201, locked_camera_id=2201)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 19000800, 18606)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ChangeCamera(normal_camera_id=2200, locked_camera_id=2200)
    Restart()


@RestartOnRest(19002849)
def Event_19002849():
    """Event 19002849"""
    RunCommonEvent(
        0,
        9005800,
        args=(19000800, 19001800, 19002800, 19002805, 19005800, 10000, 19002801, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(19000800, 19001800, 19002800, 19002805, 19002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(19000800, 19001800, 5, 19002801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(19000800, 219000, 19002805, 19002806, 0, 19002802, 0, 1), arg_types="IiIIIIii")


@RestartOnRest(19002900)
def Event_19002900():
    """Event 19002900"""
    CreateObjectVFX(19001900, vfx_id=100, model_point=1300)
    IfActionButtonParamActivated(MAIN, action_button_id=9000, entity=19001900)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=19002900,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=0,
    )
