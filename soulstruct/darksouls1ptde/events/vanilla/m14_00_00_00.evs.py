"""
Blighttown / Quelaag's Domain

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11400992, obj=1401960, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11400984, obj=1401961)
    RegisterBonfire(bonfire_flag=11400976, obj=1401962)
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=1401140)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=1401141)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=1401142)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=1401143)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=1401144)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=1401145)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=1401146)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=1401147)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=1401148)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=1401149)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=1401150)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=1401151)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=1401152)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=1401153)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=1401154)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=1401155)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=1401156)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=1401157)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=1401158)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=1401159)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=1401160)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=1401161)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=1401162)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=1401163)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=1401164)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=1401165)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=1401166)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=1401167)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=1401168)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=1401169)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=1401170)
    SkipLinesIfClient(6)
    DisableObject(1401994)
    DeleteVFX(1401995, erase_root_only=False)
    DisableObject(1401996)
    DeleteVFX(1401997, erase_root_only=False)
    DisableObject(1401998)
    DeleteVFX(1401999, erase_root_only=False)
    AND_1.Add(FlagEnabled(11000810))
    AND_1.Add(FlagEnabled(11410810))
    AND_1.Add(FlagEnabled(11410811))
    SkipLinesIfConditionTrue(2, AND_1)
    DisableObject(1401601)
    SkipLines(1)
    EnableTreasure(obj=1401601)
    Event_11400090(1, obj=1401702, vfx_id=1401703, destination=1402602, destination_1=1402603)
    Event_11405090()
    Event_11405091()
    Event_11405092()
    Event_11400900()
    Event_11400800()
    Event_11405000()
    Event_11400200()
    Event_11400210()
    Event_11400220()
    Event_11400230()
    Event_140()
    DisableSoundEvent(sound_id=1403800)
    if FlagEnabled(9):
        Event_11405392()
        DisableObject(1401990)
        DeleteVFX(1401991, erase_root_only=False)
        DisableObject(1401992)
        DeleteVFX(1401993, erase_root_only=False)
    else:
        Event_11405390()
        Event_11405391()
        Event_11405393()
        Event_11405392()
        Event_11400001()
        Event_11405394()
        Event_11405395()
    Event_11405100(0, entity=1401000, region=1402000, region_1=1402001, region_2=1402002)
    Event_11405110(
        0,
        entity=1401002,
        region=1402020,
        region_1=1402021,
        region_2=1402022,
        region_3=1402023,
        region_4=1402024,
    )
    Event_11405350(
        0,
        character=6160,
        character_1=1400411,
        character_2=1400412,
        character_3=1400413,
        character_4=1400414,
        character_5=1400415,
        left=1,
    )
    Event_11405350(
        3,
        character=1400402,
        character_1=1400426,
        character_2=1400427,
        character_3=1400428,
        character_4=1400429,
        character_5=1400430,
        left=0,
    )
    Event_11405350(
        4,
        character=1400403,
        character_1=1400431,
        character_2=1400432,
        character_3=1400433,
        character_4=1400434,
        character_5=1400435,
        left=0,
    )
    Event_11400100(0, flag=11405340, region=1402200, entity=1403000)
    Event_11400100(1, flag=11405341, region=1402201, entity=1403001)
    Event_11400100(2, flag=11405342, region=1402202, entity=1403002)
    Event_11405200(0, character=1400450, obj=1401300)
    Event_11405250(0, character=1400100)
    Event_11405250(1, character=1400101)
    Event_11405250(2, character=1400102)
    Event_11405250(3, character=1400103)
    Event_11405250(4, character=1400104)
    Event_11400850(0, character=1400200, item_lot=25300200)
    Event_11400850(1, character=1400201, item_lot=25300200)
    Event_11400850(2, character=1400202, item_lot=25300200)
    Event_11400850(3, character=1400203, item_lot=25300200)
    Event_11400850(4, character=1400204, item_lot=25300200)
    Event_11400850(5, character=1400205, item_lot=25300200)
    Event_11400850(6, character=1400206, item_lot=25300200)
    Event_11400850(7, character=1400207, item_lot=25300200)
    Event_11400850(8, character=1400208, item_lot=25300200)
    Event_11400600(0, obj=1401650, obj_act_id=11400600)
    Event_11400600(1, obj=1401651, obj_act_id=11400601)
    Event_11400600(2, obj=1401652, obj_act_id=11400602)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6531, event_flag=8940)
    HumanityRegistration(6530, event_flag=8940)
    Event_11405030()
    Event_11405032()
    Event_11405035()
    Event_11400901()
    if FlagDisabled(1257):
        DisableCharacter(6132)
    SetTeamTypeAndExitStandbyAnimation(6132, team_type=TeamType.HostileAlly)
    Event_11400520(0, character=6132, first_flag=1250, last_flag=1259, flag=1254)
    Event_11400530(0, character=6132, first_flag=1250, last_flag=1259, flag=1257)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    Event_11400520(1, character=1400700, first_flag=1270, last_flag=1279, flag=1272)
    if FlagDisabled(1280):
        SetNest(6160, region=1402300)
        Move(6160, destination=1402300, destination_type=CoordEntityType.Region, short_move=True)
    Event_11400520(2, character=6160, first_flag=1280, last_flag=1289, flag=1284)
    Event_11400531(0, character=6160, first_flag=1280, last_flag=1289, flag=1281)
    Event_11400532(0, character=6160, first_flag=1280, last_flag=1289, flag=1286)
    Event_11400501(0, character=6160, flag=1282)
    Event_11400502(0, character=6160, flag=1283)
    Event_11400503(0, character=6160, flag=1287)
    Event_11400533()
    HumanityRegistration(6170, event_flag=8398)
    SkipLinesIfFlagEnabled(2, 1296)
    SkipLinesIfFlagEnabled(1, 1290)
    SkipLines(1)
    DisableCharacter(6170)
    Event_11400510(3, character=6170, flag=1294)
    Event_11400520(3, character=6170, first_flag=1290, last_flag=1309, flag=1295)
    Event_11400536(0, character=6170, first_flag=1290, last_flag=1309, flag=1291)
    Event_11400537(0, character=6170, first_flag=1290, last_flag=1309, flag=1292)
    Event_11400538(0, character=6170, first_flag=1290, last_flag=1309, flag=1293)
    Event_11400539(0, character=6170, first_flag=1290, last_flag=1309, flag=1296)
    HumanityRegistration(6282, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1502)
    SkipLinesIfFlagEnabled(1, 1501)
    DisableCharacter(6282)
    Event_11400510(4, character=6282, flag=1512)
    Event_11400520(4, character=6282, first_flag=1490, last_flag=1514, flag=1513)
    Event_11400551(0, character=6282, first_flag=1490, last_flag=1514, flag=1501)
    Event_11400552(0, character=6282, first_flag=1490, last_flag=1514, flag=1502)
    Event_11400553()
    Event_11400554(0, character=6282)
    HumanityRegistration(6311, event_flag=8470)
    HumanityRegistration(6421, event_flag=8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagEnabled(8, 11405022)
    AND_1.Add(Host())
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(FlagEnabled(1601))
    SkipLinesIfConditionTrue(2, AND_1)
    DisableCharacter(6311)
    DisableCharacter(6421)
    Event_11400520(5, character=6311, first_flag=1600, last_flag=1619, flag=1604)
    Event_11400520(6, character=6421, first_flag=1760, last_flag=1769, flag=1764)
    Event_11400504(0, character=6311, flag=1603, character_1=6421)
    Event_11400560(0, character=6311, first_flag=1600, last_flag=1619, flag=1601, character_1=6421)
    Event_11400566(0, character=6311, character_1=6421)
    Event_11400567(0, character=6311, character_1=6421)
    SkipLinesIfConditionFalse(2, AND_1)
    WaitFrames(frames=1)
    EnableFlag(11405022)
    DisableFlag(1766)


@ContinueOnRest(11400090)
def Event_11400090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11400090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11405090)
def Event_11405090():
    """Event 11405090"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1400900)
    DisableCharacter(1400901)
    DisableCharacter(1400902)
    DisableCharacter(1400903)
    DisableCharacter(1400904)
    DisableCharacter(1400905)
    DisableCharacter(1400906)
    DisableCharacter(1400907)
    DisableCharacter(1400908)
    DisableCharacter(1400909)
    
    MAIN.Await(FlagEnabled(11400080))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1400900)
    EnableCharacter(1400901)
    EnableCharacter(1400902)
    EnableCharacter(1400903)
    EnableCharacter(1400904)
    EnableCharacter(1400905)
    EnableCharacter(1400906)
    EnableCharacter(1400907)
    EnableCharacter(1400908)
    EnableCharacter(1400909)


