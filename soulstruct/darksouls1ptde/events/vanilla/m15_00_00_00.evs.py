"""
Sen's Fortress

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CreateProjectileOwner(entity=1500200)
    SetNetworkUpdateRate(1500100, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RegisterBonfire(bonfire_flag=11500984, obj=1501961)
    RegisterLadder(start_climbing_flag=11500010, stop_climbing_flag=11500011, obj=1501140)
    RegisterLadder(start_climbing_flag=11500012, stop_climbing_flag=11500013, obj=1501141)
    RegisterLadder(start_climbing_flag=11500014, stop_climbing_flag=11500015, obj=1501142)
    RegisterLadder(start_climbing_flag=11500016, stop_climbing_flag=11500017, obj=1501143)
    SkipLinesIfHost(2)
    EnableFlag(11505240)
    DisableFlag(11505360)
    SkipLinesIfClient(2)
    DisableObject(1501994)
    DeleteVFX(1501995, erase_root_only=False)
    DisableMapCollision(collision=1503210)
    DisableObject(1501800)
    DisableObject(1501801)
    DisableObject(1501802)
    DisableObject(1501803)
    DisableObject(1501804)
    DisableObject(1501805)
    DisableObject(1501806)
    DisableObject(1501807)
    if FlagDisabled(11500803):
        EndOfAnimation(obj=1501790, animation_id=3)
    if FlagEnabled(11500806):
        EndOfAnimation(obj=1501790, animation_id=0)
    if FlagEnabled(11500809):
        EndOfAnimation(obj=1501790, animation_id=1)
    if FlagEnabled(11500812):
        EndOfAnimation(obj=1501790, animation_id=2)
    DisableMapCollision(collision=1503200)
    DisableMapCollision(collision=1503201)
    DisableMapCollision(collision=1503202)
    if FlagEnabled(11500821):
        EnableObject(1501801)
        EndOfAnimation(obj=1501801, animation_id=5)
        EnableMapCollision(collision=1503200)
    if FlagEnabled(11500822):
        EnableObject(1501802)
        EndOfAnimation(obj=1501802, animation_id=6)
        EnableMapCollision(collision=1503201)
    if FlagEnabled(11500823):
        EnableObject(1501803)
        EndOfAnimation(obj=1501803, animation_id=7)
        EnableMapCollision(collision=1503202)
    SkipLinesIfFlagDisabled(21, 11500100)
    SkipLinesIfFlagEnabled(10, 11500101)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.DropAdjacent)
    EndOfAnimation(obj=1501011, animation_id=12)
    SkipLines(9)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Drop)
    EndOfAnimation(obj=1501011, animation_id=11)
    SkipLines(4)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Disable)
    Event_11500090(0, obj=1501700, vfx_id=1501701, destination=1502600, destination_1=1502601)
    Event_11500090(1, obj=1501702, vfx_id=1501703, destination=1502602, destination_1=1502603)
    Event_11505090()
    Event_11505091()
    Event_11505092()
    Event_11500201()
    Event_11505300()
    Event_11500840()
    Event_11500841(0, flag=11500803)
    Event_11500841(1, flag=11500806)
    Event_11500841(2, flag=11500809)
    Event_11500841(3, flag=11500812)
    Event_11500790()
    Event_11500791()
    Event_11500795()
    Event_11500796()
    Event_11500797()
    Event_11500798()
    Event_11500830()
    Event_11500831()
    Event_11500850()
    Event_11505255()
    Event_11500100()
    Event_11500102()
    Event_11500103()
    Event_11500106()
    Event_11500107()
    Event_11500110(0, obj=1501030, obj_act_id=11500110)
    Event_11500110(1, obj=1501031, obj_act_id=11500111)
    Event_11500110(2, obj=1501032, obj_act_id=11500112)
    Event_11500110(3, obj=1501033, obj_act_id=11500113)
    Event_11500110(5, obj=1501035, obj_act_id=11500115)
    Event_11500110(6, obj=1501036, obj_act_id=11500116)
    Event_11505050()
    Event_11505051()
    Event_11505055()
    Event_11505110()
    Event_11505101()
    Event_11505102()
    Event_11505111(0, left=11505111, region=1502700, command_id=1)
    Event_11505111(1, left=11505112, region=1502701, command_id=2)
    Event_11505111(2, left=11505113, region=1502702, command_id=3)
    Event_11505111(3, left=11505114, region=1502703, command_id=4)
    Event_11505111(4, left=11505115, region=1502704, command_id=5)
    Event_11505111(5, left=11505116, region=1502705, command_id=6)
    Event_11505111(6, left=11505117, region=1502710, command_id=-1)
    Event_11505060(0, character=1500100)
    Event_11505060(1, character=1500101)
    Event_11505060(2, character=1500102)
    Event_11505070(0, character=1500100)
    Event_11505070(1, character=1500101)
    Event_11505070(2, character=1500102)
    Event_11505080()
    Event_11500210()
    Event_11500835()
    DisableSoundEvent(sound_id=1503800)
    if FlagEnabled(11):
        Event_11505392()
        DisableObject(1501990)
        DeleteVFX(1501991, erase_root_only=False)
    else:
        Event_11505390()
        Event_11505391()
        Event_11505393()
        Event_11505392()
        Event_11500001()
        Event_11505394()
        Event_11505395()
        Event_11505350()
        Event_11505353()
    Event_11505010()
    Event_11505011()
    Event_11505012()
    Event_11505013()
    Event_11505014()
    Event_11500900()
    Event_11505015()
    Event_11505270(
        0,
        region=1502200,
        obj=1501200,
        vfx_id=1503500,
        source_entity=1501210,
        launch_angle_y=0,
        left=11505280,
    )
    Event_11505270(
        1,
        region=1502201,
        obj=1501201,
        vfx_id=1503500,
        source_entity=1501211,
        launch_angle_y=90,
        left=11505281,
    )
    Event_11505270(
        2,
        region=1502202,
        obj=1501202,
        vfx_id=1503500,
        source_entity=1501212,
        launch_angle_y=90,
        left=11505282,
    )
    Event_11505270(
        3,
        region=1502203,
        obj=1501203,
        vfx_id=1503500,
        source_entity=1501213,
        launch_angle_y=270,
        left=11505283,
    )
    Event_11505270(
        4,
        region=1502204,
        obj=1501204,
        vfx_id=1503500,
        source_entity=1501214,
        launch_angle_y=180,
        left=11505284,
    )
    Event_11505270(
        5,
        region=1502205,
        obj=1501205,
        vfx_id=1503500,
        source_entity=1501213,
        launch_angle_y=270,
        left=11505285,
    )
    Event_11505260()
    Event_11500860(0, character=6600)
    Event_11500860(1, character=1500300)
    Event_11500860(2, character=1500301)
    Event_11500860(3, character=1500302)
    Event_11500860(4, character=1500303)
    Event_11500860(5, character=1500100)
    Event_11500860(7, character=1500102)
    Event_11500600(0, obj=1501650, obj_act_id=11500600)
    Event_11500600(2, obj=1501652, obj_act_id=11500602)
    Event_11500600(4, obj=1501654, obj_act_id=11500604)
    Event_11500600(9, obj=1501659, obj_act_id=11500609)
    Event_11500600(10, obj=1501660, obj_act_id=11500610)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6600, event_flag=8980)
    HumanityRegistration(6510, event_flag=8924)
    Event_11505030()
    Event_11505032()
    HumanityRegistration(6030, event_flag=8334)
    SkipLinesIfFlagEnabled(3, 1090)
    SkipLinesIfFlagEnabled(2, 1091)
    SkipLinesIfFlagEnabled(1, 1096)
    DisableCharacter(6030)
    Event_11500510(0, character=6030, flag=1096)
    Event_11500520(0, character=6030, first_flag=1090, last_flag=1109, flag=1097)
    Event_11500530()
    Event_11500531(0, character=6030, first_flag=1090, last_flag=1109, flag=1091)
    Event_11500532(0, character=6030, first_flag=1090, last_flag=1109, flag=1092)
    SetTeamTypeAndExitStandbyAnimation(6043, team_type=TeamType.HostileAlly)
    if FlagDisabled(1117):
        DisableCharacter(6043)
    Event_11500520(1, character=6043, first_flag=1110, last_flag=1119, flag=1115)
    Event_11500533(0, character=6043, first_flag=1110, last_flag=1119, flag=1117)
    HumanityRegistration(6280, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1514)
    SkipLinesIfFlagEnabled(2, 1513)
    SkipLinesIfFlagRangeAnyEnabled(1, (1493, 1511))
    SkipLines(1)
    DisableCharacter(6280)
    SkipLinesIfFlagEnabled(1, 11500200)
    SkipLines(1)
    Move(6280, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SkipLinesIfFlagRangeAnyEnabled(1, (1491, 1492))
    SkipLines(2)
    Kill(1500120)
    Kill(1500121)
    Event_11500510(2, character=6280, flag=1512)
    Event_11500520(2, character=6280, first_flag=1490, last_flag=1539, flag=1513)
    Event_11500534(0, character=6280, first_flag=1490, last_flag=1539, flag=1491)
    Event_11500535(0, character=6280, first_flag=1490, last_flag=1539, flag=1492)
    Event_11500536(0, character=6280, first_flag=1490, last_flag=1539, flag=1493)
    HumanityRegistration(6250, event_flag=8422)
    SkipLinesIfFlagRangeAnyEnabled(1, (1420, 1429))
    EnableFlag(1420)
    Event_11500510(3, character=6250, flag=1421)
    Event_11500520(3, character=6250, first_flag=1420, last_flag=1429, flag=1422)


@ContinueOnRest(1000000000)
def Event_1000000000():
    """Event 1000000000"""
    DisableCharacter(1500200)
    SetNetworkUpdateRate(1500100, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(11500090)
def Event_11500090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11500090"""
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


