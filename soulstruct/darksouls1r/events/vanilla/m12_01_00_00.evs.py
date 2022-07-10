"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11210000()
    Event_11212003()
    Event_11212004()
    Event_11212510(
        0,
        flag=11212520,
        flag_1=11212003,
        obj=1211021,
        character=1210001,
        item_lot_param_id=15080,
        item_lot_param_id_1=16080
    )
    Event_11215510(0, 1211021, 11212003, 11212520, 22681, 1.100000023841858)
    Event_11212510(
        1,
        flag=11212520,
        flag_1=11212004,
        obj=1211022,
        character=1210002,
        item_lot_param_id=15080,
        item_lot_param_id_1=16080
    )
    Event_11215510(1, 1211022, 11212004, 11212520, 22681, 1.100000023841858)
    Event_11212501()
    Event_11212510(
        2,
        flag=11212522,
        flag_1=11212501,
        obj=1211023,
        character=1210000,
        item_lot_param_id=15160,
        item_lot_param_id_1=16160
    )
    Event_11215510(2, 1211023, 11212501, 11212522, 22680, 1.100000023841858)
    Event_11212000()
    Event_11212001()
    Event_11212002()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableObject(1211007)
    EnableObjectInvulnerability(1211009)
    Event_11020346()
    Event_11210347()


@NeverRestart(11210000)
def Event_11210000():
    """Event 11210000"""
    RegisterBonfire(bonfire_flag=11210992, obj=1211960)
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=1211010)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=1211011)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=1211012)
    Event_11210025()
    Event_11210100()
    Event_11210103()
    Event_11210140()
    Event_11219100(0, flag=11218102, obj=1211000, animation_id=0, state=1, anchor_entity=1211001)
    Event_11219100(1, flag=11218103, obj=1211000, animation_id=10, state=0, anchor_entity=1211002)
    Event_11210170(0, left=11215220, collision=1213200, region=1212005)
    Event_11210170(4, 11215224, 1213201, 1212010)


@NeverRestart(11020346)
def Event_11020346():
    """Event 11020346"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212011))
    
    AddSpecialEffect(PLAYER, 4161)
    Restart()


@NeverRestart(11210347)
def Event_11210347():
    """Event 11210347"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212012))
    
    if ObjectDestroyed(1211009):
        return
    DisableObjectInvulnerability(1211009)
    DestroyObject(1211009)
    ForceAnimation(1211009, 0)
    PlaySoundEffect(1211009, 262000000, sound_type=SoundType.o_Object)


@NeverRestart(11210025)
def Event_11210025():
    """Event 11210025"""
    if ThisEventFlagEnabled():
        DisableObject(1211008)
        End()
    
    MAIN.Await(ObjectDestroyed(1211008))
    
    End()


@NeverRestart(11210100)
def Event_11210100():
    """Event 11210100"""
    if FlagEnabled(11210101):
        EndOfAnimation(obj=1211000, animation_id=0)
    else:
        EndOfAnimation(obj=1211000, animation_id=10)
    
    MAIN.Await(FlagEnabled(11210103))
    
    MAIN.Await(FlagEnabled(11215220))
    
    AND_1.Add(FlagDisabled(11210101))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212001))
    AND_2.Add(FlagEnabled(11210101))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212000))
    AND_2.Add(FlagEnabled(11210102))
    AND_3.Add(FlagDisabled(11210101))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212002))
    AND_3.Add(FlagEnabled(11210102))
    AND_4.Add(FlagEnabled(11210101))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212003))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionFalse(11, input_condition=AND_3)
    EnableFlag(11210102)
    EnableFlag(11218102)
    AND_5.Add(FlagDisabled(11218102))
    AND_5.Add(FlagDisabled(11218103))
    OR_2.Add(AllPlayersOutsideRegion(region=1212002))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212003))
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_6)
    AND_5.Add(OR_2)
    
    MAIN.Await(AND_5)
    
    SkipLines(32)
    SkipLinesIfFinishedConditionFalse(11, input_condition=AND_1)
    EnableFlag(11210102)
    EnableFlag(11218102)
    AND_7.Add(FlagDisabled(11218102))
    AND_7.Add(FlagDisabled(11218103))
    OR_3.Add(AllPlayersOutsideRegion(region=1212000))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212003))
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_5)
    AND_7.Add(OR_3)
    
    MAIN.Await(AND_7)
    
    SkipLines(20)
    SkipLinesIfFinishedConditionFalse(10, input_condition=AND_4)
    EnableFlag(11218103)
    AND_5.Add(FlagDisabled(11218102))
    AND_5.Add(FlagDisabled(11218103))
    OR_4.Add(AllPlayersOutsideRegion(region=1212003))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212002))
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_4.Add(AND_6)
    AND_5.Add(OR_4)
    
    MAIN.Await(AND_5)
    
    SkipLines(9)
    EnableFlag(11218103)
    AND_5.Add(FlagDisabled(11218102))
    AND_5.Add(FlagDisabled(11218103))
    OR_5.Add(AllPlayersOutsideRegion(region=1212001))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212002))
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_5.Add(AND_6)
    AND_5.Add(OR_5)
    
    MAIN.Await(AND_5)
    
    DisableFlag(11215220)
    Restart()


