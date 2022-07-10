"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11000000()
    Event_11000100()
    Event_11000101()
    Event_11000110()
    Event_11002500()
    Event_11002510(
        0,
        flag=11002520,
        flag_1=11002500,
        obj=1001000,
        character=1000009,
        item_lot_param_id=15090,
        item_lot_param_id_1=16090
    )
    Event_11005510(0, 1001000, 11002500, 11002520, 22679, 3.200000047683716)
    Event_11005610(0, character=1000009, character_1=1000010, left=11005611, command_id=1)
    Event_11005610(1, character=1000009, character_1=1000011, left=11005612, command_id=2)
    Event_11005610(2, character=1000009, character_1=1000012, left=11005613, command_id=3)
    Event_11005610(3, character=1000009, character_1=1000013, left=11005614, command_id=4)
    Event_11005610(4, character=1000009, character_1=1000014, left=11005615, command_id=5)
    Event_11005610(5, character=1000009, character_1=1000015, left=11005616, command_id=6)
    Event_11005620(0, character=1000009, character_1=1000017, left=11005621, command_id=1)
    Event_11005620(1, character=1000009, character_1=1000018, left=11005622, command_id=2)
    Event_11005620(2, character=1000009, character_1=1000019, left=11005623, command_id=3)
    Event_11005620(3, character=1000009, character_1=1000020, left=11005624, command_id=4)
    Event_11005620(4, character=1000009, character_1=1000021, left=11005625, command_id=5)
    Event_11005620(5, character=1000009, character_1=1000022, left=11005626, command_id=6)
    Event_11005600()
    Event_11002501()
    Event_11002510(
        1,
        flag=11002521,
        flag_1=11002501,
        obj=1001001,
        character=1000000,
        item_lot_param_id=15100,
        item_lot_param_id_1=16100
    )
    Event_11005510(1, 1001001, 11002501, 11002521, 22679, 3.200000047683716)
    Event_11002004()
    Event_11005110(0, collision=1003202, collision_1=1003203, collision_2=1003201, region=1002001)
    Event_11005110(1, collision=1003205, collision_1=1003206, collision_2=1003204, region=1002002)
    Event_11005110(2, collision=1003209, collision_1=1003210, collision_2=1003214, region=1002003)
    Event_11005110(3, collision=1003211, collision_1=1003212, collision_2=1003213, region=1002004)
    Event_11002000()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableGravity(1000001)
    DisableGravity(1000002)


@NeverRestart(11000000)
def Event_11000000():
    """Event 11000000"""
    RegisterBonfire(bonfire_flag=11000992, obj=1001960)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=1001002)
    Event_11002001()


@NeverRestart(11005100)
def Event_11005100(_, other_entity: int, obj: int, animation_id: int):
    """Event 11005100"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@NeverRestart(11000100)
def Event_11000100():
    """Event 11000100"""
    AND_1.Add(FlagDisabled(11000100))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1001319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1001319, 0)


@NeverRestart(11000101)
def Event_11000101():
    """Event 11000101"""
    AND_1.Add(FlagDisabled(11000100))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001319,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1001319, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11000110)
def Event_11000110():
    """Event 11000110"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1001003, animation_id=1)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1001003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    Move(PLAYER, destination=1001003, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1001003, 1)
    DisplayDialog(text=10010866, anchor_entity=1001003)


@NeverRestart(11002000)
def Event_11002000():
    """Event 11002000"""
    MAIN.Await(ObjectActivated(obj_act_id=11000121))
    
    Wait(0.75)
    WarpToMap(game_map=NEW_LONDO_RUINS, player_start=1600991)


