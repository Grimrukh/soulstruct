"""
Gelmir Hero's Grave

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
from .enums.m30_09_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73009, asset=Assets.AEG099_060_9000)
    Event_30090100(0, flag=30090540, asset=Assets.AEG027_041_0500, obj_act_id=30093540, obj_act_id_1=27041)
    CommonFunc_90005501(
        0,
        flag=30090510,
        flag_1=30091510,
        left=2,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0501,
        asset_2=Assets.AEG027_002_0500,
        flag_2=30090511,
    )
    Event_30092510()
    CommonFunc_90005680(
        0,
        flag=30090500,
        flag_1=30090501,
        flag_2=30090502,
        flag_3=30090503,
        asset=Assets.AEG027_155_0500,
    )
    Event_30092500()
    Event_30092580()
    CommonFunc_90005616(0, flag=30097000, region=30092700)
    CommonFunc_90005250(
        0,
        character=Characters.CatacombsSkeleton0,
        region=30092200,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005250(1, character=Characters.CatacombsSkeleton1, region=30092200, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton2,
        animation_id=30003,
        animation_id_1=20003,
        region=30092205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CatacombsSkeleton3, region=30092206, seconds=0.0, animation_id=3000)
    CommonFunc_90005250(0, character=Characters.CatacombsSkeleton6, region=30092219, seconds=0.0, animation_id=3026)
    CommonFunc_90005200(
        0,
        character=Characters.CatacombsSkeleton4,
        animation_id=30003,
        animation_id_1=20003,
        region=30092210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.CatacombsSkeleton5,
        animation_id=30003,
        animation_id_1=20003,
        region=30092210,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=30090215,
        animation_id=30003,
        animation_id_1=20003,
        region=30092215,
        seconds=1.2999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=30090217,
        animation_id=30003,
        animation_id_1=20003,
        region=30092215,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.WanderingNoble4, region=30092230, seconds=0.0, animation_id=0)
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble0,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        1,
        character=Characters.WanderingNoble1,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        2,
        character=Characters.WanderingNoble2,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        3,
        character=Characters.WanderingNoble3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble5,
        animation_id=30000,
        animation_id_1=20000,
        region=30092235,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.WanderingNoble6,
        animation_id=30000,
        animation_id_1=20000,
        region=30092235,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.WanderingNoble7, region=30092258, seconds=0.0, animation_id=701)
    CommonFunc_90005221(
        0,
        character=Characters.WanderingNoble8,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005250(0, character=Characters.Page0, region=30092250, seconds=0.0, animation_id=3009)
    CommonFunc_90005250(1, character=Characters.Page1, region=30092250, seconds=3.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Page4, region=30092258, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Page2, region=30092254, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Page3, region=30092254, seconds=0.0, animation_id=3010)
    CommonFunc_90005250(0, character=Characters.CemeteryShade, region=30092270, seconds=0.0, animation_id=5003)
    CommonFunc_90005250(1, character=30090301, region=30092301, seconds=0.0, animation_id=5003)
    CommonFunc_90005250(0, character=Characters.BloodhoundKnight, region=30092300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MercilessChariot0, region=30092400, seconds=1.0, animation_id=-1)
    Event_30092400(0, character=Characters.MercilessChariot0)
    Event_30092410(
        0,
        character=Characters.MercilessChariot0,
        region=30092431,
        patrol_information_id=30093420,
        region_1=30092421,
        patrol_information_id_1=30093421,
    )
    CommonFunc_90005250(0, character=Characters.MercilessChariot1, region=30092410, seconds=0.0, animation_id=-1)
    Event_30092400(1, character=Characters.MercilessChariot1)
    Event_30092399()
    Event_30092410(
        3,
        character=Characters.MercilessChariot1,
        region=30092451,
        patrol_information_id=30093440,
        region_1=30092441,
        patrol_information_id_1=30093441,
    )
    Event_30092410(
        4,
        character=Characters.MercilessChariot1,
        region=30092452,
        patrol_information_id=30093441,
        region_1=30092442,
        patrol_information_id_1=30093442,
    )
    Event_30092800()
    Event_30092810()
    Event_30092849()
    Event_30092811()
    CommonFunc_90005646(
        0,
        flag=30090800,
        left_flag=30092840,
        cancel_flag__right_flag=30092841,
        asset=Assets.AEG099_065_9000,
        player_start=30092840,
        area_id=30,
        block_id=9,
        cc_id=0,
        dd_id=0,
    )
    Event_30090790(0, asset=Assets.AEG099_630_9000, flag=30090800)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30090050()
    Event_30090519()


@ContinueOnRest(30090050)
def Event_30090050():
    """Event 30090050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30090500)


@ContinueOnRest(30090100)
def Event_30090100(_, flag: Flag | int, asset: uint, obj_act_id: uint, obj_act_id_1: int):
    """Event 30090100"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1)
    End()


@ContinueOnRest(30092510)
def Event_30092510():
    """Event 30092510"""
    CommonFunc_90005500(
        0,
        flag=30090510,
        flag_1=30091510,
        left=2,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=30093511,
        asset_2=Assets.AEG027_002_0500,
        obj_act_id_1=30093512,
        region=30092511,
        region_1=30092512,
        flag_2=30090511,
        flag_3=30092512,
        left_1=0,
    )


@ContinueOnRest(30090519)
def Event_30090519():
    """Event 30090519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30090510)


