"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(11010008)
    DisableFlag(11010580)
    SkipLinesIfFlagOff(2, 61010610)
    EndOfAnimation(1011101, 2)
    EnableNavmeshType(1013100, NavmeshType.Solid)
    SkipLinesIfClient(24)
    DisableObject(1011994)
    DeleteFX(1011995, erase_root_only=False)
    DisableObject(1011996)
    DeleteFX(1011997, erase_root_only=False)
    DisableObject(1011998)
    DeleteFX(1011999, erase_root_only=False)
    DisableObject(1011988)
    DeleteFX(1011989, erase_root_only=False)
    DisableObject(1011986)
    DeleteFX(1011987, erase_root_only=False)
    DisableObject(1011984)
    DeleteFX(1011985, erase_root_only=False)
    DisableObject(1011982)
    DeleteFX(1011983, erase_root_only=False)
    DisableObject(1011980)
    DeleteFX(1011981, erase_root_only=False)
    DisableObject(1011978)
    DeleteFX(1011979, erase_root_only=False)
    DisableObject(1011976)
    DeleteFX(1011977, erase_root_only=False)
    DisableObject(1011974)
    DeleteFX(1011975, erase_root_only=False)
    DisableObject(1011972)
    DeleteFX(1011973, erase_root_only=False)
    RunEvent(11010090, slot=0, args=(1011700, 1011701, 1012600, 1012601))
    RunEvent(11010090, slot=1, args=(1011702, 1011703, 1012602, 1012603))
    RunEvent(11015070)
    RunEvent(11015071)
    RunEvent(11015072)
    RunEvent(11010903)
    RunEvent(11015110)
    RunEvent(11015113)
    RunEvent(11015112)
    RunEvent(11015130)
    RunEvent(11010710)
    RunEvent(11010111)
    RunEvent(11010120)
    RunEvent(11010150, slot=0, args=(11010160, 1012401, 1012400))
    RunEvent(11010160, slot=0, args=(11010160, 1011314))
    RunEvent(11010170, slot=1, args=(11010171, 10010873, 1011306))
    RunEvent(11010170, slot=2, args=(11010172, 10010860, 1011311))
    RunEvent(11010180, slot=1, args=(11010181, 10010881, 1011317))
    RunEvent(11010140, slot=0, args=(11010140, 10010881, 1011310, 10010883, 2021))
    RunEvent(11010190, slot=0, args=(11010190, 10010876, 1011308, 10010883, 2017))
    RunEvent(11010190, slot=1, args=(11010191, 10010878, 1011315, 10010883, 2019))
    RunEvent(11010190, slot=2, args=(11010192, 10010878, 1011316, 10010883, 2019))
    RunEvent(11010101, slot=0, args=(1011320, 1, 101, 121, 7110), arg_types="iihii")
    RunEvent(11010102, slot=0, args=(11010142, 1011320, 100), arg_types="iih")
    RunEvent(11015185)
    RunEvent(11010611)
    RunEvent(11010600)
    RunEvent(11010601)
    RunEvent(11015116)
    RunEvent(11010609)
    RunEvent(11010607)
    RunEvent(11010608)
    RunEvent(11010621)
    RunEvent(11010700)
    RunEvent(11015170)
    RunEvent(11010100)
    RunEvent(11010780)
    RunEvent(11010580)
    RunEvent(11010585)
    DisableSoundEvent(1013800)
    SkipLinesIfFlagOn(1, 3)
    DisableSoundEvent(1013801)
    SkipLinesIfFlagOff(6, 3)
    RunEvent(11015392)
    DisableObject(1011990)
    DeleteFX(1011991, erase_root_only=False)
    DisableObject(1011992)
    DeleteFX(1011993, erase_root_only=False)
    SkipLines(11)
    RunEvent(11010000)
    RunEvent(11015390)
    RunEvent(11015391)
    RunEvent(11015393)
    RunEvent(11015392)
    RunEvent(11010001)
    RunEvent(11015394)
    RunEvent(11015395)
    RunEvent(11015396)
    RunEvent(11010750, slot=0, args=(1010800, 53500000))
    RunEvent(11010750, slot=1, args=(1010801, 53500100))
    RunEvent(11015397, slot=0, args=(1010800, 5350, 5350, 1010810), arg_types="ihii")
    RunEvent(11015398, slot=0, args=(1010801, 1010811))
    DisableSoundEvent(1013802)
    SkipLinesIfFlagOff(6, 11010901)
    RunEvent(11010901)
    DisableObject(1011890)
    DeleteFX(1011891, erase_root_only=False)
    DisableObject(1011892)
    DeleteFX(1011893, erase_root_only=False)
    SkipLines(8)
    RunEvent(11015380)
    RunEvent(11015381)
    RunEvent(11015383)
    RunEvent(11015382)
    RunEvent(11015384)
    RunEvent(11015385)
    RunEvent(11015386)
    RunEvent(11010901)
    DisableSoundEvent(1013803)
    SkipLinesIfFlagOff(4, 11010902)
    RunEvent(11010902)
    DisableObject(1011790)
    DeleteFX(1011791, erase_root_only=False)
    SkipLines(7)
    RunEvent(11015370)
    RunEvent(11015371)
    RunEvent(11015373)
    RunEvent(11015372)
    RunEvent(11015374)
    RunEvent(11015375)
    RunEvent(11010902)
    SkipLinesIfFlagOff(2, 11010900)
    RunEvent(11010900)
    SkipLines(29)
    RunEvent(11010899)
    RunEvent(11010900)
    RunEvent(11010782)
    RunEvent(11010783)
    RunEvent(11010790)
    RunEvent(11010791)
    RunEvent(11015301)
    RunEvent(11010784)
    RunEvent(11015302)
    RunEvent(11015303)
    RunEvent(11015304)
    RunEvent(11010851)
    RunEvent(11010852)
    RunEvent(11010890, slot=0, args=(11015320, 11015321, 11015322, 11015323, 11015324, 11015325, 11015326))
    RunEvent(11010890, slot=1, args=(11015327, 11015328, 11015329, 11015330, 11015331, 11015332, 11015333))
    RunEvent(11010890, slot=2, args=(11015334, 11015335, 11015336, 11015337, 11015338, 11015339, 11015340))
    RunEvent(11010850)
    RunEvent(11015307)
    RunEvent(11015308)
    RunEvent(11010200, slot=0, args=(10, 3000))
    RunEvent(11010200, slot=1, args=(20, 3001))
    RunEvent(11010200, slot=2, args=(30, 3002))
    RunEvent(11010200, slot=3, args=(40, 3009))
    RunEvent(11010200, slot=4, args=(50, 3010))
    RunEvent(11010200, slot=5, args=(60, 7004))
    RunEvent(11010200, slot=6, args=(70, 7005))
    RunEvent(11010200, slot=7, args=(80, 7008))
    RunEvent(11010200, slot=8, args=(90, 7009))
    RunEvent(11010200, slot=9, args=(100, 7011))
    RunEvent(11015250, slot=0, args=(1010250, 1010250, 5.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=1, args=(1010251, 1010250, 5.5, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=2, args=(1010260, 1010260, 5.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=3, args=(1010261, 1010260, 4.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=4, args=(1010262, 1010260, 3.0, 0.0), arg_types="iiff")
    RunEvent(11015250, slot=5, args=(1010263, 1010260, 3.0, 0.0), arg_types="iiff")
    RunEvent(11010130, slot=0, args=(1011250, 1010150, 1012150))
    RunEvent(11010130, slot=1, args=(1011251, 1010151, 1012150))
    RunEvent(11010130, slot=2, args=(1011252, 1010152, 1012150))
    RunEvent(11010130, slot=3, args=(1011253, 1010153, 1012151))
    RunEvent(11010130, slot=4, args=(1011254, 1010154, 1012151))
    RunEvent(11010130, slot=5, args=(1011255, 1010155, 1012151))
    RunEvent(11010860, slot=0, args=(6580, 0, 0))
    RunEvent(11010860, slot=1, args=(1010350, 1, 27900000))
    RunEvent(11010860, slot=2, args=(1010351, 1, 27900100))
    RunEvent(11010860, slot=3, args=(1010320, 0, 0))
    RunEvent(11010860, slot=4, args=(1010340, 0, 0))
    RunEvent(11010860, slot=5, args=(1010370, 0, 0))
    RunEvent(11010860, slot=6, args=(6010, 0, 0))
    RunEvent(11010400, slot=2, args=(1011652, 1011502))
    RunEvent(11010400, slot=3, args=(1011653, 1011503))
    RunEvent(11010400, slot=4, args=(1011654, 1011504))
    RunEvent(11010650, slot=0, args=(1011670, 11010650))
    RunEvent(11010650, slot=1, args=(1011671, 11010651))
    RunEvent(11015846, slot=0, args=(11010901, 1011890, 1011891))
    RunEvent(11015843, slot=0, args=(11010901, 1011890, 1012898, 1012897))
    RunEvent(11015846, slot=1, args=(11010902, 1011790, 1011791))
    RunEvent(11015843, slot=1, args=(11010902, 1011790, 1012888, 1012887))
    RunEvent(11015846, slot=2, args=(3, 1011990, 1011991))
    RunEvent(11015843, slot=2, args=(3, 1011990, 1012998, 1012997))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11010583)
    HumanityRegistration(6580, 8972)
    HumanityRegistration(6540, 8310)
    HumanityRegistration(6590, 8462)
    RunEvent(11015100)
    RunEvent(11015900)
    RunEvent(11015101)
    RunEvent(11015103)
    RunEvent(11015901)
    RunEvent(11015104)
    RunEvent(11015990, slot=0, args=(11015102, 6540))
    RunEvent(11015990, slot=1, args=(11015105, 6590))
    RunEvent(11015203)
    HumanityRegistration(6001, 8310)
    SkipLinesIfFlagOn(4, 1007)
    SkipLinesIfFlagOn(3, 1004)
    SkipLinesIfFlagOn(2, 1001)
    SkipLinesIfFlagOn(1, 1000)
    DisableCharacter(6001)
    SkipLinesIfFlagOn(1, 11510594)
    SkipLines(1)
    Move(6001, destination=1012530, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013050)
    RunEvent(11010510, slot=0, args=(6001, 1004))
    RunEvent(11010520, slot=0, args=(6001, 1000, 1029, 1005))
    RunEvent(11010530, slot=0, args=(6001, 1000, 1029, 1001))
    RunEvent(11010531, slot=0, args=(6001, 1000, 1029, 1007))
    HumanityRegistration(6040, 8342)
    SkipLinesIfFlagRangeAllOff(1, (1112, 1113))
    DisableCharacter(6040)
    RunEvent(11010510, slot=1, args=(6040, 1114))
    RunEvent(11010520, slot=1, args=(6040, 1110, 1119, 1115))
    RunEvent(11010532, slot=0, args=(6040, 1110, 1119, 1111))
    HumanityRegistration(6072, 8358)
    SkipLinesIfFlagOn(1, 1175)
    DisableCharacter(6072)
    RunEvent(11010533, slot=0, args=(6072, 1170, 1189, 1175))
    RunEvent(11010501, slot=0, args=(6072, 1179))
    RunEvent(11010535, slot=0, args=(6072, 1170, 1189, 1180))
    RunEvent(11010534, slot=0, args=(6072, 1170, 1189, 1181))
    RunEvent(11010537, slot=0, args=(6072, 1170, 1189, 1177))
    RunEvent(11010538)
    RunEvent(11010539)
    RunEvent(11010582)
    RunEvent(11010510, slot=3, args=(6190, 1321))
    RunEvent(11010520, slot=3, args=(6190, 1320, 1339, 1322))
    RunEvent(11015090, slot=0, args=(1321, 1322, 1011010))
    RunEvent(11010510, slot=4, args=(6230, 1401))
    RunEvent(11010520, slot=4, args=(6230, 1400, 1409, 1402))
    HumanityRegistration(6300, 8462)
    SkipLinesIfClient(1)
    DisableFlag(11010584)
    SkipLinesIfFlagOn(3, 11010584)
    SkipLinesIfFlagOn(2, 1574)
    SkipLinesIfFlagOn(1, 1570)
    DisableCharacter(6300)
    RunEvent(11010510, slot=6, args=(6300, 1574))
    RunEvent(11010520, slot=6, args=(6300, 1570, 1599, 1575))
    RunEvent(11010550, slot=0, args=(6300, 1570, 1599, 1571))
    RunEvent(11010552, slot=0, args=(6300, 1570, 1599, 1577))
    RunEvent(11010551)
    HumanityRegistration(6370, 8486)
    SkipLinesIfFlagOn(1, 11010581)
    DisableCharacter(6370)
    RunEvent(11010510, slot=7, args=(6370, 1701))
    RunEvent(11010520, slot=7, args=(6370, 1700, 1709, 1702))
    RunEvent(11010581, slot=0, args=(6370,))


def Event11010008():
    """ 11010008: Event 11010008 """
    RegisterBonfire(11010984, obj=1011961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11010976, obj=1011962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11010960, obj=1011964, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11010010, stop_climbing_flag=11010011, obj=1011140)
    RegisterLadder(start_climbing_flag=11010012, stop_climbing_flag=11010013, obj=1011141)
    RegisterLadder(start_climbing_flag=11010014, stop_climbing_flag=11010015, obj=1011142)
    RegisterLadder(start_climbing_flag=11010016, stop_climbing_flag=11010017, obj=1011143)
    RegisterLadder(start_climbing_flag=11010018, stop_climbing_flag=11010019, obj=1011144)
    RegisterLadder(start_climbing_flag=11010020, stop_climbing_flag=11010021, obj=1011145)
    RegisterLadder(start_climbing_flag=11010022, stop_climbing_flag=11010023, obj=1011146)
    RegisterLadder(start_climbing_flag=11010024, stop_climbing_flag=11010025, obj=1011147)
    RegisterLadder(start_climbing_flag=11010026, stop_climbing_flag=11010027, obj=1011148)
    RegisterLadder(start_climbing_flag=11010030, stop_climbing_flag=11010031, obj=1011150)
    RegisterLadder(start_climbing_flag=11010032, stop_climbing_flag=11010033, obj=1011151)
    RegisterLadder(start_climbing_flag=11010034, stop_climbing_flag=11010035, obj=1011152)
    CreateHazard(
        11010300,
        1011450,
        model_point=200,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        11010308,
        1011407,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        11010309,
        1011408,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )


def Event11010090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010090: Event 11010090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1, prompt_text=10010403, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, line_intersects=arg_0_3
    )
    IfActionButton(
        2, prompt_text=10010407, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Region, line_intersects=arg_0_3
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11015070():
    """ 11015070: Event 11015070 """
    EndIfThisEventOn()
    DisableCharacter(1010900)
    DisableCharacter(1010901)
    DisableCharacter(1010902)
    DisableCharacter(1010903)
    DisableCharacter(1010904)
    DisableCharacter(1010905)
    DisableCharacter(1010906)
    DisableCharacter(1010907)
    DisableCharacter(1010908)
    DisableCharacter(1010909)
    DisableCharacter(1010910)
    DisableCharacter(1010911)
    DisableCharacter(1010912)
    IfFlagOn(0, 11010050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1010900)
    EnableCharacter(1010901)
    EnableCharacter(1010902)
    EnableCharacter(1010903)
    EnableCharacter(1010904)
    EnableCharacter(1010905)
    EnableCharacter(1010906)
    EnableCharacter(1010907)
    EnableCharacter(1010908)
    EnableCharacter(1010909)
    EnableCharacter(1010910)
    EnableCharacter(1010911)
    EnableCharacter(1010912)


@RestartOnRest
def Event11015071():
    """ 11015071: Event 11015071 """
    IfFlagOn(-1, 11015075)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11010050)
    DisableFlag(11015075)
    EnableFlag(5001)
    Kill(1010900, award_souls=False)
    Kill(1010901, award_souls=False)
    Kill(1010902, award_souls=False)
    Kill(1010903, award_souls=False)
    Kill(1010904, award_souls=False)
    Kill(1010905, award_souls=False)
    Kill(1010906, award_souls=False)
    Kill(1010907, award_souls=False)
    Kill(1010908, award_souls=False)
    Kill(1010909, award_souls=False)
    Kill(1010910, award_souls=False)
    Kill(1010911, award_souls=False)
    Kill(1010912, award_souls=False)


@RestartOnRest
def Event11015072():
    """ 11015072: Event 11015072 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11010050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=UNDEAD_BURG)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11010050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=UNDEAD_BURG)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11010050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=UNDEAD_BURG)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11010050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=UNDEAD_BURG)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11010050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=UNDEAD_BURG)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11010050)
    RestartIfConditionFalse(-6)
    EnableFlag(11010050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=UNDEAD_BURG)
    RestartIfConditionFalse(7)
    DisableFlag(11010050)
    EnableFlag(11015075)


@RestartOnRest
def Event11010000():
    """ 11010000: Event 11010000 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1010802)
    End()
    DisableAI(1010802)
    SetStandbyAnimationSettings(1010802, standby_animation=7000)
    EnableInvincibility(1010802)
    DisableHealthBar(1010802)
    DisableCharacter(1010800)
    IfFlagOn(1, 11015390)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1012999)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(100110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(1010802)
    EnableCharacter(1010800)


def Event11015390():
    """ 11015390: Event 11015390 """
    IfFlagOff(1, 3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1011990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015391():
    """ 11015391: Event 11015391 """
    IfFlagOff(1, 3)
    IfFlagOn(1, 11015393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1011990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015393():
    """ 11015393: Event 11015393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 3)
    IfCharacterInsideRegion(1, PLAYER, region=1012996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1010800)


@RestartOnRest
def Event11015392():
    """ 11015392: Event 11015392 """
    SkipLinesIfFlagOff(11, 3)
    DisableCharacter(1010800)
    DisableCharacter(1010801)
    DisableCharacter(1010802)
    DisableCharacter(1010810)
    DisableCharacter(1010811)
    Kill(1010800, award_souls=False)
    Kill(1010801, award_souls=False)
    Kill(1010802, award_souls=False)
    Kill(1010810, award_souls=False)
    Kill(1010811, award_souls=False)
    End()
    DisableAI(1010800)
    IfFlagOn(1, 11010000)
    IfFlagOn(1, 11015393)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010800)
    EnableBossHealthBar(1010800, name=5350, slot=0)


def Event11010001():
    """ 11010001: Event 11010001 """
    IfCharacterDead(1, 1010800)
    IfCharacterDead(2, 1010801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(3, 1010800)
    IfCharacterDead(3, 1010801)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(3)
    SkipLinesIfFinishedConditionTrue(2, 1)
    PlaySoundEffect(anchor_entity=1010800, sound_type=SoundType.s_SFX, sound_id=777777777)
    SkipLines(1)
    PlaySoundEffect(anchor_entity=1010801, sound_type=SoundType.s_SFX, sound_id=777777777)
    KillBoss(1010800)
    DisableObject(1011990)
    DeleteFX(1011991, erase_root_only=True)
    DisableObject(1011992)
    DeleteFX(1011993, erase_root_only=True)


def Event11015394():
    """ 11015394: Event 11015394 """
    DisableNetworkSync()
    IfFlagOff(1, 3)
    IfFlagOn(1, 11010000)
    IfFlagOn(1, 11015392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015391)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013801)
    EnableSoundEvent(1013800)


def Event11015395():
    """ 11015395: Event 11015395 """
    DisableNetworkSync()
    IfFlagOn(1, 11015394)
    IfFlagOn(1, 3)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013800)
    EnableSoundEvent(1013801)


@RestartOnRest
def Event11015396():
    """ 11015396: Event 11015396 """
    EndIfFlagOn(3)
    DisableAI(1010801)
    SetStandbyAnimationSettings(1010801, standby_animation=7000)
    EnableInvincibility(1010801)
    DisableHealthBar(1010801)
    IfHealthLessThanOrEqual(0, 1010800, 0.6000000238418579)
    ResetStandbyAnimationSettings(1010801)
    Move(1010801, destination=1012650, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1010801, 7001, wait_for_completion=True)
    DisableInvincibility(1010801)
    EnableAI(1010801)
    EnableBossHealthBar(1010801, name=5350, slot=1)


@RestartOnRest
def Event11015397(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int):
    """ 11015397: Event 11015397 """
    DisableCharacter(arg_12_15)
    SkipLinesIfThisEventSlotOff(5)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    End()
    IfFlagOn(1, 11015392)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=65,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=130,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_12_15)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    ForceAnimation(arg_12_15, 8100)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(53520000, host_only=True)


@RestartOnRest
def Event11015398(_, arg_0_3: int, arg_4_7: int):
    """ 11015398: Event 11015398 """
    DisableCharacter(arg_4_7)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=2, switch_type=OnOffChange.Off)


def Event11010750(_, arg_0_3: int, arg_4_7: int):
    """ 11010750: Event 11010750 """
    IfFlagOff(1, 3)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11015380():
    """ 11015380: Event 11015380 """
    IfFlagOff(1, 11010901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012898,
        anchor_type=CoordEntityType.Region,
        line_intersects=1011890,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015381():
    """ 11015381: Event 11015381 """
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1011890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015383():
    """ 11015383: Event 11015383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010901)
    IfCharacterInsideRegion(1, PLAYER, region=1012896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1010700, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1010700)


@RestartOnRest
def Event11015382():
    """ 11015382: Event 11015382 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(1010700)
    End()
    DisableAI(1010700)
    SetStandbyAnimationSettings(1010700, standby_animation=9001)
    DisableHealthBar(1010700)
    IfAttacked(1, 1010700, attacking_character=PLAYER)
    IfHost(2)
    IfCharacterInsideRegion(2, PLAYER, region=1012701)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010005)
    ResetStandbyAnimationSettings(1010700)
    ForceAnimation(1010700, 9061, wait_for_completion=True)
    EnableAI(1010700)


def Event11015384():
    """ 11015384: Event 11015384 """
    DisableNetworkSync()
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015381)
    IfCharacterInsideRegion(1, PLAYER, region=1012890)
    IfConditionTrue(0, input_condition=1)
    EnableBossHealthBar(1010700, name=2250, slot=0)
    EnableSoundEvent(1013802)


def Event11015385():
    """ 11015385: Event 11015385 """
    DisableNetworkSync()
    IfFlagOn(1, 11015384)
    IfFlagOn(1, 11010901)
    IfConditionTrue(0, input_condition=1)
    DisableBossHealthBar(1010700, name=2250, slot=0)
    DisableSoundEvent(1013802)


def Event11015386():
    """ 11015386: Event 11015386 """
    EndIfClient()
    IfHasTAEEvent(1, 1010700, tae_event_id=700)
    IfHasTAEEvent(2, 1010700, tae_event_id=710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(1010700, destination=1012741, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(1010700, destination=1012740, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Restart()


@RestartOnRest
def Event11010901():
    """ 11010901: Event 11010901 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(1010700)
    Kill(1010700, award_souls=False)
    End()
    IfHealthLessThanOrEqual(0, 1010700, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1010700, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1010700)
    EnableFlag(11010901)
    KillBoss(1010700)
    DisableObject(1011890)
    DeleteFX(1011891, erase_root_only=True)
    DisableObject(1011892)
    DeleteFX(1011893, erase_root_only=True)


def Event11015370():
    """ 11015370: Event 11015370 """
    IfFlagOff(1, 11010902)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012888,
        anchor_type=CoordEntityType.Region,
        line_intersects=1011790,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11015371():
    """ 11015371: Event 11015371 """
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015373)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012888,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1011790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012887)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015373():
    """ 11015373: Event 11015373 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010902)
    IfCharacterInsideRegion(1, PLAYER, region=1012886)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1010750)
    EnableFlag(11010597)


@RestartOnRest
def Event11015372():
    """ 11015372: Event 11015372 """
    SkipLinesIfThisEventOn(5)
    DisableAI(1010750)
    IfFlagOn(1, 11015373)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010750)
    EnableBossHealthBar(1010750, name=2240, slot=0)


def Event11015374():
    """ 11015374: Event 11015374 """
    DisableNetworkSync()
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015372)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015371)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1013803)


def Event11015375():
    """ 11015375: Event 11015375 """
    DisableNetworkSync()
    IfFlagOn(1, 11015374)
    IfFlagOn(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013803)


@RestartOnRest
def Event11010902():
    """ 11010902: Event 11010902 """
    SkipLinesIfThisEventOff(7)
    DisableCharacter(1010750)
    DisableCharacter(1010500)
    DisableCharacter(1010501)
    Kill(1010750, award_souls=False)
    Kill(1010500, award_souls=False)
    Kill(1010501, award_souls=False)
    End()
    DisableCharacter(1010510)
    DisableCharacter(1010511)
    Kill(1010510, award_souls=False)
    Kill(1010511, award_souls=False)
    IfHealthLessThanOrEqual(0, 1010750, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1010750, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1010750)
    EnableFlag(11010902)
    KillBoss(1010750)
    DisableObject(1011790)
    DeleteFX(1011791, erase_root_only=True)


@RestartOnRest
def Event11010903():
    """ 11010903: Event 11010903 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1010310)
    End()
    IfCharacterDead(0, 1010310)
    EnableFlag(11010903)


