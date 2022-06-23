"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11810992, obj=1811960, reaction_distance=1.0)
    RegisterBonfire(bonfire_flag=11810984, obj=1811961, reaction_distance=1.0)
    RegisterLadder(start_climbing_flag=11810010, stop_climbing_flag=11810011, obj=1811140)
    DisableMapCollision(collision=1813121)
    DisableFlag(11810315)
    DisableFlag(11810112)
    DisableObjectActivation(1811100, obj_act_id=-1)
    DisableObjectActivation(1811101, obj_act_id=-1)
    DisableObjectActivation(1811102, obj_act_id=-1)
    SkipLinesIfOutsideMap(4, game_map=UNDEAD_ASYLUM)
    SkipLinesIfFlagEnabled(3, 11810002)
    PlayCutscene(180101, cutscene_flags=8, player_id=10000, move_to_region=1812011, game_map=UNDEAD_ASYLUM)
    EnableFlag(11810002)
    SetRespawnPoint(respawn_point=1812900)
    Event_11810090(0, 1811700, 1811701, 1812600, 1812601)
    Event_11810000()
    Event_11810150()
    Event_11810211()
    Event_11810200(1, 1811210, 1811211, 1811212)
    Event_11810310()
    Event_11810311()
    Event_11810312()
    Event_11810313()
    Event_11810120()
    Event_11810110()
    Event_11810111()
    Event_11810450()
    Event_11810320()
    Event_11810300()
    Event_11810850(0, 1810200, 27907000)
    Event_11810850(1, 1810213, 27907000)
    SkipLinesIfClient(44)
    Event_11810641(0, 3, 111, 11810601, 51810800)
    Event_11810641(1, 3, 270, 11810602, 51810810)
    Event_11810641(2, 3, 271, 11810603, 51810820)
    Event_11810641(3, 3, 272, 11810604, 51810830)
    Event_11810641(4, 3, 275, 11810605, 51810840)
    Event_11810641(5, 3, 293, 11810606, 51810850)
    Event_11810641(6, 3, 350, 11810607, 51810860)
    Event_11810641(7, 3, 500, 11810607, 51810860)
    Event_11810641(8, 3, 370, 11810608, 51810870)
    Event_11810641(9, 3, 375, 11810609, 51810880)
    Event_11810641(10, 3, 376, 11810610, 51810890)
    Event_11810641(11, 3, 380, 11810611, 51810900)
    Event_11810641(12, 3, 385, 11810612, 51810910)
    Event_11810641(13, 3, 501, 11810613, 51810920)
    Event_11810641(14, 0, 1330000, 11810614, 51810930)
    Event_11810641(15, 0, 1332000, 11810615, 51810940)
    Event_11810641(16, 0, 1396000, 11810616, 51810950)
    Event_11810641(17, 1, 190000, 11810617, 51810960)
    Event_11810641(18, 1, 290000, 11810618, 51810970)
    Event_11810641(19, 1, 560000, 11810619, 51810980)
    Event_11810641(20, 2, 130, 11810620, 51810990)
    Event_11810641(21, 3, 711, 11810621, 51811000)
    Event_11810600()
    Event_11815110(0, 11810601, 3000, 51810800)
    Event_11815110(1, 11810602, 3010, 51810810)
    Event_11815110(2, 11810603, 3020, 51810820)
    Event_11815110(3, 11810604, 3030, 51810830)
    Event_11815110(4, 11810605, 3040, 51810840)
    Event_11815110(5, 11810606, 3050, 51810850)
    Event_11815110(6, 11810607, 3060, 51810860)
    Event_11815110(7, 11810608, 3070, 51810870)
    Event_11815110(8, 11810609, 3080, 51810880)
    Event_11815110(9, 11810610, 3090, 51810890)
    Event_11815110(10, 11810611, 3100, 51810900)
    Event_11815110(11, 11810612, 3110, 51810910)
    Event_11815110(12, 11810613, 3120, 51810920)
    Event_11815110(13, 11810614, 3130, 51810930)
    Event_11815110(14, 11810615, 3140, 51810940)
    Event_11815110(15, 11810616, 3150, 51810950)
    Event_11815110(16, 11810617, 3160, 51810960)
    Event_11815110(17, 11810618, 3170, 51810970)
    Event_11815110(18, 11810619, 3180, 51810980)
    Event_11815110(19, 11810620, 3190, 51810990)
    Event_11815110(20, 11810621, 3200, 51811000)
    Event_11810100(0, 11810100, 1811100, 10010869)
    Event_11810100(1, 11810101, 1811101, 10010869)
    Event_11810100(2, 11810102, 1811102, 10010869)
    Event_11810100(3, 11810103, 1811103, 10010869)
    Event_11810100(4, 11810104, 1811104, 10010875)
    Event_11810100(5, 11810105, 1811105, 0)
    Event_11810100(6, 11810106, 1811106, 10010871)
    Event_11815150()
    Event_11810400(0, 0, 1811601, 1811602, 1811602, 0, 0, 0, 0)
    Event_11810400(1, 1, 1811603, 1811604, 1811604, 0, 0, 0, 0)
    Event_11810400(2, 2, 1811605, 1811606, 1811606, 0, 0, 0, 0)
    Event_11810400(3, 3, 1811607, 1811608, 1811608, 0, 0, 0, 0)
    Event_11810400(4, 4, 1811609, 1811610, 1811610, 0, 0, 0, 0)
    Event_11810400(5, 5, 1811611, 1811612, 1811613, 0, 0, 1, 0)
    Event_11810400(6, 6, 1811614, 1811615, 1811616, 1, 0, 0, 0)
    Event_11810400(7, 7, 1811617, 1811618, 1811619, 0, 1, 0, 0)
    Event_11810400(8, 8, 1811620, 1811621, 1811622, 0, 0, 0, 1)
    Event_11810400(9, 9, 1811623, 1811624, 1811624, 0, 0, 0, 0)
    DisableSoundEvent(sound_id=1813800)
    SkipLinesIfFlagEnabled(2, 11810312)
    DisableFlag(11810310)
    DisableFlag(11810314)
    SkipLinesIfFlagDisabled(1, 61810105)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SkipLinesIfFlagDisabled(7, 16)
    Event_11815392()
    DisableObject(1811990)
    DeleteVFX(vfx_id=1811991, erase_root_only=False)
    EndOfAnimation(obj=1811115, animation_id=1)
    EndOfAnimation(obj=1811111, animation_id=1)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SkipLines(6)
    Event_11815390()
    Event_11815393()
    Event_11815392()
    Event_11810001()
    Event_11815394()
    Event_11815395()
    DisableObject(1811890)
    DeleteVFX(vfx_id=1811891, erase_root_only=False)
    DisableSoundEvent(sound_id=1813801)
    EndIfFlagDisabled(11810000)
    SkipLinesIfFlagDisabled(2, 11810900)
    Event_11815382()
    SkipLines(4)
    Event_11815382()
    Event_11810900()
    Event_11815384()
    Event_11815385()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    SkipLinesIfClient(11)
    SkipLinesIfFlagEnabled(10, 705)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    SkipLinesIfConditionFalse(8, 1)
    EnableFlag(705)
    EnableFlag(50000082)
    SetRespawnPoint(respawn_point=1812900)
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    Event_11810050()
    Event_11810350()
    Event_11810220()
    HumanityRegistration(6023, event_flag=8326)
    SkipLinesIfFlagEnabled(1, 1061)
    DisableCharacter(6024)
    SetTeamType(6024, TeamType.HostileAlly)
    Event_11810520(0, 6023, 1060, 1074, 1073)
    Event_11810530(0, 6023)
    Event_11810531(0, 6024, 1060, 1074, 1061)
    Event_11810532(0, 6024, 1060, 1074, 1062)
    Event_11815010()


