"""
Divine Tower of Caelid

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
from .enums.m34_13_00_00_enums import *
from .enums.m31_12_00_00_enums import Assets as m31_12_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34130001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=34130002, asset=Assets.AEG099_060_9002)
    Event_34132800()
    Event_34132810()
    Event_34132849()
    CommonFunc_90005110(
        0,
        flag=192,
        flag_1=9130,
        asset=Assets.AEG099_991_9000,
        item_lot=34130050,
        item=8149,
        model_point=806930,
        action_button_id=9081,
        animation_id=60520,
        left=0,
    )
    CommonFunc_90005920(0, flag=34130600, asset=Assets.AEG099_630_9000, obj_act_id=34133600)
    CommonFunc_90005646(
        0,
        flag=34130800,
        left_flag=34132840,
        cancel_flag__right_flag=34132841,
        asset=Assets.AEG099_065_9000,
        player_start=1049410300,
        area_id=60,
        block_id=49,
        cc_id=41,
        dd_id=0,
    )
    CommonFunc_90005508(
        0,
        flag=34130510,
        flag_1=34131510,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0500,
        asset_1=Assets.AEG027_203_0501,
        flag_2=34130511,
    )
    CommonFunc_90005508(
        0,
        flag=34130515,
        flag_1=34131515,
        left=0,
        entity=Assets.AEG027_099_0500,
        asset=Assets.AEG027_203_0503,
        asset_1=Assets.AEG027_203_0502,
        flag_2=34130516,
    )
    CommonFunc_90005508(
        0,
        flag=34130520,
        flag_1=34131520,
        left=1,
        entity=Assets.AEG027_099_0501,
        asset=Assets.AEG027_203_0504,
        asset_1=Assets.AEG027_203_0505,
        flag_2=34130521,
    )
    Event_34132510()
    Event_34132515()
    Event_34132520()
    Event_34132580()
    CommonFunc_90005511(
        0,
        flag=34130560,
        asset=Assets.AEG027_072_0500,
        obj_act_id=34133560,
        obj_act_id_1=227010,
        left=0,
    )
    CommonFunc_90005512(0, flag=34130560, region=34132560, region_1=34132561)
    Event_34132590(0, entity=Assets.AEG027_073_0500, region=34132590, animation_id=1, asset=Assets.AEG027_074_0500)
    Event_34132590(
        1,
        entity=Assets.AEG027_073_0501,
        region=34132591,
        animation_id=1000001,
        asset=Assets.AEG027_074_0501,
    )
    CommonFunc_90005690(0, region=34132592)
    CommonFunc_90005691(0, region=34132592)
    CommonFunc_90005690(0, region=34132593)
    CommonFunc_90005691(0, region=34132593)
    CommonFunc_90005250(0, character=Characters.GodskinMonk0, region=34132299, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GodskinMonk1, radius=10.0, seconds=0.0, animation_id=-1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_34130519()


@ContinueOnRest(34132510)
def Event_34132510():
    """Event 34132510"""
    CommonFunc_90005507(
        0,
        flag=34130510,
        flag_1=34131510,
        left=0,
        asset=Assets.AEG027_070_0500,
        entity=Assets.AEG027_203_0500,
        region=34132513,
        entity_1=Assets.AEG027_203_0501,
        region_1=34132514,
        region_2=34132511,
        region_3=34132512,
        flag_2=34130511,
        flag_3=34132512,
        left_1=0,
    )


@ContinueOnRest(34132515)
def Event_34132515():
    """Event 34132515"""
    CommonFunc_90005507(
        0,
        flag=34130515,
        flag_1=34131515,
        left=0,
        asset=Assets.AEG027_099_0500,
        entity=Assets.AEG027_203_0503,
        region=34132518,
        entity_1=Assets.AEG027_203_0502,
        region_1=34132519,
        region_2=34132516,
        region_3=34132517,
        flag_2=34130516,
        flag_3=34132517,
        left_1=0,
    )


@ContinueOnRest(34132520)
def Event_34132520():
    """Event 34132520"""
    CommonFunc_90005507(
        0,
        flag=34130520,
        flag_1=34131520,
        left=1,
        asset=Assets.AEG027_099_0501,
        entity=Assets.AEG027_203_0504,
        region=34132523,
        entity_1=Assets.AEG027_203_0505,
        region_1=34132524,
        region_2=34132521,
        region_3=34132522,
        flag_2=34130521,
        flag_3=34132522,
        left_1=0,
    )


@RestartOnRest(34130519)
def Event_34130519():
    """Event 34130519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(34130520)


@ContinueOnRest(34132580)
def Event_34132580():
    """Event 34132580"""
    RegisterLadder(start_climbing_flag=34130580, stop_climbing_flag=34130581, asset=Assets.AEG027_071_0500)


@RestartOnRest(34132590)
def Event_34132590(_, entity: uint, region: uint, animation_id: int, asset: uint):
    """Event 34132590"""
    ForceAnimation(entity, 0)
    if AssetDestroyed(asset):
        RestoreAsset(asset)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    DestroyAsset(asset, request_slot=0)
    ForceAnimation(entity, animation_id)


@RestartOnRest(34132800)
def Event_34132800():
    """Event 34132800"""
    if FlagEnabled(34130800):
        return
    
    MAIN.Await(HealthValue(Characters.GodskinApostle) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GodskinApostle, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GodskinApostle))
    
    KillBossAndDisplayBanner(character=Characters.GodskinApostle, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(34130800)
    EnableFlag(9173)
    if PlayerInOwnWorld():
        EnableFlag(61173)


@RestartOnRest(34132810)
def Event_34132810():
    """Event 34132810"""
    GotoIfFlagDisabled(Label.L0, flag=34130800)
    DisableCharacter(Characters.GodskinApostle)
    DisableAnimations(Characters.GodskinApostle)
    Kill(Characters.GodskinApostle)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GodskinApostle)
    DisableAnimations(Characters.GodskinApostle)
    AND_1.Add(FlagEnabled(34132805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34132800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinApostle, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.GodskinApostle)
    EnableAnimations(Characters.GodskinApostle)
    SetNetworkUpdateRate(Characters.GodskinApostle, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodskinApostle, name=903560000)


@RestartOnRest(34132849)
def Event_34132849():
    """Event 34132849"""
    CommonFunc_9005800(
        0,
        flag=34130800,
        entity=Assets.AEG099_001_9000,
        region=34132800,
        flag_1=34132805,
        character=34135800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=34130800,
        entity=Assets.AEG099_001_9000,
        region=34132800,
        flag_1=34132805,
        flag_2=34132806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=34130800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=34130800,
        bgm_boss_conv_param_id=930000,
        flag_1=34132805,
        flag_2=34132806,
        right=0,
        flag_3=34132802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=34130800,
        entity=m31_12_Assets.AEG099_001_9000,
        region=34132800,
        flag_1=34132805,
        character=31125800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=34130800,
        entity=m31_12_Assets.AEG099_001_9000,
        region=34132800,
        flag_1=34132805,
        flag_2=31122806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=34130800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005812(0, flag=34130800, asset=Assets.AEG099_001_9001, model_point=3, right=0, model_point_1=0)
    CommonFunc_9005822(
        0,
        flag=34130800,
        bgm_boss_conv_param_id=356000,
        flag_1=34132805,
        flag_2=34132806,
        right=0,
        flag_3=0,
        left=0,
        left_1=0,
    )
