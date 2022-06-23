"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
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
    DeleteVFX(vfx_id=1401995, erase_root_only=False)
    DisableObject(1401996)
    DeleteVFX(vfx_id=1401997, erase_root_only=False)
    DisableObject(1401998)
    DeleteVFX(vfx_id=1401999, erase_root_only=False)
    IfFlagEnabled(1, 11000810)
    IfFlagEnabled(1, 11410810)
    IfFlagEnabled(1, 11410811)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(1401601)
    SkipLines(1)
    EnableTreasure(obj=1401601)
    Event_11400090(1, 1401702, 1401703, 1402602, 1402603)
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
    SkipLinesIfFlagDisabled(6, 9)
    Event_11405392()
    DisableObject(1401990)
    DeleteVFX(vfx_id=1401991, erase_root_only=False)
    DisableObject(1401992)
    DeleteVFX(vfx_id=1401993, erase_root_only=False)
    SkipLines(7)
    Event_11405390()
    Event_11405391()
    Event_11405393()
    Event_11405392()
    Event_11400001()
    Event_11405394()
    Event_11405395()
    Event_11405100(0, 1401000, 1402000, 1402001, 1402002)
    Event_11405110(0, 1401002, 1402020, 1402021, 1402022, 1402023, 1402024)
    Event_11405350(0, 6160, 1400411, 1400412, 1400413, 1400414, 1400415, 1)
    Event_11405350(3, 1400402, 1400426, 1400427, 1400428, 1400429, 1400430, 0)
    Event_11405350(4, 1400403, 1400431, 1400432, 1400433, 1400434, 1400435, 0)
    Event_11400100(0, 11405340, 1402200, 1403000)
    Event_11400100(1, 11405341, 1402201, 1403001)
    Event_11400100(2, 11405342, 1402202, 1403002)
    Event_11405200(0, 1400450, 1401300)
    Event_11405250(0, 1400100)
    Event_11405250(1, 1400101)
    Event_11405250(2, 1400102)
    Event_11405250(3, 1400103)
    Event_11405250(4, 1400104)
    Event_11400850(0, 1400200, 25300200)
    Event_11400850(1, 1400201, 25300200)
    Event_11400850(2, 1400202, 25300200)
    Event_11400850(3, 1400203, 25300200)
    Event_11400850(4, 1400204, 25300200)
    Event_11400850(5, 1400205, 25300200)
    Event_11400850(6, 1400206, 25300200)
    Event_11400850(7, 1400207, 25300200)
    Event_11400850(8, 1400208, 25300200)
    Event_11400600(0, 1401650, 11400600)
    Event_11400600(1, 1401651, 11400601)
    Event_11400600(2, 1401652, 11400602)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6531, event_flag=8940)
    HumanityRegistration(6530, event_flag=8940)
    Event_11405030()
    Event_11405032()
    Event_11405035()
    Event_11400901()
    SkipLinesIfFlagEnabled(1, 1257)
    DisableCharacter(6132)
    SetTeamTypeAndExitStandbyAnimation(6132, team_type=TeamType.HostileAlly)
    Event_11400520(0, 6132, 1250, 1259, 1254)
    Event_11400530(0, 6132, 1250, 1259, 1257)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    Event_11400520(1, 1400700, 1270, 1279, 1272)
    SkipLinesIfFlagEnabled(2, 1280)
    SetNest(6160, region=1402300)
    Move(6160, destination=1402300, destination_type=CoordEntityType.Region, short_move=True)
    Event_11400520(2, 6160, 1280, 1289, 1284)
    Event_11400531(0, 6160, 1280, 1289, 1281)
    Event_11400532(0, 6160, 1280, 1289, 1286)
    Event_11400501(0, 6160, 1282)
    Event_11400502(0, 6160, 1283)
    Event_11400503(0, 6160, 1287)
    Event_11400533()
    HumanityRegistration(6170, event_flag=8398)
    SkipLinesIfFlagEnabled(2, 1296)
    SkipLinesIfFlagEnabled(1, 1290)
    SkipLines(1)
    DisableCharacter(6170)
    Event_11400510(3, 6170, 1294)
    Event_11400520(3, 6170, 1290, 1309, 1295)
    Event_11400536(0, 6170, 1290, 1309, 1291)
    Event_11400537(0, 6170, 1290, 1309, 1292)
    Event_11400538(0, 6170, 1290, 1309, 1293)
    Event_11400539(0, 6170, 1290, 1309, 1296)
    HumanityRegistration(6282, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1502)
    SkipLinesIfFlagEnabled(1, 1501)
    DisableCharacter(6282)
    Event_11400510(4, 6282, 1512)
    Event_11400520(4, 6282, 1490, 1514, 1513)
    Event_11400551(0, 6282, 1490, 1514, 1501)
    Event_11400552(0, 6282, 1490, 1514, 1502)
    Event_11400553()
    Event_11400554(0, 6282)
    HumanityRegistration(6311, event_flag=8470)
    HumanityRegistration(6421, event_flag=8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagEnabled(8, 11405022)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagEnabled(1, 1601)
    SkipLinesIfConditionTrue(2, 1)
    DisableCharacter(6311)
    DisableCharacter(6421)
    Event_11400520(5, 6311, 1600, 1619, 1604)
    Event_11400520(6, 6421, 1760, 1769, 1764)
    Event_11400504(0, 6311, 1603, 6421)
    Event_11400560(0, 6311, 1600, 1619, 1601, 6421)
    Event_11400566(0, 6311, 6421)
    Event_11400567(0, 6311, 6421)
    SkipLinesIfConditionFalse(2, 1)
    WaitFrames(frames=1)
    EnableFlag(11405022)
    DisableFlag(1766)


@NeverRestart(11400090)
def Event_11400090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
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


@RestartOnRest(11405090)
def Event_11405090():
    """Event 11405090"""
    EndIfThisEventFlagEnabled()
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
    IfFlagEnabled(0, 11400080)
    EndIfFlagEnabled(735)
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
    IfFlagEnabled(-1, 11405095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
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
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11400080)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=BLIGHTTOWN)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11400080)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=BLIGHTTOWN)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11400080)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=BLIGHTTOWN)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11400080)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=BLIGHTTOWN)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11400080)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=BLIGHTTOWN)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11400080)
    RestartIfConditionFalse(-6)
    EnableFlag(11400080)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=BLIGHTTOWN)
    RestartIfConditionFalse(7)
    DisableFlag(11400080)
    EnableFlag(11405095)


