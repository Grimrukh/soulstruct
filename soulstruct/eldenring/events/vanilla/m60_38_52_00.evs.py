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
        90005620,
        args=(1038520570, 1038521570, 1038521571, 0, 1038522570, 1038522571, 1038522572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1038520570, 1038521573), arg_types="II")
    RunCommonEvent(0, 90005261, args=(1038520340, 1038522300, 30.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1038520350, 1038522300, 20.0, 0.0, -1), arg_types="IIffi")
    Event_1038522350()
    Event_1038522347(
        0,
        character__region__targeting_character=1038520340,
        region=1038522400,
        flag=1038520800,
        character__region=1038520350
    )
    Event_1038522347(
        1,
        character__region__targeting_character=1038520350,
        region=1038522400,
        flag=1038520800,
        character__region=1038520340
    )
    RunCommonEvent(0, 90005870, args=(1038520340, 904950602, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1038520800, 0, 1038520340, 0, 30385, 0.0), arg_types="IIIIif")
    Event_1038522339(0, character__region=1038520340, character__region_1=1038520350)
    Event_1038522349()
    RunCommonEvent(0, 90005616, args=(530385, 1038522700), arg_types="II")
    Event_1038522346(
        0,
        1038520340,
        1038520800,
        15302,
        1038522320,
        1038522340,
        15310,
        15311,
        15312,
        1038522343,
        1038522344,
        1038522345,
    )
    Event_1038522343(0, character=1038520340, region=1038522340, special_effect__special_effect_id=15310)
    Event_1038522343(1, character=1038520340, region=1038522341, special_effect__special_effect_id=15311)
    Event_1038522343(2, character=1038520340, region=1038522342, special_effect__special_effect_id=15312)
    Event_1038522344(0, flag=1038520800, character=1038520340, character_1=1038525230, character_2=1038520350)
    Event_1038522345(0, character=1038520340, character_1=1038520350, special_effect=15335)
    RunCommonEvent(
        0,
        90005211,
        args=(1038520200, 30016, 20016, 1038522200, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520201, 30016, 20016, 1038522200, 10.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520205, 30016, 20016, 1038522205, 10.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520206, 30016, 20016, 1038522205, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520210, 30016, 20016, 1038522210, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520215, 30016, 20016, 1038522215, 10.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520216, 30016, 20016, 1038522215, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520220, 30016, 20016, 1038522220, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520221, 30016, 20016, 1038522221, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520222, 30016, 20016, 1038522221, 10.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520225, 30016, 20016, 1038522225, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520226, 30016, 20016, 1038522225, 10.0, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1038520250, 1038522250, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1038520251, 30016, 20016, 1038522250, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520255, 30016, 20016, 1038522255, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520256, 30016, 20016, 1038522255, 10.0, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        2,
        90005211,
        args=(1038520257, 30016, 20016, 1038522255, 10.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520260, 30016, 20016, 1038522260, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520265, 30014, 20014, 1038522265, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        3,
        90005211,
        args=(1038520266, 30014, 20014, 1038522265, 5.0, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        4,
        90005211,
        args=(1038520267, 30014, 20014, 1038522265, 5.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520270, 30016, 20016, 1038522270, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520280, 30014, 20014, 1038522280, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520281, 30014, 20014, 1038522280, 10.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        2,
        90005211,
        args=(1038520282, 30014, 20014, 1038522280, 10.0, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520285, 30014, 20014, 1038522285, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520286, 30014, 20014, 1038522285, 10.0, 0.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        2,
        90005211,
        args=(1038520287, 30014, 20014, 1038522285, 10.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520290, 30014, 20014, 1038522290, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1038520295, 30014, 20014, 1038522295, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038520296, 30014, 20014, 1038522295, 10.0, 0.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        2,
        90005211,
        args=(1038520297, 30014, 20014, 1038522295, 10.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 900005610, args=(1038521680, 100, 800, 1038528600), arg_types="IiiI")
    RunCommonEvent(0, 90005683, args=(62314, 1038521200, 211, 78392, 78392), arg_types="IIiII")


@RestartOnRest(1038522339)
def Event_1038522339(_, character__region: uint, character__region_1: uint):
    """Event 1038522339"""
    EndIfFlagEnabled(1038520800)
    SetCharacterEventTarget(character__region, region=character__region_1)
    SetCharacterEventTarget(character__region_1, region=character__region)
    IfCharacterDead(AND_1, character__region_1)
    AwaitConditionTrue(AND_1)
    Wait(5.0)
    IfCharacterAlive(AND_2, character__region_1)
    AwaitConditionTrue(AND_2)
    Restart()


@RestartOnRest(1038522341)
def Event_1038522341(
    _,
    character: uint,
    entity: uint,
    entity_1: uint,
    entity_2: uint,
    entity_3: uint,
    entity_4: uint,
    entity_5: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 1038522341"""
    IfCharacterDead(AND_15, 1038520340)
    EndIfConditionTrue(input_condition=AND_15)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Kill(1038525230)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1038522230)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Kill(1038525230)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    EnableSpawner(entity=entity)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    EnableSpawner(entity=entity_1)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    EnableSpawner(entity=entity_2)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(5.0)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    EnableFlag(1038522230)
    Restart()


@RestartOnRest(1038522342)
def Event_1038522342(
    _,
    character: uint,
    special_effect: int,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 1038522342"""
    EndIfFlagEnabled(1038520800)
    IfCharacterHasSpecialEffect(MAIN, character, special_effect)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableFlag(1038520340)
    EnableRandomFlagInRange(flag_range=(1038520340, 1038520341))
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=10, character=character, special_effect=special_effect_1)
    SkipLinesIfFlagEnabled(4, 1038520340)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True, unknown2=1.0)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=10, character=character, special_effect=special_effect_2)
    SkipLinesIfFlagEnabled(4, 1038520341)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True, unknown2=1.0)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=10, character=character, special_effect=special_effect_3)
    SkipLinesIfFlagEnabled(4, 1038520340)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLines(3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 3022, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1038522343)
def Event_1038522343(_, character: uint, region: uint, special_effect__special_effect_id: int):
    """Event 1038522343"""
    EndIfFlagEnabled(1038520800)
    IfCharacterInsideRegion(AND_1, character=character, region=region)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect__special_effect_id, target_count=0.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, special_effect__special_effect_id)
    Restart()


@RestartOnRest(1038522344)
def Event_1038522344(_, flag: uint, character: uint, character_1: uint, character_2: uint):
    """Event 1038522344"""
    SkipLinesIfFlagDisabled(8, flag)
    DisableSpawner(entity=1038523350)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    Kill(character_2)
    End()
    IfCharacterDead(MAIN, character)
    IfConditionTrue(MAIN, input_condition=MAIN)
    EnableNetworkFlag(flag)
    DisableSpawner(entity=1038522230)
    DisableSpawner(entity=1038522231)
    DisableSpawner(entity=1038522232)
    DisableSpawner(entity=1038522240)
    DisableSpawner(entity=1038522241)
    DisableSpawner(entity=1038522242)
    DisableSpawner(entity=1038523350)
    Kill(character_1)
    Wait(15.0)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    Kill(character_2)
    End()


@RestartOnRest(1038522345)
def Event_1038522345(_, character: uint, character_1: uint, special_effect: int):
    """Event 1038522345"""
    IfHealthValueEqual(MAIN, character, value=0)
    IfCharacterHasSpecialEffect(AND_1, character_1, special_effect)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Kill(character_1, award_souls=True)
    End()


@RestartOnRest(1038522346)
def Event_1038522346(
    _,
    character: uint,
    flag: uint,
    special_effect: int,
    destination: uint,
    flag_1: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
):
    """Event 1038522346"""
    EndIfFlagEnabled(flag)
    IfCharacterHasSpecialEffect(MAIN, character, special_effect)
    IfHealthRatioLessThanOrEqual(AND_1, character, value=0.5)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableNetworkFlag(flag_1)
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(2, flag_1)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(2, flag_1)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3022, loop=True, unknown2=1.0)
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(1038522347)
def Event_1038522347(
    _,
    character__region__targeting_character: uint,
    region: uint,
    flag: uint,
    character__region: uint,
):
    """Event 1038522347"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfCharacterTargeting(AND_1, targeting_character=character__region__targeting_character, targeted_character=20000)
    IfCharacterOutsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character__region__targeting_character)
    Wait(1.0)
    SetCharacterEventTarget(character__region__targeting_character, region=character__region)
    SetCharacterEventTarget(character__region, region=character__region__targeting_character)
    Wait(5.0)
    Restart()


@UnknownRestart(1038522349)
def Event_1038522349():
    """Event 1038522349"""
    DisableFlag(1038520340)
    DisableFlag(1038520341)
    DisableFlag(1038520343)
    End()


@RestartOnRest(1038522350)
def Event_1038522350():
    """Event 1038522350"""
    AddSpecialEffect(1038520340, 8092)
    End()
