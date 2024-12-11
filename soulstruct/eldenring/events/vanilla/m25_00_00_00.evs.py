"""
METYR_ARENA

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
        flag=25000800,
        grace_flag=25000000,
        character=25000950,
        asset=25001950,
        enemy_block_distance=5.0,
    )
    Event_25002800()
    Event_25002810()
    Event_25002849()
    Event_25002812()
    Event_25002811()
    Event_25002819()
    Event_25002820(0, character=25000820, flag=25002820)
    Event_25002820(1, character=25000821, flag=25002821)
    Event_25002820(2, character=25000822, flag=25002822)
    Event_25002820(3, character=25000823, flag=25002823)
    Event_25002820(4, character=25000824, flag=25002824)
    Event_25002820(5, character=25000825, flag=25002825)
    Event_25002820(6, character=25000826, flag=25002826)
    Event_25002820(7, character=25000827, flag=25002827)
    Event_25002820(8, character=25000828, flag=25002828)
    Event_25002820(9, character=25000829, flag=25002829)
    Event_25002820(10, character=25000830, flag=25002830)
    Event_25002820(11, character=25000831, flag=25002831)
    Event_25002820(12, character=25000832, flag=25002832)
    Event_25002820(13, character=25000833, flag=25002833)
    Event_25002820(14, character=25000834, flag=25002834)
    Event_25000700(0, flag=2051459725, flag_1=25002805)
    Event_25000701(0, flag=2051459207, flag_1=25000800, flag_2=2051459750, flag_3=2051459751, flag_4=2051459752)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_25002200()


@RestartOnRest(25002200)
def Event_25002200():
    """Event 25002200"""
    DisableNetworkSync()
    if FlagEnabled(25000800):
        return
    AND_1.Add(InsideMap(game_map=METYR_ARENA))
    AND_1.Add(FlagDisabled(25000800))
    
    MAIN.Await(AND_1)


@RestartOnRest(25000700)
def Event_25000700(_, flag: Flag | int, flag_1: Flag | int):
    """Event 25000700"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag)
    End()


