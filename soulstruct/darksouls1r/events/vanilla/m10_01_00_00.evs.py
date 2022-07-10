"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11010000()
    Event_11012007()
    Event_11012008()
    Event_11012009()
    Event_11012003()
    Event_11012010()
    Event_11012011()
    Event_11012500()
    Event_11012510(
        0,
        flag=11012520,
        flag_1=11012500,
        obj=1011042,
        character=1010000,
        item_lot_param_id=15020,
        item_lot_param_id_1=16020
    )
    Event_11015510(0, 1011042, 11012500, 11012520, 22680, 1.2000000476837158)
    Event_11012014()
    Event_11012501()
    Event_11012012()
    Event_11012510(
        1,
        flag=11012521,
        flag_1=11012501,
        obj=1011043,
        character=1010001,
        item_lot_param_id=15030,
        item_lot_param_id_1=16030
    )
    Event_11015510(1, 1011043, 11012501, 11012521, 22679, 3.200000047683716)
    EnableFlag(11010790)
    EnableFlag(11010791)
    Event_11012502()
    Event_11012510(
        2,
        flag=11012522,
        flag_1=11012502,
        obj=1011041,
        character=1010057,
        item_lot_param_id=15150,
        item_lot_param_id_1=16150
    )
    Event_11015510(2, 1011041, 11012502, 11012522, 22681, 1.2000000476837158)
    if FlagDisabled(11012502):
        Event_11010899()
        Event_11010782()
        Event_11010783()
        Event_11010790()
        Event_11010791()
        Event_11015301()
        Event_11010784()
        Event_11015302()
        Event_11015303()
        Event_11015304()
        Event_11010851()
        Event_11010852()
        Event_11010850()
        Event_11015307()
        Event_11015308()
        Event_11010200(0, tae_event_id=10, animation_id=3000)
        Event_11010200(1, tae_event_id=20, animation_id=3001)
        Event_11010200(2, tae_event_id=30, animation_id=3002)
        Event_11010200(3, tae_event_id=40, animation_id=3009)
        Event_11010200(4, tae_event_id=50, animation_id=3010)
        Event_11010200(5, tae_event_id=60, animation_id=7004)
        Event_11010200(6, tae_event_id=70, animation_id=7005)
        Event_11010200(7, tae_event_id=80, animation_id=7008)
        Event_11010200(8, tae_event_id=90, animation_id=7009)
        Event_11010200(9, tae_event_id=100, animation_id=7011)
    Event_11012005()
    Event_11012006()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11010000)
