"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11410000()
    Event_11412500()
    Event_11412004()
    Event_11412510(
        0,
        flag=11412520,
        flag_1=11412500,
        obj=1411067,
        character=1410030,
        item_lot_param_id=15010,
        item_lot_param_id_1=16010
    )
    Event_11415510(0, 1411067, 11412500, 11412520, 22681, 1.2000000476837158)
    Event_11412501()
    Event_11412007()
    Event_11412008()
    Event_11412502()
    Event_11412510(
        2,
        flag=11412522,
        flag_1=11412502,
        obj=1411068,
        character=1410032,
        item_lot_param_id=15120,
        item_lot_param_id_1=16120
    )
    Event_11415510(2, 1411068, 11412502, 11412522, 22679, 3.200000047683716)
    Event_11412000()
    Event_11412001()
    Event_11412200(0, character=1410001, region=1412675, set_draw_parent=1413203, flag=11412200)
    Event_11412200(1, character=1410002, region=1412677, set_draw_parent=1413202, flag=11412201)
    Event_11412200(2, character=1410003, region=1412676, set_draw_parent=1413204, flag=11412202)
    Event_11412200(3, character=1410004, region=1412675, set_draw_parent=1413203, flag=11412203)
    Event_11415100(1, 1410007, 1410007, 9060, 15.0, 0.0)
    Event_11415100(2, 1410008, 1410008, 9060, 15.0, 0.0)
    Event_11415100(3, 1410009, 1410009, 9060, 15.0, 0.0)
    Event_11415100(4, 1410010, 1410010, 9060, 7.0, 0.0)
    Event_11415100(5, 1410011, 1410011, 9060, 5.0, 0.0)
    Event_11415120(0, region=1412000, region_1=1412500, flag=11415130)
    Event_11415120(1, region=1412001, region_1=1412501, flag=11415131)
    Event_11415120(2, region=1412002, region_1=1412502, flag=11415132)
    Event_11415120(3, region=1412003, region_1=1412503, flag=11415133)
    Event_11415120(4, region=1412004, region_1=1412504, flag=11415134)
    Event_11415000()
    Event_11415110(
        0,
        character=1410017,
        character_1=1410018,
        character_2=1410019,
        character_3=1410020,
        character_4=1410021,
        character_5=1410022
    )
    Event_11415110(
        1,
        character=1410023,
        character_1=1410024,
        character_2=1410025,
        character_3=1410026,
        character_4=1410027,
        character_5=1410028
    )
    Event_11412900(0, character=1410002, item_lot_param_id=0)
    Event_11412900(1, character=1410006, item_lot_param_id=0)
    Event_11412005()
    Event_11412006()
    Event_11412015()
    Event_11412002()
    Event_11412003()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_11412010()
    Event_11410500(0, character=6000, flag=1018, left=71410033)
    Event_11410510(0, 6000, 1000, 1019, 1019)


@NeverRestart(11410000)
def Event_11410000():
    """Event 11410000"""
    RegisterBonfire(bonfire_flag=11410992, obj=1411960)
    RegisterBonfire(bonfire_flag=11410984, obj=1411961)
    Event_11412009()
    Event_11412013()
    Event_11412014()
    Event_11410340()
    Event_11410341()
    Event_11410350()
    Event_11410360()
    Event_11415399()
    Event_11410200()
    Event_11410201(0, obj=1411010, sound_id=462000000)
    Event_11410201(1, obj=1411011, sound_id=462100000)
    Event_11410201(2, obj=1411012, sound_id=462200000)
    Event_11410201(3, obj=1411013, sound_id=462300000)
    Event_11410201(4, obj=1411014, sound_id=462400000)
    Event_11410201(5, obj=1411015, sound_id=462500000)
    Event_11410201(6, obj=1411016, sound_id=462600000)
    Event_11410201(7, obj=1411017, sound_id=462700000)
    Event_11410201(8, obj=1411018, sound_id=462800000)
    Event_11410201(9, obj=1411019, sound_id=462900000)
    Event_11410201(10, obj=1411020, sound_id=463000000)
    Event_11410201(11, obj=1411021, sound_id=463100000)
    Event_11410201(12, obj=1411022, sound_id=463200000)
    Event_11412600(0, obj=1411001, obj_act_id=11410600)
    Event_11412600(1, 1411000, 11410601)


