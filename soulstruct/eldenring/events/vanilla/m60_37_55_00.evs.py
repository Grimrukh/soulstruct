"""
West Altus Plateau (NW) (NE)

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
from .enums.m60_37_55_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    DisableCharacterCollision(0)
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanShaman0,
        region=1037552200,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        1,
        character=Characters.DemiHumanShaman1,
        region=1037552200,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_1037552200(0, character=Characters.DemiHumanShaman0, region=1037552200)
    Event_1037552200(1, character=Characters.DemiHumanShaman1, region=1037552200)
    CommonFunc_90005261(0, character=Characters.Dummy, region=1037552205, radius=10.0, seconds=0.0, animation_id=0)


@RestartOnRest(1037552200)
def Event_1037552200(_, character: Character | int, region: Region | int):
    """Event 1037552200"""
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    End()