@NeverRestart(11810090)
def Event_11810090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11810090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_0_3,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)


@RestartOnRest(11815090)
def Event_11815090():
    """Event 11815090"""
    DisableCharacter(1810900)
    IfFlagEnabled(0, 11810000)
    IfBlackWorldTendencyComparison(-1, ComparisonType.GreaterThan, value=50)
    IfFlagEnabled(-1, 11815090)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11815090)
    EnableCharacter(1810900)
    IfBlackWorldTendencyComparison(0, ComparisonType.LessThanOrEqual, value=50)
    Kill(1810900)


@NeverRestart(11815390)
def Event_11815390():
    """Event 11815390"""
    IfFlagDisabled(1, 16)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1812998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1811990,
    )
    IfConditionTrue(0, input_condition=1)
    Move(1810800, destination=1812301, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(PLAYER, target_entity=1812997)
    ForceAnimation(PLAYER, 7410)
    DisableSoapstoneMessage(1813210)
    ForceAnimation(1811115, 3)
    SkipLinesIfFlagDisabled(1, 11810112)
    ForceAnimation(1811111, 3)
    Restart()


@NeverRestart(11815393)
def Event_11815393():
    """Event 11815393"""
    SkipLinesIfThisEventFlagEnabled(5)
    IfFlagDisabled(1, 16)
    IfCharacterInsideRegion(-1, PLAYER, region=1812996)
    IfCharacterInsideRegion(-1, PLAYER, region=1812350)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1810800)


