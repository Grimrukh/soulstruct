"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11320992, obj=1321960, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11320984, obj=1321961)
    RegisterBonfire(bonfire_flag=11320976, obj=1321962)
    RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=1321140)
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=1321141)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=1321142)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=1321143)
    RegisterStatue(obj=1321900, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321901, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321902, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321903, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321904, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321905, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321906, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=1321907, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    SkipLinesIfClient(2)
    DisableObject(1321994)
    DeleteVFX(vfx_id=1321995, erase_root_only=False)
    Event_11320090(0, 1321700, 1321701, 1322600, 1322601)
    Event_11325000()
    Event_11320800()
    Event_11325001()
    Event_11320200(0, 1321200, 11320200)
    Event_11320200(1, 1321201, 11320201)
    Event_11320580()
    SkipLinesIfFlagDisabled(2, 11320100)
    Event_11320100()
    SkipLines(3)
    Event_11320110()
    Event_11320100()
    Event_11325100()
    Event_11320101()
    Event_11325150(0, 1320100, 15.0)
    Event_11325150(1, 1320101, 15.0)
    Event_11325150(2, 1320102, 10.0)
    Event_11320300(1, 1320201, 11325203, 11325205, 11325203)
    Event_11320300(2, 1320202, 11325206, 11325208, 11325206)
    Event_11320300(3, 1320203, 11325209, 11325211, 11325209)
    Event_11320300(4, 1320204, 11325212, 11325214, 11325212)
    Event_11320300(5, 1320205, 11325215, 11325217, 11325215)
    Event_11320300(6, 1320206, 11325218, 11325220, 11325218)
    Event_11320300(7, 1320207, 11325221, 11325223, 11325221)
    Event_11320300(8, 1320208, 11325224, 11325226, 11325224)
    Event_11320300(9, 1320209, 11325227, 11325229, 11325227)
    Event_11320300(10, 1320210, 11325230, 11325232, 11325230)
    Event_11320600(0, 1321650, 11320600)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6288, event_flag=8446)
    SkipLinesIfFlagEnabled(1, 1511)
    DisableCharacter(6288)
    Event_11320534(0, 6288, 1490, 1539, 1511)
    Event_11320535(0, 6288, 1490, 1539, 1514)
    HumanityRegistration(6290, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1546)
    DisableCharacter(6290)
    Event_11320510(1, 6290, 1547)
    Event_11320520(1, 6290, 1540, 1569, 1548)
    Event_11320540(0, 6290, 1540, 1569, 1546)
    Event_11320541(0, 6290, 1540, 1569, 1549)
    EnableImmortality(1320800)


@NeverRestart(11320090)
def Event_11320090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        model_point=0,
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


@RestartOnRest(11325090)
def Event_11325090():
    """Event 11325090"""
    DisableCharacter(1320900)
    IfBlackWorldTendencyComparison(-1, ComparisonType.GreaterThan, value=50)
    IfFlagEnabled(-1, 11325090)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11325090)
    EnableCharacter(1320900)
    IfBlackWorldTendencyComparison(0, ComparisonType.LessThanOrEqual, value=50)
    Kill(1320900)


@RestartOnRest(11320110)
def Event_11320110():
    """Event 11320110"""
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(1320701)
    DisableCharacter(1320702)
    DisableCharacter(1320703)
    DisableCharacter(1320704)
    DisableCharacter(1320705)
    DisableCharacter(1320706)
    DisableCharacter(1320707)
    EndIfFlagEnabled(11320100)
    Event_11325121()
    Event_11325110(0, 1, 3530, 3530, 1320701, 91, 0, 1, 5430)
    Event_11325110(1, 2, 3531, 3531, 1320702, 92, 1, 2, 5431)
    Event_11325110(2, 3, 3532, 3532, 1320703, 93, 2, 3, 5432)
    Event_11325110(3, 4, 3533, 3533, 1320704, 94, 3, 4, 5433)
    Event_11325110(4, 5, 3534, 3534, 1320705, 95, 4, 5, 5434)
    Event_11325110(5, 6, 3535, 3535, 1320706, 96, 5, 6, 5435)
    Event_11325110(6, 8, 3536, 3536, 1320707, 97, 6, 7, 5436)


@RestartOnRest(11325100)
def Event_11325100():
    """Event 11325100"""
    IfCharacterBackreadEnabled(1, 1320700)
    IfCharacterHasTAEEvent(1, 1320700, tae_event_id=300)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(8, 11325101)
    EnableFlag(11325101)
    Move(1320700, destination=1322700, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1320700, 3011, wait_for_completion=True)
    Move(1320700, destination=1322710, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1320700, region=1322710)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()
    DisableFlag(11325101)
    Move(1320700, destination=1322701, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1320700, 3014, wait_for_completion=True)
    Move(1320700, destination=1322711, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1320700, region=1322711)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()


