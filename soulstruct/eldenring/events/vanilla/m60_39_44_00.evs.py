"""
linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039440000, obj=1039441950, unknown=5.0)
    RunCommonEvent(0, 90005261, args=(1039440200, 1039442200, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039440201, 1039442200, 5.0, 1.5, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039440202, 1039442200, 5.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1039440203, 1039442200, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005616, args=(530240, 1039442710), arg_types="II")
    RunCommonEvent(
        0,
        90005780,
        args=(1039440800, 1039442160, 1039442161, 1039440750, 20, 1039442720, 11109648, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1039440800, 1039442160, 1039442161, 1039440750), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1039440800, 1039442160, 1039442161, 1039440750, 1039442720, 1039442160, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005703,
        args=(1039440700, 3661, 3662, 1043399301, 1043399314, 3660, 3663, -1),
        arg_types="IIIIIIIi",
    )
    RunCommonEvent(0, 90005704, args=(1039440700, 1043399314, 3660, 1043399301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1039440700, 3663, 3660, 3663), arg_types="IIII")
    Event_1039443700(0, character=1039440700)
    Event_1039443701()
    Event_1039443702()
    Event_1039443705()
    Event_1039443706()
    Event_1039443707()
    Event_1039443720(0, character=1039440705, character_1=1039440708)
    RunCommonEvent(0, 90005704, args=(1039440705, 3821, 3820, 1039449251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039440705, 3821, 3822, 1039449251, 3821, 3820, 3823, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1039440708, 3821, 3820, 1039449251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039440708, 3821, 3822, 1039449251, 3821, 3820, 3823, -1), arg_types="IIIIIIIi")
    Event_1039443721(0, character=1039440706)
    RunCommonEvent(0, 90005704, args=(1039440706, 3821, 3820, 1039449251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039440706, 3821, 3822, 1039449251, 3821, 3820, 3823, -1), arg_types="IIIIIIIi")
    Event_1039443722(0, character=1039440707)
    RunCommonEvent(0, 90005704, args=(1039440707, 3821, 3820, 1039449251, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039440707, 3821, 3822, 1039449251, 3821, 3820, 3823, -1), arg_types="IIIIIIIi")
    Event_1039443724(0, character=1039440705)
    RunCommonEvent(0, 90005709, args=(1039440705, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1039440705, 200, 603051), arg_types="Iii")
    Event_1039443725(0, character=1039440706)
    RunCommonEvent(0, 90005709, args=(1039440706, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1039440706, 200, 603051), arg_types="Iii")
    Event_1039443726(0, character=1039440707)
    RunCommonEvent(0, 90005709, args=(1039440707, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1039440707, 200, 603051), arg_types="Iii")
    Event_1039443732(0, character=1039440708)
    RunCommonEvent(0, 90005709, args=(1039440708, 905, 603000), arg_types="Iii")
    RunCommonEvent(0, 90005709, args=(1039440708, 200, 603051), arg_types="Iii")
    RunCommonEvent(0, 90005750, args=(1039441705, 4110, 104600, 400460, 400460, 3829, 0), arg_types="IiiIIIi")
    Event_1039443727()
    Event_1039443728(0, obj=1039441720, obj_1=1039441721, obj_2=1039441722, obj_3=1039441723)
    Event_1039443740(0, character=1039440730)
    RunCommonEvent(0, 90005702, args=(1039440730, 1039440736, 1039440735, 1039440736), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440730, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440730, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443741(0, character=1039440731)
    RunCommonEvent(0, 90005702, args=(1039440731, 1039440738, 1039440737, 1039440738), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440731, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440731, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443742(0, character=1039440740)
    RunCommonEvent(0, 90005702, args=(1039440740, 1039440746, 1039440745, 1039440746), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440740, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440740, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443743(0, character=1039440741)
    RunCommonEvent(0, 90005702, args=(1039440741, 1039440748, 1039440747, 1039440748), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440741, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440741, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443744(0, character=1039440742)
    RunCommonEvent(0, 90005702, args=(1039440742, 1039440750, 1039440749, 1039440750), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440742, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440742, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443745(0, character=1039440743)
    RunCommonEvent(0, 90005702, args=(1039440743, 1039440752, 1039440751, 1039440752), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440743, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440743, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443746(0, character=1039440744)
    RunCommonEvent(0, 90005702, args=(1039440744, 1039440754, 1039440753, 1039440754), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1039440744, 1039449284, 3820, 1039449294, 3), arg_types="IIIIi")
    RunCommonEvent(
        0,
        90005703,
        args=(1039440744, 3821, 3822, 1039449294, 1039449284, 3820, 3823, -1),
        arg_types="IIIIIIIi",
    )
    Event_1039443729()
    Event_1039443730()
    Event_1039443731()
    RunCommonEvent(0, 90005704, args=(1039440710, 3441, 3440, 1039449301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1039440710, 3441, 3442, 1039449301, 3441, 3440, 3444, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1039440710, 3443, 3440, 3444), arg_types="IIII")
    RunCommonEvent(0, 90005702, args=(1039440711, 3443, 3440, 3444), arg_types="IIII")
    Event_1039443710(0, character=1039440710)
    Event_1039443711(0, character=1039440711)
    Event_1039443712(0, attacked_entity=1039440711, flag=1039449315)
    Event_1039443713()
    Event_1039442341(
        0,
        1039440800,
        1039443240,
        1039443241,
        1039443242,
        1039443230,
        1039443231,
        1039443232,
        15300,
        15310,
        15311,
        15312,
    )
    Event_1039442342(
        0,
        1039440800,
        1039440800,
        15302,
        1039442803,
        1039440350,
        15310,
        15311,
        15312,
        1039442803,
        1039442804,
        1039442805,
        1039440351,
    )
    Event_1039442343(
        0,
        character=1039440800,
        region=1039442800,
        region_1=1039442801,
        region_2=1039442802,
        special_effect_id=15310,
        special_effect_id_1=15311,
        special_effect_id_2=15312
    )
    Event_1039442344(0, flag=1039440800, character=1039440800, character_1=1039445250)
    Event_1039442345(0, character__targeting_character=1039440800, region=1039442810)
    RunCommonEvent(0, 90005870, args=(1039440800, 904950601, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1039440800, 0, 1039440800, 0, 30240, 0.0), arg_types="IIIIif")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1039440705)
    DisableBackread(1039440706)
    DisableBackread(1039440710)
    DisableBackread(1039440711)
    DisableBackread(1039440720)


@RestartOnRest(1039442341)
def Event_1039442341(
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
    """Event 1039442341"""
    GotoIfFlagDisabled(Label.L0, flag=1039440800)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(AND_1, character, special_effect)
    IfFlagDisabled(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_1)
    EnableSpawner(entity=entity)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_2)
    EnableSpawner(entity=entity_1)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=4, character=character, special_effect=special_effect_3)
    EnableSpawner(entity=entity_2)
    EnableSpawner(entity=entity_3)
    EnableSpawner(entity=entity_4)
    EnableSpawner(entity=entity_5)
    Wait(1.0)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    DisableSpawner(entity=entity_3)
    DisableSpawner(entity=entity_4)
    DisableSpawner(entity=entity_5)
    Wait(1.0)
    Restart()


@RestartOnRest(1039442342)
def Event_1039442342(
    _,
    character: uint,
    flag: uint,
    special_effect: int,
    destination: uint,
    first_flag: uint,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
    destination_1: uint,
    destination_2: uint,
    destination_3: uint,
    last_flag: uint,
):
    """Event 1039442342"""
    EndIfFlagEnabled(flag)
    IfCharacterHasSpecialEffect(MAIN, character, special_effect)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(2, first_flag)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(2, first_flag)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(2, first_flag)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3022, loop=True, unknown2=1.0)
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(1039442343)
def Event_1039442343(
    _,
    character: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    special_effect_id: int,
    special_effect_id_1: int,
    special_effect_id_2: int,
):
    """Event 1039442343"""
    EndIfFlagEnabled(1039440800)
    IfCharacterInsideRegion(AND_2, character=character, region=region)
    IfConditionTrue(OR_5, input_condition=AND_2)
    IfCharacterInsideRegion(AND_3, character=character, region=region_1)
    IfConditionTrue(OR_5, input_condition=AND_3)
    IfCharacterInsideRegion(AND_4, character=character, region=region_2)
    IfConditionTrue(OR_5, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_5)
    GotoIfFinishedConditionFalse(Label.L2, input_condition=AND_2)
    AddSpecialEffect(character, special_effect_id)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFinishedConditionFalse(Label.L3, input_condition=AND_3)
    AddSpecialEffect(character, special_effect_id_1)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFinishedConditionFalse(Label.L4, input_condition=AND_4)
    AddSpecialEffect(character, special_effect_id_2)

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(1.0)
    Restart()


@RestartOnRest(1039442344)
def Event_1039442344(_, flag: uint, character: uint, character_1: uint):
    """Event 1039442344"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDead(MAIN, character)
    IfConditionTrue(MAIN, input_condition=MAIN)
    Kill(character_1)
    DisableSpawner(entity=1039443240)
    DisableSpawner(entity=1039443241)
    DisableSpawner(entity=1039443242)
    DisableSpawner(entity=1039443230)
    DisableSpawner(entity=1039443231)
    DisableSpawner(entity=1039443232)
    Wait(2.0)
    Kill(character_1)
    Wait(7.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1039442345)
