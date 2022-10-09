"""
Southwest Mountaintops (NE) (NW)

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
from .entities.m60_50_55_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005211(
        0,
        character=Characters.GravenSchool0,
        animation_id=30000,
        animation_id_1=20000,
        region=1050552300,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GravenSchool1,
        animation_id=30000,
        animation_id_1=20000,
        region=1050552300,
        radius=0.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.GravenSchool2,
        animation_id=30000,
        animation_id_1=20000,
        region=1050552302,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1050558600)
    CommonFunc_90005636(
        0,
        flag=1050558600,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect=4470,
        destination=1050552600,
        region=1050552601,
        flag_1=1050552600,
        patrol_information_id=1050553600,
        right=0,
    )
    CommonFunc_90005637(0, flag=1050558600, character=Characters.WanderingNoble, region=1050552601)
