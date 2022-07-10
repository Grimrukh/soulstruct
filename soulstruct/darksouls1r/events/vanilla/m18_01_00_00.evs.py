"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    if FlagDisabled(11813104):
        EnableFlag(11813104)
        AddSpecialEffect(PLAYER, 900)
    End()
    Event_11813100()
    Event_11812001()
    Event_11812000()
    RegisterLadder(start_climbing_flag=11810008, stop_climbing_flag=1181009, obj=1811010)
    RegisterLadder(start_climbing_flag=11810010, stop_climbing_flag=11810011, obj=1811011)
    EnableFlag(11810111)
    DisableObjectActivation(1811000, obj_act_id=-1)
    DisableObjectActivation(1811001, obj_act_id=-1)
    DisableObjectActivation(1811002, obj_act_id=-1)
    EndOfAnimation(obj=1811012, animation_id=0)
    Event_11810120()
    Event_11810110()
    Event_11810111()
    Event_11810641(0, item_type=3, item=111, flag=11810601, flag_1=51810800)
    Event_11810641(1, item_type=3, item=270, flag=11810602, flag_1=51810810)
    Event_11810641(2, item_type=3, item=271, flag=11810603, flag_1=51810820)
    Event_11810641(3, item_type=3, item=272, flag=11810604, flag_1=51810830)
    Event_11810641(4, item_type=3, item=275, flag=11810605, flag_1=51810840)
    Event_11810641(5, item_type=3, item=293, flag=11810606, flag_1=51810850)
    Event_11810641(6, item_type=3, item=350, flag=11810607, flag_1=51810860)
    Event_11810641(7, item_type=3, item=500, flag=11810607, flag_1=51810860)
    Event_11810641(8, item_type=3, item=370, flag=11810608, flag_1=51810870)
    Event_11810641(9, item_type=3, item=375, flag=11810609, flag_1=51810880)
    Event_11810641(10, item_type=3, item=376, flag=11810610, flag_1=51810890)
    Event_11810641(11, item_type=3, item=380, flag=11810611, flag_1=51810900)
    Event_11810641(12, item_type=3, item=385, flag=11810612, flag_1=51810910)
    Event_11810641(13, item_type=3, item=501, flag=11810613, flag_1=51810920)
    Event_11810641(14, item_type=0, item=1330000, flag=11810614, flag_1=51810930)
    Event_11810641(15, item_type=0, item=1332000, flag=11810615, flag_1=51810940)
    Event_11810641(16, item_type=0, item=1396000, flag=11810616, flag_1=51810950)
    Event_11810641(17, item_type=1, item=190000, flag=11810617, flag_1=51810960)
    Event_11810641(18, item_type=1, item=290000, flag=11810618, flag_1=51810970)
    Event_11810641(19, item_type=1, item=560000, flag=11810619, flag_1=51810980)
    Event_11810641(20, item_type=2, item=130, flag=11810620, flag_1=51810990)
    Event_11810641(21, item_type=3, item=711, flag=11810621, flag_1=51811000)
    Event_11810600()
    Event_11815110(0, flag=11810601, item_lot=3000, flag_1=51810800)
    Event_11815110(1, flag=11810602, item_lot=3010, flag_1=51810810)
    Event_11815110(2, flag=11810603, item_lot=3020, flag_1=51810820)
    Event_11815110(3, flag=11810604, item_lot=3030, flag_1=51810830)
    Event_11815110(4, flag=11810605, item_lot=3040, flag_1=51810840)
    Event_11815110(5, flag=11810606, item_lot=3050, flag_1=51810850)
    Event_11815110(6, flag=11810607, item_lot=3060, flag_1=51810860)
    Event_11815110(7, flag=11810608, item_lot=3070, flag_1=51810870)
    Event_11815110(8, flag=11810609, item_lot=3080, flag_1=51810880)
    Event_11815110(9, flag=11810610, item_lot=3090, flag_1=51810890)
    Event_11815110(10, flag=11810611, item_lot=3100, flag_1=51810900)
    Event_11815110(11, flag=11810612, item_lot=3110, flag_1=51810910)
    Event_11815110(12, flag=11810613, item_lot=3120, flag_1=51810920)
    Event_11815110(13, flag=11810614, item_lot=3130, flag_1=51810930)
    Event_11815110(14, flag=11810615, item_lot=3140, flag_1=51810940)
    Event_11815110(15, flag=11810616, item_lot=3150, flag_1=51810950)
    Event_11815110(16, flag=11810617, item_lot=3160, flag_1=51810960)
    Event_11815110(17, flag=11810618, item_lot=3170, flag_1=51810970)
    Event_11815110(18, flag=11810619, item_lot=3180, flag_1=51810980)
    Event_11815110(19, flag=11810620, item_lot=3190, flag_1=51810990)
    Event_11815110(20, flag=11810621, item_lot=3200, flag_1=51811000)
    Event_11810100(0, obj_act_id=11810100, obj=1811000, text=10010869)
    Event_11810100(1, obj_act_id=11810101, obj=1811001, text=10010869)
    Event_11810100(2, obj_act_id=11810102, obj=1811002, text=10010869)
    Event_11810100(3, obj_act_id=11810103, obj=1811003, text=10010869)
    Event_11810100(4, obj_act_id=11810104, obj=1811004, text=10010875)
    Event_11810100(5, obj_act_id=11810105, obj=1811005, text=0)
    Event_11810100(6, obj_act_id=11810106, obj=1811006, text=10010871)
    Event_11815150()
    EndOfAnimation(obj=1811009, animation_id=3)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)
    SetRespawnPoint(respawn_point=1812900)


