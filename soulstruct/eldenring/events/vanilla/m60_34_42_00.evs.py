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
    RegisterGrace(grace_flag=1034420000, obj=1034421950, unknown=5.0)
    RunCommonEvent(0, 90005870, args=(1034420800, 904502602, 25), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1034420800, 0, 1034420800, 1, 30260, 0.0), arg_types="IIIIif")
    Event_1034422800()
    Event_1034422801()
    Event_1034422802()
    RunCommonEvent(0, 90005201, args=(1034420340, 30000, 20000, 17.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1034420340, 17.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005300, args=(1034420340, 1034420340, 1034420400, 0.0, 0), arg_types="IIifi")
    Event_1034422600(0, obj=1034421600, flag=1034422600, owner_entity=1034420600)
    Event_1034422600(1, obj=1034421601, flag=1034422601, owner_entity=1034420600)
    Event_1034422600(2, obj=1034421602, flag=1034422602, owner_entity=1034420600)
    Event_1034422600(3, obj=1034421603, flag=1034422603, owner_entity=1034420600)
    Event_1034422600(4, obj=1034421604, flag=1034422604, owner_entity=1034420600)
    Event_1034422600(5, obj=1034421605, flag=1034422605, owner_entity=1034420600)
    Event_1034422600(6, obj=1034421606, flag=1034422606, owner_entity=1034420600)
    Event_1034422600(7, obj=1034421607, flag=1034422607, owner_entity=1034420600)
    Event_1034422600(8, obj=1034421608, flag=1034422608, owner_entity=1034420600)
    Event_1034422600(9, obj=1034421609, flag=1034422609, owner_entity=1034420600)
    RunCommonEvent(0, 90005525, args=(1034420650, 1034421650), arg_types="II")
    RunCommonEvent(0, 90005706, args=(1034420710, 930023, 0), arg_types="IiI")
    Event_1034420700(0, character=1034420700, obj=1034421700)
    RunCommonEvent(0, 90005704, args=(1034420700, 4221, 4220, 10009701, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1034420700, 4221, 4222, 10009701, 4221, 4220, 4224, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1034420700, 4223, 4220, 4224), arg_types="IIII")
    Event_1034420701()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1034420700)
    DisableBackread(1034420710)
    Event_1034422230()
    RunCommonEvent(0, 90005251, args=(1034420200, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1034420203, 1034422203, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1034420206, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1034420208, 1034422208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1034420209, 1034422208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1034420210, 1034422208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1034420222, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034420228, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1034420370, 30003, 20003, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1034420373, 16.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1034420390, 30.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1034422230)
def Event_1034422230():
    """Event 1034422230"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(1034420220)
    DisableAI(1034420221)
    DisableAI(1034420223)
    DisableAI(1034420229)
    DisableAI(1034420230)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420202, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420220, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420221, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420223, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420227, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420229, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420230, attacker=0)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420231, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableAI(1034420220)
    EnableAI(1034420221)
    EnableAI(1034420223)
    EnableAI(1034420229)
    EnableAI(1034420230)


@RestartOnRest(1034422600)
def Event_1034422600(_, obj: uint, flag: uint, owner_entity: uint):
    """Event 1034422600"""
    EndIfFlagEnabled(flag)
    EndIfObjectDestroyed(obj)
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=obj, attacker=20000)
    IfEntityWithinDistance(OR_2, entity=obj, other_entity=20000, radius=2.0)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DestroyObject(obj, request_slot=0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        model_point=100,
        behavior_id=802402270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    End()


@RestartOnRest(1034422800)
def Event_1034422800():
    """Event 1034422800"""
    EndIfFlagEnabled(1034420800)
    GotoIfUnknown_1004_05(Label.L0, character=1034420800, unk_8_12=True)
    DisableCharacter(1034420800)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=1034420800, attacker=PLAYER)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1034422800)
    IfUnknownCharacterCondition_34(OR_2, character=1034420800, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=1034420800, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=1034420800, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=1034420800, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=1034420800, unk_8_12=260, unk_12_16=1)
    IfCharacterHasSpecialEffect(AND_4, 1034420800, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1034420800, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1034420800, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 1034420800, 90160)
    IfCharacterHasSpecialEffect(AND_5, 1034420800, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1034420800, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1034420800, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1034420800, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 1034420800, 90162)
    IfCharacterHasSpecialEffect(AND_6, 1034420800, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1034420800, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1034420800, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1034420800, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 1034420800, 90161)
    IfCharacterHasSpecialEffect(AND_7, 1034420800, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1034420800, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1034420800, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1034420800, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 1034420800, 90162)
    IfCharacterHasSpecialEffect(AND_8, 1034420800, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1034420800, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1034420800, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 1034420800, 90160)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_4)
    IfConditionTrue(OR_3, input_condition=AND_5)
    IfConditionTrue(OR_3, input_condition=AND_6)
    IfConditionTrue(OR_3, input_condition=AND_7)
    IfConditionTrue(OR_3, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_3)
    EnableNetworkFlag(1034422800)
    Unknown_2004_83(character=1034420800, unk_4_8=1)
    EnableCharacter(1034420800)
    ForceAnimation(1034420800, 20008, unknown2=1.0)


@RestartOnRest(1034422801)
def Event_1034422801():
    """Event 1034422801"""
    DisableNetworkSync()
    EndIfFlagEnabled(1034420800)
    IfCharacterInsideRegion(MAIN, character=1034420800, region=1034422801)
    AddSpecialEffect(1034420800, 10285)
    Wait(1.0)
    Restart()


@RestartOnRest(1034422802)
def Event_1034422802():
    """Event 1034422802"""
    DisableNetworkSync()
    EndIfFlagEnabled(1034420800)
    IfCharacterInsideRegion(MAIN, character=1034420800, region=1034422802)
    AddSpecialEffect(1034420800, 10286)
    Wait(1.0)
    Restart()


@RestartOnRest(1034420700)
def Event_1034420700(_, character: uint, obj: uint):
    """Event 1034420700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagEnabled(1, 4220)
    DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    IfFlagEnabled(AND_1, 4227)
    IfFlagDisabled(OR_1, 1035422160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    IfFlagEnabled(AND_2, 4227)
    IfFlagDisabled(OR_2, 1035422160)
    IfConditionTrue(AND_2, input_condition=OR_2)
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101, unknown2=1.0)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableObject(obj)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfFlagDisabled(OR_15, 4227)
    IfFlagEnabled(OR_15, 1035422160)
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1034420701)
def Event_1034420701():
    """Event 1034420701"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4221, 4223))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034429209)
    End()
