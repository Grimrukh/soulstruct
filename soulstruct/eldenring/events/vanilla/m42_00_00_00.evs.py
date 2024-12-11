"""
m42_00_00_00

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
    RegisterGrace(grace_flag=42000000, asset=42001950)
    CommonFunc_90005646(
        0,
        flag=42007000,
        left_flag=42002840,
        cancel_flag__right_flag=42002841,
        asset=42001840,
        player_start=42002840,
        area_id=42,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    Event_42002580()
    Event_42002630()
    Event_42002640()
    Event_42002650(0, attacker=42000200, asset=42001650, flag=42002650)
    Event_42002650(1, attacker=42000200, asset=42001651, flag=42002651)
    Event_42002650(2, attacker=42000200, asset=42001652, flag=42002652)
    CommonFunc_90005555(0, flag=42007000, item_lot=42000000, asset=42001610)
    CommonFunc_900005610(0, asset=42001660, dummy_id=100, vfx_id=800, right=0)
    Event_42000700(0, character=42000700, animation_id=30013, left=0, flag=42029205)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=42000200, region=42002200, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42000201,
        animation_id=30002,
        animation_id_1=20002,
        region=42002201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000202,
        animation_id=30002,
        animation_id_1=20002,
        region=42002202,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42000203, region=42002203, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42000300,
        animation_id=30000,
        animation_id_1=20000,
        region=42002300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000305,
        animation_id=30000,
        animation_id_1=20000,
        region=42002305,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=42000310, region=42002310, radius=30.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=42000311,
        animation_id=30000,
        animation_id_1=20000,
        region=42002310,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000316,
        animation_id=30000,
        animation_id_1=20000,
        region=42002316,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42000321, region=42002319, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42000335,
        animation_id=30000,
        animation_id_1=20000,
        region=42002335,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000336,
        animation_id=30000,
        animation_id_1=20000,
        region=42002336,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000337,
        animation_id=30000,
        animation_id_1=20000,
        region=42002337,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000330,
        animation_id=30000,
        animation_id_1=20000,
        region=42002330,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42000331,
        animation_id=30000,
        animation_id_1=20000,
        region=42002331,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_42002330(0, character=42000330)
    Event_42002330(1, character=42000331)
    Event_42002315(0, character=42000316, region=42002317)
    Event_42002315(9, character=42000330, region=42002331)
    Event_42002315(10, character=42000331, region=42002331)


@ContinueOnRest(42002580)
def Event_42002580():
    """Event 42002580"""
    RegisterLadder(start_climbing_flag=42000580, stop_climbing_flag=42000581, asset=42001580)
    RegisterLadder(start_climbing_flag=42000582, stop_climbing_flag=42000583, asset=42001582)
    RegisterLadder(start_climbing_flag=42000584, stop_climbing_flag=42000585, asset=42001584)
    RegisterLadder(start_climbing_flag=42000586, stop_climbing_flag=42000587, asset=42001586)


@RestartOnRest(42002610)
def Event_42002610():
    """Event 42002610"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(42007000):
        return
    CreateAssetVFX(42001610, dummy_id=100, vfx_id=834010)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209200, entity=42001610))
    
    MAIN.Await(AND_1)
    
    FaceEntityAndForceAnimation(PLAYER, 42001610, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.0)
    CreateAssetVFX(42001610, dummy_id=100, vfx_id=800380)
    Wait(1.0)
    DeleteAssetVFX(42001610)
    Wait(2.5)
    AwardItemLot(42000000, host_only=True)


@RestartOnRest(42002630)
def Event_42002630():
    """Event 42002630"""
    GotoIfFlagDisabled(Label.L0, flag=42000630)
    DisableAssetActivation(42001631, obj_act_id=449011)
    ForceAnimation(42001630, 2, wait_for_completion=True)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(42000630))
    AND_1.Add(AssetActivated(obj_act_id=42003631))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(42000630)
    DisableAssetActivation(42001631, obj_act_id=449011)
    ForceAnimation(42001630, 1, wait_for_completion=True)
    Restart()


@RestartOnRest(42002640)
def Event_42002640():
    """Event 42002640"""
    EndOfAnimation(asset=42001641, animation_id=20)
    DisableAsset(42001640)
    End()


@RestartOnRest(42002641)
def Event_42002641():
    """Event 42002641"""
    if FlagEnabled(42000641):
        return
    GotoIfFlagDisabled(Label.L0, flag=42000640)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=42002641))
    AND_1.Add(FlagEnabled(42000640))
    
    MAIN.Await(AND_1)
    
    DisableAsset(42001640)
    EnableNetworkFlag(42000641)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(42002650)
def Event_42002650(_, attacker: Character | int, asset: Asset | int, flag: Flag | int):
    """Event 42002650"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(AssetDamaged(asset, attacker=attacker))
    
    EnableNetworkFlag(flag)
    DestroyAsset(asset)


@RestartOnRest(42002200)
def Event_42002200():
    """Event 42002200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(42000200)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=42002200))
    AND_4.Add(CharacterHasSpecialEffect(42000200, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90160))
    AND_5.Add(CharacterHasSpecialEffect(42000200, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90162))
    AND_6.Add(CharacterHasSpecialEffect(42000200, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90161))
    AND_7.Add(CharacterHasSpecialEffect(42000200, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90162))
    AND_8.Add(CharacterHasSpecialEffect(42000200, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(42000200, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=42000200))
    OR_2.Add(CharacterHasStateInfo(character=42000200, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=42000200, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=42000200, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=42000200, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=42000200, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(42000200, 3004, loop=True)
    EnableAI(42000200)


@RestartOnRest(42002315)
def Event_42002315(_, character: Character | int, region: Region | int):
    """Event 42002315"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4080)
    AddSpecialEffect(character, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4080)
    RemoveSpecialEffect(character, 4085)
    Restart()


@RestartOnRest(42002330)
def Event_42002330(_, character: Character | int):
    """Event 42002330"""
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=42002340))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(42000700)
def Event_42000700(_, character: uint, animation_id: int, left: uint, flag: Flag | int):
    """Event 42000700"""
    GotoIfFlagEnabled(Label.L5, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    ForceAnimation(character, animation_id)
    if UnsignedEqual(left=left, right=0):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 9624))
    AwaitConditionTrue(AND_1)
    Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(character)
    Goto(Label.L20)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()
