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
    RegisterGrace(grace_flag=1043310000, obj=1043311950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76161, 76158, 1043311980, 77110, 3, 78110, 78111, 78112, 78113, 78114, 78115, 78116, 78117, 78118, 78119),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1043310001, obj=1043311951, unknown=5.0)
    RegisterGrace(grace_flag=1043310002, obj=1043311952, unknown=5.0)
    Event_1043312580()
    RunCommonEvent(0, 900005610, args=(1043311650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 90005250, args=(1043310205, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310206, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310207, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310208, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310209, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310212, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310213, 1043312200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310203, 1043312201, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310204, 1043312201, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310211, 1043312201, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310280, 1043312201, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310205, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310206, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310207, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310208, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310209, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310212, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310213, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310203, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310204, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310211, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310280, 1043312280, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310214, 1043312218, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310215, 1043312213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310216, 1043312213, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310218, 1043312218, 0.0, -1), arg_types="IIfi")
    Event_1043312443(0, character=1043310215, region=1043312213)
    Event_1043312443(1, character=1043310216, region=1043312213)
    Event_1043312443(2, character=1043310218, region=1043312213)
    RunCommonEvent(0, 90005250, args=(1043310217, 1043312213, 5.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310220, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310221, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310222, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310223, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310224, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310225, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310226, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310227, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310228, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(1043310245, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(1043310246, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(1043310267, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005271, args=(1043310268, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005250, args=(1043310281, 1043312250, 0.0, -1), arg_types="IIfi")
    Event_1043312443(3, character=1043310281, region=1043312250)
    RunCommonEvent(0, 90005271, args=(1043310252, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(1, 90005271, args=(1043310271, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(2, 90005271, args=(1043310272, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005251, args=(1043310255, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1043310256, 1043312256, 0.0, 3023), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310262, 1043312262, 1.0, 3031), arg_types="IIfi")
    Event_1043312443(4, character=1043310262, region=1043312262)
    RunCommonEvent(0, 90005271, args=(1043310264, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005250, args=(1043310285, 1043312285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310269, 1043312285, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310270, 1043312285, 0.0, -1), arg_types="IIfi")
    Event_1043312242(0, attacker__character=1043315240, region=1043312242)
    Event_1043312223(0, attacker__character=1043315223, region=1043312223)
    RunCommonEvent(0, 90005250, args=(1043310304, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310305, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310306, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310307, 1043312220, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310311, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310312, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310313, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310314, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310315, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310316, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005271, args=(1043310352, 0.0, -1), arg_types="Ifi")
    RunCommonEvent(0, 90005250, args=(1043310353, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310354, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310357, 1043312223, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310400, 1043312400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310401, 1043312400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310402, 1043312400, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310403, 1043312403, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005260, args=(1043310405, 1043312403, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(1043310420, 30005, 20005, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(1043310430, 30000, 20000, 1043312430, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1043310434, 1043312430, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310440, 1043312442, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1043310441, 1043312442, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1043310442, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(
        0,
        90005501,
        args=(1043310510, 1043310511, 3, 1043311510, 1043311511, 1043311512, 1043310512),
        arg_types="IIIIIII",
    )
    Event_1043312510()
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005695, args=(1043311600, 1043311600, 200, 0, 802001200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    RunCommonEvent(0, 90005706, args=(1043310700, 930023, 0), arg_types="IiI")
    RunCommonEvent(0, 90005704, args=(1043310705, 3401, 3400, 1043309201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1043310705, 3401, 3402, 1043309201, 3401, 3400, 3403, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1043310705, 3403, 3400, 3403), arg_types="IIII")
    Event_1043310705(0, character=1043310705, obj=1043311700)
    RunCommonEvent(0, 90005750, args=(1043311701, 4110, 110620, 400061, 400061, 1043319208, 0), arg_types="IiiIIIi")
    Event_1043310706()
    Event_1043310707(0, other_entity=1043310705)
    Event_1043310708()
    Event_1043312709(0, 1043310705, 1043311700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1043310700)
    DisableBackread(1043310705)
    Event_1043310519()


@RestartOnRest(1043312443)
def Event_1043312443(_, character: uint, region: uint):
    """Event 1043312443"""
    IfPlayerInOwnWorld(AND_1)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    AddSpecialEffect(character, 8080)
    Wait(0.4000000059604645)
    Restart()


@RestartOnRest(1043312242)
def Event_1043312242(_, attacker__character: uint, region: uint):
    """Event 1043312242"""
    CancelSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1043312240)
    AddSpecialEffect(attacker__character, 4800)
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
    EnableNetworkFlag(1043312240)
    CancelSpecialEffect(attacker__character, 4800)


@RestartOnRest(1043312223)
def Event_1043312223(_, attacker__character: uint, region: uint):
    """Event 1043312223"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5655)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1043312223)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5655)
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
    EnableNetworkFlag(1043312223)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5655)


@NeverRestart(1043312510)
def Event_1043312510():
    """Event 1043312510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            1043310510,
            1043310511,
            3,
            1043311510,
            1043311511,
            1043313511,
            1043311512,
            1043313512,
            1043312511,
            1043312512,
            1043310512,
            1043310513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(1043310519)
def Event_1043310519():
    """Event 1043310519"""
    EndIfThisEventSlotFlagEnabled()
    DisableFlag(1043310510)


@NeverRestart(1043312580)
def Event_1043312580():
    """Event 1043312580"""
    RegisterLadder(start_climbing_flag=1043310580, stop_climbing_flag=1043310851, obj=1043311580)
    RegisterLadder(start_climbing_flag=1043310582, stop_climbing_flag=1043310853, obj=1043311582)
    RegisterLadder(start_climbing_flag=1043310584, stop_climbing_flag=1043310855, obj=1043311584)
    RegisterLadder(start_climbing_flag=1043310586, stop_climbing_flag=1043310857, obj=1043311586)
    RegisterLadder(start_climbing_flag=1043310588, stop_climbing_flag=1043310859, obj=1043311588)
    RegisterLadder(start_climbing_flag=1043310590, stop_climbing_flag=1043310861, obj=1043311590)
    RegisterLadder(start_climbing_flag=1043310592, stop_climbing_flag=1043310863, obj=1043311592)
    End()


@RestartOnRest(1043313700)
def Event_1043313700(_, character: uint):
    """Event 1043313700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023, unknown2=1.0)
    End()


@RestartOnRest(1043310705)
def Event_1043310705(_, character: uint, obj: uint):
    """Event 1043310705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3400)
    DisableFlag(1043319202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3405)
    GotoIfFlagEnabled(Label.L7, flag=3407)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3405)
    IfFlagEnabled(OR_1, 3407)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3400)
    GotoIfFlagEnabled(Label.L1, flag=3401)
    GotoIfFlagEnabled(Label.L3, flag=3403)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100, unknown2=1.0)
    Move(character, destination=1043312700, destination_type=CoordEntityType.Region, short_move=True)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(1043319208)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_1, 3405)
    IfFlagDisabled(AND_1, 3407)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Restart()


@NeverRestart(1043310706)
def Event_1043310706():
    """Event 1043310706"""
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(OR_1, 1043319206)
    IfFlagEnabled(OR_1, 3403)
    IfFlagEnabled(AND_1, 3405)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3398)
    IfFlagEnabled(AND_2, 1043319206)
    IfFlagEnabled(AND_2, 1043300800)
    EndIfConditionFalse(input_condition=AND_2)
    EnableFlag(3418)


@NeverRestart(1043310707)
def Event_1043310707(_, other_entity: uint):
    """Event 1043310707"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyEnabled(flag_range=(3406, 3417))
    IfFlagEnabled(AND_1, 1043319206)
    IfFlagEnabled(AND_1, 3405)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=other_entity, radius=100.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3418)


@NeverRestart(1043310708)
def Event_1043310708():
    """Event 1043310708"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1043300800)
    IfFlagEnabled(AND_1, 1043300800)
    IfFlagEnabled(AND_1, 3406)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(3418)


@RestartOnRest(1043312709)
def Event_1043312709(_, character: uint, obj: uint):
    """Event 1043312709"""
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    IfFlagEnabled(OR_1, 3405)
    IfFlagEnabled(OR_1, 3407)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 9624)
    IfCharacterBackreadEnabled(AND_1, character)
    IfFlagEnabled(AND_1, 3401)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObjectInvulnerability(obj)
    DestroyObject(obj, request_slot=0)
