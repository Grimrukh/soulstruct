"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 13)
    RegisterBonfire(11600920, obj=1601950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11600984, obj=1601961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=1601140)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=1601141)
    EnableFlag(11600102)
    SkipLinesIfClient(7)
    EnableFlag(404)
    DisableObject(1601994)
    DeleteFX(1601995, erase_root_only=False)
    DisableObject(1601996)
    DeleteFX(1601997, erase_root_only=False)
    DisableObject(1601998)
    DeleteFX(1601999, erase_root_only=False)
    DisableSpawner(1603000)
    RunEvent(11600090, slot=0, args=(1601700, 1601701, 1602600, 1602601))
    RunEvent(11600090, slot=1, args=(1601702, 1601703, 1602602, 1602603))
    RunEvent(11605090)
    RunEvent(11605091)
    RunEvent(11605092)
    RunEvent(11605100)
    RunEvent(11600150)
    RunEvent(11600100)
    RunEvent(11600101, slot=0, args=(1601101, 11600102, 0))
    RunEvent(11600110, slot=0, args=(11600110, 10010872, 1601111))
    RunEvent(11600120, slot=0, args=(11600120, 10010867, 1601110, 10010883, 2008))
    RunEvent(11600160)
    RunEvent(11600200)
    RunEvent(11600250)
    RunEvent(11600199)
    RunEvent(11600210)
    RunEvent(11600251)
    RunEvent(11600220)
    RunEvent(11600252)
    RunEvent(11600230)
    RunEvent(11600253)
    RunEvent(11600810)
    RunEvent(11600400)
    RunEvent(11605397)
    RunEvent(11605398)
    RunEvent(11605360, slot=0, args=(10000,))
    RunEvent(11605360, slot=1, args=(10001,))
    RunEvent(11605360, slot=2, args=(10002,))
    RunEvent(11605360, slot=3, args=(10003,))
    RunEvent(11605360, slot=4, args=(10004,))
    RunEvent(11605360, slot=5, args=(10005,))
    DisableMapSound(1603800)
    SkipLinesIfFlagOff(4, 13)
    RunEvent(11605392)
    DisableObject(1601990)
    DeleteFX(1601991, erase_root_only=False)
    SkipLines(13)
    RunEvent(11605390)
    RunEvent(11605391)
    RunEvent(11605393)
    RunEvent(11605392)
    RunEvent(11600001)
    RunEvent(11605394)
    RunEvent(11605395)
    RunEvent(11605396)
    RunEvent(11605350, slot=0, args=(1600801,))
    RunEvent(11605350, slot=1, args=(1600802,))
    RunEvent(11605350, slot=2, args=(1600803,))
    RunEvent(11605350, slot=3, args=(1600804,))
    RunEvent(11605399)
    DisableMapSound(1603801)
    RunEvent(11605150, slot=0, args=(1600202, 1602850))
    RunEvent(11605150, slot=1, args=(1600204, 1602850))
    RunEvent(11605150, slot=2, args=(1600205, 1602850))
    RunEvent(11605150, slot=3, args=(1600211, 1602850))
    RunEvent(11605150, slot=4, args=(1600351, 1602850))
    RunEvent(11605150, slot=5, args=(1600356, 1602850))
    RunEvent(11605150, slot=6, args=(1600357, 1602850))
    RunEvent(11605150, slot=7, args=(1600250, 1602850))
    RunEvent(11605150, slot=8, args=(1600252, 1602851))
    RunEvent(11605150, slot=9, args=(1600253, 1602851))
    RunEvent(11605150, slot=10, args=(1600255, 1602851))
    RunEvent(11605150, slot=11, args=(1600200, 1602852))
    RunEvent(11605150, slot=12, args=(1600201, 1602852))
    RunEvent(11605150, slot=13, args=(1600206, 1602852))
    RunEvent(11605150, slot=14, args=(1600251, 1602852))
    RunEvent(11605150, slot=15, args=(1600254, 1602852))
    RunEvent(11605150, slot=16, args=(1600301, 1602852))
    RunEvent(11605150, slot=17, args=(1600302, 1602852))
    RunEvent(11605150, slot=18, args=(1600352, 1602852))
    RunEvent(11605150, slot=19, args=(1600353, 1602852))
    RunEvent(11605150, slot=20, args=(1600354, 1602852))
    RunEvent(11605150, slot=21, args=(1600360, 1602852))
    RunEvent(11605150, slot=22, args=(1600350, 1602853))
    RunEvent(11605150, slot=23, args=(1600355, 1602853))
    RunEvent(11605150, slot=24, args=(1600203, 1602853))
    RunEvent(11605150, slot=25, args=(1600207, 1602853))
    RunEvent(11605150, slot=26, args=(1600208, 1602853))
    RunEvent(11605150, slot=27, args=(1600209, 1602853))
    RunEvent(11605150, slot=28, args=(1600210, 1602853))
    RunEvent(11605150, slot=29, args=(1600358, 1602854))
    RunEvent(11605150, slot=30, args=(1600359, 1602854))
    RunEvent(11605150, slot=31, args=(1600361, 1602854))
    RunEvent(11605150, slot=32, args=(1600300, 1602860))
    RunEvent(11605150, slot=33, args=(1600310, 1602860))
    RunEvent(11605001, slot=0, args=(1600200, 5.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=1, args=(1600201, 5.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=2, args=(1600202, 7.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=3, args=(1600203, 7.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=4, args=(1600204, 6.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=5, args=(1600205, 6.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=6, args=(1600206, 3.0, 9060), arg_types='ifi')
    RunEvent(11605001, slot=7, args=(1600210, 5.0, 9060), arg_types='ifi')
    RunEvent(11605050, slot=0, args=(1600250, 1602250, 3007, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=1, args=(1600251, 1602251, 3007, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=2, args=(1600252, 1602252, 3006, 1, 5.0), arg_types='iiiif')
    RunEvent(11605050, slot=3, args=(1600253, 1602253, 3006, 1, 5.0), arg_types='iiiif')
    RunEvent(11605050, slot=4, args=(1600254, 1602254, 3005, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=5, args=(1600255, 1602255, 3005, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=6, args=(1600207, 1602270, 9060, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=7, args=(1600208, 1602270, 9060, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=8, args=(1600209, 1602270, 9060, 0, 0.0), arg_types='iiiif')
    RunEvent(11605050, slot=9, args=(1600211, 1602271, 9060, 0, 0.0), arg_types='iiiif')
    RunEvent(11605200, slot=0, args=(1600400, 1600410, 1, 11600100))
    RunEvent(11605200, slot=1, args=(1600400, 1600411, 2, 11605200))
    RunEvent(11605200, slot=2, args=(1600400, 1600412, 3, 11605201))
    RunEvent(11605200, slot=3, args=(1600400, 1600413, 4, 11605202))
    RunEvent(11605200, slot=4, args=(1600400, 1600414, 5, 11605203))
    RunEvent(11605200, slot=5, args=(1600400, 1600415, 6, 11605204))
    RunEvent(11605200, slot=10, args=(1600401, 1600416, 1, 11600100))
    RunEvent(11605200, slot=11, args=(1600401, 1600417, 2, 11605210))
    RunEvent(11605200, slot=12, args=(1600401, 1600418, 3, 11605211))
    RunEvent(11605200, slot=13, args=(1600401, 1600419, 4, 11605212))
    RunEvent(11605200, slot=14, args=(1600401, 1600420, 5, 11605213))
    RunEvent(11605200, slot=15, args=(1600401, 1600421, 6, 11605214))
    RunEvent(11605250, slot=0, args=(1600410,))
    RunEvent(11605250, slot=1, args=(1600411,))
    RunEvent(11605250, slot=2, args=(1600412,))
    RunEvent(11605250, slot=3, args=(1600413,))
    RunEvent(11605250, slot=4, args=(1600414,))
    RunEvent(11605250, slot=5, args=(1600415,))
    RunEvent(11605250, slot=6, args=(1600416,))
    RunEvent(11605250, slot=7, args=(1600417,))
    RunEvent(11605250, slot=8, args=(1600418,))
    RunEvent(11605250, slot=9, args=(1600419,))
    RunEvent(11605250, slot=10, args=(1600420,))
    RunEvent(11605250, slot=11, args=(1600421,))
    RunEvent(11600850, slot=0, args=(1600400,))
    RunEvent(11600850, slot=1, args=(1600401,))
    RunEvent(11600600, slot=0, args=(1601650, 11600600))
    RunEvent(11600600, slot=1, args=(1601651, 11600601))
    RunEvent(11600600, slot=2, args=(1601652, 11600602))
    RunEvent(11600650, slot=0, args=(1601610, 1601310))
    RunEvent(11600650, slot=1, args=(1601611, 1601311))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6520, 8932)
    RunEvent(11605030)
    RunEvent(11605032)
    RunEvent(11605033)
    HumanityRegistration(6180, 8406)
    SkipLinesIfFlagOn(2, 1315)
    SkipLinesIfFlagOn(1, 1313)
    SkipLines(1)
    DisableCharacter(6180)
    RunEvent(11600510, slot=0, args=(6180, 1314))
    RunEvent(11600520, slot=0, args=(6180, 1310, 1319, 1315))
    RunEvent(11600530, slot=0, args=(6180, 1310, 1319, 1311))
    RunEvent(11600531, slot=0, args=(6180, 1310, 1319, 1312))
    RunEvent(11600532, slot=0, args=(6180, 1310, 1319, 1313))
    HumanityRegistration(6220, 8414)
    RunEvent(11600510, slot=1, args=(6220, 1381))
    RunEvent(11600520, slot=1, args=(6220, 1380, 1399, 1382))
    SetTeamTypeAndExitStandbyAnimation(6271, TeamType.HostileAlly)
    SkipLinesIfFlagOn(1, 1464)
    DisableCharacter(6271)
    RunEvent(11600520, slot=5, args=(6271, 1460, 1489, 1462))
    RunEvent(11600545, slot=0, args=(6271,))
    SkipLinesIfFlagOff(2, 15)
    DisableCharacter(6340)
    SkipLinesIfFlagOn(11, 15)
    EnableImmortality(6340)
    SkipLinesIfFlagOn(2, 1677)
    SkipLinesIfFlagOn(1, 1676)
    SkipLines(1)
    DisableCharacter(6340)
    RunEvent(11600537, slot=0, args=(6340, 1670, 1678, 1671))
    RunEvent(11600538, slot=0, args=(6340, 1670, 1678, 1672))
    RunEvent(11600539, slot=0, args=(6340, 1670, 1678, 1673))
    RunEvent(11600540, slot=0, args=(6340, 1670, 1678, 1677))
    RunEvent(11600541, slot=0, args=(6340, 1670, 1678, 1677))
    RunEvent(11606200)


@NeverRestart
def Event11600090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600090: Event 11600090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=ARG_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=ARG_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)


@RestartOnRest
def Event11605090():
    """ 11605090: Event 11605090 """
    EndIfThisEventOn()
    DisableCharacter(1600900)
    DisableCharacter(1600901)
    DisableCharacter(1600902)
    DisableCharacter(1600903)
    DisableCharacter(1600904)
    DisableCharacter(1600905)
    IfFlagOn(0, 11600050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1600900)
    EnableCharacter(1600901)
    EnableCharacter(1600902)
    EnableCharacter(1600903)
    EnableCharacter(1600904)
    EnableCharacter(1600905)


@RestartOnRest
def Event11605091():
    """ 11605091: Event 11605091 """
    IfFlagOn(-1, 11605095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11600050)
    DisableFlag(11605095)
    EnableFlag(5001)
    Kill(1600900, award_souls=False)
    Kill(1600901, award_souls=False)
    Kill(1600902, award_souls=False)
    Kill(1600903, award_souls=False)
    Kill(1600904, award_souls=False)
    Kill(1600905, award_souls=False)


@RestartOnRest
def Event11605092():
    """ 11605092: Event 11605092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11600050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11600050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11600050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11600050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11600050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11600050)
    RestartIfConditionFalse(-6)
    EnableFlag(11600050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=NEW_LONDO_RUINS)
    RestartIfConditionFalse(7)
    DisableFlag(11600050)
    EnableFlag(11605095)


@NeverRestart
def Event11605390():
    """ 11605390: Event 11605390 """
    IfFlagOff(1, 13)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1602998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1601990, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11605391():
    """ 11605391: Event 11605391 """
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1602998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1601990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11605393():
    """ 11605393: Event 11605393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605390)
    IfCharacterInsideRegion(1, PLAYER, region=1602996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1600800)
    ActivateMultiplayerBuffs(1600801)
    ActivateMultiplayerBuffs(1600802)
    ActivateMultiplayerBuffs(1600803)
    ActivateMultiplayerBuffs(1600804)


@RestartOnRest
def Event11605392():
    """ 11605392: Event 11605392 """
    SkipLinesIfFlagOff(12, 13)
    DisableCharacter(1600800)
    DisableCharacter(1600801)
    DisableCharacter(1600802)
    DisableCharacter(1600803)
    DisableCharacter(1600804)
    Kill(1600800, award_souls=False)
    Kill(1600801, award_souls=False)
    Kill(1600802, award_souls=False)
    Kill(1600803, award_souls=False)
    Kill(1600804, award_souls=False)
    EnableTreasure(1601600)
    End()
    DisableAI(1600800)
    DisableAI(1600801)
    DisableAI(1600802)
    DisableAI(1600803)
    DisableAI(1600804)
    DisableCharacter(1600801)
    Kill(1600802, award_souls=False)
    Kill(1600803, award_souls=False)
    Kill(1600804, award_souls=False)
    DisableGravity(1600800)
    SkipLinesIfThisEventOn(5)
    IfFlagOn(1, 11605399)
    IfCharacterInsideRegion(1, PLAYER, region=1602999)
    IfConditionTrue(0, input_condition=1)
    DisableNetworkSync()
    Wait(7.0)
    EnableCharacter(1600801)
    ForceAnimation(1600801, 6200)
    EnableAI(1600801)
    EnableAI(1600802)
    EnableAI(1600803)
    EnableAI(1600804)
    EnableBossHealthBar(1600800, name=5390, slot=0)
    ReferDamageToEntity(1600801, 1600800)
    ReferDamageToEntity(1600802, 1600800)
    ReferDamageToEntity(1600803, 1600800)
    ReferDamageToEntity(1600804, 1600800)


@NeverRestart
def Event11600001():
    """ 11600001: Event 11600001 """
    DisableTreasure(1601600)
    DisableObject(1601600)
    DisableObject(1601950)
    IfHealthLessThanOrEqual(1, 1600800, 0.0)
    IfFlagOn(1, 11605395)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160010, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1602120, move_to_map=NEW_LONDO_RUINS)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(160010, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1602120, move_to_map=NEW_LONDO_RUINS)
    SkipLines(1)
    PlayCutscene(160010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(1600800)
    DisableCharacter(1600801)
    DisableCharacter(1600802)
    DisableCharacter(1600803)
    DisableCharacter(1600804)
    Kill(1600800, award_souls=True)
    Kill(1600801, award_souls=True)
    Kill(1600802, award_souls=True)
    Kill(1600803, award_souls=True)
    Kill(1600804, award_souls=True)
    IfCharacterDead(0, 1600800)
    EnableFlag(13)
    DisableSpawner(1603000)
    KillBoss(1600800)
    DisableObject(1601990)
    DeleteFX(1601991, erase_root_only=True)
    EnableTreasure(1601600)
    EnableObject(1601600)
    EndIfClient()
    AwardAchievement(37)
    CreateTemporaryFX(90014, anchor_entity=1601950, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1601950)
    RegisterBonfire(11600920, obj=1601950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


@NeverRestart
def Event11605394():
    """ 11605394: Event 11605394 """
    DisableNetworkSync()
    IfFlagOff(1, 13)
    IfFlagOn(1, 11605392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11605391)
    IfCharacterInsideRegion(1, PLAYER, region=1602990)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1603800)


@NeverRestart
def Event11605395():
    """ 11605395: Event 11605395 """
    DisableNetworkSync()
    IfHealthLessThanOrEqual(1, 1600800, 0.0)
    IfFlagOn(1, 11605394)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1603800)


@NeverRestart
def Event11605396():
    """ 11605396: Event 11605396 """
    IfFlagOn(0, 11605392)
    IfHealthLessThanOrEqual(7, 1600800, 0.0)
    EndIfConditionTrue(7)
    IfCharacterAlive(1, 1600801)
    SkipLinesIfConditionFalse(5, 1)
    AICommand(1600801, command_id=1, slot=0)
    IfCharacterDead(-1, 1600801)
    IfHasTAEEvent(-1, 1600801, tae_event_id=500)
    IfConditionTrue(0, input_condition=-1)
    AICommand(1600801, command_id=-1, slot=0)
    IfCharacterAlive(2, 1600802)
    SkipLinesIfConditionFalse(5, 2)
    AICommand(1600802, command_id=1, slot=0)
    IfCharacterDead(-2, 1600802)
    IfHasTAEEvent(-2, 1600802, tae_event_id=500)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1600802, command_id=-1, slot=0)
    IfCharacterAlive(3, 1600803)
    SkipLinesIfConditionFalse(5, 3)
    AICommand(1600803, command_id=1, slot=0)
    IfCharacterDead(-3, 1600803)
    IfHasTAEEvent(-3, 1600803, tae_event_id=500)
    IfConditionTrue(0, input_condition=-3)
    AICommand(1600803, command_id=-1, slot=0)
    IfCharacterAlive(4, 1600804)
    SkipLinesIfConditionFalse(5, 4)
    AICommand(1600804, command_id=1, slot=0)
    IfCharacterDead(-4, 1600804)
    IfHasTAEEvent(-4, 1600804, tae_event_id=500)
    IfConditionTrue(0, input_condition=-4)
    AICommand(1600804, command_id=-1, slot=0)
    Restart()


@NeverRestart
def Event11605397():
    """ 11605397: Event 11605397 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 2200)
    IfFlagOn(-1, 13)
    IfConditionTrue(0, input_condition=-1)
    DisableCollision(1603310)
    DisableCollision(1603311)
    EndIfFlagOn(13)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 2200)
    EnableCollision(1603310)
    EnableCollision(1603311)
    Restart()


@NeverRestart
def Event11605398():
    """ 11605398: Event 11605398 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(3, 13)
    IfCharacterInsideRegion(1, PLAYER, region=1602999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(7, 13)
    IfCharacterHasSpecialEffect(1, PLAYER, 2200)
    IfCharacterInsideRegion(1, PLAYER, region=1602999)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2200)
    IfCharacterInsideRegion(2, PLAYER, region=1602900)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 1)
    DisableCollision(PLAYER)
    IfCharacterDead(0, PLAYER)
    EnableCollision(PLAYER)
    EnableFlag(8120)
    End()
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@NeverRestart
def Event11605399():
    """ 11605399: Event 11605399 """
    DisableNetworkSync()
    IfHost(1)
    IfStandingOnCollision(1, 1603300)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(1603000)
    End()


@NeverRestart
def Event11605360(ARG_0_3: int):
    """ 11605360: Event 11605360 """
    DisableNetworkSync()
    IfFlagOff(1, 13)
    IfCharacterInsideRegion(1, ARG_0_3, region=1602990)
    IfCharacterDoesNotHaveSpecialEffect(1, ARG_0_3, 2200)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(ARG_0_3, disable_interpolation=True)
    ForceAnimation(ARG_0_3, 6084, wait_for_completion=True)
    DisableCharacter(ARG_0_3)
    EndIfNotEqual(left=ARG_0_3, right=10000)
    EnableFlag(8120)


@NeverRestart
def Event11605350(ARG_0_3: int):
    """ 11605350: Event 11605350 """
    IfHost(7)
    IfHealthGreaterThan(7, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=7)
    EnableImmortality(ARG_0_3)
    IfHost(1)
    IfTimeElapsed(1, 1.0)
    IfHealthGreaterThan(1, 1600800, 0.0)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.009999999776482582)
    IfHealthLessThanOrEqual(2, 1600800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableImmortality(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    Restart()
    ForceAnimation(ARG_0_3, 7000, wait_for_completion=True)
    DisableCharacter(ARG_0_3)
    DisableImmortality(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)


@NeverRestart
def Event11605380():
    """ 11605380: Event 11605380 """
    IfFlagOff(1, 11600900)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1602898, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, 1602897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1600810)
    Restart()


@NeverRestart
def Event11605381():
    """ 11605381: Event 11605381 """
    DisableNetworkSync()
    IfFlagOff(1, 11600900)
    IfFlagOn(1, 11605380)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1602898, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1602897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@RestartOnRest
def Event11605382():
    """ 11605382: Event 11605382 """
    SkipLinesIfFlagOff(3, 11600900)
    DisableCharacter(1600810)
    Kill(1600810, award_souls=False)
    End()
    DisableAI(1600810)
    IfHost(1)
    IfFlagOn(1, 11605380)
    IfCharacterInsideRegion(1, PLAYER, region=1602890)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1600810)
    EnableBossHealthBar(1600810, name=2390, slot=0)


@NeverRestart
def Event11600900():
    """ 11600900: Event 11600900 """
    IfCharacterDead(0, 1600810)
    KillBoss(1600810)
    DisableObject(1601890)
    DeleteFX(1601891, erase_root_only=True)
    EndIfClient()
    IfPlayerHasGood(1, 2013, including_box=False)
    EndIfConditionTrue(1)
    AwardItemLot(1100, host_only=False)


@NeverRestart
def Event11605384():
    """ 11605384: Event 11605384 """
    DisableNetworkSync()
    IfFlagOff(1, 11600900)
    IfFlagOn(1, 11605382)
    IfCharacterInsideRegion(1, PLAYER, region=1602890)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11605381)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1603801)


@NeverRestart
def Event11605385():
    """ 11605385: Event 11605385 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=1602890)
    IfCharacterDead(1, 1600810)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1603801)


@NeverRestart
def Event11600150():
    """ 11600150: Event 11600150 """
    SkipLinesIfFlagOn(63, 11600100)
    DisableCollision(1603250)
    DisableCollision(1603251)
    DisableCollision(1603252)
    DisableCollision(1603253)
    DisableCollision(1603254)
    DisableCollision(1603255)
    DisableCollision(1603256)
    DisableCollision(1603257)
    DisableCollision(1603258)
    DisableCollision(1603259)
    DisableCollision(1603260)
    DisableCollision(1603261)
    DisableCollision(1603262)
    DisableCollision(1603263)
    DisableCollision(1603264)
    DisableCollision(1603265)
    DisableCollision(1603266)
    DisableCollision(1603267)
    DisableMapPart(1603110)
    DisableMapPart(1603111)
    DisableMapPart(1603112)
    DisableMapPart(1603113)
    DisableMapPart(1603114)
    DisableMapPart(1603115)
    DisableMapPart(1603116)
    DisableMapPart(1603117)
    DisableMapPart(1603118)
    DisableMapPart(1603119)
    DisableMapPart(1603120)
    DisableCollision(1603121)
    DisableCollision(1603122)
    IfFlagOn(0, 11600100)
    EnableCollision(1603250)
    EnableCollision(1603251)
    EnableCollision(1603252)
    EnableCollision(1603253)
    EnableCollision(1603254)
    EnableCollision(1603255)
    EnableCollision(1603256)
    EnableCollision(1603257)
    EnableCollision(1603258)
    EnableCollision(1603259)
    EnableCollision(1603260)
    EnableCollision(1603261)
    EnableCollision(1603262)
    EnableCollision(1603263)
    EnableCollision(1603264)
    EnableCollision(1603265)
    EnableCollision(1603266)
    EnableCollision(1603267)
    EnableMapPart(1603110)
    EnableMapPart(1603111)
    EnableMapPart(1603112)
    EnableMapPart(1603113)
    EnableMapPart(1603114)
    EnableMapPart(1603115)
    EnableMapPart(1603116)
    EnableMapPart(1603117)
    EnableMapPart(1603118)
    EnableMapPart(1603119)
    EnableMapPart(1603120)
    EnableCollision(1603121)
    EnableCollision(1603122)
    DisableMapSound(1603850)
    DisableCollision(1603200)
    DisableCollision(1603201)
    DisableCollision(1603202)
    DisableCollision(1603203)
    DisableCollision(1603204)
    DisableCollision(1603205)
    DisableCollision(1603206)
    DisableCollision(1603207)
    DisableCollision(1603208)
    DisableCollision(1603209)
    DisableCollision(1603210)
    DisableCollision(1603211)
    DisableCollision(1603212)
    DisableCollision(1603213)
    DisableCollision(1603214)
    DisableCollision(1603215)
    DisableCollision(1603216)
    DisableCollision(1603217)


@RestartOnRest
def Event11605100():
    """ 11605100: Event 11605100 """
    EndIfFlagOn(11600100)
    DisableBackread(1600100)
    DisableBackread(1600101)
    DisableBackread(1600102)
    DisableBackread(1600103)
    DisableBackread(1600104)
    DisableBackread(1600105)
    DisableBackread(1600106)
    DisableBackread(1600107)
    DisableBackread(1600108)
    DisableBackread(1600109)
    DisableBackread(1600110)
    DisableBackread(1600400)
    DisableBackread(1600401)
    DisableBackread(1600900)
    DisableBackread(1600901)
    DisableBackread(1600902)
    DisableBackread(1600903)
    DisableBackread(1600904)
    DisableBackread(1600905)
    IfFlagOn(0, 11600100)
    EnableBackread(1600100)
    EnableBackread(1600101)
    EnableBackread(1600102)
    EnableBackread(1600103)
    EnableBackread(1600104)
    EnableBackread(1600105)
    EnableBackread(1600106)
    EnableBackread(1600107)
    EnableBackread(1600108)
    EnableBackread(1600109)
    EnableBackread(1600110)
    EnableBackread(1600400)
    EnableBackread(1600401)
    EnableBackread(1600900)
    EnableBackread(1600901)
    EnableBackread(1600902)
    EnableBackread(1600903)
    EnableBackread(1600904)
    EnableBackread(1600905)


@NeverRestart
def Event11600100():
    """ 11600100: Event 11600100 """
    SkipLinesIfFlagOn(1, 11600101)
    SkipLinesIfThisEventOff(8)
    EndOfAnimation(1601100, 10)
    DisableCollision(1603100)
    DisableCollision(1603102)
    DisableCollision(1603103)
    DisableCollision(1603104)
    DisableObject(1601120)
    DisableFlag(404)
    End()
    EnableCollision(1603103)
    EnableCollision(1603104)
    IfFlagOn(0, 11600101)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(160000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11600100)
    Restart()


@NeverRestart
def Event11600101(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11600101: Event 11600101 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(1601100, ARG_8_11)
    EndOfAnimation(ARG_0_3, 0)
    End()
    IfDialogPromptActivated(0, prompt_text=10010502, anchor_entity=ARG_0_3, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=104, human_or_hollow_only=False)
    Move(PLAYER, destination=ARG_0_3, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(ARG_0_3, 0, wait_for_completion=True)
    EndIfFlagOn(ARG_4_7)
    ForceAnimation(1601100, ARG_8_11, wait_for_completion=True)


@NeverRestart
def Event11600110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11600110: Event 11600110 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    EnableFlag(ARG_0_3)
    EndIfClient()
    DisplayDialog(ARG_4_7, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=3)


@NeverRestart
def Event11600120(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11600120: Event 11600120 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    EnableFlag(ARG_0_3)
    EndIfClient()
    IfPlayerHasGood(1, ARG_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(ARG_12_15, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    SkipLines(1)
    DisplayDialog(ARG_4_7, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(ARG_8_11, obj_act_id=-1, relative_index=3)


@NeverRestart
def Event11600160():
    """ 11600160: Event 11600160 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1601142, 0)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)
    End()
    IfDialogPromptActivated(0, prompt_text=10010500, anchor_entity=1601142, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=194, human_or_hollow_only=False)
    EnableFlag(11600160)
    Move(PLAYER, destination=1601142, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1601142, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)


@NeverRestart
def Event11600200():
    """ 11600200: Event 11600200 """
    SkipLinesIfFlagOff(3, 11600201)
    EndOfAnimation(1601200, 21)
    DisableObjectActivation(1601202, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601200, 20)
    DisableObjectActivation(1021201, obj_act_id=6101)
    IfSingleplayer(1)
    IfFlagOff(1, 11600201)
    IfCharacterInsideRegion(1, PLAYER, region=1602200)
    IfSingleplayer(2)
    IfFlagOn(2, 11600201)
    IfCharacterInsideRegion(2, PLAYER, region=1602201)
    IfSingleplayer(3)
    IfObjectActivated(3, obj_act_id=11020202)
    IfSingleplayer(4)
    IfObjectActivated(4, obj_act_id=11600203)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605120)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 3)
    EnableFlag(11600201)
    DisableObjectActivation(1601202, obj_act_id=6101)
    ForceAnimation(1601200, 11, wait_for_completion=True)
    ForceAnimation(1601200, 1, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602201)
    ForceAnimation(1601200, 21, wait_for_completion=True)
    EnableObjectActivation(1021201, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()
    DisableFlag(11600201)
    DisableObjectActivation(1021201, obj_act_id=6101)
    ForceAnimation(1601200, 10, wait_for_completion=True)
    ForceAnimation(1601200, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602200)
    ForceAnimation(1601200, 20, wait_for_completion=True)
    EnableObjectActivation(1601202, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()


@NeverRestart
def Event11600250():
    """ 11600250: Event 11600250 """
    DisableNetworkSync()
    IfFlagOff(1, 11605120)
    IfFlagOff(1, 11600201)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1021201, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605120)
    IfFlagOn(2, 11600201)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601202, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfMultiplayer(3)
    IfFlagOff(3, 11600201)
    IfCharacterInsideRegion(3, PLAYER, region=1602200)
    IfMultiplayer(4)
    IfFlagOn(4, 11600201)
    IfCharacterInsideRegion(4, PLAYER, region=1602201)
    IfMultiplayer(5)
    IfObjectActivated(5, obj_act_id=11020202)
    IfMultiplayer(6)
    IfObjectActivated(6, obj_act_id=11600203)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11600199():
    """ 11600199: Event 11600199 """
    EndIfThisEventOn()
    IfFlagOn(0, 11600100)
    EnableObjectActivation(1601211, obj_act_id=6101)
    EnableObjectActivation(1601221, obj_act_id=6101)


@NeverRestart
def Event11600210():
    """ 11600210: Event 11600210 """
    SkipLinesIfFlagOff(3, 11600211)
    EndOfAnimation(1601210, 22)
    DisableObjectActivation(1601211, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601210, 21)
    DisableObjectActivation(1601212, obj_act_id=6101)
    SkipLinesIfFlagOn(1, 11600100)
    DisableObjectActivation(1601211, obj_act_id=6101)
    IfFlagOn(1, 11600100)
    IfFlagOff(1, 11600211)
    IfCharacterInsideRegion(1, PLAYER, region=1602211)
    IfFlagOn(2, 11600100)
    IfFlagOn(2, 11600211)
    IfCharacterInsideRegion(2, PLAYER, region=1602210)
    IfObjectActivated(3, obj_act_id=11600212)
    IfObjectActivated(4, obj_act_id=11600213)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600211)
    DisableObjectActivation(1601211, obj_act_id=6101)
    ForceAnimation(1601210, 10, wait_for_completion=True)
    ForceAnimation(1601210, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602210)
    ForceAnimation(1601210, 22, wait_for_completion=True)
    EnableObjectActivation(1601212, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(1601212, obj_act_id=6101)
    ForceAnimation(1601210, 13, wait_for_completion=True)
    ForceAnimation(1601210, 3, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602211)
    ForceAnimation(1601210, 21, wait_for_completion=True)
    EnableObjectActivation(1601211, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


@NeverRestart
def Event11600251():
    """ 11600251: Event 11600251 """
    DisableNetworkSync()
    IfFlagOff(1, 11605121)
    IfFlagOn(1, 11600211)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1601211, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605121)
    IfFlagOff(2, 11600211)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601212, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(3, 11600100)
    IfDialogPromptActivated(3, prompt_text=10010501, anchor_entity=1601211, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11600220():
    """ 11600220: Event 11600220 """
    SkipLinesIfFlagOff(3, 11600221)
    EndOfAnimation(1601220, 24)
    DisableObjectActivation(1601221, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601220, 21)
    DisableObjectActivation(1601222, obj_act_id=6101)
    SkipLinesIfFlagOn(1, 11600100)
    DisableObjectActivation(1601221, obj_act_id=6101)
    IfFlagOn(1, 11600100)
    IfFlagOff(1, 11600221)
    IfCharacterInsideRegion(1, PLAYER, region=1602221)
    IfFlagOn(2, 11600100)
    IfFlagOn(2, 11600221)
    IfCharacterInsideRegion(2, PLAYER, region=1602220)
    IfObjectActivated(3, obj_act_id=11600222)
    IfObjectActivated(4, obj_act_id=11600223)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600221)
    DisableObjectActivation(1601221, obj_act_id=6101)
    ForceAnimation(1601220, 10, wait_for_completion=True)
    ForceAnimation(1601220, 4, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602220)
    ForceAnimation(1601220, 24, wait_for_completion=True)
    EnableObjectActivation(1601222, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(1601222, obj_act_id=6101)
    ForceAnimation(1601220, 15, wait_for_completion=True)
    ForceAnimation(1601220, 5, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602221)
    ForceAnimation(1601220, 21, wait_for_completion=True)
    EnableObjectActivation(1601221, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


@NeverRestart
def Event11600252():
    """ 11600252: Event 11600252 """
    DisableNetworkSync()
    IfFlagOff(1, 11605122)
    IfFlagOn(1, 11600221)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1601221, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605122)
    IfFlagOff(2, 11600221)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601222, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(3, 11600100)
    IfDialogPromptActivated(3, prompt_text=10010501, anchor_entity=1601221, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11600230():
    """ 11600230: Event 11600230 """
    SkipLinesIfFlagOff(3, 11600231)
    EndOfAnimation(1601230, 26)
    DisableObjectActivation(1601231, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601230, 21)
    DisableObjectActivation(1601232, obj_act_id=6101)
    IfFlagOff(1, 11600231)
    IfCharacterInsideRegion(1, PLAYER, region=1602231)
    IfFlagOn(2, 11600231)
    IfCharacterInsideRegion(2, PLAYER, region=1602230)
    IfObjectActivated(3, obj_act_id=11600232)
    IfObjectActivated(4, obj_act_id=11600233)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605123)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600231)
    DisableObjectActivation(1601231, obj_act_id=6101)
    ForceAnimation(1601230, 10, wait_for_completion=True)
    ForceAnimation(1601230, 6, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602230)
    ForceAnimation(1601230, 26, wait_for_completion=True)
    EnableObjectActivation(1601232, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()
    DisableFlag(11600231)
    DisableObjectActivation(1601232, obj_act_id=6101)
    ForceAnimation(1601230, 17, wait_for_completion=True)
    ForceAnimation(1601230, 7, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602231)
    ForceAnimation(1601230, 21, wait_for_completion=True)
    EnableObjectActivation(1601231, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()


@NeverRestart
def Event11600253():
    """ 11600253: Event 11600253 """
    DisableNetworkSync()
    IfFlagOff(1, 11605123)
    IfFlagOn(1, 11600231)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1601231, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605123)
    IfFlagOff(2, 11600231)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601232, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@RestartOnRest
def Event11605150(ARG_0_3: int, ARG_4_7: int):
    """ 11605150: Event 11605150 """
    DisableNetworkSync()
    IfCharacterDead(1, ARG_0_3)
    EndIfConditionTrue(1)
    IfCharacterOutsideRegion(0, ARG_0_3, region=ARG_4_7)
    ReplanAI(ARG_0_3)
    Wait(5.0)
    Restart()


@RestartOnRest
def Event11605001(ARG_0_3: int, ARG_4_7: float, ARG_8_11: int):
    """ 11605001: Event 11605001 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    DisableAI(ARG_0_3)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_4_7)
    IfAttacked(2, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ResetStandbyAnimationSettings(ARG_0_3)
    SkipLines(1)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=ARG_8_11)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event11605050(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float):
    """ 11605050: Event 11605050 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfAttacked(2, ARG_0_3, attacking_character=10000)
    SkipLinesIfEqual(1, left=ARG_12_15, right=0)
    IfEntityWithinDistance(3, ARG_0_3, 10000, radius=ARG_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    SkipLinesIfEqual(1, left=ARG_12_15, right=0)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ResetStandbyAnimationSettings(ARG_0_3)
    SkipLines(1)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=ARG_8_11)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event11605101():
    """ 11605101: Event 11605101 """
    SkipLinesIfThisEventOff(2)
    AICommand(1600300, command_id=1, slot=0)
    End()
    IfHasTAEEvent(0, 1600300, tae_event_id=700)
    SetNest(1600300, 1602300)
    AICommand(1600300, command_id=0, slot=0)
    ReplanAI(1600300)
    IfCharacterInsideRegion(0, 1600300, region=1602301)
    AICommand(1600300, command_id=1, slot=0)


@RestartOnRest
def Event11600810():
    """ 11600810: Event 11600810 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1600500)
    End()
    IfCharacterDead(0, 1600500)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(34200200, host_only=True)


@RestartOnRest
def Event11600400():
    """ 11600400: Event 11600400 """
    DisableCollision(1600500)
    DisableGravity(1600500)
    SkipLinesIfThisEventOff(2)
    SetStandbyAnimationSettings(1600500, cancel_animation=29060)
    End()
    IfEntityWithinDistance(-1, 1600500, 10000, radius=10.0)
    IfAttacked(-1, 1600500, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(1600500)
    ForceAnimation(1600500, 29060)


@RestartOnRest
def Event11605200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11605200: Event 11605200 """
    SkipLinesIfThisEventSlotOff(3)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    End()
    DisableCharacter(ARG_4_7)
    IfCharacterBackreadEnabled(1, ARG_0_3)
    IfHasTAEEvent(1, ARG_0_3, tae_event_id=300)
    IfFlagOn(1, ARG_12_15)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    EnableCharacter(ARG_4_7)
    Move(ARG_4_7, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=100, copy_draw_Collision=ARG_0_3)
    ForceAnimation(ARG_4_7, 8300, wait_for_completion=True)
    IfDoesNotHaveTAEEvent(1, ARG_0_3, tae_event_id=300)
    End()


@RestartOnRest
def Event11605250(ARG_0_3: int):
    """ 11605250: Event 11605250 """
    DisableNetworkSync()
    SkipLinesIfThisEventSlotOn(1)
    IfHasTAEEvent(0, ARG_0_3, tae_event_id=400)
    DisableCharacter(ARG_0_3)


@RestartOnRest
def Event11600850(ARG_0_3: int):
    """ 11600850: Event 11600850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfCharacterDead(0, ARG_0_3)
    End()


@NeverRestart
def Event11600600(ARG_0_3: int, ARG_4_7: int):
    """ 11600600: Event 11600600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=-1)
    EnableTreasure(ARG_0_3)
    End()
    DisableTreasure(ARG_0_3)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@NeverRestart
def Event11600650(ARG_0_3: int, ARG_4_7: int):
    """ 11600650: Event 11600650 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(ARG_0_3, 101)
    EnableTreasure(ARG_0_3)
    End()
    DisableTreasure(ARG_0_3)
    ForceAnimation(ARG_0_3, 100, loop=True)
    IfObjectDestroyed(0, ARG_4_7)
    ForceAnimation(ARG_0_3, 101, wait_for_completion=True)
    EnableTreasure(ARG_0_3)


@NeverRestart
def Event11600510(ARG_0_3: int, ARG_4_7: int):
    """ 11600510: Event 11600510 """
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
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11600520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600520: Event 11600520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600530(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600530: Event 11600530 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1310)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600531(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600531: Event 11600531 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1311)
    IfFlagOn(1, 11600100)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600532: Event 11600532 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1312)
    IfFlagOn(1, 13)
    IfFlagOn(1, 11600593)
    IfOutsideMap(1, game_map=NEW_LONDO_RUINS)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11600537(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600537: Event 11600537 """
    EndIfFlagOff(1670)
    DisableCharacter(ARG_0_3)
    IfHost(1)
    IfFlagOn(1, 1670)
    IfFlagOff(1, 11800100)
    IfFlagOn(1, 13)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 9060, wait_for_completion=True)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600538(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600538: Event 11600538 """
    IfFlagOn(1, 1671)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600539(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600539: Event 11600539 """
    IfFlagOn(1, 1672)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11600540(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600540: Event 11600540 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1678)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11600590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    ForceAnimation(ARG_0_3, 7005, wait_for_completion=True)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11600541(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11600541: Event 11600541 """
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfFlagOn(-1, 11600590)
    IfHealthLessThanOrEqual(2, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(2, ARG_0_3, 0.0)
    IfAttacked(2, ARG_0_3, attacking_character=10000)
    IfEntityBeyondDistance(2, ARG_0_3, 10000, radius=15.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    ForceAnimation(ARG_0_3, 7005, wait_for_completion=True)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11600545(ARG_0_3: int):
    """ 11600545: Event 11600545 """
    IfFlagOn(0, 1464)
    EnableCharacter(ARG_0_3)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)


@NeverRestart
def Event11606200():
    """ 11606200: Event 11606200 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1673)
    IfFlagOn(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfFlagOn(1, 821)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(821)
    EnableFlag(831)
    EnableCharacter(6341)
    PlayCutscene(160040, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1802110, move_to_map=KILN_OF_THE_FIRST_FLAME)
    PlayCutscene(180041, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(823)
    Restart()


@NeverRestart
def Event11605030():
    """ 11605030: Event 11605030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6520, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11605034)
    IfClient(2)
    IfFlagOn(2, 11605031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6520)
    EndIfFlagOn(13)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11200300)
    IfCharacterBackreadEnabled(1, 6520)
    IfEntityWithinDistance(1, 6520, 10000, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6520, region=1602000, summon_flag=11605031, dismissal_flag=11605034)


@NeverRestart
def Event11605032():
    """ 11605032: Event 11605032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11605031)
    IfFlagOn(1, 11605393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6520, command_id=10, slot=0)
    ReplanAI(6520)
    IfCharacterInsideRegion(0, 6520, region=1602998)
    RotateToFaceEntity(6520, 1602997)
    ForceAnimation(6520, 7410)
    AICommand(6520, command_id=-1, slot=0)
    ReplanAI(6520)


@NeverRestart
def Event11605033():
    """ 11605033: Event 11605033 """
    IfFlagOn(1, 11605031)
    IfCharacterHasSpecialEffect(1, 6520, 2200)
    IfCharacterInsideRegion(1, 6520, region=1602999)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(6520)
    Wait(2.0)
    DisableInvincibility(6520)
