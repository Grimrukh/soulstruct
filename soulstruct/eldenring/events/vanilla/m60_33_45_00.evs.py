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
    RunCommonEvent(
        0,
        90005880,
        args=(1033450800, 1033450805, 1033452800, 1033450800, 30250, 60, 33, 45, 0, 1033452805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1033450800, 1033450805, 1033452801, 1033452802, 20300, 1033451805, 60, 33, 45, 0, 1033452805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1033450800,
            1033450805,
            1033452800,
            1033450800,
            1033452806,
            1033455810,
            1033451800,
            1033450810,
            1033452810,
            904600520,
            -1,
            20005,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1033450800, 1033450805, 1033451805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1033450800, 0, 1033452806, 1033452807, 0, 1), arg_types="IiIIii")
    Event_1033452200(
        0,
        character=1033450200,
        special_effect=12603,
        region=1033452200,
        region_1=1033452201,
        region_2=1033452202
    )
    RunCommonEvent(0, 90005300, args=(1033450200, 1033450200, 40264, 0.0, 0), arg_types="IIifi")


@RestartOnRest(1033452360)
def Event_1033452360():
    """Event 1033452360"""
    IfFlagEnabled(AND_1, 1033452800)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableCharacter(1033455800)
    DisableAnimations(1033455800)
    IfFlagEnabled(AND_1, 1033450800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(7.0)
    EnableCharacter(1033455800)
    EnableAnimations(1033455800)


@NeverRestart(1033452200)
def Event_1033452200(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1033452200"""
    EndIfFlagEnabled(1233450200)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, 1233450200)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(1033452201)
    DisableFlag(1033452202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1033452201, 1033452202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1033452201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1033452201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1033452201)
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
