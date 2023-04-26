"""
Southeast Liurnia (SW) (NE)

linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_37_41_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia0,
        region=1037412200,
        radius=3.0,
        seconds=0.0,
        animation_id=3020,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia1,
        region=1037412200,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia2,
        region=1037412200,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia3,
        region=1037412200,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia4,
        region=1037412204,
        radius=3.0,
        seconds=0.0,
        animation_id=3020,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia5,
        region=1037412204,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.VulgarMilitia6,
        region=1037412204,
        radius=3.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, model_point=800, right=0)
    Event_1037410220(0, character=Characters.WanderingNoble)


@RestartOnRest(1037410220)
def Event_1037410220(_, character: uint):
    """Event 1037410220"""
    Kill(character)
