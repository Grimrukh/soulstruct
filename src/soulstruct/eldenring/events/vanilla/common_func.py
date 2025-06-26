"""
Common functions that can be imported and used in other EVS scripts.

linked:


strings:

"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@RestartOnRest(90005200)
def CommonFunc_90005200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """CommonFunc 90005200"""
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
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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


@RestartOnRest(90005201)
def CommonFunc_90005201(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """CommonFunc 90005201"""
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
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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


@RestartOnRest(90005210)
def CommonFunc_90005210(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """CommonFunc 90005210"""
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
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(AND_3)
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


@RestartOnRest(90005211)
def CommonFunc_90005211(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """CommonFunc 90005211"""
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


@RestartOnRest(90005213)
def CommonFunc_90005213(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    character_1: Character | int,
    seconds_1: float,
):
    """CommonFunc 90005213"""
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
    AND_11.Add(SpecialStandbyEndedFlagEnabled(character=character_1))
    OR_3.Add(AND_11)
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
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_11)
    Wait(seconds)
    SkipLines(1)
    Wait(seconds_1)
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


@RestartOnRest(90005220)
def CommonFunc_90005220(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
):
    """CommonFunc 90005220"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_2, right=0):
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


@RestartOnRest(90005221)
def CommonFunc_90005221(_, character: uint, animation_id: int, animation_id_1: int, seconds: float, left: uint):
    """CommonFunc 90005221"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
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


@RestartOnRest(90005250)
def CommonFunc_90005250(_, character: uint, region: Region | int, seconds: float, animation_id: int):
    """CommonFunc 90005250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005251)
def CommonFunc_90005251(_, character: uint, radius: float, seconds: float, animation_id: int):
    """CommonFunc 90005251"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005260)
def CommonFunc_90005260(_, character: uint, region: Region | int, radius: float, seconds: float, animation_id: int):
    """CommonFunc 90005260"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(AND_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005261)
def CommonFunc_90005261(_, character: uint, region: Region | int, radius: float, seconds: float, animation_id: int):
    """CommonFunc 90005261"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005263)
def CommonFunc_90005263(
    _,
    character: uint,
    region: Region | int,
    radius: float,
    seconds: float,
    animation_id: int,
    region_1: Region | int,
):
    """CommonFunc 90005263"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if UnsignedNotEqual(left=region_1, right=0):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    SkipLinesIfConditionFalse(1, OR_3)
    ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005271)
def CommonFunc_90005271(_, character: uint, seconds: float, animation_id: int):
    """CommonFunc 90005271"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
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
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(90005300)
def CommonFunc_90005300(_, flag: Flag | int, character: uint, item_lot: int, seconds: float, left: int):
    """CommonFunc 90005300"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    if ValueNotEqual(left=left, right=0):
        DisableCharacter(character)
        DropMandatoryTreasure(character)
        End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterProportionDead(character=character))
    
    Wait(seconds)
    EnableFlag(flag)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=left, right=1):
        return
    if ValueEqual(left=item_lot, right=0):
        return
    AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(90005301)
def CommonFunc_90005301(_, flag: Flag | int, character: uint, item_lot__unk1: uint, seconds: float, unk1: uint):
    """CommonFunc 90005301"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfUnknown_1000_109(Label.L3, unk1=unk1, unk2=0)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterProportionDead(character=character))
    
    Wait(seconds)
    EnableFlag(flag)
    if PlayerNotInOwnWorld():
        return
    GotoIfUnknown_1000_111(Label.L0, unk1=unk1, unk2=1)
    GotoIfUnknown_1000_111(Label.L0, unk1=item_lot__unk1, unk2=0)
    AwardItemLot(item_lot__unk1, host_only=True)
    End()


@RestartOnRest(90005360)
def CommonFunc_90005360(_, flag: Flag | int, character: uint, item_lot: int):
    """CommonFunc 90005360"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisplayBanner(BannerType.Unknown14)
    if PlayerNotInOwnWorld():
        return
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(90005390)
def CommonFunc_90005390(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    anchor_entity: uint,
    character: Character | int,
    left: int,
    item_lot: int,
):
    """CommonFunc 90005390"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=601111, anchor_entity=anchor_entity, dummy_id=960, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=601110, anchor_entity=anchor_entity, dummy_id=960, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(3.0)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if ValueNotEqual(left=item_lot, right=0):
        AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(90005391)
def CommonFunc_90005391(_, flag: Flag | int, flag_1: Flag | int, character: uint, character_1: uint, left: int):
    """CommonFunc 90005391"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableGravity(character_1)
    DisableAI(character_1)
    SetCharacterFadeOnEnable(character=character_1, state=True)
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, True)
    SetBackreadStateAlternate(character_1, True)
    Wait(0.5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=character,
    )
    Wait(0.5)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=601101, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=601100, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    DisableCharacter(character)
    SetBackreadStateAlternate(character, False)
    SetBackreadStateAlternate(character_1, False)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_1)


@RestartOnRest(90005400)
def CommonFunc_90005400(_, character: uint, special_effect: int, seconds: float, seconds_1: float, left: uint):
    """CommonFunc 90005400"""
    if ThisEventSlotFlagEnabled():
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    if ValueNotEqual(left=special_effect, right=0):
        AddSpecialEffect(character, special_effect)
    else:
        AddSpecialEffect(character, 4421)
    ForceAnimation(character, 14100, loop=True)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasSpecialEffect(character, 5112))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5111))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5112):
        Wait(seconds_1)
    else:
        Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, 14102, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(90005401)
def CommonFunc_90005401(_, flag: Flag | int, character: Character | int):
    """CommonFunc 90005401"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 4430)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 4431))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(90005410)
def CommonFunc_90005410(_, flag: Flag | int, character: Character | int, entity_b: uint):
    """CommonFunc 90005410"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 9500))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    Unknown_2004_71(unk_0_4=0, entity_a=0, entity_b=entity_b)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterHasSpecialEffect(ALL_PLAYERS, 202))
    OR_3.Add(AND_3)
    OR_3.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_3)
    
    if PlayerInOwnWorld():
        DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005411)
def CommonFunc_90005411(_, asset: Asset | int, character: Character | int, left: uint):
    """CommonFunc 90005411"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if UnsignedEqual(left=left, right=0):
        WaitFrames(frames=1)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=620)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9502))
    
    DeleteAssetVFX(asset)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9503))
    
    Restart()


@RestartOnRest(90005420)
def CommonFunc_90005420(
    _,
    character: uint,
    caravan_asset__parent_asset: Asset | int,
    child_asset: Asset | int,
    character_1: Character | int,
    character_2: Character | int,
    character_3: Character | int,
    seconds: float,
):
    """CommonFunc 90005420"""
    DisableAnimations(character)
    AttachCaravanToController(caravan_asset=caravan_asset__parent_asset, character=character)
    AttachAssetToAsset(child_asset=child_asset, parent_asset=caravan_asset__parent_asset, parent_dummy_id=151)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ConnectCharacterToCaravan(character=character_2, caravan_asset=caravan_asset__parent_asset)
    ConnectCharacterToCaravan(character=character_3, caravan_asset=caravan_asset__parent_asset)
    End()
    Wait(seconds)


@RestartOnRest(90005421)
def CommonFunc_90005421(_, character: uint, asset: Asset | int, flag: Flag | int):
    """CommonFunc 90005421"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    AND_1.Add(CharacterHasSpecialEffect(character, 11500))
    AND_1.Add(FlagDisabled(character))
    
    MAIN.Await(AND_1)
    
    EnableAssetActivation(asset, obj_act_id=-1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 11500))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(90005422)
def CommonFunc_90005422(_, flag: Flag | int, asset: Asset | int, obj_act_id: uint):
    """CommonFunc 90005422"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableTreasure(asset=asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(asset=asset)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_1.Add(AND_1)
    OR_1.Add(AssetDestroyed(asset))
    
    MAIN.Await(OR_1)
    
    Wait(3.200000047683716)
    EnableTreasure(asset=asset)


@RestartOnRest(90005423)
def CommonFunc_90005423(_, character: Character | int):
    """CommonFunc 90005423"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5551))
    
    MAIN.Await(AND_1)
    
    ConnectCharacterToCaravan(character=character, caravan_asset=0)
    ChangeCharacterCloth(character, bit_count=20, state_id=2)


@RestartOnRest(90005424)
def CommonFunc_90005424(
    _,
    asset: Asset | int,
    character: Character | int,
    character_1: Character | int,
    character_2: Character | int,
    asset_1: Asset | int,
):
    """CommonFunc 90005424"""
    MAIN.Await(AssetDestroyed(asset))
    
    ChangeCharacterCloth(character, bit_count=20, state_id=2)
    ChangeCharacterCloth(character_1, bit_count=20, state_id=2)
    AddSpecialEffect(character, 5551)
    AddSpecialEffect(character_1, 5551)
    Kill(character_2, award_runes=True)
    DisableAsset(asset_1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    EnableTreasure(asset=asset)


@RestartOnRest(90005430)
def CommonFunc_90005430(_, character: Character | int):
    """CommonFunc 90005430"""
    SetBackreadStateAlternate(character, True)
    SetCharacterEnableDistance(character=character, distance=2000.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=223, state=False)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    EnableThisNetworkSlotFlag()
    End()


@RestartOnRest(90005431)
def CommonFunc_90005431(_, character: Character | int):
    """CommonFunc 90005431"""
    SetBackreadStateAlternate(character, True)
    SetCharacterEnableDistance(character=character, distance=2000.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)
    SetLockOnPoint(character=character, lock_on_dummy_id=221, state=False)
    SetLockOnPoint(character=character, lock_on_dummy_id=222, state=False)
    if ThisEventSlotFlagDisabled():
        CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part1, part_health=99999)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=-1,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=120,
        unk_24_28=112,
    )
    EnableThisNetworkSlotFlag()
    End()


@RestartOnRest(90005432)
def CommonFunc_90005432(_, character: uint, flag: Flag | int):
    """CommonFunc 90005432"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableGravity(character)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    WaitRealFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=19627):
        ForceAnimation(character, 30010, loop=True)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=200.0))
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
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_1, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_2, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_3, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_4, radius=220.0))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=CLIENT_PLAYER_5, radius=220.0))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(90005433)
def CommonFunc_90005433(_, character: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """CommonFunc 90005433"""
    WaitRealFrames(frames=1)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_1.Add(CharacterPartHealth(character, npc_part_id=30) <= 0)
    OR_1.Add(CharacterHasSpecialEffect(character, 20011126))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L4, character=character, special_effect=20011126)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    ForceAnimation(character, 20003, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    ForceAnimation(character, 20003, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_2)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    Wait(0.10000000149011612)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20000, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=9999)
    Wait(5.0)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=560)
    Restart()


@RestartOnRest(90005434)
def CommonFunc_90005434(_, character: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """CommonFunc 90005434"""
    WaitRealFrames(frames=1)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_1.Add(CharacterPartHealth(character, npc_part_id=31) <= 0)
    OR_1.Add(CharacterHasSpecialEffect(character, 20011126))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L4, character=character, special_effect=20011126)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    ForceAnimation(character, 20005, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    ForceAnimation(character, 20005, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_2)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    Wait(0.10000000149011612)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20001, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=9999)
    Wait(5.0)
    CreateNPCPart(character, npc_part_id=31, part_index=NPCPartType.Part4, part_health=560)
    Restart()


@RestartOnRest(90005435)
def CommonFunc_90005435(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """CommonFunc 90005435"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 20011113))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableFlag(flag_3)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(character, 20009, wait_for_completion=True)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(90005436)
def CommonFunc_90005436(_, character: Character | int, region: Region | int, region_1: Region | int):
    """CommonFunc 90005436"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 20011132)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    OR_1.Add(CharacterOutsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(PLAYER, 20011132)
    Restart()


@RestartOnRest(90005437)
def CommonFunc_90005437(_, character: uint, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005437"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 20011135))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L3, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag)
    EnableFlag(flag)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag_1)
    ForceAnimation(character, 20006)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20009, wait_for_completion=True)
    DisableFlag(flag)
    DisableFlag(flag_1)
    WaitRealFrames(frames=1)
    Restart()


@ContinueOnRest(90005440)
def CommonFunc_90005440(_, character: uint, character_1: uint):
    """CommonFunc 90005440"""
    AddSpecialEffect(character_1, 14500)
    DisableHealthBar(character_1)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3245))
    AND_1.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=6.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(character)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, 14501)
    AddSpecialEffect(character_1, 14502)
    EnableHealthBar(character_1)
    SetLockOnPoint(character=character_1, lock_on_dummy_id=220, state=True)
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 3245))
    OR_2.Add(EntityBeyondDistance(entity=character_1, other_entity=PLAYER, radius=6.0))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character_1, 14503))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    Restart()
    AICommand(0, command_id=0, command_slot=0)
    EzstateAIRequest(0, command_id=0, command_slot=0)


@RestartOnRest(90005445)
def CommonFunc_90005445(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: Asset | int,
):
    """CommonFunc 90005445"""
    if AssetDestroyed(asset):
        DisableAsset(asset)
        End()
    if SpecialStandbyEndedFlagEnabled(character=character):
        DisableAsset(asset)
        End()
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    EnableAssetInvulnerability(asset)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(90005446)
def CommonFunc_90005446(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: Asset | int,
):
    """CommonFunc 90005446"""
    if AssetDestroyed(asset):
        DisableAsset(asset)
        End()
    if SpecialStandbyEndedFlagEnabled(character=character):
        DisableAsset(asset)
        End()
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    EnableAssetInvulnerability(asset)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(90005450)
def CommonFunc_90005450(_, character: Character | int, asset: Asset | int, asset_1: Asset | int, asset_2: Asset | int):
    """CommonFunc 90005450"""
    SetBackreadStateAlternate(character, True)
    EnableImmortality(character)
    SetCharacterEnableDistance(character=character, distance=2000.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)
    DisableHealthBar(character)
    AttachAssetToCharacter(character=character, dummy_id=100, asset=asset)
    AttachAssetToCharacter(character=character, dummy_id=80, asset=asset_1)
    AttachAssetToCharacter(character=character, dummy_id=165, asset=asset_2)


@RestartOnRest(90005451)
def CommonFunc_90005451(_, character: Character | int, asset_group: Asset | int):
    """CommonFunc 90005451"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(AssetProportionDestructionState(
        state=True,
        asset_group=asset_group,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_proportion=0.44999998807907104,
    ))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 12450)


@RestartOnRest(90005452)
def CommonFunc_90005452(_, character: Character | int, flag: Flag | int):
    """CommonFunc 90005452"""
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 12455))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)


@RestartOnRest(90005453)
def CommonFunc_90005453(_, asset__character: uint, asset: Asset | int, dummy_id: int, seconds: float):
    """CommonFunc 90005453"""
    if AssetDestroyed(asset):
        return
    AttachAssetToCharacter(character=asset__character, dummy_id=dummy_id, asset=asset)
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    GotoIfConditionFalse(Label.L10, input_condition=OR_10)
    EnableAssetInvulnerability(asset)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(AssetDestroyed(asset__character))
    OR_1.Add(CharacterHasSpecialEffect(asset__character, 12460))
    
    MAIN.Await(OR_1)
    
    if AssetDestroyed(asset):
        return
    EnableAssetInvulnerability(asset)
    Wait(seconds)
    DestroyAsset(asset, request_slot=0)


@RestartOnRest(90005454)
def CommonFunc_90005454(_, character: uint, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005454"""
    if FlagEnabled(flag_1):
        ForceAnimation(character, 30001, loop=True)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AddSpecialEffect(character, 5005)
    ReplanAI(character)
    DisableGravity(character)
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        ForceAnimation(character, 30001, loop=True)
    else:
        ForceAnimation(character, 0, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=200.0))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5006)
    ReplanAI(character)
    EnableGravity(character)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=220.0))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005456)
def CommonFunc_90005456(_, character: Character | int, asset: Asset | int, asset_1: Asset | int, flag: Flag | int):
    """CommonFunc 90005456"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(asset, obj_act_id=-1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    AND_1.Add(CharacterHasSpecialEffect(character, 12455))
    
    MAIN.Await(AND_1)
    
    EnableAssetActivation(asset, obj_act_id=-1)
    EnableAssetActivation(asset_1, obj_act_id=-1)


@RestartOnRest(90005457)
def CommonFunc_90005457(_, character: Character | int, asset: Asset | int, asset_1: Asset | int, asset_2: Asset | int):
    """CommonFunc 90005457"""
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=12455)
    DisableAsset(asset)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    EndOfAnimation(asset=asset_1, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AttachAssetToCharacter(character=character, dummy_id=100, asset=asset)
    EndOfAnimation(asset=asset_1, animation_id=1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    DisableAssetActivation(asset_2, obj_act_id=-1)
    AND_1.Add(CharacterHasSpecialEffect(character, 12455))
    
    MAIN.Await(AND_1)
    
    DisableAsset(asset)
    EnableAssetActivation(asset_2, obj_act_id=-1)


@RestartOnRest(90005458)
def CommonFunc_90005458(_, character: Character | int, asset: Asset | int):
    """CommonFunc 90005458"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AttachAssetToCharacter(character=character, dummy_id=166, asset=asset)
    DisableAsset(asset)
    AND_1.Add(CharacterHasSpecialEffect(character, 12465))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(asset)
    EnableThisNetworkSlotFlag()
    End()


@RestartOnRest(90005459)
def CommonFunc_90005459(_, copy_draw_parent: uint, flag: Flag | int, character: uint):
    """CommonFunc 90005459"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        dummy_id=270,
        copy_draw_parent=copy_draw_parent,
    )


@RestartOnRest(90005460)
def CommonFunc_90005460(_, character: Character | int):
    """CommonFunc 90005460"""
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=60, part_index=NPCPartType.Part6, part_health=999999999)
    SetNPCPartEffects(
        character,
        npc_part_id=60,
        material_sfx_id=124,
        material_vfx_id=124,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )


