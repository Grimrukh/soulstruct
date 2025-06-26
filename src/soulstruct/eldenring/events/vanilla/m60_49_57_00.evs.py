"""
Northwest Mountaintops (SW) (NE)

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
from .enums.m60_49_57_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian0,
        animation_id=30003,
        animation_id_1=20003,
        region=1049572251,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian1,
        animation_id=30003,
        animation_id_1=20003,
        region=1049572251,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.ErdtreeGuardian6,
        animation_id=30003,
        animation_id_1=20003,
        region=1049572259,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=1049570300, character=Characters.LargeScarab, item_lot=1049570710, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1049570310, character=Characters.Scarab, item_lot=1049570700, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=1049570320,
        character=Characters.ExtraLargeScarab,
        item_lot=1049570720,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LargeScarab,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Scarab,
        animation_id=30000,
        animation_id_1=20000,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1049572350(0, source_entity=1049572351)
    Event_1049572350(1, source_entity=1049572351)
    Event_1049572350(2, source_entity=1049572352)


@RestartOnRest(1049572350)
def Event_1049572350(_, source_entity: uint):
    """Event 1049572350"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1049572350))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105210,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105220,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105230,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105240,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105250,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105260,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=source_entity,
            dummy_id=900,
            behavior_id=802105270,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()
