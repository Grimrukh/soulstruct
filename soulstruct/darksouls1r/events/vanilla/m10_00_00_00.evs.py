"""
Depths

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


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
    DeleteVFX(1001995, erase_root_only=False)
    DisableObject(1001996)
    DeleteVFX(1001997, erase_root_only=False)
    if FlagEnabled(11000100):
        EndOfAnimation(obj=1001319, animation_id=0)
    Event_11000090(0, obj=1001700, vfx_id=1001701, destination=1002600, destination_1=1002601)
    Event_11005080()
    Event_11005081()
    Event_11005082()
    Event_11000100()
    Event_11000101()
    Event_11000120(0, obj_act_id=11000120, text=10010877, anchor_entity=1001315, text_1=10010883, item=2018)
    Event_11000200()
    Event_11000800()
    Event_11005050()
    Event_11005060()
    Event_11005070()
    Event_11000110()
    Event_11000111()
    Event_11000600(0, obj=1001650, obj_act_id=11000600)
    DisableSoundEvent(sound_id=1003800)
    if FlagEnabled(2):
        Event_11005392()
        DisableObject(1001990)
        DeleteVFX(1001991, erase_root_only=False)
    else:
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
    Event_11005000(0, other_entity=1001000, obj=1001000, animation_id=1)
    Event_11005000(1, other_entity=1001001, obj=1001001, animation_id=1)
    Event_11005000(2, other_entity=1001002, obj=1001002, animation_id=3)
    Event_11005200(0, character=1000120, region=1002020)
    Event_11005200(1, character=1000121, region=1002020)
    Event_11005200(2, character=1000122, region=1002020)
    Event_11005200(3, character=1000123, region=1002020)
    Event_11005200(4, character=1000124, region=1002020)
    Event_11005200(5, character=1000125, region=1002020)
    Event_11005200(6, character=1000110, region=1002021)
    Event_11005200(7, character=1000111, region=1002021)
    Event_11005200(8, character=1000112, region=1002022)
    Event_11005200(9, character=1000113, region=1002022)
    Event_11005200(10, character=1000126, region=1002022)
    Event_11005100(0, region=1002100, character=1000100, seconds=0.0)
    Event_11005100(1, region=1002101, character=1000101, seconds=0.0)
    Event_11005100(2, region=1002102, character=1000102, seconds=0.0)
    Event_11005100(3, region=1002102, character=1000103, seconds=0.6000000238418579)
    Event_11005100(4, region=1002103, character=1000104, seconds=0.0)
    Event_11005100(5, region=1002103, character=1000105, seconds=0.20000000298023224)
    Event_11005100(6, region=1002103, character=1000106, seconds=0.8999999761581421)
    Event_11005100(7, region=1002107, character=1000107, seconds=0.0)
    Event_11005150(0, character=1000150, obj=1001100, flag=11009000, flag_1=11009010)
    Event_11005150(1, character=1000151, obj=1001101, flag=11009001, flag_1=11009011)
    Event_11005150(2, character=1000152, obj=1001102, flag=11009002, flag_1=11009012)
    Event_11000850(0, character=1000110)
    Event_11000850(1, character=1000099)
    Event_11000850(2, character=1000090)
    Event_11000850(3, character=1000300)
    Event_11005843(0, flag=2, line_intersects=1001990, anchor_entity=1002998, target_entity=1002997)
    Event_11005844(0, 2, 1001990, 1001991)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6541, event_flag=8310)
    HumanityRegistration(6591, event_flag=8462)
    HumanityRegistration(6562, event_flag=8956)
    Event_11005030()
    Event_11005029()
    Event_11005031()
    Event_11005033()
    Event_11005036()
    Event_11005034()
    Event_11005039()
    Event_11000810()
    Event_11005333()
    Event_11005990(0, flag=11005032, summoned_character=6541)
    Event_11005990(1, flag=11005035, summoned_character=6591)
    HumanityRegistration(6130, event_flag=8390)
    SkipLinesIfClient(1)
    DisableFlag(11000580)
    SkipLinesIfFlagEnabled(3, 11000580)
    SkipLinesIfFlagEnabled(2, 1250)
    SkipLinesIfFlagEnabled(1, 1253)
    DisableCharacter(6130)
    if FlagEnabled(1250):
        DisableGravity(6130)
        DisableCharacterCollision(6130)
    Event_11000530(0, character=6130, first_flag=1250, last_flag=1255, flag=1251)
    Event_11000531(0, character=6130)
    Event_11000510(0, character=6130, flag=1253)
    Event_11000520(0, character=6130, first_flag=1250, last_flag=1255, flag=1254)
    Event_11000534(0, character=6130)
    HumanityRegistration(6260, event_flag=8430)
    SkipLinesIfFlagEnabled(2, 1434)
    SkipLinesIfFlagEnabled(1, 1430)
    DisableCharacter(6260)
    Event_11000532(0, character=6260, first_flag=1430, last_flag=1459, flag=1431)
    Event_11000510(1, character=6260, flag=1434)
    Event_11000533(0, 6260, 1435)


@NeverRestart(11000090)
def Event_11000090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11000090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11005080)
def Event_11005080():
    """Event 11005080"""
    if ThisEventFlagEnabled():
        return
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
    
    MAIN.Await(FlagEnabled(11000050))
    
    if FlagEnabled(735):
        return
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
    OR_1.Add(FlagEnabled(11005085))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
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
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DEPTHS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11000050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DEPTHS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11000050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DEPTHS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11000050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DEPTHS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11000050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DEPTHS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11000050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DEPTHS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11000050))
    if not OR_6:
        return RESTART
    EnableFlag(11000050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DEPTHS))
    if not AND_7:
        return RESTART
    DisableFlag(11000050)
    EnableFlag(11005085)


@NeverRestart(11005390)
def Event_11005390():
    """Event 11005390"""
    AND_1.Add(FlagDisabled(2))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1001990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11005391)
def Event_11005391():
    """Event 11005391"""
    AND_1.Add(FlagDisabled(2))
    AND_1.Add(FlagEnabled(11005393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        boss_version=True,
        line_intersects=1001990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11005393)
def Event_11005393():
    """Event 11005393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(2))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1000800)


