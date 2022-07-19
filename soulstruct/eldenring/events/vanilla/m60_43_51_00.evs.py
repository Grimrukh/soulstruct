"""
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
from .entities.m60_43_51_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005300(0, 1043510500, 1043510500, 40314, 0.0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.Slug0,
        animation_id=30000,
        animation_id_1=20000,
        region=1043512400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug1,
        animation_id=30001,
        animation_id_1=20001,
        region=1043512400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug2,
        animation_id=30001,
        animation_id_1=20001,
        region=1043512400,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug3,
        animation_id=30001,
        animation_id_1=20001,
        region=1043512400,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1043510404, 30001, 20001, 1043512400, 0.0, 0, 0, 0, 0)
