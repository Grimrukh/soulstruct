"""
Auriza Side Tomb

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m30_13_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73013, asset=Assets.AEG099_060_9000)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallLivingPot0, region=30132250, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=30130251,
        animation_id=30000,
        animation_id_1=20000,
        region=30132251,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=30130253,
        animation_id=30000,
        animation_id_1=20000,
        region=30132251,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=Characters.SmallLivingPot1,
        animation_id=30000,
        animation_id_1=20000,
        region=30132251,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        4,
        character=Characters.SmallLivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        region=30132251,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        region=30132256,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.SmallLivingPot4,
        animation_id=30000,
        animation_id_1=20000,
        region=30132256,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallLivingPot5, region=30132270, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(1, character=Characters.SmallLivingPot6, region=30132270, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        1,
        character=Characters.SmallLivingPot7,
        animation_id=30000,
        animation_id_1=20000,
        region=30132405,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.SmallLivingPot8,
        animation_id=30000,
        animation_id_1=20000,
        region=30132405,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallLivingPot9, region=30132297, seconds=3.0, animation_id=0)
    CommonFunc_90005221(
        0,
        character=Characters.SmallLivingPot10,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        1,
        character=Characters.SmallLivingPot11,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot0,
        animation_id=30000,
        animation_id_1=20000,
        region=30132400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.LivingPot1,
        animation_id=30000,
        animation_id_1=20000,
        region=30132400,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.LivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        region=30132408,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp0, region=30132300, seconds=0.0, animation_id=3006)
    CommonFunc_90005200(
        0,
        character=Characters.Imp1,
        animation_id=30000,
        animation_id_1=20000,
        region=30132301,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Imp2,
        animation_id=30000,
        animation_id_1=20000,
        region=30132302,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp3, region=30132307, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp4, region=30132308, seconds=0.0, animation_id=3004)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp5, region=30132309, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Imp7, region=30132315, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp6, region=30132312, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Imp8,
        animation_id=30010,
        animation_id_1=20010,
        region=30132316,
        seconds=5.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Imp9,
        animation_id=30003,
        animation_id_1=20003,
        region=30132317,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Imp10, region=30132318, seconds=0.0, animation_id=3006)
    CommonFunc_90005251(0, character=Characters.Imp11, radius=4.0, seconds=0.0, animation_id=0)
    CommonFunc_90005650(
        0,
        flag=30130540,
        asset=Assets.AEG027_041_0501,
        asset_1=Assets.AEG027_115_0501,
        obj_act_id=30133541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30130540, anchor_entity=Assets.AEG027_041_0501)
    CommonFunc_90005501(
        0,
        flag=30130510,
        flag_1=30131510,
        left=0,
        asset=30131510,
        asset_1=30131511,
        asset_2=30131512,
        flag_2=30130511,
    )
    Event_30132510()
    CommonFunc_90005525(0, flag=30130570, asset=30131570)
    Event_30132580()
    Event_30132800()
    Event_30132810()
    Event_30132849()
    Event_30132811()
    CommonFunc_90005200(
        0,
        character=Characters.SmallLivingPot12,
        animation_id=30000,
        animation_id_1=20000,
        region=30132800,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.SmallLivingPot13,
        animation_id=30000,
        animation_id_1=20000,
        region=30132800,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=Characters.SmallLivingPot14,
        animation_id=30000,
        animation_id_1=20000,
        region=30132800,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        3,
        character=Characters.SmallLivingPot15,
        animation_id=30000,
        animation_id_1=20000,
        region=30132800,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005646(
        0,
        flag=30130800,
        left_flag=30132840,
        cancel_flag__right_flag=30132841,
        asset=Assets.AEG099_065_9000,
        player_start=30132840,
        area_id=30,
        block_id=13,
        cc_id=0,
        dd_id=0,
    )
    Event_30130790(0, asset=30131520, flag=30130800)
    Event_30132200(
        0,
        asset=Assets.AEG099_290_9001,
        asset_1=Assets.AEG099_290_9002,
        region=30132350,
        destination=30132211,
        flag=30131200,
        obj_act_id=30133200,
    )
    Event_30132205(0, flag=30131200, region=30132350)
    Event_30132200(
        1,
        asset=Assets.AEG099_290_9002,
        asset_1=Assets.AEG099_290_9001,
        region=30132351,
        destination=30132210,
        flag=30131201,
        obj_act_id=30133201,
    )
    Event_30132205(1, flag=30131201, region=30132351)
    Event_30132200(
        2,
        asset=Assets.AEG099_290_9003,
        asset_1=Assets.AEG099_290_9004,
        region=30132352,
        destination=30132213,
        flag=30131202,
        obj_act_id=30133202,
    )
    Event_30132205(2, flag=30131202, region=30132352)
    Event_30132200(
        3,
        asset=Assets.AEG099_290_9004,
        asset_1=Assets.AEG099_290_9003,
        region=30132353,
        destination=30132212,
        flag=30131203,
        obj_act_id=30133203,
    )
    Event_30132205(3, flag=30131203, region=30132353)
    Event_30132200(
        4,
        asset=Assets.AEG099_290_9005,
        asset_1=Assets.AEG099_290_9006,
        region=30132354,
        destination=30132215,
        flag=30131204,
        obj_act_id=30133204,
    )
    Event_30132205(4, flag=30131204, region=30132354)
    Event_30132200(
        5,
        asset=Assets.AEG099_290_9006,
        asset_1=Assets.AEG099_290_9005,
        region=30132355,
        destination=30132214,
        flag=30131205,
        obj_act_id=30133205,
    )
    Event_30132205(5, flag=30131205, region=30132355)
    Event_30132200(
        6,
        asset=Assets.AEG099_290_9007,
        asset_1=Assets.AEG099_290_9008,
        region=30132356,
        destination=30132217,
        flag=30131206,
        obj_act_id=30133206,
    )
    Event_30132205(6, flag=30131206, region=30132356)
    Event_30132200(
        7,
        asset=Assets.AEG099_290_9008,
        asset_1=Assets.AEG099_290_9007,
        region=30132357,
        destination=30132216,
        flag=30131207,
        obj_act_id=30133207,
    )
    Event_30132205(7, flag=30131207, region=30132357)
    Event_30132200(
        8,
        asset=Assets.AEG099_290_9009,
        asset_1=Assets.AEG099_290_9010,
        region=30132358,
        destination=30132219,
        flag=30131208,
        obj_act_id=30133208,
    )
    Event_30132205(8, flag=30131208, region=30132358)
    Event_30132200(
        9,
        asset=Assets.AEG099_290_9010,
        asset_1=Assets.AEG099_290_9009,
        region=30132359,
        destination=30132218,
        flag=30131209,
        obj_act_id=30133209,
    )
    Event_30132205(9, flag=30131209, region=30132359)
    Event_30132200(
        10,
        asset=Assets.AEG099_290_9011,
        asset_1=Assets.AEG099_290_9012,
        region=30132280,
        destination=30132231,
        flag=30131220,
        obj_act_id=30133220,
    )
    Event_30132205(10, flag=30131220, region=30132280)
    Event_30132200(
        11,
        asset=Assets.AEG099_290_9012,
        asset_1=Assets.AEG099_290_9011,
        region=30132281,
        destination=30132230,
        flag=30131221,
        obj_act_id=30133221,
    )
    Event_30132205(11, flag=30131221, region=30132281)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30130519()


@ContinueOnRest(30132510)
def Event_30132510():
    """Event 30132510"""
    CommonFunc_90005500(
        0,
        flag=30130510,
        flag_1=30131510,
        left=0,
        asset=30131510,
        asset_1=30131511,
        obj_act_id=30133511,
        asset_2=30131512,
        obj_act_id_1=30133512,
        region=30132511,
        region_1=30132512,
        flag_2=30130511,
        flag_3=30132512,
        left_1=0,
    )


@ContinueOnRest(30132580)
def Event_30132580():
    """Event 30132580"""
    RegisterLadder(start_climbing_flag=30130580, stop_climbing_flag=30130581, asset=Assets.AEG027_034_0500)
    RegisterLadder(start_climbing_flag=30130582, stop_climbing_flag=30130583, asset=Assets.AEG027_200_0500)


@RestartOnRest(30132200)
def Event_30132200(_, asset: uint, asset_1: uint, region: uint, destination: uint, flag: uint, obj_act_id: uint):
    """Event 30132200"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    
    MAIN.Await(AssetActivated(obj_act_id=obj_act_id))
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    DisableNetworkSync()
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    AND_1.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L20, character=PLAYER, special_effect=4170)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=True, freeze_player_delay=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    AND_2.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L18, input_condition=AND_2)
    DisableCharacter(PLAYER)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=destination,
        dummy_id=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(1.0)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    Goto(Label.L19)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(3.4000000953674316)

    # --- Label 18 --- #
    DefineLabel(18)
    Wait(1.0)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(asset, 2, wait_for_completion=True)
    DisableNetworkFlag(flag)
    EnableNetworkSync()
    EnableAssetActivation(asset, obj_act_id=-1)
    EnableAssetActivation(asset_1, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableNetworkFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    EnableAssetActivation(asset_1, obj_act_id=-1)
    EnableNetworkSync()
    Restart()


@RestartOnRest(30132205)
def Event_30132205(_, flag: uint, region: uint):
    """Event 30132205"""
    GotoIfCharacterHasSpecialEffect(Label.L0, character=PLAYER, special_effect=4170)
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4170)
    Wait(2.299999952316284)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, 4171)
    RemoveSpecialEffect(PLAYER, 4170)
    Restart()


