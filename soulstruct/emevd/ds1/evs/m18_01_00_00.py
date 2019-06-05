"""
linked:


strings:

"""
from soulstruct.emevd.ds1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11810992, obj=1811960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11810984, obj=1811961, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11810010, stop_climbing_flag=11810011, obj=1811140)
    DisableHitbox(1813121)
    DisableFlag(11810315)
    DisableFlag(11810112)
    DisableObjectActivation(1811100, obj_act_id=-1)
    DisableObjectActivation(1811101, obj_act_id=-1)
    DisableObjectActivation(1811102, obj_act_id=-1)
    SkipLinesIfOutsideMap(4, game_map=UNDEAD_ASYLUM)
    SkipLinesIfFlagOn(3, 11810002)
    PlayCutscene(180101, skippable=True, fade_out=True, player_id=PLAYER, move_to_region=1812011, move_to_map=UNDEAD_ASYLUM)
    EnableFlag(11810002)
    SetRespawnPoint(1812900)
    RunEvent(11810090, slot=0, args=(1811700, 1811701, 1812600, 1812601))
    RunEvent(11810000)
    RunEvent(11810150)
    RunEvent(11810211)
    RunEvent(11810200, slot=1, args=(1811210, 1811211, 1811212))
    RunEvent(11810310)
    RunEvent(11810311)
    RunEvent(11810312)
    RunEvent(11810313)
    RunEvent(11810120)
    RunEvent(11810110)
    RunEvent(11810111)
    RunEvent(11810450)
    RunEvent(11810320)
    RunEvent(11810300)
    RunEvent(11810850, slot=0, args=(1810200, 27907000))
    RunEvent(11810850, slot=1, args=(1810213, 27907000))
    SkipLinesIfClient(44)
    RunEvent(11810641, slot=0, args=(3, 111, 11810601, 51810800))
    RunEvent(11810641, slot=1, args=(3, 270, 11810602, 51810810))
    RunEvent(11810641, slot=2, args=(3, 271, 11810603, 51810820))
    RunEvent(11810641, slot=3, args=(3, 272, 11810604, 51810830))
    RunEvent(11810641, slot=4, args=(3, 275, 11810605, 51810840))
    RunEvent(11810641, slot=5, args=(3, 293, 11810606, 51810850))
    RunEvent(11810641, slot=6, args=(3, 350, 11810607, 51810860))
    RunEvent(11810641, slot=7, args=(3, 500, 11810607, 51810860))
    RunEvent(11810641, slot=8, args=(3, 370, 11810608, 51810870))
    RunEvent(11810641, slot=9, args=(3, 375, 11810609, 51810880))
    RunEvent(11810641, slot=10, args=(3, 376, 11810610, 51810890))
    RunEvent(11810641, slot=11, args=(3, 380, 11810611, 51810900))
    RunEvent(11810641, slot=12, args=(3, 385, 11810612, 51810910))
    RunEvent(11810641, slot=13, args=(3, 501, 11810613, 51810920))
    RunEvent(11810641, slot=14, args=(0, 1330000, 11810614, 51810930))
    RunEvent(11810641, slot=15, args=(0, 1332000, 11810615, 51810940))
    RunEvent(11810641, slot=16, args=(0, 1396000, 11810616, 51810950))
    RunEvent(11810641, slot=17, args=(1, 190000, 11810617, 51810960))
    RunEvent(11810641, slot=18, args=(1, 290000, 11810618, 51810970))
    RunEvent(11810641, slot=19, args=(1, 560000, 11810619, 51810980))
    RunEvent(11810641, slot=20, args=(2, 130, 11810620, 51810990))
    RunEvent(11810641, slot=21, args=(3, 711, 11810621, 51811000))
    RunEvent(11810600)
    RunEvent(11815110, slot=0, args=(11810601, 3000, 51810800))
    RunEvent(11815110, slot=1, args=(11810602, 3010, 51810810))
    RunEvent(11815110, slot=2, args=(11810603, 3020, 51810820))
    RunEvent(11815110, slot=3, args=(11810604, 3030, 51810830))
    RunEvent(11815110, slot=4, args=(11810605, 3040, 51810840))
    RunEvent(11815110, slot=5, args=(11810606, 3050, 51810850))
    RunEvent(11815110, slot=6, args=(11810607, 3060, 51810860))
    RunEvent(11815110, slot=7, args=(11810608, 3070, 51810870))
    RunEvent(11815110, slot=8, args=(11810609, 3080, 51810880))
    RunEvent(11815110, slot=9, args=(11810610, 3090, 51810890))
    RunEvent(11815110, slot=10, args=(11810611, 3100, 51810900))
    RunEvent(11815110, slot=11, args=(11810612, 3110, 51810910))
    RunEvent(11815110, slot=12, args=(11810613, 3120, 51810920))
    RunEvent(11815110, slot=13, args=(11810614, 3130, 51810930))
    RunEvent(11815110, slot=14, args=(11810615, 3140, 51810940))
    RunEvent(11815110, slot=15, args=(11810616, 3150, 51810950))
    RunEvent(11815110, slot=16, args=(11810617, 3160, 51810960))
    RunEvent(11815110, slot=17, args=(11810618, 3170, 51810970))
    RunEvent(11815110, slot=18, args=(11810619, 3180, 51810980))
    RunEvent(11815110, slot=19, args=(11810620, 3190, 51810990))
    RunEvent(11815110, slot=20, args=(11810621, 3200, 51811000))
    RunEvent(11810100, slot=0, args=(11810100, 1811100, 10010869))
    RunEvent(11810100, slot=1, args=(11810101, 1811101, 10010869))
    RunEvent(11810100, slot=2, args=(11810102, 1811102, 10010869))
    RunEvent(11810100, slot=3, args=(11810103, 1811103, 10010869))
    RunEvent(11810100, slot=4, args=(11810104, 1811104, 10010875))
    RunEvent(11810100, slot=5, args=(11810105, 1811105, 0))
    RunEvent(11810100, slot=6, args=(11810106, 1811106, 10010871))
    RunEvent(11815150)
    RunEvent(11810400, slot=0, args=(0, 1811601, 1811602, 1811602, 0, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=1, args=(1, 1811603, 1811604, 1811604, 0, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=2, args=(2, 1811605, 1811606, 1811606, 0, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=3, args=(3, 1811607, 1811608, 1811608, 0, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=4, args=(4, 1811609, 1811610, 1811610, 0, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=5, args=(5, 1811611, 1811612, 1811613, 0, 0, 1, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=6, args=(6, 1811614, 1811615, 1811616, 1, 0, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=7, args=(7, 1811617, 1811618, 1811619, 0, 1, 0, 0), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=8, args=(8, 1811620, 1811621, 1811622, 0, 0, 0, 1), arg_types='BiiiBBBB')
    RunEvent(11810400, slot=9, args=(9, 1811623, 1811624, 1811624, 0, 0, 0, 0), arg_types='BiiiBBBB')
    DisableMapSound(1813800)
    SkipLinesIfFlagOn(2, 11810312)
    DisableFlag(11810310)
    DisableFlag(11810314)
    SkipLinesIfFlagOff(1, 61810105)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SkipLinesIfFlagOff(7, 16)
    RunEvent(11815392)
    DisableObject(1811990)
    DeleteFX(1811991, erase_root_only=False)
    EndOfAnimation(1811115, 1)
    EndOfAnimation(1811111, 1)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SkipLines(6)
    RunEvent(11815390)
    RunEvent(11815393)
    RunEvent(11815392)
    RunEvent(11810001)
    RunEvent(11815394)
    RunEvent(11815395)
    DisableObject(1811890)
    DeleteFX(1811891, erase_root_only=False)
    DisableMapSound(1813801)
    EndIfFlagOff(11810000)
    SkipLinesIfFlagOff(2, 11810900)
    RunEvent(11815382)
    SkipLines(4)
    RunEvent(11815382)
    RunEvent(11810900)
    RunEvent(11815384)
    RunEvent(11815385)


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfClient(11)
    SkipLinesIfFlagOn(10, 705)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    SkipLinesIfConditionFalse(8, 1)
    EnableFlag(705)
    EnableFlag(50000082)
    SetRespawnPoint(1812900)
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    RunEvent(11810050)
    RunEvent(11810350)
    RunEvent(11810220)
    HumanityRegistration(6023, 8326)
    SkipLinesIfFlagOn(1, 1061)
    DisableCharacter(6024)
    SetTeamType(6024, TeamType.HostileAlly)
    RunEvent(11810520, slot=0, args=(6023, 1060, 1074, 1073))
    RunEvent(11810530, slot=0, args=(6023,))
    RunEvent(11810531, slot=0, args=(6024, 1060, 1074, 1061))
    RunEvent(11810532, slot=0, args=(6024, 1060, 1074, 1062))
    RunEvent(11815010)


@NeverRestart
def Event11810090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11810090: Event 11810090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=ARG_8_11, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=ARG_12_15, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)


@RestartOnRest
def Event11815090():
    """ 11815090: Event 11815090 """
    DisableCharacter(1810900)
    IfFlagOn(0, 11810000)
    IfBlackWorldTendencyComparison(-1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfFlagOn(-1, 11815090)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11815090)
    EnableCharacter(1810900)
    IfBlackWorldTendencyComparison(0, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    Kill(1810900, award_souls=False)


@NeverRestart
def Event11815390():
    """ 11815390: Event 11815390 """
    IfFlagOff(1, 16)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1812998, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1811990)
    IfConditionTrue(0, input_condition=1)
    Move(1810800, destination=1812301, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    RotateToFaceEntity(PLAYER, 1812997)
    ForceAnimation(PLAYER, 7410)
    DisableDeveloperMessage(1813210)
    ForceAnimation(1811115, 3)
    SkipLinesIfFlagOff(1, 11810112)
    ForceAnimation(1811111, 3)
    Restart()


@NeverRestart
def Event11815393():
    """ 11815393: Event 11815393 """
    SkipLinesIfThisEventOn(5)
    IfFlagOff(1, 16)
    IfCharacterInsideRegion(-1, PLAYER, region=1812996)
    IfCharacterInsideRegion(-1, PLAYER, region=1812350)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1810800)


@RestartOnRest
def Event11815392():
    """ 11815392: Event 11815392 """
    SkipLinesIfFlagOff(3, 16)
    DisableCharacter(1810800)
    Kill(1810800, award_souls=False)
    End()
    IfFlagOff(1, 11810310)
    IfCharacterInsideRegion(1, PLAYER, region=1812996)
    IfFlagOn(2, 11810310)
    IfCharacterInsideRegion(2, PLAYER, region=1812990)
    IfFlagOn(3, 11815393)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1810800)


@NeverRestart
def Event11810001():
    """ 11810001: Event 11810001 """
    IfHealthLessThanOrEqual(0, 1810800, 0.0)
    PlaySoundEffect(anchor_entity=1810800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1810800)
    EnableFlag(16)
    KillBoss(1810800)
    DisableObject(1811990)
    DeleteFX(1811991, erase_root_only=True)
    ForceAnimation(1811111, 1)
    SkipLinesIfFlagOff(1, 11810312)
    ForceAnimation(1811115, 1)
    DisableObjectActivation(1811111, obj_act_id=-1)


@NeverRestart
def Event11815394():
    """ 11815394: Event 11815394 """
    DisableNetworkSync()
    IfFlagOff(0, 11815396)
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810310)
    IfFlagOn(1, 11815392)
    IfCharacterInsideRegion(-1, PLAYER, region=1812990)
    IfCharacterInsideRegion(-1, PLAYER, region=1812350)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11815396)
    EnableMapSound(1813800)
    EnableBossHealthBar(1810800, name=2232, slot=0)
    Restart()


@NeverRestart
def Event11815395():
    """ 11815395: Event 11815395 """
    DisableNetworkSync()
    IfFlagOn(0, 11815396)
    IfFlagOff(1, 11815390)
    IfCharacterOutsideRegion(1, PLAYER, region=1812990)
    IfCharacterDead(2, 1810800)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11815396)
    DisableMapSound(1813800)
    DisableBossHealthBar(1810800, name=2232, slot=0)
    Restart()


@RestartOnRest
def Event11810310():
    """ 11810310: Event 11810310 """
    EndIfFlagOn(11810314)
    EndIfThisEventOn()
    EndIfFlagOn(16)
    DisableObject(1811990)
    DeleteFX(1811991, erase_root_only=False)
    DisableHealthBar(1810800)
    DisableAI(1810800)
    SetStandbyAnimationSettings(1810800, standby_animation=9000)
    Move(1810800, destination=1812305, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    IfCharacterInsideRegion(0, PLAYER, region=1812996)
    EnableFlag(11810314)
    AddSpecialEffect(1810800, 4160)
    ResetStandbyAnimationSettings(1810800)
    ForceAnimation(1810800, 9060, wait_for_completion=True)
    CancelSpecialEffect(1810800, 4160)
    SetNest(1810800, 1812300)
    EnableObject(1811990)
    CreateFX(1811991)


@NeverRestart
def Event11810311():
    """ 11810311: Event 11810311 """
    IfFlagOff(1, 16)
    IfFlagOff(1, 11815390)
    IfFlagOff(1, 11810315)
    IfCharacterInsideRegion(1, PLAYER, region=1812996)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810315)
    DisableFlag(11810112)
    ForceAnimation(1811111, 3)
    ForceAnimation(1811115, 1, wait_for_completion=True)


@NeverRestart
def Event11810312():
    """ 11810312: Event 11810312 """
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810315)
    IfStandingOnHitbox(1, 1813120)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11810315)
    EnableFlag(11810312)
    DisableObjectActivation(1811111, obj_act_id=-1)
    SetRespawnPoint(1812961)
    SaveRequest()
    EnableHitbox(1813121)
    ForceAnimation(1811115, 3, wait_for_completion=True)
    DisableHitbox(1813121)