def Event_1039442345(_, character__targeting_character: uint, region: uint):
    """Event 1039442345"""
    DisableNetworkSync()
    EndIfFlagEnabled(character__targeting_character)
    IfCharacterTargeting(AND_1, targeting_character=character__targeting_character, targeted_character=20000)
    IfCharacterOutsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1039443700)
def Event_1039443700(_, character: uint):
    """Event 1039443700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3669)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3669)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfFlagDisabled(1, 1039449214)
    Move(character, destination=1039442705, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010, unknown2=1.0)
    SkipLinesIfFlagEnabled(1, 1039449214)
    ForceAnimation(character, 930018, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    IfFlagDisabled(MAIN, 3669)
    Restart()


@RestartOnRest(1039443701)
def Event_1039443701():
    """Event 1039443701"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3660)
    EnableImmortality(1039440700)
    DisableHealthBar(1039440700)
    AwaitFlagEnabled(flag=1039449214)
    DisableImmortality(1039440700)
    EnableHealthBar(1039440700)
    End()


@RestartOnRest(1039443702)
def Event_1039443702():
    """Event 1039443702"""
    EndIfPlayerNotInOwnWorld()
    AwaitFlagEnabled(flag=3669)
    DisableNetworkFlag(1039442702)
    DisableNetworkFlag(1039442703)
    IfFlagEnabled(AND_1, 3669)
    IfFlagDisabled(AND_1, 1039449206)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1039440700, radius=70.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1039442702)
    Wait(20.0)
    Restart()


