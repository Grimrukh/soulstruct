"""
Cave of the Forlorn

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
from .entities.m31_12_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31120000, asset=Assets.AEG099_060_9000)
    Event_31122800()
    Event_31122810()
    Event_31122849()
    Event_31122811()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005646(
        0,
        flag=31120800,
        left_flag=31122840,
        cancel_flag__right_flag=31122841,
        asset=Assets.AEG099_065_9000,
        player_start=31122840,
        area_id=31,
        block_id=12,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten1,
        animation_id=30000,
        animation_id_1=20000,
        region=31122201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=31120213,
        animation_id=30000,
        animation_id_1=20000,
        region=31122201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten2,
        animation_id=30000,
        animation_id_1=20000,
        region=31122204,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.ScalyMisbegotten1,
        animation_id=30000,
        animation_id_1=20000,
        region=31122204,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Misbegotten0, region=31122203, seconds=0.0, animation_id=1700)
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten0, region=31122203, seconds=0.0, animation_id=1700)
    CommonFunc_90005250(0, character=Characters.SpiritJellyfish0, region=31122205, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SpiritJellyfish0, region=31122220, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SpiritJellyfish1, region=31122205, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.SpiritJellyfish1, region=31122220, seconds=0.0, animation_id=0)


@RestartOnRest(31122800)
def Event_31122800():
    """Event 31122800"""
    if FlagEnabled(31120800):
        return
    
    MAIN.Await(HealthValue(Characters.LeonineMisbegotten) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.LeonineMisbegotten, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.LeonineMisbegotten))
    
    KillBossAndDisplayBanner(character=Characters.LeonineMisbegotten, banner_type=BannerType.EnemyFelled)
    EnableFlag(31120800)
    EnableFlag(9247)
    if PlayerInOwnWorld():
        EnableFlag(61247)


@RestartOnRest(31122810)
def Event_31122810():
    """Event 31122810"""
    GotoIfFlagDisabled(Label.L0, flag=31120800)
    DisableCharacter(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    Kill(Characters.LeonineMisbegotten)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    GotoIfFlagEnabled(Label.L1, flag=31120802)
    AND_1.Add(FlagEnabled(31122805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31122800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LeonineMisbegotten, attacker=PLAYER))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.LeonineMisbegotten)
    EnableAnimations(Characters.LeonineMisbegotten)
    SetNetworkUpdateRate(Characters.LeonineMisbegotten, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.LeonineMisbegotten, name=903460310)


@RestartOnRest(31122811)
def Event_31122811():
    """Event 31122811"""
    if FlagEnabled(31120800):
        return
    AND_1.Add(HealthRatio(Characters.LeonineMisbegotten) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31122802)


@RestartOnRest(31122849)
def Event_31122849():
    """Event 31122849"""
    CommonFunc_9005800(
        0,
        flag=31120800,
        entity=Assets.AEG099_001_9000,
        region=31122800,
        flag_1=31122805,
        character=31125800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31120800,
        entity=Assets.AEG099_001_9000,
        region=31122800,
        flag_1=31122805,
        flag_2=31122806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31120800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=31120800,
        bgm_boss_conv_param_id=950000,
        flag_1=31122805,
        flag_2=31122806,
        right=0,
        flag_3=31122802,
        left=0,
        left_1=0,
    )
