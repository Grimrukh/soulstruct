"""
m41_02_00_00

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
    CommonFunc_90005646(
        0,
        flag=41020800,
        left_flag=41022890,
        cancel_flag__right_flag=41022891,
        asset=41021890,
        player_start=41022890,
        area_id=41,
        block_id=2,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=41021500, dummy_id=100, vfx_id=800, right=0)
    RegisterGrace(grace_flag=41020000, asset=41021950, enemy_block_distance=8.0)
    Event_41022800()
    Event_41022810()
    Event_41022811()
    Event_41022849()
    Event_41022815()
    Event_41022831()
    Event_41022830()
    Event_41022852()
    Event_41022833()
    Event_41022840(0, character=41020800)
    Event_41022840(1, character=41020810)
    Event_41022840(2, character=41020811)
    Event_41022840(3, character=41020812)
    Event_41022840(4, character=41020813)
    Event_41022840(5, character=41020814)
    Event_41022840(6, character=41020815)
    Event_41022840(7, character=41020816)
    Event_41022840(8, character=41020817)
    Event_41022860(0, character=41020810)
    Event_41022860(1, character=41020811)
    Event_41022860(2, character=41020812)
    Event_41022860(3, character=41020813)
    Event_41022860(4, character=41020814)
    Event_41022860(5, character=41020815)
    Event_41022860(6, character=41020816)
    Event_41022860(7, character=41020817)
    Event_41022870()
    Event_41022871()
    Event_41022851()
    Event_41020510(0, asset=41021510)
    CommonFunc_90005510(
        0,
        flag=41028560,
        asset=41021560,
        obj_act_id=41023560,
        obj_act_id_1=449008,
        text=20208005,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=41028562,
        asset=41021562,
        obj_act_id=41023562,
        obj_act_id_1=1449008,
        text=20208006,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=41028564,
        asset=41021564,
        obj_act_id=41023564,
        obj_act_id_1=1449008,
        text=20208006,
        left=0,
    )
    Event_41022580()
    CommonFunc_90005525(0, flag=41020600, asset=41021600)
    CommonFunc_90005706(0, character=41020700, animation_id=30022, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=41020200, region=41022200, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41020203, region=41022203, radius=1.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(0, character=41020201, region=41022201, radius=1.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005261(0, character=41020204, region=41022204, radius=1.0, seconds=0.0, animation_id=-1)
    Event_41022220(
        0,
        character=41020220,
        animation_id=30001,
        region=41022220,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=41022223,
        region_2=41022221,
    )
    CommonFunc_90005221(0, character=41020221, animation_id=30001, animation_id_1=-1, seconds=0.0, left=0)
    Event_41022220(
        1,
        character=41020222,
        animation_id=30001,
        region=41022220,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        region_1=41022222,
        region_2=41022221,
    )
    CommonFunc_90005201(
        0,
        character=41020205,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=41020206,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=41020207,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41020208, region=41022208, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=41020209,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=41020210,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41020211, region=41022216, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=41020212, region=41022212, radius=1.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005201(
        0,
        character=41020213,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41020216,
        animation_id=30000,
        animation_id_1=20000,
        region=41022216,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41020217,
        animation_id=30001,
        animation_id_1=20001,
        region=41022216,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41020218,
        animation_id=30002,
        animation_id_1=20002,
        region=41022216,
        radius=1.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=41020219, region=41022216, radius=5.0, seconds=0.0, animation_id=0)
    CommonFunc_90005445(
        0,
        character=41020240,
        animation_id=30001,
        animation_id_1=20001,
        region=41022240,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021240,
    )
    CommonFunc_90005261(0, character=41020242, region=41022242, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005446(
        0,
        character=41020243,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021243,
    )
    CommonFunc_90005211(
        0,
        character=41020245,
        animation_id=30000,
        animation_id_1=20000,
        region=41022245,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005445(
        0,
        character=41020241,
        animation_id=30001,
        animation_id_1=20001,
        region=41022241,
        seconds=2.4000000953674316,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021241,
    )
    Event_41022240(
        1,
        character=41020241,
        animation_id=30001,
        animation_id_1=20001,
        region=41022562,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021241,
        flag=41027320,
    )
    CommonFunc_90005445(
        0,
        character=41020244,
        animation_id=30001,
        animation_id_1=20001,
        region=41022244,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021244,
    )
    Event_41022240(
        4,
        character=41020244,
        animation_id=30001,
        animation_id_1=20001,
        region=41022562,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=41021244,
        flag=41027320,
    )
    CommonFunc_90005261(0, character=41020249, region=41022249, radius=1.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(0, character=41020300, region=41022300, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=41020262,
        animation_id=30002,
        animation_id_1=20002,
        region=41022262,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=41020263,
        animation_id=30000,
        animation_id_1=20000,
        region=41022263,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=41020264, radius=7.0, seconds=0.0, animation_id=1703)
    CommonFunc_90005221(0, character=41020286, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020287, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020288, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020289, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020290, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020291, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020292, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=41020293, animation_id=30022, animation_id_1=20052, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=41020352, region=41022352, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=41020353, region=41022352, radius=1.0, seconds=1.2999999523162842, animation_id=0)
    CommonFunc_90005261(0, character=41020357, region=41022357, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=41020380, region=41022380, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=41020381, region=41022357, radius=1.0, seconds=2.200000047683716, animation_id=0)


@RestartOnRest(41022220)
def Event_41022220(
    _,
    character: uint,
    animation_id: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    region_1: uint,
    region_2: uint,
):
    """Event 41022220"""
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
    ForceAnimation(character, 20017, wait_for_completion=True)
    if UnsignedNotEqual(left=region_2, right=0):
        FaceEntityAndForceAnimation(character, region_2, animation=20018)
        ForceAnimation(character, 20018, loop=True, skip_transition=True)
    
        MAIN.Await(CharacterInsideRegion(character=character, region=region_2))
    FaceEntityAndForceAnimation(character, region_1, animation=20018)
    ForceAnimation(character, 20018, loop=True, skip_transition=True)
    OR_10.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_10)
    
    ForceAnimation(character, 20019, loop=True, wait_for_completion=True)
    ForceAnimation(character, 30016, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(41022240)
def Event_41022240(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: Asset | int,
    flag: Flag | int,
):
    """Event 41022240"""
    if SpecialStandbyEndedFlagEnabled(character=character):
        DisableAsset(asset)
        End()
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    EnableAssetInvulnerability(asset)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    AND_9.Add(OR_2)
    AND_9.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_9)
    
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
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(41020510)
def Event_41020510(_, asset: Asset | int):
    """Event 41020510"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(AssetDestroyed(asset))
    
    EnableThisNetworkSlotFlag()
    End()


