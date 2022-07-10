"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11300000()
    if FlagEnabled(11302100):
        DisableMapCollision(collision=1303200)
        DisableMapCollision(collision=1303201)
        DisableMapCollision(collision=1303202)
        DisableMapCollision(collision=1303204)
        DisableMapCollision(collision=1303207)
        DisableObject(1301048)
    else:
        DisableMapCollision(collision=1303208)
        DisableMapCollision(collision=1303203)
        DisableMapCollision(collision=1303205)
        DisableObject(1301047)
    Event_11302000()
    Event_11302001()
    Event_11302002()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11300000)
def Event_11300000():
    """Event 11300000"""
    RegisterBonfire(bonfire_flag=11300992, obj=1301960)
    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=1301018)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=1301019)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=1301020)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301021)
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=1301022)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=1301023)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=1301024)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=1301025)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=1301026)
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=1301027)
    if FlagEnabled(11302100):
        RegisterLadder(start_climbing_flag=11300030, stop_climbing_flag=11300031, obj=1301047)
    Event_11300300()
    Event_11300350()
    Event_11300900(0, obj_act_id=11300900, obj=1301000, obj_1=1301013, navmesh_id=1304000)
    Event_11300900(1, obj_act_id=11300901, obj=1301001, obj_1=1301014, navmesh_id=1304001)
    Event_11305032(0, obj_act_id=11300902, obj_act_id_1=11300903, flag=11305035, flag_1=11305036)
    Event_11305030(0, flag=11300402, flag_1=11305035, flag_2=11305036, obj=1301002, obj_1=1301015, navmesh_id=1304002)
    Event_11305032(1, obj_act_id=11300904, obj_act_id_1=11300905, flag=11305037, flag_1=11305038)
    Event_11305030(1, flag=11300403, flag_1=11305037, flag_2=11305038, obj=1301003, obj_1=1301016, navmesh_id=1304003)
    Event_11300100(0, flag=11300100, region=1302001, obj=1301004, sound_id=303000000)
    Event_11300100(1, flag=11300101, region=1302002, obj=1301005, sound_id=303100000)
    Event_11300100(2, flag=11300102, region=1302003, obj=1301006, sound_id=303200000)
    Event_11300100(3, flag=11300103, region=1302004, obj=1301007, sound_id=303300000)
    Event_11300100(4, flag=11300104, region=1302005, obj=1301008, sound_id=303400000)
    Event_11300100(5, flag=11300105, region=1302006, obj=1301009, sound_id=303500000)
    Event_11300150()
    Event_11300160()
    Event_11300700(0, obj=1301028, obj_flag=11300750)
    Event_11300700(1, obj=1301029, obj_flag=11300751)
    Event_11300700(2, obj=1301030, obj_flag=11300752)
    Event_11300700(3, obj=1301031, obj_flag=11300753)
    Event_11300700(4, obj=1301032, obj_flag=11300754)
    Event_11300700(5, obj=1301033, obj_flag=11300755)
    Event_11300700(6, obj=1301034, obj_flag=11300756)
    Event_11300700(7, obj=1301035, obj_flag=11300757)
    Event_11300700(8, obj=1301036, obj_flag=11300758)
    Event_11300700(9, obj=1301037, obj_flag=11300759)
    Event_11300700(10, obj=1301038, obj_flag=11300760)
    Event_11300700(12, obj=1301039, obj_flag=11300762)
    Event_11300700(13, obj=1301040, obj_flag=11300763)
    Event_11300700(14, obj=1301041, obj_flag=11300764)
    Event_11300700(15, obj=1301042, obj_flag=11300765)
    Event_11300700(16, obj=1301043, obj_flag=11300766)
    Event_11300700(17, obj=1301044, obj_flag=11300767)
    Event_11300700(18, obj=1301045, obj_flag=11300768)
    Event_11300700(19, 1301046, 11300769)


@NeverRestart(11300700)
def Event_11300700(_, obj: int, obj_flag: int):
    """Event 11300700"""
    MAIN.Await(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=1.5))
    
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=102,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(obj, 0, wait_for_completion=True)
    Restart()