@RestartOnRest(90005461)
def CommonFunc_90005461(_, character: uint):
    """CommonFunc 90005461"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 11753))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=11)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=11)
    AND_2.Add(OR_2)
    AND_3.Add(CharacterPartHealth(character, npc_part_id=10) <= 10)
    AND_3.Add(CharacterPartHealth(character, npc_part_id=20) <= 1)
    AND_4.Add(CharacterPartHealth(character, npc_part_id=10) <= 9)
    AND_4.Add(CharacterPartHealth(character, npc_part_id=20) <= 2)
    AND_5.Add(CharacterPartHealth(character, npc_part_id=10) <= 8)
    AND_5.Add(CharacterPartHealth(character, npc_part_id=20) <= 3)
    AND_6.Add(CharacterPartHealth(character, npc_part_id=10) <= 7)
    AND_6.Add(CharacterPartHealth(character, npc_part_id=20) <= 4)
    AND_7.Add(CharacterPartHealth(character, npc_part_id=10) <= 6)
    AND_7.Add(CharacterPartHealth(character, npc_part_id=20) <= 5)
    AND_8.Add(CharacterPartHealth(character, npc_part_id=10) <= 5)
    AND_8.Add(CharacterPartHealth(character, npc_part_id=20) <= 6)
    AND_9.Add(CharacterPartHealth(character, npc_part_id=10) <= 4)
    AND_9.Add(CharacterPartHealth(character, npc_part_id=20) <= 7)
    AND_10.Add(CharacterPartHealth(character, npc_part_id=10) <= 3)
    AND_10.Add(CharacterPartHealth(character, npc_part_id=20) <= 8)
    AND_11.Add(CharacterPartHealth(character, npc_part_id=10) <= 2)
    AND_11.Add(CharacterPartHealth(character, npc_part_id=20) <= 9)
    AND_12.Add(CharacterPartHealth(character, npc_part_id=10) <= 1)
    AND_12.Add(CharacterPartHealth(character, npc_part_id=20) <= 10)
    OR_15.Add(CharacterPartHealth(character, npc_part_id=10) <= 0)
    OR_15.Add(CharacterPartHealth(character, npc_part_id=20) <= 0)
    OR_15.Add(AND_3)
    OR_15.Add(AND_4)
    OR_15.Add(AND_5)
    OR_15.Add(AND_6)
    OR_15.Add(AND_7)
    OR_15.Add(AND_8)
    OR_15.Add(AND_9)
    OR_15.Add(AND_10)
    OR_15.Add(AND_11)
    OR_15.Add(AND_12)
    OR_15.Add(CharacterHasSpecialEffect(character, 11753))
    
    MAIN.Await(OR_15)
    
    SetNPCPartHealth(character, npc_part_id=10, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(character, npc_part_id=20, desired_health=0, overwrite_max=False)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=11753):
        ForceAnimation(character, 20001)
    Wait(2.0)
    Restart()


@RestartOnRest(90005462)
def CommonFunc_90005462(_, character: uint):
    """CommonFunc 90005462"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 11752))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=11)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=11)
    AND_3.Add(CharacterPartHealth(character, npc_part_id=30) <= 10)
    AND_3.Add(CharacterPartHealth(character, npc_part_id=50) <= 1)
    AND_4.Add(CharacterPartHealth(character, npc_part_id=30) <= 9)
    AND_4.Add(CharacterPartHealth(character, npc_part_id=50) <= 2)
    AND_5.Add(CharacterPartHealth(character, npc_part_id=30) <= 8)
    AND_5.Add(CharacterPartHealth(character, npc_part_id=50) <= 3)
    AND_6.Add(CharacterPartHealth(character, npc_part_id=30) <= 7)
    AND_6.Add(CharacterPartHealth(character, npc_part_id=50) <= 4)
    AND_7.Add(CharacterPartHealth(character, npc_part_id=30) <= 6)
    AND_7.Add(CharacterPartHealth(character, npc_part_id=50) <= 5)
    AND_8.Add(CharacterPartHealth(character, npc_part_id=30) <= 5)
    AND_8.Add(CharacterPartHealth(character, npc_part_id=50) <= 6)
    AND_9.Add(CharacterPartHealth(character, npc_part_id=30) <= 4)
    AND_9.Add(CharacterPartHealth(character, npc_part_id=50) <= 7)
    AND_10.Add(CharacterPartHealth(character, npc_part_id=30) <= 3)
    AND_10.Add(CharacterPartHealth(character, npc_part_id=50) <= 8)
    AND_11.Add(CharacterPartHealth(character, npc_part_id=30) <= 2)
    AND_11.Add(CharacterPartHealth(character, npc_part_id=50) <= 9)
    AND_12.Add(CharacterPartHealth(character, npc_part_id=30) <= 1)
    AND_12.Add(CharacterPartHealth(character, npc_part_id=50) <= 10)
    OR_15.Add(CharacterPartHealth(character, npc_part_id=30) <= 0)
    OR_15.Add(CharacterPartHealth(character, npc_part_id=50) <= 0)
    OR_15.Add(AND_3)
    OR_15.Add(AND_4)
    OR_15.Add(AND_5)
    OR_15.Add(AND_6)
    OR_15.Add(AND_7)
    OR_15.Add(AND_8)
    OR_15.Add(AND_9)
    OR_15.Add(AND_10)
    OR_15.Add(AND_11)
    OR_15.Add(AND_12)
    
    MAIN.Await(OR_15)
    
    SetNPCPartHealth(character, npc_part_id=30, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(character, npc_part_id=50, desired_health=0, overwrite_max=False)
    ForceAnimation(character, 20000)
    Wait(2.0)
    Restart()


@RestartOnRest(90005463)
def CommonFunc_90005463(_, character: uint, character_1: Character | int):
    """CommonFunc 90005463"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_10.Add(EventValue(flag=character, bit_count=3) >= 5)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character_1))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 11757))
    OR_10.Add(AND_1)
    
    MAIN.Await(OR_10)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, 11757)


@RestartOnRest(90005464)
def CommonFunc_90005464(_, flag: Flag | int, character: uint, character_1: uint, value: uint):
    """CommonFunc 90005464"""
    AND_15.Add(EventValue(flag=flag, bit_count=3) > value)
    if AND_15:
        return
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, 11771))
    AND_1.Add(EventValue(flag=flag, bit_count=3) == value)
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    IncrementEventValue(flag, bit_count=3, max_value=5)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 20000)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=70,
        copy_draw_parent=character,
    )
    Wait(3.0)
    EnableAnimations(character_1)
    EnableAI(character_1)


@RestartOnRest(90005470)
def CommonFunc_90005470(_, character: uint):
    """CommonFunc 90005470"""
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    if CharacterHasSpecialEffect(character=character, special_effect=12160):
        CreateNPCPart(
            character,
            npc_part_id=20,
            part_index=NPCPartType.Part2,
            part_health=80,
            body_damage_correction=3.0,
        )
        SetNPCPartEffects(
            character,
            npc_part_id=20,
            material_sfx_id=120,
            material_vfx_id=120,
            unk_16_20=-1,
            unk_20_24=-1,
            unk_24_28=-1,
        )
    if CharacterHasSpecialEffect(character=character, special_effect=12161):
        CreateNPCPart(
            character,
            npc_part_id=30,
            part_index=NPCPartType.Part3,
            part_health=80,
            body_damage_correction=3.0,
        )
        SetNPCPartEffects(
            character,
            npc_part_id=30,
            material_sfx_id=120,
            material_vfx_id=120,
            unk_16_20=-1,
            unk_20_24=-1,
            unk_24_28=-1,
        )
    if CharacterHasSpecialEffect(character=character, special_effect=12162):
        CreateNPCPart(
            character,
            npc_part_id=40,
            part_index=NPCPartType.Part4,
            part_health=75,
            body_damage_correction=3.0,
        )
        SetNPCPartEffects(
            character,
            npc_part_id=40,
            material_sfx_id=120,
            material_vfx_id=120,
            unk_16_20=-1,
            unk_20_24=-1,
            unk_24_28=-1,
        )
    if CharacterHasSpecialEffect(character=character, special_effect=12163):
        CreateNPCPart(
            character,
            npc_part_id=50,
            part_index=NPCPartType.Part5,
            part_health=75,
            body_damage_correction=3.0,
        )
        SetNPCPartEffects(
            character,
            npc_part_id=50,
            material_sfx_id=120,
            material_vfx_id=120,
            unk_16_20=-1,
            unk_20_24=-1,
            unk_24_28=-1,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    if CharacterHasSpecialEffect(character=character, special_effect=12160):
        AND_2.Add(CharacterPartHealth(character, npc_part_id=20) <= 0)
        AND_2.Add(CharacterHasSpecialEffect(character, 12156))
        AND_2.Add(CharacterHasSpecialEffect(character, 12168))
        AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
        AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
        OR_2.Add(AND_2)
    if CharacterHasSpecialEffect(character=character, special_effect=12161):
        AND_3.Add(CharacterPartHealth(character, npc_part_id=30) <= 0)
        AND_3.Add(CharacterHasSpecialEffect(character, 12156))
        AND_3.Add(CharacterHasSpecialEffect(character, 12169))
        AND_3.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
        AND_3.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
        OR_3.Add(AND_3)
    if CharacterHasSpecialEffect(character=character, special_effect=12162):
        AND_4.Add(CharacterPartHealth(character, npc_part_id=40) <= 0)
        AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
        AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
        OR_4.Add(AND_4)
    if CharacterHasSpecialEffect(character=character, special_effect=12163):
        AND_5.Add(CharacterPartHealth(character, npc_part_id=50) <= 0)
        AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
        AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
        OR_5.Add(AND_5)
    OR_9.Add(OR_2)
    OR_9.Add(OR_3)
    OR_9.Add(OR_4)
    OR_9.Add(OR_5)
    
    MAIN.Await(OR_9)
    
    GotoIfLastConditionResultTrue(Label.L5, input_condition=OR_5)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=OR_4)
    GotoIfLastConditionResultTrue(Label.L3, input_condition=OR_3)
    GotoIfLastConditionResultTrue(Label.L2, input_condition=OR_2)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(character, 20011, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 20008, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=12156):
        ForceAnimation(character, 20006, wait_for_completion=True)
    else:
        ForceAnimation(character, 20010, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=12156):
        ForceAnimation(character, 20007, wait_for_completion=True)
    else:
        ForceAnimation(character, 2009, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)
    if CharacterHasSpecialEffect(character=character, special_effect=12160):
        SetNPCPartHealth(character, npc_part_id=20, desired_health=9999999, overwrite_max=False)
    if CharacterHasSpecialEffect(character=character, special_effect=12161):
        SetNPCPartHealth(character, npc_part_id=30, desired_health=9999999, overwrite_max=False)
    if CharacterHasSpecialEffect(character=character, special_effect=12162):
        SetNPCPartHealth(character, npc_part_id=40, desired_health=9999999, overwrite_max=False)
    if CharacterHasSpecialEffect(character=character, special_effect=12163):
        SetNPCPartHealth(character, npc_part_id=50, desired_health=9999999, overwrite_max=False)
    Wait(1.0)
    Restart()


@RestartOnRest(90005471)
def CommonFunc_90005471(_, character: uint):
    """CommonFunc 90005471"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 12160))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagEnabled():
        SetNPCPartHealth(character, npc_part_id=20, desired_health=9999999, overwrite_max=False)
        Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterPartHealth(character, npc_part_id=20) <= 0)
    AND_2.Add(CharacterHasSpecialEffect(character, 12156))
    AND_2.Add(CharacterHasSpecialEffect(character, 12168))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, 12170))
    
    MAIN.Await(OR_2)
    
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=12170):
        ForceAnimation(character, 20011, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=20, part_index=NPCPartType.Part2, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=20,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90005472)
def CommonFunc_90005472(_, character: uint):
    """CommonFunc 90005472"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 12161))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagEnabled():
        SetNPCPartHealth(character, npc_part_id=30, desired_health=9999999, overwrite_max=False)
        Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterPartHealth(character, npc_part_id=30) <= 0)
    AND_2.Add(CharacterHasSpecialEffect(character, 12156))
    AND_2.Add(CharacterHasSpecialEffect(character, 12169))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, 12170))
    
    MAIN.Await(OR_2)
    
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=12170):
        ForceAnimation(character, 20008, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=80, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=30,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90004473)
def CommonFunc_90004473(_, character: uint):
    """CommonFunc 90004473"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 12162))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagEnabled():
        SetNPCPartHealth(character, npc_part_id=40, desired_health=9999999, overwrite_max=False)
        Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterPartHealth(character, npc_part_id=40) <= 0)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, 12170))
    
    MAIN.Await(OR_2)
    
    GotoIfCharacterHasSpecialEffect(Label.L9, character=character, special_effect=12170)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=12156)
    ForceAnimation(character, 20006, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20010, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=40,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(90005474)
def CommonFunc_90005474(_, character: uint):
    """CommonFunc 90005474"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 12163))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 12170))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagEnabled():
        SetNPCPartHealth(character, npc_part_id=50, desired_health=9999999, overwrite_max=False)
        Goto(Label.L0)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterPartHealth(character, npc_part_id=50) <= 0)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 12171))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, 12170))
    
    MAIN.Await(OR_2)
    
    GotoIfCharacterHasSpecialEffect(Label.L9, character=character, special_effect=12170)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=12156)
    ForceAnimation(character, 20007, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20009, wait_for_completion=True)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=75, body_damage_correction=3.0)
    SetNPCPartEffects(
        character,
        npc_part_id=50,
        material_sfx_id=120,
        material_vfx_id=120,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@ContinueOnRest(90005476)
def CommonFunc_90005476(_, character: uint, character_1: uint):
    """CommonFunc 90005476"""
    AND_9.Add(CharacterAlive(character))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHasSpecialEffect(character, 11805))
    
    MAIN.Await(AND_1)
    
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=230,
        copy_draw_parent=character_1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(90005480)
def CommonFunc_90005480(_, character: uint):
    """CommonFunc 90005480"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16472))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16473))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16474))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16475))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfThisEventSlotFlagDisabled(2)
    OR_3.Add(CharacterPartHealthComparison(character, npc_part_id=30, value=0, comparison_type=ComparisonType.Equal))
    SkipLinesIfConditionFalse(3, OR_3)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=30, part_index=NPCPartType.Part3, part_health=61)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    OR_4.Add(CharacterPartHealthComparison(character, npc_part_id=40, value=0, comparison_type=ComparisonType.Equal))
    SkipLinesIfConditionFalse(3, OR_4)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=40, part_index=NPCPartType.Part4, part_health=61)
    SetDisplayMask(character, bit_index=11, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    OR_5.Add(CharacterPartHealthComparison(character, npc_part_id=50, value=0, comparison_type=ComparisonType.Equal))
    SkipLinesIfConditionFalse(3, OR_5)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=50, part_index=NPCPartType.Part5, part_health=61)
    SetDisplayMask(character, bit_index=12, switch_type=OnOffChange.Off)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    OR_6.Add(CharacterPartHealthComparison(character, npc_part_id=60, value=0, comparison_type=ComparisonType.Equal))
    SkipLinesIfConditionFalse(3, OR_6)
    AddSpecialEffect(character, 16498)
    CreateNPCPart(character, npc_part_id=60, part_index=NPCPartType.Part6, part_health=61)
    SetDisplayMask(character, bit_index=13, switch_type=OnOffChange.Off)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterPartHealth(character, npc_part_id=30) <= 0)
    AND_4.Add(CharacterPartHealth(character, npc_part_id=40) <= 0)
    AND_5.Add(CharacterPartHealth(character, npc_part_id=50) <= 0)
    AND_6.Add(CharacterPartHealth(character, npc_part_id=60) <= 0)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_3)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=AND_4)
    GotoIfLastConditionResultTrue(Label.L5, input_condition=AND_5)
    GotoIfLastConditionResultTrue(Label.L6, input_condition=AND_6)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16472)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=16485):
        ForceAnimation(character, 20000, wait_for_completion=True)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16473)
    SetDisplayMask(character, bit_index=11, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=16485):
        ForceAnimation(character, 20001, wait_for_completion=True)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16474)
    SetDisplayMask(character, bit_index=12, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=16485):
        ForceAnimation(character, 20002, wait_for_completion=True)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    AddSpecialEffect(character, 16497)
    AddSpecialEffect(character, 16484)
    AddSpecialEffect(character, 16475)
    SetDisplayMask(character, bit_index=13, switch_type=OnOffChange.On)
    WaitFrames(frames=2)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=16485):
        ForceAnimation(character, 20003, wait_for_completion=True)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Wait(1.0)
    Restart()


@RestartOnRest(90005481)
def CommonFunc_90005481(_, character: uint):
    """CommonFunc 90005481"""
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=9999)
    SetNPCPartEffects(
        character,
        npc_part_id=0,
        material_sfx_id=110,
        material_vfx_id=110,
        unk_16_20=-1,
        unk_20_24=-1,
        unk_24_28=-1,
    )
    AND_1.Add(CharacterHasSpecialEffect(character, 16499))
    AND_1.Add(NPCPartAttackedWithDamageType(character=character, npc_part_id=10))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 20007)
    Wait(1.0)
    Restart()


