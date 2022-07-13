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
    RegisterGrace(grace_flag=1048380000, obj=1048381950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76406, 1048381980, 77400, 4, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RegisterGrace(grace_flag=1048380001, obj=1048381951, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76407, 1048381981, 77400, 3, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005631, args=(1048381600, 61040), arg_types="Ii")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1048380180, 1048382181, 1048382182, 1048380700, 23, 1048382705, 1048382706, 0.0, 1050389259, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1048380180, 1048382181, 1048382182, 1048380700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1048380180, 1048382181, 1048382182, 1048380700, 1048380500, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1048380180, 1048382181, 1048382182, 1048380700, 1048382705, 0, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005300, args=(1048380290, 1048380290, 40402, 0.0, 0), arg_types="IIifi")
    Event_1048382201()
    Event_1048382200(0, 1048381200, 2.0)
    Event_1048382200(1, 1048381201, 4.0)
    Event_1048382200(2, 1048381202, 14.0)
    Event_1048382200(3, 1048381203, 5.0)
    Event_1048382200(4, 1048381204, 9.0)
    RunCommonEvent(0, 90005250, args=(1048380200, 1048382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048380201, 1048382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1048380202, 1048382200, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(1048380203, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380204, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380205, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380206, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380207, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380208, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380209, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380210, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1048380211, 30000, 20000, 8.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(1048380212, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1048380213, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1048380300, 1048382300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005725,
        args=(4775, 4776, 4778, 1048389205, 1048380705, 1048380706, 1048386700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1048380705, 4776, 4777, 1048389206, 4776, 4775, 4779, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1048380705, 4776, 4775, 1048389206, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1048380705, 4778, 4775, 4779), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1048380706, 4776, 4777, 1048389207, 4776, 4775, 4779, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1048380706, 4776, 4775, 1048389207, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1048380706, 1048382706, 1048382707), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4776, 1048380705, 1048380706, 4775, 4778), arg_types="IIIII")
    RunCommonEvent(0, 90005729, args=(1048389200, 1048380705, 54.0, 1048382702), arg_types="IIfI")
    RunCommonEvent(0, 90005706, args=(1048380701, 930023, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1048380700)
    DisableBackread(1048380705)
    DisableBackread(1048380706)
    DisableBackread(1048380710)
    DisableBackread(1048380701)


@RestartOnRest(1048382200)
def Event_1048382200(_, source_entity: uint, seconds: float):
    """Event 1048382200"""
    EnableNetworkSync()
    Wait(8.0)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    Wait(seconds)
    IfNewGameCycleEqual(AND_1, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_2, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_3, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_4, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_5, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleGreaterThanOrEqual(AND_8, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=1048380299,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(1048382201)
def Event_1048382201():
    """Event 1048382201"""
    CreateProjectileOwner(entity=1048380299)
