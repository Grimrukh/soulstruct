"""
Duke's Archives / Crystal Cave

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    if FlagEnabled(14):
        RegisterBonfire(bonfire_flag=11700920, obj=1701950)
    RegisterBonfire(bonfire_flag=11700992, obj=1701960)
    RegisterBonfire(bonfire_flag=11700984, obj=1701961)
    RegisterBonfire(bonfire_flag=11700976, obj=1701962)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=1701140)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=1701141)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=1701142)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701143)
    RegisterStatue(obj=1701900, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701901, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701902, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701903, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701904, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701905, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701906, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701907, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    SkipLinesIfClient(5)
    EnableFlag(405)
    DisableObject(1701994)
    DeleteVFX(1701995, erase_root_only=False)
    DisableObject(1701996)
    DeleteVFX(1701997, erase_root_only=False)
    if FlagEnabled(11700140):
        DisableFlag(405)
    SkipLinesIfClient(9)
    SkipLinesIfFlagDisabled(6, 61700105)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702410))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1702402))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1702403))
    AND_1.Add(OR_1)
    SkipLinesIfConditionTrue(2, AND_1)
    EnableFlag(61700105)
    SkipLines(1)
    DisableFlag(61700105)
    if FlagEnabled(11700002):
        EndOfAnimation(obj=1701410, animation_id=0)
    if FlagEnabled(61700105):
        ForceAnimation(1701400, 1)
    Event_11700083(0, obj=1701706, vfx_id=1701707, destination=1702606, destination_1=1702607)
    Event_11700085()
    Event_11705080()
    Event_11705081()
    Event_11705082()
    Event_11705380()
    Event_11705381()
    Event_11705386()
    Event_11705382()
    Event_11705383()
    Event_11705384()
    Event_11705385()
    Event_11700110()
    Event_11700120(0, obj_act_id=11700120, obj=1701120, obj_1=1701121, animation_id=0, left=0)
    Event_11700120(5, obj_act_id=11700125, obj=1701125, obj_1=1701126, animation_id=1, left=1)
    Event_11700160(
        0,
        flag=11700100,
        destination=1701100,
        obj_act_id=11700210,
        obj_act_id_1=11700211,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181,
    )
    Event_11700105(
        0,
        flag=11700100,
        obj=1701100,
        obj_1=1701101,
        obj_2=1701102,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181,
    )
    Event_11700160(
        1,
        flag=11700102,
        destination=1701130,
        obj_act_id=11700220,
        obj_act_id_1=11700221,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183,
    )
    Event_11700105(
        2,
        flag=11700102,
        obj=1701130,
        obj_1=1701131,
        obj_2=1701132,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183,
    )
    Event_11700090(0, flag=11700100, state=0, anchor_entity=1701101, flag_1=11705090)
    Event_11700090(1, flag=11700100, state=1, anchor_entity=1701102, flag_1=11705090)
    Event_11700090(2, flag=11700102, state=0, anchor_entity=1701131, flag_1=11705091)
    Event_11700090(3, flag=11700102, state=1, anchor_entity=1701132, flag_1=11705091)
    Event_11705150(0, flag=11700205, destination=1701200, destination_1=1701210)
    Event_11700200(
        0,
        flag=11700205,
        obj=1701200,
        obj_1=1701201,
        collision=1703200,
        collision_1=1703201,
        navmesh_id=1703010,
        navmesh_id_1=1703011,
        flag_1=11705151,
    )
    Event_11700200(
        1,
        flag=11700205,
        obj=1701210,
        obj_1=1701211,
        collision=1703210,
        collision_1=1703211,
        navmesh_id=1703012,
        navmesh_id_1=1703013,
        flag_1=11705152,
    )
    Event_11700150(0, collision=1703100, region=1702780)
    Event_11700150(1, collision=1703101, region=1702781)
    Event_11705100()
    Event_11705103()
    Event_11705108()
    Event_11705101()
    Event_11705102()
    Event_11700130()
    RunEvent(11700132, slot=0, args=(0,))
    Event_11700300(0, obj_act_id=11700300, text=10010863, anchor_entity=1701500)
    Event_11700300(1, obj_act_id=11700311, text=10010879, anchor_entity=1701501)
    Event_11700300(2, obj_act_id=11700302, text=10010863, anchor_entity=1701502)
    Event_11700300(3, obj_act_id=11700313, text=10010879, anchor_entity=1701503)
    Event_11700300(4, obj_act_id=11700304, text=10010863, anchor_entity=1701504)
    Event_11700300(5, obj_act_id=11700305, text=10010863, anchor_entity=1701505)
    Event_11700300(6, obj_act_id=11700320, text=10010865, anchor_entity=1701506)
    Event_11700140()
    Event_11700141()
    Event_11705170()
    Event_11700700()
    DisableSoundEvent(sound_id=1703800)
    if FlagEnabled(14):
        Event_11705392()
        DisableObject(1701800)
        DisableObject(1701990)
        DeleteVFX(1701991, erase_root_only=False)
    else:
        Event_11700000()
        Event_11705390()
        Event_11705391()
        Event_11705393()
        Event_11705392()
        Event_11700001()
        Event_11705394()
        Event_11705395()
        Event_11705396()
        Event_11705397()
    Event_11705200()
    Event_11705270(0, character=1700250, radius=15.0)
    Event_11705270(1, character=1700251, radius=15.0)
    Event_11705140(0, character=1700102, region=1702150)
    Event_11705140(1, character=1700103, region=1702151)
    Event_11705160(0, character=1700350, radius=3.0)
    Event_11705160(1, character=1700351, radius=3.0)
    Event_11705160(2, character=1700352, radius=10.0)
    Event_11705010(0, character=1700400)
    Event_11705020(0, character=1700400)
    Event_11705030(0, character=1700400)
    Event_11705040(0, character=1700400)
    Event_11705050(0, character=1700400, region=1702010)
    Event_11700900(0, character=1700400)
    Event_11705060(0, character=1700400)
    Event_11705010(1, character=1700401)
    Event_11705020(1, character=1700401)
    Event_11705030(1, character=1700401)
    Event_11705040(1, character=1700401)
    Event_11705050(1, character=1700401, region=1702011)
    Event_11700900(1, character=1700401)
    Event_11705060(1, character=1700401)
    Event_11700810(0, character=6610, left=0, item_lot=0)
    Event_11700810(1, character=1700450, left=1, item_lot=33001000)
    Event_11700810(2, character=1700451, left=1, item_lot=33001000)
    Event_11700810(3, character=1700452, left=1, item_lot=33001000)
    Event_11700810(4, character=1700453, left=1, item_lot=33001000)
    Event_11700810(5, character=1700190, left=0, item_lot=0)
    Event_11700810(6, character=1700191, left=0, item_lot=0)
    Event_11700810(10, character=1700501, left=0, item_lot=0)
    Event_11700810(11, character=1700502, left=0, item_lot=0)
    Event_11700810(12, character=1700150, left=0, item_lot=0)
    Event_11700810(13, character=1700151, left=0, item_lot=0)
    Event_11705280(0, character=1700350)
    Event_11705280(1, character=1700351)
    Event_11700600(1, obj=1701651, obj_act_id=11700601)
    Event_11700600(2, obj=1701652, obj_act_id=11700602)
    Event_11700600(3, obj=1701653, obj_act_id=11700603)
    Event_11700600(4, obj=1701654, obj_act_id=11700604)
    Event_11700600(5, obj=1701655, obj_act_id=11700605)
    Event_11700600(6, obj=1701656, obj_act_id=11700606)
    Event_11700600(7, obj=1701657, obj_act_id=11700607)
    Event_11700600(8, obj=1701658, obj_act_id=11700608)
    Event_11700600(9, obj=1701659, obj_act_id=11700609)
    Event_11700600(10, obj=1701660, obj_act_id=11700610)
    Event_11700600(11, obj=1701661, obj_act_id=11700611)
    Event_11700600(12, obj=1701662, obj_act_id=11700612)
    Event_11700600(13, obj=1701663, obj_act_id=11700613)
    Event_11700600(14, obj=1701664, obj_act_id=11700614)
    Event_11700600(15, obj=1701665, obj_act_id=11700615)
    Event_11700600(16, obj=1701666, obj_act_id=11700616)
    Event_11705110(0, character=1700110)
    Event_11705110(1, character=1700111)
    Event_11705110(2, character=1700112)
    Event_11705110(3, character=1700113)
    Event_11705110(4, character=1700114)
    Event_11705110(5, character=1700115)
    Event_11705110(6, character=1700116)
    Event_11705110(7, character=1700117)
    Event_11705110(8, character=1700118)
    Event_11705110(9, character=1700119)
    Event_11705110(10, character=1700120)
    Event_11705110(11, character=1700121)
    Event_11705110(12, character=1700122)
    Event_11705110(13, character=1700123)
    Event_11705110(14, character=1700124)
    Event_11705110(15, character=1700125)
    Event_11705110(16, character=1700126)
    Event_11705110(17, character=1700127)
    Event_11705110(18, character=1700908)
    Event_11705110(19, character=1700909)
    Event_11705843(0, flag=14, line_intersects=1701990, anchor_entity=1702998, target_entity=1702997)
    Event_11705846(0, flag=14, obj=1701990, vfx_id=1701991)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6610, event_flag=8988)
    HumanityRegistration(6032, event_flag=8334)
    HumanityRegistration(6033, event_flag=8334)
    SkipLinesIfFlagRangeAnyEnabled(1, (1093, 1096))
    DisableCharacter(6032)
    if FlagDisabled(1099):
        DisableCharacter(6033)
    SetTeamTypeAndExitStandbyAnimation(6033, team_type=TeamType.HostileAlly)
    if FlagEnabled(11700594):
        Move(6032, destination=1702501, destination_type=CoordEntityType.Region, set_draw_parent=1703300)
    Event_11700510(0, character=6032, flag=1096)
    Event_11700520(0, character=6032, first_flag=1090, last_flag=1109, flag=1097)
    Event_11700520(1, character=6033, first_flag=1090, last_flag=1109, flag=1097)
    Event_11700530(0, character=6032, first_flag=1090, last_flag=1109, flag=1093)
    Event_11700531(0, character=6032, first_flag=1090, last_flag=1109, flag=1094)
    Event_11700532(0, character=6032, first_flag=1090, last_flag=1109, flag=1095)
    Event_11700533(0, character=6032, first_flag=1090, last_flag=1109, flag=1099, character_1=6033)
    HumanityRegistration(6291, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1542)
    DisableCharacter(6291)
    Event_11700510(2, character=6291, flag=1547)
    Event_11700520(2, character=6291, first_flag=1540, last_flag=1569, flag=1548)
    Event_11700538(0, character=6291, first_flag=1540, last_flag=1569, flag=1541)
    Event_11700539(0, character=6291, first_flag=1540, last_flag=1569, flag=1542)
    Event_11700540(0, character=6291, first_flag=1540, last_flag=1569, flag=1543)
    SetTeamTypeAndExitStandbyAnimation(6073, team_type=TeamType.HostileAlly)
    if FlagDisabled(1181):
        DisableCharacter(6073)
    Event_11700520(3, character=6073, first_flag=1170, last_flag=1189, flag=1177)
    Event_11700545(0, character=6073, first_flag=1170, last_flag=1189, flag=1181)


@ContinueOnRest(11700080)
def Event_11700080(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11700080"""
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
    AND_3.Add(FlagEnabled(11700080))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11700080)
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_3)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@ContinueOnRest(11700083)
def Event_11700083(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11700083"""
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


@RestartOnRest(11705080)
def Event_11705080():
    """Event 11705080"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1700900)
    DisableCharacter(1700901)
    DisableCharacter(1700902)
    DisableCharacter(1700903)
    DisableCharacter(1700904)
    DisableCharacter(1700905)
    DisableCharacter(1700906)
    DisableCharacter(1700907)
    DisableCharacter(1700908)
    DisableCharacter(1700909)
    
    MAIN.Await(FlagEnabled(11700050))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1700900)
    EnableCharacter(1700901)
    EnableCharacter(1700902)
    EnableCharacter(1700903)
    EnableCharacter(1700904)
    EnableCharacter(1700905)
    EnableCharacter(1700906)
    EnableCharacter(1700907)
    EnableCharacter(1700908)
    EnableCharacter(1700909)


