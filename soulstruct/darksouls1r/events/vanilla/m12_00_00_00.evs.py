"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11200000()
    Event_11202002()
    Event_11202501()
    Event_11202510(
        1,
        flag=11202521,
        flag_1=11202501,
        obj=1201014,
        character=1200040,
        item_lot_param_id=15130,
        item_lot_param_id_1=16130
    )
    Event_11205510(1, 1201014, 11202501, 11202521, 22679, 3.200000047683716)
    Event_11205220(0, character=1200042, character_1=1200045, entity=1203600)
    Event_11205220(1, character=1200043, character_1=1200046, entity=1203601)
    Event_11205220(2, character=1200044, character_1=1200047, entity=1203602)
    Event_11202502()
    Event_11202510(
        2,
        flag=11202522,
        flag_1=11202502,
        obj=1201015,
        character=1200049,
        item_lot_param_id=15140,
        item_lot_param_id_1=16140
    )
    Event_11205510(2, 1201015, 11202502, 11202522, 22686, 3.200000047683716)
    Event_11205210(0, 1200001, 5.0)
    Event_11205210(1, 1200002, 5.0)
    Event_11205210(2, 1200003, 5.0)
    Event_11205210(3, 1200004, 5.0)
    Event_11205210(4, 1200005, 5.0)
    Event_11205210(5, 1200006, 5.0)
    Event_11205210(6, 1200007, 5.0)
    Event_11205210(7, 1200008, 5.0)
    Event_11205210(8, 1200009, 5.0)
    Event_11205200(0, 1200011, 9.0, 1.0)
    Event_11205200(1, 1200012, 2.0, 0.20000000298023224)
    Event_11205200(2, 1200013, 6.0, 0.5)
    Event_11205200(3, 1200014, 6.0, 0.5)
    Event_11205200(4, 1200015, 6.0, 0.5)
    Event_11205200(5, 1200016, 6.0, 0.5)
    Event_11202000()
    Event_11202001()
    Event_11205230(0, region=1202008)
    Event_11205230(1, region=1202009)
    Event_11205230(2, region=1202010)
    DisableFlag(11202100)
    Event_11205000(0, 1200051, 2950, 11202100, 90, 4.0, 180.0, 2950)
    Event_11205001(0, flag=11202100, character=1200051)
    Event_11202004()
    Event_11202600(0, obj=1201012, obj_act_id=11200600)
    Event_11202005()
    Event_11206200(0, character=1200019, value=60)
    Event_11206200(1, character=1200020, value=60)
    Event_11206200(2, character=1200021, value=60)
    Event_11206200(3, character=1200022, value=60)
    Event_11206200(4, character=1200023, value=60)
    Event_11206200(5, character=1200024, value=60)
    Event_11206000(0, character=1200025, value=60)
    Event_11206000(1, character=1200026, value=60)
    Event_11206000(2, character=1200027, value=60)
    Event_11206000(3, character=1200028, value=60)
    Event_11206000(4, character=1200029, value=60)
    Event_11206200(6, character=1200031, value=75)
    Event_11206200(7, character=1200034, value=75)
    Event_11206200(8, character=1200032, value=90)
    Event_11206200(9, character=1200036, value=90)
    Event_11206200(10, character=1200037, value=90)
    Event_11206000(5, character=1200039, value=90)
    Event_11206200(11, character=1200030, value=120)
    Event_11206200(12, character=1200033, value=100)
    Event_11206200(13, character=1200035, value=100)
    Event_11206000(6, character=1200038, value=100)
    Event_11206200(14, 1200010, 120)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableMapPiece(map_piece_id=1203016)
    DisableMapPiece(map_piece_id=1203017)
    DisableMapPiece(map_piece_id=1203018)
    DisableMapPiece(map_piece_id=1203019)
    DisableMapPiece(map_piece_id=1203020)
    DisableMapPiece(map_piece_id=1203021)
    DisableMapPiece(map_piece_id=1203022)
    DisableMapPiece(map_piece_id=1203023)
    DisableMapPiece(map_piece_id=1203024)
    DisableMapPiece(map_piece_id=1203025)
    DisableMapCollision(collision=1203206)
    DisableMapCollision(collision=1203207)
    DisableMapCollision(collision=1203208)
    DisableMapCollision(collision=1203209)
    DisableObject(1201011)
    DisableObject(1201000)
    DisableMapCollision(collision=1203201)
    DisableSpawner(entity=1203600)
    DisableSpawner(entity=1203601)
    DisableSpawner(entity=1203602)
    SetTeamType(1200029, TeamType.RedChild)
    Event_11205003()
    Event_11205004()
    Event_11205005()


