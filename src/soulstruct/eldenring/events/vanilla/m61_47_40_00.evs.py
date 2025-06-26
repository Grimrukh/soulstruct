"""
Land of Shadow 11-10 SE SE

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
    RegisterGrace(grace_flag=2047400000, asset=2047401950, enemy_block_distance=0.0)
    CommonFunc_90005250(0, character=2047400300, region=2047402300, seconds=0.0, animation_id=3004)
    CommonFunc_90005211(
        0,
        character=2047400400,
        animation_id=30016,
        animation_id_1=20016,
        region=2047402400,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047400401,
        animation_id=30016,
        animation_id_1=20016,
        region=2047402400,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047400402,
        animation_id=30016,
        animation_id_1=20016,
        region=2047402400,
        radius=0.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005301(0, flag=2047400499, character=2047400499, item_lot__unk1=2047400980, seconds=0.0, unk1=0)
    CommonFunc_90005271(0, character=2047400250, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=2047400252, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=2047400257, seconds=0.0, animation_id=-1)
    CommonFunc_90005557(0, entity=2047401670)
    CommonFunc_90005557(0, entity=2047401671)
    CommonFunc_90005557(0, entity=2047401672)
    CommonFunc_90005557(0, entity=2047401673)
    CommonFunc_90005557(0, entity=2047401674)
    CommonFunc_90005557(0, entity=2047401675)
    CommonFunc_90005557(0, entity=2047401676)
    CommonFunc_90005557(0, entity=2047401677)
    CommonFunc_90005557(0, entity=2047401678)
    CommonFunc_90005557(0, entity=2047401679)
    CommonFunc_90005556(0, asset=2047401689, flag=2047407900)
    Event_2047402200(0, character=2047400450, region=2047402450, region_1=2047402460, radius=2.0)
    Event_2047402200(1, character=2047400451, region=2047402451, region_1=2047402461, radius=2.0)
    Event_2047402200(2, character=2047400452, region=2047402452, region_1=2047402462, radius=2.0)


@RestartOnRest(2047402499)
def Event_2047402499(_, flag: Flag | int, character: uint, item_lot: int, seconds: float, left: int):
    """Event 2047402499"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    if ValueNotEqual(left=left, right=0):
        DisableCharacter(character)
        DropMandatoryTreasure(character)
        End()
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterProportionDead(character=character))
    
    Wait(seconds)
    EnableFlag(flag)
    if PlayerNotInOwnWorld():
        return
    if ValueEqual(left=left, right=1):
        return
    AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(2047402200)
def Event_2047402200(_, character: uint, region: Region | int, region_1: Region | int, radius: float):
    """Event 2047402200"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=20011469):
        AddSpecialEffect(character, 20011469)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_4.Add(OR_2)
    GotoIfConditionFalse(Label.L0, input_condition=OR_4)
    AddSpecialEffect(character, 20011468)
    ForceAnimation(character, 3020)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 20011467)
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=5025):
        ForceAnimation(character, 3000)
    Wait(1.0)
    Restart()
