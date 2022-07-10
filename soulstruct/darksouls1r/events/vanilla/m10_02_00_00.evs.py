"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11020000()
    Event_11020020()
    Event_11020021()
    Event_11022002()
    Event_11022000()
    Event_11022001()


@NeverRestart(11020000)
def Event_11020000():
    """Event 11020000"""
    RegisterBonfire(bonfire_flag=11020992, obj=1021960)
    SkipLinesIfFlagDisabled(4, 11020300)
    SkipLinesIfFlagEnabled(2, 11020302)
    EndOfAnimation(obj=1021000, animation_id=11)
    SkipLines(1)
    EndOfAnimation(obj=1021000, animation_id=12)
    if FlagDisabled(11020300):
        Event_11020300()
    else:
        Event_11020301()
    Event_11020120()
    Event_11020121()
    Event_11020350()
    Event_11020351()
    Event_11020352()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11020300)
def Event_11020300():
    """Event 11020300"""
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1022003))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11020300)
    EnableFlag(11020302)
    ForceAnimation(1021000, 0, wait_for_completion=True)
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022001))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022002))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()


@NeverRestart(11020301)
def Event_11020301():
    """Event 11020301"""
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(11020302))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1022000))
    AND_2.Add(Singleplayer())
    AND_2.Add(FlagEnabled(11020302))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1022001))
    AND_3.Add(Singleplayer())
    AND_3.Add(FlagEnabled(11020302))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1022002))
    AND_4.Add(Singleplayer())
    AND_4.Add(FlagDisabled(11020302))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1022003))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(7, input_condition=AND_3)
    EnableFlag(11020302)
    ForceAnimation(1021000, 2, wait_for_completion=True)
    AND_5.Add(CharacterOutsideRegion(PLAYER, region=1022001))
    AND_5.Add(CharacterOutsideRegion(PLAYER, region=1022002))
    
    MAIN.Await(AND_5)
    
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()
    DisableFlag(11020302)
    ForceAnimation(1021000, 1, wait_for_completion=True)
    AND_6.Add(CharacterOutsideRegion(PLAYER, region=1022000))
    AND_6.Add(CharacterOutsideRegion(PLAYER, region=1022003))
    
    MAIN.Await(AND_6)
    
    ForceAnimation(1021000, 21, wait_for_completion=True)
    Restart()


@NeverRestart(11020020)
def Event_11020020():
    """Event 11020020"""
    MAIN.Await(ActionButton(
        prompt_text=10010506,
        anchor_entity=1022005,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    EnableFlag(11025060)
    WaitFrames(frames=3)
    AND_1.Add(ActionButton(
        prompt_text=10010507,
        anchor_entity=1022005,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1022005))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11025060)
    RestartEvent(event_id=11020021)
    ResetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


@NeverRestart(11020021)
def Event_11020021():
    """Event 11020021"""
    MAIN.Await(FlagEnabled(11025060))
    
    Wait(20.0)
    DisableFlag(11025060)
    ResetStandbyAnimationSettings(PLAYER)
    Restart()


@NeverRestart(11020120)
def Event_11020120():
    """Event 11020120"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=1021001, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1021001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1021001, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(1021001, 0)


@NeverRestart(11020121)
def Event_11020121():
    """Event 11020121"""
    if FlagEnabled(11020120):
        return
    AND_1.Add(FlagDisabled(11020120))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1021001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1021001)
    Restart()


@NeverRestart(11020350)
def Event_11020350():
    """Event 11020350"""
    if ThisEventFlagEnabled():
        DisableObject(1021002)
        DisableMapCollision(collision=1023201)
        DisableMapPiece(map_piece_id=1023501)
        DisableMapCollision(collision=1023202)
        End()
    DisableObject(1021003)
    DisableMapCollision(collision=1023203)
    
    MAIN.Await(FlagEnabled(11020350))
    
    EnableObject(1021003)
    EnableMapCollision(collision=1023203)
    DisableObject(1021002)
    DisableMapCollision(collision=1023201)
    DisableMapPiece(map_piece_id=1023501)
    DisableMapCollision(collision=1023202)


@NeverRestart(11020351)
def Event_11020351():
    """Event 11020351"""
    if FlagEnabled(11020350):
        Kill(PLAYER)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1022004))
    
    Kill(PLAYER)


@NeverRestart(11020352)
def Event_11020352():
    """Event 11020352"""
    MAIN.Await(FlagEnabled(11020350))
    
    DisableMapCollision(collision=1023204)
    DisableMapCollision(collision=1023205)


@NeverRestart(11022000)
def Event_11022000():
    """Event 11022000"""
    MAIN.Await(InsideMap(game_map=SENS_FORTRESS))
    
    DisableMapCollision(collision=1023200)
    
    MAIN.Await(InsideMap(game_map=FIRELINK_SHRINE))
    
    EnableMapCollision(collision=1023200)
    Restart()


@NeverRestart(11022001)
def Event_11022001():
    """Event 11022001"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1022006,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1022500)
    ForceAnimation(PLAYER, 7114)
    Wait(2.0)
    EnableFlag(11813004)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100984)


@RestartOnRest(11022002)
def Event_11022002():
    """Event 11022002"""
    End()
