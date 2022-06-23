"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11000992, obj=1001960)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=1001140)
    RegisterStatue(obj=1001900, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001901, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001902, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001903, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001904, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001905, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001906, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=1001907, game_map=DEPTHS, statue_type=StatueType.Stone)
    SkipLinesIfClient(5)
    DisableFlag(11000000)
    DisableObject(1001994)
    DeleteVFX(vfx_id=1001995, erase_root_only=False)
    DisableObject(1001996)
    DeleteVFX(vfx_id=1001997, erase_root_only=False)
    SkipLinesIfFlagDisabled(1, 11000100)
    EndOfAnimation(obj=1001319, animation_id=0)
    Event_11000090(0, 1001700, 1001701, 1002600, 1002601)
    Event_11005080()
    Event_11005081()
    Event_11005082()
    Event_11000100()
    Event_11000101()
    Event_11000120(0, 11000120, 10010877, 1001315, 10010883, 2018)
    Event_11000200()
    Event_11000800()
    Event_11005050()
    Event_11005060()
    Event_11005070()
    Event_11000110()
    Event_11000111()
    Event_11000600(0, 1001650, 11000600)
    DisableSoundEvent(sound_id=1003800)
    SkipLinesIfFlagDisabled(4, 2)
    Event_11005392()
    DisableObject(1001990)
    DeleteVFX(vfx_id=1001991, erase_root_only=False)
    SkipLines(10)
    Event_11005390()
    Event_11005391()
    Event_11005393()
    Event_11005392()
    Event_11000001()
    Event_11005394()
    Event_11005395()
    Event_11005396()
    Event_11005397()
    Event_11005398()
    Event_11005000(0, 1001000, 1001000, 1)
    Event_11005000(1, 1001001, 1001001, 1)
    Event_11005000(2, 1001002, 1001002, 3)
    Event_11005200(0, 1000120, 1002020)
    Event_11005200(1, 1000121, 1002020)
    Event_11005200(2, 1000122, 1002020)
    Event_11005200(3, 1000123, 1002020)
    Event_11005200(4, 1000124, 1002020)
    Event_11005200(5, 1000125, 1002020)
    Event_11005200(6, 1000110, 1002021)
    Event_11005200(7, 1000111, 1002021)
    Event_11005200(8, 1000112, 1002022)
    Event_11005200(9, 1000113, 1002022)
    Event_11005200(10, 1000126, 1002022)
    Event_11005100(0, 1002100, 1000100, 0.0)
    Event_11005100(1, 1002101, 1000101, 0.0)
    Event_11005100(2, 1002102, 1000102, 0.0)
    Event_11005100(3, 1002102, 1000103, 0.6000000238418579)
    Event_11005100(4, 1002103, 1000104, 0.0)
    Event_11005100(5, 1002103, 1000105, 0.20000000298023224)
    Event_11005100(6, 1002103, 1000106, 0.8999999761581421)
    Event_11005100(7, 1002107, 1000107, 0.0)
    Event_11005150(0, 1000150, 1001100)
    Event_11005150(1, 1000151, 1001101)
    Event_11005150(2, 1000152, 1001102)
    Event_11000850(0, 1000110)
    Event_11000850(1, 1000099)
    Event_11000850(2, 1000090)
    Event_11000850(3, 1000300)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6541, event_flag=8310)
    HumanityRegistration(6591, event_flag=8462)
    HumanityRegistration(6562, event_flag=8956)
    Event_11005030()
    Event_11005031()
    Event_11005033()
    Event_11005034()
    Event_11005039()
    Event_11000810()
    HumanityRegistration(6130, event_flag=8390)
    SkipLinesIfClient(1)
    DisableFlag(11000580)
    SkipLinesIfFlagEnabled(3, 11000580)
    SkipLinesIfFlagEnabled(2, 1250)
    SkipLinesIfFlagEnabled(1, 1253)
    DisableCharacter(6130)
    SkipLinesIfFlagDisabled(2, 1250)
    DisableGravity(6130)
    DisableCharacterCollision(6130)
    Event_11000530(0, 6130, 1250, 1255, 1251)
    Event_11000531(0, 6130)
    Event_11000510(0, 6130, 1253)
    Event_11000520(0, 6130, 1250, 1255, 1254)
    Event_11000534(0, 6130)
    HumanityRegistration(6260, event_flag=8430)
    SkipLinesIfFlagEnabled(2, 1434)
    SkipLinesIfFlagEnabled(1, 1430)
    DisableCharacter(6260)
    Event_11000532(0, 6260, 1430, 1459, 1431)
    Event_11000510(1, 6260, 1434)
    Event_11000533(0, 6260, 1435)


