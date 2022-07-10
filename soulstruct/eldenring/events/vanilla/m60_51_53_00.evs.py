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
    RegisterGrace(grace_flag=1051530000, obj=1051531950, unknown=5.0)
    Event_1051532200(0, character=1051535200)
    Event_1051532390()
    RunCommonEvent(0, 90005200, args=(1051530321, 30005, 20005, 1051532321, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1051530322, 30006, 20006, 1051532322, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005211, args=(1051530323, 30006, 20006, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(1051530324, 30006, 20006, 0, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005300, args=(1051530210, 1051530210, 1051530700, 0.0, 0), arg_types="IIifi")
    Event_1051532220(
        0,
        character=1051530210,
        special_effect=12603,
        region=1051532210,
        region_1=1051532211,
        region_2=1051532212
    )
    RunCommonEvent(0, 90005201, args=(1051530210, 30000, 20000, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005300, args=(1051530380, 1051530180, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1051530180, 1051532181, 1051532182, 1051530180, 21, 1051532180, 1051532181, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1051530180, 1051532181, 1051532182, 1051530180), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1051530180, 1051532181, 1051532182, 1051530180, 1051530500, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1051530180, 1051532181, 1051532182, 1051530180, 1051532180, 1051532182, 0),
        arg_types="IIIIIIi",
    )
    Event_1051532330(0, attacker__character=1051535330, region=1051532330)
    Event_1051532330(1, attacker__character=1051535331, region=1051532331)
    RunCommonEvent(0, 90005200, args=(1051530284, 30000, 20000, 1051532284, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1051530283, 1051532283, 0.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005771, args=(1051530950, 1051532700), arg_types="II")


@RestartOnRest(1051532200)
def Event_1051532200(_, character: uint):
    """Event 1051532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()


@NeverRestart(1051532220)
def Event_1051532220(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1051532220"""
    EndIfFlagEnabled(1051530210)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, 1051530210)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(1051532221)
    DisableFlag(1051532222)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1051532221, 1051532222))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region_1)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region_2)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region_2)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1051532221)
    SkipLines(4)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    SetNest(character, region=region_1)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@RestartOnRest(1051532330)
def Event_1051532330(_, attacker__character: uint, region: uint):
    """Event 1051532330"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5651)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1051532330)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5651)
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
    EnableNetworkFlag(1050562200)
    CancelSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 4802)
    CancelSpecialEffect(attacker__character, 5651)


@RestartOnRest(1051532390)
def Event_1051532390():
    """Event 1051532390"""
    AddSpecialEffect(1051530331, 12019)
    IfCharacterHasSpecialEffect(AND_1, 1051530331, 12019)
    IfCharacterHasSpecialEffect(AND_1, 1051530331, 12018)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(1051530331, 20020, unknown2=1.0)
    End()