@RestartOnRest
def Event11015110():
    """ 11015110: Event 11015110 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(1011103, slot=1)
    End()
    DisableAI(1010102)
    IfEntityWithinDistance(1, PLAYER, 1010102, radius=5.0)
    IfObjectDestroyed(2, 1011103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(1010102, 3000, wait_for_completion=True)
    EnableAI(1010102)


@RestartOnRest
def Event11015111():
    """ 11015111: Event 11015111 """
    EndIfThisEventOn()
    DisableAI(1010110)
    IfCharacterInsideRegion(1, PLAYER, region=1012110)
    IfAttacked(2, 1010110, attacking_character=PLAYER)
    IfEntityWithinDistance(3, 1010110, PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimation(1010110, 13005, wait_for_completion=True)
    EnableAI(1010110)


@RestartOnRest
def Event11015113():
    """ 11015113: Event 11015113 """
    EndIfThisEventOn()
    DisableAI(1010200)
    IfCharacterInsideRegion(-1, PLAYER, region=1012050)
    IfAttacked(-1, 1010200, attacking_character=PLAYER)
    IfEntityWithinDistance(-1, 1010200, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010200)


@RestartOnRest
def Event11015112():
    """ 11015112: Event 11015112 """
    EndIfThisEventOn()
    DisableAI(1010111)
    IfAttacked(-3, 1010111, attacking_character=PLAYER)
    IfCharacterInsideRegion(-3, PLAYER, region=1012122)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=1012121)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010111)
    EndIfFinishedConditionTrue(1)
    SetNest(1010111, 1012120)
    AICommand(1010111, command_id=10, slot=0)
    ReplanAI(1010111)
    IfCharacterInsideRegion(-2, PLAYER, region=1012122)
    IfAttacked(-2, 1010111, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1010111, command_id=-1, slot=0)
    ReplanAI(1010111)


@RestartOnRest
def Event11015130():
    """ 11015130: Event 11015130 """
    DisableCharacter(1010400)
    EndIfFlagOn(11010710)
    IfObjectDestroyed(0, 1011000)
    EnableCharacter(1010400)
    SkipLinesIfFlagOn(4, 11015130)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    SetNest(1010400, 1012060)
    AICommand(1010400, command_id=10, slot=0)
    ReplanAI(1010400)
    EnableFlag(11015130)
    IfCharacterInsideRegion(0, 1010400, region=1012060)
    AICommand(1010400, command_id=-1, slot=0)
    ReplanAI(1010400)


@RestartOnRest
def Event11010710():
    """ 11010710: Event 11010710 """
    DisableCharacter(1010400)
    EndIfFlagOn(11010710)
    IfCharacterDead(0, 1010400)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33006000, host_only=True)


@RestartOnRest
def Event11010111():
    """ 11010111: Event 11010111 """
    EndIfThisEventOn()
    DisableAI(1010130)
    IfAttacked(1, 1010130, attacking_character=PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=1012170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010111)
    EnableAI(1010130)
    EndIfFinishedConditionTrue(1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=3)
    Move(1010130, destination=1012171, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1010130, 7000)
    Wait(0.20000000298023224)
    ForceAnimation(1011318, 2, wait_for_completion=True)
    EnableFlag(61010518)
    DisableNetworkSync()
    Wait(4.0)
    DisableObjectActivation(1011318, obj_act_id=1318, relative_index=0)
    DisableObjectActivation(1011318, obj_act_id=1318, relative_index=1)
    EnableObjectActivation(1011318, obj_act_id=1318, relative_index=2)
    EnableObjectActivation(1011318, obj_act_id=1318, relative_index=3)


@RestartOnRest
def Event11010120():
    """ 11010120: Event 11010120 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1011102, 0)
    End()
    DisableAI(1010103)
    IfAttacked(-1, 1010103, attacking_character=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=1012101)
    IfConditionTrue(0, input_condition=-1)
    DisableNetworkSync()
    ResetAnimation(1010103, disable_interpolation=False)
    ForceAnimation(1010103, 3006)
    Wait(0.5)
    CreateObjectFX(100100, obj=1011102, model_point=1)
    ForceAnimation(1011102, 0)
    Wait(0.5)
    EnableAI(1010103)
    CreateHazard(
        11010121,
        1011102,
        model_point=1,
        behavior_param_id=5020,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=3.0,
        repetition_time=0.0,
    )
    Wait(3.0)
    DeleteObjectFX(1011102, erase_root=True)


