"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11010008()
    DisableFlag(11010580)
    SkipLinesIfFlagDisabled(2, 61010610)
    EndOfAnimation(obj=1011101, animation_id=2)
    EnableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
    SkipLinesIfClient(22)
    DisableObject(1011994)
    DeleteVFX(1011995, erase_root_only=False)
    DisableObject(1011996)
    DeleteVFX(1011997, erase_root_only=False)
    DisableObject(1011998)
    DeleteVFX(1011999, erase_root_only=False)
    DisableObject(1011988)
    DeleteVFX(1011989, erase_root_only=False)
    DisableObject(1011986)
    DeleteVFX(1011987, erase_root_only=False)
    DisableObject(1011984)
    DeleteVFX(1011985, erase_root_only=False)
    DisableObject(1011982)
    DeleteVFX(1011983, erase_root_only=False)
    DisableObject(1011980)
    DeleteVFX(1011981, erase_root_only=False)
    DisableObject(1011978)
    DeleteVFX(1011979, erase_root_only=False)
    DisableObject(1011976)
    DeleteVFX(1011977, erase_root_only=False)
    DisableObject(1011974)
    DeleteVFX(1011975, erase_root_only=False)
    Event_11010090(0, line_intersects__obj=1011700, vfx_id=1011701, destination=1012600, destination_1=1012601)
    Event_11010090(1, line_intersects__obj=1011702, vfx_id=1011703, destination=1012602, destination_1=1012603)
    Event_11015070()
    Event_11015071()
    Event_11015072()
    Event_11010903()
    Event_11015110()
    Event_11015113()
    Event_11015112()
    Event_11015130()
    Event_11010710()
    Event_11010111()
    Event_11010120()
    Event_11010150(0, flag=11010160, region=1012401, region_1=1012400)
    Event_11010160(0, obj_act_id=11010160, obj=1011314)
    Event_11010170(1, obj_act_id=11010171, text=10010873, obj=1011306)
    Event_11010170(2, obj_act_id=11010172, text=10010860, obj=1011311)
    Event_11010180(1, obj_act_id=11010181, text=10010881, anchor_entity=1011317)
    Event_11010140(0, obj_act_id=11010140, text=10010881, anchor_entity=1011310, text_1=10010883, item=2021)
    Event_11010190(0, obj_act_id=11010190, text=10010876, obj=1011308, text_1=10010883, item=2017)
    Event_11010190(1, obj_act_id=11010191, text=10010878, obj=1011315, text_1=10010883, item=2019)
    Event_11010190(2, obj_act_id=11010192, text=10010878, obj=1011316, text_1=10010883, item=2019)
    Event_11010101(0, obj=1011320, animation_id=1, model_point=101, model_point_1=121, animation_id_1=7110)
    Event_11010102(0, flag=11010142, anchor_entity=1011320, model_point=100)
    Event_11015185()
    Event_11010611()
    Event_11010600()
    Event_11010601()
    Event_11015116()
    Event_11010609()
    Event_11010607()
    Event_11010608()
    Event_11010621()
    Event_11010700()
    Event_11015170()
    Event_11010100()
    Event_11010780()
    Event_11010580()
    Event_11010585()
    DisableSoundEvent(sound_id=1013800)
    SkipLinesIfFlagEnabled(1, 3)
    DisableSoundEvent(sound_id=1013801)
    SkipLinesIfFlagDisabled(6, 3)
    Event_11015392()
    DisableObject(1011990)
    DeleteVFX(1011991, erase_root_only=False)
    DisableObject(1011992)
    DeleteVFX(1011993, erase_root_only=False)
    SkipLines(11)
    Event_11010000()
    Event_11015390()
    Event_11015391()
    Event_11015393()
    Event_11015392()
    Event_11010001()
    Event_11015394()
    Event_11015395()
    Event_11015396()
    Event_11010750(0, character=1010800, item_lot_param_id=53500000)
    Event_11010750(1, character=1010801, item_lot_param_id=53500100)
    Event_11015397(0, character=1010800, npc_part_id=5350, npc_part_id_1=5350, character_1=1010810)
    Event_11015398(0, character=1010801, character_1=1010811)
    DisableSoundEvent(sound_id=1013802)
    SkipLinesIfFlagDisabled(6, 11010901)
    Event_11010901()
    DisableObject(1011890)
    DeleteVFX(1011891, erase_root_only=False)
    DisableObject(1011892)
    DeleteVFX(1011893, erase_root_only=False)
    SkipLines(8)
    Event_11015380()
    Event_11015381()
    Event_11015383()
    Event_11015382()
    Event_11015384()
    Event_11015385()
    Event_11015386()
    Event_11010901()
    DisableSoundEvent(sound_id=1013803)
    SkipLinesIfFlagDisabled(4, 11010902)
    Event_11010902()
    DisableObject(1011790)
    DeleteVFX(1011791, erase_root_only=False)
    SkipLines(7)
    Event_11015370()
    Event_11015371()
    Event_11015373()
    Event_11015372()
    Event_11015374()
    Event_11015375()
    Event_11010902()
    SkipLinesIfFlagDisabled(2, 11010900)
    Event_11010900()
    SkipLines(29)
    Event_11010899()
    Event_11010900()
    Event_11010782()
    Event_11010783()
    Event_11010790()
    Event_11010791()
    Event_11015301()
    Event_11010784()
    Event_11015302()
    Event_11015303()
    Event_11015304()
    Event_11010851()
    Event_11010852()
    Event_11010890(
        0,
        flag=11015320,
        flag_1=11015321,
        flag_2=11015322,
        flag_3=11015323,
        flag_4=11015324,
        flag_5=11015325,
        flag_6=11015326
    )
    Event_11010890(
        1,
        flag=11015327,
        flag_1=11015328,
        flag_2=11015329,
        flag_3=11015330,
        flag_4=11015331,
        flag_5=11015332,
        flag_6=11015333
    )
    Event_11010890(
        2,
        flag=11015334,
        flag_1=11015335,
        flag_2=11015336,
        flag_3=11015337,
        flag_4=11015338,
        flag_5=11015339,
        flag_6=11015340
    )
    Event_11010850()
    Event_11015307()
    Event_11015308()
    Event_11010200(0, tae_event_id=10, animation_id=3000)
    Event_11010200(1, tae_event_id=20, animation_id=3001)
    Event_11010200(2, tae_event_id=30, animation_id=3002)
    Event_11010200(3, tae_event_id=40, animation_id=3009)
    Event_11010200(4, tae_event_id=50, animation_id=3010)
    Event_11010200(5, tae_event_id=60, animation_id=7004)
    Event_11010200(6, tae_event_id=70, animation_id=7005)
    Event_11010200(7, tae_event_id=80, animation_id=7008)
    Event_11010200(8, tae_event_id=90, animation_id=7009)
    Event_11010200(9, tae_event_id=100, animation_id=7011)
    Event_11015250(0, 1010250, 1010250, 5.0, 0.0)
    Event_11015250(1, 1010251, 1010250, 5.5, 0.0)
    Event_11015250(2, 1010260, 1010260, 5.0, 0.0)
    Event_11015250(3, 1010261, 1010260, 4.0, 0.0)
    Event_11015250(4, 1010262, 1010260, 3.0, 0.0)
    Event_11015250(5, 1010263, 1010260, 3.0, 0.0)
    Event_11010130(0, obj=1011250, character=1010150, region=1012150)
    Event_11010130(1, obj=1011251, character=1010151, region=1012150)
    Event_11010130(2, obj=1011252, character=1010152, region=1012150)
    Event_11010130(3, obj=1011253, character=1010153, region=1012151)
    Event_11010130(4, obj=1011254, character=1010154, region=1012151)
    Event_11010130(5, obj=1011255, character=1010155, region=1012151)
    Event_11010860(0, character=6580, left=0, item_lot_param_id=0)
    Event_11010860(1, character=1010350, left=1, item_lot_param_id=27900000)
    Event_11010860(2, character=1010351, left=1, item_lot_param_id=27900100)
    Event_11010860(3, character=1010320, left=0, item_lot_param_id=0)
    Event_11010860(4, character=1010340, left=0, item_lot_param_id=0)
    Event_11010860(5, character=1010370, left=0, item_lot_param_id=0)
    Event_11010860(6, character=6010, left=0, item_lot_param_id=0)
    Event_11010400(2, obj=1011652, obj_1=1011502)
    Event_11010400(3, obj=1011653, obj_1=1011503)
    Event_11010400(4, obj=1011654, obj_1=1011504)
    Event_11010650(0, obj=1011670, obj_act_id=11010650)
    Event_11010650(1, 1011671, 11010651)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11010583()
    HumanityRegistration(6580, event_flag=8972)
    HumanityRegistration(6540, event_flag=8310)
    HumanityRegistration(6590, event_flag=8462)
    Event_11015100()
    Event_11015101()
    Event_11015103()
    Event_11015104()
    HumanityRegistration(6001, event_flag=8310)
    SkipLinesIfFlagEnabled(4, 1007)
    SkipLinesIfFlagEnabled(3, 1004)
    SkipLinesIfFlagEnabled(2, 1001)
    SkipLinesIfFlagEnabled(1, 1000)
    DisableCharacter(6001)
    SkipLinesIfFlagEnabled(1, 11510594)
    SkipLines(1)
    Move(6001, destination=1012530, destination_type=CoordEntityType.Region, set_draw_parent=1013050)
    Event_11010510(0, character=6001, flag=1004)
    Event_11010520(0, character=6001, first_flag=1000, last_flag=1029, flag=1005)
    Event_11010530(0, character=6001, first_flag=1000, last_flag=1029, flag=1001)
    Event_11010531(0, character=6001, first_flag=1000, last_flag=1029, flag=1007)
    HumanityRegistration(6040, event_flag=8342)
    SkipLinesIfFlagRangeAllDisabled(1, (1112, 1113))
    DisableCharacter(6040)
    Event_11010510(1, character=6040, flag=1114)
    Event_11010520(1, character=6040, first_flag=1110, last_flag=1119, flag=1115)
    Event_11010532(0, character=6040, first_flag=1110, last_flag=1119, flag=1111)
    HumanityRegistration(6072, event_flag=8358)
    SkipLinesIfFlagEnabled(1, 1175)
    DisableCharacter(6072)
    Event_11010533(0, character=6072, first_flag=1170, last_flag=1189, flag=1175)
    Event_11010501(0, character=6072, flag=1179)
    Event_11010535(0, character=6072, first_flag=1170, last_flag=1189, flag=1180)
    Event_11010534(0, character=6072, first_flag=1170, last_flag=1189, flag=1181)
    Event_11010537(0, character=6072, first_flag=1170, last_flag=1189, flag=1177)
    Event_11010538()
    Event_11010539()
    Event_11010582()
    Event_11010510(3, character=6190, flag=1321)
    Event_11010520(3, character=6190, first_flag=1320, last_flag=1339, flag=1322)
    Event_11015090(0, flag=1321, flag_1=1322, obj=1011010)
    Event_11010510(4, character=6230, flag=1401)
    Event_11010520(4, character=6230, first_flag=1400, last_flag=1409, flag=1402)
    HumanityRegistration(6300, event_flag=8462)
    SkipLinesIfClient(1)
    DisableFlag(11010584)
    SkipLinesIfFlagEnabled(3, 11010584)
    SkipLinesIfFlagEnabled(2, 1574)
    SkipLinesIfFlagEnabled(1, 1570)
    DisableCharacter(6300)
    Event_11010510(6, character=6300, flag=1574)
    Event_11010520(6, character=6300, first_flag=1570, last_flag=1599, flag=1575)
    Event_11010550(0, character=6300, first_flag=1570, last_flag=1599, flag=1571)
    Event_11010552(0, character=6300, first_flag=1570, last_flag=1599, flag=1577)
    Event_11010551()
    HumanityRegistration(6370, event_flag=8486)
    SkipLinesIfFlagEnabled(1, 11010581)
    DisableCharacter(6370)
    Event_11010510(7, character=6370, flag=1701)
    Event_11010520(7, character=6370, first_flag=1700, last_flag=1709, flag=1702)
    Event_11010581(0, 6370)


