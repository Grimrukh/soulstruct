"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11100000()
    Event_11100001()
    DisableMapPiece(map_piece_id=1103002)
    DisableMapCollision(collision=1103201)
    Event_11102200(0, flag=11813502, item=1507, item_1=1607, prompt_text=10050010)
    Event_11102200(1, flag=11813503, item=1510, item_1=1610, prompt_text=10050011)
    Event_11102200(2, flag=11813504, item=1512, item_1=1612, prompt_text=10050012)
    Event_11102200(3, flag=11813505, item=1513, item_1=1613, prompt_text=10050013)
    Event_11102012()
    Event_11102013()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    EnableInvincibility(1100000)
    Event_11813500()


@NeverRestart(11100000)
def Event_11100000():
    """Event 11100000"""
    RegisterBonfire(bonfire_flag=11100992, obj=1101960)
    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=1101001)
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=1101002)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=1101003)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=1101004)
    Event_11100030()
    Event_11100031()
    Event_11100136()
    Event_11100135()
    Event_11100120()
    Event_11100100(0, obj=1101008, vfx_id=1103000)
    Event_11100100(1, 1101009, 1103001)


@NeverRestart(11100001)
def Event_11100001():
    """Event 11100001"""
    Event_11102000()
    Event_11102001(
        0,
        flag=11813001,
        vfx_id=1103401,
        target_entity=1102501,
        anchor_entity=1102001,
        prompt_text=10012001,
        area_id=12,
        block_id=0,
        player_start=1200994,
        left=0
    )
    Event_11102001(
        1,
        flag=11813002,
        vfx_id=1103402,
        target_entity=1102502,
        anchor_entity=1102002,
        prompt_text=10012002,
        area_id=12,
        block_id=1,
        player_start=1210990,
        left=0
    )
    Event_11102001(
        2,
        flag=11813003,
        vfx_id=1103403,
        target_entity=1102503,
        anchor_entity=1102003,
        prompt_text=10012003,
        area_id=10,
        block_id=1,
        player_start=1010992,
        left=0
    )
    Event_11102001(
        3,
        flag=11813004,
        vfx_id=1103404,
        target_entity=1102504,
        anchor_entity=1102004,
        prompt_text=10012004,
        area_id=10,
        block_id=2,
        player_start=1020990,
        left=1
    )
    Event_11102001(
        4,
        flag=11813005,
        vfx_id=1103405,
        target_entity=1102505,
        anchor_entity=1102005,
        prompt_text=10012005,
        area_id=10,
        block_id=1,
        player_start=1010991,
        left=1
    )
    Event_11102001(
        6,
        flag=11813007,
        vfx_id=1103407,
        target_entity=1102507,
        anchor_entity=1102007,
        prompt_text=10012007,
        area_id=14,
        block_id=0,
        player_start=1400990,
        left=1
    )
    Event_11102001(7, 11813008, 1103408, 1102508, 1102008, 10012008, 15, 1, 1500990, 0)