@NeverRestart
def Event11810313():
    """ 11810313: Event 11810313 """
    DisableNetworkSync()
    IfFlagOff(1, 16)
    IfFlagOn(1, 11810312)
    IfFlagOn(1, 61810105)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1811111, anchor_type=MapEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010160, anchor_entity=1811111, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11815380():
    """ 11815380: Event 11815380 """
    IfFlagOff(1, 11810900)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1812898, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=0, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, 1812897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1810810)
    Restart()


@RestartOnRest
def Event11815382():
    """ 11815382: Event 11815382 """
    SkipLinesIfFlagOff(4, 11810900)
    DisableCharacter(1810810)
    Kill(1810810, award_souls=False)
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
    CreateFX(1811891)


@NeverRestart
def Event11810900():
    """ 11810900: Event 11810900 """
    IfCharacterDead(0, 1810810)
    KillBoss(1810810)
    DisableObject(1811890)
    DeleteFX(1811891, erase_root_only=True)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=1811141)


@NeverRestart
def Event11815384():
    """ 11815384: Event 11815384 """
    DisableNetworkSync()
    IfFlagOn(1, 16)
    IfFlagOn(1, 11815382)
    IfCharacterInsideRegion(1, PLAYER, region=1812890)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1813801)


@NeverRestart
def Event11815385():
    """ 11815385: Event 11815385 """
    DisableNetworkSync()
    IfFlagOn(1, 11815384)
    IfFlagOn(1, 11810900)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1813801)