@RestartOnRest(90005485)
def CommonFunc_90005485(_, character: uint):
    """CommonFunc 90005485"""
    DisableNetworkSync()
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetBackreadStateAlternate(character, True)
    SetCharacterEnableDistance(character=character, distance=2000.0)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=200.0))
    
    MAIN.Await(OR_1)
    
    EnableGravity(character)
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=220.0))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(90005490)
def CommonFunc_90005490(
    _,
    character: Character | int,
    character_1: Character | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    region: Region | int,
    left: uint,
):
    """CommonFunc 90005490"""
    DisableGravity(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    SetCharacterDisableOnCollisionUnload(character=character, state=False)
    SetCharacterEnableDistance(character=character, distance=2000.0)
    Move(character, destination=asset, destination_type=CoordEntityType.Asset, dummy_id=100, short_move=True)
    EndOfAnimation(asset=asset, animation_id=0)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_15.Add(AND_15)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_1.Add(OR_15)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_10.Add(CharacterDead(character_1))
    AND_1.Add(not AND_10)
    OR_1.Add(AND_1)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(character, 16601)
    if UnsignedNotEqual(left=left, right=0):
        AICommand(character, command_id=20, command_slot=0)
    else:
        AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    ForceAnimation(asset, 0, wait_for_completion=True, skip_transition=True)
    EnableAssetActivation(asset_1, obj_act_id=-1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryFiveFrames)
    Restart()


@RestartOnRest(90005491)
def CommonFunc_90005491(_, character: uint, asset: uint, region: Region | int):
    """CommonFunc 90005491"""
    AND_1.Add(CharacterAlive(character, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=asset, radius=2.0))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ActivateAsset(asset, obj_act_id=-1, relative_index=-1)
    Wait(0.5)
    Restart()


@ContinueOnRest(90005500)
def CommonFunc_90005500(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    asset: uint,
    asset_1: uint,
    obj_act_id: uint,
    asset_2: uint,
    obj_act_id_1: uint,
    region: Region | int,
    region_1: Region | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    left_1: Flag | int,
):
    """CommonFunc 90005500"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableAssetActivation(asset_2, obj_act_id=-1)
        DisableAssetActivation(asset_1, obj_act_id=-1)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(FlagDisabled(flag))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableAssetActivation(asset_2, obj_act_id=-1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(asset_2, 3, skip_transition=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_10.Add(AllPlayersOutsideRegion(region=region_1))
    OR_10.Add(FlagEnabled(flag))
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L3, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, wait_for_completion=True, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableAssetActivation(asset_1, obj_act_id=-1)
        DisableAssetActivation(asset_2, obj_act_id=-1)
    OR_5.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagEnabled(flag))
    AND_7.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(AND_7)
    
    MAIN.Await(OR_8)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableAssetActivation(asset_1, obj_act_id=-1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(asset_1, 3, skip_transition=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    OR_11.Add(AllPlayersOutsideRegion(region=region))
    OR_11.Add(FlagDisabled(flag))
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    AND_2.Add(OR_11)
    
    MAIN.Await(AND_2)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L6, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, wait_for_completion=True, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@RestartOnRest(90005501)
def CommonFunc_90005501(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    asset: uint,
    asset_1: Asset | int,
    asset_2: Asset | int,
    flag_2: Flag | int,
):
    """CommonFunc 90005501"""
    if PlayerInOwnWorld():
        DisableFlag(flag_2)
    
    MAIN.Await(AssetBackreadEnabled(asset=asset))
    
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 20)
    Goto(Label.L10)
    ForceAnimation(asset, 1000020)
    Goto(Label.L10)
    ForceAnimation(asset, 2000020)
    Goto(Label.L10)
    ForceAnimation(asset, 3000020)
    Goto(Label.L10)
    ForceAnimation(asset, 4000020)
    Goto(Label.L10)
    ForceAnimation(asset, 5000020)
    Goto(Label.L10)
    ForceAnimation(asset, 6000020)
    Goto(Label.L10)
    ForceAnimation(asset, 7000020)
    Goto(Label.L10)
    ForceAnimation(asset, 8000020)
    Goto(Label.L10)
    ForceAnimation(asset, 9000020)
    Goto(Label.L10)
    ForceAnimation(asset, 10000020)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 10, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000010, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    DisableAssetActivation(asset_2, obj_act_id=-1)
    End()


@RestartOnRest(90005502)
def CommonFunc_90005502(_, flag: Flag | int, asset: uint, region: Region | int):
    """CommonFunc 90005502"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    WaitFrames(frames=2)
    DisableAssetActivation(asset, obj_act_id=-1)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    AND_13.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_13.Add(OR_15)
    OR_1.Add(AND_13)
    OR_2.Add(ActionButtonParamActivated(action_button_id=8301, entity=asset))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_1)
    if FlagEnabled(flag):
        return
    DisplayDialog(text=4000, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)
    Restart()


@RestartOnRest(90015502)
def CommonFunc_90015502(_, flag: Flag | int, asset: uint, region: Region | int):
    """CommonFunc 90015502"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    WaitFrames(frames=2)
    DisableAssetActivation(asset, obj_act_id=-1)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    AND_13.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_13.Add(OR_15)
    AND_13.Add(HealthValue(PLAYER) != 0)
    OR_1.Add(AND_13)
    OR_2.Add(ActionButtonParamActivated(action_button_id=8301, entity=asset))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_1)
    if FlagEnabled(flag):
        return
    DisplayDialog(text=4000, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)
    Restart()


@ContinueOnRest(90005503)
def CommonFunc_90005503(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    asset: uint,
    asset__region: uint,
    region: Region | int,
    region_1: Region | int,
    region_2: Region | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    left_1: Flag | int,
):
    """CommonFunc 90005503"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    OR_1.Add(FlagDisabled(flag))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=asset__region))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_2.Add(FlagEnabled(left_1))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    OR_4.Add(OR_1)
    OR_4.Add(AND_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_10.Add(AllPlayersOutsideRegion(region=region_1))
    AND_10.Add(AllPlayersOutsideRegion(region=region))
    OR_10.Add(AND_10)
    OR_10.Add(FlagEnabled(flag))
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L3, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, wait_for_completion=True, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(FlagEnabled(flag))
    AND_6.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_6.Add(FlagEnabled(left_1))
    AND_7.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    OR_8.Add(OR_5)
    OR_8.Add(AND_6)
    OR_8.Add(AND_7)
    
    MAIN.Await(OR_8)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableAssetActivation(asset__region, obj_act_id=-1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(asset__region, 3, skip_transition=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_11.Add(AllPlayersOutsideRegion(region=asset__region))
    AND_11.Add(AllPlayersOutsideRegion(region=region_2))
    OR_11.Add(AND_11)
    OR_11.Add(FlagDisabled(flag))
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    AND_2.Add(OR_11)
    
    MAIN.Await(AND_2)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L6, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@ContinueOnRest(90005504)
def CommonFunc_90005504(_, flag: Flag | int, flag_1: Flag | int, left: uint, entity: uint, flag_2: Flag | int):
    """CommonFunc 90005504"""
    if PlayerInOwnWorld():
        DisableFlag(flag_2)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 20)
    Goto(Label.L10)
    ForceAnimation(entity, 1000020)
    Goto(Label.L10)
    ForceAnimation(entity, 2000020)
    Goto(Label.L10)
    ForceAnimation(entity, 3000020)
    Goto(Label.L10)
    ForceAnimation(entity, 4000020)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 10, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 1000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 2000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 3000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 4000010, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    End()


@ContinueOnRest(90005505)
def CommonFunc_90005505(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    asset: uint,
    asset_1: uint,
    obj_act_id: uint,
    asset_2: uint,
    obj_act_id_1: uint,
    flag_2: Flag | int,
    flag_3: Flag | int,
    left_1: Flag | int,
):
    """CommonFunc 90005505"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    if PlayerInOwnWorld():
        EnableAssetActivation(asset_2, obj_act_id=-1)
        DisableAssetActivation(asset_1, obj_act_id=-1)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    AND_3.Add(ActionButtonParamActivated(action_button_id=8320, entity=asset))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if PlayerInOwnWorld():
        DisableAssetActivation(asset_2, obj_act_id=-1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_2)
        DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_3)
    GotoIfLastConditionResultTrue(Label.L2, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(PLAYER, destination=asset, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60200)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(asset_2, 3, skip_transition=True)
    DisableNetworkFlag(flag_3)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L4)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableAssetActivation(asset_1, obj_act_id=-1)
        DisableAssetActivation(asset_2, obj_act_id=-1)
    OR_5.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    AND_7.Add(ActionButtonParamActivated(action_button_id=8320, entity=asset))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(AND_7)
    
    MAIN.Await(OR_8)
    
    if PlayerInOwnWorld():
        DisableAssetActivation(asset_1, obj_act_id=-1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L5, input_condition=AND_7)
    GotoIfLastConditionResultTrue(Label.L6, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L6, flag=flag_3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(PLAYER, destination=asset, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60200)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(asset_1, 3, skip_transition=True)
    DisableNetworkFlag(flag_3)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    
    MAIN.Await(AND_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L8)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 8 --- #
    DefineLabel(8)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, wait_for_completion=True, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@ContinueOnRest(90005507)
def CommonFunc_90005507(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    asset: uint,
    entity: uint,
    region: Region | int,
    entity_1: uint,
    region_1: Region | int,
    region_2: Region | int,
    region_3: Region | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    left_1: Flag | int,
):
    """CommonFunc 90005507"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(FlagDisabled(flag))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    ForceAnimation(entity_1, 1, skip_transition=True)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_3)
    ForceAnimation(entity_1, 1, skip_transition=True)
    Wait(0.5)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)

    # --- Label 11 --- #
    DefineLabel(11)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_10.Add(AllPlayersOutsideRegion(region=region_3))
    OR_10.Add(FlagEnabled(flag))
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 3, skip_transition=True)
    GotoIfMapDoesNotHaveUpdatePermission(Label.L3, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, wait_for_completion=True, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_6.Add(FlagEnabled(flag))
    AND_7.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(AND_7)
    
    MAIN.Await(OR_8)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    ForceAnimation(entity, 1, skip_transition=True)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_3)
    ForceAnimation(entity, 1, skip_transition=True)
    Wait(0.5)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    OR_11.Add(AllPlayersOutsideRegion(region=region_2))
    OR_11.Add(FlagDisabled(flag))
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    AND_2.Add(OR_11)
    
    MAIN.Await(AND_2)
    
    ForceAnimation(entity_1, 3, skip_transition=True)
    GotoIfMapDoesNotHaveUpdatePermission(Label.L6, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, wait_for_completion=True, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@RestartOnRest(90005508)
def CommonFunc_90005508(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: uint,
    entity: uint,
    asset: Asset | int,
    asset_1: Asset | int,
    flag_2: Flag | int,
):
    """CommonFunc 90005508"""
    if PlayerInOwnWorld():
        DisableFlag(flag_2)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 20)
    Goto(Label.L10)
    ForceAnimation(entity, 1000020)
    Goto(Label.L10)
    ForceAnimation(entity, 2000020)
    Goto(Label.L10)
    ForceAnimation(entity, 3000020)
    Goto(Label.L10)
    ForceAnimation(entity, 4000020)
    Goto(Label.L10)
    ForceAnimation(entity, 5000020)
    Goto(Label.L10)
    ForceAnimation(entity, 6000020)
    Goto(Label.L10)
    ForceAnimation(entity, 7000020)
    Goto(Label.L10)
    ForceAnimation(entity, 8000020)
    Goto(Label.L10)
    ForceAnimation(entity, 9000020)
    Goto(Label.L10)
    ForceAnimation(entity, 10000020)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    EndOfAnimation(asset=asset, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(entity, 10, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 1000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 2000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 3000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 4000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 5000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 6000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 7000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 8000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 9000010, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(entity, 10000010, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    DisableFlag(flag_1)
    EndOfAnimation(asset=asset_1, animation_id=1)
    End()


@ContinueOnRest(90005510)
def CommonFunc_90005510(
    _,
    flag: Flag | int,
    asset: uint,
    obj_act_id: uint,
    obj_act_id_1: int,
    text: EventText | int,
    left: uint,
):
    """CommonFunc 90005510"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    WaitRealFrames(frames=1)
    DisplayDialog(text=text, anchor_entity=asset)
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=1):
        DisableAssetActivation(asset, obj_act_id=obj_act_id_1)
    End()


@ContinueOnRest(90005511)
def CommonFunc_90005511(_, flag: Flag | int, asset: Asset | int, obj_act_id: uint, obj_act_id_1: int, left: uint):
    """CommonFunc 90005511"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    
    MAIN.Await(AssetActivated(obj_act_id=obj_act_id))
    
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedEqual(left=left, right=1):
        return
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1, relative_index=0)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1, relative_index=1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1, relative_index=2)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1, relative_index=3)
    End()


@ContinueOnRest(90005512)
def CommonFunc_90005512(_, flag: Flag | int, region: Region | int, region_1: Region | int):
    """CommonFunc 90005512"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return RESTART
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@RestartOnRest(90005513)
def CommonFunc_90005513(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """CommonFunc 90005513"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    ForceAnimation(asset, animation_id)


@ContinueOnRest(90005515)
def CommonFunc_90005515(_, flag: Flag | int, anchor_entity: uint):
    """CommonFunc 90005515"""
    DisableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=7101, entity=anchor_entity))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=4010, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(90005520)
def CommonFunc_90005520(
    _,
    flag: Flag | int,
    asset: uint,
    start_climbing_flag: Flag | int,
    stop_climbing_flag: Flag | int,
):
    """CommonFunc 90005520"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=2)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, asset=asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9200, entity=asset))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    if PlayerInOwnWorld():
        FaceEntityAndForceAnimation(PLAYER, asset, animation=60210)
    ForceAnimation(asset, 1, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, asset=asset)


@RestartOnRest(90005525)
def CommonFunc_90005525(_, flag: Flag | int, asset: uint):
    """CommonFunc 90005525"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=asset, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)


@RestartOnRest(900055278)
def CommonFunc_900055278(
    _,
    flag: uint,
    asset: uint,
    vfx_id: int,
    action_button_id: int,
    text: EventText | int,
    left: int,
    left_1: int,
    left_2: int,
):
    """CommonFunc 900055278"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    AND_2.Add(FlagEnabled(flag))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)
    DisplayDialog(text=text, anchor_entity=flag, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(flag)
    DeleteAssetVFX(asset)
    DisableAsset(asset)
    End()
    if ValueEqual(left=left, right=0):
        return
    if ValueEqual(left=left_1, right=0):
        return
    if ValueEqual(left=left_2, right=0):
        return


@RestartOnRest(90005540)
def CommonFunc_90005540(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """CommonFunc 90005540"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    ForceAnimation(asset, animation_id)


@RestartOnRest(90005550)
def CommonFunc_90005550(_, flag: Flag | int, asset: Asset | int, obj_act_id: uint):
    """CommonFunc 90005550"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=1)
    DisableAssetActivation(asset, obj_act_id=-1)
    EnableTreasure(asset=asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableTreasure(asset=asset)
    
    MAIN.Await(AssetActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(asset=asset)
    EnableFlag(flag)


@RestartOnRest(90005555)
def CommonFunc_90005555(_, flag: Flag | int, item_lot: int, asset: uint):
    """CommonFunc 90005555"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    CreateAssetVFX(asset, dummy_id=100, vfx_id=842050)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209200, entity=asset))
    
    MAIN.Await(AND_1)
    
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 61040)
    Wait(0.5)
    PlaySoundEffect(asset, 420009000, sound_type=SoundType.a_Ambient)
    Wait(1.5)
    DeleteAssetVFX(asset)
    CreateTemporaryVFX(vfx_id=842051, anchor_entity=asset, dummy_id=100, anchor_type=CoordEntityType.Asset)
    Wait(1.5)
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(90005556)
def CommonFunc_90005556(_, asset: Asset | int, flag: Flag | int):
    """CommonFunc 90005556"""
    DisableTreasure(asset=asset)
    DeleteAssetVFX(asset)
    if FlagEnabled(flag):
        return
    
    MAIN.Await(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 59, 59)))
    
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=100, vfx_id=861245)
    EnableTreasure(asset=asset)
    AND_3.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 59, 59)))
    OR_3.Add(not AND_3)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)
    
    Restart()


@RestartOnRest(90005557)
def CommonFunc_90005557(_, entity: uint):
    """CommonFunc 90005557"""
    ForceAnimation(entity, 3)
    
    MAIN.Await(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 59, 59)))
    
    ForceAnimation(entity, 2)
    Wait(6.0)
    ForceAnimation(entity, 0)
    AND_3.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 59, 59)))
    
    MAIN.Await(not AND_3)
    
    ForceAnimation(entity, 1)
    Wait(6.0)
    Restart()


@RestartOnRest(90005560)
def CommonFunc_90005560(_, flag: Flag | int, asset: Asset | int, left: int):
    """CommonFunc 90005560"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    PostDestruction(asset)
    EnableTreasure(asset=asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueEqual(left=left, right=0):
        DeleteAssetVFX(asset)
        CreateAssetVFX(asset, dummy_id=200, vfx_id=803300)
    DisableTreasure(asset=asset)
    AND_1.Add(AssetDestroyed(asset))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    EnableTreasure(asset=asset)
    if ValueEqual(left=left, right=0):
        DeleteAssetVFX(asset)


@ContinueOnRest(90005570)
def CommonFunc_90005570(_, flag: Flag | int, gesture_param_id: int, asset: uint, left: int, left_1: int, right: int):
    """CommonFunc 90005570"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if ValueEqual(left=left_1, right=3):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6103)
        Goto(Label.L1)
    if ValueEqual(left=left_1, right=2):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6102)
        Goto(Label.L1)
    if ValueEqual(left=left_1, right=1):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6101)
        Goto(Label.L1)
    CreateAssetVFX(asset, dummy_id=90, vfx_id=6100)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagDisabled(flag))
    if ValueEqual(left=left, right=2):
        AND_2.Add(ActionButtonParamActivated(action_button_id=4250, entity=asset))
        Goto(Label.L2)
    if ValueEqual(left=left, right=1):
        AND_2.Add(ActionButtonParamActivated(action_button_id=4300, entity=asset))
        Goto(Label.L2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=4200, entity=asset))

    # --- Label 2 --- #
    DefineLabel(2)
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    DeleteAssetVFX(asset)
    if FlagEnabled(flag):
        return
    WaitRealFrames(frames=1)
    AwardGesture(gesture_param_id=gesture_param_id)
    EnableFlag(flag)
    if ValueEqual(left=0, right=right):
        return


