"""
m43_00_00_00

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
    RegisterGrace(grace_flag=43000000, asset=43001950)
    Event_43002800()
    Event_43002810()
    Event_43002811()
    Event_43002849()
    CommonFunc_90005250(0, character=43000202, region=43002202, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000208, region=43002202, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000209, region=43002202, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000203, region=43002203, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000208, region=43002203, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000210, region=43002203, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000203, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000204, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000205, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000206, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000207, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000209, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000211, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000212, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000213, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000214, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000215, region=43002204, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=43000216, region=43002204, seconds=0.0, animation_id=-1)
    Event_43002300(0, character=43005200, character_1=43000207, seconds=0.0, animation_id=-1)
    Event_43002300(0, character=43005200, character_1=43000204, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=43000234,
        animation_id=30001,
        animation_id_1=20001,
        region=43002234,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43000235,
        animation_id=30003,
        animation_id_1=20003,
        region=43002234,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43000236,
        animation_id=30012,
        animation_id_1=20022,
        region=43002237,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43000237,
        animation_id=30012,
        animation_id_1=20022,
        region=43002237,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=43000238,
        animation_id=30012,
        animation_id_1=20022,
        region=43002237,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=43000236, region=43002237, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005250(0, character=43000237, region=43002237, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005250(0, character=43000238, region=43002237, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005250(0, character=43000240, region=43002240, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=43000240, region=43002233, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=43000241, region=43002241, seconds=0.0, animation_id=3008)
    Event_43002350(
        0,
        character=43000233,
        animation_id=30005,
        animation_id_1=20005,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_43002500()
    Event_43002501()
    CommonFunc_90005646(
        0,
        flag=43000800,
        left_flag=43002840,
        cancel_flag__right_flag=43002841,
        asset=43001840,
        player_start=43002840,
        area_id=43,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=43001680, dummy_id=100, vfx_id=800, right=0)


@RestartOnRest(43002500)
def Event_43002500():
    """Event 43002500"""
    GotoIfFlagDisabled(Label.L0, flag=43000500)
    DisableAsset(43001500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetInvulnerability(43001500)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_2)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=43002500))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(43001500)
    EnableFlag(43000500)
    End()


@RestartOnRest(43002501)
def Event_43002501():
    """Event 43002501"""
    GotoIfFlagDisabled(Label.L0, flag=43000500)
    EndOfAnimation(asset=43001510, animation_id=101101)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(43000500))
    
    ForceAnimation(43001510, 101101, wait_for_completion=True)
    EndOfAnimation(asset=43001510, animation_id=101101)
    End()


@RestartOnRest(43002300)
def Event_43002300(_, character: uint, character_1: Character | int, seconds: float, animation_id: int):
    """Event 43002300"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(43002350)
def Event_43002350(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 43002350"""
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
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(CharacterDead(43000230))
    OR_2.Add(CharacterDead(43000231))
    OR_2.Add(CharacterDead(43000232))
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


@RestartOnRest(43002800)
def Event_43002800():
    """Event 43002800"""
    if FlagEnabled(43000800):
        return
    
    MAIN.Await(HealthValue(43000800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(43008000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(43000800))
    
    KillBossAndDisplayBanner(character=43000800, banner_type=BannerType.EnemyFelled)
    EnableFlag(43000800)
    EnableFlag(9280)
    if PlayerInOwnWorld():
        EnableFlag(61280)


@RestartOnRest(43002810)
def Event_43002810():
    """Event 43002810"""
    GotoIfFlagDisabled(Label.L0, flag=43000800)
    DisableCharacter(43000800)
    DisableAnimations(43000800)
    Kill(43000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(43000800)
    AND_2.Add(FlagEnabled(43002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=43002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(43000800)
    SetNetworkUpdateRate(43000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(43000800, name=905081430)


@RestartOnRest(43002811)
def Event_43002811():
    """Event 43002811"""
    if FlagEnabled(43000800):
        return
    AND_1.Add(HealthRatio(43000800) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(43002802)


@RestartOnRest(43002849)
def Event_43002849():
    """Event 43002849"""
    CommonFunc_9005800(
        0,
        flag=43000800,
        entity=43001800,
        region=43002800,
        flag_1=43002805,
        character=43005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=43000800,
        entity=43001800,
        region=43002800,
        flag_1=43002805,
        flag_2=43002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=43000800, asset=43001800, vfx_id=4, right=0)
    CommonFunc_9005822(
        0,
        flag=43000800,
        bgm_boss_conv_param_id=931000,
        flag_1=43002805,
        flag_2=43002806,
        right=0,
        flag_3=43002802,
        left=0,
        left_1=0,
    )
