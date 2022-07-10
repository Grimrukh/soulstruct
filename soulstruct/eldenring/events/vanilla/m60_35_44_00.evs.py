"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1035442650(0, flag=710680, tutorial_param_id=1680, item=9124, flag_1=69240)
    Event_1035443700(0, character=1053440700, obj=1035441701)
    Event_1035443701(0, character=1053440700)
    RunCommonEvent(0, 90005704, args=(1053440700, 3181, 3180, 1035449201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1053440700, 3181, 3182, 1035449201, 3181, 3180, 3184, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1053440700, 3183, 3180, 3184), arg_types="IIII")
    RunCommonEvent(
        0,
        90005740,
        args=(
            1035442705,
            1035442706,
            1035442707,
            1053440700,
            700,
            1035441700,
            700,
            0.20000000298023224,
            90201,
            -1,
            -1,
            1.100000023841858,
        ),
        arg_types="IIIIiIhfiiif",
    )
    RunCommonEvent(
        0,
        90005741,
        args=(1035442708, 1035442709, 1035442707, 1053440700, 90203, 0, -1, -1, 0.5),
        arg_types="IIIIiIiif",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1053440700)
    RunCommonEvent(0, 90005261, args=(1035440200, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035440201, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035440202, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035440203, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035440204, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035440210, 1035442210, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1035440220, 30000, 20000, 1035442220, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1035442650)
def Event_1035442650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 1035442650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(flag)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(1035443700)
def Event_1035443700(_, character: uint, obj: uint):
    """Event 1035443700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3180)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3188)
    GotoIfFlagEnabled(Label.L5, flag=3189)
    GotoIfFlagEnabled(Label.L5, flag=3190)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(OR_3, 3188)
    IfFlagEnabled(OR_3, 3189)
    IfFlagEnabled(OR_3, 3190)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableObject(obj)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

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
    DisableObject(obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 3188)
    IfFlagEnabled(OR_4, 3189)
    IfFlagEnabled(OR_4, 3190)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1035443701)
def Event_1035443701(_, character: uint):
    """Event 1035443701"""
    EndIfFlagEnabled(3181)
    EndIfFlagEnabled(3183)
    IfCharacterHasSpecialEffect(OR_1, character, 90)
    IfFlagEnabled(OR_1, 3181)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfCharacterHasSpecialEffect(character=character, special_effect=90)
    ForceAnimation(character, 90205, unknown2=1.0)
    End()