@NeverRestart(11300300)
def Event_11300300():
    """Event 11300300"""
    MAIN.Await(FlagDisabled(11300402))
    
    CreateHazard(
        obj_flag=11300301,
        obj=1301015,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300302,
        obj=1301015,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300303,
        obj=1301015,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300304,
        obj=1301015,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300305,
        obj=1301015,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300306,
        obj=1301015,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300307,
        obj=1301015,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300308,
        obj=1301015,
        model_point=15,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300402))
    
    RemoveObjectFlag(obj_flag=11300301)
    RemoveObjectFlag(obj_flag=11300302)
    RemoveObjectFlag(obj_flag=11300303)
    RemoveObjectFlag(obj_flag=11300304)
    RemoveObjectFlag(obj_flag=11300305)
    RemoveObjectFlag(obj_flag=11300306)
    RemoveObjectFlag(obj_flag=11300307)
    RemoveObjectFlag(obj_flag=11300308)
    Restart()


@NeverRestart(11300350)
def Event_11300350():
    """Event 11300350"""
    MAIN.Await(FlagDisabled(11300403))
    
    CreateHazard(
        obj_flag=11300351,
        obj=1301016,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300352,
        obj=1301016,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300353,
        obj=1301016,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300354,
        obj=1301016,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300355,
        obj=1301016,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300356,
        obj=1301016,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300357,
        obj=1301016,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300358,
        obj=1301016,
        model_point=33,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300359,
        obj=1301016,
        model_point=35,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300360,
        obj=1301016,
        model_point=37,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300361,
        obj=1301016,
        model_point=39,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300403))
    
    RemoveObjectFlag(obj_flag=11300351)
    RemoveObjectFlag(obj_flag=11300352)
    RemoveObjectFlag(obj_flag=11300353)
    RemoveObjectFlag(obj_flag=11300354)
    RemoveObjectFlag(obj_flag=11300355)
    RemoveObjectFlag(obj_flag=11300356)
    RemoveObjectFlag(obj_flag=11300357)
    RemoveObjectFlag(obj_flag=11300358)
    RemoveObjectFlag(obj_flag=11300359)
    RemoveObjectFlag(obj_flag=11300360)
    RemoveObjectFlag(obj_flag=11300361)
    Restart()


@NeverRestart(11300900)
def Event_11300900(_, obj_act_id: int, obj: int, obj_1: int, navmesh_id: int):
    """Event 11300900"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj_1, animation_id=2)
        EndOfAnimation(obj=obj, animation_id=2)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    ForceAnimation(obj_1, 1)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)


@NeverRestart(11305030)
def Event_11305030(_, flag: int, flag_1: int, flag_2: int, obj: int, obj_1: int, navmesh_id: int):
    """Event 11305030"""
    if FlagEnabled(flag):
        DisableObjectActivation(obj, obj_act_id=3011)
        EndOfAnimation(obj=obj_1, animation_id=0)
        EndOfAnimation(obj=obj, animation_id=2)
    else:
        DisableObjectActivation(obj, obj_act_id=3012)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionTrue(6, input_condition=AND_2)
    EnableFlag(flag)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3012)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    Restart()
    DisableFlag(flag)
    ForceAnimation(obj_1, 1)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3011)
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    Restart()


@NeverRestart(11305032)
def Event_11305032(_, obj_act_id: int, obj_act_id_1: int, flag: int, flag_1: int):
    """Event 11305032"""
    AND_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableFlag(flag)
    Restart()
    EnableFlag(flag_1)
    Restart()


@NeverRestart(11300100)
def Event_11300100(_, flag: int, region: int, obj: int, sound_id: int):
    """Event 11300100"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=130000, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.o_Object)


@NeverRestart(11300150)
def Event_11300150():
    """Event 11300150"""
    if ThisEventFlagEnabled():
        PostDestruction(1301010)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1302000))
    
    DestroyObject(1301010)
    PlaySoundEffect(1301010, 303600000, sound_type=SoundType.a_Ambient)


