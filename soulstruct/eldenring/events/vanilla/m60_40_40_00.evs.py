"""
Northwest Limgrave Coast (SW) (SW)

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
from .enums.m60_40_40_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=Characters.Wolf, region=1040402206, radius=10.0, seconds=0.0, animation_id=3011)
    Event_1040402200(0, character=Characters.WanderingNoble0)
    Event_1040402200(1, character=Characters.WanderingNoble1)
    Event_1040402200(2, character=Characters.WanderingNoble2)
    Event_1040402200(3, character=Characters.RayaLucariaSoldier0)
    Event_1040402200(4, character=Characters.RayaLucariaSoldier1)
    Event_1040402200(5, character=Characters.RayaLucariaSoldier2)
    Event_1040402200(6, character=Characters.RayaLucariaFootSoldier0)
    Event_1040402200(7, character=Characters.RayaLucariaFootSoldier1)
    Event_1040402200(8, character=Characters.RayaLucariaFootSoldier2)
    Event_1040402220(0, character=Characters.Troll)
    CommonFunc_90005423(0, character=Characters.Troll)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005422(0, flag=1040408500, asset=Assets.AEG100_101_1000, obj_act_id=1040403500)


@RestartOnRest(1040402200)
def Event_1040402200(_, character: uint):
    """Event 1040402200"""
    Kill(character)
    End()


@RestartOnRest(1040402220)
def Event_1040402220(_, character: uint):
    """Event 1040402220"""
    AddSpecialEffect(character, 5551)
    End()
