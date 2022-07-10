"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11700000()
    Event_11702003()
    Event_11702530(0, destination=1702001, left=1702502, left_1=1701041, left_2=1)
    Event_11702530(1, destination=1702002, left=1702503, left_1=1701042, left_2=1)
    Event_11702530(2, destination=1702008, left=1702504, left_1=1701031, left_2=0)
    Event_11702530(3, destination=1702009, left=1702505, left_1=1701031, left_2=0)
    Event_11702530(4, destination=1702010, left=1702506, left_1=1701035, left_2=0)
    Event_11702530(5, destination=1702011, left=1702507, left_1=1701035, left_2=0)
    Event_11702530(6, destination=1702013, left=1702509, left_1=0, left_2=0)
    OR_7.Add(PlayerDoesNotHaveGood(2008))
    SkipLinesIfConditionFalse(1, OR_7)
    Event_11702530(7, destination=1702012, left=1702508, left_1=0, left_2=0)
    Event_11702530(8, destination=1702014, left=1702510, left_1=0, left_2=0)
    Event_11702530(9, destination=1702016, left=1702512, left_1=0, left_2=0)
    AND_7.Add(PlayerDoesNotHaveGood(2008))
    SkipLinesIfConditionFalse(1, AND_7)
    Event_11702530(10, destination=1702015, left=1702511, left_1=0, left_2=0)
    Event_11702530(11, destination=1702017, left=1702513, left_1=0, left_2=0)
    if FlagDisabled(11700002):
        Event_11702530(12, destination=1702018, left=1702514, left_1=0, left_2=0)
        Event_11702530(13, destination=1702019, left=1702515, left_1=0, left_2=0)
        Event_11702530(14, destination=1702020, left=1702516, left_1=0, left_2=0)
        Event_11702530(15, destination=1702021, left=1702517, left_1=0, left_2=0)
    Event_11702018()
    Event_11702004()
    DisableObject(1701000)
    DisableObject(1701001)
    Event_11702210(0, character__collision=1700019, obj=1701023, vfx_id=1703401, sound_id=1703800, region=1702003)
    Event_11702210(1, character__collision=1700020, obj=1701024, vfx_id=1703402, sound_id=1703801, region=1702004)
    Event_11702500()
    Event_11702510(
        0,
        flag=11702520,
        flag_1=11702500,
        obj=1701044,
        character=1700018,
        item_lot_param_id=15110,
        item_lot_param_id_1=16110
    )
    Event_11705510(0, 1701044, 11702500, 11702520, 22680, 1.2000000476837158)
    Event_11702000()
    Event_11702001()
    Event_11702002()
    Event_11702205(0, 1700002, 1700007, 1700012, 7.0)
    Event_11702205(1, 1700003, 1700008, 1700013, 5.0)
    Event_11702015()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11702005()
    Event_11702006()


