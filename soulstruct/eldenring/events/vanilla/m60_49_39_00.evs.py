"""
South Caelid (NW) (NE)

linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_49_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049390000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76414,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=7,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    CommonFunc_9005810(
        0,
        flag=1049390800,
        grace_flag=1049390001,
        character=Characters.TalkDummy2,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    RegisterGrace(grace_flag=1049390002, asset=Assets.AEG099_060_9002)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76416,
        asset=Assets.AEG099_090_9001,
        source_flag=77400,
        value=6,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    Event_1049392210()
    Event_1049392211(0, source_entity=1049391200, seconds=19.0)
    Event_1049392211(1, source_entity=Assets.AEG099_046_9001, seconds=12.0)
    Event_1049392211(2, source_entity=Assets.AEG099_046_9002, seconds=5.0)
    Event_1049392211(3, source_entity=Assets.AEG099_046_9003, seconds=18.0)
    Event_1049392211(4, source_entity=Assets.AEG099_046_9004, seconds=11.0)
    Event_1049392211(5, source_entity=Assets.AEG099_046_9005, seconds=4.0)
    Event_1049392211(7, source_entity=Assets.AEG099_046_9007, seconds=17.0)
    Event_1049392211(8, source_entity=Assets.AEG099_046_9008, seconds=10.0)
    Event_1049392211(10, source_entity=Assets.AEG099_046_9010, seconds=3.0)
    Event_1049392211(12, source_entity=Assets.AEG099_046_9012, seconds=16.0)
    Event_1049392211(13, source_entity=Assets.AEG099_046_9013, seconds=9.0)
    Event_1049392211(14, source_entity=Assets.AEG099_046_9014, seconds=2.0)
    Event_1049392211(15, source_entity=Assets.AEG099_046_9015, seconds=1.0)
    Event_1049392211(16, source_entity=Assets.AEG099_046_9016, seconds=14.0)
    Event_1049392211(17, source_entity=Assets.AEG099_046_9017, seconds=7.0)
    Event_1049392580(0, start_climbing_flag=49390580, stop_climbing_flag=49390851, asset=Assets.AEG110_099_2000)
    Event_1049392580(1, start_climbing_flag=49390582, stop_climbing_flag=49390853, asset=Assets.AEG110_099_2001)
    Event_1049392300(0, asset=Assets.AEG099_252_2000, flag=1049390200)
    Event_1049392301(1, asset=Assets.AEG099_253_2000, flag=1049390201)
    Event_1049392302(1, asset=Assets.AEG099_047_2001, flag=1049390201)
    Event_1049392303(0, asset=Assets.AEG099_047_2000, flag=1049390200)
    Event_1049392849()
    Event_1049390800()
    Event_1049392810()
    CommonFunc_9005811(0, flag=1049390800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_90005880(
        0,
        flag=1049390850,
        flag_1=1049390855,
        flag_2=1049392850,
        character=Characters.BattleMage,
        item_lot=1049390850,
        area_id=60,
        block_id=49,
        cc_id=39,
        dd_id=0,
        player_start=1049392855,
    )
    CommonFunc_90005881(
        0,
        flag=1049390850,
        flag_1=1049390855,
        left_flag=1049392851,
        cancel_flag__right_flag=1049392852,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=49,
        cc_id=39,
        dd_id=0,
        player_start=1049392855,
    )
    CommonFunc_90005882(
        0,
        flag=1049390850,
        flag_1=1049390855,
        flag_2=1049392850,
        character=Characters.BattleMage,
        flag_3=1049392856,
        character_1=1049395860,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.TalkDummy3,
        source_entity=1049392860,
        name=903704520,
        animation_id=-1,
        animation_id_1=20004,
    )
    CommonFunc_90005883(0, flag=1049390850, flag_1=1049390855, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1049390850,
        bgm_boss_conv_param_id=0,
        flag_1=1049392856,
        flag_2=1049392857,
        left=0,
        left_1=1,
    )
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar0, radius=17.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar4, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar7, radius=17.0, seconds=0.0, animation_id=-1)
    Event_1049392200(0, character=Characters.RayaLucariaScholar0, special_effect=14809)
    Event_1049392200(1, character=Characters.RayaLucariaScholar1, special_effect=14807)
    Event_1049392200(2, character=Characters.RayaLucariaScholar2, special_effect=14809)
    Event_1049392200(3, character=Characters.WanderingNoble1, special_effect=10113)
    Event_1049392200(4, character=Characters.RayaLucariaScholar4, special_effect=14807)
    Event_1049392200(5, character=Characters.RayaLucariaScholar5, special_effect=14809)
    Event_1049392200(7, character=Characters.RayaLucariaScholar6, special_effect=14808)
    Event_1049392200(9, character=Characters.RayaLucariaScholar7, special_effect=14809)
    CommonFunc_90005201(
        0,
        character=Characters.DragonbarrowDragon,
        animation_id=30000,
        animation_id_1=20000,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1049392350(
        0,
        character=Characters.Scarab0,
        special_effect=12603,
        region=1049392299,
        region_1=1049392298,
        region_2=1049392297,
    )
    CommonFunc_90005300(0, flag=1049390299, character=Characters.Scarab0, item_lot=40418, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1049390298, character=Characters.Scarab1, item_lot=40416, seconds=0.0, left=0)
    Event_1049392201(0, character=Characters.WanderingNoble0, special_effect=10113, seconds=3.0, seconds_1=5.0)
    Event_1049392201(2, character=Characters.WanderingNoble2, special_effect=10113, seconds=6.0, seconds_1=2.0)
    Event_1049392201(3, character=Characters.RayaLucariaScholar3, special_effect=10113, seconds=9.0, seconds_1=3.0)
    CommonFunc_90005250(0, character=Characters.Marionette, region=1049392405, seconds=0.0, animation_id=-1)


@RestartOnRest(1049392200)
def Event_1049392200(_, character: uint, special_effect: int):
    """Event 1049392200"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect)


