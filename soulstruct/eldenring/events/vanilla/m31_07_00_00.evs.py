"""
Seethewater Cave

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
from .entities.m31_07_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31070000, asset=Assets.AEG099_060_9000)
    Event_31072800()
    Event_31072801()
    Event_31072802()
    Event_31042810()
    Event_31042849()
    Event_31072811()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005261(0, character=31070400, region=31072400, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat0, region=31072290, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Rat1,
        region=31072290,
        radius=3.0,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005250(0, character=Characters.Rat2, region=31072295, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Rat3, region=31072295, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Rat4, region=31072297, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=31070298, region=31072297, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=31070299, region=31072297, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.Rat5, radius=6.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.GiantRat, region=31072290, radius=3.0, seconds=0.5, animation_id=0)
    Event_31072280(0, character=Characters.Rat0)
    Event_31072280(1, character=Characters.Rat1)
    Event_31072280(2, character=Characters.GiantRat)
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass0,
        animation_id=30000,
        animation_id_1=20000,
        region=31072250,
        radius=0.0,
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
        region=31072251,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass2,
        animation_id=30000,
        animation_id_1=20000,
        region=31072252,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass3,
        animation_id=30000,
        animation_id_1=20000,
        region=31072254,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass4,
        animation_id=30000,
        animation_id_1=20000,
        region=31072254,
        radius=0.0,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass5,
        animation_id=30000,
        animation_id_1=20000,
        region=31072257,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LivingMass6,
        animation_id=30000,
        animation_id_1=20000,
        region=31072258,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier0, region=31072200, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellSoldier1,
        animation_id=30002,
        animation_id_1=20002,
        region=31072201,
        radius=0.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.FungalSorcerer0, region=31072210, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer1,
        region=31072400,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer2,
        region=31072400,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer3,
        region=31072400,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer4,
        region=31072400,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer5,
        region=31072400,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=31070218, region=31072400, radius=1.0, seconds=0.0, animation_id=0)
    Event_31072213(0, character=Characters.FungalSorcerer1, region=31072213)
    Event_31072213(1, character=Characters.FungalSorcerer2, region=31072213)
    Event_31072213(2, character=Characters.FungalSorcerer3, region=31072213)
    Event_31072213(3, character=Characters.FungalSorcerer4, region=31072213)
    Event_31072213(4, character=Characters.FungalSorcerer5, region=31072213)
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer6,
        region=31072225,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer7,
        region=31072225,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer8,
        region=31072225,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_310722205(0, character=Characters.FungalSorcerer6)
    Event_310722205(1, character=Characters.FungalSorcerer7)
    Event_310722205(2, character=Characters.FungalSorcerer8)
    Event_31072225(0, character=Characters.FungalSorcerer6)
    Event_31072225(1, character=Characters.FungalSorcerer7)
    Event_31072225(2, character=Characters.FungalSorcerer8)
    CommonFunc_90005261(
        0,
        character=Characters.FungalSorcerer9,
        region=31072230,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31072230(
        1,
        character=Characters.FungalSorcerer10,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31072230(
        2,
        character=Characters.FungalSorcerer11,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31072230(
        3,
        character=Characters.FungalSorcerer12,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31072230(
        4,
        character=Characters.FungalSorcerer13,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GiantMirandaFlower,
        animation_id=30001,
        animation_id_1=20001,
        region=31072350,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=31070320,
        animation_id=30000,
        animation_id_1=30001,
        region=0,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=31070321,
        animation_id=30000,
        animation_id_1=30001,
        region=0,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=31070322,
        animation_id=30000,
        animation_id_1=30001,
        region=0,
        radius=4.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005646(
        0,
        flag=31070800,
        left_flag=31072840,
        cancel_flag__right_flag=31072841,
        asset=Assets.AEG099_065_9000,
        player_start=31072840,
        area_id=31,
        block_id=7,
        cc_id=0,
        dd_id=0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Rat6, region=31072302, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat7, region=31072302, radius=1.0, seconds=0.0, animation_id=0)
    Event_310722300(0, character=Characters.Rat6, seconds=10.0)
    Event_310722300(1, character=Characters.Rat7, seconds=11.0)


@RestartOnRest(31072213)
def Event_31072213(_, character: uint, region: uint):
    """Event 31072213"""
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
    AND_2.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
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
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31072220)
def Event_31072220(_, character: uint):
    """Event 31072220"""
    AND_15.Add(CharacterDead(character))
    if AND_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 8081))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=31072225))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    Restart()


@RestartOnRest(310722205)
def Event_310722205(_, character: uint):
    """Event 310722205"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_10.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_10.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_9)
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterHasSpecialEffect(character, 8081))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31072225))
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
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)


