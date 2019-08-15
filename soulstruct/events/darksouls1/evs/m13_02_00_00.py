"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11320992, obj=1321960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RegisterBonfire(11320984, obj=1321961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11320976, obj=1321962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=1321140)
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=1321141)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=1321142)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=1321143)
    RegisterStatue(1321900, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321901, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321902, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321903, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321904, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321905, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321906, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321907, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    SkipLinesIfClient(2)
    DisableObject(1321994)
    DeleteFX(1321995, erase_root_only=False)
    RunEvent(11320090, slot=0, args=(1321700, 1321701, 1322600, 1322601))
    RunEvent(11325000)
    RunEvent(11320800)
    RunEvent(11325001)
    RunEvent(11320200, slot=0, args=(1321200, 11320200))
    RunEvent(11320200, slot=1, args=(1321201, 11320201))
    RunEvent(11320580)
    SkipLinesIfFlagOff(2, 11320100)
    RunEvent(11320100)
    SkipLines(3)
    RunEvent(11320110)
    RunEvent(11320100)
    RunEvent(11325100)
    RunEvent(11320101)
    RunEvent(11325150, slot=0, args=(1320100, 15.0), arg_types='if')
    RunEvent(11325150, slot=1, args=(1320101, 15.0), arg_types='if')
    RunEvent(11325150, slot=2, args=(1320102, 10.0), arg_types='if')
    RunEvent(11320300, slot=1, args=(1320201, 11325203, 11325205, 11325203), arg_types='iIIi')
    RunEvent(11320300, slot=2, args=(1320202, 11325206, 11325208, 11325206), arg_types='iIIi')
    RunEvent(11320300, slot=3, args=(1320203, 11325209, 11325211, 11325209), arg_types='iIIi')
    RunEvent(11320300, slot=4, args=(1320204, 11325212, 11325214, 11325212), arg_types='iIIi')
    RunEvent(11320300, slot=5, args=(1320205, 11325215, 11325217, 11325215), arg_types='iIIi')
    RunEvent(11320300, slot=6, args=(1320206, 11325218, 11325220, 11325218), arg_types='iIIi')
    RunEvent(11320300, slot=7, args=(1320207, 11325221, 11325223, 11325221), arg_types='iIIi')
    RunEvent(11320300, slot=8, args=(1320208, 11325224, 11325226, 11325224), arg_types='iIIi')
    RunEvent(11320300, slot=9, args=(1320209, 11325227, 11325229, 11325227), arg_types='iIIi')
    RunEvent(11320300, slot=10, args=(1320210, 11325230, 11325232, 11325230), arg_types='iIIi')
    RunEvent(11320600, slot=0, args=(1321650, 11320600))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6288, 8446)
    SkipLinesIfFlagOn(1, 1511)
    DisableCharacter(6288)
    RunEvent(11320534, slot=0, args=(6288, 1490, 1539, 1511))
    RunEvent(11320535, slot=0, args=(6288, 1490, 1539, 1514))
    HumanityRegistration(6290, 8454)
    SkipLinesIfFlagOn(2, 1547)
    SkipLinesIfFlagOn(1, 1546)
    DisableCharacter(6290)
    RunEvent(11320510, slot=1, args=(6290, 1547))
    RunEvent(11320520, slot=1, args=(6290, 1540, 1569, 1548))
    RunEvent(11320540, slot=0, args=(6290, 1540, 1569, 1546))
    RunEvent(11320541, slot=0, args=(6290, 1540, 1569, 1549))
    EnableImmortality(1320800)


