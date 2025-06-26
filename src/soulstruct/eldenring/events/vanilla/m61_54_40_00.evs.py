"""
Land of Shadow 13-10 SE SW

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=2054400306, region=2054402306, radius=6.0, seconds=0.0, animation_id=0)
    Event_2054402200(0, source_entity=2054400200, region=2054402200)
    Event_2054402200(1, source_entity=2054400201, region=2054402200)
    Event_2054402200(2, source_entity=2054400202, region=2054402200)
    Event_2054402200(3, source_entity=2054400203, region=2054402200)
    Event_2054402200(4, source_entity=2054400204, region=2054402200)
    Event_2054402200(5, source_entity=2054400205, region=2054402200)
    Event_2054402200(6, source_entity=2054400206, region=2054402200)
    Event_2054402200(7, source_entity=2054400207, region=2054402200)
    Event_2054402200(8, source_entity=2054400208, region=2054402200)
    Event_2054402200(9, source_entity=2054400209, region=2054402200)


@RestartOnRest(2054402200)
def Event_2054402200(_, source_entity: uint, region: Region | int):
    """Event 2054402200"""
    if FlagEnabled(2054390800):
        return
    DisableNetworkSync()
    CreateProjectileOwner(entity=source_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=5.0)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008500,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008510,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008520,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008530,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008540,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008550,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008560,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804008570,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018500,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018510,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018520,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018530,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018540,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018550,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018560,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=source_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=804018570,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()
