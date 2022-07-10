"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005600, args=(76354, 1037521950, 3.0, 0), arg_types="IIfI")
    RunCommonEvent(0, 90005261, args=(1037520204, 1037522204, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520205, 1037522204, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520206, 1037522204, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520207, 1037522500, 7.0, 1.5, 3022), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520500, 1037522500, 10.0, 1.0, 3013), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520301, 1037522301, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520303, 1037522301, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520304, 1037522301, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520305, 1037522301, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520401, 1037522301, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005211,
        args=(1037520400, 30000, 20000, 1037522405, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005261, args=(1037520300, 1037522302, 5.0, 2.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037520310, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1037520311, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(1037520312, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(1037520313, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(4, 90005261, args=(1037520314, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(5, 90005261, args=(1037520315, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(6, 90005261, args=(1037520350, 1037522350, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005771, args=(1037520951, 1037522700), arg_types="II")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005300, args=(1037520355, 1037525350, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005600, args=(1037520001, 1037521951, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(0, 90005200, args=(1037520614, 30000, 20000, 1037522614, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520615, 30000, 20000, 1037522614, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520616, 30000, 20000, 1037522614, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520617, 30000, 20000, 1037522614, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520618, 30000, 20000, 1037522614, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520619, 30000, 20000, 1037522614, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520620, 30000, 20000, 1037522614, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520621, 30000, 20000, 1037522614, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1037520622, 30000, 20000, 1037522614, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")


@RestartOnRest(1035542210)
def Event_1035542210(_, character: uint):
    """Event 1035542210"""
    IfFlagEnabled(AND_1, 1037520350)
    EndIfConditionTrue(input_condition=AND_1)
    DisableCharacter(character)
    IfHealthLessThan(MAIN, 1037520350, value=0.699999988079071)
    EnableCharacter(character)
    AddSpecialEffect(character, 8971)


@RestartOnRest(1037522220)
def Event_1037522220():
    """Event 1037522220"""
    Kill(1037520220)
    Kill(1037520221)
    Kill(1037520222)
    Kill(1037520223)
    Kill(1037520224)
    Kill(1037520225)
    Kill(1037520226)
    Kill(1037520227)
    Kill(1037520228)
    Kill(1037520229)


@RestartOnRest(1037522900)
def Event_1037522900(
    _,
    grace_flag: uint,
    character: uint,
    obj: uint,
    unknown: float,
    character_1: uint,
    character_2: uint,
    flag: uint,
):
    """Event 1037522900"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableCharacter(character_2)
    DisableObject(obj)
    Wait(1.0)
    IfCharacterDead(MAIN, character_1)
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=obj, model_point=200, anchor_type=CoordEntityType.Object)
    EnableFlag(flag)
    Wait(0.5)
    EnableCharacter(character)
    EnableCharacter(character_2)
    EnableObject(obj)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(grace_flag=grace_flag, obj=obj, reaction_distance=5.0, reaction_angle=180.0, unknown=unknown)


@RestartOnRest(1037522300)
def Event_1037522300():
    """Event 1037522300"""
    CancelSpecialEffect(1037520300, 5070)
    CancelSpecialEffect(1037520301, 5070)


@RestartOnRest(1037522350)
def Event_1037522350(_, character: uint):
    """Event 1037522350"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 3021, wait_for_completion=True, unknown2=1.0)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037522370)
def Event_1037522370(_, character: uint):
    """Event 1037522370"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 3022, wait_for_completion=True, unknown2=1.0)
    DisableThisSlotFlag()
    End()