@RestartOnRest(41022550)
def Event_41022550(_, character: Character | int, asset: Asset | int):
    """Event 41022550"""
    if ThisEventSlotFlagEnabled():
        return
    EnableAssetInvulnerability(asset)
    AND_1.Add(SpecialStandbyEndedFlagEnabled(character=character))
    
    MAIN.Await(AND_1)
    
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset)


@ContinueOnRest(41022580)
def Event_41022580():
    """Event 41022580"""
    RegisterLadder(start_climbing_flag=41020580, stop_climbing_flag=41020581, asset=41021580)
    RegisterLadder(start_climbing_flag=41020582, stop_climbing_flag=41020583, asset=41021582)
    RegisterLadder(start_climbing_flag=41020584, stop_climbing_flag=41020585, asset=41021584)


@RestartOnRest(41022800)
def Event_41022800():
    """Event 41022800"""
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(HealthValue(41020800) <= 0)
    
    Kill(41020810)
    Kill(41020811)
    Kill(41020812)
    Kill(41020813)
    Kill(41020814)
    Kill(41020815)
    Kill(41020816)
    Kill(41020817)
    RemoveSpecialEffect(PLAYER, 19701)
    RemoveSpecialEffect(PLAYER, 19702)
    RemoveSpecialEffect(PLAYER, 19703)
    RemoveSpecialEffect(PLAYER, 19704)
    RemoveSpecialEffect(PLAYER, 19705)
    RemoveSpecialEffect(PLAYER, 19706)
    RemoveSpecialEffect(PLAYER, 19707)
    Wait(4.0)
    PlaySoundEffect(41020800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(41020800))
    
    KillBossAndDisplayBanner(character=41020800, banner_type=BannerType.EnemyFelled)
    EnableFlag(41020800)
    EnableFlag(9277)
    if PlayerInOwnWorld():
        EnableFlag(61277)


