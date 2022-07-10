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
    RegisterGrace(grace_flag=301500, obj=30151950, unknown=5.0)
    RunCommonEvent(0, 900005610, args=(30151150, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005200,
        args=(30150300, 30000, 20000, 30152400, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30150301, 30000, 20000, 30152400, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30150302, 30000, 20000, 30152400, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30150200, 30152214, 0.0, 3028), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30150310, 30152310, 0.0, 3003), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(30150201, 30003, 20003, 30152213, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(30150303, 30000, 20000, 30152217, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30150304, 30000, 20000, 30152211, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30150305, 30000, 20000, 30152217, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30150306, 30000, 20000, 30152217, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30150307, 30152200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30150308, 30152200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30150309, 30152200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005650, args=(30150540, 30151540, 30151541, 30153541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30150540, 30151540), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30150570, 30151570), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30150571, 30151571), arg_types="II")
    Event_30152800()
    Event_30152810()
    Event_30152849()
    Event_30152811()
    RunCommonEvent(
        0,
        90005646,
        args=(30150800, 30152840, 30152841, 30151840, 30152840, 30, 15, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 91005600, args=(30152800, 30151695, 5), arg_types="IIi")


@RestartOnRest(30152520)
def Event_30152520(_, flag: uint, obj: uint, flag_1: uint):
    """Event 30152520"""
    EndIfFlagEnabled(flag)
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@RestartOnRest(30152800)
def Event_30152800():
    """Event 30152800"""
    EndIfFlagEnabled(30150800)
    IfHealthValueLessThanOrEqual(MAIN, 30150800, value=0)
    Wait(4.0)
    PlaySoundEffect(30150800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30150800)
    KillBossAndDisplayBanner(character=30150800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30150800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61215)
    EnableFlag(9215)


@RestartOnRest(30152810)
def Event_30152810():
    """Event 30152810"""
    GotoIfFlagDisabled(Label.L0, flag=30150800)
    DisableCharacter(30150800)
    DisableAnimations(30150800)
    Kill(30150800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30150800)
    IfFlagEnabled(AND_2, 30152805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30152800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(30150800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30150800, name=903664301)
    Wait(0.5)
    EnableAI(30150800)


@RestartOnRest(30152811)
def Event_30152811():
    """Event 30152811"""
    EndIfFlagEnabled(30150800)
    IfHealthLessThanOrEqual(AND_1, 30150800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30152802)


@RestartOnRest(30152849)
def Event_30152849():
    """Event 30152849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30150800, 30151800, 30152800, 30152805, 30155800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30150800, 30151800, 30152800, 30152805, 30152806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30150800, 30151800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30150800, 930000, 30152805, 30152806, 0, 30152802, 0, 0), arg_types="IiIIIIii")
