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
    RunCommonEvent(
        0,
        90005646,
        args=(30040800, 30042840, 30042841, 30041840, 30042840, 30, 4, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=300400, obj=30041950, unknown=5.0)
    Event_30042800()
    Event_30042810()
    Event_30042849()
    Event_30042811()
    RunCommonEvent(0, 90005650, args=(30040540, 30041540, 30041541, 30043541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30040540, 30041540), arg_types="II")
    Event_30042500()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(30040200, 30001, 20001, 30042200, 0.0, 1, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040201, 30002, 20002, 30042201, 1.0, 1, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040202, 30010, 20010, 30042202, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040205, 30010, 20010, 30042205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040206, 30010, 20010, 30042205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(30040207, 30042207, 1.0, 0.0, 3004), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(30040210, 30010, 20010, 30042210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040211, 30010, 20010, 30042210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30040212, 30003, 20003, 30042212, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@NeverRestart(30040050)
def Event_30040050():
    """Event 30040050"""
    EndIfThisEventSlotFlagEnabled()


@NeverRestart(30042500)
def Event_30042500():
    """Event 30042500"""
    SkipLinesIfFlagDisabled(2, 57)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001070, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001060, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001050, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001040, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001030, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001020, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 51)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001010, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        90005660,
        args=(30040600, 30041600, 30042600, 801001000, 30042601, 30042602, 30042603),
        arg_types="IIIiIII",
    )
    SkipLinesIfFlagDisabled(2, 57)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001070, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(19)
    SkipLinesIfFlagDisabled(2, 56)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001060, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(16)
    SkipLinesIfFlagDisabled(2, 55)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001050, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(13)
    SkipLinesIfFlagDisabled(2, 54)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001040, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(10)
    SkipLinesIfFlagDisabled(2, 53)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001030, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(7)
    SkipLinesIfFlagDisabled(2, 52)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001020, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 51)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001010, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )
    SkipLines(1)
    RunCommonEvent(
        0,
        90005660,
        args=(30040605, 30041605, 30042605, 801001000, 30042606, 30042607, 30042608),
        arg_types="IIIiIII",
    )


@RestartOnRest(30042650)
def Event_30042650(_, tutorial_param_id: int, flag: uint):
    """Event 30042650"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(OR_1, 215000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 240000, including_storage=True)
    IfPlayerHasGood(OR_1, 243000, including_storage=True)
    IfPlayerHasGood(OR_1, 234000, including_storage=True)
    IfPlayerHasGood(OR_1, 244000, including_storage=True)
    IfPlayerHasGood(OR_1, 236000, including_storage=True)
    IfPlayerHasGood(OR_1, 232000, including_storage=True)
    IfPlayerHasGood(OR_1, 212000, including_storage=True)
    IfPlayerHasGood(OR_1, 241000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 233000, including_storage=True)
    IfPlayerHasGood(OR_1, 245000, including_storage=True)
    IfLeavingSession(AND_1)
    IfPlayerDoesNotHaveGood(AND_1, 9111, including_storage=True)
    IfInsideMap(AND_1, game_map=MURKWATER_CATACOMBS)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(30042800)
def Event_30042800():
    """Event 30042800"""
    EndIfFlagEnabled(30040800)
    IfHealthValueLessThanOrEqual(MAIN, 30040800, value=0)
    Wait(4.0)
    PlaySoundEffect(30040800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30040800)
    KillBossAndDisplayBanner(character=30040800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30040800)
    EnableFlag(9204)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61204)


@RestartOnRest(30042810)
def Event_30042810():
    """Event 30042810"""
    GotoIfFlagDisabled(Label.L0, flag=30040800)
    DisableCharacter(30040800)
    DisableAnimations(30040800)
    Kill(30040800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30040800)
    IfFlagEnabled(AND_2, 30042805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30042800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(30040801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30040800)
    SetNetworkUpdateRate(30040800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30040800, name=903400300)


@RestartOnRest(30042811)
def Event_30042811():
    """Event 30042811"""
    EndIfFlagEnabled(30040800)
    IfHealthRatioLessThanOrEqual(AND_1, 30040800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30042802)


@RestartOnRest(30042849)
def Event_30042849():
    """Event 30042849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30040800, 30041800, 30042800, 30042805, 30045800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30040800, 30041800, 30042800, 30042805, 30042806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30040800, 30041800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30040800, 930000, 30042805, 30042806, 0, 30042802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30042900)
def Event_30042900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 30042900"""
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