@NeverRestart(11219100)
def Event_11219100(_, flag: int, obj: int, animation_id: int, state: uchar, anchor_entity: int):
    """Event 11219100"""
    MAIN.Await(FlagEnabled(flag))
    
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=anchor_entity, model_point=101, anchor_type=CoordEntityType.Object)
    SetFlagState(11210101, state)
    CreateObjectVFX(obj, vfx_id=120029, model_point=191)
    ForceAnimation(obj, animation_id)
    WaitFrames(frames=180)
    DeleteObjectVFX(obj, erase_root=False)
    DisableFlag(flag)
    Restart()


@NeverRestart(11210103)
def Event_11210103():
    """Event 11210103"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212004))
    
    EnableFlag(11210103)


@NeverRestart(11210140)
def Event_11210140():
    """Event 11210140"""
    if FlagEnabled(11210141):
        EndOfAnimation(obj=1211004, animation_id=4)
    else:
        EndOfAnimation(obj=1211004, animation_id=14)
    
    MAIN.Await(FlagDisabled(11215224))
    
    AND_1.Add(FlagDisabled(11210141))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212007))
    AND_2.Add(FlagEnabled(11210141))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212006))
    AND_3.Add(FlagDisabled(11210141))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212008))
    AND_4.Add(FlagEnabled(11210141))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212009))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11215224)
    CreateObjectVFX(1211004, vfx_id=120029, model_point=191)
    SkipLinesIfFinishedConditionFalse(11, input_condition=AND_3)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211005, model_point=101, anchor_type=CoordEntityType.Object)
    EnableFlag(11210141)
    ForceAnimation(1211004, 4)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211004, erase_root=False)
    OR_2.Add(AllPlayersOutsideRegion(region=1212008))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212009))
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLines(34)
    SkipLinesIfFinishedConditionFalse(10, input_condition=AND_1)
    EnableFlag(11210141)
    ForceAnimation(1211004, 4)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211004, erase_root=False)
    OR_3.Add(AllPlayersOutsideRegion(region=1212006))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212009))
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    SkipLines(23)
    SkipLinesIfFinishedConditionFalse(12, input_condition=AND_4)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211006, model_point=101, anchor_type=CoordEntityType.Object)
    DisableFlag(11210141)
    CreateObjectVFX(1211004, vfx_id=120029, model_point=191)
    ForceAnimation(1211004, 14)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211004, erase_root=False)
    OR_4.Add(AllPlayersOutsideRegion(region=1212009))
    AND_7.Add(CharacterInsideRegion(PLAYER, region=1212008))
    AND_7.Add(TimeElapsed(seconds=1.0))
    OR_4.Add(AND_7)
    
    MAIN.Await(OR_4)
    
    SkipLines(10)
    DisableFlag(11210141)
    CreateObjectVFX(1211004, vfx_id=120029, model_point=191)
    ForceAnimation(1211004, 14)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211004, erase_root=False)
    OR_5.Add(AllPlayersOutsideRegion(region=1212007))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212008))
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_5.Add(AND_5)
    
    MAIN.Await(OR_5)
    
    DisableFlag(11215224)
    Restart()


@NeverRestart(11210170)
def Event_11210170(_, left: int, collision: int, region: int):
    """Event 11210170"""
    DisableMapCollision(collision=collision)
    if ValueEqual(left=left, right=11215220):
        AND_1.Add(AllPlayersOutsideRegion(region=1212000))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagEnabled(left))
    
    MAIN.Await(AND_1)
    
    EnableMapCollision(collision=collision)
    if ValueEqual(left=left, right=11215220):
        AND_7.Add(CharacterInsideRegion(PLAYER, region=1212000))
        AND_7.Add(TimeElapsed(seconds=2.0))
        OR_1.Add(AND_7)
    OR_1.Add(AllPlayersOutsideRegion(region=region))
    OR_1.Add(FlagDisabled(left))
    
    MAIN.Await(OR_1)
    
    Wait(5.0)
    Restart()


@NeverRestart(11210200)
def Event_11210200(_, obj: int, region: int):
    """Event 11210200"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 620))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 6950))
    OR_1.Add(SkullLanternActive())
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(obj, 262000000, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 1, wait_for_completion=True)
    DisableObject(obj)


