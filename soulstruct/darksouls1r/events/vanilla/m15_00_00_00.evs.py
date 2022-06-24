"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
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
    DeleteVFX(vfx_id=1501995, erase_root_only=False)
    DisableMapCollision(collision=1503210)
    DisableObject(1501800)
    DisableObject(1501801)
    DisableObject(1501802)
    DisableObject(1501803)
    DisableObject(1501804)
    DisableObject(1501805)
    DisableObject(1501806)
    DisableObject(1501807)
    SkipLinesIfFlagEnabled(1, 11500803)
    EndOfAnimation(obj=1501790, animation_id=3)
    SkipLinesIfFlagDisabled(1, 11500806)
    EndOfAnimation(obj=1501790, animation_id=0)
    SkipLinesIfFlagDisabled(1, 11500809)
    EndOfAnimation(obj=1501790, animation_id=1)
    SkipLinesIfFlagDisabled(1, 11500812)
    EndOfAnimation(obj=1501790, animation_id=2)
    DisableMapCollision(collision=1503200)
    DisableMapCollision(collision=1503201)
    DisableMapCollision(collision=1503202)
    SkipLinesIfFlagDisabled(3, 11500821)
    EnableObject(1501801)
    EndOfAnimation(obj=1501801, animation_id=5)
    EnableMapCollision(collision=1503200)
    SkipLinesIfFlagDisabled(3, 11500822)
    EnableObject(1501802)
    EndOfAnimation(obj=1501802, animation_id=6)
    EnableMapCollision(collision=1503201)
    SkipLinesIfFlagDisabled(3, 11500823)
    EnableObject(1501803)
    EndOfAnimation(obj=1501803, animation_id=7)
    EnableMapCollision(collision=1503202)
    SkipLinesIfFlagDisabled(21, 11500100)
    SkipLinesIfFlagEnabled(10, 11500101)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.WallTouchingFloor)
    EndOfAnimation(obj=1501011, animation_id=12)
    SkipLines(9)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Wall)
    EndOfAnimation(obj=1501011, animation_id=11)
    SkipLines(4)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    Event_11500090(0, 1501700, 1501701, 1502600, 1502601)
    Event_11500090(1, 1501702, 1501703, 1502602, 1502603)
    Event_11505090()
    Event_11505091()
    Event_11505092()
    Event_11500201()
    Event_11505300()
    Event_11500840()
    Event_11500841(0, 11500803)
    Event_11500841(1, 11500806)
    Event_11500841(2, 11500809)
    Event_11500841(3, 11500812)
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
    Event_11500110(0, 1501030, 11500110)
    Event_11500110(1, 1501031, 11500111)
    Event_11500110(2, 1501032, 11500112)
    Event_11500110(3, 1501033, 11500113)
    Event_11500110(5, 1501035, 11500115)
    Event_11500110(6, 1501036, 11500116)
    Event_11505050()
    Event_11505051()
    Event_11505055()
    Event_11505110()
    Event_11505101()
    Event_11505102()
    Event_11505111(0, 11505111, 1502700, 1)
    Event_11505111(1, 11505112, 1502701, 2)
    Event_11505111(2, 11505113, 1502702, 3)
    Event_11505111(3, 11505114, 1502703, 4)
    Event_11505111(4, 11505115, 1502704, 5)
    Event_11505111(5, 11505116, 1502705, 6)
    Event_11505111(6, 11505117, 1502710, -1)
    Event_11505060(0, 1500100)
    Event_11505060(1, 1500101)
    Event_11505060(2, 1500102)
    Event_11505070(0, 1500100)
    Event_11505070(1, 1500101)
    Event_11505070(2, 1500102)
    Event_11505080()
    Event_11500210()
    Event_11500835()
    DisableSoundEvent(sound_id=1503800)
    SkipLinesIfFlagDisabled(4, 11)
    Event_11505392()
    DisableObject(1501990)
    DeleteVFX(vfx_id=1501991, erase_root_only=False)
    SkipLines(9)
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
    Event_11505270(0, 1502200, 1501200, 1503500, 1501210, 0, 11505280)
    Event_11505270(1, 1502201, 1501201, 1503500, 1501211, 90, 11505281)
    Event_11505270(2, 1502202, 1501202, 1503500, 1501212, 90, 11505282)
    Event_11505270(3, 1502203, 1501203, 1503500, 1501213, 270, 11505283)
    Event_11505270(4, 1502204, 1501204, 1503500, 1501214, 180, 11505284)
    Event_11505270(5, 1502205, 1501205, 1503500, 1501213, 270, 11505285)
    Event_11505260()
    Event_11500860(0, 6600)
    Event_11500860(1, 1500300)
    Event_11500860(2, 1500301)
    Event_11500860(3, 1500302)
    Event_11500860(4, 1500303)
    Event_11500860(5, 1500100)
    Event_11500860(7, 1500102)
    Event_11500600(0, 1501650, 11500600)
    Event_11500600(2, 1501652, 11500602)
    Event_11500600(4, 1501654, 11500604)
    Event_11500600(9, 1501659, 11500609)
    Event_11500600(10, 1501660, 11500610)
    Event_11505843(0, 11, 1501990, 1502998, 1502997)
    Event_11505846(0, 11, 1501990, 1501991)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6600, event_flag=8980)
    HumanityRegistration(6510, event_flag=8924)
    Event_11505030()
    Event_11505029()
    Event_11505032()
    Event_11505990(0, 11505031, 6510)
    HumanityRegistration(6030, event_flag=8334)
    SkipLinesIfFlagEnabled(3, 1090)
    SkipLinesIfFlagEnabled(2, 1091)
    SkipLinesIfFlagEnabled(1, 1096)
    DisableCharacter(6030)
    Event_11500510(0, 6030, 1096)
    Event_11500520(0, 6030, 1090, 1109, 1097)
    Event_11500530()
    Event_11500531(0, 6030, 1090, 1109, 1091)
    Event_11500532(0, 6030, 1090, 1109, 1092)
    SetTeamTypeAndExitStandbyAnimation(6043, team_type=TeamType.HostileAlly)
    SkipLinesIfFlagEnabled(1, 1117)
    DisableCharacter(6043)
    Event_11500520(1, 6043, 1110, 1119, 1115)
    Event_11500533(0, 6043, 1110, 1119, 1117)
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
    Event_11500510(2, 6280, 1512)
    Event_11500520(2, 6280, 1490, 1539, 1513)
    Event_11500534(0, 6280, 1490, 1539, 1491)
    Event_11500535(0, 6280, 1490, 1539, 1492)
    Event_11500536(0, 6280, 1490, 1539, 1493)
    HumanityRegistration(6250, event_flag=8422)
    SkipLinesIfFlagRangeAnyEnabled(1, (1420, 1429))
    EnableFlag(1420)
    Event_11500510(3, 6250, 1421)
    Event_11500520(3, 6250, 1420, 1429, 1422)