@NeverRestart(11405390)
def Event_11405390():
    """Event 11405390"""
    IfFlagDisabled(1, 9)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1401990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11405391)
def Event_11405391():
    """Event 11405391"""
    IfFlagDisabled(1, 9)
    IfFlagEnabled(1, 11405393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1401990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11405393)
def Event_11405393():
    """Event 11405393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 9)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1400800)


@RestartOnRest(11405392)
def Event_11405392():
    """Event 11405392"""
    SkipLinesIfFlagDisabled(3, 9)
    DisableBackread(1400800)
    Kill(1400800)
    End()
    Event_11405396()
    Event_11405397()
    SkipLinesIfFlagEnabled(1, 11400000)
    DisableCharacter(1400800)
    DisableAI(1400800)
    IfFlagEnabled(1, 11405393)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(11, 11400000)
    DeleteVFX(vfx_id=1401991, erase_root_only=False)
    DeleteVFX(vfx_id=1401993, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140000, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    CreateVFX(vfx_id=1401991)
    CreateVFX(vfx_id=1401993)
    EnableCharacter(1400800)
    EnableFlag(11400000)
    EnableAI(1400800)
    EnableBossHealthBar(1400800, name=5280, slot=0)


@NeverRestart(11400001)
def Event_11400001():
    """Event 11400001"""
    IfCharacterDead(0, 1400800)
    EnableFlag(9)
    KillBoss(game_area_param_id=1400800)
    DisableObject(1401990)
    DeleteVFX(vfx_id=1401991)
    DisableObject(1401992)
    DeleteVFX(vfx_id=1401993)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(1400800)


@NeverRestart(11405394)
def Event_11405394():
    """Event 11405394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 9)
    IfFlagEnabled(1, 11405392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11405391)
    IfCharacterInsideRegion(1, PLAYER, region=1402990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1403800)