@NeverRestart(11000090)
def Event_11000090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11000090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
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


@RestartOnRest(11005080)
def Event_11005080():
    """Event 11005080"""
    EndIfThisEventFlagEnabled()
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
    IfFlagEnabled(0, 11000050)
    EndIfFlagEnabled(735)
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


@RestartOnRest(11005081)
def Event_11005081():
    """Event 11005081"""
    IfFlagEnabled(-1, 11005085)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11000050)
    DisableFlag(11005085)
    EnableFlag(5001)
    Kill(1000900)
    Kill(1000901)
    Kill(1000902)
    Kill(1000903)
    Kill(1000904)
    Kill(1000905)
    Kill(1000906)
    Kill(1000907)
    Kill(1000908)
    Kill(1000909)
    Kill(1000910)
    Kill(1000911)
    Kill(1000912)
    Kill(1000913)


@RestartOnRest(11005082)
def Event_11005082():
    """Event 11005082"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DEPTHS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11000050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DEPTHS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11000050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DEPTHS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11000050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DEPTHS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11000050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DEPTHS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11000050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DEPTHS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11000050)
    RestartIfConditionFalse(-6)
    EnableFlag(11000050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DEPTHS)
    RestartIfConditionFalse(7)
    DisableFlag(11000050)
    EnableFlag(11005085)


@NeverRestart(11005390)
def Event_11005390():
    """Event 11005390"""
    IfFlagDisabled(1, 2)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1001990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11005391)
def Event_11005391():
    """Event 11005391"""
    DisableNetworkSync()
    IfFlagDisabled(1, 2)
    IfFlagEnabled(1, 11005393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1001990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11005393)
def Event_11005393():
    """Event 11005393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 2)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1000800)


@RestartOnRest(11005392)
def Event_11005392():
    """Event 11005392"""
    SkipLinesIfFlagDisabled(5, 2)
    DisableCharacter(1000800)
    DisableCharacter(1000801)
    Kill(1000800)
    Kill(1000801)
    End()
    SkipLinesIfFlagEnabled(1, 11000000)
    DisableCharacter(1000800)
    DisableAI(1000800)
    IfFlagEnabled(1, 11005393)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(7, 11000000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(100000, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1000800)
    EnableFlag(11000000)
    EnableAI(1000800)
    EnableBossHealthBar(1000800, name=5260, slot=0)


@NeverRestart(11000001)
def Event_11000001():
    """Event 11000001"""
    IfCharacterDead(0, 1000800)
    EnableFlag(2)
    Kill(1000801)
    KillBoss(game_area_param_id=1000800)
    DisableObject(1001990)
    DeleteVFX(vfx_id=1001991)


@NeverRestart(11005394)
def Event_11005394():
    """Event 11005394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 2)
    IfFlagEnabled(1, 11005392)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1003800)


@NeverRestart(11005395)
def Event_11005395():
    """Event 11005395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 2)
    IfFlagEnabled(1, 11005394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1003800)


@RestartOnRest(11005396)
def Event_11005396():
    """Event 11005396"""
    DisableCharacter(1000801)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 11005390)
    CreateNPCPart(1000800, npc_part_id=5260, part_index=NPCPartType.Part1, part_health=300)
    IfCharacterPartHealthComparison(0, 1000800, npc_part_id=5260, comparison_type=ComparisonType.Equal, value=5)
    EzstateAIRequest(1000800, command_id=1001, slot=0)
    IfCharacterHasTAEEvent(0, 1000800, tae_event_id=400)
    EnableCharacter(1000801)
    Move(
        1000801,
        destination=1000800,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=1000800,
    )
    ForceAnimation(1000801, 8100)
    SetDisplayMask(1000800, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1000800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1000800, command_id=20, slot=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52610000, host_only=True)


@RestartOnRest(11005397)
def Event_11005397():
    """Event 11005397"""
    IfFlagEnabled(1, 11005390)
    IfCharacterBackreadEnabled(1, 1000800)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(1000800, npc_part_id=5261, part_index=NPCPartType.Part2, part_health=100, damage_correction=0.0)
    SetNPCPartEffects(1000800, npc_part_id=5261, material_sfx_id=60, material_vfx_id=60)