@RestartOnRest(11505090)
def Event_11505090():
    """Event 11505090"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1500900)
    DisableCharacter(1500901)
    DisableCharacter(1500902)
    DisableCharacter(1500903)
    DisableCharacter(1500904)
    DisableCharacter(1500905)
    DisableCharacter(1500906)
    DisableCharacter(1500907)
    DisableCharacter(1500908)
    DisableCharacter(1500909)
    
    MAIN.Await(FlagEnabled(11500050))
    
    if FlagEnabled(735):
        return
    EnableFlag(5000)
    EnableCharacter(1500900)
    EnableCharacter(1500901)
    EnableCharacter(1500902)
    EnableCharacter(1500903)
    EnableCharacter(1500904)
    EnableCharacter(1500905)
    EnableCharacter(1500906)
    EnableCharacter(1500907)
    EnableCharacter(1500908)
    EnableCharacter(1500909)


@RestartOnRest(11505091)
def Event_11505091():
    """Event 11505091"""
    OR_1.Add(FlagEnabled(11505095))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
        DisableFlag(735)
    DisableFlag(11500050)
    DisableFlag(11505095)
    EnableFlag(5001)
    Kill(1500900)
    Kill(1500901)
    Kill(1500902)
    Kill(1500903)
    Kill(1500904)
    Kill(1500905)
    Kill(1500906)
    Kill(1500907)
    Kill(1500908)
    Kill(1500909)


@RestartOnRest(11505092)
def Event_11505092():
    """Event 11505092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11500050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11500050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11500050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11500050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11500050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11500050))
    if not OR_6:
        return RESTART
    EnableFlag(11500050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=SENS_FORTRESS))
    if not AND_7:
        return RESTART
    DisableFlag(11500050)
    EnableFlag(11505095)