@NeverRestart(11415399)
def Event_11415399():
    """Event 11415399"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412023))
    
    Wait(0.5)
    DisableMapCollision(collision=1413200)
    ForceAnimation(PLAYER, 1510, loop=True, skip_transition=True)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412023))
    
    Wait(3.0)
    DisableInvincibility(PLAYER)


@NeverRestart(11410200)
def Event_11410200():
    """Event 11410200"""
    if ThisEventFlagEnabled():
        DisableObject(1411005)
        DisableObject(1411006)
        DisableObject(1411007)
        DisableObject(1411008)
        DisableObject(1411009)
        End()
    RestoreObject(1411005)
    EnableObjectInvulnerability(1411005)
    RestoreObject(1411006)
    EnableObjectInvulnerability(1411006)
    RestoreObject(1411007)
    EnableObjectInvulnerability(1411007)
    RestoreObject(1411008)
    EnableObjectInvulnerability(1411008)
    RestoreObject(1411009)
    EnableObjectInvulnerability(1411009)
    End()
    EnableFlag(11410200)
    DisableObjectInvulnerability(1411005)
    DisableObjectInvulnerability(1411006)
    DisableObjectInvulnerability(1411007)
    DisableObjectInvulnerability(1411008)
    DisableObjectInvulnerability(1411009)
    CreateTemporaryVFX(vfx_id=140009, anchor_entity=1411007, anchor_type=CoordEntityType.Object)
    DestroyObject(1411005)
    PlaySoundEffect(1411005, 463300000, sound_type=SoundType.o_Object)
    WaitFrames(frames=4)
    DestroyObject(1411006)
    PlaySoundEffect(1411006, 463400000, sound_type=SoundType.o_Object)
    WaitFrames(frames=3)
    DestroyObject(1411007)
    PlaySoundEffect(1411007, 463500000, sound_type=SoundType.o_Object)
    WaitFrames(frames=2)
    DestroyObject(1411008)
    PlaySoundEffect(1411008, 463600000, sound_type=SoundType.o_Object)
    WaitFrames(frames=1)
    DestroyObject(1411009)
    PlaySoundEffect(1411009, 463700000, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(1411005)
    DisableObject(1411008)
    DisableObject(1411009)


@NeverRestart(11410201)
def Event_11410201(_, obj: int, sound_id: int):
    """Event 11410201"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    End()
    DisableObjectInvulnerability(obj)
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=140008, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(obj)


@NeverRestart(11410340)
def Event_11410340():
    """Event 11410340"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1411060, animation_id=1)
        End()
    AND_1.Add(PlayerHasGood(813))
    AND_1.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412007,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411060,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412006,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411060,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11410340)
    RotateToFaceEntity(PLAYER, target_entity=1411060)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    DisplayStatus(10040005)
    Wait(2.0)
    ForceAnimation(1411060, 1)
    CreateTemporaryVFX(vfx_id=140000, anchor_entity=1411060, anchor_type=CoordEntityType.Object)


@NeverRestart(11410341)
def Event_11410341():
    """Event 11410341"""
    if FlagEnabled(11410340):
        return
    AND_1.Add(PlayerDoesNotHaveGood(813))
    AND_1.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412007,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411060,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayStatus(10040004)
    Wait(5.0)
    Restart()


@NeverRestart(11410360)
def Event_11410360():
    """Event 11410360"""
    if ThisEventFlagEnabled():
        DisableObject(1411004)
        End()
    
    MAIN.Await(ObjectDestroyed(1411004))
    
    EnableFlag(11410360)


@NeverRestart(11412009)
def Event_11412009():
    """Event 11412009"""
    if FlagEnabled(11410401):
        DisableObject(1411063)
        EnableObject(1411062)
        EndOfAnimation(obj=1411062, animation_id=0)
    else:
        DisableObject(1411062)
        EnableObject(1411063)
        EndOfAnimation(obj=1411063, animation_id=2)
    DisableFlag(11410403)
    AND_1.Add(FlagEnabled(11410401))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412017))
    AND_2.Add(FlagDisabled(11410401))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1412018))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11410403)
    CreateObjectVFX(1411062, vfx_id=140002, model_point=100)
    CreateObjectVFX(1411063, vfx_id=140002, model_point=100)
    SkipLinesIfFinishedConditionFalse(12, input_condition=AND_1)
    DisableFlag(11410401)
    Event_11412011()
    EnableObject(1411063)
    ForceAnimation(1411062, 1)
    ForceAnimation(1411063, 1, wait_for_completion=True)
    StopEvent(event_id=11412011)
    DeleteObjectVFX(1411062)
    DisableObject(1411062)
    DeleteObjectVFX(1411063)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412018))
    
    ForceAnimation(1411063, 5, wait_for_completion=True)
    Restart()
    EnableFlag(11410401)
    EnableFlag(11412109)
    Event_11412012()
    EnableObject(1411062)
    ForceAnimation(1411063, 3)
    ForceAnimation(1411062, 3, wait_for_completion=True)
    StopEvent(event_id=11412012)
    DeleteObjectVFX(1411063)
    DisableObject(1411063)
    DeleteObjectVFX(1411062)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412017))
    
    ForceAnimation(1411062, 4, wait_for_completion=True)
    Restart()


@NeverRestart(11412011)
def Event_11412011():
    """Event 11412011"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412019))
    
    MoveToEntity(PLAYER, destination=1412020, destination_type=CoordEntityType.Region)
    NightfallCameraResetRequest()
    End()


