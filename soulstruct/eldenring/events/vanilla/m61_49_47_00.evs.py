"""
Land of Shadow 12-11 NW NE

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
    RegisterGrace(grace_flag=2049470000, asset=2049471950)
    Event_2049472505()


@RestartOnRest(2049472505)
def Event_2049472505():
    """Event 2049472505"""
    DisableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(Multiplayer())
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButtonParamActivated(action_button_id=209620, entity=21001576))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=2049472020)
    SaveRequest()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=21000000,
        cutscene_flags=0,
        move_to_region=2049472020,
        map_id=61494700,
        player_id=10000,
        unk_20_24=21000000,
        unk_24_25=False,
    )
    WaitRealFrames(frames=1)
    PlayCutscene(21000010, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFrames(frames=1)
    Wait(1.0)
