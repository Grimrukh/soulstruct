"""
Liurnia to Altus Plateau (NE) (SE)

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
from .entities.m60_39_50_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005620(
        0,
        flag=1039500570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=1039502571,
        cancel_flag__right_flag=1039502572,
        right=1039502573,
    )
    Event_1039502580(
        0,
        flag=1039500800,
        flag_1=1039500805,
        flag_2=1039502800,
        character=Characters.GodricktheGrafted,
        item_lot=1039500100,
        area_id=60,
        block_id=39,
        cc_id=50,
        dd_id=0,
        player_start=1039502805,
    )
    CommonFunc_90005882(
        0,
        flag=1039500800,
        flag_1=1039500805,
        flag_2=1039502800,
        character=Characters.GodricktheGrafted,
        flag_3=1039502806,
        character_1=1039505810,
        asset=Assets.AEG099_120_3000,
        owner_entity=Characters.Dummy,
        source_entity=1039502810,
        name=904750520,
        animation_id=-1,
        animation_id_1=20012,
    )
    CommonFunc_90005885(
        0,
        flag=1039500800,
        bgm_boss_conv_param_id=921100,
        flag_1=1039502806,
        flag_2=1039502807,
        left=0,
        left_1=1,
    )
    Event_1039502575(
        0,
        flag=1039500800,
        flag_1=1039500805,
        left_flag=1039502801,
        cancel_flag__right_flag=1039502802,
        message=20300,
        anchor_entity=Assets.AEG099_170_3000,
        area_id=60,
        block_id=39,
        cc_id=50,
        dd_id=0,
        player_start=1039502805,
        flag_2=1039500570,
    )
    Event_1039502576(0, 1039500800, 1039500805, 1039501805, 1039500570)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005251(0, character=Characters.RevenantFollower, radius=30.0, seconds=1.0, animation_id=3022)
    CommonFunc_90005251(0, character=Characters.VulgarMilitia0, radius=20.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005251(0, character=Characters.VulgarMilitia1, radius=20.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005211(
        0,
        character=Characters.Misbegotten,
        animation_id=30000,
        animation_id_1=20000,
        region=1039502300,
        radius=5.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1039500302,
        animation_id=30000,
        animation_id_1=20000,
        region=1039502300,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1039500303, 30000, 20000, 1039502300, 1.5, 0, 0, 0, 0)


@RestartOnRest(1039502575)
def Event_1039502575(
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
    """Event 1039502575"""
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
    MoveCharacterAndCopyDrawParentWithFadeout(
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


@RestartOnRest(1039502576)
def Event_1039502576(_, flag: uint, flag_1: uint, entity: uint, flag_2: uint):
    """Event 1039502576"""
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


@RestartOnRest(1039502580)
def Event_1039502580(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    item_lot: int,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
):
    """Event 1039502580"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.GreatEnemyFelled)
    DeactivateGparamOverride(change_duration=10.0)
    AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)
    Wait(5.0)
    AddSpecialEffect(20000, 8870)
    Wait(2.0)
    EnableFlag(flag_2)
    EnableFlag(9295)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
    End()
