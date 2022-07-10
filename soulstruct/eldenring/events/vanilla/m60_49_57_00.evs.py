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
        90005211,
        args=(1049570251, 30003, 20003, 1049572251, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1049570252, 30003, 20003, 1049572251, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1049570259, 30003, 20003, 1049572259, 1.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005300, args=(1049570300, 1049570300, 1049570710, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1049570310, 1049570310, 1049570700, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1049570320, 1049570320, 1049570720, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005201, args=(1049570300, 30000, 20000, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1049570310, 30000, 20000, 4.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1049572350(0, source_entity=1049572351)
    Event_1049572350(1, source_entity=1049572351)
    Event_1049572350(2, 1049572352)


@RestartOnRest(1049572350)
def Event_1049572350(_, source_entity: uint):
    """Event 1049572350"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=1049570350)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1049572350)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1049570350,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802105270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()
