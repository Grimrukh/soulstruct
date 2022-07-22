"""
West Consecrated Snowfield (SE) (SE)

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
from .entities.m60_47_56_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_511_1000,
        area_id=12,
        block_id=5,
        cc_id=0,
        dd_id=0,
        player_start=12052020,
        unk_8_12=0,
        flag=1047562501,
        left_flag=1047562502,
        cancel_flag__right_flag=1047562503,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1047560180,
        summon_flag=1047562181,
        dismissal_flag=1047562182,
        character=Characters.BloodyFingerNerijus,
        sign_type=21,
        region=1047562180,
        region_1=1047562181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1047560180,
        flag_1=1047562181,
        flag_2=1047562182,
        character=Characters.BloodyFingerNerijus,
    )
    CommonFunc_90005792(
        0,
        flag=1047560180,
        flag_1=1047562181,
        flag_2=1047562182,
        character=Characters.BloodyFingerNerijus,
        item_lot_param_id=1047560700,
        seconds=0.0,
    )
    CommonFunc_90005793(0, 1047560180, 1047562181, 1047562182, 1047560180, 1047562180, 1047562182, 0)
