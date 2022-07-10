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
    RegisterGrace(grace_flag=73010, obj=30101950, unknown=5.0)
    RunCommonEvent(
        0,
        90005646,
        args=(30100800, 30102840, 30102841, 30101840, 30102840, 30, 10, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30100510, 30101510, 1, 30101510, 30101511, 30101512, 30100511),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30100515, 30101515, 3, 30101515, 30101516, 30101517, 30100516),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30100510, 30100511, 1, 30101510, 30101511, 30101512, 30100512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(30100515, 30100516, 3, 30101515, 30101516, 30101517, 30100517),
        arg_types="IIIIIII",
    )
    Event_30102510()
    RunCommonEvent(0, 90005680, args=(30100500, 30100501, 30100502, 30100503, 30101500), arg_types="IIIII")
    Event_30102500()
    Event_30102560()
    Event_30102580()
    Event_30102200()
    Event_30100100(0, flag=30100540, obj=30101540, obj_act_id=30103540, obj_act_id_1=27041)
    RunCommonEvent(
        0,
        90005620,
        args=(30100570, 30101570, 30101571, 0, 30102570, 30102571, 30102572),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30100570, 30101573), arg_types="II")
    RunCommonEvent(0, 90005200, args=(30100202, 30003, 20003, 30102202, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30100203, 30003, 20003, 30102202, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30100200, 30003, 20003, 30102200, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30100201, 30003, 20003, 30102200, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30100205, 30102205, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30100206, 30102205, 0.5, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30100215, 30102215, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30100211, 30003, 20003, 30102211, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005211, args=(30100212, 30003, 20003, 30102212, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005250, args=(30100213, 30102213, 0.0, 3011), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30100228, 30003, 20003, 30102228, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(30100236, 30003, 20003, 30102236, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        1,
        90005200,
        args=(30100237, 30003, 20003, 30102236, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(2, 90005200, args=(30100238, 30003, 20003, 30102236, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(3, 90005200, args=(30100239, 30003, 20003, 30102236, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30100240, 30102240, 0.0, 3008), arg_types="IIfi")
    RunCommonEvent(1, 90005200, args=(30100241, 30003, 20003, 30102240, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30100232, 30102232, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30100233, 30102232, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(30100234, 30102232, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30100250, 30102250, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30100251, 30102250, 0.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30100255, 30001, 20001, 30102255, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        1,
        90005200,
        args=(30100256, 30001, 20001, 30102255, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(2, 90005200, args=(30100257, 30001, 20001, 30102255, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(3, 90005200, args=(30100258, 30001, 20001, 30102258, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(30100209, 30102209, 1.0, 0.0, 3001), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30100219, 30102219, 10.0, 0.5, 0), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(30100220, 30102219, 10.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(30100221, 30102219, 10.0, 4.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(30100222, 30102221, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005201, args=(30100226, 30000, 20000, 10.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(30100300, 30102300, 0.0, 0), arg_types="IIfi")
    Event_30102480()
    Event_30102490()
    Event_30102400(0, character=30100400)
    Event_30102410(
        4,
        character=30100400,
        region=30102454,
        patrol_information_id=30103451,
        region_1=30102455,
        patrol_information_id_1=30103452
    )
    RunCommonEvent(0, 90005250, args=(30100410, 30102415, 0.0, 0), arg_types="IIfi")
    Event_30102400(1, character=30100410)
    Event_30102410(
        1,
        character=30100410,
        region=30102410,
        patrol_information_id=30103410,
        region_1=30102411,
        patrol_information_id_1=30103411
    )
    Event_30102410(
        2,
        character=30100410,
        region=30102413,
        patrol_information_id=30103411,
        region_1=30102412,
        patrol_information_id_1=30103412
    )
    Event_30102465(0, character=30100410)
    RunCommonEvent(0, 90005250, args=(30100420, 30102425, 0.0, 0), arg_types="IIfi")
    Event_30102400(2, character=30100420)
    Event_30102410(
        3,
        character=30100420,
        region=30102420,
        patrol_information_id=30103420,
        region_1=30102412,
        patrol_information_id_1=30103421
    )
    Event_30102465(1, character=30100420)
    Event_30102445()
    Event_30102450(slot=1)
    Event_30102455(slot=2)
    Event_30102460(slot=3)
    Event_30102470()
    Event_30102800()
    Event_30102810()
    Event_30102849()
    Event_30102811()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30100050()
    Event_30100519()


@NeverRestart(30100050)
def Event_30100050():
    """Event 30100050"""
    EndIfThisEventSlotFlagEnabled()


@NeverRestart(30100100)
def Event_30100100(_, flag: uint, obj: uint, obj_act_id: uint, obj_act_id_1: int):
    """Event 30100100"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfObjectActivated(AND_1, obj_act_id=obj_act_id)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(flag)
    ForceAnimation(obj, 1, unknown2=1.0)
    End()


@RestartOnRest(30102200)
def Event_30102200():
    """Event 30102200"""
    DeleteObjectVFX(30101300, erase_root=False)
    DeleteObjectVFX(30101301, erase_root=False)
    DeleteObjectVFX(30101500, erase_root=False)
    CreateObjectVFX(30101300, vfx_id=201, model_point=806721)
    CreateObjectVFX(30101301, vfx_id=201, model_point=806721)
    CreateObjectVFX(30101500, vfx_id=108, model_point=806721)
    End()


@RestartOnRest(30102400)
def Event_30102400(_, character: uint):
    """Event 30102400"""
    GotoIfFlagEnabled(Label.L0, flag=30102465)
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(30102300)
def Event_30102300(_, obj__obj_flag: uint, other_entity: uint):
    """Event 30102300"""
    EndIfFlagEnabled(30100465)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=PLAYER, radius=2.4000000953674316)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=other_entity, radius=2.4000000953674316)
    EndIfFlagEnabled(30100465)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(30100465)
    CreateHazard(
        obj_flag=obj__obj_flag,
        obj=obj__obj_flag,
        model_point=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=2.299999952316284,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveObjectFlag(obj_flag=obj__obj_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30102305)
def Event_30102305(_, obj__obj_flag: uint, other_entity: uint):
    """Event 30102305"""
    EndIfFlagEnabled(30100465)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=PLAYER, radius=3.0999999046325684)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=other_entity, radius=3.0999999046325684)
    EndIfFlagEnabled(30100465)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EndIfFlagEnabled(30100465)
    CreateHazard(
        obj_flag=obj__obj_flag,
        obj=obj__obj_flag,
        model_point=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=3.0999999046325684,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveObjectFlag(obj_flag=obj__obj_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30102410)
def Event_30102410(
    _,
    character: uint,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
):
    """Event 30102410"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterInsideRegion(MAIN, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    IfCharacterOutsideRegion(MAIN, character=character, region=region)
    Restart()


@RestartOnRest(30102445)
def Event_30102445():
    """Event 30102445"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30102405)
    IfFlagDisabled(AND_1, 30102445)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(30102460)
    DisableAI(30100400)
    EnableFlag(30102445)
    DisableFlag(30102450)
    DisableFlag(30102455)
    ForceAnimation(30100400, 20001, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Move(30100400, destination=30102460, destination_type=CoordEntityType.Region, set_draw_parent=30100400)
    ForceAnimation(30100400, 20000, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ChangePatrolBehavior(30100400, patrol_information_id=30103400)
    Wait(1.5)
    EnableAI(30100400)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(30102450)
def Event_30102450():
    """Event 30102450"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30102451)
    IfFlagDisabled(AND_1, 30102450)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(30102460)
    DisableAI(30100400)
    DisableFlag(30102445)
    EnableFlag(30102450)
    DisableFlag(30102455)
    ResetAnimation(30100400)
    ForceAnimation(30100400, 20001, loop=True, wait_for_completion=True, unknown2=1.0)
    Move(30100400, destination=30102461, destination_type=CoordEntityType.Region, set_draw_parent=30100400)
    ForceAnimation(30100400, 20000, loop=True, wait_for_completion=True, unknown2=1.0)
    ChangePatrolBehavior(30100400, patrol_information_id=30103450)
    Wait(1.5)
    EnableAI(30100400)
    Restart()


@RestartOnRest(30102455)
def Event_30102455():
    """Event 30102455"""
    EndIfPlayerNotInOwnWorld()
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30102452)
    IfFlagDisabled(AND_1, 30102455)
    IfFlagDisabled(AND_1, 30100550)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(30102460)
    IfFlagDisabled(AND_2, 30100503)
    IfFlagDisabled(AND_2, 30100500)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableAI(30100400)
    DisableFlag(30102445)
    EnableFlag(30102455)
    DisableFlag(30102450)
    ResetAnimation(30100400)
    ForceAnimation(30100400, 20001, loop=True, wait_for_completion=True, unknown2=1.0)
    Move(30100400, destination=30102462, destination_type=CoordEntityType.Region, set_draw_parent=30100400)
    ForceAnimation(30100400, 20000, loop=True, wait_for_completion=True, unknown2=1.0)
    ChangePatrolBehavior(30100400, patrol_information_id=30103451)
    Wait(1.5)
    EnableAI(30100400)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(30102460)
def Event_30102460():
    """Event 30102460"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(30102460)
    IfFlagEnabled(AND_2, 30100500)
    IfFlagDisabled(AND_2, 30100503)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfFlagDisabled(Label.L0, flag=30100500)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30102453)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=30100500)
    DisableAI(30100400)
    ResetAnimation(30100400)
    ForceAnimation(30100400, 20001, loop=True, wait_for_completion=True, unknown2=1.0)
    Move(30100400, destination=30102463, destination_type=CoordEntityType.Region, set_draw_parent=30100400)
    ForceAnimation(30100400, 20000, loop=True, wait_for_completion=True, unknown2=1.0)
    DisableFlag(30102445)
    EnableFlag(30102450)
    EnableFlag(30102455)
    EnableFlag(30102460)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(30102465)
def Event_30102465(_, character: uint):
    """Event 30102465"""
    IfFlagEnabled(AND_1, 30102460)
    IfCharacterInsideRegion(AND_1, character=character, region=30102470)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Kill(character)
    Kill(30100400)
    IfCharacterInsideRegion(AND_2, character=30100400, region=30102470)
    IfCharacterInsideRegion(AND_2, character=30100410, region=30102470)
    IfCharacterInsideRegion(AND_2, character=30100420, region=30102470)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableFlag(30100465)
    End()


@RestartOnRest(30102470)
def Event_30102470():
    """Event 30102470"""
    EndIfFlagEnabled(30102460)
    IfFlagEnabled(AND_1, 30102445)
    IfCharacterBackreadDisabled(AND_1, 30100400)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(30102445)
    Restart()


@RestartOnRest(30102480)
def Event_30102480():
    """Event 30102480"""
    EndIfFlagDisabled(30100465)
    DisableCharacter(30100400)
    DisableCharacter(30100410)
    DisableCharacter(30100420)
    End()


@RestartOnRest(30102490)
def Event_30102490():
    """Event 30102490"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(30107100)
    IfFlagEnabled(MAIN, 30100465)
    EndIfPlayerNotInOwnWorld()
    AwardItemLot(30100100, host_only=False)
    End()


@NeverRestart(30102510)
def Event_30102510():
    """Event 30102510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30100510,
            30100511,
            1,
            30101510,
            30101511,
            30103511,
            30101512,
            30103512,
            30102511,
            30102512,
            30100512,
            30100513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            30100515,
            30100516,
            3,
            30101515,
            30101516,
            30103516,
            30101517,
            30103517,
            30102516,
            30102517,
            30100517,
            30100518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30100519)
def Event_30100519():
    """Event 30100519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30100510)


@NeverRestart(30102500)
def Event_30102500():
    """Event 30102500"""
    RunCommonEvent(0, 90005681, args=(30100500, 30100501, 30100502, 30100503, 30101500), arg_types="IIIII")
    Event_30102521(0, 30100503, 30102500, 30100500)


@NeverRestart(30102520)
def Event_30102520(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30102520"""
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_4, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_5, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_6, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_7, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30102521)
def Event_30102521(_, flag: uint, region: uint, entity: uint):
    """Event 30102521"""
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=entity)
    SkipLinesIfFlagDisabled(6, 50)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 51)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 52)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 53)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 54)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103340,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103340,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103340,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 55)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103350,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 56)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103360,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103360,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103360,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(6, 57)
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103370,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=102,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103370,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=104,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103370,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30100500,
        source_entity=30101500,
        model_point=109,
        behavior_id=801103305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30102530)
def Event_30102530(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
    model_point_4: int,
    model_point_5: int,
    model_point_6: int,
    model_point_7: int,
):
    """Event 30102530"""
    IfFlagDisabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=region, right=0)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_1,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_2,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_3,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfValueComparison(Label.L5, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_4,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfValueComparison(Label.L6, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_5,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfValueComparison(Label.L7, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_6,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfValueComparison(Label.L8, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    SkipLinesIfValueEqual(2, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfValueEqual(2, left=behavior_id_1, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=model_point_7,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 8 --- #
    DefineLabel(8)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30102540)
def Event_30102540(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, attacked_entity: uint):
    """Event 30102540"""
    IfFlagEnabled(AND_13, flag)
    IfFlagEnabled(AND_13, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_13)
    IfFlagDisabled(AND_14, flag)
    IfFlagDisabled(AND_14, flag_1)
    IfConditionTrue(OR_15, input_condition=AND_14)
    IfConditionTrue(AND_15, input_condition=OR_15)
    IfFlagEnabled(AND_15, flag_3)
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    IfFlagDisabled(OR_1, flag)
    IfFlagEnabled(AND_2, flag_1)
    IfAttackedWithDamageType(AND_2, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_2, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=OR_1)
    IfConditionTrue(OR_4, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=OR_4)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(OR_5, flag)
    IfFlagDisabled(AND_6, flag_1)
    IfAttackedWithDamageType(AND_6, attacked_entity=attacked_entity, attacker=20000)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(OR_8, input_condition=OR_5)
    IfConditionTrue(OR_8, input_condition=OR_6)
    IfConditionTrue(MAIN, input_condition=OR_8)
    SkipLinesIfUnknown_203(line_count=2, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfUnknown_203(line_count=1, state=False, unk_2_3=0, unk_3_2=0, unk_4_3=0, unk_5_4=0, unk_6_5=0)
    DisableNetworkFlag(flag_3)
    DisableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    IfFlagDisabled(MAIN, flag_3)
    Restart()


@RestartOnRest(301002550)
def Event_301002550():
    """Event 301002550"""
    IfFlagEnabled(AND_1, 30100550)
    IfFlagDisabled(AND_1, 30100500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(30100550)
    Restart()


@RestartOnRest(30102560)
def Event_30102560():
    """Event 30102560"""
    GotoIfFlagEnabled(Label.L0, flag=30100500)
    DeleteVFX(30102463)
    Wait(5.0)
    CreateVFX(30102462)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(30102462)
    Wait(5.0)
    CreateVFX(30102463)
    Restart()


@NeverRestart(30102580)
def Event_30102580():
    """Event 30102580"""
    RegisterLadder(start_climbing_flag=30100580, stop_climbing_flag=30100581, obj=30101580)
    RegisterLadder(start_climbing_flag=30100582, stop_climbing_flag=30100583, obj=30101582)
    RegisterLadder(start_climbing_flag=30100584, stop_climbing_flag=30100585, obj=30101584)


@RestartOnRest(30102800)
def Event_30102800():
    """Event 30102800"""
    EndIfFlagEnabled(30100800)
    IfHealthValueLessThanOrEqual(AND_1, 30100800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 30100801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(30100800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 30100800)
    IfCharacterDead(AND_2, 30100801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    KillBossAndDisplayBanner(character=30100800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30100800)
    EnableFlag(9210)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61210)


@RestartOnRest(30102810)
def Event_30102810():
    """Event 30102810"""
    GotoIfFlagDisabled(Label.L0, flag=30100800)
    DisableCharacter(30100800)
    DisableAnimations(30100800)
    Kill(30100800)
    DisableCharacter(30100801)
    DisableAnimations(30100801)
    Kill(30100801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30100800)
    DisableAI(30100801)
    IfFlagEnabled(AND_2, 30102805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30102800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30100800)
    SetNetworkUpdateRate(30100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30100800, name=902500300)
    EnableAI(30100801)
    SetNetworkUpdateRate(30100801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30100801, name=902500301, bar_slot=1)


@RestartOnRest(30102811)
def Event_30102811():
    """Event 30102811"""
    EndIfFlagEnabled(30100800)
    IfCharacterDead(OR_1, 30100800)
    IfCharacterDead(OR_1, 30100801)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(30102802)


@RestartOnRest(30102849)
def Event_30102849():
    """Event 30102849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30100800, 30101800, 30102800, 30102805, 30105800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30100800, 30101800, 30102800, 30102805, 30102806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30100800, 30101800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30100800, 920200, 30102805, 30102806, 0, 30102802, 0, 0), arg_types="IiIIIIii")