@RestartOnRest(11705081)
def Event_11705081():
    """Event 11705081"""
    OR_1.Add(FlagEnabled(11705085))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11700050)
    DisableFlag(11705085)
    EnableFlag(5001)
    Kill(1700900)
    Kill(1700901)
    Kill(1700902)
    Kill(1700903)
    Kill(1700904)
    Kill(1700905)
    Kill(1700906)
    Kill(1700907)
    Kill(1700908)
    Kill(1700909)


@RestartOnRest(11705082)
def Event_11705082():
    """Event 11705082"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11700050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11700050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11700050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11700050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11700050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11700050))
    if not OR_6:
        return RESTART
    EnableFlag(11700050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DUKES_ARCHIVES))
    if not AND_7:
        return RESTART
    DisableFlag(11700050)
    EnableFlag(11705085)


@ContinueOnRest(11700085)
def Event_11700085():
    """Event 11700085"""
    if FlagEnabled(11800100):
        EnableFlag(11700086)
        DisableObject(1701710)
        DeleteVFX(1701711, erase_root_only=False)
        End()
    if FlagEnabled(11700086):
        DisableObject(1701710)
        DeleteVFX(1701711, erase_root_only=False)
        End()
    if Client():
        return
    
    MAIN.Await(ActionButton(
        prompt_text=10010410,
        anchor_entity=1702610,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1701710,
    ))
    
    DisplayStatus(10010630)
    Restart()


@RestartOnRest(11700000)
def Event_11700000():
    """Event 11700000"""
    if ThisEventFlagEnabled():
        return
    DisableObject(1701990)
    DeleteVFX(1701991, erase_root_only=False)
    DisableCharacter(1700800)
    EnableObjectInvulnerability(1701800)
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)
    EnableFlag(11705390)
    EnableFlag(11705391)
    EnableFlag(11705393)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170000, cutscene_flags=0, player_id=10000, move_to_region=1702801, game_map=DUKES_ARCHIVES)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        170000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1702801,
        game_map=DUKES_ARCHIVES,
    )
    SkipLines(1)
    PlayCutscene(170000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObjectInvulnerability(1701800)
    EnableObject(1701990)
    CreateVFX(1701991)
    Move(1700800, destination=1702800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1700800)


@ContinueOnRest(11705380)
def Event_11705380():
    """Event 11705380"""
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705381)
def Event_11705381():
    """Event 11705381"""
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705386)
def Event_11705386():
    """Event 11705386"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11700000))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1702896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700700)


