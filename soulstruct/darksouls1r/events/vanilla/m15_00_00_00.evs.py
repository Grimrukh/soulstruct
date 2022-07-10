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
    DisableCharacter(1500200)
    Event_11500000()
    Event_11512012()
    Event_11412013()
    Event_11512016()
    Event_11512003()
    Event_11512004()
    Event_11512005()
    Event_11512000()
    Event_11512015()
    Event_11512007()
    Event_11512008()
    Event_11512006()
    Event_11502501()
    Event_11502510(
        0,
        flag=11502520,
        flag_1=11502501,
        obj=1501101,
        character=1500010,
        item_lot_param_id=15050,
        item_lot_param_id_1=16050
    )
    Event_11505510(0, 1501101, 11502501, 11502520, 22680, 1.2000000476837158)
    Event_11502009()
    Event_11502010()
    Event_11502510(
        1,
        flag=11502521,
        flag_1=11502500,
        obj=1501102,
        character=1500006,
        item_lot_param_id=15060,
        item_lot_param_id_1=16060
    )
    Event_11505510(1, 1501102, 11502500, 11502521, 22680, 1.2000000476837158)
    Event_11502502()
    Event_11502510(
        2,
        flag=11502522,
        flag_1=11502502,
        obj=1501103,
        character=1500011,
        item_lot_param_id=15070,
        item_lot_param_id_1=16070
    )
    Event_11505510(2, 1501103, 11502502, 11502522, 22679, 3.200000047683716)
    Event_11512200(0, anchor_entity=1502005)
    Event_11512200(1, anchor_entity=1502006)
    Event_11512011()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11500000)
def Event_11500000():
    """Event 11500000"""
    RegisterBonfire(bonfire_flag=11500992, obj=1501960)
    RegisterBonfire(bonfire_flag=11500984, obj=1501961)
    RegisterBonfire(bonfire_flag=11500976, obj=1501962)
    RegisterLadder(start_climbing_flag=11500010, stop_climbing_flag=11500011, obj=1501013)
    RegisterLadder(start_climbing_flag=11500012, stop_climbing_flag=11500013, obj=1501014)
    RegisterLadder(start_climbing_flag=11500014, stop_climbing_flag=11500015, obj=1501015)
    RegisterLadder(start_climbing_flag=11500016, stop_climbing_flag=11500017, obj=1501016)
    RegisterLadder(start_climbing_flag=11500018, stop_climbing_flag=11500019, obj=1501086)
    RegisterLadder(start_climbing_flag=11500020, stop_climbing_flag=11500021, obj=1501087)
    DisableMapCollision(collision=1503205)
    DisableObject(1501032)
    DisableObject(1501033)
    DisableObject(1501034)
    DisableObject(1501035)
    DisableObject(1501036)
    DisableObject(1501037)
    DisableObject(1501038)
    DisableObject(1501039)
    if FlagDisabled(11500803):
        EndOfAnimation(obj=1501031, animation_id=3)
    if FlagEnabled(11500806):
        EndOfAnimation(obj=1501031, animation_id=0)
    if FlagEnabled(11500809):
        EndOfAnimation(obj=1501031, animation_id=1)
    if FlagEnabled(11500812):
        EndOfAnimation(obj=1501031, animation_id=2)
    DisableMapCollision(collision=1503202)
    DisableMapCollision(collision=1503203)
    DisableMapCollision(collision=1503202)
    if FlagEnabled(11500821):
        EnableObject(1501033)
        EndOfAnimation(obj=1501033, animation_id=5)
        EnableMapCollision(collision=1503202)
    if FlagEnabled(11500822):
        EnableObject(1501034)
        EndOfAnimation(obj=1501034, animation_id=6)
        EnableMapCollision(collision=1503203)
    if FlagEnabled(11500823):
        EnableObject(1501035)
        EndOfAnimation(obj=1501035, animation_id=7)
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
    EndOfAnimation(obj=1501003, animation_id=12)
    SkipLines(9)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.Wall)
    EndOfAnimation(obj=1501003, animation_id=11)
    SkipLines(4)
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    EndOfAnimation(obj=1501000, animation_id=0)
    Event_11505300()
    Event_11500790()
    Event_11500795()
    Event_11500796()
    Event_11500797()
    Event_11500789()
    Event_11500830()
    Event_11500831()
    Event_11500850()
    Event_11505255()
    Event_11500100()
    Event_11500102()
    Event_11500103()
    Event_11500106()
    Event_11500105()
    Event_11500110(0, obj=1501006, obj_act_id=11500110)
    Event_11500110(1, obj=1501007, obj_act_id=11500111)
    Event_11500110(2, obj=1501008, obj_act_id=11500112)
    Event_11500110(3, obj=1501009, obj_act_id=11500113)
    Event_11500110(4, obj=1501010, obj_act_id=11500114)
    Event_11500110(5, obj=1501011, obj_act_id=11500115)
    Event_11500110(6, obj=1501012, obj_act_id=11500116)
    Event_11505270(
        0,
        region=1502011,
        obj=1501017,
        vfx_id=1503412,
        source_entity=1501023,
        launch_angle_y=0,
        left=11505280
    )
    Event_11505270(
        1,
        region=1502012,
        obj=1501018,
        vfx_id=1503413,
        source_entity=1501024,
        launch_angle_y=90,
        left=11505281
    )
    Event_11505270(
        2,
        region=1502013,
        obj=1501019,
        vfx_id=1503414,
        source_entity=1501025,
        launch_angle_y=90,
        left=11505282
    )
    Event_11505270(
        3,
        region=1502014,
        obj=1501020,
        vfx_id=1503415,
        source_entity=1501026,
        launch_angle_y=270,
        left=11505283
    )
    Event_11505270(
        4,
        region=1502015,
        obj=1501021,
        vfx_id=1503412,
        source_entity=1501027,
        launch_angle_y=180,
        left=11505284
    )
    Event_11505270(
        5,
        region=1502016,
        obj=1501022,
        vfx_id=1503412,
        source_entity=1501026,
        launch_angle_y=270,
        left=11505285
    )
    Event_11505260()
    DisableObject(1501092)
    DisableMapCollision(collision=1503209)
    DisableMapCollision(collision=1503208)
    DisableMapCollision(collision=1503207)
    SkipLinesIfFlagDisabled(8, 11510300)
    SkipLinesIfFlagDisabled(6, 11510301)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1501091, animation_id=51)
    EnableMapCollision(collision=1503209)
    SkipLines(13)
    SkipLinesIfFlagDisabled(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1501091, animation_id=50)
    EnableMapCollision(collision=1503208)
    SkipLines(6)
    if FlagEnabled(11510303):
        DisableFlag(11510301)
        DisableFlag(11510302)
        EnableFlag(11510303)
        EndOfAnimation(obj=1501091, animation_id=53)
        EnableMapCollision(collision=1503207)
    DisableObject(1501095)
    DisableMapCollision(collision=1503213)
    DisableMapCollision(collision=1503212)
    DisableMapCollision(collision=1503211)
    SkipLinesIfFlagDisabled(1, 11510320)
    SkipLinesIfFlagDisabled(6, 11510321)
    EnableFlag(11510321)
    DisableFlag(11510322)
    DisableFlag(11510323)
    EndOfAnimation(obj=1501094, animation_id=51)
    EnableMapCollision(collision=1503213)
    SkipLines(13)
    SkipLinesIfFlagDisabled(6, 11510322)
    DisableFlag(11510321)
    EnableFlag(11510322)
    DisableFlag(11510323)
    EndOfAnimation(obj=1501094, animation_id=50)
    EnableMapCollision(collision=1503212)
    SkipLines(6)
    if FlagEnabled(11510323):
        DisableFlag(11510321)
        DisableFlag(11510322)
        EnableFlag(11510323)
        EndOfAnimation(obj=1501094, animation_id=53)
        EnableMapCollision(collision=1503211)
    Event_11510300()
    Event_11512001()
    Event_11510320()
    Event_11512002()
    Event_11510340()
    Event_11510310()
    Event_11510330()
    Event_11510200()
    Event_11510201()
    Event_11510100()
    Event_11510210()
    Event_11510211()
    Event_11510220()
    Event_11510110()
    Event_11510401()
    Event_11510215()
    Event_11510260(0, flag=11510251, region=1512251, region_1=1512250)
    Event_11510260(1, flag=11510257, region=1512253, region_1=1512252)
    Event_11510260(2, flag=11510258, region=1512255, region_1=1512254)
    Event_11502600(0, 1501100, 11502600)


