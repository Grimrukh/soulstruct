"""
Highroad Cave

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
from .entities.m31_17_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=311700, asset=Assets.AEG099_060_9000)
    Event_31172800()
    Event_31172499()
    Event_31172810()
    Event_31172811()
    Event_31172849()
    CommonFunc_90005646(
        0,
        flag=31170800,
        left_flag=31172840,
        cancel_flag__right_flag=31172841,
        asset=Assets.AEG099_065_9000,
        player_start=31172840,
        area_id=31,
        block_id=17,
        cc_id=0,
        dd_id=0,
    )
    Event_31172500()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Wolf0, region=31172200, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=31170201,
        animation_id=30005,
        animation_id_1=20005,
        region=31172204,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf1,
        animation_id=30001,
        animation_id_1=20001,
        region=31172204,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf2,
        animation_id=30004,
        animation_id_1=20004,
        region=31172204,
        radius=2.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf4,
        animation_id=30001,
        animation_id_1=20001,
        region=31172212,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf5,
        animation_id=30004,
        animation_id_1=20004,
        region=31172212,
        radius=2.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf6,
        animation_id=30000,
        animation_id_1=20000,
        region=31172216,
        radius=2.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=31170217,
        animation_id=30001,
        animation_id_1=20001,
        region=31172216,
        radius=2.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31172216(0, character=Characters.Wolf6)
    Event_31172216(1, character=31170217)
    CommonFunc_90005211(
        0,
        character=Characters.Wolf7,
        animation_id=30001,
        animation_id_1=20001,
        region=31172218,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.WolfPackLeader1,
        animation_id=30001,
        animation_id_1=20001,
        region=31172245,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31172208(7, character=Characters.Wolf1)
    Event_31172208(8, character=Characters.Wolf2)
    CommonFunc_90005211(
        0,
        character=Characters.Wolf3,
        animation_id=30003,
        animation_id_1=20003,
        region=31172207,
        radius=1.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf8,
        animation_id=30003,
        animation_id_1=20003,
        region=31172219,
        radius=1.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Wolf9,
        animation_id=30003,
        animation_id_1=20003,
        region=31172220,
        radius=1.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31172218(3, character=Characters.WolfPackLeader0, region=31172240, radius=4.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005261(0, character=Characters.Bat0, region=31172250, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Bat4, region=31172250, radius=2.0, seconds=2.0, animation_id=0)
    Event_31172254()
    CommonFunc_90005211(
        0,
        character=Characters.Bat1,
        animation_id=30000,
        animation_id_1=20000,
        region=31172251,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat2,
        animation_id=30000,
        animation_id_1=20000,
        region=31172252,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Bat3,
        animation_id=30000,
        animation_id_1=20000,
        region=31172252,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Bat5, region=31172258, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Bat6,
        animation_id=30000,
        animation_id_1=20000,
        region=31172258,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Bat7, region=31172260, radius=2.0, seconds=5.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Bat8, region=31172260, radius=2.0, seconds=10.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Octopus0, region=31172300, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Octopus1, region=31172300, radius=2.0, seconds=0.5, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Octopus2, region=31172302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Octopus3,
        region=31172302,
        radius=2.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Octopus4, region=31172308, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Octopus5, region=31172309, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Octopus6, region=31172309, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.GiantOctopus,
        animation_id=30002,
        animation_id_1=20002,
        region=31172340,
        radius=3.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, 31170340)


@RestartOnRest(31172500)
def Event_31172500():
    """Event 31172500"""
    DisableAsset(Assets.AEG003_071_1008)


@RestartOnRest(31172208)
def Event_31172208(_, character: uint):
    """Event 31172208"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31172216)
def Event_31172216(_, character: uint):
    """Event 31172216"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31172218)
def Event_31172218(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31172218"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31172254)
def Event_31172254():
    """Event 31172254"""
    AddSpecialEffect(Characters.Bat4, 10525)


@RestartOnRest(31172499)
def Event_31172499():
    """Event 31172499"""
    if FlagEnabled(31170800):
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=31172390))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GuardianGolem, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GuardianGolem, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GuardianGolem, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GuardianGolem, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GuardianGolem, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GuardianGolem, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableFlag(31172499)


@RestartOnRest(31172800)
def Event_31172800():
    """Event 31172800"""
    if FlagEnabled(31170800):
        return
    
    MAIN.Await(HealthValue(Characters.GuardianGolem) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GuardianGolem, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GuardianGolem))
    
    KillBossAndDisplayBanner(character=Characters.GuardianGolem, banner_type=BannerType.EnemyFelled)
    EnableFlag(31170800)
    EnableFlag(9235)
    if PlayerInOwnWorld():
        EnableFlag(61235)


@RestartOnRest(31172810)
def Event_31172810():
    """Event 31172810"""
    GotoIfFlagDisabled(Label.L0, flag=31170800)
    DisableCharacter(Characters.GuardianGolem)
    DisableAnimations(Characters.GuardianGolem)
    Kill(Characters.GuardianGolem)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GuardianGolem)
    SetLockOnPoint(character=Characters.GuardianGolem, lock_on_model_point=220, state=False)
    AND_2.Add(FlagEnabled(31172805))
    AND_2.Add(FlagEnabled(31172499))
    
    MAIN.Await(AND_2)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(31170801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GuardianGolem)
    SetNetworkUpdateRate(Characters.GuardianGolem, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GuardianGolem, name=904660310)
    SetLockOnPoint(character=Characters.GuardianGolem, lock_on_model_point=220, state=True)


@RestartOnRest(31172811)
def Event_31172811():
    """Event 31172811"""
    if FlagEnabled(31170800):
        return
    AND_1.Add(HealthRatio(Characters.GuardianGolem) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31172802)


@RestartOnRest(31172849)
def Event_31172849():
    """Event 31172849"""
    CommonFunc_9005800(
        0,
        flag=31170800,
        entity=Assets.AEG099_002_9000,
        region=31172800,
        flag_1=31172805,
        character=31175800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31170800,
        entity=Assets.AEG099_002_9000,
        region=31172800,
        flag_1=31172805,
        flag_2=31172806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31170800, asset=Assets.AEG099_002_9000, model_point=5, right=0)
    CommonFunc_9005822(0, 31170800, 931000, 31172805, 31172806, 31172499, 31172802, 0, 0)


@RestartOnRest(31172900)
def Event_31172900(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31172900"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(700690):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(700690))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    EnableFlag(700690)
