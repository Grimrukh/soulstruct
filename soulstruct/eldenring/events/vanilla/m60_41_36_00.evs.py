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
    RunCommonEvent(0, 900005610, args=(1041361680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005460, args=(1041360210,))
    RunCommonEvent(0, 90005461, args=(1041360210,))
    RunCommonEvent(0, 90005462, args=(1041360210,))
    RunCommonEvent(0, 90005460, args=(1041360211,))
    RunCommonEvent(0, 90005461, args=(1041360211,))
    RunCommonEvent(0, 90005462, args=(1041360211,))
    Event_1041362650(0, tutorial_param_id=1550, flag=710550)
    RunCommonEvent(
        0,
        90005725,
        args=(4730, 4731, 4733, 1041369205, 1041360700, 1041360701, 1041366700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1041360700, 4731, 4732, 1041369206, 4731, 4730, 4734, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041360700, 4731, 4730, 1041369206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1041360700, 4733, 4730, 4734), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1041360701, 4731, 4732, 1041369207, 4731, 4730, 4734, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1041360701, 4731, 4730, 1041369207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1041360701, 1041362706, 1041362707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4731, 1041360700, 1041360701, 4730, 4733), arg_types="IIIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1041360700)
    DisableBackread(1041360701)
    RunCommonEvent(0, 90005251, args=(1041360250, 80.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1041362650)
def Event_1041362650(_, tutorial_param_id: int, flag: uint):
    """Event 1041362650"""
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
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SW_SE)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1041363700)
def Event_1041363700(_, character: uint, character_1: uint, character_2: uint, obj: uint):
    """Event 1041363700"""
    WaitFrames(frames=1)
    DisableFlag(1041369200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(AND_10, 4740)
    IfFlagEnabled(AND_10, 1041369203)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1041369203)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    IfFlagEnabled(OR_1, 4745)
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4740)
    GotoIfFlagEnabled(Label.L2, flag=4741)
    GotoIfFlagEnabled(Label.L4, flag=4743)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    ForceAnimation(character, 30003, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableObject(obj)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableObject(obj)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 1041369200)
    Restart()


@RestartOnRest(1041363706)
def Event_1041363706(_, attacked_entity: uint):
    """Event 1041363706"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 1041362701)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1041362708)
    End()


@NeverRestart(1041363707)
def Event_1041363707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1041363707"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(first_flag)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    IfAttackedWithDamageType(AND_1, attacked_entity=character, attacker=20000)
    IfHealthValueLessThan(AND_1, character, value=1)
    IfConditionTrue(OR_2, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfFlagEnabled(OR_3, flag_2)
    IfAttackedWithDamageType(AND_3, attacked_entity=character_1, attacker=20000)
    IfHealthValueLessThan(AND_3, character_1, value=1)
    IfConditionTrue(OR_4, input_condition=OR_3)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfConditionTrue(OR_5, input_condition=OR_2)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20009, unknown2=1.0)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(MAIN, flag_2)
    DisableNetworkFlag(flag_2)
    End()
