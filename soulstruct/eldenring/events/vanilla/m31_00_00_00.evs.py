"""
Murkwater Cave

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
from .enums.m31_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31000000, asset=Assets.AEG099_060_9000)
    Event_31002800()
    Event_31002810()
    Event_31002849()
    Event_31002811()
    Event_31002813()
    Event_31002814()
    Event_31002850()
    Event_31002860()
    Event_31002899()
    Event_31002861()
    Event_31002863()
    Event_31002845()
    Event_31002875()
    Event_31002876(
        0,
        flag=31000845,
        left_flag=31002840,
        cancel_flag__right_flag=31002841,
        asset=Assets.AEG099_065_9000,
        player_start=31002840,
        area_id=31,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    Event_31002500(0, attacked_entity=31001500, region=31002500)
    Event_31002500(1, attacked_entity=31001501, region=31002501)
    Event_31002500(2, attacked_entity=31001502, region=31002502)
    Event_31003700(0, character=Characters.Patches1)
    Event_31003710(0, character=Characters.Patches3)
    Event_31003701(0, character=Characters.Patches1, flag=31002709, flag_1=31009201, character_1=Characters.Patches0)
    Event_31003711(0, character=Characters.Patches3, flag=31002709, flag_1=31009201, character_1=Characters.Patches2)
    Event_31003702(0, character=Characters.Patches0)
    Event_31003703()
    Event_31003704(0, character=Characters.Patches0, seconds=10.0)
    Event_31003705(0, character=Characters.Patches0)
    Event_31003707()
    Event_31003713(0, character=Characters.Patches2)
    Event_31003714(0, character=Characters.Patches2, seconds=10.0)
    Event_31003715(0, attacked_entity=Characters.Patches2)
    CommonFunc_90005704(0, attacked_entity=Characters.Patches0, flag=31009219, flag_1=3680, flag_2=31009201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches0,
        flag=3681,
        flag_1=3682,
        flag_2=31009201,
        flag_3=31009219,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    Event_31003706(0, character=Characters.Patches0, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005704(0, attacked_entity=Characters.Patches1, flag=31009219, flag_1=3680, flag_2=31009201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches1,
        flag=3681,
        flag_1=3682,
        flag_2=31009201,
        flag_3=31009219,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Patches1, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005704(0, attacked_entity=Characters.Patches3, flag=3681, flag_1=3680, flag_2=31009201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches3,
        flag=3681,
        flag_1=3682,
        flag_2=31009201,
        flag_3=3681,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Patches3, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005704(0, attacked_entity=Characters.Patches2, flag=31009269, flag_1=3680, flag_2=31009201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Patches2,
        flag=3681,
        flag_1=3682,
        flag_2=31009201,
        flag_3=31009269,
        first_flag=3680,
        last_flag=3684,
        right=-1,
    )
    Event_31003716(0, character=Characters.Patches2, flag=3683, first_flag=3680, last_flag=3684)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(31000700)
    DisableBackread(Characters.Patches1)
    DisableBackread(31000702)
    DisableBackread(Characters.Patches3)
    Event_31002230(0, character=Characters.Highwayman0, region=31002200, radius=2.0, seconds=0.0, animation_id=0)
    Event_31002200(
        0,
        character=Characters.Highwayman1,
        animation_id=30010,
        animation_id_1=20010,
        region=31002202,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31002210(
        0,
        character=Characters.Highwayman2,
        region=31002205,
        radius=3.0,
        seconds=0.0,
        animation_id=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31002210(
        1,
        character=Characters.Highwayman3,
        region=31002205,
        radius=3.0,
        seconds=0.0,
        animation_id=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31002200(
        1,
        character=Characters.Highwayman4,
        animation_id=30010,
        animation_id_1=20010,
        region=31002209,
        radius=2.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31002200(
        2,
        character=Characters.Highwayman5,
        animation_id=30010,
        animation_id_1=20010,
        region=31002209,
        radius=2.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31002200(
        3,
        character=Characters.Highwayman6,
        animation_id=30010,
        animation_id_1=20010,
        region=31002209,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=31002500,
        region_2=31002501,
        region_3=31002502,
    )
    Event_31003712()


@RestartOnRest(31002500)
def Event_31002500(_, attacked_entity: uint, region: uint):
    """Event 31002500"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(31002200)
