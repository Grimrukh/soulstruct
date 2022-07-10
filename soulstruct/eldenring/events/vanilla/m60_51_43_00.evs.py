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
    RegisterGrace(grace_flag=1051430000, obj=1051431950, unknown=5.0)
    RunCommonEvent(0, 90005870, args=(1051430800, 904770600, 16), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1051430800, 0, 1051430800, 0, 30425, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1051430800, 16, 0), arg_types="III")
    Event_1051432209()
    Event_1051432200(0, 1051430800, 55.0, 0.0, -1)
    Event_1051430700(0, character=1051430700)
    RunCommonEvent(
        0,
        90005703,
        args=(1051430700, 3641, 3642, 1051439201, 1051439212, 3640, 3643, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1051430700, 1051439212, 3640, 1051439201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1051430700, 3643, 3640, 3643), arg_types="IIII")
    Event_1051430702(0, 1051430700, 0.8999999761581421)
    Event_1051430703(0, 1051430700)


@RestartOnRest(1051432200)
def Event_1051432200(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1051432200"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=radius)
    IfFlagDisabled(AND_1, 1051430210)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1051432209)
def Event_1051432209():
    """Event 1051432209"""
    EndIfPlayerNotInOwnWorld()
    IfEntityBeyondDistance(MAIN, entity=PLAYER, other_entity=1051430800, radius=160.0)
    DisableNetworkFlag(1051430210)


@RestartOnRest(1051430700)
def Event_1051430700(_, character: uint):
    """Event 1051430700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(2, 3640)
    DisableFlag(1051439202)
    DisableFlag(1051439212)
    IfFlagEnabled(OR_2, 3645)
    IfFlagEnabled(OR_2, 3647)
    IfTimeOfDay(AND_2, earliest=(20, 0, 0), latest=(5, 30, 0))
    IfEventValueGreaterThanOrEqual(AND_2, flag=1051439230, bit_count=5, value=1)
    IfConditionTrue(AND_2, input_condition=OR_2)
    GotoIfConditionFalse(Label.L4, input_condition=AND_2)
    DisableFlagRange((1051439240, 1051439249))
    EnableRandomFlagInRange(flag_range=(1051439240, 1051439249))
    SkipLinesIfFlagEnabled(1, 1051439220)
    SkipLinesIfFlagDisabled(1, 1051439240)
    EnableNetworkFlag(1051432703)

    # --- Label 4 --- #
    DefineLabel(4)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3645)
    GotoIfFlagEnabled(Label.L6, flag=3646)
    GotoIfFlagEnabled(Label.L7, flag=3647)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3645)
    IfFlagEnabled(OR_3, 3646)
    IfFlagEnabled(OR_3, 3647)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3640)
    GotoIfFlagEnabled(Label.L1, flag=3641)
    GotoIfFlagEnabled(Label.L3, flag=3643)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    SkipLinesIfFlagDisabled(2, 1051432704)
    ForceAnimation(character, 930016, unknown2=1.0)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(3, 1051432703)
    ForceAnimation(character, 930015, unknown2=1.0)
    Move(
        character,
        destination=1051432700,
        destination_type=CoordEntityType.Region,
        model_point=900,
        copy_draw_parent=character,
    )
    Goto(Label.L20)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 20034, unknown2=1.0)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3645)
    IfFlagEnabled(OR_4, 3647)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=3640)
    GotoIfFlagEnabled(Label.L1, flag=3641)
    GotoIfFlagEnabled(Label.L2, flag=3642)
    GotoIfFlagEnabled(Label.L3, flag=3643)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 20034, unknown2=1.0)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3646)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1051430701)
def Event_1051430701(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 1051430701"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(flag_2)
    IfFlagDisabled(AND_1, flag_3)
    IfFlagEnabled(AND_1, first_flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=character, attacker=40000)
    IfHealthGreaterThanOrEqual(AND_4, character, value=1.0)
    SkipLinesIfConditionFalse(2, AND_4)
    IfHealthLessThan(AND_2, character, value=0.6499999761581421)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_5, character, value=0.8999999761581421)
    SkipLinesIfConditionFalse(2, AND_5)
    IfHealthLessThan(AND_2, character, value=0.550000011920929)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_6, character, value=0.800000011920929)
    SkipLinesIfConditionFalse(2, AND_6)
    IfHealthLessThan(AND_2, character, value=0.44999998807907104)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_7, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_7)
    IfHealthLessThan(AND_2, character, value=0.3499999940395355)
    Goto(Label.L10)
    IfHealthGreaterThanOrEqual(AND_8, character, value=0.699999988079071)
    SkipLinesIfConditionFalse(2, AND_8)
    IfHealthLessThan(AND_2, character, value=0.25)
    Goto(Label.L10)
    IfHealthLessThan(AND_2, character, value=0.15000000596046448)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    IfConditionTrue(AND_2, input_condition=OR_1)
    IfFlagEnabled(OR_2, flag_2)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfHealthGreaterThan(AND_3, character, value=0.0)
    IfConditionTrue(AND_3, input_condition=OR_2)
    IfFlagEnabled(OR_3, flag_3)
    IfFlagDisabled(OR_3, first_flag)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_4)
    RestartIfFinishedConditionTrue(input_condition=OR_3)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 20034, unknown2=1.0)
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
    Restart()


@RestartOnRest(1051430702)
def Event_1051430702(_, character: uint, value: float):
    """Event 1051430702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3643)
    IfFlagEnabled(AND_1, 3642)
    IfHealthLessThanOrEqual(AND_1, character, value=value)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(character, 20039, unknown2=1.0)
    WaitFrames(frames=1)
    RestartIfCharacterDoesNotHaveSpecialEffect(character=character, special_effect=9663)
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3643))
    EnableNetworkFlag(3640)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableFlag(1051439212)
    SaveRequest()
    Wait(8.0)
    DisableFlag(1051439212)
    SaveRequest()