@RestartOnRest(11815392)
def Event_11815392():
    """Event 11815392"""
    SkipLinesIfFlagDisabled(3, 16)
    DisableCharacter(1810800)
    Kill(1810800)
    End()
    IfFlagDisabled(1, 11810310)
    IfCharacterInsideRegion(1, PLAYER, region=1812996)
    IfFlagEnabled(2, 11810310)
    IfCharacterInsideRegion(2, PLAYER, region=1812990)
    IfFlagEnabled(3, 11815393)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1810800)


@NeverRestart(11810001)
def Event_11810001():
    """Event 11810001"""
    IfHealthLessThanOrEqual(0, 1810800, value=0.0)
    PlaySoundEffect(anchor_entity=1810800, sound_id=777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1810800)
    EnableFlag(16)
    KillBoss(game_area_param_id=1810800)
    DisableObject(1811990)
    DeleteVFX(vfx_id=1811991)
    ForceAnimation(1811111, 1)
    SkipLinesIfFlagDisabled(1, 11810312)
    ForceAnimation(1811115, 1)
    DisableObjectActivation(1811111, obj_act_id=-1)


@NeverRestart(11815394)
def Event_11815394():
    """Event 11815394"""
    DisableNetworkSync()
    IfFlagDisabled(0, 11815396)
    IfFlagDisabled(1, 16)
    IfFlagEnabled(1, 11810310)
    IfFlagEnabled(1, 11815392)
    IfCharacterInsideRegion(-1, PLAYER, region=1812990)
    IfCharacterInsideRegion(-1, PLAYER, region=1812350)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11815396)
    EnableSoundEvent(sound_id=1813800)
    EnableBossHealthBar(1810800, name=2232, slot=0)
    Restart()


@NeverRestart(11815395)
def Event_11815395():
    """Event 11815395"""
    DisableNetworkSync()
    IfFlagEnabled(0, 11815396)
    IfFlagDisabled(1, 11815390)
    IfCharacterOutsideRegion(1, PLAYER, region=1812990)
    IfCharacterDead(2, 1810800)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11815396)
    DisableSoundEvent(sound_id=1813800)
    DisableBossHealthBar(1810800, name=2232, slot=0)
    Restart()


@RestartOnRest(11810310)
def Event_11810310():
    """Event 11810310"""
    EndIfFlagEnabled(11810314)
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(16)
    DisableObject(1811990)
    DeleteVFX(vfx_id=1811991, erase_root_only=False)
    DisableHealthBar(1810800)
    DisableAI(1810800)
    SetStandbyAnimationSettings(1810800, standby_animation=9000)
    Move(1810800, destination=1812305, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterInsideRegion(0, PLAYER, region=1812996)
    EnableFlag(11810314)
    AddSpecialEffect(1810800, 4160)
    SetStandbyAnimationSettings(1810800)
    ForceAnimation(1810800, 9060, wait_for_completion=True)
    CancelSpecialEffect(1810800, 4160)
    SetNest(1810800, region=1812300)
    EnableObject(1811990)
    CreateVFX(vfx_id=1811991)


@NeverRestart(11810311)
def Event_11810311():
    """Event 11810311"""
    IfFlagDisabled(1, 16)
    IfFlagDisabled(1, 11815390)
    IfFlagDisabled(1, 11810315)
    IfCharacterInsideRegion(1, PLAYER, region=1812996)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810315)
    DisableFlag(11810112)
    ForceAnimation(1811111, 3)
    ForceAnimation(1811115, 1, wait_for_completion=True)


