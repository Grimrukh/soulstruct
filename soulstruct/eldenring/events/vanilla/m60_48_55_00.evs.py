"""
Southwest Mountaintops (NW) (NW)

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
from .enums.m60_48_55_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, flag=1048550200, character=1048550200, item_lot=40522, seconds=0.0, left=0)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005421(0, character=Characters.CaravanDummy, asset=Assets.AEG100_101_9000, flag=1248558301)
    CommonFunc_90005422(0, flag=1248558301, asset=Assets.AEG100_120_9000, obj_act_id=1248553301)
    CommonFunc_90005424(
        0,
        asset=Assets.AEG100_120_9000,
        character=Characters.SnowTroll0,
        character_1=Characters.SnowTroll1,
        character_2=Characters.CaravanDummy,
        asset_1=Assets.AEG100_101_9000,
    )
    CommonFunc_90005423(0, character=Characters.SnowTroll0)
    CommonFunc_90005423(0, character=Characters.SnowTroll1)
    CommonFunc_90005476(0, character=Characters.NightsCavalry0, character_1=Characters.NightsCavalryHorse0)
    CommonFunc_90005476(0, character=Characters.NightsCavalry1, character_1=Characters.NightsCavalryHorse1)
    Event_1248552820(0, character=Characters.NightsCavalry0, seconds=0.0)
    Event_1248552820(1, character=Characters.NightsCavalry1, seconds=0.0)
    Event_1248552830(0, character=Characters.NightsCavalry0, character_1=Characters.NightsCavalryHorse0)
    Event_1248552830(1, character=Characters.NightsCavalry1, character_1=Characters.NightsCavalryHorse1)
    Event_1248552840(
        0,
        character=Characters.NightsCavalry0,
        character_1=Characters.NightsCavalryHorse0,
        destination=1248552800,
    )
    Event_1248552840(
        1,
        character=Characters.NightsCavalry1,
        character_1=Characters.NightsCavalryHorse1,
        destination=1248552801,
    )
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry0,
        name=903150608,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse0,
    )
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry1,
        name=903150609,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse1,
    )
    RunCommonEvent(
        1248552800,
        slot=0,
        args=(1248550800, 0, 1248550800, 0, 1048550700, 1248550801, 1048550710),
        arg_types="IIIIiIi",
    )
    Event_1248552321(
        0,
        character=Characters.NightsCavalry0,
        character_1=Characters.NightsCavalry1,
        npc_threat_level=10,
        flag=1248552815,
    )
    Event_1248552320(0, character=Characters.NightsCavalry0, character_1=Characters.NightsCavalry1)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005420(
        0,
        character=Characters.CaravanDummy,
        caravan_asset__parent_asset=Assets.AEG100_120_9000,
        child_asset=Assets.AEG100_101_9000,
        character_1=Characters.Dummy,
        character_2=Characters.SnowTroll0,
        character_3=Characters.SnowTroll1,
        seconds=0.0,
    )


@RestartOnRest(1248552320)
def Event_1248552320(_, character: uint, character_1: uint):
    """Event 1248552320"""
    if FlagEnabled(1248550800):
        return
    OR_1.Add(CharacterDead(character))
    OR_1.Add(CharacterDead(character_1))
    OR_2.Add(OR_1)
    AND_1.Add(HealthRatio(character) <= 0.5)
    AND_1.Add(HealthRatio(character_1) <= 0.5)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(1248552815)


@ContinueOnRest(1248552321)
def Event_1248552321(_, character: uint, character_1: uint, npc_threat_level: uint, flag: uint):
    """Event 1248552321"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FieldBattleMusicEnabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(AND_1)
    
    EnableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(CharacterDead(character_1))
    OR_2.Add(AND_2)
    OR_2.Add(FieldBattleMusicDisabled(npc_threat_level=npc_threat_level))
    
    MAIN.Await(OR_2)
    
    DisableFieldBattleMusicHeatUp(npc_threat_level=npc_threat_level)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(1248552800)
def Event_1248552800(
    _,
    flag: uint,
    left: uint,
    character: uint,
    left_1: uint,
    item_lot: int,
    character_1: uint,
    item_lot_1: int,
):
    """Event 1248552800"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableAnimations(character)
    DisableAnimations(character_1)
    Kill(character)
    Kill(character_1)
    DisableCharacter(Characters.NightsCavalryHorse0)
    DisableAnimations(Characters.NightsCavalryHorse0)
    Kill(Characters.NightsCavalryHorse0)
    DisableCharacter(Characters.NightsCavalryHorse1)
    DisableAnimations(Characters.NightsCavalryHorse1)
    Kill(Characters.NightsCavalryHorse1)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot_1, host_only=True)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_15.Add(HealthValue(character) <= 0)
    AND_15.Add(HealthValue(character_1) <= 0)
    
    MAIN.Await(AND_15)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    AND_14.Add(CharacterDead(character))
    AND_14.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_14)
    
    SkipLinesIfUnsignedEqual(6, left=left_1, right=3)
    SkipLinesIfUnsignedEqual(4, left=left_1, right=2)
    SkipLinesIfUnsignedEqual(2, left=left_1, right=1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.EnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.GreatEnemyFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DemigodFelled)
    Goto(Label.L1)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.LegendFelled)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(5.0)
    AwardItemLot(item_lot_1, host_only=True)
    AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(1248552820)
def Event_1248552820(_, character: uint, seconds: float):
    """Event 1248552820"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(TimeOfDayInRange(earliest=(19, 59, 59), latest=(5, 59, 59)))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(TimeOfDayInRange(earliest=(5, 59, 59), latest=(19, 59, 59)))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()
    Wait(seconds)


@RestartOnRest(1248552830)
def Event_1248552830(_, character: uint, character_1: uint):
    """Event 1248552830"""
    AND_15.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    AND_14.Add(CharacterBackreadEnabled(character))
    AwaitConditionTrue(AND_14)
    AND_1.Add(CharacterHasSpecialEffect(character, 11830))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(CharacterHasSpecialEffect(character, 11830))
    
    MAIN.Await(AND_2)
    
    DisableAnimations(character)
    DisableAnimations(character_1)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAnimations(character)
    DisableAnimations(character_1)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    AND_2.Add(CharacterHasSpecialEffect(character, 11831))
    
    MAIN.Await(AND_2)
    
    EnableAnimations(character)
    EnableAnimations(character_1)
    DisableInvincibility(character)
    DisableInvincibility(character_1)
    Wait(1.0)
    Restart()


@RestartOnRest(1248552840)
def Event_1248552840(_, character: uint, character_1: uint, destination: uint):
    """Event 1248552840"""
    AND_15.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_15)
    End()
    AND_14.Add(CharacterBackreadEnabled(character))
    AwaitConditionTrue(AND_14)
    DisableAI(character)
    DisableAI(character_1)
    Wait(1.5)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    EnableAI(character)
    EnableAI(character_1)