@ContinueOnRest(11505300)
def Event_11505300():
    """Event 11505300"""
    CreateHazard(
        obj_flag=11505301,
        obj=1501850,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505302,
        obj=1501851,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505303,
        obj=1501852,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505304,
        obj=1501853,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505305,
        obj=1501854,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505306,
        obj=1501855,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505307,
        obj=1501856,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505308,
        obj=1501857,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505309,
        obj=1501858,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505310,
        obj=1501859,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505311,
        obj=1501860,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505312,
        obj=1501861,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505313,
        obj=1501862,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505314,
        obj=1501863,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505315,
        obj=1501864,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505316,
        obj=1501865,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505317,
        obj=1501866,
        dummy_id=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505290,
        obj=1501010,
        dummy_id=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


@ContinueOnRest(11505390)
def Event_11505390():
    """Event 11505390"""
    AND_1.Add(FlagDisabled(11))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1501990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11505391)
def Event_11505391():
    """Event 11505391"""
    AND_1.Add(FlagDisabled(11))
    AND_1.Add(FlagEnabled(11505393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1501990,
    ))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11505393)
def Event_11505393():
    """Event 11505393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1500800)


@RestartOnRest(11505392)
def Event_11505392():
    """Event 11505392"""
    if FlagEnabled(11):
        DisableCharacter(1500800)
        DropMandatoryTreasure(1500800)
        DisableBackread(1500800)
    
        MAIN.Await(CharacterBackreadEnabled(1500100))
    
        AICommand(1500100, command_id=10, command_slot=0)
        ReplanAI(1500100)
        End()
    DisableAI(1500800)
    SetStandbyAnimationSettings(1500800, standby_animation=9000)
    Event_11505351()
    Event_11505352()
    AND_1.Add(FlagEnabled(11505393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    
    MAIN.Await(AND_1)
    
    EnableAI(1500800)
    SetStandbyAnimationSettings(1500800, cancel_animation=9060)
    EnableBossHealthBar(1500800, name=2320)


@ContinueOnRest(11500001)
def Event_11500001():
    """Event 11500001"""
    DeleteVFX(1503010, erase_root_only=False)
    
    MAIN.Await(CharacterDead(1500800))
    
    EnableFlag(11)
    KillBoss(game_area_param_id=1500800)
    DisableObject(1501990)
    DeleteVFX(1501991)
    CreateVFX(1503010)
    AICommand(1500100, command_id=10, command_slot=0)
    ReplanAI(1500100)
    DisableFlag(11807020)
    DisableFlag(11807030)
    DisableFlag(11807040)
    DisableFlag(11807050)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(1500800)
    DisableBackread(1500800)


@ContinueOnRest(11505394)
def Event_11505394():
    """Event 11505394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11))
    AND_1.Add(FlagEnabled(11505392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11505391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    AND_1.Add(CharacterAlive(1500800))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1503800)


@ContinueOnRest(11505395)
def Event_11505395():
    """Event 11505395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11))
    AND_1.Add(FlagEnabled(11505394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1503800)
    PlaySoundEffect(1502990, 150100002, sound_type=SoundType.a_Ambient)


@ContinueOnRest(11505350)
def Event_11505350():
    """Event 11505350"""
    if Client():
        return
    
    MAIN.Await(CharacterHasTAEEvent(1500800, tae_event_id=100))
    
    MAIN.Await(CharacterDead(1500800))


@EndOnRest(11505351)
def Event_11505351():
    """Event 11505351"""
    if FlagEnabled(11):
        return
    EnableNetworkSync()
    
    MAIN.Await(FlagDisabled(11505355))
    
    CreateNPCPart(1500800, npc_part_id=2320, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(1500800, npc_part_id=2320, material_sfx_id=56, material_vfx_id=56)
    
    MAIN.Await(CharacterPartHealth(1500800, npc_part_id=2320) <= 0)
    
    EzstateAIRequest(1500800, command_id=1300, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(1500800, tae_event_id=1204))
    
    EnableFlag(11505355)
    CreateNPCPart(1500800, npc_part_id=2321, part_index=NPCPartType.Part2, part_health=100)
    SetNPCPartEffects(1500800, npc_part_id=2321, material_sfx_id=56, material_vfx_id=56)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    DisableFlag(11505355)
    RestartEvent(event_id=11505352)
    SetNPCPartHealth(1500800, npc_part_id=2321, desired_health=-1, overwrite_max=False)
    EzstateAIRequest(1500800, command_id=1303, command_slot=0)
    Restart()


@EndOnRest(11505352)
def Event_11505352():
    """Event 11505352"""
    if FlagEnabled(11):
        return
    EnableNetworkSync()
    
    MAIN.Await(FlagEnabled(11505355))
    
    AND_1.Add(FlagEnabled(11505355))
    AND_1.Add(CharacterPartHealth(1500800, npc_part_id=2321) <= 0)
    
    MAIN.Await(AND_1)
    
    RestartEvent(event_id=11505351)
    EzstateAIRequest(1500800, command_id=1301, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(1500800, tae_event_id=1203))
    
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    EzstateAIRequest(1500800, command_id=1304, command_slot=0)
    DisableFlag(11505355)
    Restart()


@ContinueOnRest(11505353)
def Event_11505353():
    """Event 11505353"""
    AND_1.Add(CharacterHasTAEEvent(1500800, tae_event_id=400))
    AND_2.Add(CharacterHasTAEEvent(1500800, tae_event_id=300))
    AND_3.Add(HealthRatio(1500800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    DisableMapCollision(collision=1503000)
    SkipLines(1)
    EnableMapCollision(collision=1503000)
    EndIfLastConditionResultTrue(input_condition=AND_3)
    AND_4.Add(CharacterDoesNotHaveTAEEvent(1500800, tae_event_id=400))
    AND_4.Add(CharacterDoesNotHaveTAEEvent(1500800, tae_event_id=300))
    
    MAIN.Await(AND_4)
    
    Restart()


@ContinueOnRest(11500201)
def Event_11500201():
    """Event 11500201"""
    if FlagEnabled(11500200):
        EndOfAnimation(obj=1501000, animation_id=0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502050))
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1502050))
    
    Restart()


@ContinueOnRest(11500790)
def Event_11500790():
    """Event 11500790"""
    MAIN.Await(FlagEnabled(11500791))
    
    AND_1.Add(FlagDisabled(11505050))
    AND_1.Add(CharacterAlive(1500101))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11505052)
    Wait(5.0)
    EnableObject(1501800)
    ForceAnimation(1501800, 0)
    Wait(1.5)
    EnableMapCollision(collision=1503210)
    Wait(3.5)
    WaitForNetworkApproval(max_seconds=10.0)
    if FlagDisabled(11505210):
        EnableFlag(11505220)
        Restart()
    if FlagDisabled(11505211):
        EnableFlag(11505221)
        Restart()
    if FlagDisabled(11505212):
        EnableFlag(11505222)
        Restart()
    if FlagDisabled(11505213):
        EnableFlag(11505223)
    Restart()


@RestartOnRest(11500791)
def Event_11500791():
    """Event 11500791"""
    if ThisEventFlagEnabled():
        DisableCharacter(1500110)
        End()
    DisableAI(1500110)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502110))
    
    EnableFlag(11500791)
    EnableObject(1501800)
    ForceAnimation(1500110, 500, wait_for_completion=True)
    ForceAnimation(1500110, 603, wait_for_completion=True)
    EnableAI(1500110)
    CreateHazard(
        obj_flag=11505200,
        obj=1501800,
        dummy_id=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(1501800, 12, wait_for_completion=True)
    DisableObject(1501800)


@ContinueOnRest(11500795)
def Event_11500795():
    """Event 11500795"""
    MAIN.Await(FlagEnabled(11505220))
    
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(1501800)
    EnableObject(1501804)
    if FlagEnabled(11500812):
        Event_11500700(0, obj_flag=11505200, obj=1501804, animation_id=1, life=2.5, entity=1501812, flag=11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(10, obj_flag=11505200, obj=1501804, animation_id=2, life=7.5, entity=1501813, flag=11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(20, obj_flag=11505200, obj=1501804, animation_id=3, life=7.5, entity=1501810, flag=11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(30, obj_flag=11505200, obj=1501804, animation_id=4, life=12.5, entity=1501811, flag=11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505200,
            obj=1501801,
            animation_id=5,
            collision=1503200,
            entity=1501811,
            flag=11505210,
            flag_1=11500821,
            obj_1=1501804,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505200,
            obj=1501802,
            animation_id=6,
            collision=1503201,
            entity=1501811,
            flag=11505210,
            flag_1=11500822,
            obj_1=1501804,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505200,
            obj=1501803,
            animation_id=7,
            collision=1503202,
            entity=1501811,
            flag=11505210,
            flag_1=11500823,
            obj_1=1501804,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    Event_11500700(40, obj_flag=11505200, obj=1501804, animation_id=8, life=18.5, entity=1501811, flag=11505210)
    
    MAIN.Await(FlagDisabled(11505210))
    
    Restart()


@ContinueOnRest(11500796)
def Event_11500796():
    """Event 11500796"""
    MAIN.Await(FlagEnabled(11505221))
    
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(1501800)
    EnableObject(1501805)
    if FlagEnabled(11500812):
        Event_11500700(1, obj_flag=11505201, obj=1501805, animation_id=1, life=2.5, entity=1501812, flag=11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(11, obj_flag=11505201, obj=1501805, animation_id=2, life=7.5, entity=1501813, flag=11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(21, obj_flag=11505201, obj=1501805, animation_id=3, life=7.5, entity=1501810, flag=11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(31, obj_flag=11505201, obj=1501805, animation_id=4, life=12.5, entity=1501811, flag=11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505201,
            obj=1501801,
            animation_id=5,
            collision=1503200,
            entity=1501811,
            flag=11505211,
            flag_1=11500821,
            obj_1=1501805,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505201,
            obj=1501802,
            animation_id=6,
            collision=1503201,
            entity=1501811,
            flag=11505211,
            flag_1=11500822,
            obj_1=1501805,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505201,
            obj=1501803,
            animation_id=7,
            collision=1503202,
            entity=1501811,
            flag=11505211,
            flag_1=11500823,
            obj_1=1501805,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    Event_11500700(41, obj_flag=11505201, obj=1501805, animation_id=8, life=18.5, entity=1501811, flag=11505211)
    
    MAIN.Await(FlagDisabled(11505211))
    
    Restart()


@ContinueOnRest(11500797)
def Event_11500797():
    """Event 11500797"""
    MAIN.Await(FlagEnabled(11505222))
    
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(1501800)
    EnableObject(1501806)
    if FlagEnabled(11500812):
        Event_11500700(2, obj_flag=11505202, obj=1501806, animation_id=1, life=2.5, entity=1501812, flag=11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(12, obj_flag=11505202, obj=1501806, animation_id=2, life=7.5, entity=1501813, flag=11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(22, obj_flag=11505202, obj=1501806, animation_id=3, life=7.5, entity=1501810, flag=11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(32, obj_flag=11505202, obj=1501806, animation_id=4, life=12.5, entity=1501811, flag=11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505202,
            obj=1501801,
            animation_id=5,
            collision=1503200,
            entity=1501811,
            flag=11505212,
            flag_1=11500821,
            obj_1=1501806,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505202,
            obj=1501802,
            animation_id=6,
            collision=1503201,
            entity=1501811,
            flag=11505212,
            flag_1=11500822,
            obj_1=1501806,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505202,
            obj=1501803,
            animation_id=7,
            collision=1503202,
            entity=1501811,
            flag=11505212,
            flag_1=11500823,
            obj_1=1501806,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    Event_11500700(42, obj_flag=11505202, obj=1501806, animation_id=8, life=18.5, entity=1501811, flag=11505212)
    
    MAIN.Await(FlagDisabled(11505212))
    
    Restart()


@ContinueOnRest(11500798)
def Event_11500798():
    """Event 11500798"""
    MAIN.Await(FlagEnabled(11505223))
    
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(1501800)
    EnableObject(1501807)
    if FlagEnabled(11500812):
        Event_11500700(3, obj_flag=11505203, obj=1501807, animation_id=1, life=2.5, entity=1501812, flag=11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(13, obj_flag=11505203, obj=1501807, animation_id=2, life=7.5, entity=1501813, flag=11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(23, obj_flag=11505203, obj=1501807, animation_id=3, life=7.5, entity=1501810, flag=11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(33, obj_flag=11505203, obj=1501807, animation_id=4, life=12.5, entity=1501811, flag=11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505203,
            obj=1501801,
            animation_id=5,
            collision=1503200,
            entity=1501811,
            flag=11505213,
            flag_1=11500821,
            obj_1=1501807,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505203,
            obj=1501802,
            animation_id=6,
            collision=1503201,
            entity=1501811,
            flag=11505213,
            flag_1=11500822,
            obj_1=1501807,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505203,
            obj=1501803,
            animation_id=7,
            collision=1503202,
            entity=1501811,
            flag=11505213,
            flag_1=11500823,
            obj_1=1501807,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    Event_11500700(43, obj_flag=11505203, obj=1501807, animation_id=8, life=18.5, entity=1501811, flag=11505213)
    
    MAIN.Await(FlagDisabled(11505213))
    
    Restart()


@ContinueOnRest(11500700)
def Event_11500700(_, obj_flag: int, obj: int, animation_id: int, life: float, entity: int, flag: int):
    """Event 11500700"""
    DisableMapCollision(collision=1503210)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=life,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableFlag(flag)


@ContinueOnRest(11500750)
def Event_11500750(
    _,
    obj_flag: int,
    obj: int,
    animation_id: int,
    collision: int,
    entity: int,
    flag: int,
    flag_1: int,
    obj_1: int,
):
    """Event 11500750"""
    DisableMapCollision(collision=1503210)
    EnableFlag(flag_1)
    EnableObject(obj)
    DisableObject(obj_1)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=12.5,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    EnableMapCollision(collision=collision)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)


@ContinueOnRest(11500830)
def Event_11500830():
    """Event 11500830"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502810))
    
    EnableFlag(11500830)


@ContinueOnRest(11500831)
def Event_11500831():
    """Event 11500831"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11500751))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502811))
    AND_2.Add(FlagEnabled(11500752))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502812))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    Kill(PLAYER)


@ContinueOnRest(11500850)
def Event_11500850():
    """Event 11500850"""
    DisableFlag(11505250)
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfLastConditionResultFalse(23, input_condition=AND_1)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, dummy_id=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(1501790, 3, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500812)
        ForceAnimation(1501790, 2, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(1501790, 1, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500806)
        ForceAnimation(1501790, 0, wait_for_completion=True)
        Restart()
    RestartIfLastConditionResultFalse(input_condition=AND_2)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(1501790, 5, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500812)
        ForceAnimation(1501790, 4, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(1501790, 7, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500806)
        ForceAnimation(1501790, 6, wait_for_completion=True)
        Restart()
    EnableFlag(11500802)
    Restart()


@ContinueOnRest(11505255)
def Event_11505255():
    """Event 11505255"""
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(FlagDisabled(11505251))
    AND_1.Add(FlagDisabled(11500809))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502800))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(FlagDisabled(11505252))
    AND_2.Add(FlagEnabled(11500803))
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502801))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    SkipLinesIfLastConditionResultTrue(19, input_condition=AND_2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    if FlagDisabled(11500803):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        EnableFlag(11500803)
        EnableFlag(11500809)
        ForceAnimation(1501790, 0, wait_for_completion=True)
        ForceAnimation(1501790, 1, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(1501790, 1, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(1501790, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    if FlagEnabled(11500809):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        DisableFlag(11500809)
        DisableFlag(11500803)
        ForceAnimation(1501790, 6, wait_for_completion=True)
        ForceAnimation(1501790, 7, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(1501790, 7, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(1501790, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


@ContinueOnRest(11500840)
def Event_11500840():
    """Event 11500840"""
    MAIN.Await(FlagEnabled(11505240))
    
    EnableFlag(11505240)
    
    MAIN.Await(FlagDisabled(11505240))
    
    Restart()


@ContinueOnRest(11500841)
def Event_11500841(_, flag: int):
    """Event 11500841"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11505240))
    AND_1.Add(FlagDisabled(flag))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11505240))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11505240)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    DisableFlag(flag)
    SkipLines(1)
    EnableFlag(flag)
    Restart()


