"""
Land of Shadow 11-11 SE NE

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
    RegisterGrace(grace_flag=2047450000, asset=2047451950)
    CommonFunc_90005870(0, character=2047450800, name=905840501, npc_threat_level=12)
    CommonFunc_90005860(0, flag=2047450800, left=0, character=2047450800, left_1=0, item_lot=30955, seconds=0.0)
    CommonFunc_90005250(0, character=2047450800, region=2047452292, seconds=0.0, animation_id=-1)
    CommonFunc_90005872(0, character=2047450800, npc_threat_level=12, right=0)
    CommonFunc_90005250(0, character=2047450203, region=2047452203, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450204, region=2047452310, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2047450208, radius=18.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450214, region=2047452216, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450235, region=2047452216, seconds=1.0, animation_id=-1)
    CommonFunc_90005251(0, character=2047450222, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450236, region=2047452236, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450223, region=2047452223, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=2047450224, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047450310, region=2047452310, seconds=0.0, animation_id=-1)
    CommonFunc_90005301(0, flag=2047450380, character=2047450380, item_lot__unk1=2047450700, seconds=6.0, unk1=0)
    CommonFunc_90005557(0, entity=2047451680)
    CommonFunc_90005557(0, entity=2047451681)
    CommonFunc_90005557(0, entity=2047451682)
    CommonFunc_90005557(0, entity=2047451683)
    CommonFunc_90005557(0, entity=2047451684)
    CommonFunc_90005557(0, entity=2047451685)
    CommonFunc_90005557(0, entity=2047451686)
    CommonFunc_90005557(0, entity=2047451687)
    CommonFunc_90005557(0, entity=2047451688)
    CommonFunc_90005556(0, asset=2047451689, flag=2047457800)
    Event_2047452580()
    Event_2047452540(0, flag=2047450540, region=2047452540)


@RestartOnRest(2047452540)
def Event_2047452540(_, flag: Flag | int, region: Region | int):
    """Event 2047452540"""
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    End()


@ContinueOnRest(2047452580)
def Event_2047452580():
    """Event 2047452580"""
    RegisterLadder(start_climbing_flag=2047450580, stop_climbing_flag=2047450581, asset=2047451580)
    RegisterLadder(start_climbing_flag=2047450582, stop_climbing_flag=2047450583, asset=2047451582)
    RegisterLadder(start_climbing_flag=2047450584, stop_climbing_flag=2047450585, asset=2047451584)
    RegisterLadder(start_climbing_flag=2047450586, stop_climbing_flag=2047450587, asset=2047451586)
