"""
Raya Lucaria Crystal Tunnel

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
from .enums.m32_02_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32020000, asset=Assets.AEG099_060_9000)
    Event_32022800()
    Event_32022810()
    Event_32022811()
    Event_32022849()
    Event_32022200(
        0,
        character=Characters.GlintstoneMiner2,
        animation_id=30002,
        animation_id_1=20002,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9015,
        asset_1=Assets.AEG099_780_9016,
        asset_2=0,
        asset_3=0,
    )
    Event_32022250(
        0,
        character=Characters.GlintstoneMiner3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_861_9000,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020206,
    )
    Event_32022270(
        0,
        character=Characters.GlintstoneMiner3,
        animation_id=30006,
        animation_id_1=20006,
        flag=32020206,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022200(
        2,
        character=Characters.GlintstoneMiner4,
        animation_id=30002,
        animation_id_1=20002,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9018,
        asset_1=Assets.AEG099_780_9019,
        asset_2=0,
        asset_3=0,
    )
    Event_32022200(
        5,
        character=Characters.GlintstoneMiner10,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9036,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32022200(
        6,
        character=Characters.GlintstoneMiner11,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9025,
        asset_1=Assets.AEG099_780_9026,
        asset_2=0,
        asset_3=0,
    )
    Event_32022200(
        7,
        character=Characters.GlintstoneMiner12,
        animation_id=30002,
        animation_id_1=20002,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9033,
        asset_1=Assets.AEG099_780_9034,
        asset_2=Assets.AEG099_780_9035,
        asset_3=0,
    )
    Event_32022250(
        1,
        character=Characters.GlintstoneMiner14,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_861_9001,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020221,
    )
    Event_32022270(
        1,
        character=Characters.GlintstoneMiner14,
        animation_id=30006,
        animation_id_1=20006,
        flag=32020221,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022250(
        2,
        character=Characters.GlintstoneMiner15,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_861_9004,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020222,
    )
    Event_32022270(
        2,
        character=Characters.GlintstoneMiner15,
        animation_id=30006,
        animation_id_1=20006,
        flag=32020222,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022250(
        3,
        character=Characters.GlintstoneMiner16,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_862_9006,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020230,
    )
    Event_32022270(
        3,
        character=Characters.GlintstoneMiner16,
        animation_id=30007,
        animation_id_1=20007,
        flag=32020230,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022250(
        4,
        character=Characters.GlintstoneMiner17,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_862_9007,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020231,
    )
    Event_32022270(
        4,
        character=Characters.GlintstoneMiner17,
        animation_id=30006,
        animation_id_1=20006,
        flag=32020231,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022250(
        5,
        character=Characters.GlintstoneMiner18,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_862_9008,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32020232,
    )
    Event_32022270(
        5,
        character=Characters.GlintstoneMiner18,
        animation_id=30007,
        animation_id_1=20007,
        flag=32020232,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32022200(
        20,
        character=Characters.GlintstoneMiner19,
        animation_id=30002,
        animation_id_1=20002,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9069,
        asset_1=Assets.AEG099_780_9070,
        asset_2=0,
        asset_3=0,
    )
    Event_32022200(
        21,
        character=Characters.GlintstoneMiner20,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9071,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32022510()
    CommonFunc_90005502(0, flag=32020514, asset=Assets.AEG027_080_0501, region=32022517)
    CommonFunc_90005501(
        0,
        flag=32020510,
        flag_1=32020511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1001,
        asset_2=Assets.AEG027_080_1000,
        flag_2=32020512,
    )
    CommonFunc_90005501(
        0,
        flag=32020515,
        flag_1=32020516,
        left=2,
        asset=Assets.AEG027_001_0500,
        asset_1=Assets.AEG027_080_0501,
        asset_2=Assets.AEG027_080_0500,
        flag_2=32020517,
    )
    CommonFunc_90005501(
        0,
        flag=32020520,
        flag_1=32020521,
        left=0,
        asset=Assets.AEG027_001_1001,
        asset_1=Assets.AEG027_080_1003,
        asset_2=Assets.AEG027_080_1002,
        flag_2=32020522,
    )
    CommonFunc_90005501(
        0,
        flag=32020525,
        flag_1=32020526,
        left=0,
        asset=Assets.AEG027_001_1002,
        asset_1=Assets.AEG027_080_1005,
        asset_2=Assets.AEG027_080_1004,
        flag_2=32020527,
    )
    CommonFunc_90005646(
        0,
        flag=32020800,
        left_flag=32022840,
        cancel_flag__right_flag=32022841,
        asset=Assets.AEG099_065_9000,
        player_start=32022840,
        area_id=32,
        block_id=2,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner0, region=32022200, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GlintstoneMiner1, radius=26.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner5, region=32022208, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner6, region=32022210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner7, region=32022210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner8, region=32022213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner8, region=32022212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner9, region=32022210, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner9, region=32022213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner13, region=32022217, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=32020220, region=32022220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BigGlintstoneMiner, region=32022230, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GlintstoneMiner21, region=32022230, seconds=5.0, animation_id=-1)
    CommonFunc_90005260(
        0,
        character=Characters.GlintstoneMiner22,
        region=32022230,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005251(0, character=Characters.Marionette3, radius=18.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.Marionette4,
        animation_id=30010,
        animation_id_1=20010,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Marionette5,
        animation_id=30010,
        animation_id_1=20010,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=32020305, region=32022305, seconds=2.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Marionette0,
        animation_id=30011,
        animation_id_1=20011,
        region=32022306,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette1,
        animation_id=30011,
        animation_id_1=20011,
        region=32022306,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        region=32022306,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_32020519()


@ContinueOnRest(32022510)
def Event_32022510():
    """Event 32022510"""
    CommonFunc_90005500(
        0,
        flag=32020510,
        flag_1=32020511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1001,
        obj_act_id=32023511,
        asset_2=Assets.AEG027_080_1000,
        obj_act_id_1=32023512,
        region=32022511,
        region_1=32022512,
        flag_2=32020512,
        flag_3=32020513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=32020515,
        flag_1=32020516,
        left=2,
        asset=Assets.AEG027_001_0500,
        asset_1=Assets.AEG027_080_0501,
        obj_act_id=32023516,
        asset_2=Assets.AEG027_080_0500,
        obj_act_id_1=32023517,
        region=32022516,
        region_1=32022517,
        flag_2=32020517,
        flag_3=32020518,
        left_1=32020514,
    )
    CommonFunc_90005500(
        0,
        flag=32020520,
        flag_1=32020521,
        left=0,
        asset=Assets.AEG027_001_1001,
        asset_1=Assets.AEG027_080_1003,
        obj_act_id=32023521,
        asset_2=Assets.AEG027_080_1002,
        obj_act_id_1=32023522,
        region=32022521,
        region_1=32022522,
        flag_2=32020522,
        flag_3=32020523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=32020525,
        flag_1=32020526,
        left=0,
        asset=Assets.AEG027_001_1002,
        asset_1=Assets.AEG027_080_1005,
        obj_act_id=32023526,
        asset_2=Assets.AEG027_080_1004,
        obj_act_id_1=32023527,
        region=32022526,
        region_1=32022527,
        flag_2=32020527,
        flag_3=32020528,
        left_1=0,
    )


@ContinueOnRest(32020519)
def Event_32020519():
    """Event 32020519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32020510)
    EnableFlag(32020520)
    EnableFlag(32020525)
    EnableThisSlotFlag()