@RestartOnRest(1049392201)
def Event_1049392201(_, character: uint, special_effect: int, seconds: float, seconds_1: float):
    """Event 1049392201"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect)
    Wait(seconds_1)
    RemoveSpecialEffect(character, special_effect)
    Wait(seconds)
    Restart()


@RestartOnRest(1049392210)
def Event_1049392210():
    """Event 1049392210"""
    CreateProjectileOwner(entity=Characters.Human)


@RestartOnRest(1049392211)
def Event_1049392211(_, source_entity: uint, seconds: float):
    """Event 1049392211"""
    EnableNetworkSync()
    Wait(8.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    Wait(seconds)
    AND_1.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_2.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_3.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_4.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_5.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=Characters.Human,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@ContinueOnRest(1049392300)
def Event_1049392300(_, asset: uint, flag: uint):
    """Event 1049392300"""
    EnableNetworkSync()
    CreateAssetVFX(asset, vfx_id=200, model_point=1502)
    
    MAIN.Await(FlagEnabled(flag))
    
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(asset)
    DeleteAssetVFX(asset)


@ContinueOnRest(1049392301)
def Event_1049392301(_, asset: uint, flag: uint):
    """Event 1049392301"""
    EnableNetworkSync()
    CreateAssetVFX(asset, vfx_id=200, model_point=1501)
    
    MAIN.Await(FlagEnabled(flag))
    
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(asset)
    DeleteAssetVFX(asset)


@ContinueOnRest(1049392302)
def Event_1049392302(_, asset: uint, flag: uint):
    """Event 1049392302"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9520, entity=asset))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    DisplayDialog(text=30000, anchor_entity=asset)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=100, model_point=806031)
    End()


@ContinueOnRest(1049392303)
def Event_1049392303(_, asset: uint, flag: uint):
    """Event 1049392303"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9520, entity=asset))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    EnableFlag(1050390200)
    DisplayDialog(text=30000, anchor_entity=asset)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=100, model_point=806031)


@ContinueOnRest(1049392350)
def Event_1049392350(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1049392350"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    DisableFlag(1049392201)
    DisableFlag(1049392202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1049392201, 1049392202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@ContinueOnRest(1049392580)
def Event_1049392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, asset: uint):
    """Event 1049392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, asset=asset)


@RestartOnRest(1049390800)
def Event_1049390800():
    """Event 1049390800"""
    if FlagEnabled(1049390800):
        return
    AND_1.Add(HealthValue(Characters.NoxFighter0) <= 0)
    AND_1.Add(HealthValue(Characters.NoxFighter1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.NoxFighter0, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.NoxFighter0))
    
    KillBossAndDisplayBanner(character=Characters.NoxFighter0, banner_type=BannerType.EnemyFelled)
    if PlayerInOwnWorld():
        AwardItemLot(1049390800, host_only=True)
    EnableFlag(1049390800)


@RestartOnRest(1049392810)
def Event_1049392810():
    """Event 1049392810"""
    GotoIfFlagDisabled(Label.L0, flag=1049390800)
    DisableCharacter(Characters.NoxFighter0)
    DisableAnimations(Characters.NoxFighter0)
    Kill(Characters.NoxFighter0)
    DisableCharacter(Characters.NoxFighter1)
    DisableAnimations(Characters.NoxFighter1)
    Kill(Characters.NoxFighter1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.NoxFighter0)
    DisableAI(Characters.NoxFighter1)
    AND_2.Add(FlagEnabled(1049392805))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1049392800))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1049392805))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.NoxFighter0)
    EnableAI(Characters.NoxFighter1)
    SetNetworkUpdateRate(Characters.NoxFighter0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.NoxFighter1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.NoxFighter0, name=903300560)
    EnableBossHealthBar(Characters.NoxFighter1, name=903300561, bar_slot=1)


@RestartOnRest(1049392849)
def Event_1049392849():
    """Event 1049392849"""
    CommonFunc_9005800(
        0,
        flag=1049390800,
        entity=Assets.AEG099_002_9000,
        region=1049392800,
        flag_1=1049392805,
        character=1049395800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1049390800,
        entity=Assets.AEG099_002_9000,
        region=1049392800,
        flag_1=1049392805,
        flag_2=1049392806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1049390800, asset=Assets.AEG099_002_9000, model_point=4, right=0)
    CommonFunc_9005822(
        0,
        flag=1049390800,
        bgm_boss_conv_param_id=920900,
        flag_1=1049392805,
        flag_2=1049392806,
        right=0,
        flag_3=1049392802,
        left=0,
        left_1=0,
    )
