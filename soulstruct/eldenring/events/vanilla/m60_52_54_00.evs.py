"""
Southeast Mountaintops (NW) (SW)

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
from .enums.m60_52_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1052540000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76510,
        flag_1=76506,
        asset=Assets.AEG099_090_9000,
        source_flag=77500,
        value=6,
        flag_2=78500,
        flag_3=78501,
        flag_4=78502,
        flag_5=78503,
        flag_6=78504,
        flag_7=78505,
        flag_8=78506,
        flag_9=78507,
        flag_10=78508,
        flag_11=78509,
    )
    Event_1052542200(0, character=1052545200)
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper0,
        animation_id=30003,
        animation_id_1=20003,
        region=1052542304,
        seconds=1.7000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper1,
        animation_id=30003,
        animation_id_1=20003,
        region=1052542304,
        seconds=1.7000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper2,
        animation_id=30004,
        animation_id_1=20004,
        region=1052542304,
        seconds=1.7000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper,
        animation_id=30003,
        animation_id_1=20003,
        region=1052542311,
        seconds=1.899999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1052540320,
        animation_id=30005,
        animation_id_1=20005,
        region=1052542320,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MassiveFingercreeper,
        animation_id=30005,
        animation_id_1=20005,
        region=1052542321,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1052540322,
        animation_id=30005,
        animation_id_1=20005,
        region=1052542322,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SnowTroll0,
        animation_id=30003,
        animation_id_1=20003,
        region=1052542331,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.SnowTroll2, region=1052542334, radius=50.0, seconds=0.0, animation_id=0)
    CommonFunc_90005300(0, flag=1052540491, character=Characters.SnowTroll0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1052540492, character=Characters.SnowTroll1, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1052540494, character=Characters.SnowTroll2, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy, flag=1052542700)


@RestartOnRest(1052542200)
def Event_1052542200(_, character: uint):
    """Event 1052542200"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()
