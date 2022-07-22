"""
Northwest Liurnia (SE) (SW)

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
from .entities.m60_34_48_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034480000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76214,
        flag_1=76212,
        asset=Assets.AEG099_090_9000,
        source_flag=77220,
        value=2,
        flag_2=78220,
        flag_3=78221,
        flag_4=78222,
        flag_5=78223,
        flag_6=78224,
        flag_7=78225,
        flag_8=78226,
        flag_9=78227,
        flag_10=78228,
        flag_11=78229,
    )
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, character=Characters.GiantOctopus1)
    CommonFunc_90005525(0, flag=1034480610, asset=Assets.AEG004_984_1000)
    CommonFunc_90005525(0, flag=1034480611, asset=Assets.AEG004_983_1000)
    Event_1034482600(0, asset=1034481620, entity=1034481621, flag=82022)
    Event_1034482800()
    Event_1034482810()
    Event_1034482849()
    Event_1034482610(0, asset=Assets.AEG099_045_9000, flag=1034482640, owner_entity=Characters.Dummy)
    Event_1034482610(1, asset=Assets.AEG099_045_9001, flag=1034482641, owner_entity=Characters.Dummy)
    Event_1034482610(2, asset=Assets.AEG099_045_9002, flag=1034482642, owner_entity=Characters.Dummy)
    Event_1034482610(3, asset=1034481643, flag=1034482643, owner_entity=Characters.Dummy)
    Event_1034482610(4, asset=Assets.AEG099_045_9004, flag=1034482644, owner_entity=Characters.Dummy)
    Event_1034482610(5, asset=Assets.AEG099_045_9005, flag=1034482645, owner_entity=Characters.Dummy)
    Event_1034482610(6, asset=1034481646, flag=1034482646, owner_entity=Characters.Dummy)
    Event_1034482610(7, asset=1034481647, flag=1034482647, owner_entity=Characters.Dummy)
    Event_1034482610(8, asset=1034481648, flag=1034482648, owner_entity=Characters.Dummy)
    Event_1034482610(9, asset=1034481649, flag=1034482649, owner_entity=Characters.Dummy)
    Event_1034482260(
        0,
        flag=1034480250,
        destination=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1034482260(
        1,
        flag=1034480251,
        destination=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1034482261(
        0,
        flag=1034480250,
        asset=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        character_1=1034485260,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1034481300,
        flag_1=1034482250,
    )
    Event_1034482261(
        1,
        flag=1034480251,
        asset=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        character_1=1034485263,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1034481310,
        flag_1=1034482251,
    )
    Event_1034482262(
        0,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034482250,
    )
    Event_1034482262(
        1,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034482250,
    )
    Event_1034482262(
        3,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034482250,
    )
    Event_1034482262(
        4,
        character=Characters.Balloon1,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character_1=Characters.Marionette3,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034482251,
    )
    Event_1034482262(
        5,
        character=Characters.Balloon1,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character_1=Characters.Marionette4,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034482251,
    )
    CommonFunc_90005706(0, 1034480700, 930023, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble6)
    CommonFunc_90005251(0, character=Characters.WanderingNoble0, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble0,
        region=1034482210,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble2,
        region=1034482210,
        radius=15.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble3,
        region=1034482210,
        radius=15.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble4,
        region=1034482210,
        radius=15.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble5,
        region=1034482210,
        radius=15.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, 1034480211, 1034482211, 15.0, 0.0, 0)


@RestartOnRest(1034482260)
def Event_1034482260(
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
    """Event 1034482260"""
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


@RestartOnRest(1034482261)
def Event_1034482261(
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
    """Event 1034482261"""
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


@RestartOnRest(1034482262)
def Event_1034482262(
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
    """Event 1034482262"""
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


@RestartOnRest(1034482600)
def Event_1034482600(_, asset: uint, entity: uint, flag: uint):
    """Event 1034482600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1034482610)
def Event_1034482610(_, asset: uint, flag: uint, owner_entity: uint):
    """Event 1034482610"""
    if FlagEnabled(flag):
        return
    if AssetDestroyed(asset):
        return
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(EntityWithinDistance(entity=asset, other_entity=20000, radius=2.0))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DestroyAsset(asset, request_slot=0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=asset,
            model_point=100,
            behavior_id=802402070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    End()


@RestartOnRest(1034482800)
def Event_1034482800():
    """Event 1034482800"""
    if FlagEnabled(1034480800):
        return
    
    MAIN.Await(HealthValue(Characters.Revenant) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Revenant, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Revenant))
    
    KillBossAndDisplayBanner(character=Characters.Revenant, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_1000, obj_act_id=-1)
    EnableFlag(1034480800)
    End()


@RestartOnRest(1034482810)
def Event_1034482810():
    """Event 1034482810"""
    GotoIfFlagDisabled(Label.L0, flag=1034480800)
    DisableCharacter(Characters.Revenant)
    DisableAnimations(Characters.Revenant)
    Kill(Characters.Revenant)
    EnableAssetActivation(Assets.AEG004_970_1000, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.Revenant, 30000, loop=True)
    DisableAI(Characters.Revenant)
    AND_2.Add(FlagEnabled(1034482805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1034482800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Revenant)
    SetNetworkUpdateRate(Characters.Revenant, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.Revenant, 20000)
    EnableBossHealthBar(Characters.Revenant, name=904020540)
    DisableAssetActivation(Assets.AEG004_970_1000, obj_act_id=-1)


@RestartOnRest(1034482849)
def Event_1034482849():
    """Event 1034482849"""
    CommonFunc_9005800(
        0,
        flag=1034480800,
        entity=Assets.AEG099_001_9000,
        region=1034482800,
        flag_1=1034482805,
        character=1034485800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1034480800,
        entity=Assets.AEG099_001_9000,
        region=1034482800,
        flag_1=1034482805,
        flag_2=1034482806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1034480800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1034480800,
        bgm_boss_conv_param_id=920900,
        flag_1=1034482805,
        flag_2=1034482806,
        right=0,
        flag_3=1034482802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, 1034480800, 1034481801, 3, 0, 0)