@ContinueOnRest(11500835)
def Event_11500835():
    """Event 11500835"""
    if Host():
        return
    WaitFrames(frames=10)
    EnableFlag(11505360)
    AND_1.Add(FlagEnabled(11505250))
    AND_2.Add(FlagDisabled(11505250))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    Wait(3.0)
    if FlagDisabled(11500803):
        EndOfAnimation(obj=1501790, animation_id=3)
    if FlagEnabled(11500806):
        EndOfAnimation(obj=1501790, animation_id=0)
    if FlagEnabled(11500809):
        EndOfAnimation(obj=1501790, animation_id=1)
    if FlagEnabled(11500812):
        EndOfAnimation(obj=1501790, animation_id=2)


@ContinueOnRest(11500100)
def Event_11500100():
    """Event 11500100"""
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502060))
    AND_2.Add(ThisEventFlagEnabled())
    AND_2.Add(FlagDisabled(11500101))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502061))
    AND_3.Add(ThisEventFlagEnabled())
    AND_3.Add(FlagDisabled(11500101))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1502062))
    AND_4.Add(ThisEventFlagEnabled())
    AND_4.Add(FlagEnabled(11500101))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1502060))
    AND_5.Add(ThisEventFlagEnabled())
    AND_5.Add(FlagEnabled(11500101))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1502063))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Disable)
    SkipLinesIfLastConditionResultFalse(16, input_condition=AND_1)
    EnableFlag(11500100)
    ForceAnimation(1501011, 0, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.DropAdjacent)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1502062))
    
    Restart()
    SkipLinesIfLastConditionResultTrue(27, input_condition=AND_4)
    SkipLinesIfLastConditionResultTrue(26, input_condition=AND_5)
    EnableFlag(11500101)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.DropAdjacent)
    ForceAnimation(1501011, 1, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Drop)
    AND_6.Add(AllPlayersOutsideRegion(region=1502060))
    AND_6.Add(AllPlayersOutsideRegion(region=1502063))
    
    MAIN.Await(AND_6)
    
    Restart()
    DisableFlag(11500101)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Drop)
    DisableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.DropAdjacent)
    DisableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Drop)
    ForceAnimation(1501011, 2, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Disable)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Disable)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.DropAdjacent)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Drop)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.DropAdjacent)
    AND_7.Add(AllPlayersOutsideRegion(region=1502061))
    AND_7.Add(AllPlayersOutsideRegion(region=1502062))
    
    MAIN.Await(AND_7)
    
    Restart()