@RestartOnRest(1039443705)
def Event_1039443705():
    """Event 1039443705"""
    EndIfFlagEnabled(1039449214)
    IfCharacterHasSpecialEffect(AND_1, 1039440700, 420)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039449207)
    End()


@RestartOnRest(1039443706)
def Event_1039443706():
    """Event 1039443706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1039449214)
    EnableFlag(1043399314)
    IfFlagEnabled(MAIN, 1039449214)
    DisableFlag(1043399314)
    End()


@RestartOnRest(1039443707)
def Event_1039443707():
    """Event 1039443707"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3669)
    AwaitFlagEnabled(flag=1035539204)
    EnableNetworkFlag(3678)
    End()


@RestartOnRest(1039443710)
def Event_1039443710(_, character: uint):
    """Event 1039443710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3440)
    IfFlagEnabled(AND_1, 11109405)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3450)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3450)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90102, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
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
    IfFlagEnabled(OR_15, 3450)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1039443711)
def Event_1039443711(_, character: uint):
    """Event 1039443711"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3440)
    IfFlagEnabled(AND_1, 11109405)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(1039441710)
    IfFlagEnabled(OR_1, 3451)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3451)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableImmortality(character)
    EnableObject(1039441710)
    DisableHealthBar(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagEnabled(6, 1039449316)
    EnableCharacter(character)
    EnableBackread(character)
    EnableObject(1039441710)
    ForceAnimation(character, 90104, unknown2=1.0)
    DisableAnimations(character)
    Goto(Label.L20)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(1039441710)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagEnabled(OR_15, 3451)
    IfConditionFalse(MAIN, input_condition=OR_15)
    Restart()


@RestartOnRest(1039443712)
def Event_1039443712(_, attacked_entity: uint, flag: uint):
    """Event 1039443712"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3451)
    EndIfFlagEnabled(flag)
    IfFlagEnabled(OR_1, flag)
    IfAttackedWithDamageType(OR_1, attacked_entity=attacked_entity, attacker=PLAYER)
    AwaitConditionTrue(OR_1)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3444))
    EnableNetworkFlag(3443)
    SaveRequest()
    DisableAnimations(attacked_entity)
    ForceAnimation(attacked_entity, 90200, unknown2=1.0)
    End()


@RestartOnRest(1039443713)
def Event_1039443713():
    """Event 1039443713"""
    EndIfFlagEnabled(3443)
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfHealthValueEqual(AND_1, 1039440710, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(1039440710, True)
    IfTimeElapsed(AND_2, seconds=10.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SetBackreadStateAlternate(1039440710, False)
    End()


@RestartOnRest(1039443720)
def Event_1039443720(_, character: uint, character_1: uint):
    """Event 1039443720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_10, 3820)
    IfFlagEnabled(AND_10, 1039449253)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    IfFlagEnabled(OR_1, 3825)
    IfFlagEnabled(OR_1, 3826)
    IfFlagEnabled(AND_1, 3828)
    IfFlagEnabled(AND_1, 1039449296)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3825)
    IfFlagEnabled(OR_2, 3826)
    IfFlagEnabled(AND_2, 3828)
    IfFlagEnabled(AND_2, 1039449296)
    IfConditionTrue(OR_2, input_condition=AND_2)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(5, 1039442715)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930011, unknown2=1.0)
    Move(character, destination=1039442700, destination_type=CoordEntityType.Region, short_move=True)
    EnableImmortality(character)
    SkipLinesIfFlagDisabled(5, 1039442715)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, 930024, unknown2=1.0)
    EnableImmortality(character_1)
    EnableNetworkFlag(1039442716)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_15, 3825)
    IfFlagDisabled(AND_15, 3826)
    IfFlagDisabled(AND_15, 3828)
    IfConditionTrue(OR_15, input_condition=AND_15)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 1039442715)
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1039443721)
def Event_1039443721(_, character: uint):
    """Event 1039443721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_10, 3820)
    IfFlagEnabled(AND_10, 1039449253)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3827)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(OR_2, 3827)
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930012, unknown2=1.0)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_15, 3827)
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1039443722)
def Event_1039443722(_, character: uint):
    """Event 1039443722"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_10, 3820)
    IfFlagEnabled(AND_10, 1039449253)
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1039449253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(AND_1, 3828)
    IfFlagDisabled(AND_1, 1039449296)
    IfConditionTrue(OR_1, input_condition=AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    IfFlagEnabled(AND_2, 3828)
    IfFlagDisabled(AND_2, 1039449296)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3820)
    GotoIfFlagEnabled(Label.L2, flag=3821)
    GotoIfFlagEnabled(Label.L3, flag=3822)
    GotoIfFlagEnabled(Label.L4, flag=3823)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930014, unknown2=1.0)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(AND_15, 3828)
    AwaitConditionTrue(AND_15)
    Restart()