@ContinueOnRest(11705382)
def Event_11705382():
    """Event 11705382"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010404,
        anchor_entity=1702895,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1702894)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    DisableBossHealthBar(1700700, name=5290)
    Restart()


@RestartOnRest(11705383)
def Event_11705383():
    """Event 11705383"""
    DisableAI(1700700)
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(AND_1)
    
    EnableAI(1700700)
    EnableBossHealthBar(1700700, name=5290)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1702890))
    
    Restart()


@ContinueOnRest(11705384)
def Event_11705384():
    """Event 11705384"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=1703801)
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1703801)
    OR_1.Add(FlagEnabled(11700000))
    OR_1.Add(CharacterOutsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(11705385)
def Event_11705385():
    """Event 11705385"""
    EnableImmortality(1700700)
    AddSpecialEffect(1700700, 5441)
    AddSpecialEffect(1700700, 5442)
    AddSpecialEffect(1700700, 5443)
    
    MAIN.Await(FlagEnabled(11700000))
    
    DisableCharacter(1700700)
    DisableObject(1701050)
    DisableObject(1701890)
    DeleteVFX(1701891)


@ContinueOnRest(11705390)
def Event_11705390():
    """Event 11705390"""
    AND_1.Add(FlagDisabled(14))
    AND_1.Add(FlagEnabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1701990,
    ))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    FaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1700800)
    Restart()


