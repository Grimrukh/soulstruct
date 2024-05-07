"""
Stormfoot Catacombs

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
from .enums.m30_02_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=300200, asset=Assets.AEG099_060_9000)
    CommonFunc_90005646(
        0,
        flag=30020800,
        left_flag=30022840,
        cancel_flag__right_flag=30022841,
        asset=Assets.AEG099_065_9000,
        player_start=30022840,
        area_id=30,
        block_id=2,
        cc_id=0,
        dd_id=0,
    )
    Event_30022800()
    Event_30022810()
    Event_30022849()
    Event_30022811()
    CommonFunc_90005550(0, flag=30020680, asset=30021680, obj_act_id=30023680)
    CommonFunc_90005650(
        0,
        flag=30020540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30023541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30020540, anchor_entity=Assets.AEG027_041_0500)
    CommonFunc_90005680(
        0,
        flag=30020500,
        flag_1=30020501,
        flag_2=30020502,
        flag_3=30020503,
        asset=Assets.AEG027_156_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30020505,
        flag_1=30020506,
        flag_2=30020507,
        flag_3=30020508,
        asset=Assets.AEG027_156_0501,
    )
    Event_30022510()
    Event_30022580()
    CommonFunc_90005706(0, character=Characters.Commoner, animation_id=930025, left=Assets.AEG099_590_9000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_90005211(
        0,
        character=Characters.Imp0,
        animation_id=30010,
        animation_id_1=20010,
        region=30022200,
        radius=1.5,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp1, region=30022201, radius=0.0, seconds=0.0, animation_id=3006)
    CommonFunc_90005211(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30022202,
        radius=1.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp3,
        animation_id=30010,
        animation_id_1=20010,
        region=30022203,
        radius=1.0,
        seconds=0.20000000298023224,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp4,
        animation_id=30010,
        animation_id_1=20010,
        region=30022204,
        radius=1.0,
        seconds=0.20000000298023224,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp5,
        animation_id=30003,
        animation_id_1=20003,
        region=30022205,
        radius=1.0,
        seconds=4.800000190734863,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp6,
        animation_id=30003,
        animation_id_1=20003,
        region=30022206,
        radius=0.0,
        seconds=0.4000000059604645,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp7,
        animation_id=30003,
        animation_id_1=20003,
        region=30022206,
        radius=0.0,
        seconds=0.20000000298023224,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp8,
        animation_id=30002,
        animation_id_1=20002,
        region=30022206,
        radius=0.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp9,
        animation_id=30010,
        animation_id_1=20010,
        region=30022206,
        radius=0.0,
        seconds=0.8999999761581421,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp10,
        animation_id=30010,
        animation_id_1=20010,
        region=30022206,
        radius=0.0,
        seconds=0.10000000149011612,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp11,
        animation_id=30010,
        animation_id_1=20010,
        region=30022212,
        radius=0.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp12,
        animation_id=30010,
        animation_id_1=20010,
        region=30022212,
        radius=0.0,
        seconds=2.5,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp13,
        animation_id=30003,
        animation_id_1=20003,
        region=30022214,
        radius=1.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp14, region=30022215, radius=1.0, seconds=0.0, animation_id=0)
    Event_30020050()


@ContinueOnRest(30020050)
def Event_30020050():
    """Event 30020050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30020500)
    EnableFlag(30020505)


@ContinueOnRest(30022510)
def Event_30022510():
    """Event 30022510"""
    CommonFunc_90005681(0, flag=30020500, flag_1=30020501, flag_2=30020502, flag_3=30020503, attacked_entity=30021500)
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101070,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101060,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101050,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101040,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101030,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101020,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101010,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30020502,
            source_entity=Assets.AEG027_156_0500,
            region=30022500,
            owner_entity=Characters.TalkDummy1,
            behavior_id=801101000,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    CommonFunc_90005681(0, flag=30020505, flag_1=30020506, flag_2=30020507, flag_3=30020508, attacked_entity=30021505)
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101070,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101060,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101050,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101040,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101030,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101020,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101010,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=30020507,
            source_entity=Assets.AEG027_156_0501,
            region=30022505,
            owner_entity=Characters.TalkDummy2,
            behavior_id=801101000,
            behavior_id_1=801101005,
            dummy_id=101,
            dummy_id_1=0,
            dummy_id_2=0,
            dummy_id_3=0,
        )


@ContinueOnRest(30022580)
def Event_30022580():
    """Event 30022580"""
    RegisterLadder(start_climbing_flag=30020580, stop_climbing_flag=30020581, asset=Assets.AEG027_009_0500)


@ContinueOnRest(30022610)
def Event_30022610(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    dummy_id: int,
    dummy_id_1: int,
    dummy_id_2: int,
    dummy_id_3: int,
):
    """Event 30022610"""
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
            behavior_id=801101000,
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
            behavior_id=801101005,
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
            behavior_id=801101000,
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
            behavior_id=801101005,
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
            behavior_id=801101000,
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
            behavior_id=801101005,
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
            behavior_id=801101000,
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
            behavior_id=801101005,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@RestartOnRest(30022650)
def Event_30022650(_, tutorial_param_id: int, flag: uint):
    """Event 30022650"""
    if Multiplayer():
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=STORMFOOT_CATACOMBS))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(30022800)
def Event_30022800():
    """Event 30022800"""
    if FlagEnabled(30020800):
        return
    
    MAIN.Await(HealthValue(Characters.ErdtreeBurialWatchdog) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.ErdtreeBurialWatchdog, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.ErdtreeBurialWatchdog))
    
    KillBossAndDisplayBanner(character=Characters.ErdtreeBurialWatchdog, banner_type=BannerType.EnemyFelled)
    EnableFlag(30020800)
    EnableFlag(9202)
    if PlayerInOwnWorld():
        EnableFlag(61202)


@RestartOnRest(30022810)
def Event_30022810():
    """Event 30022810"""
    GotoIfFlagDisabled(Label.L0, flag=30020800)
    DisableCharacter(Characters.ErdtreeBurialWatchdog)
    DisableAnimations(Characters.ErdtreeBurialWatchdog)
    Kill(Characters.ErdtreeBurialWatchdog)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ErdtreeBurialWatchdog)
    AND_2.Add(FlagEnabled(30022805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30022800))
    
    MAIN.Await(AND_2)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(30020801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.ErdtreeBurialWatchdog)
    SetNetworkUpdateRate(Characters.ErdtreeBurialWatchdog, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ErdtreeBurialWatchdog, name=904260301)


@RestartOnRest(30022811)
def Event_30022811():
    """Event 30022811"""
    if FlagEnabled(30020800):
        return
    AND_1.Add(HealthRatio(Characters.ErdtreeBurialWatchdog) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30022802)


@RestartOnRest(30022849)
def Event_30022849():
    """Event 30022849"""
    CommonFunc_9005800(
        0,
        flag=30020800,
        entity=Assets.AEG099_001_9000,
        region=30022800,
        flag_1=30022805,
        character=30025800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30020800,
        entity=Assets.AEG099_001_9000,
        region=30022800,
        flag_1=30022805,
        flag_2=30022806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30020800, asset=Assets.AEG099_001_9000, dummy_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30020800,
        bgm_boss_conv_param_id=930000,
        flag_1=30022805,
        flag_2=30022806,
        right=0,
        flag_3=30022802,
        left=0,
        left_1=0,
    )
