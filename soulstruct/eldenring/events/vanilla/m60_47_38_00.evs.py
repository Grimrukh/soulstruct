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
    Event_1047382210()
    Event_1047382211(0, 1047381200, 2.0)
    Event_1047382211(1, 1047381201, 7.0)
    RunCommonEvent(
        0,
        90005605,
        args=(1047381610, 60, 50, 36, 0, 1050360602, 0, 1047382650, 1047382654, 1047382655, 0, 0, 0.0, 0.0),
        arg_types="IBBbbIiIIIIiff",
    )
    RunCommonEvent(
        0,
        90005620,
        args=(1047380570, 1047381570, 1047381571, 1047381572, 1047382570, 1047382571, 1047382572),
        arg_types="IIIIIIi",
    )
    Event_1047382569(0, flag=1047380570, obj=1047381573)
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004070, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004060, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004050, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004040, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004030, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004020, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004010, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1047382500, 1047381500, 200, 0, 802004000, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    RunCommonEvent(0, 900005610, args=(1047381650, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005636,
        args=(31218690, 1047380620, 1047381620, 4470, 1047382627, 1047382625, 1047382630, 1047383620, 0),
        arg_types="IIIiIIIIi",
    )
    RunCommonEvent(0, 90005637, args=(31218690, 1047380620, 1047382625), arg_types="III")
    RunCommonEvent(0, 90005251, args=(1047380294, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1047380296, 1047382296, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005300, args=(1047380299, 1047380299, 1047380700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005250, args=(1047380301, 1047382453, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1047380302, 1047382302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1047380306, 1047382302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1047380307, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1047380312, 1047382302, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1047380450, 1047382450, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(1047382459, 15.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(1047380474, 1047382474, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005513,
        args=(1047380540, 1047381540, 1047381541, 1047383541, 99026, 1, 2),
        arg_types="IIIIiii",
    )
    Event_1047381580()
    RunCommonEvent(0, 90005706, args=(1047380701, 930025, 1047381700), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1047380700)
    DisableBackread(1047380701)


@RestartOnRest(1047382210)
def Event_1047382210():
    """Event 1047382210"""
    CreateProjectileOwner(entity=1047380298)


@RestartOnRest(1047382211)
def Event_1047382211(_, source_entity: uint, seconds: float):
    """Event 1047382211"""
    EnableNetworkSync()
    Wait(8.0)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    Wait(seconds)
    IfNewGameCycleEqual(AND_1, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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
        owner_entity=1047380298,
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


@NeverRestart(1047382569)
def Event_1047382569(_, flag: uint, obj: uint):
    """Event 1047382569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806043)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@NeverRestart(1047381580)
def Event_1047381580():
    """Event 1047381580"""
    RegisterLadder(start_climbing_flag=1047380580, stop_climbing_flag=1047380581, obj=1047381580)
    RegisterLadder(start_climbing_flag=1047380582, stop_climbing_flag=1047380583, obj=1047381582)
    RegisterLadder(start_climbing_flag=1047380584, stop_climbing_flag=1047380585, obj=1047381584)