@NeverRestart(1000000000)
def Event_1000000000():
    """Event 1000000000"""
    DisableCharacter(1500200)
    SetNetworkUpdateRate(1500100, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@NeverRestart(11500090)
def Event_11500090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500090"""
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


@RestartOnRest(11505090)
def Event_11505090():
    """Event 11505090"""
    EndIfThisEventFlagEnabled()
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
    IfFlagEnabled(0, 11500050)
    EndIfFlagEnabled(735)
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
    IfFlagEnabled(-1, 11505095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
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
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11500050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=SENS_FORTRESS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11500050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=SENS_FORTRESS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11500050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=SENS_FORTRESS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11500050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=SENS_FORTRESS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11500050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=SENS_FORTRESS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11500050)
    RestartIfConditionFalse(-6)
    EnableFlag(11500050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=SENS_FORTRESS)
    RestartIfConditionFalse(7)
    DisableFlag(11500050)
    EnableFlag(11505095)


@NeverRestart(11505300)
def Event_11505300():
    """Event 11505300"""
    CreateHazard(
        obj_flag=11505301,
        obj=1501850,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505302,
        obj=1501851,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505303,
        obj=1501852,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505304,
        obj=1501853,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505305,
        obj=1501854,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505306,
        obj=1501855,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505307,
        obj=1501856,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505308,
        obj=1501857,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505309,
        obj=1501858,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505310,
        obj=1501859,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505311,
        obj=1501860,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505312,
        obj=1501861,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505313,
        obj=1501862,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505314,
        obj=1501863,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505315,
        obj=1501864,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505316,
        obj=1501865,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505317,
        obj=1501866,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505290,
        obj=1501010,
        model_point=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


@NeverRestart(11505390)
def Event_11505390():
    """Event 11505390"""
    IfFlagDisabled(1, 11)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1501990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11505391)
def Event_11505391():
    """Event 11505391"""
    IfFlagDisabled(1, 11)
    IfFlagEnabled(1, 11505393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1501990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11505393)
def Event_11505393():
    """Event 11505393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1500800)


@RestartOnRest(11505392)
def Event_11505392():
    """Event 11505392"""
    SkipLinesIfFlagDisabled(7, 11)
    DisableCharacter(1500800)
    DropMandatoryTreasure(1500800)
    DisableBackread(1500800)
    IfCharacterBackreadEnabled(0, 1500100)
    AICommand(1500100, command_id=10, slot=0)
    ReplanAI(1500100)
    End()
    DisableAI(1500800)
    SetStandbyAnimationSettings(1500800, standby_animation=9000)
    Event_11505351()
    Event_11505352()
    IfFlagEnabled(1, 11505393)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1500800)
    SetStandbyAnimationSettings(1500800, cancel_animation=9060)
    EnableBossHealthBar(1500800, name=2320)


@NeverRestart(11500001)
def Event_11500001():
    """Event 11500001"""
    DeleteVFX(vfx_id=1503010, erase_root_only=False)
    IfCharacterDead(0, 1500800)
    EnableFlag(11)
    KillBoss(game_area_param_id=1500800)
    DisableObject(1501990)
    DeleteVFX(vfx_id=1501991)
    CreateVFX(vfx_id=1503010)
    AICommand(1500100, command_id=10, slot=0)
    ReplanAI(1500100)
    DisableFlag(11807020)
    DisableFlag(11807030)
    DisableFlag(11807040)
    DisableFlag(11807050)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(1500800)
    DisableBackread(1500800)


