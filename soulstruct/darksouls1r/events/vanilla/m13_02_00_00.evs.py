"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


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
    DeleteVFX(1321995, erase_root_only=False)
    Event_11320090(0, line_intersects__obj=1321700, vfx_id=1321701, destination=1322600, destination_1=1322601)
    Event_11325000()
    Event_11320800()
    Event_11325001()
    Event_11320200(0, obj=1321200, flag=11320200)
    Event_11320200(1, obj=1321201, flag=11320201)
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
    Event_11320300(1, character=1320201, first_flag=11325203, last_flag=11325205, flag=11325203)
    Event_11320300(2, character=1320202, first_flag=11325206, last_flag=11325208, flag=11325206)
    Event_11320300(3, character=1320203, first_flag=11325209, last_flag=11325211, flag=11325209)
    Event_11320300(4, character=1320204, first_flag=11325212, last_flag=11325214, flag=11325212)
    Event_11320300(5, character=1320205, first_flag=11325215, last_flag=11325217, flag=11325215)
    Event_11320300(6, character=1320206, first_flag=11325218, last_flag=11325220, flag=11325218)
    Event_11320300(7, character=1320207, first_flag=11325221, last_flag=11325223, flag=11325221)
    Event_11320300(8, character=1320208, first_flag=11325224, last_flag=11325226, flag=11325224)
    Event_11320300(9, character=1320209, first_flag=11325227, last_flag=11325229, flag=11325227)
    Event_11320300(10, character=1320210, first_flag=11325230, last_flag=11325232, flag=11325230)
    Event_11320600(0, 1321650, 11320600)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6288, event_flag=8446)
    SkipLinesIfFlagEnabled(1, 1511)
    DisableCharacter(6288)
    Event_11320534(0, character=6288, first_flag=1490, last_flag=1539, flag=1511)
    Event_11320535(0, character=6288, first_flag=1490, last_flag=1539, flag=1514)
    HumanityRegistration(6290, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1546)
    DisableCharacter(6290)
    Event_11320510(1, character=6290, flag=1547)
    Event_11320520(1, character=6290, first_flag=1540, last_flag=1569, flag=1548)
    Event_11320540(0, character=6290, first_flag=1540, last_flag=1569, flag=1546)
    Event_11320541(0, character=6290, first_flag=1540, last_flag=1569, flag=1549)
    EnableImmortality(1320800)


