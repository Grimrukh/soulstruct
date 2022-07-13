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
    RegisterGrace(grace_flag=311700, obj=31171950, unknown=5.0)
    Event_31172800()
    Event_31172499()
    Event_31172810()
    Event_31172811()
    Event_31172849()
    RunCommonEvent(
        0,
        90005646,
        args=(31170800, 31172840, 31172841, 31171840, 31172840, 31, 17, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_31172500()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31170200, 31172200, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31170201, 30005, 20005, 31172204, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170203, 30001, 20001, 31172204, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170204, 30004, 20004, 31172204, 2.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170212, 30001, 20001, 31172212, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170213, 30004, 20004, 31172212, 2.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170216, 30000, 20000, 31172216, 2.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170217, 30001, 20001, 31172216, 2.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_31172216(0, character=31170216)
    Event_31172216(1, character=31170217)
    RunCommonEvent(0, 90005211, args=(31170218, 30001, 20001, 31172218, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170245, 30001, 20001, 31172245, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_31172208(7, character=31170203)
    Event_31172208(8, character=31170204)
    RunCommonEvent(0, 90005211, args=(31170207, 30003, 20003, 31172207, 1.5, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170219, 30003, 20003, 31172219, 1.5, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170220, 30003, 20003, 31172220, 1.5, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_31172218(3, 31170240, 31172240, 4.0, 0.0, 3001)
    RunCommonEvent(0, 90005261, args=(31170250, 31172250, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170254, 31172250, 2.0, 2.0, 0), arg_types="IIffi")
    Event_31172254()
    RunCommonEvent(0, 90005211, args=(31170251, 30000, 20000, 31172251, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170252, 30000, 20000, 31172252, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31170253, 30000, 20000, 31172252, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31170258, 31172258, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31170259, 30000, 20000, 31172258, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31170260, 31172260, 2.0, 5.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170261, 31172260, 2.0, 10.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170300, 31172300, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170301, 31172300, 2.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170302, 31172302, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170303, 31172302, 2.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170308, 31172308, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170309, 31172309, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31170310, 31172309, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31170340, 30002, 20002, 31172340, 3.0, 0.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005460, args=(31170340,))
    RunCommonEvent(0, 90005461, args=(31170340,))
    RunCommonEvent(0, 90005462, args=(31170340,))


@RestartOnRest(31172500)
def Event_31172500():
    """Event 31172500"""
    DisableObject(31171500)


@RestartOnRest(31172208)
def Event_31172208(_, character: uint):
    """Event 31172208"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=4.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31172216)
def Event_31172216(_, character: uint):
    """Event 31172216"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=3.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31172218)
def Event_31172218(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31172218"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=radius)
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
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
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


@RestartOnRest(31172254)
def Event_31172254():
    """Event 31172254"""
    AddSpecialEffect(31170254, 10525)


@RestartOnRest(31172499)
def Event_31172499():
    """Event 31172499"""
    EndIfFlagEnabled(31170800)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=31172390)
    IfAttackedWithDamageType(OR_1, attacked_entity=31170800, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=31170800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31170800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31170800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31170800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=31170800, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(31172499)


@RestartOnRest(31172800)
def Event_31172800():
    """Event 31172800"""
    EndIfFlagEnabled(31170800)
    IfHealthValueLessThanOrEqual(MAIN, 31170800, value=0)
    Wait(4.0)
    PlaySoundEffect(31170800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31170800)
    KillBossAndDisplayBanner(character=31170800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31170800)
    EnableFlag(9235)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61235)


@RestartOnRest(31172810)
def Event_31172810():
    """Event 31172810"""
    GotoIfFlagDisabled(Label.L0, flag=31170800)
    DisableCharacter(31170800)
    DisableAnimations(31170800)
    Kill(31170800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31170800)
    SetLockOnPoint(character=31170800, lock_on_model_point=220, state=False)
    IfFlagEnabled(AND_2, 31172805)
    IfFlagEnabled(AND_2, 31172499)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(31170801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31170800)
    SetNetworkUpdateRate(31170800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31170800, name=904660310)
    SetLockOnPoint(character=31170800, lock_on_model_point=220, state=True)


@RestartOnRest(31172811)
def Event_31172811():
    """Event 31172811"""
    EndIfFlagEnabled(31170800)
    IfHealthRatioLessThanOrEqual(AND_1, 31170800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31172802)


@RestartOnRest(31172849)
def Event_31172849():
    """Event 31172849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31170800, 31171800, 31172800, 31172805, 31175800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31170800, 31171800, 31172800, 31172805, 31172806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31170800, 31171800, 5, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(31170800, 931000, 31172805, 31172806, 31172499, 31172802, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(31172900)
def Event_31172900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31172900"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(700690)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 700690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    EnableFlag(700690)
