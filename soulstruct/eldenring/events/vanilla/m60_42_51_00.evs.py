"""
South Altus Plateau (NE) (NW)

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
from .enums.m60_42_51_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76309, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76309,
        asset=Assets.AEG099_060_9001,
        source_flag=77300,
        value=3,
        flag_2=78300,
        flag_3=78301,
        flag_4=78302,
        flag_5=78303,
        flag_6=78304,
        flag_7=78305,
        flag_8=78306,
        flag_9=78307,
        flag_10=78308,
        flag_11=78309,
    )
    CommonFunc_90005300(0, flag=1042510300, character=Characters.Gargoyle, item_lot=1042510900, seconds=0.0, left=0)
    Event_1042512240(0, asset=Assets.AEG099_070_9000, entity=Assets.AEG099_071_9000, flag=62031)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005200(
        0,
        character=Characters.Gargoyle,
        animation_id=30004,
        animation_id_1=20004,
        region=1042512301,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1042512240)
def Event_1042512240(_, asset: uint, entity: uint, flag: uint):
    """Event 1042512240"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=200, model_point=803220)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)