@RestartOnRest(1039443724)
def Event_1039443724(_, character: uint):
    """Event 1039443724"""
    EndIfFlagEnabled(3821)
    EndIfFlagEnabled(3822)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3821, 3822))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20027, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443725)
def Event_1039443725(_, character: uint):
    """Event 1039443725"""
    EndIfFlagEnabled(3821)
    EndIfFlagEnabled(3822)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3821, 3822))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20030, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443726)
def Event_1039443726(_, character: uint):
    """Event 1039443726"""
    EndIfFlagEnabled(3821)
    EndIfFlagEnabled(3822)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3821, 3822))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20033, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443727)
def Event_1039443727():
    """Event 1039443727"""
    WaitFrames(frames=1)
    EndIfFlagDisabled(3450)
    EndIfFlagDisabled(3440)
    EndIfFlagDisabled(3820)
    EndIfFlagEnabled(1039449278)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfFlagEnabled(2, 1039449274)
    EnableNetworkFlag(1039449274)
    End()
    SkipLinesIfFlagEnabled(2, 1039449275)
    EnableNetworkFlag(1039449275)
    End()
    SkipLinesIfFlagEnabled(2, 1039449276)
    EnableNetworkFlag(1039449276)
    End()
    SkipLinesIfFlagEnabled(2, 1039449277)
    EnableNetworkFlag(1039449277)
    End()
    SkipLinesIfFlagEnabled(2, 1039449278)
    EnableNetworkFlag(1039449278)
    End()
    End()