@NeverRestart
def Event11320090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320090: Event 11320090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
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
def Event11325090():
    """ 11325090: Event 11325090 """
    DisableCharacter(1320900)
    IfBlackWorldTendencyComparison(-1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfFlagOn(-1, 11325090)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11325090)
    EnableCharacter(1320900)
    IfBlackWorldTendencyComparison(0, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    Kill(1320900, award_souls=False)


@RestartOnRest
def Event11320110():
    """ 11320110: Event 11320110 """
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(1320701)
    DisableCharacter(1320702)
    DisableCharacter(1320703)
    DisableCharacter(1320704)
    DisableCharacter(1320705)
    DisableCharacter(1320706)
    DisableCharacter(1320707)
    EndIfFlagOn(11320100)
    RunEvent(11325121)
    RunEvent(11325110, slot=0, args=(1, 3530, 3530, 1320701, 91, 0, 1, 5430), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=1, args=(2, 3531, 3531, 1320702, 92, 1, 2, 5431), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=2, args=(3, 3532, 3532, 1320703, 93, 2, 3, 5432), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=3, args=(4, 3533, 3533, 1320704, 94, 3, 4, 5433), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=4, args=(5, 3534, 3534, 1320705, 95, 4, 5, 5434), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=5, args=(6, 3535, 3535, 1320706, 96, 5, 6, 5435), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=6, args=(8, 3536, 3536, 1320707, 97, 6, 7, 5436), arg_types='hhiiiBBi')


@RestartOnRest
def Event11325100():
    """ 11325100: Event 11325100 """
    IfCharacterBackreadEnabled(1, 1320700)
    IfHasTAEEvent(1, 1320700, tae_event_id=300)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(8, 11325101)
    EnableFlag(11325101)
    Move(1320700, destination=1322700, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1320700, 3011, wait_for_completion=True)
    Move(1320700, destination=1322710, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(1320700, 1322710)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()
    DisableFlag(11325101)
    Move(1320700, destination=1322701, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1320700, 3014, wait_for_completion=True)
    Move(1320700, destination=1322711, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(1320700, 1322711)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()


@UnknownRestart
def Event11325110(ARG_0_1: short, ARG_2_3: short, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_16: uchar, ARG_17_17: uchar, ARG_20_23: int):
    """ 11325110: Event 11325110 """
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(1320700, bit_index=ARG_16_16, switch_type=OnOffChange.On)
    SetHitboxMask(1320700, bit_index=ARG_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, ARG_20_23)
    End()
    IfCharacterBackreadEnabled(0, 1320700)
    CreateNPCPart(1320700, npc_part_id=ARG_2_3, part_index=ARG_0_1, part_health=270, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, 1320700, npc_part_id=ARG_4_7, value=0)
    IfFlagOff(1, 11325120)
    IfAttacked(1, 1320700, attacking_character=10000)
    IfHealthLessThanOrEqual(2, 1320700, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(1320700, disable_interpolation=False)
    Move(ARG_8_11, destination=1320700, destination_type=CoordEntityType.Character, model_point=ARG_12_15, copy_draw_hitbox=1320700)
    EnableCharacter(ARG_8_11)
    ForceAnimation(ARG_8_11, 8100)
    ForceAnimation(1320700, 8000)
    SetDisplayMask(1320700, bit_index=ARG_16_16, switch_type=OnOffChange.On)
    SetHitboxMask(1320700, bit_index=ARG_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, ARG_20_23)


@UnknownRestart
def Event11325121():
    """ 11325121: Event 11325121 """
    IfHasTAEEvent(0, 1320700, tae_event_id=500)
    EnableFlag(11325120)
    IfHasTAEEvent(0, 1320700, tae_event_id=600)
    DisableFlag(11325120)
    Restart()


@RestartOnRest
def Event11320100():
    """ 11320100: Event 11320100 """
    SkipLinesIfThisEventOff(9)
    DisableCharacter(1320700)
    DisableCharacter(1320701)
    DisableCharacter(1320702)
    DisableCharacter(1320703)
    DisableCharacter(1320704)
    DisableCharacter(1320705)
    DisableCharacter(1320706)
    DisableCharacter(1320707)
    End()
    IfCharacterDead(0, 1320700)
    AwardItemLot(35300000, host_only=False)


@NeverRestart
def Event11320101():
    """ 11320101: Event 11320101 """
    EndIfFlagOn(11320100)
    IfFlagOn(1, 11325110)
    IfFlagOn(1, 11325111)
    IfFlagOn(1, 11325112)
    IfFlagOn(1, 11325113)
    IfFlagOn(1, 11325114)
    IfFlagOn(1, 11325115)
    IfFlagOn(1, 11325116)
    IfConditionTrue(0, input_condition=1)
    Kill(1320700, award_souls=True)


@RestartOnRest
def Event11325150(ARG_0_3: int, ARG_4_7: float):
    """ 11325150: Event 11325150 """
    EndIfThisEventSlotOn()
    SetStandbyAnimationSettings(ARG_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, ARG_0_3, 10000, radius=ARG_4_7)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=9060)


@NeverRestart
def Event11325000():
    """ 11325000: Event 11325000 """
    EndIfThisEventOn()
    SetStandbyAnimationSettings(1320800, standby_animation=9000)
    IfHost(1)
    IfEntityWithinDistance(1, 1320800, 10000, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(1320800, cancel_animation=9060)


@NeverRestart
def Event11320800():
    """ 11320800: Event 11320800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1320800)
    End()
    IfCharacterDead(0, 1320800)
    EnableFlag(11320800)


@RestartOnRest
def Event11325001():
    """ 11325001: Event 11325001 """
    DisableCharacter(1320801)
    EndIfFlagOn(11320800)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(1320800, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(1320800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1320800, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1320800)
    CreateNPCPart(1320800, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, 1320800, npc_part_id=3451, value=0)
    IfHealthLessThanOrEqual(2, 1320800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(1320800, 8000)
    IfHasTAEEvent(0, 1320800, tae_event_id=400)
    EnableCharacter(1320801)
    Move(1320801, destination=1320800, destination_type=CoordEntityType.Character, model_point=19, copy_draw_hitbox=1320800)
    ForceAnimation(1320801, 8100)
    SetDisplayMask(1320800, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(1320800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1320800, command_id=20, slot=0)
    ReplanAI(1320800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34510000, host_only=True)


@NeverRestart
def Event11320200(ARG_0_3: int, ARG_4_7: int):
    """ 11320200: Event 11320200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(ARG_0_3)
    End()
    IfObjectDestroyed(0, ARG_0_3)
    EnableFlag(ARG_4_7)


@RestartOnRest
def Event11320300(ARG_0_3: int, ARG_4_7: uint, ARG_8_11: uint, ARG_12_15: int):
    """ 11320300: Event 11320300 """
    DisableCharacter(ARG_0_3)
    EndIfThisEventSlotOn()
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((ARG_4_7, ARG_8_11))
    IfFlagOn(0, ARG_12_15)
    EnableCharacter(ARG_0_3)
    IfCharacterDead(0, ARG_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33000000, host_only=True)
    End()


@NeverRestart
def Event11320600(ARG_0_3: int, ARG_4_7: int):
    """ 11320600: Event 11320600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=-1)
    EnableTreasure(ARG_0_3)
    End()
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@NeverRestart
def Event11320510(ARG_0_3: int, ARG_4_7: int):
    """ 11320510: Event 11320510 """
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
def Event11320520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320520: Event 11320520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11320534(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320534: Event 11320534 """
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1547)
    IfFlagOff(1, 1548)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410593)
    IfFlagOn(1, 11020606)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11320535(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320535: Event 11320535 """
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1511)
    IfFlagOn(-1, 11320591)
    IfFlagOn(-1, 1548)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11320540(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320540: Event 11320540 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1545)
    IfFlagOn(1, 11020606)
    IfFlagOn(1, 1511)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11320541(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11320541: Event 11320541 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1546)
    IfFlagOn(1, 11320591)
    IfCharacterBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11320580():
    """ 11320580: Event 11320580 """
    IfFlagOn(0, 11325030)
    RotateToFaceEntity(PLAYER, 1320800)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagOff(0, 11325030)
    ResetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()