@NeverRestart(11810312)
def Event_11810312():
    """Event 11810312"""
    IfFlagDisabled(1, 16)
    IfFlagEnabled(1, 11810315)
    IfStandingOnCollision(1, 1813120)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11810315)
    EnableFlag(11810312)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SetRespawnPoint(respawn_point=1812961)
    SaveRequest()
    EnableMapCollision(collision=1813121)
    ForceAnimation(1811115, 3, wait_for_completion=True)
    DisableMapCollision(collision=1813121)


@NeverRestart(11810313)
def Event_11810313():
    """Event 11810313"""
    DisableNetworkSync()
    IfFlagDisabled(1, 16)
    IfFlagEnabled(1, 11810312)
    IfFlagEnabled(1, 61810105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1811111,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010160, anchor_entity=1811111, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11815380)
def Event_11815380():
    """Event 11815380"""
    IfFlagDisabled(1, 11810900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1812898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=0,
    )
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1812897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1810810)
    Restart()


@RestartOnRest(11815382)
def Event_11815382():
    """Event 11815382"""
    SkipLinesIfFlagDisabled(4, 11810900)
    DisableCharacter(1810810)
    Kill(1810810)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=1811141)
    End()
    DisableAI(1810810)
    EnableInvincibility(1810810)
    DisableHealthBar(1810810)
    IfCharacterInsideRegion(0, PLAYER, region=1812896)
    EnableAI(1810810)
    DisableInvincibility(1810810)
    EnableBossHealthBar(1810810, name=2231, slot=0)
    EnableObject(1811890)
    CreateVFX(vfx_id=1811891)


@NeverRestart(11810900)
def Event_11810900():
    """Event 11810900"""
    IfCharacterDead(0, 1810810)
    KillBoss(game_area_param_id=1810810)
    DisableObject(1811890)
    DeleteVFX(vfx_id=1811891)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=1811141)


@NeverRestart(11815384)
def Event_11815384():
    """Event 11815384"""
    DisableNetworkSync()
    IfFlagEnabled(1, 16)
    IfFlagEnabled(1, 11815382)
    IfCharacterInsideRegion(1, PLAYER, region=1812890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1813801)


@NeverRestart(11815385)
def Event_11815385():
    """Event 11815385"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11815384)
    IfFlagEnabled(1, 11810900)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1813801)


@NeverRestart(11810000)
def Event_11810000():
    """Event 11810000"""
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=1812000)
    DisableBackread(1810800)
    IssuePrefetchRequest(request_id=0)
    WaitFrames(frames=1)
    PlayCutscene(180125, cutscene_flags=0, player_id=10000)
    PlayCutscene(100225, cutscene_flags=0, player_id=10000, move_to_region=1022100, game_map=FIRELINK_SHRINE)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, 16)
    EnableBackread(1810800)
    EnableFlag(11810000)
    SetRespawnPoint(respawn_point=1022960)
    SaveRequest()
    AwardAchievement(achievement_id=28)


@NeverRestart(11810150)
def Event_11810150():
    """Event 11810150"""
    SkipLinesIfFlagEnabled(3, 11810000)
    DisableObject(1811300)
    IfFlagEnabled(0, 11810000)
    EnableObject(1811300)
    IfActionButton(
        0,
        prompt_text=10010506,
        anchor_entity=1812001,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    )
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    SkipLinesIfMultiplayer(6)
    SetStandbyAnimationSettings(PLAYER)
    PlayCutscene(180126, cutscene_flags=0, player_id=10000, move_to_region=1022121, game_map=FIRELINK_SHRINE)
    PlayCutscene(100226, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=28)
    Restart()
    IfActionButton(
        1,
        prompt_text=10010507,
        anchor_entity=1812001,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    )
    IfCharacterOutsideRegion(2, PLAYER, region=1812001)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


@NeverRestart(11810100)
def Event_11810100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11810100"""
    SkipLinesIfThisEventSlotFlagDisabled(5)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)
    End()
    SkipLinesIfClient(4)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    SkipLinesIfEqual(1, left=arg_8_11, right=0)
    DisplayDialog(text=arg_8_11, anchor_entity=arg_4_7, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)


