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
    RegisterGrace(grace_flag=31090000, obj=31091950, unknown=5.0)
    Event_31092800()
    Event_31092810()
    Event_31092849()
    Event_31092811()
    RunCommonEvent(0, 900005610, args=(31091200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005261, args=(31090200, 31092200, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(31090201, 30001, 20001, 31092201, 1.0, 1.399999976158142, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31090202, 30002, 20002, 31092201, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31090203, 30000, 20000, 31092201, 1.0, 1.600000023841858, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31090205, 30000, 20000, 31092201, 1.0, 1.7999999523162842, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31090214, 30002, 20002, 31092214, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31090215, 30002, 20002, 31092214, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31090218, 30001, 20001, 31092214, 1.0, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31090251, 30002, 20002, 31092214, 1.0, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(31090254, 31092254, 1.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31090256, 30002, 20002, 31092256, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    Event_31092301(0, 31090227, 1.0)
    Event_31092301(1, 31090258, 0.5)
    Event_31092301(2, 31090301, 1.0)
    RunCommonEvent(0, 90005261, args=(31090350, 31092350, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31092350()
    Event_31092351()
    Event_31092300()
    RunCommonEvent(
        0,
        90005646,
        args=(31090800, 31092840, 31092841, 31091840, 31092840, 31, 9, 0, 0),
        arg_types="IIIIIBBbb",
    )


@RestartOnRest(31092300)
def Event_31092300():
    """Event 31092300"""
    IfCharacterDead(OR_15, 31090300)
    EndIfConditionTrue(input_condition=OR_15)
    GotoIfUnknown_1004_05(Label.L0, character=31090300, unk_8_12=True)
    DisableAI(31090300)
    ForceAnimation(31090300, 30002, unknown2=1.0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090227, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090258, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090300, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090301, attacker=0)
    IfEntityWithinDistance(OR_1, entity=31090300, other_entity=PLAYER, radius=3.0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=31092301)
    IfCharacterHasSpecialEffect(AND_4, 31090300, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31090300, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31090300, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 31090300, 90160)
    IfCharacterHasSpecialEffect(AND_5, 31090300, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31090300, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31090300, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31090300, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 31090300, 90162)
    IfCharacterHasSpecialEffect(AND_6, 31090300, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31090300, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31090300, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31090300, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 31090300, 90161)
    IfCharacterHasSpecialEffect(AND_7, 31090300, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31090300, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31090300, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31090300, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 31090300, 90162)
    IfCharacterHasSpecialEffect(AND_8, 31090300, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31090300, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31090300, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 31090300, 90160)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(0.5)
    EnableAI(31090300)
    ForceAnimation(31090300, 20002, skip_transition=True, unknown2=1.0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=31090300, unk_4_8=1)


@RestartOnRest(31092301)
def Event_31092301(_, character: uint, seconds: float):
    """Event 31092301"""
    IfCharacterDead(OR_15, character)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    DisableAI(character)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090227, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090258, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090300, attacker=0)
    IfAttackedWithDamageType(OR_1, attacked_entity=31090301, attacker=0)
    IfObjectDestroyed(OR_1, 31091550)
    IfObjectDestroyed(OR_1, 31091551)
    IfObjectDestroyed(OR_1, 31091552)
    IfObjectDestroyed(OR_1, 31091553)
    IfObjectDestroyed(OR_1, 31091554)
    IfObjectDestroyed(OR_1, 31091555)
    IfObjectDestroyed(OR_1, 31091556)
    IfObjectDestroyed(OR_1, 31091557)
    IfObjectDestroyed(OR_1, 31091558)
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
    IfEntityWithinDistance(OR_1, entity=character, other_entity=PLAYER, radius=3.0)
    IfCharacterInsideRegion(OR_1, character=PLAYER, region=31092301)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(OR_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(seconds)
    EnableAI(character)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31092350)
def Event_31092350():
    """Event 31092350"""
    IfCharacterDead(AND_15, 31090350)
    EndIfConditionTrue(input_condition=AND_15)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 31090350, 8081)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=31092351)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(31090350, 8081)
    Restart()


@RestartOnRest(31092351)
def Event_31092351():
    """Event 31092351"""
    IfCharacterDead(AND_15, 31090350)
    EndIfConditionTrue(input_condition=AND_15)
    IfCharacterHasSpecialEffect(AND_1, 31090350, 8081)
    IfCharacterOutsideRegion(AND_1, character=PLAYER, region=31092351)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CancelSpecialEffect(31090350, 8081)
    Restart()


@RestartOnRest(31092800)
def Event_31092800():
    """Event 31092800"""
    EndIfFlagEnabled(31090800)
    IfHealthValueLessThanOrEqual(MAIN, 31090800, value=0)
    Wait(4.0)
    PlaySoundEffect(31090800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31090800)
    KillBossAndDisplayBanner(character=31090800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31090800)
    EnableFlag(9240)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61240)


@RestartOnRest(31092810)
def Event_31092810():
    """Event 31092810"""
    GotoIfFlagDisabled(Label.L0, flag=31090800)
    DisableCharacter(31090800)
    DisableAnimations(31090800)
    Kill(31090800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31090800)
    AddSpecialEffect(31090800, 8092)
    IfFlagEnabled(AND_2, 31092805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31092800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31090800)
    SetNetworkUpdateRate(31090800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31090800, name=904130310)


@RestartOnRest(31092811)
def Event_31092811():
    """Event 31092811"""
    EndIfFlagEnabled(31090800)
    IfHealthLessThanOrEqual(AND_1, 31090800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31092802)


@RestartOnRest(31092849)
def Event_31092849():
    """Event 31092849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31090800, 31091800, 31092800, 31092805, 31095800, 10010, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31090800, 31091800, 31092800, 31092805, 31092806, 10010), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31090800, 31091800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31090800, 931000, 31092805, 31092806, 0, 31092802, 0, 0), arg_types="IiIIIIii")
