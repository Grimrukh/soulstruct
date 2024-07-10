"""
Southwest Liurnia (NW) (NE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_33_43_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.ErdtreeAvatar, name=904810600, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1033430800,
        left=0,
        character=Characters.ErdtreeAvatar,
        left_1=0,
        item_lot=30205,
        seconds=0.0,
    )
    CommonFunc_90005251(0, character=Characters.ErdtreeAvatar, radius=20.0, seconds=0.0, animation_id=0)
    CommonFunc_90005872(0, character=Characters.ErdtreeAvatar, npc_threat_level=18, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, dummy_id=100, vfx_id=800, right=1033438600)
    CommonFunc_90005300(0, flag=1033430200, character=Characters.Scarab, item_lot=40238, seconds=0.0, left=0)
