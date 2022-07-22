"""
West Liurnia (NE) (SW)

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
from .entities.m60_34_46_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034460000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005920(0, 1034460600, 1034461600, 1034463600)


@RestartOnRest(1034462210)
def Event_1034462210(_, entity: uint):
    """Event 1034462210"""
    ForceAnimation(entity, 30000)
    DisableAsset(1038461210)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1034462210))
    
    EnableAsset(1038461210)
    Wait(3.0)
    ForceAnimation(entity, 20000)
    Wait(6.0)
    DisableAsset(1038461210)
    End()