def Event11010101(_, arg_0_3: int, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int):
    """ 11010101: Event 11010101 """
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_0_3, arg_4_7)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=arg_8_9,
        trigger_attribute=255,
    )
    Move(PLAYER, destination=arg_0_3, destination_type=CoordEntityType.Object, model_point=arg_12_15, short_move=True)
    ForceAnimation(PLAYER, arg_16_19)
    ForceAnimation(arg_0_3, arg_4_7)


def Event11010102(_, arg_0_3: int, arg_4_7: int, arg_8_9: short):
    """ 11010102: Event 11010102 """
    DisableNetworkSync()
    IfFlagOn(-1, arg_0_3)
    IfActionButton(
        -1,
        prompt_text=10010400,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=arg_8_9,
        trigger_attribute=255,
    )
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_0_3)
    DisplayDialog(
        10010161,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11010125():
    """ 11010125: Event 11010125 """
    EndIfThisEventOn()
    DisableCharacter(1010104)
    Move(1010104, destination=1012130, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    IfThisEventOn(0)
    EnableCharacter(1010104)


@RestartOnRest
def Event11010126():
    """ 11010126: Event 11010126 """
    EndIfThisEventOn()
    IfFlagOn(0, 51010030)
    EnableFlag(11010125)


@RestartOnRest
def Event11010130(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010130: Event 11010130 """
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_0_3, 2)
    End()
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(0, PLAYER, region=arg_8_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    ForceAnimation(arg_4_7, 7001)
    EnableAI(arg_4_7)
    Wait(0.10000000149011612)
    ForceAnimation(arg_0_3, 2)


def Event11010150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010150: Event 11010150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


def Event11010160(_, arg_0_3: int, arg_4_7: int):
    """ 11010160: Event 11010160 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    Wait(2.0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)


def Event11010180(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010180: Event 11010180 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11010170(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010170: Event 11010170 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11010140(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11010140: Event 11010140 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11010190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11010190: Event 11010190 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11010100():
    """ 11010100: Event 11010100 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1011149, 0)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011149)
    End()
    IfActionButton(
        0,
        prompt_text=10010500,
        anchor_entity=1011149,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=255,
    )
    EnableFlag(11010100)
    Move(PLAYER, destination=1011149, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1011149, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011149)


def Event11010400(_, arg_0_3: int, arg_4_7: int):
    """ 11010400: Event 11010400 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 101)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfObjectDestroyed(0, arg_4_7)
    ForceAnimation(arg_0_3, 101, wait_for_completion=True)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11015250(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 11015250: Event 11015250 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    IfEntityWithinDistance(0, PLAYER, arg_4_7, radius=arg_8_11)
    DisableNetworkSync()
    Wait(arg_12_15)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


def Event11015185():
    """ 11015185: Event 11015185 """
    IfFlagOn(1, 61010610)
    IfObjectActivated(1, obj_act_id=11010600)
    IfFlagOff(2, 61010610)
    IfObjectActivated(2, obj_act_id=11010600)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015180)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015181)
    Restart()
    EnableFlag(11015182)
    Restart()


def Event11010611():
    """ 11010611: Event 11010611 """
    DisableNetworkSync()
    IfFramesElapsed(1, 10)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1011100, obj_act_id=-1)


def Event11010600():
    """ 11010600: Event 11010600 """
    IfFlagOn(1, 11015181)
    IfHost(1)
    IfFlagOn(2, 11015182)
    IfHost(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015180)
    DisableFlag(11015181)
    DisableFlag(11015182)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(2, 61010610)
    RunEvent(11010611)
    Restart()
    EnableNavmeshType(1013100, NavmeshType.Solid)
    EnableFlag(11010605)
    ForceAnimation(1011101, 2)
    WaitFrames(60)
    RunEvent(11010611)
    Restart()
    SkipLinesIfFlagOff(2, 61010610)
    RunEvent(11010611)
    Restart()
    DisableNavmeshType(1013100, NavmeshType.Solid)
    ForceAnimation(1011101, 4)
    WaitFrames(200)
    RunEvent(11010611)
    Restart()


def Event11010601():
    """ 11010601: Event 11010601 """
    IfFlagOn(0, 11010605)
    DisableFlag(11010605)
    Wait(0.5)
    CreateHazard(
        11010602,
        1011101,
        model_point=42,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        11010603,
        1011101,
        model_point=43,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        11010604,
        1011101,
        model_point=44,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()


@RestartOnRest
def Event11015116():
    """ 11015116: Event 11015116 """
    IfFlagOff(1, 61010610)
    IfFlagOff(1, 11010607)
    IfFlagOff(1, 11010600)
    IfCharacterInsideRegion(1, PLAYER, region=1012200)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015115)
    IfFlagOn(-1, 11015181)
    IfFlagOn(-1, 61010610)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015115)


@RestartOnRest
def Event11010609():
    """ 11010609: Event 11010609 """
    DisableNetworkSync()
    IfFlagOn(1, 11015115)
    IfFlagOff(1, 61010610)
    IfConditionTrue(0, input_condition=1)
    ActivateObject(1011100, obj_act_id=-1, relative_index=-1)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event11010607():
    """ 11010607: Event 11010607 """
    SkipLinesIfThisEventOff(3)
    Move(6010, destination=1012201, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(6010, 1012201)
    End()
    IfCharacterInsideRegion(1, 6010, region=1012771)
    IfEntityWithinDistance(1, 6010, 1011100, radius=3.0)
    IfFlagOn(1, 11015181)
    IfConditionTrue(0, input_condition=1)
    SetNest(6010, 1012201)
    ClearTargetList(6010)
    ReplanAI(6010)


@RestartOnRest
def Event11010608():
    """ 11010608: Event 11010608 """
    IfFlagOn(1, 61010610)
    IfCharacterBackreadEnabled(1, 1010310)
    IfCharacterInsideRegion(1, 1010310, region=1012771)
    IfConditionTrue(0, input_condition=1)
    AICommand(1010310, command_id=1, slot=0)
    SetNest(1010310, 1012773)
    IfFlagOff(0, 61010610)
    AICommand(1010310, command_id=-1, slot=0)
    SetNest(1010310, 1012772)
    Restart()


def Event11010621():
    """ 11010621: Event 11010621 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1011121, 4)
    DisableObjectActivation(1011120, obj_act_id=-1)
    End()
    EndOfAnimation(1011121, 3)
    IfObjectActivated(0, obj_act_id=11010620)
    ForceAnimation(1011121, 4)


def Event11010700():
    """ 11010700: Event 11010700 """
    SkipLinesIfThisEventOff(2)
    DisableObjectActivation(1011110, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11010700)
    TriggerMultiplayerEvent(10010)
    IfHealthGreaterThan(0, PLAYER, 0.0)
    SkipLinesIfFlagOn(2, 11400200)
    PlayCutscene(100100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(2)
    PlayCutscene(100105, skippable=True, fade_out=False, player_id=PLAYER)
    EnableFlag(11500200)
    WaitFrames(1)
    AwardAchievement(29)


def Event11015170():
    """ 11015170: Event 11015170 """
    IfMultiplayerEvent(0, 10010)
    DisableNetworkSync()
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    Restart()


@RestartOnRest
def Event11010860(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010860: Event 11010860 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    SkipLinesIfEqual(4, left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)
    End()


def Event11010650(_, arg_0_3: int, arg_4_7: int):
    """ 11010650: Event 11010650 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11010899():
    """ 11010899: Event 11010899 """
    EnableImmortality(1010300)
    DisableCharacter(1010300)
    SetNest(1010300, 1012320)
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1010300, UpdateAuthority.Forced)
    DisableFlag(11010782)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    SkipLinesIfConditionFalse(6, 1)
    DisableFlag(11015310)
    EnableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013211)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    DisableCharacterCollision(1010300)
    DisableGravity(1010300)
    IfFlagOn(2, 11010791)
    IfFlagOn(2, 11015311)
    SkipLinesIfConditionFalse(4, 2)
    EnableCharacter(1010300)
    Move(1010300, destination=1012320, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ResetStandbyAnimationSettings(1010300)
    SetNest(1010300, 1012340)
    RunEvent(11010805, slot=0, args=(11015320, 11015325, 7004, 11015350))
    RunEvent(11010805, slot=1, args=(11015326, 11015331, 7008, 11015350))
    RunEvent(11010805, slot=2, args=(11015332, 11015333, 7009, 11015350))
    RunEvent(11010805, slot=3, args=(11015334, 11015337, 7011, 11015350))
    RunEvent(11010805, slot=4, args=(11015338, 11015339, 7006, 11015350))
    RunEvent(11010805, slot=5, args=(11015320, 11015323, 7009, 11015351))
    RunEvent(11010805, slot=6, args=(11015324, 11015339, 7006, 11015351))
    RunEvent(11010805, slot=7, args=(11015320, 11015323, 7011, 11015352))
    RunEvent(11010805, slot=8, args=(11015324, 11015339, 7006, 11015352))
    RunEvent(11010805, slot=9, args=(11015320, 11015321, 7004, 11015353))
    RunEvent(11010805, slot=10, args=(11015322, 11015333, 7008, 11015353))
    RunEvent(11010805, slot=11, args=(11015334, 11015335, 7009, 11015353))
    RunEvent(11010805, slot=12, args=(11015336, 11015337, 7011, 11015353))
    RunEvent(11010800, slot=0, args=(11015338, 11015339, 7010, 11015353))
    RunEvent(11010800, slot=1, args=(11015320, 11015339, 7010, 11015354))


@RestartOnRest
def Event11010900():
    """ 11010900: Event 11010900 """
    SkipLinesIfThisEventOff(4)
    DisableCharacter(1010300)
    DisableCharacter(1010301)
    DisableCharacter(1010302)
    End()
    IfHealthLessThan(7, 1010300, 0.10000000149011612)
    IfFlagOff(7, 11015312)
    IfFlagOff(7, 11015300)
    IfConditionTrue(1, input_condition=7)
    IfConditionTrue(2, input_condition=7)
    IfConditionTrue(3, input_condition=7)
    IfFlagOff(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(2, 11010791)
    IfFlagOff(2, 11015311)
    IfFlagOn(3, 11010791)
    IfFlagOn(3, 11015311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(3, 1)
    ForceAnimation(1010300, 7001, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    ForceAnimation(1010300, 7007, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    DisableImmortality(1010300)
    Kill(1010300, award_souls=True)


@RestartOnRest
def Event11010790():
    """ 11010790: Event 11010790 """
    DisableGravity(1010302)
    EnableInvincibility(1010302)
    DisableCharacter(1010302)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1010302, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=1012301)
    EnableFlag(11010790)
    SetNetworkUpdateRate(1010302, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableCollision(1013200)
    EnableCharacter(1010302)
    Move(1010302, destination=1012300, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1010302, 7012, wait_for_completion=True)
    DisableCharacter(1010302)
    EnableCollision(1013200)


def Event11010791():
    """ 11010791: Event 11010791 """
    EndIfThisEventOn()
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOff(1, 11010782)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfCharacterInsideRegion(1, PLAYER, region=1012305)
    IfAllPlayersOutsideRegion(1, region=1012337)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    EnableFlag(11010791)
    EnableFlag(11010780)
    EnableCharacter(1010300)
    Move(1010300, destination=1012302, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7005)
    WaitFrames(395)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DisableFlag(11015310)


def Event11010780():
    """ 11010780: Event 11010780 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1011290, 2)
    End()
    IfHasTAEEvent(0, 1010300, tae_event_id=1000)
    ForceAnimation(1011290, 1, wait_for_completion=True)
    ForceAnimation(1011290, 2, loop=True)


@RestartOnRest
def Event11010784():
    """ 11010784: Event 11010784 """
    IfHasTAEEvent(0, 1010300, tae_event_id=500)
    EnableFlag(11015300)
    IfHasTAEEvent(0, 1010300, tae_event_id=600)
    DisableFlag(11015300)
    Restart()


@RestartOnRest
def Event11015301():
    """ 11015301: Event 11015301 """
    DisableCharacter(1010301)
    IfCharacterBackreadEnabled(0, 1010300)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(1010300, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010300, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1010300, command_id=20, slot=0)
    End()
    CreateNPCPart(
        1010300,
        npc_part_id=3430,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, 1010300, npc_part_id=3430, value=0)
    IfFlagOff(1, 11015300)
    IfAttacked(1, 1010300, attacking_character=PLAYER)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfCharacterDead(2, 1010300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, 11015311)
    ForceAnimation(1010300, 8000)
    SkipLines(1)
    ForceAnimation(1010300, 8010)
    IfHasTAEEvent(0, 1010300, tae_event_id=400)
    SetDisplayMask(1010300, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010300, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        1010301,
        destination=1010300,
        destination_type=CoordEntityType.Character,
        model_point=66,
        copy_draw_parent=1010300,
    )
    EnableCharacter(1010301)
    ForceAnimation(1010301, 8100)
    AICommand(1010300, command_id=20, slot=0)
    ReplanAI(1010300)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34310000, host_only=True)


def Event11015302():
    """ 11015302: Event 11015302 """
    IfHost(-7)
    IfCharacterType(-7, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfConditionTrue(6, input_condition=1)
    IfConditionTrue(7, input_condition=1)
    IfFlagOn(2, 11010100)
    IfCharacterInsideRegion(2, PLAYER, region=1012330)
    IfCharacterInsideRegion(3, PLAYER, region=1012331)
    IfFlagOn(4, 11010100)
    IfCharacterInsideRegion(4, PLAYER, region=1012332)
    IfCharacterInsideRegion(5, PLAYER, region=1012333)
    IfFlagOn(6, 11015305)
    IfFlagOn(7, 11015317)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11015350)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11015351)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11015352)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(11015353)
    SkipLinesIfFinishedConditionTrue(2, 6)
    SkipLinesIfFinishedConditionTrue(1, 7)
    SkipLines(1)
    EnableFlag(11015354)
    DisableFlagRange((11015320, 11015339))
    SkipLinesIfClient(2)
    EnableRandomFlagInRange((11015320, 11015339))
    EnableFlag(11015313)
    Restart()


def Event11010805(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010805: Event 11010805 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfNotEqual(2, left=arg_8_11, right=7011)
    EnableFlag(11015312)
    AddSpecialEffect(1010300, 4160)
    SkipLinesIfEqual(1, left=arg_8_11, right=7006)
    ForceAnimation(1010300, arg_8_11)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7004)
    WaitFrames(190)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7006)
    WaitFrames(90)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7008)
    WaitFrames(200)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7009)
    WaitFrames(180)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7011)
    WaitFrames(192)
    CancelSpecialEffect(1010300, 4160)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015312)
    DisableFlag(11015310)
    Restart()


def Event11010800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010800: Event 11010800 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    EnableFlag(11015311)
    EnableCharacterCollision(1010300)
    EnableGravity(1010300)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ResetStandbyAnimationSettings(1010300)
    SetBackreadStateAlternate(1010300, state=True)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(1010300, 4160)
    ForceAnimation(1010300, arg_8_11)
    WaitFrames(111)
    CancelSpecialEffect(1010300, 4160)
    SetBackreadStateAlternate(1010300, state=False)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015317)
    DisableFlag(11015310)
    Restart()


def Event11010890(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 11010890: Event 11010890 """
    IfFlagOn(1, 11015313)
    IfFlagOn(2, 11015313)
    IfFlagOn(3, 11015313)
    IfFlagOn(4, 11015313)
    IfFlagOn(5, 11015313)
    IfFlagOn(6, 11015313)
    IfFlagOn(7, 11015313)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(2, arg_4_7)
    IfFlagOn(3, arg_8_11)
    IfFlagOn(4, arg_12_15)
    IfFlagOn(5, arg_16_19)
    IfFlagOn(6, arg_20_23)
    IfFlagOn(7, arg_24_27)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=6)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(0, input_condition=-7)
    DisableFlag(11015313)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(arg_0_3)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(arg_4_7)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(arg_8_11)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(arg_20_23)
    SkipLinesIfFinishedConditionFalse(1, 7)
    EnableFlag(arg_24_27)
    Restart()


def Event11015303():
    """ 11015303: Event 11015303 """
    IfFlagOff(1, 11015306)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11010100)
    IfCharacterInsideRegion(-7, PLAYER, region=1012332)
    IfCharacterInsideRegion(-7, PLAYER, region=1012335)
    IfCharacterInsideRegion(-7, PLAYER, region=1012336)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(2, 11015306)
    IfFlagOff(2, 11015311)
    IfFlagOn(2, 11010791)
    IfAllPlayersOutsideRegion(2, region=1012332)
    IfAllPlayersOutsideRegion(2, region=1012335)
    IfAllPlayersOutsideRegion(2, region=1012336)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015306)
    Restart()
    DisableFlag(11015306)
    RestartEvent(11015304, slot=0)
    Restart()


def Event11015304():
    """ 11015304: Event 11015304 """
    DisableNetworkSync()
    IfFlagOff(1, 11015305)
    IfFlagOn(1, 11015306)
    IfConditionTrue(0, input_condition=1)
    Wait(20.0)
    EnableFlag(11015305)
    Restart()


def Event11010850():
    """ 11010850: Event 11010850 """
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfAttacked(1, 1010300, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015317)
    Restart()


def Event11010851():
    """ 11010851: Event 11010851 """
    IfFlagOff(1, 11015316)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfAllPlayersOutsideRegion(1, region=1012338)
    IfHealthLessThan(1, 1010300, 0.699999988079071)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfFlagOn(2, 11015316)
    IfFlagOn(2, 11010791)
    IfCharacterInsideRegion(2, PLAYER, region=1012338)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015316)
    Restart()
    DisableFlag(11015316)
    RestartEvent(11010852, slot=0)
    Restart()


def Event11010852():
    """ 11010852: Event 11010852 """
    DisableNetworkSync()
    IfFlagOff(1, 11015315)
    IfFlagOn(1, 11015316)
    IfConditionTrue(0, input_condition=1)
    Wait(60.0)
    EnableFlag(11015315)
    Restart()


@RestartOnRest
def Event11015307():
    """ 11015307: Event 11015307 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    SetNest(1010300, 1012320)
    IfHasTAEEvent(0, 1010300, tae_event_id=700)
    Move(1010300, destination=1012340, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7016)
    WaitFrames(110)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    AICommand(1010300, command_id=-1, slot=1)
    DisableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    DisableFlag(11015305)
    DisableFlag(11015309)
    DisableFlag(11015311)
    Restart()


def Event11015308():
    """ 11015308: Event 11015308 """
    IfFlagOff(1, 11015309)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfAllPlayersOutsideRegion(1, region=1012334)
    IfFlagOn(2, 11015309)
    IfFlagOff(2, 11015310)
    IfFlagOn(2, 11010791)
    IfHealthGreaterThanOrEqual(2, 1010300, 0.10000000149011612)
    IfCharacterInsideRegion(2, PLAYER, region=1012334)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(11015309)
    AICommand(1010300, command_id=1, slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()
    DisableFlag(11015309)
    AICommand(1010300, command_id=-1, slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()


def Event11010782():
    """ 11010782: Event 11010782 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1012337)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(10)
    RestartIfFlagOn(11015311)
    EnableFlag(11015310)
    EnableFlag(11015312)
    DisableFlag(11010791)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(1010300, 7013, wait_for_completion=True)
    DisableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013210)


