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
    RegisterGrace(grace_flag=1044350000, obj=1044351950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76161, 76106, 1044351980, 77110, 0, 78110, 78111, 78112, 78113, 78114, 78115, 78116, 78117, 78118, 78119),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005880,
        args=(1044350800, 1044350805, 1044352800, 1044350800, 30130, 60, 44, 35, 0, 1044352805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1044350800, 1044350805, 1044352801, 1044352802, 20300, 1044351805, 60, 44, 35, 0, 1044352805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1044350800,
            1044350805,
            1044352800,
            1044350800,
            1044352806,
            1044355810,
            1044351800,
            1044350810,
            1044352810,
            904290520,
            -1,
            20021,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1044350800, 1044350805, 1044351805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1044350800, 0, 1044352806, 1044352807, 0, 1), arg_types="IiIIii")
    RunCommonEvent(
        0,
        90005390,
        args=(1035430270, 1035432270, 1035430270, 1035430280, 1, 1044350100),
        arg_types="IIIIii",
    )
    RunCommonEvent(0, 90005391, args=(1035430270, 1035432270, 1035430270, 1035430280, 1), arg_types="IIIIi")
    RunCommonEvent(0, 90005701, args=(1044350720, 3981, 3982, 1044359301, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005700,
        args=(1044350720, 3981, 3982, 1044359301, 0.6499999761581421, 3980, 3983, -1),
        arg_types="IIIIfIIi",
    )
    RunCommonEvent(0, 90005702, args=(1044350720, 3983, 3980, 3983), arg_types="IIII")
    Event_1044353720(0, character__obj=1044350720)
    Event_1044352740(0, character=1044350710, character_1=1044350705)
    RunCommonEvent(
        0,
        90005780,
        args=(1044350800, 1044352160, 1044352161, 1044350702, 20, 1044352720, 1044349257, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1044350800, 1044352160, 1044352161, 1044350702), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1044350800, 1044352160, 1044352161, 1044350702, 1044352720, 0, 0),
        arg_types="IIIIIIi",
    )
    Event_1044352600(0, attacked_entity=1044351600, region=1044352600)
    Event_1044352650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    Event_1044350710(0, character=1044350700, character_1=1044350701)
    RunCommonEvent(0, 90005704, args=(1044350700, 3601, 3600, 1044359251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1044350700, 3601, 3602, 1044359251, 3603, 3600, 3603, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1044350700, 3603, 3600, 3604), arg_types="IIII")
    Event_1044350715(0, character=1044350700, character_1=1044350701)
    RunCommonEvent(0, 90005730, args=(1044359257, 20.0, 1044359265, 3615, 1044359255, 1044359256), arg_types="IfIIII")
    RunCommonEvent(0, 90005731, args=(1044359265, 1044350701, 30.0, 50.0), arg_types="IIff")
    Event_1044350711()
    Event_1044350713()
    Event_1044350712(0, 1044350703)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044350700)
    DisableBackread(1044350701)
    Event_1044352250()
    RunCommonEvent(0, 90005251, args=(1044350200, 5.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044350201, 5.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044350202, 5.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044350203, 5.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044350230, 15.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1044350231, 15.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1044350220, 1044352220, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005251, args=(1044350221, 55.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1044352250)
def Event_1044352250():
    """Event 1044352250"""
    Kill(1044350250)
    Kill(1044350251)


@RestartOnRest(1044352600)
def Event_1044352600(_, attacked_entity: uint, region: uint):
    """Event 1044352600"""
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacked_entity, attacker=0)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1, unknown2=1.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(1044352650)
def Event_1044352650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044352650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=EAST_WEEPING_PENINSULA_NW_NW)
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


@RestartOnRest(1044352740)
def Event_1044352740(_, character: uint, character_1: uint):
    """Event 1044352740"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)


@RestartOnRest(1044350710)
def Event_1044350710(_, character: uint, character_1: uint):
    """Event 1044350710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(1044359252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L15, flag=3615)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(MAIN, 3615)
    Restart()

    # --- Label 15 --- #
    DefineLabel(15)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L5, flag=1044350715)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetCharacterTalkRange(character=character_1, distance=100.0)
    Goto(Label.L20)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    ForceAnimation(character, 930010, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L5, flag=1044350715)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3615)
    Restart()


@RestartOnRest(1044350711)
def Event_1044350711():
    """Event 1044350711"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1044350800)
    IfFlagEnabled(AND_1, 3605)
    IfFlagEnabled(AND_1, 1044352800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1044352717)
    EnableFlag(3618)


@RestartOnRest(1044350712)
def Event_1044350712(_, character: uint):
    """Event 1044350712"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(MAIN, 1044352160)
    SetCharacterTalkRange(character=character, distance=100.0)
    EnableFlag(1044352715)


@RestartOnRest(1044350713)
def Event_1044350713():
    """Event 1044350713"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1044350800)
    IfFlagEnabled(MAIN, 1044350800)
    EndIfFlagDisabled(1044352160)
    EnableFlag(1044349258)


@RestartOnRest(1044350714)
def Event_1044350714(_, character: uint):
    """Event 1044350714"""
    DisableCharacter(character)
    IfFlagDisabled(AND_1, 1044350800)
    IfFlagEnabled(AND_1, 3605)
    IfFlagEnabled(AND_1, 3600)
    EndIfConditionTrue(input_condition=AND_1)
    DisableBackread(character)
    End()


@RestartOnRest(1044350715)
def Event_1044350715(_, character: uint, character_1: uint):
    """Event 1044350715"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1044359260)
    IfFlagEnabled(AND_1, 3615)
    IfFlagEnabled(AND_1, 1044359260)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    WaitFrames(frames=1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetCharacterTalkRange(character=character_1, distance=17.0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 20039, unknown2=1.0)
    End()


@NeverRestart(1044353720)
def Event_1044353720(_, character__obj: uint):
    """Event 1044353720"""
    WaitFrames(frames=1)
    DisableFlag(1044359300)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3980)
    IfFlagEnabled(AND_1, 1044352720)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1044352720)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3980)
    GotoIfFlagEnabled(Label.L2, flag=3981)
    GotoIfFlagEnabled(Label.L4, flag=3983)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    ForceAnimation(character__obj, 30003, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character__obj)
    EnableBackread(character__obj)
    SetTeamType(character__obj, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character__obj)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(MAIN, 1044359300)
    Restart()