def Event_11010000():
    """Event 11010000"""
    RegisterBonfire(bonfire_flag=11010992, obj=1011960)
    RegisterBonfire(bonfire_flag=11010984, obj=1011961)
    RegisterBonfire(bonfire_flag=11010976, obj=1011962)
    RegisterLadder(start_climbing_flag=11010010, stop_climbing_flag=11010011, obj=1011000)
    RegisterLadder(start_climbing_flag=11010012, stop_climbing_flag=11010013, obj=1011001)
    RegisterLadder(start_climbing_flag=11010014, stop_climbing_flag=11010015, obj=1011002)
    RegisterLadder(start_climbing_flag=11010016, stop_climbing_flag=11010017, obj=1011003)
    RegisterLadder(start_climbing_flag=11010018, stop_climbing_flag=11010019, obj=1011004)
    RegisterLadder(start_climbing_flag=11010020, stop_climbing_flag=11010021, obj=1011005)
    RegisterLadder(start_climbing_flag=11010022, stop_climbing_flag=11010023, obj=1011006)
    RegisterLadder(start_climbing_flag=11010024, stop_climbing_flag=11010025, obj=1011007)
    RegisterLadder(start_climbing_flag=11010026, stop_climbing_flag=11010027, obj=1011008)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011010)
    RegisterLadder(start_climbing_flag=11010030, stop_climbing_flag=11010031, obj=1011011)
    CreateHazard(
        obj_flag=11010302,
        obj=1011036,
        model_point=200,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=11010308,
        obj=1011407,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=11010309,
        obj=1011408,
        model_point=100,
        behavior_param_id=5000,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    if FlagEnabled(61010610):
        EndOfAnimation(obj=1011013, animation_id=2)
        EnableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
    Event_11010140(0, region=1012050)
    Event_11010140(1, region=1012051)
    Event_11012200(0, obj_act_id=11010150, obj=1011019, text=10010860)
    Event_11012200(1, obj_act_id=11010151, obj=1011020, text=10010860)
    Event_11012200(2, obj_act_id=11010152, obj=1011021, text=10010860)
    Event_11012200(3, obj_act_id=11010153, obj=1011022, text=10010860)
    Event_11012200(4, obj_act_id=11010154, obj=1011023, text=10010860)
    Event_11012200(5, obj_act_id=11010155, obj=1011024, text=10010860)
    Event_11012210(0, obj_act_id=11010160, obj=1011033, text=10010860)
    Event_11012210(2, obj_act_id=11010162, obj=1011027, text=10010860)
    Event_11012210(3, obj_act_id=11010163, obj=1011028, text=0)
    Event_11012210(4, obj_act_id=11010164, obj=1011029, text=0)
    Event_11012210(5, obj_act_id=11010165, obj=1011031, text=0)
    Event_11012210(7, obj_act_id=11010167, obj=1011034, text=10010162)
    Event_11012210(8, obj_act_id=11010168, obj=1011030, text=10010162)
    Event_11012210(9, obj_act_id=11010169, obj=1011026, text=10010861)
    Event_11015000()
    Event_11010611()
    Event_11010600()
    Event_11010601()
    Event_11010621()
    Event_11010100()
    Event_11012004()


@NeverRestart(11010140)
def Event_11010140(_, region: int):
    """Event 11010140"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11012200)
def Event_11012200(_, obj_act_id: int, obj: int, text: int):
    """Event 11012200"""
    if ValueNotEqual(left=obj_act_id, right=0):
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        EndOfAnimation(obj=obj, animation_id=0)
        End()
    if FlagEnabled(obj_act_id):
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)


@NeverRestart(11012210)
def Event_11012210(_, obj_act_id: int, obj: int, text: int):
    """Event 11012210"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if ValueNotEqual(left=text, right=0):
        DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@NeverRestart(11010100)
def Event_11010100():
    """Event 11010100"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1011009, animation_id=0)
        RegisterLadder(start_climbing_flag=11010032, stop_climbing_flag=11010033, obj=1011009)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010500,
        anchor_entity=1011009,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    EnableFlag(11010100)
    Move(PLAYER, destination=1011009, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1011009, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11010032, stop_climbing_flag=11010033, obj=1011009)


@NeverRestart(11015000)
def Event_11015000():
    """Event 11015000"""
    AND_1.Add(FlagEnabled(61010610))
    AND_1.Add(ObjectActivated(obj_act_id=11010170))
    AND_2.Add(FlagDisabled(61010610))
    AND_2.Add(ObjectActivated(obj_act_id=11010170))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11015180)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_2)
    EnableFlag(11015182)
    Restart()
    EnableFlag(11015181)
    Restart()


@NeverRestart(11010611)
def Event_11010611():
    """Event 11010611"""
    AND_1.Add(FramesElapsed(frames=10))
    AND_1.Add(InsideMap(game_map=UNDEAD_BURG))
    
    MAIN.Await(AND_1)
    
    EnableObjectActivation(1011012, obj_act_id=-1)


@NeverRestart(11010600)
def Event_11010600():
    """Event 11010600"""
    AND_1.Add(FlagEnabled(11015181))
    AND_1.Add(Host())
    AND_2.Add(FlagEnabled(11015182))
    AND_2.Add(Host())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11015180)
    DisableFlag(11015181)
    DisableFlag(11015182)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    if FlagDisabled(61010610):
        DisableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
        ForceAnimation(1011013, 4)
        WaitFrames(frames=200)
    Event_11010611()
    Restart()
    if FlagEnabled(61010610):
        EnableNavmeshType(navmesh_id=1013100, navmesh_type=NavmeshType.Solid)
        EnableFlag(11010605)
        ForceAnimation(1011013, 2)
        WaitFrames(frames=60)
    Event_11010611()
    Restart()


@NeverRestart(11010601)
def Event_11010601():
    """Event 11010601"""
    MAIN.Await(FlagEnabled(11010605))
    
    DisableFlag(11010605)
    Wait(0.5)
    CreateHazard(
        obj_flag=11010602,
        obj=1011013,
        model_point=42,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=11010603,
        obj=1011013,
        model_point=43,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=11010604,
        obj=1011013,
        model_point=44,
        behavior_param_id=5010,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.5,
        repetition_time=0.0,
    )
    Restart()


@NeverRestart(11010621)
def Event_11010621():
    """Event 11010621"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1011017, animation_id=4)
        DisableObjectActivation(1011016, obj_act_id=-1)
        End()
    EndOfAnimation(obj=1011017, animation_id=3)
    
    MAIN.Await(ObjectActivated(obj_act_id=11010171))
    
    ForceAnimation(1011017, 4)


@NeverRestart(11010899)
def Event_11010899():
    """Event 11010899"""
    EnableImmortality(1010057)
    DisableCharacter(1010057)
    SetNest(1010057, region=1012320)
    DisableFlag(11010782)
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    SkipLinesIfConditionFalse(6, AND_1)
    DisableFlag(11015310)
    EnableCharacter(1010057)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, set_draw_parent=1013211)
    SetStandbyAnimationSettings(1010057, standby_animation=7006)
    DisableCharacterCollision(1010057)
    DisableGravity(1010057)
    AND_2.Add(FlagEnabled(11010791))
    AND_2.Add(FlagEnabled(11015311))
    SkipLinesIfConditionFalse(4, AND_2)
    EnableCharacter(1010057)
    Move(1010057, destination=1012320, destination_type=CoordEntityType.Region, short_move=True)
    ResetStandbyAnimationSettings(1010057)
    SetNest(1010057, region=1012340)
    Event_11010805(0, first_flag=11015320, last_flag=11015325, animation_id=7004, flag=11015350)
    Event_11010805(1, first_flag=11015326, last_flag=11015331, animation_id=7008, flag=11015350)
    Event_11010805(2, first_flag=11015332, last_flag=11015333, animation_id=7009, flag=11015350)
    Event_11010805(3, first_flag=11015334, last_flag=11015337, animation_id=7011, flag=11015350)
    Event_11010805(4, first_flag=11015338, last_flag=11015339, animation_id=7006, flag=11015350)
    Event_11010805(5, first_flag=11015320, last_flag=11015323, animation_id=7009, flag=11015351)
    Event_11010805(6, first_flag=11015324, last_flag=11015339, animation_id=7006, flag=11015351)
    Event_11010805(7, first_flag=11015320, last_flag=11015323, animation_id=7011, flag=11015352)
    Event_11010805(8, first_flag=11015324, last_flag=11015339, animation_id=7006, flag=11015352)
    Event_11010805(9, first_flag=11015320, last_flag=11015321, animation_id=7004, flag=11015353)
    Event_11010805(10, first_flag=11015322, last_flag=11015333, animation_id=7008, flag=11015353)
    Event_11010805(11, first_flag=11015334, last_flag=11015335, animation_id=7009, flag=11015353)
    Event_11010805(12, first_flag=11015336, last_flag=11015337, animation_id=7011, flag=11015353)
    Event_11010800(0, first_flag=11015338, last_flag=11015339, animation_id=7010, flag=11015353)
    Event_11010800(1, 11015320, 11015339, 7010, 11015354)