@RestartOnRest(1039443728)
def Event_1039443728(_, obj: uint, obj_1: uint, obj_2: uint, obj_3: uint):
    """Event 1039443728"""
    WaitFrames(frames=1)
    DisableObject(obj)
    DisableObject(obj_1)
    DisableObject(obj_2)
    DisableObject(obj_3)
    IfFlagEnabled(OR_1, 3827)
    IfFlagEnabled(OR_1, 3828)
    IfFlagEnabled(AND_1, 3829)
    IfFlagEnabled(AND_1, 1039449270)
    IfConditionTrue(OR_1, input_condition=AND_1)
    EndIfConditionFalse(input_condition=OR_1)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableObject(obj_2)
    EnableObject(obj_3)
    IfFlagEnabled(AND_5, 1039440736)
    SkipLinesIfConditionFalse(1, AND_5)
    DisableObject(obj)
    IfFlagEnabled(AND_5, 1039440746)
    SkipLinesIfConditionFalse(1, AND_5)
    DisableObject(obj_2)
    IfFlagEnabled(AND_6, 1039440738)
    SkipLinesIfConditionFalse(1, AND_6)
    DisableObject(obj_1)
    IfFlagEnabled(AND_7, 1039440748)
    IfFlagEnabled(AND_7, 1039440750)
    IfFlagEnabled(AND_7, 1039440752)
    SkipLinesIfConditionFalse(1, AND_7)
    DisableObject(obj_3)
    DisableCharacter(1039440730)
    DisableBackread(1039440730)
    DisableCharacter(1039440731)
    DisableBackread(1039440731)
    DisableCharacter(1039440740)
    DisableBackread(1039440740)
    DisableCharacter(1039440741)
    DisableBackread(1039440741)
    DisableCharacter(1039440742)
    DisableBackread(1039440742)
    DisableCharacter(1039440743)
    DisableBackread(1039440743)
    DisableCharacter(1039440744)
    DisableBackread(1039440744)
    End()