@NeverRestart(11300160)
def Event_11300160():
    """Event 11300160"""
    if ThisEventFlagEnabled():
        DisableObject(1301012)
        End()
    
    MAIN.Await(ObjectDestroyed(1301012))
    
    End()


@NeverRestart(11302000)
def Event_11302000():
    """Event 11302000"""
    MAIN.Await(ActionButton(
        prompt_text=10010501,
        anchor_entity=1300000,
        anchor_type=CoordEntityType.Character,
        max_distance=3.0,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    ForceAnimation(1301011, 1, wait_for_completion=True)
    Wait(2.0)
    SetCameraVibration(vibration_id=101, anchor_entity=1302007, anchor_type=CoordEntityType.Region)
    ForceAnimation(PLAYER, 7050, wait_for_completion=True)
    ForceAnimation(PLAYER, 7052)
    Wait(2.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1302007, anchor_type=CoordEntityType.Region)
    Wait(2.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1302007, anchor_type=CoordEntityType.Region)
    Wait(2.0)
    ForceAnimation(1301011, 0)
    if FlagEnabled(11302100):
        DisableFlag(11302100)
        DisableMapCollision(collision=1303203)
        DisableMapCollision(collision=1303205)
        DisableMapCollision(collision=1303208)
        DisableObject(1301047)
        EnableMapCollision(collision=1303200)
        EnableMapCollision(collision=1303201)
        EnableMapCollision(collision=1303202)
        EnableMapCollision(collision=1303204)
        EnableMapCollision(collision=1303207)
        EnableObject(1301048)
    else:
        EnableFlag(11302100)
        DisableMapCollision(collision=1303200)
        DisableMapCollision(collision=1303201)
        DisableMapCollision(collision=1303202)
        DisableMapCollision(collision=1303204)
        DisableMapCollision(collision=1303207)
        DisableObject(1301048)
        EnableMapCollision(collision=1303208)
        EnableMapCollision(collision=1303205)
        EnableMapCollision(collision=1303203)
        EnableObject(1301047)
        RegisterLadder(start_climbing_flag=11300030, stop_climbing_flag=11300031, obj=1301047)
    Restart()


@NeverRestart(11302001)
def Event_11302001():
    """Event 11302001"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302008))
    AND_1.Add(FlagEnabled(11302100))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11302100)
    DisableMapCollision(collision=1303203)
    DisableMapCollision(collision=1303205)
    DisableMapCollision(collision=1303208)
    DisableObject(1301047)
    EnableMapCollision(collision=1303200)
    EnableMapCollision(collision=1303201)
    EnableMapCollision(collision=1303202)
    EnableMapCollision(collision=1303204)
    EnableMapCollision(collision=1303207)
    EnableObject(1301048)
    Wait(0.5)
    SetCameraVibration(vibration_id=200, anchor_entity=1302009, anchor_type=CoordEntityType.Region)
    Wait(3.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1302009, anchor_type=CoordEntityType.Region)
    Restart()


@NeverRestart(11302002)
def Event_11302002():
    """Event 11302002"""
    AND_1.Add(InsideMap(game_map=ASH_LAKE))
    AND_1.Add(FlagDisabled(11302100))
    
    MAIN.Await(AND_1)
    
    DisableMapPiece(map_piece_id=1303000)
    DisableMapPiece(map_piece_id=1303001)
    DisableMapPiece(map_piece_id=1303002)
    DisableMapPiece(map_piece_id=1303003)
    DisableMapPiece(map_piece_id=1303004)
    DisableMapCollision(collision=1303203)
    DisableMapCollision(collision=1303205)
    DisableMapCollision(collision=1303208)
    DisableMapCollision(collision=1303200)
    DisableMapCollision(collision=1303201)
    DisableMapCollision(collision=1303202)
    DisableMapCollision(collision=1303204)
    DisableMapCollision(collision=1303206)
    DisableMapCollision(collision=1303207)
    DisableMapCollision(collision=1303209)
    DisableObject(1301048)
    DisableObject(1301011)
    DisableObject(1301047)
