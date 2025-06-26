"""
Land of Shadow 11-11 NW SE

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76913, asset=2045461950)
    CommonFunc_90005250(0, character=2045460210, region=2045452200, seconds=0.0, animation_id=0)
    Event_2045462351(
        0,
        character=2045460240,
        animation_id=30001,
        animation_id_1=20001,
        region=2045462351,
        radius=1.0,
        seconds=0.0,
        left=2045462351,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2045462351(
        1,
        character=2045460246,
        animation_id=30001,
        animation_id_1=20001,
        region=2045462351,
        radius=1.0,
        seconds=0.0,
        left=2045462351,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2045462351(
        2,
        character=2045460247,
        animation_id=30001,
        animation_id_1=20001,
        region=2045462351,
        radius=1.0,
        seconds=0.0,
        left=2045462351,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2045460252,
        animation_id=30001,
        animation_id_1=20001,
        radius=20.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=2045460307, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460308, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460309, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460310, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460311, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460312, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460313, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460317, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2045460318, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005250(0, character=2045465220, region=2045462220, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2045465221, region=2045462227, seconds=0.0, animation_id=0)
    Event_2045462350(0, character=2045460350, region=2045462350, region_1=2045462351, radius=1.0)
    Event_2045462540(0, flag=2045460540, region=2045462540)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005301(0, flag=2045460200, character=2045460200, item_lot__unk1=2045460500, seconds=4.0, unk1=0)
    Event_2045462200(
        0,
        character=2045460200,
        animation_id=30007,
        animation_id_1=20007,
        region=2245462200,
        flag=2245462208,
    )
    CommonFunc_90005430(0, character=2045460200)
    Event_2045462210(0, character=2045460200, flag=2245462200, flag_1=2245462208)
    CommonFunc_90005435(
        0,
        character=2045460200,
        flag=2245462201,
        flag_1=2245462202,
        flag_2=2245462203,
        flag_3=2245462204,
    )
    CommonFunc_90005437(0, character=2045460200, flag=2045462208, flag_1=2045462209)
    CommonFunc_90005433(0, character=2045460200, flag=2245462205, flag_1=2245462206, flag_2=2245462207)
    CommonFunc_90005434(0, character=2045460200, flag=2245462205, flag_1=2245462206, flag_2=2245462207)
    CommonFunc_90005436(0, character=2045460200, region=2245462210, region_1=2245462211)


@RestartOnRest(2045462540)
def Event_2045462540(_, flag: Flag | int, region: Region | int):
    """Event 2045462540"""
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    End()


@RestartOnRest(2045462200)
def Event_2045462200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    flag: Flag | int,
):
    """Event 2045462200"""
    if FlagEnabled(2245462199):
        return
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(2245462199)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(2045462210)
def Event_2045462210(_, character: uint, flag: Flag | int, flag_1: Flag | int):
    """Event 2045462210"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableGravity(character)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 30010, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=320.0))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 20010, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    EnableGravity(character)
    AddSpecialEffect(character, 5006)
    ReplanAI(character)
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=340.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_1, radius=340.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_2, radius=340.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_3, radius=340.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_4, radius=340.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_5, radius=340.0))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(2245462203)
def Event_2245462203(_, character: uint, flag: Flag | int):
    """Event 2245462203"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableGravity(character)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    WaitRealFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 30010, loop=True)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=320.0))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 20010, loop=True)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    EnableGravity(character)
    AddSpecialEffect(character, 5006)
    ReplanAI(character)
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=350.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_1, radius=350.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_2, radius=350.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_3, radius=350.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_4, radius=350.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_5, radius=350.0))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(2045462350)
def Event_2045462350(_, character: uint, region: Region | int, region_1: Region | int, radius: float):
    """Event 2045462350"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=20011469):
        AddSpecialEffect(character, 20011469)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_4.Add(OR_2)
    GotoIfConditionFalse(Label.L0, input_condition=OR_4)
    AddSpecialEffect(character, 20011468)
    EnableNetworkFlag(2045462350)
    ForceAnimation(character, 3020)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 20011467)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5025):
        ForceAnimation(character, 3000)
    Wait(1.0)
    Restart()


@RestartOnRest(2045462351)
def Event_2045462351(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: Flag | int,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 2045462351"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
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
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(FlagEnabled(left))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()