def Event11010783():
    """ 11010783: Event 11010783 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11015315)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    SetStandbyAnimationSettings(1010300, standby_animation=7018)
    ForceAnimation(1010300, 7017, wait_for_completion=True)
    IfHealthGreaterThanOrEqual(0, 1010300, 0.699999988079071)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7019)
    WaitFrames(50)
    DisableFlag(11015315)
    DisableFlag(11015316)
    DisableFlag(11015310)
    Restart()


def Event11010200(_, arg_0_3: int, arg_4_7: int):
    """ 11010200: Event 11010200 """
    IfCharacterBackreadEnabled(1, 1010300)
    IfHasTAEEvent(1, 1010300, tae_event_id=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    HellkiteBreathControl(1010300, obj=1011060, animation_id=arg_4_7)
    IfDoesNotHaveTAEEvent(0, 1010300, tae_event_id=arg_0_3)
    Restart()


def Event11010510(_, arg_0_3: int, arg_4_7: int):
    """ 11010510: Event 11010510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    RestartIfThisEventSlotOff()
    IfFlagOn(0, 744)
    EnableFlag(744)
    IfFlagOff(0, 744)
    Restart()


def Event11010520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010520: Event 11010520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11010501(_, arg_0_3: int, arg_4_7: int):
    """ 11010501: Event 11010501 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SetAIParamID(arg_0_3, 1)
    SaveRequest()
    RestartIfThisEventOff()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Restart()


def Event11010530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010530: Event 11010530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1000)
    IfFlagOn(1, 11010591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11010531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010531: Event 11010531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1008)
    IfFlagOn(1, 11510594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1012530, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013050)
    SetNest(arg_0_3, 1012530)
    EnableCharacter(arg_0_3)


def Event11010532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010532: Event 11010532 """
    IfFlagOff(1, 1114)
    IfFlagOn(1, 1110)
    IfFlagOn(1, 11010181)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)