@NeverRestart(11200000)
def Event_11200000():
    """Event 11200000"""
    RegisterBonfire(bonfire_flag=11200992, obj=1201960)
    RegisterBonfire(bonfire_flag=11200984, obj=1201961)
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=1201004)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=1201005)
    Event_11200100()
    Event_11200110()
    Event_11200101()
    Event_11200120()
    DisableObject(1201006)


@NeverRestart(11200100)
def Event_11200100():
    """Event 11200100"""
    OR_1.Add(FlagEnabled(61200500))
    OR_1.Add(ThisEventSlotFlagEnabled())
    SkipLinesIfConditionFalse(2, OR_1)
    EndOfAnimation(obj=1201002, animation_id=1)
    End()
    AND_1.Add(PlayerHasGood(2006))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1202004,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201002,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11200100)
    EnableFlag(61200500)
    RotateToFaceEntity(PLAYER, target_entity=1201002)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    DisplayDialog(text=10010865, anchor_entity=1201002)
    ForceAnimation(1201002, 1)


@NeverRestart(11200110)
def Event_11200110():
    """Event 11200110"""
    if FlagEnabled(11200100):
        return
    AND_1.Add(PlayerDoesNotHaveGood(2006))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1202004,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201002,
    ))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11200100):
        return
    DisplayDialog(text=10010160, anchor_entity=1201002)
    Restart()


@NeverRestart(11200101)
def Event_11200101():
    """Event 11200101"""
    OR_1.Add(FlagEnabled(61200501))
    OR_1.Add(ThisEventSlotFlagEnabled())
    SkipLinesIfConditionFalse(2, OR_1)
    EndOfAnimation(obj=1201003, animation_id=1)
    End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1202005,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201003,
    ))
    
    EnableFlag(11200101)
    EnableFlag(61200501)
    RotateToFaceEntity(PLAYER, target_entity=1201003)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    ForceAnimation(1201003, 1)


@NeverRestart(11200120)
def Event_11200120():
    """Event 11200120"""
    if ThisEventSlotFlagEnabled():
        DisableObject(1201007)
        End()
    
    MAIN.Await(ObjectDestroyed(1201007))
    
    EnableFlag(11200120)


@NeverRestart(11202000)
def Event_11202000():
    """Event 11202000"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1202006))
    
    DisableMapCollision(collision=1203200)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1202006))
    
    EnableMapCollision(collision=1203200)
    Restart()


@NeverRestart(11202001)
def Event_11202001():
    """Event 11202001"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1202007,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1202503)
    ForceAnimation(PLAYER, 7114)
    Wait(2.0)
    EnableFlag(11813001)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100981)


@RestartOnRest(11205200)
def Event_11205200(_, character: int, radius: float, seconds: float):
    """Event 11205200"""
    DisableGravity(character)
    DisableCharacter(character)
    DisableAI(character)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    Wait(seconds)
    EnableGravity(character)
    EnableCharacter(character)
    ForceAnimation(character, 7000, wait_for_completion=True)
    EnableAI(character)


@RestartOnRest(11205210)
def Event_11205210(_, character: int, radius: float):
    """Event 11205210"""
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@NeverRestart(11202002)
def Event_11202002():
    """Event 11202002"""
    DisableGravity(1200000)
    EnableInvincibility(1200000)
    DisableCharacter(1200000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1202003))
    
    DisableCharacterCollision(1200000)
    EnableCharacter(1200000)
    Move(1200000, destination=1202502, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1200000, 7012, wait_for_completion=True)
    DisableCharacter(1200000)