@ContinueOnRest(11500102)
def Event_11500102():
    """Event 11500102"""
    SkipLinesIfThisEventFlagDisabled(4)
    SkipLinesIfFlagEnabled(1, 11500100)
    EndOfAnimation(obj=1501011, animation_id=20)
    End()
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(PlayerHasGood(2003))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        dummy_id=105,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1501011, destination_type=CoordEntityType.Object, dummy_id=120, short_move=True)
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(1501011, 10)
    if Client():
        return
    DisplayDialog(text=10010862, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11500103)
def Event_11500103():
    """Event 11500103"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11500102))
    AND_1.Add(PlayerDoesNotHaveGood(2003))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        dummy_id=105,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010163, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11500106)
def Event_11500106():
    """Event 11500106"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11500105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1501001)
    Restart()


@ContinueOnRest(11500107)
def Event_11500107():
    """Event 11500107"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1501001, animation_id=0)
        End()
    AND_1.Add(FlagDisabled(11500105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11500105)
    Move(PLAYER, destination=1501001, destination_type=CoordEntityType.Object, dummy_id=120, short_move=True)
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(1501001, 0)


@ContinueOnRest(11500110)
def Event_11500110(_, obj: int, obj_act_id: int):
    """Event 11500110"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    AND_1.Add(PlayerHasGood(2003))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=10010883, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=10010862, anchor_entity=obj, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11505270)
