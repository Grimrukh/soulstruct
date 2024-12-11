"""
Land of Shadow 11-10 NE NE

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
    RegisterGrace(grace_flag=2047430000, asset=2047431950, enemy_block_distance=0.0)
    CommonFunc_90005301(0, flag=2047430300, character=2047430300, item_lot__unk1=2047430980, seconds=0.0, unk1=0)
    CommonFunc_90005261(0, character=2047430203, region=2047432203, radius=10.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=2047430212, region=2047432203, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2047430213, region=2047432203, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2047430217, region=2047432203, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=2047430218, region=2047432203, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=2047430300,
        animation_id=30002,
        animation_id_1=20002,
        region=2047432300,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2047430214, region=2047432203, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047430215, region=2047432203, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047430216, region=2047432203, seconds=0.0, animation_id=0)
    Event_2047432222(0, attacker__character=2047435201, region=2047432201)
    Event_2047432240(0, attacker__character=2047435202, region=2047432202)


@RestartOnRest(2047432222)
def Event_2047432222(_, attacker__character: uint, region: Region | int):
    """Event 2047432222"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 90020)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(2047432222):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 90020)
    AddSpecialEffect(attacker__character, 5650)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2047432222)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(2047432240)
def Event_2047432240(_, attacker__character: uint, region: Region | int):
    """Event 2047432240"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 90020)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(2047432240):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 90020)
    AddSpecialEffect(attacker__character, 5650)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2047432240)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(2047432250)
def Event_2047432250(_, character: Character | int):
    """Event 2047432250"""
    AddSpecialEffect(character, 20007030)
