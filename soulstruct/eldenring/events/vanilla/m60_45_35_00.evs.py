"""
East Weeping Peninsula (NW) (NE)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@RestartOnRest(1045352200)
def Event_1045352200():
    """Event 1045352200"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=1045350200, radius=30.0))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(1045350200, 3011)
    End()
