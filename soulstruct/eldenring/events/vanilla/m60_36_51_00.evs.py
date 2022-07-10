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
    RunCommonEvent(0, 90005683, args=(62313, 1036511300, 208, 78390, 78390), arg_types="IIiII")
    RunCommonEvent(0, 900005610, args=(1036511680, 100, 800, 1036518600), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005620,
        args=(1036510570, 1036511570, 1036511571, 1036511572, 1036512570, 1036512571, 1036512572),
        arg_types="IIIIIIi",
    )
    Event_1036512575()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1036512400(0, 1036510400, 2.0, 0.0, 0)
    Event_1036512400(1, 1036510401, 2.0, 0.0, 0)
    Event_1036512400(2, 1036510410, 2.0, 0.0, 0)
    Event_1036512400(3, 1036510411, 2.0, 0.0, 0)
    Event_1036512400(4, 1036510412, 2.0, 0.0, 0)
    Event_1036512450(5, 1036510407, 2.0, 0.0, 0)
    Event_1036512450(6, 1036510408, 2.0, 0.0, 0)
    Event_1036512450(7, 1036510409, 2.0, 0.0, 0)
    Event_1036512450(8, 1036510413, 2.0, 0.0, 0)
    Event_1036512450(9, 1036510414, 2.0, 0.0, 0)
    Event_1036512450(10, 1036510416, 2.0, 0.0, 0)
    Event_1036512450(11, 1036510417, 2.0, 0.0, 0)
    Event_1036512450(12, 1036510418, 2.0, 0.0, 0)
    Event_1036512450(13, 1036510419, 2.0, 0.0, 0)
    Event_1036512450(14, 1036510420, 2.0, 0.0, 0)
    Event_1036512450(15, 1036510400, 2.0, 0.0, 0)
    Event_1036512450(16, 1036510401, 2.0, 0.0, 0)
    Event_1036512450(17, 1036510404, 2.0, 0.0, 0)
    RunCommonEvent(0, 90005251, args=(1036510450, 5.0, 0.0, 3001), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1036510300, 1036512300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1036510300, 1036512301, 0.0, -1), arg_types="IIfi")
    Event_1036512300()
    RunCommonEvent(0, 90005261, args=(1036510310, 1036512300, 3.0, 1.0, -1), arg_types="IIffi")


@RestartOnRest(1036512300)
def Event_1036512300():
    """Event 1036512300"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1036512300)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1036512301)
    ChangePatrolBehavior(1036510300, patrol_information_id=1036513301)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1036512400)
def Event_1036512400(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036512400"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterInsideRegion(AND_10, character=1036510300, region=1036512400)
    IfHasAIStatus(AND_10, 1036510300, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_10)
    IfCharacterInsideRegion(AND_11, character=1036510304, region=1036512400)
    IfHasAIStatus(AND_11, 1036510304, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_11)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1036512450)
def Event_1036512450(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036512450"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfEntityWithinDistance(AND_8, entity=1036510300, other_entity=character, radius=8.0)
    IfHasAIStatus(AND_8, 1036510300, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfEntityWithinDistance(AND_7, entity=1036510304, other_entity=character, radius=8.0)
    IfHasAIStatus(AND_7, 1036510304, ai_status=AIStatusType.Battle)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1036512575)
def Event_1036512575():
    """Event 1036512575"""
    DisableNetworkSync()
    SkipLinesIfFlagEnabled(3, 1036510570)
    DisableObjectActivation(1036511580, obj_act_id=110063)
    IfFlagEnabled(MAIN, 1036510570)
    EnableObjectActivation(1036511580, obj_act_id=110063)
