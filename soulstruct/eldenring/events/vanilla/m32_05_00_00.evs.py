"""
Altus Tunnel

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
from .entities.m32_05_00_00_entities import *
from .entities.m31_18_00_00_entities import Characters as m31_18_Characters


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=32050000, asset=Assets.AEG099_060_9000)
    Event_32052800()
    Event_32052810()
    Event_32052811()
    Event_32052849()
    CommonFunc_90005501(
        0,
        flag=32050510,
        flag_1=32050511,
        left=0,
        asset=Assets.AEG027_001_1000,
        asset_1=Assets.AEG027_080_1001,
        asset_2=Assets.AEG027_080_1000,
        flag_2=32050512,
    )
    Event_32052510()
    CommonFunc_90005646(
        0,
        flag=32050800,
        left_flag=32052840,
        cancel_flag__right_flag=32052841,
        asset=Assets.AEG099_065_9000,
        player_start=32052840,
        area_id=32,
        block_id=5,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    Event_32052200(
        0,
        character=Characters.GlintstoneMiner3,
        animation_id=30002,
        animation_id_1=20002,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9005,
        asset_1=Assets.AEG099_780_9006,
        asset_2=Assets.AEG099_780_9007,
        asset_3=0,
    )
    Event_32052200(
        1,
        character=Characters.GlintstoneMiner4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9008,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32052200(
        2,
        character=Characters.GlintstoneMiner5,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_780_9009,
        asset_1=0,
        asset_2=0,
        asset_3=0,
    )
    Event_32052250(
        0,
        character=Characters.GlintstoneMiner6,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=Assets.AEG099_864_9002,
        asset_1=0,
        asset_2=0,
        asset_3=0,
        flag=32050211,
    )
    Event_32052270(
        0,
        character=Characters.GlintstoneMiner6,
        animation_id=30007,
        animation_id_1=20007,
        flag=32050211,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    Event_32052400()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32050519()
    Event_32052820()
    CommonFunc_90005250(0, 32050200, 32052200, 0.0, -1)
    CommonFunc_90005251(0, 32050201, 20.0, 0.0, -1)
    CommonFunc_90005250(0, 32050205, 32052205, 0.0, -1)
    CommonFunc_90005250(0, 32050212, 32052212, 0.0, -1)
    CommonFunc_90005250(0, 32050250, 32052200, 0.0, -1)
    CommonFunc_90005261(0, 32050255, 32052206, 2.0, 0.0, -1)
    CommonFunc_90005261(0, 32050257, 32052206, 2.0, 0.0, -1)
    CommonFunc_90005250(0, 32050256, 32052205, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.Avionette4, region=32052212, seconds=1.0, animation_id=3033)
    CommonFunc_90005250(0, character=32050259, region=32052212, seconds=1.0, animation_id=3033)
    CommonFunc_90005250(0, 32050300, 32052300, 0.0, -1)
    CommonFunc_90005250(0, 32050301, 32052300, 0.0, -1)
    CommonFunc_90005250(0, character=Characters.Snail2, region=32052300, seconds=0.0, animation_id=3011)
    CommonFunc_90005250(0, 32050305, 32052305, 0.0, -1)
    CommonFunc_90005260(0, character=Characters.Snail4, region=32052306, radius=10.0, seconds=0.0, animation_id=3011)
    CommonFunc_90005250(0, 32050307, 32052306, 0.0, -1)
    CommonFunc_90005250(0, 32050308, 32052306, 0.0, -1)
    CommonFunc_90005271(0, 32050310, 0.0, -1)
    CommonFunc_90005271(0, 32050311, 0.0, -1)
    CommonFunc_90005271(0, 32050312, 0.0, -1)
    CommonFunc_90005271(0, 32050313, 0.0, -1)
    CommonFunc_90005271(0, 32050314, 0.0, -1)
    CommonFunc_90005271(0, 32050315, 0.0, -1)
    CommonFunc_90005271(0, 32050316, 0.0, -1)
    CommonFunc_90005271(0, 32050317, 0.0, -1)
    CommonFunc_90005271(0, 32050318, 0.0, -1)


@NeverRestart(32052510)
def Event_32052510():
    """Event 32052510"""
    CommonFunc_90005500(
        0,
        32050510,
        32050511,
        0,
        32051510,
        32051511,
        32053511,
        32051512,
        32053512,
        32052511,
        32052512,
        32050512,
        32050513,
        0,
    )


@NeverRestart(32050519)
def Event_32050519():
    """Event 32050519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(32050510)
    DisableThisSlotFlag()