@RestartOnRest(41022810)
def Event_41022810():
    """Event 41022810"""
    GotoIfFlagDisabled(Label.L0, flag=41020800)
    DisableCharacter(41020800)
    DisableAnimations(41020800)
    Kill(41020800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(41020800)
    DisableHealthBar(41020810)
    DisableHealthBar(41020811)
    DisableHealthBar(41020812)
    DisableHealthBar(41020813)
    DisableHealthBar(41020814)
    DisableHealthBar(41020815)
    DisableHealthBar(41020816)
    DisableHealthBar(41020817)
    DisableFlag(41022835)
    DisableFlag(41022836)
    DisableFlag(41022837)
    GotoIfFlagEnabled(Label.L1, flag=41020801)
    AND_2.Add(FlagEnabled(41022805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=41022800))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(41020801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(41022805))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=41022800))
    
    MAIN.Await(AND_3)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(41020800)
    SetNetworkUpdateRate(41020800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(41020800, name=142700)


@RestartOnRest(41022811)
def Event_41022811():
    """Event 41022811"""
    if FlagEnabled(41020800):
        return
    AND_1.Add(CharacterHasSpecialEffect(41020800, 20018688))
    
    MAIN.Await(AND_1)
    
    EnableFlag(41022802)


@RestartOnRest(41022815)
def Event_41022815():
    """Event 41022815"""
    if FlagEnabled(41020800):
        return
    AND_1.Add(CharacterHasSpecialEffect(41020800, 20018016))
    AND_1.Add(CharacterDead(41020810))
    AND_1.Add(CharacterDead(41020811))
    AND_1.Add(CharacterDead(41020812))
    AND_1.Add(CharacterDead(41020813))
    AND_1.Add(CharacterDead(41020814))
    AND_1.Add(CharacterDead(41020815))
    AND_1.Add(CharacterDead(41020816))
    AND_1.Add(CharacterDead(41020817))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(41020800, 20018653))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=41022820)
    GotoIfFlagEnabled(Label.L1, flag=41022821)
    GotoIfFlagEnabled(Label.L2, flag=41022822)
    GotoIfFlagEnabled(Label.L3, flag=41022823)
    GotoIfFlagEnabled(Label.L4, flag=41022824)
    GotoIfFlagEnabled(Label.L5, flag=41022825)
    GotoIfFlagEnabled(Label.L6, flag=41022826)
    GotoIfFlagEnabled(Label.L7, flag=41022827)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022880)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022881)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022882)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022883)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022884)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022885)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020816, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020817)
    EnableAI(41020817)
    EnableFlag(41022886)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024810)
    ForceSpawnerToSpawn(spawner=41024817)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020817, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020817, 61020)
    Move(41020800, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableCharacter(41020810)
    EnableAI(41020810)
    EnableCharacter(41020811)
    EnableAI(41020811)
    EnableCharacter(41020812)
    EnableAI(41020812)
    EnableCharacter(41020813)
    EnableAI(41020813)
    EnableCharacter(41020814)
    EnableAI(41020814)
    EnableCharacter(41020815)
    EnableAI(41020815)
    EnableCharacter(41020816)
    EnableAI(41020816)
    EnableFlag(41022887)
    ForceSpawnerToSpawn(spawner=41024811)
    ForceSpawnerToSpawn(spawner=41024812)
    ForceSpawnerToSpawn(spawner=41024813)
    ForceSpawnerToSpawn(spawner=41024814)
    ForceSpawnerToSpawn(spawner=41024815)
    ForceSpawnerToSpawn(spawner=41024816)
    ForceSpawnerToSpawn(spawner=41024810)
    Move(41020810, destination=41022810, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020811, destination=41022811, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020812, destination=41022812, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020813, destination=41022813, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020814, destination=41022814, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020815, destination=41022815, destination_type=CoordEntityType.Region, short_move=True)
    Move(41020816, destination=41022816, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020810, 61020)
    ForceAnimation(41020811, 61020)
    ForceAnimation(41020812, 61020)
    ForceAnimation(41020813, 61020)
    ForceAnimation(41020814, 61020)
    ForceAnimation(41020815, 61020)
    ForceAnimation(41020816, 61020)
    Move(41020800, destination=41022817, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(41020800, 61020)
    WaitRealFrames(frames=1)
    DisableFlag(41022832)
    Restart()


@RestartOnRest(41022830)
def Event_41022830():
    """Event 41022830"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(FlagDisabled(41022832))
    
    GotoIfFlagEnabled(Label.L0, flag=41022820)
    GotoIfFlagEnabled(Label.L1, flag=41022821)
    GotoIfFlagEnabled(Label.L2, flag=41022822)
    GotoIfFlagEnabled(Label.L3, flag=41022823)
    GotoIfFlagEnabled(Label.L4, flag=41022824)
    GotoIfFlagEnabled(Label.L5, flag=41022825)
    GotoIfFlagEnabled(Label.L6, flag=41022826)
    GotoIfFlagEnabled(Label.L7, flag=41022827)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(41022820)
    EnableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(41022820)
    DisableFlag(41022821)
    EnableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    EnableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    EnableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    EnableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    EnableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    EnableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(41022820)
    DisableFlag(41022821)
    DisableFlag(41022822)
    DisableFlag(41022823)
    DisableFlag(41022824)
    DisableFlag(41022825)
    DisableFlag(41022826)
    DisableFlag(41022827)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(41022831)
def Event_41022831():
    """Event 41022831"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(41020800):
        return
    WaitUnknown_1001_7(unk1=40, unk2=119)
    EnableFlag(41022832)
    WaitRealFrames(frames=1)
    GotoIfFlagEnabled(Label.L0, flag=41022821)
    GotoIfFlagEnabled(Label.L1, flag=41022822)
    GotoIfFlagEnabled(Label.L2, flag=41022823)
    GotoIfFlagEnabled(Label.L3, flag=41022824)
    GotoIfFlagEnabled(Label.L4, flag=41022825)
    GotoIfFlagEnabled(Label.L5, flag=41022826)
    GotoIfFlagEnabled(Label.L6, flag=41022827)
    GotoIfFlagEnabled(Label.L7, flag=41022820)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkFlag(41022820)
    EnableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    EnableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    EnableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    EnableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    EnableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    EnableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 6 --- #
    DefineLabel(6)
    DisableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    EnableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 7 --- #
    DefineLabel(7)
    EnableNetworkFlag(41022820)
    DisableNetworkFlag(41022821)
    DisableNetworkFlag(41022822)
    DisableNetworkFlag(41022823)
    DisableNetworkFlag(41022824)
    DisableNetworkFlag(41022825)
    DisableNetworkFlag(41022826)
    DisableNetworkFlag(41022827)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagDisabled(41022832))
    
    Restart()


@RestartOnRest(41022852)
def Event_41022852():
    """Event 41022852"""
    if FlagEnabled(41020800):
        return
    OR_1.Add(CharacterHasSpecialEffect(41020800, 20018654))
    OR_1.Add(CharacterHasSpecialEffect(41020800, 20018639))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(41022852):
        EnableFlag(41022852)
        WaitRealFrames(frames=10)
        Restart()
    SkipLinesIfFlagEnabled(2, 41022880)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020810, special_effect=20018040)
    Kill(41020810)
    SkipLinesIfFlagEnabled(2, 41022881)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020811, special_effect=20018040)
    Kill(41020811)
    SkipLinesIfFlagEnabled(2, 41022882)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020812, special_effect=20018040)
    Kill(41020812)
    SkipLinesIfFlagEnabled(2, 41022883)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020813, special_effect=20018040)
    Kill(41020813)
    SkipLinesIfFlagEnabled(2, 41022884)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020814, special_effect=20018040)
    Kill(41020814)
    SkipLinesIfFlagEnabled(2, 41022885)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020815, special_effect=20018040)
    Kill(41020815)
    SkipLinesIfFlagEnabled(2, 41022886)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020816, special_effect=20018040)
    Kill(41020816)
    SkipLinesIfFlagEnabled(2, 41022887)
    SkipLinesIfCharacterHasSpecialEffect(1, character=41020817, special_effect=20018040)
    Kill(41020817)
    WaitRealFrames(frames=1)
    DisableFlag(41022880)
    DisableFlag(41022881)
    DisableFlag(41022882)
    DisableFlag(41022883)
    DisableFlag(41022884)
    DisableFlag(41022885)
    DisableFlag(41022886)
    DisableFlag(41022887)
    Wait(1.0)
    Restart()