@NeverRestart(11505394)
def Event_11505394():
    """Event 11505394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11)
    IfFlagEnabled(1, 11505392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11505391)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfCharacterAlive(1, 1500800)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1503800)


@NeverRestart(11505395)
def Event_11505395():
    """Event 11505395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11)
    IfFlagEnabled(1, 11505394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1503800)
    PlaySoundEffect(1502990, 150100002, sound_type=SoundType.a_Ambient)


@NeverRestart(11505350)
def Event_11505350():
    """Event 11505350"""
    EndIfClient()
    IfCharacterHasTAEEvent(0, 1500800, tae_event_id=100)
    IfCharacterDead(0, 1500800)


@UnknownRestart(11505351)
def Event_11505351():
    """Event 11505351"""
    EndIfFlagEnabled(11)
    EnableNetworkSync()
    IfFlagDisabled(0, 11505355)
    CreateNPCPart(1500800, npc_part_id=2320, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(1500800, npc_part_id=2320, material_sfx_id=56, material_vfx_id=56)
    IfCharacterPartHealthComparison(0, 1500800, npc_part_id=2320, comparison_type=ComparisonType.Equal, value=5)
    EzstateAIRequest(1500800, command_id=1300, slot=0)
    IfCharacterHasTAEEvent(0, 1500800, tae_event_id=1204)
    EnableFlag(11505355)
    CreateNPCPart(1500800, npc_part_id=2321, part_index=NPCPartType.Part2, part_health=100)
    SetNPCPartEffects(1500800, npc_part_id=2321, material_sfx_id=56, material_vfx_id=56)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    DisableFlag(11505355)
    RestartEvent(event_id=11505352)
    SetNPCPartHealth(1500800, npc_part_id=2321, desired_health=-1, overwrite_max=False)
    EzstateAIRequest(1500800, command_id=1303, slot=0)
    Restart()


@UnknownRestart(11505352)
def Event_11505352():
    """Event 11505352"""
    EndIfFlagEnabled(11)
    EnableNetworkSync()
    IfFlagEnabled(0, 11505355)
    IfFlagEnabled(1, 11505355)
    IfCharacterPartHealthComparison(1, 1500800, npc_part_id=2321, comparison_type=ComparisonType.Equal, value=5)
    IfConditionTrue(0, input_condition=1)
    RestartEvent(event_id=11505351)
    EzstateAIRequest(1500800, command_id=1301, slot=0)
    IfCharacterHasTAEEvent(0, 1500800, tae_event_id=1203)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    EzstateAIRequest(1500800, command_id=1304, slot=0)
    DisableFlag(11505355)
    Restart()


@NeverRestart(11505353)
def Event_11505353():
    """Event 11505353"""
    IfCharacterHasTAEEvent(1, 1500800, tae_event_id=400)
    IfCharacterHasTAEEvent(2, 1500800, tae_event_id=300)
    IfHealthLessThanOrEqual(3, 1500800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=1)
    DisableMapCollision(collision=1503000)
    SkipLines(1)
    EnableMapCollision(collision=1503000)
    EndIfFinishedConditionTrue(input_condition=3)
    IfCharacterDoesNotHaveTAEEvent(4, 1500800, tae_event_id=400)
    IfCharacterDoesNotHaveTAEEvent(4, 1500800, tae_event_id=300)
    IfConditionTrue(0, input_condition=4)
    Restart()


@NeverRestart(11500201)
def Event_11500201():
    """Event 11500201"""
    SkipLinesIfFlagDisabled(1, 11500200)
    EndOfAnimation(obj=1501000, animation_id=0)
    IfCharacterInsideRegion(0, PLAYER, region=1502050)
    IfCharacterOutsideRegion(0, PLAYER, region=1502050)
    Restart()


@NeverRestart(11500790)
def Event_11500790():
    """Event 11500790"""
    IfFlagEnabled(0, 11500791)
    IfFlagDisabled(1, 11505050)
    IfCharacterAlive(1, 1500101)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11505052)
    Wait(5.0)
    EnableObject(1501800)
    ForceAnimation(1501800, 0)
    Wait(1.5)
    EnableMapCollision(collision=1503210)
    Wait(3.5)
    WaitForNetworkApproval(max_seconds=10.0)
    SkipLinesIfFlagEnabled(2, 11505210)
    EnableFlag(11505220)
    Restart()
    SkipLinesIfFlagEnabled(2, 11505211)
    EnableFlag(11505221)
    Restart()
    SkipLinesIfFlagEnabled(2, 11505212)
    EnableFlag(11505222)
    Restart()
    SkipLinesIfFlagEnabled(1, 11505213)
    EnableFlag(11505223)
    Restart()