@NeverRestart(11002004)
def Event_11002004():
    """Event 11002004"""
    OR_1.Add(PlayerStandingOnCollision(1003207))
    OR_1.Add(PlayerStandingOnCollision(1003208))
    OR_2.Add(PlayerStandingOnCollision(1003213))
    OR_2.Add(PlayerStandingOnCollision(1003214))
    OR_2.Add(PlayerStandingOnCollision(1003200))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionFalse(10, input_condition=OR_1)
    DisableMapCollision(collision=1003213)
    DisableMapCollision(collision=1003214)
    DisableMapCollision(collision=1003200)
    OR_4.Add(PlayerStandingOnCollision(1003207))
    OR_4.Add(PlayerStandingOnCollision(1003208))
    
    MAIN.Await(not OR_4)
    
    EnableMapCollision(collision=1003213)
    EnableMapCollision(collision=1003214)
    EnableMapCollision(collision=1003200)
    Restart()
    DisableMapCollision(collision=1003207)
    DisableMapCollision(collision=1003208)
    OR_4.Add(PlayerStandingOnCollision(1003213))
    OR_4.Add(PlayerStandingOnCollision(1003214))
    OR_4.Add(PlayerStandingOnCollision(1003200))
    
    MAIN.Await(not OR_4)
    
    EnableMapCollision(collision=1003207)
    EnableMapCollision(collision=1003208)
    Restart()


@NeverRestart(11005110)
def Event_11005110(_, collision: int, collision_1: int, collision_2: int, region: int):
    """Event 11005110"""
    AND_1.Add(PlayerStandingOnCollision(collision))
    AND_2.Add(PlayerStandingOnCollision(collision_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(12, input_condition=AND_1)
    DisableMapCollision(collision=collision_2)
    AND_3.Add(PlayerStandingOnCollision(collision))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(not AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EnableMapCollision(collision=collision_2)
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_4)
    DisableMapCollision(collision=collision)
    DisableMapCollision(collision=collision_1)
    Wait(2.0)
    Restart()
    DisableMapCollision(collision=collision)
    DisableMapCollision(collision=collision_1)
    AND_3.Add(PlayerStandingOnCollision(collision_2))
    
    MAIN.Await(not AND_3)
    
    EnableMapCollision(collision=collision)
    EnableMapCollision(collision=collision_1)
    Restart()


@NeverRestart(11002001)
def Event_11002001():
    """Event 11002001"""
    DisableObjectActivation(1001004, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1001004, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1001004, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1001004, obj_act_id=-1, relative_index=3)
    if FlagEnabled(11002101):
        EndOfAnimation(obj=1001004, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=15000000,
        anchor_entity=1002000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    if FlagEnabled(11813506):
        DisplayDialog(text=10040003)
        ForceAnimation(1001004, 0)
        EnableFlag(11002101)
        End()
    DisplayDialog(text=10040002)
    Wait(3.0)
    Restart()


@RestartOnRest(11002500)
def Event_11002500():
    """Event 11002500"""
    DisableSoundEvent(sound_id=1003801)
    DisableCharacter(1000009)
    DisableObject(1001006)
    DeleteVFX(1003400, erase_root_only=False)
    if ThisEventFlagEnabled():
        Kill(1000009)
        Kill(1000010)
        Kill(1000011)
        Kill(1000012)
        Kill(1000013)
        Kill(1000014)
        Kill(1000015)
        Kill(1000016)
        Kill(1000017)
        Kill(1000018)
        Kill(1000019)
        Kill(1000020)
        Kill(1000021)
        Kill(1000022)
        Kill(1000023)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1002005))
    
    EnableFlag(11005500)
    EnableObject(1001006)
    CreateVFX(1003400)
    EnableCharacter(1000009)
    FadeInCharacter(character=1000009, duration=2.0)
    EnableSoundEvent(sound_id=1003801)
    EnableBossHealthBar(1000009, name=5200)
    
    MAIN.Await(CharacterDead(1000009))
    
    AwardItemLot(1070, host_only=True)
    EnableFlag(11813507)
    DisableBossHealthBar(1000009)
    DisableSoundEvent(sound_id=1003801)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)
    DisableObject(1001006)
    DeleteVFX(1003400)


