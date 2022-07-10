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
    RegisterGrace(grace_flag=1047580000, obj=1047581950, unknown=5.0)
    Event_1047583500(0, region=1047582710)
    Event_1047583700(0, character=1047580705, character_1=1047580710, obj=1047581701)
    Event_1047583701(0, character=1047580705, entity=1047581700)
    Event_1047583702(0, character=1047580705)
    Event_1047583703(0, character=1047580705)
    Event_1047583704(0, entity=1047580705)
    RunCommonEvent(0, 90005750, args=(1047581701, 4350, 104110, 400411, 400411, 1047589210, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005708, args=(1047580710, 6001, 0), arg_types="III")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005451, args=(1247580400, 1247586420), arg_types="II")
    RunCommonEvent(0, 90005452, args=(1247580400, 1247580400), arg_types="II")
    RunCommonEvent(0, 90005454, args=(1247580400, 1247582400, 1247580400), arg_types="III")
    RunCommonEvent(0, 90005458, args=(1247580400, 1247581401), arg_types="II")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581420, 101, 0.0), arg_types="IIif")
    RunCommonEvent(1, 90005453, args=(1247580400, 1247581421, 102, 0.10000000149011612), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581422, 103, 0.20000000298023224), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581423, 104, 0.30000001192092896), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581424, 105, 0.4000000059604645), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581425, 106, 0.5), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581426, 107, 0.6000000238418579), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581427, 108, 0.699999988079071), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581428, 109, 0.800000011920929), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581429, 110, 0.8999999761581421), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581430, 111, 1.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581436, 117, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581437, 118, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581438, 119, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581439, 120, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581440, 121, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581441, 122, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581442, 123, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581443, 124, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581444, 125, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581445, 126, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581446, 127, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581447, 128, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581452, 133, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581453, 134, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581454, 135, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581455, 136, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581456, 137, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581457, 138, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581458, 139, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581459, 140, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581460, 141, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581461, 142, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581468, 149, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581469, 150, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581470, 151, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581471, 152, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581472, 153, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581473, 154, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581474, 155, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581475, 156, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581476, 157, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581477, 158, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005453, args=(1247580400, 1247581478, 159, 0.0), arg_types="IIif")
    RunCommonEvent(0, 90005456, args=(1247580400, 1247581410, 1247581418, 1247580400), arg_types="IIII")
    Event_1247582350(0, 1247580400, 1247582400)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1047580700)
    DisableBackread(1047580705)


@RestartOnRest(1047583500)
def Event_1047583500(_, region: uint):
    """Event 1047583500"""
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfFailedToCreateSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(OR_2, character=20000, region=region)
    IfFailedToCreateSession(OR_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    CancelSpecialEffect(20000, 9621)
    Restart()


@RestartOnRest(1047583700)
def Event_1047583700(_, character: uint, character_1: uint, obj: uint):
    """Event 1047583700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    EnableBackread(character_1)
    EnableCharacter(character_1)
    EnableCharacterCollision(character_1)
    DisableGravity(character_1)
    SetTeamType(character_1, TeamType.NoTeam)
    ForceAnimation(character_1, 930009, unknown2=1.0)
    MoveObjectToCharacter(obj, character=character)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4100)
    DisableFlag(1036419203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4106)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 4106)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4100)
    GotoIfFlagEnabled(Label.L2, flag=4101)
    GotoIfFlagEnabled(Label.L3, flag=4102)
    GotoIfFlagEnabled(Label.L4, flag=4103)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.NoTeam)
    ForceAnimation(character, 930011, unknown2=1.0)
    SkipLinesIfFlagDisabled(1, 1047582700)
    EnableCharacter(character)
    SkipLinesIfFlagDisabled(1, 1047582701)
    ForceAnimation(character, 930013, unknown2=1.0)
    SkipLinesIfFlagDisabled(2, 1047589205)
    DisableBackread(character)
    DisableCharacter(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_4, 4106)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1047583701)
def Event_1047583701(_, character: uint, entity: uint):
    """Event 1047583701"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1047589205)
    EndIfFlagEnabled(1047582700)
    SkipLinesIfPlayerInOwnWorld(2)
    IfFlagEnabled(MAIN, 1047582700)
    Goto(Label.L1)
    IfActionButtonParamActivated(AND_1, action_button_id=6340, entity=entity)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 90008, unknown2=1.0)
    EnableNetworkFlag(1047582700)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.5)
    EnableCharacter(character)
    ForceAnimation(character, 20025, unknown2=1.0)
    End()


@RestartOnRest(1047583702)
def Event_1047583702(_, character: uint):
    """Event 1047583702"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1047589205)
    IfFlagEnabled(MAIN, 1047589205)
    Wait(30.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1047583703)
def Event_1047583703(_, character: uint):
    """Event 1047583703"""
    EndIfPlayerNotInOwnWorld()
    WaitFrames(frames=1)
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1047589210)
    SkipLinesIfFlagEnabled(1, 1047589205)
    IfCharacterHasSpecialEffect(MAIN, character, 9600)
    EnableFlag(1047589210)
    End()


@RestartOnRest(1047583704)
def Event_1047583704(_, entity: uint):
    """Event 1047583704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(4100)
    EndIfFlagDisabled(4106)
    EndIfFlagEnabled(1047589205)
    EndIfFlagEnabled(1047582700)
    IfFlagEnabled(MAIN, 1047582701)
    Wait(3.5)
    ForceAnimation(entity, 20019, unknown2=1.0)
    End()


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005450, args=(1247580400, 1247581400, 1247581410, 1247581418), arg_types="IIII")


@RestartOnRest(1247582350)
def Event_1247582350(_, character: uint, region: uint):
    """Event 1247582350"""
    EndIfFlagEnabled(1247580400)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=10.0)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(1247580400)
    AICommand(character, command_id=10, command_slot=0)
    EnableFlag(1247582350)
    Wait(9.0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Wait(1.0)
    Restart()