@RestartOnRest(31072225)
def Event_31072225(_, character: uint):
    """Event 31072225"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8092)


@RestartOnRest(31072230)
def Event_31072230(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 31072230"""
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer9))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer10))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer11))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer12))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.FungalSorcerer13))
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
    OR_5.Add(AND_1)
    OR_5.Add(OR_2)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_5)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
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


@RestartOnRest(31072280)
def Event_31072280(_, character: uint):
    """Event 31072280"""
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
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(310722300)
def Event_310722300(_, character: uint, seconds: float):
    """Event 310722300"""
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
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=31072302))
    OR_5.Add(AND_1)
    
    MAIN.Await(OR_5)
    
    Wait(seconds)
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(31072800)
def Event_31072800():
    """Event 31072800"""
    if FlagEnabled(31070800):
        return
    AND_1.Add(CharacterDead(Characters.KindredofRot0))
    AND_1.Add(CharacterDead(Characters.KindredofRot1))
    
    MAIN.Await(AND_1)
    
    KillBossAndDisplayBanner(character=Characters.KindredofRot0, banner_type=BannerType.EnemyFelled)
    EnableFlag(31070800)
    EnableFlag(9239)
    if PlayerInOwnWorld():
        EnableFlag(61239)


@RestartOnRest(31072801)
def Event_31072801():
    """Event 31072801"""
    if FlagEnabled(31070800):
        return
    
    MAIN.Await(HealthValue(Characters.KindredofRot0) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.KindredofRot0, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31072802)
def Event_31072802():
    """Event 31072802"""
    if FlagEnabled(31070800):
        return
    
    MAIN.Await(HealthValue(Characters.KindredofRot1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.KindredofRot1, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31042810)
def Event_31042810():
    """Event 31042810"""
    GotoIfFlagDisabled(Label.L0, flag=31070800)
    DisableCharacter(Characters.KindredofRot0)
    DisableCharacter(Characters.KindredofRot1)
    DisableAnimations(Characters.KindredofRot0)
    DisableAnimations(Characters.KindredofRot1)
    Kill(Characters.KindredofRot0)
    Kill(Characters.KindredofRot1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.KindredofRot1, 30009, loop=True)
    DisableAI(Characters.KindredofRot0)
    DisableAI(Characters.KindredofRot1)
    AddSpecialEffect(Characters.KindredofRot0, 8092)
    AddSpecialEffect(Characters.KindredofRot1, 8092)
    AND_2.Add(FlagEnabled(31072805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31072800))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(31070801)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBossHealthBar(Characters.KindredofRot0, name=903810310)
    EnableBossHealthBar(Characters.KindredofRot1, name=903810311, bar_slot=1)
    EnableAI(Characters.KindredofRot0)
    EnableAI(Characters.KindredofRot1)
    SetNetworkUpdateRate(Characters.KindredofRot0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.KindredofRot1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    ForceAnimation(Characters.KindredofRot1, 20029)


@RestartOnRest(31072811)
def Event_31072811():
    """Event 31072811"""
    if FlagEnabled(31070800):
        return
    OR_15.Add(CharacterDead(Characters.KindredofRot0))
    OR_15.Add(CharacterDead(Characters.KindredofRot1))
    
    MAIN.Await(OR_15)
    
    EnableFlag(31072842)


@RestartOnRest(31042849)
def Event_31042849():
    """Event 31042849"""
    CommonFunc_9005800(
        0,
        flag=31070800,
        entity=Assets.AEG099_001_9000,
        region=31072800,
        flag_1=31072805,
        character=31075800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31070800,
        entity=Assets.AEG099_001_9000,
        region=31072800,
        flag_1=31072805,
        flag_2=31072806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=31070800, asset=Assets.AEG099_001_9000, model_point=5, right=0)
    CommonFunc_9005822(
        0,
        flag=31070800,
        bgm_boss_conv_param_id=931000,
        flag_1=31072805,
        flag_2=31072806,
        right=0,
        flag_3=31072842,
        left=0,
        left_1=0,
    )
