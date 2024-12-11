"""
Land of Shadow 12-12 SW NE

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


@ContinueOnRest(2049492500)
def Event_2049492500():
    """Event 2049492500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2049492500):
        return
    if FlagEnabled(124):
        return
    DeleteAssetVFX(2049491500)
    CreateAssetVFX(2049491500, dummy_id=90, vfx_id=6102)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9512, entity=2049491500))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(2049492500)
    EnableNetworkFlag(124)
    Wait(1.0)
    DeleteAssetVFX(2049491500, erase_root=False)