@NeverRestart(11810100)
def Event_11810100(_, obj_act_id: int, obj: int, text: int):
    """Event 11810100"""
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


@NeverRestart(11810120)
def Event_11810120():
    """Event 11810120"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812002))
    AND_2.Add(FlagEnabled(11810105))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1812003))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11810110)
def Event_11810110():
    """Event 11810110"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(1811007, obj_act_id=-1)
        EndOfAnimation(obj=1811007, animation_id=1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=11810110))
    
    EnableFlag(11810110)


@NeverRestart(11810111)
def Event_11810111():
    """Event 11810111"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(1811008, obj_act_id=-1)
        EndOfAnimation(obj=1811008, animation_id=1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=11810111))
    
    EnableFlag(11810111)


@NeverRestart(11810400)
def Event_11810400(
    _,
    class_type: uchar,
    obj: int,
    obj_1: int,
    obj_2: int,
    state: uchar,
    state_1: uchar,
    state_2: uchar,
    state_3: uchar,
):
    """Event 11810400"""
    AND_1.Add(PlayerClass(class_type))
    if not AND_1:
        return
    DisableSoapstoneMessage(1813200)
    DisableSoapstoneMessage(1813201)
    DisableSoapstoneMessage(1813202)
    DisableSoapstoneMessage(1813203)
    DisableSoapstoneMessage(1813204)
    DisableTreasure(obj=1811601)
    DisableTreasure(obj=1811602)
    DisableTreasure(obj=1811603)
    DisableTreasure(obj=1811604)
    DisableTreasure(obj=1811605)
    DisableTreasure(obj=1811606)
    DisableTreasure(obj=1811607)
    DisableTreasure(obj=1811608)
    DisableTreasure(obj=1811609)
    DisableTreasure(obj=1811610)
    DisableTreasure(obj=1811611)
    DisableTreasure(obj=1811612)
    DisableTreasure(obj=1811613)
    DisableTreasure(obj=1811614)
    DisableTreasure(obj=1811615)
    DisableTreasure(obj=1811616)
    DisableTreasure(obj=1811617)
    DisableTreasure(obj=1811618)
    DisableTreasure(obj=1811619)
    DisableTreasure(obj=1811620)
    DisableTreasure(obj=1811621)
    DisableTreasure(obj=1811622)
    DisableTreasure(obj=1811623)
    DisableTreasure(obj=1811624)
    DisableObject(1811601)
    DisableObject(1811602)
    DisableObject(1811603)
    DisableObject(1811604)
    DisableObject(1811605)
    DisableObject(1811606)
    DisableObject(1811607)
    DisableObject(1811608)
    DisableObject(1811609)
    DisableObject(1811610)
    DisableObject(1811611)
    DisableObject(1811612)
    DisableObject(1811613)
    DisableObject(1811614)
    DisableObject(1811615)
    DisableObject(1811616)
    DisableObject(1811617)
    DisableObject(1811618)
    DisableObject(1811619)
    DisableObject(1811620)
    DisableObject(1811621)
    DisableObject(1811622)
    DisableObject(1811623)
    DisableObject(1811624)
    SetSoapstoneMessageState(1813200, state)
    SetSoapstoneMessageState(1813201, state_1)
    SetSoapstoneMessageState(1813202, state_2)
    SetSoapstoneMessageState(1813203, state_2)
    SetSoapstoneMessageState(1813204, state_3)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableObject(obj_2)
    EnableTreasure(obj=obj)
    EnableTreasure(obj=obj_1)
    EnableTreasure(obj=obj_2)


@NeverRestart(11810600)
def Event_11810600():
    """Event 11810600"""
    AND_1.Add(FlagEnabled(11815200))
    AND_2.Add(FlagEnabled(11815201))
    AND_3.Add(FlagEnabled(11815202))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    EnableFlag(11815100)
    DisableFlag(11815101)
    DisableFlag(11815102)
    DisableFlagRange((11815200, 11815202))
    Restart()
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_3)
    DisableFlag(11815100)
    DisableFlag(11815101)
    EnableFlag(11815102)
    DisableFlag(71810093)
    DisableFlagRange((11815200, 11815202))
    Restart()
    DisableFlag(11815100)
    EnableFlag(11815101)
    DisableFlag(11815102)
    DisableFlag(71810092)
    DisableFlagRange((11815200, 11815202))
    Restart()


@NeverRestart(11810641)
def Event_11810641(_, item_type: int, item: int, flag: int, flag_1: int):
    """Event 11810641"""
    MAIN.Await(AnyItemDroppedInRegion(region=1812200))
    
    AND_2.Add(ItemDropped(item=item, item_type=item_type))
    SkipLinesIfConditionTrue(2, AND_2)
    EnableFlag(11815201)
    Restart()
    if FlagDisabled(flag_1):
        EnableFlag(11815200)
        SetNextSnugglyTrade(flag=flag)
        Restart()
    EnableFlag(11815202)
    Restart()


@NeverRestart(11815110)
def Event_11815110(_, flag: int, item_lot: int, flag_1: int):
    """Event 11815110"""
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    WaitFrames(frames=1)
    SnugglyItemDrop(item_lot=item_lot, region=1812201, flag=flag, collision=1813102)


@NeverRestart(11815150)
def Event_11815150():
    """Event 11815150"""
    MAIN.Await(TimeElapsed(seconds=1.0))
    
    EnableFlag(11815151)


@NeverRestart(11813100)
def Event_11813100():
    """Event 11813100"""
    DisableSoundEvent(sound_id=1813810)
    DropMandatoryTreasure(1810000)
    if ThisEventFlagEnabled():
        return
    SetRespawnPoint(respawn_point=1813900)
    ForceAnimation(PLAYER, 7605, loop=True)
    Wait(3.0)
    EnableSoundEvent(sound_id=1813810)
    SetCameraVibration(vibration_id=101, anchor_entity=1812004, anchor_type=CoordEntityType.Region)
    ForceAnimation(PLAYER, 7702)


@NeverRestart(11812000)
def Event_11812000():
    """Event 11812000"""
    if FlagEnabled(11813101):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1812001))
    
    DisableMapPiece(map_piece_id=1813000)
    DisableMapCollision(collision=1813201)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1812001))
    
    EnableMapPiece(map_piece_id=1813000)
    EnableMapCollision(collision=1813201)
    Restart()


@NeverRestart(11812001)
def Event_11812001():
    """Event 11812001"""
    if FlagEnabled(11813101):
        return
    
    MAIN.Await(ActionButton(
        prompt_text=10010000,
        anchor_entity=1812000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    DisableMapCollision(collision=1813200)
    DisableMapCollision(collision=1813202)
    Move(PLAYER, destination=1812500, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 760)
    Wait(0.25)
    ForceAnimation(PLAYER, 900)
    Wait(0.5)
    ForceAnimation(PLAYER, 1500, loop=True)
    Wait(4.75)
    ForceAnimation(PLAYER, 1500)
    EnableMapCollision(collision=1813200)
    EnableMapCollision(collision=1813202)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)
