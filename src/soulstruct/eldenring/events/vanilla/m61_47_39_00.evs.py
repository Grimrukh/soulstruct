"""
Land of Shadow 11-09 NE NE

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
    RegisterGrace(grace_flag=2047390000, asset=2047391950, enemy_block_distance=0.0)
    CommonFunc_90005211(
        0,
        character=2047390800,
        animation_id=30000,
        animation_id_1=20000,
        region=2047392800,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=2047390800, name=906260600, npc_threat_level=24)
    CommonFunc_90005860(0, flag=2047390800, left=0, character=2047390800, left_1=0, item_lot=30855, seconds=0.0)
    CommonFunc_90005211(
        0,
        character=2047390200,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047390201,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047390202,
        animation_id=30016,
        animation_id_1=20016,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047390203,
        animation_id=30016,
        animation_id_1=20016,
        region=2047392201,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047390204,
        animation_id=30016,
        animation_id_1=20016,
        region=2047392201,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047390205,
        animation_id=30016,
        animation_id_1=20016,
        region=2047392201,
        radius=0.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005301(0, flag=2047390300, character=2047390400, item_lot__unk1=2047390070, seconds=3.0, unk1=0)
