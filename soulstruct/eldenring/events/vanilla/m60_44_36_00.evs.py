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
    RunCommonEvent(0, 9005810, args=(1044360800, 76120, 1044360950, 1044361950, 5.0), arg_types="IIIIf")
    Event_1044362800()
    Event_1044362810()
    Event_1044362849()
    RunCommonEvent(0, 90005300, args=(1044360220, 1044360220, 40112, 0.0, 0), arg_types="IIifi")
    Event_1044362500()
    RunCommonEvent(0, 90005704, args=(1044360700, 3461, 3460, 1044369201, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        1044363711,
        args=(1044360700, 3461, 3462, 1044369201, 0.6499999761581421, 3460, 3463, -1),
        arg_types="IIIIfIIi",
    )
    Event_1044363710(0, character=1044360700)
    Event_1044363712(0, entity=1044360700)
    Event_1044363713()
    Event_1044363714(0, entity=1044360700)
    RunCommonEvent(0, 90005709, args=(1044360700, 905, 603001), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1044360700, 200, 603051), arg_types="Iii")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044360700)
    DisableBackread(1044360710)
    RunCommonEvent(0, 90005251, args=(1044360250, 30.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044360231, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044360234, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044360235, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1044360211, 1044362211, 1.0, 0.0, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044360212, 1044362211, 1.0, 0.5, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044360213, 1044362211, 1.0, 0.30000001192092896, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044360214, 1044362211, 1.0, 0.699999988079071, 1701), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1044360200, 1044362200, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1044360200, 30014, 20014, 1044362200, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005421, args=(1044360300, 1044361301, 1044368301), arg_types="III")
    RunCommonEvent(0, 90005422, args=(1044368301, 1044361300, 1044363301), arg_types="III")
    RunCommonEvent(0, 90005424, args=(1044361300, 1044360302, 1044360303, 1044360300, 1044361301), arg_types="IIIII")
    RunCommonEvent(0, 90005423, args=(1044360302,))
    RunCommonEvent(0, 90005423, args=(1044360303,))
    Event_1044362300()


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(
        0,
        90005420,
        args=(1044360300, 1044361300, 1044361301, 1044360301, 1044360302, 1044360303, 0.0),
        arg_types="IIIIIIf",
    )


@RestartOnRest(1044362500)
def Event_1044362500():
    """Event 1044362500"""
    EnableObjectInvulnerability(1044361500)


@RestartOnRest(1044362300)
def Event_1044362300():
    """Event 1044362300"""
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=150,
        behavior_param_id=100700,
        target_type=DamageTargetType.Character,
        radius=3.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=200,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=201,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=202,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=203,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=204,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1044361301,
        obj=1044361300,
        model_point=205,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )


