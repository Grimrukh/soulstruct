"""
South Weeping Peninsula (NE) (SE)

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
from .entities.m60_43_30_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=1043300800,
        grace_flag=76161,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_1043302800()
    Event_1043302810()
    Event_1043302849()
    CommonFunc_90005780(
        0,
        flag=1043300800,
        summon_flag=1043302701,
        dismissal_flag=1043302161,
        character=Characters.Edgar,
        sign_type=20,
        region=1043302701,
        right=1043319209,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1043300800, flag_1=1043302701, flag_2=1043302161, character=Characters.Edgar)
    CommonFunc_90005782(0, 1043302701, 1043302805, 1043300700, 1043302850, 1043302809, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(0, 1043300340, 30001, 20001, 1043302340, 0.5, 0, 0, 0, 0)


@RestartOnRest(1043302500)
def Event_1043302500():
    """Event 1043302500"""
    EnableCharacter(0)
    EnableAnimations(0)


@RestartOnRest(1043302800)
def Event_1043302800():
    """Event 1043302800"""
    if FlagEnabled(1043300800):
        return
    
    MAIN.Await(HealthValue(Characters.LeonineMisbegotten) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.LeonineMisbegotten, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.LeonineMisbegotten))
    
    KillBossAndDisplayBanner(character=Characters.LeonineMisbegotten, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(1043300800)
    EnableFlag(9180)
    if PlayerInOwnWorld():
        EnableFlag(61180)
    End()


@RestartOnRest(1043302810)
def Event_1043302810():
    """Event 1043302810"""
    GotoIfFlagDisabled(Label.L0, flag=1043300800)
    DisableCharacter(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    Kill(Characters.LeonineMisbegotten)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.LeonineMisbegotten)
    SetLockOnPoint(character=Characters.LeonineMisbegotten, lock_on_model_point=220, state=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1043302805))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1043302850))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LeonineMisbegotten, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=Characters.LeonineMisbegotten, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.LeonineMisbegotten, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.LeonineMisbegotten, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.LeonineMisbegotten, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.LeonineMisbegotten, state_info=260))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.LeonineMisbegotten)
    SetNetworkUpdateRate(Characters.LeonineMisbegotten, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.LeonineMisbegotten, name=903460500)
    SetLockOnPoint(character=Characters.LeonineMisbegotten, lock_on_model_point=220, state=True)
    AddSpecialEffect(Characters.LeonineMisbegotten, 8089)


@RestartOnRest(1043302849)
def Event_1043302849():
    """Event 1043302849"""
    CommonFunc_9005800(
        0,
        flag=1043300800,
        entity=Assets.AEG099_002_9000,
        region=1043302850,
        flag_1=1043302805,
        character=1043305800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1043300800,
        entity=Assets.AEG099_002_9000,
        region=1043302850,
        flag_1=1043302805,
        flag_2=1043302806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1043300800, asset=Assets.AEG099_002_9000, model_point=5, right=0)
    CommonFunc_9005822(0, 1043300800, 950000, 1043302805, 1043302806, 0, 0, 0, 0)
