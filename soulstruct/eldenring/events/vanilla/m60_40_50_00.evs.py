"""
South Altus Plateau (NW) (SW)

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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_41_50_00_enums import Characters as m60_41_50_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1040502200(0, vfx_id=1040502200)
    Event_1040502200(1, vfx_id=1040502201)
    Event_1040502200(2, vfx_id=1040502202)
    Event_1040502200(3, vfx_id=1040502203)
    Event_1040502200(4, vfx_id=1040502204)
    Event_1040502200(5, vfx_id=1040502205)
    Event_1040502200(6, vfx_id=1040502206)
    Event_1040502200(7, vfx_id=1040502207)
    Event_1040502200(8, vfx_id=1040502208)
    Event_1040502200(9, vfx_id=1040502209)
    Event_1040502200(10, vfx_id=1040502210)
    Event_1040502200(11, vfx_id=1040502211)
    Event_1040502200(12, vfx_id=1040502212)
    Event_1040502200(13, vfx_id=1040502213)
    Event_1040502200(14, vfx_id=1040502214)
    Event_1040502200(15, vfx_id=1040502215)
    Event_1040502200(16, vfx_id=1040502216)
    Event_1040502200(17, vfx_id=1040502217)
    Event_1040502200(18, vfx_id=1040502218)
    Event_1040502200(19, vfx_id=1040502219)
    Event_1040502200(20, vfx_id=1040502220)
    Event_1040502200(21, vfx_id=1040502221)
    Event_1040502200(22, vfx_id=1040502222)
    Event_1040502200(23, vfx_id=1040502223)
    Event_1040502200(24, vfx_id=1040502224)
    Event_1040502200(25, vfx_id=1040502225)
    Event_1040502200(26, vfx_id=1040502226)


@RestartOnRest(1040502200)
def Event_1040502200(_, vfx_id: VFXEvent | int):
    """Event 1040502200"""
    GotoIfFlagEnabled(Label.L0, flag=1041500800)
    
    MAIN.Await(CharacterDead(m60_41_50_00_Characters.FallingstarBeast))

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()