@NeverRestart
def Event11810000():
    """ 11810000: Event 11810000 """
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=1812000)
    DisableBackread(1810800)
    IssuePrefetchRequest(0)
    WaitFrames(1)
    PlayCutscene(180125, skippable=True, fade_out=False, player_id=PLAYER)
    PlayCutscene(100225, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1022100, move_to_map=FIRELINK_SHRINE)
    WaitFrames(1)
    SkipLinesIfFlagOn(1, 16)
    EnableBackread(1810800)
    EnableFlag(11810000)
    SetRespawnPoint(1022960)
    SaveRequest()
    AwardAchievement(28)


@NeverRestart
def Event11810150():
    """ 11810150: Event 11810150 """
    SkipLinesIfFlagOn(3, 11810000)
    DisableObject(1811300)
    IfFlagOn(0, 11810000)
    EnableObject(1811300)
    IfDialogPromptActivated(0, prompt_text=10010506, anchor_entity=1812001, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False)
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    SkipLinesIfMultiplayer(6)
    ResetStandbyAnimationSettings(PLAYER)
    PlayCutscene(180126, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1022121, move_to_map=FIRELINK_SHRINE)
    PlayCutscene(100226, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(28)
    Restart()
    IfDialogPromptActivated(1, prompt_text=10010507, anchor_entity=1812001, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False)
    IfCharacterOutsideRegion(2, PLAYER, region=1812001)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11810100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11810100: Event 11810100 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=3)
    End()
    SkipLinesIfClient(4)
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    EnableFlag(ARG_0_3)
    SkipLinesIfEqual(1, left=ARG_8_11, right=0)
    DisplayDialog(ARG_8_11, anchor_entity=ARG_4_7, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_4_7, obj_act_id=-1, relative_index=3)