@RestartOnRest(11005392)
def Event_11005392():
    """Event 11005392"""
    if FlagEnabled(2):
        DisableCharacter(1000800)
        DisableCharacter(1000801)
        Kill(1000800)
        Kill(1000801)
        End()
    if FlagDisabled(11000000):
        DisableCharacter(1000800)
    DisableAI(1000800)
    AND_1.Add(FlagEnabled(11005393))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_1:
        return
    SkipLinesIfFlagEnabled(7, 11000000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(100000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1000800)
    EnableFlag(11000000)
    EnableAI(1000800)
    EnableBossHealthBar(1000800, name=5260)
    DisplayBanner(BannerType.MagicRevival)


@NeverRestart(11000001)
def Event_11000001():
    """Event 11000001"""
    MAIN.Await(CharacterDead(1000800))
    
    EnableFlag(2)
    Kill(1000801)
    KillBoss(game_area_param_id=1000800)
    DisableObject(1001990)
    DeleteVFX(1001991)


@NeverRestart(11005394)
def Event_11005394():
    """Event 11005394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(2))
    AND_1.Add(FlagEnabled(11005392))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1003800)


@NeverRestart(11005395)
def Event_11005395():
    """Event 11005395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(2))
    AND_1.Add(FlagEnabled(11005394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1003800)


@RestartOnRest(11005396)
def Event_11005396():
    """Event 11005396"""
    DisableCharacter(1000801)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11005390))
    
    CreateNPCPart(1000800, npc_part_id=5260, part_index=NPCPartType.Part1, part_health=300)
    
    MAIN.Await(CharacterPartHealth(1000800, npc_part_id=5260) <= 0)
    
    EzstateAIRequest(1000800, command_id=1001, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(1000800, tae_event_id=400))
    
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
    AICommand(1000800, command_id=20, command_slot=0)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(52610000, host_only=True)