@NeverRestart(11412012)
def Event_11412012():
    """Event 11412012"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412020))
    
    WaitFrames(frames=2)
    MoveToEntity(PLAYER, destination=1412019, destination_type=CoordEntityType.Region)
    NightfallCameraResetRequest()
    End()


@NeverRestart(11412013)
def Event_11412013():
    """Event 11412013"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412021))
    AND_1.Add(FlagEnabled(11412109))
    AND_1.Add(FlagDisabled(11410401))
    AND_1.Add(FlagDisabled(11410403))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11410401)
    EnableFlag(11410403)
    DisableObject(1411063)
    EnableObject(1411062)
    ForceAnimation(1411062, 3, wait_for_completion=True)
    DeleteObjectVFX(1411062)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412017))
    
    ForceAnimation(1411062, 4, wait_for_completion=True)
    DisableFlag(11410403)
    Restart()


@NeverRestart(11412014)
def Event_11412014():
    """Event 11412014"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412022))
    AND_1.Add(FlagEnabled(11410401))
    AND_1.Add(FlagDisabled(11410403))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11410401)
    EnableFlag(11410403)
    DisableObject(1411062)
    EnableObject(1411063)
    ForceAnimation(1411063, 1, wait_for_completion=True)
    DeleteObjectVFX(1411063)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412018))
    
    ForceAnimation(1411063, 5, wait_for_completion=True)
    DisableFlag(11410403)
    Restart()


@NeverRestart(11410350)
def Event_11410350():
    """Event 11410350"""
    PostDestruction(1411003)


@NeverRestart(11412000)
def Event_11412000():
    """Event 11412000"""
    if OutsideMap(game_map=KILN_OF_THE_FIRST_FLAME):
        return
    DisableMapCollision(collision=1413201)
    if ThisEventFlagDisabled():
        DisableMapPiece(map_piece_id=1413000)
        DisableMapPiece(map_piece_id=1413001)
        DisableMapPiece(map_piece_id=1413002)
        DisableMapPiece(map_piece_id=1413003)
        DisableObject(1411061)
    
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1412012))
    
        EnableMapPiece(map_piece_id=1413000)
        EnableMapPiece(map_piece_id=1413001)
        EnableMapPiece(map_piece_id=1413002)
        EnableMapPiece(map_piece_id=1413003)
        EnableObject(1411061)
    EndOfAnimation(obj=1411061, animation_id=1)
    SetRespawnPoint(respawn_point=1413900)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412013))
    
    EnableMapCollision(collision=1413201)
    ForceAnimation(1411061, 3)


@NeverRestart(11412001)
def Event_11412001():
    """Event 11412001"""
    MAIN.Await(InsideMap(game_map=ASH_LAKE))
    
    DisableMapCollision(collision=1413205)


@RestartOnRest(11412200)
def Event_11412200(_, character: int, region: int, set_draw_parent: int, flag: int):
    """Event 11412200"""
    if ThisEventSlotFlagEnabled():
        Move(character, destination=region, destination_type=CoordEntityType.Region, set_draw_parent=set_draw_parent)
        SetNest(character, region=region)
        SetAIParamID(character, ai_param_id=282000)
        End()
    DisableCharacter(character)
    AND_1.Add(InsideMap(game_map=LOST_IZALITH))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableFlag(flag)
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetNest(character, region=region)
    SetAIParamID(character, ai_param_id=282000)


@RestartOnRest(11415100)
def Event_11415100(_, entity: int, character: int, cancel_animation: int, radius: float, seconds: float):
    """Event 11415100"""
    MAIN.Await(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=radius))
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)


@RestartOnRest(11415120)
def Event_11415120(_, region: int, region_1: int, flag: int):
    """Event 11415120"""
    if FlagEnabled(11412901):
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(FlagDisabled(11412121))
    
    EnableFlag(11412121)
    if FlagEnabled(11412120):
        ForceAnimation(1410006, 9061, wait_for_completion=True)
        DisableFlagRange((11415130, 11415134))
    MoveToEntity(1410006, destination=region_1, destination_type=CoordEntityType.Region)
    SetNest(1410006, region=region_1)
    EnableFlag(flag)
    SetStandbyAnimationSettings(1410006, cancel_animation=9060)
    ForceAnimation(1410006, 9060, wait_for_completion=True)
    DisableFlag(11412121)
    EnableFlag(11412120)
    Restart()


@RestartOnRest(11415000)
def Event_11415000():
    """Event 11415000"""
    if FlagEnabled(11412901):
        return
    AND_1.Add(CharacterAlive(1410006))
    AND_1.Add(FlagEnabled(11412120))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=1410006, radius=18.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11412121)
    ForceAnimation(1410006, 9061, wait_for_completion=True)
    DisableFlagRange((11415130, 11415134))
    DisableFlag(11412121)
    DisableFlag(11412120)
    SetStandbyAnimationSettings(1410006, standby_animation=9000)
    Restart()


@RestartOnRest(11415110)
def Event_11415110(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
):
    """Event 11415110"""
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    
    MAIN.Await(CharacterDead(character))
    
    SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableCharacter(character_5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=character,
    )
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=character,
    )
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=character,
    )
    Move(
        character_5,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)
    ForceAnimation(character_3, 7000)
    ForceAnimation(character_4, 7000)
    ForceAnimation(character_5, 7000)


@RestartOnRest(11412500)
def Event_11412500():
    """Event 11412500"""
    DisableSoundEvent(sound_id=1413800)
    if ThisEventFlagEnabled():
        DisableObject(1411065)
        DeleteVFX(1413401, erase_root_only=False)
        DisableObject(1411064)
        DeleteVFX(1413400, erase_root_only=False)
        DisableCharacter(1410030)
        End()
    DisableAI(1410030)
    EnableInvincibility(1410030)
    SkipLinesIfFlagEnabled(21, 11412101)
    DisableObject(1411065)
    DeleteVFX(1413401, erase_root_only=False)
    DisableObject(1411064)
    DeleteVFX(1413400, erase_root_only=False)
    DisableCharacter(1410030)
    EnableInvincibility(1410030)
    DisableHealthBar(1410030)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412011))
    
    EnableObject(1411065)
    CreateVFX(1413401)
    EnableObject(1411064)
    CreateVFX(1413400)
    EnableCharacter(1410030)
    DisableGravity(1410030)
    DisableCharacterCollision(1410030)
    ForceAnimation(1410030, 9061)
    Wait(4.0)
    EnableGravity(1410030)
    EnableCharacterCollision(1410030)
    EnableFlag(11412101)
    SkipLines(9)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412010))
    Move(1410030, destination=1412506, destination_type=CoordEntityType.Region, short_move=True)
    OR_1.Add(AND_1)
    OR_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412008,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411064,
    ))
    OR_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412009,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411065,
    ))
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, target_entity=1412507)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    DisableInvincibility(1410030)
    EnableAI(1410030)
    EnableBossHealthBar(1410030, name=2250)
    EnableSoundEvent(sound_id=1413800)
    
    MAIN.Await(CharacterDead(1410030))
    
    DisableBossHealthBar(1410030)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    Wait(4.0)
    DisableSoundEvent(sound_id=1413800)
    DisableObject(1411065)
    DeleteVFX(1413401)
    DisableObject(1411064)
    DeleteVFX(1413400)


@NeverRestart(11412004)
def Event_11412004():
    """Event 11412004"""
    if ThisEventFlagEnabled():
        DisableObject(1411023)
        DisableObject(1411024)
        DisableObject(1411025)
        DisableObject(1411026)
        DisableObject(1411027)
        DisableObject(1411028)
        DisableObject(1411029)
        DisableObject(1411030)
        DisableObject(1411031)
        DisableObject(1411032)
        DisableObject(1411033)
        DisableObject(1411034)
        DisableObject(1411035)
        DisableObject(1411036)
        DisableObject(1411037)
        DisableObject(1411038)
        DisableObject(1411039)
        DisableObject(1411040)
        DisableObject(1411041)
        DisableObject(1411042)
        DisableObject(1411043)
        DisableObject(1411044)
        DisableObject(1411045)
        DisableObject(1411046)
        DisableObject(1411047)
        DisableObject(1411048)
        DisableObject(1411049)
        DisableObject(1411050)
        DisableObject(1411051)
        DisableObject(1411052)
        DisableObject(1411053)
        DisableObject(1411054)
        DisableObject(1411055)
        DisableObject(1411056)
        DisableObject(1411057)
        DisableObject(1411058)
        DisableObject(1411059)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(1410030, tae_event_id=1))
    
    DestroyObject(1411023)
    DestroyObject(1411024)
    DestroyObject(1411025)
    DestroyObject(1411026)
    DestroyObject(1411027)
    DestroyObject(1411028)
    DestroyObject(1411029)
    DestroyObject(1411030)
    DestroyObject(1411031)
    DestroyObject(1411032)
    DestroyObject(1411033)
    DestroyObject(1411034)
    DestroyObject(1411035)
    DestroyObject(1411036)
    DestroyObject(1411037)
    DestroyObject(1411038)
    DestroyObject(1411039)
    DestroyObject(1411040)
    DestroyObject(1411041)
    DestroyObject(1411042)
    DestroyObject(1411043)
    DestroyObject(1411044)
    DestroyObject(1411045)
    DestroyObject(1411046)
    DestroyObject(1411047)
    DestroyObject(1411048)
    DestroyObject(1411049)
    DestroyObject(1411050)
    DestroyObject(1411051)
    DestroyObject(1411052)
    DestroyObject(1411053)
    DestroyObject(1411054)
    DestroyObject(1411055)
    DestroyObject(1411056)
    DestroyObject(1411057)
    DestroyObject(1411058)
    DestroyObject(1411059)


@NeverRestart(11410500)
def Event_11410500(_, character: int, flag: int, left: int):
    """Event 11410500"""
    if FlagEnabled(flag):
        SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
        End()
    if ValueEqual(left=left, right=0):
        AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
        AND_1.Add(HealthRatioLessThanOrEqual(character, value=0.8999999761581421))
        AND_1.Add(HealthRatioGreaterThan(character, value=0.0))
    
        MAIN.Await(AND_1)
    else:
        AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
        OR_1.Add(HealthRatioLessThanOrEqual(character, value=0.8999999761581421))
        OR_1.Add(FlagEnabled(left))
        AND_2.Add(OR_1)
        AND_2.Add(HealthRatioGreaterThan(character, value=0.0))
    
        MAIN.Await(AND_2)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11410510)
def Event_11410510(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11410510"""
    if FlagEnabled(flag):
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatioLessThanOrEqual(character, value=0.0))
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11412002)
def Event_11412002():
    """Event 11412002"""
    if FlagEnabled(0):
        DeleteVFX(1413403, erase_root_only=False)
        End()
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1412025,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1412508)
    ForceAnimation(PLAYER, 7522)
    Wait(2.0)
    EnableFlag(11813000)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100980)


