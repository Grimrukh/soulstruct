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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_33_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1042330000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005300(0, flag=1042330220, character=Characters.Scarab, item_lot_param_id=40132, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=1042330405, region=1042332400, radius=5.0, seconds=0.0, animation_id=3006)
    CommonFunc_90005620(
        0,
        flag=1042330570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1042332570,
        cancel_flag__right_flag=1042332571,
        right=1042332572,
    )
    CommonFunc_90005880(
        0,
        flag=1042330800,
        flag_1=1042330805,
        flag_2=1042332800,
        character=Characters.AncientHeroofZamor,
        item_lot_param_id=1042330100,
        area_id=60,
        block_id=42,
        cc_id=33,
        dd_id=0,
        player_start=1042332805,
    )
    CommonFunc_90005882(
        0,
        1042330800,
        1042330805,
        1042332800,
        1042330800,
        1042332806,
        1042335810,
        1042331800,
        1042330810,
        1042332810,
        907100520,
        -1,
        20002,
    )
    CommonFunc_90005885(
        0,
        flag=1042330800,
        bgm_boss_conv_param_id=0,
        flag_1=1042332806,
        flag_2=1042332807,
        left=0,
        left_1=1,
    )
    Event_1042332575(
        0,
        flag=1042330800,
        flag_1=1042330805,
        left_flag=1042332801,
        cancel_flag__right_flag=1042332802,
        message=20300,
        anchor_entity=Assets.AEG099_170_1000,
        area_id=60,
        block_id=42,
        cc_id=33,
        dd_id=0,
        player_start=1042332805,
        flag_2=1042330570,
    )
    Event_1042332576(0, flag=1042330800, flag_1=1042330805, entity=Assets.AEG099_170_1000, flag_2=1042330570)
    CommonFunc_90005400(0, character=1042330230, special_effect_id=0, seconds=0.0, seconds_1=0.0, left=0)
    CommonFunc_90005401(0, flag=0, character=1042330230)
    Event_1042332200(0, character=1042330200, seconds=0.0)
    Event_1042332200(1, character=1042330201, seconds=2.0)
    Event_1042332200(2, character=Characters.MausoleumSoldier7, seconds=1.0)
    Event_1042332200(3, character=1042330203, seconds=0.5)
    Event_1042332200(4, character=Characters.MausoleumSoldier6, seconds=1.5)
    Event_1042332200(5, character=Characters.MausoleumSoldier5, seconds=2.0)
    Event_1042332200(6, character=1042330206, seconds=0.0)
    Event_1042332200(7, character=1042330207, seconds=2.5)
    Event_1042332200(8, character=1042330208, seconds=3.0)
    Event_1042332200(9, character=Characters.MausoleumSoldier4, seconds=0.5)
    Event_1042332200(10, character=Characters.MausoleumSoldier3, seconds=0.0)
    Event_1042332200(11, character=Characters.MausoleumSoldier2, seconds=0.0)
    Event_1042332200(12, character=Characters.MausoleumSoldier1, seconds=2.5)
    Event_1042332200(13, 1042330214, 3.0)


@RestartOnRest(1042332200)
def Event_1042332200(_, character: uint, seconds: float):
    """Event 1042332200"""
    GotoIfFlagDisabled(Label.L0, flag=1242330400)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(1242330400))
    
    MAIN.Await(MAIN)
    
    Wait(seconds)
    Kill(character)


@RestartOnRest(1042332575)
def Event_1042332575(
    _,
    flag: uint,
    flag_1: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    message: int,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag_2: uint,
):
    """Event 1042332575"""
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9230, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagEnabled(cancel_flag__right_flag):
        return RESTART
    OR_3.Add(Multiplayer())
    OR_3.Add(MultiplayerPending())
    if OR_3:
        return RESTART
    if FlagDisabled(flag_2):
        Wait(0.5)
        DisplayDialog(text=20510, anchor_entity=anchor_entity, display_distance=5.0)
        Wait(3.0)
        Restart()
    EnableNetworkFlag(flag_1)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450)
    Wait(1.5)
    MoveCharacterAndCopyDrawParentWitHFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=player_start,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=True,
        reset_camera=True,
    )
    EnableFlag(9021)
    End()
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1042332576)
def Event_1042332576(_, flag: uint, flag_1: uint, entity: uint, flag_2: uint):
    """Event 1042332576"""
    ForceAnimation(entity, 0, loop=True)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(Singleplayer())
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True)
    AND_11.Add(Singleplayer())
    AND_12.Add(MultiplayerPending())
    AND_11.Add(not AND_12)
    
    MAIN.Await(not AND_11)
    
    WaitFrames(frames=1)
    Restart()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042330700)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1042336420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1242330400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1242332400, flag_1=1242330400)
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9000, model_point=101, seconds=0.0)
    CommonFunc_90005453(
        1,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9001,
        model_point=102,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9002,
        model_point=103,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9003,
        model_point=104,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9004,
        model_point=105,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9005, model_point=106, seconds=0.5)
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9006,
        model_point=107,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9007,
        model_point=108,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9008,
        model_point=109,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=1042330400,
        asset=Assets.AEG300_006_9009,
        model_point=110,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9010, model_point=111, seconds=1.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9016, model_point=117, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9017, model_point=118, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9018, model_point=119, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9019, model_point=120, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9020, model_point=121, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9021, model_point=122, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9022, model_point=123, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9023, model_point=124, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9024, model_point=125, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9025, model_point=126, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9026, model_point=127, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9027, model_point=128, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9032, model_point=133, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9033, model_point=134, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9034, model_point=135, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9035, model_point=136, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9036, model_point=137, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9037, model_point=138, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9038, model_point=139, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9039, model_point=140, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9040, model_point=141, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9041, model_point=142, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9048, model_point=149, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9049, model_point=150, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9050, model_point=151, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9051, model_point=152, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9052, model_point=153, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9053, model_point=154, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9054, model_point=155, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9055, model_point=156, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9056, model_point=157, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9057, model_point=158, seconds=0.0)
    CommonFunc_90005453(0, asset__character=1042330400, asset=Assets.AEG300_006_9058, model_point=159, seconds=0.0)
    CommonFunc_90005456(0, 1042330400, 1042331410, 1042331418, 1042330400)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(0, 1042330400, 1042331400, 1042331410, 1042331418)


@RestartOnRest(1042332800)
def Event_1042332800():
    """Event 1042332800"""
    OR_1.Add(FlagEnabled(1042332800))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    DisableCharacter(1042335800)
    DisableAnimations(1042335800)
    DisableAsset(1042335801)
    AND_1.Add(FlagEnabled(1042330800))
    
    MAIN.Await(AND_1)
    
    Wait(7.0)
    EnableCharacter(1042335800)
    EnableAnimations(1042335800)
    EnableAsset(1042335801)