@NeverRestart(11405395)
def Event_11405395():
    """Event 11405395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 9)
    IfFlagEnabled(1, 11405394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1403800)


@UnknownRestart(11405396)
def Event_11405396():
    """Event 11405396"""
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5281, part_index=NPCPartType.Part2, part_health=300)
    SetNPCPartEffects(1400800, npc_part_id=5281, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthComparison(2, 1400800, npc_part_id=5281, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(3, 1400800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ForceAnimation(1400800, 3011, wait_for_completion=True)
    Restart()


@UnknownRestart(11405397)
def Event_11405397():
    """Event 11405397"""
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5280, part_index=NPCPartType.Part1, part_health=1)
    SetNPCPartEffects(1400800, npc_part_id=5280, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthComparison(2, 1400800, npc_part_id=5280, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(3, 1400800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ForceAnimation(1400800, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest(11400800)
def Event_11400800():
    """Event 11400800"""
    SkipLinesIfThisEventFlagDisabled(5)
    DisableCharacter(1400700)
    DisableSoundEvent(sound_id=1403801)
    DisableMapCollision(collision=1403100)
    DisableMapCollision(collision=1403101)
    End()
    IfCharacterDead(0, 1400700)
    EnableFlag(140)
    DisableSoundEvent(sound_id=1403801)
    DisableMapCollision(collision=1403100)
    DisableMapCollision(collision=1403101)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    EndIfConditionFalse(1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


@NeverRestart(11405000)
def Event_11405000():
    """Event 11405000"""
    SkipLinesIfThisEventFlagDisabled(2)
    AddSpecialEffect(1400700, 5401)
    End()
    IfHealthNotEqual(0, 1400700, value=1.0)
    AddSpecialEffect(1400700, 5401)


@RestartOnRest(11400900)
def Event_11400900():
    """Event 11400900"""
    SkipLinesIfFlagDisabled(2, 11400902)
    DisableCharacter(1400000)
    End()
    IfCharacterAlive(1, 1400000)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    IfHealthLessThanOrEqual(0, 1400000, value=0.0)
    EnableNetworkSync()
    EzstateAIRequest(1400000, command_id=1200, slot=0)
    Restart()


@NeverRestart(11405100)
def Event_11405100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11405100"""
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@NeverRestart(11405110)
def Event_11405110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11405110"""
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_16_19)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@RestartOnRest(11405250)
def Event_11405250(_, arg_0_3: int):
    """Event 11405250"""
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2811,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(arg_0_3, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(arg_0_3, npc_part_id=2811, material_sfx_id=1, material_vfx_id=1)
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2811, desired_health=0, overwrite_max=False)


@RestartOnRest(11405300)
def Event_11405300():
    """Event 11405300"""
    Event_11405301(0, 1400500, 1, 3290, 3290, 11405301)
    Event_11405310(0, 1400500, 11405301, 0, 1)
    Event_11405310(1, 1400500, 11405301, 2, 3)
    Event_11405320(0, 1400500, 11405301, 1401500, 1401501, 120, 123)
    Event_11405320(1, 1400500, 11405301, 1401502, 1401503, 126, 129)
    Event_11405330(0, 1400500, 11405301, 1400600, 1400601, 120, 123)
    Event_11405330(1, 1400500, 11405301, 1400602, 1400603, 126, 129)
    Event_11405301(1, 1400500, 2, 3291, 3291, 11405302)
    Event_11405310(2, 1400500, 11405302, 5, 11)
    Event_11405320(2, 1400500, 11405302, 1401504, 1401505, 135, 137)
    Event_11405330(2, 1400500, 11405302, 1400604, 1400605, 135, 137)
    Event_11405330(3, 1400500, 11405302, 1400606, 1400607, 153, 155)
    Event_11405301(2, 1400500, 3, 3292, 3292, 11405303)
    Event_11405310(3, 1400500, 11405303, 6, 7)
    Event_11405310(4, 1400500, 11405303, 8, 10)
    Event_11405320(3, 1400500, 11405303, 1401506, 1401507, 138, 141)
    Event_11405320(4, 1400500, 11405303, 1401508, 1401509, 144, 150)
    Event_11405330(4, 1400500, 11405303, 1400608, 1400609, 138, 141)
    Event_11405330(5, 1400500, 11405303, 1400610, 1400611, 144, 150)
    Event_11405301(3, 1400500, 4, 3293, 3293, 11405304)
    Event_11405310(5, 1400500, 11405304, 4, 9)
    Event_11405320(5, 1400500, 11405304, 1401510, 1401511, 132, 134)
    Event_11405330(6, 1400500, 11405304, 1400612, 1400613, 132, 134)
    Event_11405330(7, 1400500, 11405304, 1400614, 1400615, 150, 152)


@UnknownRestart(11405301)
def Event_11405301(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """Event 11405301"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(arg_0_3, npc_part_id=arg_6_7, part_index=arg_4_5, part_health=100)
    IfCharacterPartHealthComparison(1, arg_0_3, npc_part_id=arg_8_11, comparison_type=ComparisonType.Equal, value=5)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11405290, 11405291))
    IfFlagEnabled(3, 11405290)
    IfFlagEnabled(4, 11405291)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, condition=4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(arg_12_15)
    SkipLinesIfFlagDisabled(1, 11405301)
    ForceAnimation(arg_0_3, 8000)
    SkipLinesIfFlagDisabled(1, 11405302)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart(11405310)