@RestartOnRest(11012502)
def Event_11012502():
    """Event 11012502"""
    if ThisEventFlagEnabled():
        DisableCharacter(1010057)
        DisableCharacter(1010059)
        DisableCharacter(1010058)
        End()
    AND_7.Add(HealthRatioLessThan(1010057, value=0.10000000149011612))
    AND_7.Add(FlagDisabled(11015312))
    AND_7.Add(FlagDisabled(11015300))
    AND_1.Add(AND_7)
    AND_2.Add(AND_7)
    AND_3.Add(AND_7)
    AND_1.Add(FlagDisabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_2.Add(FlagEnabled(11010791))
    AND_2.Add(FlagDisabled(11015311))
    AND_3.Add(FlagEnabled(11010791))
    AND_3.Add(FlagEnabled(11015311))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_1)
    ForceAnimation(1010057, 7001, wait_for_completion=True)
    DisableCharacter(1010057)
    End()
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_2)
    ForceAnimation(1010057, 7007, wait_for_completion=True)
    DisableCharacter(1010057)
    End()
    DisableImmortality(1010057)
    Kill(1010057, award_souls=True)


@RestartOnRest(11010790)
def Event_11010790():
    """Event 11010790"""
    DisableGravity(1010058)
    EnableInvincibility(1010058)
    DisableCharacter(1010058)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1012301))
    
    DisableCharacterCollision(1010058)
    EnableFlag(11010790)
    SetNetworkUpdateRate(1010058, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableMapCollision(collision=1013200)
    EnableCharacter(1010058)
    Move(1010058, destination=1012300, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1010058, 7012, wait_for_completion=True)
    DisableCharacter(1010058)
    EnableMapCollision(collision=1013200)


@NeverRestart(11010791)
def Event_11010791():
    """Event 11010791"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010790))
    AND_1.Add(FlagDisabled(11010782))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012305))
    AND_1.Add(AllPlayersOutsideRegion(region=1012337))
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11015310)
    EnableFlag(11010791)
    EnableFlag(11010780)
    EnableCharacter(1010057)
    Move(1010057, destination=1012302, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010057, standby_animation=7006)
    ForceAnimation(1010057, 7005)
    WaitFrames(frames=395)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    DisableFlag(11015310)


@NeverRestart(11010780)
def Event_11010780():
    """Event 11010780"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=1011290, animation_id=2)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(1010057, tae_event_id=1000))
    
    ForceAnimation(1011290, 1, wait_for_completion=True)
    ForceAnimation(1011290, 2, loop=True)


@RestartOnRest(11010784)
def Event_11010784():
    """Event 11010784"""
    MAIN.Await(CharacterHasTAEEvent(1010057, tae_event_id=500))
    
    EnableFlag(11015300)
    
    MAIN.Await(CharacterHasTAEEvent(1010057, tae_event_id=600))
    
    DisableFlag(11015300)
    Restart()


@RestartOnRest(11015301)
def Event_11015301():
    """Event 11015301"""
    DisableCharacter(1010059)
    
    MAIN.Await(CharacterBackreadEnabled(1010057))
    
    if ThisEventFlagEnabled():
        SetDisplayMask(1010057, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(1010057, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(1010057, command_id=20, command_slot=0)
        End()
    CreateNPCPart(1010057, npc_part_id=3430, part_index=NPCPartType.Part1, part_health=200)
    AND_1.Add(CharacterPartHealthLessThanOrEqual(1010057, npc_part_id=3430, value=0))
    AND_1.Add(FlagDisabled(11015300))
    AND_1.Add(Attacked(attacked_entity=1010057, attacker=PLAYER))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_2.Add(CharacterDead(1010057))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    if FlagDisabled(11015311):
        ForceAnimation(1010057, 8000)
    else:
        ForceAnimation(1010057, 8010)
    
    MAIN.Await(CharacterHasTAEEvent(1010057, tae_event_id=400))
    
    SetDisplayMask(1010057, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010057, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        1010059,
        destination=1010057,
        destination_type=CoordEntityType.Character,
        model_point=66,
        copy_draw_parent=1010057,
    )
    EnableCharacter(1010059)
    ForceAnimation(1010059, 8100)
    AICommand(1010057, command_id=20, command_slot=0)
    ReplanAI(1010057)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(34310000, host_only=True)


@NeverRestart(11015302)
def Event_11015302():
    """Event 11015302"""
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_2.Add(AND_1)
    AND_2.Add(FlagEnabled(11010100))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1012330))
    AND_3.Add(AND_1)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1012331))
    AND_4.Add(AND_1)
    AND_4.Add(FlagEnabled(11010100))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1012332))
    AND_5.Add(AND_1)
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1012333))
    AND_6.Add(AND_1)
    AND_6.Add(FlagEnabled(11015305))
    AND_7.Add(AND_1)
    AND_7.Add(FlagEnabled(11015317))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_2)
    EnableFlag(11015350)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_3)
    EnableFlag(11015351)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_4)
    EnableFlag(11015352)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_5)
    EnableFlag(11015353)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_6)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_7)
    SkipLines(1)
    EnableFlag(11015354)
    DisableFlagRange((11015320, 11015339))
    EnableRandomFlagInRange(flag_range=(11015320, 11015339))
    Restart()


