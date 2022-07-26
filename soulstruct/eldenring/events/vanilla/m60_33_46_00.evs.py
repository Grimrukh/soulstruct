"""
West Liurnia (NW) (SE)

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
from .entities.m60_33_46_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1033460000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76214,
        flag_1=76210,
        asset=Assets.AEG099_090_9001,
        source_flag=77220,
        value=0,
        flag_2=78220,
        flag_3=78221,
        flag_4=78222,
        flag_5=78223,
        flag_6=78224,
        flag_7=78225,
        flag_8=78226,
        flag_9=78227,
        flag_10=78228,
        flag_11=78229,
    )
    CommonFunc_90005251(0, character=Characters.GiantLobster0, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantLobster1, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantLobster2, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantLobster3, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=13,
        block_id=0,
        cc_id=0,
        dd_id=0,
        player_start=13002509,
        unk_8_12=0,
        flag=1033462610,
        left_flag=1033462611,
        cancel_flag__right_flag=1033462612,
        left=1033460610,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1033462611(
        0,
        flag=1033460611,
        destination=Assets.AEG099_295_9000,
        left_flag=1033462613,
        cancel_flag__right_flag=1033462614,
    )
    Event_1033462612(0, flag=1033460611, asset=Assets.AEG027_216_9000)


@RestartOnRest(1033462611)
def Event_1033462611(_, flag: uint, destination: uint, left_flag: uint, cancel_flag__right_flag: uint):
    """Event 1033462611"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(PlayerNotInOwnWorld())
    if OR_1:
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9523, entity=destination))
    
    DisplayDialogAndSetFlags(
        message=108186,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(PlayerHasGood(8186))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050)
    Wait(1.5)
    DisplayDialog(text=308186, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Asset, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(2.5)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(1033460610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1033462612)
def Event_1033462612(_, flag: uint, asset: uint):
    """Event 1033462612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableAsset(asset)
