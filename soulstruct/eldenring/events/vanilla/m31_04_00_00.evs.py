"""
Stillwater Cave

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
from .entities.m31_04_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31040000, asset=Assets.AEG099_060_9000)
    Event_31042800()
    Event_31042810()
    Event_31042849()
    Event_31042811()
    CommonFunc_90005646(
        0,
        flag=31040800,
        left_flag=31042840,
        cancel_flag__right_flag=31042841,
        asset=Assets.AEG099_065_9000,
        player_start=31042840,
        area_id=31,
        block_id=4,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer0,
        region=31042200,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer1,
        region=31042205,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer2,
        region=31042205,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer3,
        region=31042207,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer4,
        region=31042207,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer5,
        region=31042207,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer6,
        region=31042211,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer7,
        region=31042212,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer8,
        region=31042216,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer9,
        region=31042216,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005251(0, character=Characters.FungalSorcerer10, radius=1.5, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.FungalSorcerer11, radius=1.5, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.FungalSorcerer12, radius=1.5, seconds=0.0, animation_id=1701)
    CommonFunc_90005251(0, character=Characters.FungalSorcerer13, radius=1.5, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer14,
        region=31042223,
        radius=1.5,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005251(0, character=Characters.FungalSorcerer10, radius=1.5, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaFlower0,
        region=31042250,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantMirandaFlower1,
        animation_id=30001,
        animation_id_1=20001,
        region=31042207,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantMirandaFlower2,
        animation_id=30001,
        animation_id_1=20001,
        region=31042207,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantMirandaFlower3,
        animation_id=30001,
        animation_id_1=20001,
        region=31042257,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower0,
        region=31042260,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower1,
        region=31042260,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower2,
        region=31042260,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower3,
        region=31042260,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower4,
        region=31042260,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower5,
        animation_id=30001,
        animation_id_1=20001,
        region=31042275,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower6,
        animation_id=30001,
        animation_id_1=20001,
        region=31042275,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower7,
        animation_id=30001,
        animation_id_1=20001,
        region=31042275,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower8,
        animation_id=30001,
        animation_id_1=20001,
        region=31042275,
        radius=2.0,
        seconds=0.8999999761581421,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower9,
        animation_id=30001,
        animation_id_1=20001,
        region=31042275,
        radius=2.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.OldWomanBat,
        animation_id=30000,
        animation_id_1=20000,
        region=31042300,
        radius=2.0,
        seconds=10.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=31040310, region=31042310, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Bat0,
        animation_id=30000,
        animation_id_1=20000,
        region=31042311,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=31040312, region=31042312, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Bat1,
        animation_id=30000,
        animation_id_1=20000,
        region=31042318,
        radius=2.0,
        seconds=0.0,
        left=2,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat2,
        animation_id=30000,
        animation_id_1=20000,
        region=31042318,
        radius=2.0,
        seconds=0.30000001192092896,
        left=2,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat3,
        animation_id=30000,
        animation_id_1=20000,
        region=31042318,
        radius=2.0,
        seconds=0.5,
        left=2,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat4,
        animation_id=30000,
        animation_id_1=20000,
        region=31042323,
        radius=2.0,
        seconds=5.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat5,
        animation_id=30000,
        animation_id_1=20000,
        region=31042323,
        radius=2.0,
        seconds=5.199999809265137,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31042310(0, character=Characters.OldWomanBat)
    Event_31042310(1, character=31040310)
    Event_31042310(2, character=Characters.Bat0)
    Event_31042310(3, character=31040312)
    Event_31042310(4, character=Characters.Bat1)
    Event_31042310(5, character=Characters.Bat2)
    Event_31042310(6, character=Characters.Bat3)
    Event_31042310(7, character=Characters.Bat4)
    Event_31042310(8, character=Characters.Bat5)


@RestartOnRest(31042310)
def Event_31042310(_, character: uint):
    """Event 31042310"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31042800)
def Event_31042800():
    """Event 31042800"""
    if FlagEnabled(31040800):
        return
    
    MAIN.Await(HealthValue(Characters.CleanrotKnight) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CleanrotKnight, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.CleanrotKnight))
    
    KillBossAndDisplayBanner(character=Characters.CleanrotKnight, banner_type=BannerType.EnemyFelled)
    EnableFlag(31040800)
    EnableFlag(9236)
    if PlayerInOwnWorld():
        EnableFlag(61236)


@RestartOnRest(31042810)
def Event_31042810():
    """Event 31042810"""
    GotoIfFlagDisabled(Label.L0, flag=31040800)
    DisableCharacter(Characters.CleanrotKnight)
    DisableAnimations(Characters.CleanrotKnight)
    Kill(Characters.CleanrotKnight)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.CleanrotKnight)
    AddSpecialEffect(Characters.CleanrotKnight, 90000)
    ForceAnimation(Characters.CleanrotKnight, 30001)
    AND_2.Add(FlagEnabled(31042805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31042800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    ForceAnimation(Characters.CleanrotKnight, 20001)
    EnableAI(Characters.CleanrotKnight)
    SetNetworkUpdateRate(Characters.CleanrotKnight, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CleanrotKnight, name=903800310)


@RestartOnRest(31042811)
def Event_31042811():
    """Event 31042811"""
    if FlagEnabled(31040800):
        return
    AND_1.Add(HealthRatio(Characters.CleanrotKnight) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31042802)


@RestartOnRest(31042849)
def Event_31042849():
    """Event 31042849"""
    CommonFunc_9005800(
        0,
        flag=31040800,
        entity=Assets.AEG099_002_9000,
        region=31042800,
        flag_1=31042805,
        character=31045800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31040800,
        entity=Assets.AEG099_002_9000,
        region=31042800,
        flag_1=31042805,
        flag_2=31042806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31040800, asset=Assets.AEG099_002_9000, model_point=5, right=0)
    CommonFunc_9005822(
        0,
        flag=31040800,
        bgm_boss_conv_param_id=931000,
        flag_1=31042805,
        flag_2=31042806,
        right=0,
        flag_3=31042802,
        left=0,
        left_1=0,
    )