@NeverRestart(11010805)
def Event_11010805(_, first_flag: int, last_flag: int, animation_id: int, flag: int):
    """Event 11010805"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11015310))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    AND_1.Add(HealthRatioGreaterThan(1010057, value=0.10000000149011612))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11015311):
        return RESTART
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    if ValueEqual(left=animation_id, right=7011):
        EnableFlag(11015312)
        AddSpecialEffect(1010057, 4160)
    if ValueNotEqual(left=animation_id, right=7006):
        ForceAnimation(1010057, animation_id)
    if ValueEqual(left=animation_id, right=7004):
        WaitFrames(frames=190)
    if ValueEqual(left=animation_id, right=7006):
        WaitFrames(frames=90)
    if ValueEqual(left=animation_id, right=7008):
        WaitFrames(frames=200)
    if ValueEqual(left=animation_id, right=7009):
        WaitFrames(frames=180)
    if ValueEqual(left=animation_id, right=7011):
        WaitFrames(frames=192)
    CancelSpecialEffect(1010057, 4160)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(flag)
    DisableFlag(11015312)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11010800)
def Event_11010800(_, first_flag: int, last_flag: int, animation_id: int, flag: int):
    """Event 11010800"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11015310))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    AND_1.Add(HealthRatioGreaterThan(1010057, value=0.10000000149011612))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11015311):
        return RESTART
    EnableFlag(11015311)
    EnableCharacterCollision(1010057)
    EnableGravity(1010057)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    ResetStandbyAnimationSettings(1010057)
    SetBackreadStateAlternate(1010057, True)
    SetNetworkUpdateRate(1010057, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(1010057, 4160)
    ForceAnimation(1010057, animation_id)
    WaitFrames(frames=111)
    CancelSpecialEffect(1010057, 4160)
    SetBackreadStateAlternate(1010057, False)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(flag)
    DisableFlag(11015317)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11015303)
def Event_11015303():
    """Event 11015303"""
    AND_1.Add(FlagDisabled(11015306))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagEnabled(11010100))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1012332))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1012335))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1012336))
    AND_1.Add(OR_7)
    AND_2.Add(FlagEnabled(11015306))
    AND_2.Add(FlagDisabled(11015311))
    AND_2.Add(FlagEnabled(11010791))
    AND_2.Add(AllPlayersOutsideRegion(region=1012332))
    AND_2.Add(AllPlayersOutsideRegion(region=1012335))
    AND_2.Add(AllPlayersOutsideRegion(region=1012336))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableFlag(11015306)
    Restart()
    DisableFlag(11015306)
    RestartEvent(event_id=11015304)
    Restart()


@NeverRestart(11015304)
def Event_11015304():
    """Event 11015304"""
    AND_1.Add(FlagDisabled(11015305))
    AND_1.Add(FlagEnabled(11015306))
    
    MAIN.Await(AND_1)
    
    Wait(20.0)
    EnableFlag(11015305)
    Restart()