@RestartOnRest(11405091)
def Event_11405091():
    """Event 11405091"""
    OR_1.Add(FlagEnabled(11405095))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11400080)
    DisableFlag(11405095)
    EnableFlag(5001)
    Kill(1400900)
    Kill(1400901)
    Kill(1400902)
    Kill(1400903)
    Kill(1400904)
    Kill(1400905)
    Kill(1400906)
    Kill(1400907)
    Kill(1400908)
    Kill(1400909)


@RestartOnRest(11405092)
def Event_11405092():
    """Event 11405092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11400080))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11400080))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11400080))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11400080))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11400080))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11400080))
    if not OR_6:
        return RESTART
    EnableFlag(11400080)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=BLIGHTTOWN))
    if not AND_7:
        return RESTART
    DisableFlag(11400080)
    EnableFlag(11405095)


@ContinueOnRest(11405390)
def Event_11405390():
    """Event 11405390"""
    AND_1.Add(FlagDisabled(9))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1401990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11405391)
def Event_11405391():
    """Event 11405391"""
    AND_1.Add(FlagDisabled(9))
    AND_1.Add(FlagEnabled(11405393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1401990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11405393)
def Event_11405393():
    """Event 11405393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(9))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1402996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1400800)


@RestartOnRest(11405392)
def Event_11405392():
    """Event 11405392"""
    if FlagEnabled(9):
        DisableBackread(1400800)
        Kill(1400800)
        End()
    Event_11405396()
    Event_11405397()
    if FlagDisabled(11400000):
        DisableCharacter(1400800)
    DisableAI(1400800)
    AND_1.Add(FlagEnabled(11405393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1402996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(11, 11400000)
    DeleteVFX(1401991, erase_root_only=False)
    DeleteVFX(1401993, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    CreateVFX(1401991)
    CreateVFX(1401993)
    EnableCharacter(1400800)
    EnableFlag(11400000)
    EnableAI(1400800)
    EnableBossHealthBar(1400800, name=5280)


@ContinueOnRest(11400001)
def Event_11400001():
    """Event 11400001"""
    MAIN.Await(CharacterDead(1400800))
    
    EnableFlag(9)
    KillBoss(game_area_param_id=1400800)
    DisableObject(1401990)
    DeleteVFX(1401991)
    DisableObject(1401992)
    DeleteVFX(1401993)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(1400800)


@ContinueOnRest(11405394)
def Event_11405394():
    """Event 11405394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(9))
    AND_1.Add(FlagEnabled(11405392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11405391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1402990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1403800)


@ContinueOnRest(11405395)
def Event_11405395():
    """Event 11405395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(9))
    AND_1.Add(FlagEnabled(11405394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1403800)


@EndOnRest(11405396)
def Event_11405396():
    """Event 11405396"""
    AND_1.Add(CharacterAlive(1400800))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    
    MAIN.Await(CharacterBackreadEnabled(1400800))
    
    CreateNPCPart(1400800, npc_part_id=5281, part_index=NPCPartType.Part2, part_health=300)
    SetNPCPartEffects(1400800, npc_part_id=5281, material_sfx_id=75, material_vfx_id=75)
    AND_2.Add(CharacterPartHealth(1400800, npc_part_id=5281) <= 0)
    AND_3.Add(HealthRatio(1400800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
    ForceAnimation(1400800, 3011, wait_for_completion=True)
    Restart()


@EndOnRest(11405397)
def Event_11405397():
    """Event 11405397"""
    AND_1.Add(CharacterAlive(1400800))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    
    MAIN.Await(CharacterBackreadEnabled(1400800))
    
    CreateNPCPart(1400800, npc_part_id=5280, part_index=NPCPartType.Part1, part_health=1)
    SetNPCPartEffects(1400800, npc_part_id=5280, material_sfx_id=60, material_vfx_id=60)
    AND_2.Add(CharacterPartHealth(1400800, npc_part_id=5280) <= 0)
    AND_3.Add(HealthRatio(1400800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
    ForceAnimation(1400800, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest(11400800)
def Event_11400800():
    """Event 11400800"""
    if ThisEventFlagEnabled():
        DisableCharacter(1400700)
        DisableSoundEvent(sound_id=1403801)
        DisableMapCollision(collision=1403100)
        DisableMapCollision(collision=1403101)
        End()
    
    MAIN.Await(CharacterDead(1400700))
    
    EnableFlag(140)
    DisableSoundEvent(sound_id=1403801)
    DisableMapCollision(collision=1403100)
    DisableMapCollision(collision=1403101)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerCovenant(Covenant.ChaosServant))
    if not AND_1:
        return
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


@ContinueOnRest(11405000)
def Event_11405000():
    """Event 11405000"""
    if ThisEventFlagEnabled():
        AddSpecialEffect(1400700, 5401)
        End()
    
    MAIN.Await(HealthRatio(1400700) != 1.0)
    
    AddSpecialEffect(1400700, 5401)


@RestartOnRest(11400900)
def Event_11400900():
    """Event 11400900"""
    if FlagEnabled(11400902):
        DisableCharacter(1400000)
        End()
    AND_1.Add(CharacterAlive(1400000))
    SkipLinesIfConditionTrue(2, AND_1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    
    MAIN.Await(HealthRatio(1400000) <= 0.0)
    
    EnableNetworkSync()
    EzstateAIRequest(1400000, command_id=1200, command_slot=0)
    Restart()


@ContinueOnRest(11405100)
def Event_11405100(_, entity: int, region: int, region_1: int, region_2: int):
    """Event 11405100"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@ContinueOnRest(11405110)
def Event_11405110(_, entity: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 11405110"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_3))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_3))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@RestartOnRest(11405250)
def Event_11405250(_, character: int):
    """Event 11405250"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(
        character,
        npc_part_id=2811,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2811, material_sfx_id=1, material_vfx_id=1)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    SetNPCPartHealth(character, npc_part_id=2811, desired_health=0, overwrite_max=False)


@RestartOnRest(11405300)
def Event_11405300():
    """Event 11405300"""
    Event_11405301(0, character=1400500, part_index=1, npc_part_id=3290, npc_part_id_1=3290, flag=11405301)
    Event_11405310(0, character=1400500, flag=11405301, bit_index=0, bit_index_1=1)
    Event_11405310(1, character=1400500, flag=11405301, bit_index=2, bit_index_1=3)
    Event_11405320(0, character=1400500, flag=11405301, obj=1401500, obj_1=1401501, dummy_id=120, dummy_id_1=123)
    Event_11405320(1, character=1400500, flag=11405301, obj=1401502, obj_1=1401503, dummy_id=126, dummy_id_1=129)
    Event_11405330(
        0,
        character=1400500,
        flag=11405301,
        character_1=1400600,
        character_2=1400601,
        dummy_id=120,
        dummy_id_1=123,
    )
    Event_11405330(
        1,
        character=1400500,
        flag=11405301,
        character_1=1400602,
        character_2=1400603,
        dummy_id=126,
        dummy_id_1=129,
    )
    Event_11405301(1, character=1400500, part_index=2, npc_part_id=3291, npc_part_id_1=3291, flag=11405302)
    Event_11405310(2, character=1400500, flag=11405302, bit_index=5, bit_index_1=11)
    Event_11405320(2, character=1400500, flag=11405302, obj=1401504, obj_1=1401505, dummy_id=135, dummy_id_1=137)
    Event_11405330(
        2,
        character=1400500,
        flag=11405302,
        character_1=1400604,
        character_2=1400605,
        dummy_id=135,
        dummy_id_1=137,
    )
    Event_11405330(
        3,
        character=1400500,
        flag=11405302,
        character_1=1400606,
        character_2=1400607,
        dummy_id=153,
        dummy_id_1=155,
    )
    Event_11405301(2, character=1400500, part_index=3, npc_part_id=3292, npc_part_id_1=3292, flag=11405303)
    Event_11405310(3, character=1400500, flag=11405303, bit_index=6, bit_index_1=7)
    Event_11405310(4, character=1400500, flag=11405303, bit_index=8, bit_index_1=10)
    Event_11405320(3, character=1400500, flag=11405303, obj=1401506, obj_1=1401507, dummy_id=138, dummy_id_1=141)
    Event_11405320(4, character=1400500, flag=11405303, obj=1401508, obj_1=1401509, dummy_id=144, dummy_id_1=150)
    Event_11405330(
        4,
        character=1400500,
        flag=11405303,
        character_1=1400608,
        character_2=1400609,
        dummy_id=138,
        dummy_id_1=141,
    )
    Event_11405330(
        5,
        character=1400500,
        flag=11405303,
        character_1=1400610,
        character_2=1400611,
        dummy_id=144,
        dummy_id_1=150,
    )
    Event_11405301(3, character=1400500, part_index=4, npc_part_id=3293, npc_part_id_1=3293, flag=11405304)
    Event_11405310(5, character=1400500, flag=11405304, bit_index=4, bit_index_1=9)
    Event_11405320(5, character=1400500, flag=11405304, obj=1401510, obj_1=1401511, dummy_id=132, dummy_id_1=134)
    Event_11405330(
        6,
        character=1400500,
        flag=11405304,
        character_1=1400612,
        character_2=1400613,
        dummy_id=132,
        dummy_id_1=134,
    )
    Event_11405330(
        7,
        character=1400500,
        flag=11405304,
        character_1=1400614,
        character_2=1400615,
        dummy_id=150,
        dummy_id_1=152,
    )


@EndOnRest(11405301)
def Event_11405301(_, character: int, part_index: short, npc_part_id: short, npc_part_id_1: int, flag: int):
    """Event 11405301"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=100)
    AND_1.Add(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11405290, 11405291))
    AND_3.Add(FlagEnabled(11405290))
    AND_4.Add(FlagEnabled(11405291))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(flag)
    if FlagEnabled(11405301):
        ForceAnimation(character, 8000)
    if FlagEnabled(11405302):
        ForceAnimation(character, 8010)


@EndOnRest(11405310)
def Event_11405310(_, character: int, flag: int, bit_index: uchar, bit_index_1: uchar):
    """Event 11405310"""
    if FlagDisabled(flag):
        AND_1.Add(FlagEnabled(flag))
        AND_2.Add(CharacterDead(character))
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfLastConditionResultTrue(input_condition=AND_2)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)


@EndOnRest(11405320)
def Event_11405320(_, character: int, flag: int, obj: int, obj_1: int, dummy_id: short, dummy_id_1: short):
    """Event 11405320"""
    DisableObject(obj)
    DisableObject(obj_1)
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    EnableObject(obj)
    EnableObject(obj_1)
    MoveObjectToCharacter(obj, character=character, dummy_id=dummy_id)
    MoveObjectToCharacter(obj_1, character=character, dummy_id=dummy_id_1)
    DestroyObject(obj)
    DestroyObject(obj_1)


@EndOnRest(11405330)
def Event_11405330(
    _,
    character: int,
    flag: int,
    character_1: int,
    character_2: int,
    dummy_id: int,
    dummy_id_1: int,
):
    """Event 11405330"""
    if FlagEnabled(flag):
        return
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    ResetAnimation(character)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id_1,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)


@RestartOnRest(11405350)
def Event_11405350(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    left: int,
):
    """Event 11405350"""
    SkipLinesIfValueEqual(1, left=left, right=0)
    SkipLinesIfFlagEnabled(1, 11400533)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
        End()
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    
    MAIN.Await(CharacterDead(character))
    
    SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=101,
        copy_draw_parent=character,
    )
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=102,
        copy_draw_parent=character,
    )
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=103,
        copy_draw_parent=character,
    )
    Move(
        character_5,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=104,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableCharacter(character_5)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)
    ForceAnimation(character_3, 7000)
    ForceAnimation(character_4, 7000)
    ForceAnimation(character_5, 7000)


@ContinueOnRest(11400100)
def Event_11400100(_, flag: int, region: int, entity: int):
    """Event 11400100"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    EnableFlag(flag)
    DisableSpawner(entity=entity)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    DisableFlag(flag)
    EnableSpawner(entity=entity)
    Restart()


@RestartOnRest(11400850)
def Event_11400850(_, character: int, item_lot: int):
    """Event 11400850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11400600)
def Event_11400600(_, obj: int, obj_act_id: int):
    """Event 11400600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11400200)
def Event_11400200():
    """Event 11400200"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1401110, obj_act_id=-1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=11400201))
    
    MAIN.Await(HealthRatio(PLAYER) > 0.0)
    
    DisableBackread(1400800)
    DisableBackread(1400700)
    WaitFrames(frames=1)
    if FlagDisabled(11010700):
        PlayCutscene(140010, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(140015, cutscene_flags=0, player_id=10000)
        EnableFlag(11500200)
    WaitFrames(frames=1)
    if FlagDisabled(9):
        EnableBackread(1400800)
    EnableBackread(1400700)
    EnableFlag(11400200)
    AwardAchievement(achievement_id=30)
    AwardItemLot(9030, host_only=True)


@ContinueOnRest(11400210)
def Event_11400210():
    """Event 11400210"""
    if ThisEventFlagEnabled():
        DisableObject(1401200)
        End()
    
    MAIN.Await(ObjectDestroyed(1401200))
    
    EnableFlag(11400210)


@ContinueOnRest(11400220)
def Event_11400220():
    """Event 11400220"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1402400))
    
    AddSpecialEffect(PLAYER, 4140)
    Restart()


@ContinueOnRest(11400230)
def Event_11400230():
    """Event 11400230"""
    DisableNetworkSync()
    if FlagEnabled(590):
        EndOfAnimation(obj=1001200, animation_id=1)
        End()
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(590))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1001200)
    Restart()


@RestartOnRest(11405200)
def Event_11405200(_, character: int, obj: int):
    """Event 11405200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    RestoreObject(obj)
    DisableCharacterCollision(character)
    DisableGravity(character)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, dummy_id=100, short_move=True)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(ObjectDestroyed(obj))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character)
    EnableCharacterCollision(character)
    EnableGravity(character)


@ContinueOnRest(11400510)
def Event_11400510(_, character: int, flag: int):
    """Event 11400510"""
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventSlotFlagDisabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400520)
def Event_11400520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400501)
def Event_11400501(_, character: int, flag: int):
    """Event 11400501"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1284))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1272))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400502)
def Event_11400502(_, character: int, flag: int):
    """Event 11400502"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    OR_2.Add(FlagEnabled(1280))
    OR_2.Add(FlagEnabled(1281))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400503)
def Event_11400503(_, character: int, flag: int):
    """Event 11400503"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1286))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400504)
def Event_11400504(_, character: int, flag: int, character_1: int):
    """Event 11400504"""
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1601))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1763))
    AND_2.Add(FlagEnabled(1760))
    AND_2.Add(HealthRatio(character_1) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(character_1) > 0.0)
    AND_2.Add(Attacked(attacked_entity=character_1, attacker=PLAYER))
    AND_2.Add(ThisEventFlagDisabled())
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(1763))
    OR_2.Add(FlagEnabled(745))
    AND_3.Add(OR_2)
    AND_3.Add(ThisEventFlagDisabled())
    AND_4.Add(OR_2)
    AND_4.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(4, input_condition=AND_4)
    if FlagDisabled(1604):
        EnableFlag(flag)
    if FlagDisabled(1764):
        EnableFlag(1763)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Enemy)
    EnableCharacter(character_1)
    SetTeamTypeAndExitStandbyAnimation(character_1, team_type=TeamType.Enemy)
    if ThisEventFlagEnabled():
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_7.Add(OR_7)
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    if not AND_7:
        return
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


