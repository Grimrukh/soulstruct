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
    RegisterGrace(grace_flag=76300, obj=1037511950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76300, 1037511980, 77300, 0, 78300, 78301, 78302, 78303, 78304, 78305, 78306, 78307, 78308, 78309),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005870, args=(1037510800, 904510600, 28), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1037510800, 0, 1037510800, 1, 30300, 0.0), arg_types="IIIIif")
    Event_1037512208(0, 1037510208, 1037512208, 5.0, 0.0, 20005)
    RunCommonEvent(0, 90005251, args=(1037510200, 45.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1037510210, 1037510210, 40224, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1037510500, 1037510500, 40300, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 900005610, args=(1037511300, 100, 800, 39200514), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1037511301, 100, 800, 39200514), arg_types="IiiI")
    RunCommonEvent(0, 90005771, args=(1037510950, 1037512700), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1037512350(0, character=1037510800)
    Event_1037512301(0, 1037510800)


@RestartOnRest(1037512208)
def Event_1037512208(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 1037512208"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
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
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
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
    Wait(seconds)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(1037512301)
def Event_1037512301(_, character: uint):
    """Event 1037512301"""
    EndIfFlagEnabled(1037510810)
    IfCharacterHasSpecialEffect(MAIN, character, 14887)
    EnableFlag(1037510810)
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@RestartOnRest(1037512350)
def Event_1037512350(_, character: uint):
    """Event 1037512350"""
    GotoIfFlagEnabled(Label.L0, flag=1037510810)
    GotoIfFlagEnabled(Label.L0, flag=1037510800)
    GotoIfFlagEnabled(Label.L0, flag=1041520820)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHuman(AND_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1037512300)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Unknown_2004_73(entity=character, unk_4_8=1)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20019, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    End()