@RestartOnRest(11005397)
def Event_11005397():
    """Event 11005397"""
    AND_1.Add(FlagEnabled(11005390))
    AND_1.Add(CharacterBackreadEnabled(1000800))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(1000800, npc_part_id=5261, part_index=NPCPartType.Part2, part_health=100, damage_correction=0.0)
    SetNPCPartEffects(1000800, npc_part_id=5261, material_sfx_id=60, material_vfx_id=60)


@RestartOnRest(11005398)
def Event_11005398():
    """Event 11005398"""
    MAIN.Await(FlagEnabled(11005390))
    
    CreateNPCPart(1000800, npc_part_id=5262, part_index=NPCPartType.Part3, part_health=1)
    
    MAIN.Await(CharacterPartHealth(1000800, npc_part_id=5262) <= 0)
    
    AICommand(1000800, command_id=1, command_slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    if FlagDisabled(11005396):
        AICommand(1000800, command_id=0, command_slot=0)
    else:
        AICommand(1000800, command_id=20, command_slot=0)
    Restart()


@NeverRestart(11005000)
def Event_11005000(_, other_entity: int, obj: int, animation_id: int):
    """Event 11005000"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@NeverRestart(11000100)
def Event_11000100():
    """Event 11000100"""
    AND_1.Add(FlagDisabled(11000100))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1001319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1001319, 0)


@NeverRestart(11000101)
def Event_11000101():
    """Event 11000101"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11000100))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1001319, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11000110)
def Event_11000110():
    """Event 11000110"""
    SkipLinesIfFlagEnabled(1, 590)
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1001200, animation_id=1)
    End()
    AND_1.Add(PlayerHasGood(2007))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11000111)
    Move(PLAYER, destination=1001200, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1001200, 1)
    if Client():
        return
    DisplayDialog(text=10010866, anchor_entity=1001200)
    EnableFlag(590)


@NeverRestart(11000111)
def Event_11000111():
    """Event 11000111"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(11000110))
    AND_1.Add(PlayerDoesNotHaveGood(2007))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(Client())
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(11000110):
        return
    DisplayDialog(text=10010163, anchor_entity=1001200)
    Restart()


@NeverRestart(11000120)
def Event_11000120(_, obj_act_id: int, text: int, anchor_entity: int, text_1: int, item: int):
    """Event 11000120"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    if Client():
        return
    AND_1.Add(PlayerHasGood(item))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=text_1, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11000200)
