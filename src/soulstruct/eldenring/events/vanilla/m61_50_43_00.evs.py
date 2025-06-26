"""
Land of Shadow 12-10 NE NW

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
    RegisterGrace(grace_flag=2050430000, asset=2050431950, enemy_block_distance=0.0)
    Event_2050432300(
        0,
        character=2050430200,
        patrol_information_id=2050433200,
        region=2050432200,
        flag=2050432200,
        seconds=0.0,
    )
    Event_2050432300(
        1,
        character=2050430201,
        patrol_information_id=2050433201,
        region=2050432200,
        flag=2050432200,
        seconds=0.0,
    )
    Event_2050432300(
        2,
        character=2050430230,
        patrol_information_id=2050433230,
        region=2050432200,
        flag=2050432200,
        seconds=5.0,
    )
    CommonFunc_90005261(0, character=2050430200, region=2050432201, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=2050430201, region=2050432201, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=2050430230, region=2050432201, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2050430291, region=2050432291, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430253, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430250, radius=25.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430251, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430252, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430263, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2050430257, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=2050430311, region=2050430311, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_900005580(0, flag=580600, asset=2050431500, flag_1=9146)
    CommonFunc_90005748(0, entity=2050431700, action_button_id=206020, text=1030021, display_distance=30.0, flag=4911)


@RestartOnRest(2050432300)
def Event_2050432300(
    _,
    character: Character | int,
    patrol_information_id: uint,
    region: Region | int,
    flag: Flag | int,
    seconds: float,
):
    """Event 2050432300"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    EnableNetworkFlag(flag)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(2050432800)
def Event_2050432800():
    """Event 2050432800"""
    if FlagEnabled(2050430800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterDead(2050430710))
    AND_1.Add(FlagEnabled(2050432810))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    KillBossAndDisplayBanner(character=2050430710, banner_type=BannerType.EnemyFelled)
    DeactivateGparamOverride(change_duration=10.0)
    EnableNetworkFlag(2050430800)
    Wait(5.0)
    AddSpecialEffect(ALL_PLAYERS, 8870)
    Wait(2.0)
    DisableFlag(2050432810)
    WarpToMap(game_map=LANDOFSHADOW_12_10_NE_NW, player_start=2049442721, unk_8_12=61504300)
    End()


@RestartOnRest(2050432801)
def Event_2050432801():
    """Event 2050432801"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2050430800):
        return
    if FlagEnabled(2050430801):
        return
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagEnabled(2049442702))
    
    MAIN.Await(AND_1)
    
    OR_3.Add(Multiplayer())
    OR_3.Add(MultiplayerPending())
    if OR_3:
        return RESTART
    AddSpecialEffect(PLAYER, 514)
    Wait(1.5)
    EnableNetworkFlag(2050430801)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=2050432810,
        dummy_id=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=True,
        reset_camera=True,
    )
    EnableFlag(9021)
    End()


@RestartOnRest(2050432802)
def Event_2050432802():
    """Event 2050432802"""
    GotoIfFlagDisabled(Label.L0, flag=2050430800)
    DisableCharacter(2050430710)
    DisableAnimations(2050430710)
    Kill(2050430710)
    DisableAsset(2050431720)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2050430710)
    DisableAnimations(2050430710)
    DisableAI(2050430710)
    DisableAsset(2050431720)
    if FlagDisabled(2050430801):
        return
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    EnableFlag(1099002100)
    DisableCharacter(2050435810)
    EnableFlag(2050432810)
    AddSpecialEffect(PLAYER, 190)
    ActivateGparamOverride(gparam_sub_id=0, change_duration=0.0)
    SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=False)
    DisableCharacter(2050435800)
    DisableAnimations(2050435800)
    DisableAI(2050435800)
    DisableHealthBar(2050430710)
    DisableNetworkFlag(2050430801)
    AddSpecialEffect(PLAYER, 514)
    EnableAsset(2050431720)
    MoveAssetToCharacter(2050431720, character=2050431801, dummy_id=100)
    CreateAssetVFX(2050431720, dummy_id=200, vfx_id=806700)
    EnableCharacter(2050430710)
    Move(2050430710, destination=2050432812, destination_type=CoordEntityType.Region, short_move=True)
    EnableAnimations(2050430710)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2050430710, radius=10.0))
    OR_1.Add(TimeElapsed(seconds=5.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2050430710, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2050430710))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1099002100)
    EnableAI(2050430710)
    SetNetworkUpdateRate(2050430710, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(2050432805)
    Wait(1.0)
    EnableBossHealthBar(2050430710, name=142501)


@RestartOnRest(2050432805)
def Event_2050432805():
    """Event 2050432805"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=2050430800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(2050432805))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    SetBossMusic(bgm_boss_conv_param_id=921100, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(2050432802))
    OR_2.Add(FlagEnabled(2050430800))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=2050430800)
    WaitFrames(frames=1)
    SetBossMusic(bgm_boss_conv_param_id=925000, state=BossMusicState.HeatUp)
    OR_3.Add(FlagEnabled(2050430800))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SetBossMusic(bgm_boss_conv_param_id=925000, state=BossMusicState.NormalFadeOut)