def Event11010533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010533: Event 11010533 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfFlagOn(1, 11310590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    ClearEventValue(600, bit_count=4)


def Event11010534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010534: Event 11010534 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 724)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1176)
    IfFlagOff(2, 1177)
    IfFlagOff(2, 1179)
    IfFlagOff(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010535: Event 11010535 """
    IfFlagOff(1, 1176)
    IfFlagOn(-7, 1175)
    IfFlagOn(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11010537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010537: Event 11010537 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOff(1, 1196)
    IfFlagOff(1, 1198)
    IfEventValueComparison(1, 600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    IfThisEventOff(1)
    IfFlagOn(2, 703)
    IfFlagOn(3, 11010599)
    IfFlagOn(3, arg_12_15)
    IfThisEventOn(3)
    IfFlagOff(4, 11010599)
    IfFlagOn(4, arg_12_15)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, 3)
    SkipLinesIfFinishedConditionFalse(9, 1)
    EnableFlag(11010599)
    SkipLinesIfClient(3)
    EnableFlag(50006070)
    DisableFlag(50006071)
    DisableFlag(50006080)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DropMandatoryTreasure(arg_0_3)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11010538():
    """ 11010538: Event 11010538 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 11010596)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11010596)
    ClearEventValue(600, bit_count=4)
    Restart()


