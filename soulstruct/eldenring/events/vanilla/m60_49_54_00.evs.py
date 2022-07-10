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
    RegisterGrace(grace_flag=1049540000, obj=1049541950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76652, 76650, 1049541980, 77520, 0, 78520, 78521, 78522, 78523, 78524, 78525, 78526, 78527, 78528, 78529),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1049540200, 1049540200, 1049540700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005501,
        args=(1049540510, 1049541511, 10, 12031510, 12031511, 12031512, 1049540512),
        arg_types="IIIIIII",
    )
    Event_1049542510()
    RunCommonEvent(0, 90005640, args=(1049540540, 1049541540), arg_types="II")
    Event_1049542210()
    Event_1049542216(0, character=1049540216)
    RunCommonEvent(0, 90005261, args=(1049540260, 1049542260, 10.0, 0.0, 20010), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1049540373, 1049542260, 10.0, 0.0, 20002), arg_types="IIffi")
    Event_1049542350(0, character__region=1049540350, character=1049540370)
    RunCommonEvent(0, 900005610, args=(1049541600, 100, 800, 0), arg_types="IiiI")
    Event_1049543700(0, 1049540700, 1049542700, 155.0)
    RunCommonEvent(0, 90005706, args=(1049540710, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049540700)
    DisableBackread(1049540710)


@RestartOnRest(1049542210)
def Event_1049542210():
    """Event 1049542210"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(1049540210)
    DisableAI(1049540211)
    DisableAI(1049540212)
    IfAttackedWithDamageType(OR_1, attacked_entity=1049540210, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1049540211, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=1049540212, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=1049540210, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540210, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540210, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540210, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540210, unk_8_12=260, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540211, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540211, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540211, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540211, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540211, unk_8_12=260, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540212, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540212, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540212, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540212, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1049540212, unk_8_12=260, unk_12_16=1)
    IfCharacterHasSpecialEffect(AND_1, 1049540210, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 1049540210, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 1049540210, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 1049540210, 90160)
    IfCharacterHasSpecialEffect(AND_2, 1049540210, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 1049540210, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 1049540210, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 1049540210, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, 1049540210, 90162)
    IfCharacterHasSpecialEffect(AND_3, 1049540210, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, 1049540210, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, 1049540210, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, 1049540210, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_3, 1049540210, 90161)
    IfCharacterHasSpecialEffect(AND_4, 1049540210, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1049540210, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1049540210, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1049540210, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1049540210, 90162)
    IfCharacterHasSpecialEffect(AND_5, 1049540210, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1049540210, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1049540210, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1049540210, 90160)
    IfCharacterHasSpecialEffect(AND_6, 1049540211, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1049540211, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1049540211, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1049540211, 90160)
    IfCharacterHasSpecialEffect(AND_7, 1049540211, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1049540211, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1049540211, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1049540211, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1049540211, 90162)
    IfCharacterHasSpecialEffect(AND_8, 1049540211, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1049540211, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1049540211, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1049540211, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1049540211, 90161)
    IfCharacterHasSpecialEffect(AND_9, 1049540211, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_9, 1049540211, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_9, 1049540211, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_9, 1049540211, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_9, 1049540211, 90162)
    IfCharacterHasSpecialEffect(AND_10, 1049540211, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, 1049540211, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, 1049540211, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_10, 1049540211, 90160)
    IfCharacterHasSpecialEffect(AND_11, 1049540212, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_11, 1049540212, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_11, 1049540212, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_11, 1049540212, 90160)
    IfCharacterHasSpecialEffect(AND_12, 1049540212, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_12, 1049540212, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_12, 1049540212, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_12, 1049540212, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_12, 1049540212, 90162)
    IfCharacterHasSpecialEffect(AND_13, 1049540212, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_13, 1049540212, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_13, 1049540212, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_13, 1049540212, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_13, 1049540212, 90161)
    IfCharacterHasSpecialEffect(AND_14, 1049540212, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_14, 1049540212, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_14, 1049540212, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_14, 1049540212, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_14, 1049540212, 90162)
    IfCharacterHasSpecialEffect(AND_15, 1049540212, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_15, 1049540212, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_15, 1049540212, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_15, 1049540212, 90160)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(OR_1, input_condition=AND_3)
    IfConditionTrue(OR_1, input_condition=AND_4)
    IfConditionTrue(OR_1, input_condition=AND_5)
    IfConditionTrue(OR_1, input_condition=AND_6)
    IfConditionTrue(OR_1, input_condition=AND_7)
    IfConditionTrue(OR_1, input_condition=AND_8)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfConditionTrue(OR_1, input_condition=AND_10)
    IfConditionTrue(OR_1, input_condition=AND_11)
    IfConditionTrue(OR_1, input_condition=AND_12)
    IfConditionTrue(OR_1, input_condition=AND_13)
    IfConditionTrue(OR_1, input_condition=AND_14)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableAI(1049540210)
    EnableAI(1049540211)
    EnableAI(1049540212)


@RestartOnRest(1049542216)
def Event_1049542216(_, character: uint):
    """Event 1049542216"""
    EnableImmortality(character)
    DisableAnimations(character)
    ForceAnimation(character, 30005, loop=True, unknown2=1.0)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    End()


@RestartOnRest(1049542350)
def Event_1049542350(_, character__region: uint, character: uint):
    """Event 1049542350"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    SetCharacterEventTarget(character, region=character__region)
    IfCharacterHasSpecialEffect(AND_1, character, 11893)
    IfCharacterAlive(AND_1, character__region)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkUpdateRate(character__region, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=283,
        set_draw_parent=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(character, 20003, unknown2=1.0)
    AddSpecialEffect(character__region, 11880)
    AddSpecialEffect(character, 11880)
    ReplanAI(character__region)
    Wait(5.0)
    SetNetworkUpdateRate(character__region, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@NeverRestart(1049542510)
def Event_1049542510():
    """Event 1049542510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1049540510,
            1049540511,
            10,
            12031510,
            1049541511,
            1049543511,
            12031512,
            12033512,
            1049542511,
            12032512,
            1049540512,
            1049542513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@RestartOnRest(1049540519)
def Event_1049540519():
    """Event 1049540519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1049540510)


@RestartOnRest(1049543700)
def Event_1049543700(_, character: uint, region: uint, distance: float):
    """Event 1049543700"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1049549201)
    EndIfFlagEnabled(1047589205)
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagEnabled(1, 1049512700)
    DisableFlag(1049549200)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(1049549200)
    Wait(30.0)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005421, args=(1249540300, 1249541301, 1249548301), arg_types="III")
    RunCommonEvent(0, 90005422, args=(1249548301, 1249541300, 1249543301), arg_types="III")
    RunCommonEvent(0, 90005424, args=(1249541300, 1249540302, 1249540303, 1249540300, 1249541301), arg_types="IIIII")
    RunCommonEvent(0, 90005423, args=(1249540302,))
    RunCommonEvent(0, 90005423, args=(1249540303,))
    RunCommonEvent(0, 90005261, args=(1249540300, 1249542300, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1249540301, 1249542300, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1249540302, 1249542300, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1249540303, 1249542300, 10.0, 0.0, 0), arg_types="IIffi")


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(
        0,
        90005420,
        args=(1249540300, 1249541300, 1249541301, 1249540301, 1249540302, 1249540303, 0.0),
        arg_types="IIIIIIf",
    )
