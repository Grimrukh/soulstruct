"""
linked:


strings:

"""
from soulstruct.emevd.darksouls1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11400992, obj=1401960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RegisterBonfire(11400984, obj=1401961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11400976, obj=1401962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
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
    DeleteFX(1401995, erase_root_only=False)
    DisableObject(1401996)
    DeleteFX(1401997, erase_root_only=False)
    DisableObject(1401998)
    DeleteFX(1401999, erase_root_only=False)
    IfFlagOn(1, 11000810)
    IfFlagOn(1, 11410810)
    IfFlagOn(1, 11410811)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(1401601)
    SkipLines(1)
    EnableTreasure(1401601)
    RunEvent(11400090, slot=1, args=(1401702, 1401703, 1402602, 1402603))
    RunEvent(11405090)
    RunEvent(11405091)
    RunEvent(11405092)
    RunEvent(11400900)
    RunEvent(11400800)
    RunEvent(11405000)
    RunEvent(11400200)
    RunEvent(11400210)
    RunEvent(11400220)
    RunEvent(11400230)
    RunEvent(140)
    DisableMapSound(1403800)
    SkipLinesIfFlagOff(6, 9)
    RunEvent(11405392)
    DisableObject(1401990)
    DeleteFX(1401991, erase_root_only=False)
    DisableObject(1401992)
    DeleteFX(1401993, erase_root_only=False)
    SkipLines(7)
    RunEvent(11405390)
    RunEvent(11405391)
    RunEvent(11405393)
    RunEvent(11405392)
    RunEvent(11400001)
    RunEvent(11405394)
    RunEvent(11405395)
    RunEvent(11405100, slot=0, args=(1401000, 1402000, 1402001, 1402002))
    RunEvent(11405110, slot=0, args=(1401002, 1402020, 1402021, 1402022, 1402023, 1402024))
    RunEvent(11405350, slot=0, args=(6160, 1400411, 1400412, 1400413, 1400414, 1400415, 1))
    RunEvent(11405350, slot=3, args=(1400402, 1400426, 1400427, 1400428, 1400429, 1400430, 0))
    RunEvent(11405350, slot=4, args=(1400403, 1400431, 1400432, 1400433, 1400434, 1400435, 0))
    RunEvent(11400100, slot=0, args=(11405340, 1402200, 1403000))
    RunEvent(11400100, slot=1, args=(11405341, 1402201, 1403001))
    RunEvent(11400100, slot=2, args=(11405342, 1402202, 1403002))
    RunEvent(11405200, slot=0, args=(1400450, 1401300))
    RunEvent(11405250, slot=0, args=(1400100,))
    RunEvent(11405250, slot=1, args=(1400101,))
    RunEvent(11405250, slot=2, args=(1400102,))
    RunEvent(11405250, slot=3, args=(1400103,))
    RunEvent(11405250, slot=4, args=(1400104,))
    RunEvent(11400850, slot=0, args=(1400200, 25300200))
    RunEvent(11400850, slot=1, args=(1400201, 25300200))
    RunEvent(11400850, slot=2, args=(1400202, 25300200))
    RunEvent(11400850, slot=3, args=(1400203, 25300200))
    RunEvent(11400850, slot=4, args=(1400204, 25300200))
    RunEvent(11400850, slot=5, args=(1400205, 25300200))
    RunEvent(11400850, slot=6, args=(1400206, 25300200))
    RunEvent(11400850, slot=7, args=(1400207, 25300200))
    RunEvent(11400850, slot=8, args=(1400208, 25300200))
    RunEvent(11400600, slot=0, args=(1401650, 11400600))
    RunEvent(11400600, slot=1, args=(1401651, 11400601))
    RunEvent(11400600, slot=2, args=(1401652, 11400602))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6531, 8940)
    HumanityRegistration(6530, 8940)
    RunEvent(11405030)
    RunEvent(11405032)
    RunEvent(11405035)
    RunEvent(11400901)
    SkipLinesIfFlagOn(1, 1257)
    DisableCharacter(6132)
    SetTeamTypeAndExitStandbyAnimation(6132, TeamType.HostileAlly)
    RunEvent(11400520, slot=0, args=(6132, 1250, 1259, 1254))
    RunEvent(11400530, slot=0, args=(6132, 1250, 1259, 1257))
    SkipLinesIfFlagRangeAnyOn(1, (1270, 1279))
    EnableFlag(1270)
    RunEvent(11400520, slot=1, args=(1400700, 1270, 1279, 1272))
    SkipLinesIfFlagOn(2, 1280)
    SetNest(6160, 1402300)
    Move(6160, destination=1402300, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    RunEvent(11400520, slot=2, args=(6160, 1280, 1289, 1284))
    RunEvent(11400531, slot=0, args=(6160, 1280, 1289, 1281))
    RunEvent(11400532, slot=0, args=(6160, 1280, 1289, 1286))
    RunEvent(11400501, slot=0, args=(6160, 1282))
    RunEvent(11400502, slot=0, args=(6160, 1283))
    RunEvent(11400503, slot=0, args=(6160, 1287))
    RunEvent(11400533)
    HumanityRegistration(6170, 8398)
    SkipLinesIfFlagOn(2, 1296)
    SkipLinesIfFlagOn(1, 1290)
    SkipLines(1)
    DisableCharacter(6170)
    RunEvent(11400510, slot=3, args=(6170, 1294))
    RunEvent(11400520, slot=3, args=(6170, 1290, 1309, 1295))
    RunEvent(11400536, slot=0, args=(6170, 1290, 1309, 1291))
    RunEvent(11400537, slot=0, args=(6170, 1290, 1309, 1292))
    RunEvent(11400538, slot=0, args=(6170, 1290, 1309, 1293))
    RunEvent(11400539, slot=0, args=(6170, 1290, 1309, 1296))
    HumanityRegistration(6282, 8446)
    SkipLinesIfFlagOn(3, 1512)
    SkipLinesIfFlagOn(2, 1502)
    SkipLinesIfFlagOn(1, 1501)
    DisableCharacter(6282)
    RunEvent(11400510, slot=4, args=(6282, 1512))
    RunEvent(11400520, slot=4, args=(6282, 1490, 1514, 1513))
    RunEvent(11400551, slot=0, args=(6282, 1490, 1514, 1501))
    RunEvent(11400552, slot=0, args=(6282, 1490, 1514, 1502))
    RunEvent(11400553)
    RunEvent(11400554, slot=0, args=(6282,))
    HumanityRegistration(6311, 8470)
    HumanityRegistration(6421, 8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagOn(8, 11405022)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagOn(1, 1601)
    SkipLinesIfConditionTrue(2, 1)
    DisableCharacter(6311)
    DisableCharacter(6421)
    RunEvent(11400520, slot=5, args=(6311, 1600, 1619, 1604))
    RunEvent(11400520, slot=6, args=(6421, 1760, 1769, 1764))
    RunEvent(11400504, slot=0, args=(6311, 1603, 6421))
    RunEvent(11400560, slot=0, args=(6311, 1600, 1619, 1601, 6421))
    RunEvent(11400566, slot=0, args=(6311, 6421))
    RunEvent(11400567, slot=0, args=(6311, 6421))
    SkipLinesIfConditionFalse(2, 1)
    WaitFrames(1)
    EnableFlag(11405022)
    DisableFlag(1766)


@NeverRestart
def Event11400090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400090: Event 11400090 """
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
def Event11405090():
    """ 11405090: Event 11405090 """
    EndIfThisEventOn()
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
    IfFlagOn(0, 11400080)
    EndIfFlagOn(735)
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


@RestartOnRest
def Event11405091():
    """ 11405091: Event 11405091 """
    IfFlagOn(-1, 11405095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11400080)
    DisableFlag(11405095)
    EnableFlag(5001)
    Kill(1400900, award_souls=False)
    Kill(1400901, award_souls=False)
    Kill(1400902, award_souls=False)
    Kill(1400903, award_souls=False)
    Kill(1400904, award_souls=False)
    Kill(1400905, award_souls=False)
    Kill(1400906, award_souls=False)
    Kill(1400907, award_souls=False)
    Kill(1400908, award_souls=False)
    Kill(1400909, award_souls=False)


@RestartOnRest
def Event11405092():
    """ 11405092: Event 11405092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11400080)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=BLIGHTTOWN)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11400080)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=BLIGHTTOWN)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11400080)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=BLIGHTTOWN)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11400080)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=BLIGHTTOWN)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11400080)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=BLIGHTTOWN)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11400080)
    RestartIfConditionFalse(-6)
    EnableFlag(11400080)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=BLIGHTTOWN)
    RestartIfConditionFalse(7)
    DisableFlag(11400080)
    EnableFlag(11405095)


