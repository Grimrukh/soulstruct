"""
Forbidden Lands (NW) (NW)

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
from .entities.m60_48_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005211(
        0,
        character=Characters.Scarab2,
        animation_id=30001,
        animation_id_1=20001,
        region=0,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005476(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    Event_1048512820(0, character=Characters.NightsCavalry, character_1=Characters.NightsCavalryHorse)
    CommonFunc_90005871(
        0,
        character=Characters.NightsCavalry,
        name=903150607,
        npc_threat_level=10,
        character_1=Characters.NightsCavalryHorse,
    )
    RunCommonEvent(1048512800, slot=0, args=(1048510800, 0, 1048510800, 0, 1048510700, 0.0), arg_types="IIIIif")
    CommonFunc_90005872(0, character=Characters.NightsCavalry, npc_threat_level=10, right=0)


@RestartOnRest(1048512800)
def Event_1048512800(_, flag: uint, left: uint, character: uint, left_1: uint, item_lot: int, seconds: float):
    """Event 1048512800"""
    if ValueNotEqual(left=item_lot, right=0):
        Unknown_2004_76(flag=flag, item_lot=item_lot)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(Characters.NightsCavalryHorse)
    DisableAnimations(Characters.NightsCavalryHorse)
    Kill(Characters.NightsCavalryHorse)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=item_lot, right=0):
        return
    Wait(1.0)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(character) <= 0)
    
    Wait(2.0)
    PlaySoundEffect(character, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(character))
    
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
    AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds)


@RestartOnRest(1048512820)
def Event_1048512820(_, character: uint, character_1: uint):
    """Event 1048512820"""
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    AND_2.Add(CharacterHasSpecialEffect(character, 11825))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_3)
    
    AddSpecialEffect(character, 11825)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_4.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_4)
    
    AddSpecialEffect(character, 11826)
    Wait(1.0)
    Restart()