@NeverRestart(11810120)
def Event_11810120():
    """Event 11810120"""
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=1812020)
    IfFlagEnabled(2, 11810105)
    IfCharacterInsideRegion(2, PLAYER, region=1812021)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11810110)
def Event_11810110():
    """Event 11810110"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableObjectActivation(1811110, obj_act_id=-1)
    EndOfAnimation(obj=1811110, animation_id=1)
    End()
    IfObjectActivated(0, obj_act_id=11810110)
    EnableFlag(11810110)
    EndIfClient()
    DisplayDialog(text=10010870, anchor_entity=1811110, button_type=ButtonType.Yes_or_No)


@NeverRestart(11810111)
def Event_11810111():
    """Event 11810111"""
    IfObjectActivated(0, obj_act_id=11810111)
    EnableFlag(11810112)
    Restart()


@NeverRestart(11810211)
def Event_11810211():
    """Event 11810211"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableObject(1811215)
    EndOfAnimation(obj=1811216, animation_id=0)
    End()
    DisableObject(1811216)
    DisableObject(1811217)
    IfCharacterInsideRegion(0, PLAYER, region=1812120)
    CreateHazard(
        obj_flag=11810212,
        obj=1811215,
        model_point=1,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=2.5,
        repetition_time=0.0,
    )
    ForceAnimation(1811215, 0, wait_for_completion=True)
    DisableObject(1811215)
    EnableObject(1811216)
    EndOfAnimation(obj=1811216, animation_id=0)
    EnableObject(1811217)


@NeverRestart(11810200)
def Event_11810200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11810200"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    DisableObject(arg_0_3)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    End()
    DisableObject(arg_4_7)
    IfObjectDestroyed(0, arg_0_3)
    DisableObject(arg_0_3)
    EnableObject(arg_4_7)
    DestroyObject(arg_4_7)
    DisableObject(arg_8_11)


@NeverRestart(11810400)
def Event_11810400(
    _,
    arg_0_0: uchar,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_18_18: uchar,
    arg_19_19: uchar,
):
    """Event 11810400"""
    IfPlayerClass(1, arg_0_0)
    EndIfConditionFalse(1)
    DisableSoapstoneMessage(1813200)
    DisableSoapstoneMessage(1813201)
    DisableSoapstoneMessage(1813202)
    DisableSoapstoneMessage(1813203)
    DisableSoapstoneMessage(1813204)
    DisableTreasure(obj=1811601)
    DisableTreasure(obj=1811602)
    DisableTreasure(obj=1811603)
    DisableTreasure(obj=1811604)
    DisableTreasure(obj=1811605)
    DisableTreasure(obj=1811606)
    DisableTreasure(obj=1811607)
    DisableTreasure(obj=1811608)
    DisableTreasure(obj=1811609)
    DisableTreasure(obj=1811610)
    DisableTreasure(obj=1811611)
    DisableTreasure(obj=1811612)
    DisableTreasure(obj=1811613)
    DisableTreasure(obj=1811614)
    DisableTreasure(obj=1811615)
    DisableTreasure(obj=1811616)
    DisableTreasure(obj=1811617)
    DisableTreasure(obj=1811618)
    DisableTreasure(obj=1811619)
    DisableTreasure(obj=1811620)
    DisableTreasure(obj=1811621)
    DisableTreasure(obj=1811622)
    DisableTreasure(obj=1811623)
    DisableTreasure(obj=1811624)
    DisableObject(1811601)
    DisableObject(1811602)
    DisableObject(1811603)
    DisableObject(1811604)
    DisableObject(1811605)
    DisableObject(1811606)
    DisableObject(1811607)
    DisableObject(1811608)
    DisableObject(1811609)
    DisableObject(1811610)
    DisableObject(1811611)
    DisableObject(1811612)
    DisableObject(1811613)
    DisableObject(1811614)
    DisableObject(1811615)
    DisableObject(1811616)
    DisableObject(1811617)
    DisableObject(1811618)
    DisableObject(1811619)
    DisableObject(1811620)
    DisableObject(1811621)
    DisableObject(1811622)
    DisableObject(1811623)
    DisableObject(1811624)
    SetSoapstoneMessageState(1813200, arg_16_16)
    SetSoapstoneMessageState(1813201, arg_17_17)
    SetSoapstoneMessageState(1813202, arg_18_18)
    SetSoapstoneMessageState(1813203, arg_18_18)
    SetSoapstoneMessageState(1813204, arg_19_19)
    EnableObject(arg_4_7)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    EnableTreasure(obj=arg_4_7)
    EnableTreasure(obj=arg_8_11)
    EnableTreasure(obj=arg_12_15)


