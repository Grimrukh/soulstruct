"""
Land of Shadow 11-11 SE SE

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
    RegisterGrace(grace_flag=2047440000, asset=2047441950, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=2047440001, asset=2047441951, enemy_block_distance=4.0)
    CommonFunc_90005250(0, character=2047440351, region=2047442351, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047440352, region=2047442351, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=2047440330, region=2047442330, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440339, region=2047442330, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440340, region=2047442330, seconds=0.0, animation_id=0)
    CommonFunc_90005301(0, flag=2047440360, character=2047440360, item_lot__unk1=30865, seconds=0.0, unk1=0)
    CommonFunc_90005250(0, character=2047440270, region=2047442200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440200, region=2047442200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440260, region=2047442200, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440265, region=2047442263, seconds=0.5, animation_id=3005)
    CommonFunc_90005200(
        0,
        character=2047440264,
        animation_id=30002,
        animation_id_1=20002,
        region=2047442263,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047440263,
        animation_id=30002,
        animation_id_1=20002,
        region=2047442263,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047440203,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=2047440266, region=2047442232, radius=0.5, seconds=0.0, animation_id=3008)
    CommonFunc_90005261(0, character=2047440271, region=2047442271, radius=0.0, seconds=0.0, animation_id=3008)
    CommonFunc_90005250(0, character=2047440225, region=2047442223, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440228, region=2047442225, seconds=0.5, animation_id=3001)
    CommonFunc_90005250(0, character=2047440227, region=2047442227, seconds=0.0, animation_id=3000)
    Event_2047442200(0, character=2047440225)
    Event_2047442200(1, character=2047440228)
    CommonFunc_90005250(0, character=2047440222, region=2047442222, seconds=0.0, animation_id=3020)
    CommonFunc_90005250(0, character=2047440232, region=2047442232, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=2047440235, region=2047442232, seconds=0.0, animation_id=3010)
    CommonFunc_90005250(0, character=2047440224, region=2047442232, seconds=0.5, animation_id=3010)
    Event_2047442200(2, character=2047440232)
    CommonFunc_90005250(0, character=2047440221, region=2047442221, seconds=0.0, animation_id=3020)
    CommonFunc_90005200(
        0,
        character=2047440231,
        animation_id=30010,
        animation_id_1=20010,
        region=2047442226,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047440226,
        animation_id=30010,
        animation_id_1=20010,
        region=2047442226,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047440236,
        animation_id=30010,
        animation_id_1=20010,
        region=2047442226,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=2047440236,
        animation_id=30010,
        animation_id_1=20010,
        region=2047442226,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2047440240, region=2047442226, seconds=0.0, animation_id=3013)
    Event_2047442200(3, character=2047440237)
    CommonFunc_90005250(0, character=2047440237, region=2047442237, seconds=0.0, animation_id=3001)
    Event_2047442200(4, character=2047440238)
    CommonFunc_90005250(0, character=2047440238, region=2047442237, seconds=0.0, animation_id=3001)
    CommonFunc_90005201(
        0,
        character=2047440230,
        animation_id=30010,
        animation_id_1=20010,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=2047440229,
        animation_id=30010,
        animation_id_1=20010,
        radius=7.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=2047440211, region=2047442212, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440260, region=2047442212, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440206, region=2047442206, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440207, region=2047442206, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440214, region=2047442206, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440217, region=2047442206, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440216, region=2047442222, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=2047440280,
        animation_id=30004,
        animation_id_1=20004,
        region=2047442211,
        radius=3.799999952316284,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2047440310,
        animation_id=30000,
        animation_id_1=20000,
        region=2047442201,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005301(0, flag=2047440310, character=2047440310, item_lot__unk1=2047440900, seconds=6.0, unk1=0)
    CommonFunc_90005261(0, character=2047440252, region=2047442252, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440253, region=2047442252, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=2047440321,
        animation_id=30000,
        animation_id_1=20000,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=1,
        left_3=0,
    )
    CommonFunc_90005261(0, character=2047440320, region=2047442237, radius=2.0, seconds=0.0, animation_id=3012)
    CommonFunc_90005261(0, character=2047440322, region=2047442322, radius=2.0, seconds=0.0, animation_id=3012)
    CommonFunc_90005250(0, character=2047440302, region=2047442302, seconds=0.5, animation_id=0)
    CommonFunc_90005250(0, character=2047440301, region=2047442301, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=2047440243, region=2047442226, seconds=0.0, animation_id=0)
    Event_2047442580()
    Event_2047442500(
        0,
        flag=2047448500,
        asset=2047441500,
        asset_1=2047441501,
        obj_act_id=2047443500,
        obj_act_id_1=464016,
        animation_id=1,
        animation_id_1=2,
        animation_id_2=1,
    )
    CommonFunc_900005610(0, asset=2047441200, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2047441201, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=2047441202, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005580(0, flag=580600, asset=2047441600, flag_1=9146)
    CommonFunc_90005605(
        0,
        asset=2047441610,
        area_id=61,
        block_id=46,
        cc_id=46,
        dd_id=0,
        player_start=2046464500,
        unk_8_12=0,
        flag=2047442650,
        left_flag=2047442654,
        cancel_flag__right_flag=2047442655,
        left=2047440610,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_2047442611(
        0,
        flag=2047440611,
        destination=2047441611,
        left_flag=2047442613,
        cancel_flag__right_flag=2047442614,
        flag_1=2047440610,
    )
    Event_2047442612(0, flag=2047440611, asset=2047441612)
    CommonFunc_90005706(0, character=2047440700, animation_id=30010, left=0)
    CommonFunc_90005748(0, entity=2047441700, action_button_id=206020, text=1030050, display_distance=30.0, flag=4920)


@ContinueOnRest(2047442580)
def Event_2047442580():
    """Event 2047442580"""
    RegisterLadder(start_climbing_flag=2047440580, stop_climbing_flag=2047440581, asset=2047441580)
    RegisterLadder(start_climbing_flag=2047440582, stop_climbing_flag=2047440583, asset=2047441582)
    RegisterLadder(start_climbing_flag=2047440584, stop_climbing_flag=2047440585, asset=2047441584)
    RegisterLadder(start_climbing_flag=2047440586, stop_climbing_flag=2047440587, asset=2047441586)
    RegisterLadder(start_climbing_flag=2047440588, stop_climbing_flag=2047440589, asset=2047441588)
    RegisterLadder(start_climbing_flag=2047440590, stop_climbing_flag=2047440591, asset=2047441590)
    RegisterLadder(start_climbing_flag=2047440592, stop_climbing_flag=2047440593, asset=2047441592)


@RestartOnRest(2047442500)
def Event_2047442500(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
):
    """Event 2047442500"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    EndOfAnimation(asset=asset_1, animation_id=animation_id_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    ForceAnimation(asset, animation_id)


@RestartOnRest(2047442200)
def Event_2047442200(_, character: Character | int):
    """Event 2047442200"""
    if CharacterDoesNotHaveSpecialEffect(character=character, special_effect=13690):
        AddSpecialEffect(character, 13690)


@RestartOnRest(2047442300)
def Event_2047442300(_, character: Character | int):
    """Event 2047442300"""
    AddSpecialEffect(character, 20007030)


@RestartOnRest(2047442611)
def Event_2047442611(
    _,
    flag: Flag | int,
    destination: uint,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 2047442611"""
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
    EnableNetworkFlag(flag_1)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(2047442612)
def Event_2047442612(_, flag: Flag | int, asset: Asset | int):
    """Event 2047442612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableAsset(asset)


@RestartOnRest(2047442360)
def Event_2047442360():
    """Event 2047442360"""
    AND_1.Add(FlagEnabled(2047440360))
    if AND_1:
        return
    
    MAIN.Await(CharacterDead(2047440360))
    
    AwardItemLot(30865, host_only=False)
    EnableNetworkFlag(2047440360)
