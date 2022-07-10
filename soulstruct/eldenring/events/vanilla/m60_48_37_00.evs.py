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
    RegisterGrace(grace_flag=1048370000, obj=1048371950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76458, 76405, 1048371980, 77410, 0, 78410, 78411, 78412, 78413, 78414, 78415, 78416, 78417, 78418, 78419),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005201, args=(1048370800, 30000, 20000, 50.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005870, args=(1048370800, 904501600, 25), arg_types="IiI")
    RunCommonEvent(0, 90005861, args=(1048370800, 0, 1048370800, 1, 30400, 30064, 0.0), arg_types="IIIIiif")
    Event_1048372200(
        0,
        character=1048370299,
        special_effect=12603,
        region=1048372299,
        region_1=1048372298,
        region_2=1048372297
    )
    RunCommonEvent(0, 90005300, args=(1048370299, 1048370299, 40406, 0.0, 0), arg_types="IIifi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048370700)


@NeverRestart(1048372200)
def Event_1048372200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1048372200"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, character, special_effect)
    IfCharacterAlive(AND_2, character)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableFlag(1048372201)
    DisableFlag(1048372202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1048372201, 1048372202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1048372201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()
