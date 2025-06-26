"""
Land of Shadow 12-11 NW SE

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
    CommonFunc_90005557(0, entity=2049461680)
    CommonFunc_90005557(0, entity=2049461681)
    CommonFunc_90005557(0, entity=2049461682)
    CommonFunc_90005557(0, entity=2049461683)
    CommonFunc_90005557(0, entity=2049461684)
    CommonFunc_90005557(0, entity=2049461685)
    CommonFunc_90005557(0, entity=2049461686)
    CommonFunc_90005557(0, entity=2049461687)
    CommonFunc_90005556(0, asset=2049461688, flag=2049467900)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2049460180,
        summon_flag=2049462181,
        dismissal_flag=2049462182,
        character=2049460710,
        sign_type=22,
        region=2049462710,
        region_1=2049462711,
        seconds=0.0,
        right_1=2045429291,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2049460180, flag_1=2049462181, flag_2=2049462182, character=2049460710)
    CommonFunc_90005792(
        0,
        flag=2049460180,
        flag_1=2049462181,
        flag_2=2049462182,
        character=2049460710,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2049460180,
        flag_1=2049462181,
        flag_2=2049462182,
        character=2049460710,
        other_entity=2049462710,
        region=0,
        left=0,
    )
    CommonFunc_90005774(0, flag=2049460180, item_lot=116401, flag_1=400645)
    CommonFunc_90005757(
        0,
        character=2049460700,
        character_1=2049460701,
        flag=4385,
        flag_1=4951,
        flag_2=2045422710,
        flag_3=4383,
    )
    CommonFunc_90005759(
        0,
        flag=2045429280,
        flag_1=4385,
        flag_2=4961,
        character=2049460700,
        flag_3=4951,
        flag_4=2045429291,
        first_flag=4950,
        last_flag=4956,
        flag_5=2045429281,
        flag_6=2045429282,
        flag_7=4901,
        seconds=1.0,
        flag_8=2045429341,
        radius=30.0,
    )
    CommonFunc_90005778(0, flag=2049462700, flag_1=4951, flag_2=400751, attacked_entity=2049460700)
    CommonFunc_90005779(0, character=2049460700, flag=4951, animation_id=20016, flag_1=4385, flag_2=4383)
    CommonFunc_90005744(0, entity=2049460700, flag=2049469200, flag_1=2049469200, animation_id=20015)
    CommonFunc_90005766(0, flag=2049462181, character=2049460710, distance=100.0, flag_1=2045429277, flag_2=4961)
    CommonFunc_90005767(
        0,
        flag=2045429280,
        first_flag=4380,
        last_flag=4383,
        character=2049460710,
        flag_1=4901,
        character_1=2049460711,
        flag_2=2045429297,
    )
    CommonFunc_90005777(0, character=2049460711, flag=4961, flag_1=4383, flag_2=2049462181)
    CommonFunc_90005774(0, flag=2045429297, item_lot=116401, flag_1=400645)
