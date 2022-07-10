"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1038422200(0, character=1038420200)
    Event_1038422200(1, character=1038420201)
    Event_1038422200(2, character=1038420202)
    Event_1038422200(3, character=1038420210)
    Event_1038422200(4, character=1038420211)
    Event_1038422200(5, character=1038420212)
    Event_1038422230(0, character=1038420220, region=1038422230, flag=1038422220)
    Event_1038422230(1, character=1038420221, region=1038422230, flag=1038422221)
    Event_1038422230(2, character=1038420222, region=1038422230, flag=1038422222)
    Event_1038422230(3, character=1038420223, region=1038422230, flag=1038422223)
    Event_1038422230(4, character=1038420224, region=1038422230, flag=1038422224)
    Event_1038422230(5, character=1038420225, region=1038422230, flag=1038422225)
    Event_1038422230(6, character=1038420226, region=1038422231, flag=1038422226)
    Event_1038422230(7, character=1038420227, region=1038422231, flag=1038422227)
    Event_1038422230(8, character=1038420228, region=1038422231, flag=1038422228)
    Event_1038422230(9, character=1038420229, region=1038422231, flag=1038422229)
    Event_1038422230(10, character=1038420230, region=1038422231, flag=1038422230)
    Event_1038422240()
    Event_1038422580()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(1038420240, 1038422240, 30.0, 0.0, 0), arg_types="IIffi")


@RestartOnRest(1038422200)
def Event_1038422200(_, character: uint):
    """Event 1038422200"""
    Kill(character)
    End()


@RestartOnRest(1038422230)
def Event_1038422230(_, character: uint, region: uint, flag: uint):
    """Event 1038422230"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_1, input_condition=OR_2)
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
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableNetworkFlag(flag)
    Unknown_2004_83(character=character, unk_4_8=1)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ForceAnimation(character, 30004, unknown2=1.0)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004, unknown2=1.0)
    End()


@RestartOnRest(1038422240)
def Event_1038422240():
    """Event 1038422240"""
    IfCharacterDead(OR_15, 1038420240)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(1038420240, 8089)
    End()


@NeverRestart(1038422580)
def Event_1038422580():
    """Event 1038422580"""
    RegisterLadder(start_climbing_flag=1038420580, stop_climbing_flag=1038420581, obj=1038421580)
    RegisterLadder(start_climbing_flag=1038420582, stop_climbing_flag=1038420583, obj=1038421582)
    RegisterLadder(start_climbing_flag=1038420584, stop_climbing_flag=1038420585, obj=1038421584)