@ContinueOnRest(11400530)
def Event_11400530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400530"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1256))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)


@ContinueOnRest(11400531)
def Event_11400531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400531"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1280))
    AND_1.Add(FlagEnabled(11400593))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11405001)
    SetNest(character, region=1402301)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.FightingAlly)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character, region=1402300))
    AND_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11405001)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Ally)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@ContinueOnRest(11400532)
def Event_11400532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400532"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1281))
    AND_1.Add(FlagEnabled(753))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@RestartOnRest(11400533)
def Event_11400533():
    """Event 11400533"""
    if ThisEventFlagEnabled():
        DisableCharacter(1400411)
        DisableCharacter(1400412)
        DisableCharacter(1400413)
        DisableCharacter(1400414)
        DisableCharacter(1400415)
        End()
    
    MAIN.Await(CharacterDead(6160))
    
    End()


@ContinueOnRest(11400536)
def Event_11400536(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400536"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1290))
    OR_1.Add(PlayerHasWeapon(1331000))
    OR_1.Add(PlayerHasWeapon(1331100))
    OR_1.Add(PlayerHasWeapon(1331200))
    OR_1.Add(PlayerHasWeapon(1331300))
    OR_1.Add(PlayerHasWeapon(1331400))
    OR_1.Add(PlayerHasWeapon(1331500))
    OR_1.Add(PlayerHasWeapon(1332000))
    OR_1.Add(PlayerHasWeapon(1332100))
    OR_1.Add(PlayerHasWeapon(1332200))
    OR_1.Add(PlayerHasWeapon(1332300))
    OR_1.Add(PlayerHasWeapon(1332400))
    OR_1.Add(PlayerHasWeapon(1332500))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11400537)
