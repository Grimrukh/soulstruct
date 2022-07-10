"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11320000()
    Event_11325000()
    Event_11320800()
    Event_11325001()
    if FlagEnabled(11320100):
        Event_11320100()
    else:
        Event_11320110()
        Event_11320100()
        Event_11325100()
        Event_11320101()
    Event_11322000()
    Event_11322001()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    EnableImmortality(1320008)


@NeverRestart(11320000)
def Event_11320000():
    """Event 11320000"""
    RegisterBonfire(bonfire_flag=11320992, obj=1321960)
    RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=1321000)
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=1321001)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=1321002)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=1321003)
    Event_11320200(0, obj=1321004, flag=11320200)
    Event_11320200(1, 1321005, 11320201)


@RestartOnRest(11320110)
def Event_11320110():
    """Event 11320110"""
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(1320001)
    DisableCharacter(1320002)
    DisableCharacter(1320003)
    DisableCharacter(1320004)
    DisableCharacter(1320005)
    DisableCharacter(1320006)
    DisableCharacter(1320007)
    if FlagEnabled(11320100):
        return
    Event_11325121()
    Event_11325110(
        0,
        part_index=1,
        npc_part_id=3530,
        npc_part_id_1=3530,
        character=1320001,
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
        character=1320002,
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
        character=1320003,
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
        character=1320004,
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
        character=1320005,
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
        character=1320006,
        model_point=96,
        bit_index=5,
        bit_index_1=6,
        special_effect_id=5435
    )
    Event_11325110(6, 8, 3536, 3536, 1320007, 97, 6, 7, 5436)


