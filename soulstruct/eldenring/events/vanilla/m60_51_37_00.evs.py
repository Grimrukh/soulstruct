"""
South Caelid (SE) (NE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_51_37_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1051372598(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=51,
        cc_id=37,
        dd_id=0,
        player_start=1051382300,
        unk_8_12=0,
        flag=0,
        left_flag=1052382610,
        cancel_flag__right_flag=1052382611,
    )
    Event_1051372599()


@RestartOnRest(1051372598)
def Event_1051372598(
    _,
    asset: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: uchar,
    dd_id: uchar,
    player_start: uint,
    unk_8_12: int,
    flag: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 1051372598"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806870)
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    AND_4.Add(MultiplayerPending())
    AND_5.Add(Multiplayer())
    AND_4.Add(not AND_5)
    AND_7.Add(PlayerInOwnWorld())
    AND_7.Add(MultiplayerPending())
    AND_7.Add(Multiplayer())
    AND_7.Add(ActionButtonParamActivated(action_button_id=9140, entity=asset))
    OR_2.Add(InvasionPending())
    OR_2.Add(Invasion())
    AND_8.Add(OR_2)
    OR_14.Add(AND_1)
    OR_14.Add(AND_4)
    OR_14.Add(AND_7)
    OR_14.Add(AND_8)
    
    MAIN.Await(OR_14)
    
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_1)
    GotoIfLastConditionResultTrue(Label.L3, input_condition=AND_7)
    DeleteAssetVFX(asset)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
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
    AND_10.Add(MultiplayerPending())
    AND_10.Add(Multiplayer())
    OR_15.Add(AND_10)
    AND_11.Add(MultiplayerPending())
    AND_12.Add(not AND_11)
    AND_13.Add(Multiplayer())
    AND_12.Add(not AND_13)
    OR_15.Add(AND_12)
    SkipLinesIfConditionTrue(1, OR_15)
    Restart()
    OR_4.Add(InvasionPending())
    OR_4.Add(Invasion())
    if OR_4:
        return RESTART
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    EnableNetworkFlag(1052382602)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=player_start,
        dummy_id=10,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    DisableInvincibility(PLAYER)
    GotoIfFlagEnabled(Label.L4, flag=1252380800)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    NotifyBossBattleStart()

    # --- Label 2 --- #
    DefineLabel(2)
    ActivateMultiplayerBuffs(1052385800)
    BanishInvaders(unknown=0)
    EnableNetworkFlag(1052382805)

    # --- Label 4 --- #
    DefineLabel(4)
    Restart()
    SkipLines(1)
    DisableFlag(flag)
    SkipLines(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unk_8_12=unk_8_12)


@RestartOnRest(1051372599)
def Event_1051372599():
    """Event 1051372599"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown3))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=CharacterType.Unknown5))
    if OR_15:
        return
    
    MAIN.Await(FlagEnabled(1052382602))
    
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=ALL_PLAYERS,
        destination_type=CoordEntityType.Region,
        destination=1051382302,
        dummy_id=10,
        copy_draw_parent=ALL_PLAYERS,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    ActivateMultiplayerBuffs(1052385800)
    EnableNetworkFlag(1052382806)

    # --- Label 1 --- #
    DefineLabel(1)
    End()
