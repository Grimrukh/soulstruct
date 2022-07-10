"""
linked:
0
84
156
238

strings:
0: N:\\GR\\data\\Param\\event\\common_macro.emevd
84: N:\\GR\\data\\Param\\event\\common.emevd
156: N:\\GR\\data\\Param\\event\\common_func.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043350000, obj=1043351950, unknown=5.0)
    Event_1043352270(0, attacker__character=1043355270, region=1043352270)
    Event_1043350652(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    Event_1043353750(0, character=1043350700, character_1=1043350703)
    RunCommonEvent(0, 90005704, args=(1043350710, 3621, 3620, 1043359251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1043350710, 3621, 3622, 1043359251, 3621, 3620, 3624, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1043350710, 1043359259, 1043359259, 1043359259), arg_types="IIII")
    Event_1043353710(0, character=1043350710)
    Event_1043353711(0, 1043350710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043350710)
    Event_1043352200()


@RestartOnRest(1043352200)
def Event_1043352200():
    """Event 1043352200"""
    DropMandatoryTreasure(1043355200)


@RestartOnRest(1043352270)
def Event_1043352270(_, attacker__character: uint, region: uint):
    """Event 1043352270"""
    EnableNetworkSync()
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5653)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1043352270)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5653)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1043352270)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5653)


@RestartOnRest(1043350652)
def Event_1043350652(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1043350652"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=WEST_WEEPING_PENINSULA_NE_NE)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1043353710)
def Event_1043353710(_, character: uint):
    """Event 1043353710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3620)
    DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    IfFlagDisabled(OR_1, 1043369200)
    IfFlagEnabled(OR_1, 1043360800)
    IfFlagEnabled(AND_1, 3626)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagDisabled(OR_3, 1043369200)
    IfFlagEnabled(OR_3, 1043360800)
    IfFlagEnabled(AND_3, 3626)
    IfConditionTrue(AND_3, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_4, 1043369200)
    IfFlagEnabled(OR_4, 1043360800)
    IfFlagEnabled(AND_4, 3626)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionFalse(MAIN, input_condition=AND_4)
    Restart()


@RestartOnRest(1043353711)
def Event_1043353711(_, character: uint):
    """Event 1043353711"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1044389209)
    EndIfFlagEnabled(1035469209)
    EndIfFlagEnabled(1039529209)
    GotoIfFlagEnabled(Label.L1, flag=1043359259)
    IfFlagEnabled(MAIN, 1043359259)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    EndIfFlagEnabled(3626)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1043353750)
def Event_1043353750(_, character: uint, character_1: uint):
    """Event 1043353750"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    DisableCharacter(1043350701)
    DisableCharacter(1043350702)
    DisableBackread(1043350701)
    DisableBackread(1043350702)
    DisableAI(1043350701)
    DisableAI(1043350702)
