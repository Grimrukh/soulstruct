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
    RunCommonEvent(0, 90005600, args=(76307, 1040541950, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005100,
        args=(71602, 76307, 1040541980, 77350, 0, 78350, 78351, 78352, 78353, 78354, 78355, 78356, 78357, 78358, 78359),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1040540500, 1040540500, 40312, 0.0, 0), arg_types="IIifi")
    Event_1040542700(0, character=1040540705)
    RunCommonEvent(0, 90005704, args=(1040540705, 4201, 4200, 1040549201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1040540705, 4201, 4202, 1040549201, 4201, 4200, 4204, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1040540705, 4203, 4200, 4204), arg_types="IIII")
    Event_1040542705(0, character=1040540700)
    Event_1040542706(0, character=1040540700)
    RunCommonEvent(0, 90005706, args=(1040540710, 30023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1040540700)
    DisableBackread(1040540705)
    DisableBackread(1040540710)
    RunCommonEvent(0, 90005261, args=(1040540270, 1040542270, 20.0, 0.0, 0), arg_types="IIffi")
    Event_1040542201(0, character=1040540250, patrol_information_id=1040543250)
    Event_1040542201(1, character=1040540251, patrol_information_id=1040543251)
    Event_1040542201(2, character=1040540252, patrol_information_id=1040543252)
    Event_1040542201(3, character=1040540253, patrol_information_id=1040543253)
    Event_1040542201(4, character=1040540254, patrol_information_id=1040543254)
    RunCommonEvent(0, 90005201, args=(1040540350, 30005, 20005, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1040540340, 0.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1040540402, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005424, args=(1040541300, 1040540302, 1040540303, 1040540300, 1040541301), arg_types="IIIII")
    Event_1040542301()
    RunCommonEvent(0, 90005423, args=(1040540302,))
    RunCommonEvent(0, 90005423, args=(1040540303,))
    Event_1040542300()
    Event_1040542210(0, character=1040540330, patrol_information_id=1040542330)
    Event_1040542210(1, character=1040540310, patrol_information_id=1040542310)
    Event_1040542210(2, character=1040540311, patrol_information_id=1040542311)
    Event_1040542210(3, character=1040540312, patrol_information_id=1040542312)
    Event_1040542210(4, character=1040540313, patrol_information_id=1040542313)
    Event_1040542210(5, character=1040540314, patrol_information_id=1040542314)
    Event_1040542210(6, character=1040540315, patrol_information_id=1040542315)
    Event_1040542210(7, 1040540316, 1040542316)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(
        0,
        90005420,
        args=(1040540300, 1040541300, 1040541301, 1040540301, 1040540302, 1040540303, 0.0),
        arg_types="IIIIIIf",
    )


@RestartOnRest(1040542201)
def Event_1040542201(_, character: uint, patrol_information_id: uint):
    """Event 1040542201"""
    EndIfFlagEnabled(1040542201)
    IfCharacterInsideRegion(MAIN, character=1040540301, region=1040542301)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(1040542201)
    End()


@RestartOnRest(1040542210)
def Event_1040542210(_, character: uint, patrol_information_id: uint):
    """Event 1040542210"""
    EndIfFlagEnabled(1040542210)
    IfCharacterInsideRegion(MAIN, character=1040540301, region=1040542309)
    AddSpecialEffect(1040540301, 5555)
    Wait(1.0)
    AddSpecialEffect(character, 5002)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(1040542210)
    End()


@RestartOnRest(1040542300)
def Event_1040542300():
    """Event 1040542300"""
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=150,
        behavior_param_id=100700,
        target_type=DamageTargetType.Character,
        radius=3.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=200,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=201,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=202,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=203,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=204,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        obj_flag=1040541301,
        obj=1040541300,
        model_point=205,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )


@RestartOnRest(1040542301)
def Event_1040542301():
    """Event 1040542301"""
    EndIfFlagEnabled(1040542301)
    IfCharacterDead(MAIN, 1040540390)
    AwaitConditionTrue(MAIN)
    Kill(1040540301)
    End()


@RestartOnRest(1040542700)
def Event_1040542700(_, character: uint):
    """Event 1040542700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 4200)
    DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_1, 4208)
    IfFlagEnabled(AND_1, 1040549254)
    IfFlagEnabled(OR_1, 4207)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(AND_2, 4208)
    IfFlagEnabled(AND_2, 1040549254)
    IfFlagEnabled(OR_2, 4207)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
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
    IfFlagEnabled(AND_15, 4208)
    IfFlagEnabled(AND_15, 1040549254)
    IfFlagEnabled(OR_15, 4207)
    IfConditionTrue(OR_15, input_condition=AND_15)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1040542705)
def Event_1040542705(_, character: uint):
    """Event 1040542705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 4205)
    IfFlagEnabled(OR_1, 4206)
    IfFlagEnabled(OR_1, 4207)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagDisabled(AND_1, 4203)
    IfFlagDisabled(AND_2, 4217)
    IfFlagEnabled(AND_2, 4203)
    IfFlagDisabled(AND_2, 11009554)
    IfFlagDisabled(AND_2, 1051569454)
    IfFlagDisabled(AND_2, 11059304)
    IfFlagEnabled(AND_3, 1040549254)
    IfFlagDisabled(AND_3, 4217)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(OR_2, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930000, unknown2=1.0)
    EnableNetworkFlag(1040549254)
    DisableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_10, 4205)
    IfFlagEnabled(OR_10, 4206)
    IfFlagEnabled(OR_10, 4207)
    IfConditionTrue(AND_10, input_condition=OR_10)
    IfFlagDisabled(AND_10, 4203)
    IfFlagDisabled(AND_11, 4217)
    IfFlagEnabled(AND_11, 4203)
    IfFlagDisabled(AND_11, 11009554)
    IfFlagDisabled(AND_11, 1051569454)
    IfFlagDisabled(AND_11, 11059304)
    IfFlagEnabled(AND_12, 1040549254)
    IfFlagDisabled(AND_12, 4217)
    IfConditionTrue(OR_11, input_condition=AND_10)
    IfConditionTrue(OR_11, input_condition=AND_11)
    IfConditionTrue(OR_11, input_condition=AND_12)
    IfConditionFalse(MAIN, input_condition=OR_11)
    Restart()


@RestartOnRest(1040542706)
def Event_1040542706(_, character: uint):
    """Event 1040542706"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EnableImmortality(character)
    IfAttackedWithDamageType(MAIN, attacked_entity=character, attacker=PLAYER)
    EnableNetworkFlag(1040542710)
    ForceAnimation(character, 20010, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    End()
