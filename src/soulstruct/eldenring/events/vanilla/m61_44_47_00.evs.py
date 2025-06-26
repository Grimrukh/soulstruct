"""
Land of Shadow 11-11 NW NW

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
    CommonFunc_90005870(0, character=2044470800, name=905820600, npc_threat_level=16)
    CommonFunc_90005860(0, flag=2044470800, left=0, character=2044470800, left_1=0, item_lot=30910, seconds=0.0)
    CommonFunc_90005872(0, character=2044470800, npc_threat_level=16, right=2044472802)
    Event_2044472810()
    CommonFunc_90005557(0, entity=2044471680)
    CommonFunc_90005557(0, entity=2044471681)
    CommonFunc_90005557(0, entity=2044471682)
    CommonFunc_90005557(0, entity=2044471683)
    CommonFunc_90005557(0, entity=2044471684)
    CommonFunc_90005557(0, entity=2044471685)
    CommonFunc_90005557(0, entity=2044471686)
    CommonFunc_90005557(0, entity=2044471687)
    CommonFunc_90005557(0, entity=2044471688)
    CommonFunc_90005556(0, asset=2044471689, flag=2044477900)
    CommonFunc_90005501(
        0,
        flag=2044470510,
        flag_1=2044470511,
        left=1,
        asset=2044471510,
        asset_1=2044471511,
        asset_2=2044471512,
        flag_2=2044470512,
    )
    Event_2044472510()


@ContinueOnRest(2044470050)
def Event_2044470050():
    """Event 2044470050"""
    if ThisEventSlotFlagEnabled():
        return


@ContinueOnRest(2044472810)
def Event_2044472810():
    """Event 2044472810"""
    if FlagEnabled(2044470800):
        return
    if FlagDisabled(2044472802):
        MAIN.Await(CharacterHasSpecialEffect(2044470800, 20010130))
    EnableNetworkFlag(2044472802)
    End()


@ContinueOnRest(2044472510)
def Event_2044472510():
    """Event 2044472510"""
    CommonFunc_90005500(
        0,
        flag=2044470510,
        flag_1=2044470511,
        left=1,
        asset=2044471510,
        asset_1=2044471511,
        obj_act_id=2044473511,
        asset_2=2044471512,
        obj_act_id_1=2044473512,
        region=2044472511,
        region_1=2044472512,
        flag_2=2044470512,
        flag_3=2044470513,
        left_1=0,
    )