@ContinueOnRest(11705391)
def Event_11705391():
    """Event 11705391"""
    AND_1.Add(FlagDisabled(14))
    AND_1.Add(FlagEnabled(11705393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterAlive(1700800))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705393)
def Event_11705393():
    """Event 11705393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11700000))
        AND_1.Add(FlagDisabled(14))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1702996))
        AND_2.Add(ThisEventFlagEnabled())
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfLastConditionResultTrue(input_condition=AND_2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)


@RestartOnRest(11705392)
def Event_11705392():
    """Event 11705392"""
    if FlagEnabled(14):
        DisableCharacter(1700800)
        Kill(1700800)
        DisableCharacter(1700801)
        Kill(1700801)
        End()
    DisableAI(1700800)
    AND_1.Add(FlagEnabled(11705393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702990))
    
    MAIN.Await(AND_1)
    
    EnableAI(1700800)
    EnableBossHealthBar(1700800, name=5290)


@ContinueOnRest(11700001)
def Event_11700001():
    """Event 11700001"""
    DisableObject(1701950)
    
    MAIN.Await(CharacterDead(1700800))
    
    EnableFlag(14)
    KillBoss(game_area_param_id=1700800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=38)
    DisableObject(1701990)
    DeleteVFX(1701991)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1701950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1701950)
    RegisterBonfire(bonfire_flag=11700920, obj=1701950)


@ContinueOnRest(11705394)
def Event_11705394():
    """Event 11705394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(14))
    AND_1.Add(FlagEnabled(11705392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11705391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1703800)


@ContinueOnRest(11705395)
def Event_11705395():
    """Event 11705395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(14))
    AND_1.Add(FlagEnabled(11705394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1703800)


@RestartOnRest(11705396)
def Event_11705396():
    """Event 11705396"""
    AddSpecialEffect(1700800, 5440)
    AddSpecialEffect(1700800, 5441)
    AddSpecialEffect(1700800, 5442)
    AddSpecialEffect(1700800, 5443)
    EnableImmortality(1700800)
    CreateObjectVFX(1701800, vfx_id=100, dummy_id=170004)
    
    MAIN.Await(ObjectDestroyed(1701800))
    
    DeleteObjectVFX(1703100)
    ForceAnimation(1700800, 7000)
    
    MAIN.Await(CharacterHasTAEEvent(1700800, tae_event_id=500))
    
    RemoveSpecialEffect(1700800, 5440)
    RemoveSpecialEffect(1700800, 5441)
    RemoveSpecialEffect(1700800, 5442)
    RemoveSpecialEffect(1700800, 5443)
    DisableImmortality(1700800)


@RestartOnRest(11705397)
def Event_11705397():
    """Event 11705397"""
    DisableCharacter(1700801)
    if FlagEnabled(14):
        return
    if ThisEventFlagEnabled():
        SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
        SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(1700800, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(1700800))
    
    CreateNPCPart(1700800, npc_part_id=5290, part_index=NPCPartType.Part1, part_health=330)
    AND_1.Add(HealthRatio(1700800) > 0.0)
    AND_1.Add(CharacterPartHealth(1700800, npc_part_id=5290) <= 0)
    AND_2.Add(HealthRatio(1700800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    ForceAnimation(1700800, 8000)
    
    MAIN.Await(CharacterHasTAEEvent(1700800, tae_event_id=400))
    
    Move(
        1700801,
        destination=1700800,
        destination_type=CoordEntityType.Character,
        dummy_id=150,
        copy_draw_parent=1700800,
    )
    EnableCharacter(1700801)
    SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
    ForceAnimation(1700801, 8100)
    AICommand(1700800, command_id=20, command_slot=0)
    ReplanAI(1700800)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(52910000, host_only=True)


@ContinueOnRest(11700160)
def Event_11700160(
    _,
    flag: int,
    destination: int,
    obj_act_id: int,
    obj_act_id_1: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
):
    """Event 11700160"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_3.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_1)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_3)
    SkipLinesIfLastConditionResultTrue(9, input_condition=AND_2)
    SkipLinesIfFlagEnabled(8, flag)
    SkipLinesIfLastConditionResultFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 0)
    WaitFrames(frames=105)
    EnableFlag(flag_2)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()
    SkipLinesIfLastConditionResultFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 2)
    WaitFrames(frames=105)
    EnableFlag(flag_3)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()


