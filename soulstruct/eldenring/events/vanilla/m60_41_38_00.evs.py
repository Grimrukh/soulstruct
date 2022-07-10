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
    RegisterGrace(grace_flag=1041380000, obj=1041381950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(71001, 76102, 1041381980, 77100, 3, 78100, 78101, 78102, 78103, 78104, 78105, 78106, 78107, 78108, 78109),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1041382650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    RunCommonEvent(0, 90005460, args=(1041380240,))
    RunCommonEvent(0, 90005461, args=(1041380240,))
    RunCommonEvent(0, 90005462, args=(1041380240,))
    RunCommonEvent(0, 90005300, args=(1041380230, 1041380230, 40104, 0.0, 0), arg_types="IIifi")
    Event_1041382200(0, character=1041380250, region=1041382250, owner_entity=1041380258)
    Event_1041382200(1, character=1041380251, region=1041382250, owner_entity=1041380258)
    Event_1041382200(2, character=1041380252, region=1041382250, owner_entity=1041380258)
    Event_1041382200(3, character=1041380253, region=1041382250, owner_entity=1041380258)
    Event_1041383710(0, flag=4720, flag_1=1042389201, flag_2=1041389370)
    Event_1041383730(0, character=1041380720)
    RunCommonEvent(0, 90005752, args=(1041381700, 200, 120, 3.0), arg_types="Iiif")
    Event_1041383731()
    RunCommonEvent(0, 90005750, args=(1041381702, 4350, 101910, 400191, 400191, 1041389414, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(1041381702, 4350, 101910, 400191, 400191, 3708, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005750, args=(1041381702, 4350, 101910, 400191, 400191, 3709, 0), arg_types="IiiIIIi")
    Event_1041383750(0, character=1041380705)
    Event_1041383760(0, flag=78103, other_entity=1041380950, flag_1=1041389500)
    Event_1041383761(0, other_entity=1041380950, flag=1041389500)
    Event_1041383762(0, other_entity=1041380950, flag=1041389501)
    Event_1041383763(0, 1041380950, 1041389501)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1041380720)
    DisableBackread(1041380730)
    DisableObject(1041381700)
    RunCommonEvent(0, 90005251, args=(1041380220, 100.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1041380216, 25.0, 0.0, 1704), arg_types="Iffi")


@RestartOnRest(1041382200)
def Event_1041382200(_, character: uint, region: uint, owner_entity: uint):
    """Event 1041382200"""
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


@RestartOnRest(1041382650)
def Event_1041382650(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1041382650"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_NW_SE)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1041383700)
def Event_1041383700(_, character: uint):
    """Event 1041383700"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1041383701)
def Event_1041383701(_, entity: uint):
    """Event 1041383701"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3223)
    IfFlagEnabled(MAIN, 3221)
    ForceAnimation(entity, 20015, unknown2=1.0)


@RestartOnRest(1041383710)
def Event_1041383710(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1041383710"""
    IfFlagDisabled(OR_1, flag)
    IfFlagEnabled(OR_1, flag_1)
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkFlag(flag_2)
    End()
    EnableNetworkFlag(flag_2)
    IfFlagDisabled(OR_2, flag)
    IfFlagEnabled(OR_2, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1041383730)
def Event_1041383730(_, character: uint):
    """Event 1041383730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3705)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(1041381701)
    DisableObject(1041381700)
    DeleteVFX(120)
    SkipLinesIfFlagEnabled(1, 1041389412)
    EnableNetworkFlag(1041389414)
    IfFlagEnabled(MAIN, 3705)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableObject(1041381701)
    EnableObject(1041381700)
    ForceAnimation(character, 90100, unknown2=1.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableObject(1041381701)
    EnableObject(1041381700)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(1041381700)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(MAIN, 3705)
    Restart()


@RestartOnRest(1041383731)
def Event_1041383731():
    """Event 1041383731"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3705)
    GotoIfFlagDisabled(Label.L1, flag=1041382731)
    GotoIfFlagDisabled(Label.L2, flag=1041382732)
    GotoIfFlagDisabled(Label.L3, flag=1041382733)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(AND_1, attacked_entity=1041381700, attacker=20000)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1041382736)
    Wait(20.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    IfAttackedWithDamageType(AND_2, attacked_entity=1041381700, attacker=20000)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1041382737)
    Wait(15.0)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    IfAttackedWithDamageType(AND_3, attacked_entity=1041381700, attacker=20000)
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1041382738)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1041383750)
def Event_1041383750(_, character: uint):
    """Event 1041383750"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1041383760)
def Event_1041383760(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1041383760"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372701)
    IfFlagDisabled(OR_1, flag)
    IfEntityBeyondDistance(OR_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1041383761)
def Event_1041383761(_, other_entity: uint, flag: uint):
    """Event 1041383761"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4680)
    IfFlagEnabled(MAIN, 4680)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1041383762)
def Event_1041383762(_, other_entity: uint, flag: uint):
    """Event 1041383762"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(MAIN, 1042379203)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1041383763)
def Event_1041383763(_, other_entity: uint, flag: uint):
    """Event 1041383763"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379207)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372702)
    IfEntityBeyondDistance(MAIN, entity=20000, other_entity=other_entity, radius=5.0)
    DisableFlag(1042372702)
    Restart()
