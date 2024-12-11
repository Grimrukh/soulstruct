"""
Land of Shadow 11-09 NE SW

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
    Event_2046382800()
    Event_2046382810()
    Event_2046382849()
    CommonFunc_90005201(
        0,
        character=2046380210,
        animation_id=30001,
        animation_id_1=20001,
        radius=12.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2046380350, region=2046382350, seconds=0.0, animation_id=0)
    CommonFunc_900005610(0, asset=2046381500, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(2046382800)
def Event_2046382800():
    """Event 2046382800"""
    Unknown_2004_76(flag=2046380800, item_lot=30810)
    if FlagEnabled(2046380800):
        return
    
    MAIN.Await(HealthValue(2046380800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2046380800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2046380800))
    
    KillBossAndDisplayBanner(character=2046380800, banner_type=BannerType.EnemyFelled)
    EnableFlag(2046380800)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    AwardItemLot(30810, host_only=True)
    End()


@RestartOnRest(2046382810)
def Event_2046382810():
    """Event 2046382810"""
    GotoIfFlagDisabled(Label.L0, flag=2046380800)
    DisableCharacter(2046380800)
    DisableAnimations(2046380800)
    Kill(2046380800)
    if PlayerNotInOwnWorld():
        return
    Wait(1.0)
    AwardItemLot(30810, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2046380800)
    SetTeamType(2046380800, TeamType.Enemy)
    DisableCharacter(2046380800)
    AND_2.Add(FlagEnabled(2046382805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2046382800))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(2046380800)
    ForceAnimation(2046380800, 63100, wait_for_completion=True)
    AddSpecialEffect(2046380800, 20018712)
    WaitRealFrames(frames=1)
    EnableAI(2046380800)
    SetNetworkUpdateRate(2046380800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2046380800, name=900000561)


@RestartOnRest(2046382849)
def Event_2046382849():
    """Event 2046382849"""
    CommonFunc_9005800(
        0,
        flag=2046380800,
        entity=2046381800,
        region=2046382800,
        flag_1=2046382805,
        character=2046385800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2046380800,
        entity=2046381800,
        region=2046382800,
        flag_1=2046382805,
        flag_2=2046382806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2046380800, asset=2046381800, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=2046380800,
        bgm_boss_conv_param_id=921100,
        flag_1=2046382805,
        flag_2=2046382806,
        right=0,
        flag_3=2046382802,
        left=0,
        left_1=0,
    )