@NeverRestart(11810450)
def Event_11810450():
    """Event 11810450"""
    EndIfThisEventFlagEnabled()
    DisableSoapstoneMessage(1813220)
    DisableSoapstoneMessage(1813221)
    IfFlagEnabled(-1, 11810590)
    IfFlagEnabled(-1, 50000082)
    IfConditionTrue(0, input_condition=-1)
    EnableSoapstoneMessage(1813220)
    EnableSoapstoneMessage(1813221)


@NeverRestart(11810220)
def Event_11810220():
    """Event 11810220"""
    SkipLinesIfThisEventFlagDisabled(4)
    DisableFlag(11810220)
    RestoreObject(1811200)
    RestoreObject(1811201)
    RestoreObject(1811202)
    DisableObject(1811201)
    IfFlagEnabled(1, 11810000)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1812400)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810220)
    DisableObject(1811200)
    EnableObject(1811201)
    DestroyObject(1811201)
    DisableObject(1811202)
    PlaySoundEffect(anchor_entity=1811200, sound_id=851000000, sound_type=SoundType.o_Object)
    CreateTemporaryVFX(vfx_id=180100, anchor_entity=1811200, anchor_type=CoordEntityType.Object)


@NeverRestart(11810320)
def Event_11810320():
    """Event 11810320"""
    EndIfFlagEnabled(11810000)
    EnableInvincibility(1810810)
    IfCharacterBackreadEnabled(0, 1810810)
    AICommand(1810810, command_id=10, slot=0)
    IfFlagEnabled(0, 11810000)
    DisableInvincibility(1810810)
    IfCharacterBackreadEnabled(0, 1810810)
    AICommand(1810810, command_id=-1, slot=0)