@RestartOnRest(1039443729)
def Event_1039443729():
    """Event 1039443729"""
    EndIfPlayerNotInOwnWorld()
    WaitFramesAfterCutscene(frames=1)
    IfFlagEnabled(OR_1, 3822)
    IfFlagEnabled(OR_1, 3442)
    EndIfConditionTrue(input_condition=OR_1)
    IfFlagEnabled(OR_15, 3821)
    IfFlagEnabled(AND_1, 3441)
    IfFlagEnabled(AND_1, 3450)
    IfConditionTrue(OR_15, input_condition=AND_1)
    SkipLinesIfFlagEnabled(1, 1039440736)
    IfFlagEnabled(OR_2, 1039440736)
    SkipLinesIfFlagEnabled(1, 1039440738)
    IfFlagEnabled(OR_2, 1039440738)
    SkipLinesIfFlagEnabled(1, 1039440746)
    IfFlagEnabled(OR_2, 1039440746)
    SkipLinesIfFlagEnabled(1, 1039440748)
    IfFlagEnabled(OR_2, 1039440748)
    SkipLinesIfFlagEnabled(1, 1039440750)
    IfFlagEnabled(OR_2, 1039440750)
    SkipLinesIfFlagEnabled(1, 1039440752)
    IfFlagEnabled(OR_2, 1039440752)
    SkipLinesIfFlagEnabled(1, 1039440754)
    IfFlagEnabled(OR_2, 1039440754)
    IfConditionTrue(OR_15, input_condition=OR_2)
    AwaitConditionTrue(OR_15)
    EnableNetworkFlag(1039449251)
    SkipLinesIfFlagDisabled(1, 3450)
    EnableNetworkFlag(1039449301)
    AddSpecialEffect(1039440730, 15220)
    AddSpecialEffect(1039440731, 15220)
    AddSpecialEffect(1039440740, 15220)
    AddSpecialEffect(1039440741, 15220)
    AddSpecialEffect(1039440742, 15220)
    AddSpecialEffect(1039440743, 15220)
    AddSpecialEffect(1039440744, 15220)
    End()


@RestartOnRest(1039443730)
def Event_1039443730():
    """Event 1039443730"""
    EndIfPlayerNotInOwnWorld()
    WaitFramesAfterCutscene(frames=1)
    IfFlagEnabled(AND_15, 3822)
    IfFlagEnabled(AND_15, 3442)
    EndIfConditionTrue(input_condition=AND_15)
    IfFlagEnabled(AND_1, 3443)
    IfFlagEnabled(AND_1, 3450)
    IfConditionTrue(OR_15, input_condition=AND_1)
    IfFlagEnabled(AND_2, 1039440736)
    IfFlagEnabled(AND_2, 1039440738)
    IfFlagEnabled(AND_2, 1039440746)
    IfFlagEnabled(AND_2, 1039440748)
    IfFlagEnabled(AND_2, 1039440750)
    IfFlagEnabled(AND_2, 1039440752)
    IfFlagEnabled(AND_2, 1039440754)
    IfConditionTrue(OR_15, input_condition=AND_2)
    AwaitConditionTrue(OR_15)
    DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
    EnableNetworkFlag(3822)
    IfFlagEnabled(AND_5, 3450)
    IfFlagDisabled(AND_5, 3443)
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(3440, 3443))
    EnableNetworkFlag(3442)
    AddSpecialEffect(1039440730, 15220)
    AddSpecialEffect(1039440731, 15220)
    AddSpecialEffect(1039440740, 15220)
    AddSpecialEffect(1039440741, 15220)
    AddSpecialEffect(1039440742, 15220)
    AddSpecialEffect(1039440743, 15220)
    AddSpecialEffect(1039440744, 15220)
    End()


