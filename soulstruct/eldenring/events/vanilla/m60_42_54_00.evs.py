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
    RegisterLadder(start_climbing_flag=1042540580, stop_climbing_flag=1042540581, obj=1042541580)
    RegisterLadder(start_climbing_flag=1042540582, stop_climbing_flag=1042540583, obj=1042541582)
    RegisterLadder(start_climbing_flag=1042540584, stop_climbing_flag=1042540585, obj=1042541584)
    RunCommonEvent(
        0,
        90005633,
        args=(580350, 580050, 1042540400, 30017, 20017, 1042541400, 1042541410),
        arg_types="IIIiiII",
    )
    RunCommonEvent(0, 90005706, args=(1042540700, 30025, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042540700)
    RunCommonEvent(0, 90005250, args=(1042540200, 1042542200, 0.0, 3005), arg_types="IIfi")
    Event_1042542350(0, character=1042540300, region=1042542300, character_1=1042545300)
    Event_1042542350(1, character=1042540301, region=1042542301, character_1=1042545300)
    Event_1042542350(2, character=1042540302, region=1042542302, character_1=1042545300)
    Event_1042542350(3, character=1042540310, region=1042542310, character_1=1042545310)
    Event_1042542350(4, character=1042540311, region=1042542311, character_1=1042545310)
    Event_1042542350(5, character=1042540312, region=1042542312, character_1=1042545310)
    Event_1042542350(6, character=1042540313, region=1042542313, character_1=1042545310)
    Event_1042542350(7, character=1042540314, region=1042542314, character_1=1042545310)
    Event_1042542350(8, character=1042540315, region=1042542315, character_1=1042545310)
    Event_1042542350(9, character=1042540316, region=1042542316, character_1=1042545310)
    Event_1042542350(10, character=1042540317, region=1042542317, character_1=1042545310)
    Event_1042542350(11, character=1042540318, region=1042542318, character_1=1042545310)
    Event_1042542350(12, character=1042540327, region=1042542327, character_1=1042545327)
    Event_1042542350(13, character=1042540328, region=1042542328, character_1=1042545327)
    Event_1042542350(14, character=1042540329, region=1042542329, character_1=1042545327)
    RunCommonEvent(0, 90005251, args=(1042540331, 4.0, 0.0, 3004), arg_types="Iffi")
    Event_1042542350(15, character=1042540338, region=1042542338, character_1=1042545338)
    Event_1042542350(16, character=1042540339, region=1042542339, character_1=1042545338)
    Event_1042542350(17, character=1042540303, region=1042542303, character_1=1042545303)
    Event_1042542350(18, character=1042540304, region=1042542304, character_1=1042545303)
    Event_1042542350(19, character=1042540305, region=1042542305, character_1=1042545303)
    RunCommonEvent(0, 90005200, args=(1042540651, 30004, 20004, 1042542651, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1042540652, 30004, 20004, 1042542651, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1042540653, 30004, 20004, 1042542651, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1042542350)
def Event_1042542350(_, character: uint, region: uint, character_1: uint):
    """Event 1042542350"""
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
