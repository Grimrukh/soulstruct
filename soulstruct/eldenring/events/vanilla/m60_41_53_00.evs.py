"""
North Altus Plateau (SW) (NE)

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
from .entities.m60_41_53_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.WormfaceLarge, name=904580600, npc_threat_level=8)
    CommonFunc_90005860(
        0,
        flag=1041530800,
        left=0,
        character=Characters.WormfaceLarge,
        left_1=0,
        item_lot__item_lot_param_id=30320,
        seconds=0.0,
    )
    CommonFunc_90005636(
        0,
        flag=32058691,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect_id=4470,
        destination=1041532650,
        region=1041532651,
        flag_1=1041532650,
        patrol_information_id=1041533650,
        right=0,
    )
    CommonFunc_90005637(0, flag=32058691, character=Characters.WanderingNoble, region=1041531650)
    CommonFunc_90005300(0, 1041530500, 1041530500, 40308, 0.0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.Wormface6,
        region=1041532362,
        radius=3.0,
        seconds=0.0,
        animation_id=3010,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface7,
        animation_id=30000,
        animation_id_1=20000,
        region=1041532365,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface4,
        animation_id=30001,
        animation_id_1=20001,
        region=1041532357,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Wormface5, region=1041532361, seconds=0.0, animation_id=3011)
    CommonFunc_90005201(0, 1041530800, 30000, 20000, 15.0, 0.0, 0, 0, 0, 0)
