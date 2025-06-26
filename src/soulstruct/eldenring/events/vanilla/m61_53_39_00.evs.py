"""
Land of Shadow 13-09 NW NE

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2053390000, asset=2053391950)
    Event_2053392546()
    Event_2053392547()
    Event_2053392200(0, source_entity=2053390201, region=2053392200)
    Event_2053392200(1, source_entity=2053390202, region=2053392200)
    Event_2053392200(2, source_entity=2053390203, region=2053392200)
    Event_2053392200(3, source_entity=2053390204, region=2053392200)
    Event_2053392200(4, source_entity=2053390205, region=2053392200)
    Event_2053392200(5, source_entity=2053390206, region=2053392200)
    Event_2053392200(6, source_entity=2053390207, region=2053392200)
    Event_2053392300(
        0,
        character=580420,
        flag=580120,
        character_1=2053390300,
        animation_id=30015,
        animation_id_1=20015,
        asset=2053391500,
        asset_1=2053391501,
    )


@RestartOnRest(2053392200)
def Event_2053392200(_, source_entity: uint, region: Region | int):
    """Event 2053392200"""
    if FlagEnabled(2054390800):
        return
    DisableNetworkSync()
    CreateProjectileOwner(entity=source_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.5, max_seconds=5.0)
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


@RestartOnRest(2053392300)
def Event_2053392300(
    _,
    character: uint,
    flag: Flag | int,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    asset: uint,
    asset_1: Asset | int,
):
    """Event 2053392300"""
    AddSpecialEffect(character, 10124)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset_1)
    DisableFlag(2053392300)
    if FlagEnabled(character):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=15.0))
    
    MAIN.Await(AND_1)
    
    EnableAsset(asset)
    EnableAsset(asset_1)
    ForceAnimation(asset, 2)
    Wait(13.0)
    EnableCharacter(character_1)
    RemoveSpecialEffect(character, 10124)
    ForceAnimation(character_1, animation_id)
    EnableFlag(2053392300)
    AND_2.Add(FlagEnabled(2053392300))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_2)
    
    Wait(4.0)
    ForceAnimation(character_1, animation_id_1)
    ForceAnimation(asset, 1)
    Wait(3.799999952316284)
    DisableCharacter(character_1)
    DisableAsset(asset)
    EnableTreasure(asset=asset_1)


@RestartOnRest(2053392546)
def Event_2053392546():
    """Event 2053392546"""
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2053392546))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2053391546, 1)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208500,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208510,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208520,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208530,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208540,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208550,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208560,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804208570,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218500,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218510,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218520,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218530,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218540,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218550,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218560,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=2053392546,
            asset=2053391546,
            dummy_id=200,
            behavior_param_id=804218570,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(2053392547)
def Event_2053392547():
    """Event 2053392547"""
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2053392547))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2053391547, 1)
    GotoIfFlagEnabled(Label.L0, flag=70)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208500,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208510,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208520,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208530,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208540,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208550,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208560,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804208570,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218500,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(51):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218510,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(52):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218520,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(53):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218530,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(54):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218540,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(55):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218550,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(56):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218560,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )
    if FlagEnabled(57):
        CreateHazard(
            asset_flag=2053392547,
            asset=2053391547,
            dummy_id=200,
            behavior_param_id=804218570,
            target_type=DamageTargetType.Character,
            radius=4.0,
            life=20.0,
            repetition_time=0.0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