@NeverRestart(11100070)
def Event_11100070(_, obj: int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11100070"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj_1, animation_id=animation_id_1)
        PostDestruction(obj)
        EnableTreasure(obj=obj_1)
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


@NeverRestart(11100100)
def Event_11100100(_, obj: int, vfx_id: int):
    """Event 11100100"""
    if ThisEventSlotFlagEnabled():
        DestroyObject(obj)
        ForceAnimation(obj, 0)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    
    MAIN.Await(ObjectDestroyed(obj))
    
    DeleteVFX(vfx_id)


@NeverRestart(11100030)
def Event_11100030():
    """Event 11100030"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=1101000, animation_id=2)
        DisableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)
        End()
    EnableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1101000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1102010, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1101000, 1, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=1102040, navmesh_type=NavmeshType.Solid)


@NeverRestart(11100031)
def Event_11100031():
    """Event 11100031"""
    AND_1.Add(FlagDisabled(11100030))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1101000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1101000, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11100120)
def Event_11100120():
    """Event 11100120"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=11100120))
    
    DisplayDialog(text=10010868, anchor_entity=1101010)


@NeverRestart(11100135)
def Event_11100135():
    """Event 11100135"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1101006, animation_id=1)
        EndOfAnimation(obj=1101007, animation_id=1)
        DisableNavmeshType(navmesh_id=1102041, navmesh_type=NavmeshType.Solid)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010503,
        anchor_entity=1101005,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    DisableObject(1101018)
    DisableObject(1101019)
    DisableObject(1101020)
    Move(PLAYER, destination=1101005, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8010)
    ForceAnimation(1101005, 1, wait_for_completion=True)
    PlayCutscene(110000, cutscene_flags=0, player_id=10000)
    ForceAnimation(1101006, 1)
    ForceAnimation(1101007, 1)
    DisableNavmeshType(navmesh_id=1102041, navmesh_type=NavmeshType.Solid)


@NeverRestart(11100136)
def Event_11100136():
    """Event 11100136"""
    AND_1.Add(FlagDisabled(11100135))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1101007,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160, anchor_entity=1101007)
    Restart()


@NeverRestart(11102000)
def Event_11102000():
    """Event 11102000"""
    if FlagDisabled(11813000):
        DeleteVFX(1103400, erase_root_only=False)
        End()
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012000,
        anchor_entity=1102000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1102500)
    ForceAnimation(PLAYER, 7522)
    Wait(0.699999988079071)
    if FlagEnabled(0):
        WarpToMap(game_map=LOST_IZALITH, player_start=1410991)
    else:
        WarpToMap(game_map=LOST_IZALITH, player_start=1410990)


@NeverRestart(11102001)
def Event_11102001(
    _,
    flag: int,
    vfx_id: int,
    target_entity: int,
    anchor_entity: int,
    prompt_text: int,
    area_id: uchar,
    block_id: uchar,
    player_start: int,
    left: int,
):
    """Event 11102001"""
    if FlagDisabled(flag):
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=prompt_text,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    if ValueEqual(left=left, right=1):
        ForceAnimation(PLAYER, 7522)
        Wait(0.699999988079071)
    else:
        ForceAnimation(PLAYER, 7114)
        Wait(1.5)
    WarpToMap(game_map=(area_id, block_id), player_start=player_start)


@NeverRestart(11813500)
def Event_11813500():
    """Event 11813500"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(ActionButton(
        prompt_text=15000000,
        anchor_entity=1100000,
        anchor_type=CoordEntityType.Character,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    AwardItemLot(1040, host_only=True)
    EnableFlag(11813506)
    EnableFlag(11813500)
    Wait(2.0)
    DisplayBattlefieldMessage(10040000, display_location_index=0)
    Wait(5.0)
    DisplayStatus(10040001)


@NeverRestart(11102200)
def Event_11102200(_, flag: int, item: int, item_1: int, prompt_text: int):
    """Event 11102200"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerHasGood(item))
    AND_1.Add(ActionButton(
        prompt_text=prompt_text,
        anchor_entity=1100000,
        anchor_type=CoordEntityType.Character,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(PlayerHasGood(item_1))
    AND_2.Add(ActionButton(
        prompt_text=prompt_text,
        anchor_entity=1100000,
        anchor_type=CoordEntityType.Character,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_1)
    RemoveGoodFromPlayer(item=item)
    AwardItemLot(15000, host_only=True)
    End()
    RemoveGoodFromPlayer(item=item_1)
    AwardItemLot(16000, host_only=True)
    EnableFlag(flag)
    Wait(1.0)
    Event_11102011()


@NeverRestart(11102011)
def Event_11102011():
    """Event 11102011"""
    DisplayDialog(text=10040013)
    Wait(3.0)
    OR_7.Add(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=1))
    SkipLinesIfConditionFalse(2, OR_7)
    DisplayStatus(10040010)
    SkipLines(11)
    AND_7.Add(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=2))
    SkipLinesIfConditionFalse(2, AND_7)
    DisplayStatus(10040011)
    SkipLines(7)
    OR_6.Add(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=3))
    SkipLinesIfConditionFalse(2, OR_6)
    DisplayStatus(10040012)
    SkipLines(3)
    AND_6.Add(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=4))
    SkipLinesIfConditionFalse(1, AND_6)
    DisplayStatus(10040009)


@NeverRestart(11102012)
def Event_11102012():
    """Event 11102012"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=1))
    
    AwardItemLot(1050, host_only=True)


@NeverRestart(11102013)
def Event_11102013():
    """Event 11102013"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(TrueFlagCountEqual(FlagType.Absolute, flag_range=(11813502, 11813505), value=3))
    
    AwardItemLot(1060, host_only=True)