def Event_31002200(
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
    region_1: uint,
    region_2: uint,
    region_3: uint,
):
    """Event 31002200"""
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
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
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


@RestartOnRest(31002210)
def Event_31002210(
    _,
    character: uint,
    region: uint,
    radius: float,
    seconds: float,
    animation_id: int,
    region_1: uint,
    region_2: uint,
    region_3: uint,
):
    """Event 31002210"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31002230)
def Event_31002230(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 31002230"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(31002800)
def Event_31002800():
    """Event 31002800"""
    OR_1.Add(FlagEnabled(31000800))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagEnabled(3691))
    if OR_1:
        return
    
    MAIN.Await(HealthValue(Characters.Patches0) <= 0)
    
    if FlagEnabled(31000800):
        return
    Wait(4.0)
    PlaySoundEffect(Characters.Patches0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.Patches0))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(31000800))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(31000800)
    KillBossAndDisplayBanner(character=Characters.Patches0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31000800)
    EnableFlag(9232)
    if PlayerInOwnWorld():
        EnableFlag(61232)
    AwardItemLot(101830, host_only=False)


@RestartOnRest(31002810)
def Event_31002810():
    """Event 31002810"""
    OR_1.Add(FlagEnabled(31000800))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagEnabled(3691))
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    DisableCharacter(Characters.Patches0)
    DisableAnimations(Characters.Patches0)
    DisableBackread(Characters.Patches0)
    Kill(Characters.Patches0)
    if FlagDisabled(31000800):
        EnableFlag(31000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Patches0)
    AddSpecialEffect(Characters.Patches0, 9643)
    GotoIfFlagDisabled(Label.L1, flag=31008521)
    EnableNetworkFlag(31008820)
    Move(
        Characters.Patches0,
        destination=31002820,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.Patches0,
    )
    ChangePatrolBehavior(Characters.Patches0, patrol_information_id=0)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(31002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31002800))
    
    MAIN.Await(AND_2)
    
    if FlagDisabled(31008820):
        EnableNetworkFlag(31008821)
        DisableCharacter(Characters.Patches0)
        End()
    SetTeamType(Characters.Patches0, TeamType.Enemy)
    EnableAI(Characters.Patches0)
    SetNetworkUpdateRate(Characters.Patches0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Patches0, name=130900)
    EnableNetworkFlag(31000811)


@RestartOnRest(31002811)
def Event_31002811():
    """Event 31002811"""
    OR_1.Add(FlagEnabled(31000800))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagEnabled(3691))
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(31009810))
    
    SetTeamType(Characters.Patches0, TeamType.FriendlyNPC)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(31000800))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(31000800)
    PlaySoundEffect(Characters.Patches0, 888880000, sound_type=SoundType.s_SFX)
    KillBossAndDisplayBanner(character=Characters.Patches0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31000800)
    if PlayerInOwnWorld():
        EnableFlag(61232)
    EnableFlag(9232)
    AwardItemLot(101830, host_only=False)
    ChangePatrolBehavior(Characters.Patches0, patrol_information_id=31003820)
    ReplanAI(Characters.Patches0)


@RestartOnRest(31002813)
def Event_31002813():
    """Event 31002813"""
    OR_1.Add(FlagEnabled(31000800))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagEnabled(3691))
    if OR_1:
        return
    
    MAIN.Await(FlagState(FlagSetting.Change, FlagType.Absolute, 31008521))
    
    if FlagDisabled(31008821):
        return
    EnableCharacter(Characters.Patches0)
    Wait(4.0)
    SetTeamType(Characters.Patches0, TeamType.Enemy)
    EnableAI(Characters.Patches0)
    SetNetworkUpdateRate(Characters.Patches0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(Characters.Patches0, name=130900)
    EnableNetworkFlag(31000811)
    SetNest(Characters.Patches0, region=31002820)


@RestartOnRest(31002814)
def Event_31002814():
    """Event 31002814"""
    OR_1.Add(FlagEnabled(31000800))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagEnabled(3691))
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(31002713))
    
    EnableAI(Characters.Patches0)
    SetTeamType(Characters.Patches0, TeamType.Enemy)


@RestartOnRest(31002849)
def Event_31002849():
    """Event 31002849"""
    Event_31002830(
        0,
        flag=31000800,
        entity=Assets.AEG099_001_9000,
        region=31002800,
        flag_1=31002805,
        character=31005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    Event_31002831(
        0,
        flag=31000800,
        entity=Assets.AEG099_001_9000,
        region=31002800,
        flag_1=31002805,
        flag_2=31002806,
        action_button_id=10000,
    )
    Event_31002832(0, flag=31000800, asset=Assets.AEG099_001_9000, model_point=4, right=0)
    Event_31002833(
        0,
        flag=31000800,
        bgm_boss_conv_param_id=931000,
        flag_1=31002805,
        flag_2=31002806,
        right=31000811,
        flag_3=0,
        left=0,
        left_1=0,
    )


@RestartOnRest(31002831)
def Event_31002831(_, flag: uint, entity: uint, region: uint, flag_1: uint, flag_2: uint, action_button_id: int):
    """Event 31002831"""
    if FlagEnabled(3691):
        return
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    MAIN.Await(AND_1)
    
    SuppressSoundForFogGate(duration=5.0)
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(TimeElapsed(seconds=3.0))
    OR_2.Add(OR_1)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    RestartIfFinishedConditionTrue(input_condition=OR_1)
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(31002830)
def Event_31002830(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 31002830"""
    if FlagEnabled(3691):
        return
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    else:
        RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31002832)