def Event_11505270(_, region: int, obj: int, vfx_id: int, source_entity: int, launch_angle_y: int, left: int):
    """Event 11505270"""
    SkipLinesIfFlagDisabled(2, left)
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLines(12)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(ObjectDamaged(obj, attacker=-1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(left)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=obj, dummy_id=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id, erase_root_only=False)
    ForceAnimation(obj, 0, wait_for_completion=True)
    if ValueNotEqual(left=left, right=11505284):
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            dummy_id=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            dummy_id=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            dummy_id=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(11505280, 11505285)) >= 2)
    
    DisableFlag(left)
    ForceAnimation(obj, 1, wait_for_completion=True)
    Restart()


@ContinueOnRest(11505260)
def Event_11505260():
    """Event 11505260"""
    MAIN.Await(FlagEnabled(11505284))
    
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        dummy_id=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    
    MAIN.Await(FlagDisabled(11505284))
    
    Restart()


@RestartOnRest(11505050)
def Event_11505050():
    """Event 11505050"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1500101)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1502101))
    OR_1.Add(Attacked(attacked_entity=1500101, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11505050)
    
    MAIN.Await(FlagDisabled(11505052))
    
    EnableAI(1500101)


@RestartOnRest(11505051)
def Event_11505051():
    """Event 11505051"""
    AND_1.Add(FlagEnabled(11505050))
    AND_2.Add(FlagEnabled(11505052))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_1)
    Move(1500101, destination=1502100, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1500101, 9001, wait_for_completion=True)
    DisableFlag(11505052)
    Restart()


@RestartOnRest(11505055)
def Event_11505055():
    """Event 11505055"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1500100, authority_level=UpdateAuthority.Forced)
    AND_1.Add(ObjectDestroyed(1501100))
    AND_1.Add(ObjectDestroyed(1501101))
    AND_1.Add(ObjectDestroyed(1501102))
    AND_1.Add(ObjectDestroyed(1501103))
    AND_1.Add(ObjectDestroyed(1501104))
    AND_1.Add(ObjectDestroyed(1501105))
    AND_1.Add(ObjectDestroyed(1501106))
    AND_1.Add(ObjectDestroyed(1501107))
    AND_1.Add(ObjectDestroyed(1501108))
    
    MAIN.Await(AND_1)
    
    AICommand(1500100, command_id=20, command_slot=1)
    ReplanAI(1500100)


