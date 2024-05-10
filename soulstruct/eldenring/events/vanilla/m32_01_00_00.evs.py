"""
Limgrave Tunnels

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
from .enums.m32_01_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32010000, asset=Assets.AEG099_060_9000)
    Event_32012800()
    Event_32012810()
    Event_32012811()
    Event_32012849()
    Event_32012510()
    CommonFunc_90005501(
        0,
        flag=32010510,
        flag_1=32010511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1000,
        asset_2=Assets.AEG027_080_1001,
        flag_2=32010512,
    )
    CommonFunc_90005501(
        0,
        flag=32010515,
        flag_1=32010516,
        left=0,
        asset=Assets.AEG027_001_1001,
        asset_1=Assets.AEG027_080_1002,
        asset_2=Assets.AEG027_080_1003,
        flag_2=32010517,
    )
    CommonFunc_90005501(
        0,
        flag=32010520,
        flag_1=32010521,
        left=0,
        asset=Assets.AEG027_001_1002,
        asset_1=Assets.AEG027_080_1004,
        asset_2=Assets.AEG027_080_1005,
        flag_2=32010522,
    )
    CommonFunc_90005646(
        0,
        flag=32010800,
        left_flag=32012840,
        cancel_flag__right_flag=32012841,
        asset=Assets.AEG099_065_9000,
        player_start=32012840,
        area_id=32,
        block_id=1,
        cc_id=0,
        dd_id=0,
    )
    Event_32012250(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30004,
        animation_id_1=20004,
        special_effect=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9001,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010201,
    )
    Event_32012270(
        0,
        character=Characters.TunnelMiner0,
        animation_id=30005,
        animation_id_1=20005,
        flag=32010201,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32012250(
        1,
        character=Characters.TunnelMiner1,
        animation_id=30004,
        animation_id_1=20004,
        special_effect=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9000,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010202,
    )
    Event_32012270(
        1,
        character=Characters.TunnelMiner1,
        animation_id=30005,
        animation_id_1=20005,
        flag=32010202,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32012250(
        2,
        character=Characters.TunnelMiner2,
        animation_id=30004,
        animation_id_1=20004,
        special_effect=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9005,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010203,
    )
    Event_32012270(
        2,
        character=Characters.TunnelMiner2,
        animation_id=30006,
        animation_id_1=20006,
        flag=32010203,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.TunnelMiner3,
        animation_id=30006,
        animation_id_1=20006,
        region=32012205,
        radius=5.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=1,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    Event_32012250(
        3,
        character=Characters.TunnelMiner4,
        animation_id=30002,
        animation_id_1=20002,
        special_effect=16574,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9002,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010211,
    )
    Event_32012270(
        3,
        character=Characters.TunnelMiner4,
        animation_id=30005,
        animation_id_1=20005,
        flag=32010211,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32012250(
        4,
        character=Characters.TunnelMiner6,
        animation_id=30000,
        animation_id_1=20000,
        special_effect=16572,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9007,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010215,
    )
    Event_32012270(
        4,
        character=Characters.TunnelMiner6,
        animation_id=30006,
        animation_id_1=20006,
        flag=32010215,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32012250(
        5,
        character=Characters.TunnelMiner8,
        animation_id=30004,
        animation_id_1=20004,
        special_effect=16576,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_860_9003,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32010218,
    )
    Event_32012270(
        5,
        character=Characters.TunnelMiner8,
        animation_id=30005,
        animation_id_1=20005,
        flag=32010218,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_32010519()
    Event_32012820()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(32010519):
        return
    EnableFlag(32010510)
    EnableFlag(32010515)
    EnableFlag(32010520)
    CommonFunc_90005211(
        0,
        character=Characters.TunnelMiner3,
        animation_id=30006,
        animation_id_1=20006,
        region=32012205,
        radius=5.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=1,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner5, region=32012300, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner5, region=32012301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner7, region=32012220, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner9, region=32012219, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.TunnelMiner10, region=32012220, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallerDog0, region=32012300, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallerDog0, region=32012301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.SmallerDog1, region=32012301, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Rat0, region=32012350, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Rat1, region=32012350, seconds=0.0, animation_id=-1)
    CommonFunc_AITrigger_RegionOrHurt(0, character=Characters.Rat2, region=32012350, seconds=0.0, animation_id=-1)


@ContinueOnRest(32012510)
def Event_32012510():
    """Event 32012510"""
    CommonFunc_90005500(
        0,
        flag=32010510,
        flag_1=32010511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1000,
        obj_act_id=32013511,
        asset_2=Assets.AEG027_080_1001,
        obj_act_id_1=32013512,
        region=32012511,
        region_1=32012512,
        flag_2=32010512,
        flag_3=32010513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=32010515,
        flag_1=32010516,
        left=0,
        asset=Assets.AEG027_001_1001,
        asset_1=Assets.AEG027_080_1002,
        obj_act_id=32013516,
        asset_2=Assets.AEG027_080_1003,
        obj_act_id_1=32013517,
        region=32012516,
        region_1=32012517,
        flag_2=32010517,
        flag_3=32010518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=32010520,
        flag_1=32010521,
        left=0,
        asset=Assets.AEG027_001_1002,
        asset_1=Assets.AEG027_080_1004,
        obj_act_id=32013521,
        asset_2=Assets.AEG027_080_1005,
        obj_act_id_1=32013522,
        region=32012521,
        region_1=32012522,
        flag_2=32010522,
        flag_3=32010523,
        left_1=0,
    )


@ContinueOnRest(32010519)
def Event_32010519():
    """Event 32010519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableThisSlotFlag()