def Event_31002832(_, flag: uint, asset: uint, model_point: int, right: uint):
    """Event 31002832"""
    if FlagEnabled(3691):
        return
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_3.Add(FlagEnabled(right))
    AND_3.Add(FlagDisabled(flag))
    OR_4.Add(Invasion())
    OR_4.Add(InvasionPending())
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(not AND_7)
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_5.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    OR_8.Add(AND_1)
    OR_8.Add(AND_2)
    OR_8.Add(AND_3)
    OR_8.Add(AND_4)
    OR_8.Add(AND_5)
    
    MAIN.Await(OR_8)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, vfx_id=101, model_point=model_point)
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_11.Add(OR_11)
    AND_11.Add(FlagDisabled(flag))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_12.Add(OR_12)
    AND_12.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_13.Add(FlagEnabled(right))
    AND_13.Add(FlagDisabled(flag))
    OR_14.Add(Invasion())
    OR_14.Add(InvasionPending())
    AND_14.Add(OR_14)
    AND_14.Add(FlagEnabled(flag))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(not OR_7)
    OR_15.Add(Invasion())
    OR_15.Add(InvasionPending())
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag))
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_15.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_9.Add(not AND_11)
    AND_9.Add(not AND_12)
    AND_9.Add(not AND_13)
    AND_9.Add(not AND_14)
    AND_9.Add(not AND_15)
    
    MAIN.Await(AND_9)
    
    Restart()


@RestartOnRest(31002833)
def Event_31002833(
    _,
    flag: uint,
    bgm_boss_conv_param_id: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    left: int,
    left_1: int,
):
    """Event 31002833"""
    if FlagEnabled(3691):
        return
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Stop2)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Stop1)


@RestartOnRest(31002899)
def Event_31002899():
    """Event 31002899"""
    Event_31002870(
        0,
        flag=31000850,
        entity=Assets.AEG099_001_9000,
        region=31002800,
        flag_1=31002855,
        character=31005850,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    Event_31002872(0, flag=31000850, asset=Assets.AEG099_001_9000, model_point=4, right=0)
    Event_31002873(
        0,
        flag=31000850,
        bgm_boss_conv_param_id=931000,
        flag_1=31002855,
        flag_2=31002856,
        right=31000861,
        flag_3=0,
        left=0,
        left_1=0,
    )


@RestartOnRest(31002850)
def Event_31002850():
    """Event 31002850"""
    OR_1.Add(FlagEnabled(31000850))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagDisabled(3691))
    if OR_1:
        return
    
    MAIN.Await(HealthValue(Characters.Patches2) <= 0)
    
    if FlagEnabled(31000850):
        return
    Wait(4.0)
    PlaySoundEffect(Characters.Patches2, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.Patches2))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(31000850))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(31000850)
    KillBossAndDisplayBanner(character=Characters.Patches2, banner_type=BannerType.EnemyFelled)
    EnableFlag(31000850)
    EnableFlag(9232)
    if PlayerInOwnWorld():
        EnableFlag(61232)


