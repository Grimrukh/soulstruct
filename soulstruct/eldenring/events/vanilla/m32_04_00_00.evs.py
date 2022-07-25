"""
Old Altus Tunnel

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
from .entities.m32_04_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32040000, asset=Assets.AEG099_060_9000)
    Event_32042800()
    Event_32042810()
    Event_32042811()
    Event_32042849()
    Event_32042200(
        0,
        character=Characters.TunnelMiner1,
        animation_id=30004,
        animation_id_1=20004,
        special_effect_id=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9052,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32042250(
        0,
        character=Characters.TunnelMiner2,
        animation_id=30000,
        animation_id_1=20000,
        special_effect_id=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_864_9002,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32040207,
    )
    Event_32042270(
        0,
        character=Characters.TunnelMiner2,
        animation_id=30005,
        animation_id_1=20005,
        flag=32040207,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32042200(
        2,
        character=Characters.TunnelMiner3,
        animation_id=30004,
        animation_id_1=20004,
        special_effect_id=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9054,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32042200(
        3,
        character=Characters.TunnelMiner4,
        animation_id=30004,
        animation_id_1=20004,
        special_effect_id=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9053,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32042510()
    CommonFunc_90005501(
        0,
        flag=32040510,
        flag_1=32040511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1001,
        asset_2=Assets.AEG027_080_1000,
        flag_2=32040512,
    )
    Event_32042580()
    CommonFunc_90005646(
        0,
        flag=32040800,
        left_flag=32042840,
        cancel_flag__right_flag=32042841,
        asset=Assets.AEG099_065_9000,
        player_start=32042840,
        area_id=32,
        block_id=4,
        cc_id=0,
        dd_id=0,
    )
    Event_32049570(
        0,
        flag=32040570,
        destination=32041570,
        left_flag=32042570,
        cancel_flag__right_flag=32042571,
        flag_1=32042572,
    )
    Event_32042569(0, flag=32040570, asset=32041570, asset_1=32041571, asset_2=32041572, asset_3=32041573)
    CommonFunc_900005610(0, 32041690, 100, 800, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32040519()
    CommonFunc_90005250(0, character=Characters.TunnelMiner0, region=32042200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner5, region=32042217, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.TunnelMiner6,
        animation_id=30005,
        animation_id_1=20005,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=32040250, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=32040302, region=32042213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier0, region=32042213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier1, region=32042305, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight0, region=32042305, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight1, region=32042351, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog0, region=32042200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog3, region=32042410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog4, region=32042410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, 32040412, 32042217, 0.0, -1)


@ContinueOnRest(32042510)
def Event_32042510():
    """Event 32042510"""
    CommonFunc_90005500(
        0,
        32040510,
        32040511,
        0,
        32041510,
        32041511,
        32043511,
        32041512,
        32043512,
        32042511,
        32042512,
        32040512,
        32040513,
        0,
    )


@ContinueOnRest(32040519)
def Event_32040519():
    """Event 32040519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32040510)
    EnableThisSlotFlag()


@RestartOnRest(32049570)
def Event_32049570(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint, flag_1: uint):
    """Event 32049570"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(PlayerNotInOwnWorld())
    if OR_1:
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9220, entity=destination))
    
    DisplayDialogAndSetFlags(
        message=108000,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8000, flag=flag_1, bit_count=2)
    AND_2.Add(EventValue(flag=flag_1, bit_count=6) >= 2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050)
    Wait(1.5)
    DisplayDialog(text=308000, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Asset, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(1.3300000429153442)
    ForceAnimation(PLAYER, 60811)
    Wait(1.5)
    DisplayDialog(text=208000, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8000, quantity=2)
    EnableNetworkFlag(flag)


@RestartOnRest(32042569)
def Event_32042569(_, flag: uint, asset: uint, asset_1: uint, asset_2: uint, asset_3: uint):
    """Event 32042569"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(flag):
        DeleteAssetVFX(asset)
        DeleteAssetVFX(asset_3)
        EnableAsset(asset_1)
        EnableAsset(asset_2)
        DisableAsset(asset_3)
        End()
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_3)
    DisableAsset(asset_1)
    DisableAsset(asset_2)
    CreateAssetVFX(asset, vfx_id=200, model_point=806040)
    CreateAssetVFX(asset, vfx_id=201, model_point=806040)
    CreateAssetVFX(asset_3, vfx_id=101, model_point=806042)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableAsset(asset_1)
    Wait(1.3300000429153442)
    EnableAsset(asset_2)
    Wait(0.5)
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_3, erase_root=False)
    DisableAsset(asset_3)


