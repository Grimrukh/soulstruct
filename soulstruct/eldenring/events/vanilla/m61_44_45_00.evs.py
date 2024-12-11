"""
Land of Shadow 11-11 SW NW

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76944, asset=2044451950)
    CommonFunc_9005810(
        0,
        flag=2044450800,
        grace_flag=76945,
        character=2044450951,
        asset=2044451951,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=76945,
        asset=2044451981,
        source_flag=77900,
        value=6,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
    Event_2044450800()
    Event_2044452810()
    Event_2044452811()
    Event_2044452849()
    Event_2044452820()
    Event_2044452821()
    CommonFunc_90005221(0, character=2044450301, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2044450306, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005501(
        0,
        flag=2044450510,
        flag_1=2044450511,
        left=0,
        asset=2044451510,
        asset_1=2044451511,
        asset_2=2044451512,
        flag_2=2044450512,
    )
    CommonFunc_90005501(
        0,
        flag=2044450515,
        flag_1=2044450516,
        left=2,
        asset=2044451515,
        asset_1=2044451516,
        asset_2=2044451517,
        flag_2=2044450517,
    )
    Event_2044452510()
    CommonFunc_900005610(0, asset=2044451699, dummy_id=100, vfx_id=800, right=0)


@ContinueOnRest(2044450050)
def Event_2044450050():
    """Event 2044450050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(2044452510)
def Event_2044452510():
    """Event 2044452510"""
    CommonFunc_90005500(
        0,
        flag=2044450510,
        flag_1=2044450511,
        left=0,
        asset=2044451510,
        asset_1=2044451511,
        obj_act_id=2044453511,
        asset_2=2044451512,
        obj_act_id_1=2044453512,
        region=2044452511,
        region_1=2044452512,
        flag_2=2044450512,
        flag_3=2044450513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=2044450515,
        flag_1=2044450516,
        left=2,
        asset=2044451515,
        asset_1=2044451516,
        obj_act_id=2044453516,
        asset_2=2044451517,
        obj_act_id_1=2044453517,
        region=2044452516,
        region_1=2044452517,
        flag_2=2044450517,
        flag_3=2044450518,
        left_1=0,
    )


@ContinueOnRest(2044450800)
def Event_2044450800():
    """Event 2044450800"""
    GotoIfFlagDisabled(Label.L0, flag=2044450800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(2044450800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2044450800, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(2044450800))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(2044450800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=2044450800, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(2044450800)
    EnableFlag(9160)
    if PlayerInOwnWorld():
        EnableFlag(61160)


@RestartOnRest(2044452810)
def Event_2044452810():
    """Event 2044452810"""
    GotoIfFlagDisabled(Label.L0, flag=2044450800)
    DisableCharacter(2044450800)
    DisableAnimations(2044450800)
    Kill(2044450800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2044450800)
    CreateProjectileOwner(entity=2044450820)
    AND_2.Add(FlagEnabled(2044452805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2044452800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(2044450800)
    SetNetworkUpdateRate(2044450800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2044450800, name=905030000)


@RestartOnRest(2044452811)
def Event_2044452811():
    """Event 2044452811"""
    if FlagEnabled(2044450800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2044450800, 10010050))
    
    EnableFlag(2044452802)


@RestartOnRest(2044452820)
def Event_2044452820():
    """Event 2044452820"""
    if FlagEnabled(2044450800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2044450800, 20010470))
    
    GotoIfFlagEnabled(Label.L5, flag=70)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409400,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409410,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409420,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409430,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409440,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409450,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804409460,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    ShootProjectile(
        owner_entity=2044450820,
        source_entity=2044451820,
        dummy_id=-1,
        behavior_id=804409470,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419400,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419410,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419420,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419430,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419440,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419450,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=2044450820,
            source_entity=2044451820,
            dummy_id=-1,
            behavior_id=804419460,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    ShootProjectile(
        owner_entity=2044450820,
        source_entity=2044451820,
        dummy_id=-1,
        behavior_id=804419470,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(2044452821)
def Event_2044452821():
    """Event 2044452821"""
    if FlagEnabled(2044450800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2044450800, 20010471))
    
    ShootProjectile(
        owner_entity=2044450820,
        source_entity=2044450800,
        dummy_id=210,
        behavior_id=250300205,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(2044452849)
def Event_2044452849():
    """Event 2044452849"""
    CommonFunc_9005800(
        0,
        flag=2044450800,
        entity=2044451800,
        region=2044452800,
        flag_1=2044452805,
        character=2044455800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2044450800,
        entity=2044451800,
        region=2044452800,
        flag_1=2044452805,
        flag_2=2044452806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2044450800, asset=2044451800, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=2044450800, asset=2044451801, vfx_id=5, right=0)
    CommonFunc_9005822(
        0,
        flag=2044450800,
        bgm_boss_conv_param_id=503000,
        flag_1=2044452805,
        flag_2=2044452806,
        right=2044452805,
        flag_3=2044452802,
        left=0,
        left_1=0,
    )