@ContinueOnRest(900005571)
def CommonFunc_900005571(_, flag: Flag | int, gesture_param_id: int, flag_1: Flag | int, right: int):
    """CommonFunc 900005571"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AwardGesture(gesture_param_id=gesture_param_id)
    EnableFlag(flag)
    if ValueEqual(left=0, right=right):
        return


@RestartOnRest(900005580)
def CommonFunc_900005580(_, flag: Flag | int, asset: Asset | int, flag_1: Flag | int):
    """CommonFunc 900005580"""
    DisableAsset(asset)
    DisableTreasure(asset=asset)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    EnableAsset(asset)
    EnableTreasure(asset=asset)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableAsset(asset)
    DisableTreasure(asset=asset)


@RestartOnRest(90005600)
def CommonFunc_90005600(_, grace_flag: Flag | int, asset: uint, enemy_block_distance: float, character: uint):
    """CommonFunc 90005600"""
    RegisterGrace(grace_flag=grace_flag, asset=asset, enemy_block_distance=enemy_block_distance)
    if UnsignedNotEqual(left=0, right=character):
        DisableAnimations(character)
    GotoIfFlagEnabled(Label.L0, flag=grace_flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=5.0))
    AND_1.Add(FlagEnabled(grace_flag))
    
    MAIN.Await(AND_1)
    
    if UnsignedEqual(left=0, right=character):
        return
    DisableAnimations(character)
    AddSpecialEffect(character, 530)
    Wait(1.5)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)


@RestartOnRest(90005605)
def CommonFunc_90005605(
    _,
    asset: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
    player_start: PlayerStart | int,
    unk_8_12: int,
    flag: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    left: Flag | int,
    text: EventText | int,
    seconds: float,
    seconds_1: float,
):
    """CommonFunc 90005605"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    if ThisEventSlotFlagDisabled():
        DeleteAssetVFX(asset)
        DisableFlag(flag)
        WaitFrames(frames=1)
    OR_10.Add(Multiplayer())
    OR_10.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_10.Add(FlagDisabled(left))
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806870)
    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    SkipLinesIfUnsignedEqual(3, left=left, right=0)
    SkipLinesIfValueNotEqual(2, left=text, right=0)
    AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    OR_4.Add(Multiplayer())
    OR_4.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_4.Add(FlagDisabled(left))
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    OR_7.Add(Multiplayer())
    OR_7.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_7.Add(FlagDisabled(left))
    AND_7.Add(not OR_7)
    AND_7.Add(FlagDisabled(flag))
    AND_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, left))
    OR_14.Add(AND_1)
    OR_14.Add(AND_4)
    OR_14.Add(AND_7)
    if UnsignedNotEqual(left=left, right=0):
        OR_14.Add(AND_9)
    
    MAIN.Await(OR_14)
    
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_1)
    GotoIfLastConditionResultFalse(Label.L2, input_condition=AND_4)
    DeleteAssetVFX(asset)
    DisableFlag(flag)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    OR_13.Add(UnsignedEqual(left=left, right=0))
    OR_13.Add(ValueEqual(left=text, right=0))
    GotoIfConditionTrue(Label.L4, input_condition=OR_13)
    GotoIfFlagEnabled(Label.L4, flag=left)
    DisplayDialog(text=text, anchor_entity=asset, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    AwaitDialogResponse(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    OR_15.Add(Multiplayer())
    OR_15.Add(MultiplayerPending())
    if OR_15:
        return RESTART
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unk_8_12=unk_8_12)
    Restart()
    Wait(seconds)
    Wait(seconds_1)


@ContinueOnRest(900005610)
def CommonFunc_900005610(_, asset: Asset | int, dummy_id: int, vfx_id: int, right: Flag | int):
    """CommonFunc 900005610"""
    DisableNetworkSync()
    DeleteAssetVFX(asset)
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    AND_1.Add(CharacterMounted(character=PLAYER))
    
    MAIN.Await(AND_1)
    
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=vfx_id)
    if UnsignedNotEqual(left=0, right=right):
        OR_2.Add(FlagDisabled(right))
    OR_2.Add(CharacterNotMounted(character=PLAYER))
    
    MAIN.Await(OR_2)
    
    Restart()


@ContinueOnRest(90005615)
def CommonFunc_90005615(_, region: Region | int, left: Flag | int):
    """CommonFunc 90005615"""
    DisableNetworkSync()
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ALL_PLAYERS, 9621)
    Wait(0.10000000149011612)
    if UnsignedNotEqual(left=left, right=0):
        OR_2.Add(FlagDisabled(left))
    OR_2.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region))
    OR_2.Add(Invasion())
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(ALL_PLAYERS, 9621)
    Restart()


@ContinueOnRest(90005616)
def CommonFunc_90005616(_, flag: Flag | int, region: Region | int):
    """CommonFunc 90005616"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(400239))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DisplayFlashingMessage(20600)


@ContinueOnRest(90005620)
def CommonFunc_90005620(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    asset_2: Asset | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    right: int,
):
    """CommonFunc 90005620"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806040)
    if UnsignedNotEqual(left=asset_2, right=0):
        CreateAssetVFX(asset, dummy_id=201, vfx_id=806040)
    DisableAsset(asset_1)
    if UnsignedNotEqual(left=asset_2, right=0):
        DisableAsset(asset_2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9220, entity=asset))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L9, flag=flag)
    AwaitDialogResponse(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=1.75,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(0.5)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8000, flag=9580, bit_count=8)
    GotoIfUnsignedNotEqual(Label.L2, left=asset_2, right=0)
    AND_2.Add(EventValue(flag=9580, bit_count=8) >= 1)
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(EventValue(flag=9580, bit_count=8) >= 2)
    GotoIfConditionTrue(Label.L4, input_condition=AND_3)
    ForceAnimation(PLAYER, 50050)
    Wait(1.399999976158142)
    AND_4.Add(EventValue(flag=9580, bit_count=8) >= 1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_4)
    DisplayDialog(text=308000, anchor_entity=asset)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisplayDialog(text=408000, anchor_entity=asset)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    Move(PLAYER, destination=asset, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(2.700000047683716)
    DisplayDialog(text=208000, anchor_entity=asset)
    EnableAsset(asset_1)
    RemoveGoodFromPlayer(item=8000, quantity=1)
    EnableNetworkFlag(flag)
    Goto(Label.L8)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(PLAYER, destination=asset, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(2.6700000762939453)
    EnableAsset(asset_1)
    ForceAnimation(PLAYER, 60811)
    Wait(1.5)
    DisplayDialog(text=208000, anchor_entity=asset)
    EnableAsset(asset_2)
    RemoveGoodFromPlayer(item=8000, quantity=2)
    EnableNetworkFlag(flag)
    Goto(Label.L8)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableAsset(asset_1)
    EnableAsset(asset_2)

    # --- Label 8 --- #
    DefineLabel(8)
    DeleteAssetVFX(asset)
    End()
    if ValueEqual(left=0, right=right):
        return


@ContinueOnRest(90005621)
def CommonFunc_90005621(_, flag: Flag | int, asset: uint):
    """CommonFunc 90005621"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=806042)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@RestartOnRest(90005630)
def CommonFunc_90005630(_, far_view_id: uint, asset: uint, dummy_id: int):
    """CommonFunc 90005630"""
    DisableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9270, entity=asset))
    
    MAIN.Await(AND_1)
    
    UseFarViewCamera(far_view_id=far_view_id, asset=asset, dummy_id=dummy_id)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=60480)
    Wait(1.0)
    Restart()


@RestartOnRest(90005631)
def CommonFunc_90005631(_, anchor_entity: uint, text: EventText | int):
    """CommonFunc 90005631"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9330, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    Wait(2.0)
    Restart()


@RestartOnRest(90005632)
def CommonFunc_90005632(_, flag: Flag | int, asset: uint, item_lot: int):
    """CommonFunc 90005632"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    DeleteAssetVFX(asset, erase_root=False)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806840)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=asset))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(90005633)
def CommonFunc_90005633(
    _,
    character: uint,
    flag: Flag | int,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    asset: uint,
    asset_1: Asset | int,
):
    """CommonFunc 90005633"""
    AddSpecialEffect(character, 10124)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset_1)
    if FlagEnabled(character):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=15.0))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    RemoveSpecialEffect(character, 10124)
    ForceAnimation(character_1, animation_id)
    EnableAsset(asset)
    EnableAsset(asset_1)
    ForceAnimation(asset, 2)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character_1, animation_id_1)
    ForceAnimation(asset, 1)
    Wait(3.799999952316284)
    DisableCharacter(character_1)
    DisableAsset(asset)
    EnableTreasure(asset=asset_1)


@RestartOnRest(90005636)
def CommonFunc_90005636(
    _,
    flag: Flag | int,
    character: uint,
    entity: uint,
    special_effect: int,
    destination: uint,
    region: Region | int,
    flag_1: Flag | int,
    patrol_information_id: uint,
    right: int,
):
    """CommonFunc 90005636"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    OR_5.Add(AND_2)
    AND_3.Add(FlagEnabled(flag_1))
    AND_3.Add(CharacterInsideRegion(character=character, region=region))
    OR_5.Add(AND_3)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    if FlagEnabled(flag_1):
        AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=30.0))
    AND_4.Add(ActionButtonParamActivated(action_button_id=9300, entity=entity))
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    CreateTemporaryVFX(vfx_id=643041, anchor_entity=character, dummy_id=905, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=643040, anchor_entity=character, dummy_id=960, anchor_type=CoordEntityType.Character)
    Wait(0.20000000298023224)
    DisableCharacter(character)
    DisableAI(character)
    GotoIfLastConditionResultFalse(Label.L2, input_condition=AND_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
    Wait(0.10000000149011612)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfLastConditionResultFalse(Label.L3, input_condition=AND_4)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(flag_1):
        EnableNetworkFlag(flag_1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
    if UnsignedNotEqual(left=0, right=patrol_information_id):
        ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    WaitFrames(frames=1)
    EnableCharacter(character)
    DisableAnimations(character)
    ForceAnimation(character, 20028)
    Wait(0.5)
    EnableAI(character)
    AddSpecialEffect(character, special_effect)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()
    if ValueEqual(left=0, right=right):
        return


@RestartOnRest(90005637)
def CommonFunc_90005637(_, flag: Flag | int, character: Character | int, region: Region | int):
    """CommonFunc 90005637"""
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 4463)
    Wait(3.0)
    Restart()


@RestartOnRest(90005638)
def CommonFunc_90005638(_, flag: Flag | int, asset: Asset | int, asset_1: Asset | int):
    """CommonFunc 90005638"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    DisableAsset(asset_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetInvulnerability(asset)
    EnableAssetInvulnerability(asset_1)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=100, vfx_id=841075)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset_1, dummy_id=100, vfx_id=841076)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetDamaged(asset, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset, request_slot=0)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, dummy_id=100, vfx_id=841072)
    CreateAssetVFX(asset_1, dummy_id=100, vfx_id=841072)
    DisableAssetInvulnerability(asset_1)
    WaitRealFrames(frames=1)
    DestroyAsset(asset_1, request_slot=0)
    EnableFlag(flag)
    Wait(2.0)
    DisplayDialog(text=2020030, display_distance=100.0, number_buttons=NumberButtons.OneButton)


@RestartOnRest(90005639)
def CommonFunc_90005639(
    _,
    flag: Flag | int,
    asset: Asset | int,
    asset_1: Asset | int,
    asset_2: Asset | int,
    seconds: float,
):
    """CommonFunc 90005639"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    EnableAssetInvulnerability(asset_1)
    EnableTreasure(asset=asset_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset_2)
    DisableTreasure(asset=asset_2)
    EnableAssetInvulnerability(asset_1)
    EnableAssetInvulnerability(asset)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetDamaged(asset, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset, request_slot=0)
    Wait(seconds)
    EnableAsset(asset_2)
    EnableTreasure(asset=asset_2)
    EnableFlag(flag)


@RestartOnRest(90005640)
def CommonFunc_90005640(_, flag: Flag | int, asset: uint):
    """CommonFunc 90005640"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    
    MAIN.Await(AssetBackreadEnabled(asset=asset))
    
    EndOfAnimation(asset=asset, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=50.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ForceAnimation(asset, 1)


@RestartOnRest(90005645)
def CommonFunc_90005645(
    _,
    flag: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    asset: uint,
    player_start: PlayerStart | int,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
):
    """CommonFunc 90005645"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableAsset(asset)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(asset)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9290, entity=asset))
    
    MAIN.Await(AND_2)
    
    AwaitDialogResponse(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@ContinueOnRest(90005646)
def CommonFunc_90005646(
    _,
    flag: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    asset: uint,
    player_start: PlayerStart | int,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
):
    """CommonFunc 90005646"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        CreateAssetVFX(asset, dummy_id=190, vfx_id=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9290, entity=asset))
    
    MAIN.Await(AND_2)
    
    AwaitDialogResponse(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@ContinueOnRest(90005650)
def CommonFunc_90005650(_, flag: Flag | int, asset: uint, asset_1: uint, obj_act_id: uint, obj_act_id_1: int):
    """CommonFunc 90005650"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    if PlayerInOwnWorld():
        DisplayDialog(text=4200, anchor_entity=asset_1, display_distance=5.0)
    else:
        DisplayFlashingMessage(4200)
    ForceAnimation(asset, 1)
    End()


@ContinueOnRest(90005652)
def CommonFunc_90005652(_, flag: Flag | int, asset: uint, flag_1: Flag | int):
    """CommonFunc 90005652"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisplayDialog(text=4200, display_distance=5.0)
    ForceAnimation(asset, 1)
    End()


@ContinueOnRest(90005651)
def CommonFunc_90005651(_, flag: Flag | int, anchor_entity: uint):
    """CommonFunc 90005651"""
    DisableNetworkSync()
    OR_1.Add(ActionButtonParamActivated(action_button_id=7200, entity=anchor_entity))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=4001, anchor_entity=anchor_entity)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(90005660)
def CommonFunc_90005660(
    _,
    owner_entity: uint,
    entity: uint,
    region: Region | int,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """CommonFunc 90005660"""
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@ContinueOnRest(90005670)
def CommonFunc_90005670(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    entity: uint,
    region: Region | int,
    region_1: Region | int,
    right: Flag | int,
):
    """CommonFunc 90005670"""
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_9)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagDisabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag)
    ForceAnimation(entity, 12, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_10.Add(AllPlayersOutsideRegion(region=region_1))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    if UnsignedNotEqual(left=0, right=right):
        GotoIfFlagDisabled(Label.L10, flag=right)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag_1)
    EnableFlag(flag_2)
    ForceAnimation(entity, 20, wait_for_completion=True)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    Wait(0.10000000149011612)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_1)
    ForceAnimation(entity, 21, wait_for_completion=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag)
        ForceAnimation(entity, 10)
    else:
        ForceAnimation(entity, 10, wait_for_completion=True)
    Restart()


@ContinueOnRest(90005673)
def CommonFunc_90005673(_, flag: Flag | int, region: Region | int):
    """CommonFunc 90005673"""
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_1.Add(OR_9)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag)
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_10.Add(OR_10)
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(AND_10)
    OR_2.Add(AllPlayersOutsideRegion(region=region))
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_10)
    Wait(1.0)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag)
    Restart()


@ContinueOnRest(90005671)
def CommonFunc_90005671(
    _,
    flag: Flag | int,
    asset__asset_flag: uint,
    asset_flag__region: uint,
    dummy_id: int,
    behavior_param_id: int,
):
    """CommonFunc 90005671"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=asset_flag__region))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4195))
    
    MAIN.Await(AND_1)
    
    MoveAssetToCharacter(asset__asset_flag, character=PLAYER, dummy_id=93)
    WaitFrames(frames=1)
    CreateHazard(
        asset_flag=asset_flag__region,
        asset=asset__asset_flag,
        dummy_id=dummy_id,
        behavior_param_id=behavior_param_id,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    Wait(0.5)
    Restart()


@ContinueOnRest(90005672)
def CommonFunc_90005672(_, flag: Flag | int, region: Region | int):
    """CommonFunc 90005672"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@ContinueOnRest(90005675)
def CommonFunc_90005675(
    _,
    flag: Flag | int,
    asset_flag: Flag | int,
    asset: uint,
    region: Region | int,
    behaviour_id: int,
    seconds: float,
    right: int,
):
    """CommonFunc 90005675"""
    AND_10.Add(MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)))
    AND_10.Add(FlagEnabled(flag))
    GotoIfConditionFalse(Label.L10, input_condition=AND_10)
    DisableNetworkFlag(flag)
    DisableThisSlotFlag()

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag)
    if ThisEventSlotFlagDisabled():
        Wait(seconds)
    if ValueNotEqual(left=1, right=right):
        ForceAnimation(asset, 1)
    else:
        ForceAnimation(asset, 2)
    if ValueNotEqual(left=behaviour_id, right=0):
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            dummy_id_start=30,
            dummy_id_end=31,
            behaviour_id=behaviour_id,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    else:
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            dummy_id_start=30,
            dummy_id_end=31,
            behaviour_id=103000,
            target_type=DamageTargetType.Character,
            radius=0.10000000149011612,
            life=1.0,
            repetition_time=0.0,
        )
    Wait(1.0)
    RemoveAssetFlag(asset_flag=asset_flag)
    Wait(4.099999904632568)
    Wait(0.10000000149011612)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005680)
def CommonFunc_90005680(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int, asset: uint):
    """CommonFunc 90005680"""
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableFlag(flag_3)
    
    MAIN.Await(AssetBackreadEnabled(asset=asset))
    
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(asset, 20)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(asset, 10)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()


@ContinueOnRest(90005681)
def CommonFunc_90005681(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    attacked_entity: uint,
):
    """CommonFunc 90005681"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    OR_1.Add(FlagDisabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_2.Add(AND_2)
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    
    MAIN.Await(OR_4)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag)
        EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(FlagEnabled(flag))
    AND_6.Add(FlagDisabled(flag_1))
    AND_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_6.Add(AND_6)
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    
    MAIN.Await(OR_8)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(flag)
        EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(flag_3)
    EnableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_3))
    
    Restart()


@ContinueOnRest(90005682)
def CommonFunc_90005682(
    _,
    flag: Flag | int,
    source_entity: uint,
    region: Region | int,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    dummy_id: int,
    dummy_id_1: int,
    dummy_id_2: int,
    dummy_id_3: int,
):
    """CommonFunc 90005682"""
    AND_1.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=dummy_id_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=dummy_id_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101100,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=101102,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@ContinueOnRest(90005683)