@RestartOnRest(11500791)
def Event_11500791():
    """Event 11500791"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1500110)
    End()
    DisableAI(1500110)
    IfCharacterInsideRegion(0, PLAYER, region=1502110)
    EnableFlag(11500791)
    EnableObject(1501800)
    ForceAnimation(1500110, 500, wait_for_completion=True)
    ForceAnimation(1500110, 603, wait_for_completion=True)
    EnableAI(1500110)
    CreateHazard(
        obj_flag=11505200,
        obj=1501800,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(1501800, 12, wait_for_completion=True)
    DisableObject(1501800)


@NeverRestart(11500795)
def Event_11500795():
    """Event 11500795"""
    IfFlagEnabled(0, 11505220)
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(1501800)
    EnableObject(1501804)
    SkipLinesIfFlagDisabled(3, 11500812)
    Event_11500700(0, 11505200, 1501804, 1, 2.5, 1501812, 11505210)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500803)
    Event_11500700(10, 11505200, 1501804, 2, 7.5, 1501813, 11505210)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagDisabled(3, 11500806)
    Event_11500700(20, 11505200, 1501804, 3, 7.5, 1501810, 11505210)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500830)
    Event_11500700(30, 11505200, 1501804, 4, 12.5, 1501811, 11505210)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500821)
    Event_11500750(0, 11505200, 1501801, 5, 1503200, 1501811, 11505210, 11500821, 1501804)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500822)
    Event_11500750(1, 11505200, 1501802, 6, 1503201, 1501811, 11505210, 11500822, 1501804)
    IfFlagDisabled(0, 11505210)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500823)
    Event_11500750(2, 11505200, 1501803, 7, 1503202, 1501811, 11505210, 11500823, 1501804)
    IfFlagDisabled(0, 11505210)
    Restart()
    Event_11500700(40, 11505200, 1501804, 8, 18.5, 1501811, 11505210)
    IfFlagDisabled(0, 11505210)
    Restart()


@NeverRestart(11500796)
def Event_11500796():
    """Event 11500796"""
    IfFlagEnabled(0, 11505221)
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(1501800)
    EnableObject(1501805)
    SkipLinesIfFlagDisabled(3, 11500812)
    Event_11500700(1, 11505201, 1501805, 1, 2.5, 1501812, 11505211)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500803)
    Event_11500700(11, 11505201, 1501805, 2, 7.5, 1501813, 11505211)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagDisabled(3, 11500806)
    Event_11500700(21, 11505201, 1501805, 3, 7.5, 1501810, 11505211)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500830)
    Event_11500700(31, 11505201, 1501805, 4, 12.5, 1501811, 11505211)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500821)
    Event_11500750(0, 11505201, 1501801, 5, 1503200, 1501811, 11505211, 11500821, 1501805)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500822)
    Event_11500750(1, 11505201, 1501802, 6, 1503201, 1501811, 11505211, 11500822, 1501805)
    IfFlagDisabled(0, 11505211)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500823)
    Event_11500750(2, 11505201, 1501803, 7, 1503202, 1501811, 11505211, 11500823, 1501805)
    IfFlagDisabled(0, 11505211)
    Restart()
    Event_11500700(41, 11505201, 1501805, 8, 18.5, 1501811, 11505211)
    IfFlagDisabled(0, 11505211)
    Restart()


@NeverRestart(11500797)
def Event_11500797():
    """Event 11500797"""
    IfFlagEnabled(0, 11505222)
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(1501800)
    EnableObject(1501806)
    SkipLinesIfFlagDisabled(3, 11500812)
    Event_11500700(2, 11505202, 1501806, 1, 2.5, 1501812, 11505212)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500803)
    Event_11500700(12, 11505202, 1501806, 2, 7.5, 1501813, 11505212)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagDisabled(3, 11500806)
    Event_11500700(22, 11505202, 1501806, 3, 7.5, 1501810, 11505212)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500830)
    Event_11500700(32, 11505202, 1501806, 4, 12.5, 1501811, 11505212)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500821)
    Event_11500750(0, 11505202, 1501801, 5, 1503200, 1501811, 11505212, 11500821, 1501806)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500822)
    Event_11500750(1, 11505202, 1501802, 6, 1503201, 1501811, 11505212, 11500822, 1501806)
    IfFlagDisabled(0, 11505212)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500823)
    Event_11500750(2, 11505202, 1501803, 7, 1503202, 1501811, 11505212, 11500823, 1501806)
    IfFlagDisabled(0, 11505212)
    Restart()
    Event_11500700(42, 11505202, 1501806, 8, 18.5, 1501811, 11505212)
    IfFlagDisabled(0, 11505212)
    Restart()


@NeverRestart(11500798)
def Event_11500798():
    """Event 11500798"""
    IfFlagEnabled(0, 11505223)
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(1501800)
    EnableObject(1501807)
    SkipLinesIfFlagDisabled(3, 11500812)
    Event_11500700(3, 11505203, 1501807, 1, 2.5, 1501812, 11505213)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500803)
    Event_11500700(13, 11505203, 1501807, 2, 7.5, 1501813, 11505213)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagDisabled(3, 11500806)
    Event_11500700(23, 11505203, 1501807, 3, 7.5, 1501810, 11505213)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500830)
    Event_11500700(33, 11505203, 1501807, 4, 12.5, 1501811, 11505213)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500821)
    Event_11500750(0, 11505203, 1501801, 5, 1503200, 1501811, 11505213, 11500821, 1501807)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500822)
    Event_11500750(1, 11505203, 1501802, 6, 1503201, 1501811, 11505213, 11500822, 1501807)
    IfFlagDisabled(0, 11505213)
    Restart()
    SkipLinesIfFlagEnabled(3, 11500823)
    Event_11500750(2, 11505203, 1501803, 7, 1503202, 1501811, 11505213, 11500823, 1501807)
    IfFlagDisabled(0, 11505213)
    Restart()
    Event_11500700(43, 11505203, 1501807, 8, 18.5, 1501811, 11505213)
    IfFlagDisabled(0, 11505213)
    Restart()


@NeverRestart(11500700)
def Event_11500700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """Event 11500700"""
    DisableMapCollision(collision=1503210)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        obj_flag=arg_0_3,
        obj=arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=arg_12_15,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    RemoveObjectFlag(obj_flag=arg_0_3)
    DisableObject(arg_4_7)
    EndOfAnimation(obj=arg_4_7, animation_id=0)
    DisableFlag(arg_20_23)


@NeverRestart(11500750)
def Event_11500750(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """Event 11500750"""
    DisableMapCollision(collision=1503210)
    EnableFlag(arg_24_27)
    EnableObject(arg_4_7)
    DisableObject(arg_28_31)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        obj_flag=arg_0_3,
        obj=arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=12.5,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableMapCollision(collision=arg_12_15)
    RemoveObjectFlag(obj_flag=arg_0_3)
    DisableFlag(arg_20_23)


@NeverRestart(11500830)
def Event_11500830():
    """Event 11500830"""
    IfCharacterInsideRegion(0, PLAYER, region=1502810)
    EnableFlag(11500830)


@NeverRestart(11500831)
def Event_11500831():
    """Event 11500831"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11500751)
    IfCharacterInsideRegion(1, PLAYER, region=1502811)
    IfFlagEnabled(2, 11500752)
    IfCharacterInsideRegion(2, PLAYER, region=1502812)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Kill(PLAYER)


