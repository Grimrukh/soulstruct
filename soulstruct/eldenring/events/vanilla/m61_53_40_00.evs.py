"""
Land of Shadow 13-10 SW SE

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
from soulstruct.eldenring.game_types import *


@RestartOnRest(2053402200)
def Event_2053402200(_, source_entity: uint, region: Region | int):
    """Event 2053402200"""
    if FlagEnabled(2054390800):
        return
    DisableNetworkSync()
    CreateProjectileOwner(entity=source_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
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
    Wait(1.0)
    Restart()