def Event_11000200():
    """Event 11000200"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1000200)
    AND_1.Add(FlagDisabled(11000200))
    AND_1.Add(EntityWithinDistance(entity=1000200, other_entity=PLAYER, radius=9.0))
    
    MAIN.Await(AND_1)
    
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
    if ThisEventFlagEnabled():
        DisableCharacter(1000500)
        End()
    
    MAIN.Await(CharacterDead(1000500))
    
    EnableFlag(11000800)


@RestartOnRest(11005050)
def Event_11005050():
    """Event 11005050"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1000099, radius=7.0))
    OR_1.Add(Attacked(attacked_entity=1000099, attacker=PLAYER))
    OR_1.Add(ObjectDestroyed(1001400))
    OR_1.Add(HasAIStatus(1000110, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1000099, cancel_animation=9060)


@NeverRestart(11005060)
def Event_11005060():
    """Event 11005060"""
    if ThisEventFlagEnabled():
        return
    CreateObjectVFX(1001400, vfx_id=10, model_point=100013)
    
    MAIN.Await(ObjectDestroyed(1001400))
    
    DeleteObjectVFX(1001400)


@RestartOnRest(11005070)
def Event_11005070():
    """Event 11005070"""
    AND_7.Add(CharacterDead(1000090))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableCharacter(1000090)
    End()
    if ThisEventFlagEnabled():
        return
    DisableAI(1000090)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002200))
    AND_2.Add(Attacked(attacked_entity=1000090, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    ForceAnimation(1000090, 500)
    EnableAI(1000090)


@RestartOnRest(11005100)
def Event_11005100(_, region: int, character: int, seconds: float):
    """Event 11005100"""
    if ThisEventSlotFlagDisabled():
        DisableGravity(character)
        DisableCharacterCollision(character)
        OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
        OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
        MAIN.Await(OR_1)
    
        Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character)


@RestartOnRest(11005200)
def Event_11005200(_, character: int, region: int):
    """Event 11005200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)


@RestartOnRest(11005150)
def Event_11005150(_, character: int, obj: int, flag: int, flag_1: int):
    """Event 11005150"""
    AND_4.Add(CharacterDead(character))
    SkipLinesIfConditionTrue(2, AND_4)
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_5.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_5)
    SkipLinesIfFlagEnabled(1, flag)
    SkipLinesIfThisEventSlotFlagDisabled(9)
    AND_3.Add(CharacterDead(character))
    AND_3.Add(Host())
    SkipLinesIfConditionFalse(2, AND_3)
    DisableCharacter(character)
    EnableFlag(flag_1)
    if FlagEnabled(flag_1):
        DisableCharacter(character)
    PostDestruction(obj)
    End()
    RestoreObject(obj)
    DisableCharacter(character)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_2.Add(ObjectDestroyed(obj))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    DestroyObject(obj)
    PlaySoundEffect(obj, 132200000, sound_type=SoundType.o_Object)
    EnableCharacter(character)
    ForceAnimation(character, 3002)
    EnableFlag(flag)
    End()
    EnableCharacter(character)
    EnableFlag(flag)


@RestartOnRest(11000850)
def Event_11000850(_, character: int):
    """Event 11000850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@NeverRestart(11000600)
def Event_11000600(_, obj: int, obj_act_id: int):
    """Event 11000600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(11000510)
def Event_11000510(_, character: int, flag: int):
    """Event 11000510"""
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
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11000520)
def Event_11000520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11000520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11000530)
def Event_11000530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11000530"""
    if FlagDisabled(11000580):
        AND_1.Add(FlagDisabled(1253))
        AND_1.Add(FlagEnabled(1250))
        AND_1.Add(HealthRatio(character) > 0.0)
        OR_1.Add(ObjectDestroyed(1001250))
        OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
        AND_1.Add(OR_1)
    
        MAIN.Await(AND_1)
    
        DisableFlagRange((first_flag, last_flag))
        EnableFlag(flag)
    if ObjectNotDestroyed(1001250):
        DestroyObject(1001250)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=7821)
    EnableFlag(11000580)


@NeverRestart(11000531)
def Event_11000531(_, character: int):
    """Event 11000531"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1252))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)


@NeverRestart(11000532)
def Event_11000532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11000532"""
    AND_1.Add(FlagDisabled(1434))
    AND_1.Add(FlagDisabled(1435))
    AND_1.Add(FlagEnabled(1430))
    AND_1.Add(FlagEnabled(11010700))
    AND_1.Add(FlagEnabled(11400200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11000533)
def Event_11000533(_, character: int, flag: int):
    """Event 11000533"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlag(1434)
    EnableFlag(flag)


@NeverRestart(11000534)
def Event_11000534(_, character: int):
    """Event 11000534"""
    AND_1.Add(FlagEnabled(1250))
    AND_1.Add(FlagDisabled(1253))
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(character)
    
    MAIN.Await(ObjectDestroyed(1001250))
    
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(character)


@NeverRestart(11005030)
def Event_11005030():
    """Event 11005030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6541, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005037)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11005032))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6541)
    if FlagEnabled(2):
        return
    If_Unknown_3_24(AND_1, unk1=5, unk2=2)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11005032))
    AND_1.Add(FlagDisabled(11005037))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(6541))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6541,
        region=1002000,
        summon_flag=11005032,
        dismissal_flag=11005037,
    )