@RestartOnRest(31002860)
def Event_31002860():
    """Event 31002860"""
    OR_1.Add(FlagEnabled(31000850))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagDisabled(3691))
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    DisableCharacter(Characters.Patches2)
    DisableAnimations(Characters.Patches2)
    DisableBackread(Characters.Patches2)
    Kill(Characters.Patches2)
    if FlagEnabled(3683):
        EnableFlag(31000850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Patches2)
    AddSpecialEffect(Characters.Patches2, 9643)
    GotoIfFlagDisabled(Label.L1, flag=31008523)
    EnableNetworkFlag(31008870)
    Move(
        Characters.Patches2,
        destination=31002820,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.Patches2,
    )
    ChangePatrolBehavior(Characters.Patches2, patrol_information_id=0)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(31002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31002800))
    
    MAIN.Await(AND_2)
    
    if FlagDisabled(31008870):
        EnableNetworkFlag(31008871)
        DisableCharacter(Characters.Patches2)
        End()
    SetTeamType(Characters.Patches2, TeamType.Enemy)
    EnableAI(Characters.Patches2)
    SetNetworkUpdateRate(Characters.Patches2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Patches2, name=130900)
    EnableNetworkFlag(31000861)


@RestartOnRest(31002861)
def Event_31002861():
    """Event 31002861"""
    OR_1.Add(FlagEnabled(31000850))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagDisabled(3691))
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(31009889))
    
    SetTeamType(Characters.Patches2, TeamType.FriendlyNPC)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(31000850))
    
    MAIN.Await(OR_2)
    
    EnableNetworkFlag(31000850)
    PlaySoundEffect(Characters.Patches2, 888880000, sound_type=SoundType.s_SFX)
    KillBossAndDisplayBanner(character=Characters.Patches2, banner_type=BannerType.EnemyFelled)
    EnableFlag(31000850)
    if PlayerInOwnWorld():
        EnableFlag(61232)
    EnableFlag(9232)
    ChangePatrolBehavior(Characters.Patches2, patrol_information_id=31003820)
    ReplanAI(Characters.Patches2)


@RestartOnRest(31002863)
def Event_31002863():
    """Event 31002863"""
    OR_1.Add(FlagEnabled(31000850))
    OR_1.Add(FlagEnabled(3683))
    OR_1.Add(FlagDisabled(3691))
    if OR_1:
        return
    
    MAIN.Await(FlagState(FlagSetting.Change, FlagType.Absolute, 31008523))
    
    if FlagDisabled(31008871):
        return
    EnableCharacter(Characters.Patches2)
    Wait(4.0)
    SetTeamType(Characters.Patches2, TeamType.Enemy)
    EnableAI(Characters.Patches2)
    SetNetworkUpdateRate(Characters.Patches2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(5.0)
    EnableBossHealthBar(Characters.Patches2, name=130900)
    EnableNetworkFlag(31000861)
    SetNest(Characters.Patches2, region=31002820)


@RestartOnRest(31002870)
def Event_31002870(
    _,
    flag: uint,
    entity: uint,
    region: uint,
    flag_1: uint,
    character: uint,
    action_button_id: int,
    left: uint,
    region_1: uint,
):
    """Event 31002870"""
    if FlagDisabled(3691):
        return
    GotoIfFlagEnabled(Label.L10, flag=flag)
    WaitFrames(frames=1)
    GotoIfUnsignedEqual(Label.L0, left=left, right=0)
    GotoIfFlagEnabled(Label.L0, flag=left)
    if UnsignedNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(FlagEnabled(left))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag):
        return RESTART
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L3)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    OR_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfPlayerNotInOwnWorld(Label.L2)
    if FlagEnabled(flag):
        return RESTART
    SuppressSoundForFogGate(duration=5.0)
    if CharacterDoesNotHaveSpecialEffect(character=PLAYER, special_effect=4250):
        RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    else:
        RotateToFaceEntity(PLAYER, region, animation=60060)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_5.Add(OR_4)
    AND_4.Add(OR_5)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagDisabled(flag))
    OR_6.Add(AND_4)
    OR_6.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_6)
    
    if FlagEnabled(flag):
        return RESTART
    RestartIfFinishedConditionTrue(input_condition=OR_4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(character)
    EnableNetworkFlag(flag_1)
    if PlayerNotInOwnWorld():
        return
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    if PlayerNotInOwnWorld():
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(flag))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_10.Add(OR_10)
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=entity))
    
    MAIN.Await(AND_10)
    
    RotateToFaceEntity(PLAYER, region, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@RestartOnRest(31002872)
def Event_31002872(_, flag: uint, asset: uint, model_point: int, right: uint):
    """Event 31002872"""
    if FlagDisabled(3691):
        return
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_3.Add(FlagEnabled(right))
    AND_3.Add(FlagDisabled(flag))
    OR_4.Add(Invasion())
    OR_4.Add(InvasionPending())
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(not AND_7)
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_5.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    OR_8.Add(AND_1)
    OR_8.Add(AND_2)
    OR_8.Add(AND_3)
    OR_8.Add(AND_4)
    OR_8.Add(AND_5)
    
    MAIN.Await(OR_8)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, vfx_id=101, model_point=model_point)
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_11.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    AND_11.Add(OR_11)
    AND_11.Add(FlagDisabled(flag))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_12.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_12.Add(OR_12)
    AND_12.Add(FlagDisabled(flag))
    if UnsignedNotEqual(left=0, right=right):
        AND_13.Add(FlagEnabled(right))
    AND_13.Add(FlagDisabled(flag))
    OR_14.Add(Invasion())
    OR_14.Add(InvasionPending())
    AND_14.Add(OR_14)
    AND_14.Add(FlagEnabled(flag))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(not OR_7)
    OR_15.Add(Invasion())
    OR_15.Add(InvasionPending())
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag))
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_15.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_9.Add(not AND_11)
    AND_9.Add(not AND_12)
    AND_9.Add(not AND_13)
    AND_9.Add(not AND_14)
    AND_9.Add(not AND_15)
    
    MAIN.Await(AND_9)
    
    Restart()