@ContinueOnRest(11700105)
def Event_11700105(_, flag: int, obj: int, obj_1: int, obj_2: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 11700105"""
    if FlagEnabled(flag):
        EndOfAnimation(obj=obj, animation_id=11)
        EnableObjectActivation(obj_1, obj_act_id=-1)
        DisableObjectActivation(obj_2, obj_act_id=-1)
    else:
        DisableObjectActivation(obj_1, obj_act_id=-1)
        EnableObjectActivation(obj_2, obj_act_id=-1)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(flag_2))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(flag_3))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    EnableFlag(flag)
    ForceAnimation(obj, 1)
    WaitFrames(frames=300)
    DisableFlag(flag_1)
    Restart()
    DisableFlag(flag)
    ForceAnimation(obj, 3)
    WaitFrames(frames=344)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11700090)
def Event_11700090(_, flag: int, state: uchar, anchor_entity: int, flag_1: int):
    """Event 11700090"""
    DisableNetworkSync()
    AND_1.Add(FlagState(state, FlagType.Absolute, flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=195,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010170, anchor_entity=anchor_entity)
    Restart()


@ContinueOnRest(11705150)
def Event_11705150(_, flag: int, destination: int, destination_1: int):
    """Event 11705150"""
    AND_1.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    if FlagDisabled(flag):
        ForceAnimation(destination, 0)
    else:
        ForceAnimation(destination, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_2)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    if FlagDisabled(flag):
        ForceAnimation(destination_1, 0)
    else:
        ForceAnimation(destination_1, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    AND_3.Add(FlagDisabled(11705151))
    AND_3.Add(FlagDisabled(11705152))
    
    MAIN.Await(AND_3)
    
    Restart()


@ContinueOnRest(11700200)
def Event_11700200(
    _,
    flag: int,
    obj: int,
    obj_1: int,
    collision: int,
    collision_1: int,
    navmesh_id: int,
    navmesh_id_1: int,
    flag_1: int,
):
    """Event 11700200"""
    DisableObject(obj_1)
    if FlagDisabled(flag):
        EndOfAnimation(obj=obj, animation_id=3)
        DisableMapCollision(collision=collision_1)
        RemoveNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
        AddNavmeshFaceFlag(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Disable)
    else:
        EndOfAnimation(obj=obj, animation_id=1)
        DisableMapCollision(collision=collision)
        AddNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
        RemoveNavmeshFaceFlag(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Disable)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    if FlagDisabled(flag):
        ForceAnimation(obj, 1)
        DisableMapCollision(collision=collision)
        EnableObject(obj_1)
        AddNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Disable)
        ForceAnimation(obj_1, 1)
        WaitFrames(frames=180)
        DisableObject(obj_1)
        EnableMapCollision(collision=collision_1)
        EnableFlag(flag)
        DisableFlag(flag_1)
        Restart()
    ForceAnimation(obj, 3)
    DisableMapCollision(collision=collision_1)
    EnableObject(obj_1)
    AddNavmeshFaceFlag(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Disable)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=180)
    DisableObject(obj_1)
    EnableMapCollision(collision=collision)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11700110)
def Event_11700110():
    """Event 11700110"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1701111, obj_act_id=-1)
        EndOfAnimation(obj=1701110, animation_id=0)
        DisableObject(1701109)
        DisableMapCollision(collision=1703220)
        End()
    DisableObject(1701109)
    DisableMapCollision(collision=1703221)
    
    MAIN.Await(ObjectActivated(obj_act_id=11700110))
    
    DisableMapCollision(collision=1703220)
    EnableObject(1701109)
    ForceAnimation(1701110, 0)
    ForceAnimation(1701109, 0, wait_for_completion=True)
    DisableObject(1701109)
    EnableMapCollision(collision=1703221)


@ContinueOnRest(11700120)
def Event_11700120(_, obj_act_id: int, obj: int, obj_1: int, animation_id: int, left: int):
    """Event 11700120"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SkipLinesIfValueEqual(1, left=left, right=1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    End()
    if ValueNotEqual(left=left, right=0):
        OR_1.Add(FlagEnabled(11700140))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(OR_1)
    
    EnableFlag(obj_act_id)
    ForceAnimation(obj, animation_id)


@ContinueOnRest(11700150)
def Event_11700150(_, collision: int, region: int):
    """Event 11700150"""
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    EnableMapCollision(collision=collision)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DisableMapCollision(collision=collision)
    Restart()


@ContinueOnRest(11705100)
def Event_11705100():
    """Event 11705100"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    AND_1.Add(Host())
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=1702900)
    SaveRequest()