@NeverRestart(11412003)
def Event_11412003():
    """Event 11412003"""
    if FlagDisabled(0):
        DeleteVFX(1413404, erase_root_only=False)
        End()
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1412026,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1412509)
    ForceAnimation(PLAYER, 7522)
    Wait(2.0)
    EnableFlag(11813000)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100980)


@RestartOnRest(11412005)
def Event_11412005():
    """Event 11412005"""
    if ThisEventFlagEnabled():
        Kill(1410016)
        End()
    DisableAI(1410016)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=1410016, radius=10.0))
    
    ForceAnimation(1410016, 200, wait_for_completion=True)
    ForceAnimation(1410016, 200)


@RestartOnRest(11412006)
def Event_11412006():
    """Event 11412006"""
    if ThisEventFlagEnabled():
        DisableCharacter(1410017)
        DisableCharacter(1410023)
        DisableCharacter(1410013)
        DisableCharacter(1410014)
        DisableCharacter(1410015)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=1410017, radius=10.0))
    
    SetTeamType(1410017, TeamType.HostileAlly)
    SetTeamType(1410018, TeamType.HostileAlly)
    SetTeamType(1410019, TeamType.HostileAlly)
    SetTeamType(1410020, TeamType.HostileAlly)
    SetTeamType(1410021, TeamType.HostileAlly)
    SetTeamType(1410022, TeamType.HostileAlly)
    SetTeamType(1410023, TeamType.HostileAlly)
    SetTeamType(1410024, TeamType.HostileAlly)
    SetTeamType(1410025, TeamType.HostileAlly)
    SetTeamType(1410026, TeamType.HostileAlly)
    SetTeamType(1410027, TeamType.HostileAlly)
    SetTeamType(1410028, TeamType.HostileAlly)
    SetTeamType(1410013, TeamType.RedChild)
    SetTeamType(1410014, TeamType.RedChild)
    SetTeamType(1410015, TeamType.RedChild)