@RestartOnRest(11202501)
def Event_11202501():
    """Event 11202501"""
    DisableSoundEvent(sound_id=1203800)
    DisableCharacter(1200040)
    DisableCharacter(1200042)
    DisableCharacter(1200043)
    DisableCharacter(1200044)
    DisableObject(1201008)
    DeleteVFX(1203402, erase_root_only=False)
    if ThisEventFlagEnabled():
        Kill(1200040)
        DisableCharacter(1200041)
        Kill(1200041)
        DisableCharacter(1200048)
        Kill(1200048)
        End()
    DisableObject(1201961)
    DisableGravity(1200041)
    DisableCharacter(1200041)
    DisableGravity(1200048)
    EnableImmortality(1200048)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1202000))
    
    EnableObject(1201008)
    CreateVFX(1203402)
    EnableCharacter(1200042)
    ForceAnimation(1200042, 6200)
    WaitRandomSeconds(min_seconds=0.800000011920929, max_seconds=1.5)
    EnableCharacter(1200043)
    ForceAnimation(1200043, 6200)
    WaitRandomSeconds(min_seconds=0.800000011920929, max_seconds=1.5)
    EnableCharacter(1200044)
    ForceAnimation(1200044, 6200)
    Wait(2.0)
    EnableSoundEvent(sound_id=1203800)
    EnableBossHealthBar(1200048, name=4520)
    EnableFlag(11202104)
    AND_1.Add(CharacterDead(1200042))
    AND_1.Add(CharacterDead(1200043))
    AND_1.Add(CharacterDead(1200044))
    
    MAIN.Await(AND_1)
    
    DisableBossHealthBar(1200040, name=4520)
    DisableFlag(11202104)
    Wait(3.0)
    EnableBossHealthBar(1200040, name=5210)
    EnableFlag(11202105)
    AICommand(1200045, command_id=10, command_slot=0)
    AICommand(1200046, command_id=10, command_slot=0)
    AICommand(1200047, command_id=10, command_slot=0)
    EnableCharacter(1200040)
    ForceAnimation(1200040, 6200, wait_for_completion=True)
    ReplanAI(1200040)
    
    MAIN.Await(CharacterDead(1200040))
    
    DisableCharacter(1200048)
    Kill(1200048)
    DisableBossHealthBar(1200040)
    DisableFlag(11202105)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(sound_id=1203800)
    DisableObject(1201008)
    DeleteVFX(1203402)


@RestartOnRest(11205220)
def Event_11205220(_, character: int, character_1: int, entity: int):
    """Event 11205220"""
    if FlagEnabled(11202501):
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(HealthRatioLessThanOrEqual(character, value=0.0))
    
    AddSpecialEffect(1200048, 93105)
    
    MAIN.Await(CharacterDead(character))
    
    EnableSpawner(entity=entity)
    
    MAIN.Await(HealthRatioLessThanOrEqual(1200040, value=0.0))
    
    DisableSpawner(entity=entity)
    WaitRandomSeconds(min_seconds=0.10000000149011612, max_seconds=1.0)
    Kill(character_1)