@RestartOnRest(25000701)
def Event_25000701(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int, flag_4: Flag | int):
    """Event 25000701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    End()


@RestartOnRest(25002800)
def Event_25002800():
    """Event 25002800"""
    if FlagEnabled(25000800):
        return
    
    MAIN.Await(HealthValue(25000800) <= 0)
    
    Kill(25000820)
    Kill(25000821)
    Kill(25000822)
    Kill(25000823)
    Kill(25000824)
    Kill(25000825)
    Kill(25000826)
    Kill(25000827)
    Kill(25000828)
    Kill(25000829)
    Kill(25000830)
    Kill(25000831)
    Kill(25000832)
    Kill(25000833)
    Kill(25000834)
    Wait(4.0)
    PlaySoundEffect(25000800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(25000800))
    
    KillBossAndDisplayBanner(character=25000800, banner_type=BannerType.LegendFelled)
    EnableFlag(25000800)
    EnableFlag(9155)
    if PlayerInOwnWorld():
        EnableFlag(61155)


@RestartOnRest(25002810)
def Event_25002810():
    """Event 25002810"""
    GotoIfFlagDisabled(Label.L0, flag=25000800)
    DisableCharacter(25000800)
    DisableAnimations(25000800)
    Kill(25000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(25000800)
    DisableHealthBar(25000800)
    SetLockOnPoint(character=25000800, lock_on_dummy_id=220, state=False)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=25002800))
    AND_1.Add(CharacterBackreadEnabled(25000800))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=25000800))
    OR_2.Add(CharacterHasStateInfo(character=25000800, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=25000800, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=25000800, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=25000800, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=25000800, state_info=260))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(25002803)
    Wait(0.10000000149011612)
    EnableNetworkFlag(25000801)
    if PlayerInOwnWorld():
        EnableNetworkFlag(2051452602)
    EnableNetworkFlag(25002801)
    SetLockOnPoint(character=25000800, lock_on_dummy_id=220, state=True)
    EnableAI(25000800)
    SetNetworkUpdateRate(25000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(25000800, name=905200000)


@RestartOnRest(25002819)
def Event_25002819():
    """Event 25002819"""
    if FlagEnabled(25000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(25000800, 20010850))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(25002820):
        EnableGravity(25000820)
        EnableAnimations(25000820)
        EnableAI(25000820)
        ForceSpawnerToSpawn(spawner=25004820)
        EnableFlag(25002820)
        WaitRealFrames(frames=1)
        Move(25000820, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002821):
        EnableGravity(25000821)
        EnableAnimations(25000821)
        EnableAI(25000821)
        ForceSpawnerToSpawn(spawner=25004821)
        EnableFlag(25002821)
        WaitRealFrames(frames=1)
        Move(25000821, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002822):
        EnableGravity(25000822)
        EnableAnimations(25000822)
        EnableAI(25000822)
        ForceSpawnerToSpawn(spawner=25004822)
        EnableFlag(25002822)
        WaitRealFrames(frames=1)
        Move(25000822, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002823):
        EnableGravity(25000823)
        EnableAnimations(25000823)
        EnableAI(25000823)
        ForceSpawnerToSpawn(spawner=25004823)
        EnableFlag(25002823)
        WaitRealFrames(frames=1)
        Move(25000823, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002824):
        EnableGravity(25000824)
        EnableAnimations(25000824)
        EnableAI(25000824)
        ForceSpawnerToSpawn(spawner=25004824)
        EnableFlag(25002824)
        WaitRealFrames(frames=1)
        Move(25000824, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002825):
        EnableGravity(25000825)
        EnableAnimations(25000825)
        EnableAI(25000825)
        ForceSpawnerToSpawn(spawner=25004825)
        EnableFlag(25002825)
        WaitRealFrames(frames=1)
        Move(25000825, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002826):
        EnableGravity(25000826)
        EnableAnimations(25000826)
        EnableAI(25000826)
        ForceSpawnerToSpawn(spawner=25004826)
        EnableFlag(25002826)
        WaitRealFrames(frames=1)
        Move(25000826, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002827):
        EnableGravity(25000827)
        EnableAnimations(25000827)
        EnableAI(25000827)
        ForceSpawnerToSpawn(spawner=25004827)
        EnableFlag(25002827)
        WaitRealFrames(frames=1)
        Move(25000827, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002828):
        EnableGravity(25000828)
        EnableAnimations(25000828)
        EnableAI(25000828)
        ForceSpawnerToSpawn(spawner=25004828)
        EnableFlag(25002828)
        WaitRealFrames(frames=1)
        Move(25000828, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002829):
        EnableGravity(25000829)
        EnableAnimations(25000829)
        EnableAI(25000829)
        ForceSpawnerToSpawn(spawner=25004829)
        EnableFlag(25002829)
        WaitRealFrames(frames=1)
        Move(25000829, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002830):
        EnableGravity(25000830)
        EnableAnimations(25000830)
        EnableAI(25000830)
        ForceSpawnerToSpawn(spawner=25004830)
        EnableFlag(25002830)
        WaitRealFrames(frames=1)
        Move(25000830, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002831):
        EnableGravity(25000831)
        EnableAnimations(25000831)
        EnableAI(25000831)
        ForceSpawnerToSpawn(spawner=25004831)
        EnableFlag(25002831)
        WaitRealFrames(frames=1)
        Move(25000831, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002832):
        EnableGravity(25000832)
        EnableAnimations(25000832)
        EnableAI(25000832)
        ForceSpawnerToSpawn(spawner=25004832)
        EnableFlag(25002832)
        WaitRealFrames(frames=1)
        Move(25000832, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002833):
        EnableGravity(25000833)
        EnableAnimations(25000833)
        EnableAI(25000833)
        ForceSpawnerToSpawn(spawner=25004833)
        EnableFlag(25002833)
        WaitRealFrames(frames=1)
        Move(25000833, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)
    if FlagDisabled(25002834):
        EnableGravity(25000834)
        EnableAnimations(25000834)
        EnableAI(25000834)
        ForceSpawnerToSpawn(spawner=25004834)
        EnableFlag(25002834)
        WaitRealFrames(frames=1)
        Move(25000834, destination=25000800, destination_type=CoordEntityType.Character, dummy_id=40, short_move=True)
        Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    ActivateMultiplayerBuffs(25005848)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(25002820)
def Event_25002820(_, character: Character | int, flag: Flag | int):
    """Event 25002820"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterDead(character))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableNetworkFlag(flag)
    Wait(0.10000000149011612)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()


@RestartOnRest(25002811)
def Event_25002811():
    """Event 25002811"""
    if FlagEnabled(25000800):
        return
    DeactivateGparamOverride(change_duration=6.0)
    
    MAIN.Await(CharacterHasSpecialEffect(25000800, 20010880))
    
    DisableAsset(25001610)
    DisableAsset(25005610)
    ActivateGparamOverride(gparam_sub_id=3, change_duration=3.0)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(25000800, 20010880))
    
    EnableAsset(25001610)
    EnableAsset(25005610)
    Restart()


@RestartOnRest(25002812)
def Event_25002812():
    """Event 25002812"""
    if FlagEnabled(25000800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(25000800, 20010890))
    
    EnableFlag(25002802)


@RestartOnRest(25002849)
def Event_25002849():
    """Event 25002849"""
    CommonFunc_9005800(
        0,
        flag=25000800,
        entity=0,
        region=0,
        flag_1=25002805,
        character=25005800,
        action_button_id=10000,
        left=25002801,
        region_1=25002800,
    )
    CommonFunc_9005822(
        0,
        flag=25000800,
        bgm_boss_conv_param_id=520000,
        flag_1=25002805,
        flag_2=25002806,
        right=25002803,
        flag_3=25002802,
        left=0,
        left_1=0,
    )