@NeverRestart(11010008)
def Event_11010008():
    """Event 11010008"""
    RegisterBonfire(bonfire_flag=11010984, obj=1011961)
    RegisterBonfire(bonfire_flag=11010976, obj=1011962)
    RegisterBonfire(bonfire_flag=11010960, obj=1011964)
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
        obj_flag=11010300,
        obj=1011450,
        model_point=200,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=11010308,
        obj=1011407,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=11010309,
        obj=1011408,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )


@NeverRestart(11010090)
def Event_11010090(_, line_intersects__obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11010090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        line_intersects=line_intersects__obj,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        line_intersects=line_intersects__obj,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11015070)
def Event_11015070():
    """Event 11015070"""
    EndIfThisEventFlagEnabled()
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
    IfFlagEnabled(0, 11010050)
    EndIfFlagEnabled(735)
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


@RestartOnRest(11015071)
def Event_11015071():
    """Event 11015071"""
    IfFlagEnabled(-1, 11015075)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11010050)
    DisableFlag(11015075)
    EnableFlag(5001)
    Kill(1010900)
    Kill(1010901)
    Kill(1010902)
    Kill(1010903)
    Kill(1010904)
    Kill(1010905)
    Kill(1010906)
    Kill(1010907)
    Kill(1010908)
    Kill(1010909)
    Kill(1010910)
    Kill(1010911)
    Kill(1010912)


@RestartOnRest(11015072)
def Event_11015072():
    """Event 11015072"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11010050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=UNDEAD_BURG)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11010050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=UNDEAD_BURG)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11010050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=UNDEAD_BURG)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11010050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=UNDEAD_BURG)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11010050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=UNDEAD_BURG)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11010050)
    RestartIfConditionFalse(-6)
    EnableFlag(11010050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=UNDEAD_BURG)
    RestartIfConditionFalse(7)
    DisableFlag(11010050)
    EnableFlag(11015075)


@RestartOnRest(11010000)
def Event_11010000():
    """Event 11010000"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1010802)
    End()
    DisableAI(1010802)
    SetStandbyAnimationSettings(1010802, standby_animation=7000)
    EnableInvincibility(1010802)
    DisableHealthBar(1010802)
    DisableCharacter(1010800)
    IfFlagEnabled(1, 11015390)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1012999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100110, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(100110, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1010802)
    EnableCharacter(1010800)


@NeverRestart(11015390)
def Event_11015390():
    """Event 11015390"""
    IfFlagDisabled(1, 3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1011990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11015391)
def Event_11015391():
    """Event 11015391"""
    IfFlagDisabled(1, 3)
    IfFlagEnabled(1, 11015393)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1011990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11015393)
