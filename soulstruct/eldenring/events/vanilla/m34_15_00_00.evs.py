"""
Isolated Divine Tower

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
from .entities.m34_15_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34150000, asset=Assets.AEG099_060_9000)
    Event_34152500()
    CommonFunc_90005508(
        0,
        flag=34150510,
        flag_1=34151510,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0501,
        asset_1=Assets.AEG027_203_0500,
        flag_2=34150511,
    )
    CommonFunc_90005110(
        0,
        flag=196,
        flag_1=9120,
        asset=Assets.AEG099_991_9000,
        item_lot=34150000,
        item=8153,
        model_point=806940,
        action_button_id=9085,
        animation_id=60525,
        left=0,
    )


@ContinueOnRest(34152500)
def Event_34152500():
    """Event 34152500"""
    CommonFunc_90005507(
        0,
        flag=34150510,
        flag_1=34151510,
        left=0,
        asset=Assets.AEG027_070_0500,
        entity=Assets.AEG027_203_0501,
        region=34152513,
        entity_1=Assets.AEG027_203_0500,
        region_1=34152514,
        region_2=34152511,
        region_3=34152512,
        flag_2=34150511,
        flag_3=34152512,
        left_1=0,
    )


@RestartOnRest(34152800)
def Event_34152800():
    """Event 34152800"""
    if FlagEnabled(34150800):
        return
    
    MAIN.Await(HealthValue(34150800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(34150800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(34150800))
    
    KillBossAndDisplayBanner(character=34150800, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(34150800)


@RestartOnRest(34152810)
def Event_34152810():
    """Event 34152810"""
    GotoIfFlagDisabled(Label.L0, flag=34150800)
    DisableCharacter(34150800)
    DisableAnimations(34150800)
    Kill(34150800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34150800)
    DisableAnimations(34150800)
    AND_1.Add(FlagEnabled(34152805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34152800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=34150800, attacker=PLAYER))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34150800)
    EnableAnimations(34150800)
    SetNetworkUpdateRate(34150800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34150800)


@RestartOnRest(34152849)
def Event_34152849():
    """Event 34152849"""
    CommonFunc_9005800(
        0,
        flag=34150800,
        entity=34151800,
        region=34152800,
        flag_1=34152805,
        character=34155800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=34150800,
        entity=34151800,
        region=34152800,
        flag_1=34152805,
        flag_2=34152806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=34150800, asset=34151800, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=34150800,
        bgm_boss_conv_param_id=900000,
        flag_1=34152805,
        flag_2=34152806,
        right=0,
        flag_3=11002852,
        left=0,
        left_1=0,
    )
