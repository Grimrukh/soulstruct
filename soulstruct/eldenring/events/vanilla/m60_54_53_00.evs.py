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
    RegisterGrace(grace_flag=1054530000, obj=1054531950, unknown=5.0)
    Event_1054530703()
    RunCommonEvent(0, 90005771, args=(1054531950, 1054532702), arg_types="II")


@NeverRestart(1054532500)
def Event_1054532500():
    """Event 1054532500"""
    EndIfFlagEnabled(1054530520)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9320, entity=1054531500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1054530500)
    EnableFlag(130)
    DisplayDialog(text=99999100, anchor_entity=0, display_distance=4.0, button_type=ButtonType.Yes_or_No)


@RestartOnRest(1054533700)
def Event_1054533700():
    """Event 1054533700"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L0, flag=1054532700)
    GotoIfFlagEnabled(Label.L1, flag=1054532700)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=1054531950, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1054532700)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityBeyondDistance(AND_2, entity=20000, other_entity=1054531950, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkFlag(1054532700)
    Restart()


@RestartOnRest(1054533701)
def Event_1054533701():
    """Event 1054533701"""
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L0, flag=1054532701)
    GotoIfFlagEnabled(Label.L1, flag=1054532701)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=1054531950, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1054532701)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    IfEntityBeyondDistance(AND_2, entity=20000, other_entity=1054531950, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableNetworkFlag(1054532701)
    Restart()


@RestartOnRest(1054533702)
def Event_1054533702():
    """Event 1054533702"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1054539200)
    EndIfFlagEnabled(1054539201)
    IfFlagEnabled(AND_1, 1054539200)
    IfFlagEnabled(AND_1, 4652)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(PLAYER, 68110, unknown2=1.0)
    End()


@NeverRestart(1054533703)
def Event_1054533703():
    """Event 1054533703"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(OR_1, 1054539200)
    IfFlagEnabled(OR_1, 1054539201)
    IfConditionTrue(AND_1, input_condition=OR_1)
    EndIfConditionFalse(input_condition=AND_1)
    DisableNetworkFlag(1054539200)
    DisableNetworkFlag(1054539201)
    DisableNetworkFlag(1054539205)
    End()


@RestartOnRest(1054530703)
def Event_1054530703():
    """Event 1054530703"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(1054532703)
    IfFlagRangeAnyEnabled(MAIN, flag_range=(71300, 71399))
    EnableFlag(1054532703)
    End()
