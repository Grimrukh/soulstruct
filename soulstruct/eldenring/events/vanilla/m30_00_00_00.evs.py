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
    RegisterGrace(grace_flag=73000, obj=30001950, unknown=5.0)
    Event_30002800()
    Event_30002810()
    Event_30002829()
    Event_30002811()
    RunCommonEvent(0, 90005550, args=(30000620, 30001620, 30003620), arg_types="III")
    RunCommonEvent(0, 90005550, args=(30000621, 30001621, 30003621), arg_types="III")
    RunCommonEvent(0, 90005550, args=(30000622, 30001622, 30003622), arg_types="III")
    RunCommonEvent(0, 90005550, args=(30000623, 30001623, 30003623), arg_types="III")
    RunCommonEvent(0, 90005650, args=(30000540, 30001540, 30001541, 30003541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30000540, 30001540), arg_types="II")
    RunCommonEvent(0, 90005680, args=(30000500, 30000501, 30000502, 30000503, 30001500), arg_types="IIIII")
    Event_30002510()
    RunCommonEvent(
        0,
        90005620,
        args=(30000570, 30001570, 30001571, 0, 30002571, 30002572, 30002573),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005621, args=(30000570, 30001573), arg_types="II")
    RunCommonEvent(
        0,
        90005646,
        args=(30000800, 30002840, 30002841, 30001840, 30002840, 30, 0, 0, 0),
        arg_types="IIIIIBBbb",
    )


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30000050()
    RunCommonEvent(0, 90005211, args=(30000200, 30003, 20003, 30002200, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30000201, 30003, 20003, 30002201, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30000204, 30003, 20003, 8.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30000205, 30003, 20003, 30002205, 1.0, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30000206, 30003, 20003, 30002205, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30000207, 30003, 20003, 30002207, 1.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30000208, 30003, 20003, 30002207, 1.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30000211, 30003, 20003, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30000212, 30003, 20003, 30002212, 1.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30000213, 30003, 20003, 30002215, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005201, args=(30000214, 30003, 20003, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30000215, 30003, 20003, 30002215, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30000216, 30003, 20003, 30002215, 1.0, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30000217, 30003, 20003, 30002215, 1.0, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30000218, 30003, 20003, 30002215, 1.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005200, args=(30000223, 30003, 20003, 30002223, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30000224, 30003, 20003, 30002223, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005201, args=(30000225, 30003, 20003, 3.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(30000226, 3.0, 0.0, 0), arg_types="Iffi")


@NeverRestart(30000050)
def Event_30000050():
    """Event 30000050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30000500)


@NeverRestart(30002500)
def Event_30002500():
    """Event 30002500"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    EndOfAnimation(obj=30001500, animation_id=12)
    GotoIfFlagEnabled(Label.L0, flag=30000500)
    IfFlagDisabled(AND_1, 30000500)
    IfAttackedWithDamageType(AND_1, attacked_entity=30001500, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(30001500, 12, wait_for_completion=True, unknown2=1.0)
    EnableFlag(30000500)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_2, 30000500)
    IfAttackedWithDamageType(AND_2, attacked_entity=30001500, attacker=20000)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableFlag(30000500)
    ForceAnimation(30001500, 21, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(30009570)
def Event_30009570(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint, seconds: float):
    """Event 30009570"""
    IfFlagEnabled(OR_1, flag)
    IfPlayerNotInOwnWorld(OR_1)
    EndIfConditionTrue(input_condition=OR_1)
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    IfActionButtonParamActivated(MAIN, action_button_id=9220, entity=destination)
    DisplayDialogAndSetFlags(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    IfPlayerHasGood(AND_2, 8000)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050, unknown2=1.0)
    Wait(1.399999976158142)
    DisplayDialog(text=308000, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    RotateToFaceEntity(PLAYER, destination, animation=60010)
    Wait(seconds)
    DisplayDialog(text=208000, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8000, quantity=1)
    EnableNetworkFlag(flag)


@RestartOnRest(30002570)
def Event_30002570(_, flag: uint, obj: uint, obj_1: uint, obj_2: uint):
    """Event 30002570"""
    EndIfFlagEnabled(30002570)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1)
    DisableObject(obj_2)
    CreateObjectVFX(obj, vfx_id=200, model_point=806040)
    CreateObjectVFX(obj_1, vfx_id=101, model_point=806041)
    IfFlagEnabled(MAIN, flag)
    DeleteObjectVFX(obj_1, erase_root=False)
    Wait(2.0)
    DisableObject(obj_1)
    DisableObject(30001572)
    EnableObject(obj_2)
    DeleteObjectVFX(obj)
    DeleteObjectVFX(obj_1, erase_root=False)


@NeverRestart(30002610)
def Event_30002610(
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
    """Event 30002610"""
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
        behavior_id=801101200,
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
        behavior_id=801101205,
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
        behavior_id=801101200,
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
        behavior_id=801101205,
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
        behavior_id=801101200,
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
        behavior_id=801101205,
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
        behavior_id=801101200,
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
        behavior_id=801101205,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30002611)
def Event_30002611():
    """Event 30002611"""
    IfFlagEnabled(AND_1, 30000500)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30002500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateProjectileOwner(entity=30000500)
    ShootProjectile(
        owner_entity=30000500,
        source_entity=30001500,
        model_point=100,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30000500,
        source_entity=30001500,
        model_point=100,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30000500,
        source_entity=30001500,
        model_point=101,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=30000500,
        source_entity=30001500,
        model_point=101,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(6.0)
    Restart()


@NeverRestart(30002510)
def Event_30002510():
    """Event 30002510"""
    RunCommonEvent(0, 90005681, args=(30000500, 30000501, 30000502, 30000503, 30001500), arg_types="IIIII")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101270, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101260, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101250, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101240, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101230, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101220, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101210, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(
        0,
        90005682,
        args=(30000502, 30001500, 30002500, 30000500, 801101200, 801101205, 100, 101, 0, 0),
        arg_types="IIIIiiiiii",
    )


@RestartOnRest(30002800)
def Event_30002800():
    """Event 30002800"""
    EndIfFlagEnabled(30000800)
    IfHealthValueLessThanOrEqual(MAIN, 30000800, value=0)
    Wait(4.0)
    PlaySoundEffect(30008000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30000800)
    KillBossAndDisplayBanner(character=30000800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30000800)
    EnableFlag(9200)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61200)


@RestartOnRest(30002810)
def Event_30002810():
    """Event 30002810"""
    GotoIfFlagDisabled(Label.L0, flag=30000800)
    DisableCharacter(30005800)
    DisableAnimations(30005800)
    Kill(30005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30005800)
    IfFlagEnabled(AND_2, 30002805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30002800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(30005800)
    SetNetworkUpdateRate(30005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30000800, name=903664300)


@RestartOnRest(30002811)
def Event_30002811():
    """Event 30002811"""
    EndIfFlagEnabled(30000800)
    IfHealthLessThanOrEqual(AND_1, 30000800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30002802)


@RestartOnRest(30002829)
def Event_30002829():
    """Event 30002829"""
    RunCommonEvent(
        0,
        9005800,
        args=(30000800, 30001800, 30002800, 30002805, 30005800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30000800, 30001800, 30002800, 30002805, 30002806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30000800, 30001800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30000800, 930000, 30002805, 30002806, 0, 30002802, 0, 0), arg_types="IiIIIIii")