@NeverRestart
def Event11810120():
    """ 11810120: Event 11810120 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=1812020)
    IfFlagOn(2, 11810105)
    IfCharacterInsideRegion(2, PLAYER, region=1812021)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart
def Event11810110():
    """ 11810110: Event 11810110 """
    SkipLinesIfThisEventOff(3)
    DisableObjectActivation(1811110, obj_act_id=-1)
    EndOfAnimation(1811110, 1)
    End()
    IfObjectActivated(0, obj_act_id=11810110)
    EnableFlag(11810110)
    EndIfClient()
    DisplayDialog(10010870, anchor_entity=1811110, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)


@NeverRestart
def Event11810111():
    """ 11810111: Event 11810111 """
    IfObjectActivated(0, obj_act_id=11810111)
    EnableFlag(11810112)
    Restart()


@NeverRestart
def Event11810211():
    """ 11810211: Event 11810211 """
    SkipLinesIfThisEventOff(3)
    DisableObject(1811215)
    EndOfAnimation(1811216, 0)
    End()
    DisableObject(1811216)
    DisableObject(1811217)
    IfCharacterInsideRegion(0, PLAYER, region=1812120)
    CreateHazard(11810212, 1811215, model_point=1, behavior_param_id=5110, target_type=DamageTargetType.Character, radius=0.800000011920929, life=2.5, repetition_time=0.0)
    ForceAnimation(1811215, 0, wait_for_completion=True)
    DisableObject(1811215)
    EnableObject(1811216)
    EndOfAnimation(1811216, 0)
    EnableObject(1811217)


@NeverRestart
def Event11810200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11810200: Event 11810200 """
    SkipLinesIfThisEventSlotOff(4)
    DisableObject(ARG_0_3)
    DisableObject(ARG_4_7)
    DisableObject(ARG_8_11)
    End()
    DisableObject(ARG_4_7)
    IfObjectDestroyed(0, ARG_0_3)
    DisableObject(ARG_0_3)
    EnableObject(ARG_4_7)
    DestroyObject(ARG_4_7, slot=1)
    DisableObject(ARG_8_11)