@RestartOnRest(30092500)
def Event_30092500():
    """Event 30092500"""
    CommonFunc_90005681(
        0,
        flag=30090500,
        flag_1=30090501,
        flag_2=30090502,
        flag_3=30090503,
        attacked_entity=Assets.AEG027_155_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103270,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103260,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103250,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103240,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103230,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103220,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103210,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30090502,
            source_entity=Assets.AEG027_155_0500,
            region=30092500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801103200,
            behavior_id_1=801103205,
            dummy_id=100,
            dummy_id_1=101,
            dummy_id_2=0,
            dummy_id_3=0,
        )


@RestartOnRest(30092300)
def Event_30092300(_, asset__asset_flag: uint, other_entity: uint):
    """Event 30092300"""
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=PLAYER, radius=2.4000000953674316))
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=other_entity, radius=2.4000000953674316))
    
    MAIN.Await(OR_1)
    
    CreateHazard(
        asset_flag=asset__asset_flag,
        asset=asset__asset_flag,
        dummy_id=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=2.299999952316284,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30092305)
def Event_30092305(_, asset__asset_flag: uint, other_entity: uint):
    """Event 30092305"""
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=PLAYER, radius=3.0999999046325684))
    OR_1.Add(EntityWithinDistance(entity=asset__asset_flag, other_entity=other_entity, radius=3.0999999046325684))
    
    MAIN.Await(OR_1)
    
    CreateHazard(
        asset_flag=asset__asset_flag,
        asset=asset__asset_flag,
        dummy_id=100,
        behavior_param_id=103000,
        target_type=DamageTargetType.Character,
        radius=3.0999999046325684,
        life=1.0,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    Wait(0.699999988079071)
    Restart()


@RestartOnRest(30092399)
def Event_30092399():
    """Event 30092399"""
    SetDisplayMask(Characters.MercilessChariot1, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.MercilessChariot1, bit_index=11, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.MercilessChariot1, bit_index=5, switch_type=OnOffChange.On)
    AttachAssetToCharacter(character=Characters.MercilessChariot1, dummy_id=110, asset=Assets.AEG099_331_9001)


@RestartOnRest(30092400)
def Event_30092400(_, character: Character | int):
    """Event 30092400"""
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    DisableHealthBar(character)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    End()


@RestartOnRest(30092410)
def Event_30092410(
    _,
    character: Character | int,
    region: Region | int,
    patrol_information_id: uint,
    region_1: Region | int,
    patrol_information_id_1: uint,
):
    """Event 30092410"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    Restart()


@ContinueOnRest(30092580)
def Event_30092580():
    """Event 30092580"""
    RegisterLadder(start_climbing_flag=30090580, stop_climbing_flag=30090581, asset=Assets.AEG027_040_0500)
    RegisterLadder(start_climbing_flag=30090582, stop_climbing_flag=30090583, asset=Assets.AEG027_005_0501)


@ContinueOnRest(30092610)
def Event_30092610(
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
    """Event 30092610"""
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
            behavior_id=801103200,
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
            behavior_id=801103205,
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
            behavior_id=801103200,
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
            behavior_id=801103205,
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
            behavior_id=801103200,
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
            behavior_id=801103205,
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
            behavior_id=801103200,
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
            behavior_id=801103205,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@RestartOnRest(30090790)
def Event_30090790(_, asset: Asset | int, flag: Flag | int):
    """Event 30090790"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ThisEventSlotFlagDisabled())
    
    MAIN.Await(AND_1)
    
    EnableThisSlotFlag()
    EnableAssetActivation(asset, obj_act_id=-1)
    End()


@RestartOnRest(30092800)
def Event_30092800():
    """Event 30092800"""
    if FlagEnabled(30090800):
        return
    
    MAIN.Await(HealthValue(Characters.RedWolf) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.RedWolf, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.RedWolf))
    
    KillBossAndDisplayBanner(character=Characters.RedWolf, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(30091520, obj_act_id=-1)
    EnableFlag(30090800)
    EnableFlag(9209)
    if PlayerInOwnWorld():
        EnableFlag(61209)


@RestartOnRest(30092810)
def Event_30092810():
    """Event 30092810"""
    GotoIfFlagDisabled(Label.L0, flag=30090800)
    DisableCharacter(Characters.RedWolf)
    DisableAnimations(Characters.RedWolf)
    Kill(Characters.RedWolf)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.RedWolf)
    EnableAssetActivation(30091520, obj_act_id=-1)
    AND_2.Add(FlagEnabled(30092805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30092800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.RedWolf)
    SetNetworkUpdateRate(Characters.RedWolf, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.RedWolf, name=903181300)


@RestartOnRest(30092811)
def Event_30092811():
    """Event 30092811"""
    if FlagEnabled(30090800):
        return
    AND_1.Add(HealthRatio(Characters.RedWolf) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30092802)


@RestartOnRest(30092849)
def Event_30092849():
    """Event 30092849"""
    CommonFunc_9005800(
        0,
        flag=30090800,
        entity=Assets.AEG099_001_9000,
        region=30092800,
        flag_1=30092805,
        character=30095800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30090800,
        entity=Assets.AEG099_001_9000,
        region=30092800,
        flag_1=30092805,
        flag_2=30092806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30090800, asset=Assets.AEG099_001_9000, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30090800,
        bgm_boss_conv_param_id=921400,
        flag_1=30092805,
        flag_2=30092806,
        right=0,
        flag_3=30092802,
        left=0,
        left_1=0,
    )
