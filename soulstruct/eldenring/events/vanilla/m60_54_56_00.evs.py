"""
Northeast Mountaintops (SE) (SW)

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_54_56_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1054562200(0, character=1054565200)
    Event_1054562500()


@RestartOnRest(1054562200)
def Event_1054562200(_, character: uint):
    """Event 1054562200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@RestartOnRest(1054562500)
def Event_1054562500():
    """Event 1054562500"""
    if FlagEnabled(1254560800):
        return
    SetCharacterTalkRange(character=Characters.Dummy, distance=300.0)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005870(0, character=Characters.BorealistheFreezingFog, name=904503600, npc_threat_level=25)
    CommonFunc_90005861(
        0,
        flag=1254560800,
        left=0,
        character=Characters.BorealistheFreezingFog,
        left_1=1,
        item_lot__item_lot_param_id=30510,
        text=30066,
        seconds=0.0,
    )
    Event_1054562815()
    Event_1054562820(
        0,
        1054560800,
        30003,
        20003,
        1054562830,
        0.0,
        0.0,
        0,
        0,
        0,
        0,
        1054562831,
        1054562832,
        1054562833,
        1054562834,
        1054562835,
    )


@RestartOnRest(1054562815)
def Event_1054562815():
    """Event 1054562815"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1054562811))
    AwaitConditionTrue(OR_1)
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=1254560800)
    GotoIfSpecialStandbyEndedFlagEnabled(Label.L1, character=Characters.BorealistheFreezingFog)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1054562810))
    GotoIfConditionTrue(Label.L2, input_condition=OR_2)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=1054562812))
    GotoIfConditionFalse(Label.L3, input_condition=OR_3)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    RemoveSpecialEffect(PLAYER, 4213)
    SetWeather(weather=Weather.HeavySnow, duration=30.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    SetWeather(weather=Weather.SnowyHeavyFog, duration=-1.0, immediate_change=False)
    Wait(5.0)
    AddSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SetWeather(weather=Weather.HeavySnow, duration=30.0, immediate_change=False)
    Wait(3.0)
    RemoveSpecialEffect(PLAYER, 4213)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(PLAYER, 4213)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    End()


@RestartOnRest(1054562820)
def Event_1054562820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    region_1: uint,
    region_2: uint,
    region_3: uint,
    region_4: uint,
    region_5: uint,
):
    """Event 1054562820"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OutsideMap(game_map=SPIRITCALLER_CAVE))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(WeatherState(weather=Weather.SnowyHeavyFog, unk_4_8=3.0, unk_8_12=0.0))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableNetworkFlag(1054562820)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    GotoIfConditionTrue(Label.L5, input_condition=OR_5)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    GotoIfConditionTrue(Label.L6, input_condition=OR_6)
    OR_7.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    GotoIfConditionTrue(Label.L7, input_condition=OR_7)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    GotoIfConditionTrue(Label.L8, input_condition=OR_8)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    GotoIfConditionTrue(Label.L9, input_condition=OR_8)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    GotoIfConditionTrue(Label.L10, input_condition=OR_8)
    Goto(Label.L14)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(character, destination=1054562820, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 6 --- #
    DefineLabel(6)
    Move(character, destination=1054562821, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 7 --- #
    DefineLabel(7)
    Move(character, destination=1054562822, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 8 --- #
    DefineLabel(8)
    Move(character, destination=1054562823, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 9 --- #
    DefineLabel(9)
    Move(character, destination=1054562824, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 10 --- #
    DefineLabel(10)
    Move(character, destination=1054562825, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L14)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(character, 10206)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()