@RestartOnRest(32022200)
def Event_32022200(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
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
    """Event 32022200"""
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


@RestartOnRest(32022250)
def Event_32022250(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
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
    """Event 32022250"""
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
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(32022270)
def Event_32022270(
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
    """Event 32022270"""
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


@RestartOnRest(32022800)
def Event_32022800():
    """Event 32022800"""
    if FlagEnabled(32020800):
        return
    
    MAIN.Await(HealthValue(Characters.Crystalian) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(32028000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Crystalian))
    
    KillBossAndDisplayBanner(character=Characters.Crystalian, banner_type=BannerType.EnemyFelled)
    EnableFlag(32020800)
    EnableFlag(9262)
    if PlayerInOwnWorld():
        EnableFlag(61262)


@RestartOnRest(32022810)
def Event_32022810():
    """Event 32022810"""
    GotoIfFlagDisabled(Label.L0, flag=32020800)
    DisableCharacter(Characters.Crystalian)
    DisableAnimations(Characters.Crystalian)
    Kill(Characters.Crystalian)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Crystalian)
    AddSpecialEffect(Characters.Crystalian, 8090)
    EnableInvincibility(Characters.Crystalian)
    SetLockOnPoint(character=Characters.Crystalian, lock_on_model_point=220, state=False)
    ForceAnimation(Characters.Crystalian, 30001, loop=True)
    AND_2.Add(FlagEnabled(32022805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32022800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.Crystalian, 20001)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Crystalian)
    SetNetworkUpdateRate(Characters.Crystalian, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Crystalian, name=903350320)
    DisableInvincibility(Characters.Crystalian)
    SetLockOnPoint(character=Characters.Crystalian, lock_on_model_point=220, state=True)


@RestartOnRest(32022811)
def Event_32022811():
    """Event 32022811"""
    if FlagEnabled(32020800):
        return
    AND_1.Add(HealthRatio(Characters.Crystalian) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(32022802)


@RestartOnRest(32022849)
def Event_32022849():
    """Event 32022849"""
    CommonFunc_9005800(
        0,
        flag=32020800,
        entity=Assets.AEG099_001_9000,
        region=32022800,
        flag_1=32022805,
        character=32025800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=32020800,
        entity=Assets.AEG099_001_9000,
        region=32022800,
        flag_1=32022805,
        flag_2=32022806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32020800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=32020800,
        bgm_boss_conv_param_id=931000,
        flag_1=32022805,
        flag_2=32022806,
        right=0,
        flag_3=32022802,
        left=0,
        left_1=0,
    )
