"""
West Weeping Peninsula (NE) (SW)

linked:
0
72
154

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_34_00_entities import *
from .entities.m60_43_34_00_entities import Characters as m60_43_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(0, character=Characters.Page0, region=1042342210, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Page1, region=1042342210, radius=5.0, seconds=1.0, animation_id=0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, character=Characters.GiantOctopus)
    CommonFunc_90005706(0, character=m60_43_Characters.Commoner, animation_id=30025, left=0)