@RestartOnRest(11202502)
def Event_11202502():
    """Event 11202502"""
    DisableSoundEvent(sound_id=1203801)
    DeleteVFX(1203400, erase_root_only=False)
    DisableCharacter(1200049)
    DisableCharacter(1200050)
    DisableObject(1201010)
    DeleteVFX(1203403, erase_root_only=False)
    if ThisEventFlagEnabled():
        DisableCharacter(1200049)
        Kill(1200049)
        End()
    AND_1.Add(FlagEnabled(11202501))
    AND_1.Add(FlagDisabled(11202502))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11205002)
    CreateVFX(1203400)
    Wait(2.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10010513,
        anchor_entity=1202001,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1202500)
    ForceAnimation(PLAYER, 7114)
    Wait(1.0)
    EnableCharacter(1200050)
    DisableGravity(1200050)
    DisableCharacterCollision(1200050)
    ForceAnimation(1200050, 3007)
    Wait(2.0)
    DisableMapPiece(map_piece_id=1203000)
    DisableMapPiece(map_piece_id=1203001)
    DisableMapPiece(map_piece_id=1203002)
    DisableMapPiece(map_piece_id=1203004)
    DisableMapPiece(map_piece_id=1203005)
    DisableMapPiece(map_piece_id=1203006)
    DisableMapPiece(map_piece_id=1203007)
    DisableMapPiece(map_piece_id=1203008)
    DisableMapPiece(map_piece_id=1203009)
    DisableMapPiece(map_piece_id=1203010)
    DisableMapPiece(map_piece_id=1203011)
    DisableMapPiece(map_piece_id=1203012)
    DisableMapPiece(map_piece_id=1203013)
    DisableMapPiece(map_piece_id=1203014)
    DisableMapPiece(map_piece_id=1203015)
    DisableMapCollision(collision=1203202)
    DisableMapCollision(collision=1203203)
    DisableMapCollision(collision=1203204)
    DisableMapCollision(collision=1203205)
    DisableObject(1201003)
    DisableObject(1201001)
    EnableMapPiece(map_piece_id=1203016)
    EnableMapPiece(map_piece_id=1203017)
    EnableMapPiece(map_piece_id=1203018)
    EnableMapPiece(map_piece_id=1203019)
    EnableMapPiece(map_piece_id=1203020)
    EnableMapPiece(map_piece_id=1203021)
    EnableMapPiece(map_piece_id=1203022)
    EnableMapPiece(map_piece_id=1203023)
    EnableMapPiece(map_piece_id=1203024)
    EnableMapPiece(map_piece_id=1203025)
    EnableMapCollision(collision=1203206)
    EnableMapCollision(collision=1203207)
    EnableMapCollision(collision=1203208)
    EnableMapCollision(collision=1203209)
    EnableObject(1201011)
    EnableObject(1201000)
    EnableObject(1201010)
    DeleteVFX(1203400, erase_root_only=False)
    DisableCharacter(1200051)
    DeleteVFX(1203403)
    SetMapDrawParamSlot(map_area_id=12, draw_param_slot=1)
    EnableCharacter(1200049)
    Wait(4.0)
    EnableAI(1200049)
    EnableSoundEvent(sound_id=1203801)
    EnableBossHealthBar(1200049, name=5600)
    
    MAIN.Await(CharacterDead(1200049))
    
    AwardItemLot(56000000, host_only=True)
    DisableBossHealthBar(1200049)
    DisplayBanner(BannerType.VictoryAchieved)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    EnableFlag(11202502)
    DisableSoundEvent(sound_id=1203801)
    
    MAIN.Await(ActionButton(
        prompt_text=10010514,
        anchor_entity=1202002,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1202501)
    ForceAnimation(PLAYER, 7114)
    Wait(1.0)
    ForceAnimation(1200050, 3007)
    Wait(1.0)
    EnableMapPiece(map_piece_id=1203000)
    EnableMapPiece(map_piece_id=1203001)
    EnableMapPiece(map_piece_id=1203002)
    EnableMapPiece(map_piece_id=1203004)
    EnableMapPiece(map_piece_id=1203005)
    EnableMapPiece(map_piece_id=1203006)
    EnableMapPiece(map_piece_id=1203007)
    EnableMapPiece(map_piece_id=1203008)
    EnableMapPiece(map_piece_id=1203009)
    EnableMapPiece(map_piece_id=1203010)
    EnableMapPiece(map_piece_id=1203011)
    EnableMapPiece(map_piece_id=1203012)
    EnableMapPiece(map_piece_id=1203013)
    EnableMapPiece(map_piece_id=1203014)
    EnableMapPiece(map_piece_id=1203015)
    EnableMapCollision(collision=1203202)
    EnableMapCollision(collision=1203203)
    EnableMapCollision(collision=1203204)
    EnableMapCollision(collision=1203205)
    EnableObject(1201003)
    EnableObject(1201001)
    DisableMapPiece(map_piece_id=1203016)
    DisableMapPiece(map_piece_id=1203017)
    DisableMapPiece(map_piece_id=1203018)
    DisableMapPiece(map_piece_id=1203019)
    DisableMapPiece(map_piece_id=1203020)
    DisableMapPiece(map_piece_id=1203021)
    DisableMapPiece(map_piece_id=1203022)
    DisableMapPiece(map_piece_id=1203023)
    DisableMapPiece(map_piece_id=1203024)
    DisableMapPiece(map_piece_id=1203025)
    DisableMapCollision(collision=1203206)
    DisableMapCollision(collision=1203207)
    DisableMapCollision(collision=1203208)
    DisableMapCollision(collision=1203209)
    DisableObject(1201011)
    DisableObject(1201000)
    DisableObject(1201010)
    DeleteVFX(1203403, erase_root_only=False)
    SetMapDrawParamSlot(map_area_id=12, draw_param_slot=0)
    DisableFlag(11205002)


@NeverRestart(11205230)
def Event_11205230(_, region: int):
    """Event 11205230"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DisplayStatus(10040020)
    Wait(5.0)
    Restart()


@RestartOnRest(11205000)
def Event_11205000(
    _,
    character: int,
    movement_type: int,
    flag: int,
    model_point: short,
    max_distance: float,
    facing_angle: float,
    name: short,
):
    """Event 11205000"""
    SkipLinesIfFlagDisabled(17, flag)
    OR_1.Add(CharacterDead(character))
    OR_1.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterDead(character))
    AND_1.Add(FlagEnabled(flag))
    SkipLinesIfConditionFalse(10, AND_1)
    NightfallClearSpecialMovement()
    DisableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfFlagDisabled(2, 11202104)
    EnableBossHealthBar(1200048, name=4520)
    SkipLines(2)
    SkipLinesIfFlagDisabled(1, 11202105)
    EnableBossHealthBar(1200048, name=5210)
    EnableGravity(PLAYER)
    ForceAnimation(PLAYER, 9803)
    DisableFlag(flag)
    SkipLines(14)
    AND_2.Add(FlagDisabled(11202004))
    AND_2.Add(FlagDisabled(11205002))
    AND_2.Add(ActionButton(
        prompt_text=15000001,
        anchor_entity=character,
        anchor_type=CoordEntityType.Character,
        facing_angle=facing_angle,
        max_distance=max_distance,
        model_point=model_point,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_2)
    
    DisableGravity(PLAYER)
    NightfallSetSpecialMovement(character=character, movement_type=movement_type, is_active=OnOffChange.On)
    ForceAnimation(PLAYER, 9800)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 9800))
    
    ForceAnimation(character, 9800)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 9801))
    
    ForceAnimation(PLAYER, 9801, loop=True)
    NightfallSetSpecialMovement(character=character, movement_type=movement_type, is_active=OnOffChange.Off)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    EnableFlag(flag)
    Restart()


@RestartOnRest(11205001)
def Event_11205001(_, flag: int, character: int):
    """Event 11205001"""
    SkipLinesIfFlagDisabled(19, flag)
    OR_7.Add(CharacterHasSpecialEffect(PLAYER, 9802))
    SkipLinesIfConditionFalse(14, OR_7)
    CancelSpecialEffect(PLAYER, 9802)
    EnableGravity(PLAYER)
    ForceAnimation(PLAYER, 9802)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 9803))
    
    NightfallClearSpecialMovement()
    DisableBossHealthBar(character, bar_slot=1)
    SkipLinesIfFlagDisabled(2, 11202104)
    EnableBossHealthBar(1200048, name=4520)
    SkipLines(2)
    SkipLinesIfFlagDisabled(1, 11202105)
    EnableBossHealthBar(1200048, name=5210)
    ForceAnimation(character, 9800)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 9804))
    
    DisableFlag(flag)
    AND_7.Add(CharacterHasSpecialEffect(PLAYER, 9811))
    SkipLinesIfConditionFalse(1, AND_7)
    CancelSpecialEffect(PLAYER, 9810)
    Restart()


@RestartOnRest(11202004)
def Event_11202004():
    """Event 11202004"""
    if ThisEventFlagEnabled():
        Kill(1200051)
        End()
    AND_1.Add(FlagDisabled(11202501))
    AND_1.Add(EventValueGreaterThanOrEqual(flag=810, bit_count=8, value=5))
    OR_1.Add(AND_1)
    OR_1.Add(HealthRatioLessThanOrEqual(1200051, value=0.0))
    
    MAIN.Await(OR_1)
    
    Kill(1200051)


@RestartOnRest(11202005)
def Event_11202005():
    """Event 11202005"""
    DisableCharacter(1200017)
    DisableCharacter(1200018)
    if FlagEnabled(51200190):
        EndOfAnimation(obj=1201013, animation_id=0)
        DisableObjectActivation(1201013, obj_act_id=-1)
        EnableTreasure(obj=1201013)
        End()
    OR_7.Add(EventValueGreaterThanOrEqual(flag=810, bit_count=8, value=135))
    SkipLinesIfConditionFalse(6, OR_7)
    EndOfAnimation(obj=1201013, animation_id=0)
    DisableObjectActivation(1201013, obj_act_id=-1)
    EnableCharacter(1200018)
    
    MAIN.Await(HealthRatioLessThanOrEqual(1200018, value=0.0))
    
    AwardItemLot(51200190, host_only=True)
    End()
    AND_7.Add(EventValueGreaterThanOrEqual(flag=810, bit_count=8, value=60))
    SkipLinesIfConditionFalse(6, AND_7)
    EndOfAnimation(obj=1201013, animation_id=0)
    DisableObjectActivation(1201013, obj_act_id=-1)
    EnableCharacter(1200017)
    
    MAIN.Await(HealthRatioLessThanOrEqual(1200017, value=0.0))
    
    AwardItemLot(51200190, host_only=True)
    End()
    DisableTreasure(obj=1201013)
    
    MAIN.Await(ObjectActivated(obj_act_id=11200601))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=1201013)


@RestartOnRest(11205003)
def Event_11205003():
    """Event 11205003"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200026, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200031, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200034, radius=20.0))
    
    MAIN.Await(OR_1)
    
    SetTeamType(1200026, TeamType.RedChild)
    SetTeamType(1200031, TeamType.HostileAlly)
    SetTeamType(1200034, TeamType.HostileAlly)


@RestartOnRest(11205004)
def Event_11205004():
    """Event 11205004"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200025, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200028, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200033, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200030, radius=20.0))
    
    MAIN.Await(OR_1)
    
    SetTeamType(1200025, TeamType.RedChild)
    SetTeamType(1200028, TeamType.RedChild)
    SetTeamType(1200030, TeamType.HostileAlly)
    SetTeamType(1200033, TeamType.HostileAlly)
    SetTeamType(1200032, TeamType.HostileAlly)
    SetTeamType(1200036, TeamType.HostileAlly)
    SetTeamType(1200037, TeamType.HostileAlly)
    SetTeamType(1200039, TeamType.HostileAlly)


@RestartOnRest(11205005)
def Event_11205005():
    """Event 11205005"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200027, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200038, radius=20.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1200035, radius=20.0))
    
    MAIN.Await(OR_1)
    
    SetTeamType(1200027, TeamType.RedChild)
    SetTeamType(1200038, TeamType.HostileAlly)
    SetTeamType(1200035, TeamType.HostileAlly)
    SetTeamType(1200032, TeamType.HostileAlly)
    SetTeamType(1200036, TeamType.HostileAlly)
    SetTeamType(1200037, TeamType.HostileAlly)
    SetTeamType(1200039, TeamType.HostileAlly)


@NeverRestart(11202510)
def Event_11202510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11202510"""
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


@NeverRestart(11205510)
def Event_11205510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11205510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()


@NeverRestart(11202600)
def Event_11202600(_, obj: int, obj_act_id: int):
    """Event 11202600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11206000)
def Event_11206000(_, character: int, value: uint):
    """Event 11206000"""
    OR_7.Add(EventValueLessThan(flag=810, bit_count=8, value=value))
    SkipLinesIfConditionFalse(1, OR_7)
    DisableCharacter(character)
    End()


@RestartOnRest(11206200)
def Event_11206200(_, character: int, value: uint):
    """Event 11206200"""
    OR_7.Add(EventValueGreaterThanOrEqual(flag=810, bit_count=8, value=value))
    SkipLinesIfConditionFalse(1, OR_7)
    DisableCharacter(character)
    End()
