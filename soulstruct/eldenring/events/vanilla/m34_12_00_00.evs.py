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
    RegisterGrace(grace_flag=34120000, obj=34121950, unknown=5.0)
    RegisterGrace(grace_flag=34120001, obj=34121951, unknown=5.0)
    RegisterGrace(grace_flag=34120002, obj=34121952, unknown=5.0)
    Event_34122800()
    Event_34122810()
    Event_34122811()
    Event_34122849()
    Event_34122510()
    Event_34122515()
    RunCommonEvent(
        0,
        90005501,
        args=(34120510, 34120511, 0, 34121510, 34121511, 34121512, 34120512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34120515, 34121515, 0, 34121515, 34121516, 34121517, 34120516),
        arg_types="IIIIIII",
    )
    Event_34122580()
    RunCommonEvent(
        0,
        90005646,
        args=(34120800, 34122840, 34122841, 34121840, 34122840, 34, 12, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(34121680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005560, args=(34120650, 34121650, 0), arg_types="IIi")
    RunCommonEvent(0, 90005525, args=(34120590, 34121590), arg_types="II")
    RunCommonEvent(0, 90005525, args=(34120591, 34121591), arg_types="II")
    RunCommonEvent(0, 90005525, args=(34120592, 34121592), arg_types="II")
    RunCommonEvent(0, 90005525, args=(34120593, 34121593), arg_types="II")
    RunCommonEvent(0, 90005525, args=(34120594, 34121594), arg_types="II")
    RunCommonEvent(
        0,
        90005110,
        args=(194, 9122, 34121599, 34120500, 8151, 806936, 9083, 60523, 0),
        arg_types="IIIiiiiii",
    )
    Event_32012200(0, 34120301, 30000, 20000, 16572, 0.0, 0, 0, 0, 0, 34121600, 34121601, 0, 0)
    Event_32012200(1, 34120302, 30002, 20002, 16574, 0.0, 0, 0, 0, 0, 34121602, 0, 0, 0)
    Event_32012200(2, 34120303, 30000, 20000, 16572, 0.0, 0, 0, 0, 0, 34121603, 34121604, 0, 0)
    Event_32012200(3, 34120304, 30000, 20000, 16572, 0.0, 0, 0, 0, 0, 34121610, 0, 0, 0)
    Event_34122400(0, 34120200, 34122200)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_34120519()
    RunCommonEvent(0, 90005250, args=(34120203, 34122201, 0.5, 3020), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(34120203, 2.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(34120210, 34122210, 8.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(34120211, 34122211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120212, 34122211, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(34120213, 16.0, 0.0, 3020), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(34120215, 34122210, 0.5, 3020), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(34120216, 34122216, 15.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(34120250, 34122250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120251, 34122250, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120255, 34122255, 0.20000000298023224, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120256, 34122255, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120257, 34122255, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120258, 34122258, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120259, 34122258, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120260, 34122260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120261, 34122261, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120262, 34122263, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120263, 34122263, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120264, 34122263, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(34120265, 34122265, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005260, args=(34120266, 34122265, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005260, args=(34120267, 34122265, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(34120268, 34122268, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120270, 34122270, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120271, 34122270, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120272, 34122270, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120273, 34122270, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120300, 34122300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120305, 34122305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(34120350, 34122350, 0.0, -1), arg_types="IIfi")


@NeverRestart(34122510)
def Event_34122510():
    """Event 34122510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            34120510,
            34120511,
            0,
            34121510,
            34121511,
            34123511,
            34121512,
            34123512,
            34122511,
            34122512,
            34120512,
            34120513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34122515)
def Event_34122515():
    """Event 34122515"""
    RunCommonEvent(
        0,
        90005507,
        args=(
            34120515,
            34121515,
            0,
            34121515,
            34121516,
            34122518,
            34121517,
            34122519,
            34122516,
            34122517,
            34120516,
            34122517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34120519)
def Event_34120519():
    """Event 34120519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(34120510)
    DisableThisSlotFlag()


@RestartOnRest(34122580)
def Event_34122580():
    """Event 34122580"""
    RegisterLadder(start_climbing_flag=34120530, stop_climbing_flag=34120531, obj=34121530)


@RestartOnRest(32012200)
def Event_32012200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    obj: uint,
    obj_1: uint,
    obj_2: uint,
    obj_3: uint,
):
    """Event 32012200"""
    EndIfThisEventSlotFlagEnabled()
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfObjectDestroyed(OR_10, obj)
    IfObjectDestroyed(OR_10, obj_1)
    IfObjectDestroyed(OR_10, obj_2)
    IfObjectDestroyed(OR_10, obj_3)
    IfConditionTrue(AND_1, input_condition=OR_10)
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
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(34122400)
def Event_34122400(_, character: uint, region: uint):
    """Event 34122400"""
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 8081)
    CancelSpecialEffect(character, 8082)
    Wait(0.4000000059604645)
    Restart()


@RestartOnRest(34122800)
def Event_34122800():
    """Event 34122800"""
    EndIfFlagEnabled(34120800)
    IfHealthValueLessThanOrEqual(MAIN, 34120800, value=0)
    Wait(4.0)
    PlaySoundEffect(34128500, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 34120800)
    KillBossAndDisplayBanner(character=34120800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(34120800)
    EnableFlag(9264)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61264)


@RestartOnRest(34122810)
def Event_34122810():
    """Event 34122810"""
    GotoIfFlagDisabled(Label.L0, flag=34120800)
    DisableCharacter(34120800)
    DisableAnimations(34120800)
    Kill(34120800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34120800)
    GotoIfFlagEnabled(Label.L1, flag=34120801)
    DisableCharacter(34120800)
    ForceAnimation(34120800, 30000, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34122801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=34120800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(34120801)
    EnableCharacter(34120800)
    ForceAnimation(34120800, 20000, skip_transition=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 34122805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=34122800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34120800)
    SetNetworkUpdateRate(34120800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34120800, name=903600320)


@RestartOnRest(34122811)
def Event_34122811():
    """Event 34122811"""
    EndIfFlagEnabled(34120800)
    IfHealthRatioLessThanOrEqual(AND_1, 34120800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(34122802)


@RestartOnRest(34122849)
def Event_34122849():
    """Event 34122849"""
    RunCommonEvent(
        0,
        9005800,
        args=(34120800, 34121800, 34122800, 34122805, 34125800, 10000, 34120801, 34122801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(34120800, 34121800, 34122800, 34122805, 34122806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(34120800, 34121800, 3, 34120801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(34120800, 931000, 34122805, 34122806, 0, 34122802, 0, 0), arg_types="IiIIIIii")
    RunCommonEvent(0, 9005811, args=(34120800, 34121801, 3, 34120801), arg_types="IIiI")
