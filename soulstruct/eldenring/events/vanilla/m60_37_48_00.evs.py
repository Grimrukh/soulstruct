"""
linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_48_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037480000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005300(0, flag=1037480200, character=Characters.Scarab1, item_lot_param_id=40236, seconds=0.0, left=0)
    CommonFunc_90005300(0, 1037480210, 1037480210, 40254, 0.0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037480700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1037486420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1237480400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1237482400, flag_1=1237480400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9000, model_point=101, seconds=0.0)
    CommonFunc_90005453(
        1,
        asset__character=1037480400,
        asset=Assets.AEG300_006_9001,
        model_point=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=1037480400,
        asset=Assets.AEG300_006_9002,
        model_point=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481423, model_point=104, seconds=0.30000001192092896)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481424, model_point=105, seconds=0.4000000059604645)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481425, model_point=106, seconds=0.5)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481426, model_point=107, seconds=0.6000000238418579)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481427, model_point=108, seconds=0.699999988079071)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481428, model_point=109, seconds=0.800000011920929)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481429, model_point=110, seconds=0.8999999761581421)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481430, model_point=111, seconds=1.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9016, model_point=117, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9017, model_point=118, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9018, model_point=119, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481439, model_point=120, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481440, model_point=121, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481441, model_point=122, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481442, model_point=123, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481443, model_point=124, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481444, model_point=125, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481445, model_point=126, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481446, model_point=127, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481447, model_point=128, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9032, model_point=133, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9033, model_point=134, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9034, model_point=135, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481455, model_point=136, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481456, model_point=137, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481457, model_point=138, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481458, model_point=139, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481459, model_point=140, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481460, model_point=141, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481461, model_point=142, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9068, model_point=149, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9069, model_point=150, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=Assets.AEG300_006_9070, model_point=151, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481471, model_point=152, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481472, model_point=153, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481473, model_point=154, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481474, model_point=155, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481475, model_point=156, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481476, model_point=157, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481477, model_point=158, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1037480400, asset=1037481478, model_point=159, seconds=0.0)
    CommonFunc_90005456(0, 1037480400, 1037481410, 1037481418, 1037480400)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(0, 1037480400, 1037481400, 1037481410, 1037481418)
