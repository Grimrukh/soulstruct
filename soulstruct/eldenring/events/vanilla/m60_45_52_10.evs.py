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
    RegisterGrace(grace_flag=76314, obj=1045521950, unknown=5.0)
    Event_1045522500()
    RunCommonEvent(0, 90005870, args=(1045520800, 903250600, 12), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1045520800, 0, 1045520800, 0, 30315, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1045520800, 12, 0), arg_types="III")
    RunCommonEvent(0, 9005811, args=(1045520800, 1045521800, 5, 0), arg_types="IIiI")
    RunCommonEvent(0, 90005251, args=(1045520201, 70.0, 0.0, 3006), arg_types="Iffi")
    Event_1045522200()
    RunCommonEvent(0, 90005300, args=(1045520200, 1045520200, 30360, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1045520202, 1045520202, 30365, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005251, args=(1045520300, 100.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045520301, 100.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045520302, 100.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045520303, 100.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1045520304, 100.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(1045520400, 30000, 20000, 33.0, 2.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005560, args=(1045520600, 1045521600, 0), arg_types="IIi")
    RunCommonEvent(0, 90005683, args=(62315, 1045521300, 205, 78394, 78394), arg_types="IIiII")
    RunCommonEvent(0, 900005610, args=(1045521685, 100, 800, 1045528600), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1045521680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005780,
        args=(1045520800, 1045522160, 1045522161, 1045520710, 20, 1045522720, 1042559208, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1045520800, 1045522160, 1045522161, 1045520710), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1045520800, 1045522160, 1045522161, 1045520710, 1045522722, 1045522721, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005780,
        args=(1045520800, 1045522170, 1045522171, 1045520730, 20, 1045522731, 1045529250, 0, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(1045520800, 1045522170, 1045522171, 1045520730), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1045520800, 1045522170, 1045522171, 1045520730, 1045522730, 1045522732, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1045520180, 1045522181, 1045522182, 1045520705, 23, 1045522180, 1044522181, 0.0, 35009315, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1045520180, 1045522181, 1045522182, 1045520705), arg_types="IIII")
    RunCommonEvent(0, 90005792, args=(1045520180, 1045522181, 1045522182, 1045520705, 113800, 0.0), arg_types="IIIIif")
    RunCommonEvent(
        0,
        90005793,
        args=(1045520180, 1045522181, 1045522182, 1045520705, 1045522180, 0, 0),
        arg_types="IIIIIIi",
    )
    Event_1045520700()
    Event_1045520710()
    Event_1045520720()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1045520700)
    DisableBackread(1045520701)
    DisableBackread(1045520705)


@RestartOnRest(1045522200)
def Event_1045522200():
    """Event 1045522200"""
    EndIfFlagEnabled(1045520200)
    IfAllPlayersInsideRegion(AND_1, region=1045522182)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(1045520200, 8082)
    ClearTargetList(1045520200)


@RestartOnRest(1045522500)
def Event_1045522500():
    """Event 1045522500"""
    GotoIfFlagDisabled(Label.L0, flag=1045520500)
    DisableObject(1045521500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=1045522550)
    DeleteObjectVFX(1045521500)
    CreateObjectVFX(1045521500, vfx_id=101, model_point=1540)
    EnableNetworkFlag(1045522550)

    # --- Label 2 --- #
    DefineLabel(2)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9503, entity=1045521500)
    IfFlagEnabled(AND_2, 182)
    IfFlagEnabled(AND_2, 105)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20003, anchor_entity=1045521500, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(1045520500)
    DeleteObjectVFX(1045521500)
    DisableObject(1045521500)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteObjectVFX(1045521500)
    CreateObjectVFX(1045521500, vfx_id=101, model_point=1540)
    End()


@RestartOnRest(1045520700)
def Event_1045520700():
    """Event 1045520700"""
    EnableObjectInvulnerability(1045521700)
    DisableGravity(1045520700)
    DisableAnimations(1045520700)
    ForceAnimation(1045520700, 90101, unknown2=1.0)
    Move(1045520700, destination=1045522700, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(1045520710)
def Event_1045520710():
    """Event 1045520710"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAllDisabled(flag_range=(1042559207, 1042559209))
    IfFlagRangeAnyEnabled(AND_1, flag_range=(4181, 4183))
    AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1042559207, 1042559209))
    End()


@RestartOnRest(1045520720)
def Event_1045520720():
    """Event 1045520720"""
    WaitFrames(frames=1)
    DisableFlag(1045529250)
    EndIfFlagEnabled(1045520800)
    EndIfFlagEnabled(7606)
    EnableFlag(1045529250)
    End()


@NeverRestart(150)
def Event_150():
    """Event 150"""
    RunCommonEvent(0, 90005485, args=(1045520202,))