@RestartOnRest(11005398)
def Event_11005398():
    """Event 11005398"""
    IfFlagEnabled(0, 11005390)
    CreateNPCPart(1000800, npc_part_id=5262, part_index=NPCPartType.Part3, part_health=1)
    IfCharacterPartHealthComparison(0, 1000800, npc_part_id=5262, comparison_type=ComparisonType.Equal, value=5)
    AICommand(1000800, command_id=1, slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    SkipLinesIfFlagEnabled(2, 11005396)
    AICommand(1000800, command_id=0, slot=0)
    SkipLines(1)
    AICommand(1000800, command_id=20, slot=0)
    Restart()


@NeverRestart(11005000)
def Event_11005000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11005000"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(arg_4_7)
    End()
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=arg_0_3, radius=3.0)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    DisableObject(arg_4_7)


@NeverRestart(11000100)
def Event_11000100():
    """Event 11000100"""
    IfFlagDisabled(1, 11000100)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1001319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1001319, 0)


@NeverRestart(11000101)
def Event_11000101():
    """Event 11000101"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11000100)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010161, anchor_entity=1001319, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11000110)
def Event_11000110():
    """Event 11000110"""
    SkipLinesIfFlagEnabled(1, 590)
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1001200, animation_id=1)
    End()
    IfPlayerHasGood(1, 2007)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11000111)
    Move(PLAYER, destination=1001200, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1001200, 1)
    EndIfClient()
    DisplayDialog(text=10010866, anchor_entity=1001200)
    EnableFlag(590)


@NeverRestart(11000111)
def Event_11000111():
    """Event 11000111"""
    DisableNetworkSync()
    IfFlagEnabled(-1, 11000110)
    IfPlayerDoesNotHaveGood(1, 2007)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfClient(2)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(11000110)
    DisplayDialog(text=10010163, anchor_entity=1001200)
    Restart()


@NeverRestart(11000120)
def Event_11000120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11000120"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(text=arg_12_15, anchor_entity=arg_8_11, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=arg_4_7, anchor_entity=arg_8_11, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11000200)
def Event_11000200():
    """Event 11000200"""
    EndIfThisEventFlagEnabled()
    DisableAI(1000200)
    IfFlagDisabled(1, 11000200)
    IfEntityWithinDistance(1, entity=1000200, other_entity=PLAYER, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    ForceAnimation(1000200, 500, wait_for_completion=True)
    EnableAI(1000200)


@RestartOnRest(11000800)
def Event_11000800():
    """Event 11000800"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1000500)
    End()
    IfCharacterDead(0, 1000500)
    EnableFlag(11000800)


@RestartOnRest(11005050)
def Event_11005050():
    """Event 11005050"""
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=1000099, radius=7.0)
    IfAttacked(-1, attacked_entity=1000099, attacker=PLAYER)
    IfObjectDestroyed(-1, 1001400)
    IfHasAIStatus(-1, 1000110, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1000099, cancel_animation=9060)


@NeverRestart(11005060)
def Event_11005060():
    """Event 11005060"""
    EndIfThisEventFlagEnabled()
    CreateObjectVFX(vfx_id=1001400, obj=10, model_point=100013)
    IfObjectDestroyed(0, 1001400)
    DeleteObjectVFX(1001400)


@RestartOnRest(11005070)
def Event_11005070():
    """Event 11005070"""
    IfCharacterDead(7, 1000090)
    SkipLinesIfConditionFalse(2, 7)
    DisableCharacter(1000090)
    End()
    EndIfThisEventFlagEnabled()
    DisableAI(1000090)
    IfCharacterInsideRegion(1, PLAYER, region=1002200)
    IfAttacked(2, attacked_entity=1000090, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    ForceAnimation(1000090, 500)
    EnableAI(1000090)


@RestartOnRest(11005100)
def Event_11005100(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """Event 11005100"""
    SkipLinesIfThisEventSlotFlagEnabled(6)
    DisableGravity(arg_4_7)
    DisableCharacterCollision(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, attacked_entity=arg_4_7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableGravity(arg_4_7)
    EnableCharacterCollision(arg_4_7)
    SetStandbyAnimationSettings(arg_4_7)


@RestartOnRest(11005200)
def Event_11005200(_, arg_0_3: int, arg_4_7: int):
    """Event 11005200"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest(11005150)
def Event_11005150(_, arg_0_3: int, arg_4_7: int):
    """Event 11005150"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    PostDestruction(arg_4_7)
    End()
    RestoreObject(arg_4_7)
    DisableCharacter(arg_0_3)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=arg_0_3, radius=3.0)
    IfObjectDestroyed(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(5, condition=1)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_id=132200000, sound_type=SoundType.o_Object)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3002)
    End()
    EnableCharacter(arg_0_3)


@RestartOnRest(11000850)
def Event_11000850(_, arg_0_3: int):
    """Event 11000850"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@NeverRestart(11000600)
def Event_11000600(_, arg_0_3: int, arg_4_7: int):
    """Event 11000600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11000510)