@RestartOnRest(11412501)
def Event_11412501():
    """Event 11412501"""
    DisableSoundEvent(sound_id=1413801)
    if ThisEventFlagEnabled():
        Kill(1410031)
        DisableCharacter(1410031)
        End()
    DisableAI(1410031)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412024))
    
    ResetStandbyAnimationSettings(1410031)
    EnableAI(1410031)
    EnableBossHealthBar(1410031, name=2320)
    EnableSoundEvent(sound_id=1413801)
    
    MAIN.Await(CharacterDead(1410031))
    
    DisableBossHealthBar(1410031)
    DisableSoundEvent(sound_id=1413801)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)


@NeverRestart(11412007)
def Event_11412007():
    """Event 11412007"""
    if FlagEnabled(11412502):
        return
    AND_1.Add(FlagDisabled(11412501))
    AND_1.Add(ActionButton(
        prompt_text=15000000,
        anchor_entity=1410032,
        anchor_type=CoordEntityType.Character,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10040006)
    Wait(3.0)
    Restart()


@RestartOnRest(11412008)
def Event_11412008():
    """Event 11412008"""
    if FlagEnabled(11412502):
        return
    AND_1.Add(FlagEnabled(11412501))
    AND_1.Add(ActionButton(
        prompt_text=15000000,
        anchor_entity=1410032,
        anchor_type=CoordEntityType.Character,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10040007)
    Wait(2.0)
    Kill(1410032, award_souls=True)


@RestartOnRest(11412502)
def Event_11412502():
    """Event 11412502"""
    if ThisEventFlagEnabled():
        Kill(1410032)
        DisableCharacter(1410032)
        End()
    
    MAIN.Await(CharacterDead(1410032))
    
    End()


@NeverRestart(11412010)
def Event_11412010():
    """Event 11412010"""
    DisableCharacterCollision(1410029)
    DisableGravity(1410029)
    HellkiteBreathControl(1410029, obj=1411066, animation_id=7005)
    Wait(5.0)
    Restart()


@NeverRestart(11412015)
def Event_11412015():
    """Event 11412015"""
    Wait(180.0)
    AND_1.Add(InsideMap(game_map=LOST_IZALITH))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1412014))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1412015))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(PLAYER, 130300002, sound_type=SoundType.s_SFX)
    Wait(2.0)
    PlaySoundEffect(PLAYER, 130300002, sound_type=SoundType.s_SFX)
    Wait(2.0)
    PlaySoundEffect(PLAYER, 130300002, sound_type=SoundType.s_SFX)
    Wait(2.0)
    Restart()


@NeverRestart(11410999)
def Event_11410999():
    """Event 11410999"""
    SetMapDrawParamSlot(map_area_id=14, draw_param_slot=0)
    Wait(5.0)
    SetMapDrawParamSlot(map_area_id=14, draw_param_slot=1)
    Wait(5.0)
    Restart()


@NeverRestart(11412510)
def Event_11412510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11412510"""
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


@NeverRestart(11415510)
def Event_11415510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11415510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()


@NeverRestart(11412600)
def Event_11412600(_, obj: int, obj_act_id: int):
    """Event 11412600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11412900)
def Event_11412900(_, character: int, item_lot_param_id: int):
    """Event 11412900"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueNotEqual(left=item_lot_param_id, right=0):
        AwardItemLot(item_lot_param_id, host_only=True)
    End()