@NeverRestart(11810300)
def Event_11810300():
    """Event 11810300"""
    EndIfClient()
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(16)
    SkipLinesIfFlagEnabled(3, 11810301)
    EnableFlag(50000081)
    EnableFlag(50001661)
    EnableFlag(11810301)
    IfFlagDisabled(1, 16)
    IfFlagDisabled(1, 11810090)
    IfHealthLessThanOrEqual(1, 1810800, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(50000081)
    DisableFlag(50001661)
    EnableFlag(50001660)


@RestartOnRest(11810850)
def Event_11810850(_, arg_0_3: int, arg_4_7: int):
    """Event 11810850"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


@RestartOnRest(11810350)
def Event_11810350():
    """Event 11810350"""
    SkipLinesIfFlagEnabled(32, 11810000)
    DisableObject(1811650)
    DisableCharacter(1810200)
    DisableCharacter(1810201)
    DisableCharacter(1810202)
    DisableCharacter(1810203)
    DisableCharacter(1810204)
    DisableCharacter(1810205)
    DisableCharacter(1810206)
    DisableCharacter(1810207)
    DisableCharacter(1810208)
    DisableCharacter(1810209)
    DisableCharacter(1810210)
    DisableCharacter(1810211)
    DisableCharacter(1810212)
    DisableCharacter(1810213)
    IfFlagEnabled(0, 11810000)
    DisableFlag(11810211)
    EnableCharacter(1810200)
    EnableCharacter(1810201)
    EnableCharacter(1810202)
    EnableCharacter(1810203)
    EnableCharacter(1810204)
    EnableCharacter(1810205)
    EnableCharacter(1810206)
    EnableCharacter(1810207)
    EnableCharacter(1810208)
    EnableCharacter(1810209)
    EnableCharacter(1810210)
    EnableCharacter(1810211)
    EnableCharacter(1810212)
    EnableCharacter(1810213)
    EnableObject(1811650)
    EnableTreasure(obj=1811650)
    DisableObject(1811600)
    DisableCharacter(1810101)
    DisableCharacter(1810102)
    DisableCharacter(1810103)
    DisableCharacter(1810104)
    DisableCharacter(1810106)
    DisableCharacter(1810107)
    DisableCharacter(1810108)
    DisableCharacter(1810110)
    DisableCharacter(1810111)
    DisableCharacter(1810112)
    DisableCharacter(1810113)


@NeverRestart(11810600)
def Event_11810600():
    """Event 11810600"""
    IfFlagEnabled(1, 11815200)
    IfFlagEnabled(2, 11815201)
    IfFlagEnabled(3, 11815202)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, condition=1)
    EnableFlag(11815100)
    DisableFlag(11815101)
    DisableFlag(11815102)
    DisableFlagRange((11815200, 11815202))
    Restart()
    SkipLinesIfFinishedConditionFalse(6, condition=3)
    DisableFlag(11815100)
    DisableFlag(11815101)
    EnableFlag(11815102)
    DisableFlag(71810093)
    DisableFlagRange((11815200, 11815202))
    Restart()
    DisableFlag(11815100)
    EnableFlag(11815101)
    DisableFlag(11815102)
    DisableFlag(71810092)
    DisableFlagRange((11815200, 11815202))
    Restart()


@NeverRestart(11810641)
def Event_11810641(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11810641"""
    IfAnyItemDroppedInRegion(0, region=1812200)
    IfItemDropped(2, item=arg_4_7, item_type=arg_0_3)
    SkipLinesIfConditionTrue(2, 2)
    EnableFlag(11815201)
    Restart()
    SkipLinesIfFlagEnabled(3, arg_12_15)
    EnableFlag(11815200)
    SetNextSnugglyTrade(flag=arg_8_11)
    Restart()
    EnableFlag(11815202)
    Restart()


@NeverRestart(11815110)
def Event_11815110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11815110"""
    EndIfFlagDisabled(arg_0_3)
    EndIfFlagEnabled(arg_8_11)
    WaitFrames(frames=1)
    SnugglyItemDrop(item_lot=arg_4_7, region=1812201, flag=arg_0_3, collision=1813102)


@NeverRestart(11815150)
def Event_11815150():
    """Event 11815150"""
    IfTimeElapsed(0, seconds=1.0)
    EnableFlag(11815151)


@NeverRestart(11810050)
def Event_11810050():
    """Event 11810050"""
    IfPlayerCovenant(1, Covenant.DarkmoonBlade)
    EndIfConditionFalse(1)
    EnableFlag(71510036)
    EnableFlag(71510037)


@NeverRestart(11810510)
def Event_11810510(_, arg_0_3: int, arg_4_7: int):
    """Event 11810510"""
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, 703)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11810520)
def Event_11810520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11810520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11810530)
def Event_11810530(_, arg_0_3: int):
    """Event 11810530"""
    IfFlagEnabled(1, 1060)
    IfFlagEnabled(-2, 11810590)
    IfFlagEnabled(-2, 11810591)
    IfFlagEnabled(-2, 11810592)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=1812121)
    IfCharacterInsideRegion(-3, PLAYER, region=1812990)
    IfConditionTrue(1, input_condition=-3)
    IfThisEventFlagDisabled(1)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    Kill(arg_0_3, award_souls=True)


@NeverRestart(11810531)
def Event_11810531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11810531"""
    IfFlagEnabled(1, 1073)
    IfFlagEnabled(1, 11810000)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11810532)
def Event_11810532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11810532"""
    SkipLinesIfThisEventFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagEnabled(1, 1061)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.0)
    IfInsideMap(1, game_map=UNDEAD_ASYLUM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@RestartOnRest(11815010)
def Event_11815010():
    """Event 11815010"""
    EndIfThisEventFlagEnabled()
    AddSpecialEffect(6023, 5492)
    DisableHealthBar(6023)
    WaitFrames(frames=5)
    EnableHealthBar(6023)