@ContinueOnRest(11505110)
def Event_11505110():
    """Event 11505110"""
    AND_1.Add(FlagEnabled(11505100))
    AND_2.Add(FlagEnabled(11505100))
    AND_3.Add(FlagEnabled(11505100))
    AND_4.Add(FlagEnabled(11505100))
    AND_5.Add(FlagEnabled(11505100))
    AND_6.Add(FlagEnabled(11505100))
    AND_7.Add(FlagEnabled(11505100))
    AND_1.Add(FlagEnabled(11505111))
    AND_2.Add(FlagEnabled(11505112))
    AND_3.Add(FlagEnabled(11505113))
    AND_4.Add(FlagEnabled(11505114))
    AND_5.Add(FlagEnabled(11505115))
    AND_6.Add(FlagEnabled(11505116))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(11505111, 11505116)))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_6)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_5)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_4)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5303,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_3)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5302,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_2)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5301,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfLastConditionResultFalse(8, input_condition=AND_1)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1500100,
        dummy_id=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()


@ContinueOnRest(11505111)
def Event_11505111(_, left: int, region: int, command_id: int):
    """Event 11505111"""
    AND_1.Add(FlagDisabled(11505100))
    AND_1.Add(FlagDisabled(11505105))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(FlagDisabled(left))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    if ValueLessThan(left=left, right=11505112):
        AND_1.Add(AllPlayersOutsideRegion(region=1502701))
    if ValueLessThan(left=left, right=11505113):
        AND_1.Add(AllPlayersOutsideRegion(region=1502702))
    if ValueLessThan(left=left, right=11505114):
        AND_1.Add(AllPlayersOutsideRegion(region=1502703))
    if ValueLessThan(left=left, right=11505115):
        AND_1.Add(AllPlayersOutsideRegion(region=1502704))
    if ValueLessThan(left=left, right=11505116):
        AND_1.Add(AllPlayersOutsideRegion(region=1502705))
    if ValueLessThan(left=left, right=11505117):
        AND_1.Add(AllPlayersOutsideRegion(region=1502710))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((11505111, 11505116))
    EnableFlag(left)
    AICommand(1500100, command_id=command_id, command_slot=2)
    Restart()


@ContinueOnRest(11505101)
def Event_11505101():
    """Event 11505101"""
    MAIN.Await(FlagEnabled(11505105))
    
    EnableFlag(11505105)
    
    MAIN.Await(FlagDisabled(11505105))
    
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@ContinueOnRest(11505102)
def Event_11505102():
    """Event 11505102"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11505105))
    
    Wait(30.0)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@RestartOnRest(11505060)
def Event_11505060(_, character: int):
    """Event 11505060"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=500))
    
    EzstateAIRequest(character, command_id=1500, command_slot=0)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(character, tae_event_id=500))
    
    Restart()


