"""
West Liurnia (NW) (NE)

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
from .enums.m60_33_47_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1033470000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=12,
        block_id=2,
        cc_id=0,
        dd_id=0,
        player_start=12022210,
        unk_8_12=0,
        flag=1033472610,
        left_flag=1033472611,
        cancel_flag__right_flag=1033472612,
        left=1033470610,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1033472611(
        0,
        flag=1033470611,
        destination=Assets.AEG099_295_9000,
        left_flag=1033472613,
        cancel_flag__right_flag=1033472614,
    )
    Event_1033472612(0, flag=1033470611, asset=Assets.AEG027_216_9000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower0,
        region=1033472200,
        radius=0.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower1,
        region=1033472200,
        radius=0.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower2,
        region=1033472200,
        radius=0.0,
        seconds=2.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=1033472200,
        radius=0.0,
        seconds=1.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower4,
        region=1033472200,
        radius=0.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower5,
        region=1033472200,
        radius=0.0,
        seconds=1.0,
        animation_id=1705,
    )


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005421(0, character=Characters.CaravanDummy, asset=Assets.AEG100_101_9000, flag=1033478301)
    CommonFunc_90005422(0, flag=1033478301, asset=Assets.AEG100_100_9000, obj_act_id=1033473301)
    CommonFunc_90005424(
        0,
        asset=Assets.AEG100_100_9000,
        character=Characters.Troll0,
        character_1=Characters.Troll1,
        character_2=Characters.CaravanDummy,
        asset_1=Assets.AEG100_101_9000,
    )
    CommonFunc_90005423(0, character=Characters.Troll0)
    CommonFunc_90005423(0, character=Characters.Troll1)


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005420(
        0,
        character=Characters.CaravanDummy,
        caravan_asset__parent_asset=Assets.AEG100_100_9000,
        child_asset=Assets.AEG100_101_9000,
        character_1=Characters.Dummy,
        character_2=Characters.Troll0,
        character_3=Characters.Troll1,
        seconds=0.0,
    )


@RestartOnRest(1033472610)
def Event_1033472610(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
    player_start: PlayerStart | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 1033472610"""
    if Multiplayer():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L5, flag=1033470610)
    AwaitDialogResponse(
        message=108186,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
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
    AND_5.Add(PlayerHasGood(8186))
    SkipLinesIfConditionTrue(3, AND_5)
    AwaitDialogResponse(
        message=308186,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=0,
        right_flag=0,
        cancel_flag=0,
    )
    Wait(1.0)
    Restart()
    EnableFlag(1033470610)
    AwaitDialogResponse(
        message=208186,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
        anchor_entity=anchor_entity,
        display_distance=2.0,
        left_flag=0,
        right_flag=0,
        cancel_flag=0,
    )
    RemoveGoodFromPlayer(item=8186, quantity=1)

    # --- Label 5 --- #
    DefineLabel(5)
    FaceEntityAndForceAnimation(PLAYER, anchor_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1033472611)
def Event_1033472611(
    _,
    flag: Flag | int,
    destination: uint,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 1033472611"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(PlayerNotInOwnWorld())
    if OR_1:
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9523, entity=destination))
    
    AwaitDialogResponse(
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
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(2.5)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(1033470610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1033472612)
def Event_1033472612(_, flag: Flag | int, asset: Asset | int):
    """Event 1033472612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableAsset(asset)
