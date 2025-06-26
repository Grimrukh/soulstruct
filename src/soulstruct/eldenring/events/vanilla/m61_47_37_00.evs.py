"""
Land of Shadow 11-09 SE NE

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
    CommonFunc_90005201(
        0,
        character=2047370210,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370211,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370212,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370213,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370214,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370220,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370221,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370222,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370223,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370224,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370225,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370226,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370227,
        animation_id=30002,
        animation_id_1=20002,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370228,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047370229,
        animation_id=30002,
        animation_id_1=20002,
        radius=25.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005301(0, flag=2047370300, character=2047370300, item_lot__unk1=2047370010, seconds=6.0, unk1=0)


@RestartOnRest(2047372200)
def Event_2047372200(_, character: uint, radius: float):
    """Event 2047372200"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, 701, loop=True)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(AND_2)
    
    SetSpecialStandbyEndedFlag(character=character, state=True)
    ForceAnimation(character, 1701, wait_for_completion=True)