@RestartOnRest(1044362650)
def Event_1044362650(_, tutorial_param_id: int, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1044362650"""
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
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag_2, bit_count=1)


@RestartOnRest(1044362651)
def Event_1044362651(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1044362651"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=EAST_LIMGRAVE_SW_SW)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1044362652)
def Event_1044362652(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1044362652"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
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
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 9530)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=EAST_LIMGRAVE_SW_SW)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1044362654)
def Event_1044362654(_, tutorial_param_id: int, flag: uint):
    """Event 1044362654"""
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    IfPlayerHasWeapon(OR_15, 33000000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 33210000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 34000000, including_storage=True)
    IfPlayerHasWeapon(OR_15, 34040000, including_storage=True)
    EndIfConditionTrue(input_condition=OR_15)
    IfPlayerHasWeapon(OR_1, 33000000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 33210000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 34000000, including_storage=True)
    IfPlayerHasWeapon(OR_1, 34040000, including_storage=True)
    IfFlagDisabled(AND_1, flag)
    IfLeavingSession(AND_1)
    IfInsideMap(AND_1, game_map=EAST_LIMGRAVE_SW_SW)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    EndIfFlagEnabled(flag)
    Wait(1.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9101, flag=flag, bit_count=1)


@RestartOnRest(1044363700)
def Event_1044363700(
    _,
    character__obj: uint,
    character__obj_1: uint,
    character__obj_2: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044363700"""
    WaitFrames(frames=1)
    DisableFlag(flag)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(character__obj)
    EnableCharacter(character__obj_1)
    EnableObject(character__obj_2)
    EnableBackread(character__obj)
    EnableBackread(character__obj_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableCharacter(character__obj)
    DisableCharacter(character__obj_1)
    DisableObject(character__obj_2)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character__obj)
    DropMandatoryTreasure(character__obj_1)
    DisableCharacter(character__obj)
    DisableCharacter(character__obj_1)
    DisableObject(character__obj)
    DisableObject(character__obj_1)
    DisableObject(character__obj_2)
    DisableBackread(character__obj)
    DisableBackread(character__obj_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, flag)
    Restart()


@RestartOnRest(1044363701)
def Event_1044363701(_, flag: uint, flag_1: uint, flag_2: uint, first_flag: uint, last_flag: uint):
    """Event 1044363701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(flag)
    SkipLinesIfFlagEnabled(4, flag_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(first_flag)
    End()
    EndIfFlagEnabled(flag_2)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)


@RestartOnRest(1044363702)
def Event_1044363702(_, character: uint, flag: uint, first_flag: uint, flag_1: uint, last_flag: uint, flag_2: uint):
    """Event 1044363702"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, first_flag)
    IfFlagEnabled(AND_1, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)


@RestartOnRest(1044363710)
def Event_1044363710(_, character: uint):
    """Event 1044363710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3460)
    DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 3465)
    IfFlagDisabled(AND_1, 1044369231)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_2, 3465)
    IfFlagDisabled(AND_2, 1044369231)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3463)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90105, unknown2=1.0)
    DisableInvincibility(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(AND_5, 3465)
    IfFlagDisabled(AND_5, 1044369231)
    AwaitConditionFalse(AND_5)
    Restart()


@RestartOnRest(1044363711)
def Event_1044363711(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    value: float,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 1044363711"""
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(MAIN, 3000)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    DisableFlag(flag_2)
    IfFlagDisabled(AND_1, flag)
    IfFlagDisabled(AND_1, flag_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=40000)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfHealthLessThan(AND_2, character, value=value)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(OR_2, flag_2)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()


@RestartOnRest(1044363712)
def Event_1044363712(_, entity: uint):
    """Event 1044363712"""
    EndIfFlagEnabled(3461)
    AwaitFlagEnabled(flag=3461)
    ForceAnimation(entity, 90207, unknown2=1.0)
    End()


@RestartOnRest(1044363713)
def Event_1044363713():
    """Event 1044363713"""
    IfFlagEnabled(AND_1, 1044369236)
    IfFlagEnabled(AND_1, 1044369230)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    IfTrueFlagCountGreaterThanOrEqual(AND_2, FlagType.Absolute, flag_range=(100500, 100749), value=3)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1044369237)
    IfTrueFlagCountGreaterThanOrEqual(AND_3, FlagType.Absolute, flag_range=(100500, 100749), value=6)
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1044369235)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@NeverRestart(1044363714)
def Event_1044363714(_, entity: uint):
    """Event 1044363714"""
    EndIfFlagDisabled(3465)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 1044369231)
    IfEntityWithinDistance(AND_1, entity=entity, other_entity=20000, radius=50.0)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(3478)
    End()


@RestartOnRest(1044362800)
def Event_1044362800():
    """Event 1044362800"""
    EndIfFlagEnabled(1044360800)
    IfHealthValueLessThanOrEqual(MAIN, 1044360800, value=0)
    Wait(4.0)
    PlaySoundEffect(1044360800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1044360800)
    KillBossAndDisplayBanner(character=1044360800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(1044361560, obj_act_id=-1)
    EnableFlag(1044360800)


@RestartOnRest(1044362810)
def Event_1044362810():
    """Event 1044362810"""
    GotoIfFlagDisabled(Label.L0, flag=1044360800)
    DisableCharacter(1044360800)
    DisableAnimations(1044360800)
    Kill(1044360800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1044360800)
    IfFlagEnabled(AND_2, 1044362805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1044362800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(1044360800)
    SetNetworkUpdateRate(1044360800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1044360800, name=904340540)
    DisableObjectActivation(1044361560, obj_act_id=-1)


@RestartOnRest(1044362849)
def Event_1044362849():
    """Event 1044362849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1044360800, 1044361800, 1044362800, 1044362805, 1044365800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1044360800, 1044361800, 1044362800, 1044362805, 1044362806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1044360800, 1044361800, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1044360800, 920900, 1044362805, 1044362806, 0, 1044362802, 0, 0),
        arg_types="IiIIIIii",
    )
    RunCommonEvent(0, 9005812, args=(1044360800, 1044361801, 3, 0, 0), arg_types="IIiIi")