@ContinueOnRest(11705101)
def Event_11705101():
    """Event 11705101"""
    AND_1.Add(Host())
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(51700990))
    AND_1.Add(FlagDisabled(11705101))
    AND_1.Add(FlagDisabled(11700133))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702100))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11705106))
    AND_3.Add(Host())
    AND_3.Add(FlagEnabled(11705107))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFlagEnabled(9, 11700002)
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170010, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(170010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    ForceAnimation(1701410, 0)
    EnableFlag(11700002)
    EnableFlag(61700105)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_1)
    SkipLinesIfLastConditionResultTrue(9, input_condition=AND_3)
    if FlagDisabled(61700105):
        Event_11705108()
        Restart()
    EnableSoundEvent(sound_id=1703500)
    ForceAnimation(1701400, 0)
    WaitFrames(frames=150)
    ForceAnimation(1701400, 1)
    Event_11705108()
    Restart()
    if FlagEnabled(61700105):
        Event_11705108()
        Restart()
    DisableSoundEvent(sound_id=1703500)
    EnableFlag(11700133)
    ForceAnimation(1701400, 2)
    WaitFrames(frames=50)
    Event_11705108()
    Restart()


@ContinueOnRest(11705102)
def Event_11705102():
    """Event 11705102"""
    DisableNetworkSync()
    if FlagDisabled(61700105):
        DisableSoundEvent(sound_id=1703500)


@ContinueOnRest(11705103)
def Event_11705103():
    """Event 11705103"""
    AND_1.Add(FlagEnabled(61700105))
    AND_1.Add(ObjectActivated(obj_act_id=11705105))
    AND_2.Add(FlagDisabled(61700105))
    AND_2.Add(ObjectActivated(obj_act_id=11705105))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    EnableFlag(11705106)
    Restart()
    EnableFlag(11705107)
    Restart()


@ContinueOnRest(11705108)
def Event_11705108():
    """Event 11705108"""
    DisableNetworkSync()
    AND_1.Add(FramesElapsed(frames=10))
    AND_1.Add(InsideMap(game_map=DUKES_ARCHIVES))
    
    MAIN.Await(AND_1)
    
    EnableObjectActivation(1701401, obj_act_id=-1)


