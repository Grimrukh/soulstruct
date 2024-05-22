"""
West Liurnia (SE) (NE)

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
from .enums.m60_35_45_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035450000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76205,
        asset=Assets.AEG099_090_9001,
        source_flag=77200,
        value=5,
        flag_2=78200,
        flag_3=78201,
        flag_4=78202,
        flag_5=78203,
        flag_6=78204,
        flag_7=78205,
        flag_8=78206,
        flag_9=78207,
        flag_10=78208,
        flag_11=78209,
    )
    CommonFunc_90005725(
        0,
        flag=4750,
        flag_1=4751,
        flag_2=4753,
        flag_3=1035459205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1035456700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4751,
        flag_1=4752,
        flag_2=1035459206,
        flag_3=4751,
        first_flag=4750,
        last_flag=4754,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4751, flag_1=4750, flag_2=1035459206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4753, first_flag=4750, last_flag=4754)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4751,
        flag_1=4752,
        flag_2=1035459207,
        flag_3=4751,
        first_flag=4750,
        last_flag=4754,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4751, flag_1=4750, flag_2=1035459207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1035452706, flag_1=1035452707)
    CommonFunc_90005727(
        0,
        flag=4751,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4750,
        last_flag=4753,
    )
    Event_1035452500()
    Event_1035452600(
        0,
        anchor_entity=Assets.AEG099_090_9000,
        area_id=60,
        block_id=35,
        cc_id=46,
        dd_id=0,
        player_start=1035462610,
        flag=1035460605,
        target_entity=1035452611,
        animation_id=60470,
        action_button_id=9522,
    )
    Event_1035452605(0, flag=1035450605, target_entity=1035452601, animation=60471)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    CommonFunc_90005251(0, character=Characters.WolfPackLeader, radius=10.0, seconds=0.0, animation_id=3011)
    CommonFunc_90005211(
        0,
        character=Characters.BloodhoundKnight,
        animation_id=30002,
        animation_id_1=20002,
        region=1035452210,
        radius=3.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )


@RestartOnRest(1035452500)
def Event_1035452500():
    """Event 1035452500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1035457100):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1035457100))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    DisplayDialog(text=30100, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(1035452600)
def Event_1035452600(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag: uint,
    target_entity: uint,
    animation_id: int,
    action_button_id: int,
):
    """Event 1035452600"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    SkipLinesIfConditionTrue(7, OR_1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    AND_9.Add(PlayerHasGood(8109))
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    DisplayDialog(text=20030, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    FaceEntity(PLAYER, target_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1035452605)
def Event_1035452605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1035452605"""
    if FlagDisabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    FaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)
