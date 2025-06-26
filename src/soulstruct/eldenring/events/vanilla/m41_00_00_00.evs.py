"""
m41_00_00_00

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
    CommonFunc_900005610(0, asset=41001510, dummy_id=100, vfx_id=800, right=0)
    RegisterGrace(grace_flag=41000000, asset=41001950)
    Event_41000800()
    Event_41002810()
    Event_41002811()
    Event_41002849()
    CommonFunc_90005250(0, character=41000200, region=41002200, seconds=0.0, animation_id=3033)
    CommonFunc_90005221(0, character=41000201, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005200(
        0,
        character=41000203,
        animation_id=30001,
        animation_id_1=20001,
        region=41002203,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=41000204,
        animation_id=30001,
        animation_id_1=20001,
        region=41002203,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=41000205,
        animation_id=30001,
        animation_id_1=20001,
        region=41002203,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=41000211, radius=27.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=41000212, radius=32.0, seconds=3.0, animation_id=0)
    CommonFunc_90005250(0, character=41000208, region=41002208, seconds=0.0, animation_id=3036)
    CommonFunc_90005201(
        0,
        character=41000209,
        animation_id=30001,
        animation_id_1=20001,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=41000215, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005200(
        0,
        character=41000217,
        animation_id=30001,
        animation_id_1=20001,
        region=41002217,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=41000219, animation_id=30001, animation_id_1=20001, seconds=3.0, left=0)
    CommonFunc_90005221(0, character=41000220, animation_id=30001, animation_id_1=20001, seconds=3.0, left=0)
    CommonFunc_90005200(
        0,
        character=41000222,
        animation_id=30007,
        animation_id_1=20007,
        region=41002222,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_41002555(0, character=41000222, asset=41001522)
    CommonFunc_90005200(
        0,
        character=41000225,
        animation_id=30007,
        animation_id_1=20007,
        region=41002222,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_41002555(1, character=41000225, asset=41001525)
    CommonFunc_90005200(
        0,
        character=41000226,
        animation_id=30007,
        animation_id_1=20007,
        region=41002222,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_41002555(2, character=41000226, asset=41001526)
    CommonFunc_90005201(
        0,
        character=41000231,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=41000232,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=41000233, region=41002233, seconds=0.0, animation_id=0)
    CommonFunc_90005445(
        0,
        character=41000308,
        animation_id=30000,
        animation_id_1=20000,
        region=41002306,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001308,
    )
    CommonFunc_90005446(
        0,
        character=41000308,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001308,
    )
    CommonFunc_90005200(
        0,
        character=41000255,
        animation_id=30000,
        animation_id_1=20000,
        region=41002255,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41000256,
        animation_id=30000,
        animation_id_1=20000,
        region=41002310,
        radius=7.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005445(
        0,
        character=41000310,
        animation_id=30004,
        animation_id_1=20004,
        region=41002310,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001310,
    )
    CommonFunc_90005200(
        0,
        character=41000353,
        animation_id=30000,
        animation_id_1=20000,
        region=41002353,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=41000260, radius=50.0, seconds=1.0, animation_id=0)
    CommonFunc_90005251(0, character=41000261, radius=50.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=41000311,
        animation_id=30000,
        animation_id_1=20000,
        region=41002311,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=41000314,
        animation_id=30000,
        animation_id_1=20000,
        region=41002314,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41000315, region=41002315, radius=6.0, seconds=7.0, animation_id=-1)
    CommonFunc_90005261(0, character=41000316, region=41002316, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=41000317,
        animation_id=30003,
        animation_id_1=20003,
        region=41002317,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41000317, region=41002317, radius=3.0, seconds=2.0, animation_id=3003)
    CommonFunc_90005211(
        0,
        character=41000318,
        animation_id=30003,
        animation_id_1=20003,
        region=41002317,
        radius=3.0,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=41000318,
        region=41002317,
        radius=3.0,
        seconds=3.200000047683716,
        animation_id=3003,
    )
    CommonFunc_90005251(0, character=41000244, radius=1.0, seconds=1.0, animation_id=1700)
    CommonFunc_90005250(0, character=41000242, region=41002242, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=41000243, region=41002242, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=41000245, region=41002242, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=41000246, region=41002242, seconds=1.0, animation_id=0)
    CommonFunc_90005445(
        0,
        character=41000322,
        animation_id=30004,
        animation_id_1=20004,
        region=41002322,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001322,
    )
    CommonFunc_90005445(
        0,
        character=41000324,
        animation_id=30004,
        animation_id_1=20004,
        region=41002324,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001324,
    )
    CommonFunc_90005251(0, character=41000320, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=41000321, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=41000323, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=41000325, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005250(0, character=41000342, region=41002342, seconds=4.0, animation_id=-1)
    Event_41002361()
    CommonFunc_90005200(
        0,
        character=41000359,
        animation_id=30001,
        animation_id_1=20001,
        region=41002359,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=41000268, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41000269, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41000248, animation_id=30010, animation_id_1=20010, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=41000327,
        animation_id=30003,
        animation_id_1=20003,
        region=41002326,
        radius=3.0,
        seconds=0.800000011920929,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41000329,
        animation_id=30003,
        animation_id_1=20003,
        region=41002326,
        radius=3.0,
        seconds=1.2000000476837158,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41000341,
        animation_id=30003,
        animation_id_1=20003,
        region=41002326,
        radius=3.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005446(
        0,
        character=41000330,
        animation_id=30004,
        animation_id_1=20004,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41001330,
    )
    CommonFunc_90005251(0, character=41000330, radius=8.0, seconds=0.4000000059604645, animation_id=3002)
    Event_41002360()
    CommonFunc_90005201(
        0,
        character=41000360,
        animation_id=30001,
        animation_id_1=20001,
        radius=11.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_41000500(0, flag=41000500, asset=41001500, region=41002500)
    Event_41000500(1, flag=41000501, asset=41001501, region=41002501)
    CommonFunc_90005646(
        0,
        flag=41000800,
        left_flag=41002840,
        cancel_flag__right_flag=41002841,
        asset=41001840,
        player_start=41002840,
        area_id=41,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005690(0, region=41002600)
    CommonFunc_90005691(0, region=41002600)
    Event_41002610()
    CommonFunc_90005706(0, character=41000700, animation_id=30021, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    EnableAssetInvulnerability(41001303)


@RestartOnRest(41000500)
def Event_41000500(_, flag: Flag | int, asset: Asset | int, region: Region | int):
    """Event 41000500"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetInvulnerability(asset)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)
    EnableFlag(flag)
    End()