@NeverRestart(11002002)
def Event_11002002():
    """Event 11002002"""
    End()


@RestartOnRest(11005610)
def Event_11005610(_, character: int, character_1: int, left: int, command_id: int):
    """Event 11005610"""
    DisableCharacter(character_1)
    if ValueNotEqual(left=left, right=11005611):
        AwaitThisEventSlotOn()
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=150))
    AND_1.Add(HealthRatioGreaterThan(character, value=0.0))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.On)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=140,
        copy_draw_parent=character,
    )
    EnableFlag(left)
    AICommand(character, command_id=command_id, command_slot=0)
    ForceAnimation(character_1, 8100)
    Wait(0.5)
    ForceAnimation(character, 8200)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=300))
    
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(character, command_id=1, command_slot=2)
    
    MAIN.Await(CharacterDead(character_1))
    
    AICommand(character, command_id=0, command_slot=2)


@RestartOnRest(11005620)
def Event_11005620(_, character: int, character_1: int, left: int, command_id: int):
    """Event 11005620"""
    DisableCharacter(character_1)
    if ValueNotEqual(left=left, right=11005621):
        AwaitThisEventSlotOn()
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=160))
    AND_1.Add(HealthRatioGreaterThan(character, value=0.0))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(character, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=2, switch_type=OnOffChange.On)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=141,
        copy_draw_parent=character,
    )
    EnableFlag(left)
    AICommand(character, command_id=command_id, command_slot=1)
    ForceAnimation(character_1, 8100)
    Wait(1.2999999523162842)
    ForceAnimation(character, 8210)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=600))
    
    ReplanAI(character)
    SetDisplayMask(character, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(character, command_id=1, command_slot=3)
    
    MAIN.Await(CharacterDead(character_1))
    
    AICommand(character, command_id=0, command_slot=3)


@RestartOnRest(11005600)
def Event_11005600():
    """Event 11005600"""
    DisableCharacter(1000016)
    DisableCharacter(1000023)
    OR_1.Add(FlagEnabled(11005500))
    OR_1.Add(FlagEnabled(11002500))
    OR_1.Add(FlagEnabled(11002002))
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFlagEnabled(2, 11002500)
    SkipLinesIfFlagEnabled(1, 11002002)
    SkipLines(3)
    Kill(1000016)
    Kill(1000023)
    End()
    EnableCharacter(1000016)
    EnableCharacter(1000023)
    AICommand(1000009, command_id=1, command_slot=2)
    AICommand(1000009, command_id=1, command_slot=3)
    AND_1.Add(CharacterDead(1000016))
    AND_2.Add(CharacterDead(1000023))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    AICommand(1000009, command_id=0, command_slot=2)
    
    MAIN.Await(CharacterDead(1000023))
    
    AICommand(1000009, command_id=0, command_slot=3)
    SkipLines(3)
    AICommand(1000009, command_id=0, command_slot=3)
    
    MAIN.Await(CharacterDead(1000016))
    
    AICommand(1000009, command_id=0, command_slot=2)


@RestartOnRest(11002501)
def Event_11002501():
    """Event 11002501"""
    if ThisEventFlagEnabled():
        DisableCharacter(1000000)
        Kill(1000000)
        End()
    if FlagDisabled(11002500):
        EnableInvincibility(1000000)
    
        MAIN.Await(FlagEnabled(11005500))
    
        FadeOutCharacter(character=1000000, duration=2.0)
        Wait(2.0)
        DisableCharacter(1000000)
    
        MAIN.Await(FlagEnabled(11002500))
    
        EnableCharacter(1000000)
        FadeInCharacter(character=1000000, duration=2.0)
        DisableInvincibility(1000000)
    
    MAIN.Await(CharacterDead(1000000))
    
    End()


@NeverRestart(11002510)
def Event_11002510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11002510"""
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


@NeverRestart(11005510)
def Event_11005510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11005510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()