def Event_11015393():
    """Event 11015393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 3)
    IfCharacterInsideRegion(1, PLAYER, region=1012996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1010800)


@RestartOnRest(11015392)
def Event_11015392():
    """Event 11015392"""
    SkipLinesIfFlagDisabled(11, 3)
    DisableCharacter(1010800)
    DisableCharacter(1010801)
    DisableCharacter(1010802)
    DisableCharacter(1010810)
    DisableCharacter(1010811)
    Kill(1010800)
    Kill(1010801)
    Kill(1010802)
    Kill(1010810)
    Kill(1010811)
    End()
    DisableAI(1010800)
    IfFlagEnabled(1, 11010000)
    IfFlagEnabled(1, 11015393)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010800)
    EnableBossHealthBar(1010800, name=5350)


@NeverRestart(11010001)
def Event_11010001():
    """Event 11010001"""
    IfCharacterDead(1, 1010800)
    IfCharacterDead(2, 1010801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(3, 1010800)
    IfCharacterDead(3, 1010801)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(3)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    PlaySoundEffect(1010800, 777777777, sound_type=SoundType.s_SFX)
    SkipLines(1)
    PlaySoundEffect(1010801, 777777777, sound_type=SoundType.s_SFX)
    KillBoss(game_area_param_id=1010800)
    DisableObject(1011990)
    DeleteVFX(1011991)
    DisableObject(1011992)
    DeleteVFX(1011993)


@NeverRestart(11015394)
def Event_11015394():
    """Event 11015394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 3)
    IfFlagEnabled(1, 11010000)
    IfFlagEnabled(1, 11015392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11015391)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1013801)
    EnableSoundEvent(sound_id=1013800)


@NeverRestart(11015395)
def Event_11015395():
    """Event 11015395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11015394)
    IfFlagEnabled(1, 3)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1013800)
    EnableSoundEvent(sound_id=1013801)


@RestartOnRest(11015396)
def Event_11015396():
    """Event 11015396"""
    EndIfFlagEnabled(3)
    DisableAI(1010801)
    SetStandbyAnimationSettings(1010801, standby_animation=7000)
    EnableInvincibility(1010801)
    DisableHealthBar(1010801)
    IfHealthLessThanOrEqual(0, 1010800, value=0.6000000238418579)
    SetStandbyAnimationSettings(1010801)
    Move(1010801, destination=1012650, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1010801, 7001, wait_for_completion=True)
    DisableInvincibility(1010801)
    EnableAI(1010801)
    EnableBossHealthBar(1010801, name=5350, bar_slot=1)


@RestartOnRest(11015397)
def Event_11015397(_, character: int, npc_part_id: short, npc_part_id_1: int, character_1: int):
    """Event 11015397"""
    DisableCharacter(character_1)
    SkipLinesIfThisEventSlotFlagDisabled(5)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, 5434)
    AICommand(character, command_id=20, command_slot=0)
    End()
    IfFlagEnabled(1, 11015392)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=65)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=130,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    ForceAnimation(character_1, 8100)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, 5434)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(53520000, host_only=True)


@RestartOnRest(11015398)
def Event_11015398(_, character: int, character_1: int):
    """Event 11015398"""
    DisableCharacter(character_1)
    IfCharacterBackreadEnabled(0, character)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=2, switch_type=OnOffChange.Off)


@NeverRestart(11010750)
def Event_11010750(_, character: int, item_lot_param_id: int):
    """Event 11010750"""
    IfFlagDisabled(1, 3)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, character)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(11015380)
def Event_11015380():
    """Event 11015380"""
    IfFlagDisabled(1, 11010901)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1011890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11015381)
def Event_11015381():
    """Event 11015381"""
    IfFlagDisabled(1, 11010901)
    IfFlagEnabled(1, 11015383)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1011890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11015383)
def Event_11015383():
    """Event 11015383"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11010901)
    IfCharacterInsideRegion(1, PLAYER, region=1012896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1010700, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1010700)


@RestartOnRest(11015382)
def Event_11015382():
    """Event 11015382"""
    SkipLinesIfThisEventFlagDisabled(2)
    SetStandbyAnimationSettings(1010700)
    End()
    DisableAI(1010700)
    SetStandbyAnimationSettings(1010700, standby_animation=9001)
    DisableHealthBar(1010700)
    IfAttacked(1, attacked_entity=1010700, attacker=PLAYER)
    IfHost(2)
    IfCharacterInsideRegion(2, PLAYER, region=1012701)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010005)
    SetStandbyAnimationSettings(1010700)
    ForceAnimation(1010700, 9061, wait_for_completion=True)
    EnableAI(1010700)


@NeverRestart(11015384)
def Event_11015384():
    """Event 11015384"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11010901)
    IfFlagEnabled(1, 11015382)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11015381)
    IfCharacterInsideRegion(1, PLAYER, region=1012890)
    IfConditionTrue(0, input_condition=1)
    EnableBossHealthBar(1010700, name=2250)
    EnableSoundEvent(sound_id=1013802)


@NeverRestart(11015385)
def Event_11015385():
    """Event 11015385"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11015384)
    IfFlagEnabled(1, 11010901)
    IfConditionTrue(0, input_condition=1)
    DisableBossHealthBar(1010700, name=2250)
    DisableSoundEvent(sound_id=1013802)