@RestartOnRest(1051430703)
def Event_1051430703(_, character: uint):
    """Event 1051430703"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 3647)
    IfEventValueGreaterThanOrEqual(AND_1, flag=1051439235, bit_count=5, value=9)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1051439212)
    EnableInvincibility(character)


@RestartOnRest(1051433705)
def Event_1051433705(_, character: uint):
    """Event 1051433705"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3641)
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3644))
    EnableNetworkFlag(3640)
    SaveRequest()
    DisableNetworkFlag(1051439201)
    SetTeamType(character, TeamType.FriendlyNPC)
    End()


@RestartOnRest(1051433706)
def Event_1051433706(_, flag: uint):
    """Event 1051433706"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3643)
    EndIfFlagDisabled(1051439224)
    DisableNetworkConnectedFlagRange(flag_range=(3640, 3644))
    EnableNetworkFlag(3642)
    SaveRequest()
    EnableFlag(flag)
    End()


@RestartOnRest(1051433707)
def Event_1051433707(_, flag: uint, flag_1: uint):
    """Event 1051433707"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3643)
    EndIfFlagDisabled(3645)
    DisableFlag(flag_1)
    IfFlagEnabled(AND_1, 1051439225)
    IfFlagDisabled(AND_1, 1051439227)
    EndIfConditionFalse(input_condition=AND_1)
    EnableFlag(flag_1)
    EnableFlag(flag)
    End()


@RestartOnRest(1051433708)
def Event_1051433708(
    _,
    item: int,
    item_1: int,
    item_2: int,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    last_flag: uint,
):
    """Event 1051433708"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3643)
    EndIfFlagDisabled(3645)
    GotoIfFlagEnabled(Label.L1, flag=1051439226)
    GotoIfFlagEnabled(Label.L1, flag=1051439219)
    IfPlayerDoesNotHaveGood(AND_1, item)
    IfPlayerDoesNotHaveGood(AND_1, item_1)
    IfPlayerDoesNotHaveGood(AND_1, item_2)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    IfPlayerHasGood(AND_2, item)
    IfPlayerDoesNotHaveGood(AND_2, item_1)
    IfPlayerDoesNotHaveGood(AND_2, item_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    IfPlayerDoesNotHaveGood(AND_3, item)
    IfPlayerHasGood(AND_3, item_1)
    IfPlayerDoesNotHaveGood(AND_3, item_2)
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    IfPlayerDoesNotHaveGood(AND_4, item)
    IfPlayerDoesNotHaveGood(AND_4, item_1)
    IfPlayerHasGood(AND_4, item_2)
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(first_flag)
    IfPlayerHasGood(OR_5, item)
    IfPlayerHasGood(OR_5, item_1)
    IfPlayerHasGood(OR_5, item_2)
    IfConditionTrue(AND_5, input_condition=OR_5)
    IfFlagDisabled(AND_5, 1051439226)
    IfFlagDisabled(AND_5, 1051439219)
    IfConditionTrue(MAIN, input_condition=AND_5)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    IfFlagEnabled(OR_6, 1051439226)
    IfFlagEnabled(OR_6, 1051439219)
    IfPlayerDoesNotHaveGood(OR_6, item)
    IfPlayerHasGood(OR_6, item_1)
    IfPlayerHasGood(OR_6, item_2)
    IfConditionTrue(MAIN, input_condition=OR_6)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    IfFlagEnabled(OR_7, 1051439226)
    IfFlagEnabled(OR_7, 1051439219)
    IfPlayerHasGood(OR_7, item)
    IfPlayerDoesNotHaveGood(OR_7, item_1)
    IfPlayerHasGood(OR_7, item_2)
    IfConditionTrue(MAIN, input_condition=OR_7)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_2)
    IfFlagEnabled(OR_8, 1051439226)
    IfFlagEnabled(OR_8, 1051439219)
    IfPlayerHasGood(OR_8, item)
    IfPlayerHasGood(OR_8, item_1)
    IfPlayerDoesNotHaveGood(OR_8, item_2)
    IfConditionTrue(MAIN, input_condition=OR_8)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(last_flag)
    IfPlayerDoesNotHaveGood(AND_9, item)
    IfPlayerDoesNotHaveGood(AND_9, item_1)
    IfPlayerDoesNotHaveGood(AND_10, item)
    IfPlayerDoesNotHaveGood(AND_10, item_2)
    IfPlayerDoesNotHaveGood(AND_11, item_1)
    IfPlayerDoesNotHaveGood(AND_11, item_2)
    IfFlagEnabled(OR_12, 1051439226)
    IfFlagEnabled(OR_12, 1051439219)
    IfConditionTrue(OR_12, input_condition=AND_9)
    IfConditionTrue(OR_12, input_condition=AND_10)
    IfConditionTrue(OR_12, input_condition=AND_11)
    IfConditionTrue(MAIN, input_condition=OR_12)
    Restart()
