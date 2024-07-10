"""
Tombsward Catacombs

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
from .enums.m30_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73000, asset=Assets.AEG099_060_9000)
    Event_30002800()
    Event_30002810()
    Event_30002829()
    Event_30002811()
    CommonFunc_90005550(0, flag=30000620, asset=30001620, obj_act_id=30003620)
    CommonFunc_90005550(0, flag=30000621, asset=30001621, obj_act_id=30003621)
    CommonFunc_90005550(0, flag=30000622, asset=30001622, obj_act_id=30003622)
    CommonFunc_90005550(0, flag=30000623, asset=30001623, obj_act_id=30003623)
    CommonFunc_90005650(
        0,
        flag=30000540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_1000,
        obj_act_id=30003541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30000540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005680(
        0,
        flag=30000500,
        flag_1=30000501,
        flag_2=30000502,
        flag_3=30000503,
        asset=Assets.AEG027_155_0500,
    )
    Event_30002510()
    CommonFunc_90005620(
        0,
        flag=30000570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30002571,
        cancel_flag__right_flag=30002572,
        right=30002573,
    )
    CommonFunc_90005621(0, flag=30000570, asset=Assets.AEG099_270_9001)
    CommonFunc_90005646(
        0,
        flag=30000800,
        left_flag=30002840,
        cancel_flag__right_flag=30002841,
        asset=Assets.AEG099_065_9000,
        player_start=30002840,
        area_id=30,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30000050()
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton0,
        animation_id=30003,
        animation_id_1=20003,
        region=30002200,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton1,
        animation_id=30003,
        animation_id_1=20003,
        region=30002201,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.CatacombsSkeleton3,
        animation_id=30003,
        animation_id_1=20003,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton4,
        animation_id=30003,
        animation_id_1=20003,
        region=30002205,
        radius=1.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton5,
        animation_id=30003,
        animation_id_1=20003,
        region=30002205,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=30000207,
        animation_id=30003,
        animation_id_1=20003,
        region=30002207,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton6,
        animation_id=30003,
        animation_id_1=20003,
        region=30002207,
        radius=1.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.CatacombsSkeleton8,
        animation_id=30003,
        animation_id_1=20003,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton9,
        animation_id=30003,
        animation_id_1=20003,
        region=30002212,
        radius=1.0,
        seconds=0.8999999761581421,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton10,
        animation_id=30003,
        animation_id_1=20003,
        region=30002215,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.CatacombsSkeleton11,
        animation_id=30003,
        animation_id_1=20003,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton12,
        animation_id=30003,
        animation_id_1=20003,
        region=30002215,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton13,
        animation_id=30003,
        animation_id_1=20003,
        region=30002215,
        radius=1.0,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton14,
        animation_id=30003,
        animation_id_1=20003,
        region=30002215,
        radius=1.0,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton15,
        animation_id=30003,
        animation_id_1=20003,
        region=30002215,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton16,
        animation_id=30003,
        animation_id_1=20003,
        region=30002223,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton17,
        animation_id=30003,
        animation_id_1=20003,
        region=30002223,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=30000225,
        animation_id=30003,
        animation_id_1=20003,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=30000226, radius=3.0, seconds=0.0, animation_id=0)


@ContinueOnRest(30000050)
def Event_30000050():
    """Event 30000050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30000500)


