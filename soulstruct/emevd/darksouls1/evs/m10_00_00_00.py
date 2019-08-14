"""
linked:


strings:

"""
from soulstruct.emevd.darksouls1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11000992, obj=1001960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=1001140)
    RegisterStatue(1001900, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001901, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001902, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001903, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001904, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001905, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001906, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001907, game_map=DEPTHS, statue_type=StatueType.Stone)
    SkipLinesIfClient(5)
    DisableFlag(11000000)
    DisableObject(1001994)
    DeleteFX(1001995, erase_root_only=False)
    DisableObject(1001996)
    DeleteFX(1001997, erase_root_only=False)
    SkipLinesIfFlagOff(1, 11000100)
    EndOfAnimation(1001319, 0)
    RunEvent(11000090, slot=0, args=(1001700, 1001701, 1002600, 1002601))
    RunEvent(11005080)
    RunEvent(11005081)
    RunEvent(11005082)
    RunEvent(11000100)
    RunEvent(11000101)
    RunEvent(11000120, slot=0, args=(11000120, 10010877, 1001315, 10010883, 2018))
    RunEvent(11000200)
    RunEvent(11000800)
    RunEvent(11005050)
    RunEvent(11005060)
    RunEvent(11005070)
    RunEvent(11000110)
    RunEvent(11000111)
    RunEvent(11000600, slot=0, args=(1001650, 11000600))
    DisableMapSound(1003800)
    SkipLinesIfFlagOff(4, 2)
    RunEvent(11005392)
    DisableObject(1001990)
    DeleteFX(1001991, erase_root_only=False)
    SkipLines(10)
    RunEvent(11005390)
    RunEvent(11005391)
    RunEvent(11005393)
    RunEvent(11005392)
    RunEvent(11000001)
    RunEvent(11005394)
    RunEvent(11005395)
    RunEvent(11005396)
    RunEvent(11005397)
    RunEvent(11005398)
    RunEvent(11005000, slot=0, args=(1001000, 1001000, 1))
    RunEvent(11005000, slot=1, args=(1001001, 1001001, 1))
    RunEvent(11005000, slot=2, args=(1001002, 1001002, 3))
    RunEvent(11005200, slot=0, args=(1000120, 1002020))
    RunEvent(11005200, slot=1, args=(1000121, 1002020))
    RunEvent(11005200, slot=2, args=(1000122, 1002020))
    RunEvent(11005200, slot=3, args=(1000123, 1002020))
    RunEvent(11005200, slot=4, args=(1000124, 1002020))
    RunEvent(11005200, slot=5, args=(1000125, 1002020))
    RunEvent(11005200, slot=6, args=(1000110, 1002021))
    RunEvent(11005200, slot=7, args=(1000111, 1002021))
    RunEvent(11005200, slot=8, args=(1000112, 1002022))
    RunEvent(11005200, slot=9, args=(1000113, 1002022))
    RunEvent(11005200, slot=10, args=(1000126, 1002022))
    RunEvent(11005100, slot=0, args=(1002100, 1000100, 0.0), arg_types='iif')
    RunEvent(11005100, slot=1, args=(1002101, 1000101, 0.0), arg_types='iif')
    RunEvent(11005100, slot=2, args=(1002102, 1000102, 0.0), arg_types='iif')
    RunEvent(11005100, slot=3, args=(1002102, 1000103, 0.6000000238418579), arg_types='iif')
    RunEvent(11005100, slot=4, args=(1002103, 1000104, 0.0), arg_types='iif')
    RunEvent(11005100, slot=5, args=(1002103, 1000105, 0.20000000298023224), arg_types='iif')
    RunEvent(11005100, slot=6, args=(1002103, 1000106, 0.8999999761581421), arg_types='iif')
    RunEvent(11005100, slot=7, args=(1002107, 1000107, 0.0), arg_types='iif')
    RunEvent(11005150, slot=0, args=(1000150, 1001100))
    RunEvent(11005150, slot=1, args=(1000151, 1001101))
    RunEvent(11005150, slot=2, args=(1000152, 1001102))
    RunEvent(11000850, slot=0, args=(1000110,))
    RunEvent(11000850, slot=1, args=(1000099,))
    RunEvent(11000850, slot=2, args=(1000090,))
    RunEvent(11000850, slot=3, args=(1000300,))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6541, 8310)
    HumanityRegistration(6591, 8462)
    HumanityRegistration(6562, 8956)
    RunEvent(11005030)
    RunEvent(11005031)
    RunEvent(11005033)
    RunEvent(11005034)
    RunEvent(11005039)
    RunEvent(11000810)
    HumanityRegistration(6130, 8390)
    SkipLinesIfClient(1)
    DisableFlag(11000580)
    SkipLinesIfFlagOn(3, 11000580)
    SkipLinesIfFlagOn(2, 1250)
    SkipLinesIfFlagOn(1, 1253)
    DisableCharacter(6130)
    SkipLinesIfFlagOff(2, 1250)
    DisableGravity(6130)
    DisableCollision(6130)
    RunEvent(11000530, slot=0, args=(6130, 1250, 1255, 1251))
    RunEvent(11000531, slot=0, args=(6130,))
    RunEvent(11000510, slot=0, args=(6130, 1253))
    RunEvent(11000520, slot=0, args=(6130, 1250, 1255, 1254))
    RunEvent(11000534, slot=0, args=(6130,))
    HumanityRegistration(6260, 8430)
    SkipLinesIfFlagOn(2, 1434)
    SkipLinesIfFlagOn(1, 1430)
    DisableCharacter(6260)
    RunEvent(11000532, slot=0, args=(6260, 1430, 1459, 1431))
    RunEvent(11000510, slot=1, args=(6260, 1434))
    RunEvent(11000533, slot=0, args=(6260, 1435))