@NeverRestart(11700000)
def Event_11700000():
    """Event 11700000"""
    RegisterBonfire(bonfire_flag=11700992, obj=1701960)
    RegisterBonfire(bonfire_flag=11700984, obj=1701961)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=1701025)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=1701026)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=1701013)
    if FlagEnabled(11700002):
        EndOfAnimation(obj=1701030, animation_id=0)
    ForceAnimation(1701028, 1)
    Event_11705103()
    Event_11705101()
    Event_11700110()
    Event_11700120()
    Event_11700160(
        0,
        flag=11700100,
        destination=1701004,
        obj_act_id=11700210,
        obj_act_id_1=11700211,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181
    )
    Event_11700105(
        0,
        flag=11700100,
        obj=1701004,
        obj_1=1701005,
        obj_2=1701006,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181
    )
    Event_11700160(
        1,
        flag=11700102,
        destination=1701016,
        obj_act_id=11700220,
        obj_act_id_1=11700221,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183
    )
    Event_11700105(
        2,
        flag=11700102,
        obj=1701016,
        obj_1=1701017,
        obj_2=1701018,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183
    )
    Event_11700090(0, flag=11700100, state=0, anchor_entity=1701005, flag_1=11705090)
    Event_11700090(1, flag=11700100, state=1, anchor_entity=1701006, flag_1=11705090)
    Event_11700090(2, flag=11700102, state=0, anchor_entity=1701017, flag_1=11705091)
    Event_11700090(3, flag=11700102, state=1, anchor_entity=1701018, flag_1=11705091)
    Event_11705150(0, flag=11700205, destination=1701019, destination_1=1701021)
    Event_11700200(
        0,
        flag=11700205,
        obj=1701019,
        obj_1=1701020,
        collision=1703201,
        collision_1=1703202,
        navmesh_id=1703010,
        navmesh_id_1=1703011,
        flag_1=11705151
    )
    Event_11700200(
        1,
        flag=11700205,
        obj=1701021,
        obj_1=1701022,
        collision=1703203,
        collision_1=1703204,
        navmesh_id=1703012,
        navmesh_id_1=1703013,
        flag_1=11705152
    )
    Event_11700150(0, collision=1703100, region=1702780)
    Event_11700150(1, collision=1703207, region=1702781)
    Event_11702200(0, line_intersects=1701031)
    Event_11700300(1, obj_act_id=11700311, obj=1701032, text=0)
    Event_11700300(2, obj_act_id=11700302, obj=1701033, text=0)
    Event_11700300(3, obj_act_id=11700313, obj=1701034, text=0)
    Event_11702200(1, line_intersects=1701035)
    Event_11700300(5, obj_act_id=11700305, obj=1701036, text=0)
    Event_11700300(6, obj_act_id=11700320, obj=1701037, text=10010867)
    Event_11700140()
    Event_11702600(0, 1701043, 11700600)


@NeverRestart(11700160)
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
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_3.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_1)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_2)
    SkipLinesIfFlagEnabled(8, flag)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 0)
    WaitFrames(frames=105)
    EnableFlag(flag_2)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 2)
    WaitFrames(frames=105)
    EnableFlag(flag_3)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()


