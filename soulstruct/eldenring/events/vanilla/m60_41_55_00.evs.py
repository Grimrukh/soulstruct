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
    Unknown_2004_60(character=1041550400, obj=1041552000)
    Unknown_2004_60(character=1041550401, obj=1041552000)
    Unknown_2004_60(character=1041550402, obj=1041552000)
    Unknown_2004_60(character=1041550403, obj=1041552000)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1041552400(0, character=1041550400)
    Event_1041552400(1, character=1041550401)
    Event_1041552400(2, character=1041550402)
    Event_1041552400(3, character=1041550406)
    Event_1041552400(4, character=1041550408)
    Event_1041552400(5, character=1041550409)
    RunCommonEvent(0, 90005201, args=(1041550301, 30001, 20001, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(1041550351, 30000, 20000, 1041552351, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1041550352, 1041552352, 0.0, 3000), arg_types="IIfi")
    Event_1041552350(0, character=1041550200, region=1041552200, character_1=1041555200)
    Event_1041552350(1, character=1041550201, region=1041552201, character_1=1041555200)
    Event_1041552350(2, character=1041550202, region=1041552202, character_1=1041555200)
    Event_1041552350(3, character=1041550203, region=1041552203, character_1=1041555200)
    Event_1041552350(4, character=1041550204, region=1041552204, character_1=1041555200)
    Event_1041552350(5, character=1041550205, region=1041552205, character_1=1041555200)
    RunCommonEvent(0, 90005200, args=(1041550250, 30001, 20001, 1041552250, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(1041550251, 30001, 20001, 1041552250, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1041550252, 30001, 20001, 1041552250, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1041550253, 30001, 20001, 1041552250, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1041550254, 30001, 20001, 1041552250, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1041550255, 30001, 20001, 1041552250, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )


@RestartOnRest(1041552350)
def Event_1041552350(_, character: uint, region: uint, character_1: uint):
    """Event 1041552350"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    ForceAnimation(character, 20018, unknown2=1.0)
    Wait(1.600000023841858)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 30008, loop=True, unknown2=1.0)
    DisableAI(character)
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
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=260, unk_12_16=1)
    IfHasAIStatus(
        OR_1,
        character_1,
        ai_status=AIStatusType.Battle,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    IfConditionTrue(OR_1, input_condition=AND_4)
    IfConditionTrue(OR_1, input_condition=AND_5)
    IfConditionTrue(OR_1, input_condition=AND_6)
    IfConditionTrue(OR_1, input_condition=AND_7)
    IfConditionTrue(OR_1, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(0.10000000149011612)
    ForceAnimation(character, 20008, unknown2=1.0)
    EnableAI(character)
    Wait(5.0)
    IfHasAIStatus(AND_2, character, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(AND_2, character=character, region=region)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfCharacterDead(OR_2, character)
    AwaitConditionTrue(OR_2)
    Restart()


@RestartOnRest(1041552400)
def Event_1041552400(_, character: uint):
    """Event 1041552400"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=260, unk_12_16=1)
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
    IfConditionTrue(OR_1, input_condition=AND_4)
    IfConditionTrue(OR_1, input_condition=AND_5)
    IfConditionTrue(OR_1, input_condition=AND_6)
    IfConditionTrue(OR_1, input_condition=AND_7)
    IfConditionTrue(OR_1, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    EnableAI(character)