@NeverRestart(11005029)
def Event_11005029():
    """Event 11005029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6541, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005037)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11005032))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6541)
    if FlagEnabled(2):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11005032))
    AND_1.Add(FlagDisabled(11005037))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(6541))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
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
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11005032))
    AND_1.Add(FlagEnabled(11005393))
    
    MAIN.Await(AND_1)
    
    AICommand(6541, command_id=10, command_slot=0)
    ReplanAI(6541)
    
    MAIN.Await(CharacterInsideRegion(6541, region=1002998))
    
    RotateToFaceEntity(6541, target_entity=1002997)
    ForceAnimation(6541, 7410)
    AICommand(6541, command_id=-1, command_slot=0)
    ReplanAI(6541)


@NeverRestart(11005033)
def Event_11005033():
    """Event 11005033"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6591, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005038)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11005035))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6591)
    if FlagEnabled(2):
        return
    If_Unknown_3_24(AND_1, unk1=5, unk2=2)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11020607))
    AND_1.Add(FlagDisabled(11005035))
    AND_1.Add(FlagDisabled(11005038))
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(CharacterBackreadEnabled(6591))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6591,
        region=1002002,
        summon_flag=11005035,
        dismissal_flag=11005038,
    )


@NeverRestart(11005333)
def Event_11005333():
    """Event 11005333"""
    MAIN.Await(FlagEnabled(11005035))
    
    AddSpecialEffect(6591, 5450)


@NeverRestart(11005990)
def Event_11005990(_, flag: int, summoned_character: int):
    """Event 11005990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@NeverRestart(11005036)
def Event_11005036():
    """Event 11005036"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6591, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11005038)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11005035))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6591)
    if FlagEnabled(2):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11005035))
    AND_1.Add(FlagDisabled(11005038))
    AND_1.Add(FlagEnabled(11020607))
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(CharacterBackreadEnabled(6591))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6591,
        region=1002002,
        summon_flag=11005035,
        dismissal_flag=11005038,
    )


@NeverRestart(11005034)
def Event_11005034():
    """Event 11005034"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11005035))
    AND_1.Add(FlagEnabled(11005393))
    
    MAIN.Await(AND_1)
    
    AICommand(6591, command_id=10, command_slot=0)
    ReplanAI(6591)
    
    MAIN.Await(CharacterInsideRegion(6591, region=1002998))
    
    RotateToFaceEntity(6591, target_entity=1002997)
    ForceAnimation(6591, 7410)
    AICommand(6591, command_id=-1, command_slot=0)
    ReplanAI(6591)


@NeverRestart(11005039)
def Event_11005039():
    """Event 11005039"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11005040):
        return
    if FlagEnabled(2):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11000810))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1002005))
    
    MAIN.Await(AND_1)
    
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
    AND_1.Add(FlagEnabled(11005040))
    AND_1.Add(FlagDisabled(11005041))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(6562)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(6562))
    
    EnableFlag(11000810)


@NeverRestart(11005843)
def Event_11005843(_, flag: int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11005843"""
    AND_1.Add(Host())
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=line_intersects,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@NeverRestart(11005844)
def Event_11005844(_, flag: int, obj: int, vfx_id: int):
    """Event 11005844"""
    OR_1.Add(Multiplayer())
    OR_1.Add(UnknownPlayerType5())
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableObject(obj)
    CreateVFX(vfx_id)
    AND_3.Add(UnknownPlayerType5())
    AND_2.Add(not AND_3)
    AND_2.Add(Singleplayer())
    
    MAIN.Await(AND_2)
    
    DisableObject(obj)
    DeleteVFX(vfx_id)
    Restart()