@NeverRestart(11015386)
def Event_11015386():
    """Event 11015386"""
    EndIfClient()
    IfCharacterHasTAEEvent(1, 1010700, tae_event_id=700)
    IfCharacterHasTAEEvent(2, 1010700, tae_event_id=710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(1010700, destination=1012741, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(1010700, destination=1012740, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@RestartOnRest(11010901)
def Event_11010901():
    """Event 11010901"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableCharacter(1010700)
    Kill(1010700)
    End()
    IfHealthLessThanOrEqual(0, 1010700, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1010700, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1010700)
    EnableFlag(11010901)
    KillBoss(game_area_param_id=1010700)
    DisableObject(1011890)
    DeleteVFX(1011891)
    DisableObject(1011892)
    DeleteVFX(1011893)


@NeverRestart(11015370)
def Event_11015370():
    """Event 11015370"""
    IfFlagDisabled(1, 11010902)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012888,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1011790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart(11015371)
def Event_11015371():
    """Event 11015371"""
    IfFlagDisabled(1, 11010902)
    IfFlagEnabled(1, 11015373)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1012888,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1011790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1012887)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11015373)
def Event_11015373():
    """Event 11015373"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11010902)
    IfCharacterInsideRegion(1, PLAYER, region=1012886)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1010750)
    EnableFlag(11010597)


@RestartOnRest(11015372)
def Event_11015372():
    """Event 11015372"""
    SkipLinesIfThisEventFlagEnabled(5)
    DisableAI(1010750)
    IfFlagEnabled(1, 11015373)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010750)
    EnableBossHealthBar(1010750, name=2240)


@NeverRestart(11015374)
def Event_11015374():
    """Event 11015374"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11010902)
    IfFlagEnabled(1, 11015372)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11015371)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1013803)


@NeverRestart(11015375)
def Event_11015375():
    """Event 11015375"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11015374)
    IfFlagEnabled(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1013803)


@RestartOnRest(11010902)
def Event_11010902():
    """Event 11010902"""
    SkipLinesIfThisEventFlagDisabled(7)
    DisableCharacter(1010750)
    DisableCharacter(1010500)
    DisableCharacter(1010501)
    Kill(1010750)
    Kill(1010500)
    Kill(1010501)
    End()
    DisableCharacter(1010510)
    DisableCharacter(1010511)
    Kill(1010510)
    Kill(1010511)
    IfHealthLessThanOrEqual(0, 1010750, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1010750, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1010750)
    EnableFlag(11010902)
    KillBoss(game_area_param_id=1010750)
    DisableObject(1011790)
    DeleteVFX(1011791)


@RestartOnRest(11010903)
def Event_11010903():
    """Event 11010903"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1010310)
    End()
    IfCharacterDead(0, 1010310)
    EnableFlag(11010903)


@RestartOnRest(11015110)
def Event_11015110():
    """Event 11015110"""
    SkipLinesIfThisEventFlagDisabled(2)
    PostDestruction(1011103)
    End()
    DisableAI(1010102)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=1010102, radius=5.0)
    IfObjectDestroyed(2, 1011103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(1010102, 3000, wait_for_completion=True)
    EnableAI(1010102)


@RestartOnRest(11015111)
def Event_11015111():
    """Event 11015111"""
    EndIfThisEventFlagEnabled()
    DisableAI(1010110)
    IfCharacterInsideRegion(1, PLAYER, region=1012110)
    IfAttacked(2, attacked_entity=1010110, attacker=PLAYER)
    IfEntityWithinDistance(3, entity=1010110, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    ForceAnimation(1010110, 13005, wait_for_completion=True)
    EnableAI(1010110)


@RestartOnRest(11015113)
def Event_11015113():
    """Event 11015113"""
    EndIfThisEventFlagEnabled()
    DisableAI(1010200)
    IfCharacterInsideRegion(-1, PLAYER, region=1012050)
    IfAttacked(-1, attacked_entity=1010200, attacker=PLAYER)
    IfEntityWithinDistance(-1, entity=1010200, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010200)


@RestartOnRest(11015112)
def Event_11015112():
    """Event 11015112"""
    EndIfThisEventFlagEnabled()
    DisableAI(1010111)
    IfAttacked(-3, attacked_entity=1010111, attacker=PLAYER)
    IfCharacterInsideRegion(-3, PLAYER, region=1012122)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=1012121)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010111)
    EndIfFinishedConditionTrue(input_condition=1)
    SetNest(1010111, region=1012120)
    AICommand(1010111, command_id=10, command_slot=0)
    ReplanAI(1010111)
    IfCharacterInsideRegion(-2, PLAYER, region=1012122)
    IfAttacked(-2, attacked_entity=1010111, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1010111, command_id=-1, command_slot=0)
    ReplanAI(1010111)


@RestartOnRest(11015130)
def Event_11015130():
    """Event 11015130"""
    DisableCharacter(1010400)
    EndIfFlagEnabled(11010710)
    IfObjectDestroyed(0, 1011000)
    EnableCharacter(1010400)
    SkipLinesIfFlagEnabled(4, 11015130)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    SetNest(1010400, region=1012060)
    AICommand(1010400, command_id=10, command_slot=0)
    ReplanAI(1010400)
    EnableFlag(11015130)
    IfCharacterInsideRegion(0, 1010400, region=1012060)
    AICommand(1010400, command_id=-1, command_slot=0)
    ReplanAI(1010400)


@RestartOnRest(11010710)
def Event_11010710():
    """Event 11010710"""
    DisableCharacter(1010400)
    EndIfFlagEnabled(11010710)
    IfCharacterDead(0, 1010400)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33006000, host_only=True)


@RestartOnRest(11010111)
def Event_11010111():
    """Event 11010111"""
    EndIfThisEventFlagEnabled()
    DisableAI(1010130)
    IfAttacked(1, attacked_entity=1010130, attacker=PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=1012170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010111)
    EnableAI(1010130)
    EndIfFinishedConditionTrue(input_condition=1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=3)
    Move(1010130, destination=1012171, destination_type=CoordEntityType.Region, short_move=True)
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


@RestartOnRest(11010120)
def Event_11010120():
    """Event 11010120"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1011102, animation_id=0)
    End()
    DisableAI(1010103)
    IfAttacked(-1, attacked_entity=1010103, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=1012101)
    IfConditionTrue(0, input_condition=-1)
    DisableNetworkSync()
    ResetAnimation(1010103)
    ForceAnimation(1010103, 3006)
    Wait(0.5)
    CreateObjectVFX(1011102, vfx_id=1, model_point=100100)
    ForceAnimation(1011102, 0)
    Wait(0.5)
    EnableAI(1010103)
    CreateHazard(
        obj_flag=11010121,
        obj=1011102,
        model_point=1,
        behavior_param_id=5020,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=3.0,
        repetition_time=0.0,
    )
    Wait(3.0)
    DeleteObjectVFX(1011102)


@NeverRestart(11010101)
def Event_11010101(_, obj: int, animation_id: int, model_point: short, model_point_1: int, animation_id_1: int):
    """Event 11010101"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=model_point,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=model_point_1, short_move=True)
    ForceAnimation(PLAYER, animation_id_1)
    ForceAnimation(obj, animation_id)


@NeverRestart(11010102)
def Event_11010102(_, flag: int, anchor_entity: int, model_point: short):
    """Event 11010102"""
    DisableNetworkSync()
    IfFlagEnabled(-1, flag)
    IfActionButton(
        -1,
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=model_point,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(flag)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    Restart()


@RestartOnRest(11010125)
def Event_11010125():
    """Event 11010125"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1010104)
    Move(1010104, destination=1012130, destination_type=CoordEntityType.Region, short_move=True)
    IfThisEventFlagEnabled(0)
    EnableCharacter(1010104)


@RestartOnRest(11010126)
def Event_11010126():
    """Event 11010126"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 51010030)
    EnableFlag(11010125)


@RestartOnRest(11010130)
def Event_11010130(_, obj: int, character: int, region: int):
    """Event 11010130"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EndOfAnimation(obj=obj, animation_id=2)
    End()
    DisableAI(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    ForceAnimation(character, 7001)
    EnableAI(character)
    Wait(0.10000000149011612)
    ForceAnimation(obj, 2)


@NeverRestart(11010150)
def Event_11010150(_, flag: int, region: int, region_1: int):
    """Event 11010150"""
    DisableNetworkSync()
    SkipLinesIfFlagEnabled(4, flag)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11010160)
def Event_11010160(_, obj_act_id: int, obj: int):
    """Event 11010160"""
    SkipLinesIfThisEventSlotFlagDisabled(5)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EnableFlag(obj_act_id)
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@NeverRestart(11010180)
def Event_11010180(_, obj_act_id: int, text: int, anchor_entity: int):
    """Event 11010180"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EndIfClient()
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@NeverRestart(11010170)
def Event_11010170(_, obj_act_id: int, text: int, obj: int):
    """Event 11010170"""
    SkipLinesIfThisEventSlotFlagDisabled(5)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EnableFlag(obj_act_id)
    EndIfClient()
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@NeverRestart(11010140)
def Event_11010140(_, obj_act_id: int, text: int, anchor_entity: int, text_1: int, item: int):
    """Event 11010140"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EndIfClient()
    IfPlayerHasGood(1, item)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(text=text_1, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@NeverRestart(11010190)
def Event_11010190(_, obj_act_id: int, text: int, obj: int, text_1: int, item: int):
    """Event 11010190"""
    SkipLinesIfThisEventSlotFlagDisabled(5)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EnableFlag(obj_act_id)
    EndIfClient()
    IfPlayerHasGood(1, item)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(text=text_1, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@NeverRestart(11010100)
def Event_11010100():
    """Event 11010100"""
    SkipLinesIfThisEventFlagDisabled(3)
    EndOfAnimation(obj=1011149, animation_id=0)
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
        trigger_attribute=TriggerAttribute.All,
    )
    EnableFlag(11010100)
    Move(PLAYER, destination=1011149, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1011149, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011149)


@NeverRestart(11010400)
def Event_11010400(_, obj: int, obj_1: int):
    """Event 11010400"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(obj=obj, animation_id=101)
    EnableTreasure(obj=obj)
    End()
    DisableTreasure(obj=obj)
    ForceAnimation(obj, 100, loop=True)
    IfObjectDestroyed(0, obj_1)
    ForceAnimation(obj, 101, wait_for_completion=True)
    EnableTreasure(obj=obj)


@RestartOnRest(11015250)
def Event_11015250(_, character: int, other_entity: int, radius: float, seconds: float):
    """Event 11015250"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableCharacterCollision(character)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=other_entity, radius=radius)
    DisableNetworkSync()
    Wait(seconds)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@NeverRestart(11015185)
def Event_11015185():
    """Event 11015185"""
    IfFlagEnabled(1, 61010610)
    IfObjectActivated(1, obj_act_id=11010600)
    IfFlagDisabled(2, 61010610)
    IfObjectActivated(2, obj_act_id=11010600)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015180)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableFlag(11015181)
    Restart()
    EnableFlag(11015182)
    Restart()


@NeverRestart(11010611)
def Event_11010611():
    """Event 11010611"""
    DisableNetworkSync()
    IfFramesElapsed(1, frames=10)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1011100, obj_act_id=-1)


