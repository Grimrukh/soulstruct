"""
Land of Shadow 12-12 SW SE

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
    CommonFunc_9005810(
        0,
        flag=2049480800,
        grace_flag=2049480000,
        character=2049480950,
        asset=2049481950,
        enemy_block_distance=0.0,
    )
    RegisterGrace(grace_flag=2049480001, asset=2049481951, enemy_block_distance=0.0)
    Event_2049482800()
    Event_2049482810()
    Event_2049482811()
    Event_2049482849()


@RestartOnRest(2049482800)
def Event_2049482800():
    """Event 2049482800"""
    if FlagEnabled(2049480800):
        return
    
    MAIN.Await(HealthValue(2049480800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(2049480800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2049480800))
    
    KillBossAndDisplayBanner(character=2049480800, banner_type=BannerType.LegendFelled)
    EnableFlag(2049480800)
    EnableFlag(9164)
    if PlayerInOwnWorld():
        EnableFlag(61164)


@RestartOnRest(2049482810)
def Event_2049482810():
    """Event 2049482810"""
    GotoIfFlagDisabled(Label.L0, flag=2049480800)
    DisableCharacter(2049485800)
    DisableAnimations(2049485800)
    Kill(2049485800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2049485800)
    AddSpecialEffect(2049480100, 9531)
    DisableAnimations(2049485800)
    GotoIfFlagEnabled(Label.L1, flag=2049480801)
    AddSpecialEffect(2049480100, 9531)
    Move(2049480800, destination=2049482810, destination_type=CoordEntityType.Region, short_move=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2049482801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2049480800, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    EnableNetworkFlag(2049480801)
    EnableAnimations(2049485800)
    AddSpecialEffect(2049480800, 5000)
    ChangePatrolBehavior(2049480800, patrol_information_id=2049483810)
    WaitRealFrames(frames=1)
    EnableAI(2049485800)
    SetNetworkUpdateRate(2049485800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(2049480100, 9532)
    Wait(5.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(2049482805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2049482800))
    
    MAIN.Await(AND_2)
    
    EnableAnimations(2049485800)
    EnableAI(2049485800)
    SetNetworkUpdateRate(2049485800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(2049480100, 9532)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.5)
    EnableBossHealthBar(2049480800, name=905000000)


@RestartOnRest(2049482811)
def Event_2049482811():
    """Event 2049482811"""
    if FlagEnabled(2049480800):
        return
    AND_1.Add(CharacterHasSpecialEffect(2049480800, 10010048))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2049482802)


@RestartOnRest(2049482849)
def Event_2049482849():
    """Event 2049482849"""
    CommonFunc_9005800(
        0,
        flag=2049480800,
        entity=2049481800,
        region=2049482800,
        flag_1=2049482805,
        character=2049485800,
        action_button_id=10000,
        left=2049480801,
        region_1=2049482801,
    )
    CommonFunc_9005801(
        0,
        flag=2049480800,
        entity=2049481800,
        region=2049482800,
        flag_1=2049482805,
        flag_2=2049482806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2049480800, asset=2049481800, vfx_id=4, right=2049480801)
    CommonFunc_9005811(0, flag=2049480800, asset=2049481801, vfx_id=4, right=0)
    CommonFunc_9005822(
        0,
        flag=2049480800,
        bgm_boss_conv_param_id=950000,
        flag_1=2049482805,
        flag_2=2049482806,
        right=0,
        flag_3=2049482802,
        left=0,
        left_1=0,
    )