@RestartOnRest(41002555)
def Event_41002555(_, character: uint, asset: Asset | int):
    """Event 41002555"""
    if ThisEventSlotFlagEnabled():
        return
    if AssetDestroyed(asset):
        MAIN.Await(CharacterHasSpecialEffect(character, 9624))
    
        ForceAnimation(character, 0)
        EnableAI(character)
    End()
    EnableAssetInvulnerability(asset)
    if UnsignedEqual(left=character, right=0):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 9624))
    
    OR_1.Add(SpecialStandbyEndedFlagEnabled(character=character))
    OR_1.Add(CharacterDoesNotHaveSpecialEffect(character, 9624))
    
    MAIN.Await(OR_1)
    
    DisableAssetInvulnerability(asset)


@ContinueOnRest(41002360)
def Event_41002360():
    """Event 41002360"""
    if ThisEventSlotFlagEnabled():
        return
    SetLockOnPoint(character=41000360, lock_on_dummy_id=220, state=False)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=41002360))
    OR_1.Add(AND_1)
    OR_1.Add(HealthRatio(41000360) <= 0.9998999834060669)
    OR_1.Add(SpecialStandbyEndedFlagEnabled(character=41000360))
    
    MAIN.Await(OR_1)
    
    EnableThisNetworkSlotFlag()
    SetLockOnPoint(character=41000360, lock_on_dummy_id=220, state=True)
    if SpecialStandbyEndedFlagDisabled(character=41000360):
        ForceAnimation(41000360, 20000, loop=True)
    Wait(0.5)
    if SpecialStandbyEndedFlagDisabled(character=41000372):
        ForceAnimation(41000372, 20000, loop=True)
    Wait(0.30000001192092896)
    if SpecialStandbyEndedFlagDisabled(character=41000373):
        ForceAnimation(41000373, 20000, loop=True)
    Wait(0.699999988079071)
    if SpecialStandbyEndedFlagDisabled(character=41000371):
        ForceAnimation(41000371, 20000, loop=True)
    Wait(0.5)
    if SpecialStandbyEndedFlagDisabled(character=41000374):
        ForceAnimation(41000374, 20000, loop=True)