@NeverRestart(11010850)
def Event_11010850():
    """Event 11010850"""
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_1.Add(Attacked(attacked_entity=1010057, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11015317)
    Restart()


@NeverRestart(11010851)
def Event_11010851():
    """Event 11010851"""
    AND_1.Add(FlagDisabled(11015316))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(AllPlayersOutsideRegion(region=1012338))
    AND_1.Add(HealthRatioLessThan(1010057, value=0.699999988079071))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_2.Add(FlagEnabled(11015316))
    AND_2.Add(FlagEnabled(11010791))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1012338))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableFlag(11015316)
    Restart()
    DisableFlag(11015316)
    RestartEvent(event_id=11010852)
    Restart()


@NeverRestart(11010852)
def Event_11010852():
    """Event 11010852"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11015315))
    AND_1.Add(FlagEnabled(11015316))
    
    MAIN.Await(AND_1)
    
    Wait(60.0)
    EnableFlag(11015315)
    Restart()


@RestartOnRest(11015307)
def Event_11015307():
    """Event 11015307"""
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagEnabled(11015311))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    
    MAIN.Await(AND_1)
    
    EnableAI(1010057)
    ClearTargetList(1010057)
    ReplanAI(1010057)
    SetNest(1010057, region=1012320)
    
    MAIN.Await(CharacterHasTAEEvent(1010057, tae_event_id=700))
    
    Move(1010057, destination=1012340, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010057, standby_animation=7006)
    ForceAnimation(1010057, 7016)
    WaitFrames(frames=110)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, short_move=True)
    AICommand(1010057, command_id=-1, command_slot=1)
    DisableAI(1010057)
    ClearTargetList(1010057)
    ReplanAI(1010057)
    DisableFlag(11015305)
    DisableFlag(11015309)
    DisableFlag(11015311)
    Restart()


@NeverRestart(11015308)
def Event_11015308():
    """Event 11015308"""
    AND_1.Add(FlagDisabled(11015309))
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_1.Add(AllPlayersOutsideRegion(region=1012334))
    AND_2.Add(FlagEnabled(11015309))
    AND_2.Add(FlagDisabled(11015310))
    AND_2.Add(FlagEnabled(11010791))
    AND_2.Add(HealthRatioGreaterThanOrEqual(1010057, value=0.10000000149011612))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1012334))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    EnableFlag(11015309)
    AICommand(1010057, command_id=1, command_slot=1)
    ClearTargetList(1010057)
    ReplanAI(1010057)
    Restart()
    DisableFlag(11015309)
    AICommand(1010057, command_id=-1, command_slot=1)
    ClearTargetList(1010057)
    ReplanAI(1010057)
    Restart()


@NeverRestart(11010782)
def Event_11010782():
    """Event 11010782"""
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010790))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012337))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=10)
    if FlagEnabled(11015311):
        return RESTART
    EnableFlag(11015310)
    EnableFlag(11015312)
    DisableFlag(11010791)
    ForceAnimation(1010057, 7013, wait_for_completion=True)
    DisableCharacter(1010057)
    Move(1010057, destination=1012310, destination_type=CoordEntityType.Region, set_draw_parent=1013210)


@NeverRestart(11010783)
def Event_11010783():
    """Event 11010783"""
    AND_1.Add(FlagDisabled(11015310))
    AND_1.Add(FlagEnabled(11010790))
    AND_1.Add(FlagEnabled(11010791))
    AND_1.Add(FlagDisabled(11015311))
    AND_1.Add(FlagEnabled(11015315))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11015310)
    SetStandbyAnimationSettings(1010057, standby_animation=7018)
    ForceAnimation(1010057, 7017, wait_for_completion=True)
    
    MAIN.Await(HealthRatioGreaterThanOrEqual(1010057, value=0.699999988079071))
    
    SetStandbyAnimationSettings(1010057, standby_animation=7006)
    ForceAnimation(1010057, 7019)
    WaitFrames(frames=50)
    DisableFlag(11015315)
    DisableFlag(11015316)
    DisableFlag(11015310)
    Restart()


@NeverRestart(11010200)
def Event_11010200(_, tae_event_id: int, animation_id: int):
    """Event 11010200"""
    AND_1.Add(CharacterBackreadEnabled(1010057))
    AND_1.Add(CharacterHasTAEEvent(1010057, tae_event_id=tae_event_id))
    
    MAIN.Await(AND_1)
    
    HellkiteBreathControl(1010057, obj=1011035, animation_id=animation_id)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(1010057, tae_event_id=tae_event_id))
    
    Restart()


@NeverRestart(11012003)
def Event_11012003():
    """Event 11012003"""
    DisableObjectActivation(1011025, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011025, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011025, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011025, obj_act_id=-1, relative_index=3)
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1012052,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1011025,
    ))
    
    if FlagEnabled(11602001):
        WarpToMap(game_map=NEW_LONDO_RUINS, player_start=1600990)
    else:
        DisplayDialog(text=10010161)
        Wait(2.0)
    Restart()


@NeverRestart(11012004)
def Event_11012004():
    """Event 11012004"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterDead(1010057))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012334))
    
    MAIN.Await(AND_1)
    
    End()