@RestartOnRest(31002873)
def Event_31002873(
    _,
    flag: uint,
    bgm_boss_conv_param_id: int,
    flag_1: uint,
    flag_2: uint,
    right: uint,
    flag_3: uint,
    left: int,
    left_1: int,
):
    """Event 31002873"""
    if FlagDisabled(3691):
        return
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Start)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Stop2)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Stop1)


@RestartOnRest(31002845)
def Event_31002845():
    """Event 31002845"""
    GotoIfFlagEnabled(Label.L2, flag=3863)
    GotoIfFlagDisabled(Label.L0, flag=31000800)
    AND_1.Add(FlagEnabled(31000800))
    AND_1.Add(FlagDisabled(3691))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagDisabled(31000850))
    AND_2.Add(FlagEnabled(3691))
    GotoIfConditionTrue(Label.L3, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L4, flag=31000850)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(31000845)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(31000845)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableFlag(31000845)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 31000800))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 31000850))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3691))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 3683))
    
    MAIN.Await(OR_15)
    
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(31002875)
def Event_31002875():
    """Event 31002875"""
    GotoIfFlagEnabled(Label.L0, flag=3691)
    EnableAsset(Assets.AEG099_630_9001)
    if FlagDisabled(31008521):
        EnableAssetActivation(Assets.AEG099_630_9001, obj_act_id=200)
    DisableAsset(Assets.AEG099_630_9002)
    DisableAssetActivation(Assets.AEG099_630_9002, obj_act_id=200)
    DisableTreasure(asset=Assets.AEG099_630_9002)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG099_630_9001)
    DisableAssetActivation(Assets.AEG099_630_9001, obj_act_id=200)
    DisableTreasure(asset=Assets.AEG099_630_9001)
    EnableAsset(Assets.AEG099_630_9002)
    if FlagDisabled(31008523):
        EnableAssetActivation(Assets.AEG099_630_9002, obj_act_id=200)


