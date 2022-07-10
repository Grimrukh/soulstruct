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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76309, obj=1042511950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76314, 76309, 1042511980, 77300, 3, 78300, 78301, 78302, 78303, 78304, 78305, 78306, 78307, 78308, 78309),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005300, args=(1042510300, 1042510300, 1042510900, 0.0, 0), arg_types="IIifi")
    Event_1042512240(0, 1042511690, 1042511691, 62031)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(1042510300, 30004, 20004, 1042512301, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1042512240)
def Event_1042512240(_, obj: uint, entity: uint, flag: uint):
    """Event 1042512240"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