@RestartOnRest(32012200)
def Event_32012200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
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
    """Event 32012200"""
    if ThisEventSlotFlagEnabled():
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32012250)
def Event_32012250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
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
    """Event 32012250"""
    if FlagEnabled(flag):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableFlag(flag)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    AddSpecialEffect(character, 16571)
    AddSpecialEffect(character, special_effect)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32012270)
def Event_32012270(
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
    """Event 32012270"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(flag):
        return
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
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
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


@RestartOnRest(32012650)
def Event_32012650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 32012650"""
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
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=109, flag=flag, bit_count=1)
    EnableFlag(700690)


@RestartOnRest(32012651)
def Event_32012651(_, tutorial_param_id: int, flag: uint, flag_1: uint, tutorial_param_id_1: int):
    """Event 32012651"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=LIMGRAVE_TUNNELS))
    AND_1.Add(PlayerDoesNotHaveGood(9116, including_storage=True))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag_1)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9116, flag=flag, bit_count=1)


@RestartOnRest(32012800)
def Event_32012800():
    """Event 32012800"""
    if FlagEnabled(32010800):
        return
    
    MAIN.Await(HealthValue(Characters.MineTroll) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32018000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(HealthValue(Characters.MineTroll) == 0)
    
    KillBossAndDisplayBanner(character=Characters.MineTroll, banner_type=BannerType.EnemyFelled)
    EnableFlag(32010800)
    EnableFlag(9261)
    if PlayerInOwnWorld():
        EnableFlag(61261)


@RestartOnRest(32012810)
def Event_32012810():
    """Event 32012810"""
    GotoIfFlagDisabled(Label.L0, flag=32010800)
    DisableCharacter(Characters.MineTroll)
    DisableAnimations(Characters.MineTroll)
    Kill(Characters.MineTroll)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MineTroll)
    GotoIfFlagEnabled(Label.L1, flag=32010801)
    ForceAnimation(Characters.MineTroll, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32012801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.MineTroll, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(32010801)
    ForceAnimation(Characters.MineTroll, 20000, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(32012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MineTroll)
    SetNetworkUpdateRate(Characters.MineTroll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MineTroll, name=904600320)


@RestartOnRest(32012811)
def Event_32012811():
    """Event 32012811"""
    if FlagEnabled(32010800):
        return
    AND_1.Add(HealthRatio(Characters.MineTroll) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32012802)


@RestartOnRest(32012820)
def Event_32012820():
    """Event 32012820"""
    if FlagEnabled(32010800):
        return
    if FlagEnabled(32010801):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(32018590):
        return
    DisableFlag(32018590)


@RestartOnRest(32012849)
def Event_32012849():
    """Event 32012849"""
    CommonFunc_9005800(
        0,
        flag=32010800,
        entity=Assets.AEG099_002_9000,
        region=32012800,
        flag_1=32012805,
        character=32015800,
        action_button_id=10000,
        left=32010801,
        region_1=32012801,
    )
    CommonFunc_9005801(
        0,
        flag=32010800,
        entity=Assets.AEG099_002_9000,
        region=32012800,
        flag_1=32012805,
        flag_2=32012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32010800, asset=Assets.AEG099_002_9000, dummy_id=7, right=32010801)
    CommonFunc_9005822(
        0,
        flag=32010800,
        bgm_boss_conv_param_id=931000,
        flag_1=32012805,
        flag_2=32012806,
        right=0,
        flag_3=32012802,
        left=0,
        left_1=0,
    )


@RestartOnRest(32012920)
def Event_32012920():
    """Event 32012920"""
    DisableNetworkSync()
    
    MAIN.Await(AssetBackreadEnabled(asset=Assets.AEG027_001_1001))
    
    EnableFlag(32010519)
    
    MAIN.Await(AssetBackreadDisabled(asset=Assets.AEG027_001_1001))
    
    DisableFlag(32010519)
    Restart()
