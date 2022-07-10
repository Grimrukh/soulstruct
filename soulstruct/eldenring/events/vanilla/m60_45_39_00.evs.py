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
    RunCommonEvent(0, 90005616, args=(530170, 1045392700), arg_types="II")
    Event_1045392281(0, character=1045390250, region=1045392280, owner_entity=1045390281)
    Event_1045392281(1, character=1045390251, region=1045392280, owner_entity=1045390281)
    Event_1045392281(2, character=1045390252, region=1045392280, owner_entity=1045390281)
    Event_1045392281(3, character=1045390253, region=1045392280, owner_entity=1045390281)
    Event_1045392281(4, character=1045390254, region=1045392280, owner_entity=1045390281)
    Event_1045392281(5, character=1045390255, region=1045392280, owner_entity=1045390281)
    Event_1045392281(6, character=1045390256, region=1045392280, owner_entity=1045390281)
    Event_1045392281(7, character=1045390257, region=1045392280, owner_entity=1045390281)
    Event_1045392281(8, character=1045390258, region=1045392280, owner_entity=1045390281)
    Event_1045392280(0, attacker__character=1045395280, region=1045392280)
    RunCommonEvent(
        0,
        90005620,
        args=(1045390570, 1045391570, 1045391571, 0, 1045392570, 1045392571, 1045392572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(1045390570, 1045391573), arg_types="II")
    Event_1045392341(
        0,
        1045390800,
        1045393240,
        1045393241,
        1045393242,
        1045393230,
        1045393231,
        1045393232,
        15300,
        15310,
        15311,
        15312,
    )
    Event_1045392342(
        0,
        1045390800,
        1045390800,
        15302,
        1045392343,
        1045390350,
        15310,
        15311,
        15312,
        1045392343,
        1045392344,
        1045392345,
        1045390351,
    )
    Event_1045392343(
        0,
        character=1045390800,
        region=1045392340,
        region_1=1045392341,
        region_2=1045392342,
        special_effect_id=15310,
        special_effect_id_1=15311,
        special_effect_id_2=15312
    )
    Event_1045392345(0, flag=1045390800, character=1045390800, character_1=1045395230)
    Event_1045392346(0, character__targeting_character=1045390800, region=1045392810)
    RunCommonEvent(0, 90005870, args=(1045390800, 904950600, 24), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1045390800, 0, 1045390800, 0, 30170, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005704, args=(1045390700, 4041, 4040, 1044399201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1045390700, 4041, 4042, 1044399201, 4041, 4040, 4043, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1045390700, 4043, 4040, 4043), arg_types="IIII")
    Event_1045390700(0, character=1045390700)
    Event_1045390701()
    RunCommonEvent(0, 90005775, args=(81463900, 1045399206, -1.0), arg_types="iIf")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045390700)
    Event_1045392282()


@RestartOnRest(1045392280)
def Event_1045392280(_, attacker__character: uint, region: uint):
    """Event 1045392280"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5654)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1045392280)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5654)
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
    EnableNetworkFlag(1045392280)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5654)


@RestartOnRest(1045392281)
def Event_1045392281(_, character: uint, region: uint, owner_entity: uint):
    """Event 1045392281"""
    IfCharacterDead(AND_10, character)
    EndIfConditionTrue(input_condition=AND_10)
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=PLAYER)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    IfCharacterHollow(OR_7, PLAYER)
    IfCharacterWhitePhantom(OR_7, PLAYER)
    IfCharacterOutsideRegion(AND_11, character=PLAYER, region=region)
    IfConditionTrue(AND_11, input_condition=OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    ForceAnimation(character, 20011, unknown2=1.0)
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    CancelSpecialEffect(character, 8090)


@RestartOnRest(1045392282)
def Event_1045392282():
    """Event 1045392282"""
    DropMandatoryTreasure(1045395282)


@RestartOnRest(1045392341)
def Event_1045392341(
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
    """Event 1045392341"""
    GotoIfFlagDisabled(Label.L0, flag=1045390800)
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


@RestartOnRest(1045392342)
def Event_1045392342(
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
    """Event 1045392342"""
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


@RestartOnRest(1045392343)
def Event_1045392343(
    _,
    character: uint,
    region: uint,
    region_1: uint,
    region_2: uint,
    special_effect_id: int,
    special_effect_id_1: int,
    special_effect_id_2: int,
):
    """Event 1045392343"""
    EndIfFlagEnabled(1045390800)
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


@RestartOnRest(1045392345)
def Event_1045392345(_, flag: uint, character: uint, character_1: uint):
    """Event 1045392345"""
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
    DisableSpawner(entity=1045393230)
    DisableSpawner(entity=1045393231)
    DisableSpawner(entity=1045393232)
    DisableSpawner(entity=1045393240)
    DisableSpawner(entity=1045393241)
    DisableSpawner(entity=1045393242)
    Wait(2.0)
    Kill(character_1)
    Wait(7.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(1045392346)
def Event_1045392346(_, character__targeting_character: uint, region: uint):
    """Event 1045392346"""
    DisableNetworkSync()
    EndIfFlagEnabled(1045390800)
    IfCharacterTargeting(AND_1, targeting_character=character__targeting_character, targeted_character=20000)
    IfCharacterOutsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1045390700)
def Event_1045390700(_, character: uint):
    """Event 1045390700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 4040)
    DisableFlag(1044399202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4046)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 4046)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L0, flag=4040)
    GotoIfFlagEnabled(Label.L1, flag=4041)
    GotoIfFlagEnabled(Label.L3, flag=4043)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90105, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 4046)
    Restart()


@RestartOnRest(1045390701)
def Event_1045390701():
    """Event 1045390701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1045390800)
    IfFlagEnabled(MAIN, 1045390800)
    EndIfFlagDisabled(4045)
    EnableFlag(4058)