@NeverRestart
def Event11810400(ARG_0_0: uchar, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_16: uchar, ARG_17_17: uchar, ARG_18_18: uchar, ARG_19_19: uchar):
    """ 11810400: Event 11810400 """
    IfPlayerClass(1, ARG_0_0)
    EndIfConditionFalse(1)
    DisableDeveloperMessage(1813200)
    DisableDeveloperMessage(1813201)
    DisableDeveloperMessage(1813202)
    DisableDeveloperMessage(1813203)
    DisableDeveloperMessage(1813204)
    DisableTreasure(1811601)
    DisableTreasure(1811602)
    DisableTreasure(1811603)
    DisableTreasure(1811604)
    DisableTreasure(1811605)
    DisableTreasure(1811606)
    DisableTreasure(1811607)
    DisableTreasure(1811608)
    DisableTreasure(1811609)
    DisableTreasure(1811610)
    DisableTreasure(1811611)
    DisableTreasure(1811612)
    DisableTreasure(1811613)
    DisableTreasure(1811614)
    DisableTreasure(1811615)
    DisableTreasure(1811616)
    DisableTreasure(1811617)
    DisableTreasure(1811618)
    DisableTreasure(1811619)
    DisableTreasure(1811620)
    DisableTreasure(1811621)
    DisableTreasure(1811622)
    DisableTreasure(1811623)
    DisableTreasure(1811624)
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
    SetDeveloperMessageState(1813200, state=ARG_16_16)
    SetDeveloperMessageState(1813201, state=ARG_17_17)
    SetDeveloperMessageState(1813202, state=ARG_18_18)
    SetDeveloperMessageState(1813203, state=ARG_18_18)
    SetDeveloperMessageState(1813204, state=ARG_19_19)
    EnableObject(ARG_4_7)
    EnableObject(ARG_8_11)
    EnableObject(ARG_12_15)
    EnableTreasure(ARG_4_7)
    EnableTreasure(ARG_8_11)
    EnableTreasure(ARG_12_15)


