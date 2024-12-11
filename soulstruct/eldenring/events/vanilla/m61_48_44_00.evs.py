"""
Land of Shadow 12-11 SW SW

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
    RegisterGrace(grace_flag=2048440001, asset=2048441951)
    CommonFunc_9005810(
        0,
        flag=2048440800,
        grace_flag=2048440000,
        character=2048440950,
        asset=2048441950,
        enemy_block_distance=0.0,
    )
    CommonFunc_90005300(0, flag=2048440392, character=2048440392, item_lot=40902, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=2048440393, character=2048440393, item_lot=40920, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=2048440398, character=2048440398, item_lot=40922, seconds=0.0, left=0)
    CommonFunc_90005200(
        0,
        character=2048440392,
        animation_id=30002,
        animation_id_1=20002,
        region=2048442392,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2048442800()
    Event_2048442810()
    Event_2048442849()
    Event_2048442840()
    Event_2048442811()
    CommonFunc_90005780(
        0,
        flag=2048440800,
        summon_flag=2048442160,
        dismissal_flag=2048442161,
        character=2048440720,
        sign_type=0,
        region=2048442721,
        right=2048459286,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=2048440800, flag_1=2048442160, flag_2=2048442161, character=2048440720)
    CommonFunc_90005784(
        0,
        flag=2048442160,
        flag_1=2048442805,
        character=2048440720,
        region=2048442800,
        region_1=2048442805,
        animation=0,
    )
    CommonFunc_90005250(0, character=2048440271, region=2048442271, seconds=0.0, animation_id=3008)
    Event_2048442200(0, character=2048440200)
    CommonFunc_90005250(0, character=2048440200, region=2048442292, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2048440260, region=2048442292, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2048440292, region=2048442292, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2048440203, region=2048442203, seconds=0.0, animation_id=3008)
    CommonFunc_90005251(0, character=2048440304, radius=25.0, seconds=0.0, animation_id=0)
    Event_2048442580()
    CommonFunc_90005501(
        0,
        flag=2048440510,
        flag_1=2048440511,
        left=0,
        asset=2048441510,
        asset_1=2048441511,
        asset_2=2048441512,
        flag_2=2048440512,
    )
    Event_2048442510()
    CommonFunc_900005610(0, asset=2048441200, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2048440180,
        summon_flag=2048442181,
        dismissal_flag=2048442182,
        character=2048440750,
        sign_type=22,
        region=2048442710,
        region_1=2048442711,
        seconds=0.0,
        right_1=2045429290,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2048440180, flag_1=2048442181, flag_2=2048442182, character=2048440750)
    CommonFunc_90005792(
        0,
        flag=2048440180,
        flag_1=2048442181,
        flag_2=2048442182,
        character=2048440750,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2048440180,
        flag_1=2048442181,
        flag_2=2048442182,
        character=2048440750,
        other_entity=2048442710,
        region=0,
        left=0,
    )
    CommonFunc_90005774(0, flag=2048440180, item_lot=116401, flag_1=400645)
    CommonFunc_90005757(
        0,
        character=2048440740,
        character_1=2048440741,
        flag=4385,
        flag_1=4950,
        flag_2=2045422710,
        flag_3=4383,
    )
    CommonFunc_90005759(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4960,
        character=2048440740,
        flag_3=4950,
        flag_4=2045429290,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429340,
        radius=30.0,
    )
    CommonFunc_90005778(0, flag=2048442720, flag_1=4950, flag_2=400750, attacked_entity=2048440740)
    CommonFunc_90005779(0, character=2048440740, flag=4950, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2048440740, flag=2048449300, flag_1=2048449300, animation_id=20015)
    CommonFunc_90005766(0, flag=2048442181, character=2048440750, distance=100.0, flag_1=2045429277, flag_2=4960)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2048440750,
        flag_1=4901,
        character_1=2048440751,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2048440751, flag=4960, flag_1=4383, flag_2=2048442181)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)
    Event_2048440715(0, flag=2048459286, flag_1=2048440800, flag_2=4927)


@ContinueOnRest(2048442580)
def Event_2048442580():
    """Event 2048442580"""
    RegisterLadder(start_climbing_flag=2048440580, stop_climbing_flag=2048440581, asset=2048441580)
    RegisterLadder(start_climbing_flag=2048440582, stop_climbing_flag=2048440583, asset=2048441582)


@ContinueOnRest(2048442510)
def Event_2048442510():
    """Event 2048442510"""
    CommonFunc_90005500(
        0,
        flag=2048440510,
        flag_1=2048440511,
        left=0,
        asset=2048441510,
        asset_1=2048441511,
        obj_act_id=2048443511,
        asset_2=2048441512,
        obj_act_id_1=2048443512,
        region=2048442511,
        region_1=2048442512,
        flag_2=2048440512,
        flag_3=2048440513,
        left_1=0,
    )


@RestartOnRest(2048442200)
def Event_2048442200(_, character: Character | int):
    """Event 2048442200"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=13690):
        AddSpecialEffect(character, 13690)