@UnknownRestart(11325110)
def Event_11325110(
    _,
    arg_0_1: short,
    arg_2_3: short,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_20_23: int,
):
    """Event 11325110"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(1320700, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, 1320700)
    CreateNPCPart(1320700, npc_part_id=arg_2_3, part_index=arg_0_1, part_health=270)
    IfCharacterPartHealthComparison(1, 1320700, npc_part_id=arg_4_7, comparison_type=ComparisonType.Equal, value=5)
    IfFlagDisabled(1, 11325120)
    IfAttacked(1, attacked_entity=1320700, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, 1320700, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(1320700)
    Move(
        arg_8_11,
        destination=1320700,
        destination_type=CoordEntityType.Character,
        model_point=arg_12_15,
        copy_draw_parent=1320700,
    )
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(1320700, 8000)
    SetDisplayMask(1320700, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, arg_20_23)


@UnknownRestart(11325121)
def Event_11325121():
    """Event 11325121"""
    IfCharacterHasTAEEvent(0, 1320700, tae_event_id=500)
    EnableFlag(11325120)
    IfCharacterHasTAEEvent(0, 1320700, tae_event_id=600)
    DisableFlag(11325120)
    Restart()


@RestartOnRest(11320100)
def Event_11320100():
    """Event 11320100"""
    SkipLinesIfThisEventFlagDisabled(9)
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


@NeverRestart(11320101)
def Event_11320101():
    """Event 11320101"""
    EndIfFlagEnabled(11320100)
    IfFlagEnabled(1, 11325110)
    IfFlagEnabled(1, 11325111)
    IfFlagEnabled(1, 11325112)
    IfFlagEnabled(1, 11325113)
    IfFlagEnabled(1, 11325114)
    IfFlagEnabled(1, 11325115)
    IfFlagEnabled(1, 11325116)
    IfConditionTrue(0, input_condition=1)
    Kill(1320700, award_souls=True)


@RestartOnRest(11325150)
def Event_11325150(_, arg_0_3: int, arg_4_7: float):
    """Event 11325150"""
    EndIfThisEventSlotFlagEnabled()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@NeverRestart(11325000)
def Event_11325000():
    """Event 11325000"""
    EndIfThisEventFlagEnabled()
    SetStandbyAnimationSettings(1320800, standby_animation=9000)
    IfHost(1)
    IfEntityWithinDistance(1, entity=1320800, other_entity=PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(1320800, cancel_animation=9060)


@NeverRestart(11320800)
def Event_11320800():
    """Event 11320800"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1320800)
    End()
    IfCharacterDead(0, 1320800)
    EnableFlag(11320800)


@RestartOnRest(11325001)
def Event_11325001():
    """Event 11325001"""
    DisableCharacter(1320801)
    EndIfFlagEnabled(11320800)
    SkipLinesIfThisEventFlagDisabled(4)
    SetDisplayMask(1320800, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1320800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1320800, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1320800)
    CreateNPCPart(1320800, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200)
    IfCharacterPartHealthComparison(1, 1320800, npc_part_id=3451, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, 1320800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(1320800, 8000)
    IfCharacterHasTAEEvent(0, 1320800, tae_event_id=400)
    EnableCharacter(1320801)
    Move(
        1320801,
        destination=1320800,
        destination_type=CoordEntityType.Character,
        model_point=19,
        copy_draw_parent=1320800,
    )
    ForceAnimation(1320801, 8100)
    SetDisplayMask(1320800, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1320800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1320800, command_id=20, slot=0)
    ReplanAI(1320800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34510000, host_only=True)


@NeverRestart(11320200)
def Event_11320200(_, arg_0_3: int, arg_4_7: int):
    """Event 11320200"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(0, arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest(11320300)
def Event_11320300(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """Event 11320300"""
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(arg_4_7, arg_8_11))
    IfFlagEnabled(0, arg_12_15)
    EnableCharacter(arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33000000, host_only=True)
    End()


@NeverRestart(11320600)
def Event_11320600(_, arg_0_3: int, arg_4_7: int):
    """Event 11320600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11320510)
def Event_11320510(_, arg_0_3: int, arg_4_7: int):
    """Event 11320510"""
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


@NeverRestart(11320520)
def Event_11320520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11320534)
def Event_11320534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320534"""
    IfFlagDisabled(1, 1512)
    IfFlagDisabled(1, 1547)
    IfFlagDisabled(1, 1548)
    IfFlagEnabled(1, 1507)
    IfFlagEnabled(1, 11410593)
    IfFlagEnabled(1, 11020606)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11320535)
def Event_11320535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320535"""
    IfFlagDisabled(1, 1512)
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1511)
    IfFlagEnabled(-1, 11320591)
    IfFlagEnabled(-1, 1548)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11320540)
def Event_11320540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320540"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1545)
    IfFlagEnabled(1, 11020606)
    IfFlagEnabled(1, 1511)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11320541)
def Event_11320541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11320541"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1546)
    IfFlagEnabled(1, 11320591)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11320580)
def Event_11320580():
    """Event 11320580"""
    IfFlagEnabled(0, 11325030)
    RotateToFaceEntity(PLAYER, target_entity=1320800)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagDisabled(0, 11325030)
    SetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()
