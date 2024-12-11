"""
Land of Shadow 11-11 (Alternate) NE NE

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
    RegisterGrace(grace_flag=76940, asset=2047471950)
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=76940,
        asset=2047471980,
        source_flag=77900,
        value=2,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
    Event_2047472200(0, attacker__character=2047475200, region=2047472200)
    Event_2047472201(0, character=2047475201)
    Event_2047472202(0, character=2047475202)
    Event_2047472203(0, character=2047475203)
    CommonFunc_90005201(
        0,
        character=2047470200,
        animation_id=30006,
        animation_id_1=20006,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005501(
        0,
        flag=2047470510,
        flag_1=2047470511,
        left=1,
        asset=2047471510,
        asset_1=2047471511,
        asset_2=2047471512,
        flag_2=2047470512,
    )
    Event_2047472510()
    CommonFunc_900005610(0, asset=2047472500, dummy_id=100, vfx_id=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_2047470050()


@ContinueOnRest(2047470050)
def Event_2047470050():
    """Event 2047470050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(2047470510)


@RestartOnRest(2047472200)
def Event_2047472200(_, attacker__character: uint, region: Region | int):
    """Event 2047472200"""
    RemoveSpecialEffect(attacker__character, 90020)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(2047472200):
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
    
    EnableNetworkFlag(2047472200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(2047472201)
def Event_2047472201(_, character: Character | int):
    """Event 2047472201"""
    AddSpecialEffect(character, 4404)
    End()


@RestartOnRest(2047472202)
def Event_2047472202(_, character: Character | int):
    """Event 2047472202"""
    AddSpecialEffect(character, 4405)


@RestartOnRest(2047472203)
def Event_2047472203(_, character: Character | int):
    """Event 2047472203"""
    AddSpecialEffect(character, 4401)


@ContinueOnRest(2047472510)
def Event_2047472510():
    """Event 2047472510"""
    CommonFunc_90005500(
        0,
        flag=2047470510,
        flag_1=2047470511,
        left=1,
        asset=2047471510,
        asset_1=2047471511,
        obj_act_id=2047473511,
        asset_2=2047471512,
        obj_act_id_1=2047473512,
        region=2047472511,
        region_1=2047472512,
        flag_2=2047470512,
        flag_3=2047470513,
        left_1=0,
    )