def Event_11405310(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """Event 11405310"""
    SkipLinesIfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart(11405320)
def Event_11405320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """Event 11405320"""
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagEnabled(arg_4_7)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11)
    DestroyObject(arg_12_15)


@UnknownRestart(11405330)
def Event_11405330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11405330"""
    EndIfFlagEnabled(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(arg_0_3)
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_16_19,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=arg_20_23,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)


@RestartOnRest(11405350)
def Event_11405350(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11405350"""
    SkipLinesIfEqual(1, left=arg_24_27, right=0)
    SkipLinesIfFlagEnabled(1, 11400533)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    End()
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    IfCharacterDead(0, arg_0_3)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_12_15,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_16_19,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=arg_0_3,
    )
    Move(
        arg_20_23,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    EnableCharacter(arg_16_19)
    EnableCharacter(arg_20_23)
    ForceAnimation(arg_4_7, 7000)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    ForceAnimation(arg_16_19, 7000)
    ForceAnimation(arg_20_23, 7000)


@NeverRestart(11400100)
def Event_11400100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11400100"""
    SkipLinesIfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableFlag(arg_0_3)
    DisableSpawner(entity=arg_8_11)
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    DisableFlag(arg_0_3)
    EnableSpawner(entity=arg_8_11)
    Restart()


@RestartOnRest(11400850)
def Event_11400850(_, arg_0_3: int, arg_4_7: int):
    """Event 11400850"""
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


@NeverRestart(11400600)
def Event_11400600(_, arg_0_3: int, arg_4_7: int):
    """Event 11400600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11400200)
def Event_11400200():
    """Event 11400200"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObjectActivation(1401110, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11400201)
    IfHealthGreaterThan(0, PLAYER, value=0.0)
    DisableBackread(1400800)
    DisableBackread(1400700)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(2, 11010700)
    PlayCutscene(140010, cutscene_flags=0, player_id=10000)
    SkipLines(2)
    PlayCutscene(140015, cutscene_flags=0, player_id=10000)
    EnableFlag(11500200)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, 9)
    EnableBackread(1400800)
    EnableBackread(1400700)
    EnableFlag(11400200)
    AwardAchievement(achievement_id=30)
    AwardItemLot(9030, host_only=True)


@NeverRestart(11400210)
def Event_11400210():
    """Event 11400210"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1401200)
    End()
    IfObjectDestroyed(0, 1401200)
    EnableFlag(11400210)


