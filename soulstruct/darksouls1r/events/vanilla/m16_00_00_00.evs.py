"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11600000()
    Event_11602000()
    Event_11602001()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    if FlagDisabled(11600202):
        EnableFlag(11600211)
        EnableFlag(11600221)
        EnableFlag(11600202)
    Wait(0.10000000149011612)


@NeverRestart(11600000)
def Event_11600000():
    """Event 11600000"""
    RegisterBonfire(bonfire_flag=11600992, obj=1601960)
    RegisterBonfire(bonfire_flag=11600984, obj=1601961)
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=1601005)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=1601014)
    Event_11600100()
    Event_11600101()
    Event_11600160()
    Event_11600210()
    Event_11600251()
    Event_11600220()
    Event_11600252()
    Event_11600810()
    Event_11600400()


@NeverRestart(11600100)
def Event_11600100():
    """Event 11600100"""
    DisableMapCollision(collision=1603100)
    DisableMapCollision(collision=1603102)
    DisableMapCollision(collision=1603103)
    DisableMapCollision(collision=1603104)
    DisableObject(1601004)
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1601000, animation_id=10)
        EndOfAnimation(obj=1601001, animation_id=0)
        End()
    AND_1.Add(FlagEnabled(11600101))
    AND_2.Add(FlagEnabled(11012004))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11600100)
    SaveRequest()
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    ForceAnimation(1601000, 0, wait_for_completion=True)
    SkipLines(1)
    ForceAnimation(1601000, 1, wait_for_completion=True)
    ForceAnimation(1601000, 10)


@NeverRestart(11600101)
def Event_11600101():
    """Event 11600101"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1601000, animation_id=10)
        EndOfAnimation(obj=1601001, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010502,
        anchor_entity=1601001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1601001, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1601001, 0, wait_for_completion=True)


@NeverRestart(11600160)
def Event_11600160():
    """Event 11600160"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1601006, animation_id=0)
        RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601006)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010500,
        anchor_entity=1601006,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    EnableFlag(11600160)
    Move(PLAYER, destination=1601006, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1601006, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601006)


@NeverRestart(11600210)
def Event_11600210():
    """Event 11600210"""
    if FlagEnabled(11600211):
        EndOfAnimation(obj=1601007, animation_id=22)
        DisableObjectActivation(1601008, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601007, animation_id=21)
        DisableObjectActivation(1601009, obj_act_id=6101)
    if ThisEventFlagDisabled():
        DisableObjectActivation(1601009, obj_act_id=6101)
    AND_1.Add(FlagDisabled(11600211))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602003))
    AND_2.Add(FlagEnabled(11600211))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602002))
    AND_3.Add(ObjectActivated(obj_act_id=11600212))
    AND_4.Add(ObjectActivated(obj_act_id=11600213))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    SkipLines(9)
    EnableFlag(11600211)
    DisableObjectActivation(1601008, obj_act_id=6101)
    ForceAnimation(1601007, 10, wait_for_completion=True)
    ForceAnimation(1601007, 2, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602002))
    
    ForceAnimation(1601007, 22, wait_for_completion=True)
    EnableObjectActivation(1601009, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(1601009, obj_act_id=6101)
    ForceAnimation(1601007, 13, wait_for_completion=True)
    ForceAnimation(1601007, 3, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602003))
    
    ForceAnimation(1601007, 21, wait_for_completion=True)
    EnableObjectActivation(1601008, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


@NeverRestart(11600251)
def Event_11600251():
    """Event 11600251"""
    AND_1.Add(FlagDisabled(11605121))
    AND_1.Add(FlagEnabled(11600211))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601008,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605121))
    AND_2.Add(FlagDisabled(11600211))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601009,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600210))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601009,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@NeverRestart(11600220)
def Event_11600220():
    """Event 11600220"""
    if FlagEnabled(11600221):
        EndOfAnimation(obj=1601010, animation_id=24)
        DisableObjectActivation(1601011, obj_act_id=6101)
    else:
        EndOfAnimation(obj=1601010, animation_id=21)
        DisableObjectActivation(1601012, obj_act_id=6101)
    if ThisEventFlagDisabled():
        DisableObjectActivation(1601012, obj_act_id=6101)
    AND_1.Add(FlagDisabled(11600221))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602005))
    AND_2.Add(FlagEnabled(11600221))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602004))
    AND_3.Add(ObjectActivated(obj_act_id=11600222))
    AND_4.Add(ObjectActivated(obj_act_id=11600223))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    SkipLines(9)
    EnableFlag(11600221)
    DisableObjectActivation(1601011, obj_act_id=6101)
    ForceAnimation(1601010, 10, wait_for_completion=True)
    ForceAnimation(1601010, 4, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602004))
    
    ForceAnimation(1601010, 24, wait_for_completion=True)
    EnableObjectActivation(1601012, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(1601012, obj_act_id=6101)
    ForceAnimation(1601010, 15, wait_for_completion=True)
    ForceAnimation(1601010, 5, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602005))
    
    ForceAnimation(1601010, 21, wait_for_completion=True)
    EnableObjectActivation(1601011, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


@NeverRestart(11600252)
def Event_11600252():
    """Event 11600252"""
    AND_1.Add(FlagDisabled(11605122))
    AND_1.Add(FlagEnabled(11600221))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605122))
    AND_2.Add(FlagDisabled(11600221))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601012,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600220))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1601012,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@RestartOnRest(11600810)
def Event_11600810():
    """Event 11600810"""
    if ThisEventFlagEnabled():
        DisableCharacter(1600500)
        End()
    
    MAIN.Await(CharacterDead(1600500))
    
    AwardItemLot(34200200, host_only=True)


@RestartOnRest(11600400)
def Event_11600400():
    """Event 11600400"""
    DisableCharacterCollision(1600500)
    DisableGravity(1600500)
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(1600500, cancel_animation=29060)
        End()
    OR_1.Add(EntityWithinDistance(entity=1600500, other_entity=PLAYER, radius=10.0))
    OR_1.Add(Attacked(attacked_entity=1600500, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ResetStandbyAnimationSettings(1600500)
    ForceAnimation(1600500, 29060)


@NeverRestart(11602000)
def Event_11602000():
    """Event 11602000"""
    MAIN.Await(ObjectActivated(obj_act_id=11600120))
    
    Wait(0.75)
    WarpToMap(game_map=DEPTHS, player_start=1000990)


@NeverRestart(11602001)
def Event_11602001():
    """Event 11602001"""
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1602006,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1601013,
    ))
    
    if ThisEventFlagDisabled():
        DisplayDialog(text=10010162)
        Wait(1.0)
    WarpToMap(game_map=UNDEAD_BURG, player_start=1010990)