@RestartOnRest(11325100)
def Event_11325100():
    """Event 11325100"""
    AND_1.Add(CharacterBackreadEnabled(1320000))
    AND_1.Add(CharacterHasTAEEvent(1320000, tae_event_id=300))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(11325101):
        EnableFlag(11325101)
        Move(1320000, destination=1322000, destination_type=CoordEntityType.Region, short_move=True)
        ForceAnimation(1320000, 3011, wait_for_completion=True)
        Move(1320000, destination=1322001, destination_type=CoordEntityType.Region, short_move=True)
        SetNest(1320000, region=1322001)
        ForceAnimation(1320000, 9060, wait_for_completion=True)
        ReplanAI(1320000)
        Restart()
    DisableFlag(11325101)
    Move(1320000, destination=1322002, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1320000, 3014, wait_for_completion=True)
    Move(1320000, destination=1322003, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(1320000, region=1322003)
    ForceAnimation(1320000, 9060, wait_for_completion=True)
    ReplanAI(1320000)
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
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(1320000, bit_index=bit_index, switch_type=OnOffChange.On)
        SetCollisionMask(1320000, bit_index=bit_index_1, switch_type=OnOffChange.Off)
        AddSpecialEffect(1320000, special_effect_id)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(1320000))
    
    CreateNPCPart(1320000, npc_part_id=npc_part_id, part_index=part_index, part_health=270)
    AND_1.Add(CharacterPartHealthLessThanOrEqual(1320000, npc_part_id=npc_part_id_1, value=0))
    AND_1.Add(FlagDisabled(11325120))
    AND_1.Add(Attacked(attacked_entity=1320000, attacker=PLAYER))
    AND_2.Add(HealthRatioLessThanOrEqual(1320000, value=0.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(1320000)
    Move(
        character,
        destination=1320000,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=1320000,
    )
    EnableCharacter(character)
    ForceAnimation(character, 8100)
    ForceAnimation(1320000, 8000)
    SetDisplayMask(1320000, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(1320000, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320000, special_effect_id)


@UnknownRestart(11325121)
def Event_11325121():
    """Event 11325121"""
    MAIN.Await(CharacterHasTAEEvent(1320000, tae_event_id=500))
    
    EnableFlag(11325120)
    
    MAIN.Await(CharacterHasTAEEvent(1320000, tae_event_id=600))
    
    DisableFlag(11325120)
    Restart()


@RestartOnRest(11320100)
def Event_11320100():
    """Event 11320100"""
    if ThisEventFlagEnabled():
        DisableCharacter(1320000)
        DisableCharacter(1320001)
        DisableCharacter(1320002)
        DisableCharacter(1320003)
        DisableCharacter(1320004)
        DisableCharacter(1320005)
        DisableCharacter(1320006)
        DisableCharacter(1320007)
        End()
    
    MAIN.Await(CharacterDead(1320000))
    
    AwardItemLot(35300000, host_only=False)


@NeverRestart(11320101)
def Event_11320101():
    """Event 11320101"""
    if FlagEnabled(11320100):
        return
    AND_1.Add(FlagEnabled(11325110))
    AND_1.Add(FlagEnabled(11325111))
    AND_1.Add(FlagEnabled(11325112))
    AND_1.Add(FlagEnabled(11325113))
    AND_1.Add(FlagEnabled(11325114))
    AND_1.Add(FlagEnabled(11325115))
    AND_1.Add(FlagEnabled(11325116))
    
    MAIN.Await(AND_1)
    
    Kill(1320000, award_souls=True)


@NeverRestart(11325000)
def Event_11325000():
    """Event 11325000"""
    if ThisEventFlagEnabled():
        return
    SetStandbyAnimationSettings(1320008, standby_animation=9000)
    AND_1.Add(Host())
    AND_1.Add(EntityWithinDistance(entity=1320008, other_entity=PLAYER, radius=30.0))
    
    MAIN.Await(AND_1)
    
    SetStandbyAnimationSettings(1320008, cancel_animation=9060)


@RestartOnRest(11320800)
def Event_11320800():
    """Event 11320800"""
    if ThisEventFlagEnabled():
        DisableCharacter(1320008)
        End()
    
    MAIN.Await(CharacterDead(1320008))
    
    EnableFlag(11320800)


@RestartOnRest(11325001)
def Event_11325001():
    """Event 11325001"""
    DisableCharacter(1320009)
    if FlagEnabled(11320800):
        return
    if ThisEventFlagEnabled():
        SetDisplayMask(1320008, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(1320008, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(1320008, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(1320008))
    
    CreateNPCPart(1320008, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200)
    AND_1.Add(CharacterPartHealthLessThanOrEqual(1320008, npc_part_id=3451, value=0))
    AND_2.Add(HealthRatioLessThanOrEqual(1320008, value=0.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(1320008, 8000)
    
    MAIN.Await(CharacterHasTAEEvent(1320008, tae_event_id=400))
    
    EnableCharacter(1320009)
    Move(
        1320009,
        destination=1320008,
        destination_type=CoordEntityType.Character,
        model_point=19,
        copy_draw_parent=1320008,
    )
    ForceAnimation(1320009, 8100)
    SetDisplayMask(1320008, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1320008, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1320008, command_id=20, command_slot=0)
    ReplanAI(1320008)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return


@NeverRestart(11320200)
def Event_11320200(_, obj: int, flag: int):
    """Event 11320200"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    
    MAIN.Await(ObjectDestroyed(obj))
    
    EnableFlag(flag)


@NeverRestart(11322000)
def Event_11322000():
    """Event 11322000"""
    AND_1.Add(InsideMap(game_map=CATACOMBS))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1322004))
    AND_3.Add(InsideMap(game_map=ASH_LAKE))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_3)
    DisableMapCollision(collision=1323200)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1322004))
    
    EnableMapCollision(collision=1323200)
    Restart()


@NeverRestart(11322001)
def Event_11322001():
    """Event 11322001"""
    MAIN.Await(InsideMap(game_map=BLIGHTTOWN))
    
    DisableMapCollision(collision=1323201)
    DisableMapCollision(collision=1323202)
    
    MAIN.Await(InsideMap(game_map=ASH_LAKE))
    
    EnableMapCollision(collision=1323201)
    EnableMapCollision(collision=1323202)
    Restart()