@ContinueOnRest(41002361)
def Event_41002361():
    """Event 41002361"""
    if ThisEventSlotFlagEnabled():
        return
    SetLockOnPoint(character=41000359, lock_on_dummy_id=220, state=False)
    OR_1.Add(HealthRatio(41000359) <= 0.9998999834060669)
    OR_1.Add(HealthRatio(41000268) <= 0.9998999834060669)
    OR_1.Add(HealthRatio(41000269) <= 0.9998999834060669)
    OR_1.Add(SpecialStandbyEndedFlagEnabled(character=41000359))
    
    MAIN.Await(OR_1)
    
    EnableThisNetworkSlotFlag()
    SetLockOnPoint(character=41000359, lock_on_dummy_id=220, state=True)
    if SpecialStandbyEndedFlagDisabled(character=41000359):
        ForceAnimation(41000359, 20001, loop=True)
    if SpecialStandbyEndedFlagDisabled(character=41000268):
        ForceAnimation(41000268, 20052, loop=True)
    if SpecialStandbyEndedFlagDisabled(character=41000269):
        ForceAnimation(41000269, 20052, loop=True)


@RestartOnRest(41002370)
def Event_41002370(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    character_1: Character | int,
    radius_1: float,
):
    """Event 41002370"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_9.Add(CharacterDead(character_1))
    AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    OR_3.Add(AND_9)
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(41000800)
def Event_41000800():
    """Event 41000800"""
    if FlagEnabled(41000800):
        return
    
    MAIN.Await(HealthValue(41000800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(41000800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(41000800))
    
    KillBossAndDisplayBanner(character=41000800, banner_type=BannerType.EnemyFelled)
    EnableFlag(41000800)
    EnableFlag(9275)
    if PlayerInOwnWorld():
        EnableFlag(61275)


@RestartOnRest(41002810)
def Event_41002810():
    """Event 41002810"""
    GotoIfFlagDisabled(Label.L0, flag=41000800)
    DisableCharacter(41000800)
    DisableAnimations(41000800)
    Kill(41000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(41000800)
    AND_2.Add(FlagEnabled(41002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=41002800))
    
    MAIN.Await(AND_2)
    
    EnableAI(41000800)
    EnableAnimations(41000800)
    SetNetworkUpdateRate(41000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(41000800, name=905810410)


@RestartOnRest(41002811)
def Event_41002811():
    """Event 41002811"""
    if FlagEnabled(41000800):
        return
    
    MAIN.Await(HealthRatio(41000800) <= 0.699999988079071)
    
    EnableFlag(41002802)


@RestartOnRest(41002849)
def Event_41002849():
    """Event 41002849"""
    CommonFunc_9005800(
        0,
        flag=41000800,
        entity=41001800,
        region=41002800,
        flag_1=41002805,
        character=41005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=41000800,
        entity=41001800,
        region=41002800,
        flag_1=41002805,
        flag_2=41002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=41000800, asset=41001800, vfx_id=8, right=0)
    CommonFunc_9005822(
        0,
        flag=41000800,
        bgm_boss_conv_param_id=941000,
        flag_1=41002805,
        flag_2=41002806,
        right=0,
        flag_3=41002802,
        left=1,
        left_1=0,
    )


@RestartOnRest(41002610)
def Event_41002610():
    """Event 41002610"""
    GotoIfFlagEnabled(Label.L9, flag=41002601)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41002610))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=41002611))
    OR_1.Add(FlagEnabled(41002601))
    
    MAIN.Await(OR_1)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(41002601)
    ForceAnimation(41001611, 0, skip_transition=True)
    ForceAnimation(41001610, 12, wait_for_completion=True, skip_transition=True)
    ForceAnimation(41001610, 20, wait_for_completion=True, skip_transition=True)
    ForceAnimation(41001610, 21, wait_for_completion=True, skip_transition=True)
    ForceAnimation(41001610, 10, wait_for_completion=True, skip_transition=True)
    AND_2.Add(AllPlayersOutsideRegion(region=41002610))
    AND_2.Add(AllPlayersOutsideRegion(region=41002611))
    AND_2.Add(AssetBackreadEnabled(asset=41001610))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(41002601))
    
    MAIN.Await(OR_2)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(41002601)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(41002601))
    
    Restart()