@NeverRestart
def Event11405390():
    """ 11405390: Event 11405390 """
    IfFlagOff(1, 9)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1402998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1401990, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11405391():
    """ 11405391: Event 11405391 """
    IfFlagOff(1, 9)
    IfFlagOn(1, 11405393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1402998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1401990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11405393():
    """ 11405393: Event 11405393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 9)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1400800)


@RestartOnRest
def Event11405392():
    """ 11405392: Event 11405392 """
    SkipLinesIfFlagOff(3, 9)
    DisableBackread(1400800)
    Kill(1400800, award_souls=False)
    End()
    RunEvent(11405396)
    RunEvent(11405397)
    SkipLinesIfFlagOn(1, 11400000)
    DisableCharacter(1400800)
    DisableAI(1400800)
    IfFlagOn(1, 11405393)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(11, 11400000)
    DeleteFX(1401991, erase_root_only=False)
    DeleteFX(1401993, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(140000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    CreateFX(1401991)
    CreateFX(1401993)
    EnableCharacter(1400800)
    EnableFlag(11400000)
    EnableAI(1400800)
    EnableBossHealthBar(1400800, name=5280, slot=0)


@NeverRestart
def Event11400001():
    """ 11400001: Event 11400001 """
    IfCharacterDead(0, 1400800)
    EnableFlag(9)
    KillBoss(1400800)
    DisableObject(1401990)
    DeleteFX(1401991, erase_root_only=True)
    DisableObject(1401992)
    DeleteFX(1401993, erase_root_only=True)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(1400800)


@NeverRestart
def Event11405394():
    """ 11405394: Event 11405394 """
    DisableNetworkSync()
    IfFlagOff(1, 9)
    IfFlagOn(1, 11405392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11405391)
    IfCharacterInsideRegion(1, PLAYER, region=1402990)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1403800)


@NeverRestart
def Event11405395():
    """ 11405395: Event 11405395 """
    DisableNetworkSync()
    IfFlagOn(1, 9)
    IfFlagOn(1, 11405394)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1403800)


@UnknownRestart
def Event11405396():
    """ 11405396: Event 11405396 """
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5281, part_index=NPCPartType.Part2, part_health=300, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(1400800, npc_part_id=5281, material_special_effect_id=75, material_fx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, 1400800, npc_part_id=5281, value=0)
    IfHealthLessThanOrEqual(3, 1400800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    ForceAnimation(1400800, 3011, wait_for_completion=True)
    Restart()


@UnknownRestart
def Event11405397():
    """ 11405397: Event 11405397 """
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5280, part_index=NPCPartType.Part1, part_health=1, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(1400800, npc_part_id=5280, material_special_effect_id=60, material_fx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, 1400800, npc_part_id=5280, value=0)
    IfHealthLessThanOrEqual(3, 1400800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    ForceAnimation(1400800, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event11400800():
    """ 11400800: Event 11400800 """
    SkipLinesIfThisEventOff(5)
    DisableCharacter(1400700)
    DisableMapSound(1403801)
    DisableHitbox(1403100)
    DisableHitbox(1403101)
    End()
    IfCharacterDead(0, 1400700)
    EnableFlag(140)
    DisableMapSound(1403801)
    DisableHitbox(1403100)
    DisableHitbox(1403101)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    EndIfConditionFalse(1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


@NeverRestart
def Event11405000():
    """ 11405000: Event 11405000 """
    SkipLinesIfThisEventOff(2)
    AddSpecialEffect(1400700, 5401)
    End()
    IfHealthNotEqual(0, 1400700, 1.0)
    AddSpecialEffect(1400700, 5401)


@RestartOnRest
def Event11400900():
    """ 11400900: Event 11400900 """
    SkipLinesIfFlagOff(2, 11400902)
    DisableCharacter(1400000)
    End()
    IfCharacterAlive(1, 1400000)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    IfHealthLessThanOrEqual(0, 1400000, 0.0)
    EnableNetworkSync()
    EzstateAIRequest(1400000, command_id=1200, slot=0)
    Restart()


@NeverRestart
def Event11405100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11405100: Event 11405100 """
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_12_15)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@NeverRestart
def Event11405110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 11405110: Event 11405110 """
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_12_15)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_16_19)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@RestartOnRest
def Event11405250(ARG_0_3: int):
    """ 11405250: Event 11405250 """
    IfCharacterDead(1, ARG_0_3)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    CreateNPCPart(ARG_0_3, npc_part_id=2811, part_index=NPCPartType.Part2, part_health=100, damage_correction=0.0, body_damage_correction=0.0, is_invincible=True, start_in_stop_state=False)
    SetNPCPartBulletDamageScaling(ARG_0_3, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(ARG_0_3, npc_part_id=2811, material_special_effect_id=1, material_fx_id=1)
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    SetNPCPartHealth(ARG_0_3, npc_part_id=2811, desired_hp=0, overwrite_max=False)


@RestartOnRest
def Event11405300():
    """ 11405300: Event 11405300 """
    RunEvent(11405301, slot=0, args=(1400500, 1, 3290, 3290, 11405301), arg_types='ihhii')
    RunEvent(11405310, slot=0, args=(1400500, 11405301, 0, 1), arg_types='iiBB')
    RunEvent(11405310, slot=1, args=(1400500, 11405301, 2, 3), arg_types='iiBB')
    RunEvent(11405320, slot=0, args=(1400500, 11405301, 1401500, 1401501, 120, 123), arg_types='iiiihh')
    RunEvent(11405320, slot=1, args=(1400500, 11405301, 1401502, 1401503, 126, 129), arg_types='iiiihh')
    RunEvent(11405330, slot=0, args=(1400500, 11405301, 1400600, 1400601, 120, 123))
    RunEvent(11405330, slot=1, args=(1400500, 11405301, 1400602, 1400603, 126, 129))
    RunEvent(11405301, slot=1, args=(1400500, 2, 3291, 3291, 11405302), arg_types='ihhii')
    RunEvent(11405310, slot=2, args=(1400500, 11405302, 5, 11), arg_types='iiBB')
    RunEvent(11405320, slot=2, args=(1400500, 11405302, 1401504, 1401505, 135, 137), arg_types='iiiihh')
    RunEvent(11405330, slot=2, args=(1400500, 11405302, 1400604, 1400605, 135, 137))
    RunEvent(11405330, slot=3, args=(1400500, 11405302, 1400606, 1400607, 153, 155))
    RunEvent(11405301, slot=2, args=(1400500, 3, 3292, 3292, 11405303), arg_types='ihhii')
    RunEvent(11405310, slot=3, args=(1400500, 11405303, 6, 7), arg_types='iiBB')
    RunEvent(11405310, slot=4, args=(1400500, 11405303, 8, 10), arg_types='iiBB')
    RunEvent(11405320, slot=3, args=(1400500, 11405303, 1401506, 1401507, 138, 141), arg_types='iiiihh')
    RunEvent(11405320, slot=4, args=(1400500, 11405303, 1401508, 1401509, 144, 150), arg_types='iiiihh')
    RunEvent(11405330, slot=4, args=(1400500, 11405303, 1400608, 1400609, 138, 141))
    RunEvent(11405330, slot=5, args=(1400500, 11405303, 1400610, 1400611, 144, 150))
    RunEvent(11405301, slot=3, args=(1400500, 4, 3293, 3293, 11405304), arg_types='ihhii')
    RunEvent(11405310, slot=5, args=(1400500, 11405304, 4, 9), arg_types='iiBB')
    RunEvent(11405320, slot=5, args=(1400500, 11405304, 1401510, 1401511, 132, 134), arg_types='iiiihh')
    RunEvent(11405330, slot=6, args=(1400500, 11405304, 1400612, 1400613, 132, 134))
    RunEvent(11405330, slot=7, args=(1400500, 11405304, 1400614, 1400615, 150, 152))


@UnknownRestart
def Event11405301(ARG_0_3: int, ARG_4_5: short, ARG_6_7: short, ARG_8_11: int, ARG_12_15: int):
    """ 11405301: Event 11405301 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, ARG_0_3)
    CreateNPCPart(ARG_0_3, npc_part_id=ARG_6_7, part_index=ARG_4_5, part_health=100, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, ARG_0_3, npc_part_id=ARG_8_11, value=0)
    IfCharacterDead(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11405290, 11405291))
    IfFlagOn(3, 11405290)
    IfFlagOn(4, 11405291)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(ARG_12_15)
    SkipLinesIfFlagOff(1, 11405301)
    ForceAnimation(ARG_0_3, 8000)
    SkipLinesIfFlagOff(1, 11405302)
    ForceAnimation(ARG_0_3, 8010)