@NeverRestart
def Event11810450():
    """ 11810450: Event 11810450 """
    EndIfThisEventOn()
    DisableDeveloperMessage(1813220)
    DisableDeveloperMessage(1813221)
    IfFlagOn(-1, 11810590)
    IfFlagOn(-1, 50000082)
    IfConditionTrue(0, input_condition=-1)
    EnableDeveloperMessage(1813220)
    EnableDeveloperMessage(1813221)


@NeverRestart
def Event11810220():
    """ 11810220: Event 11810220 """
    SkipLinesIfThisEventOff(4)
    DisableFlag(11810220)
    RestoreObject(1811200)
    RestoreObject(1811201)
    RestoreObject(1811202)
    DisableObject(1811201)
    IfFlagOn(1, 11810000)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1812400)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11810220)
    DisableObject(1811200)
    EnableObject(1811201)
    DestroyObject(1811201, slot=1)
    DisableObject(1811202)
    PlaySoundEffect(anchor_entity=1811200, sound_type=SoundType.o_Object, sound_id=851000000)
    CreateTemporaryFX(180100, anchor_entity=1811200, anchor_type=MapEntityType.Object, model_point=-1)


@NeverRestart
def Event11810320():
    """ 11810320: Event 11810320 """
    EndIfFlagOn(11810000)
    EnableInvincibility(1810810)
    IfCharacterBackreadEnabled(0, 1810810)
    AICommand(1810810, command_id=10, slot=0)
    IfFlagOn(0, 11810000)
    DisableInvincibility(1810810)
    IfCharacterBackreadEnabled(0, 1810810)
    AICommand(1810810, command_id=-1, slot=0)