@ContinueOnRest(30002500)
def Event_30002500():
    """Event 30002500"""
    if ThisEventSlotFlagDisabled():
        EndOfAnimation(asset=Assets.AEG027_155_0500, animation_id=12)
    GotoIfFlagEnabled(Label.L0, flag=30000500)
    AND_1.Add(FlagDisabled(30000500))
    AND_1.Add(AttackedWithDamageType(attacked_entity=30001500, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Assets.AEG027_155_0500, 12, wait_for_completion=True)
    EnableFlag(30000500)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(30000500))
    AND_2.Add(AttackedWithDamageType(attacked_entity=30001500, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_2)
    
    DisableFlag(30000500)
    ForceAnimation(Assets.AEG027_155_0500, 21, wait_for_completion=True)
    Restart()


@RestartOnRest(30009570)
def Event_30009570(
    _,
    flag: Flag | int,
    destination: uint,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    seconds: float,
):
    """Event 30009570"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(PlayerNotInOwnWorld())
    if OR_1:
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9220, entity=destination))
    
    AwaitDialogResponse(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(PlayerHasGood(8000))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050)
    Wait(1.399999976158142)
    DisplayDialog(text=308000, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    FaceEntityAndForceAnimation(PLAYER, destination, animation=60010)
    Wait(seconds)
    DisplayDialog(text=208000, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8000, quantity=1)
    EnableNetworkFlag(flag)


@RestartOnRest(30002570)
def Event_30002570(_, flag: Flag | int, asset: Asset | int, asset_1: Asset | int, asset_2: Asset | int):
    """Event 30002570"""
    if FlagEnabled(30002570):
        return
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    DisableAsset(asset_2)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806040)
    CreateAssetVFX(asset_1, dummy_id=101, vfx_id=806041)
    
    MAIN.Await(FlagEnabled(flag))
    
    DeleteAssetVFX(asset_1, erase_root=False)
    Wait(2.0)
    DisableAsset(asset_1)
    DisableAsset(30001572)
    EnableAsset(asset_2)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1, erase_root=False)


@ContinueOnRest(30002610)
def Event_30002610(
    _,
    flag: Flag | int,
    source_entity: uint,
    region: Region | int,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    dummy_id: int,
    dummy_id_1: int,
    dummy_id_2: int,
    dummy_id_3: int,
):
    """Event 30002610"""
    AND_1.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=801101200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id,
            behavior_id=801101205,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=dummy_id_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=801101200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_1,
            behavior_id=801101205,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=dummy_id_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=801101200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_2,
            behavior_id=801101205,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=dummy_id_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=801101200,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=dummy_id_3,
            behavior_id=801101205,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@ContinueOnRest(30002611)
def Event_30002611():
    """Event 30002611"""
    AND_1.Add(FlagEnabled(30000500))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30002500))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=Characters.Dummy)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=Assets.AEG027_155_0500,
        dummy_id=100,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=Assets.AEG027_155_0500,
        dummy_id=100,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=Assets.AEG027_155_0500,
        dummy_id=101,
        behavior_id=101100,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=Assets.AEG027_155_0500,
        dummy_id=101,
        behavior_id=101102,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(6.0)
    Restart()


@ContinueOnRest(30002510)
def Event_30002510():
    """Event 30002510"""
    CommonFunc_90005681(
        0,
        flag=30000500,
        flag_1=30000501,
        flag_2=30000502,
        flag_3=30000503,
        attacked_entity=Assets.AEG027_155_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101270,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101260,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101250,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101240,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101230,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101220,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101210,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30000502,
            source_entity=Assets.AEG027_155_0500,
            region=30002500,
            owner_entity=Characters.Dummy,
            behavior_id=801101200,
            behavior_id_1=801101205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )


@RestartOnRest(30002800)
def Event_30002800():
    """Event 30002800"""
    if FlagEnabled(30000800):
        return
    
    MAIN.Await(HealthValue(Characters.CemeteryShade) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(30008000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.CemeteryShade))
    
    KillBossAndDisplayBanner(character=Characters.CemeteryShade, banner_type=BannerType.EnemyFelled)
    EnableFlag(30000800)
    EnableFlag(9200)
    if PlayerInOwnWorld():
        EnableFlag(61200)


@RestartOnRest(30002810)
def Event_30002810():
    """Event 30002810"""
    GotoIfFlagDisabled(Label.L0, flag=30000800)
    DisableCharacter(30005800)
    DisableAnimations(30005800)
    Kill(30005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30005800)
    AND_2.Add(FlagEnabled(30002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30002800))
    
    MAIN.Await(AND_2)
    
    EnableAI(30005800)
    SetNetworkUpdateRate(30005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CemeteryShade, name=903664300)


@RestartOnRest(30002811)
def Event_30002811():
    """Event 30002811"""
    if FlagEnabled(30000800):
        return
    AND_1.Add(HealthRatio(Characters.CemeteryShade) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30002802)


@RestartOnRest(30002829)
def Event_30002829():
    """Event 30002829"""
    CommonFunc_9005800(
        0,
        flag=30000800,
        entity=Assets.AEG099_001_9000,
        region=30002800,
        flag_1=30002805,
        character=30005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30000800,
        entity=Assets.AEG099_001_9000,
        region=30002800,
        flag_1=30002805,
        flag_2=30002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30000800, asset=Assets.AEG099_001_9000, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30000800,
        bgm_boss_conv_param_id=930000,
        flag_1=30002805,
        flag_2=30002806,
        right=0,
        flag_3=30002802,
        left=0,
        left_1=0,
    )
