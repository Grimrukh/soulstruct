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
    Event_1047372200(
        0,
        flag=1047370350,
        flag_1=1047372350,
        anchor_entity=1047370300,
        character=1047370350,
        left=1,
        item_lot_param_id=1047370100
    )
    RunCommonEvent(0, 90005391, args=(1047370350, 1047372350, 1047370300, 1047370350, 1), arg_types="IIIIi")
    RunCommonEvent(0, 90005251, args=(1047370300, 10.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1047372200)
def Event_1047372200(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 1047372200"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(6.0)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfValueEqual(1, left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)
