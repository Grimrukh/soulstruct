"""
Land of Shadow 11-11 (Alternate) SE NW

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
    Event_2046452800()
    Event_2046452810()
    Event_2046452849()
    CommonFunc_90005250(0, character=2046450200, region=2046452200, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=2046450319, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450320, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450321, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450322, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450323, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450325, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450329, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450332, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450336, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450339, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450340, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450341, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450342, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450343, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450344, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450345, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450352, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450353, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450354, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450355, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450356, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=2046450365, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_900005610(0, asset=2046451599, dummy_id=100, vfx_id=800, right=0)
    Event_2046452550(
        0,
        character=580410,
        flag=580110,
        character_1=2046450550,
        animation_id=30015,
        animation_id_1=20015,
        asset=2046451550,
        asset_1=2046451560,
    )


@RestartOnRest(2046452550)
def Event_2046452550(
    _,
    character: uint,
    flag: Flag | int,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    asset: uint,
    asset_1: Asset | int,
):
    """Event 2046452550"""
    AddSpecialEffect(character, 10124)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAsset(asset)
    DisableAsset(asset_1)
    DisableTreasure(asset=asset_1)
    if FlagEnabled(character):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=15.0))
    AND_1.Add(FlagEnabled(330))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    RemoveSpecialEffect(character, 10124)
    ForceAnimation(character_1, animation_id)
    EnableAsset(asset)
    EnableAsset(asset_1)
    ForceAnimation(asset, 2)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character_1, animation_id_1)
    ForceAnimation(asset, 1)
    Wait(3.799999952316284)
    DisableCharacter(character_1)
    DisableAsset(asset)
    EnableTreasure(asset=asset_1)


@RestartOnRest(2046452800)
def Event_2046452800():
    """Event 2046452800"""
    Unknown_2004_76(flag=2046450800, item_lot=30900)
    if FlagEnabled(2046450800):
        return
    
    MAIN.Await(HealthValue(2046450800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2046450800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2046450800))
    
    KillBossAndDisplayBanner(character=2046450800, banner_type=BannerType.EnemyFelled)
    EnableFlag(2046450800)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    AwardItemLot(30900, host_only=True)
    End()


@RestartOnRest(2046452810)
def Event_2046452810():
    """Event 2046452810"""
    GotoIfFlagDisabled(Label.L0, flag=2046450800)
    DisableCharacter(2046450800)
    DisableAnimations(2046450800)
    Kill(2046450800)
    if PlayerNotInOwnWorld():
        return
    Wait(1.0)
    AwardItemLot(30900, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2046450800)
    SetTeamType(2046450800, TeamType.Enemy)
    DisableCharacter(2046450800)
    AND_2.Add(FlagEnabled(2046452805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2046452800))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(2046450800)
    ForceAnimation(2046450800, 63100, wait_for_completion=True)
    WaitRealFrames(frames=1)
    EnableAI(2046450800)
    SetNetworkUpdateRate(2046450800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2046450800, name=900000560)


@RestartOnRest(2046452849)
def Event_2046452849():
    """Event 2046452849"""
    CommonFunc_9005800(
        0,
        flag=2046450800,
        entity=2046451800,
        region=2046452800,
        flag_1=2046452805,
        character=2046455800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2046450800,
        entity=2046451800,
        region=2046452800,
        flag_1=2046452805,
        flag_2=2046452806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2046450800, asset=2046451800, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=2046450800,
        bgm_boss_conv_param_id=921100,
        flag_1=2046452805,
        flag_2=2046452806,
        right=0,
        flag_3=2046452802,
        left=0,
        left_1=0,
    )