@NeverRestart(11210205)
def Event_11210205(_, anchor_entity: int, region: int, flag: int):
    """Event 11210205"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    if FlagEnabled(flag):
        return
    PlaySoundEffect(anchor_entity, 120199999, sound_type=SoundType.o_Object)
    Wait(2.0)
    Restart()


@NeverRestart(11210230)
def Event_11210230(_, obj: int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11210230"""
    if ThisEventSlotFlagDisabled():
        EndOfAnimation(obj=obj_1, animation_id=animation_id_1)
        PostDestruction(obj)
        End()
    DisableTreasure(obj=obj_1)
    SkipLinesIfClient(1)
    CreateObjectVFX(obj_1, vfx_id=99005, model_point=90)
    ForceAnimation(obj_1, animation_id, loop=True)
    
    MAIN.Await(ObjectDestroyed(obj))
    
    ForceAnimation(obj_1, animation_id_1, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)


@NeverRestart(11212000)
def Event_11212000():
    """Event 11212000"""
    DisableMapCollision(collision=1213203)
    
    MAIN.Await(InsideMap(game_map=OOLACILE))
    
    EnableMapCollision(collision=1213203)
    
    MAIN.Await(InsideMap(game_map=ASH_LAKE))
    
    DisableMapCollision(collision=1213203)
    Restart()


@NeverRestart(11212001)
def Event_11212001():
    """Event 11212001"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212016))
    
    DisableMapCollision(collision=1213202)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1212016))
    
    EnableMapCollision(collision=1213202)
    Restart()


@NeverRestart(11212002)
def Event_11212002():
    """Event 11212002"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1212013,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1212500)
    ForceAnimation(PLAYER, 7522)
    Wait(1.0)
    EnableFlag(11813002)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100982)


@RestartOnRest(11212003)
def Event_11212003():
    """Event 11212003"""
    DisableSoundEvent(sound_id=1213800)
    DisableCharacter(1210001)
    DisableObject(1211017)
    DisableObject(1211018)
    DeleteVFX(1213403, erase_root_only=False)
    DeleteVFX(1213404, erase_root_only=False)
    if FlagEnabled(11212500):
        Kill(1210001)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212014))
    
    Wait(2.0)
    EnableObject(1211017)
    EnableObject(1211018)
    CreateVFX(1213403)
    CreateVFX(1213404)
    EnableCharacter(1210001)
    FadeInCharacter(character=1210001, duration=2.0)
    EnableBossHealthBar(1210001, name=5350)
    EnableSoundEvent(sound_id=1213800)
    
    MAIN.Await(CharacterDead(1210001))
    
    EnableFlag(11212500)
    DisableBossHealthBar(1210001)
    DisableSoundEvent(sound_id=1213800)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1211017)
    DisableObject(1211018)
    DeleteVFX(1213403)
    DeleteVFX(1213404)


@RestartOnRest(11212004)
def Event_11212004():
    """Event 11212004"""
    DisableSoundEvent(sound_id=1213801)
    DisableCharacter(1210002)
    DisableObject(1211019)
    DisableObject(1211020)
    DeleteVFX(1213405, erase_root_only=False)
    DeleteVFX(1213406, erase_root_only=False)
    if FlagEnabled(11212500):
        Kill(1210002)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212015))
    
    EnableObject(1211019)
    EnableObject(1211020)
    CreateVFX(1213405)
    CreateVFX(1213406)
    EnableCharacter(1210002)
    FadeInCharacter(character=1210002, duration=2.0)
    EnableBossHealthBar(1210002, name=5350)
    EnableSoundEvent(sound_id=1213801)
    
    MAIN.Await(CharacterDead(1210002))
    
    EnableFlag(11212500)
    DisableBossHealthBar(1210002)
    DisableSoundEvent(sound_id=1213801)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1211019)
    DisableObject(1211020)
    DeleteVFX(1213405)
    DeleteVFX(1213406)


@RestartOnRest(11212501)
def Event_11212501():
    """Event 11212501"""
    DisableSoundEvent(sound_id=1213802)
    DisableCharacter(1210000)
    DisableObject(1211015)
    DisableObject(1211016)
    DeleteVFX(1213401, erase_root_only=False)
    DeleteVFX(1213402, erase_root_only=False)
    if ThisEventFlagEnabled():
        Kill(1210000)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212017))
    
    EnableObject(1211015)
    EnableObject(1211016)
    CreateVFX(1213401)
    CreateVFX(1213402)
    EnableCharacter(1210000)
    FadeInCharacter(character=1210000, duration=2.0)
    EnableBossHealthBar(1210000, name=3471)
    EnableSoundEvent(sound_id=1213802)
    
    MAIN.Await(CharacterDead(1210000))
    
    DisableBossHealthBar(1210000)
    DisableSoundEvent(sound_id=1213802)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1211015)
    DisableObject(1211016)
    DeleteVFX(1213401)
    DeleteVFX(1213402)


@NeverRestart(11212510)
def Event_11212510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11212510"""
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


@NeverRestart(11215510)
def Event_11215510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11215510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()
