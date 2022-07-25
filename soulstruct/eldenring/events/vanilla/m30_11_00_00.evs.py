"""
Deathtouched Catacombs

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
from .entities.m30_11_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73011, asset=Assets.AEG099_060_9000)
    Event_30112800()
    Event_30112810()
    Event_30112849()
    Event_30112811()
    CommonFunc_90005616(0, flag=30117000, region=30112700)
    CommonFunc_90005650(
        0,
        flag=30110540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30113541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30110540, anchor_entity=Assets.AEG027_041_0500)
    Event_30112580()
    CommonFunc_90005646(
        0,
        flag=30110800,
        left_flag=30112840,
        cancel_flag__right_flag=30112841,
        asset=Assets.AEG099_065_9000,
        player_start=30112840,
        area_id=30,
        block_id=11,
        cc_id=0,
        dd_id=0,
    )
    Event_30110790(0, 30111520, 30110800)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton0,
        animation_id=30003,
        animation_id_1=20003,
        region=30112200,
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
        region=30112201,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton2,
        animation_id=30003,
        animation_id_1=20003,
        region=30112202,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton3,
        animation_id=30003,
        animation_id_1=20003,
        region=30112203,
        radius=1.0,
        seconds=0.0,
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
        region=30112205,
        radius=1.0,
        seconds=1.5,
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
        region=30112205,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.CatacombsSkeleton7,
        animation_id=30003,
        animation_id_1=20003,
        radius=5.0,
        seconds=0.0,
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
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton9,
        animation_id=30003,
        animation_id_1=20003,
        region=30112209,
        radius=1.0,
        seconds=0.5,
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
        region=30112209,
        radius=1.0,
        seconds=5.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton11,
        animation_id=30003,
        animation_id_1=20003,
        region=30112209,
        radius=1.0,
        seconds=10.5,
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
        region=30112209,
        radius=1.0,
        seconds=15.5,
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
        region=30112213,
        radius=0.0,
        seconds=1.5,
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
        region=30112213,
        radius=0.0,
        seconds=1.5,
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
        region=30112215,
        radius=3.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.CatacombsSkeleton16,
        animation_id=30003,
        animation_id_1=20003,
        region=30112215,
        radius=3.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(0, 30110217, 30003, 20003, 30112217, 3.0, 8.5, 0, 0, 0, 0)


@ContinueOnRest(30112580)
def Event_30112580():
    """Event 30112580"""
    RegisterLadder(start_climbing_flag=30110580, stop_climbing_flag=30110581, asset=30111580)


@RestartOnRest(30110790)
def Event_30110790(_, asset: uint, flag: uint):
    """Event 30110790"""
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


@RestartOnRest(30112800)
def Event_30112800():
    """Event 30112800"""
    if FlagEnabled(30110800):
        return
    
    MAIN.Await(HealthValue(Characters.BlackKnifeAssassin) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BlackKnifeAssassin, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.BlackKnifeAssassin))
    
    KillBossAndDisplayBanner(character=Characters.BlackKnifeAssassin, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG099_630_9000, obj_act_id=-1)
    EnableFlag(30110800)
    EnableFlag(9203)
    if PlayerInOwnWorld():
        EnableFlag(61203)


@RestartOnRest(30112810)
def Event_30112810():
    """Event 30112810"""
    GotoIfFlagDisabled(Label.L0, flag=30110800)
    DisableCharacter(Characters.BlackKnifeAssassin)
    DisableAnimations(Characters.BlackKnifeAssassin)
    Kill(Characters.BlackKnifeAssassin)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BlackKnifeAssassin)
    DisableHealthBar(Characters.BlackKnifeAssassin)
    DisableAssetActivation(Assets.AEG099_630_9000, obj_act_id=-1)
    ForceAnimation(Characters.BlackKnifeAssassin, 30000)
    AND_2.Add(FlagEnabled(30112805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30112800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.BlackKnifeAssassin)
    SetNetworkUpdateRate(Characters.BlackKnifeAssassin, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(Characters.BlackKnifeAssassin, 4404)
    Wait(1.0)
    EnableBossHealthBar(Characters.BlackKnifeAssassin, name=902100300)
    Wait(0.699999988079071)
    ForceAnimation(Characters.BlackKnifeAssassin, 20000)


@RestartOnRest(30112811)
def Event_30112811():
    """Event 30112811"""
    if FlagEnabled(30110800):
        return
    AND_1.Add(HealthRatio(Characters.BlackKnifeAssassin) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30112802)


@RestartOnRest(30112849)
def Event_30112849():
    """Event 30112849"""
    CommonFunc_9005800(
        0,
        flag=30110800,
        entity=Assets.AEG099_001_9000,
        region=30112800,
        flag_1=30112805,
        character=30115800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30110800,
        entity=Assets.AEG099_001_9000,
        region=30112800,
        flag_1=30112805,
        flag_2=30112806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30110800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30110800, 921500, 30112805, 30112806, 0, 30112802, 0, 0)


@RestartOnRest(30112900)
def Event_30112900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 30112900"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(700690):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(700690))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    EnableFlag(700690)