@NeverRestart(11505300)
def Event_11505300():
    """Event 11505300"""
    CreateHazard(
        obj_flag=11505301,
        obj=1501046,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505302,
        obj=1501047,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505303,
        obj=1501048,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505304,
        obj=1501049,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505305,
        obj=1501050,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505306,
        obj=1501051,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505307,
        obj=1501052,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505308,
        obj=1501053,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505309,
        obj=1501054,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505310,
        obj=1501055,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505311,
        obj=1501056,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505312,
        obj=1501057,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505313,
        obj=1501058,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505314,
        obj=1501059,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505315,
        obj=1501060,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505316,
        obj=1501061,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505317,
        obj=1501062,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505290,
        obj=1501002,
        model_point=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


@NeverRestart(11500790)
def Event_11500790():
    """Event 11500790"""
    Wait(5.0)
    EnableObject(1501032)
    ForceAnimation(1501032, 0)
    Wait(1.5)
    EnableMapCollision(collision=1503205)
    Wait(3.5)
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


@NeverRestart(11500795)
def Event_11500795():
    """Event 11500795"""
    MAIN.Await(FlagEnabled(11505220))
    
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(1501032)
    EnableObject(1501036)
    if FlagEnabled(11500812):
        Event_11500700(0, 11505200, 1501036, 1, 2.5, 1501042, 11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(10, 11505200, 1501036, 2, 7.5, 1501043, 11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(20, 11505200, 1501036, 3, 7.5, 1501040, 11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(30, 11505200, 1501036, 4, 12.5, 1501041, 11505210)
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505200,
            obj=1501033,
            animation_id=5,
            collision=1503202,
            entity=1501041,
            flag=11505210,
            flag_1=11500821,
            obj_1=1501036
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505200,
            obj=1501034,
            animation_id=6,
            collision=1503203,
            entity=1501041,
            flag=11505210,
            flag_1=11500822,
            obj_1=1501036
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505200,
            obj=1501035,
            animation_id=7,
            collision=1503202,
            entity=1501041,
            flag=11505210,
            flag_1=11500823,
            obj_1=1501036
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    Event_11500700(40, 11505200, 1501036, 8, 18.5, 1501041, 11505210)
    
    MAIN.Await(FlagDisabled(11505210))
    
    Restart()


@NeverRestart(11500796)
def Event_11500796():
    """Event 11500796"""
    MAIN.Await(FlagEnabled(11505221))
    
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(1501032)
    EnableObject(1501037)
    if FlagEnabled(11500812):
        Event_11500700(1, 11505201, 1501037, 1, 2.5, 1501042, 11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(11, 11505201, 1501037, 2, 7.5, 1501043, 11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(21, 11505201, 1501037, 3, 7.5, 1501040, 11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(31, 11505201, 1501037, 4, 12.5, 1501041, 11505211)
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505201,
            obj=1501033,
            animation_id=5,
            collision=1503202,
            entity=1501041,
            flag=11505211,
            flag_1=11500821,
            obj_1=1501037
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505201,
            obj=1501034,
            animation_id=6,
            collision=1503203,
            entity=1501041,
            flag=11505211,
            flag_1=11500822,
            obj_1=1501037
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505201,
            obj=1501035,
            animation_id=7,
            collision=1503202,
            entity=1501041,
            flag=11505211,
            flag_1=11500823,
            obj_1=1501037
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    Event_11500700(41, 11505201, 1501037, 8, 18.5, 1501041, 11505211)
    
    MAIN.Await(FlagDisabled(11505211))
    
    Restart()


@NeverRestart(11500797)
def Event_11500797():
    """Event 11500797"""
    MAIN.Await(FlagEnabled(11505222))
    
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(1501032)
    EnableObject(1501038)
    if FlagEnabled(11500812):
        Event_11500700(2, 11505202, 1501038, 1, 2.5, 1501042, 11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(12, 11505202, 1501038, 2, 7.5, 1501043, 11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(22, 11505202, 1501038, 3, 7.5, 1501040, 11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(32, 11505202, 1501038, 4, 12.5, 1501041, 11505212)
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505202,
            obj=1501033,
            animation_id=5,
            collision=1503202,
            entity=1501041,
            flag=11505212,
            flag_1=11500821,
            obj_1=1501038
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505202,
            obj=1501034,
            animation_id=6,
            collision=1503203,
            entity=1501041,
            flag=11505212,
            flag_1=11500822,
            obj_1=1501038
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505202,
            obj=1501035,
            animation_id=7,
            collision=1503202,
            entity=1501041,
            flag=11505212,
            flag_1=11500823,
            obj_1=1501038
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    Event_11500700(42, 11505202, 1501038, 8, 18.5, 1501041, 11505212)
    
    MAIN.Await(FlagDisabled(11505212))
    
    Restart()


@NeverRestart(11500789)
def Event_11500789():
    """Event 11500789"""
    MAIN.Await(FlagEnabled(11505223))
    
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(1501032)
    EnableObject(1501039)
    if FlagEnabled(11500812):
        Event_11500700(3, 11505203, 1501039, 1, 2.5, 1501042, 11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(13, 11505203, 1501039, 2, 7.5, 1501043, 11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(23, 11505203, 1501039, 3, 7.5, 1501040, 11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(33, 11505203, 1501039, 4, 12.5, 1501041, 11505213)
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505203,
            obj=1501033,
            animation_id=5,
            collision=1503202,
            entity=1501041,
            flag=11505213,
            flag_1=11500821,
            obj_1=1501039
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505203,
            obj=1501034,
            animation_id=6,
            collision=1503203,
            entity=1501041,
            flag=11505213,
            flag_1=11500822,
            obj_1=1501039
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505203,
            obj=1501035,
            animation_id=7,
            collision=1503202,
            entity=1501041,
            flag=11505213,
            flag_1=11500823,
            obj_1=1501039
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    Event_11500700(43, 11505203, 1501039, 8, 18.5, 1501041, 11505213)
    
    MAIN.Await(FlagDisabled(11505213))
    
    Restart()


@NeverRestart(11500700)
def Event_11500700(_, obj_flag: int, obj: int, animation_id: int, life: float, entity: int, flag: int):
    """Event 11500700"""
    DisableMapCollision(collision=1503205)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
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


@NeverRestart(11500750)
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
    DisableMapCollision(collision=1503205)
    EnableFlag(flag_1)
    EnableObject(obj)
    DisableObject(obj_1)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
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


@NeverRestart(11500830)
def Event_11500830():
    """Event 11500830"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502021))
    
    EnableFlag(11500830)


@NeverRestart(11500831)
def Event_11500831():
    """Event 11500831"""
    AND_1.Add(FlagEnabled(11500751))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502022))
    AND_2.Add(FlagEnabled(11500752))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502023))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    Kill(PLAYER)


@NeverRestart(11500850)
def Event_11500850():
    """Event 11500850"""
    DisableFlag(11505250)
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501031,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501031,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFinishedConditionFalse(23, input_condition=AND_1)
    Move(PLAYER, destination=1501031, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(1501031, 3, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500812)
        ForceAnimation(1501031, 2, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(1501031, 1, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500806)
        ForceAnimation(1501031, 0, wait_for_completion=True)
    Restart()
    Move(PLAYER, destination=1501031, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(1501031, 5, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500812)
        ForceAnimation(1501031, 4, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(1501031, 7, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500806)
        ForceAnimation(1501031, 6, wait_for_completion=True)
    Restart()


@NeverRestart(11505255)
def Event_11505255():
    """Event 11505255"""
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(FlagDisabled(11505251))
    AND_1.Add(FlagDisabled(11500809))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502019))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(FlagDisabled(11505252))
    AND_2.Add(FlagEnabled(11500803))
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502020))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11505250)
    SkipLinesIfFinishedConditionTrue(19, input_condition=AND_2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    if FlagDisabled(11500803):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        EnableFlag(11500803)
        EnableFlag(11500809)
        ForceAnimation(1501031, 0, wait_for_completion=True)
        ForceAnimation(1501031, 1, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(1501031, 1, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(1501031, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    if FlagEnabled(11500809):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        DisableFlag(11500809)
        DisableFlag(11500803)
        ForceAnimation(1501031, 6, wait_for_completion=True)
        ForceAnimation(1501031, 7, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(1501031, 7, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=1501031, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(1501031, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


@NeverRestart(11500100)
def Event_11500100():
    """Event 11500100"""
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502007))
    AND_2.Add(ThisEventFlagEnabled())
    AND_2.Add(FlagDisabled(11500101))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502008))
    AND_3.Add(ThisEventFlagEnabled())
    AND_3.Add(FlagDisabled(11500101))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1502009))
    AND_4.Add(ThisEventFlagEnabled())
    AND_4.Add(FlagEnabled(11500101))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1502007))
    AND_5.Add(ThisEventFlagEnabled())
    AND_5.Add(FlagEnabled(11500101))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1502010))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    
    MAIN.Await(OR_1)
    
    EnableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Solid)
    SkipLinesIfFinishedConditionFalse(16, input_condition=AND_1)
    EnableFlag(11500100)
    ForceAnimation(1501003, 0, wait_for_completion=True)
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
    
    MAIN.Await(AllPlayersOutsideRegion(region=1502009))
    
    Restart()
    SkipLinesIfFinishedConditionTrue(27, input_condition=AND_4)
    SkipLinesIfFinishedConditionTrue(26, input_condition=AND_5)
    EnableFlag(11500101)
    DisableNavmeshType(navmesh_id=1503100, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503110, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503101, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503111, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503102, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=1503112, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503103, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=1503113, navmesh_type=NavmeshType.WallTouchingFloor)
    ForceAnimation(1501003, 1, wait_for_completion=True)
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
    AND_6.Add(AllPlayersOutsideRegion(region=1502007))
    AND_6.Add(AllPlayersOutsideRegion(region=1502010))
    
    MAIN.Await(AND_6)
    
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
    ForceAnimation(1501003, 2, wait_for_completion=True)
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
    AND_7.Add(AllPlayersOutsideRegion(region=1502008))
    AND_7.Add(AllPlayersOutsideRegion(region=1502009))
    
    MAIN.Await(AND_7)
    
    Restart()


@NeverRestart(11500102)
def Event_11500102():
    """Event 11500102"""
    SkipLinesIfThisEventFlagDisabled(3)
    SkipLinesIfFlagEnabled(1, 11500100)
    EndOfAnimation(obj=1501003, animation_id=20)
    End()
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(PlayerHasGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1501003, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(1501003, 10)
    DisplayDialog(text=10010864, button_type=ButtonType.Yes_or_No)


@NeverRestart(11500103)
def Event_11500103():
    """Event 11500103"""
    AND_1.Add(FlagDisabled(11500102))
    AND_1.Add(PlayerDoesNotHaveGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010163, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11500106)
def Event_11500106():
    """Event 11500106"""
    AND_1.Add(FlagDisabled(11500105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1501001)
    Restart()


@NeverRestart(11500105)
def Event_11500105():
    """Event 11500105"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1501001, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    EnableFlag(11500105)
    Move(PLAYER, destination=1501001, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(1501001, 0)


@NeverRestart(11500110)
def Event_11500110(_, obj: int, obj_act_id: int):
    """Event 11500110"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    DisplayDialog(text=10010864, anchor_entity=obj, button_type=ButtonType.Yes_or_No)


@NeverRestart(11505270)
def Event_11505270(_, region: int, obj: int, vfx_id: int, source_entity: int, launch_angle_y: int, left: int):
    """Event 11505270"""
    SkipLinesIfFlagDisabled(2, left)
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLines(13)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(ObjectDamaged(obj, attacker=-1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(left)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=obj, model_point=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id, erase_root_only=False)
    ForceAnimation(obj, 0, wait_for_completion=True)
    if ValueNotEqual(left=left, right=11505284):
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=1500200,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
    
    MAIN.Await(TrueFlagCountGreaterThanOrEqual(FlagType.Absolute, flag_range=(11505280, 11505286), value=2))
    
    DisableFlag(left)
    ForceAnimation(obj, 1, wait_for_completion=True)
    Restart()


@NeverRestart(11505260)
def Event_11505260():
    """Event 11505260"""
    MAIN.Await(FlagEnabled(11505284))
    
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        source_entity=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    
    MAIN.Await(FlagDisabled(11505284))
    
    Restart()


@RestartOnRest(11515398)
def Event_11515398():
    """Event 11515398"""
    AND_1.Add(CharacterDead(1500006))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(1500006))
    
    CreateNPCPart(
        1500006,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(1500006, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(1500006, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatioLessThanOrEqual(1500006, value=0.0))
    
    SetNPCPartHealth(1500006, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515060)
def Event_11515060(_, character: int):
    """Event 11515060"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(
        character,
        npc_part_id=2870,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatioLessThanOrEqual(character, value=0.0))
    
    SetNPCPartHealth(character, npc_part_id=2870, desired_health=0, overwrite_max=False)


@NeverRestart(11510100)
def Event_11510100():
    """Event 11510100"""
    if ThisEventFlagEnabled():
        PostDestruction(1501088)
        PostDestruction(1501090)
        EndOfAnimation(obj=1501089, animation_id=0)
        EndOfAnimation(obj=1501090, animation_id=1)
        EnableObjectInvulnerability(1501089)
        End()
    
    MAIN.Await(ObjectDestroyed(1501088))
    
    ForceAnimation(1501089, 0)
    ForceAnimation(1501090, 0, wait_for_completion=True)
    DestroyObject(1501090)


@NeverRestart(11510110)
def Event_11510110():
    """Event 11510110"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1501083, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501083,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1501083, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1501083, 0)


@NeverRestart(11510200)
def Event_11510200():
    """Event 11510200"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1501064, obj_act_id=-1)
        EndOfAnimation(obj=1501063, animation_id=0)
        EndOfAnimation(obj=1501065, animation_id=0)
        EndOfAnimation(obj=1501064, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501064,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1501064, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1501064, 0, wait_for_completion=True)
    ForceAnimation(1501063, 0)
    EndOfAnimation(obj=1501065, animation_id=0)


@NeverRestart(11510201)
def Event_11510201():
    """Event 11510201"""
    AND_1.Add(FlagDisabled(11510200))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1502025,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1501063,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160)
    Restart()


@NeverRestart(11510210)
def Event_11510210():
    """Event 11510210"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1501066, animation_id=0)
        End()
    EnableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501066,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1501066, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1501066, 0)
    DisableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Solid)


@NeverRestart(11510211)
def Event_11510211():
    """Event 11510211"""
    AND_1.Add(FlagDisabled(11510210))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1501066,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1501066)
    Restart()


@NeverRestart(11510220)
def Event_11510220():
    """Event 11510220"""
    ForceAnimation(1501067, 0)
    if FlagEnabled(11502010):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502002))
    
    ForceAnimation(1501067, -1)
    
    MAIN.Await(FlagEnabled(11502010))
    
    ForceAnimation(1501067, 0)


@NeverRestart(11510260)
def Event_11510260(_, flag: int, region: int, region_1: int):
    """Event 11510260"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
        AddSpecialEffect(PLAYER, 4150)
        Wait(3.0)
        Restart()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11510710)
def Event_11510710(_, obj_act_id: int, character: int, region: int, region_1: int):
    """Event 11510710"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
        EnableFlag(obj_act_id)
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterInsideRegion(character, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11510300)
def Event_11510300():
    """Event 11510300"""
    AND_1.Add(FlagDisabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501091,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501091,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFlagDisabled(12, 11510301)
    SkipLinesIfFinishedConditionFalse(11, input_condition=AND_2)
    OR_7.Add(PlayerHasGood(2004))
    SkipLinesIfConditionFalse(2, OR_7)
    DisplayDialog(text=10010863)
    SkipLines(7)
    AND_7.Add(PlayerHasGood(2003))
    SkipLinesIfConditionFalse(2, AND_7)
    DisplayDialog(text=10010862)
    SkipLines(3)
    DisplayDialog(text=10010164)
    Wait(3.0)
    Restart()
    SkipLinesIfFlagDisabled(8, 11510302)
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_2)
    OR_6.Add(PlayerHasGood(2004))
    SkipLinesIfConditionFalse(2, OR_6)
    DisplayDialog(text=10010863)
    SkipLines(3)
    DisplayDialog(text=10010164)
    Wait(3.0)
    Restart()
    EnableFlag(11515300)
    SkipLinesIfFlagDisabled(9, 11510303)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1501091, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1501091, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        0,
        entity=1501091,
        obj=1501092,
        animation_id=0,
        collision=1503207,
        collision_1=1503208,
        flag=11510303,
        flag_1=11510302,
        flag_2=11515300,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(16, 11510302)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1501091, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1501091, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        3,
        entity=1501091,
        obj=1501092,
        animation_id=1,
        collision=1503208,
        collision_1=1503209,
        flag=11510302,
        flag_1=11510301,
        flag_2=11515300,
        frames=360
    )
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1501091, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1501091, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        entity=1501091,
        obj=1501092,
        animation_id=3,
        collision=1503208,
        collision_1=1503207,
        flag=11510302,
        flag_1=11510303,
        flag_2=11515300,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(9, 11510301)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1501091, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1501091, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        7,
        entity=1501091,
        obj=1501092,
        animation_id=2,
        collision=1503209,
        collision_1=1503208,
        flag=11510301,
        flag_1=11510302,
        flag_2=11515300,
        frames=360
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    DisplayDialog(text=10010170)
    Restart()


@NeverRestart(11510320)
def Event_11510320():
    """Event 11510320"""
    AND_1.Add(FlagDisabled(11510321))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501094,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11510323))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501094,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFlagDisabled(12, 11510321)
    SkipLinesIfFinishedConditionFalse(11, input_condition=AND_2)
    OR_7.Add(PlayerHasGood(2004))
    SkipLinesIfConditionFalse(2, OR_7)
    DisplayDialog(text=10010863)
    SkipLines(7)
    AND_7.Add(PlayerHasGood(2003))
    SkipLinesIfConditionFalse(2, AND_7)
    DisplayDialog(text=10010862)
    SkipLines(3)
    DisplayDialog(text=10010164)
    Wait(3.0)
    Restart()
    SkipLinesIfFlagDisabled(8, 11510322)
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_2)
    OR_6.Add(PlayerHasGood(2004))
    SkipLinesIfConditionFalse(2, OR_6)
    DisplayDialog(text=10010863)
    SkipLines(3)
    DisplayDialog(text=10010164)
    Wait(3.0)
    Restart()
    EnableFlag(11515302)
    SkipLinesIfFlagDisabled(9, 11510323)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1501094, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1501094, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        0,
        entity=1501094,
        obj=1501095,
        animation_id=0,
        collision=1503211,
        collision_1=1503212,
        flag=11510323,
        flag_1=11510322,
        flag_2=11515302,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    SkipLinesIfFlagDisabled(16, 11510322)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1501094, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1501094, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        3,
        entity=1501094,
        obj=1501095,
        animation_id=1,
        collision=1503212,
        collision_1=1503213,
        flag=11510322,
        flag_1=11510321,
        flag_2=11515302,
        frames=360
    )
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1501094, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1501094, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        entity=1501094,
        obj=1501095,
        animation_id=3,
        collision=1503212,
        collision_1=1503211,
        flag=11510322,
        flag_1=11510323,
        flag_2=11515302,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    SkipLinesIfFlagDisabled(9, 11510321)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1501094, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1501094, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        7,
        entity=1501094,
        obj=1501095,
        animation_id=2,
        collision=1503213,
        collision_1=1503212,
        flag=11510321,
        flag_1=11510322,
        flag_2=11515302,
        frames=360
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    DisplayDialog(text=10010170)
    Restart()


@NeverRestart(11515320)
def Event_11515320(
    _,
    entity: int,
    obj: int,
    animation_id: int,
    collision: int,
    collision_1: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    frames: int,
):
    """Event 11515320"""
    DisableMapCollision(collision=collision)
    EnableObject(obj)
    ForceAnimation(entity, animation_id)
    ForceAnimation(obj, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(obj)
    EnableMapCollision(collision=collision_1)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)


@NeverRestart(11515330)
def Event_11515330(
    _,
    entity: int,
    obj: int,
    animation_id: int,
    animation_id_1: int,
    collision: int,
    collision_1: int,
    collision_2: int,
    collision_3: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    animation_id_2: int,
    frames: int,
    frames_1: int,
):
    """Event 11515330"""
    DisableMapCollision(collision=collision)
    DisableMapCollision(collision=collision_1)
    DisableMapCollision(collision=collision_2)
    EnableObject(obj)
    ForceAnimation(entity, animation_id)
    ForceAnimation(obj, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(entity, animation_id_2)
    WaitFrames(frames=130)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(entity, animation_id_1)
    ForceAnimation(obj, animation_id_1)
    WaitFrames(frames=frames_1)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(obj)
    EnableMapCollision(collision=collision_3)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)


@NeverRestart(11510340)
def Event_11510340():
    """Event 11510340"""
    if FlagEnabled(11515300):
        EnableMapCollision(collision=1503210)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagDisabled(11515300))
    
        Restart()
    if FlagEnabled(11510303):
        EnableMapCollision(collision=1503210)
        DisableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510302):
        DisableMapCollision(collision=1503210)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510301):
        EnableMapCollision(collision=1503210)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    DisplayDialog(text=10010170)
    Restart()


@NeverRestart(11510310)
def Event_11510310():
    """Event 11510310"""
    AND_1.Add(FlagEnabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501091,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagEnabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501091,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagEnabled(11515300))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    DisplayDialog(text=10010170)
    Restart()
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()


@NeverRestart(11510330)
def Event_11510330():
    """Event 11510330"""
    AND_1.Add(FlagEnabled(11510321))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501094,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagEnabled(11510323))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1501094,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagEnabled(11515302))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    DisplayDialog(text=10010170)
    Restart()
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()


@NeverRestart(11510401)
def Event_11510401():
    """Event 11510401"""
    if ThisEventFlagEnabled():
        DisableObject(1501068)
        End()
    EnableObjectInvulnerability(1501068)
    
    MAIN.Await(EntityWithinDistance(entity=1501068, other_entity=PLAYER, radius=15.0))
    
    DisableObjectInvulnerability(1501068)
    DestroyObject(1501068)
    ForceAnimation(1501068, 0)
    PlaySoundEffect(1501068, 590000000, sound_type=SoundType.o_Object)


@NeverRestart(11510215)
def Event_11510215():
    """Event 11510215"""
    if ThisEventFlagEnabled():
        DisableObject(1501085)
        End()
    
    MAIN.Await(ObjectDestroyed(1501085))
    
    End()


@NeverRestart(11512000)
def Event_11512000():
    """Event 11512000"""
    AND_1.Add(FlagEnabled(11813508))
    AND_1.Add(ActionButton(
        prompt_text=10010512,
        anchor_entity=1502026,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisableMapCollision(collision=1503215)
    DisableMapCollision(collision=1503216)
    DisableMapCollision(collision=1503217)
    DisableMapCollision(collision=1503218)
    WaitFrames(frames=1)
    Move(PLAYER, destination=1502026, destination_type=CoordEntityType.Region, set_draw_parent=1503231)
    Wait(5.0)
    EnableMapCollision(collision=1503215)
    Restart()


@NeverRestart(11512015)
def Event_11512015():
    """Event 11512015"""
    AND_1.Add(FlagEnabled(11813508))
    AND_1.Add(ActionButton(
        prompt_text=10010512,
        anchor_entity=1502027,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1502500, destination_type=CoordEntityType.Region, set_draw_parent=1503215)
    NightfallCameraResetRequest()
    Restart()


@NeverRestart(11512001)
def Event_11512001():
    """Event 11512001"""
    AND_1.Add(FlagDisabled(11510301))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502029))
    AND_2.Add(FlagDisabled(11510301))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502030))
    AND_3.Add(FlagEnabled(11510303))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1502031))
    AND_4.Add(FlagDisabled(11510302))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1502032))
    AND_5.Add(FlagDisabled(11510303))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1502033))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_5)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11515300)
    SkipLinesIfFlagDisabled(22, 11510303)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_3)
    ForceAnimation(1501091, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        0,
        entity=1501091,
        obj=1501092,
        animation_id=0,
        collision=1503207,
        collision_1=1503208,
        flag=11510303,
        flag_1=11510302,
        flag_2=11515300,
        frames=180
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_4)
    ForceAnimation(1501091, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        1,
        entity=1501091,
        obj=1501092,
        animation_id=0,
        collision=1503207,
        collision_1=1503208,
        flag=11510303,
        flag_1=11510302,
        flag_2=11515300,
        frames=180
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_2)
    ForceAnimation(1501091, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        0,
        1501091,
        1501092,
        0,
        1,
        1503209,
        1503208,
        1503207,
        1503209,
        11510303,
        11510301,
        11515300,
        11,
        180,
        360,
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    ForceAnimation(1501091, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        1,
        1501091,
        1501092,
        0,
        1,
        1503209,
        1503208,
        1503207,
        1503209,
        11510303,
        11510301,
        11515300,
        11,
        180,
        360,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(17, 11510302)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_2)
    ForceAnimation(1501091, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        2,
        entity=1501091,
        obj=1501092,
        animation_id=1,
        collision=1503208,
        collision_1=1503209,
        flag=11510302,
        flag_1=11510301,
        flag_2=11515300,
        frames=360
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    ForceAnimation(1501091, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        3,
        entity=1501091,
        obj=1501092,
        animation_id=1,
        collision=1503208,
        collision_1=1503209,
        flag=11510302,
        flag_1=11510301,
        flag_2=11515300,
        frames=360
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_5)
    ForceAnimation(1501091, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        entity=1501091,
        obj=1501092,
        animation_id=3,
        collision=1503208,
        collision_1=1503207,
        flag=11510302,
        flag_1=11510303,
        flag_2=11515300,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(12, 11510301)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_4)
    ForceAnimation(1501091, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        5,
        entity=1501091,
        obj=1501092,
        animation_id=2,
        collision=1503209,
        collision_1=1503208,
        flag=11510301,
        flag_1=11510302,
        flag_2=11515300,
        frames=360
    )
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_5)
    ForceAnimation(1501091, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        2,
        1501091,
        1501092,
        2,
        3,
        1503209,
        1503208,
        1503207,
        1503207,
        11510301,
        11510303,
        11515300,
        13,
        360,
        180,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    Restart()


@NeverRestart(11512002)
def Event_11512002():
    """Event 11512002"""
    AND_1.Add(FlagEnabled(11510323))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502034))
    AND_2.Add(FlagDisabled(11510323))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502035))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11515302)
    SkipLinesIfFlagDisabled(7, 11510303)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    ForceAnimation(1501094, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        1,
        1501094,
        1501095,
        0,
        1,
        1503213,
        1503212,
        1503211,
        1503213,
        11510323,
        11510321,
        11515302,
        11,
        180,
        360,
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    SkipLinesIfFlagDisabled(7, 11510322)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_2)
    ForceAnimation(1501094, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        entity=1501094,
        obj=1501095,
        animation_id=3,
        collision=1503212,
        collision_1=1503211,
        flag=11510322,
        flag_1=11510323,
        flag_2=11515302,
        frames=180
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    SkipLinesIfFlagDisabled(7, 11510321)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_2)
    ForceAnimation(1501094, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        2,
        1501094,
        1501095,
        2,
        3,
        1503213,
        1503212,
        1503211,
        1503211,
        11510321,
        11510323,
        11515302,
        13,
        360,
        180,
    )
    
    MAIN.Await(FlagDisabled(11515302))
    
    Restart()
    Restart()


@NeverRestart(11512003)
def Event_11512003():
    """Event 11512003"""
    OR_1.Add(PlayerStandingOnCollision(1503231))
    OR_1.Add(PlayerStandingOnCollision(1503232))
    OR_1.Add(PlayerStandingOnCollision(1503233))
    OR_1.Add(PlayerStandingOnCollision(1503234))
    OR_1.Add(PlayerStandingOnCollision(1503235))
    OR_1.Add(PlayerStandingOnCollision(1503236))
    OR_1.Add(PlayerStandingOnCollision(1503237))
    OR_1.Add(PlayerStandingOnCollision(1503238))
    OR_1.Add(PlayerStandingOnCollision(1503239))
    OR_1.Add(PlayerStandingOnCollision(1503240))
    
    MAIN.Await(OR_1)
    
    EnableMapCollision(collision=1503231)
    EnableMapCollision(collision=1503232)
    EnableMapCollision(collision=1503233)
    EnableMapCollision(collision=1503234)
    EnableMapCollision(collision=1503235)
    EnableMapCollision(collision=1503236)
    EnableMapCollision(collision=1503237)
    EnableMapCollision(collision=1503238)
    EnableMapCollision(collision=1503239)
    EnableMapCollision(collision=1503240)
    DisableMapCollision(collision=1503222)
    DisableMapCollision(collision=1503223)
    DisableMapCollision(collision=1503224)
    DisableMapCollision(collision=1503225)
    DisableMapCollision(collision=1503226)
    DisableMapCollision(collision=1503227)
    DisableMapCollision(collision=1503228)
    DisableMapCollision(collision=1503229)
    DisableMapCollision(collision=1503230)
    OR_2.Add(PlayerStandingOnCollision(1503231))
    OR_2.Add(PlayerStandingOnCollision(1503232))
    OR_2.Add(PlayerStandingOnCollision(1503233))
    OR_2.Add(PlayerStandingOnCollision(1503234))
    OR_2.Add(PlayerStandingOnCollision(1503235))
    OR_2.Add(PlayerStandingOnCollision(1503236))
    OR_2.Add(PlayerStandingOnCollision(1503237))
    OR_2.Add(PlayerStandingOnCollision(1503238))
    OR_2.Add(PlayerStandingOnCollision(1503239))
    OR_2.Add(PlayerStandingOnCollision(1503240))
    
    MAIN.Await(not OR_2)
    
    Restart()


@NeverRestart(11512004)
def Event_11512004():
    """Event 11512004"""
    OR_1.Add(PlayerStandingOnCollision(1503221))
    OR_1.Add(PlayerStandingOnCollision(1503222))
    OR_1.Add(PlayerStandingOnCollision(1503223))
    OR_1.Add(PlayerStandingOnCollision(1503224))
    OR_1.Add(PlayerStandingOnCollision(1503225))
    OR_1.Add(PlayerStandingOnCollision(1503226))
    OR_1.Add(PlayerStandingOnCollision(1503227))
    OR_1.Add(PlayerStandingOnCollision(1503228))
    OR_1.Add(PlayerStandingOnCollision(1503229))
    OR_1.Add(PlayerStandingOnCollision(1503230))
    
    MAIN.Await(OR_1)
    
    EnableMapCollision(collision=1503221)
    EnableMapCollision(collision=1503222)
    EnableMapCollision(collision=1503223)
    EnableMapCollision(collision=1503224)
    EnableMapCollision(collision=1503225)
    EnableMapCollision(collision=1503226)
    EnableMapCollision(collision=1503227)
    EnableMapCollision(collision=1503228)
    EnableMapCollision(collision=1503229)
    EnableMapCollision(collision=1503230)
    DisableMapCollision(collision=1503231)
    DisableMapCollision(collision=1503232)
    DisableMapCollision(collision=1503233)
    DisableMapCollision(collision=1503234)
    DisableMapCollision(collision=1503235)
    DisableMapCollision(collision=1503236)
    DisableMapCollision(collision=1503237)
    DisableMapCollision(collision=1503238)
    DisableMapCollision(collision=1503239)
    DisableMapCollision(collision=1503240)
    OR_2.Add(PlayerStandingOnCollision(1503221))
    OR_2.Add(PlayerStandingOnCollision(1503222))
    OR_2.Add(PlayerStandingOnCollision(1503223))
    OR_2.Add(PlayerStandingOnCollision(1503224))
    OR_2.Add(PlayerStandingOnCollision(1503225))
    OR_2.Add(PlayerStandingOnCollision(1503226))
    OR_2.Add(PlayerStandingOnCollision(1503227))
    OR_2.Add(PlayerStandingOnCollision(1503228))
    OR_2.Add(PlayerStandingOnCollision(1503229))
    OR_2.Add(PlayerStandingOnCollision(1503230))
    
    MAIN.Await(not OR_2)
    
    Restart()


@NeverRestart(11512005)
def Event_11512005():
    """Event 11512005"""
    MAIN.Await(InsideMap(game_map=FIRELINK_SHRINE))
    
    DisableMapCollision(collision=1503241)
    
    MAIN.Await(InsideMap(game_map=SENS_FORTRESS))
    
    EnableMapCollision(collision=1503241)
    Restart()


@RestartOnRest(11512006)
def Event_11512006():
    """Event 11512006"""
    DisableCharacter(1500009)
    if FlagEnabled(11502501):
        Kill(1500009)
        End()
    DisableGravity(1500009)
    DisableCharacterCollision(1500009)


@RestartOnRest(11502501)
def Event_11502501():
    """Event 11502501"""
    DisableSoundEvent(sound_id=1503802)
    DisableCharacter(1500010)
    EnableInvincibility(1500014)
    DisableGravity(1500014)
    DisableCharacterCollision(1500014)
    DisableCharacter(1500014)
    DisableObject(1501073)
    DeleteVFX(1503404, erase_root_only=False)
    DisableObject(1501074)
    DeleteVFX(1503405, erase_root_only=False)
    DisableObject(1501075)
    DeleteVFX(1503406, erase_root_only=False)
    DisableObject(1501076)
    DeleteVFX(1503407, erase_root_only=False)
    DisableObject(1501077)
    DeleteVFX(1503408, erase_root_only=False)
    DisableObject(1501078)
    DeleteVFX(1503409, erase_root_only=False)
    DisableObject(1501079)
    DeleteVFX(1503410, erase_root_only=False)
    DisableObject(1501080)
    DeleteVFX(1503411, erase_root_only=False)
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(11502502))
    SkipLinesIfConditionFalse(2, OR_1)
    Kill(1500010)
    End()
    AND_1.Add(PlayerStandingOnCollision(1503212))
    AND_1.Add(FlagEnabled(11510322))
    AND_1.Add(FlagDisabled(11515302))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1502003))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1502004))
    
    MAIN.Await(AND_1)
    
    EnableObject(1501073)
    CreateVFX(1503404)
    EnableObject(1501074)
    CreateVFX(1503405)
    EnableObject(1501075)
    CreateVFX(1503406)
    EnableObject(1501076)
    CreateVFX(1503407)
    EnableObject(1501077)
    CreateVFX(1503408)
    EnableObject(1501078)
    CreateVFX(1503409)
    EnableObject(1501079)
    CreateVFX(1503410)
    EnableObject(1501080)
    CreateVFX(1503411)
    EnableCharacter(1500014)
    FadeInCharacter(character=1500014, duration=0.5)
    Wait(0.5)
    EnableCharacter(1500010)
    FadeInCharacter(character=1500010, duration=0.5)
    Wait(1.0)
    FadeOutCharacter(character=1500014, duration=0.5)
    Wait(0.5)
    DisableCharacter(1500014)
    EnableBossHealthBar(1500010, name=5270)
    EnableSoundEvent(sound_id=1503802)
    
    MAIN.Await(CharacterDead(1500010))
    
    DisableBossHealthBar(1500010)
    DisableSoundEvent(sound_id=1503802)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DeleteVFX(1503404)
    DisableObject(1501074)
    DeleteVFX(1503405)
    DisableObject(1501075)
    DeleteVFX(1503406)
    DisableObject(1501076)
    DeleteVFX(1503407)
    DisableObject(1501077)
    DeleteVFX(1503408)
    DisableObject(1501078)
    DeleteVFX(1503409)
    DisableObject(1501079)
    DeleteVFX(1503410)
    DisableObject(1501080)
    DeleteVFX(1503411)
    DisableObject(1501081)
    AwardItemLot(52700000, host_only=True)
    EnableFlag(11502501)


@NeverRestart(11512007)
def Event_11512007():
    """Event 11512007"""
    DisableMapCollision(collision=1503220)
    EnableMapCollision(collision=1503216)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502017))
    
    EnableMapCollision(collision=1503220)
    DisableMapCollision(collision=1503216)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1502017))
    
    Restart()


@NeverRestart(11512008)
def Event_11512008():
    """Event 11512008"""
    EnableMapCollision(collision=1503219)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502018))
    
    DisableMapCollision(collision=1503219)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1502018))
    
    Restart()


@RestartOnRest(11502009)
def Event_11502009():
    """Event 11502009"""
    DisableSoundEvent(sound_id=1503801)
    DisableCharacter(1500005)
    DisableObject(1501072)
    DeleteVFX(1503400, erase_root_only=False)
    EnableInvincibility(1500012)
    DisableGravity(1500012)
    DisableCharacterCollision(1500012)
    DisableCharacter(1500012)
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(11502502))
    SkipLinesIfConditionFalse(2, OR_1)
    Kill(1500005)
    End()
    DisableCharacter(1500007)
    DisableCharacter(1500008)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502000))
    
    EnableObject(1501072)
    CreateVFX(1503400)
    EnableCharacter(1500012)
    FadeInCharacter(character=1500012, duration=0.5)
    Wait(0.5)
    EnableCharacter(1500005)
    FadeInCharacter(character=1500005, duration=0.5)
    Wait(1.0)
    FadeOutCharacter(character=1500012, duration=0.5)
    Wait(0.5)
    DisableCharacter(1500012)
    EnableBossHealthBar(1500005, name=2360)
    EnableSoundEvent(sound_id=1503801)
    
    MAIN.Await(CharacterDead(1500005))
    
    DisableBossHealthBar(1500005)
    DisableSoundEvent(sound_id=1503801)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    if FlagEnabled(11502010):
        AwardItemLot(23600000, host_only=True)
        EnableFlag(11502500)
    DisableObject(1501072)
    DeleteVFX(1503400)
    EnableFlag(11502009)


@RestartOnRest(11502010)
def Event_11502010():
    """Event 11502010"""
    DisableSoundEvent(sound_id=1503800)
    DisableCharacter(1500006)
    DisableObject(1501069)
    DeleteVFX(1503401, erase_root_only=False)
    DisableObject(1501070)
    DeleteVFX(1503402, erase_root_only=False)
    DisableObject(1501071)
    DeleteVFX(1503403, erase_root_only=False)
    EnableInvincibility(1500013)
    DisableGravity(1500013)
    DisableCharacterCollision(1500013)
    DisableCharacter(1500013)
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(11502502))
    SkipLinesIfConditionFalse(2, OR_1)
    Kill(1500006)
    End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502001))
    
    EnableObject(1501069)
    CreateVFX(1503401)
    EnableObject(1501070)
    CreateVFX(1503402)
    EnableObject(1501071)
    CreateVFX(1503403)
    EnableCharacter(1500013)
    FadeInCharacter(character=1500013, duration=0.5)
    Wait(0.5)
    EnableCharacter(1500006)
    FadeInCharacter(character=1500006, duration=0.5)
    Wait(1.0)
    FadeOutCharacter(character=1500013, duration=0.5)
    Wait(0.5)
    DisableCharacter(1500013)
    EnableBossHealthBar(1500006, name=2360)
    EnableSoundEvent(sound_id=1503800)
    
    MAIN.Await(CharacterDead(1500006))
    
    DisableBossHealthBar(1500006)
    DisableSoundEvent(sound_id=1503800)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    if FlagEnabled(11502009):
        AwardItemLot(23600000, host_only=True)
        EnableFlag(11502500)
        PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DeleteVFX(1503401)
    DisableObject(1501070)
    DeleteVFX(1503402)
    DisableObject(1501071)
    DeleteVFX(1503403)
    EnableFlag(11502010)


@NeverRestart(11512011)
def Event_11512011():
    """Event 11512011"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1502039,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1502501)
    ForceAnimation(PLAYER, 7522)
    Wait(1.0)
    EnableFlag(11813008)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100988)


@NeverRestart(11512200)
def Event_11512200(_, anchor_entity: int):
    """Event 11512200"""
    MAIN.Await(ActionButton(
        prompt_text=10010412,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    DisableCharacterCollision(PLAYER)
    Move(PLAYER, destination=1502502, destination_type=CoordEntityType.Region, set_draw_parent=1503220)
    NightfallCameraResetRequest()
    ForceAnimation(PLAYER, 900)
    Wait(0.5)
    EnableCharacterCollision(PLAYER)
    Restart()


@RestartOnRest(11502502)
def Event_11502502():
    """Event 11502502"""
    DisableSoundEvent(sound_id=1503803)
    DisableCharacter(1500011)
    DisableObject(1501097)
    DisableObject(1501099)
    DisableObject(1501098)
    DeleteVFX(1503416, erase_root_only=False)
    DeleteVFX(1503417, erase_root_only=False)
    DeleteVFX(1503418, erase_root_only=False)
    if ThisEventFlagEnabled():
        Kill(1500011)
        ForceAnimation(1501081, 0, loop=True)
        ForceAnimation(1501082, 0, loop=True)
        ForceAnimation(1501084, 0, loop=True)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502038))
    
    EnableObject(1501097)
    EnableObject(1501099)
    EnableObject(1501098)
    CreateVFX(1503416)
    CreateVFX(1503417)
    CreateVFX(1503418)
    EnableCharacter(1500011)
    FadeInCharacter(character=1500011, duration=2.0)
    EnableBossHealthBar(1500011, name=2371)
    EnableSoundEvent(sound_id=1503803)
    
    MAIN.Await(CharacterDead(1500011))
    
    DisableBossHealthBar(1500011)
    DisableSoundEvent(sound_id=1503803)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1501097)
    DisableObject(1501099)
    DisableObject(1501098)
    DeleteVFX(1503416)
    DeleteVFX(1503417)
    DeleteVFX(1503418)
    ForceAnimation(1501081, 0, loop=True)
    ForceAnimation(1501082, 0, loop=True)
    ForceAnimation(1501084, 0, loop=True)


@NeverRestart(11512012)
def Event_11512012():
    """Event 11512012"""
    if FlagEnabled(11813508):
        DisableObject(1501045)
        End()
    DisableObject(1501044)
    Wait(6.0)
    DisableObject(1501045)
    EnableObject(1501044)
    ForceAnimation(1501044, 0)
    Wait(0.8999999761581421)
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1502024))
    SkipLinesIfConditionFalse(1, OR_7)
    Kill(PLAYER)
    EnableMapCollision(collision=1503206)
    EnableFlag(11512112)
    Wait(5.099999904632568)
    if FlagEnabled(11813508):
        return
    DisableFlag(11512112)
    DisableObject(1501044)
    EnableObject(1501045)
    DisableMapCollision(collision=1503206)
    ForceAnimation(1501045, 0)
    Restart()


@NeverRestart(11412013)
def Event_11412013():
    """Event 11412013"""
    if FlagEnabled(11813508):
        DeleteVFX(1503425, erase_root_only=False)
        DeleteVFX(1503426, erase_root_only=False)
        End()
    AND_1.Add(FlagEnabled(11512112))
    AND_1.Add(ActionButton(
        prompt_text=10010511,
        anchor_entity=1501044,
        anchor_type=CoordEntityType.Object,
        max_distance=4.0,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1501044)
    ForceAnimation(PLAYER, 7114)
    Wait(1.5)
    AwardItemLot(1080, host_only=True)
    EnableFlag(11813508)
    DeleteVFX(1503425)
    DeleteVFX(1503426)


@NeverRestart(11512016)
def Event_11512016():
    """Event 11512016"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502028))
    
    DisableMapCollision(collision=1503240)


@NeverRestart(11502510)
def Event_11502510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11502510"""
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


@NeverRestart(11505510)
def Event_11505510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11505510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()


@NeverRestart(11502600)
def Event_11502600(_, obj: int, obj_act_id: int):
    """Event 11502600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)
