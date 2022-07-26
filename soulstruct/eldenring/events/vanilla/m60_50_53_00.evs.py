"""
Southwest Mountaintops (SE) (NW)

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
from .entities.m60_50_53_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1050532200(0, character=1050535200)
    CommonFunc_90005300(0, flag=1050530210, character=Characters.Scarab, item_lot=1050530700, seconds=0.0, left=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1050538620)
    CommonFunc_90005683(0, flag=62511, asset=Assets.AEG099_057_1000, vfx_id=211, flag_1=78592, flag_2=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=1050538600)
    CommonFunc_90005620(
        0,
        flag=1050530570,
        asset=1050531570,
        asset_1=1050531571,
        asset_2=1050531572,
        left_flag=1050532570,
        cancel_flag__right_flag=1050532571,
        right=1050532572,
    )
    CommonFunc_90005621(0, flag=1050530570, asset=1050531573)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_393_1000, text=61050)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper,
        animation_id=30004,
        animation_id_1=20004,
        region=1050532201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1050532200)
def Event_1050532200(_, character: uint):
    """Event 1050532200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    End()