@NeverRestart(11010600)
def Event_11010600():
    """Event 11010600"""
    IfFlagEnabled(1, 11015181)
    IfHost(1)
    IfFlagEnabled(2, 11015182)
    IfHost(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015180)
    DisableFlag(11015181)
    DisableFlag(11015182)
    SkipLinesIfFinishedConditionTrue(9, condition=2)
    SkipLinesIfFlagEnabled(2, 61010610)
    Event_11010611()
    Restart()
    EnableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
    EnableFlag(11010605)
    ForceAnimation(1011101, 2)
    WaitFrames(frames=60)
    Event_11010611()
    Restart()
    SkipLinesIfFlagDisabled(2, 61010610)
    Event_11010611()
    Restart()
    DisableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
    ForceAnimation(1011101, 4)
    WaitFrames(frames=200)
    Event_11010611()
    Restart()


@NeverRestart(11010601)
def Event_11010601():
    """Event 11010601"""
    IfFlagEnabled(0, 11010605)
    DisableFlag(11010605)
    Wait(0.5)
    CreateHazard(
        obj_flag=11010602,
        obj=1011101,
        model_point=42,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=11010603,
        obj=1011101,
        model_point=43,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=11010604,
        obj=1011101,
        model_point=44,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()


@RestartOnRest(11015116)
def Event_11015116():
    """Event 11015116"""
    IfFlagDisabled(1, 61010610)
    IfFlagDisabled(1, 11010607)
    IfFlagDisabled(1, 11010600)
    IfCharacterInsideRegion(1, PLAYER, region=1012200)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015115)
    IfFlagEnabled(-1, 11015181)
    IfFlagEnabled(-1, 61010610)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015115)


@RestartOnRest(11010609)
def Event_11010609():
    """Event 11010609"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11015115)
    IfFlagDisabled(1, 61010610)
    IfConditionTrue(0, input_condition=1)
    ActivateObject(1011100, obj_act_id=-1, relative_index=-1)
    Wait(1.0)
    Restart()


@RestartOnRest(11010607)
def Event_11010607():
    """Event 11010607"""
    SkipLinesIfThisEventFlagDisabled(3)
    Move(6010, destination=1012201, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(6010, region=1012201)
    End()
    IfCharacterInsideRegion(1, 6010, region=1012771)
    IfEntityWithinDistance(1, entity=6010, other_entity=1011100, radius=3.0)
    IfFlagEnabled(1, 11015181)
    IfConditionTrue(0, input_condition=1)
    SetNest(6010, region=1012201)
    ClearTargetList(6010)
    ReplanAI(6010)


@RestartOnRest(11010608)
def Event_11010608():
    """Event 11010608"""
    IfFlagEnabled(1, 61010610)
    IfCharacterBackreadEnabled(1, 1010310)
    IfCharacterInsideRegion(1, 1010310, region=1012771)
    IfConditionTrue(0, input_condition=1)
    AICommand(1010310, command_id=1, command_slot=0)
    SetNest(1010310, region=1012773)
    IfFlagDisabled(0, 61010610)
    AICommand(1010310, command_id=-1, command_slot=0)
    SetNest(1010310, region=1012772)
    Restart()


@NeverRestart(11010621)
def Event_11010621():
    """Event 11010621"""
    SkipLinesIfThisEventFlagDisabled(3)
    EndOfAnimation(obj=1011121, animation_id=4)
    DisableObjectActivation(1011120, obj_act_id=-1)
    End()
    EndOfAnimation(obj=1011121, animation_id=3)
    IfObjectActivated(0, obj_act_id=11010620)
    ForceAnimation(1011121, 4)


@NeverRestart(11010700)
def Event_11010700():
    """Event 11010700"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObjectActivation(1011110, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11010700)
    TriggerMultiplayerEvent(event_id=10010)
    IfHealthGreaterThan(0, PLAYER, value=0.0)
    SkipLinesIfFlagEnabled(2, 11400200)
    PlayCutscene(100100, cutscene_flags=0, player_id=10000)
    SkipLines(2)
    PlayCutscene(100105, cutscene_flags=0, player_id=10000)
    EnableFlag(11500200)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=29)


@NeverRestart(11015170)
def Event_11015170():
    """Event 11015170"""
    IfMultiplayerEvent(0, event_id=10010)
    DisableNetworkSync()
    PlaySoundEffect(1011111, 130300002, sound_type=SoundType.o_Object)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(1011111, 130300002, sound_type=SoundType.o_Object)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(1011111, 130300002, sound_type=SoundType.o_Object)
    Restart()


@RestartOnRest(11010860)
def Event_11010860(_, character: int, left: int, item_lot_param_id: int):
    """Event 11010860"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(character)
    Kill(character)
    End()
    IfCharacterDead(0, character)
    SkipLinesIfEqual(4, left=left, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)
    End()


@NeverRestart(11010650)
def Event_11010650(_, obj: int, obj_act_id: int):
    """Event 11010650"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(11010899)
def Event_11010899():
    """Event 11010899"""
    EnableImmortality(1010300)
    DisableCharacter(1010300)
    SetNest(1010300, region=1012320)
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1010300, authority_level=UpdateAuthority.Forced)
    DisableFlag(11010782)
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    SkipLinesIfConditionFalse(6, 1)
    DisableFlag(11015310)
    EnableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, set_draw_parent=1013211)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    DisableCharacterCollision(1010300)
    DisableGravity(1010300)
    IfFlagEnabled(2, 11010791)
    IfFlagEnabled(2, 11015311)
    SkipLinesIfConditionFalse(4, 2)
    EnableCharacter(1010300)
    Move(1010300, destination=1012320, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010300)
    SetNest(1010300, region=1012340)
    Event_11010805(0, first_flag=11015320, last_flag=11015325, animation_id=7004, flag=11015350)
    Event_11010805(1, first_flag=11015326, last_flag=11015331, animation_id=7008, flag=11015350)
    Event_11010805(2, first_flag=11015332, last_flag=11015333, animation_id=7009, flag=11015350)
    Event_11010805(3, first_flag=11015334, last_flag=11015337, animation_id=7011, flag=11015350)
    Event_11010805(4, first_flag=11015338, last_flag=11015339, animation_id=7006, flag=11015350)
    Event_11010805(5, first_flag=11015320, last_flag=11015323, animation_id=7009, flag=11015351)
    Event_11010805(6, first_flag=11015324, last_flag=11015339, animation_id=7006, flag=11015351)
    Event_11010805(7, first_flag=11015320, last_flag=11015323, animation_id=7011, flag=11015352)
    Event_11010805(8, first_flag=11015324, last_flag=11015339, animation_id=7006, flag=11015352)
    Event_11010805(9, first_flag=11015320, last_flag=11015321, animation_id=7004, flag=11015353)
    Event_11010805(10, first_flag=11015322, last_flag=11015333, animation_id=7008, flag=11015353)
    Event_11010805(11, first_flag=11015334, last_flag=11015335, animation_id=7009, flag=11015353)
    Event_11010805(12, first_flag=11015336, last_flag=11015337, animation_id=7011, flag=11015353)
    Event_11010800(0, first_flag=11015338, last_flag=11015339, animation_id=7010, flag=11015353)
    Event_11010800(1, 11015320, 11015339, 7010, 11015354)