def CommonFunc_90005683(_, flag: Flag | int, asset: uint, dummy_id: int, flag_1: Flag | int, flag_2: Flag | int):
    """CommonFunc 90005683"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteAssetVFX(asset)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=9260, entity=asset))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=4210, anchor_entity=asset)
    EnableFlag(flag_1)
    EnableFlag(flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfUnsignedEqual(Label.L10, left=1049551600, right=asset)
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=800530)
    Goto(Label.L1)

    # --- Label 10 --- #
    DefineLabel(10)
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=800531)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=800530)


@ContinueOnRest(90005684)
def CommonFunc_90005684(_, anchor_entity: uint):
    """CommonFunc 90005684"""
    DisableNetworkSync()
    AND_1.Add(ActionButtonParamActivated(action_button_id=9260, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=4210, anchor_entity=anchor_entity)
    Wait(1.0)
    Restart()


@ContinueOnRest(90005685)
def CommonFunc_90005685(_, character: Character | int):
    """CommonFunc 90005685"""
    EnableImmortality(character)
    DisableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(90005686)
def CommonFunc_90005686(_, source_entity: uint, flag: Flag | int):
    """CommonFunc 90005686"""
    MAIN.Await(FlagEnabled(flag))
    
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        dummy_id=10,
        behavior_id=244600980,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        dummy_id=15,
        behavior_id=244600980,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        dummy_id=20,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        dummy_id=25,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=source_entity,
        source_entity=source_entity,
        dummy_id=30,
        behavior_id=244600981,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(90005687)
def CommonFunc_90005687(_, character: Character | int, patrol_information_id: uint, region: Region | int):
    """CommonFunc 90005687"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    WaitFrames(frames=1)


@ContinueOnRest(90005688)
def CommonFunc_90005688(
    _,
    character: Character | int,
    region: Region | int,
    patrol_information_id: uint,
    region_1: Region | int,
    patrol_information_id_1: uint,
    region_2: Region | int,
    patrol_information_id_2: uint,
):
    """CommonFunc 90005688"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    if UnsignedNotEqual(left=0, right=region_2):
        GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_2)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(30090400, patrol_information_id=patrol_information_id_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    Restart()


@RestartOnRest(90005690)
def CommonFunc_90005690(_, region: Region | int):
    """CommonFunc 90005690"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4080)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    RemoveSpecialEffect(PLAYER, 4080)
    Restart()


@RestartOnRest(90005691)
def CommonFunc_90005691(_, region: Region | int):
    """CommonFunc 90005691"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    RemoveSpecialEffect(PLAYER, 4085)
    Restart()


@RestartOnRest(90005694)
def CommonFunc_90005694(
    _,
    asset_flag: Flag | int,
    asset: Asset | int,
    dummy_id_start: int,
    dummy_id_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """CommonFunc 90005694"""
    RemoveAssetFlag(asset_flag=asset_flag)
    if ValueEqual(left=0, right=dummy_id_end):
        CreateHazard(
            asset_flag=asset_flag,
            asset=asset,
            dummy_id=dummy_id_start,
            behavior_param_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )
    else:
        CreateBigHazardousAsset(
            asset_flag=asset_flag,
            asset=asset,
            dummy_id_start=dummy_id_start,
            dummy_id_end=dummy_id_end,
            behaviour_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )


@RestartOnRest(90005695)
def CommonFunc_90005695(
    _,
    asset__asset_flag: uint,
    asset: Asset | int,
    dummy_id_start: int,
    dummy_id_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """CommonFunc 90005695"""
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    if AssetDestroyed(asset):
        return
    if ValueEqual(left=0, right=dummy_id_end):
        CreateHazard(
            asset_flag=asset__asset_flag,
            asset=asset,
            dummy_id=dummy_id_start,
            behavior_param_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )
    else:
        CreateBigHazardousAsset(
            asset_flag=asset__asset_flag,
            asset=asset,
            dummy_id_start=dummy_id_start,
            dummy_id_end=dummy_id_end,
            behaviour_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )
    
    MAIN.Await(AssetDestroyed(asset__asset_flag))
    
    RemoveAssetFlag(asset_flag=asset__asset_flag)


@RestartOnRest(90005700)
def CommonFunc_90005700(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    value: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    right: int,
):
    """CommonFunc 90005700"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagDisabled(3000))
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(HealthRatio(character) > 0.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=TORRENT))
    OR_1.Add(CharacterHasSpecialEffect(character, 1650000))
    AND_2.Add(OR_1)
    AND_2.Add(HealthRatio(character) < value)
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, 9641))
    OR_2.Add(FlagEnabled(flag_2))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()


@RestartOnRest(90005701)
def CommonFunc_90005701(
    _,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: int,
):
    """CommonFunc 90005701"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagDisabled(3000))
    
    WaitFrames(frames=1)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=9, right=right)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=8, right=right)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=7, right=right)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=6, right=right)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=5, right=right)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=4, right=right)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=3, right=right)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=2, right=right)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=1, right=right)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_3)
    
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_4.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_4.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_4)
    
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_5.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_5.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_5)
    
    WaitFrames(frames=1)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_6)
    
    WaitFrames(frames=1)

    # --- Label 4 --- #
    DefineLabel(4)
    OR_7.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_7.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_7)
    
    WaitFrames(frames=1)

    # --- Label 5 --- #
    DefineLabel(5)
    OR_8.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_8.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_8)
    
    WaitFrames(frames=1)

    # --- Label 6 --- #
    DefineLabel(6)
    OR_9.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_9.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_9)
    
    WaitFrames(frames=1)

    # --- Label 7 --- #
    DefineLabel(7)
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_10)
    
    WaitFrames(frames=1)

    # --- Label 8 --- #
    DefineLabel(8)
    OR_11.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_11.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    
    MAIN.Await(OR_11)
    
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(90005702)
def CommonFunc_90005702(_, character: Character | int, flag: Flag | int, first_flag: Flag | int, last_flag: Flag | int):
    """CommonFunc 90005702"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()


@RestartOnRest(90005703)
def CommonFunc_90005703(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    right: int,
):
    """CommonFunc 90005703"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    GotoIfFlagEnabled(Label.L0, flag=first_flag)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=445):
        AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(FlagEnabled(first_flag))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 9629)
    AddSpecialEffect(character, 9634)
    AddSpecialEffect(character, 9642)
    AddSpecialEffect(character, 9647)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=445):
        AddSpecialEffect(character, 440)
    AddSpecialEffect(character, 9645)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=TORRENT))
    OR_1.Add(CharacterHasSpecialEffect(character, 1650000))
    AND_4.Add(HealthRatio(character) >= 1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    AND_2.Add(HealthRatio(character) < 0.6499999761581421)
    Goto(Label.L10)
    AND_5.Add(HealthRatio(character) >= 0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    AND_2.Add(HealthRatio(character) < 0.550000011920929)
    Goto(Label.L10)
    AND_6.Add(HealthRatio(character) >= 0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    AND_2.Add(HealthRatio(character) < 0.44999998807907104)
    Goto(Label.L10)
    AND_7.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    AND_2.Add(HealthRatio(character) < 0.3499999940395355)
    Goto(Label.L10)
    AND_8.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    AND_2.Add(HealthRatio(character) < 0.25)
    Goto(Label.L10)
    AND_2.Add(HealthRatio(character) < 0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_2.Add(OR_1)
    OR_5.Add(FlagEnabled(flag))
    OR_5.Add(FlagEnabled(flag_1))
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(CharacterHasSpecialEffect(character, 9641))
    OR_2.Add(OR_5)
    OR_2.Add(AND_2)
    AND_3.Add(HealthRatio(character) > 0.0)
    AND_3.Add(OR_2)
    OR_3.Add(FlagEnabled(flag_3))
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if LastResult(OR_3):
        return RESTART
    SetTeamType(character, TeamType.HostileNPC)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=445):
        AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)
    GotoIfLastConditionResultTrue(Label.L9, input_condition=OR_5)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    Restart()


@RestartOnRest(90005704)
def CommonFunc_90005704(
    _,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: int,
):
    """CommonFunc 90005704"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=4, right=right)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=3, right=right)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=2, right=right)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=1, right=right)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagDisabled(flag_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    if LastResult(OR_1):
        return RESTART
    WaitFrames(frames=1)

    # --- Label 4 --- #
    DefineLabel(4)
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(FlagDisabled(flag_1))
    OR_4.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_4.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    if LastResult(OR_3):
        return RESTART
    WaitFrames(frames=1)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_5.Add(FlagEnabled(flag))
    OR_5.Add(FlagDisabled(flag_1))
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)
    
    if LastResult(OR_5):
        return RESTART
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_7.Add(FlagEnabled(flag))
    OR_7.Add(FlagDisabled(flag_1))
    OR_8.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_8.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_8.Add(OR_7)
    
    MAIN.Await(OR_8)
    
    if LastResult(OR_7):
        return RESTART
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_9.Add(FlagEnabled(flag))
    OR_9.Add(FlagDisabled(flag_1))
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_10.Add(OR_9)
    
    MAIN.Await(OR_10)
    
    if LastResult(OR_9):
        return RESTART
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(90005705)
def CommonFunc_90005705(_, character: uint):
    """CommonFunc 90005705"""
    WaitFrames(frames=1)
    EnableCharacter(character)
    EnableBackread(character)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    ForceAnimation(character, 20022)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(90005706)
def CommonFunc_90005706(_, character: uint, animation_id: int, left: uint):
    """CommonFunc 90005706"""
    EnableBackread(character)
    EnableCharacter(character)
    DisableGravity(character)
    ForceAnimation(character, animation_id)
    if UnsignedEqual(left=left, right=0):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 9624))
    AwaitConditionTrue(AND_1)
    Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(character)
    End()


@RestartOnRest(90005707)
def CommonFunc_90005707(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    right: int,
    animation_id: int,
    left: Flag | int,
    flag_4: Flag | int,
):
    """CommonFunc 90005707"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(FlagEnabled(first_flag))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 9642)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=TORRENT))
    OR_1.Add(CharacterHasSpecialEffect(character, 1650000))
    AND_4.Add(HealthRatio(character) >= 1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    AND_2.Add(HealthRatio(character) < 0.6499999761581421)
    Goto(Label.L10)
    AND_5.Add(HealthRatio(character) >= 0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    AND_2.Add(HealthRatio(character) < 0.550000011920929)
    Goto(Label.L10)
    AND_6.Add(HealthRatio(character) >= 0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    AND_2.Add(HealthRatio(character) < 0.44999998807907104)
    Goto(Label.L10)
    AND_7.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    AND_2.Add(HealthRatio(character) < 0.3499999940395355)
    Goto(Label.L10)
    AND_8.Add(HealthRatio(character) >= 0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    AND_2.Add(HealthRatio(character) < 0.25)
    Goto(Label.L10)
    AND_2.Add(HealthRatio(character) < 0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_2.Add(OR_1)
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(CharacterHasSpecialEffect(character, 9641))
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(flag_1))
    OR_2.Add(AND_2)
    AND_3.Add(HealthRatio(character) > 0.0)
    AND_3.Add(OR_2)
    OR_3.Add(FlagEnabled(flag_3))
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    if LastResult(OR_3):
        return RESTART
    GotoIfLastConditionResultTrue(Label.L9, input_condition=OR_5)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    if UnsignedNotEqual(left=left, right=0):
        WaitRealFrames(frames=2)
    
        MAIN.Await(FlagDisabled(left))
    ForceAnimation(character, animation_id)
    EnableFlag(flag_4)
    Restart()


@RestartOnRest(90005708)
def CommonFunc_90005708(_, character: Character | int, flag: Flag | int, left: uint):
    """CommonFunc 90005708"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    WaitRealFrames(frames=1)
    if FlagDisabled(flag):
        return RESTART
    if UnsignedEqual(left=left, right=0):
        ResetCharacterPosition(character=character)
    else:
        Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(90005709)
def CommonFunc_90005709(_, attacked_entity: uint, dummy_id: int, vfx_id: int):
    """CommonFunc 90005709"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity))
    
    CreateTemporaryVFX(
        vfx_id=vfx_id,
        anchor_entity=attacked_entity,
        dummy_id=dummy_id,
        anchor_type=CoordEntityType.Character,
    )
    Restart()


@RestartOnRest(90005710)
def CommonFunc_90005710(_, flag: Flag | int, asset: Asset | int, dummy_id: int, vfx_id: int):
    """CommonFunc 90005710"""
    MAIN.Await(FlagDisabled(flag))
    
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=vfx_id)
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(2.0)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(90005711)
def CommonFunc_90005711(_, flag: Flag | int, patrol_information_id: uint):
    """CommonFunc 90005711"""
    GotoIfPlayerInOwnWorld(Label.L0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateAuthority(ALL_PLAYERS, authority_level=UpdateAuthority.Forced)
    
    MAIN.Await(FlagEnabled(flag))
    
    ChangePatrolBehavior(ALL_SPIRIT_SUMMONS, patrol_information_id=patrol_information_id)
    Restart()


@RestartOnRest(90005712)
def CommonFunc_90005712(_, character: Character | int, asset: Asset | int, dummy_id: int, vfx_id: int):
    """CommonFunc 90005712"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=vfx_id)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9502))
    
    DeleteAssetVFX(asset)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9503))
    
    Restart()


@RestartOnRest(90005713)
def CommonFunc_90005713(_, flag: Flag | int, character: Character | int, character_1: Character | int):
    """CommonFunc 90005713"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 9500))
    OR_1.Add(AND_1)
    AND_2.Add(PlayerNotInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character_1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterHasSpecialEffect(ALL_PLAYERS, 202))
    OR_3.Add(AND_3)
    AND_4.Add(PlayerNotInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    if PlayerInOwnWorld():
        DisableNetworkFlag(flag)
    Restart()


@RestartOnRest(90005715)
def CommonFunc_90005715(
    _,
    character: Character | int,
    character_1: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    distance: float,
):
    """CommonFunc 90005715"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=character, distance=17.0)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=17.0)
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(90005716)
def CommonFunc_90005716(_, character: Character | int, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005716"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterDead(character))
    
    SetBackreadStateAlternate(character, True)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(TimeElapsed(seconds=30.0))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(90005720)
def CommonFunc_90005720(_, character: uint, character_1: uint, special_effect: int, dummy_id: int):
    """CommonFunc 90005720"""
    if CharacterHasSpecialEffect(character=character, special_effect=11020):
        return
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, 10960))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    AddSpecialEffect(character_1, 8551)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 20000)
    End()


@RestartOnRest(90005721)
def CommonFunc_90005721(_, character: Character | int, character_1: Character | int):
    """CommonFunc 90005721"""
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=0.5, max_seconds=1.5)
    Kill(character_1, award_runes=True)
    End()


@RestartOnRest(90005722)
def CommonFunc_90005722(_, character: Character | int, character_1: Character | int):
    """CommonFunc 90005722"""
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=11020)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(HealthRatio(character) < 0.6499999761581421)
    OR_1.Add(HealthRatio(character_1, target_comparison_type=ComparisonType.GreaterThanOrEqual) < 0.6499999761581421)
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 11012)
    AddSpecialEffect(character, 11020)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()


@RestartOnRest(90005723)
def CommonFunc_90005723(_, character: Character | int):
    """CommonFunc 90005723"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 11001))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 11020))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 11000)
    OR_1.Add(CharacterHasSpecialEffect(character, 11001))
    OR_1.Add(CharacterHasSpecialEffect(character, 11020))
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 11000)
    Restart()


@RestartOnRest(90005724)
def CommonFunc_90005724(
    _,
    flag: Flag | int,
    character: uint,
    item_lot: int,
    seconds: float,
    left: int,
    character_1: uint,
):
    """CommonFunc 90005724"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    if ValueNotEqual(left=left, right=0):
        DisableCharacter(character)
        DisableAnimations(character)
        DropMandatoryTreasure(character)
        End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(seconds)
    EnableFlag(flag)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=left, right=1):
        return
    AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(90005725)
def CommonFunc_90005725(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    character: uint,
    character_1: Character | int,
    asset: Asset | int,
):
    """CommonFunc 90005725"""
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagEnabled(flag_3))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(flag_3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(asset)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=11035):
        ForceAnimation(character, 930003)
    if CharacterHasSpecialEffect(character=character, special_effect=11035):
        ForceAnimation(character, 930002)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(90005726)
def CommonFunc_90005726(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    character: uint,
    asset: Asset | int,
):
    """CommonFunc 90005726"""
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagEnabled(flag_3))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(flag_3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930003)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(90005727)
def CommonFunc_90005727(
    _,
    flag: Flag | int,
    character: Character | int,
    character_1: Character | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
):
    """CommonFunc 90005727"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(last_flag):
        return
    AddSpecialEffect(character, 9629)
    AddSpecialEffect(character, 9634)
    AddSpecialEffect(character, 9642)
    AddSpecialEffect(character, 440)
    AddSpecialEffect(character, 9645)
    AddSpecialEffect(character_1, 9629)
    AddSpecialEffect(character_1, 9634)
    AddSpecialEffect(character_1, 9642)
    AddSpecialEffect(character_1, 440)
    AddSpecialEffect(character_1, 9645)
    OR_1.Add(FlagEnabled(flag))
    OR_15.Add(OR_1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    AND_1.Add(HealthValue(character) < 1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=ALL_PLAYERS))
    AND_2.Add(HealthValue(character_1) < 1)
    OR_15.Add(AND_1)
    OR_15.Add(AND_2)
    
    MAIN.Await(OR_15)
    
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    AddSpecialEffect(character, 9628)
    AddSpecialEffect(character, 9635)
    AddSpecialEffect(character, 9643)
    AddSpecialEffect(character, 442)
    AddSpecialEffect(character, 9644)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableAI(character_1)
    AddSpecialEffect(character_1, 9628)
    AddSpecialEffect(character_1, 9635)
    AddSpecialEffect(character_1, 9643)
    AddSpecialEffect(character_1, 442)
    AddSpecialEffect(character_1, 9644)
    if FlagDisabled(last_flag):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        EnableNetworkFlag(flag)
    End()


@RestartOnRest(90005728)
def CommonFunc_90005728(_, attacked_entity: Character | int, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005728"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(90005729)
def CommonFunc_90005729(_, flag: Flag | int, character: Character | int, distance: float, flag_1: Flag | int):
    """CommonFunc 90005729"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    SetCharacterTalkRange(character=character, distance=distance)
    AwaitFlagEnabled(flag=flag_1)
    Wait(30.0)
    DisableNetworkFlag(flag_1)
    Restart()