@NeverRestart
def Event11000090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11000090: Event 11000090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=ARG_0_3)
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
def Event11005080():
    """ 11005080: Event 11005080 """
    EndIfThisEventOn()
    DisableCharacter(1000900)
    DisableCharacter(1000901)
    DisableCharacter(1000902)
    DisableCharacter(1000903)
    DisableCharacter(1000904)
    DisableCharacter(1000905)
    DisableCharacter(1000906)
    DisableCharacter(1000907)
    DisableCharacter(1000908)
    DisableCharacter(1000909)
    DisableCharacter(1000910)
    DisableCharacter(1000911)
    DisableCharacter(1000912)
    DisableCharacter(1000913)
    IfFlagOn(0, 11000050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1000900)
    EnableCharacter(1000901)
    EnableCharacter(1000902)
    EnableCharacter(1000903)
    EnableCharacter(1000904)
    EnableCharacter(1000905)
    EnableCharacter(1000906)
    EnableCharacter(1000907)
    EnableCharacter(1000908)
    EnableCharacter(1000909)
    EnableCharacter(1000910)
    EnableCharacter(1000911)
    EnableCharacter(1000912)
    EnableCharacter(1000913)


@RestartOnRest
def Event11005081():
    """ 11005081: Event 11005081 """
    IfFlagOn(-1, 11005085)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11000050)
    DisableFlag(11005085)
    EnableFlag(5001)
    Kill(1000900, award_souls=False)
    Kill(1000901, award_souls=False)
    Kill(1000902, award_souls=False)
    Kill(1000903, award_souls=False)
    Kill(1000904, award_souls=False)
    Kill(1000905, award_souls=False)
    Kill(1000906, award_souls=False)
    Kill(1000907, award_souls=False)
    Kill(1000908, award_souls=False)
    Kill(1000909, award_souls=False)
    Kill(1000910, award_souls=False)
    Kill(1000911, award_souls=False)
    Kill(1000912, award_souls=False)
    Kill(1000913, award_souls=False)