@NeverRestart(11700105)
def Event_11700105(_, flag: int, obj: int, obj_1: int, obj_2: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 11700105"""
    if FlagEnabled(flag):
        EndOfAnimation(obj=obj, animation_id=11)
        EnableObjectActivation(obj_1, obj_act_id=-1)
        DisableObjectActivation(obj_2, obj_act_id=-1)
    else:
        DisableObjectActivation(obj_1, obj_act_id=-1)
        EnableObjectActivation(obj_2, obj_act_id=-1)
    AND_1.Add(FlagEnabled(flag_2))
    AND_2.Add(FlagEnabled(flag_3))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    EnableFlag(flag)
    ForceAnimation(obj, 1)
    WaitFrames(frames=300)
    DisableFlag(flag_1)
    SkipLines(4)
    DisableFlag(flag)
    ForceAnimation(obj, 3)
    WaitFrames(frames=344)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11700090)
def Event_11700090(_, flag: int, state: uchar, anchor_entity: int, flag_1: int):
    """Event 11700090"""
    AND_1.Add(FlagState(state, FlagType.Absolute, flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=195,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010170, anchor_entity=anchor_entity)
    Restart()


@NeverRestart(11705150)
def Event_11705150(_, flag: int, destination: int, destination_1: int):
    """Event 11705150"""
    AND_1.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    if FlagDisabled(flag):
        ForceAnimation(destination, 0)
    else:
        ForceAnimation(destination, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_2)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
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


@NeverRestart(11700200)
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
        DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    else:
        EndOfAnimation(obj=obj, animation_id=1)
        DisableMapCollision(collision=collision)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    if FlagDisabled(flag):
        ForceAnimation(obj, 1)
        DisableMapCollision(collision=collision)
        EnableObject(obj_1)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
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
    EnableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=180)
    DisableObject(obj_1)
    EnableMapCollision(collision=collision)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11700110)
def Event_11700110():
    """Event 11700110"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1701010, obj_act_id=-1)
        EndOfAnimation(obj=1701008, animation_id=0)
        EndOfAnimation(obj=1701009, animation_id=0)
        DisableObject(1701007)
        DisableMapCollision(collision=1703205)
        End()
    DisableObject(1701007)
    DisableMapCollision(collision=1703206)
    
    MAIN.Await(ObjectActivated(obj_act_id=11700110))
    
    DisableObjectActivation(1701010, obj_act_id=-1)
    DisableMapCollision(collision=1703205)
    EnableObject(1701007)
    ForceAnimation(1701008, 0)
    EndOfAnimation(obj=1701009, animation_id=0)
    ForceAnimation(1701007, 0, wait_for_completion=True)
    DisableObject(1701007)
    EnableMapCollision(collision=1703206)


@NeverRestart(11700120)
def Event_11700120():
    """Event 11700120"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1701012, obj_act_id=-1)
        EndOfAnimation(obj=1701011, animation_id=0)
        EndOfAnimation(obj=1701014, animation_id=1)
        End()
    OR_1.Add(ObjectActivated(obj_act_id=11700120))
    OR_1.Add(ObjectActivated(obj_act_id=11700121))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11700120)
    ForceAnimation(1701011, 0)
    ForceAnimation(1701014, 1)
    DisplayDialog(text=10010175)


@NeverRestart(11700150)
def Event_11700150(_, collision: int, region: int):
    """Event 11700150"""
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=region))
    
    EnableMapCollision(collision=collision)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DisableMapCollision(collision=collision)
    Restart()


@NeverRestart(11705101)
def Event_11705101():
    """Event 11705101"""
    DisableSoundEvent(sound_id=1703803)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702006))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 5602))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1703803)
    OR_1.Add(CharacterOutsideRegion(PLAYER, region=1702006))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 5602))
    
    MAIN.Await(OR_1)
    
    Restart()


@NeverRestart(11705103)
def Event_11705103():
    """Event 11705103"""
    AND_1.Add(FlagEnabled(61700105))
    AND_1.Add(ObjectActivated(obj_act_id=11705105))
    AND_2.Add(FlagDisabled(61700105))
    AND_2.Add(ObjectActivated(obj_act_id=11705105))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010411, anchor_entity=1701029)
    Wait(3.0)
    Restart()


@NeverRestart(11700140)
def Event_11700140():
    """Event 11700140"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1701027, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701027,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    Move(PLAYER, destination=1701027, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1701027, 0)


@NeverRestart(11700300)
def Event_11700300(_, obj_act_id: int, obj: int, text: int):
    """Event 11700300"""
    if FlagEnabled(obj_act_id):
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if ValueNotEqual(left=text, right=0):
        DisplayDialog(text=text, anchor_entity=obj)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@NeverRestart(11702000)
def Event_11702000():
    """Event 11702000"""
    DisableObjectActivation(1701002, obj_act_id=-1)
    
    MAIN.Await(FlagEnabled(11702100))
    
    EnableObjectActivation(1701002, obj_act_id=-1)
    
    MAIN.Await(ObjectActivated(obj_act_id=11700222))
    
    Wait(1.0)
    WarpToMap(game_map=DUKES_ARCHIVES, player_start=1700991)
    WaitFrames(frames=1)
    Restart()


@NeverRestart(11702001)
def Event_11702001():
    """Event 11702001"""
    DisableObjectActivation(1701003, obj_act_id=-1)
    
    MAIN.Await(FlagEnabled(11702100))
    
    EnableObjectActivation(1701003, obj_act_id=-1)
    
    MAIN.Await(ObjectActivated(obj_act_id=11700223))
    
    Wait(1.0)
    WarpToMap(game_map=DUKES_ARCHIVES, player_start=1700990)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(11702002)
def Event_11702002():
    """Event 11702002"""
    if ThisEventFlagEnabled():
        Move(1700000, destination=1702500, destination_type=CoordEntityType.Region, copy_draw_parent=1703200)
        Move(1700001, destination=1702501, destination_type=CoordEntityType.Region, copy_draw_parent=1703200)
        End()
    Wait(0.10000000149011612)


@RestartOnRest(11702205)
def Event_11702205(_, character: int, character_1: int, character_2: int, radius: float):
    """Event 11702205"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        SetStandbyAnimationSettings(character_2)
        End()
    DisableCharacter(character_1)
    DisableAI(character)
    DisableAI(character_2)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character_2, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    SetStandbyAnimationSettings(character_2, cancel_animation=9060)
    EnableAI(character_2)
    SkipLinesIfFinishedConditionFalse(3, input_condition=OR_1)
    EnableAI(character)
    End()
    SkipLines(2)
    EnableCharacter(character_1)
    DisableCharacter(character)


@RestartOnRest(11702015)
def Event_11702015():
    """Event 11702015"""
    if ThisEventFlagEnabled():
        DisableCharacter(1700004)
        DisableCharacter(1700005)
        DisableCharacter(1700006)
        SetStandbyAnimationSettings(1700014)
        SetStandbyAnimationSettings(1700015)
        SetStandbyAnimationSettings(1700016)
        End()
    DisableCharacter(1700009)
    DisableCharacter(1700010)
    DisableCharacter(1700011)
    DisableAI(1700004)
    DisableAI(1700005)
    DisableAI(1700006)
    DisableAI(1700014)
    DisableAI(1700015)
    DisableAI(1700016)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1702000))
    
    Wait(3.0)
    EnableAI(1700014)
    EnableAI(1700004)
    SetStandbyAnimationSettings(1700014, cancel_animation=9060)
    AND_1.Add(CharacterAlive(1700004))
    AND_1.Add(CharacterAlive(1700014))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableCharacter(1700009)
    DisableCharacter(1700004)
    Wait(2.5)
    EnableAI(1700015)
    EnableAI(1700005)
    SetStandbyAnimationSettings(1700015, cancel_animation=9060)
    AND_2.Add(CharacterAlive(1700005))
    AND_2.Add(CharacterAlive(1700015))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableCharacter(1700010)
    DisableCharacter(1700005)
    Wait(1.5)
    EnableAI(1700016)
    EnableAI(1700006)
    SetStandbyAnimationSettings(1700016, cancel_animation=9060)
    AND_3.Add(CharacterAlive(1700006))
    AND_3.Add(CharacterAlive(1700016))
    SkipLinesIfConditionFalse(2, AND_3)
    EnableCharacter(1700011)
    DisableCharacter(1700006)
    End()


@RestartOnRest(11702210)
def Event_11702210(_, character__collision: int, obj: int, vfx_id: int, sound_id: int, region: int):
    """Event 11702210"""
    DisableSoundEvent(sound_id=sound_id)
    DisableCharacter(character__collision)
    DisableObject(obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    if FlagEnabled(11702100):
        Kill(character__collision)
        End()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(FlagEnabled(11702100))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(11702100):
        Kill(character__collision)
        End()
    EnableObject(obj)
    CreateVFX(vfx_id)
    EnableCharacter(character__collision)
    SetTeamType(character__collision, TeamType.HostileAlly)
    ForceAnimation(character__collision, 6951, wait_for_completion=True)
    EnableBossHealthBar(character__collision, name=5410)
    EnableImmortality(character__collision)
    EnableSoundEvent(sound_id=sound_id)
    
    MAIN.Await(HealthRatioLessThanOrEqual(character__collision, value=0.20000000298023224))
    
    Wait(0.5)
    DisableGravity(character__collision)
    DisableMapCollision(collision=character__collision)
    ResetAnimation(character__collision)
    ForceAnimation(character__collision, 6303)
    FadeOutCharacter(character=character__collision, duration=1.5)
    Wait(1.399999976158142)
    DisableCharacter(character__collision)
    DisableBossHealthBar(character__collision)
    DisableSoundEvent(sound_id=sound_id)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    EnableFlag(11702100)


@NeverRestart(11702018)
def Event_11702018():
    """Event 11702018"""
    MAIN.Await(FlagEnabled(11012109))
    
    DisableMapCollision(collision=1703208)
    DisableMapCollision(collision=1703209)
    
    MAIN.Await(FlagDisabled(11012109))
    
    EnableMapCollision(collision=1703208)
    EnableMapCollision(collision=1703209)
    Restart()


@RestartOnRest(11702500)
def Event_11702500():
    """Event 11702500"""
    DisableSoundEvent(sound_id=1703802)
    DisableCharacter(1700018)
    DisableObject(1701038)
    DeleteVFX(1703400, erase_root_only=False)
    if ThisEventFlagEnabled():
        Kill(1700018)
        RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701039)
        End()
    DisableObject(1701039)
    DisableObject(1701040)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1702005))
    
    EnableObject(1701038)
    CreateVFX(1703400)
    EnableCharacter(1700018)
    FadeInCharacter(character=1700018, duration=2.0)
    EnableBossHealthBar(1700018, name=5290)
    EnableSoundEvent(sound_id=1703802)
    
    MAIN.Await(CharacterDead(1700018))
    
    DisableBossHealthBar(1700018)
    DisableSoundEvent(sound_id=1703802)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1701038)
    DeleteVFX(1703400)
    EnableObject(1701039)
    EnableObject(1701040)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701039)


@NeverRestart(11702003)
def Event_11702003():
    """Event 11702003"""
    if FlagEnabled(11813507):
        return
    AND_1.Add(FlagDisabled(11813507))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701041,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1701041,
    ))
    AND_2.Add(FlagDisabled(11813507))
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1701042,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1701042,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010409)
    Wait(2.0)
    Restart()


@NeverRestart(11702004)
def Event_11702004():
    """Event 11702004"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1702006))
    
    DisableMapCollision(collision=1703210)
    DisableMapCollision(collision=1703211)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1702006))
    
    EnableMapCollision(collision=1703210)
    EnableMapCollision(collision=1703211)
    Restart()


