"""
m43_01_00_00

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
    RegisterGrace(grace_flag=43010000, asset=43011950)
    RegisterGrace(grace_flag=43010001, asset=43011951)
    Event_43012800()
    Event_43012810()
    Event_43012811()
    Event_43012849()
    CommonFunc_90005251(0, character=43010300, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=43010200, region=43012200, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=43010201, region=43012201, seconds=0.0, animation_id=3014)
    CommonFunc_90005261(0, character=43010209, region=43012209, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=43010304, region=43012304, radius=30.0, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=43010205,
        animation_id=30014,
        animation_id_1=20014,
        region=43012205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43010206,
        animation_id=30014,
        animation_id_1=20014,
        region=43012205,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43010212,
        animation_id=30016,
        animation_id_1=20016,
        region=43012212,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=43010306, region=43012306, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=43010307,
        animation_id=30017,
        animation_id_1=20017,
        region=43012307,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=43010350, region=43012350, seconds=0.0, animation_id=3004)
    CommonFunc_90005301(0, flag=43010350, character=43010350, item_lot__unk1=43010900, seconds=0.0, unk1=0)
    CommonFunc_90005646(
        0,
        flag=43010800,
        left_flag=43012840,
        cancel_flag__right_flag=43012841,
        asset=43011840,
        player_start=43012840,
        area_id=43,
        block_id=1,
        cc_id=0,
        dd_id=0,
    )
    Event_43012500()
    CommonFunc_90005690(0, region=43012500)
    CommonFunc_90005691(0, region=43012500)
    CommonFunc_900005610(0, asset=43011680, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=43011681, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(43012500)
def Event_43012500():
    """Event 43012500"""
    if FlagEnabled(43010500):
        return
    DisableAssetActivation(43011540, obj_act_id=447080)
    
    MAIN.Await(FlagEnabled(43010800))
    
    EnableFlag(43010500)
    EnableAssetActivation(43011540, obj_act_id=447080)


@RestartOnRest(43012800)
def Event_43012800():
    """Event 43012800"""
    if FlagEnabled(43010800):
        return
    
    MAIN.Await(HealthValue(43010800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(43010800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(43010800))
    
    KillBossAndDisplayBanner(character=43010800, banner_type=BannerType.EnemyFelled)
    EnableFlag(43010800)
    EnableFlag(9281)
    if PlayerInOwnWorld():
        EnableFlag(61281)


@RestartOnRest(43012810)
def Event_43012810():
    """Event 43012810"""
    GotoIfFlagDisabled(Label.L0, flag=43010800)
    DisableCharacter(43015800)
    DisableAnimations(43015800)
    Kill(43015800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(43010800, TeamType.Enemy)
    DisableAI(43015800)
    DisableAnimations(43015800)
    AND_2.Add(FlagEnabled(43012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=43012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(43010800, 20018660)
    WaitRealFrames(frames=1)
    EnableAnimations(43015800)
    EnableAI(43010800)
    SetNetworkUpdateRate(43010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(43010800, name=140700)


@RestartOnRest(43012811)
def Event_43012811():
    """Event 43012811"""
    if FlagEnabled(43010800):
        return
    AND_1.Add(HealthRatio(43010800) <= 0.5)
    
    MAIN.Await(AND_1)
    
    EnableFlag(43012802)


@RestartOnRest(43012849)
def Event_43012849():
    """Event 43012849"""
    CommonFunc_9005800(
        0,
        flag=43010800,
        entity=43011800,
        region=43012800,
        flag_1=43012805,
        character=43015800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=43010800,
        entity=43011800,
        region=43012800,
        flag_1=43012805,
        flag_2=43012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=43010800, asset=43011800, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=43010800,
        bgm_boss_conv_param_id=920300,
        flag_1=43012805,
        flag_2=43012806,
        right=0,
        flag_3=43012802,
        left=0,
        left_1=0,
    )