@RestartOnRest(31002876)
def Event_31002876(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    asset: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 31002876"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(asset):
        DeleteAssetVFX(asset, erase_root=False)
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        CreateAssetVFX(asset, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9290, entity=asset))
    
    MAIN.Await(AND_2)
    
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(31003700)
def Event_31003700(_, character: uint):
    """Event 31003700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3686)
    AND_1.Add(FlagEnabled(3685))
    AND_1.Add(FlagEnabled(31000800))
    AND_1.Add(FlagDisabled(31002704))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3686))
    AND_3.Add(FlagEnabled(3685))
    AND_3.Add(FlagEnabled(31000800))
    AND_3.Add(FlagDisabled(31002704))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=31002714)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3686))
    AND_4.Add(FlagEnabled(3685))
    AND_4.Add(FlagEnabled(31000800))
    AND_4.Add(FlagDisabled(31002704))
    OR_4.Add(AND_4)
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(31003701)
def Event_31003701(_, character: uint, flag: uint, flag_1: uint, character_1: uint):
    """Event 31003701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    if AND_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=3681)
    GotoIfFlagEnabled(Label.L2, flag=3686)
    GotoIfFlagDisabled(Label.L2, flag=31002704)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3681))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=5.0))
    
    MAIN.Await(AND_3)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character_1)
    ReplanAI(character_1)
    End()


@RestartOnRest(31003702)
def Event_31003702(_, character: uint):
    """Event 31003702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3685):
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagEnabled(31008521))
    AND_1.Add(FlagEnabled(31002805))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=character, distance=50.0)
    End()


@RestartOnRest(31003703)
def Event_31003703():
    """Event 31003703"""
    if FlagEnabled(3683):
        return
    if FlagEnabled(31000800):
        return
    DisableFlag(31009810)
    DisableFlag(31009215)
    DisableFlag(31009214)
    DisableFlag(31009217)
    WaitFrames(frames=1)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3682)
    
    MAIN.Await(FlagEnabled(31000800))
    
    DisableFlag(31009219)
    End()


@RestartOnRest(31003704)
def Event_31003704(_, character: uint, seconds: float):
    """Event 31003704"""
    WaitFrames(frames=1)
    if FlagDisabled(3685):
        return
    if FlagEnabled(3683):
        return
    if FlagEnabled(31000800):
        return
    GotoIfFlagEnabled(Label.L2, flag=31002713)
    if FlagDisabled(31002704):
        DisableFlag(31009811)
    GotoIfFlagEnabled(Label.L1, flag=31002704)
    EnableImmortality(character)
    
    MAIN.Await(HealthRatio(character) <= 0.5)
    
    DisableImmortality(character)
    if FlagEnabled(3683):
        return
    EnableFlag(31002704)
    EnableFlag(31009811)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9701)
    AddSpecialEffect(character, 5005)
    AddSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9645)
    if PlayerInOwnWorld():
        RemoveSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9647)
    AddSpecialEffect(character, 9642)
    SetTeamType(character, TeamType.FriendlyNPC)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    OR_3.Add(FlagEnabled(31002713))
    
    MAIN.Await(OR_3)
    
    GotoIfFlagEnabled(Label.L2, flag=31002713)
    if FlagEnabled(3683):
        return
    SkipLinesIfFinishedConditionTrue(1, input_condition=OR_2)
    Restart()
    EnableFlag(31009215)
    EnableFlag(31009810)
    DisableFlag(31009201)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    SetCharacterTalkRange(character=character, distance=17.0)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60819):
        return
    AND_10.Add(CharacterDead(character, target_comparison_type=ComparisonType.NotEqual))
    AND_10.Add(FlagEnabled(31000800))
    
    MAIN.Await(AND_10)
    
    EnableFlag(60819)
    AwardGesture(gesture_param_id=41)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    AddSpecialEffect(character, 9704)
    AddSpecialEffect(character, 9644)
    AddSpecialEffect(character, 9643)
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003705)
def Event_31003705(_, character: uint):
    """Event 31003705"""
    GotoIfPlayerNotInOwnWorld(Label.L1)
    WaitFrames(frames=1)
    if FlagDisabled(3685):
        return
    if FlagEnabled(3683):
        return
    if FlagEnabled(31000800):
        return
    DisableFlag(31009212)
    DisableFlag(31009211)
    DisableFlag(31009213)
    AND_1.Add(FlagEnabled(31002703))
    AND_1.Add(FlagDisabled(3683))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(2.5)
    if FlagEnabled(31000800):
        return
    WaitFrames(frames=1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagDisabled(3683))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    if FlagEnabled(31000800):
        return
    WaitFrames(frames=1)
    AND_10.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_10.Add(FlagDisabled(3683))
    AND_10.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_10)
    
    if FlagEnabled(31000800):
        return
    WaitFrames(frames=1)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_3.Add(FlagDisabled(3683))
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(31000800):
        return
    EnableNetworkFlag(31002713)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(31002713))
    
    if FlagEnabled(31000800):
        return
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003706)
def Event_31003706(_, character: uint, flag: uint, first_flag: uint, last_flag: uint):
    """Event 31003706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(31000800):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(3685))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(31002714)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()


