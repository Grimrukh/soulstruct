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
    RegisterGrace(grace_flag=31040000, obj=31041950, unknown=5.0)
    Event_31042800()
    Event_31042810()
    Event_31042849()
    Event_31042811()
    RunCommonEvent(
        0,
        90005646,
        args=(31040800, 31042840, 31042841, 31041840, 31042840, 31, 4, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31040200, 31042200, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040205, 31042205, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040206, 31042205, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040207, 31042207, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040208, 31042207, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040209, 31042207, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040211, 31042211, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040212, 31042212, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040216, 31042216, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040217, 31042216, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(31040219, 1.5, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(31040220, 1.5, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(31040221, 1.5, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(31040222, 1.5, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(31040223, 31042223, 1.5, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(31040219, 1.5, 0.0, 1701), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(31040250, 31042250, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31040253, 30001, 20001, 31042207, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31040254, 30001, 20001, 31042207, 2.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31040257, 30001, 20001, 31042257, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31040260, 31042260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040261, 31042260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040262, 31042260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040263, 31042260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31040264, 31042260, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31040275, 30001, 20001, 31042275, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31040276, 30001, 20001, 31042275, 2.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31040277, 30001, 20001, 31042275, 2.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31040278, 30001, 20001, 31042275, 2.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(31040279, 30001, 20001, 31042275, 2.0, 0.699999988079071, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31040300, 30000, 20000, 31042300, 2.0, 10.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31040310, 31042310, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31040311, 30000, 20000, 31042311, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31040312, 31042312, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31040318, 30000, 20000, 31042318, 2.0, 0.0, 2, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31040319, 30000, 20000, 31042318, 2.0, 0.30000001192092896, 2, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31040320, 30000, 20000, 31042318, 2.0, 0.5, 2, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31040323, 30000, 20000, 31042323, 2.0, 5.0, 1, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31040324, 30000, 20000, 31042323, 2.0, 5.199999809265137, 1, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    Event_31042310(0, character=31040300)
    Event_31042310(1, character=31040310)
    Event_31042310(2, character=31040311)
    Event_31042310(3, character=31040312)
    Event_31042310(4, character=31040318)
    Event_31042310(5, character=31040319)
    Event_31042310(6, character=31040320)
    Event_31042310(7, character=31040323)
    Event_31042310(8, 31040324)


@RestartOnRest(31042310)
def Event_31042310(_, character: uint):
    """Event 31042310"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31042800)
def Event_31042800():
    """Event 31042800"""
    EndIfFlagEnabled(31040800)
    IfHealthValueLessThanOrEqual(MAIN, 31040800, value=0)
    Wait(4.0)
    PlaySoundEffect(31040800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31040800)
    KillBossAndDisplayBanner(character=31040800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31040800)
    EnableFlag(9236)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61236)


@RestartOnRest(31042810)
def Event_31042810():
    """Event 31042810"""
    GotoIfFlagDisabled(Label.L0, flag=31040800)
    DisableCharacter(31040800)
    DisableAnimations(31040800)
    Kill(31040800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31040800)
    AddSpecialEffect(31040800, 90000)
    ForceAnimation(31040800, 30001, unknown2=1.0)
    IfFlagEnabled(AND_2, 31042805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31042800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    ForceAnimation(31040800, 20001, unknown2=1.0)
    EnableAI(31040800)
    SetNetworkUpdateRate(31040800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31040800, name=903800310)


@RestartOnRest(31042811)
def Event_31042811():
    """Event 31042811"""
    EndIfFlagEnabled(31040800)
    IfHealthLessThanOrEqual(AND_1, 31040800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31042802)


@RestartOnRest(31042849)
def Event_31042849():
    """Event 31042849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31040800, 31041800, 31042800, 31042805, 31045800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31040800, 31041800, 31042800, 31042805, 31042806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31040800, 31041800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31040800, 931000, 31042805, 31042806, 0, 31042802, 0, 0), arg_types="IiIIIIii")
