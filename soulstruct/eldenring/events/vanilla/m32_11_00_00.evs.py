"""
Yelough Anix Tunnel

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
from .entities.m32_11_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32110000, asset=Assets.AEG099_060_9000)
    Event_32112800()
    Event_32112810()
    Event_32112811()
    Event_32112849()
    Event_32112820(1, character=Characters.MalformedStar1, destination=Assets.AEG003_316_9001)
    Event_32112820(2, character=Characters.MalformedStar2, destination=Assets.AEG003_316_9002)
    Event_32112820(3, character=Characters.MalformedStar3, destination=Assets.AEG003_316_9003)
    Event_32112820(4, character=Characters.MalformedStar4, destination=Assets.AEG003_316_9004)
    Event_32112820(5, character=Characters.MalformedStar5, destination=Assets.AEG003_316_9005)
    Event_32112820(6, character=Characters.MalformedStar6, destination=Assets.AEG003_316_9006)
    Event_32112820(7, character=Characters.MalformedStar7, destination=Assets.AEG003_316_9007)
    Event_32112820(8, character=Characters.MalformedStar8, destination=Assets.AEG003_316_9008)
    Event_32112830(1, character=Characters.MalformedStar1)
    Event_32112830(2, character=Characters.MalformedStar2)
    Event_32112830(3, character=Characters.MalformedStar3)
    Event_32112830(4, character=Characters.MalformedStar4)
    Event_32112830(5, character=Characters.MalformedStar5)
    Event_32112830(6, character=Characters.MalformedStar6)
    Event_32112830(7, character=Characters.MalformedStar7)
    Event_32112830(8, character=Characters.MalformedStar8)
    Event_32112510()
    CommonFunc_90005501(
        0,
        flag=32110510,
        flag_1=32110511,
        left=0,
        asset=Assets.AEG024_846_0500,
        asset_1=Assets.AEG027_080_0501,
        asset_2=Assets.AEG027_080_0500,
        flag_2=32110512,
    )
    Event_32112580()
    CommonFunc_90005511(
        0,
        flag=32110560,
        asset=Assets.AEG027_043_0500,
        obj_act_id=32113560,
        obj_act_id_1=257013,
        left=0,
    )
    CommonFunc_90005512(0, flag=32110560, region=32112550, region_1=32112551)
    CommonFunc_90005646(
        0,
        flag=32110800,
        left_flag=32112840,
        cancel_flag__right_flag=32112841,
        asset=Assets.AEG099_065_9000,
        player_start=32112840,
        area_id=32,
        block_id=11,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32110519()
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30007,
        animation_id_1=20007,
        region=32112200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner1,
        animation_id=30007,
        animation_id_1=20007,
        region=32112200,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner2,
        animation_id=30007,
        animation_id_1=20007,
        region=32112205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner3,
        animation_id=30007,
        animation_id_1=20007,
        region=32112206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.TunnelMiner3, region=32112206, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner4,
        animation_id=30007,
        animation_id_1=20007,
        region=32112206,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=32110208,
        animation_id=30007,
        animation_id_1=20007,
        region=32112208,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=32110208, region=32112208, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner5,
        animation_id=30007,
        animation_id_1=20007,
        region=32112209,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner6,
        animation_id=30007,
        animation_id_1=20007,
        region=32112209,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.TunnelMiner6, region=32112209, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.TunnelMiner7,
        animation_id=30006,
        animation_id_1=20006,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner8,
        animation_id=30007,
        animation_id_1=20007,
        region=32112215,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.TunnelMiner8, region=32112215, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.TunnelMiner9,
        animation_id=30007,
        animation_id_1=20007,
        region=32112216,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.OnyxLord0, region=32112300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.OnyxLord1, region=32112301, seconds=0.0, animation_id=-1)


@ContinueOnRest(32112510)
def Event_32112510():
    """Event 32112510"""
    CommonFunc_90005500(
        0,
        flag=32110510,
        flag_1=32110511,
        left=0,
        asset=Assets.AEG024_846_0500,
        asset_1=Assets.AEG027_080_0501,
        obj_act_id=32113511,
        asset_2=Assets.AEG027_080_0500,
        obj_act_id_1=32113512,
        region=32112511,
        region_1=32112512,
        flag_2=32110512,
        flag_3=32110513,
        left_1=0,
    )


@ContinueOnRest(32110519)
def Event_32110519():
    """Event 32110519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32110510)
    EnableThisSlotFlag()


