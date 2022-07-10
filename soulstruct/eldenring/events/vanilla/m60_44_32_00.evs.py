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
    Event_1044322200(
        0,
        character=1044320200,
        special_effect=12603,
        region=1044322200,
        region_1=1044322201,
        region_2=1044322202
    )
    RunCommonEvent(0, 90005300, args=(1044320200, 1044320200, 40138, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005860, args=(1044320800, 0, 1044320340, 0, 1044320400, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(1044320340, 904980602, 24), arg_types="IiI")
    RunCommonEvent(0, 90005300, args=(1044320850, 1044320344, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005476, args=(1044320342, 1044320344), arg_types="II")
    RunCommonEvent(0, 90005477)
    Event_1044322340(0, character=1044320342, character_1=1044320344)
    RunCommonEvent(0, 90005860, args=(1044320850, 0, 1044320342, 0, 1044320410, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005871, args=(1044320342, 903150601, 10, 1044320344), arg_types="IiII")
    RunCommonEvent(0, 90005872, args=(1044320342, 10, 0), arg_types="III")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(
        0,
        90005211,
        args=(1044320340, 30000, 20000, 1044322340, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@NeverRestart(1044322200)
def Event_1044322200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1044322200"""
    EndIfFlagEnabled(1044320200)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, 1044320200)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(1044322201)
    DisableFlag(1044322202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1044322201, 1044322202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1044322201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1044322210)
def Event_1044322210(_, obj: uint, entity: uint, flag: uint):
    """Event 1044322210"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1044322340)
def Event_1044322340(_, character: uint, character_1: uint):
    """Event 1044322340"""
    IfCharacterAlive(AND_1, character)
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    IfCharacterHasSpecialEffect(AND_2, character, 11825)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    IfCharacterBackreadEnabled(AND_3, character_1)
    IfConditionTrue(MAIN, input_condition=AND_3)
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterBackreadDisabled(AND_4, character_1)
    IfConditionTrue(MAIN, input_condition=AND_4)
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()


@RestartOnRest(1044322600)
def Event_1044322600():
    """Event 1044322600"""
    DisableObject(1044321600)
    DisableObject(1044321601)
    DisableObject(1044321602)
    DisableObject(1044321603)
    DisableObject(1044321604)
