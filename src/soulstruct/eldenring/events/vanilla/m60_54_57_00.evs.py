"""
Northeast Mountaintops (SE) (NW)

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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1054572200(0, character=1054575200)


@RestartOnRest(1054572200)
def Event_1054572200(_, character: uint):
    """Event 1054572200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()
