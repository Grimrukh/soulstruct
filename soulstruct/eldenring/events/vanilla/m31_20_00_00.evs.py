"""
Abandoned Cave

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
from .entities.m31_20_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_31202800()
    Event_31202801()
    Event_31202802()
    Event_31202810()
    Event_31202811()
    Event_31092849()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    RegisterGrace(grace_flag=31200000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005646(
        0,
        flag=31200800,
        left_flag=31202840,
        cancel_flag__right_flag=31202841,
        asset=Assets.AEG099_065_9000,
        player_start=31202840,
        area_id=31,
        block_id=20,
        cc_id=0,
        dd_id=0,
    )
    Event_31202550(0, owner_entity=Characters.Dummy4, source_entity=Assets.AEG099_046_9005, seconds=5.0, seconds_1=0.0)
    Event_31202550(2, owner_entity=Characters.Dummy6, source_entity=Assets.AEG099_046_9015, seconds=5.0, seconds_1=0.0)
    Event_31202550(3, owner_entity=Characters.Dummy7, source_entity=Assets.AEG099_046_9020, seconds=5.0, seconds_1=1.0)
    Event_31202550(5, owner_entity=Characters.Dummy1, source_entity=Assets.AEG099_046_9001, seconds=5.0, seconds_1=2.0)
    Event_31202550(1, 31200480, 31201580, 5.0, 3.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.MirandaRotFlower0,
        animation_id=30000,
        animation_id_1=20000,
        region=31202240,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.MirandaRotFlower1,
        animation_id=30000,
        animation_id_1=20000,
        region=31202240,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.MirandaRotFlower2,
        animation_id=30000,
        animation_id_1=20000,
        region=31202240,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=Characters.MirandaRotFlower3,
        animation_id=30000,
        animation_id_1=20000,
        region=31202240,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Rat1, region=31202230, seconds=0.0, animation_id=0)
    CommonFunc_90005250(1, 31200231, 31202230, 0.0, 0)


@RestartOnRest(31202520)
def Event_31202520(_, flag: uint, flag_1: uint, asset: uint):
    """Event 31202520"""
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(31202550)
def Event_31202550(_, owner_entity: uint, source_entity: uint, seconds: float, seconds_1: float):
    """Event 31202550"""
    Wait(seconds)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    Wait(seconds_1)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802730070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Restart()


@RestartOnRest(31202800)
def Event_31202800():
    """Event 31202800"""
    if FlagEnabled(31200800):
        return
    AND_1.Add(CharacterDead(Characters.CleanrotKnight0))
    AND_1.Add(CharacterDead(Characters.CleanrotKnight1))
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    KillBossAndDisplayBanner(character=Characters.CleanrotKnight0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31200800)
    EnableFlag(9245)
    if PlayerInOwnWorld():
        EnableFlag(61245)


@RestartOnRest(31202801)
def Event_31202801():
    """Event 31202801"""
    if FlagEnabled(31200800):
        return
    
    MAIN.Await(HealthValue(Characters.CleanrotKnight0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CleanrotKnight0, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31202802)
def Event_31202802():
    """Event 31202802"""
    if FlagEnabled(31200800):
        return
    
    MAIN.Await(HealthValue(Characters.CleanrotKnight1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CleanrotKnight1, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31202810)
def Event_31202810():
    """Event 31202810"""
    GotoIfFlagDisabled(Label.L0, flag=31200800)
    DisableCharacter(Characters.CleanrotKnight0)
    DisableCharacter(Characters.CleanrotKnight1)
    DisableAnimations(Characters.CleanrotKnight0)
    DisableAnimations(Characters.CleanrotKnight1)
    Kill(Characters.CleanrotKnight0)
    Kill(Characters.CleanrotKnight1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.CleanrotKnight0)
    DisableAI(Characters.CleanrotKnight1)
    ForceAnimation(Characters.CleanrotKnight0, 30001)
    AND_2.Add(FlagEnabled(31202805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31202800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.CleanrotKnight0)
    SetNetworkUpdateRate(Characters.CleanrotKnight0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    EnableBossHealthBar(Characters.CleanrotKnight0, name=903800311)
    ForceAnimation(Characters.CleanrotKnight0, 20001)
    Wait(5.0)
    EnableAI(Characters.CleanrotKnight1)
    SetNetworkUpdateRate(Characters.CleanrotKnight1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    OR_15.Add(AttackedWithDamageType(attacked_entity=Characters.CleanrotKnight1, attacker=0))
    OR_15.Add(TimeElapsed(seconds=7.0))
    AwaitConditionTrue(OR_15)
    EnableBossHealthBar(Characters.CleanrotKnight1, name=903800312, bar_slot=1)


@RestartOnRest(31202811)
def Event_31202811():
    """Event 31202811"""
    if FlagEnabled(31200800):
        return
    OR_15.Add(CharacterDead(Characters.CleanrotKnight0))
    OR_15.Add(CharacterDead(Characters.CleanrotKnight1))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31202842)


@RestartOnRest(31092849)
def Event_31092849():
    """Event 31092849"""
    CommonFunc_9005800(
        0,
        flag=31200800,
        entity=Assets.AEG099_001_9000,
        region=31202800,
        flag_1=31202805,
        character=31205800,
        action_button_id=10010,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31200800,
        entity=Assets.AEG099_001_9000,
        region=31202800,
        flag_1=31202805,
        flag_2=31202806,
        action_button_id=10010,
    )
    CommonFunc_9005811(0, flag=31200800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 31200800, 931000, 31202805, 31202806, 0, 31202842, 0, 0)
