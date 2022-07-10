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
    RunCommonEvent(
        0,
        90005646,
        args=(30030800, 30032840, 30032841, 30031840, 30032840, 30, 3, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=300300, obj=30031950, unknown=5.0)
    Event_30032800()
    Event_30032810()
    Event_30032849()
    Event_30032821()
    Event_30032838()
    Event_30032890()
    Event_30032845()
    Event_30032870(0, character=30030801, flag=30032882)
    Event_30032871(0, character=30030802, flag=30032883)
    Event_30032871(1, character=30030803, flag=30032884)
    Event_30032871(2, character=30030804, flag=30032884)
    Event_30032871(3, character=30030805, flag=30032885)
    Event_30032871(4, character=30030806, flag=30032885)
    Event_30032871(5, character=30030807, flag=30032886)
    Event_30032871(6, character=30030808, flag=30032886)
    Event_30032871(7, character=30030809, flag=30032887)
    Event_30032871(8, character=30030810, flag=30032887)
    RunCommonEvent(0, 90005650, args=(30030540, 30031540, 30031541, 30033541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30030540, 30031540), arg_types="II")
    Event_30032400(
        0,
        owner_entity=30030600,
        entity=30031600,
        region=30032600,
        behavior_id=0,
        source_entity=30032601,
        source_entity_1=30032602,
        source_entity_2=30032603
    )
    RunCommonEvent(0, 90005525, args=(30030570, 30031570), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030571, 30031571), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030572, 30031572), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030573, 30031573), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030574, 30031574), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030575, 30031575), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030576, 30031576), arg_types="II")
    RunCommonEvent(0, 90005525, args=(30030577, 30031577), arg_types="II")
    Event_30032579()
    RunCommonEvent(0, 90005410, args=(30032100, 30031100, 30035100), arg_types="III")
    RunCommonEvent(0, 90005411, args=(30031100, 30030100, 10), arg_types="III")
    RunCommonEvent(0, 91005600, args=(30030800, 30031695, 3), arg_types="IIi")
    RunCommonEvent(0, 90005920, args=(30030520, 30031520, 30033520), arg_types="III")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30030050()
    RunCommonEvent(0, 90005250, args=(30030200, 30032200, 0.0, 3005), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(30030201, 30032201, 1.0, 0.0, 3012), arg_types="IIffi")
    RunCommonEvent(0, 90005211, args=(30030202, 30010, 20010, 30032202, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005200, args=(30030203, 30001, 20001, 30032203, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(30030204, 30010, 20010, 15.0, 2.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_30032205(0, 30030205, 30010, 20010, 30032204, 1.0, 0.0, 0, 0, 0, 0)
    Event_30032205(1, 30030206, 30010, 20010, 30032204, 1.0, 0.0, 0, 0, 0, 0)
    RunCommonEvent(0, 90005250, args=(30030207, 30032207, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30030208, 30032208, 0.0, 0), arg_types="IIfi")
    Event_30032207(0, character=30030207, region=30032307)
    Event_30032207(1, character=30030208, region=30032308)
    Event_30032207(2, character=30030209, region=30032307)
    RunCommonEvent(0, 90005200, args=(30030209, 30002, 20002, 30032207, 3.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@NeverRestart(30030050)
def Event_30030050():
    """Event 30030050"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(30030500)


@RestartOnRest(30032579)
def Event_30032579():
    """Event 30032579"""
    DisableObject(30031575)


@RestartOnRest(30032400)
def Event_30032400(
    _,
    owner_entity: uint,
    entity: uint,
    region: uint,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 30032400"""
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(entity, 1, wait_for_completion=True, unknown2=1.0)
    Wait(0.5)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.6000000238418579)
    SkipLinesIfValueEqual(4, left=behavior_id, right=0)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    SkipLinesIfFlagDisabled(3, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(3, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=801032070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    IfAllPlayersOutsideRegion(MAIN, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(30032205)
def Event_30032205(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30032205"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    DisableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    SkipLinesIfUnsignedEqual(1, left=0, right=region)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfCharacterBackreadEnabled(AND_1, character)
    IfCharacterHasSpecialEffect(OR_11, character, 5080)
    IfCharacterHasSpecialEffect(OR_11, character, 5450)
    IfConditionTrue(AND_1, input_condition=OR_11)
    IfUnsignedEqual(AND_9, left=left_1, right=0)
    IfUnsignedEqual(AND_9, left=left_2, right=0)
    IfUnsignedEqual(AND_9, left=left_3, right=0)
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    SkipLinesIfUnsignedEqual(1, left=left_1, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Battle)
    SkipLinesIfUnsignedEqual(1, left=left_2, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown5)
    SkipLinesIfUnsignedEqual(1, left=left_3, right=0)
    IfHasAIStatus(OR_9, character, ai_status=AIStatusType.Unknown4)
    IfConditionTrue(AND_1, input_condition=OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    Wait(2.0)
    ForceAnimation(character, 3016, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    EnableGravity(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(30032207)
def Event_30032207(_, character: uint, region: uint):
    """Event 30032207"""
    IfCharacterDead(OR_15, character)
    IfThisEventSlotFlagEnabled(OR_15)
    EndIfConditionTrue(input_condition=OR_15)
    AddSpecialEffect(character, 17155)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfConditionTrue(MAIN, input_condition=OR_2)
    CancelSpecialEffect(character, 17155)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30032800)
def Event_30032800():
    """Event 30032800"""
    EndIfFlagEnabled(30030800)
    IfHealthValueLessThanOrEqual(MAIN, 30030800, value=0)
    Kill(30030801)
    Kill(30030802)
    Kill(30030803)
    Kill(30030804)
    Kill(30030805)
    Kill(30030806)
    Kill(30030807)
    Kill(30030808)
    Kill(30030809)
    Kill(30030810)
    DisableSpawner(entity=30033801)
    DisableSpawner(entity=30033802)
    DisableSpawner(entity=30033803)
    DisableSpawner(entity=30033804)
    DisableSpawner(entity=30033805)
    DisableSpawner(entity=30033806)
    Wait(4.0)
    PlaySoundEffect(30030800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30030800)
    KillBossAndDisplayBanner(character=30030800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30030800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61206)
    EnableFlag(9206)


@RestartOnRest(30032810)
def Event_30032810():
    """Event 30032810"""
    GotoIfFlagDisabled(Label.L0, flag=30030800)
    DisableCharacter(30030800)
    DisableAnimations(30030800)
    Kill(30030800)
    Kill(30030801)
    DisableSpawner(entity=30033801)
    DisableSpawner(entity=30033802)
    DisableSpawner(entity=30033803)
    DisableSpawner(entity=30033804)
    DisableSpawner(entity=30033805)
    DisableSpawner(entity=30033806)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30030800)
    SkipLinesIfPlayerNotInOwnWorld(1)
    ForceAnimation(30030800, 30013, unknown2=1.0)
    IfFlagEnabled(AND_2, 30032805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30032800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(30030800)
    SetNetworkUpdateRate(30030800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30030800, name=904140300)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    DisableNetworkConnectedFlagRange(flag_range=(30032822, 30032839))
    EnableNetworkFlag(30032822)
    EnableNetworkFlag(30032839)
    Wait(1.2000000476837158)
    EnableFlag(30032812)
    MakeEnemyAppear(character=30033801)
    EnableNetworkFlag(30032882)
    ForceAnimation(30030800, 20013, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(30032849)
def Event_30032849():
    """Event 30032849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30030800, 30031800, 30032800, 30032805, 30035800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30030800, 30031800, 30032800, 30032805, 30032806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30030800, 30031800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30030800, 920200, 30032805, 30032806, 0, 30032860, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30032890)
def Event_30032890():
    """Event 30032890"""
    DisableNetworkSync()
    EndIfFlagEnabled(30030800)
    EndIfPlayerNotInOwnWorld()
    AwaitFlagEnabled(flag=30032805)
    GotoIfFlagEnabled(Label.L1, flag=30032813)
    IfCharacterDead(MAIN, 30030801)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)
    IfHealthLessThan(AND_1, 30030800, value=0.8999999761581421)
    SkipLinesIfConditionTrue(4, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(30032822, 30032839))
    EnableNetworkFlag(30032822)
    EnableNetworkFlag(30032839)
    Goto(Label.L0)
    DisableNetworkFlag(30032822)
    EnableNetworkFlag(30032813)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=30032814)
    IfCharacterDead(MAIN, 30030802)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)
    EnableNetworkFlag(30032814)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L10, flag=30032815)
    IfCharacterDead(AND_9, 30030803)
    IfCharacterDead(AND_9, 30030804)
    IfConditionTrue(MAIN, input_condition=AND_9)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)
    EnableNetworkFlag(30032815)
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L11, flag=30032816)
    IfCharacterDead(AND_10, 30030805)
    IfCharacterDead(AND_10, 30030806)
    IfConditionTrue(MAIN, input_condition=AND_10)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)
    EnableNetworkFlag(30032816)
    Goto(Label.L0)

    # --- Label 11 --- #
    DefineLabel(11)
    GotoIfFlagEnabled(Label.L12, flag=30032817)
    IfCharacterDead(AND_2, 30030807)
    IfCharacterDead(AND_2, 30030808)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)
    EnableNetworkFlag(30032817)
    Goto(Label.L0)

    # --- Label 12 --- #
    DefineLabel(12)
    IfCharacterDead(AND_11, 30030809)
    IfCharacterDead(AND_11, 30030810)
    IfConditionTrue(MAIN, input_condition=AND_11)
    Wait(1.0)
    AddSpecialEffect(30030800, 15044)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(MAIN, 30030800, 15007)
    IfHealthGreaterThanOrEqual(AND_3, 30030800, value=0.8999999761581421)
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    MakeEnemyAppear(character=30033801)
    IfCharacterAlive(MAIN, 30030801)
    EnableNetworkFlag(30032882)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L9, flag=30032817)
    MakeEnemyAppear(character=30033806)
    IfCharacterAlive(AND_8, 30030809)
    IfCharacterAlive(AND_8, 30030810)
    IfConditionTrue(MAIN, input_condition=AND_8)
    EnableNetworkFlag(30032887)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L8, flag=30032816)
    MakeEnemyAppear(character=30033805)
    IfCharacterAlive(AND_6, 30030807)
    IfCharacterAlive(AND_6, 30030808)
    IfConditionTrue(MAIN, input_condition=AND_6)
    EnableNetworkFlag(30032886)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagDisabled(Label.L4, flag=30032815)
    MakeEnemyAppear(character=30033804)
    IfCharacterAlive(AND_5, 30030805)
    IfCharacterAlive(AND_5, 30030806)
    IfConditionTrue(MAIN, input_condition=AND_5)
    EnableNetworkFlag(30032885)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L5, flag=30032814)
    MakeEnemyAppear(character=30033803)
    EnableFlag(30032860)
    IfCharacterAlive(AND_7, 30030803)
    IfCharacterAlive(AND_7, 30030804)
    IfConditionTrue(MAIN, input_condition=AND_7)
    EnableNetworkFlag(30032884)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagDisabled(Label.L6, flag=30032813)
    MakeEnemyAppear(character=30033802)
    IfCharacterAlive(MAIN, 30030802)
    EnableNetworkFlag(30032883)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagDisabled(Label.L7, flag=30032812)
    MakeEnemyAppear(character=30033801)
    EnableNetworkFlag(30032882)
    IfCharacterAlive(MAIN, 30030801)
    AddSpecialEffect(30030800, 15045)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)


@RestartOnRest(30032845)
def Event_30032845():
    """Event 30032845"""
    DisableNetworkSync()
    EndIfFlagEnabled(30030800)
    EndIfPlayerNotInOwnWorld()
    IfHealthLessThan(MAIN, 30030800, value=0.8999999761581421)
    DisableNetworkFlag(30032822)
    EnableNetworkFlag(30032834)


@RestartOnRest(30032821)
def Event_30032821():
    """Event 30032821"""
    DisableNetworkSync()
    EndIfFlagEnabled(30030800)
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(AND_15, 30030800, 15046)
    IfFlagEnabled(AND_15, 30032839)
    IfConditionTrue(MAIN, input_condition=AND_15)
    IfHealthGreaterThanOrEqual(OR_15, 30030800, value=0.8999999761581421)
    GotoIfConditionTrue(Label.L0, input_condition=OR_15)
    GotoIfFlagEnabled(Label.L0, flag=30032822)
    GotoIfFlagEnabled(Label.L1, flag=30032823)
    GotoIfFlagEnabled(Label.L1, flag=30032824)
    GotoIfFlagEnabled(Label.L1, flag=30032825)
    GotoIfFlagEnabled(Label.L2, flag=30032826)
    GotoIfFlagEnabled(Label.L2, flag=30032827)
    GotoIfFlagEnabled(Label.L2, flag=30032828)
    GotoIfFlagEnabled(Label.L3, flag=30032829)
    GotoIfFlagEnabled(Label.L3, flag=30032830)
    GotoIfFlagEnabled(Label.L3, flag=30032831)
    GotoIfFlagEnabled(Label.L4, flag=30032832)
    GotoIfFlagEnabled(Label.L4, flag=30032833)
    GotoIfFlagEnabled(Label.L4, flag=30032834)

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032829, 30032834))
    DisableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032829, 30032834))
    DisableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032823, 30032828))
    DisableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032823, 30032828))
    DisableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()


@NeverRestart(30032838)
def Event_30032838():
    """Event 30032838"""
    DisableNetworkSync()
    EndIfFlagEnabled(30030800)
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(30032823, 30032834))
    IfFlagDisabled(AND_1, 30032839)
    IfCharacterHasSpecialEffect(AND_1, 30030800, 15046)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=30032822)
    GotoIfFlagEnabled(Label.L1, flag=30032823)
    GotoIfFlagEnabled(Label.L2, flag=30032824)
    GotoIfFlagEnabled(Label.L3, flag=30032825)
    GotoIfFlagEnabled(Label.L4, flag=30032826)
    GotoIfFlagEnabled(Label.L5, flag=30032827)
    GotoIfFlagEnabled(Label.L6, flag=30032828)
    GotoIfFlagEnabled(Label.L7, flag=30032829)
    GotoIfFlagEnabled(Label.L8, flag=30032830)
    GotoIfFlagEnabled(Label.L9, flag=30032831)
    GotoIfFlagEnabled(Label.L10, flag=30032832)
    GotoIfFlagEnabled(Label.L11, flag=30032833)
    GotoIfFlagEnabled(Label.L12, flag=30032834)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(30032839)
    DisableNetworkFlag(30032822)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Move(30030800, destination=30032823, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(30030800, destination=30032824, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    Move(30030800, destination=30032825, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    Move(30030800, destination=30032826, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    Move(30030800, destination=30032827, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    Move(30030800, destination=30032828, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    Move(30030800, destination=30032829, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    Move(30030800, destination=30032830, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    Move(30030800, destination=30032831, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    Move(30030800, destination=30032832, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    Move(30030800, destination=30032833, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()

    # --- Label 12 --- #
    DefineLabel(12)
    Move(30030800, destination=30032834, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    IfCharacterDoesNotHaveSpecialEffect(MAIN, 30030800, 15046)
    Restart()


@RestartOnRest(30032870)
def Event_30032870(_, character: uint, flag: uint):
    """Event 30032870"""
    EndIfFlagEnabled(30030800)
    IfFlagEnabled(AND_1, flag)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    ActivateMultiplayerBuffs(character)
    IfCharacterDead(MAIN, character)
    Restart()


@RestartOnRest(30032871)
def Event_30032871(_, character: uint, flag: uint):
    """Event 30032871"""
    EndIfFlagEnabled(30030800)
    IfFlagEnabled(AND_1, flag)
    IfCharacterAlive(AND_1, character)
    IfConditionTrue(AND_2, input_condition=AND_1)
    IfLeavingSession(AND_3)
    IfConditionFalse(AND_2, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=AND_2)
    ActivateMultiplayerBuffs(character)
    Wait(1.0)
    IfCharacterHasSpecialEffect(OR_1, character, 7820)
    IfCharacterHasSpecialEffect(OR_1, character, 7821)
    IfCharacterHasSpecialEffect(OR_1, character, 7822)
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()