@RestartOnRest(11010900)
def Event_11010900():
    """Event 11010900"""
    SkipLinesIfThisEventFlagDisabled(4)
    DisableCharacter(1010300)
    DisableCharacter(1010301)
    DisableCharacter(1010302)
    End()
    IfHealthLessThan(7, 1010300, value=0.10000000149011612)
    IfFlagDisabled(7, 11015312)
    IfFlagDisabled(7, 11015300)
    IfConditionTrue(1, input_condition=7)
    IfConditionTrue(2, input_condition=7)
    IfConditionTrue(3, input_condition=7)
    IfFlagDisabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfFlagEnabled(2, 11010791)
    IfFlagDisabled(2, 11015311)
    IfFlagEnabled(3, 11010791)
    IfFlagEnabled(3, 11015311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(3, condition=1)
    ForceAnimation(1010300, 7001, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    SkipLinesIfFinishedConditionFalse(3, condition=2)
    ForceAnimation(1010300, 7007, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    DisableImmortality(1010300)
    Kill(1010300, award_souls=True)


@RestartOnRest(11010790)
def Event_11010790():
    """Event 11010790"""
    DisableGravity(1010302)
    EnableInvincibility(1010302)
    DisableCharacter(1010302)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1010302, authority_level=UpdateAuthority.Forced)
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=1012301)
    EnableFlag(11010790)
    SetNetworkUpdateRate(1010302, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableMapCollision(collision=1013200)
    EnableCharacter(1010302)
    Move(1010302, destination=1012300, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1010302, 7012, wait_for_completion=True)
    DisableCharacter(1010302)
    EnableMapCollision(collision=1013200)


@NeverRestart(11010791)
def Event_11010791():
    """Event 11010791"""
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010790)
    IfFlagDisabled(1, 11010782)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfCharacterInsideRegion(1, PLAYER, region=1012305)
    IfAllPlayersOutsideRegion(1, region=1012337)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    EnableFlag(11010791)
    EnableFlag(11010780)
    EnableCharacter(1010300)
    Move(1010300, destination=1012302, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7005)
    WaitFrames(frames=395)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    DisableFlag(11015310)


@NeverRestart(11010780)
def Event_11010780():
    """Event 11010780"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1011290, animation_id=2)
    End()
    IfCharacterHasTAEEvent(0, 1010300, tae_event_id=1000)
    ForceAnimation(1011290, 1, wait_for_completion=True)
    ForceAnimation(1011290, 2, loop=True)


@RestartOnRest(11010784)
def Event_11010784():
    """Event 11010784"""
    IfCharacterHasTAEEvent(0, 1010300, tae_event_id=500)
    EnableFlag(11015300)
    IfCharacterHasTAEEvent(0, 1010300, tae_event_id=600)
    DisableFlag(11015300)
    Restart()


@RestartOnRest(11015301)
def Event_11015301():
    """Event 11015301"""
    DisableCharacter(1010301)
    IfCharacterBackreadEnabled(0, 1010300)
    SkipLinesIfThisEventFlagDisabled(4)
    SetDisplayMask(1010300, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010300, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1010300, command_id=20, command_slot=0)
    End()
    CreateNPCPart(1010300, npc_part_id=3430, part_index=NPCPartType.Part1, part_health=200)
    IfCharacterPartHealthLessThanOrEqual(1, 1010300, npc_part_id=3430, value=0)
    IfFlagDisabled(1, 11015300)
    IfAttacked(1, attacked_entity=1010300, attacker=PLAYER)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfCharacterDead(2, 1010300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfFlagEnabled(2, 11015311)
    ForceAnimation(1010300, 8000)
    SkipLines(1)
    ForceAnimation(1010300, 8010)
    IfCharacterHasTAEEvent(0, 1010300, tae_event_id=400)
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
    AICommand(1010300, command_id=20, command_slot=0)
    ReplanAI(1010300)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34310000, host_only=True)


@NeverRestart(11015302)
def Event_11015302():
    """Event 11015302"""
    IfHost(-7)
    IfCharacterWhitePhantom(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfConditionTrue(6, input_condition=1)
    IfConditionTrue(7, input_condition=1)
    IfFlagEnabled(2, 11010100)
    IfCharacterInsideRegion(2, PLAYER, region=1012330)
    IfCharacterInsideRegion(3, PLAYER, region=1012331)
    IfFlagEnabled(4, 11010100)
    IfCharacterInsideRegion(4, PLAYER, region=1012332)
    IfCharacterInsideRegion(5, PLAYER, region=1012333)
    IfFlagEnabled(6, 11015305)
    IfFlagEnabled(7, 11015317)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    EnableFlag(11015350)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    EnableFlag(11015351)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    EnableFlag(11015352)
    SkipLinesIfFinishedConditionFalse(1, condition=5)
    EnableFlag(11015353)
    SkipLinesIfFinishedConditionTrue(2, condition=6)
    SkipLinesIfFinishedConditionTrue(1, condition=7)
    SkipLines(1)
    EnableFlag(11015354)
    DisableFlagRange((11015320, 11015339))
    SkipLinesIfClient(2)
    EnableRandomFlagInRange(flag_range=(11015320, 11015339))
    EnableFlag(11015313)
    Restart()


@NeverRestart(11010805)
def Event_11010805(_, first_flag: int, last_flag: int, animation_id: int, flag: int):
    """Event 11010805"""
    IfHost(1)
    IfFlagEnabled(1, 11015310)
    IfFlagEnabled(1, flag)
    IfFlagRangeAnyEnabled(1, flag_range=(first_flag, last_flag))
    IfHealthGreaterThan(1, 1010300, value=0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagEnabled(11015311)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfNotEqual(2, left=animation_id, right=7011)
    EnableFlag(11015312)
    AddSpecialEffect(1010300, 4160)
    SkipLinesIfEqual(1, left=animation_id, right=7006)
    ForceAnimation(1010300, animation_id)
    SkipLinesIfNotEqual(1, left=animation_id, right=7004)
    WaitFrames(frames=190)
    SkipLinesIfNotEqual(1, left=animation_id, right=7006)
    WaitFrames(frames=90)
    SkipLinesIfNotEqual(1, left=animation_id, right=7008)
    WaitFrames(frames=200)
    SkipLinesIfNotEqual(1, left=animation_id, right=7009)
    WaitFrames(frames=180)
    SkipLinesIfNotEqual(1, left=animation_id, right=7011)
    WaitFrames(frames=192)
    CancelSpecialEffect(1010300, 4160)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(flag)
    DisableFlag(11015312)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11010800)
def Event_11010800(_, first_flag: int, last_flag: int, animation_id: int, flag: int):
    """Event 11010800"""
    IfHost(1)
    IfFlagEnabled(1, 11015310)
    IfFlagEnabled(1, flag)
    IfFlagRangeAnyEnabled(1, flag_range=(first_flag, last_flag))
    IfHealthGreaterThan(1, 1010300, value=0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagEnabled(11015311)
    EnableFlag(11015311)
    EnableCharacterCollision(1010300)
    EnableGravity(1010300)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010300)
    SetBackreadStateAlternate(1010300, True)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(1010300, 4160)
    ForceAnimation(1010300, animation_id)
    WaitFrames(frames=111)
    CancelSpecialEffect(1010300, 4160)
    SetBackreadStateAlternate(1010300, False)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(flag)
    DisableFlag(11015317)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11010890)
def Event_11010890(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int, flag_6: int):
    """Event 11010890"""
    IfFlagEnabled(1, 11015313)
    IfFlagEnabled(2, 11015313)
    IfFlagEnabled(3, 11015313)
    IfFlagEnabled(4, 11015313)
    IfFlagEnabled(5, 11015313)
    IfFlagEnabled(6, 11015313)
    IfFlagEnabled(7, 11015313)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(2, flag_1)
    IfFlagEnabled(3, flag_2)
    IfFlagEnabled(4, flag_3)
    IfFlagEnabled(5, flag_4)
    IfFlagEnabled(6, flag_5)
    IfFlagEnabled(7, flag_6)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=6)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(0, input_condition=-7)
    DisableFlag(11015313)
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    EnableFlag(flag)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    EnableFlag(flag_1)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    EnableFlag(flag_2)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    EnableFlag(flag_3)
    SkipLinesIfFinishedConditionFalse(1, condition=5)
    EnableFlag(flag_4)
    SkipLinesIfFinishedConditionFalse(1, condition=6)
    EnableFlag(flag_5)
    SkipLinesIfFinishedConditionFalse(1, condition=7)
    EnableFlag(flag_6)
    Restart()


@NeverRestart(11015303)
def Event_11015303():
    """Event 11015303"""
    IfFlagDisabled(1, 11015306)
    IfFlagDisabled(1, 11015311)
    IfFlagEnabled(1, 11010791)
    IfFlagEnabled(1, 11010100)
    IfCharacterInsideRegion(-7, PLAYER, region=1012332)
    IfCharacterInsideRegion(-7, PLAYER, region=1012335)
    IfCharacterInsideRegion(-7, PLAYER, region=1012336)
    IfConditionTrue(1, input_condition=-7)
    IfFlagEnabled(2, 11015306)
    IfFlagDisabled(2, 11015311)
    IfFlagEnabled(2, 11010791)
    IfAllPlayersOutsideRegion(2, region=1012332)
    IfAllPlayersOutsideRegion(2, region=1012335)
    IfAllPlayersOutsideRegion(2, region=1012336)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableFlag(11015306)
    Restart()
    DisableFlag(11015306)
    RestartEvent(event_id=11015304)
    Restart()


@NeverRestart(11015304)
def Event_11015304():
    """Event 11015304"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11015305)
    IfFlagEnabled(1, 11015306)
    IfConditionTrue(0, input_condition=1)
    Wait(20.0)
    EnableFlag(11015305)
    Restart()


@NeverRestart(11010850)
def Event_11010850():
    """Event 11010850"""
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfAttacked(1, attacked_entity=1010300, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015317)
    Restart()


@NeverRestart(11010851)
def Event_11010851():
    """Event 11010851"""
    IfFlagDisabled(1, 11015316)
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfAllPlayersOutsideRegion(1, region=1012338)
    IfHealthLessThan(1, 1010300, value=0.699999988079071)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfFlagEnabled(2, 11015316)
    IfFlagEnabled(2, 11010791)
    IfCharacterInsideRegion(2, PLAYER, region=1012338)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableFlag(11015316)
    Restart()
    DisableFlag(11015316)
    RestartEvent(event_id=11010852)
    Restart()


@NeverRestart(11010852)
def Event_11010852():
    """Event 11010852"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11015315)
    IfFlagEnabled(1, 11015316)
    IfConditionTrue(0, input_condition=1)
    Wait(60.0)
    EnableFlag(11015315)
    Restart()


@RestartOnRest(11015307)
def Event_11015307():
    """Event 11015307"""
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010791)
    IfFlagEnabled(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    SetNest(1010300, region=1012320)
    IfCharacterHasTAEEvent(0, 1010300, tae_event_id=700)
    Move(1010300, destination=1012340, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7016)
    WaitFrames(frames=110)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    AICommand(1010300, command_id=-1, command_slot=1)
    DisableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    DisableFlag(11015305)
    DisableFlag(11015309)
    DisableFlag(11015311)
    Restart()


@NeverRestart(11015308)
def Event_11015308():
    """Event 11015308"""
    IfFlagDisabled(1, 11015309)
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010791)
    IfHealthGreaterThanOrEqual(1, 1010300, value=0.10000000149011612)
    IfAllPlayersOutsideRegion(1, region=1012334)
    IfFlagEnabled(2, 11015309)
    IfFlagDisabled(2, 11015310)
    IfFlagEnabled(2, 11010791)
    IfHealthGreaterThanOrEqual(2, 1010300, value=0.10000000149011612)
    IfCharacterInsideRegion(2, PLAYER, region=1012334)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    EnableFlag(11015309)
    AICommand(1010300, command_id=1, command_slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()
    DisableFlag(11015309)
    AICommand(1010300, command_id=-1, command_slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()


@NeverRestart(11010782)
def Event_11010782():
    """Event 11010782"""
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010790)
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1012337)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=10)
    RestartIfFlagEnabled(11015311)
    EnableFlag(11015310)
    EnableFlag(11015312)
    DisableFlag(11010791)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(1010300, 7013, wait_for_completion=True)
    DisableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, set_draw_parent=1013210)


@NeverRestart(11010783)
def Event_11010783():
    """Event 11010783"""
    IfFlagDisabled(1, 11015310)
    IfFlagEnabled(1, 11010790)
    IfFlagEnabled(1, 11010791)
    IfFlagDisabled(1, 11015311)
    IfFlagEnabled(1, 11015315)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    SetStandbyAnimationSettings(1010300, standby_animation=7018)
    ForceAnimation(1010300, 7017, wait_for_completion=True)
    IfHealthGreaterThanOrEqual(0, 1010300, value=0.699999988079071)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7019)
    WaitFrames(frames=50)
    DisableFlag(11015315)
    DisableFlag(11015316)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11010200)
def Event_11010200(_, tae_event_id: int, animation_id: int):
    """Event 11010200"""
    IfCharacterBackreadEnabled(1, 1010300)
    IfCharacterHasTAEEvent(1, 1010300, tae_event_id=tae_event_id)
    IfConditionTrue(0, input_condition=1)
    HellkiteBreathControl(1010300, obj=1011060, animation_id=animation_id)
    IfCharacterDoesNotHaveTAEEvent(0, 1010300, tae_event_id=tae_event_id)
    Restart()


@NeverRestart(11010510)
def Event_11010510(_, character: int, flag: int):
    """Event 11010510"""
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, flag)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(character)
    IfFlagEnabled(0, 703)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()
    RestartIfThisEventSlotFlagDisabled()
    IfFlagEnabled(0, 744)
    EnableFlag(744)
    IfFlagDisabled(0, 744)
    Restart()


@NeverRestart(11010520)
def Event_11010520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11010501)
def Event_11010501(_, character: int, flag: int):
    """Event 11010501"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1175)
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SetAIParamID(character, ai_param_id=1)
    SaveRequest()
    RestartIfThisEventFlagDisabled()
    IfFlagEnabled(0, 744)
    IfFlagDisabled(0, 744)
    Restart()


@NeverRestart(11010530)
def Event_11010530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010530"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1000)
    IfFlagEnabled(1, 11010591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11010531)
def Event_11010531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010531"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1008)
    IfFlagEnabled(1, 11510594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(character, destination=1012530, destination_type=CoordEntityType.Region, set_draw_parent=1013050)
    SetNest(character, region=1012530)
    EnableCharacter(character)


@NeverRestart(11010532)
def Event_11010532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010532"""
    IfFlagDisabled(1, 1114)
    IfFlagEnabled(1, 1110)
    IfFlagEnabled(1, 11010181)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetStandbyAnimationSettings(character)


@NeverRestart(11010533)
def Event_11010533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010533"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1174)
    IfFlagEnabled(1, 11310590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    ClearEventValue(600, bit_count=4)


@NeverRestart(11010534)
def Event_11010534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010534"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1175)
    IfFlagEnabled(1, 724)
    IfCharacterAlive(1, character)
    IfThisEventFlagDisabled(1)
    IfHost(2)
    IfFlagDisabled(2, 1176)
    IfFlagDisabled(2, 1177)
    IfFlagDisabled(2, 1179)
    IfFlagDisabled(2, 1180)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11010535)
def Event_11010535(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010535"""
    IfFlagDisabled(1, 1176)
    IfFlagEnabled(-7, 1175)
    IfFlagEnabled(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, character, value=0.0)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, 1180)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EndIfFinishedConditionTrue(input_condition=1)
    DropMandatoryTreasure(character)


@NeverRestart(11010537)
def Event_11010537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010537"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1175)
    IfFlagDisabled(1, 1196)
    IfFlagDisabled(1, 1198)
    IfEventValueGreaterThanOrEqual(1, flag=600, bit_count=4, value=2)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, 703)
    IfFlagEnabled(3, 11010599)
    IfFlagEnabled(3, flag)
    IfThisEventFlagEnabled(3)
    IfFlagDisabled(4, 11010599)
    IfFlagEnabled(4, flag)
    IfThisEventFlagEnabled(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, condition=3)
    SkipLinesIfFinishedConditionFalse(9, condition=1)
    EnableFlag(11010599)
    SkipLinesIfClient(3)
    EnableFlag(50006070)
    DisableFlag(50006071)
    DisableFlag(50006080)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DropMandatoryTreasure(character)
    End()
    SkipLinesIfFinishedConditionFalse(3, condition=2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    End()
    DropMandatoryTreasure(character)


@NeverRestart(11010538)
def Event_11010538():
    """Event 11010538"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1175)
    IfFlagEnabled(1, 11010596)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11010596)
    ClearEventValue(600, bit_count=4)
    Restart()


@NeverRestart(11010539)
def Event_11010539():
    """Event 11010539"""
    EndIfClient()
    IfFlagEnabled(1, 1177)
    IfFlagEnabled(1, 50006071)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(815)


@NeverRestart(11010550)
def Event_11010550(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010550"""
    IfFlagDisabled(1, 1574)
    IfFlagEnabled(1, 1570)
    IfFlagEnabled(1, 11010190)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11010584)