@ContinueOnRest(30130519)
def Event_30130519():
    """Event 30130519"""
    if FlagEnabled(30130519):
        return
    EnableFlag(30130510)


@RestartOnRest(30130790)
def Event_30130790(_, asset: uint, flag: uint):
    """Event 30130790"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ThisEventSlotFlagDisabled())
    
    MAIN.Await(AND_1)
    
    EnableThisSlotFlag()
    EnableAssetActivation(asset, obj_act_id=-1)
    End()


@RestartOnRest(30132800)
def Event_30132800():
    """Event 30132800"""
    if FlagEnabled(30130800):
        return
    
    MAIN.Await(HealthValue(Characters.GraveWardenDuelist) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GraveWardenDuelist, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GraveWardenDuelist))
    
    KillBossAndDisplayBanner(character=Characters.GraveWardenDuelist, banner_type=BannerType.EnemyFelled)
    Kill(Characters.SmallLivingPot12, award_runes=True)
    Kill(Characters.SmallLivingPot13, award_runes=True)
    Kill(Characters.SmallLivingPot14, award_runes=True)
    Kill(Characters.SmallLivingPot15, award_runes=True)
    EnableFlag(30130800)
    EnableFlag(9213)
    if PlayerInOwnWorld():
        EnableFlag(61213)


@RestartOnRest(30132802)
def Event_30132802():
    """Event 30132802"""
    if FlagEnabled(30130810):
        return
    
    MAIN.Await(HealthValue(30130810) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(30130810, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(30130810))
    
    KillBossAndDisplayBanner(character=30130810, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(30130810)


@RestartOnRest(30132810)
def Event_30132810():
    """Event 30132810"""
    GotoIfFlagDisabled(Label.L0, flag=30130800)
    DisableCharacter(Characters.GraveWardenDuelist)
    DisableAnimations(Characters.GraveWardenDuelist)
    Kill(Characters.GraveWardenDuelist)
    DisableCharacter(Characters.SmallLivingPot12)
    DisableAnimations(Characters.SmallLivingPot12)
    Kill(Characters.SmallLivingPot12)
    DisableCharacter(Characters.SmallLivingPot13)
    DisableAnimations(Characters.SmallLivingPot13)
    Kill(Characters.SmallLivingPot13)
    DisableCharacter(Characters.SmallLivingPot14)
    DisableAnimations(Characters.SmallLivingPot14)
    Kill(Characters.SmallLivingPot14)
    DisableCharacter(Characters.SmallLivingPot15)
    DisableAnimations(Characters.SmallLivingPot15)
    Kill(Characters.SmallLivingPot15)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GraveWardenDuelist)
    AND_2.Add(FlagEnabled(30132805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30132800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GraveWardenDuelist)
    SetNetworkUpdateRate(Characters.GraveWardenDuelist, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GraveWardenDuelist, name=903400301)


@RestartOnRest(30132811)
def Event_30132811():
    """Event 30132811"""
    if FlagEnabled(30130800):
        return
    AND_1.Add(HealthRatio(Characters.GraveWardenDuelist) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30132802)


@RestartOnRest(30132812)
def Event_30132812():
    """Event 30132812"""
    GotoIfFlagDisabled(Label.L0, flag=30130810)
    DisableCharacter(30130810)
    DisableAnimations(30130810)
    Kill(30130810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30130810)
    AND_2.Add(FlagEnabled(30132815))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30132810))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30130810)
    SetNetworkUpdateRate(Characters.GraveWardenDuelist, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30130810)


@RestartOnRest(30132849)
def Event_30132849():
    """Event 30132849"""
    CommonFunc_9005800(
        0,
        flag=30130800,
        entity=Assets.AEG099_001_9000,
        region=30132800,
        flag_1=30132805,
        character=30135800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30130800,
        entity=Assets.AEG099_001_9000,
        region=30132800,
        flag_1=30132805,
        flag_2=30132806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30130800, asset=Assets.AEG099_001_9000, dummy_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30130800,
        bgm_boss_conv_param_id=900000,
        flag_1=30132805,
        flag_2=30132806,
        right=0,
        flag_3=30132802,
        left=0,
        left_1=0,
    )


@RestartOnRest(30132850)
def Event_30132850():
    """Event 30132850"""
    CommonFunc_9005800(
        0,
        flag=30130810,
        entity=30131810,
        region=30132810,
        flag_1=30132815,
        character=30135810,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30130810,
        entity=30131810,
        region=30132810,
        flag_1=30132815,
        flag_2=30132816,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30130810, asset=30131810, dummy_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30130810,
        bgm_boss_conv_param_id=930000,
        flag_1=30132815,
        flag_2=30132816,
        right=0,
        flag_3=11002852,
        left=0,
        left_1=0,
    )
