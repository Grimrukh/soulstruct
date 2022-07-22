"""
Liurnia to Altus Plateau (NW) (SW)

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
from .entities.m60_36_50_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1036500000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005880(
        0,
        flag=1036500800,
        flag_1=1036500805,
        flag_2=1036502800,
        character=Characters.OnyxLord,
        item_lot=30255,
        area_id=60,
        block_id=36,
        cc_id=50,
        dd_id=0,
        player_start=1036502805,
    )
    CommonFunc_90005881(
        0,
        flag=1036500800,
        flag_1=1036500805,
        left_flag=1036502801,
        cancel_flag__right_flag=1036502802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=36,
        cc_id=50,
        dd_id=0,
        player_start=1036502805,
    )
    CommonFunc_90005882(
        0,
        flag=1036500800,
        flag_1=1036500805,
        flag_2=1036502800,
        character=Characters.OnyxLord,
        flag_3=1036502806,
        character_1=1036505810,
        asset=Assets.AEG099_120_1000,
        owner_entity=Characters.Dummy,
        source_entity=1036502810,
        name=903600520,
        animation_id=-1,
        animation_id_1=20001,
    )
    CommonFunc_90005883(0, flag=1036500800, flag_1=1036500805, entity=Assets.AEG099_170_1000)
    CommonFunc_90005885(
        0,
        flag=1036500800,
        bgm_boss_conv_param_id=0,
        flag_1=1036502806,
        flag_2=1036502807,
        left=0,
        left_1=1,
    )
    CommonFunc_90005300(0, flag=1036500340, character=Characters.RedWolf, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005633(0, 580310, 580010, 1036500600, 30016, 20016, 1036501600, 1036501610)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton0,
        region=1036502210,
        radius=1.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton1,
        region=1036502210,
        radius=1.0,
        seconds=0.5,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton2,
        region=1036502210,
        radius=1.0,
        seconds=1.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton3,
        region=1036502214,
        radius=1.0,
        seconds=1.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton4,
        region=1036502214,
        radius=1.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton5,
        region=1036502214,
        radius=1.0,
        seconds=0.5,
        animation_id=1700,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Skeleton6,
        region=1036502214,
        radius=1.0,
        seconds=2.0,
        animation_id=1700,
    )
    CommonFunc_90005261(0, character=1036500218, region=1036502218, radius=1.0, seconds=1.0, animation_id=1700)
    CommonFunc_90005261(0, character=1036500219, region=1036502218, radius=1.0, seconds=0.5, animation_id=1700)
    CommonFunc_90005261(0, 1036500220, 1036502218, 1.0, 0.0, 1700)