@NeverRestart(11012005)
def Event_11012005():
    """Event 11012005"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1012055,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1012504)
    ForceAnimation(PLAYER, 7522)
    Wait(0.699999988079071)
    EnableFlag(11813005)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100985)


@NeverRestart(11012006)
def Event_11012006():
    """Event 11012006"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1012056,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1012505)
    ForceAnimation(PLAYER, 7114)
    Wait(2.0)
    EnableFlag(11813003)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100983)


@RestartOnRest(11012501)
def Event_11012501():
    """Event 11012501"""
    DisableSoundEvent(sound_id=1013801)
    DisableObject(1011039)
    DisableObject(1011040)
    DeleteVFX(1013404, erase_root_only=False)
    DeleteVFX(1013405, erase_root_only=False)
    if ThisEventFlagEnabled():
        DisableCharacter(1010001)
        Kill(1010001)
        End()
    AND_1.Add(FlagEnabled(11012114))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1012061))
    OR_1.Add(FlagEnabled(11015114))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11015114):
        Wait(3.0)
    EnableObject(1011039)
    EnableObject(1011040)
    CreateVFX(1013404)
    CreateVFX(1013405)
    Move(1010001, destination=1012501, destination_type=CoordEntityType.Region, short_move=True)
    SetStandbyAnimationSettings(1010001, cancel_animation=9060)
    Wait(5.0)
    EnableBossHealthBar(1010001, name=2232)
    EnableSoundEvent(sound_id=1013801)
    
    MAIN.Await(CharacterDead(1010001))
    
    DisableBossHealthBar(1010001)
    DisableSoundEvent(sound_id=1013801)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1011039)
    DisableObject(1011040)
    DeleteVFX(1013404)
    DeleteVFX(1013405)


@NeverRestart(11012012)
def Event_11012012():
    """Event 11012012"""
    if FlagEnabled(11012501):
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012060))
    AND_1.Add(FlagDisabled(11012501))
    
    MAIN.Await(AND_1)
    
    Wait(5.0)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    ForceAnimation(1010004, 2007)
    AddSpecialEffect(1010004, 5600)
    ForceAnimation(1010005, 2007)
    AddSpecialEffect(1010005, 5600)
    ForceAnimation(1010006, 2007)
    AddSpecialEffect(1010006, 5600)
    ForceAnimation(1010007, 2007)
    AddSpecialEffect(1010007, 5600)
    ForceAnimation(1010008, 2007)
    AddSpecialEffect(1010008, 5600)
    ForceAnimation(1010009, 2007)
    AddSpecialEffect(1010009, 5600)
    ForceAnimation(1010010, 2007)
    AddSpecialEffect(1010010, 5600)
    ForceAnimation(1010011, 2007)
    AddSpecialEffect(1010011, 5600)
    ForceAnimation(1010012, 2007)
    AddSpecialEffect(1010012, 5600)
    ForceAnimation(1010013, 2007)
    AddSpecialEffect(1010013, 5600)
    ForceAnimation(1010014, 2007)
    AddSpecialEffect(1010014, 5600)
    ForceAnimation(1010015, 2007)
    AddSpecialEffect(1010015, 5600)
    ForceAnimation(1010016, 2007)
    AddSpecialEffect(1010016, 5600)
    ForceAnimation(1010017, 2007)
    AddSpecialEffect(1010017, 5600)
    ForceAnimation(1010018, 2007)
    AddSpecialEffect(1010018, 5600)
    ForceAnimation(1010019, 2007)
    AddSpecialEffect(1010019, 5600)
    ForceAnimation(1010020, 2007)
    AddSpecialEffect(1010020, 5600)
    ForceAnimation(1010021, 2007)
    AddSpecialEffect(1010021, 5600)
    ForceAnimation(1010022, 2007)
    AddSpecialEffect(1010022, 5600)
    ForceAnimation(1010023, 2007)
    AddSpecialEffect(1010023, 5600)
    ForceAnimation(1010024, 2007)
    AddSpecialEffect(1010024, 5600)
    ForceAnimation(1010025, 2007)
    AddSpecialEffect(1010025, 5600)
    ForceAnimation(1010026, 2007)
    AddSpecialEffect(1010026, 5600)
    ForceAnimation(1010027, 2007)
    AddSpecialEffect(1010027, 5600)
    ForceAnimation(1010028, 2007)
    AddSpecialEffect(1010028, 5600)
    ForceAnimation(1010029, 2007)
    AddSpecialEffect(1010029, 5600)
    ForceAnimation(1010030, 2007)
    AddSpecialEffect(1010030, 5600)
    ForceAnimation(1010031, 2007)
    AddSpecialEffect(1010031, 5600)
    ForceAnimation(1010032, 2007)
    AddSpecialEffect(1010032, 5600)
    ForceAnimation(1010033, 2007)
    AddSpecialEffect(1010033, 5600)
    ForceAnimation(1010034, 2007)
    AddSpecialEffect(1010034, 5600)
    ForceAnimation(1010035, 2007)
    AddSpecialEffect(1010035, 5600)
    ForceAnimation(1010036, 2007)
    AddSpecialEffect(1010036, 5600)
    ForceAnimation(1010037, 2007)
    AddSpecialEffect(1010037, 5600)
    ForceAnimation(1010038, 2007)
    AddSpecialEffect(1010038, 5600)
    ForceAnimation(1010039, 2007)
    AddSpecialEffect(1010039, 5600)
    ForceAnimation(1010040, 2007)
    AddSpecialEffect(1010040, 5600)
    ForceAnimation(1010041, 2007)
    AddSpecialEffect(1010041, 5600)
    ForceAnimation(1010042, 2007)
    AddSpecialEffect(1010042, 5600)
    ForceAnimation(1010043, 2007)
    AddSpecialEffect(1010043, 5600)
    ForceAnimation(1010044, 2007)
    AddSpecialEffect(1010044, 5600)
    ForceAnimation(1010045, 2007)
    AddSpecialEffect(1010045, 5600)
    ForceAnimation(1010046, 2007)
    AddSpecialEffect(1010046, 5600)
    ForceAnimation(1010047, 2007)
    AddSpecialEffect(1010047, 5600)
    ForceAnimation(1010048, 2007)
    AddSpecialEffect(1010048, 5600)
    ForceAnimation(1010049, 2007)
    AddSpecialEffect(1010049, 5600)
    ForceAnimation(1010050, 2007)
    AddSpecialEffect(1010050, 5600)
    ForceAnimation(1010051, 2007)
    AddSpecialEffect(1010051, 5600)
    ForceAnimation(1010052, 2007)
    AddSpecialEffect(1010052, 5600)
    ForceAnimation(1010053, 2007)
    AddSpecialEffect(1010053, 5600)
    ForceAnimation(1010054, 2007)
    AddSpecialEffect(1010054, 5600)
    ForceAnimation(1010055, 2007)
    AddSpecialEffect(1010055, 5600)
    ForceAnimation(1010056, 2007)
    AddSpecialEffect(1010056, 5600)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 5602))
    SkipLinesIfConditionFalse(2, OR_7)
    AddSpecialEffect(PLAYER, 5601)
    ForceAnimation(PLAYER, 6230)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(40.0)
    Restart()


