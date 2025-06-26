"""
Land of Shadow 13-10 NW NW

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
        flag=2052430800,
        grace_flag=PLAYER,
        character=2052430950,
        asset=2052431950,
        enemy_block_distance=5.0,
    )
    Event_2052432800()
    Event_2052432810()
    Event_2052432816()
    Event_2052432849()
    Event_2052432820(0, character=2052430810)
    Event_2052432820(1, character=2052430811)
    Event_2052432820(2, character=2052430812)
    Event_2052432820(3, character=2052430813)
    Event_2052432820(4, character=2052430814)
    Event_2052432820(5, character=2052430815)
    Event_2052432820(6, character=2052430820)
    Event_2052432820(7, character=2052430821)
    Event_2052432820(8, character=2052430822)
    CommonFunc_90005640(0, flag=2052430540, asset=2052431540)
    CommonFunc_900005610(0, asset=2052431601, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(2052432800)
def Event_2052432800():
    """Event 2052432800"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2052430800):
        return
    OR_1.Add(HealthValue(2052430800) <= 0)
    OR_1.Add(FlagEnabled(2052432848))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(2052432848)
    Wait(4.0)
    PlaySoundEffect(2052430800, 888880000, sound_type=SoundType.s_SFX)
    OR_2.Add(CharacterDead(2052430800))
    OR_2.Add(FlagEnabled(2052432848))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=2052430800, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(2052430800)
    if PlayerInOwnWorld():
        EnableFlag(61161)
    EnableFlag(9161)


@RestartOnRest(2052432810)
def Event_2052432810():
    """Event 2052432810"""
    GotoIfFlagDisabled(Label.L0, flag=2052430800)
    DisableCharacter(2052430810)
    DisableAnimations(2052430810)
    Kill(2052430810)
    DisableCharacter(2052430811)
    DisableAnimations(2052430811)
    Kill(2052430811)
    DisableCharacter(2052430812)
    DisableAnimations(2052430812)
    Kill(2052430812)
    DisableCharacter(2052430813)
    DisableAnimations(2052430813)
    Kill(2052430813)
    DisableCharacter(2052430814)
    DisableAnimations(2052430814)
    Kill(2052430814)
    DisableCharacter(2052430815)
    DisableAnimations(2052430815)
    Kill(2052430815)
    DisableCharacter(2052430820)
    DisableAnimations(2052430820)
    Kill(2052430820)
    DisableCharacter(2052430821)
    DisableAnimations(2052430821)
    Kill(2052430821)
    DisableCharacter(2052430822)
    DisableAnimations(2052430822)
    Kill(2052430822)
    DisableCharacter(2052430800)
    DisableAnimations(2052430800)
    Kill(2052430800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2052430800)
    DisableAI(2052430810)
    DisableAI(2052430811)
    DisableAI(2052430812)
    DisableAI(2052430813)
    DisableAI(2052430814)
    DisableAI(2052430815)
    DisableAI(2052430820)
    DisableAI(2052430821)
    DisableAI(2052430822)
    DisableHealthBar(2052430800)
    DisableHealthBar(2052430810)
    DisableHealthBar(2052430811)
    DisableHealthBar(2052430812)
    DisableHealthBar(2052430813)
    DisableHealthBar(2052430814)
    DisableHealthBar(2052430815)
    DisableHealthBar(2052430820)
    DisableHealthBar(2052430821)
    DisableHealthBar(2052430822)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=2052432800))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430810))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430811))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430812))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430813))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430814))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430815))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430820))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430821))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2052430822))
    OR_1.Add(CharacterHasStateInfo(character=2052430800, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430800, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430800, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430800, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430800, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430810, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430810, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430810, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430810, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430810, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430811, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430811, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430811, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430811, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430811, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430812, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430812, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430812, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430812, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430812, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430813, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430813, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430813, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430813, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430813, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430814, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430814, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430814, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430814, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430814, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430815, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430815, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430815, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430815, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430815, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430820, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430820, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430820, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430820, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430820, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430821, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430821, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430821, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430821, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430821, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=2052430822, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=2052430822, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=2052430822, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=2052430822, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=2052430822, state_info=260))
    OR_1.Add(FlagEnabled(2052432801))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(2052432801)
    SetNetworkUpdateRate(2052430800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(2052430810, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430811, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430812, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430813, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430814, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430815, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430820, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430821, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    SetNetworkUpdateRate(2052430822, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    EnableAI(2052430800)
    EnableAI(2052430810)
    EnableAI(2052430811)
    EnableAI(2052430812)
    EnableAI(2052430813)
    EnableAI(2052430814)
    EnableAI(2052430815)
    EnableAI(2052430820)
    EnableAI(2052430821)
    EnableAI(2052430822)
    EnableBossHealthBar(2052430800, name=905320000, bar_slot=1)
    SetCharacterEventTarget(2052430810, entity=2052430800)
    SetCharacterEventTarget(2052430811, entity=2052430800)
    SetCharacterEventTarget(2052430812, entity=2052430800)
    SetCharacterEventTarget(2052430813, entity=2052430800)
    SetCharacterEventTarget(2052430814, entity=2052430800)
    SetCharacterEventTarget(2052430815, entity=2052430800)
    SetCharacterEventTarget(2052430820, entity=2052430800)
    SetCharacterEventTarget(2052430821, entity=2052430800)
    SetCharacterEventTarget(2052430822, entity=2052430800)


@ContinueOnRest(2052432816)
def Event_2052432816():
    """Event 2052432816"""
    if FlagEnabled(2052430800):
        return
    if FlagEnabled(2052432802):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2052430800, 20011848))
    
    EnableNetworkFlag(2052432802)
    End()


@RestartOnRest(2052432820)
def Event_2052432820(_, character: Character | int):
    """Event 2052432820"""
    if FlagEnabled(2052430800):
        return
    
    MAIN.Await(HealthValue(2052430800) <= 0)
    
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=20013255)
    DisableAI(character)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    Kill(character)
    Wait(6.0)
    DisableCharacter(character)


@RestartOnRest(2052432849)
def Event_2052432849():
    """Event 2052432849"""
    CommonFunc_9005800(
        0,
        flag=2052430800,
        entity=2052431800,
        region=2052432800,
        flag_1=2052432805,
        character=2052435800,
        action_button_id=210000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=2052430800,
        entity=2052431800,
        region=2052432800,
        flag_1=2052432805,
        flag_2=2052432806,
        action_button_id=210000,
    )
    CommonFunc_9005811(0, flag=2052430800, asset=2052431800, vfx_id=3, right=0)
    CommonFunc_9005811(0, flag=2052430800, asset=2052431801, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=2052430800,
        bgm_boss_conv_param_id=942000,
        flag_1=2052432805,
        flag_2=2052432806,
        right=0,
        flag_3=2052432802,
        left=0,
        left_1=0,
    )