@ContinueOnRest(2048442800)
def Event_2048442800():
    """Event 2048442800"""
    if FlagEnabled(2048440800):
        return
    
    MAIN.Await(HealthValue(2048440800) <= 0)
    
    Wait(6.0)
    PlaySoundEffect(2048440800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(2048440800))
    
    KillBossAndDisplayBanner(character=2048440800, banner_type=BannerType.LegendFelled)
    EnableFlag(2048440800)
    EnableFlag(9190)
    if PlayerInOwnWorld():
        EnableFlag(61190)
    if PlayerInOwnWorld():
        EnableFlag(4925)
    OR_15.Add(CharacterInsideRegion(character=PLAYER, region=2048442400))
    OR_15.Add(CharacterOutsideRegion(character=PLAYER, region=2048442410))
    
    MAIN.Await(OR_15)
    
    SuppressSoundEvent(sound_id=6, unk_4_8=0, suppression_active=False)


@RestartOnRest(2048442810)
def Event_2048442810():
    """Event 2048442810"""
    GotoIfFlagDisabled(Label.L0, flag=2048440800)
    DisableCharacter(2048440800)
    DisableAnimations(2048440800)
    Kill(2048440800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2048440800)
    DisableHealthBar(2048440800)
    AND_2.Add(FlagEnabled(2048442805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2048442800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.5)
    EnableAI(2048440800)
    SetNetworkUpdateRate(2048440800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    EnableBossHealthBar(2048440800, name=905300000)


@RestartOnRest(2048442811)
def Event_2048442811():
    """Event 2048442811"""
    if FlagEnabled(2048440800):
        return
    AND_1.Add(CharacterHasSpecialEffect(2048440800, 20012001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(2048442802)


@RestartOnRest(2048442840)
def Event_2048442840():
    """Event 2048442840"""
    if FlagEnabled(2048440800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=2048440800, region=2048442840))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2048440800, 20012270)
    Wait(1.600000023841858)
    Restart()


@RestartOnRest(2048442849)
def Event_2048442849():
    """Event 2048442849"""
    CommonFunc_9005800(
        0,
        flag=2048440800,
        entity=2048441800,
        region=2048442800,
        flag_1=2048442805,
        character=2048445800,
        action_button_id=10000,
        left=0,
        region_1=2048442800,
    )
    CommonFunc_9005801(
        0,
        flag=2048440800,
        entity=2048441800,
        region=2048442800,
        flag_1=2048442805,
        flag_2=2048442806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=2048440800, asset=2048441800, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=2048440800, asset=2048441801, vfx_id=4, right=0)
    CommonFunc_9005822(
        0,
        flag=2048440800,
        bgm_boss_conv_param_id=530000,
        flag_1=2048442805,
        flag_2=2048442806,
        right=0,
        flag_3=2048442802,
        left=0,
        left_1=1,
    )


@RestartOnRest(2048440715)
def Event_2048440715(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2048440715"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag)
    OR_10.Add(FlagEnabled(flag_1))
    OR_10.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_10)
    
    DisableFlag(flag)


@RestartOnRest(2048440716)
def Event_2048440716(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 2048440716"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag)
    OR_10.Add(FlagEnabled(flag_1))
    OR_10.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_10)
    
    DisableFlag(flag)