@RestartOnRest(11505070)
def Event_11505070(_, character: int):
    """Event 11505070"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=1400))
    
    Wait(10.0)
    EzstateAIRequest(character, command_id=1501, command_slot=0)
    Restart()


@RestartOnRest(11505080)
def Event_11505080():
    """Event 11505080"""
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(1500122)
        End()
    OR_1.Add(Attacked(attacked_entity=1500122, attacker=PLAYER))
    OR_1.Add(HealthRatio(1500122) != 1.0)
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1500122)
    ForceAnimation(1500122, 2000)


@RestartOnRest(11505010)
def Event_11505010():
    """Event 11505010"""
    AND_1.Add(CharacterAlive(1500010))
    AND_1.Add(CharacterBackreadEnabled(1500010))
    AND_1.Add(CharacterHasSpecialEffect(1500010, 5421))
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1500010,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        dummy_id=7,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=1500010,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=1500010,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(1500010, command_id=10, command_slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11505011)
def Event_11505011():
    """Event 11505011"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(1500010, 5420))
    AND_1.Add(Attacked(attacked_entity=1500010, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(1500010, 3150)
    RemoveSpecialEffect(1500010, 3151)
    AND_7.Add(CharacterBackreadDisabled(1500010))
    if AND_7:
        return RESTART
    AND_2.Add(CharacterHasSpecialEffect(1500010, 5421))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    AND_3.Add(CharacterHasSpecialEffect(1500010, 5422))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    AND_4.Add(CharacterHasSpecialEffect(1500010, 5423))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    AND_5.Add(CharacterHasSpecialEffect(1500010, 5424))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceAnimation(1500010, 3006, wait_for_completion=True)
    ReplanAI(1500010)
    RemoveSpecialEffect(1500010, 3150)
    RemoveSpecialEffect(1500010, 3151)
    Restart()


@RestartOnRest(11505012)
def Event_11505012():
    """Event 11505012"""
    AND_1.Add(CharacterHasSpecialEffect(1500010, 5421))
    AND_1.Add(CharacterHasSpecialEffect(1500010, 3150))
    AND_2.Add(CharacterHasSpecialEffect(1500010, 5420))
    AND_2.Add(CharacterHasSpecialEffect(1500010, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(1500010, command_id=200, command_slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=210, command_slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(1500010, 5420))
    OR_2.Add(CharacterHasSpecialEffect(1500010, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11505013)
def Event_11505013():
    """Event 11505013"""
    AND_1.Add(CharacterHasSpecialEffect(1500010, 5422))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(1500010, 3150))
    AND_2.Add(CharacterHasSpecialEffect(1500010, 5423))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(1500010, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(1500010, 3150)
    RemoveSpecialEffect(1500010, 3151)
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(1500010, command_id=201, command_slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=211, command_slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(1500010, 5420))
    OR_2.Add(CharacterHasSpecialEffect(1500010, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11505014)
def Event_11505014():
    """Event 11505014"""
    AND_1.Add(Singleplayer())
    AND_1.Add(CharacterInsideRegion(1500010, region=1502010))
    AND_1.Add(CharacterBackreadDisabled(1500010))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(1500010, 5421)
    ClearTargetList(1500010)
    ReplanAI(1500010)
    Move(1500010, destination=1502010, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterBackreadEnabled(1500010))
    
    Restart()


@RestartOnRest(11505015)
def Event_11505015():
    """Event 11505015"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(1500010))
    if AND_1:
        return
    ResetAnimation(1500010, disable_interpolation=True)
    ForceAnimation(1500010, 0)
    ReplanAI(1500010)


@RestartOnRest(11500900)
def Event_11500900():
    """Event 11500900"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(1500010)
        End()
    
    MAIN.Await(CharacterDead(1500010))
    
    End()


@ContinueOnRest(11500210)
def Event_11500210():
    """Event 11500210"""
    if Client():
        return
    
    MAIN.Await(InsideMap(game_map=SENS_FORTRESS))
    
    MAIN.Await(TimeElapsed(seconds=5.0))
    
    MAIN.Await(FlagEnabled(11))
    
    MAIN.Await(ActionButton(
        prompt_text=10010120,
        anchor_entity=1502505,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    DisableBackread(1500201)
    WaitFrames(frames=1)
    if FlagDisabled(11510400):
        PlayCutscene(150000, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    else:
        PlayCutscene(150002, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=33)
    Restart()


@RestartOnRest(11500860)
def Event_11500860(_, character: int):
    """Event 11500860"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11500600)
def Event_11500600(_, obj: int, obj_act_id: int):
    """Event 11500600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11500510)
def Event_11500510(_, character: int, flag: int):
    """Event 11500510"""
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


@ContinueOnRest(11500520)
def Event_11500520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11500530)
def Event_11500530():
    """Event 11500530"""
    if FlagDisabled(11500593):
        DisableObjectActivation(1501032, obj_act_id=-1)
    
        MAIN.Await(FlagEnabled(11500593))
    
        EnableObjectActivation(1501032, obj_act_id=-1)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11500112))
    
    DisableFlag(71500021)


@ContinueOnRest(11500531)
def Event_11500531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500531"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1090))
    AND_1.Add(FlagEnabled(11500112))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11500532)
def Event_11500532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500532"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1092))
    AND_1.Add(FlagEnabled(11500594))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11500533)
def Event_11500533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500533"""
    AND_1.Add(FlagDisabled(1114))
    AND_1.Add(FlagEnabled(1113))
    AND_1.Add(FlagEnabled(723))
    AND_1.Add(InsideMap(game_map=SENS_FORTRESS))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11500534)
def Event_11500534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500534"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1490))
    AND_1.Add(FlagEnabled(11500591))
    AND_1.Add(FlagEnabled(11500200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(character, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(character, region=1502510)
    Kill(1500120)
    Kill(1500121)


@ContinueOnRest(11500535)
def Event_11500535(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500535"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1490))
    AND_1.Add(FlagDisabled(11500591))
    AND_1.Add(FlagEnabled(11500200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(character, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(character, region=1502510)
    Kill(1500120)
    Kill(1500121)


@ContinueOnRest(11500536)
def Event_11500536(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11500536"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1491))
    AND_1.Add(FlagEnabled(11500850))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1512))
    AND_2.Add(FlagEnabled(1492))
    AND_2.Add(FlagEnabled(11500592))
    AND_2.Add(FlagEnabled(11500850))
    AND_2.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11505030)
def Event_11505030():
    """Event 11505030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6510, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11505033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11505031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6510)
    if FlagEnabled(11):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(6510))
    AND_1.Add(EntityWithinDistance(entity=6510, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6510,
        region=1502000,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


@ContinueOnRest(11505032)
def Event_11505032():
    """Event 11505032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11505031))
    AND_1.Add(FlagEnabled(11505393))
    
    MAIN.Await(AND_1)
    
    AICommand(6510, command_id=10, command_slot=0)
    ReplanAI(6510)
    
    MAIN.Await(CharacterInsideRegion(6510, region=1502998))
    
    FaceEntity(6510, target_entity=1502997)
    ForceAnimation(6510, 7410)
    AICommand(6510, command_id=-1, command_slot=0)
    ReplanAI(6510)
