"""
Liurnia to Altus Plateau (SE) (SW)

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
from .entities.m60_38_48_00_entities import *
from .entities.m60_37_49_00_entities import Characters as m60_37_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1038480000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005870(0, character=Characters.ErdtreeAvatar, name=904810601, npc_threat_level=18)
    CommonFunc_90005860(
        0,
        flag=1038480800,
        left=0,
        character=Characters.ErdtreeAvatar,
        left_1=0,
        item_lot__item_lot_param_id=30200,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.ErdtreeAvatar, npc_threat_level=18, right=0)
    Event_1038482580()
    CommonFunc_90005683(0, 62201, 1038481684, 209, 78290, 78290)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(m60_37_Characters.FesteringFingerprintVyke)
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower0,
        region=1038482200,
        radius=0.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower1,
        region=1038482200,
        radius=0.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower2,
        region=1038482200,
        radius=0.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=1038482200,
        radius=0.0,
        seconds=1.399999976158142,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower4,
        region=1038482200,
        radius=0.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower5,
        region=1038482200,
        radius=0.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower6,
        region=1038482200,
        radius=0.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower7,
        region=1038482200,
        radius=0.0,
        seconds=1.399999976158142,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower8,
        region=1038482200,
        radius=0.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower9,
        region=1038482200,
        radius=0.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower10,
        region=1038482200,
        radius=0.0,
        seconds=1.399999976158142,
        animation_id=1705,
    )
    CommonFunc_90005261(0, 1038480211, 1038482200, 0.0, 1.0, 1705)


@ContinueOnRest(1038482580)
def Event_1038482580():
    """Event 1038482580"""
    RegisterLadder(start_climbing_flag=1038480580, stop_climbing_flag=1038480581, asset=1038481580)
    RegisterLadder(start_climbing_flag=1038480582, stop_climbing_flag=1038480583, asset=1038481582)
    RegisterLadder(start_climbing_flag=1038480584, stop_climbing_flag=1038480585, asset=1038481584)
