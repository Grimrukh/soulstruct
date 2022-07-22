"""
Morne Tunnel

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
from .entities.m32_00_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32000000, asset=Assets.AEG099_060_9000)
    Event_32002800()
    Event_32002810()
    Event_32002811()
    Event_32002849()
    Event_32002510()
    CommonFunc_90005501(
        0,
        flag=32000510,
        flag_1=32000511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1000,
        asset_2=Assets.AEG027_080_1001,
        flag_2=32000512,
    )
    Event_32002580()
    CommonFunc_90005646(
        0,
        flag=32000800,
        left_flag=32002840,
        cancel_flag__right_flag=32002841,
        asset=Assets.AEG099_065_9000,
        player_start=32002840,
        area_id=32,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    Event_32002250(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30000,
        animation_id_1=20000,
        special_effect_id=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9001,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000201,
    )
    Event_32002270(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30005,
        animation_id_1=20005,
        flag=32000201,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002250(
        3,
        character=Characters.TunnelMiner1,
        animation_id=30002,
        animation_id_1=20002,
        special_effect_id=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9002,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000205,
    )
    Event_32002270(
        3,
        character=Characters.TunnelMiner1,
        animation_id=30005,
        animation_id_1=20005,
        flag=32000205,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002250(
        4,
        character=Characters.TunnelMiner2,
        animation_id=30000,
        animation_id_1=20000,
        special_effect_id=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9003,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000206,
    )
    Event_32002270(
        4,
        character=Characters.TunnelMiner2,
        animation_id=30006,
        animation_id_1=20006,
        flag=32000206,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002250(
        5,
        character=Characters.TunnelMiner9,
        animation_id=30000,
        animation_id_1=20000,
        special_effect_id=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9007,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000215,
    )
    Event_32002270(
        5,
        character=Characters.TunnelMiner9,
        animation_id=30006,
        animation_id_1=20006,
        flag=32000215,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002250(
        1,
        character=Characters.TunnelMiner10,
        animation_id=30002,
        animation_id_1=20002,
        special_effect_id=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9005,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000216,
    )
    Event_32002270(
        1,
        character=Characters.TunnelMiner10,
        animation_id=30005,
        animation_id_1=20005,
        flag=32000216,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002250(
        2,
        character=Characters.TunnelMiner11,
        animation_id=30000,
        animation_id_1=20000,
        special_effect_id=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9004,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32000219,
    )
    Event_32002270(
        2,
        character=Characters.TunnelMiner11,
        animation_id=30005,
        animation_id_1=20005,
        flag=32000219,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32002300(5, character=Characters.Misbegotten2, region=32002305, seconds=0.0, animation_id=-1)
    Event_32002300(6, character=Characters.Misbegotten3, region=32002305, seconds=0.0, animation_id=-1)
    Event_32002310(
        15,
        character=Characters.Misbegotten5,
        region=32002315,
        seconds=0.0,
        animation_id=-1,
        attacked_entity=Characters.Misbegotten6,
        attacked_entity_1=Characters.Misbegotten8,
    )
    Event_32002310(
        16,
        character=Characters.Misbegotten6,
        region=32002315,
        seconds=0.0,
        animation_id=-1,
        attacked_entity=Characters.Misbegotten5,
        attacked_entity_1=Characters.Misbegotten8,
    )
    Event_32002310(18, 32000318, 32002315, 0.0, -1, 32000315, 32000316)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32000519()
    CommonFunc_90005250(0, character=Characters.TunnelMiner3, region=32002207, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner4, region=32002207, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner5, region=32002210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner6, region=32002211, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.TunnelMiner7, region=32002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Misbegotten0, radius=27.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten1,
        animation_id=30000,
        animation_id_1=20000,
        region=32002302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Misbegotten7, region=32002317, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, 32000319, 32002315, 0.0, -1)


@ContinueOnRest(32002510)
def Event_32002510():
    """Event 32002510"""
    CommonFunc_90005500(
        0,
        32000510,
        32000511,
        0,
        32001510,
        32001511,
        32003511,
        32001512,
        32003512,
        32002511,
        32002512,
        32000512,
        32000513,
        0,
    )


@ContinueOnRest(32000519)
def Event_32000519():
    """Event 32000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32000510)
    DisableThisSlotFlag()


