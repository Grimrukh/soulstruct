"""
Land of Shadow 12-09 NE NE

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
    CommonFunc_90005250(0, character=2051390200, region=2051392200, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=2051390300,
        animation_id=30003,
        animation_id_1=20003,
        region=2051392300,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2051390301,
        animation_id=30003,
        animation_id_1=20003,
        region=2051392301,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2051390302,
        animation_id=30003,
        animation_id_1=20003,
        region=2051392302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(2051392200)
def Event_2051392200(_, character: Character | int):
    """Event 2051392200"""
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 20011075))
    AddSpecialEffect(character, 20011073)


@RestartOnRest(2051392210)
def Event_2051392210(_, character: Character | int, character_1: Character | int):
    """Event 2051392210"""
    AND_1.Add(CharacterHasSpecialEffect(character, 20011075))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 20011076)
    Wait(10.0)
    AddSpecialEffect(character_1, 20011073)
