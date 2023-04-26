"""
Tombsward Cave

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
from .enums.m31_02_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=310200, asset=Assets.AEG099_060_9000)
    Event_31022800()
    Event_31022810()
    Event_31022811()
    Event_31022849()
    CommonFunc_90005250(0, character=31025800, region=31022361, seconds=0.0, animation_id=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005646(
        0,
        flag=31020800,
        left_flag=31022840,
        cancel_flag__right_flag=31022841,
        asset=Assets.AEG099_065_9000,
        player_start=31022840,
        area_id=31,
        block_id=2,
        cc_id=0,
        dd_id=0,
    )
    Event_31022900(0, tutorial_param_id=1580, flag=710580)
    Event_31022901(0, tutorial_param_id=1690, flag=710690, flag_1=31020040)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer0,
        region=31022200,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer1,
        region=31022201,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer2,
        region=31022205,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer3,
        region=31022206,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer4,
        region=31022206,
        radius=2.0,
        seconds=0.5,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer5,
        region=31022200,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer6,
        region=31022200,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31022211(0, character=Characters.FungalSorcerer5)
    Event_31022211(1, character=Characters.FungalSorcerer6)
    Event_31022223(
        0,
        character=Characters.FungalSorcerer7,
        animation_id=30001,
        animation_id_1=20001,
        region=31022218,
        radius=1.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.FungalSorcerer8,
        attacked_entity=Characters.FungalSorcerer9,
    )
    Event_31022223(
        1,
        character=Characters.FungalSorcerer8,
        animation_id=30001,
        animation_id_1=20001,
        region=31022218,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.FungalSorcerer7,
        attacked_entity=Characters.FungalSorcerer9,
    )
    Event_31022223(
        2,
        character=Characters.FungalSorcerer9,
        animation_id=30001,
        animation_id_1=20001,
        region=31022218,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        character_1=Characters.FungalSorcerer7,
        attacked_entity=Characters.FungalSorcerer8,
    )
    CommonFunc_90005261(0, character=Characters.GiantRat0, region=31022250, radius=2.0, seconds=0.0, animation_id=0)
    Event_31022255()
    Event_31022256()
    CommonFunc_90005261(0, character=Characters.GiantRat1, region=31022251, radius=2.0, seconds=0.0, animation_id=0)
    Event_31022250(0, character=Characters.GiantRat0)
    Event_31022250(0, character=Characters.Rat0)
    Event_31022250(0, character=Characters.Rat1)
    CommonFunc_90005261(0, character=Characters.Rat0, region=31022260, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=31022260, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Rat2,
        region=31022266,
        radius=2.0,
        seconds=0.30000001192092896,
        animation_id=0,
    )
    Event_31022260(0, character=Characters.GiantRat0)
    Event_31022260(1, character=Characters.GiantRat1)
    Event_31022260(2, character=Characters.Rat0)
    Event_31022260(3, character=Characters.Rat1)
    Event_31022260(4, character=31020262)
    Event_31022260(5, character=31020263)
    Event_31022260(6, character=31020264)
    Event_31022260(7, character=31020265)
    Event_31022260(8, character=Characters.Rat2)
    CommonFunc_90005211(
        0,
        character=31020301,
        animation_id=30000,
        animation_id_1=20000,
        region=31022300,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=31020302,
        animation_id=30000,
        animation_id_1=20000,
        region=31022300,
        radius=2.0,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass0,
        animation_id=30000,
        animation_id_1=20000,
        region=31022303,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass1,
        animation_id=30000,
        animation_id_1=20000,
        region=31022304,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower0,
        region=31022350,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower1,
        region=31022350,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower2,
        region=31022357,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower3,
        region=31022358,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.MirandaFlower4, region=31022358, radius=2.0, seconds=0.0, animation_id=0)


@RestartOnRest(31022211)
def Event_31022211(_, character: uint):
    """Event 31022211"""
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
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31022212))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer5))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer5, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer5, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer5, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer5, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer5, state_info=260))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer6, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer6, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer6, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer6, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.FungalSorcerer6, state_info=260))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31022223)
def Event_31022223(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    character_1: uint,
    attacked_entity: uint,
):
    """Event 31022223"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
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


@RestartOnRest(31022250)
def Event_31022250(_, character: uint):
    """Event 31022250"""
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
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=7.0))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GiantRat0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Rat0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Rat1))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=260))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31022255)
def Event_31022255():
    """Event 31022255"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31022255))
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()


@RestartOnRest(31022256)
def Event_31022256():
    """Event 31022256"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(Characters.GiantRat0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31022256))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31022250))
    AND_1.Add(FlagEnabled(31022255))
    AND_4.Add(CharacterHasSpecialEffect(Characters.GiantRat0, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.GiantRat0, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.GiantRat0, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.GiantRat0, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.GiantRat0, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.GiantRat0, 90160))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GiantRat0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantRat0, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(Characters.GiantRat0)


@RestartOnRest(31022260)
def Event_31022260(_, character: uint):
    """Event 31022260"""
    AddSpecialEffect(character, 90000)


@RestartOnRest(31022800)
def Event_31022800():
    """Event 31022800"""
    if FlagEnabled(31020800):
        return
    
    MAIN.Await(HealthValue(Characters.GiantMirandaFlower) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GiantMirandaFlower, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GiantMirandaFlower))
    
    KillBossAndDisplayBanner(character=Characters.GiantMirandaFlower, banner_type=BannerType.EnemyFelled)
    Kill(31025800)
    EnableFlag(31020800)
    EnableFlag(9230)
    if PlayerInOwnWorld():
        EnableFlag(61230)


@RestartOnRest(31022810)
def Event_31022810():
    """Event 31022810"""
    GotoIfFlagDisabled(Label.L0, flag=31020800)
    DisableCharacter(Characters.GiantMirandaFlower)
    DisableAnimations(Characters.GiantMirandaFlower)
    Kill(31025800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GiantMirandaFlower)
    AND_2.Add(FlagEnabled(31022805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31022800))
    
    MAIN.Await(AND_2)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(31020801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GiantMirandaFlower)
    SetNetworkUpdateRate(Characters.GiantMirandaFlower, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GiantMirandaFlower, name=904480311)


@RestartOnRest(31022811)
def Event_31022811():
    """Event 31022811"""
    if FlagEnabled(31020800):
        return
    AND_1.Add(HealthRatio(Characters.GiantMirandaFlower) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31022802)


@RestartOnRest(31022849)
def Event_31022849():
    """Event 31022849"""
    CommonFunc_9005800(
        0,
        flag=31020800,
        entity=Assets.AEG099_003_9000,
        region=31022800,
        flag_1=31022805,
        character=31025800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31020800,
        entity=Assets.AEG099_003_9000,
        region=31022800,
        flag_1=31022805,
        flag_2=31022806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31020800, asset=Assets.AEG099_003_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=31020800,
        bgm_boss_conv_param_id=931000,
        flag_1=31022805,
        flag_2=31022806,
        right=0,
        flag_3=31022802,
        left=0,
        left_1=0,
    )


@RestartOnRest(31022900)
def Event_31022900(_, tutorial_param_id: int, flag: uint):
    """Event 31022900"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerHasGood(9500))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(31022901)
def Event_31022901(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31022901"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)
