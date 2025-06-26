"""
East Liurnia (NE) (NW)

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
from .enums.m60_38_47_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038470000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005400(0, character=Characters.Runebear, special_effect=0, seconds=0.0, seconds_1=0.0, left=0)
    CommonFunc_90005401(0, flag=0, character=Characters.Runebear)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1038470700)
    CommonFunc_90005251(0, character=Characters.GravenSchool, radius=30.0, seconds=0.0, animation_id=1700)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1038476420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1238470400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1238472400, flag_1=1238470400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9000,
        dummy_id=101,
        seconds=0.0,
    )
    CommonFunc_90005453(
        1,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9001,
        dummy_id=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9002,
        dummy_id=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471423,
        dummy_id=104,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471424,
        dummy_id=105,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471425, dummy_id=106, seconds=0.5)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471426,
        dummy_id=107,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471427,
        dummy_id=108,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471428,
        dummy_id=109,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=1038471429,
        dummy_id=110,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471430, dummy_id=111, seconds=1.0)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9016,
        dummy_id=117,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9017,
        dummy_id=118,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9018,
        dummy_id=119,
        seconds=0.0,
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471439, dummy_id=120, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471440, dummy_id=121, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471441, dummy_id=122, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471442, dummy_id=123, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471443, dummy_id=124, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471444, dummy_id=125, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471445, dummy_id=126, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471446, dummy_id=127, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471447, dummy_id=128, seconds=0.0)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9032,
        dummy_id=133,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9033,
        dummy_id=134,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9034,
        dummy_id=135,
        seconds=0.0,
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471455, dummy_id=136, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471456, dummy_id=137, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471457, dummy_id=138, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471458, dummy_id=139, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471459, dummy_id=140, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471460, dummy_id=141, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471461, dummy_id=142, seconds=0.0)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9048,
        dummy_id=149,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9049,
        dummy_id=150,
        seconds=0.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9050,
        dummy_id=151,
        seconds=0.0,
    )
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471471, dummy_id=152, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471472, dummy_id=153, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471473, dummy_id=154, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471474, dummy_id=155, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471475, dummy_id=156, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471476, dummy_id=157, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471477, dummy_id=158, seconds=0.0)
    CommonFunc_90005453(0, asset__character=Characters.WalkingMausoleum, asset=1038471478, dummy_id=159, seconds=0.0)
    CommonFunc_90005456(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_004_9000,
        asset_1=Assets.AEG300_009_9000,
        flag=1238470400,
    )


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_003_9000,
        asset_1=Assets.AEG300_004_9000,
        asset_2=Assets.AEG300_009_9000,
    )
