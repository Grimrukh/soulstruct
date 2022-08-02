"""
Northwest Liurnia (SE) (SE)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_35_48_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1035482210(0, character=1035480220)
    Event_1035482210(1, character=1035480230)
    Event_1035482270()
    Event_1035482270(slot=1)
    Event_1035482280()
    Event_1035482280(slot=1)
    Event_1035482260(
        0,
        flag=1035480250,
        destination=Assets.AEG099_160_9000,
        character=Characters.Balloon,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1035482261(
        0,
        flag=1035480250,
        asset=Assets.AEG099_160_9000,
        character=Characters.Balloon,
        character_1=1035485260,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1035480100,
        flag_1=1035482250,
    )
    Event_1035482262(
        0,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1035482250,
    )
    Event_1035482262(
        1,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1035482250,
    )
    Event_1035482262(
        3,
        character=Characters.Balloon,
        seconds=0.0,
        attacked_entity=Characters.Balloon,
        seconds_1=0.0,
        character_1=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1035482250,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005201(
        0,
        character=Characters.LargeCrabSnow,
        animation_id=30001,
        animation_id_1=20001,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.LargeCrabSnow, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaSoldier, radius=1.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1035482210)
def Event_1035482210(_, character: uint):
    """Event 1035482210"""
    Kill(character)


@RestartOnRest(1035482260)
def Event_1035482260(
    _,
    flag: uint,
    destination: uint,
    character: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1035482260"""
    if FlagEnabled(flag):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    if AND_1:
        return
    ForceAnimation(destination, 0)
    Move(character, destination=destination, destination_type=CoordEntityType.Asset, model_point=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1035482261)
def Event_1035482261(
    _,
    flag: uint,
    asset: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot: int,
    flag_1: uint,
):
    """Event 1035482261"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=200, model_point=803160)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ForceAnimation(asset, 1)
    DeleteAssetVFX(asset)
    Wait(1.0)
    DisableAsset(asset)
    if PlayerInOwnWorld():
        Wait(0.30000001192092896)
        AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1035482262)
def Event_1035482262(
    _,
    character: uint,
    seconds: float,
    attacked_entity: uint,
    seconds_1: float,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag: uint,
):
    """Event 1035482262"""
    if FlagEnabled(character):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character_1)
    ForceAnimation(character_1, animation_id)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=character_1, other_entity=20000, radius=radius))
    AND_1.Add(OR_2)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character_1, state=True)
    Wait(seconds_2)
    ForceAnimation(character_1, animation_id_1)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1035482270)
def Event_1035482270():
    """Event 1035482270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1035482270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy0,
            source_entity=1035482271,
            model_point=900,
            behavior_id=802102070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1035482280)
def Event_1035482280():
    """Event 1035482280"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1035482280))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy1,
            source_entity=1035482281,
            model_point=900,
            behavior_id=802102070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()
