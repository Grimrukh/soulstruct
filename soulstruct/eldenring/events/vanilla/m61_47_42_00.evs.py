"""
Land of Shadow 11-10 NE SE

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
    CommonFunc_90005250(0, character=2047420266, region=2047422266, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047420267, region=2047422266, seconds=0.5, animation_id=0)
    CommonFunc_90005250(0, character=2047420262, region=2047422262, seconds=0.0, animation_id=4100)
    CommonFunc_90005790(
        0,
        right=0,
        flag=2047420180,
        summon_flag=2047422181,
        dismissal_flag=2047422182,
        character=2047420300,
        sign_type=23,
        region=2047422180,
        region_1=2047422181,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=2047420180, flag_1=2047422181, flag_2=2047422182, character=2047420300)
    CommonFunc_90005792(
        0,
        flag=2047420180,
        flag_1=2047422181,
        flag_2=2047422182,
        character=2047420300,
        item_lot=0,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=2047420180,
        flag_1=2047422181,
        flag_2=2047422182,
        character=2047420300,
        other_entity=2047422180,
        region=0,
        left=0,
    )
    Event_2047422550(0, flag=580110, asset=2047421550, item_lot=80110)


@RestartOnRest(2047422550)
def Event_2047422550(_, flag: Flag | int, asset: uint, item_lot: int):
    """Event 2047422550"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    DeleteAssetVFX(asset, erase_root=False)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806845)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=asset))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot, host_only=True)
