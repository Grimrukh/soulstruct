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
    RegisterGrace(grace_flag=1045360000, obj=1045361950, unknown=5.0)
    RunCommonEvent(0, 90005460, args=(1045360211,))
    RunCommonEvent(0, 90005461, args=(1045360211,))
    RunCommonEvent(0, 90005462, args=(1045360211,))
    RunCommonEvent(0, 90005463, args=(1045362212, 1045360211), arg_types="II")
    RunCommonEvent(0, 90005464, args=(1045362212, 1045360211, 1045360212, 0), arg_types="IIII")
    RunCommonEvent(0, 90005464, args=(1045362212, 1045360211, 1045360213, 1), arg_types="IIII")
    RunCommonEvent(0, 90005464, args=(1045362212, 1045360211, 1045360214, 2), arg_types="IIII")
    RunCommonEvent(0, 90005464, args=(1045362212, 1045360211, 1045360215, 3), arg_types="IIII")
    RunCommonEvent(0, 90005464, args=(1045362212, 1045360211, 1045360216, 4), arg_types="IIII")
    Event_1045362200()
    Event_1045362400()
    RunCommonEvent(
        0,
        90005725,
        args=(4725, 4726, 4728, 1045369305, 1045360700, 1045360701, 1045366700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1045360700, 4726, 4727, 1045369306, 4726, 4725, 4729, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1045360700, 4726, 4725, 1045369306, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1045360700, 4728, 4725, 4729), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1045360701, 4726, 4727, 1045369307, 4726, 4725, 4729, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1045360701, 4726, 4725, 1045369307, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1045360701, 1045362706, 1045362707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4726, 1045360700, 1045360701, 4725, 4728), arg_types="IIIII")
    RunCommonEvent(0, 90005729, args=(1045369300, 1045360700, 40.0, 1045362702), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005725,
        args=(4725, 4726, 4728, 1045369305, 1045360702, 1045360703, 1045366701),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1045360702, 4726, 4727, 1045369306, 4726, 4725, 4729, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1045360702, 4726, 4725, 1045369306, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1045360702, 4728, 4725, 4729), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1045360703, 4726, 4727, 1045369307, 4726, 4725, 4729, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1045360703, 4726, 4725, 1045369307, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1045360703, 1045362706, 1045362707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4726, 1045360702, 1045360703, 4725, 4728), arg_types="IIIII")
    RunCommonEvent(0, 90005729, args=(1045369300, 1045360702, 40.0, 1045362702), arg_types="IIfI")
    RunCommonEvent(0, 90005706, args=(1045360710, 930023, 0), arg_types="IiI")
    Event_1045363704()
    RunCommonEvent(0, 90005706, args=(1045360710, 30023, 0), arg_types="IiI")
    Event_1045363715()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045360700)
    DisableBackread(1045360701)
    DisableBackread(1045360710)
    DisableBackread(1045360702)
    DisableBackread(1045360703)


@RestartOnRest(1045362200)
def Event_1045362200():
    """Event 1045362200"""
    AddSpecialEffect(1045360211, 11771)


@RestartOnRest(1045362400)
def Event_1045362400():
    """Event 1045362400"""
    EndIfFlagEnabled(1045360500)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 310)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1045362400)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1045360500)


@RestartOnRest(1045363700)
def Event_1045363700(_, character: uint, character_1: uint, character_2: uint, obj: uint):
    """Event 1045363700"""
    WaitFrames(frames=1)
    DisableFlag(1045369200)
    GotoIfPlayerNotInOwnWorld(Label.L0)

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
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, 1045369221)
    GotoIfConditionFalse(Label.L20, input_condition=AND_1)
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
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(1, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
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
    SkipLinesIfFlagDisabled(1, 4980)
    ForceAnimation(character, 30001, unknown2=1.0)
    SkipLinesIfFlagRangeAllDisabled(2, (4982, 4983))
    ForceAnimation(character, 30002, unknown2=1.0)
    DisableAI(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L20, flag=1045369222)
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
    IfFlagEnabled(MAIN, 1045369200)
    Restart()


@NeverRestart(1045363702)
def Event_1045363702(_, character: uint):
    """Event 1045363702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4743)
    EndIfFlagDisabled(1045369221)
    IfCharacterDead(MAIN, character)
    EnableNetworkFlag(1045369222)
    End()


@NeverRestart(1045363703)
def Event_1045363703(_, character: uint):
    """Event 1045363703"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4745)
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfFlagEnabled(OR_2, 4740)
    IfFlagEnabled(OR_2, 4741)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=4980)
    GotoIfFlagRangeAnyEnabled(Label.L10, flag_range=(4982, 4983))

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(OR_5, character, 9601)
    IfCharacterHasSpecialEffect(OR_5, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=9601)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=9603)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityWithinDistance(OR_6, entity=20000, other_entity=character, radius=4.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_6, character, 9601)
    IfConditionTrue(MAIN, input_condition=OR_6)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9601)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    IfEntityBeyondDistance(OR_7, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_7, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_7)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9603)
    ForceAnimation(character, 20010, unknown2=1.0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 10 --- #
    DefineLabel(10)
    IfCharacterHasSpecialEffect(OR_10, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_10)
    GotoIfCharacterHasSpecialEffect(Label.L11, character=character, special_effect=9603)

    # --- Label 11 --- #
    DefineLabel(11)
    IfEntityBeyondDistance(OR_11, entity=20000, other_entity=character, radius=6.0)
    IfCharacterDoesNotHaveSpecialEffect(OR_11, character, 9603)
    IfConditionTrue(MAIN, input_condition=OR_11)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=9603)
    ForceAnimation(character, 20011, unknown2=1.0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9603)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1045363704)
def Event_1045363704():
    """Event 1045363704"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045369229)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=1045360700, radius=7.5)
    EnableNetworkFlag(1045369229)
    End()


@RestartOnRest(1045363705)
def Event_1045363705(_, character: uint):
    """Event 1045363705"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 4745)
    IfFlagEnabled(OR_1, 4746)
    IfFlagEnabled(OR_1, 4747)
    IfFlagEnabled(OR_2, 4740)
    IfFlagEnabled(OR_2, 4741)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(AND_1, input_condition=OR_2)
    EndIfConditionFalse(input_condition=AND_1)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=9602)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, character, 9602)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(character)
    IfCharacterHasSpecialEffect(MAIN, character, 9602)
    Restart()


@RestartOnRest(1045363706)
def Event_1045363706(_, character: uint, attacked_entity: uint):
    """Event 1045363706"""
    EndIfPlayerNotInOwnWorld()
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=20000)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=40000)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 1041362709)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1041362708)
    EndIfFlagEnabled(4741)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9601)
    ForceAnimation(character, 20004, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=9602)
    ForceAnimation(character, 20006, unknown2=1.0)


@NeverRestart(1045363707)
def Event_1045363707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1045363707"""
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
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    IfFlagEnabled(MAIN, flag_2)
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1045363710)
def Event_1045363710(_, character: uint):
    """Event 1045363710"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023, unknown2=1.0)


@RestartOnRest(1045363715)
def Event_1045363715():
    """Event 1045363715"""
    DisableFlag(1044399265)
    SkipLinesIfFlagEnabled(1, 4728)
    EnableFlag(1044399265)
    End()