@NeverRestart(11400220)
def Event_11400220():
    """Event 11400220"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1402400)
    AddSpecialEffect(PLAYER, 4140)
    Restart()


@NeverRestart(11400230)
def Event_11400230():
    """Event 11400230"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(2, 590)
    EndOfAnimation(obj=1001200, animation_id=1)
    End()
    IfSingleplayer(1)
    IfFlagDisabled(1, 590)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010161, anchor_entity=1001200)
    Restart()


@RestartOnRest(11405200)
def Event_11405200(_, arg_0_3: int, arg_4_7: int):
    """Event 11405200"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    RestoreObject(arg_4_7)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfObjectDestroyed(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)


@NeverRestart(11400510)
def Event_11400510(_, arg_0_3: int, arg_4_7: int):
    """Event 11400510"""
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
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400520)
def Event_11400520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11400501)
def Event_11400501(_, arg_0_3: int, arg_4_7: int):
    """Event 11400501"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1284)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1272)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400502)
def Event_11400502(_, arg_0_3: int, arg_4_7: int):
    """Event 11400502"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(-2, 1280)
    IfFlagEnabled(-2, 1281)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400503)
def Event_11400503(_, arg_0_3: int, arg_4_7: int):
    """Event 11400503"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1286)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400504)
def Event_11400504(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11400504"""
    IfFlagDisabled(1, 1603)
    IfFlagEnabled(1, 1601)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfThisEventFlagDisabled(1)
    IfFlagDisabled(2, 1763)
    IfFlagEnabled(2, 1760)
    IfHealthLessThanOrEqual(2, arg_8_11, value=0.8999999761581421)
    IfHealthGreaterThan(2, arg_8_11, value=0.0)
    IfAttacked(2, attacked_entity=arg_8_11, attacker=PLAYER)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(-2, arg_4_7)
    IfFlagEnabled(-2, 1763)
    IfFlagEnabled(-2, 745)
    IfConditionTrue(3, input_condition=-2)
    IfThisEventFlagDisabled(3)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventFlagEnabled(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=4)
    SkipLinesIfFlagEnabled(1, 1604)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagEnabled(1, 1764)
    EnableFlag(1763)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.Enemy)
    EnableCharacter(arg_8_11)
    SetTeamTypeAndExitStandbyAnimation(arg_8_11, team_type=TeamType.Enemy)
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(7, input_condition=-7)
    IfPlayerCovenant(7, Covenant.ForestHunter)
    EndIfConditionFalse(7)
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


@NeverRestart(11400530)
def Event_11400530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400530"""
    IfFlagDisabled(1, 1253)
    IfFlagEnabled(1, 1256)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)


@NeverRestart(11400531)
def Event_11400531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400531"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1280)
    IfFlagEnabled(1, 11400593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11405001)
    SetNest(arg_0_3, region=1402301)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.FightingAlly)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(2, arg_0_3, region=1402300)
    IfAttacked(3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11405001)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.Ally)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@NeverRestart(11400532)
def Event_11400532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400532"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1281)
    IfFlagEnabled(1, 753)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@RestartOnRest(11400533)
def Event_11400533():
    """Event 11400533"""
    SkipLinesIfThisEventFlagDisabled(6)
    DisableCharacter(1400411)
    DisableCharacter(1400412)
    DisableCharacter(1400413)
    DisableCharacter(1400414)
    DisableCharacter(1400415)
    End()
    IfCharacterDead(0, 6160)
    End()


@NeverRestart(11400536)
def Event_11400536(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400536"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1290)
    IfPlayerHasWeapon(-1, 1331000)
    IfPlayerHasWeapon(-1, 1331100)
    IfPlayerHasWeapon(-1, 1331200)
    IfPlayerHasWeapon(-1, 1331300)
    IfPlayerHasWeapon(-1, 1331400)
    IfPlayerHasWeapon(-1, 1331500)
    IfPlayerHasWeapon(-1, 1332000)
    IfPlayerHasWeapon(-1, 1332100)
    IfPlayerHasWeapon(-1, 1332200)
    IfPlayerHasWeapon(-1, 1332300)
    IfPlayerHasWeapon(-1, 1332400)
    IfPlayerHasWeapon(-1, 1332500)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11400537)
