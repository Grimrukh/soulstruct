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
    RegisterGrace(grace_flag=31050000, obj=31051950, unknown=5.0)
    Event_31052800()
    Event_31052810()
    Event_31052849()
    Event_31052811()
    Event_31052830(0, flag=31050801, character=31050100)
    RunCommonEvent(
        0,
        90005646,
        args=(31050800, 31052840, 31052841, 31051840, 31052840, 31, 5, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(31051550, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31050200, 31052200, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(31050201, 2.0, 0.0, 1700), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(31050203, 31052203, 2.0, 0.0, 1700), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31050205, 30002, 20002, 31052205, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31050206, 30001, 20001, 31052205, 2.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31050209, 30002, 20002, 31052209, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31050230, 31052230, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050251, 31052251, 5.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050254, 31052254, 2.0, 0.0, 3005), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050257, 31052257, 2.0, 0.0, 3003), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050280, 31052280, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050300, 31052300, 2.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050301, 31052301, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31052301()
    RunCommonEvent(0, 90005261, args=(31050302, 31052300, 2.0, 0.10000000149011612, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31050304, 30000, 20000, 31052305, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31050305, 30000, 20000, 31052305, 2.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31050306, 30000, 20000, 31052305, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31050307, 30000, 20000, 31052305, 2.0, 0.699999988079071, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31050308, 30000, 20000, 31052305, 2.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31050309, 30000, 20000, 31052305, 2.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31050310, 30000, 20000, 31052305, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31050315, 31052315, 2.0, 0.0, 3012), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050316, 31052316, 2.0, 0.0, 3012), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31050317, 31052317, 2.0, 0.0, 3012), arg_types="IIffi")


@RestartOnRest(31052301)
def Event_31052301():
    """Event 31052301"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(31050301, 8081)
    AddSpecialEffect(31050301, 8082)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfEntityWithinDistance(AND_1, entity=31050301, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfHasAIStatus(OR_2, 31050301, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(OR_2, attacked_entity=31050301, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(31050301, 8081)
    CancelSpecialEffect(31050301, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31052800)
def Event_31052800():
    """Event 31052800"""
    EndIfFlagEnabled(31050800)
    IfHealthValueLessThanOrEqual(MAIN, 31050800, value=0)
    Wait(4.0)
    PlaySoundEffect(31050800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31050800)
    KillBossAndDisplayBanner(character=31050800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31050800)
    EnableFlag(9237)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61237)


@RestartOnRest(31052810)
def Event_31052810():
    """Event 31052810"""
    GotoIfFlagDisabled(Label.L0, flag=31050800)
    DisableCharacter(31050800)
    DisableAnimations(31050800)
    Kill(31050800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(31050800)
    GotoIfFlagEnabled(Label.L1, flag=31050801)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31052801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(31050801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 31052805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31052800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(31050800)
    Wait(1.0)
    EnableAI(31050800)
    SetNetworkUpdateRate(31050800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(31050800, 3013, unknown2=1.0)
    EnableBossHealthBar(31050800, name=904290310)


@RestartOnRest(31052811)
def Event_31052811():
    """Event 31052811"""
    EndIfFlagEnabled(31050800)
    IfHealthRatioLessThanOrEqual(AND_1, 31050800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31052802)


@RestartOnRest(31052830)
def Event_31052830(_, flag: uint, character: uint):
    """Event 31052830"""
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31052849)
def Event_31052849():
    """Event 31052849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31050800, 31051800, 31052800, 31052805, 31055800, 10000, 31050801, 31052801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31050800, 31051800, 31052800, 31052805, 31052806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31050800, 31051800, 5, 31050801), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(31050800, 31051801, 3, 31050801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31050800, 931000, 31052805, 31052806, 0, 31052802, 0, 0), arg_types="IiIIIIii")
