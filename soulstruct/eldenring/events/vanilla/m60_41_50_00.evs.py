"""
South Altus Plateau (NW) (SE)

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
from .entities.m60_41_50_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.FallingstarBeast, name=904680602, npc_threat_level=19)
    CommonFunc_90005860(
        0,
        flag=1041500800,
        left=0,
        character=Characters.FallingstarBeast,
        left_1=0,
        item_lot=30310,
        seconds=0.0,
    )
    Event_1041502200()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005201(0, 1041500800, 30009, 20009, 30.0, 0.0, 0, 0, 0, 0)


@RestartOnRest(1041502200)
def Event_1041502200():
    """Event 1041502200"""
    GotoIfFlagEnabled(Label.L0, flag=1041500800)
    
    MAIN.Await(SpecialStandbyEndedFlagEnabled(character=Characters.FallingstarBeast))

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(1041502200, erase_root_only=False)
    End()