@RestartOnRest(90005730)
def CommonFunc_90005730(
    _,
    flag: Flag | int,
    seconds: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """CommonFunc 90005730"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(FlagDisabled(flag_4))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagDisabled(flag_2))
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag_4))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    if LastResult(OR_2):
        return RESTART
    EnableFlag(flag)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_4.Add(FlagEnabled(flag))
    OR_4.Add(FlagDisabled(flag_2))
    OR_4.Add(FlagEnabled(flag_3))
    OR_4.Add(FlagEnabled(flag_4))
    OR_4.Add(FlagDisabled(flag_1))
    OR_3.Add(TimeElapsed(seconds=seconds))
    OR_3.Add(OR_4)
    
    MAIN.Await(OR_3)
    
    if LastResult(OR_4):
        return RESTART
    EnableFlag(flag)
    Restart()


@RestartOnRest(90005731)
def CommonFunc_90005731(_, flag: Flag | int, other_entity: uint, radius: float, radius_1: float):
    """CommonFunc 90005731"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=radius_1))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(90005732)
def CommonFunc_90005732(_, flag: Flag | int, region: Region | int, region_1: Region | int):
    """CommonFunc 90005732"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    EnableFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(90005733)
def CommonFunc_90005733(_, flag: Flag | int):
    """CommonFunc 90005733"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    SendPlayerCharacterDataToOnlinePlayers(pool_type=0)
    Restart()


@RestartOnRest(90005734)
def CommonFunc_90005734(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    region: Region | int,
    region_1: Region | int,
    flag_2: Flag | int,
    right: int,
):
    """CommonFunc 90005734"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    EnableFlag(flag_2)
    WaitFrames(frames=1)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=-1, right=right):
        DisableFlag(flag_2)
    Restart()


@RestartOnRest(90005735)
def CommonFunc_90005735(_, character: uint, flag: Flag | int, flag_1: Flag | int, entity: uint, radius: float):
    """CommonFunc 90005735"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    SetBackreadStateAlternate(character, False)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=character, radius=radius))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, True)
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(EntityWithinDistance(entity=entity, other_entity=character, radius=radius))
    
    MAIN.Await(not AND_2)
    
    SetBackreadStateAlternate(character, False)
    Restart()


@RestartOnRest(90005736)
def CommonFunc_90005736(
    _,
    character: uint,
    asset: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    radius: float,
    distance: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    right: int,
    animation_id: int,
    right_1: int,
    asset_1: Asset | int,
):
    """CommonFunc 90005736"""
    SkipLinesIfValueEqual(2, left=1, right=right)
    SkipLinesIfValueEqual(1, left=0, right=right_1)
    DisableAsset(asset_1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    if FlagEnabled(flag):
        return
    SkipLinesIfValueEqual(3, left=1, right=right)
    SkipLinesIfValueEqual(2, left=0, right=right_1)
    EnableAsset(asset_1)
    CreateAssetVFX(asset_1, dummy_id=100, vfx_id=600904)
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=ALL_PLAYERS))
    AND_1.Add(OR_2)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    AND_2.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=asset, radius=radius))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_2)
    DisableGravity(character)
    DisableAnimations(character)
    DisableCharacterCollision(character)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagEnabled(flag=flag_1)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=1, right=right)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=0, right=right)

    # --- Label 1 --- #
    DefineLabel(1)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    ForceAnimation(character, animation_id)
    EnableCharacter(character)
    EnableGravity(character)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(asset, 1)
    Wait(1.0)
    if ValueNotEqual(left=0, right=right_1):
        DeleteAssetVFX(asset_1)
    ForceAnimation(character, animation_id)
    EnableCharacter(character)
    CreateTemporaryVFX(vfx_id=302603, anchor_entity=character, dummy_id=220, anchor_type=CoordEntityType.Character)
    Wait(1.0)
    DisableAsset(asset)
    EnableGravity(character)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    SetCharacterTalkRange(character=character, distance=distance)
    End()


@RestartOnRest(90005737)
def CommonFunc_90005737(_, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005737"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(Invasion())
    OR_1.Add(InvasionPending())
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(Invasion())
    OR_2.Add(InvasionPending())
    
    MAIN.Await(not OR_2)
    
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005740)
def CommonFunc_90005740(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
):
    """CommonFunc 90005740"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    else:
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005741)
def CommonFunc_90005741(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    animation_id: int,
    special_effect: int,
    seconds: float,
):
    """CommonFunc 90005741"""
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    if ValueNotEqual(left=special_effect, right=-1):
        ForceAnimation(character, animation__animation_id)
    else:
        ForceAnimation(character, animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    else:
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_1.Add(FlagDisabled(flag))
    if ValueNotEqual(left=special_effect, right=-1):
        AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    DisableFlag(flag_1)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005742)
def CommonFunc_90005742(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    flag_2: Flag | int,
):
    """CommonFunc 90005742"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    else:
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    AND_15.Add(FlagEnabled(flag_2))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    OR_3.Add(AND_15)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_15)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005743)
def CommonFunc_90005743(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    animation_id: int,
    special_effect: int,
    seconds: float,
    flag_2: Flag | int,
):
    """CommonFunc 90005743"""
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    if ValueNotEqual(left=special_effect, right=-1):
        ForceAnimation(character, animation__animation_id)
    else:
        ForceAnimation(character, animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    else:
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id, wait_for_completion=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_1.Add(FlagDisabled(flag))
    if ValueNotEqual(left=special_effect, right=-1):
        AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_15.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_15)
    
    MAIN.Await(OR_1)
    
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_15)
    DisableFlag(flag_1)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005744)
def CommonFunc_90005744(_, entity: uint, flag: Flag | int, flag_1: Flag | int, animation_id: int):
    """CommonFunc 90005744"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, animation_id)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag):
        return RESTART
    if FlagEnabled(flag_1):
        return


@RestartOnRest(90005745)
def CommonFunc_90005745(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, seconds: float):
    """CommonFunc 90005745"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L10, flag=flag_1)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    Wait(seconds)
    DisableFlag(flag_2)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()


@RestartOnRest(90005746)
def CommonFunc_90005746(_, character: uint, flag: Flag | int, distance: float):
    """CommonFunc 90005746"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(character))
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(flag)


@RestartOnRest(90005747)
def CommonFunc_90005747(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds_1: float,
):
    """CommonFunc 90005747"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    GotoIfFlagEnabled(Label.L1, flag=flag_4)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(TimeElapsed(seconds=seconds))
    OR_5.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_5)
    
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_6.Add(TimeElapsed(seconds=seconds_1))
    OR_6.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_6)
    
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(90005748)
def CommonFunc_90005748(
    _,
    entity: uint,
    action_button_id: int,
    text: EventText | int,
    display_distance: float,
    flag: Flag | int,
):
    """CommonFunc 90005748"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    DisplayDialog(text=text, display_distance=display_distance, button_type=ButtonType.Yes_or_No)
    EnableFlag(flag)
    Wait(1.0)
    Restart()


@RestartOnRest(90005749)
def CommonFunc_90005749(_, character: Character | int, character_1: uint, flag: Flag | int, flag_1: Flag | int):
    """CommonFunc 90005749"""
    WaitRealFrames(frames=2)
    GotoIfFlagDisabled(Label.L20, flag=flag)
    EnableInvincibility(character_1)
    EnableImmortality(character)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=100.0))
    
    Move(character, destination=character_1, destination_type=CoordEntityType.Character, dummy_id=11, short_move=True)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(character_1, 9910)
    DisableCharacter(character)
    DisableAnimations(character_1)
    CreateTemporaryVFX(vfx_id=604220, anchor_entity=character_1, dummy_id=200, anchor_type=CoordEntityType.Character)
    EnableNetworkFlag(flag_1)
    Wait(5.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 19 --- #
    DefineLabel(19)
    AND_10.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_10)
    
    DisableCharacter(character)
    DisableAnimations(character_1)
    Wait(5.0)
    DisableCharacter(character_1)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    Restart()


@ContinueOnRest(90005750)
def CommonFunc_90005750(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    vfx_id: int,
):
    """CommonFunc 90005750"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=vfx_id, right=0):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    else:
        CreateAssetVFX(asset, dummy_id=90, vfx_id=6101)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(90005751)
def CommonFunc_90005751(_, attacked_entity: uint, dummy_id: int, vfx_id: int):
    """CommonFunc 90005751"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(
        vfx_id=vfx_id,
        anchor_entity=attacked_entity,
        dummy_id=dummy_id,
        anchor_type=CoordEntityType.Asset,
    )
    Restart()


@ContinueOnRest(90005752)
def CommonFunc_90005752(_, asset: uint, dummy_id: int, vfx_id: int, seconds: float):
    """CommonFunc 90005752"""
    DisableNetworkSync()
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=ALL_PLAYERS))
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(AND_2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if LastResult(AND_2):
        return RESTART
    DeleteAssetVFX(asset)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(AttackedWithDamageType(attacked_entity=asset, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_3)
    
    CreateAssetVFX(asset, dummy_id=dummy_id, vfx_id=vfx_id)
    Restart()


@RestartOnRest(90005753)
def CommonFunc_90005753(
    _,
    entity: uint,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """CommonFunc 90005753"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    AwaitFlagEnabled(flag=flag)
    GotoIfFlagDisabled(Label.L0, flag=flag_5)
    GotoIfFlagEnabled(Label.L1, flag=flag_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=ALL_PLAYERS, radius=10.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_5)
    GotoIfFlagEnabled(Label.L13, flag=flag_2)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(TimeElapsed(seconds=seconds))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L11, input_condition=AND_2)
    Goto(Label.L12)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(flag_1)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    Goto(Label.L20)

    # --- Label 11 --- #
    DefineLabel(11)
    SkipLinesIfFlagEnabled(6, flag_6)
    AND_3.Add(EntityWithinDistance(entity=entity, other_entity=ALL_PLAYERS, radius=10.0))
    SkipLinesIfConditionFalse(4, AND_3)
    EnableFlag(flag_1)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    DisableFlag(flag_3)
    EnableFlag(flag_6)
    Goto(Label.L20)

    # --- Label 12 --- #
    DefineLabel(12)
    EnableFlag(flag_4)
    DisableFlag(flag_5)
    Goto(Label.L20)

    # --- Label 13 --- #
    DefineLabel(13)
    EnableFlag(flag_1)
    DisableFlag(flag_4)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    DisableFlag(flag_3)
    EnableFlag(flag_6)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(90005754)
def CommonFunc_90005754(
    _,
    flag: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
    region: Region | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    right: Flag | int,
    character: Character | int,
    right_1: Flag | int,
    distance: float,
    flag_4: Flag | int,
    right_2: Flag | int,
    flag_5: Flag | int,
    right_3: Flag | int,
):
    """CommonFunc 90005754"""
    if PlayerNotInOwnWorld():
        return
    DisableBackread(character)
    WaitFrames(frames=1)
    if FlagEnabled(flag_3):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfUnsignedEqual(Label.L1, left=0, right=right_2)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    OR_2.Add(FlagEnabled(right_1))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    OR_3.Add(FlagEnabled(flag))
    AND_3.Add(OR_3)
    OR_4.Add(FlagDisabled(right_2))
    AND_4.Add(FlagEnabled(right_2))
    AND_4.Add(FlagEnabled(flag_5))
    OR_4.Add(AND_4)
    AND_3.Add(OR_4)
    OR_5.Add(FlagEnabled(right_1))
    OR_5.Add(AND_3)
    
    MAIN.Await(OR_5)
    
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(2, left=0, right=right_1)
    SkipLinesIfFlagDisabled(1, right_1)
    DisableFlagRange((first_flag, last_flag))
    if UnsignedNotEqual(left=0, right=right):
        if FlagEnabled(right):
            return
    EnableFlag(flag)
    if UnsignedNotEqual(left=0, right=right_3):
        EnableFlag(right_3)
    EnableBackread(character)
    SetCharacterTalkRange(character=character, distance=distance)
    OR_10.Add(FlagEnabled(flag_4))
    OR_10.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_10)
    
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    if FlagEnabled(flag_4):
        return
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    EnableFlag(flag_1)
    End()


@RestartOnRest(90005755)
def CommonFunc_90005755(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    right: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    max_value__value: uint,
):
    """CommonFunc 90005755"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    MAIN.Await(FlagEnabled(flag_1))
    
    if UnsignedNotEqual(left=0, right=right):
        DisableFlag(right)
    IncrementEventValue(flag_3, bit_count=4, max_value=max_value__value)
    AND_1.Add(EventValue(flag=flag_3, bit_count=4) == max_value__value)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(90005756)
def CommonFunc_90005756(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """CommonFunc 90005756"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag_2))
    
    if FlagDisabled(flag_1):
        return
    EnableFlag(flag)
    End()


@RestartOnRest(90005757)
def CommonFunc_90005757(
    _,
    character: uint,
    character_1: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """CommonFunc 90005757"""
    WaitRealFrames(frames=1)
    EnableFlag(flag_2)
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_2)
    
    WaitRealFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_3))
    if OR_1:
        return
    if FlagDisabled(flag_1):
        EnableCharacter(character)
        ForceAnimation(character, 30007)
        DisableCharacter(character_1)
        End()
    DisableCharacter(character)
    EnableCharacter(character_1)
    ForceAnimation(character_1, 30008)
    SetTeamType(character_1, TeamType.NoTeam)
    DisableAnimations(character_1)


@RestartOnRest(90005758)
def CommonFunc_90005758(_, flag: Flag | int, flag_1: Flag | int, animation_id: int, entity: uint, flag_2: Flag | int):
    """CommonFunc 90005758"""
    WaitFrames(frames=2)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, animation_id, loop=True)


@ContinueOnRest(90005759)
def CommonFunc_90005759(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    flag_3: Flag | int,
    flag_4: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    seconds: float,
    flag_8: Flag | int,
    radius: float,
):
    """CommonFunc 90005759"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    GotoIfFlagEnabled(Label.L10, flag=flag_8)
    GotoIfFlagDisabled(Label.L0, flag=flag_8)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_3):
        return
    OR_1.Add(CharacterProportionDead(character=character))
    OR_1.Add(HealthValue(character) <= 0)
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_3)
    OR_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 1)
    SkipLinesIfConditionFalse(1, OR_2)
    EnableFlag(flag_5)
    OR_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 2)
    SkipLinesIfConditionFalse(6, OR_3)
    EnableFlag(flag_6)
    if FlagEnabled(flag_7):
        return
    EnableFlag(flag_8)
    Wait(seconds)
    EnableFlag(flag_4)
    AND_5.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_5)
    
    DisableFlag(flag_8)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    if FlagEnabled(flag_7):
        return
    EnableFlag(flag_4)
    AND_5.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_5)
    
    DisableFlag(flag_8)
    End()


@RestartOnRest(90005760)
def CommonFunc_90005760(_, flag: Flag | int, character: uint, region: Region | int, flag_1: Flag | int):
    """CommonFunc 90005760"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 20000)
    End()


@RestartOnRest(90005761)
def CommonFunc_90005761(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    animation_id: int,
    distance: float,
):
    """CommonFunc 90005761"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_5)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    
    MAIN.Await(FlagEnabled(flag_4))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id, loop=True)
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(flag_4))
    
    Restart()


@RestartOnRest(90005762)
def CommonFunc_90005762(
    _,
    character: uint,
    asset: Asset | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    distance: float,
):
    """CommonFunc 90005762"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_6)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    
    MAIN.Await(FlagEnabled(flag_4))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L5, flag=flag_5)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableAsset(asset)
    DisableAnimations(character)
    SetCharacterTalkRange(character=character, distance=distance)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableAsset(asset)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAsset(asset)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    DisableAsset(asset)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_4))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(90005763)
def CommonFunc_90005763(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    asset: Asset | int,
    animation_id: int,
):
    """CommonFunc 90005763"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_1.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.NoTeam)
    SetCharacterTalkRange(character=character, distance=distance)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id, loop=True)
    EnableAsset(asset)
    MoveAssetToCharacter(asset, character=character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_2))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(90005764)
def CommonFunc_90005764(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    animation_id: int,
    distance: float,
    destination: uint,
    asset: Asset | int,
):
    """CommonFunc 90005764"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_5)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableGravity(character)
    DisableAssetInvulnerability(asset)
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    
    MAIN.Await(FlagEnabled(flag_4))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableInvincibility(character)
    EnableAssetInvulnerability(asset)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, animation_id)
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(flag_4))
    
    Restart()


@RestartOnRest(90005765)
def CommonFunc_90005765(
    _,
    character: uint,
    flag: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    animation_id: int,
    distance: float,
    flag_4: Flag | int,
    seconds: float,
):
    """CommonFunc 90005765"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(flag):
        DisableFlag(flag_3)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=first_flag)
    GotoIfFlagEnabled(Label.L3, flag=last_flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableImmortality(character)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id, loop=True)
    SetCharacterTalkRange(character=character, distance=distance)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)

    # --- Label 4 --- #
    DefineLabel(4)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_1.Add(FlagDisabled(flag_2))
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 1)
    AND_2.Add(FlagEnabled(flag_4))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    if LastResult(AND_1):
        return RESTART
    Wait(seconds)
    DisableFlag(flag_4)
    Restart()


@RestartOnRest(90005766)
def CommonFunc_90005766(
    _,
    flag: Flag | int,
    character: Character | int,
    distance: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """CommonFunc 90005766"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(flag_1)
    EnableFlag(flag_2)