def Event_11400537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400537"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1293))
    AND_1.Add(FlagEnabled(11400595))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400538)
def Event_11400538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400538"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1291))
    AND_1.Add(FlagEnabled(10))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400539)
def Event_11400539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400539"""
    AND_1.Add(FlagEnabled(1290))
    AND_1.Add(FlagEnabled(10))
    AND_2.Add(FlagDisabled(1294))
    AND_2.Add(FlagEnabled(1291))
    AND_2.Add(FlagDisabled(71400061))
    AND_2.Add(FlagEnabled(10))
    AND_3.Add(FlagDisabled(1294))
    AND_3.Add(FlagEnabled(1292))
    AND_3.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11400551)
def Event_11400551(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400551"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1497))
    AND_1.Add(FlagEnabled(11020592))
    AND_1.Add(InsideMap(game_map=BLIGHTTOWN))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(814)


@ContinueOnRest(11400552)
def Event_11400552(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400552"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1501))
    AND_1.Add(FlagEnabled(11400590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11400553)
def Event_11400553():
    """Event 11400553"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11400590))
    
    End()


@ContinueOnRest(11400554)
def Event_11400554(_, character: int):
    """Event 11400554"""
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(1501))
    
    MAIN.Await(OR_1)
    
    if ThisEventFlagDisabled():
        MAIN.Await(FlagDisabled(814))
    SetStandbyAnimationSettings(character, cancel_animation=7856)