@RestartOnRest(41022833)
def Event_41022833():
    """Event 41022833"""
    DisableNetworkSync()
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 1)
    
    AddSpecialEffect(ALL_PLAYERS, 19701)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 2)
    
    AddSpecialEffect(ALL_PLAYERS, 19702)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 3)
    
    AddSpecialEffect(ALL_PLAYERS, 19703)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 4)
    
    AddSpecialEffect(ALL_PLAYERS, 19704)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 5)
    
    AddSpecialEffect(ALL_PLAYERS, 19705)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 6)
    
    AddSpecialEffect(ALL_PLAYERS, 19706)
    
    MAIN.Await(EventValue(flag=41022835, bit_count=3) >= 7)
    
    AddSpecialEffect(ALL_PLAYERS, 19700)


@RestartOnRest(41022840)
def Event_41022840(_, character: Character | int):
    """Event 41022840"""
    DisableNetworkSync()
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 20018017))
    
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=41022100))
    SkipLinesIfConditionTrue(1, AND_1)
    IncrementEventValue(41022835, bit_count=3, max_value=7)
    Wait(1.0)
    Restart()


@RestartOnRest(41022849)
def Event_41022849():
    """Event 41022849"""
    CommonFunc_9005800(
        0,
        flag=41020800,
        entity=41021800,
        region=41022800,
        flag_1=41022805,
        character=41025800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=41020800,
        entity=41021800,
        region=41022800,
        flag_1=41022805,
        flag_2=41022806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=41020800, asset=41021800, vfx_id=4, right=0)
    CommonFunc_9005822(
        0,
        flag=41020800,
        bgm_boss_conv_param_id=941000,
        flag_1=41022805,
        flag_2=41022806,
        right=0,
        flag_3=41022802,
        left=0,
        left_1=0,
    )