@NeverRestart(11500850)
def Event_11500850():
    """Event 11500850"""
    DisableFlag(11505250)
    IfFlagDisabled(1, 11505250)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(2, 11505250)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFinishedConditionFalse(23, condition=1)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    SkipLinesIfFlagDisabled(4, 11500812)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(1501790, 3, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagDisabled(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500812)
    ForceAnimation(1501790, 2, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagDisabled(4, 11500806)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagEnabled(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500806)
    ForceAnimation(1501790, 0, wait_for_completion=True)
    Restart()
    RestartIfFinishedConditionFalse(input_condition=2)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    SkipLinesIfFlagDisabled(4, 11500812)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(1501790, 5, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagEnabled(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500812)
    ForceAnimation(1501790, 4, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagDisabled(4, 11500806)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagDisabled(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500806)
    ForceAnimation(1501790, 6, wait_for_completion=True)
    Restart()
    EnableFlag(11500802)
    Restart()


@NeverRestart(11505255)
def Event_11505255():
    """Event 11505255"""
    IfFlagDisabled(1, 11505250)
    IfFlagDisabled(1, 11505251)
    IfFlagDisabled(1, 11500809)
    IfTimeElapsed(1, seconds=2.0)
    IfCharacterInsideRegion(1, PLAYER, region=1502800)
    IfFlagDisabled(2, 11505250)
    IfFlagDisabled(2, 11505252)
    IfFlagEnabled(2, 11500803)
    IfTimeElapsed(2, seconds=2.0)
    IfCharacterInsideRegion(2, PLAYER, region=1502801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    SkipLinesIfFinishedConditionTrue(19, condition=2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFlagEnabled(5, 11500803)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    EnableFlag(11500803)
    EnableFlag(11500809)
    ForceAnimation(1501790, 0, wait_for_completion=True)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    SkipLinesIfFlagDisabled(4, 11500806)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    SkipLinesIfFlagDisabled(4, 11500812)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(1501790, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    SkipLinesIfFlagDisabled(5, 11500809)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    DisableFlag(11500809)
    DisableFlag(11500803)
    ForceAnimation(1501790, 6, wait_for_completion=True)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    SkipLinesIfFlagDisabled(4, 11500806)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    SkipLinesIfFlagDisabled(4, 11500812)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(1501790, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


@NeverRestart(11500840)
def Event_11500840():
    """Event 11500840"""
    IfFlagEnabled(0, 11505240)
    EnableFlag(11505240)
    IfFlagDisabled(0, 11505240)
    Restart()


@NeverRestart(11500841)
def Event_11500841(_, arg_0_3: int):
    """Event 11500841"""
    IfHost(1)
    IfFlagEnabled(1, 11505240)
    IfFlagDisabled(1, arg_0_3)
    IfHost(2)
    IfFlagEnabled(2, 11505240)
    IfFlagEnabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11505240)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisableFlag(arg_0_3)
    SkipLines(1)
    EnableFlag(arg_0_3)
    Restart()


@NeverRestart(11500835)
def Event_11500835():
    """Event 11500835"""
    EndIfHost()
    WaitFrames(frames=10)
    EnableFlag(11505360)
    IfFlagEnabled(1, 11505250)
    IfFlagDisabled(2, 11505250)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    Wait(3.0)
    SkipLinesIfFlagEnabled(1, 11500803)
    EndOfAnimation(obj=1501790, animation_id=3)
    SkipLinesIfFlagDisabled(1, 11500806)
    EndOfAnimation(obj=1501790, animation_id=0)
    SkipLinesIfFlagDisabled(1, 11500809)
    EndOfAnimation(obj=1501790, animation_id=1)
    SkipLinesIfFlagDisabled(1, 11500812)
    EndOfAnimation(obj=1501790, animation_id=2)


@NeverRestart(11500100)
def Event_11500100():
    """Event 11500100"""
    IfThisEventFlagDisabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1502060)
    IfThisEventFlagEnabled(2)
    IfFlagDisabled(2, 11500101)
    IfCharacterInsideRegion(2, PLAYER, region=1502061)
    IfThisEventFlagEnabled(3)
    IfFlagDisabled(3, 11500101)
    IfCharacterInsideRegion(3, PLAYER, region=1502062)
    IfThisEventFlagEnabled(4)
    IfFlagEnabled(4, 11500101)
    IfCharacterInsideRegion(4, PLAYER, region=1502060)
    IfThisEventFlagEnabled(5)
    IfFlagEnabled(5, 11500101)
    IfCharacterInsideRegion(5, PLAYER, region=1502063)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    SkipLinesIfFinishedConditionFalse(16, condition=1)
    EnableFlag(11500100)
    ForceAnimation(1501011, 0, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(0, region=1502062)
    Restart()
    SkipLinesIfFinishedConditionTrue(27, condition=4)
    SkipLinesIfFinishedConditionTrue(26, condition=5)
    EnableFlag(11500101)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.WallTouchingFloor)
    ForceAnimation(1501011, 1, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Wall)
    IfAllPlayersOutsideRegion(6, region=1502060)
    IfAllPlayersOutsideRegion(6, region=1502063)
    IfConditionTrue(0, input_condition=6)
    Restart()
    DisableFlag(11500101)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Wall)
    ForceAnimation(1501011, 2, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(7, region=1502061)
    IfAllPlayersOutsideRegion(7, region=1502062)
    IfConditionTrue(0, input_condition=7)
    Restart()


@NeverRestart(11500102)
def Event_11500102():
    """Event 11500102"""
    SkipLinesIfThisEventFlagDisabled(4)
    SkipLinesIfFlagEnabled(1, 11500100)
    EndOfAnimation(obj=1501011, animation_id=20)
    End()
    IfThisEventFlagDisabled(1)
    IfPlayerHasGood(1, 2003)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1501011, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(1501011, 10)
    EndIfClient()
    DisplayDialog(text=10010862, button_type=ButtonType.Yes_or_No)


@NeverRestart(11500103)
def Event_11500103():
    """Event 11500103"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11500102)
    IfPlayerDoesNotHaveGood(1, 2003)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010163, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11500106)
def Event_11500106():
    """Event 11500106"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010161, anchor_entity=1501001)
    Restart()


@NeverRestart(11500107)
def Event_11500107():
    """Event 11500107"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1501001, animation_id=0)
    End()
    IfFlagDisabled(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11500105)
    Move(PLAYER, destination=1501001, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(1501001, 0)


@NeverRestart(11500110)
def Event_11500110(_, arg_0_3: int, arg_4_7: int):
    """Event 11500110"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    EnableFlag(arg_4_7)
    EndIfClient()
    IfPlayerHasGood(1, 2003)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(text=10010883, anchor_entity=arg_0_3, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=10010862, anchor_entity=arg_0_3, button_type=ButtonType.Yes_or_No)


@NeverRestart(11505270)
def Event_11505270(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11505270"""
    SkipLinesIfFlagDisabled(2, arg_20_23)
    EndOfAnimation(obj=arg_4_7, animation_id=0)
    SkipLines(12)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfObjectDamagedBy(-1, arg_4_7, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_20_23)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=arg_4_7, model_point=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id=arg_8_11, erase_root_only=False)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    SkipLinesIfEqual(5, left=arg_20_23, right=11505284)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    IfTrueFlagCountGreaterThanOrEqual(0, FlagType.Absolute, flag_range=(11505280, 11505285), value=2)
    DisableFlag(arg_20_23)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    Restart()


@NeverRestart(11505260)
def Event_11505260():
    """Event 11505260"""
    IfFlagEnabled(0, 11505284)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    IfFlagDisabled(0, 11505284)
    Restart()


@RestartOnRest(11505050)
def Event_11505050():
    """Event 11505050"""
    EndIfThisEventFlagEnabled()
    DisableAI(1500101)
    IfCharacterInsideRegion(-1, PLAYER, region=1502101)
    IfAttacked(-1, attacked_entity=1500101, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11505050)
    IfFlagDisabled(0, 11505052)
    EnableAI(1500101)


@RestartOnRest(11505051)
def Event_11505051():
    """Event 11505051"""
    IfFlagEnabled(1, 11505050)
    IfFlagEnabled(2, 11505052)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    Move(1500101, destination=1502100, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1500101, 9001, wait_for_completion=True)
    DisableFlag(11505052)
    Restart()


@RestartOnRest(11505055)
def Event_11505055():
    """Event 11505055"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1500100, authority_level=UpdateAuthority.Forced)
    IfObjectDestroyed(1, 1501100)
    IfObjectDestroyed(1, 1501101)
    IfObjectDestroyed(1, 1501102)
    IfObjectDestroyed(1, 1501103)
    IfObjectDestroyed(1, 1501104)
    IfObjectDestroyed(1, 1501105)
    IfObjectDestroyed(1, 1501106)
    IfObjectDestroyed(1, 1501107)
    IfObjectDestroyed(1, 1501108)
    IfConditionTrue(0, input_condition=1)
    AICommand(1500100, command_id=20, slot=1)
    ReplanAI(1500100)


@NeverRestart(11505110)
def Event_11505110():
    """Event 11505110"""
    IfFlagEnabled(1, 11505100)
    IfFlagEnabled(2, 11505100)
    IfFlagEnabled(3, 11505100)
    IfFlagEnabled(4, 11505100)
    IfFlagEnabled(5, 11505100)
    IfFlagEnabled(6, 11505100)
    IfFlagEnabled(7, 11505100)
    IfFlagEnabled(1, 11505111)
    IfFlagEnabled(2, 11505112)
    IfFlagEnabled(3, 11505113)
    IfFlagEnabled(4, 11505114)
    IfFlagEnabled(5, 11505115)
    IfFlagEnabled(6, 11505116)
    IfFlagRangeAllDisabled(7, flag_range=(11505111, 11505116))
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, condition=6)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, condition=5)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, condition=4)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5303,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, condition=3)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5302,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, condition=2)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5301,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, condition=1)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()


@NeverRestart(11505111)
def Event_11505111(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11505111"""
    IfFlagDisabled(1, 11505100)
    IfFlagDisabled(1, 11505105)
    IfTimeElapsed(1, seconds=2.0)
    IfFlagDisabled(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505112)
    IfAllPlayersOutsideRegion(1, region=1502701)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505113)
    IfAllPlayersOutsideRegion(1, region=1502702)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505114)
    IfAllPlayersOutsideRegion(1, region=1502703)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505115)
    IfAllPlayersOutsideRegion(1, region=1502704)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505116)
    IfAllPlayersOutsideRegion(1, region=1502705)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505117)
    IfAllPlayersOutsideRegion(1, region=1502710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((11505111, 11505116))
    EnableFlag(arg_0_3)
    AICommand(1500100, command_id=arg_8_11, slot=2)
    Restart()


@NeverRestart(11505101)
def Event_11505101():
    """Event 11505101"""
    IfFlagEnabled(0, 11505105)
    EnableFlag(11505105)
    IfFlagDisabled(0, 11505105)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@NeverRestart(11505102)
def Event_11505102():
    """Event 11505102"""
    DisableNetworkSync()
    IfFlagEnabled(0, 11505105)
    Wait(30.0)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@RestartOnRest(11505060)
def Event_11505060(_, arg_0_3: int):
    """Event 11505060"""
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfCharacterDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest(11505070)
def Event_11505070(_, arg_0_3: int):
    """Event 11505070"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest(11505080)
def Event_11505080():
    """Event 11505080"""
    SkipLinesIfThisEventFlagDisabled(2)
    SetStandbyAnimationSettings(1500122)
    End()
    IfAttacked(-1, attacked_entity=1500122, attacker=PLAYER)
    IfHealthNotEqual(-1, 1500122, value=1.0)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1500122)
    ForceAnimation(1500122, 2000)


@RestartOnRest(11505010)
def Event_11505010():
    """Event 11505010"""
    IfCharacterAlive(1, 1500010)
    IfCharacterBackreadEnabled(1, 1500010)
    IfCharacterHasSpecialEffect(1, 1500010, 5421)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1500010,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=1500010,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=1500010,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(1500010, command_id=10, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    Restart()


@RestartOnRest(11505011)
def Event_11505011():
    """Event 11505011"""
    IfCharacterDoesNotHaveSpecialEffect(1, 1500010, 5420)
    IfAttacked(1, attacked_entity=1500010, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    IfCharacterBackreadDisabled(7, 1500010)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, 1500010, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, 1500010, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, 1500010, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, 1500010, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(1500010, 3006, wait_for_completion=True)
    ReplanAI(1500010)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    Restart()


@RestartOnRest(11505012)
def Event_11505012():
    """Event 11505012"""
    IfCharacterHasSpecialEffect(1, 1500010, 5421)
    IfCharacterHasSpecialEffect(1, 1500010, 3150)
    IfCharacterHasSpecialEffect(2, 1500010, 5420)
    IfCharacterHasSpecialEffect(2, 1500010, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(1500010, command_id=200, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=210, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, 1500010, 5420)
    IfCharacterHasSpecialEffect(-2, 1500010, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11505013)
def Event_11505013():
    """Event 11505013"""
    IfCharacterHasSpecialEffect(1, 1500010, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, 1500010, 3150)
    IfCharacterHasSpecialEffect(2, 1500010, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, 1500010, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(1500010, command_id=201, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=211, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, 1500010, 5420)
    IfCharacterHasSpecialEffect(-2, 1500010, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11505014)
def Event_11505014():
    """Event 11505014"""
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, 1500010, region=1502010)
    IfCharacterBackreadDisabled(1, 1500010)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(1500010, 5421)
    ClearTargetList(1500010)
    ReplanAI(1500010)
    Move(1500010, destination=1502010, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, 1500010)
    Restart()


@RestartOnRest(11505015)
def Event_11505015():
    """Event 11505015"""
    EndIfHost()
    IfCharacterBackreadDisabled(1, 1500010)
    EndIfConditionTrue(1)
    ResetAnimation(1500010, disable_interpolation=True)
    ForceAnimation(1500010, 0)
    ReplanAI(1500010)


@RestartOnRest(11500900)
def Event_11500900():
    """Event 11500900"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(1500010)
    End()
    IfCharacterDead(0, 1500010)
    End()


@NeverRestart(11500210)
def Event_11500210():
    """Event 11500210"""
    EndIfClient()
    IfInsideMap(0, game_map=SENS_FORTRESS)
    IfTimeElapsed(0, seconds=5.0)
    IfFlagEnabled(0, 11)
    IfActionButton(0, prompt_text=10010120, anchor_entity=1502505, anchor_type=CoordEntityType.Region)
    DisableBackread(1500201)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(2, 11510400)
    PlayCutscene(150000, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    SkipLines(2)
    SetMapDrawParamSlot(map_area_id=15, slot=2)
    PlayCutscene(150002, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=33)
    Restart()


@RestartOnRest(11500860)
def Event_11500860(_, arg_0_3: int):
    """Event 11500860"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@NeverRestart(11500600)
def Event_11500600(_, arg_0_3: int, arg_4_7: int):
    """Event 11500600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11500510)
def Event_11500510(_, arg_0_3: int, arg_4_7: int):
    """Event 11500510"""
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


@NeverRestart(11500520)
def Event_11500520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11500530)
def Event_11500530():
    """Event 11500530"""
    SkipLinesIfFlagEnabled(3, 11500593)
    DisableObjectActivation(1501032, obj_act_id=-1)
    IfFlagEnabled(0, 11500593)
    EnableObjectActivation(1501032, obj_act_id=-1)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 11500112)
    DisableFlag(71500021)


@NeverRestart(11500531)
def Event_11500531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500531"""
    IfFlagDisabled(1, 1096)
    IfFlagEnabled(1, 1090)
    IfFlagEnabled(1, 11500112)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11500532)
def Event_11500532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500532"""
    IfFlagDisabled(1, 1096)
    IfFlagEnabled(1, 1092)
    IfFlagEnabled(1, 11500594)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11500533)
def Event_11500533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500533"""
    IfFlagDisabled(1, 1114)
    IfFlagEnabled(1, 1113)
    IfFlagEnabled(1, 723)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11500534)
def Event_11500534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500534"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1490)
    IfFlagEnabled(1, 11500591)
    IfFlagEnabled(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(arg_0_3, region=1502510)
    Kill(1500120)
    Kill(1500121)


@NeverRestart(11500535)
def Event_11500535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500535"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1490)
    IfFlagDisabled(1, 11500591)
    IfFlagEnabled(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(arg_0_3, region=1502510)
    Kill(1500120)
    Kill(1500121)


@NeverRestart(11500536)
def Event_11500536(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11500536"""
    IfHost(1)
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1491)
    IfFlagEnabled(1, 11500850)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfHost(2)
    IfFlagDisabled(2, 1512)
    IfFlagEnabled(2, 1492)
    IfFlagEnabled(2, 11500592)
    IfFlagEnabled(2, 11500850)
    IfCharacterBackreadDisabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11505030)
def Event_11505030():
    """Event 11505030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6510, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11505033)
    IfClient(2)
    IfFlagEnabled(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6510)
    EndIfFlagEnabled(11)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6510)
    IfEntityWithinDistance(1, entity=6510, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6510,
        region=1502000,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


@NeverRestart(11505990)
def Event_11505990(_, arg_0_3: int, arg_4_7: int):
    """Event 11505990"""
    IfFlagEnabled(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagDisabled(0, arg_0_3)
    Restart()


@NeverRestart(11505029)
def Event_11505029():
    """Event 11505029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6510, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11505033)
    IfClient(2)
    IfFlagEnabled(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6510)
    EndIfFlagEnabled(11)
    If_Unknown_3_24(1, unk1=4, unk2=3)
    IfHost(1)
    IfFlagDisabled(1, 11505031)
    IfFlagDisabled(1, 11505033)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6510)
    IfEntityWithinDistance(1, entity=6510, other_entity=PLAYER, radius=10.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6510,
        region=1502000,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


@NeverRestart(11505032)
def Event_11505032():
    """Event 11505032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11505031)
    IfFlagEnabled(1, 11505393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6510, command_id=10, slot=0)
    ReplanAI(6510)
    IfCharacterInsideRegion(0, 6510, region=1502998)
    RotateToFaceEntity(6510, target_entity=1502997)
    ForceAnimation(6510, 7410)
    AICommand(6510, command_id=-1, slot=0)
    ReplanAI(6510)


@NeverRestart(11505843)
def Event_11505843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11505843"""
    IfHost(1)
    IfMultiplayer(1)
    IfFlagEnabled(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=arg_4_7,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@NeverRestart(11505846)
def Event_11505846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11505846"""
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(vfx_id=arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteVFX(vfx_id=arg_8_11)
    Restart()
