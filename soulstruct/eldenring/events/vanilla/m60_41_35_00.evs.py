"""
West Weeping Peninsula (NW) (NE)

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
from .enums.m60_41_35_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1041350000, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005300(0, flag=1041350210, character=Characters.Scarab, item_lot=40144, seconds=0.0, left=0)
    Event_1041350700(0, character=Characters.Dummy)
    Event_1041350701()
    CommonFunc_90005708(0, character=Characters.Dummy, flag=6001, left=0)
    Event_1041353702()


@RestartOnRest(1041352680)
def Event_1041352680():
    """Event 1041352680"""
    CreateAssetVFX(Assets.AEG003_316_9000, vfx_id=100, model_point=800)


@RestartOnRest(1041350700)
def Event_1041350700(_, character: uint):
    """Event 1041350700"""
    DisableGravity(character)
    DisableCharacterCollision(character)


@RestartOnRest(1041350701)
def Event_1041350701():
    """Event 1041350701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9611))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9612))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60510)
    Wait(0.20000000298023224)
    Restart()


@RestartOnRest(1041353702)
def Event_1041353702():
    """Event 1041353702"""
    DisableFlag(1041359950)
    if PlayerNotInOwnWorld():
        return
    EnableFlag(1041359950)
    End()