@NeverRestart(11702200)
def Event_11702200(_, line_intersects: int):
    """Event 11702200"""
    if FlagEnabled(11813507):
        return
    AND_1.Add(FlagDisabled(11813507))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=line_intersects,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=line_intersects,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010409)
    Wait(2.0)
    Restart()


@RestartOnRest(11702005)
def Event_11702005():
    """Event 11702005"""
    if FlagEnabled(11702006):
        return
    AND_1.Add(FlagDisabled(11702006))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702007))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(1700017, 680)


@RestartOnRest(11702006)
def Event_11702006():
    """Event 11702006"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(1700017)
        Kill(1700017)
        End()
    
    MAIN.Await(CharacterDead(1700017))
    
    AwardItemLot(6500, host_only=True)


@NeverRestart(11702510)
def Event_11702510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11702510"""
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


@NeverRestart(11705510)
def Event_11705510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11705510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()


@NeverRestart(11702530)
def Event_11702530(_, destination: int, left: int, left_1: int, left_2: int):
    """Event 11702530"""
    if ValueEqual(left=left_1, right=0):
        AND_1.Add(FlagEnabled(11813507))
        AND_1.Add(ActionButton(
            prompt_text=10010408,
            anchor_entity=destination,
            anchor_type=CoordEntityType.Region,
            trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        ))
    
        MAIN.Await(AND_1)
    else:
        AND_2.Add(FlagEnabled(11813507))
        AND_2.Add(ActionButton(
            prompt_text=10010408,
            anchor_entity=destination,
            anchor_type=CoordEntityType.Region,
            trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
            line_intersects=left_1,
        ))
    
        MAIN.Await(AND_2)
    if ValueEqual(left=left, right=0):
        Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    else:
        MoveToEntity(PLAYER, destination=left, destination_type=CoordEntityType.Region)
    if ValueEqual(left=left_2, right=1):
        NightfallCameraResetRequest()
    ForceAnimation(PLAYER, 7410)
    Wait(2.0)
    Restart()


@NeverRestart(11702600)
def Event_11702600(_, obj: int, obj_act_id: int):
    """Event 11702600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)