@RestartOnRest(31003707)
def Event_31003707():
    """Event 31003707"""
    WaitFrames(frames=1)
    OR_10.Add(FlagEnabled(3685))
    OR_10.Add(FlagEnabled(3691))
    OR_10.Add(FlagEnabled(3692))
    OR_10.Add(FlagEnabled(3694))
    SkipLinesIfConditionFalse(3, OR_10)
    DisableAsset(Assets.AEG099_520_9000)
    DisableAssetActivation(Assets.AEG099_520_9000, obj_act_id=200)
    End()
    EnableAsset(Assets.AEG099_520_9000)
    EnableAssetActivation(Assets.AEG099_520_9000, obj_act_id=200)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(31008522):
        DisableAssetActivation(Assets.AEG099_520_9000, obj_act_id=200)
        End()
    
    MAIN.Await(FlagEnabled(31008522))
    
    CreateTemporaryVFX(
        vfx_id=806881,
        anchor_entity=Assets.AEG099_520_9000,
        model_point=90,
        anchor_type=CoordEntityType.Asset,
    )
    CreateTemporaryVFX(
        vfx_id=806882,
        anchor_entity=Assets.AEG099_520_9000,
        model_point=90,
        anchor_type=CoordEntityType.Asset,
    )
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=True, freeze_player_delay=0.0)
    Wait(2.200000047683716)
    AND_1.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(2.799999952316284)
    AND_2.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_2)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=0.0)
    GotoIfFlagEnabled(Label.L1, flag=3683)
    GotoIfFlagDisabled(Label.L1, flag=3686)
    GotoIfFlagEnabled(Label.L2, flag=31009231)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=EAST_LIMGRAVE_SW_NE, player_start=1045372710)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=31000001,
        cutscene_flags=0,
        move_to_region=1045372710,
        map_id=60453700,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=True,
    )
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=31000000,
        cutscene_flags=0,
        move_to_region=1045372710,
        map_id=60453700,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=True,
    )
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=0.0)
    End()


@RestartOnRest(31003709)
def Event_31003709():
    """Event 31003709"""
    DisableCharacter(31000702)
    DisableCharacter(Characters.Patches3)
    DisableBackread(31000702)
    DisableBackread(Characters.Patches3)
    End()


@RestartOnRest(31003710)
def Event_31003710(_, character: uint):
    """Event 31003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3692)
    GotoIfFlagEnabled(Label.L5, flag=3694)
    AND_1.Add(FlagEnabled(3691))
    AND_1.Add(FlagEnabled(31000850))
    AND_1.Add(FlagEnabled(3683))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3692))
    OR_3.Add(FlagEnabled(3694))
    AND_3.Add(FlagEnabled(3691))
    AND_3.Add(FlagEnabled(31000850))
    AND_3.Add(FlagEnabled(3683))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=31002723)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3692))
    OR_4.Add(FlagEnabled(3694))
    AND_4.Add(FlagEnabled(3691))
    AND_4.Add(FlagEnabled(31000850))
    AND_4.Add(FlagEnabled(3683))
    OR_4.Add(AND_4)
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(31003711)
def Event_31003711(_, character: uint, flag: uint, flag_1: uint, character_1: uint):
    """Event 31003711"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagDisabled(3691))
    AND_1.Add(FlagDisabled(3692))
    AND_1.Add(FlagDisabled(3694))
    if AND_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=3681)
    GotoIfFlagEnabled(Label.L2, flag=3686)
    GotoIfFlagDisabled(Label.L2, flag=31002727)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3681))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=5.0))
    
    MAIN.Await(AND_3)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character_1)
    ReplanAI(character_1)
    End()


@RestartOnRest(31003712)
def Event_31003712():
    """Event 31003712"""
    if PlayerInOwnWorld():
        EnableFlag(31002715)
    End()


