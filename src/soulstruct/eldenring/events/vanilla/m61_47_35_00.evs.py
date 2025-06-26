"""
Land of Shadow 11-08 NE NE

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=2047350000, asset=2047351950)
    CommonFunc_90005200(
        0,
        character=2047350214,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047350215,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352200,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047350216,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352200,
        seconds=1.100000023841858,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047350213,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047350219,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352201,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047350220,
        animation_id=30001,
        animation_id_1=20001,
        region=2047352201,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_2047351500()


@RestartOnRest(2047351500)
def Event_2047351500():
    """Event 2047351500"""
    GotoIfFlagDisabled(Label.L0, flag=2047350500)
    DisableAsset(2047351500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=2047352550)
    DeleteAssetVFX(2047351500)
    CreateAssetVFX(2047351500, dummy_id=101, vfx_id=1550)
    EnableNetworkFlag(2047352550)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209504, entity=2047351500))
    AND_2.Add(FlagEnabled(4927))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=2020004, anchor_entity=2047351500, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(2047350500)
    DeleteAssetVFX(2047351500)
    DisableAsset(2047351500)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteAssetVFX(2047351500)
    CreateAssetVFX(2047351500, dummy_id=101, vfx_id=1550)
    End()
