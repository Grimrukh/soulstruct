"""
Land of Shadow 11-10 SE NW

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
    Event_2046412800()
    Event_2046412810()
    Event_2046412849()
    CommonFunc_900005610(0, asset=2046411550, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(2046412800)
def Event_2046412800():
    """Event 2046412800"""
    if FlagEnabled(2046410800):
        return
    
    MAIN.Await(HealthValue(2046410800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2046410800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2046410800))
    
    KillBossAndDisplayBanner(character=2046410800, banner_type=BannerType.EnemyFelled)
    EnableFlag(2046410800)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    AwardItemLot(30820, host_only=True)
    End()


@RestartOnRest(2046412810)
def Event_2046412810():
    """Event 2046412810"""
    GotoIfFlagDisabled(Label.L0, flag=2046410800)
    DisableCharacter(2046410800)
    DisableAnimations(2046410800)
    Kill(2046410800)
    if PlayerNotInOwnWorld():
        return
    Wait(1.0)
    AwardItemLot(30820, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2046410800)
    SetTeamType(2046410800, TeamType.Enemy)
    DisableCharacter(2046410800)
    AND_2.Add(FlagEnabled(2046412805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2046412800))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(2046410800)
    ForceAnimation(2046410800, 63100, wait_for_completion=True)
    AddSpecialEffect(2046410800, 20018696)
    WaitRealFrames(frames=1)
    EnableAI(2046410800)
    SetNetworkUpdateRate(2046410800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2046410800, name=900000563)


@RestartOnRest(2046412849)
def Event_2046412849():
    """Event 2046412849"""
    CommonFunc_9005800(
        0,
        flag=2046410800,
        entity=2046411800,
        region=2046412800,
        flag_1=2046412805,
        character=2046415800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2046410800,
        entity=2046411800,
        region=2046412800,
        flag_1=2046412805,
        flag_2=2046412806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2046410800, asset=2046411800, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=2046410800,
        bgm_boss_conv_param_id=921100,
        flag_1=2046412805,
        flag_2=2046412806,
        right=0,
        flag_3=2046412802,
        left=0,
        left_1=0,
    )