@UnknownRestart
def Event11405310(ARG_0_3: int, ARG_4_7: int, ARG_8_8: uchar, ARG_9_9: uchar):
    """ 11405310: Event 11405310 """
    SkipLinesIfFlagOn(6, ARG_4_7)
    IfFlagOn(1, ARG_4_7)
    IfCharacterDead(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SetDisplayMask(ARG_0_3, bit_index=ARG_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(ARG_0_3, bit_index=ARG_9_9, switch_type=OnOffChange.On)


@UnknownRestart
def Event11405320(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_17: short, ARG_18_19: short):
    """ 11405320: Event 11405320 """
    DisableObject(ARG_8_11)
    DisableObject(ARG_12_15)
    EndIfFlagOn(ARG_4_7)
    IfFlagOn(1, ARG_4_7)
    IfCharacterDead(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableObject(ARG_8_11)
    EnableObject(ARG_12_15)
    MoveObjectToCharacter(ARG_8_11, character=ARG_0_3, model_point=ARG_16_17)
    MoveObjectToCharacter(ARG_12_15, character=ARG_0_3, model_point=ARG_18_19)
    DestroyObject(ARG_8_11, slot=1)
    DestroyObject(ARG_12_15, slot=1)


@UnknownRestart
def Event11405330(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 11405330: Event 11405330 """
    EndIfFlagOn(ARG_4_7)
    DisableCharacter(ARG_8_11)
    DisableCharacter(ARG_12_15)
    IfFlagOn(1, ARG_4_7)
    IfCharacterDead(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    Move(ARG_8_11, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=ARG_16_19, copy_draw_hitbox=ARG_0_3)
    Move(ARG_12_15, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=ARG_20_23, copy_draw_hitbox=ARG_0_3)
    EnableCharacter(ARG_8_11)
    EnableCharacter(ARG_12_15)
    ForceAnimation(ARG_8_11, 7000)
    ForceAnimation(ARG_12_15, 7000)


@RestartOnRest
def Event11405350(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 11405350: Event 11405350 """
    SkipLinesIfEqual(1, left=ARG_24_27, right=0)
    SkipLinesIfFlagOn(1, 11400533)
    SkipLinesIfThisEventSlotOff(2)
    SetDisplayMask(ARG_0_3, bit_index=2, switch_type=OnOffChange.On)
    End()
    DisableCharacter(ARG_4_7)
    DisableCharacter(ARG_8_11)
    DisableCharacter(ARG_12_15)
    DisableCharacter(ARG_16_19)
    DisableCharacter(ARG_20_23)
    IfCharacterDead(0, ARG_0_3)
    SetDisplayMask(ARG_0_3, bit_index=2, switch_type=OnOffChange.On)
    Move(ARG_4_7, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=100, copy_draw_hitbox=ARG_0_3)
    Move(ARG_8_11, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=101, copy_draw_hitbox=ARG_0_3)
    Move(ARG_12_15, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=102, copy_draw_hitbox=ARG_0_3)
    Move(ARG_16_19, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=103, copy_draw_hitbox=ARG_0_3)
    Move(ARG_20_23, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=104, copy_draw_hitbox=ARG_0_3)
    EnableCharacter(ARG_4_7)
    EnableCharacter(ARG_8_11)
    EnableCharacter(ARG_12_15)
    EnableCharacter(ARG_16_19)
    EnableCharacter(ARG_20_23)
    ForceAnimation(ARG_4_7, 7000)
    ForceAnimation(ARG_8_11, 7000)
    ForceAnimation(ARG_12_15, 7000)
    ForceAnimation(ARG_16_19, 7000)
    ForceAnimation(ARG_20_23, 7000)


@NeverRestart
def Event11400100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11400100: Event 11400100 """
    SkipLinesIfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    EnableFlag(ARG_0_3)
    DisableSpawner(ARG_8_11)
    IfAllPlayersOutsideRegion(0, region=ARG_4_7)
    DisableFlag(ARG_0_3)
    EnableSpawner(ARG_8_11)
    Restart()


@RestartOnRest
def Event11400850(ARG_0_3: int, ARG_4_7: int):
    """ 11400850: Event 11400850 """
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


@NeverRestart
def Event11400600(ARG_0_3: int, ARG_4_7: int):
    """ 11400600: Event 11400600 """
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
def Event11400200():
    """ 11400200: Event 11400200 """
    SkipLinesIfThisEventOff(2)
    DisableObjectActivation(1401110, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11400201)
    IfHealthGreaterThan(0, PLAYER, 0.0)
    DisableBackread(1400800)
    DisableBackread(1400700)
    WaitFrames(1)
    SkipLinesIfFlagOn(2, 11010700)
    PlayCutscene(140010, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(2)
    PlayCutscene(140015, skippable=True, fade_out=False, player_id=PLAYER)
    EnableFlag(11500200)
    WaitFrames(1)
    SkipLinesIfFlagOn(1, 9)
    EnableBackread(1400800)
    EnableBackread(1400700)
    EnableFlag(11400200)
    AwardAchievement(30)
    AwardItemLot(9030, host_only=True)


@NeverRestart
def Event11400210():
    """ 11400210: Event 11400210 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1401200)
    End()
    IfObjectDestroyed(0, 1401200)
    EnableFlag(11400210)


@NeverRestart
def Event11400220():
    """ 11400220: Event 11400220 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1402400)
    AddSpecialEffect(PLAYER, 4140)
    Restart()


@NeverRestart
def Event11400230():
    """ 11400230: Event 11400230 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(2, 590)
    EndOfAnimation(1001200, 1)
    End()
    IfSingleplayer(1)
    IfFlagOff(1, 590)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1001200, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=101, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entity=1001200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@RestartOnRest
def Event11405200(ARG_0_3: int, ARG_4_7: int):
    """ 11405200: Event 11405200 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    RestoreObject(ARG_4_7)
    DisableCollision(ARG_0_3)
    DisableGravity(ARG_0_3)
    Move(ARG_0_3, destination=ARG_4_7, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfObjectDestroyed(-1, ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(ARG_0_3)
    EnableCollision(ARG_0_3)
    EnableGravity(ARG_0_3)


@NeverRestart
def Event11400510(ARG_0_3: int, ARG_4_7: int):
    """ 11400510: Event 11400510 """
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
def Event11400520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400520: Event 11400520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11400501(ARG_0_3: int, ARG_4_7: int):
    """ 11400501: Event 11400501 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1284)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1272)
    IfThisEventOff(1)
    IfFlagOn(2, ARG_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_4_7)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11400502(ARG_0_3: int, ARG_4_7: int):
    """ 11400502: Event 11400502 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(-2, 1280)
    IfFlagOn(-2, 1281)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfFlagOn(2, ARG_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_4_7)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11400503(ARG_0_3: int, ARG_4_7: int):
    """ 11400503: Event 11400503 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1286)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfFlagOn(2, ARG_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_4_7)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11400504(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11400504: Event 11400504 """
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1601)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfThisEventOff(1)
    IfFlagOff(2, 1763)
    IfFlagOn(2, 1760)
    IfHealthLessThanOrEqual(2, ARG_8_11, 0.8999999761581421)
    IfHealthGreaterThan(2, ARG_8_11, 0.0)
    IfAttacked(2, ARG_8_11, attacking_character=10000)
    IfThisEventOff(2)
    IfFlagOn(-2, ARG_4_7)
    IfFlagOn(-2, 1763)
    IfFlagOn(-2, 745)
    IfConditionTrue(3, input_condition=-2)
    IfThisEventOff(3)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFlagOn(1, 1604)
    EnableFlag(ARG_4_7)
    SkipLinesIfFlagOn(1, 1764)
    EnableFlag(1763)
    EnableCharacter(ARG_0_3)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.Enemy)
    EnableCharacter(ARG_8_11)
    SetTeamTypeAndExitStandbyAnimation(ARG_8_11, TeamType.Enemy)
    EndIfThisEventOn()
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(7, input_condition=-7)
    IfPlayerCovenant(7, Covenant.ForestHunter)
    EndIfConditionFalse(7)
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


@NeverRestart
def Event11400530(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400530: Event 11400530 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1256)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)


@NeverRestart
def Event11400531(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400531: Event 11400531 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1280)
    IfFlagOn(1, 11400593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableFlag(11405001)
    SetNest(ARG_0_3, 1402301)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.FightingAlly)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(2, ARG_0_3, region=1402300)
    IfAttacked(3, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11405001)
    SkipLinesIfFinishedConditionTrue(1, 3)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.Ally)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@NeverRestart
def Event11400532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400532: Event 11400532 """
    IfFlagOff(1, 1282)
    IfFlagOff(1, 1283)
    IfFlagOff(1, 1287)
    IfFlagOn(1, 1281)
    IfFlagOn(1, 753)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@RestartOnRest
def Event11400533():
    """ 11400533: Event 11400533 """
    SkipLinesIfThisEventOff(6)
    DisableCharacter(1400411)
    DisableCharacter(1400412)
    DisableCharacter(1400413)
    DisableCharacter(1400414)
    DisableCharacter(1400415)
    End()
    IfCharacterDead(0, 6160)
    End()


@NeverRestart
def Event11400536(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400536: Event 11400536 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1290)
    IfPlayerHasWeapon(-1, 1331000, including_box=False)
    IfPlayerHasWeapon(-1, 1331100, including_box=False)
    IfPlayerHasWeapon(-1, 1331200, including_box=False)
    IfPlayerHasWeapon(-1, 1331300, including_box=False)
    IfPlayerHasWeapon(-1, 1331400, including_box=False)
    IfPlayerHasWeapon(-1, 1331500, including_box=False)
    IfPlayerHasWeapon(-1, 1332000, including_box=False)
    IfPlayerHasWeapon(-1, 1332100, including_box=False)
    IfPlayerHasWeapon(-1, 1332200, including_box=False)
    IfPlayerHasWeapon(-1, 1332300, including_box=False)
    IfPlayerHasWeapon(-1, 1332400, including_box=False)
    IfPlayerHasWeapon(-1, 1332500, including_box=False)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11400537(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400537: Event 11400537 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1293)
    IfFlagOn(1, 11400595)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11400538(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400538: Event 11400538 """
    IfFlagOff(1, 1294)
    IfFlagOn(1, 1291)
    IfFlagOn(1, 10)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11400539(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400539: Event 11400539 """
    IfFlagOn(1, 1290)
    IfFlagOn(1, 10)
    IfFlagOff(2, 1294)
    IfFlagOn(2, 1291)
    IfFlagOff(2, 71400061)
    IfFlagOn(2, 10)
    IfFlagOff(3, 1294)
    IfFlagOn(3, 1292)
    IfCharacterBackreadDisabled(3, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11400551(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400551: Event 11400551 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1497)
    IfFlagOn(1, 11020592)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)
    EnableFlag(814)


@NeverRestart
def Event11400552(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11400552: Event 11400552 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1501)
    IfFlagOn(1, 11400590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11400553():
    """ 11400553: Event 11400553 """
    EndIfClient()
    EndIfThisEventOn()
    IfFlagOn(0, 11400590)
    End()


@NeverRestart
def Event11400554(ARG_0_3: int):
    """ 11400554: Event 11400554 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    IfThisEventOn(-1)
    IfFlagOn(-1, 1501)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventOn(1)
    IfFlagOff(0, 814)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=7856)


@NeverRestart
def Event11400560(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11400560: Event 11400560 """
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1600)
    IfFlagOn(1, 11400582)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)
    EnableCharacter(ARG_16_19)
    DisableFlag(1766)
    EnableFlag(11405022)


@NeverRestart
def Event11400566(ARG_0_3: int, ARG_4_7: int):
    """ 11400566: Event 11400566 """
    SkipLinesIfHost(1)
    EndIfFlagOn(11405022)
    IfFlagOn(1, 746)
    EndIfConditionFalse(1)
    WaitFrames(1)
    DisableCharacter(ARG_0_3)
    DisableCharacter(ARG_4_7)
    EnableFlag(1766)
    DisableFlag(11405022)


@NeverRestart
def Event11400567(ARG_0_3: int, ARG_4_7: int):
    """ 11400567: Event 11400567 """
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfFlagOff(1, 746)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    DisableCharacter(ARG_0_3)
    DisableCharacter(ARG_4_7)
    DisableFlag(11405022)


@NeverRestart
def Event140():
    """ 140: Event 140 """
    DisableNetworkSync()
    IfThisEventOn(1)
    IfDialogPromptActivated(1, prompt_text=10010182, anchor_entity=1401960, anchor_type=CoordEntityType.Object, facing_angle=180.0, max_distance=3.4000000953674316, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010184, anchor_entity=1401960, display_distance=3.4000000953674316, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11405030():
    """ 11405030: Event 11405030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6531, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11405033)
    IfClient(2)
    IfFlagOn(2, 11405031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6531)
    EndIfFlagOn(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11400901)
    IfCharacterBackreadEnabled(1, 6531)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6531, region=1402050, summon_flag=11405031, dismissal_flag=11405033)


@NeverRestart
def Event11405032():
    """ 11405032: Event 11405032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11405031)
    IfFlagOn(1, 11405393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6531, command_id=10, slot=0)
    ReplanAI(6531)
    IfCharacterInsideRegion(0, 6531, region=1402998)
    RotateToFaceEntity(6531, 1402997)
    ForceAnimation(6531, 7410)
    AICommand(6531, command_id=-1, slot=0)
    ReplanAI(6531)


@NeverRestart
def Event11405035():
    """ 11405035: Event 11405035 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11405036)
    EndIfFlagOn(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11400901)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1402061)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6530, region=1402060, summon_flag=11405036, dismissal_flag=11405037)
    Wait(20.0)
    Restart()


@NeverRestart
def Event11400901():
    """ 11400901: Event 11400901 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11405036)
    IfFlagOff(1, 11405037)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6530)
    EndIfThisEventOn()
    IfCharacterDead(0, 6530)
    EnableFlag(11400901)