@RestartOnRest
def Event11005082():
    """ 11005082: Event 11005082 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DEPTHS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11000050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DEPTHS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11000050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DEPTHS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11000050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DEPTHS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11000050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DEPTHS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11000050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DEPTHS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11000050)
    RestartIfConditionFalse(-6)
    EnableFlag(11000050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DEPTHS)
    RestartIfConditionFalse(7)
    DisableFlag(11000050)
    EnableFlag(11005085)


@NeverRestart
def Event11005390():
    """ 11005390: Event 11005390 """
    IfFlagOff(1, 2)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1002998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1001990, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11005391():
    """ 11005391: Event 11005391 """
    DisableNetworkSync()
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1002998, anchor_type=CoordEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1001990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11005393():
    """ 11005393: Event 11005393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 2)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1000800)


@RestartOnRest
def Event11005392():
    """ 11005392: Event 11005392 """
    SkipLinesIfFlagOff(5, 2)
    DisableCharacter(1000800)
    DisableCharacter(1000801)
    Kill(1000800, award_souls=False)
    Kill(1000801, award_souls=False)
    End()
    SkipLinesIfFlagOn(1, 11000000)
    DisableCharacter(1000800)
    DisableAI(1000800)
    IfFlagOn(1, 11005393)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(7, 11000000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(100000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1000800)
    EnableFlag(11000000)
    EnableAI(1000800)
    EnableBossHealthBar(1000800, name=5260, slot=0)


@NeverRestart
def Event11000001():
    """ 11000001: Event 11000001 """
    IfCharacterDead(0, 1000800)
    EnableFlag(2)
    Kill(1000801, award_souls=False)
    KillBoss(1000800)
    DisableObject(1001990)
    DeleteFX(1001991, erase_root_only=True)


@NeverRestart
def Event11005394():
    """ 11005394: Event 11005394 """
    DisableNetworkSync()
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005392)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1003800)


@NeverRestart
def Event11005395():
    """ 11005395: Event 11005395 """
    DisableNetworkSync()
    IfFlagOn(1, 2)
    IfFlagOn(1, 11005394)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1003800)


