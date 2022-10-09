"""
Lakeside Crystal Cave

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
from .entities.m31_05_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31050000, asset=Assets.AEG099_060_9000)
    Event_31052800()
    Event_31052810()
    Event_31052849()
    Event_31052811()
    Event_31052830(0, flag=31050801, character=Characters.TalkDummy1)
    CommonFunc_90005646(
        0,
        flag=31050800,
        left_flag=31052840,
        cancel_flag__right_flag=31052841,
        asset=31051840,
        player_start=31052840,
        area_id=31,
        block_id=5,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.DemiHuman0, region=31052200, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.DemiHuman1, radius=2.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, character=Characters.DemiHuman2, region=31052203, radius=2.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman3,
        animation_id=30002,
        animation_id_1=20002,
        region=31052205,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman4,
        animation_id=30001,
        animation_id_1=20001,
        region=31052205,
        radius=2.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman5,
        animation_id=30002,
        animation_id_1=20002,
        region=31052209,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LargeDemiHuman,
        region=31052230,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanShaman0,
        region=31052251,
        radius=5.0,
        seconds=0.0,
        animation_id=3005,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanShaman1,
        region=31052254,
        radius=2.0,
        seconds=0.0,
        animation_id=3005,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanShaman2,
        region=31052257,
        radius=2.0,
        seconds=0.0,
        animation_id=3003,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanBeastman,
        region=31052280,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Snail0,
        region=31052300,
        radius=2.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Snail1, region=31052301, radius=2.0, seconds=0.0, animation_id=0)
    Event_31052301()
    CommonFunc_90005261(
        0,
        character=Characters.Snail2,
        region=31052300,
        radius=2.0,
        seconds=0.10000000149011612,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail3,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail4,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail5,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail6,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail7,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.8999999761581421,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail8,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Snail9,
        animation_id=30000,
        animation_id_1=20000,
        region=31052305,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Snail10, region=31052315, radius=2.0, seconds=0.0, animation_id=3012)
    CommonFunc_90005261(0, character=Characters.Snail11, region=31052316, radius=2.0, seconds=0.0, animation_id=3012)
    CommonFunc_90005261(0, character=Characters.Snail12, region=31052317, radius=2.0, seconds=0.0, animation_id=3012)


@RestartOnRest(31052301)
def Event_31052301():
    """Event 31052301"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(Characters.Snail1, 8081)
    AddSpecialEffect(Characters.Snail1, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=Characters.Snail1, other_entity=PLAYER, radius=4.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(Characters.Snail1, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Snail1))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(Characters.Snail1, 8081)
    RemoveSpecialEffect(Characters.Snail1, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31052800)
def Event_31052800():
    """Event 31052800"""
    if FlagEnabled(31050800):
        return
    
    MAIN.Await(HealthValue(Characters.BloodhoundKnight) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.BloodhoundKnight, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.BloodhoundKnight))
    
    KillBossAndDisplayBanner(character=Characters.BloodhoundKnight, banner_type=BannerType.EnemyFelled)
    EnableFlag(31050800)
    EnableFlag(9237)
    if PlayerInOwnWorld():
        EnableFlag(61237)


@RestartOnRest(31052810)
def Event_31052810():
    """Event 31052810"""
    GotoIfFlagDisabled(Label.L0, flag=31050800)
    DisableCharacter(Characters.BloodhoundKnight)
    DisableAnimations(Characters.BloodhoundKnight)
    Kill(Characters.BloodhoundKnight)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.BloodhoundKnight)
    GotoIfFlagEnabled(Label.L1, flag=31050801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31052801))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(31050801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(31052805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31052800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.BloodhoundKnight)
    Wait(1.0)
    EnableAI(Characters.BloodhoundKnight)
    SetNetworkUpdateRate(Characters.BloodhoundKnight, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(Characters.BloodhoundKnight, 3013)
    EnableBossHealthBar(Characters.BloodhoundKnight, name=904290310)


@RestartOnRest(31052811)
def Event_31052811():
    """Event 31052811"""
    if FlagEnabled(31050800):
        return
    AND_1.Add(HealthRatio(Characters.BloodhoundKnight) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31052802)


@RestartOnRest(31052830)
def Event_31052830(_, flag: uint, character: uint):
    """Event 31052830"""
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31052849)
def Event_31052849():
    """Event 31052849"""
    CommonFunc_9005800(
        0,
        flag=31050800,
        entity=Assets.AEG099_002_9000,
        region=31052800,
        flag_1=31052805,
        character=31055800,
        action_button_id=10000,
        left=31050801,
        region_1=31052801,
    )
    CommonFunc_9005801(
        0,
        flag=31050800,
        entity=Assets.AEG099_002_9000,
        region=31052800,
        flag_1=31052805,
        flag_2=31052806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31050800, asset=Assets.AEG099_002_9000, model_point=5, right=31050801)
    CommonFunc_9005811(0, flag=31050800, asset=Assets.AEG099_001_9000, model_point=3, right=31050801)
    CommonFunc_9005822(
        0,
        flag=31050800,
        bgm_boss_conv_param_id=931000,
        flag_1=31052805,
        flag_2=31052806,
        right=0,
        flag_3=31052802,
        left=0,
        left_1=0,
    )