def Event11010539():
    """ 11010539: Event 11010539 """
    EndIfClient()
    IfFlagOn(1, 1177)
    IfFlagOn(1, 50006071)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(815)


def Event11010550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010550: Event 11010550 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(1, 11010190)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11010584)


def Event11010551():
    """ 11010551: Event 11010551 """
    EndIfFlagOn(11010593)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=3)
    IfFlagOn(0, 11010593)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=1)


def Event11010552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010552: Event 11010552 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(-1, 3)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010581(_, arg_0_3: int):
    """ 11010581: Event 11010581 """
    EndIfThisEventOn()
    IfFlagOn(0, 11010700)
    EnableCharacter(arg_0_3)


@RestartOnRest
def Event11010582():
    """ 11010582: Event 11010582 """
    SkipLinesIfClient(1)
    DisableFlag(11010586)
    SkipLinesIfFlagOn(4, 11010586)
    IfFlagOn(-1, 1175)
    IfFlagOn(-1, 1179)
    IfFlagOn(-1, 1181)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010586)
    DisableCharacter(1010320)


def Event11010583():
    """ 11010583: Event 11010583 """
    EndIfClient()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Wait(1.0)
    Move(6001, destination=1012010, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6001, standby_animation=7845)
    Move(6040, destination=1012011, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Move(6072, destination=1012012, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6072, standby_animation=7880)
    Move(6190, destination=1012013, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6190, standby_animation=9000)
    DisableFlag(11015090)
    RestoreObject(1011010)
    RestartEvent(11015090, slot=0)
    Move(6230, destination=1012014, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6230, standby_animation=9000)
    Move(6300, destination=1012015, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6300, standby_animation=7825)
    Restart()


def Event11010580():
    """ 11010580: Event 11010580 """
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(1, 11015030)
    IfFlagOff(1, 11015031)
    IfConditionTrue(2, input_condition=-7)
    IfFlagOff(2, 11015030)
    IfFlagOn(2, 11015031)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionFalse(9, 1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, 6480)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11015031)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11015031)
    Restart()


