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
    RegisterGrace(grace_flag=310300, obj=31031950, unknown=5.0)
    Event_31032800()
    Event_31032810()
    Event_31032811()
    Event_31032849()
    RunCommonEvent(
        0,
        90005646,
        args=(31030800, 31032840, 31032841, 31031840, 31032840, 31, 3, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005261, args=(31030202, 31032202, 2.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(31030210, 30000, 20000, 31032210, 6.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(31030211, 30005, 20005, 31032210, 8.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(31030216, 30001, 20001, 31032216, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")


@RestartOnRest(31032650)
def Event_31032650(_, tutorial_param_id: int, flag: uint):
    """Event 31032650"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(AND_5, 250, including_storage=True)
    EndIfConditionTrue(input_condition=AND_5)
    IfPlayerHasGood(AND_1, 250, including_storage=True)
    IfLeavingSession(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9115, flag=flag, bit_count=1)


@RestartOnRest(31032651)
def Event_31032651(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31032651"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)


@RestartOnRest(31032800)
def Event_31032800():
    """Event 31032800"""
    EndIfFlagEnabled(31030800)
    IfHealthValueLessThanOrEqual(MAIN, 31030800, value=0)
    Wait(4.0)
    PlaySoundEffect(31030800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 31030800)
    KillBossAndDisplayBanner(character=31030800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31030800)
    EnableFlag(9233)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61233)
    Wait(5.0)
    AwardItemLot(20330, host_only=True)
    End()


@RestartOnRest(31032810)
def Event_31032810():
    """Event 31032810"""
    GotoIfFlagDisabled(Label.L0, flag=31030800)
    DisableCharacter(31030800)
    DisableAnimations(31030800)
    Kill(31030800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31030800)
    DisableAnimations(31030800)
    ForceAnimation(31030800, 30003, unknown2=1.0)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31032800)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(31030801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31030800)
    EnableAnimations(31030800)
    SetNetworkUpdateRate(31030800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31030800, name=903970310)
    Wait(1.0)
    ForceAnimation(31030800, 20003, unknown2=1.0)


@RestartOnRest(31032811)
def Event_31032811():
    """Event 31032811"""
    EndIfFlagEnabled(31030800)
    IfHealthLessThanOrEqual(AND_1, 31030800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(31032802)


@RestartOnRest(31032849)
def Event_31032849():
    """Event 31032849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31030800, 31031800, 31032800, 31032805, 31035800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31030800, 31031800, 31032800, 31032805, 31032806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31030800, 31031800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31030800, 931000, 31032805, 31032806, 0, 31032802, 0, 0), arg_types="IiIIIIii")