@RestartOnRest(90005767)
def CommonFunc_90005767(
    _,
    flag: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    character: Character | int,
    flag_1: Flag | int,
    character_1: Character | int,
    flag_2: Flag | int,
):
    """CommonFunc 90005767"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    if FlagEnabled(last_flag):
        return
    OR_1.Add(CharacterProportionDead(character=character))
    OR_1.Add(CharacterProportionDead(character=character_1))
    
    MAIN.Await(OR_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(last_flag)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(4895)
    AND_2.Add(CharacterProportionDead(character=character_1))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag_2)
    SaveRequest()


@RestartOnRest(90005768)
def CommonFunc_90005768(
    _,
    flag: Flag | int,
    item_lot: int,
    flag_1: Flag | int,
    item_lot_1: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """CommonFunc 90005768"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    if AND_1:
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    AND_3.Add(EventValue(flag=flag_3, bit_count=4) == 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        AwardItemLot(item_lot, host_only=True)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    if PlayerInOwnWorld():
        AwardItemLot(item_lot_1, host_only=True)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    End()


@RestartOnRest(90005769)
def CommonFunc_90005769(
    _,
    character: Character | int,
    flag: Flag | int,
    character_1: Character | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """CommonFunc 90005769"""
    WaitFrames(frames=1)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag_4))
    if OR_1:
        return
    AND_10.Add(FlagEnabled(flag))
    OR_11.Add(HealthValue(character) <= 0)
    OR_11.Add(CharacterDead(character))
    AND_10.Add(OR_11)
    OR_10.Add(FlagEnabled(flag_1))
    OR_10.Add(HealthValue(character_1) <= 0)
    OR_10.Add(CharacterDead(character_1))
    AND_10.Add(OR_10)
    
    MAIN.Await(AND_10)
    
    EnableFlag(flag_2)


@RestartOnRest(90005770)
def CommonFunc_90005770(_, flag: Flag | int):
    """CommonFunc 90005770"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableNetworkFlag(flag)


@RestartOnRest(90005771)
def CommonFunc_90005771(_, other_entity: uint, flag: Flag | int):
    """CommonFunc 90005771"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    EnableFlag(flag)
    
    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    Restart()


@RestartOnRest(90005772)
def CommonFunc_90005772(_, character: Character | int):
    """CommonFunc 90005772"""
    DisableBackread(character)
    DisableCharacter(character)


@ContinueOnRest(90005773)
def CommonFunc_90005773(_, flag: Flag | int):
    """CommonFunc 90005773"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    SaveRequest()
    Restart()


@ContinueOnRest(90005774)
def CommonFunc_90005774(_, flag: Flag | int, item_lot: int, flag_1: Flag | int):
    """CommonFunc 90005774"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(flag))
    AwaitConditionTrue(AND_2)
    if PlayerInOwnWorld():
        AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(90005775)
def CommonFunc_90005775(_, world_map_point_param_id: int, flag: Flag | int, distance: float):
    """CommonFunc 90005775"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    OpenWorldMapPoint(world_map_point_param_id=world_map_point_param_id, distance=distance)


@RestartOnRest(90005776)
def CommonFunc_90005776(_, flag: Flag | int, flag_1: Flag | int, item_lot: int):
    """CommonFunc 90005776"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(FlagEnabled(flag_1))
    AwaitConditionTrue(AND_2)
    AwardItemLot(item_lot, host_only=False)
    End()


@RestartOnRest(90005777)
def CommonFunc_90005777(_, character: Character | int, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """CommonFunc 90005777"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    SkipLinesIfConditionFalse(1, OR_1)
    End()
    if FlagEnabled(flag_2):
        return
    EnableCharacter(character)
    AND_2.Add(HealthValue(character) >= 1)
    AND_2.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(90005778)
def CommonFunc_90005778(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, attacked_entity: Character | int):
    """CommonFunc 90005778"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    EnableFlag(flag)
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    DisableFlag(flag)
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=TORRENT))
    OR_6.Add(FlagEnabled(flag_1))
    OR_6.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_6)
    
    EnableFlag(flag)


@RestartOnRest(90005779)
def CommonFunc_90005779(
    _,
    character: uint,
    flag: Flag | int,
    animation_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """CommonFunc 90005779"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9617))
    
    AND_1.Add(HealthValue(character) >= 1)
    if not AND_1:
        return
    ForceAnimation(character, animation_id, wait_for_completion=True)


@ContinueOnRest(90005780)
def CommonFunc_90005780(
    _,
    flag: Flag | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
    character: uint,
    sign_type: int,
    region: Region | int,
    right: Flag | int,
    unknown: uchar,
    right_1: int,
):
    """CommonFunc 90005780"""
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    EraseNPCSummonSign(character=character)
    if FlagEnabled(flag):
        return
    if FlagEnabled(dismissal_flag):
        return
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=sign_type,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )
    if ValueEqual(left=0, right=right_1):
        return


@ContinueOnRest(90005781)
def CommonFunc_90005781(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, character: uint):
    """CommonFunc 90005781"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableBackread(character)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    SetBackreadStateAlternate(character, True)
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, False)


@ContinueOnRest(90005782)
def CommonFunc_90005782(
    _,
    flag: Flag | int,
    region: uint,
    character: Character | int,
    target_entity: uint,
    region_1: Region | int,
    animation: int,
):
    """CommonFunc 90005782"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(region))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region_1))
    
    if ValueNotEqual(left=animation, right=0):
        FaceEntityAndForceAnimation(character, target_entity, animation=animation, wait_for_completion=True)
    else:
        FaceEntityAndForceAnimation(character, target_entity, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_5)
    
    if LastResult(OR_4):
        return RESTART
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(90005784)
def CommonFunc_90005784(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    character: Character | int,
    region: uint,
    region_1: Region | int,
    animation: int,
):
    """CommonFunc 90005784"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region_1))
    
    if ValueNotEqual(left=animation, right=0):
        FaceEntityAndForceAnimation(character, region, animation=animation, wait_for_completion=True)
    else:
        FaceEntityAndForceAnimation(character, region, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_5)
    
    if LastResult(OR_4):
        return RESTART
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(90005783)
def CommonFunc_90005783(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    other_entity: uint,
    region: Region | int,
    left: int,
):
    """CommonFunc 90005783"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=75.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)
    
    MAIN.Await(OR_10)
    
    AND_11.Add(FlagEnabled(flag))
    AND_11.Add(FlagEnabled(flag_2))
    if AND_11:
        return
    SendNPCSummonHome(character=character)
    End()


@RestartOnRest(90005785)
def CommonFunc_90005785(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    other_entity: uint,
    region: Region | int,
    radius: float,
):
    """CommonFunc 90005785"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag_1))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    
    MAIN.Await(OR_10)
    
    AND_11.Add(FlagEnabled(flag))
    AND_11.Add(FlagEnabled(flag_2))
    if AND_11:
        return
    SendNPCSummonHome(character=character)
    End()


@ContinueOnRest(90005790)
def CommonFunc_90005790(
    _,
    right: Flag | int,
    flag: Flag | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
    character: Character | int,
    sign_type: int,
    region: Region | int,
    region_1: Region | int,
    seconds: float,
    right_1: Flag | int,
    unknown: uchar,
    right_2: int,
):
    """CommonFunc 90005790"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=0, right=right):
        if FlagEnabled(right):
            return
    if FlagEnabled(flag):
        return
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(dismissal_flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(right))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(summon_flag))
    if UnsignedNotEqual(left=0, right=right_1):
        AND_1.Add(FlagEnabled(right_1))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_1.Add(FlagDisabled(9000))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    PlaceSummonSign(
        sign_type=sign_type,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )
    Wait(1.0)
    Restart()
    if ValueEqual(left=0, right=right_2):
        return


@ContinueOnRest(90005791)
def CommonFunc_90005791(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, character: uint):
    """CommonFunc 90005791"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableBackread(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    SetBackreadStateAlternate(character, True)
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, False)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)


@RestartOnRest(90005792)
def CommonFunc_90005792(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    item_lot: int,
    seconds: float,
):
    """CommonFunc 90005792"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterProportionDead(character=character))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    EnableFlag(flag)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    AwardItemLot(item_lot, host_only=True)
    End()
    OR_1.Add(FlagEnabled(flag_2))


@RestartOnRest(90005793)
def CommonFunc_90005793(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    other_entity: uint,
    region: Region | int,
    left: int,
):
    """CommonFunc 90005793"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=110.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)
    
    MAIN.Await(OR_10)
    
    if FlagEnabled(flag):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_2))


@RestartOnRest(90005795)
def CommonFunc_90005795(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    message: EventText | int,
    action_button_id: int,
    asset: uint,
    vfx_id: int,
):
    """CommonFunc 90005795"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteAssetVFX(asset)
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=vfx_id)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    OR_3.Add(OR_2)
    OR_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_3.Add(FlagDisabled(flag_2))
    
    MAIN.Await(OR_3)
    
    if LastResult(OR_2):
        return RESTART
    if FlagDisabled(flag_2):
        return RESTART
    AwaitDialogResponse(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=2.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagDisabled(left_flag):
        return RESTART
    EnableFlag(flag_1)
    AddSpecialEffect(PLAYER, 15)
    Wait(20.0)
    Restart()


@RestartOnRest(90005796)
def CommonFunc_90005796(_, flag: Flag | int, character: Character | int, banner_type: uchar, region: Region | int):
    """CommonFunc 90005796"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(90005797)
def CommonFunc_90005797(
    _,
    flag: Flag | int,
    character: Character | int,
    banner_type: uchar,
    region: Region | int,
    special_effect: int,
):
    """CommonFunc 90005797"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    AddSpecialEffect(ALL_PLAYERS, special_effect)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(90005798)
def CommonFunc_90005798(
    _,
    flag: Flag | int,
    character: Character | int,
    banner_type: uchar,
    region: Region | int,
    flag_1: Flag | int,
):
    """CommonFunc 90005798"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(90005799)
def CommonFunc_90005799(
    _,
    flag: Flag | int,
    character: Character | int,
    banner_type: uchar,
    region: Region | int,
    flag_1: Flag | int,
    character_1: uint,
):
    """CommonFunc 90005799"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    DisableAnimations(character_1)
    DisableGravity(character_1)
    AND_1.Add(CharacterProportionDead(character=character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Kill(character_1)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(9005800)
def CommonFunc_9005800(
    _,
    flag: Flag | int,
    entity: uint,
    region: uint,
    flag_1: Flag | int,
    character: Character | int,
    action_button_id: int,
    left: Flag | int,
    region_1: Region | int,
):
    """CommonFunc 9005800"""
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        FaceEntityAndForceAnimation(PLAYER, region, animation=60060, wait_for_completion=True)
    else:
        FaceEntityAndForceAnimation(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    if LastResult(OR_4):
        return RESTART

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    FaceEntityAndForceAnimation(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(9005801)
def CommonFunc_9005801(
    _,
    flag: Flag | int,
    entity: uint,
    region: uint,
    flag_1: Flag | int,
    flag_2: Flag | int,
    action_button_id: int,
):
    """CommonFunc 9005801"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    MAIN.Await(AND_1)
    
    SuppressSoundForFogGate(duration=5.0)
    FaceEntityAndForceAnimation(PLAYER, region, animation=60060, wait_for_completion=True)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    if LastResult(OR_1):
        return RESTART
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(9005810)
def CommonFunc_9005810(
    _,
    flag: Flag | int,
    grace_flag: Flag | int,
    character: Character | int,
    asset: uint,
    enemy_block_distance: float,
):
    """CommonFunc 9005810"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAsset(asset)
    Wait(1.0)
    
    MAIN.Await(FlagEnabled(flag))
    
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=asset, dummy_id=200, anchor_type=CoordEntityType.Asset)
    Wait(0.5)
    EnableCharacter(character)
    EnableAsset(asset)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(
        grace_flag=grace_flag,
        asset=asset,
        reaction_distance=5.0,
        reaction_angle=180.0,
        enemy_block_distance=enemy_block_distance,
    )


@RestartOnRest(9005811)
def CommonFunc_9005811(_, flag: Flag | int, asset: uint, vfx_id: int, right: Flag | int):
    """CommonFunc 9005811"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_3.Add(FlagEnabled(right))
    AND_3.Add(FlagDisabled(flag))
    OR_4.Add(Invasion())
    OR_4.Add(InvasionPending())
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    AND_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(not AND_7)
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_5.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    OR_8.Add(AND_1)
    OR_8.Add(AND_2)
    OR_8.Add(AND_3)
    OR_8.Add(AND_4)
    OR_8.Add(AND_5)
    
    MAIN.Await(OR_8)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_11.Add(OR_11)
    AND_11.Add(FlagDisabled(flag))
    OR_12.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_12.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_12.Add(OR_12)
    AND_12.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_13.Add(FlagEnabled(right))
    AND_13.Add(FlagDisabled(flag))
    OR_14.Add(Invasion())
    OR_14.Add(InvasionPending())
    AND_14.Add(OR_14)
    AND_14.Add(FlagEnabled(flag))
    OR_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(not OR_7)
    OR_15.Add(Invasion())
    OR_15.Add(InvasionPending())
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag))
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_15.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_9.Add(not AND_11)
    AND_9.Add(not AND_12)
    AND_9.Add(not AND_13)
    AND_9.Add(not AND_14)
    AND_9.Add(not AND_15)
    
    MAIN.Await(AND_9)
    
    Restart()


@RestartOnRest(9005812)
def CommonFunc_9005812(_, flag: Flag | int, asset: Asset | int, vfx_id: int, right: Flag | int, vfx_id_1: int):
    """CommonFunc 9005812"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    AND_1.Add(FlagDisabled(flag))
    OR_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_3.Add(OR_3)
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_4.Add(OR_4)
    OR_5.Add(AND_1)
    OR_5.Add(AND_3)
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    if UnsignedNotEqual(left=0, right=right):
        AND_11.Add(FlagEnabled(right))
    AND_11.Add(FlagDisabled(flag))
    OR_13.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_13.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_13.Add(OR_13)
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_14.Add(OR_14)
    AND_15.Add(not AND_11)
    AND_15.Add(not AND_13)
    AND_15.Add(not AND_14)
    
    MAIN.Await(AND_15)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(Invasion())
    OR_2.Add(InvasionPending())
    OR_3.Add(FlagEnabled(9982))
    OR_5.Add(OR_2)
    OR_5.Add(OR_3)
    
    MAIN.Await(OR_5)
    
    OR_12.Add(Invasion())
    OR_12.Add(InvasionPending())
    OR_13.Add(FlagEnabled(9982))
    AND_15.Add(not OR_12)
    AND_15.Add(not OR_13)
    
    MAIN.Await(AND_15)
    
    Restart()
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id_1)


@RestartOnRest(9005813)
def CommonFunc_9005813(_, flag: Flag | int, asset: Asset | int, vfx_id: int, right: Flag | int, vfx_id_1: int):
    """CommonFunc 9005813"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    AND_1.Add(FlagDisabled(flag))
    OR_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_3.Add(OR_3)
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_4.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_4.Add(OR_4)
    OR_5.Add(AND_1)
    OR_5.Add(AND_3)
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    if UnsignedNotEqual(left=0, right=right):
        AND_11.Add(FlagEnabled(right))
    AND_11.Add(FlagDisabled(flag))
    OR_13.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_13.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_13.Add(OR_13)
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_14.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_14.Add(OR_14)
    AND_15.Add(not AND_11)
    AND_15.Add(not AND_13)
    AND_15.Add(not AND_14)
    
    MAIN.Await(AND_15)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(Invasion())
    OR_2.Add(InvasionPending())
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    OR_5.Add(OR_2)
    
    MAIN.Await(OR_5)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id_1)
    OR_12.Add(Invasion())
    OR_12.Add(InvasionPending())
    OR_12.Add(Multiplayer())
    OR_12.Add(MultiplayerPending())
    AND_15.Add(not OR_12)
    
    MAIN.Await(AND_15)
    
    Restart()


@RestartOnRest(9005822)
def CommonFunc_9005822(
    _,
    flag: Flag | int,
    bgm_boss_conv_param_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: Flag | int,
    flag_3: Flag | int,
    left: int,
    left_1: int,
):
    """CommonFunc 9005822"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)


@RestartOnRest(9005823)
def CommonFunc_9005823(
    _,
    flag: Flag | int,
    bgm_boss_conv_param_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    left: int,
    left_1: int,
):
    """CommonFunc 9005823"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag_4))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L2, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_4)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=1)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_2.Add(FlagEnabled(flag_4))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L2, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    UnknownSound_2010_8(sound_id=90003003)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 2 --- #
    DefineLabel(2)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)


@RestartOnRest(9005824)
def CommonFunc_9005824(
    _,
    flag: Flag | int,
    bgm_boss_conv_param_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    left: int,
    left_1: int,
):
    """CommonFunc 9005824"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag_4))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L2, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_4)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=1)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_2.Add(FlagEnabled(flag_4))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L2, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Unknown)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 2 --- #
    DefineLabel(2)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)


@RestartOnRest(90005830)
def CommonFunc_90005830(_, flag: Flag | int, region: Region | int):
    """CommonFunc 90005830"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return RESTART
    AddSpecialEffect(PLAYER, 4250)
    Wait(3.0)
    Restart()


@RestartOnRest(9005840)
def CommonFunc_9005840(_, flag: Flag | int, left: Flag | int, character: uint):
    """CommonFunc 9005840"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)


@RestartOnRest(9005845)
def CommonFunc_9005845(_, flag: Flag | int, character: uint):
    """CommonFunc 9005845"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    GotoIfFlagEnabled(Label.L1, flag=11000801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=11000800, radius=20.0))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(11000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(11002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=11002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(11005800)
    SetNetworkUpdateRate(11005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(11000800)


@RestartOnRest(90005860)
def CommonFunc_90005860(
    _,
    flag: Flag | int,
    left: Flag | int,
    character: uint,
    left_1: uint,
    item_lot: int,
    seconds: float,
):
    """CommonFunc 90005860"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.GreatEnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.LegendFelled)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds)


@RestartOnRest(90005861)
def CommonFunc_90005861(
    _,
    flag: Flag | int,
    left: Flag | int,
    character: uint,
    left_1: uint,
    item_lot: int,
    text: EventText | int,
    seconds: float,
):
    """CommonFunc 90005861"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.GreatEnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.LegendFelled)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot, host_only=True)
    Wait(2.0)
    DisplayFlashingMessage(text)
    End()
    Wait(seconds)


@ContinueOnRest(90005870)
def CommonFunc_90005870(_, character: Character | int, name: NPCName | int, npc_threat_level: uint):
    """CommonFunc 90005870"""
    DisableNetworkSync()
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_12.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_12.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_12.Add(not AND_12)
    OR_12.Add(CharacterDead(character))
    OR_12.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_12)
    
    OR_13.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9291)
    Restart()


