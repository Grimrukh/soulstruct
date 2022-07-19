"""
North Caelid (SE) (SE)

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
from .entities.m60_51_40_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005633(
        0,
        character=580360,
        flag=580060,
        character_1=Characters.WanderingNoble,
        animation_id=30017,
        animation_id_1=20017,
        asset=Assets.AEG099_166_9000,
        asset_1=Assets.AEG099_990_9000,
    )
    CommonFunc_90005870(0, character=Characters.PutridAvatar, name=904811601, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1051400800,
        left=0,
        character=Characters.PutridAvatar,
        left_1=0,
        item_lot__item_lot_param_id=30415,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.PutridAvatar, npc_threat_level=18, right=0)
    CommonFunc_90005250(0, character=Characters.ErdtreeGuardian0, region=1051402200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ErdtreeGuardian1, region=1051402200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ErdtreeGuardian2, region=1051402200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GuardianGolem, region=1051402300, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, 1051400300, 7.0, 0.0, -1)