@NeverRestart(11012009)
def Event_11012009():
    """Event 11012009"""
    DisableFlag(11012109)
    AND_1.Add(InsideMap(game_map=UNDEAD_BURG))
    AND_7.Add(PlayerStandingOnCollision(1013200))
    AND_1.Add(not AND_7)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11012109)
    OR_2.Add(OutsideMap(game_map=UNDEAD_BURG))
    OR_2.Add(PlayerStandingOnCollision(1013200))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11012500)
def Event_11012500():
    """Event 11012500"""
    DisableSoundEvent(sound_id=1013800)
    DisableObject(1011037)
    DisableObject(1011038)
    DeleteVFX(1013402, erase_root_only=False)
    DeleteVFX(1013403, erase_root_only=False)
    if ThisEventFlagEnabled():
        DisableCharacter(1010000)
        Kill(1010000)
        End()
    AND_1.Add(OutsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_1.Add(OutsideMap(game_map=DUKES_ARCHIVES))
    OR_1.Add(CharacterOutsideRegion(PLAYER, region=1702006))
    AND_1.Add(OR_1)
    SkipLinesIfConditionFalse(1, AND_1)
    Move(1010000, destination=1012500, destination_type=CoordEntityType.Region, short_move=True)
    DisableAI(1010000)
    EnableInvincibility(1010000)
    DisableHealthBar(1010000)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1012057))
    AND_2.Add(Attacked(attacked_entity=1010000, attacker=PLAYER))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1012058))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1012059))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableObject(1011037)
    EnableObject(1011038)
    CreateVFX(1013402)
    CreateVFX(1013403)
    Event_11012013()
    EnableAI(1010000)
    DisableInvincibility(1010000)
    EnableBossHealthBar(1010000, name=2790)
    EnableSoundEvent(sound_id=1013800)
    
    MAIN.Await(CharacterDead(1010000))
    
    StopEvent(event_id=11012013)
    DisableBossHealthBar(1010000)
    DisableSoundEvent(sound_id=1013800)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1011037)
    DisableObject(1011038)
    DeleteVFX(1013402)
    DeleteVFX(1013403)


