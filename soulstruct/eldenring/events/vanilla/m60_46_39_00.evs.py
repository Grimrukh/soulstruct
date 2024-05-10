"""
East Limgrave (NE) (NW)

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
from .enums.m60_46_39_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1035472602()
    CommonFunc_90005300(0, flag=1046390210, character=Characters.Scarab, item_lot=40118, seconds=0.0, item_is_dropped=0)
    Event_1035472200(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=51,
        cc_id=43,
        dd_id=0,
        player_start=1051430600,
        unk_8_12=0,
        flag=1051432650,
        left_flag=1051432651,
        cancel_flag__right_flag=1051432652,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005261(0, character=Characters.Troll, region=1046392340, radius=30.0, seconds=0.0, animation_id=0)


@ContinueOnRest(1035472200)
def Event_1035472200(
    _,
    asset: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    unk_8_12: int,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    left: uint,
    text: int,
    seconds: float,
    seconds_1: float,
):
    """Event 1035472200"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    if ThisEventSlotFlagDisabled():
        DeleteAssetVFX(asset)
        DisableFlag(flag)
        WaitFrames(frames=1)
    OR_10.Add(Multiplayer())
    OR_10.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_10.Add(FlagDisabled(left))
    GotoIfConditionTrue(Label.L1, input_condition=OR_10)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, vfx_id=200, dummy_id=806870)
    EnableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    SkipLinesIfUnsignedEqual(3, left=left, right=0)
    SkipLinesIfValueNotEqual(2, left=text, right=0)
    AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    OR_4.Add(Multiplayer())
    OR_4.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_4.Add(FlagDisabled(left))
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    OR_7.Add(Multiplayer())
    OR_7.Add(MultiplayerPending())
    if UnsignedNotEqual(left=left, right=0):
        OR_7.Add(FlagDisabled(left))
    AND_7.Add(not OR_7)
    AND_7.Add(FlagDisabled(flag))
    AND_9.Add(FlagState(FlagSetting.Change, FlagType.Absolute, left))
    OR_14.Add(AND_1)
    OR_14.Add(AND_4)
    OR_14.Add(AND_7)
    if UnsignedNotEqual(left=left, right=0):
        OR_14.Add(AND_9)
    
    MAIN.Await(OR_14)
    
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_1)
    GotoIfLastConditionResultFalse(Label.L2, input_condition=AND_4)
    DeleteAssetVFX(asset)
    DisableFlag(flag)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(0.032999999821186066)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    OR_13.Add(UnsignedEqual(left=left, right=0))
    OR_13.Add(ValueEqual(left=text, right=0))
    GotoIfConditionTrue(Label.L4, input_condition=OR_13)
    GotoIfFlagEnabled(Label.L4, flag=left)
    DisplayDialog(text=text, anchor_entity=asset, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    AwaitDialogResponse(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L6, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    OR_15.Add(Multiplayer())
    OR_15.Add(MultiplayerPending())
    if OR_15:
        return RESTART
    EnableFlag(1051430210)
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unk_8_12=unk_8_12)
    Restart()
    Wait(seconds)
    Wait(seconds_1)


@RestartOnRest(1035472602)
def Event_1035472602():
    """Event 1035472602"""
    AddSpecialEffect(Characters.Troll, 8090)