@ContinueOnRest(90005871)
def CommonFunc_90005871(
    _,
    character: Character | int,
    name: NPCName | int,
    npc_threat_level: uint,
    character_1: Character | int,
):
    """CommonFunc 90005871"""
    DisableNetworkSync()
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    AND_1.Add(FlagDisabled(9000))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        SetNetworkUpdateAuthority(character_1, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_2.Add(not AND_2)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        SetNetworkUpdateAuthority(character_1, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
        SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_12.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_12.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    OR_12.Add(not AND_12)
    OR_12.Add(CharacterDead(character))
    OR_12.Add(FlagEnabled(9000))
    
    MAIN.Await(OR_12)
    
    OR_13.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    if FlagDisabled(9000):
        Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
        SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DisableFlag(9291)
    Restart()


@ContinueOnRest(90005872)
def CommonFunc_90005872(_, character: Character | int, npc_threat_level: uint, right: Flag | int):
    """CommonFunc 90005872"""
    DisableNetworkSync()
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    else:
        AND_1.Add(HealthRatio(character) <= 0.550000011920929)
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(AND_1)
    
    EnableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    OR_2.Add(CharacterDead(character))
    OR_2.Add(FieldBattleMusicDisabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(OR_2)
    
    DisableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(90005880)
def CommonFunc_90005880(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    item_lot: int,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
    player_start: PlayerStart | int,
):
    """CommonFunc 90005880"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    DeactivateGparamOverride(change_duration=10.0)
    AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)
    Wait(5.0)
    AddSpecialEffect(ALL_PLAYERS, 8870)
    Wait(2.0)
    EnableFlag(flag_2)
    EnableFlag(9295)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
    End()


@RestartOnRest(90005881)
def CommonFunc_90005881(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    message: EventText | int,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
    player_start: uint,
):
    """CommonFunc 90005881"""
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9230, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    AwaitDialogResponse(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagEnabled(cancel_flag__right_flag):
        return RESTART
    OR_3.Add(Multiplayer())
    OR_3.Add(MultiplayerPending())
    if OR_3:
        return RESTART
    EnableNetworkFlag(flag_1)
    AddSpecialEffect(PLAYER, 514)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450)
    Wait(1.5)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=player_start,
        dummy_id=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=True,
        reset_camera=True,
    )
    EnableFlag(9021)
    End()
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(90005882)
def CommonFunc_90005882(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    flag_3: Flag | int,
    character_1: uint,
    asset: uint,
    owner_entity: uint,
    source_entity: uint,
    name: NPCName | int,
    animation_id: int,
    animation_id_1: int,
):
    """CommonFunc 90005882"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableAsset(asset)
    if FlagDisabled(flag_1):
        return
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    EnableFlag(1099002100)
    EnableFlag(flag_2)
    AddSpecialEffect(PLAYER, 190)
    ActivateGparamOverride(gparam_sub_id=0, change_duration=0.0)
    SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=False)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        dummy_id=100,
        behavior_id=100500,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id)
    else:
        DisableCharacter(character)
        DisableAnimations(character)
    DisableHealthBar(character)
    DisableNetworkFlag(flag_1)
    AddSpecialEffect(PLAYER, 514)
    EnableAsset(asset)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806700)
    ForceAnimation(PLAYER, 60451)
    Wait(1.0)
    AddSpecialEffect(ALL_PLAYERS, 8870)
    OR_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=12.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1099002100)
    if ValueEqual(left=-1, right=animation_id):
        EnableCharacter(character)
        EnableAnimations(character)
    if ValueNotEqual(left=-1, right=animation_id_1):
        ForceAnimation(character, animation_id_1)
    EnableAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(flag_3)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)


@RestartOnRest(90005883)
def CommonFunc_90005883(_, flag: Flag | int, flag_1: Flag | int, entity: uint):
    """CommonFunc 90005883"""
    ForceAnimation(entity, 0, loop=True)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    ForceAnimation(entity, 10, loop=True)
    if FlagEnabled(flag_1):
        return
    AND_1.Add(Singleplayer())
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True)
    AND_11.Add(Singleplayer())
    AND_12.Add(MultiplayerPending())
    AND_11.Add(not AND_12)
    
    MAIN.Await(not AND_11)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005884)
def CommonFunc_90005884(_, flag: Flag | int, flag_1: Flag | int, character: uint, asset: Asset | int):
    """CommonFunc 90005884"""
    AddSpecialEffect(character, 9531)
    DisableAI(character)
    DisableAnimations(character)
    DisableAsset(asset)
    if FlagDisabled(flag):
        return
    if FlagDisabled(flag_1):
        return
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9532)
    EnableAnimations(character)
    EnableAsset(asset)


@RestartOnRest(90005885)
def CommonFunc_90005885(
    _,
    flag: Flag | int,
    bgm_boss_conv_param_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    left: int,
    left_1: int,
):
    """CommonFunc 90005885"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    if ValueNotEqual(left=0, right=bgm_boss_conv_param_id):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    else:
        SetBossMusic(bgm_boss_conv_param_id=921100, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(4, left=left, right=1)
    SkipLinesIfValueEqual(2, left=0, right=bgm_boss_conv_param_id)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    SkipLines(1)
    SetBossMusic(bgm_boss_conv_param_id=925000, state=BossMusicState.HeatUp)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(5, left=left_1, right=1)
    SkipLinesIfValueEqual(2, left=0, right=bgm_boss_conv_param_id)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
    SkipLines(1)
    SetBossMusic(bgm_boss_conv_param_id=925000, state=BossMusicState.LongFadeOut)
    End()
    if ValueNotEqual(left=0, right=bgm_boss_conv_param_id):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)
    else:
        SetBossMusic(bgm_boss_conv_param_id=925000, state=BossMusicState.NormalFadeOut)


@RestartOnRest(91005600)
def CommonFunc_91005600(_, flag: Flag | int, asset: Asset | int, vfx_id: int):
    """CommonFunc 91005600"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    OR_1.Add(Invasion())
    OR_1.Add(InvasionPending())
    AND_1.Add(OR_1)
    OR_4.Add(AND_1)
    OR_4.Add(FlagEnabled(9982))
    
    MAIN.Await(OR_4)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    OR_5.Add(Multiplayer())
    OR_5.Add(MultiplayerPending())
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_8.Add(not AND_5)
    AND_8.Add(FlagDisabled(9982))
    
    MAIN.Await(AND_8)
    
    Restart()
    
    MAIN.Await(FlagEnabled(flag))


@RestartOnRest(90005100)
def CommonFunc_90005100(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    asset: Asset | int,
    source_flag: Flag | int,
    value: uint,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
):
    """CommonFunc 90005100"""
    if FlagDisabled(9000):
        DeleteAssetVFX(asset, erase_root=False)
        WaitFrames(frames=1)
    DeleteAssetVFX(asset)
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_8)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_9)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_10)
        Goto(Label.L6)
    EnableFlag(flag_11)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfFlagEnabled(Label.L5, flag=69080)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100680))
    
    MAIN.Await(AND_2)
    
    EnableFlag(710510)
    DisplayTutorialMessage(tutorial_param_id=1510, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9108, flag=710510, bit_count=1)
    EnableFlag(69080)

    # --- Label 5 --- #
    DefineLabel(5)
    End()
    DeleteAssetVFX(asset, erase_root=False)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    DisableFlag(flag_8)
    DisableFlag(flag_9)
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    AND_10.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_10:
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    AND_11.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_11:
        return RESTART
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=0,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_2)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=1,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_3)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=2,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_4)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=3,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_5)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=4,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=5,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=6,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=7,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=8,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=9):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=9,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    OR_2.Add(EventValue(flag=source_flag, bit_count=4) != value)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005101)
def CommonFunc_90005101(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    asset: Asset | int,
    source_flag: Flag | int,
    value: uint,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
):
    """CommonFunc 90005101"""
    if FlagDisabled(9000):
        DeleteAssetVFX(asset, erase_root=False)
        WaitFrames(frames=1)
    DeleteAssetVFX(asset)
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6401)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_8)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_9)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_10)
        Goto(Label.L6)
    EnableFlag(flag_11)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfFlagEnabled(Label.L5, flag=710510)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100680))
    
    MAIN.Await(AND_2)
    
    EnableFlag(710510)
    DisplayTutorialMessage(tutorial_param_id=1510, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9108, flag=710510, bit_count=1)

    # --- Label 5 --- #
    DefineLabel(5)
    End()
    DeleteAssetVFX(asset, erase_root=False)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    DisableFlag(flag_8)
    DisableFlag(flag_9)
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    AND_10.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_10:
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    AND_11.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_11:
        return RESTART
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6401)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=0,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_2)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=1,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_3)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=2,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_4)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=3,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_5)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=4,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=5,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=6,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=7,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=8,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=9):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=9,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    OR_2.Add(EventValue(flag=source_flag, bit_count=4) != value)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005102)
def CommonFunc_90005102(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    asset: Asset | int,
    source_flag: Flag | int,
    value: uint,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
):
    """CommonFunc 90005102"""
    if FlagDisabled(9000):
        DeleteAssetVFX(asset, erase_root=False)
        WaitFrames(frames=1)
    DeleteAssetVFX(asset)
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    AND_1.Add(FlagEnabled(flag_12))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_8)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_9)
        Goto(Label.L6)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_10)
        Goto(Label.L6)
    EnableFlag(flag_11)
    Goto(Label.L6)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfFlagEnabled(Label.L5, flag=69080)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100680))
    
    MAIN.Await(AND_2)
    
    EnableFlag(710510)
    DisplayTutorialMessage(tutorial_param_id=1510, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9108, flag=710510, bit_count=1)
    EnableFlag(69080)

    # --- Label 5 --- #
    DefineLabel(5)
    End()
    DeleteAssetVFX(asset, erase_root=False)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    DisableFlag(flag_8)
    DisableFlag(flag_9)
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    AND_10.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_10:
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    AND_11.Add(EventValue(flag=source_flag, bit_count=4) > value)
    if AND_11:
        return RESTART
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=0,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_2)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=1,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_3)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=2,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_4)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=3,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_5)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=4,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=5,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=6):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=6,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=7):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=7,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=8):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=8,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    if UnsignedEqual(left=value, right=9):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=4,
            operand=9,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    OR_2.Add(EventValue(flag=source_flag, bit_count=4) != value)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(90005110)
def CommonFunc_90005110(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    asset: uint,
    item_lot: int,
    item: BaseItemParam | int,
    vfx_id: int,
    action_button_id: int,
    animation_id: int,
    left: int,
):
    """CommonFunc 90005110"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=100, vfx_id=vfx_id)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    
    MAIN.Await(AND_1)
    
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id)
    DeleteAssetVFX(asset)
    Wait(4.0)
    DisplayBanner(BannerType.GreatRuneRestored)
    AwardItemLot(item_lot, host_only=True)
    RemoveGoodFromPlayer(item=item, quantity=1)
    EnableFlag(flag)
    End()
    if ValueEqual(left=left, right=0):
        return


@RestartOnRest(9005910)
def CommonFunc_9005910(_, asset: Asset | int, first_flag: Flag | int, last_flag: Flag | int, right: int):
    """CommonFunc 9005910"""
    DeleteAssetVFX(asset)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueGreaterThanOrEqual(left=3, right=right):
        CreateAssetVFX(asset, dummy_id=201, vfx_id=62)
    else:
        CreateAssetVFX(asset, dummy_id=201, vfx_id=63)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    CreateAssetVFX(asset, dummy_id=201, vfx_id=61)
    
    MAIN.Await(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    DeleteAssetVFX(asset)
    End()


@RestartOnRest(9005911)
def CommonFunc_9005911(_, asset: uint):
    """CommonFunc 9005911"""
    CreateAssetVFX(asset, dummy_id=201, vfx_id=40)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=3.0))
    
    DeleteAssetVFX(asset)


@RestartOnRest(9005912)
def CommonFunc_9005912(_, flag: Flag | int, place_name_id: PlaceName | int):
    """CommonFunc 9005912"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    DisplaySubareaWelcomeMessage(place_name_id=place_name_id)


@RestartOnRest(9005920)
def CommonFunc_9005920(
    _,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
):
    """CommonFunc 9005920"""
    if FlagDisabled(9800):
        DisableCharacter(character)
        DisableAnimations(character)
    else:
        EnableCharacter(character)
        EnableAnimations(character)
    if FlagDisabled(9801):
        DisableCharacter(character_1)
        DisableAnimations(character_1)
    else:
        EnableCharacter(character_1)
        EnableAnimations(character_1)
    if FlagDisabled(9802):
        DisableCharacter(character_2)
        DisableAnimations(character_2)
    else:
        EnableCharacter(character_2)
        EnableAnimations(character_2)
    if FlagDisabled(9803):
        DisableCharacter(character_3)
        DisableAnimations(character_3)
    else:
        EnableCharacter(character_3)
        EnableAnimations(character_3)
    if FlagDisabled(9804):
        DisableCharacter(character_4)
        DisableAnimations(character_4)
    else:
        EnableCharacter(character_4)
        EnableAnimations(character_4)
    if FlagDisabled(9805):
        DisableCharacter(character_5)
        DisableAnimations(character_5)
    else:
        EnableCharacter(character_5)
        EnableAnimations(character_5)
    if FlagDisabled(9806):
        DisableCharacter(character_6)
        DisableAnimations(character_6)
    else:
        EnableCharacter(character_6)
        EnableAnimations(character_6)
    if FlagDisabled(9807):
        DisableCharacter(character_7)
        DisableAnimations(character_7)
    else:
        EnableCharacter(character_7)
        EnableAnimations(character_7)
    if FlagDisabled(9808):
        DisableCharacter(character_8)
        DisableAnimations(character_8)
    else:
        EnableCharacter(character_8)
        EnableAnimations(character_8)
    if FlagDisabled(9809):
        DisableCharacter(character_9)
        DisableAnimations(character_9)
    else:
        EnableCharacter(character_9)
        EnableAnimations(character_9)


@RestartOnRest(90005920)
def CommonFunc_90005920(_, flag: Flag | int, asset: Asset | int, obj_act_id: uint):
    """CommonFunc 90005920"""
    if FlagEnabled(flag):
        return
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6150)
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(0.30000001192092896)
    DeleteAssetVFX(asset)


@RestartOnRest(9005990)
def CommonFunc_9005990(_, seconds: float):
    """CommonFunc 9005990"""
    Wait(seconds)


@RestartOnRest(98005100)
def CommonFunc_98005100(_, match_type: uchar, flag: Flag | int, text: EventText | int, text_1: EventText | int):
    """CommonFunc 98005100"""
    SetAreaWelcomeMessageState(state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ArenaMatchReadyState(ready=True))
    
    MAIN.Await(AND_1)
    
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=text, priority=1, should_interrupt=True)
    EnableFlag(280)
    DisplayBanner(BannerType.Commence)
    if PlayerInOwnWorld():
        WaitUntilArenaHalfTime(match_type=match_type, is_second_half=False)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_2)
    
    DisplayFlashingMessageWithPriority(text=text_1, priority=2, should_interrupt=True)
    AddSpecialEffect(PLAYER, 1160)
    if PlayerInOwnWorld():
        WaitUntilArenaHalfTime(match_type=match_type, is_second_half=True)
    
    MAIN.Await(PlayerInOwnWorld())
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)


@RestartOnRest(98005110)
def CommonFunc_98005110(_, flag: Flag | int):
    """CommonFunc 98005110"""
    OR_1.Add(ArenaSoloScoreComparison(comparison_type=ComparisonType.Equal, score=1))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)


@RestartOnRest(98005120)
def CommonFunc_98005120(_, flag: Flag | int):
    """CommonFunc 98005120"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableInvincibility(PLAYER)
    DisableFlag(280)
    DisplayFlashingMessageWithPriority(text=88040, priority=0, should_interrupt=True)
    WaitFrames(frames=1)
    Wait(5.0)
    Unknown_2003_83(unk_0_1=False)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.OneVersusOne, has_spirit_summon=False)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.OneVersusOne, has_spirit_summon=False)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.TwoVersusTwo, has_spirit_summon=False)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.ThreeVersusThree, has_spirit_summon=False)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.TwoVersusTwo, has_spirit_summon=True)
    GotoLinesIfArenaMatchType(Label.L9, match_type=ArenaMatchType.ThreeVersusThree, has_spirit_summon=True)
    OR_1.Add(ArenaSoloResult(result=ArenaResult.Win))
    OR_2.Add(ArenaSoloResult(result=ArenaResult.Draw))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    Goto(Label.L2)

    # --- Label 9 --- #
    DefineLabel(9)
    OR_1.Add(ArenaTeamResults(result=ArenaResult.Win))
    OR_2.Add(ArenaTeamResults(result=ArenaResult.Draw))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    DisplayBanner(BannerType.Victory)
    AddSpecialEffect(PLAYER, 1140)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88050, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisplayBanner(BannerType.Stalemate)
    AddSpecialEffect(PLAYER, 1150)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88051, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisplayBanner(BannerType.Defeat)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88052, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()


@RestartOnRest(98005121)
def CommonFunc_98005121(_, flag: Flag | int):
    """CommonFunc 98005121"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableInvincibility(PLAYER)
    DisableFlag(280)
    OR_3.Add(ArenaSoloResult(result=ArenaResult.Draw))
    SkipLinesIfConditionFalse(2, OR_3)
    DisplayFlashingMessageWithPriority(text=88040, priority=0, should_interrupt=True)
    Wait(3.5)
    Wait(1.0)
    Unknown_2003_83(unk_0_1=False)
    WaitFrames(frames=1)
    OR_1.Add(ArenaSoloResult(result=ArenaResult.Win))
    OR_2.Add(ArenaSoloResult(result=ArenaResult.Draw))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    DisplayBanner(BannerType.Victory)
    AddSpecialEffect(PLAYER, 1140)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88050, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisplayBanner(BannerType.Stalemate)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88051, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisplayBanner(BannerType.Defeat)
    Wait(5.0)
    DisplayFlashingMessageWithPriority(text=88052, priority=0, should_interrupt=True)
    Wait(0.5)
    BanishPhantomsAndUpdateServerPvPStats(unknown=0)
    End()
