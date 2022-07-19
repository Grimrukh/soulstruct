"""
Southwest Mountaintops (NW) (NE)

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
from .entities.m60_49_55_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049550000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76652,
        flag_1=76651,
        asset=Assets.AEG099_090_9000,
        source_flag=77520,
        value=1,
        flag_2=78520,
        flag_3=78521,
        flag_4=78522,
        flag_5=78523,
        flag_6=78524,
        flag_7=78525,
        flag_8=78526,
        flag_9=78527,
        flag_10=78528,
        flag_11=78529,
    )
    Event_1049552210(0, character=Characters.WanderingNoble3)
    Event_1049552210(1, character=Characters.WanderingNoble7)
    Event_1049552210(2, character=Characters.WanderingNoble8)
    Event_1049552200(0, attacker__character=1049555200, region=1049552200)
    Event_1049552500()
    Event_1049552550(0, character=Characters.WanderingNoble6, asset=Assets.AEG099_390_9052)
    Event_1049552550(1, character=Characters.WanderingNoble2, asset=Assets.AEG099_390_9056)
    Event_1049552550(2, character=Characters.WanderingNoble11, asset=Assets.AEG099_390_9006)
    CommonFunc_90005683(0, flag=62512, asset=Assets.AEG099_057_1000, vfx_id=211, flag_1=78594, flag_2=0)
    Event_1049552400(
        0,
        flag=1049550405,
        flag_1=1049552405,
        anchor_entity=Characters.WanderingNoble9,
        character=Characters.Runebear,
        left=1,
        item_lot_param_id=1049550700,
    )
    Event_1049552401(
        0,
        flag=1049550405,
        flag_1=1049552405,
        character=Characters.WanderingNoble9,
        character_1=Characters.Runebear,
        left=1,
    )
    Event_1049552410(0, character=Characters.WanderingNoble9)
    Event_1049552420(
        0,
        character=Characters.WanderingNoble12,
        animation_id=30000,
        animation_id_1=20000,
        region=0,
        radius=0.800000011920929,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005706(0, 1049550710, 930023, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1049550700)
    DisableBackread(Characters.WanderingNoble10)


@RestartOnRest(1049552200)
def Event_1049552200(_, attacker__character: uint, region: uint):
    """Event 1049552200"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1049552200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1049552200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(1049552210)
def Event_1049552210(_, character: uint):
    """Event 1049552210"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
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
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    
    MAIN.Await(OR_1)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableAI(character)


@RestartOnRest(1049552400)
def Event_1049552400(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 1049552400"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 4305)
    Wait(3.0)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if ValueNotEqual(left=item_lot_param_id, right=0):
        AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(1049552401)
def Event_1049552401(_, flag: uint, flag_1: uint, character: uint, character_1: uint, left: int):
    """Event 1049552401"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableGravity(character_1)
    DisableAI(character_1)
    SetCharacterFadeOnEnable(character=character_1, state=True)
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, True)
    SetBackreadStateAlternate(character_1, True)
    Wait(0.800000011920929)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    Wait(0.5)
    AddSpecialEffect(character, 4305)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=601101, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=601100, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    DisableCharacter(character)
    SetBackreadStateAlternate(character, False)
    SetBackreadStateAlternate(character_1, False)
    TriggerAISound(ai_sound_param_id=6410, anchor_entity=1049552400, unk_8_12=1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_1)


@RestartOnRest(1049552410)
def Event_1049552410(_, character: uint):
    """Event 1049552410"""
    if FlagEnabled(1049540405):
        return
    DisableGravity(character)
    DisableAI(character)
    ForceAnimation(character, 30006, loop=True)


@RestartOnRest(1049552420)
def Event_1049552420(
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
):
    """Event 1049552420"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if FlagEnabled(1049550405):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        EnableCharacterCollision(character)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.WanderingNoble9, attacker=0))
    OR_3.Add(CharacterHasStateInfo(character=Characters.WanderingNoble9, state_info=436))
    OR_3.Add(CharacterHasStateInfo(character=Characters.WanderingNoble9, state_info=2))
    OR_3.Add(CharacterHasStateInfo(character=Characters.WanderingNoble9, state_info=5))
    OR_3.Add(CharacterHasStateInfo(character=Characters.WanderingNoble9, state_info=6))
    OR_3.Add(CharacterHasStateInfo(character=Characters.WanderingNoble9, state_info=260))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
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
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    End()


@RestartOnRest(1049552500)
def Event_1049552500():
    """Event 1049552500"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1049552500))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    TriggerAISound(ai_sound_param_id=6410, anchor_entity=1049552501, unk_8_12=1)


@RestartOnRest(1049552550)
def Event_1049552550(_, character: uint, asset: uint):
    """Event 1049552550"""
    AttachAssetToCharacter(character=character, model_point=72, asset=asset)
