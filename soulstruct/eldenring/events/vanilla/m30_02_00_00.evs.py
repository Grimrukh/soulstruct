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
    RegisterGrace(grace_flag=300200, obj=30021950, unknown=5.0)
    RunCommonEvent(
        0,
        90005646,
        args=(30020800, 30022840, 30022841, 30021840, 30022840, 30, 2, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_30022800()
    Event_30022810()
    Event_30022849()
    Event_30022811()
    RunCommonEvent(0, 90005550, args=(30020680, 30021680, 30023680), arg_types="III")
    RunCommonEvent(0, 90005650, args=(30020540, 30021540, 30021541, 30023541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30020540, 30021540), arg_types="II")
    RunCommonEvent(0, 90005680, args=(30020500, 30020501, 30020502, 30020503, 30021500), arg_types="IIIII")
    RunCommonEvent(0, 90005680, args=(30020505, 30020506, 30020507, 30020508, 30021505), arg_types="IIIII")
    Event_30022510()
    Event_30022580()
    RunCommonEvent(0, 90005706, args=(30020700, 930025, 30021700), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(30020700)
    RunCommonEvent(0, 90005211, args=(30020200, 30010, 20010, 30022200, 1.5, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(30020201, 30022201, 0.0, 0.0, 3006), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(30020202, 30010, 20010, 30022202, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30020203, 30010, 20010, 30022203, 1.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30020204, 30010, 20010, 30022204, 1.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30020205, 30003, 20003, 30022205, 1.0, 4.800000190734863, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30020206, 30003, 20003, 30022206, 0.0, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30020207, 30003, 20003, 30022206, 0.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30020208, 30002, 20002, 30022206, 0.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30020209, 30010, 20010, 30022206, 0.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30020210, 30010, 20010, 30022206, 0.0, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30020212, 30010, 20010, 30022212, 0.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30020213, 30010, 20010, 30022212, 0.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30020214, 30003, 20003, 30022214, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(30020215, 30022215, 1.0, 0.0, 0), arg_types="IIffi")
    Event_30020050()


@NeverRestart(30020050)
def Event_30020050():
    """Event 30020050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30020500)
    EnableFlag(30020505)


@NeverRestart(30022510)
def Event_30022510():
    """Event 30022510"""
    RunCommonEvent(0, 90005681, args=(30020500, 30020501, 30020502, 30020503, 30021500), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101070, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101060, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101050, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101040, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101030, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101020, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101010, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30020502, 30021500, 30022500, 30020500, 801101000, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    RunCommonEvent(0, 90005681, args=(30020505, 30020506, 30020507, 30020508, 30021505), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101070, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101060, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101050, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101040, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101030, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101020, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101010, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30020507, 30021505, 30022505, 30020505, 801101000, 801101005, 101, 0, 0, 0),
        arg_types="IIIIiiiiii",
    )


@NeverRestart(30022580)
def Event_30022580():
    """Event 30022580"""
    RegisterLadder(start_climbing_flag=30020580, stop_climbing_flag=30020581, obj=30021580)


@NeverRestart(30022610)
def Event_30022610(
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
    """Event 30022610"""
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
        behavior_id=801101000,
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
        behavior_id=801101005,
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
        behavior_id=801101000,
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
        behavior_id=801101005,
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
        behavior_id=801101000,
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
        behavior_id=801101005,
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
        behavior_id=801101000,
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
        behavior_id=801101005,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@RestartOnRest(30022650)
def Event_30022650(_, tutorial_param_id: int, flag: uint):
    """Event 30022650"""
    EndIfTryingToCreateSession()
    IfPlayerHasGood(OR_1, 215000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 240000, including_storage=True)
    IfPlayerHasGood(OR_1, 243000, including_storage=True)
    IfPlayerHasGood(OR_1, 234000, including_storage=True)
    IfPlayerHasGood(OR_1, 244000, including_storage=True)
    IfPlayerHasGood(OR_1, 236000, including_storage=True)
    IfPlayerHasGood(OR_1, 232000, including_storage=True)
    IfPlayerHasGood(OR_1, 212000, including_storage=True)
    IfPlayerHasGood(OR_1, 241000, including_storage=True)
    IfPlayerHasGood(OR_1, 213000, including_storage=True)
    IfPlayerHasGood(OR_1, 233000, including_storage=True)
    IfPlayerHasGood(OR_1, 245000, including_storage=True)
    IfLeavingSession(AND_1)
    IfPlayerDoesNotHaveGood(AND_1, 9111, including_storage=True)
    IfInsideMap(AND_1, game_map=STORMFOOT_CATACOMBS)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfTryingToCreateSession()
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(30022800)
def Event_30022800():
    """Event 30022800"""
    EndIfFlagEnabled(30020800)
    IfHealthValueLessThanOrEqual(MAIN, 30020800, value=0)
    Wait(4.0)
    PlaySoundEffect(30020800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30020800)
    KillBossAndDisplayBanner(character=30020800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30020800)
    EnableFlag(9202)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61202)


@RestartOnRest(30022810)
def Event_30022810():
    """Event 30022810"""
    GotoIfFlagDisabled(Label.L0, flag=30020800)
    DisableCharacter(30020800)
    DisableAnimations(30020800)
    Kill(30020800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30020800)
    IfFlagEnabled(AND_2, 30022805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30022800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(30020801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30020800)
    SetNetworkUpdateRate(30020800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30020800, name=904260301)


@RestartOnRest(30022811)
def Event_30022811():
    """Event 30022811"""
    EndIfFlagEnabled(30020800)
    IfHealthLessThanOrEqual(AND_1, 30020800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30022802)


@RestartOnRest(30022849)
def Event_30022849():
    """Event 30022849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30020800, 30021800, 30022800, 30022805, 30025800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30020800, 30021800, 30022800, 30022805, 30022806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30020800, 30021800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30020800, 930000, 30022805, 30022806, 0, 30022802, 0, 0), arg_types="IiIIIIii")
