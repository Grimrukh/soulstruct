"""
Land of Shadow 12-11 SE SE

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
    RegisterGrace(grace_flag=2051440000, asset=2051441950)
    Event_2051442800()
    Event_2051442810()
    Event_2051442849()
    CommonFunc_90005250(0, character=2051440200, region=2051442210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2051440202, region=2051442210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2051440203, region=2051442210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2051440204, region=2051442210, seconds=0.0, animation_id=-1)
    CommonFunc_90005301(0, flag=2051440300, character=2051440300, item_lot__unk1=2051440500, seconds=3.0, unk1=0)
    CommonFunc_90005301(0, flag=2051440310, character=2051440310, item_lot__unk1=2051440510, seconds=3.0, unk1=0)
    CommonFunc_900005610(0, asset=2051441270, dummy_id=100, vfx_id=800, right=0)
    Event_2051442490()


@RestartOnRest(2051442490)
def Event_2051442490():
    """Event 2051442490"""
    if FlagEnabled(4927):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2051442490))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(4927)
    AddSpecialEffect(ALL_PLAYERS, 20004230)


@RestartOnRest(2051442800)
def Event_2051442800():
    """Event 2051442800"""
    Unknown_2004_76(flag=2051440800, item_lot=30830)
    if FlagEnabled(2051440800):
        return
    
    MAIN.Await(HealthValue(2051440800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2051440800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2051440800))
    
    KillBossAndDisplayBanner(character=2051440800, banner_type=BannerType.EnemyFelled)
    EnableFlag(2051440800)
    if PlayerNotInOwnWorld():
        return
    Wait(5.0)
    AwardItemLot(30830, host_only=True)
    End()


@RestartOnRest(2051442810)
def Event_2051442810():
    """Event 2051442810"""
    GotoIfFlagDisabled(Label.L0, flag=2051440800)
    DisableCharacter(2051440800)
    DisableAnimations(2051440800)
    Kill(2051440800)
    if PlayerNotInOwnWorld():
        return
    Wait(1.0)
    AwardItemLot(30830, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2051440800)
    SetTeamType(2051440800, TeamType.Enemy)
    DisableCharacter(2051440800)
    AND_2.Add(FlagEnabled(2051442805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2051442800))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(2051440800)
    ForceAnimation(2051440800, 63100, wait_for_completion=True)
    AddSpecialEffect(2051440800, 20018695)
    WaitRealFrames(frames=1)
    EnableAI(2051440800)
    SetNetworkUpdateRate(2051440800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(2051440800, name=900000562)


@RestartOnRest(2051442849)
def Event_2051442849():
    """Event 2051442849"""
    CommonFunc_9005800(
        0,
        flag=2051440800,
        entity=2051441800,
        region=2051442800,
        flag_1=2051442805,
        character=2051445800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2051440800,
        entity=2051441800,
        region=2051442800,
        flag_1=2051442805,
        flag_2=2051442806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2051440800, asset=2051441800, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=2051440800,
        bgm_boss_conv_param_id=921100,
        flag_1=2051442805,
        flag_2=2051442806,
        right=0,
        flag_3=2051442802,
        left=0,
        left_1=0,
    )