@RestartOnRest
def Event11005396():
    """ 11005396: Event 11005396 """
    DisableCharacter(1000801)
    EndIfThisEventOn()
    IfFlagOn(0, 11005390)
    CreateNPCPart(1000800, npc_part_id=5260, part_index=NPCPartType.Part1, part_health=300, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0, 1000800, npc_part_id=5260, value=0)
    EzstateAIRequest(1000800, command_id=1001, slot=0)
    IfHasTAEEvent(0, 1000800, tae_event_id=400)
    EnableCharacter(1000801)
    Move(1000801, destination=1000800, destination_type=CoordEntityType.Character, model_point=100, copy_draw_hitbox=1000800)
    ForceAnimation(1000801, 8100)
    SetDisplayMask(1000800, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(1000800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1000800, command_id=20, slot=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52610000, host_only=True)


@RestartOnRest
def Event11005397():
    """ 11005397: Event 11005397 """
    IfFlagOn(1, 11005390)
    IfCharacterBackreadEnabled(1, 1000800)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(1000800, npc_part_id=5261, part_index=NPCPartType.Part2, part_health=100, damage_correction=0.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(1000800, npc_part_id=5261, material_special_effect_id=60, material_fx_id=60)


@RestartOnRest
def Event11005398():
    """ 11005398: Event 11005398 """
    IfFlagOn(0, 11005390)
    CreateNPCPart(1000800, npc_part_id=5262, part_index=NPCPartType.Part3, part_health=1, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0, 1000800, npc_part_id=5262, value=0)
    AICommand(1000800, command_id=1, slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    SkipLinesIfFlagOn(2, 11005396)
    AICommand(1000800, command_id=0, slot=0)
    SkipLines(1)
    AICommand(1000800, command_id=20, slot=0)
    Restart()


@NeverRestart
def Event11005000(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11005000: Event 11005000 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(ARG_4_7)
    End()
    IfEntityWithinDistance(0, 10000, ARG_0_3, radius=3.0)
    ForceAnimation(ARG_4_7, ARG_8_11, wait_for_completion=True)
    DisableObject(ARG_4_7)


@NeverRestart
def Event11000100():
    """ 11000100: Event 11000100 """
    IfFlagOff(1, 11000100)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1001319, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=101, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1001319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1001319, 0)


@NeverRestart
def Event11000101():
    """ 11000101: Event 11000101 """
    DisableNetworkSync()
    IfFlagOff(1, 11000100)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1001319, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entity=1001319, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11000110():
    """ 11000110: Event 11000110 """
    SkipLinesIfFlagOn(1, 590)
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1001200, 1)
    End()
    IfPlayerHasGood(1, 2007, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1001200, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11000111)
    Move(PLAYER, destination=1001200, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1001200, 1)
    EndIfClient()
    DisplayDialog(10010866, anchor_entity=1001200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    EnableFlag(590)


@NeverRestart
def Event11000111():
    """ 11000111: Event 11000111 """
    DisableNetworkSync()
    IfFlagOn(-1, 11000110)
    IfPlayerDoesNotHaveGood(1, 2007, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=1001200, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfClient(2)
    IfDialogPromptActivated(2, prompt_text=10010400, anchor_entity=1001200, anchor_type=CoordEntityType.Object, facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(11000110)
    DisplayDialog(10010163, anchor_entity=1001200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.NoButton)
    Restart()


@NeverRestart
def Event11000120(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11000120: Event 11000120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    EndIfClient()
    IfPlayerHasGood(1, ARG_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(ARG_12_15, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    SkipLines(1)
    DisplayDialog(ARG_4_7, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)


@RestartOnRest
def Event11000200():
    """ 11000200: Event 11000200 """
    EndIfThisEventOn()
    DisableAI(1000200)
    IfFlagOff(1, 11000200)
    IfEntityWithinDistance(1, 1000200, 10000, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    EnableAI(1000200)


@RestartOnRest
def Event11000800():
    """ 11000800: Event 11000800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1000500)
    End()
    IfCharacterDead(0, 1000500)
    EnableFlag(11000800)


@RestartOnRest
def Event11005050():
    """ 11005050: Event 11005050 """
    IfEntityWithinDistance(-1, 10000, 1000099, radius=7.0)
    IfAttacked(-1, 1000099, attacking_character=10000)
    IfObjectDestroyed(-1, 1001400)
    IfHasAIStatus(-1, 1000110, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1000099, cancel_animation=9060)


@NeverRestart
def Event11005060():
    """ 11005060: Event 11005060 """
    EndIfThisEventOn()
    CreateObjectFX(100013, obj=1001400, model_point=10)
    IfObjectDestroyed(0, 1001400)
    DeleteObjectFX(1001400, erase_root=True)


@RestartOnRest
def Event11005070():
    """ 11005070: Event 11005070 """
    IfCharacterDead(7, 1000090)
    SkipLinesIfConditionFalse(2, 7)
    DisableCharacter(1000090)
    End()
    EndIfThisEventOn()
    DisableAI(1000090)
    IfCharacterInsideRegion(1, PLAYER, region=1002200)
    IfAttacked(2, 1000090, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimation(1000090, 500)
    EnableAI(1000090)


@RestartOnRest
def Event11005100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 11005100: Event 11005100 """
    SkipLinesIfThisEventSlotOn(6)
    DisableGravity(ARG_4_7)
    DisableCollision(ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_0_3)
    IfAttacked(-1, ARG_4_7, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    Wait(ARG_8_11)
    EnableGravity(ARG_4_7)
    EnableCollision(ARG_4_7)
    ResetStandbyAnimationSettings(ARG_4_7)


@RestartOnRest
def Event11005200(ARG_0_3: int, ARG_4_7: int):
    """ 11005200: Event 11005200 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_4_7)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event11005150(ARG_0_3: int, ARG_4_7: int):
    """ 11005150: Event 11005150 """
    SkipLinesIfThisEventSlotOff(2)
    PostDestruction(ARG_4_7, slot=1)
    End()
    RestoreObject(ARG_4_7)
    DisableCharacter(ARG_0_3)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=3.0)
    IfObjectDestroyed(2, ARG_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, 1)
    DestroyObject(ARG_4_7, slot=1)
    PlaySoundEffect(anchor_entity=ARG_4_7, sound_type=SoundType.o_Object, sound_id=132200000)
    EnableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 3002)
    End()
    EnableCharacter(ARG_0_3)


@RestartOnRest
def Event11000850(ARG_0_3: int):
    """ 11000850: Event 11000850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfCharacterDead(0, ARG_0_3)
    End()


@NeverRestart
def Event11000600(ARG_0_3: int, ARG_4_7: int):
    """ 11000600: Event 11000600 """
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
def Event11000510(ARG_0_3: int, ARG_4_7: int):
    """ 11000510: Event 11000510 """
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
def Event11000520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11000520: Event 11000520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11000530(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11000530: Event 11000530 """
    SkipLinesIfFlagOn(9, 11000580)
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1250)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfObjectDestroyed(-1, 1001250)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    SkipLinesIfObjectDestroyed(1, 1001250)
    DestroyObject(1001250, slot=1)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=7821)
    EnableFlag(11000580)


@NeverRestart
def Event11000531(ARG_0_3: int):
    """ 11000531: Event 11000531 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1252)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11000532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11000532: Event 11000532 """
    IfFlagOff(1, 1434)
    IfFlagOff(1, 1435)
    IfFlagOn(1, 1430)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    DisableCharacter(ARG_0_3)


@NeverRestart
def Event11000533(ARG_0_3: int, ARG_4_7: int):
    """ 11000533: Event 11000533 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlag(1434)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event11000534(ARG_0_3: int):
    """ 11000534: Event 11000534 """
    IfFlagOn(1, 1250)
    IfFlagOff(1, 1253)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(ARG_0_3)
    IfObjectDestroyed(0, 1001250)
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(ARG_0_3)


@NeverRestart
def Event11005030():
    """ 11005030: Event 11005030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6541, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005037)
    IfClient(2)
    IfFlagOn(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6541)
    EndIfFlagOn(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6541)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6541, region=1002000, summon_flag=11005032, dismissal_flag=11005037)


@NeverRestart
def Event11005031():
    """ 11005031: Event 11005031 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005032)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6541, command_id=10, slot=0)
    ReplanAI(6541)
    IfCharacterInsideRegion(0, 6541, region=1002998)
    RotateToFaceEntity(6541, 1002997)
    ForceAnimation(6541, 7410)
    AICommand(6541, command_id=-1, slot=0)
    ReplanAI(6541)


@NeverRestart
def Event11005033():
    """ 11005033: Event 11005033 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6591, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005038)
    IfClient(2)
    IfFlagOn(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6591)
    EndIfFlagOn(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, 6591)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6591, region=1002002, summon_flag=11005035, dismissal_flag=11005038)
    IfFlagOn(0, 11005035)
    AddSpecialEffect(6591, 5450)


@NeverRestart
def Event11005034():
    """ 11005034: Event 11005034 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005035)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6591, command_id=10, slot=0)
    ReplanAI(6591)
    IfCharacterInsideRegion(0, 6591, region=1002998)
    RotateToFaceEntity(6591, 1002997)
    ForceAnimation(6591, 7410)
    AICommand(6591, command_id=-1, slot=0)
    ReplanAI(6591)


@NeverRestart
def Event11005039():
    """ 11005039: Event 11005039 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11005040)
    EndIfFlagOn(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11000810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002005)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6562, region=1002001, summon_flag=11005040, dismissal_flag=11005041)
    Wait(20.0)
    Restart()


@NeverRestart
def Event11000810():
    """ 11000810: Event 11000810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11005040)
    IfFlagOff(1, 11005041)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6562)
    EndIfThisEventOn()
    IfCharacterDead(0, 6562)
    EnableFlag(11000810)