@RestartOnRest(11705110)
def Event_11705110(_, character: int):
    """Event 11705110"""
    AND_1.Add(FlagEnabled(61700105))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1702100))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1702101))
    AND_1.Add(OR_7)
    AND_2.Add(FlagEnabled(61700105))
    AND_2.Add(AllPlayersOutsideRegion(region=1702100))
    AND_2.Add(AllPlayersOutsideRegion(region=1702101))
    AND_3.Add(FlagDisabled(61700105))
    AND_3.Add(FlagEnabled(11700002))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_1)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    AND_7.Add(AllPlayersOutsideRegion(region=1702100))
    AND_7.Add(AllPlayersOutsideRegion(region=1702101))
    OR_2.Add(AND_7)
    OR_2.Add(FlagDisabled(61700105))
    
    MAIN.Await(OR_2)
    
    Restart()
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_2)
    AICommand(character, command_id=2, command_slot=0)
    ReplanAI(character)
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1702100))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1702101))
    OR_3.Add(FlagDisabled(61700105))
    
    MAIN.Await(OR_3)
    
    Restart()
    AICommand(character, command_id=3, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(FlagEnabled(61700105))
    
    Restart()


@RestartOnRest(11700130)
def Event_11700130():
    """Event 11700130"""
    if Client():
        return
    if FlagEnabled(51700990):
        DisableCharacter(1700100)
        Kill(1700100)
        End()
    DisableCharacterCollision(1700100)
    DisableGravity(1700100)


@RestartOnRest(11705140)
def Event_11705140(_, character: int, region: int):
    """Event 11705140"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11705101))
    
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(OR_1)
    
    ClearTargetList(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@ContinueOnRest(11700140)
def Event_11700140():
    """Event 11700140"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1701300, animation_id=0)
        End()
    AND_1.Add(PlayerHasGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(FlagEnabled(14))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(405)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=1701300, destination_type=CoordEntityType.Object, dummy_id=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1701300, 0)
    if Client():
        return
    DisplayDialog(text=10010864, anchor_entity=1701300, button_type=ButtonType.Yes_or_No)
    End()


@ContinueOnRest(11700141)
def Event_11700141():
    """Event 11700141"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11700140))
    AND_1.Add(PlayerDoesNotHaveGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11700140))
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010163, anchor_entity=1701300)
    Restart()


@RestartOnRest(11705170)
def Event_11705170():
    """Event 11705170"""
    DisableNetworkSync()
    if Client():
        return
    DisableFlag(11705170)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1702402))
    
    EnableFlag(11705170)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1702402))
    
    Restart()


@RestartOnRest(11705160)
def Event_11705160(_, character: int, radius: float):
    """Event 11705160"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    
    SetStandbyAnimationSettings(character, cancel_animation=13000)


@RestartOnRest(11705250)
def Event_11705250(_, region: int, character: int, animation_id: int):
    """Event 11705250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    EnableAI(character)


@RestartOnRest(11705270)
def Event_11705270(_, character: int, radius: float):
    """Event 11705270"""
    if ThisEventSlotFlagEnabled():
        return
    SetStandbyAnimationSettings(character, standby_animation=9000)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@ContinueOnRest(11700300)
def Event_11700300(_, obj_act_id: int, text: int, anchor_entity: int):
    """Event 11700300"""
    if Client():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11705200)
def Event_11705200():
    """Event 11705200"""
    Event_11705240(0, character=1700900)
    Event_11705240(1, character=1700901)
    Event_11705240(2, character=1700902)
    Event_11705240(3, character=1700903)
    Event_11705201(0, flag=11705200, character=1700300, region=1702301, flag_1=11705202)
    Event_11705201(1, flag=11705201, character=1700300, region=1702306, flag_1=11705202)
    Event_11705201(2, flag=11705202, character=1700300, region=1702305, flag_1=11705202)
    EnableFlag(11705210)
    Event_11705201(10, flag=11705210, character=1700301, region=1702311, flag_1=11705213)
    Event_11705201(11, flag=11705211, character=1700301, region=1702312, flag_1=11705213)
    Event_11705201(12, flag=11705212, character=1700301, region=1702313, flag_1=11705213)
    Event_11705201(13, flag=11705213, character=1700301, region=1702314, flag_1=11705213)
    EnableFlag(11705220)
    Event_11705201(20, flag=11705220, character=1700302, region=1702321, flag_1=11705221)
    Event_11705201(21, flag=11705221, character=1700302, region=1702322, flag_1=11705221)


@RestartOnRest(11705240)
def Event_11705240(_, character: int):
    """Event 11705240"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AICommand(character, command_id=1, command_slot=0)


@EndOnRest(11705201)
def Event_11705201(_, flag: int, character: int, region: int, flag_1: int):
    """Event 11705201"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=1000))
    
    MAIN.Await(AND_1)
    
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(character, region=region)
    ForceAnimation(character, 7000, wait_for_completion=True)
    if FlagEnabled(flag_1):
        AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11700810)
def Event_11700810(_, character: int, left: int, item_lot: int):
    """Event 11700810"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueNotEqual(left=left, right=0):
        OR_7.Add(CharacterHuman(PLAYER))
        OR_7.Add(CharacterHollow(PLAYER))
        if not OR_7:
            return
        AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(11705280)
def Event_11705280(_, character: int):
    """Event 11705280"""
    MAIN.Await(CharacterAlive(character))
    
    MAIN.Await(CharacterDead(character))
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(32300100, host_only=True)


@ContinueOnRest(11700600)
def Event_11700600(_, obj: int, obj_act_id: int):
    """Event 11700600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11705010)
def Event_11705010(_, character: int):
    """Event 11705010"""
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=character,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        dummy_id=7,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=character,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11705020)
def Event_11705020(_, character: int):
    """Event 11705020"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5420))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    AND_7.Add(CharacterBackreadDisabled(character))
    if AND_7:
        return RESTART
    AND_2.Add(CharacterHasSpecialEffect(character, 5421))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_3.Add(CharacterHasSpecialEffect(character, 5422))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_4.Add(CharacterHasSpecialEffect(character, 5423))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_5.Add(CharacterHasSpecialEffect(character, 5424))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceAnimation(character, 3006, wait_for_completion=True)
    ReplanAI(character)
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    Restart()


@RestartOnRest(11705030)
def Event_11705030(_, character: int):
    """Event 11705030"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_1.Add(CharacterHasSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5420))
    AND_2.Add(CharacterHasSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(character, command_id=200, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=210, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11705040)
def Event_11705040(_, character: int):
    """Event 11705040"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5422))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5423))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(character, command_id=201, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=211, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11705050)
def Event_11705050(_, character: int, region: int):
    """Event 11705050"""
    AND_1.Add(Singleplayer())
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 5421)
    ClearTargetList(character)
    ReplanAI(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    Restart()


@RestartOnRest(11700900)
def Event_11700900(_, character: int):
    """Event 11700900"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@RestartOnRest(11705060)
def Event_11705060(_, character: int):
    """Event 11705060"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    if AND_1:
        return
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 0)
    ReplanAI(character)