@NeverRestart(11012013)
def Event_11012013():
    """Event 11012013"""
    if FlagEnabled(11012500):
        return
    Wait(5.0)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    ForceAnimation(1010000, 2007)
    AddSpecialEffect(1010000, 5600)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    OR_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 5602))
    SkipLinesIfConditionFalse(2, OR_7)
    AddSpecialEffect(PLAYER, 5601)
    ForceAnimation(PLAYER, 6230)
    Wait(1.399999976158142)
    PlaySoundEffect(1011015, 130300002, sound_type=SoundType.o_Object)
    Wait(30.0)
    Restart()


@NeverRestart(11012007)
def Event_11012007():
    """Event 11012007"""
    OR_1.Add(PlayerStandingOnCollision(1013201))
    OR_1.Add(PlayerStandingOnCollision(1013202))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=1013204)
    AND_7.Add(PlayerStandingOnCollision(1013201))
    AND_2.Add(not AND_7)
    AND_6.Add(PlayerStandingOnCollision(1013202))
    AND_2.Add(not AND_6)
    
    MAIN.Await(AND_2)
    
    EnableMapCollision(collision=1013204)
    Restart()


@NeverRestart(11012008)
def Event_11012008():
    """Event 11012008"""
    OR_1.Add(PlayerStandingOnCollision(1013203))
    OR_1.Add(PlayerStandingOnCollision(1013204))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=1013201)
    DisableMapCollision(collision=1013202)
    AND_7.Add(PlayerStandingOnCollision(1013203))
    AND_2.Add(not AND_7)
    AND_6.Add(PlayerStandingOnCollision(1013204))
    AND_2.Add(not AND_6)
    
    MAIN.Await(AND_2)
    
    EnableMapCollision(collision=1013201)
    EnableMapCollision(collision=1013202)
    Restart()


@NeverRestart(11012010)
def Event_11012010():
    """Event 11012010"""
    AND_1.Add(PlayerStandingOnCollision(1013203))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012053))
    
    MAIN.Await(AND_1)
    
    MoveToEntity(PLAYER, destination=1012502, destination_type=CoordEntityType.Region)
    NightfallCameraResetRequest()
    Wait(1.0)
    Restart()


@NeverRestart(11012011)
def Event_11012011():
    """Event 11012011"""
    AND_1.Add(PlayerStandingOnCollision(1013204))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1012054))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1012503, destination_type=CoordEntityType.Region, set_draw_parent=1013203)
    NightfallCameraResetRequest()
    Wait(1.0)
    Restart()


@RestartOnRest(11012014)
def Event_11012014():
    """Event 11012014"""
    DisableCharacter(1010002)
    EnableImmortality(1010002)
    DisableGravity(1010003)
    DisableCharacterCollision(1010003)
    EnableInvincibility(1010003)
    DisableCharacter(1010003)
    if FlagEnabled(11012114):
        Kill(1010002)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1012061))
    
    EnableObject(1011039)
    EnableObject(1011040)
    CreateVFX(1013404)
    CreateVFX(1013405)
    EnableCharacter(1010002)
    FadeInCharacter(character=1010002, duration=1.0)
    Wait(2.0)
    EnableBossHealthBar(1010002, name=5270)
    EnableSoundEvent(sound_id=1013801)
    
    MAIN.Await(HealthRatioLessThanOrEqual(1010002, value=0.20000000298023224))
    
    Move(1010003, destination=1010002, destination_type=CoordEntityType.Character, model_point=230, short_move=True)
    EnableCharacter(1010003)
    FadeInCharacter(character=1010003, duration=1.0)
    FadeOutCharacter(character=1010003, duration=2.0)
    FadeOutCharacter(character=1010002, duration=2.0)
    Wait(2.0)
    DisableCharacter(1010003)
    DisableCharacter(1010002)
    DisableBossHealthBar(1010002)
    DisableSoundEvent(sound_id=1013801)
    EnableFlag(11012114)
    EnableFlag(11015114)


@NeverRestart(11012510)
def Event_11012510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11012510"""
    DisableObject(obj)
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
    AND_1.Add(PlayerHasGood(1500))
    AND_1.Add(ActionButton(
        prompt_text=10050000,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(PlayerHasGood(1600))
    AND_2.Add(ActionButton(
        prompt_text=10050001,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_3.Add(PlayerDoesNotHaveGood(1500))
    AND_3.Add(PlayerDoesNotHaveGood(1600))
    AND_3.Add(ActionButton(
        prompt_text=10050002,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7522)
    Wait(0.6000000238418579)
    AwardItemLot(item_lot_param_id, host_only=True)
    RemoveGoodFromPlayer(item=1500)
    SkipLines(9)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7522)
    Wait(0.6000000238418579)
    AwardItemLot(item_lot_param_id_1, host_only=True)
    RemoveGoodFromPlayer(item=1600)
    SkipLines(2)
    DisplayDialog(text=10050003)
    Restart()
    DeleteObjectVFX(obj)
    DisableObject(obj)
    EnableFlag(flag)
    End()


@NeverRestart(11015510)
def Event_11015510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11015510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()
