"""
North Caelid (SE) (SW)

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
from .enums.m60_50_40_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1050400000, asset=Assets.AEG099_060_9000)
    RunCommonEvent(
        1050402210,
        slot=0,
        args=(1050400200, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=1,
        args=(1050400201, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=2,
        args=(1050400202, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=3,
        args=(1050400203, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=4,
        args=(1050400204, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=5,
        args=(1050400205, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1050402210,
        slot=6,
        args=(1050400207, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    Event_1050402201(0, character=Characters.DragonbarrowDragon0)
    Event_1050402201(1, character=Characters.DragonbarrowDragon1)
    Event_1050402201(2, character=Characters.DragonbarrowDragon2)
    Event_1050402201(3, character=Characters.DragonbarrowDragon3)
    Event_1050402201(4, character=Characters.DragonbarrowDragon4)
    Event_1050402201(5, character=Characters.DragonbarrowDragon5)
    Event_1050402201(6, character=Characters.DragonbarrowDragon6)
    Event_1050402202(0, character=Characters.DragonbarrowDragon0)
    Event_1050402202(1, character=Characters.DragonbarrowDragon1)
    Event_1050402202(2, character=Characters.DragonbarrowDragon2)
    Event_1050402202(3, character=Characters.DragonbarrowDragon3)
    Event_1050402202(4, character=Characters.DragonbarrowDragon4)
    Event_1050402202(5, character=Characters.DragonbarrowDragon5)
    Event_1050402202(6, character=Characters.DragonbarrowDragon6)
    Event_1050402204(0, character=Characters.DragonbarrowDragon0)
    Event_1050402204(1, character=Characters.DragonbarrowDragon1)
    Event_1050402204(2, character=Characters.DragonbarrowDragon2)
    Event_1050402204(3, character=Characters.DragonbarrowDragon3)
    Event_1050402204(4, character=Characters.DragonbarrowDragon4)
    Event_1050402204(5, character=Characters.DragonbarrowDragon5)
    Event_1050402204(6, character=Characters.DragonbarrowDragon6)
    Event_1050402203()
    Event_1050402206()
    Event_1050402800()
    CommonFunc_90005300(
        0,
        flag=1050400800,
        character=Characters.LargeDragonbarrowDragon,
        item_lot=1050400800,
        seconds=0.0,
        item_is_dropped=0,
    )
    Event_1050402205()


@RestartOnRest(1050402201)
def Event_1050402201(_, character: uint):
    """Event 1050402201"""
    if FlagEnabled(1050400599):
        return
    AddSpecialEffect(character, 4405)
    
    MAIN.Await(CharacterDead(character))
    
    AND_1.Add(HealthRatio(Characters.LargeDragonbarrowDragon) > 3.0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AddSpecialEffect(Characters.LargeDragonbarrowDragon, 4402)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(Characters.LargeDragonbarrowDragon, 4404)


@RestartOnRest(1050402202)
def Event_1050402202(_, character: uint):
    """Event 1050402202"""
    GotoIfFlagEnabled(Label.L0, flag=1050400599)
    
    MAIN.Await(CharacterDead(Characters.LargeDragonbarrowDragon))
    
    EnableFlag(1050400599)
    Kill(character, award_runes=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)


@RestartOnRest(1050402203)
def Event_1050402203():
    """Event 1050402203"""
    MAIN.Await(CharacterDead(Characters.LargeDragonbarrowDragon))
    
    DestroyAsset(Assets.AEG007_476_1000)
    DisableMapCollision(collision=1050401500)


@RestartOnRest(1050402204)
def Event_1050402204(_, character: uint):
    """Event 1050402204"""
    DisableNetworkSync()
    DisableHealthBar(character)
    Wait(3.0)
    EnableHealthBar(character)


@RestartOnRest(1050402205)
def Event_1050402205():
    """Event 1050402205"""
    if FlagEnabled(1050400800):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterDead(Characters.LargeDragonbarrowDragon))
    
    Wait(2.0)
    DisplayFlashingMessage(30063)


@RestartOnRest(1050402206)
def Event_1050402206():
    """Event 1050402206"""
    DisableAsset(1050406500)


@RestartOnRest(1050402210)
def Event_1050402210(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1050402210"""
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
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    OR_14.Add(AttackedWithDamageType(attacked_entity=character))
    OR_14.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_14.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_14.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_14.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_14.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_14.Add(TimeElapsed(seconds=seconds))
    AwaitConditionTrue(OR_14)
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


@RestartOnRest(1050402800)
def Event_1050402800():
    """Event 1050402800"""
    if FlagEnabled(1050400599):
        return
    ForceAnimation(Characters.LargeDragonbarrowDragon, 30006)
    GotoIfFlagEnabled(Label.L0, flag=1050402599)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_9)
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1050402800))
    OR_1.Add(AND_2)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LargeDragonbarrowDragon))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon1))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon2))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon3))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon4))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon5))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonbarrowDragon6))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(1050402599)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(HasAIStatus(Characters.LargeDragonbarrowDragon, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon0, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon1, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon2, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon3, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon4, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon5, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(Characters.DragonbarrowDragon6, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 10251))
    
    MAIN.Await(AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.LargeDragonbarrowDragon, 20006)
    Wait(20.0)
    if FlagEnabled(1050400599):
        return
    AND_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionTrue(1, AND_3)
    AddSpecialEffect(20000, 10251)
    AddSpecialEffect(Characters.DragonbarrowDragon0, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon1, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon2, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon3, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon4, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon5, 10250)
    AddSpecialEffect(Characters.DragonbarrowDragon6, 10250)
    Wait(18.0)
    ForceAnimation(Characters.LargeDragonbarrowDragon, 30006)
    Wait(10.0)
    Restart()
