"""
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
from .entities.m60_40_53_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76306, asset=Assets.AEG099_060_9000)
    Event_1040532800()
    Event_1040532810()
    Event_1040532849()
    AttachAssetToAsset(child_asset=1040531201, parent_asset=1040531200, parent_model_point=151)
    Event_1040532650()
    Event_1040532660()
    Event_1040532665()
    Event_1040532670()
    Event_1040532680()
    Event_1040532685()
    Event_1040532690()
    CommonFunc_90005300(0, 1040530500, 1040530500, 40320, 0.0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, 1040530400, 1040532400, 15.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530401, 1040532400, 7.0, 0.4000000059604645, -1)
    CommonFunc_90005261(0, 1040530404, 1040532404, 7.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530404, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005250(0, 1040530402, 1040532402, 0.0, -1)
    CommonFunc_90005261(0, 1040530430, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530431, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530432, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530433, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530434, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530435, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530436, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530437, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530438, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530439, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530440, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530441, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530442, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530443, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530444, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530445, 1040532430, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530451, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530452, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530453, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530454, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530455, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530456, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530457, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530458, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530461, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530462, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530463, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530464, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005261(0, 1040530465, 1040532452, 5.0, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass5,
        animation_id=30000,
        animation_id_1=20000,
        region=1040532450,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1040530250,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=1040530260,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1040530212, 10.0, 0.0, -1)
    CommonFunc_90005251(0, 1040530267, 10.0, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellFootSoldier2,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellSoldier,
        animation_id=30004,
        animation_id_1=20004,
        region=1040532207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        region=1040532207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        region=1040532207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1040530405, 6.0, 0.0, -1)
    CommonFunc_90005251(0, 1040530460, 5.0, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.Wormface3, region=1040532357, seconds=0.0, animation_id=3000)
    CommonFunc_90005251(0, character=Characters.Wormface3, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=Characters.Wormface1,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Wormface6,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Wormface7,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Wormface8,
        animation_id=30000,
        animation_id_1=20000,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.Wormface0, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=1040530390, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005200(
        0,
        character=Characters.Slug0,
        animation_id=30000,
        animation_id_1=20000,
        region=1040532405,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug1,
        animation_id=30000,
        animation_id_1=20000,
        region=1040532405,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug2,
        animation_id=30000,
        animation_id_1=20000,
        region=1040532405,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1040530303, 30000, 20000, 1040532405, 0.800000011920929, 0, 0, 0, 0)


@RestartOnRest(1040532800)
def Event_1040532800():
    """Event 1040532800"""
    if FlagEnabled(1040530800):
        return
    
    MAIN.Await(HealthValue(Characters.SanguineNoble) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.SanguineNoble, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.SanguineNoble))
    
    KillBossAndDisplayBanner(character=Characters.SanguineNoble, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)
    EnableFlag(1040530800)


@RestartOnRest(1040532810)
def Event_1040532810():
    """Event 1040532810"""
    GotoIfFlagDisabled(Label.L0, flag=1040530800)
    DisableCharacter(Characters.SanguineNoble)
    DisableAnimations(Characters.SanguineNoble)
    Kill(Characters.SanguineNoble)
    EnableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.SanguineNoble)
    ForceAnimation(Characters.SanguineNoble, 30000, loop=True)
    AND_2.Add(FlagEnabled(1040532805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1040532800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.SanguineNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.SanguineNoble, 20000)
    EnableAI(Characters.SanguineNoble)
    Wait(2.799999952316284)
    EnableBossHealthBar(Characters.SanguineNoble, name=903550540)
    DisableAssetActivation(Assets.AEG004_970_1002, obj_act_id=1110064)


@RestartOnRest(1040532849)
def Event_1040532849():
    """Event 1040532849"""
    CommonFunc_9005800(
        0,
        flag=1040530800,
        entity=Assets.AEG099_001_9000,
        region=1040532800,
        flag_1=1040532805,
        character=1040535800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1040530800,
        entity=Assets.AEG099_001_9000,
        region=1040532800,
        flag_1=1040532805,
        flag_2=1040532806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1040530800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1040530800,
        bgm_boss_conv_param_id=920900,
        flag_1=1040532805,
        flag_2=1040532806,
        right=0,
        flag_3=1040532802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, 1040530800, 1040531801, 3, 0, 0)


@RestartOnRest(1040532650)
def Event_1040532650():
    """Event 1040532650"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1040532650, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG003_316_9000)
    CreateVFX(1040532650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG003_316_9000)
    DeleteVFX(1040532650, erase_root_only=False)
    End()


@RestartOnRest(1040532660)
def Event_1040532660():
    """Event 1040532660"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1040530655):
        return
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1040532651))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9521, entity=Assets.AEG003_316_9000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1040530655)
    DisableAsset(Assets.AEG003_316_9000)
    DisableMapPiece(map_piece_id=1040532651)
    RotateToFaceEntity(PLAYER, Assets.AEG003_316_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532665)
def Event_1040532665():
    """Event 1040532665"""
    MAIN.Await(FlagEnabled(1040530655))
    
    Wait(1.0)
    PlaySoundEffect(1040532650, 806855, sound_type=SoundType.s_SFX)
    DeleteVFX(1040532650)
    End()


@RestartOnRest(1040532670)
def Event_1040532670():
    """Event 1040532670"""
    GotoIfFlagEnabled(Label.L0, flag=1040530655)
    DisableAsset(Assets.AEG007_234_1000)
    
    MAIN.Await(FlagEnabled(1039530505))
    
    EnableAsset(Assets.AEG007_234_1000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG007_234_1000)
    End()


@RestartOnRest(1040532680)
def Event_1040532680():
    """Event 1040532680"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=1040531651, attacker=20000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1040530680)
    End()


@RestartOnRest(1040532685)
def Event_1040532685():
    """Event 1040532685"""
    MAIN.Await(FlagEnabled(1040530680))
    
    ForceAnimation(Assets.AEG007_234_1000, 1, wait_for_completion=True)
    DisableAsset(Assets.AEG007_234_1000)
    End()


@RestartOnRest(1040532690)
def Event_1040532690():
    """Event 1040532690"""
    AND_15.Add(FlagEnabled(1040530655))
    GotoIfConditionTrue(Label.L2, input_condition=AND_15)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)

    # --- Label 2 --- #
    DefineLabel(2)
    Kill(Characters.Imp, award_runes=True)
    if AND_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1040533610)
    GotoIfFlagEnabled(Label.L1, flag=1040532701)
    DisableSpawner(entity=1040533610)
    AND_1.Add(FlagEnabled(1039530505))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1040532610))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=1040533610)
    ClearTargetList(Characters.Imp)
    MakeEnemyAppear(character=1040533610)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterDead(Characters.Imp))
    SkipLinesIfConditionFalse(4, AND_2)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=10.0)
    EnableSpawner(entity=1040533610)
    ClearTargetList(Characters.Imp)
    MakeEnemyAppear(character=1040533610)
    if FlagEnabled(1040530655):
        Wait(5.0)
    DisableSpawner(entity=1040533610)
    EnableFlag(1040532701)
    Restart()