@RestartOnRest(32052200)
def Event_32052200(
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
    """Event 32052200"""
    if ThisEventSlotFlagEnabled():
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
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    End()


@RestartOnRest(32052250)
def Event_32052250(
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
    """Event 32052250"""
    if FlagEnabled(flag):
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
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    End()


@RestartOnRest(32052270)
def Event_32052270(
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
    """Event 32052270"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(flag):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        EnableCharacterCollision(character)
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
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        DisableCharacterCollision(character)
    End()


@RestartOnRest(32052400)
def Event_32052400():
    """Event 32052400"""
    GotoIfCharacterHasSpecialEffect(Label.L0, character=m31_18_Characters.MalformedStar, special_effect=16747)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32052401))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(m31_18_Characters.MalformedStar, 16747)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    Restart()


@RestartOnRest(32052800)
def Event_32052800():
    """Event 32052800"""
    if FlagEnabled(32050800):
        return
    AND_1.Add(HealthValue(Characters.Crystalian0) <= 0)
    AND_1.Add(HealthValue(Characters.Crystalian1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Crystalian0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(HealthValue(Characters.Crystalian0) == 0)
    AND_2.Add(HealthValue(Characters.Crystalian1) == 0)
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.Crystalian0, banner_type=BannerType.EnemyFelled)
    EnableFlag(32050800)
    EnableFlag(9265)
    if PlayerInOwnWorld():
        EnableFlag(61265)


@RestartOnRest(32052810)
def Event_32052810():
    """Event 32052810"""
    GotoIfFlagDisabled(Label.L0, flag=32050800)
    DisableCharacter(Characters.Crystalian0)
    DisableCharacter(Characters.Crystalian1)
    DisableAnimations(Characters.Crystalian0)
    DisableAnimations(Characters.Crystalian1)
    Kill(Characters.Crystalian0)
    Kill(Characters.Crystalian1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Crystalian0)
    DisableAI(Characters.Crystalian1)
    GotoIfFlagEnabled(Label.L1, flag=32050801)
    ForceAnimation(Characters.Crystalian0, 30000, loop=True)
    ForceAnimation(Characters.Crystalian1, 30000, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=32052801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Crystalian0, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Crystalian1, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableNetworkFlag(32050801)
    ForceAnimation(Characters.Crystalian0, 20000)
    ForceAnimation(Characters.Crystalian1, 20000)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.Crystalian0, 30000, loop=True)
    ForceAnimation(Characters.Crystalian1, 30000, loop=True)
    AND_2.Add(FlagEnabled(32052805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=32052800))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.Crystalian0, 20000)
    ForceAnimation(Characters.Crystalian1, 20000)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Crystalian0)
    EnableAI(Characters.Crystalian1)
    SetNetworkUpdateRate(Characters.Crystalian0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.Crystalian1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Crystalian0, name=903350321)
    EnableBossHealthBar(Characters.Crystalian1, name=903350322, bar_slot=1)


@RestartOnRest(32052811)
def Event_32052811():
    """Event 32052811"""
    if FlagEnabled(32050800):
        return
    AND_1.Add(HealthRatio(Characters.Crystalian0) <= 0.6000000238418579)
    AND_1.Add(HealthRatio(Characters.Crystalian0) <= 0.6000000238418579)
    OR_1.Add(AND_1)
    OR_1.Add(CharacterDead(Characters.Crystalian0))
    OR_1.Add(CharacterDead(Characters.Crystalian1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(32052802)


@RestartOnRest(32052820)
def Event_32052820():
    """Event 32052820"""
    if FlagEnabled(32050800):
        return
    if FlagEnabled(32050801):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(32058590):
        return
    DisableFlag(32058590)


@RestartOnRest(32052849)
def Event_32052849():
    """Event 32052849"""
    CommonFunc_9005800(
        0,
        flag=32050800,
        entity=Assets.AEG099_003_9000,
        region=32052800,
        flag_1=32052805,
        character=32055800,
        action_button_id=10000,
        left=32050801,
        region_1=32052801,
    )
    CommonFunc_9005801(
        0,
        flag=32050800,
        entity=Assets.AEG099_003_9000,
        region=32052800,
        flag_1=32052805,
        flag_2=32052806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=32050800, asset=Assets.AEG099_003_9000, model_point=7, right=32050801)
    CommonFunc_9005822(0, 32050800, 931000, 32052805, 32052806, 0, 32052802, 0, 0)