def Event_11400537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400537"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1293)
    IfFlagEnabled(1, 11400595)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11400538)
def Event_11400538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400538"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1291)
    IfFlagEnabled(1, 10)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11400539)
def Event_11400539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400539"""
    IfFlagEnabled(1, 1290)
    IfFlagEnabled(1, 10)
    IfFlagDisabled(2, 1294)
    IfFlagEnabled(2, 1291)
    IfFlagDisabled(2, 71400061)
    IfFlagEnabled(2, 10)
    IfFlagDisabled(3, 1294)
    IfFlagEnabled(3, 1292)
    IfCharacterBackreadDisabled(3, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11400551)
def Event_11400551(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400551"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1497)
    IfFlagEnabled(1, 11020592)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


@NeverRestart(11400552)
def Event_11400552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11400552"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1501)
    IfFlagEnabled(1, 11400590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11400553)
def Event_11400553():
    """Event 11400553"""
    EndIfClient()
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 11400590)
    End()


@NeverRestart(11400554)
def Event_11400554(_, arg_0_3: int):
    """Event 11400554"""
    SkipLinesIfThisEventFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventFlagEnabled(-1)
    IfFlagEnabled(-1, 1501)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventFlagEnabled(1)
    IfFlagDisabled(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


@NeverRestart(11400560)
def Event_11400560(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11400560"""
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagDisabled(1, 1603)
    IfFlagEnabled(1, 1600)
    IfFlagEnabled(1, 11400582)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableCharacter(arg_16_19)
    DisableFlag(1766)
    EnableFlag(11405022)


@NeverRestart(11400566)
def Event_11400566(_, arg_0_3: int, arg_4_7: int):
    """Event 11400566"""
    SkipLinesIfHost(1)
    EndIfFlagEnabled(11405022)
    IfFlagEnabled(1, 746)
    EndIfConditionFalse(1)
    WaitFrames(frames=1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    EnableFlag(1766)
    DisableFlag(11405022)


@NeverRestart(11400567)
def Event_11400567(_, arg_0_3: int, arg_4_7: int):
    """Event 11400567"""
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfFlagDisabled(1, 746)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableFlag(11405022)


@NeverRestart(140)
def Event_140():
    """Event 140"""
    DisableNetworkSync()
    IfThisEventFlagEnabled(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=1401960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        text=10010184,
        anchor_entity=1401960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@NeverRestart(11405030)
def Event_11405030():
    """Event 11405030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6531, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11405033)
    IfClient(2)
    IfFlagEnabled(2, 11405031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6531)
    EndIfFlagEnabled(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 11400901)
    IfCharacterBackreadEnabled(1, 6531)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6531,
        region=1402050,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


@NeverRestart(11405032)
def Event_11405032():
    """Event 11405032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11405031)
    IfFlagEnabled(1, 11405393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6531, command_id=10, slot=0)
    ReplanAI(6531)
    IfCharacterInsideRegion(0, 6531, region=1402998)
    RotateToFaceEntity(6531, target_entity=1402997)
    ForceAnimation(6531, 7410)
    AICommand(6531, command_id=-1, slot=0)
    ReplanAI(6531)


@NeverRestart(11405035)
def Event_11405035():
    """Event 11405035"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11405036)
    EndIfFlagEnabled(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11400901)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1402061)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6530,
        region=1402060,
        summon_flag=11405036,
        dismissal_flag=11405037,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11400901)
def Event_11400901():
    """Event 11400901"""
    SkipLinesIfHost(3)
    IfFlagEnabled(1, 11405036)
    IfFlagDisabled(1, 11405037)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6530)
    EndIfThisEventFlagEnabled()
    IfCharacterDead(0, 6530)
    EnableFlag(11400901)