def Event_11000510(_, arg_0_3: int, arg_4_7: int):
    """Event 11000510"""
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


@NeverRestart(11000520)
def Event_11000520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11000520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11000530)
def Event_11000530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11000530"""
    SkipLinesIfFlagEnabled(9, 11000580)
    IfFlagDisabled(1, 1253)
    IfFlagEnabled(1, 1250)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfObjectDestroyed(-1, 1001250)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfObjectDestroyed(1, 1001250)
    DestroyObject(1001250)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7821)
    EnableFlag(11000580)


@NeverRestart(11000531)
def Event_11000531(_, arg_0_3: int):
    """Event 11000531"""
    IfFlagDisabled(1, 1253)
    IfFlagEnabled(1, 1252)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


@NeverRestart(11000532)
def Event_11000532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11000532"""
    IfFlagDisabled(1, 1434)
    IfFlagDisabled(1, 1435)
    IfFlagEnabled(1, 1430)
    IfFlagEnabled(1, 11010700)
    IfFlagEnabled(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11000533)
def Event_11000533(_, arg_0_3: int, arg_4_7: int):
    """Event 11000533"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlag(1434)
    EnableFlag(arg_4_7)


@NeverRestart(11000534)
def Event_11000534(_, arg_0_3: int):
    """Event 11000534"""
    IfFlagEnabled(1, 1250)
    IfFlagDisabled(1, 1253)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(arg_0_3)
    IfObjectDestroyed(0, 1001250)
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(arg_0_3)


@NeverRestart(11005030)
def Event_11005030():
    """Event 11005030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6541, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005037)
    IfClient(2)
    IfFlagEnabled(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6541)
    EndIfFlagEnabled(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(-1, 1004)
    IfFlagEnabled(-1, 1005)
    IfFlagEnabled(-1, 1006)
    IfFlagEnabled(-1, 1010)
    IfFlagEnabled(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6541)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6541,
        region=1002000,
        summon_flag=11005032,
        dismissal_flag=11005037,
    )


@NeverRestart(11005031)
def Event_11005031():
    """Event 11005031"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11005032)
    IfFlagEnabled(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6541, command_id=10, slot=0)
    ReplanAI(6541)
    IfCharacterInsideRegion(0, 6541, region=1002998)
    RotateToFaceEntity(6541, target_entity=1002997)
    ForceAnimation(6541, 7410)
    AICommand(6541, command_id=-1, slot=0)
    ReplanAI(6541)


@NeverRestart(11005033)
def Event_11005033():
    """Event 11005033"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6591, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005038)
    IfClient(2)
    IfFlagEnabled(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6591)
    EndIfFlagEnabled(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 11020607)
    IfFlagEnabled(-1, 1572)
    IfFlagEnabled(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 1574)
    IfCharacterBackreadEnabled(1, 6591)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6591,
        region=1002002,
        summon_flag=11005035,
        dismissal_flag=11005038,
    )
    IfFlagEnabled(0, 11005035)
    AddSpecialEffect(6591, 5450)


@NeverRestart(11005034)
def Event_11005034():
    """Event 11005034"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11005035)
    IfFlagEnabled(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6591, command_id=10, slot=0)
    ReplanAI(6591)
    IfCharacterInsideRegion(0, 6591, region=1002998)
    RotateToFaceEntity(6591, target_entity=1002997)
    ForceAnimation(6591, 7410)
    AICommand(6591, command_id=-1, slot=0)
    ReplanAI(6591)


@NeverRestart(11005039)
def Event_11005039():
    """Event 11005039"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11005040)
    EndIfFlagEnabled(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11000810)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002005)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6562,
        region=1002001,
        summon_flag=11005040,
        dismissal_flag=11005041,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11000810)
def Event_11000810():
    """Event 11000810"""
    SkipLinesIfHost(3)
    IfFlagEnabled(1, 11005040)
    IfFlagDisabled(1, 11005041)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6562)
    EndIfThisEventFlagEnabled()
    IfCharacterDead(0, 6562)
    EnableFlag(11000810)