@ContinueOnRest(32112580)
def Event_32112580():
    """Event 32112580"""
    RegisterLadder(start_climbing_flag=32110580, stop_climbing_flag=32110581, asset=Assets.AEG027_046_0500)
    RegisterLadder(start_climbing_flag=32110582, stop_climbing_flag=32110583, asset=Assets.AEG027_009_0500)
    RegisterLadder(start_climbing_flag=32110584, stop_climbing_flag=32110585, asset=Assets.AEG027_008_0500)


@RestartOnRest(32112800)
def Event_32112800():
    """Event 32112800"""
    if FlagEnabled(32110800):
        return
    
    MAIN.Await(HealthValue(Characters.MalformedStar0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MalformedStar0))
    
    KillBossAndDisplayBanner(character=Characters.MalformedStar0, banner_type=BannerType.EnemyFelled)
    EnableFlag(32110800)
    EnableFlag(9268)
    if PlayerInOwnWorld():
        EnableFlag(61268)


@RestartOnRest(32112810)
def Event_32112810():
    """Event 32112810"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(Characters.MalformedStar0)
    DisableAnimations(Characters.MalformedStar0)
    Kill(Characters.MalformedStar0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MalformedStar0)
    SetCharacterEventTarget(Characters.MalformedStar0, region=32110810)
    SetBackreadStateAlternate(Characters.TalkDummy2, True)
    GotoIfFlagEnabled(Label.L1, flag=32110801)
    DisableCharacter(Characters.MalformedStar0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32112801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.MalformedStar0, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(32110801)
    EnableCharacter(Characters.MalformedStar0)
    ForceAnimation(Characters.MalformedStar0, 20016)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(32112805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32112800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MalformedStar0)
    SetNetworkUpdateRate(Characters.MalformedStar0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MalformedStar0, name=904620320)


@RestartOnRest(32112811)
def Event_32112811():
    """Event 32112811"""
    if FlagEnabled(32110800):
        return
    AND_1.Add(HealthRatio(Characters.MalformedStar0) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32112802)


@RestartOnRest(32112820)
def Event_32112820(_, character: uint, destination: uint):
    """Event 32112820"""
    MAIN.Await(CharacterHasSpecialEffect(character, 16714))
    
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=character,
    )
    Wait(1.0)
    RemoveSpecialEffect(character, 16714)
    Restart()


@RestartOnRest(32112830)
def Event_32112830(_, character: uint):
    """Event 32112830"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5038))
    AND_1.Add(CharacterDead(Characters.MalformedStar0))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(32112849)
def Event_32112849():
    """Event 32112849"""
    CommonFunc_9005800(
        0,
        flag=32110800,
        entity=Assets.AEG099_003_9000,
        region=32112800,
        flag_1=32112805,
        character=32115800,
        action_button_id=10000,
        left=32110801,
        region_1=32112801,
    )
    CommonFunc_9005801(
        0,
        flag=32110800,
        entity=Assets.AEG099_003_9000,
        region=32112800,
        flag_1=32112805,
        flag_2=32112806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32110800, asset=Assets.AEG099_003_9000, model_point=7, right=32110801)
    CommonFunc_9005822(
        0,
        flag=32110800,
        bgm_boss_conv_param_id=920700,
        flag_1=32112805,
        flag_2=32112806,
        right=0,
        flag_3=32112802,
        left=0,
        left_1=0,
    )
