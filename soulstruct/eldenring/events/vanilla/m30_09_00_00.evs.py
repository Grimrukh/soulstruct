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
    RegisterGrace(grace_flag=73009, obj=30091950, unknown=5.0)
    Event_30090100(0, flag=30090540, obj=30091540, obj_act_id=30093540, obj_act_id_1=27041)
    RunCommonEvent(
        0,
        90005501,
        args=(30090510, 30091510, 2, 30091510, 30091511, 30091512, 30090511),
        arg_types="IIIIIII",
    )
    Event_30092510()
    RunCommonEvent(0, 90005680, args=(30090500, 30090501, 30090502, 30090503, 30091500), arg_types="IIIII")
    Event_30092500()
    Event_30092580()
    RunCommonEvent(0, 90005616, args=(30097000, 30092700), arg_types="II")
    RunCommonEvent(0, 90005250, args=(30090200, 30092200, 0.20000000298023224, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30090201, 30092200, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30090205, 30003, 20003, 30092205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30090206, 30092206, 0.0, 3000), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090219, 30092219, 0.0, 3026), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30090210, 30003, 20003, 30092210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30090211, 30003, 20003, 30092210, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30090215, 30003, 20003, 30092215, 1.2999999523162842, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(2, 90005200, args=(30090217, 30003, 20003, 30092215, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30090234, 30092230, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(30090230, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(1, 90005221, args=(30090231, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(2, 90005221, args=(30090232, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(3, 90005221, args=(30090233, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(30090235, 30000, 20000, 30092235, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30090236, 30000, 20000, 30092235, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30090239, 30092258, 0.0, 701), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(30090240, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005250, args=(30090250, 30092250, 0.0, 3009), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30090251, 30092250, 3.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090258, 30092258, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090254, 30092254, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090255, 30092254, 0.0, 3010), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090270, 30092270, 0.0, 5003), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30090301, 30092301, 0.0, 5003), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090300, 30092300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30090400, 30092400, 1.0, -1), arg_types="IIfi")
    Event_30092400(0, character=30090400)
    Event_30092410(
        0,
        character=30090400,
        region=30092431,
        patrol_information_id=30093420,
        region_1=30092421,
        patrol_information_id_1=30093421
    )
    RunCommonEvent(0, 90005250, args=(30090410, 30092410, 0.0, -1), arg_types="IIfi")
    Event_30092400(1, character=30090410)
    Event_30092399()
    Event_30092410(
        3,
        character=30090410,
        region=30092451,
        patrol_information_id=30093440,
        region_1=30092441,
        patrol_information_id_1=30093441
    )
    Event_30092410(
        4,
        character=30090410,
        region=30092452,
        patrol_information_id=30093441,
        region_1=30092442,
        patrol_information_id_1=30093442
    )
    Event_30092800()
    Event_30092810()
    Event_30092849()
    Event_30092811()
    RunCommonEvent(
        0,
        90005646,
        args=(30090800, 30092840, 30092841, 30091840, 30092840, 30, 9, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_30090790(0, 30091670, 30090800)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30090050()
    Event_30090519()


@NeverRestart(30090050)
def Event_30090050():
    """Event 30090050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30090500)


@NeverRestart(30090100)
def Event_30090100(_, flag: uint, obj: uint, obj_act_id: uint, obj_act_id_1: int):
    """Event 30090100"""
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


@NeverRestart(30092510)
def Event_30092510():
    """Event 30092510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30090510,
            30091510,
            2,
            30091510,
            30091511,
            30093511,
            30091512,
            30093512,
            30092511,
            30092512,
            30090511,
            30092512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30090519)
def Event_30090519():
    """Event 30090519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30090510)


@RestartOnRest(30092500)
def Event_30092500():
    """Event 30092500"""
    RunCommonEvent(0, 90005681, args=(30090500, 30090501, 30090502, 30090503, 30091500), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103270, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103260, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103250, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103240, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103230, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103220, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103210, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30090502, 30091500, 30092500, 30090500, 801103200, 801103205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )


@RestartOnRest(30092300)
def Event_30092300(_, obj__obj_flag: uint, other_entity: uint):
    """Event 30092300"""
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=PLAYER, radius=2.4000000953674316)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=other_entity, radius=2.4000000953674316)
    IfConditionTrue(MAIN, input_condition=OR_1)
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


@RestartOnRest(30092305)
def Event_30092305(_, obj__obj_flag: uint, other_entity: uint):
    """Event 30092305"""
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=PLAYER, radius=3.0999999046325684)
    IfEntityWithinDistance(OR_1, entity=obj__obj_flag, other_entity=other_entity, radius=3.0999999046325684)
    IfConditionTrue(MAIN, input_condition=OR_1)
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


@RestartOnRest(30092399)
def Event_30092399():
    """Event 30092399"""
    SetDisplayMask(30090410, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(30090410, bit_index=11, switch_type=OnOffChange.On)
    SetCollisionMask(30090410, bit_index=5, switch_type=OnOffChange.On)
    AttachObjectToCharacter(character=30090410, model_point=110, obj=30091410)


@RestartOnRest(30092400)
def Event_30092400(_, character: uint):
    """Event 30092400"""
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    End()


@RestartOnRest(30092410)
def Event_30092410(
    _,
    character: uint,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
):
    """Event 30092410"""
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


@NeverRestart(30092580)
def Event_30092580():
    """Event 30092580"""
    RegisterLadder(start_climbing_flag=30090580, stop_climbing_flag=30090581, obj=30091580)
    RegisterLadder(start_climbing_flag=30090582, stop_climbing_flag=30090583, obj=30091582)


@NeverRestart(30092610)
def Event_30092610(
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
):
    """Event 30092610"""
    IfFlagEnabled(AND_1, flag)
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
        behavior_id=801103200,
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
        behavior_id=801103205,
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
        behavior_id=801103200,
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
        behavior_id=801103205,
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
        behavior_id=801103200,
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
        behavior_id=801103205,
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
        behavior_id=801103200,
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
        behavior_id=801103205,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@RestartOnRest(30090790)
def Event_30090790(_, obj: uint, flag: uint):
    """Event 30090790"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfThisEventSlotFlagDisabled(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    EnableObjectActivation(obj, obj_act_id=-1)
    End()


@RestartOnRest(30092800)
def Event_30092800():
    """Event 30092800"""
    EndIfFlagEnabled(30090800)
    IfHealthValueLessThanOrEqual(MAIN, 30090800, value=0)
    Wait(4.0)
    PlaySoundEffect(30090800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30090800)
    KillBossAndDisplayBanner(character=30090800, banner_type=BannerType.DutyFulfilled)
    EnableObjectActivation(30091520, obj_act_id=-1)
    EnableFlag(30090800)
    EnableFlag(9209)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61209)


@RestartOnRest(30092810)
def Event_30092810():
    """Event 30092810"""
    GotoIfFlagDisabled(Label.L0, flag=30090800)
    DisableCharacter(30090800)
    DisableAnimations(30090800)
    Kill(30090800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30090800)
    EnableObjectActivation(30091520, obj_act_id=-1)
    IfFlagEnabled(AND_2, 30092805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30092800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30090800)
    SetNetworkUpdateRate(30090800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30090800, name=903181300)


@RestartOnRest(30092811)
def Event_30092811():
    """Event 30092811"""
    EndIfFlagEnabled(30090800)
    IfHealthLessThanOrEqual(AND_1, 30090800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30092802)


@RestartOnRest(30092849)
def Event_30092849():
    """Event 30092849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30090800, 30091800, 30092800, 30092805, 30095800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30090800, 30091800, 30092800, 30092805, 30092806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30090800, 30091800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30090800, 921400, 30092805, 30092806, 0, 30092802, 0, 0), arg_types="IiIIIIii")
