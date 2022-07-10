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
    RegisterGrace(grace_flag=31120000, obj=31121950, unknown=5.0)
    Event_31122800()
    Event_31122810()
    Event_31122849()
    Event_31122811()
    RunCommonEvent(0, 900005610, args=(31121200, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005646,
        args=(31120800, 31122840, 31122841, 31121840, 31122840, 31, 12, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(31120201, 30000, 20000, 31122201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(31120213, 30000, 20000, 31122201, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(31120203, 30000, 20000, 31122204, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(31120214, 30000, 20000, 31122204, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(31120200, 31122203, 0.0, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31120211, 31122203, 0.0, 1700), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31120227, 31122205, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31120227, 31122220, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31120228, 31122205, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31120228, 31122220, 0.0, 0), arg_types="IIfi")


@RestartOnRest(31122800)
def Event_31122800():
    """Event 31122800"""
    EndIfFlagEnabled(31120800)
    IfHealthValueLessThanOrEqual(MAIN, 31120800, value=0)
    Wait(4.0)
    PlaySoundEffect(31120800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31120800)
    KillBossAndDisplayBanner(character=31120800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31120800)
    EnableFlag(9247)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61247)


@RestartOnRest(31122810)
def Event_31122810():
    """Event 31122810"""
    GotoIfFlagDisabled(Label.L0, flag=31120800)
    DisableCharacter(31120800)
    DisableAnimations(31120800)
    Kill(31120800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31120800)
    DisableAnimations(31120800)
    GotoIfFlagEnabled(Label.L1, flag=31120802)
    IfFlagEnabled(AND_1, 31122805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31122800)
    IfAttackedWithDamageType(OR_1, attacked_entity=31120800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31120800)
    EnableAnimations(31120800)
    SetNetworkUpdateRate(31120800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31120800, name=903460310)


@RestartOnRest(31122811)
def Event_31122811():
    """Event 31122811"""
    EndIfFlagEnabled(31120800)
    IfHealthLessThanOrEqual(AND_1, 31120800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31122802)


@RestartOnRest(31122849)
def Event_31122849():
    """Event 31122849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31120800, 31121800, 31122800, 31122805, 31125800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31120800, 31121800, 31122800, 31122805, 31122806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31120800, 31121800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31120800, 950000, 31122805, 31122806, 0, 31122802, 0, 0), arg_types="IiIIIIii")