@RestartOnRest(11700700)
def Event_11700700():
    """Event 11700700"""
    MAIN.Await(CharacterAlive(1700510))
    
    if FlagEnabled(11700700):
        return
    AND_1.Add(DLCOwned())
    AND_1.Add(CharacterDead(1700510))
    AND_1.Add(FlagEnabled(11200530))
    AND_1.Add(FlagDisabled(1121))
    
    MAIN.Await(AND_1)
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(27100200, host_only=True)


@ContinueOnRest(11700510)
def Event_11700510(_, character: int, flag: int):
    """Event 11700510"""
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


@ContinueOnRest(11700520)
def Event_11700520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11700530)
def Event_11700530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700530"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1092))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702410))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11020694)
    EnableCharacter(character)
    DisableFlag(61700320)
    EndOfAnimation(obj=1701506, animation_id=1)
    EnableObjectActivation(1701506, obj_act_id=27401, relative_index=0)
    EnableObjectActivation(1701506, obj_act_id=27401, relative_index=1)
    DisableObjectActivation(1701506, obj_act_id=27401, relative_index=2)
    DisableObjectActivation(1701506, obj_act_id=27401, relative_index=3)


@ContinueOnRest(11700531)
def Event_11700531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700531"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1093))
    AND_1.Add(FlagEnabled(61700320))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11700594)


@ContinueOnRest(11700532)
def Event_11700532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700532"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1094))
    AND_1.Add(Host())
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1702410))
    AND_2.Add(FlagDisabled(1096))
    AND_2.Add(FlagEnabled(1093))
    AND_2.Add(FlagEnabled(14))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11700594)
    EnableCharacter(character)
    Move(character, destination=1702501, destination_type=CoordEntityType.Region, set_draw_parent=1703300)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    SetNest(character, region=1702501)


@ContinueOnRest(11700533)
def Event_11700533(_, character: int, first_flag: int, last_flag: int, flag: int, character_1: int):
    """Event 11700533"""
    if FlagDisabled(11700595):
        DisableObject(1701664)
        DisableObjectActivation(1701664, obj_act_id=-1)
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(FlagEnabled(1095))
    AND_1.Add(FlagEnabled(14))
    AND_1.Add(FlagEnabled(728))
    AND_1.Add(FlagEnabled(11700592))
    AND_2.Add(FlagDisabled(1096))
    AND_2.Add(FlagEnabled(1095))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    EnableCharacter(character_1)
    EnableFlag(11700595)


@ContinueOnRest(11700538)
def Event_11700538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700538"""
    DisableCharacter(1700500)
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1540))
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagDisabled(1513))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1501, 1511)))
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(FlagEnabled(1541))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(1700500)
    SetDisplayMask(1700500, bit_index=1, switch_type=OnOffChange.Off)


@ContinueOnRest(11700539)
def Event_11700539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700539"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1541))
    AND_1.Add(CharacterDead(1700500))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(
        character,
        destination=1700500,
        destination_type=CoordEntityType.Character,
        dummy_id=101,
        copy_draw_parent=1700500,
    )
    EnableCharacter(character)


@ContinueOnRest(11700540)
def Event_11700540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700540"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1542))
    AND_1.Add(FlagEnabled(11700593))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1547))
    AND_2.Add(FlagEnabled(1542))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_1)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11700545)
def Event_11700545(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11700545"""
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1175))
    AND_1.Add(FlagEnabled(724))
    AND_2.Add(FlagEnabled(1181))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11705843)
def Event_11705843(_, flag: int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11705843"""
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
    
    FaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@ContinueOnRest(11705846)
def Event_11705846(_, flag: int, obj: int, vfx_id: int):
    """Event 11705846"""
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
