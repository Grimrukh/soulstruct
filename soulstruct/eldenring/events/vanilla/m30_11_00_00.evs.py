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
    RegisterGrace(grace_flag=73011, obj=30111950, unknown=5.0)
    Event_30112800()
    Event_30112810()
    Event_30112849()
    Event_30112811()
    RunCommonEvent(0, 90005616, args=(30117000, 30112700), arg_types="II")
    RunCommonEvent(0, 90005650, args=(30110540, 30111540, 30111541, 30113541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30110540, 30111540), arg_types="II")
    Event_30112580()
    RunCommonEvent(
        0,
        90005646,
        args=(30110800, 30112840, 30112841, 30111840, 30112840, 30, 11, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_30110790(0, 30111520, 30110800)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005211, args=(30110200, 30003, 20003, 30112200, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110201, 30003, 20003, 30112201, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110202, 30003, 20003, 30112202, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110203, 30003, 20003, 30112203, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110205, 30003, 20003, 30112205, 1.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110206, 30003, 20003, 30112205, 1.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30110207, 30003, 20003, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(30110208, 30003, 20003, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005211, args=(30110209, 30003, 20003, 30112209, 1.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110210, 30003, 20003, 30112209, 1.0, 5.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110211, 30003, 20003, 30112209, 1.0, 10.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110212, 30003, 20003, 30112209, 1.0, 15.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110213, 30003, 20003, 30112213, 0.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110214, 30003, 20003, 30112213, 0.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110215, 30003, 20003, 30112215, 3.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110216, 30003, 20003, 30112215, 3.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30110217, 30003, 20003, 30112217, 3.0, 8.5, 0, 0, 0, 0), arg_types="IiiIffIIII")


@NeverRestart(30112580)
def Event_30112580():
    """Event 30112580"""
    RegisterLadder(start_climbing_flag=30110580, stop_climbing_flag=30110581, obj=30111580)


@RestartOnRest(30110790)
def Event_30110790(_, obj: uint, flag: uint):
    """Event 30110790"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfThisEventSlotFlagDisabled(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    EnableObjectActivation(obj, obj_act_id=-1)
    End()


@RestartOnRest(30112800)
def Event_30112800():
    """Event 30112800"""
    EndIfFlagEnabled(30110800)
    IfHealthValueLessThanOrEqual(MAIN, 30110800, value=0)
    Wait(4.0)
    PlaySoundEffect(30110800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30110800)
    KillBossAndDisplayBanner(character=30110800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(30111670, obj_act_id=-1)
    EnableFlag(30110800)
    EnableFlag(9203)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61203)


@RestartOnRest(30112810)
def Event_30112810():
    """Event 30112810"""
    GotoIfFlagDisabled(Label.L0, flag=30110800)
    DisableCharacter(30110800)
    DisableAnimations(30110800)
    Kill(30110800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30110800)
    DisableHealthBar(30110800)
    DisableObjectActivation(30111670, obj_act_id=-1)
    ForceAnimation(30110800, 30000, unknown2=1.0)
    IfFlagEnabled(AND_2, 30112805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30112800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30110800)
    SetNetworkUpdateRate(30110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(30110800, 4404)
    Wait(1.0)
    EnableBossHealthBar(30110800, name=902100300)
    Wait(0.699999988079071)
    ForceAnimation(30110800, 20000, unknown2=1.0)


@RestartOnRest(30112811)
def Event_30112811():
    """Event 30112811"""
    EndIfFlagEnabled(30110800)
    IfHealthRatioLessThanOrEqual(AND_1, 30110800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30112802)


@RestartOnRest(30112849)
def Event_30112849():
    """Event 30112849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30110800, 30111800, 30112800, 30112805, 30115800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30110800, 30111800, 30112800, 30112805, 30112806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30110800, 30111800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30110800, 921500, 30112805, 30112806, 0, 30112802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30112900)
def Event_30112900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 30112900"""
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
