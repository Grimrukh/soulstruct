"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_35_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1042352222(0, character=1042350222, region=1042352222)
    Event_1042352222(1, character=Characters.Bat, region=1042352223)
    Event_1042352222(2, character=1042350224, region=1042352223)
    CommonFunc_90005633(0, 580340, 580040, 1042350600, 30017, 20017, 1042351600, 1042351610)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, 1042350210, 1042352210, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton0,
        animation_id=30016,
        animation_id_1=20016,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1042350200, 20.0, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton1,
        animation_id=30016,
        animation_id_1=20016,
        radius=20.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1042350201, 20.0, 1.0, -1)
    CommonFunc_90005201(
        0,
        character=Characters.Skeleton2,
        animation_id=30016,
        animation_id_1=20016,
        radius=20.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, 1042350202, 20.0, 1.5, -1)


@RestartOnRest(1042352222)
def Event_1042352222(_, character: uint, region: uint):
    """Event 1042352222"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(character, 8080)
