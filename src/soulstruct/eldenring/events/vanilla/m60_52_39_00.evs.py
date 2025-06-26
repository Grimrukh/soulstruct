"""
Southeast Caelid (NW) (NW)

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


@RestartOnRest(1052392699)
def Event_1052392699(_, asset: Asset | int):
    """Event 1052392699"""
    GotoIfFlagEnabled(Label.L0, flag=9411)
    GotoIfFlagEnabled(Label.L1, flag=1052380800)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(9411))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(asset)
    
    MAIN.Await(FlagEnabled(1052380800))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