@ContinueOnRest(11400560)
def Event_11400560(_, character: int, first_flag: int, last_flag: int, flag: int, character_1: int):
    """Event 11400560"""
    AND_1.Add(Host())
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1600))
    AND_1.Add(FlagEnabled(11400582))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableCharacter(character_1)
    DisableFlag(1766)
    EnableFlag(11405022)


@ContinueOnRest(11400566)
def Event_11400566(_, character: int, character_1: int):
    """Event 11400566"""
    SkipLinesIfHost(1)
    if FlagEnabled(11405022):
        return
    AND_1.Add(FlagEnabled(746))
    if not AND_1:
        return
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableFlag(1766)
    DisableFlag(11405022)


@ContinueOnRest(11400567)
def Event_11400567(_, character: int, character_1: int):
    """Event 11400567"""
    AND_1.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(not AND_2)
    AND_1.Add(FlagDisabled(746))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableFlag(11405022)


@ContinueOnRest(140)
def Event_140():
    """Event 140"""
    DisableNetworkSync()
    AND_1.Add(ThisEventFlagEnabled())
    AND_1.Add(ActionButton(
        prompt_text=10010182,
        anchor_entity=1401960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        dummy_id=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(
        text=10010184,
        anchor_entity=1401960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@ContinueOnRest(11405030)
def Event_11405030():
    """Event 11405030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6531, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11405033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11405031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6531)
    if FlagEnabled(9):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11400901))
    AND_1.Add(CharacterBackreadEnabled(6531))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6531,
        region=1402050,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


@ContinueOnRest(11405032)
def Event_11405032():
    """Event 11405032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11405031))
    AND_1.Add(FlagEnabled(11405393))
    
    MAIN.Await(AND_1)
    
    AICommand(6531, command_id=10, command_slot=0)
    ReplanAI(6531)
    
    MAIN.Await(CharacterInsideRegion(6531, region=1402998))
    
    FaceEntity(6531, target_entity=1402997)
    ForceAnimation(6531, 7410)
    AICommand(6531, command_id=-1, command_slot=0)
    ReplanAI(6531)


@ContinueOnRest(11405035)
def Event_11405035():
    """Event 11405035"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11405036):
        return
    if FlagEnabled(9):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11400901))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1402061))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6530,
        region=1402060,
        summon_flag=11405036,
        dismissal_flag=11405037,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(11400901)
def Event_11400901():
    """Event 11400901"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(11405036))
    AND_1.Add(FlagDisabled(11405037))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(6530)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(6530))
    
    EnableFlag(11400901)