@ContinueOnRest(32002580)
def Event_32002580():
    """Event 32002580"""
    RegisterLadder(start_climbing_flag=32000530, stop_climbing_flag=32000531, asset=Assets.AEG027_000_1000)


@RestartOnRest(32002200)
def Event_32002200(
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
    """Event 32002200"""
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


@RestartOnRest(32002250)
def Event_32002250(
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
    """Event 32002250"""
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


@RestartOnRest(32002270)
def Event_32002270(
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
    """Event 32002270"""
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


@RestartOnRest(32002300)
def Event_32002300(_, character: uint, region: uint, seconds: float, animation_id: int):
    """Event 32002300"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(HasAIStatus(Characters.Misbegotten4, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(32002310)
def Event_32002310(
    _,
    character: uint,
    region: uint,
    seconds: float,
    animation_id: int,
    attacked_entity: uint,
    attacked_entity_1: uint,
):
    """Event 32002310"""
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
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=0))
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=0))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(32002800)
def Event_32002800():
    """Event 32002800"""
    if FlagEnabled(32000800):
        return
    
    MAIN.Await(HealthValue(Characters.ScalyMisbegotten) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.ScalyMisbegotten, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.ScalyMisbegotten))
    
    KillBossAndDisplayBanner(character=Characters.ScalyMisbegotten, banner_type=BannerType.EnemyFelled)
    EnableFlag(32000800)
    EnableFlag(9260)
    if PlayerInOwnWorld():
        EnableFlag(61260)


@RestartOnRest(32002810)
def Event_32002810():
    """Event 32002810"""
    GotoIfFlagDisabled(Label.L0, flag=32000800)
    DisableCharacter(Characters.ScalyMisbegotten)
    DisableAnimations(Characters.ScalyMisbegotten)
    Kill(Characters.ScalyMisbegotten)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.ScalyMisbegotten)
    GotoIfFlagEnabled(Label.L1, flag=32000801)
    ForceAnimation(Characters.ScalyMisbegotten, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32002801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.ScalyMisbegotten, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(32000801)
    ForceAnimation(Characters.ScalyMisbegotten, 20000, wait_for_completion=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(32002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.ScalyMisbegotten)
    SetNetworkUpdateRate(Characters.ScalyMisbegotten, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.ScalyMisbegotten, name=903451320)
    AddSpecialEffect(Characters.ScalyMisbegotten, 8089)


@RestartOnRest(32002811)
def Event_32002811():
    """Event 32002811"""
    if FlagEnabled(32000800):
        return
    AND_1.Add(HealthRatio(Characters.ScalyMisbegotten) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32002802)


@RestartOnRest(32002820)
def Event_32002820(_, character: uint):
    """Event 32002820"""
    if FlagEnabled(32000800):
        return
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 4305)


@RestartOnRest(32002849)
def Event_32002849():
    """Event 32002849"""
    CommonFunc_9005800(
        0,
        flag=32000800,
        entity=Assets.AEG099_002_9000,
        region=32002800,
        flag_1=32002805,
        character=32005800,
        action_button_id=10000,
        left=32000801,
        region_1=32002801,
    )
    CommonFunc_9005801(
        0,
        flag=32000800,
        entity=Assets.AEG099_002_9000,
        region=32002800,
        flag_1=32002805,
        flag_2=32002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32000800, asset=Assets.AEG099_002_9000, model_point=7, right=32000801)
    CommonFunc_9005822(0, 32000800, 931000, 32002805, 32002806, 0, 32002802, 0, 0)