@NeverRestart(11010551)
def Event_11010551():
    """Event 11010551"""
    EndIfFlagEnabled(11010593)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=3)
    IfFlagEnabled(0, 11010593)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=1)


@NeverRestart(11010552)
def Event_11010552(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11010552"""
    IfFlagDisabled(1, 1574)
    IfFlagEnabled(1, 1570)
    IfFlagEnabled(-1, 3)
    IfFlagEnabled(2, 812)
    IfFlagEnabled(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11010581)
def Event_11010581(_, character: int):
    """Event 11010581"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 11010700)
    EnableCharacter(character)


@RestartOnRest(11010582)
def Event_11010582():
    """Event 11010582"""
    SkipLinesIfClient(1)
    DisableFlag(11010586)
    SkipLinesIfFlagEnabled(4, 11010586)
    IfFlagEnabled(-1, 1175)
    IfFlagEnabled(-1, 1179)
    IfFlagEnabled(-1, 1181)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010586)
    DisableCharacter(1010320)


@NeverRestart(11010583)
def Event_11010583():
    """Event 11010583"""
    EndIfClient()
    IfFlagEnabled(0, 744)
    IfFlagDisabled(0, 744)
    Wait(1.0)
    Move(6001, destination=1012010, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(6001, standby_animation=7845)
    Move(6040, destination=1012011, destination_type=CoordEntityType.Region, short_move=True)
    Move(6072, destination=1012012, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(6072, standby_animation=7880)
    Move(6190, destination=1012013, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(6190, standby_animation=9000)
    DisableFlag(11015090)
    RestoreObject(1011010)
    RestartEvent(event_id=11015090)
    Move(6230, destination=1012014, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(6230, standby_animation=9000)
    Move(6300, destination=1012015, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(6300, standby_animation=7825)
    Restart()


@NeverRestart(11010580)
def Event_11010580():
    """Event 11010580"""
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagEnabled(1, 11015030)
    IfFlagDisabled(1, 11015031)
    IfConditionTrue(2, input_condition=-7)
    IfFlagDisabled(2, 11015030)
    IfFlagEnabled(2, 11015031)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionFalse(9, condition=1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, target_entity=6480)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11015031)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(1)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11015031)
    Restart()


@NeverRestart(11010585)
def Event_11010585():
    """Event 11010585"""
    DisableNetworkSync()
    WaitFrames(frames=2)
    EnableFlag(11010580)


@RestartOnRest(11015090)
def Event_11015090(_, flag: int, flag_1: int, obj: int):
    """Event 11015090"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    EnableObjectInvulnerability(obj)
    IfFlagEnabled(-1, flag)
    IfFlagEnabled(-1, flag_1)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(obj)
    WaitFrames(frames=1)
    DestroyObject(obj)
    PlaySoundEffect(obj, 125200000, sound_type=SoundType.o_Object)
    EnableFlag(11015090)
    IfFlagEnabled(0, 703)
    End()


@NeverRestart(11015100)
def Event_11015100():
    """Event 11015100"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6540, authority_level=UpdateAuthority.Forced)
    SkipLinesIfThisEventFlagDisabled(1)
    DisableCharacter(6001)
    SkipLinesIfFlagEnabled(3, 11015106)
    IfClient(2)
    IfFlagEnabled(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6540)
    EndIfFlagEnabled(3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(-1, 1004)
    IfFlagEnabled(-1, 1005)
    IfFlagEnabled(-1, 1006)
    IfFlagEnabled(-1, 1010)
    IfFlagEnabled(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6540)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6540,
        region=1012000,
        summon_flag=11015102,
        dismissal_flag=11015106,
    )
    DisableCharacter(6001)


@NeverRestart(11015101)
def Event_11015101():
    """Event 11015101"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11015102)
    IfFlagEnabled(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6540, command_id=10, command_slot=0)
    ReplanAI(6540)
    IfCharacterInsideRegion(0, 6540, region=1012998)
    RotateToFaceEntity(6540, target_entity=1012997)
    ForceAnimation(6540, 7410)
    AICommand(6540, command_id=-1, command_slot=0)
    ReplanAI(6540)


@NeverRestart(11015103)
def Event_11015103():
    """Event 11015103"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6590, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11015107)
    IfClient(2)
    IfFlagEnabled(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6590)
    EndIfFlagEnabled(3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 11020607)
    IfFlagEnabled(-1, 1572)
    IfFlagEnabled(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 1574)
    IfCharacterBackreadEnabled(1, 6590)
    IfEntityWithinDistance(1, entity=6590, other_entity=PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6590,
        region=1012001,
        summon_flag=11015105,
        dismissal_flag=11015107,
    )
    IfFlagEnabled(0, 11015105)
    AddSpecialEffect(6590, 5450)


@NeverRestart(11015104)
def Event_11015104():
    """Event 11015104"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11015105)
    IfFlagEnabled(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6590, command_id=10, command_slot=0)
    ReplanAI(6590)
    IfCharacterInsideRegion(0, 6590, region=1012998)
    RotateToFaceEntity(6590, target_entity=1012997)
    ForceAnimation(6590, 7410)
    AICommand(6590, command_id=-1, command_slot=0)
    ReplanAI(6590)
