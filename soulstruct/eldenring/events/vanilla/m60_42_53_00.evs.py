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
    RunCommonEvent(0, 90005300, args=(1042530501, 1042530501, 1042530300, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005390,
        args=(1042530350, 1042532350, 1042530365, 1042530350, 0, 1043530100),
        arg_types="IIIIii",
    )
    RunCommonEvent(0, 90005391, args=(1042530350, 1042532350, 1042530365, 1042530350, 0), arg_types="IIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1042530202, 1042532202, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1042530201, 30002, 20002, 1042532300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1042530305, 30010, 20010, 1042532305, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1042530317, 30010, 20010, 1042532305, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1042530318, 30010, 20010, 1042532305, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1042530319, 1042532202, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042530320, 1042532202, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1042530323, 1042532202, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(1042530300, 30005, 20021, 1042532300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1042530308, 30010, 20010, 1042532300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1042530309, 30010, 20010, 1042532300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1042530322, 1042532300, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1042530314, 30005, 20021, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1042530403, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1042530407, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1042530409, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1042530413, 30010, 20010, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1042532365(0, 1042530365)


@RestartOnRest(1042532365)
def Event_1042532365(_, character: uint):
    """Event 1042532365"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=0)
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
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=character, unk_8_12=260, unk_12_16=1)
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


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005490, args=(1042530402, 1042530403, 1042531402, 0, 0, 1042532402, 0), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1042530406, 1042530407, 1042531406, 0, 0, 1042532406, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1042530408, 1042530409, 1042531408, 0, 0, 1042532408, 1), arg_types="IIIIIII")
    RunCommonEvent(0, 90005490, args=(1042530412, 1042530413, 1042531412, 0, 0, 1042532412, 1), arg_types="IIIIIII")
