"""
Southeast Mountaintops (SE) (NW)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *
from .enums.m60_54_53_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1054530000, asset=Assets.AEG099_060_9000)
    Event_1054530703()
    CommonFunc_90005771(0, other_entity=Assets.AEG099_060_9000, flag=1054532702)


@ContinueOnRest(1054532500)
def Event_1054532500():
    """Event 1054532500"""
    if FlagEnabled(1054530520):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=1054531500))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1054530500)
    EnableFlag(130)
    DisplayDialog(text=99999100, display_distance=4.0, button_type=ButtonType.Yes_or_No)


@RestartOnRest(1054533700)
def Event_1054533700():
    """Event 1054533700"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=1054532700)
    GotoIfFlagEnabled(Label.L1, flag=1054532700)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=Assets.AEG099_060_9000, radius=3.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1054532700)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=Assets.AEG099_060_9000, radius=3.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkFlag(1054532700)
    Restart()


@RestartOnRest(1054533701)
def Event_1054533701():
    """Event 1054533701"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=1054532701)
    GotoIfFlagEnabled(Label.L1, flag=1054532701)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=Assets.AEG099_060_9000, radius=3.0))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1054532701)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=Assets.AEG099_060_9000, radius=3.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkFlag(1054532701)
    Restart()


@RestartOnRest(1054533702)
def Event_1054533702():
    """Event 1054533702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1054539200):
        return
    if FlagEnabled(1054539201):
        return
    AND_1.Add(FlagEnabled(1054539200))
    AND_1.Add(FlagEnabled(4652))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 68110)
    End()


@ContinueOnRest(1054533703)
def Event_1054533703():
    """Event 1054533703"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(1054539200))
    OR_1.Add(FlagEnabled(1054539201))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    DisableNetworkFlag(1054539200)
    DisableNetworkFlag(1054539201)
    DisableNetworkFlag(1054539205)
    End()


@RestartOnRest(1054530703)
def Event_1054530703():
    """Event 1054530703"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(1054532703)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(71300, 71399)))
    
    EnableFlag(1054532703)
    End()
