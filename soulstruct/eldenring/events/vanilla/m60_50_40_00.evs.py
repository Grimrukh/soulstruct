"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1050400000, obj=1050401950, unknown=5.0)
    RunCommonEvent(0, 1050402210, args=(1050400200, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 1050402210, args=(1050400201, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(2, 1050402210, args=(1050400202, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(3, 1050402210, args=(1050400203, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(4, 1050402210, args=(1050400204, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(5, 1050402210, args=(1050400205, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(6, 1050402210, args=(1050400207, 30000, 20000, 1050402800, 18.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1050402201(0, character=1050400200)
    Event_1050402201(1, character=1050400201)
    Event_1050402201(2, character=1050400202)
    Event_1050402201(3, character=1050400203)
    Event_1050402201(4, character=1050400204)
    Event_1050402201(5, character=1050400205)
    Event_1050402201(6, character=1050400207)
    Event_1050402202(0, character=1050400200)
    Event_1050402202(1, character=1050400201)
    Event_1050402202(2, character=1050400202)
    Event_1050402202(3, character=1050400203)
    Event_1050402202(4, character=1050400204)
    Event_1050402202(5, character=1050400205)
    Event_1050402202(6, character=1050400207)
    Event_1050402204(0, character=1050400200)
    Event_1050402204(1, character=1050400201)
    Event_1050402204(2, character=1050400202)
    Event_1050402204(3, character=1050400203)
    Event_1050402204(4, character=1050400204)
    Event_1050402204(5, character=1050400205)
    Event_1050402204(6, character=1050400207)
    Event_1050402203()
    Event_1050402206()
    Event_1050402800()
    RunCommonEvent(0, 90005300, args=(1050400800, 1050400800, 1050400800, 0.0, 0), arg_types="IIifi")
    Event_1050402205()


@RestartOnRest(1050402201)
def Event_1050402201(_, character: uint):
    """Event 1050402201"""
    EndIfFlagEnabled(1050400599)
    AddSpecialEffect(character, 4405)
    IfCharacterDead(MAIN, character)
    IfHealthGreaterThan(AND_1, 1050400800, value=3.0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AddSpecialEffect(1050400800, 4402)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(1050400800, 4404)


@RestartOnRest(1050402202)
def Event_1050402202(_, character: uint):
    """Event 1050402202"""
    GotoIfFlagEnabled(Label.L0, flag=1050400599)
    IfCharacterDead(MAIN, 1050400800)
    EnableFlag(1050400599)
    Kill(character, award_souls=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)


@RestartOnRest(1050402203)
def Event_1050402203():
    """Event 1050402203"""
    IfCharacterDead(MAIN, 1050400800)
    DestroyObject(1050401599)
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
    EndIfFlagEnabled(1050400800)
    EndIfPlayerNotInOwnWorld()
    IfCharacterDead(MAIN, 1050400800)
    Wait(2.0)
    DisplayBattlefieldMessage(30063)


@RestartOnRest(1050402206)
def Event_1050402206():
    """Event 1050402206"""
    DisableObject(1050406500)


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
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfAttackedWithDamageType(OR_14, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_14, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_14, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_14, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_14, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_14, character=character, unk_8_12=260, unk_12_16=1)
    IfTimeElapsed(OR_14, seconds=seconds)
    AwaitConditionTrue(OR_14)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1050402800)
def Event_1050402800():
    """Event 1050402800"""
    EndIfFlagEnabled(1050400599)
    ForceAnimation(1050400800, 30006, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=1050402599)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_2, input_condition=AND_9)
    IfCharacterHuman(OR_2, PLAYER)
    IfCharacterHollow(OR_2, PLAYER)
    IfCharacterWhitePhantom(OR_2, PLAYER)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1050402800)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400800, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400200, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400201, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400202, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400203, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400204, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400205, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1050400207, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(1050402599)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    IfHasAIStatus(OR_2, 1050400800, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400200, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400201, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400202, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400203, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400204, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400205, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 1050400207, ai_status=AIStatusType.Battle)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 10251)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(1050400800, 20006, unknown2=1.0)
    Wait(20.0)
    EndIfFlagEnabled(1050400599)
    IfCharacterType(AND_3, PLAYER, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionTrue(1, AND_3)
    AddSpecialEffect(20000, 10251)
    AddSpecialEffect(1050400200, 10250)
    AddSpecialEffect(1050400201, 10250)
    AddSpecialEffect(1050400202, 10250)
    AddSpecialEffect(1050400203, 10250)
    AddSpecialEffect(1050400204, 10250)
    AddSpecialEffect(1050400205, 10250)
    AddSpecialEffect(1050400207, 10250)
    Wait(18.0)
    ForceAnimation(1050400800, 30006, unknown2=1.0)
    Wait(10.0)
    Restart()
