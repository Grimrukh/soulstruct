"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterLadder(start_climbing_flag=49381500, stop_climbing_flag=49381501, obj=1049381500)
    RegisterLadder(start_climbing_flag=49381502, stop_climbing_flag=49381503, obj=1049381502)
    RegisterLadder(start_climbing_flag=49381504, stop_climbing_flag=49381505, obj=1049381504)
    RunCommonEvent(0, 9005810, args=(1049380800, 1049380000, 1049380950, 1049381950, 5.0), arg_types="IIIIf")
    RegisterGrace(grace_flag=1049380001, obj=1049381951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76413, 1049381981, 77400, 5, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005511, args=(1049380560, 1049381560, 1049383560, 99020, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1049380560, 1049382560, 1049382561), arg_types="III")
    RunCommonEvent(
        0,
        90005780,
        args=(1049380800, 1049382160, 1049382161, 1049380700, 20, 1049382701, 0, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1049380800, 1049382160, 1049382161, 1049380700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1049380800, 1049382160, 1049382161, 1049380700, 1049382700, 1049382400, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005300, args=(1049380290, 1049380290, 40404, 0.0, 0), arg_types="IIifi")
    Event_1049382210()
    Event_1049382211(0, 1049381235, 6.0)
    Event_1049382211(1, 1049381236, 12.0)
    Event_1049382211(2, 1049381237, 3.0)
    Event_1049382211(3, 1049381238, 2.0)
    Event_1049382211(4, 1049381239, 10.0)
    Event_1049382211(5, 1049381240, 14.0)
    Event_1049382211(6, 1049381241, 8.0)
    Event_1049382211(7, 1049381242, 5.0)
    Event_1049382211(8, 1049381243, 4.0)
    RunCommonEvent(0, 90005250, args=(1049380399, 1049382399, 0.0, -1), arg_types="IIfi")
    Event_1049382200(0, character=1049380200, special_effect_id=14807)
    Event_1049382200(1, character=1049380201, special_effect_id=14807)
    Event_1049382200(2, character=1049380202, special_effect_id=14807)
    RunCommonEvent(0, 90005250, args=(1049380200, 1049382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1049380201, 1049382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1049380202, 1049382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1049380311, 30002, 20002, 1049382311, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1049380306, 1049382311, 82.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1049380310, 1049382311, 22.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1049380312, 1049382311, 115.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1049380313, 1049382311, 50.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1049380800, 35.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005870, args=(1049380800, 903050600, 11), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1049380800, 0, 1049380800, 1, 30405, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1049380800, 11, 0), arg_types="III")
    Event_1049382820(0, character=1049380800, character_1=1049385800, special_effect=11130, animation_id=20015)
    Event_1049382824(0, character=1049380800, character_1=1049385801, special_effect=11131, animation_id=20015)
    Event_1049382821(0, 1049380800, 1049385800, 1049385801, 20016)


@RestartOnRest(1049382200)
def Event_1049382200(_, character: uint, special_effect_id: int):
    """Event 1049382200"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1049382210)
def Event_1049382210():
    """Event 1049382210"""
    CreateProjectileOwner(entity=1049380299)


@RestartOnRest(1049382211)
def Event_1049382211(_, source_entity: uint, seconds: float):
    """Event 1049382211"""
    EnableNetworkSync()
    Wait(8.0)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    Wait(seconds)
    IfNewGameCycleEqual(AND_1, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_2, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_3, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_4, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_5, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleGreaterThanOrEqual(AND_8, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=1049380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(1049382399)
def Event_1049382399(_, character: uint, destination: uint, special_effect: int):
    """Event 1049382399"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, character, special_effect)
    IfCharacterAlive(AND_2, character)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(1049382820)
def Event_1049382820(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1049382820"""
    GotoIfFlagDisabled(Label.L0, flag=1049380800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1049382300)
    DisableAI(character_1)
    DisableCharacter(character_1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AICommand(character, command_id=-1, command_slot=0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    SkipLinesIfFlagEnabled(2, 1049382300)
    EnableFlag(1049382300)
    ForceAnimation(character_1, animation_id, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(1049382821)
def Event_1049382821(_, character: uint, character_1: uint, character_2: uint, animation_id: int):
    """Event 1049382821"""
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDead(OR_1, character)
    IfConditionTrue(MAIN, input_condition=OR_1)
    ForceAnimation(character_1, animation_id, skip_transition=True, unknown2=1.0)
    ForceAnimation(character_2, animation_id, skip_transition=True, unknown2=1.0)
    Wait(3.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    Kill(character_2)
    End()


@RestartOnRest(1049382824)
def Event_1049382824(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1049382824"""
    GotoIfFlagDisabled(Label.L0, flag=1049380800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1049382301)
    DisableAI(character_1)
    DisableCharacter(character_1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AICommand(character, command_id=-1, command_slot=0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    SkipLinesIfFlagEnabled(2, 1049382301)
    EnableFlag(1049382301)
    ForceAnimation(character_1, animation_id, wait_for_completion=True, unknown2=1.0)