@NeverRestart(11320090)
def Event_11320090(_, line_intersects__obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11320090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=line_intersects__obj,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
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
    Event_11325110(
        0,
        part_index=1,
        npc_part_id=3530,
        npc_part_id_1=3530,
        character=1320701,
        model_point=91,
        bit_index=0,
        bit_index_1=1,
        special_effect_id=5430
    )
    Event_11325110(
        1,
        part_index=2,
        npc_part_id=3531,
        npc_part_id_1=3531,
        character=1320702,
        model_point=92,
        bit_index=1,
        bit_index_1=2,
        special_effect_id=5431
    )
    Event_11325110(
        2,
        part_index=3,
        npc_part_id=3532,
        npc_part_id_1=3532,
        character=1320703,
        model_point=93,
        bit_index=2,
        bit_index_1=3,
        special_effect_id=5432
    )
    Event_11325110(
        3,
        part_index=4,
        npc_part_id=3533,
        npc_part_id_1=3533,
        character=1320704,
        model_point=94,
        bit_index=3,
        bit_index_1=4,
        special_effect_id=5433
    )
    Event_11325110(
        4,
        part_index=5,
        npc_part_id=3534,
        npc_part_id_1=3534,
        character=1320705,
        model_point=95,
        bit_index=4,
        bit_index_1=5,
        special_effect_id=5434
    )
    Event_11325110(
        5,
        part_index=6,
        npc_part_id=3535,
        npc_part_id_1=3535,
        character=1320706,
        model_point=96,
        bit_index=5,
        bit_index_1=6,
        special_effect_id=5435
    )
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
    ForceAnimation(1320700, 3011, wait_for_completion=1)
    Move(1320700, destination=1322710, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1320700, region=1322710)
    ForceAnimation(1320700, 9060, wait_for_completion=1)
    ReplanAI(1320700)
    Restart()
    DisableFlag(11325101)
    Move(1320700, destination=1322701, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1320700, 3014, wait_for_completion=1)
    Move(1320700, destination=1322711, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1320700, region=1322711)
    ForceAnimation(1320700, 9060, wait_for_completion=1)
    ReplanAI(1320700)
    Restart()


@UnknownRestart(11325110)
def Event_11325110(
    _,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    character: int,
    model_point: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect_id: int,
):
    """Event 11325110"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(1320700, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, special_effect_id)
    End()
    IfCharacterBackreadEnabled(0, 1320700)
    CreateNPCPart(1320700, npc_part_id=npc_part_id, part_index=part_index, part_health=270)
    IfCharacterPartHealthLessThanOrEqual(1, 1320700, npc_part_id=npc_part_id_1, value=0)
    IfFlagDisabled(1, 11325120)
    IfAttacked(1, attacked_entity=1320700, attacker=PLAYER)
    IfHealthLessThanOrEqual(2, 1320700, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(1320700)
    Move(
        character,
        destination=1320700,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=1320700,
    )
    EnableCharacter(character)
    ForceAnimation(character, 8100)
    ForceAnimation(1320700, 8000)
    SetDisplayMask(1320700, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, special_effect_id)


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
    Kill(1320700, award_souls=1)


@RestartOnRest(11325150)
def Event_11325150(_, character: int, radius: float):
    """Event 11325150"""
    EndIfThisEventSlotFlagEnabled()
    SetStandbyAnimationSettings(character, standby_animation=9000)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=radius)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


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
    AICommand(1320800, command_id=20, command_slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1320800)
    CreateNPCPart(1320800, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200)
    IfCharacterPartHealthLessThanOrEqual(1, 1320800, npc_part_id=3451, value=0)
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
    AICommand(1320800, command_id=20, command_slot=0)
    ReplanAI(1320800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34510000, host_only=True)


@NeverRestart(11320200)
def Event_11320200(_, obj: int, flag: int):
    """Event 11320200"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(obj)
    End()
    IfObjectDestroyed(0, obj)
    EnableFlag(flag)


@RestartOnRest(11320300)
def Event_11320300(_, character: int, first_flag: uint, last_flag: uint, flag: int):
    """Event 11320300"""
    DisableCharacter(character)
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    IfFlagEnabled(0, flag)
    EnableCharacter(character)
    IfCharacterDead(0, character)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33000000, host_only=True)
    End()


@NeverRestart(11320600)
def Event_11320600(_, obj: int, obj_act_id: int):
    """Event 11320600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    SetObjectActivation(obj, obj_act_id=-1, state=0)
    EnableTreasure(obj=obj)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(11320510)
def Event_11320510(_, character: int, flag: int):
    """Event 11320510"""
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
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11320520)
def Event_11320520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11320520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11320534)
def Event_11320534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11320534"""
    IfFlagDisabled(1, 1512)
    IfFlagDisabled(1, 1547)
    IfFlagDisabled(1, 1548)
    IfFlagEnabled(1, 1507)
    IfFlagEnabled(1, 11410593)
    IfFlagEnabled(1, 11020606)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11320535)
def Event_11320535(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11320535"""
    IfFlagDisabled(1, 1512)
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1511)
    IfFlagEnabled(-1, 11320591)
    IfFlagEnabled(-1, 1548)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterBackreadDisabled(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11320540)
def Event_11320540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11320540"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1545)
    IfFlagEnabled(1, 11020606)
    IfFlagEnabled(1, 1511)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11320541)
def Event_11320541(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11320541"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1546)
    IfFlagEnabled(1, 11320591)
    IfCharacterBackreadDisabled(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11320580)
def Event_11320580():
    """Event 11320580"""
    IfFlagEnabled(0, 11325030)
    RotateToFaceEntity(PLAYER, target_entity=1320800)
    ForceAnimation(PLAYER, 7910, wait_for_completion=1)
    ForceAnimation(PLAYER, 7911, loop=1)
    IfFlagDisabled(0, 11325030)
    SetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=1)
    Restart()