@NeverRestart
def Event11810300():
    """ 11810300: Event 11810300 """
    EndIfClient()
    EndIfThisEventOn()
    EndIfFlagOn(16)
    SkipLinesIfFlagOn(3, 11810301)
    EnableFlag(50000081)
    EnableFlag(50001661)
    EnableFlag(11810301)
    IfFlagOff(1, 16)
    IfFlagOff(1, 11810090)
    IfHealthLessThanOrEqual(1, 1810800, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(50000081)
    DisableFlag(50001661)
    EnableFlag(50001660)


@RestartOnRest
def Event11810850(ARG_0_3: int, ARG_4_7: int):
    """ 11810850: Event 11810850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfCharacterDead(0, ARG_0_3)
    EndIfEqual(left=ARG_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(ARG_4_7, host_only=True)


@RestartOnRest
def Event11810350():
    """ 11810350: Event 11810350 """
    SkipLinesIfFlagOn(32, 11810000)
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
    IfFlagOn(0, 11810000)
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
    EnableTreasure(1811650)
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


@NeverRestart
def Event11810600():
    """ 11810600: Event 11810600 """
    IfFlagOn(1, 11815200)
    IfFlagOn(2, 11815201)
    IfFlagOn(3, 11815202)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, 1)
    EnableFlag(11815100)
    DisableFlag(11815101)
    DisableFlag(11815102)
    DisableFlagRange((11815200, 11815202))
    Restart()
    SkipLinesIfFinishedConditionFalse(6, 3)
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


@NeverRestart
def Event11810641(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11810641: Event 11810641 """
    IfAnyItemDroppedInRegion(0, 1812200)
    IfItemDropped(2, ARG_4_7, item_type=ARG_0_3)
    SkipLinesIfConditionTrue(2, 2)
    EnableFlag(11815201)
    Restart()
    SkipLinesIfFlagOn(3, ARG_12_15)
    EnableFlag(11815200)
    SetNextSnugglyTrade(ARG_8_11)
    Restart()
    EnableFlag(11815202)
    Restart()


@NeverRestart
def Event11815110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11815110: Event 11815110 """
    EndIfFlagOff(ARG_0_3)
    EndIfFlagOn(ARG_8_11)
    WaitFrames(1)
    SnugglyItemDrop(ARG_4_7, region=1812201, flag=ARG_0_3, hitbox=1813102)


@NeverRestart
def Event11815150():
    """ 11815150: Event 11815150 """
    IfTimeElapsed(0, 1.0)
    EnableFlag(11815151)


@NeverRestart
def Event11810050():
    """ 11810050: Event 11810050 """
    IfPlayerCovenant(1, Covenant.DarkmoonBlade)
    EndIfConditionFalse(1)
    EnableFlag(71510036)
    EnableFlag(71510037)


@NeverRestart
def Event11810510(ARG_0_3: int, ARG_4_7: int):
    """ 11810510: Event 11810510 """
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfFlagOn(2, ARG_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, ARG_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(ARG_0_3)
    IfFlagOn(0, 703)
    EnableFlag(ARG_4_7)
    SetTeamType(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11810520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11810520: Event 11810520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11810530(ARG_0_3: int):
    """ 11810530: Event 11810530 """
    IfFlagOn(1, 1060)
    IfFlagOn(-2, 11810590)
    IfFlagOn(-2, 11810591)
    IfFlagOn(-2, 11810592)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=1812121)
    IfCharacterInsideRegion(-3, PLAYER, region=1812990)
    IfConditionTrue(1, input_condition=-3)
    IfThisEventOff(1)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    Kill(ARG_0_3, award_souls=True)


@NeverRestart
def Event11810531(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11810531: Event 11810531 """
    IfFlagOn(1, 1073)
    IfFlagOn(1, 11810000)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11810532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11810532: Event 11810532 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfFlagOn(1, 1061)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.0)
    IfInsideMap(1, game_map=UNDEAD_ASYLUM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@RestartOnRest
def Event11815010():
    """ 11815010: Event 11815010 """
    EndIfThisEventOn()
    AddSpecialEffect(6023, 5492)
    DisableHealthBar(6023)
    WaitFrames(5)
    EnableHealthBar(6023)
