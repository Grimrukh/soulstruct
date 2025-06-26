"""
Land of Shadow 12-09 NW SE

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005706(0, character=2049380700, animation_id=30014, left=2049382700)
    Event_2049380700(0, asset=2049381700, character=2049380700)


@RestartOnRest(2049380700)
def Event_2049380700(_, asset: Asset | int, character: Character | int):
    """Event 2049380700"""
    WaitFrames(frames=1)
    EnableAssetInvulnerability(asset)
    MoveAssetToCharacter(asset, character=character)
    End()
