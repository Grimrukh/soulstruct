"""
West Liurnia (NE) (SE)

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
from .enums.m60_35_46_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035460000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76206,
        asset=Assets.AEG099_090_9002,
        source_flag=77200,
        value=6,
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
    CommonFunc_90005201(
        0,
        character=1035460350,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1035462600(
        0,
        anchor_entity=Assets.AEG099_090_9000,
        area_id=60,
        block_id=35,
        cc_id=45,
        dd_id=0,
        player_start=1035452610,
        flag=1035450605,
        target_entity=Assets.AEG099_261_2001,
        animation_id=60470,
        action_button_id=9522,
    )
    Event_1035462600(
        1,
        anchor_entity=Assets.AEG099_090_9001,
        area_id=60,
        block_id=36,
        cc_id=47,
        dd_id=0,
        player_start=1036472610,
        flag=1036470605,
        target_entity=Assets.AEG099_261_2000,
        animation_id=60470,
        action_button_id=9522,
    )
    Event_1035462605(0, flag=1035460605, target_entity=1035462601, animation=60471)
    Event_1035462605(1, flag=1035460615, target_entity=1035462606, animation=60471)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9011, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005795(
        0,
        flag=7607,
        flag_1=0,
        flag_2=1035469205,
        left_flag=1035462141,
        cancel_flag__right_flag=1035462142,
        message=80607,
        action_button_id=9000,
        asset=Assets.AEG099_090_9020,
        model_point=30010,
    )
    if CeremonyActive(ceremony=40):
        CommonFunc_90005796(
            0,
            flag=7607,
            character=Characters.BloodyFingerRavenmountAssassin,
            banner_type=5,
            region=1035462141,
        )
        Event_1035462145()
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.YuraHunterofBloodyFingers1,
        flag=3621,
        flag_1=3620,
        flag_2=1035469201,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.YuraHunterofBloodyFingers1,
        flag=3621,
        flag_1=3622,
        flag_2=1035469201,
        flag_3=3621,
        first_flag=3620,
        last_flag=3624,
        right=-1,
    )
    CommonFunc_90005702(
        0,
        character=Characters.YuraHunterofBloodyFingers1,
        flag=1035469209,
        first_flag=1035469209,
        last_flag=1035469209,
    )
    Event_1035463700(0, character=Characters.YuraHunterofBloodyFingers1)
    Event_1035463701()
    Event_1035463702(0, character=Characters.YuraHunterofBloodyFingers1)
    CommonFunc_90005774(0, flag=7607, item_lot=1035460700, flag_1=1035467700)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.YuraHunterofBloodyFingers1)
    DisableBackread(Characters.YuraHunterofBloodyFingers0)
    DisableBackread(Characters.BloodyFingerRavenmountAssassin)
    CommonFunc_90005251(0, character=Characters.Wolf0, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Wolf1, radius=7.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1035462145)
def Event_1035462145():
    """Event 1035462145"""
    if CeremonyInactive(ceremony=40):
        return
    EnableBackread(Characters.BloodyFingerRavenmountAssassin)
    EnableBackread(Characters.YuraHunterofBloodyFingers0)
    SetTeamType(Characters.BloodyFingerRavenmountAssassin, TeamType.Human)
    SetTeamType(Characters.YuraHunterofBloodyFingers0, TeamType.Enemy)
    DeleteAssetVFX(1035466700)
    CreateAssetVFX(1035466700, vfx_id=200, model_point=806700)


@RestartOnRest(1035463700)
def Event_1035463700(_, character: uint):
    """Event 1035463700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3620):
        DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3627)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3627))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3627))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1035463701)
def Event_1035463701():
    """Event 1035463701"""
    WaitFrames(frames=1)
    if FlagEnabled(3631):
        return
    if FlagDisabled(3620):
        return
    if FlagDisabled(1043379260):
        return
    EnableFlag(1035469205)
    End()


@RestartOnRest(1035463702)
def Event_1035463702(_, character: uint):
    """Event 1035463702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043359259):
        return
    if FlagEnabled(1044389209):
        return
    if FlagEnabled(1039529209):
        return
    GotoIfFlagEnabled(Label.L1, flag=1035469209)
    
    MAIN.Await(FlagEnabled(1035469209))
    
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    if FlagEnabled(3627):
        return
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(1035462600)
def Event_1035462600(
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
    """Event 1035462600"""
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
    RotateToFaceEntity(PLAYER, target_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, animation_id)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1035462605)
def Event_1035462605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1035462605"""
    if FlagDisabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)