@RestartOnRest(32042580)
def Event_32042580():
    """Event 32042580"""
    RegisterLadder(start_climbing_flag=32040530, stop_climbing_flag=32040531, asset=Assets.AEG027_046_1000)
    RegisterLadder(start_climbing_flag=32040532, stop_climbing_flag=32040533, asset=Assets.AEG027_000_1001)


@RestartOnRest(32042200)
def Event_32042200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
):
    """Event 32042200"""
    if ThisEventSlotFlagEnabled():
        return
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
    OR_10.Add(AssetDestroyed(asset))
    OR_10.Add(AssetDestroyed(asset_1))
    OR_10.Add(AssetDestroyed(asset_2))
    OR_10.Add(AssetDestroyed(asset_3))
    AND_1.Add(OR_10)
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32042250)
def Event_32042250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect_id: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    asset: uint,
    asset_1: uint,
    asset_2: uint,
    asset_3: uint,
    flag: uint,
):
    """Event 32042250"""
    if FlagEnabled(flag):
        return
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
    OR_10.Add(AssetDestroyed(asset))
    OR_10.Add(AssetDestroyed(asset_1))
    OR_10.Add(AssetDestroyed(asset_2))
    OR_10.Add(AssetDestroyed(asset_3))
    AND_1.Add(OR_10)
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableFlag(flag)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect_id)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32042270)
def Event_32042270(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    flag: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 32042270"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(flag):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(32042800)
def Event_32042800():
    """Event 32042800"""
    if FlagEnabled(32040800):
        return
    
    MAIN.Await(HealthValue(Characters.MineTroll) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MineTroll))
    
    KillBossAndDisplayBanner(character=Characters.MineTroll, banner_type=BannerType.EnemyFelled)
    EnableFlag(32040800)
    EnableFlag(9263)
    if PlayerInOwnWorld():
        EnableFlag(61263)


@RestartOnRest(32042810)
def Event_32042810():
    """Event 32042810"""
    GotoIfFlagDisabled(Label.L0, flag=32040800)
    DisableCharacter(Characters.MineTroll)
    DisableAnimations(Characters.MineTroll)
    Kill(Characters.MineTroll)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MineTroll)
    ForceAnimation(Characters.MineTroll, 30000, loop=True)
    AND_2.Add(FlagEnabled(32042805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32042800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.MineTroll, 20000)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MineTroll)
    SetNetworkUpdateRate(Characters.MineTroll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MineTroll, name=904600321)


@RestartOnRest(32042811)
def Event_32042811():
    """Event 32042811"""
    if FlagEnabled(32040800):
        return
    AND_1.Add(HealthRatio(Characters.MineTroll) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32042802)


@RestartOnRest(32042849)
def Event_32042849():
    """Event 32042849"""
    CommonFunc_9005800(
        0,
        flag=32040800,
        entity=Assets.AEG099_001_9000,
        region=32042800,
        flag_1=32042805,
        character=32045800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=32040800,
        entity=Assets.AEG099_001_9000,
        region=32042800,
        flag_1=32042805,
        flag_2=32042806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32040800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 32040800, 931000, 32042805, 32042806, 0, 32042802, 0, 0)