@RestartOnRest(31003713)
def Event_31003713(_, character: uint):
    """Event 31003713"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(3691):
        return
    if FlagEnabled(3683):
        return
    GotoIfFlagEnabled(Label.L1, flag=31000850)
    DisableFlag(31009889)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3682)
    SaveRequest()
    AND_1.Add(FlagEnabled(31008523))
    AND_1.Add(FlagEnabled(31002855))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=character, distance=50.0)
    
    MAIN.Await(FlagEnabled(31000850))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(31009269)
    End()


@RestartOnRest(31003714)
def Event_31003714(_, character: uint, seconds: float):
    """Event 31003714"""
    WaitFrames(frames=1)
    if FlagDisabled(3691):
        return
    if FlagEnabled(3683):
        return
    if FlagEnabled(31000850):
        return
    GotoIfFlagEnabled(Label.L2, flag=31002722)
    GotoIfFlagEnabled(Label.L1, flag=31002730)
    EnableImmortality(character)
    AND_5.Add(FlagEnabled(31009257))
    
    MAIN.Await(AND_5)
    
    GotoIfFlagEnabled(Label.L5, flag=31002855)
    
    MAIN.Await(FlagEnabled(31002855))

    # --- Label 5 --- #
    DefineLabel(5)
    Wait(3.0)
    DisableImmortality(character)
    AddSpecialEffect(character, 18670)
    if FlagEnabled(3683):
        return
    EnableFlag(31002721)
    
    MAIN.Await(FlagEnabled(31002730))

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    AddSpecialEffect(character, 9701)
    AddSpecialEffect(character, 5005)
    AddSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9645)
    if PlayerInOwnWorld():
        RemoveSpecialEffect(character, 9703)
    AddSpecialEffect(character, 9647)
    AddSpecialEffect(character, 9642)
    SetTeamType(character, TeamType.FriendlyNPC)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    OR_3.Add(FlagEnabled(31002722))
    
    MAIN.Await(OR_3)
    
    GotoIfFlagEnabled(Label.L2, flag=31002722)
    if FlagEnabled(3683):
        return
    SkipLinesIfFinishedConditionTrue(1, input_condition=OR_2)
    Restart()
    EnableFlag(31002728)
    EnableFlag(31009889)
    DisableFlag(31009201)
    AddSpecialEffect(character, 9706)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    SetCharacterTalkRange(character=character, distance=17.0)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60832):
        return
    AND_10.Add(CharacterDead(character, target_comparison_type=ComparisonType.NotEqual))
    AND_10.Add(FlagEnabled(31000850))
    
    MAIN.Await(AND_10)
    
    EnableFlag(60832)
    AwardGesture(gesture_param_id=90)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFramesAfterCutscene(frames=1)
    AddSpecialEffect(character, 9702)
    AddSpecialEffect(character, 5006)
    AddSpecialEffect(character, 9704)
    AddSpecialEffect(character, 9644)
    AddSpecialEffect(character, 9706)
    AddSpecialEffect(character, 9643)
    SetTeamType(character, TeamType.Enemy)
    End()


@RestartOnRest(31003715)
def Event_31003715(_, attacked_entity: uint):
    """Event 31003715"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(3691):
        return
    if FlagEnabled(3683):
        return
    if FlagEnabled(31000850):
        return
    AND_1.Add(FlagEnabled(31002720))
    AND_1.Add(FlagDisabled(3683))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(2.5)
    if FlagEnabled(31000850):
        return
    WaitFrames(frames=1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    AND_2.Add(FlagDisabled(3683))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    if FlagEnabled(31000850):
        return
    WaitFrames(frames=1)
    AND_10.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    AND_10.Add(FlagDisabled(3683))
    AND_10.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_10)
    
    if FlagEnabled(31000850):
        return
    WaitFrames(frames=1)
    AND_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    AND_3.Add(FlagDisabled(3683))
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(31000850):
        return
    EnableNetworkFlag(31002722)
    End()


@RestartOnRest(31003716)
def Event_31003716(_, character: uint, flag: uint, first_flag: uint, last_flag: uint):
    """Event 31003716"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(31000800):
        return
    if FlagEnabled(31000850):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(3691))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(31002723)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