@RestartOnRest(41022860)
def Event_41022860(_, character: Character | int):
    """Event 41022860"""
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 20018022))
    
    Move(character, destination=41022860, destination_type=CoordEntityType.Region, short_move=True)
    DisableCharacter(character)
    DisableAI(character)
    WaitRealFrames(frames=10)
    Restart()


@RestartOnRest(41022851)
def Event_41022851():
    """Event 41022851"""
    if FlagEnabled(41020800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(41020800, 20018648))
    
    Move(41020800, destination=41022860, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=10)
    Restart()


@RestartOnRest(41022870)
def Event_41022870():
    """Event 41022870"""
    if FlagEnabled(41020800):
        return
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(CharacterHasSpecialEffect(41020800, 20018016))
    OR_1.Add(CharacterHasSpecialEffect(41020800, 20018653))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AND_2.Add(HealthRatio(41020800) <= 1.0)
    AND_2.Add(HealthRatio(41020800) >= 0.800000011920929)
    SkipLinesIfConditionFalse(3, AND_2)
    AddSpecialEffect(41020800, 20018630)
    Wait(1.0)
    Restart()
    AND_3.Add(HealthRatio(41020800) < 0.800000011920929)
    AND_3.Add(HealthRatio(41020800) >= 0.699999988079071)
    SkipLinesIfConditionFalse(3, AND_3)
    AddSpecialEffect(41020800, 20018631)
    Wait(1.0)
    Restart()
    AND_4.Add(HealthRatio(41020800) < 0.699999988079071)
    AND_4.Add(HealthRatio(41020800) >= 0.6000000238418579)
    SkipLinesIfConditionFalse(3, AND_4)
    AddSpecialEffect(41020800, 20018632)
    Wait(1.0)
    Restart()
    AND_5.Add(HealthRatio(41020800) < 0.6000000238418579)
    AND_5.Add(HealthRatio(41020800) >= 0.5)
    SkipLinesIfConditionFalse(3, AND_5)
    AddSpecialEffect(41020800, 20018633)
    Wait(1.0)
    Restart()
    AND_6.Add(HealthRatio(41020800) < 0.5)
    AND_6.Add(HealthRatio(41020800) >= 0.4000000059604645)
    SkipLinesIfConditionFalse(3, AND_6)
    AddSpecialEffect(41020800, 20018634)
    Wait(1.0)
    Restart()
    AND_7.Add(HealthRatio(41020800) < 0.4000000059604645)
    AND_7.Add(HealthRatio(41020800) >= 0.30000001192092896)
    SkipLinesIfConditionFalse(3, AND_7)
    AddSpecialEffect(41020800, 20018635)
    Wait(1.0)
    Restart()
    AND_8.Add(HealthRatio(41020800) < 0.30000001192092896)
    AND_8.Add(HealthRatio(41020800) >= 0.20000000298023224)
    SkipLinesIfConditionFalse(3, AND_8)
    AddSpecialEffect(41020800, 20018636)
    Wait(1.0)
    Restart()
    AND_9.Add(HealthRatio(41020800) < 0.20000000298023224)
    AND_9.Add(HealthRatio(41020800) >= 0.10000000149011612)
    SkipLinesIfConditionFalse(3, AND_9)
    AddSpecialEffect(41020800, 20018637)
    Wait(1.0)
    Restart()
    AddSpecialEffect(41020800, 20018638)
    Wait(1.0)
    Restart()


@RestartOnRest(41022871)
def Event_41022871():
    """Event 41022871"""
    if FlagEnabled(41020800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(41020800, 20018639))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(41020800, 61050, wait_for_completion=True)
    WaitRealFrames(frames=10)
    Restart()
