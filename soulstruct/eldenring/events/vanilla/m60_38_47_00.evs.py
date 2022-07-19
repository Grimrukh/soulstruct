"""
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
from .entities.m60_38_47_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038470000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005400(0, character=Characters.Runebear, special_effect_id=0, seconds=0.0, seconds_1=0.0, left=0)
    CommonFunc_90005401(0, 0, 1038470340)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038470700)
    CommonFunc_90005251(0, 1038470250, 30.0, 0.0, 1700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1038476420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1238470400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1238472400, flag_1=1238470400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9000, model_point=101, seconds=0.0)
    CommonFunc_90005453(
        1,
        asset__character=1038470400,
        asset=Assets.AEG300_006_9001,
        model_point=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=1038470400,
        asset=Assets.AEG300_006_9002,
        model_point=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471423, model_point=104, seconds=0.30000001192092896)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471424, model_point=105, seconds=0.4000000059604645)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471425, model_point=106, seconds=0.5)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471426, model_point=107, seconds=0.6000000238418579)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471427, model_point=108, seconds=0.699999988079071)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471428, model_point=109, seconds=0.800000011920929)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471429, model_point=110, seconds=0.8999999761581421)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471430, model_point=111, seconds=1.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9016, model_point=117, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9017, model_point=118, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9018, model_point=119, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471439, model_point=120, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471440, model_point=121, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471441, model_point=122, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471442, model_point=123, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471443, model_point=124, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471444, model_point=125, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471445, model_point=126, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471446, model_point=127, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471447, model_point=128, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9032, model_point=133, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9033, model_point=134, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9034, model_point=135, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471455, model_point=136, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471456, model_point=137, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471457, model_point=138, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471458, model_point=139, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471459, model_point=140, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471460, model_point=141, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471461, model_point=142, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9048, model_point=149, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9049, model_point=150, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=Assets.AEG300_006_9050, model_point=151, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471471, model_point=152, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471472, model_point=153, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471473, model_point=154, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471474, model_point=155, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471475, model_point=156, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471476, model_point=157, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471477, model_point=158, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1038470400, asset=1038471478, model_point=159, seconds=0.0)
    CommonFunc_90005456(0, 1038470400, 1038471410, 1038471418, 1238470400)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(0, 1038470400, 1038471400, 1038471410, 1038471418)
