"""
Academy Crystal Cave

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
from .enums.m31_06_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31060000, asset=Assets.AEG099_060_9000)
    Event_31062800()
    Event_31062801()
    Event_31062802()
    Event_31062810()
    Event_31062849()
    Event_31062811()
    CommonFunc_90005525(0, flag=31060600, asset=31061600)
    CommonFunc_90005511(0, flag=31060540, asset=Assets.AEG027_043_1000, obj_act_id=31063540, obj_act_id_1=27043, left=0)
    CommonFunc_90005512(0, flag=31060540, region=31062540, region_1=31062541)
    CommonFunc_90005646(
        0,
        flag=31060800,
        left_flag=31062840,
        cancel_flag__right_flag=31062841,
        asset=Assets.AEG099_065_9000,
        player_start=31062840,
        area_id=31,
        block_id=6,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, flag=31062800, asset=Assets.AEG099_001_9002, dummy_id=5)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar0,
        region=31062200,
        radius=2.0,
        seconds=1.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar1,
        region=31062200,
        radius=2.0,
        seconds=1.2000000476837158,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar2,
        region=31062200,
        radius=2.0,
        seconds=1.399999976158142,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar3,
        region=31062203,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar4,
        region=31062203,
        radius=2.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar5,
        region=31062205,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar6,
        region=31062211,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=31060212, region=31062211, radius=2.0, seconds=0.20000000298023224, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.RayaLucariaScholar7,
        region=31062215,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Rat0, region=31062280, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=31062281, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat2, region=31062281, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=31060283, region=31062283, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.BattleMage, region=31062300, radius=2.0, seconds=0.0, animation_id=0)


@RestartOnRest(31062300)
def Event_31062300():
    """Event 31062300"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.BattleMage, region=31062301))
    
    Wait(2.0)
    ChangePatrolBehavior(Characters.BattleMage, patrol_information_id=31063301)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31062800)
def Event_31062800():
    """Event 31062800"""
    if FlagEnabled(31060800):
        return
    AND_1.Add(CharacterDead(Characters.Crystalian0))
    AND_1.Add(CharacterDead(Characters.Crystalian1))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    KillBossAndDisplayBanner(character=Characters.Crystalian0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31060800)
    if PlayerInOwnWorld():
        EnableFlag(61238)
    EnableFlag(9238)


@RestartOnRest(31062801)
def Event_31062801():
    """Event 31062801"""
    if FlagEnabled(31060800):
        return
    
    MAIN.Await(HealthValue(Characters.Crystalian0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Crystalian0, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31062802)
def Event_31062802():
    """Event 31062802"""
    if FlagEnabled(31060800):
        return
    
    MAIN.Await(HealthValue(Characters.Crystalian1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Crystalian1, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31062810)
def Event_31062810():
    """Event 31062810"""
    GotoIfFlagDisabled(Label.L0, flag=31060800)
    DisableCharacter(Characters.Crystalian0)
    DisableCharacter(Characters.Crystalian1)
    DisableAnimations(Characters.Crystalian0)
    DisableAnimations(Characters.Crystalian1)
    Kill(Characters.Crystalian0)
    Kill(Characters.Crystalian1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Crystalian0)
    DisableAI(Characters.Crystalian1)
    ForceAnimation(Characters.Crystalian0, 30000)
    ForceAnimation(Characters.Crystalian1, 30000)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31062800))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Crystalian0, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Crystalian1, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(31060801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(31062805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31062800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Crystalian0)
    EnableAI(Characters.Crystalian1)
    SetNetworkUpdateRate(Characters.Crystalian0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.Crystalian1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Crystalian0, name=903350310)
    EnableBossHealthBar(Characters.Crystalian1, name=903350311, bar_slot=1)
    ForceAnimation(Characters.Crystalian0, 20000)
    ForceAnimation(Characters.Crystalian1, 20000)


@RestartOnRest(31062811)
def Event_31062811():
    """Event 31062811"""
    if FlagEnabled(31060800):
        return
    OR_15.Add(CharacterDead(Characters.Crystalian0))
    OR_15.Add(CharacterDead(Characters.Crystalian1))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31062842)


@RestartOnRest(31062849)
def Event_31062849():
    """Event 31062849"""
    CommonFunc_9005800(
        0,
        flag=31060800,
        entity=Assets.AEG099_001_9000,
        region=31062800,
        flag_1=31062805,
        character=31065800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31060800,
        entity=Assets.AEG099_001_9000,
        region=31062800,
        flag_1=31062805,
        flag_2=31062806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31060800, asset=Assets.AEG099_001_9000, dummy_id=3, right=0)
    CommonFunc_9005813(0, flag=31060800, asset=Assets.AEG099_001_9001, dummy_id=3, right=0, dummy_id_1=806760)
    CommonFunc_9005822(
        0,
        flag=31060800,
        bgm_boss_conv_param_id=931000,
        flag_1=31062805,
        flag_2=31062806,
        right=0,
        flag_3=31062842,
        left=0,
        left_1=0,
    )
