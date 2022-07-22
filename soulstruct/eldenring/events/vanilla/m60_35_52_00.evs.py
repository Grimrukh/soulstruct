"""
Far West Altus Plateau (SE) (SE)

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
from .entities.m60_35_52_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1035522200(0, character=Characters.DemiHuman2)
    Event_1035522200(1, character=Characters.DemiHuman0)
    Event_1035522200(2, 1035520202)


@RestartOnRest(1035522200)
def Event_1035522200(_, character: uint):
    """Event 1035522200"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    ForceAnimation(character, 3015, skip_transition=True)
    End()
