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
from .entities.m60_37_42_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005860(
        0,
        flag=1037420800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot__item_lot_param_id=1037420400,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DeathRiteBird, name=904980603, npc_threat_level=24)
    RegisterGrace(grace_flag=1037420000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76206,
        flag_1=76203,
        asset=Assets.AEG099_090_9001,
        source_flag=77200,
        value=3,
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
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=35,
        cc_id=45,
        dd_id=0,
        player_start=1035452630,
        unk_8_12=0,
        flag=1037422610,
        left_flag=1037422611,
        cancel_flag__right_flag=1037422612,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    RunEvent(1037422600, slot=0, args=(0,))
    CommonFunc_90005630(0, far_view_id=61374200, asset=Assets.AEG099_130_9000, model_point=123)
    Event_1037423700(0, character=Characters.RyatheScout, asset=Assets.AEG099_320_9000)
    Event_1037423702(0, flag=1037422704, flag_1=1037422703, flag_2=1037429207, seconds=20.0)
    Event_1037423703(0, attacked_entity=1037421700, other_entity=Characters.RyatheScout)
    CommonFunc_90005752(0, asset=Assets.AEG099_320_9000, vfx_id=200, model_point=120, seconds=3.0)
    Event_1037423710(0, character=Characters.Patches, asset=Assets.AEG003_363_1000)
    Event_1037423711(0, character=Characters.Patches, flag=1037422731, flag_1=1038419251)
    Event_1037423712()
    CommonFunc_90005704(0, attacked_entity=Characters.Patches, flag=3681, flag_1=3680, flag_2=1038419251, right=3)
    CommonFunc_90005703(0, 1037420720, 3681, 3682, 1038419251, 3681, 3680, 3684, -1)
    CommonFunc_90005702(0, 1037420720, 3683, 3680, 3684)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.RyatheScout)
    DisableBackread(1037420705)
    DisableAsset(Assets.AEG099_320_9000)
    CommonFunc_90005261(0, character=Characters.Revenant, region=1037422200, radius=2.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005251(0, character=Characters.RevenantFollower0, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005251(0, character=Characters.RevenantFollower1, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005251(0, character=Characters.RevenantFollower2, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005251(0, character=Characters.RevenantFollower4, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005251(0, character=Characters.RevenantFollower5, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005251(0, character=Characters.RevenantFollower6, radius=10.0, seconds=0.0, animation_id=1705)
    CommonFunc_90005261(0, character=1037420221, region=1037422200, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=1037420222, region=1037422200, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=1037420223, region=1037422200, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=1037420224, region=1037422200, radius=2.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, 1037420225, 1037422200, 2.0, 1.0, -1)
    CommonFunc_90005251(0, 1037420213, 10.0, 0.0, -1)
    CommonFunc_90005261(
        0,
        character=Characters.DeathRiteBird,
        region=1037422340,
        radius=10.0,
        seconds=0.0,
        animation_id=1700,
    )
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, 1037420301)


@RestartOnRest(1037422610)
def Event_1037422610(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 1037422610"""
    if Multiplayer():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=anchor_entity))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=4300,
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
    RotateToFaceEntity(PLAYER, anchor_entity, wait_for_completion=True)
    ForceAnimation(PLAYER, 60490)
    Wait(3.0)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1037423700)
def Event_1037423700(_, character: uint, asset: uint):
    """Event 1037423700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3420):
        DisableFlag(1038519203)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3425)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(3425))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3420)
    GotoIfFlagEnabled(Label.L2, flag=3421)
    GotoIfFlagEnabled(Label.L3, flag=3422)
    GotoIfFlagEnabled(Label.L4, flag=3423)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAsset(asset)
    MoveAssetToCharacter(asset, character=character)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAsset(asset)
    MoveAssetToCharacter(asset, character=character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAsset(asset)
    MoveAssetToCharacter(asset, character=character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    MoveAssetToCharacter(asset, character=character)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3425))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1037423702)
def Event_1037423702(_, flag: uint, flag_1: uint, flag_2: uint, seconds: float):
    """Event 1037423702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3420):
        return
    if FlagDisabled(3425):
        return
    if FlagEnabled(flag_2):
        return
    SetCharacterTalkRange(character=Characters.RyatheScout, distance=30.0)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Wait(seconds)
    EnableFlag(flag)
    End()


@RestartOnRest(1037423703)
def Event_1037423703(_, attacked_entity: uint, other_entity: uint):
    """Event 1037423703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3425):
        return
    if FlagEnabled(1037422708):
        return
    GotoIfFlagDisabled(Label.L1, flag=1037422701)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(TimeElapsed(seconds=7.0))
    OR_3.Add(AND_2)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionFalse(Label.L7, input_condition=AND_2)
    Wait(0.10000000149011612)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L5, flag=1037422701)
    GotoIfFlagDisabled(Label.L6, flag=1037422707)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    AND_5.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=10.0))
    SkipLinesIfConditionFalse(1, AND_5)
    EnableFlag(1037422702)
    
    MAIN.Await(FlagEnabled(1037422701))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    AND_6.Add(EntityWithinDistance(entity=20000, other_entity=other_entity, radius=10.0))
    SkipLinesIfConditionFalse(1, AND_6)
    EnableFlag(1037422706)
    
    MAIN.Await(FlagEnabled(1037422707))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(1037422708)
    End()


@RestartOnRest(1037423710)
def Event_1037423710(_, character: uint, asset: uint):
    """Event 1037423710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3687)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(3687))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    EnableAsset(asset)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3687))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1037423711)
def Event_1037423711(_, character: uint, flag: uint, flag_1: uint):
    """Event 1037423711"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3683):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    if AND_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(3681))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 9700))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    MAIN.Await(AND_2)
    
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ReplanAI(character)
    End()


@RestartOnRest(1037423712)
def Event_1037423712():
    """Event 1037423712"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(31009206):
        return
    if FlagEnabled(1038419254):
        return
    AND_1.Add(FlagDisabled(3685))
    AND_1.Add(FlagDisabled(3686))
    AND_1.Add(FlagDisabled(3687))
    if AND_1:
        return
    EnableFlag(1038419254)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()