@RestartOnRest(1039443731)
def Event_1039443731():
    """Event 1039443731"""
    WaitFramesAfterCutscene(frames=1)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_14, 3825)
    IfFlagEnabled(OR_14, 3826)
    IfFlagEnabled(OR_14, 3828)
    AwaitConditionTrue(OR_14)
    EndIfFlagEnabled(1039449289)
    DisableNetworkConnectedFlagRange(flag_range=(1039442730, 1039442739))
    DisableNetworkFlag(1039442715)
    GotoIfFlagEnabled(Label.L1, flag=3825)
    GotoIfFlagEnabled(Label.L2, flag=3826)
    GotoIfFlagEnabled(Label.L3, flag=3828)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L20, flag=1039449258)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    IfFlagEnabled(AND_2, 1039449261)
    IfFlagDisabled(AND_2, 11109430)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfFlagEnabled(AND_3, 1039449261)
    IfFlagDisabled(AND_3, 3443)
    IfFlagDisabled(AND_3, 3063)
    IfFlagDisabled(AND_3, 11109430)
    IfConditionTrue(OR_2, input_condition=AND_3)
    IfFlagEnabled(AND_4, 1039449263)
    IfFlagEnabled(AND_4, 11109430)
    IfFlagDisabled(AND_4, 3450)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfFlagEnabled(AND_5, 1039449263)
    IfFlagEnabled(AND_5, 3443)
    IfFlagEnabled(AND_5, 3063)
    IfFlagDisabled(AND_5, 3450)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfFlagEnabled(AND_6, 1039449266)
    IfFlagEnabled(AND_6, 3450)
    IfConditionTrue(OR_2, input_condition=AND_6)
    GotoIfConditionTrue(Label.L20, input_condition=OR_2)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L20, flag=1039449282)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    EnableRandomFlagInRange(flag_range=(1039442730, 1039442739))
    SkipLinesIfFlagRangeAllDisabled(1, (1039442730, 1039442732))
    EnableNetworkFlag(1039442715)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3825)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3826)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3828)
    IfFlagState(OR_15, FlagSetting.Change, FlagType.Absolute, 3450)
    RestartIfConditionTrue(input_condition=OR_15)


@RestartOnRest(1039443732)
def Event_1039443732(_, character: uint):
    """Event 1039443732"""
    EndIfFlagEnabled(3821)
    EndIfFlagEnabled(3822)
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3821, 3822))
    AwaitConditionTrue(AND_1)
    ForceAnimation(character, 20030, unknown2=1.0)
    SetTeamType(character, TeamType.NoTeam)
    End()


@RestartOnRest(1039443740)
def Event_1039443740(_, character: uint):
    """Event 1039443740"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440735, 1039440736))
    DisableNetworkConnectedFlagRange(flag_range=(1039440735, 1039440736))
    EnableNetworkFlag(1039440735)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440735)
    GotoIfFlagEnabled(Label.L4, flag=1039440736)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443741)
def Event_1039443741(_, character: uint):
    """Event 1039443741"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440737, 1039440738))
    DisableNetworkConnectedFlagRange(flag_range=(1039440737, 1039440738))
    EnableNetworkFlag(1039440737)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440737)
    GotoIfFlagEnabled(Label.L4, flag=1039440738)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443742)
def Event_1039443742(_, character: uint):
    """Event 1039443742"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440745, 1039440746))
    DisableNetworkConnectedFlagRange(flag_range=(1039440745, 1039440746))
    EnableNetworkFlag(1039440745)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440745)
    GotoIfFlagEnabled(Label.L4, flag=1039440746)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443743)
def Event_1039443743(_, character: uint):
    """Event 1039443743"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440747, 1039440748))
    DisableNetworkConnectedFlagRange(flag_range=(1039440747, 1039440748))
    EnableNetworkFlag(1039440747)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440747)
    GotoIfFlagEnabled(Label.L4, flag=1039440748)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30024, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443744)
def Event_1039443744(_, character: uint):
    """Event 1039443744"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440749, 1039440750))
    DisableNetworkConnectedFlagRange(flag_range=(1039440749, 1039440750))
    EnableNetworkFlag(1039440749)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440749)
    GotoIfFlagEnabled(Label.L4, flag=1039440750)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443745)
def Event_1039443745(_, character: uint):
    """Event 1039443745"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440751, 1039440752))
    DisableNetworkConnectedFlagRange(flag_range=(1039440751, 1039440752))
    EnableNetworkFlag(1039440751)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440751)
    GotoIfFlagEnabled(Label.L4, flag=1039440752)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30022, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(1039443746)
def Event_1039443746(_, character: uint):
    """Event 1039443746"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1039440753, 1039440754))
    DisableNetworkConnectedFlagRange(flag_range=(1039440753, 1039440754))
    EnableNetworkFlag(1039440753)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L1, flag=3821)
    GotoIfFlagEnabled(Label.L2, flag=3822)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L3, flag=1039440753)
    GotoIfFlagEnabled(Label.L4, flag=1039440754)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 30025, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()