def Event11010585():
    """ 11010585: Event 11010585 """
    DisableNetworkSync()
    WaitFrames(2)
    EnableFlag(11010580)


@RestartOnRest
def Event11015090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11015090: Event 11015090 """
    EndIfFlagOn(arg_0_3)
    EndIfFlagOn(arg_4_7)
    EnableObjectInvulnerability(arg_8_11)
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(arg_8_11)
    WaitFrames(1)
    DestroyObject(arg_8_11, slot=1)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=125200000)
    EnableFlag(11015090)
    IfFlagOn(0, 703)
    End()


def Event11015100():
    """ 11015100: Event 11015100 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6540, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6001)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6540)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6540)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6540, region=1012000, summon_flag=11015102, dismissal_flag=11015106)
    DisableCharacter(6001)


def Event11015101():
    """ 11015101: Event 11015101 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015102)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6540, command_id=10, slot=0)
    ReplanAI(6540)
    IfCharacterInsideRegion(0, 6540, region=1012998)
    RotateToFaceEntity(6540, 1012997)
    ForceAnimation(6540, 7410)
    AICommand(6540, command_id=-1, slot=0)
    ReplanAI(6540)


def Event11015103():
    """ 11015103: Event 11015103 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6590, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6590)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, 6590)
    IfEntityWithinDistance(1, 6590, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6590, region=1012001, summon_flag=11015105, dismissal_flag=11015107)


def Event11015203():
    """ 11015203: Event 11015203 """
    IfFlagOn(0, 11015105)
    AddSpecialEffect(6590, 5450)


def Event11015104():
    """ 11015104: Event 11015104 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015105)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6590, command_id=10, slot=0)
    ReplanAI(6590)
    IfCharacterInsideRegion(0, 6590, region=1012998)
    RotateToFaceEntity(6590, 1012997)
    ForceAnimation(6590, 7410)
    AICommand(6590, command_id=-1, slot=0)
    ReplanAI(6590)


def Event11015900():
    """ 11015900: Event 11015900 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6540, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6001)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6540)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6540)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6540, region=1012000, summon_flag=11015102, dismissal_flag=11015106)
    DisableCharacter(6001)


def Event11015901():
    """ 11015901: Event 11015901 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6590, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6590)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, 6590)
    IfEntityWithinDistance(1, 6590, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6590, region=1012001, summon_flag=11015105, dismissal_flag=11015107)


def Event11015990(_, arg_0_3: int, arg_4_7: int):
    """ 11015990: Event 11015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11015843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11015843: Event 11015843 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_4_7,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


def Event11015846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11015846: Event 11015846 """
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateFX(arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteFX(arg_8_11, erase_root_only=True)
    Restart()
