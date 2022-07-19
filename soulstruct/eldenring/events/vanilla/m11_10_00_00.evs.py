"""
Roundtable Hold

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
from .entities.m11_10_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=11100000, asset=Assets.AEG099_060_9000, enemy_block_distance=1.0)
    Event_11100020()
    Event_11100030()
    Event_11100031()
    CommonFunc_90005790(
        0,
        right=0,
        flag=11100180,
        summon_flag=11102180,
        dismissal_flag=11102181,
        character=Characters.MadTongueAlberich,
        sign_type=23,
        region=11102385,
        region_1=11102386,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=11100180, flag_1=11102180, flag_2=11102181, character=Characters.MadTongueAlberich)
    CommonFunc_90005792(
        0,
        flag=11100180,
        flag_1=11102180,
        flag_2=11102181,
        character=Characters.MadTongueAlberich,
        item_lot_param_id=11100800,
        seconds=0.0,
    )
    Event_11102600()
    Event_11102602()
    Event_11102605()
    Event_11102606()
    Event_11102620(
        0,
        flag=11100180,
        left_flag=11102621,
        cancel_flag__right_flag=11102622,
        asset=Assets.AEG099_065_9000,
        player_start=11102620,
        area_id=11,
        block_id=10,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005620(
        0,
        flag=11100570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=11102570,
        cancel_flag__right_flag=11102571,
        right=11102572,
    )
    CommonFunc_90005621(0, flag=11100570, asset=Assets.AEG099_270_9000)
    CommonFunc_90005620(
        0,
        flag=11100575,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9001,
        asset_2=Assets.AEG027_217_9000,
        left_flag=11102575,
        cancel_flag__right_flag=11102576,
        right=11102577,
    )
    CommonFunc_90005621(0, flag=11100575, asset=Assets.AEG099_270_9001)
    Event_11102680()
    Event_11103700(0, character=Characters.ScalyMisbegotten)
    RunCommonEvent(11103702)
    RunCommonEvent(11103703)
    Event_11103705(0, character=Characters.FingerReaderEnia)
    CommonFunc_90005708(0, character=Characters.FingerReaderEnia, flag=3480, left=0)
    Event_11103706(0, entity=Characters.TheTwoFingers)
    Event_11103707(0, entity=Characters.TheTwoFingers)
    CommonFunc_90005708(0, character=Characters.FingerReaderEnia, flag=11109355, left=0)
    Event_11103710(0, character=Characters.Roderika0)
    Event_11103711(0, character=Characters.Roderika1)
    Event_11103712(0, character=Characters.Roderika2)
    Event_11103713()
    Event_11103714(0, entity=Characters.Roderika1)
    Event_11100704()
    Event_11103715(0, character=Characters.KnightDiallos0)
    Event_11103716(0, character=Characters.KnightDiallos1)
    Event_11103720(0, character=Characters.YuraHunterofBloodyFingers)
    Event_11100730(0, character=Characters.DHunteroftheDead0, asset=Assets.AEG221_524_4500)
    Event_11100731(
        0,
        character=Characters.DHunteroftheDead1,
        asset=Assets.AEG099_421_9000,
        entity=Assets.AEG227_033_0501,
    )
    Event_11100732()
    CommonFunc_90005708(0, character=Characters.DHunteroftheDead0, flag=4110, left=0)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot_param_id=103400,
        first_flag=400349,
        last_flag=400349,
        flag=4048,
        model_point=0,
    )
    CommonFunc_90005775(0, 81463900, 1045399206, -1.0)
    Event_11100735(0, character=Characters.FiaDeathbedCompanion0)
    Event_11100736(0, character=Characters.FiaDeathbedCompanion1)
    CommonFunc_90005740(
        0,
        11102845,
        11102846,
        11102847,
        11100740,
        702,
        11101741,
        702,
        0.4000000059604645,
        90300,
        90302,
        -1,
        1.2999999523162842,
    )
    CommonFunc_90005741(0, 11102848, 11102849, 11102847, 11100740, 90320, 0, 90322, -1, 0.5)
    Event_11100737(0, entity=Characters.FiaDeathbedCompanion1)
    CommonFunc_90005733(0, flag=11102844)
    Event_11100750(0, character=Characters.SorcererRogier, asset=Assets.AEG221_531_4500)
    CommonFunc_90005708(0, character=Characters.SorcererRogier, flag=3900, left=0)
    CommonFunc_90005708(0, character=Characters.SorcererRogier, flag=3903, left=0)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4110,
        item_lot_param_id=103590,
        first_flag=400359,
        last_flag=400359,
        flag=3909,
        model_point=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4110,
        item_lot_param_id=103580,
        first_flag=400356,
        last_flag=400358,
        flag=400359,
        model_point=0,
    )
    Event_11100740(0, character=Characters.SirGideonOfnir0)
    Event_11100741(0, character=Characters.SirGideonOfnir1)
    CommonFunc_90005775(0, 85495300, 11109687, -1.0)
    Event_11100745(0, character=Characters.BrotherCorhyn)
    Event_11100755(0, character=Characters.DungEater0)
    Event_11100756(0, character=Characters.DungEater1)
    Event_11100760(0, character=Characters.NepheliLoux0)
    Event_11100761(0, character=Characters.NepheliLoux1)
    Event_11100765(0, character=Characters.EnshaoftheRoyalRemains0)
    CommonFunc_90005774(0, flag=11109656, item_lot_param_id=11100900, flag_1=11107900)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9002,
        action_button_id=4110,
        item_lot_param_id=104900,
        first_flag=400490,
        last_flag=400490,
        flag=11109656,
        model_point=0,
    )
    RunCommonEvent(11103770)
    RunCommonEvent(11103771)
    RunCommonEvent(11103772)
    Event_11103775()
    Event_11100790()
    Event_11100791(0, flag=400282, flag_1=11109770)
    Event_11100791(1, flag=400283, flag_1=11109771)
    Event_11100791(2, flag=68210, flag_1=11109772)
    Event_11100791(3, flag=400285, flag_1=11109773)
    Event_11100795()
    Event_11100796()
    Event_11100797()
    Event_11102651(0, flag=710700, tutorial_param_id=1700, item=9125, flag_1=69250)
    Event_11102650(0, flag=710720, tutorial_param_id=1720, item=9128, flag_1=69280)
    Event_11102652(0, 710780, 1780, 9132, 69320)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.FingerReaderEnia)
    DisableBackread(Characters.Roderika0)
    DisableBackread(Characters.Roderika1)
    DisableBackread(Characters.ScalyMisbegotten)
    DisableBackread(Characters.KnightDiallos0)
    DisableBackread(Characters.KnightDiallos1)
    DisableBackread(Characters.DHunteroftheDead0)
    DisableBackread(Characters.DHunteroftheDead1)
    DisableBackread(Characters.FiaDeathbedCompanion0)
    DisableBackread(Characters.FiaDeathbedCompanion1)
    DisableBackread(Characters.DungEater0)
    DisableBackread(Characters.DungEater1)
    DisableBackread(Characters.SirGideonOfnir0)
    DisableBackread(Characters.SirGideonOfnir1)
    DisableBackread(Characters.SorcererRogier)
    DisableBackread(Characters.EnshaoftheRoyalRemains0)
    DisableBackread(Characters.EnshaoftheRoyalRemains1)
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(Characters.NepheliLoux0)
    DisableBackread(Characters.NepheliLoux1)
    DisableBackread(Characters.MadTongueAlberich)
    EnableAssetInvulnerability(Assets.AEG221_531_4500)
    EnableAssetInvulnerability(Assets.AEG221_524_4500)
    Event_11002548()
    Event_11100680()
    Event_11102100()


@NeverRestart(11100020)
def Event_11100020():
    """Event 11100020"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(InsideMap(game_map=ROUNDTABLE_HOLD))
    
    MAIN.Await(AND_1)
    
    EnableFlag(71190)
    OpenWorldMapPoint(world_map_point_param_id=111000, distance=100.0)
    EnableFlag(105)


@RestartOnRest(11100030)
def Event_11100030():
    """Event 11100030"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(3001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(30)


@NeverRestart(11100031)
def Event_11100031():
    """Event 11100031"""
    if FlagDisabled(120):
        return
    if FlagEnabled(121):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(120))
    
    MAIN.Await(AND_1)
    
    DisableFlag(71900)
    EnableFlag(121)


@NeverRestart(11102100)
def Event_11102100():
    """Event 11102100"""
    GotoIfFlagEnabled(Label.L1, flag=302)
    GotoIfFlagDisabled(Label.L0, flag=300)
    SetWeather(weather=Weather.WindyPuffyClouds, duration=-1.0, immediate_change=True)
    DeleteVFX(11102100, erase_root_only=False)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetWeather(weather=Weather.Cloudless, duration=-1.0, immediate_change=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(11102101, erase_root_only=False)
    DeleteVFX(11102110, erase_root_only=False)
    DeleteVFX(11102111, erase_root_only=False)
    DeleteVFX(11102112, erase_root_only=False)
    DeleteVFX(11102113, erase_root_only=False)
    DeleteVFX(11102114, erase_root_only=False)
    DeleteVFX(11102115, erase_root_only=False)
    DeleteVFX(11102116, erase_root_only=False)
    DeleteVFX(11102117, erase_root_only=False)
    DeleteVFX(11102118, erase_root_only=False)
    DeleteVFX(11102119, erase_root_only=False)
    DeleteVFX(11102120, erase_root_only=False)
    DeleteVFX(11102121, erase_root_only=False)
    DeleteVFX(11102122, erase_root_only=False)
    DeleteVFX(11102123, erase_root_only=False)
    DeleteVFX(11102124, erase_root_only=False)
    DeleteVFX(11102125, erase_root_only=False)
    DeleteVFX(11102126, erase_root_only=False)
    DeleteVFX(11102127, erase_root_only=False)
    DeleteVFX(11102128, erase_root_only=False)
    DeleteVFX(11102129, erase_root_only=False)
    DeleteVFX(11102130, erase_root_only=False)
    DeleteVFX(11102131, erase_root_only=False)
    DeleteVFX(11102132, erase_root_only=False)
    DeleteVFX(11102133, erase_root_only=False)
    DeleteVFX(11102134, erase_root_only=False)
    DeleteVFX(11102135, erase_root_only=False)
    DeleteVFX(11102136, erase_root_only=False)
    DeleteVFX(11102137, erase_root_only=False)
    DeleteVFX(11102138, erase_root_only=False)
    DeleteVFX(11102139, erase_root_only=False)
    DeleteVFX(11102140, erase_root_only=False)
    DeleteVFX(11102141, erase_root_only=False)
    DeleteVFX(11102142, erase_root_only=False)
    DeleteVFX(11102143, erase_root_only=False)
    DeleteVFX(11102144, erase_root_only=False)
    DeleteVFX(11102145, erase_root_only=False)
    DeleteVFX(11102146, erase_root_only=False)
    DeleteVFX(11102147, erase_root_only=False)
    End()


@RestartOnRest(11002548)
def Event_11002548():
    """Event 11002548"""
    if FlagEnabled(11108548):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(181))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11108548)


@RestartOnRest(11102600)
def Event_11102600():
    """Event 11102600"""
    DisableNetworkSync()
    RemoveSpecialEffect(PLAYER, 9621)
    AND_1.Add(InsideMap(game_map=ROUNDTABLE_HOLD))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=11102600))
    AND_1.Add(CeremonyInactive(ceremony=20))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 9621)
    Wait(1.0)
    AND_2.Add(InsideMap(game_map=ROUNDTABLE_HOLD))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=11102600))
    AND_2.Add(CeremonyInactive(ceremony=20))
    
    MAIN.Await(not AND_2)
    
    Restart()


@RestartOnRest(11102602)
def Event_11102602():
    """Event 11102602"""
    if OutsideMap(game_map=ROUNDTABLE_HOLD):
        return
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=ROUNDTABLE_HOLD,
        x=-305.70001220703125,
        y=-20.579999923706055,
        z=-298.1000061035156,
    )


@RestartOnRest(11102605)
def Event_11102605():
    """Event 11102605"""
    AwaitFlagEnabled(flag=3063)
    EndOfAnimation(asset=Assets.AEG227_033_0500, animation_id=2)
    End()


@RestartOnRest(11102606)
def Event_11102606():
    """Event 11102606"""
    AND_1.Add(FlagEnabled(11109659))
    AND_1.Add(FlagEnabled(3966))
    AND_2.Add(FlagEnabled(11109358))
    AND_2.Add(FlagEnabled(11109660))
    AND_2.Add(FlagEnabled(3967))
    AND_3.Add(FlagEnabled(110))
    AND_3.Add(FlagEnabled(3967))
    OR_1.Add(FlagEnabled(11109358))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AwaitConditionTrue(OR_1)
    EndOfAnimation(asset=Assets.AEG227_033_0502, animation_id=2)
    End()


@NeverRestart(11102620)
def Event_11102620(
    _,
    flag: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
    asset: uint,
    player_start: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
):
    """Event 11102620"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        CreateAssetVFX(asset, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9290, entity=asset))
    
    MAIN.Await(AND_2)
    
    DisplayDialogAndSetFlags(
        message=4100,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    EnableFlag(cancel_flag__right_flag)
    Wait(2.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(PLAYER, Assets.AEG099_065_9000, wait_for_completion=True)
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start, unk_8_12=-11100)


@RestartOnRest(11102650)
def Event_11102650(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(104))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(11102651)
def Event_11102651(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102651"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(105))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(11102652)
def Event_11102652(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 11102652"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(InsideMap(game_map=ROUNDTABLE_HOLD))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(2.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@NeverRestart(11100680)
def Event_11100680():
    """Event 11100680"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    if FlagEnabled(11109656):
        return
    DisableHealthBar(Characters.TalkDummy3)
    ActivateGparamOverride(gparam_sub_id=1, change_duration=0.0)
    SetTeamType(Characters.EnshaoftheRoyalRemains1, TeamType.Enemy)
    EndOfAnimation(asset=1110548, animation_id=0)
    AND_1.Add(CharacterDead(Characters.EnshaoftheRoyalRemains1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11109656)
    DisplayBanner(BannerType.GreatEnemyFelled)
    DisableFlag(1035429211)
    SetPseudoMultiplayerReturnPosition(region=11102766)
    AddSpecialEffect(20000, 4820)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@NeverRestart(11102680)
def Event_11102680():
    """Event 11102680"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    if FlagEnabled(11109656):
        return
    EnableBackread(Characters.EnshaoftheRoyalRemains1)
    DisableAI(Characters.EnshaoftheRoyalRemains1)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=11102681))
    OR_1.Add(TimeElapsed(seconds=5.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.EnshaoftheRoyalRemains1, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=11000766, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=11000766, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=11000766, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=11000766, state_info=260))
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.EnshaoftheRoyalRemains1)


@RestartOnRest(11103700)
def Event_11103700(_, character: uint):
    """Event 11103700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3220):
        DisableFlag(11009248)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG221_610_4500)
    DisableAsset(Assets.AEG221_657_4500)
    OR_1.Add(FlagEnabled(3225))
    OR_1.Add(FlagEnabled(3226))
    OR_1.Add(FlagEnabled(3227))
    OR_1.Add(FlagEnabled(3228))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3225))
    OR_2.Add(FlagEnabled(3226))
    OR_2.Add(FlagEnabled(3227))
    OR_2.Add(FlagEnabled(3228))
    
    MAIN.Await(OR_2)
    
    Restart()
    SetCharacterTalkRange(character=character, distance=50.0)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3220)
    GotoIfFlagEnabled(Label.L2, flag=3221)
    GotoIfFlagEnabled(Label.L4, flag=3223)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_5.Add(CeremonyActive(ceremony=20))
    AND_5.Add(FlagEnabled(1035429211))
    SkipLinesIfConditionTrue(6, AND_5)
    DeleteAssetVFX(Assets.AEG099_090_9001)
    CreateAssetVFX(Assets.AEG099_090_9001, vfx_id=100, model_point=803450)
    if FlagEnabled(110):
        EnableAsset(Assets.AEG221_657_4500)
    if FlagDisabled(110):
        EnableAsset(Assets.AEG221_610_4500)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    AND_10.Add(FlagEnabled(3225))
    AND_10.Add(FlagEnabled(11109205))
    AND_10.Add(FlagDisabled(11109209))
    AND_10.Add(FlagEnabled(11109206))
    SkipLinesIfConditionFalse(1, AND_10)
    ForceAnimation(character, 930013)
    AND_11.Add(FlagEnabled(3225))
    AND_11.Add(FlagEnabled(11109209))
    AND_11.Add(FlagDisabled(11109339))
    AND_11.Add(FlagEnabled(11109340))
    SkipLinesIfConditionFalse(1, AND_11)
    ForceAnimation(character, 930015)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, 920015)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_3.Add(FlagEnabled(3225))
    OR_3.Add(FlagEnabled(3226))
    OR_3.Add(FlagEnabled(3227))
    OR_3.Add(FlagEnabled(3228))
    
    MAIN.Await(not OR_3)
    
    Restart()


@RestartOnRest(11103702)
def Event_11103702():
    """Event 11103702"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=11102700))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.ScalyMisbegotten, radius=8.0))
    AND_1.Add(FlagEnabled(3225))
    AND_1.Add(FlagEnabled(11109205))
    AND_1.Add(FlagDisabled(11102702))
    AND_1.Add(FlagDisabled(11109209))
    AND_1.Add(FlagEnabled(11109206))
    AND_1.Add(OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11102704)
    End()


@RestartOnRest(11103703)
def Event_11103703():
    """Event 11103703"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=11102700))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.ScalyMisbegotten, radius=8.0))
    AND_1.Add(FlagEnabled(3225))
    AND_1.Add(FlagEnabled(11109205))
    AND_1.Add(FlagDisabled(11102702))
    AND_1.Add(FlagEnabled(11109209))
    AND_1.Add(FlagDisabled(11109339))
    AND_1.Add(FlagEnabled(11109340))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(11102708)
    End()


@RestartOnRest(11100704)
def Event_11100704():
    """Event 11100704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109213):
        return
    
    MAIN.Await(FlagEnabled(11109213))
    
    EnableFlag(10007450)
    DisableFlag(10007452)


@RestartOnRest(11103705)
def Event_11103705(_, character: uint):
    """Event 11103705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3480):
        DisableFlag(11109355)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=3489)
    OR_1.Add(FlagEnabled(3485))
    OR_1.Add(FlagEnabled(3486))
    OR_1.Add(FlagEnabled(3487))
    OR_1.Add(FlagEnabled(3488))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3485))
    OR_3.Add(FlagEnabled(3486))
    OR_3.Add(FlagEnabled(3487))
    OR_3.Add(FlagEnabled(3488))
    OR_3.Add(FlagEnabled(3489))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3480)
    GotoIfFlagEnabled(Label.L2, flag=3481)
    GotoIfFlagEnabled(Label.L3, flag=3482)
    GotoIfFlagEnabled(Label.L4, flag=3483)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
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
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(3485))
    OR_4.Add(FlagEnabled(3486))
    OR_4.Add(FlagEnabled(3487))
    OR_4.Add(FlagEnabled(3488))
    OR_4.Add(FlagEnabled(3489))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(11103706)
def Event_11103706(_, entity: uint):
    """Event 11103706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(60843):
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=6321, entity=entity))
    
    EnableFlag(60843)
    AwardGesture(gesture_param_id=102)
    End()


@RestartOnRest(11103707)
def Event_11103707(_, entity: uint):
    """Event 11103707"""
    ForceAnimation(entity, 930001)
    WaitFrames(frames=1)
    if FlagEnabled(3485):
        return
    if FlagEnabled(3486):
        return
    ForceAnimation(entity, 930000)
    End()


@RestartOnRest(11103710)
def Event_11103710(_, character: uint):
    """Event 11103710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3707))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_2.Add(FlagEnabled(3707))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(3707))
    
    Restart()


@RestartOnRest(11103711)
def Event_11103711(_, character: uint):
    """Event 11103711"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3708))
    AND_1.Add(FlagEnabled(3709))
    AND_1.Add(FlagEnabled(11109279))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    AND_5.Add(FlagEnabled(3709))
    AND_5.Add(FlagDisabled(11109279))
    SkipLinesIfConditionTrue(1, AND_5)
    DisableAsset(Assets.AEG221_498_4500)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(Assets.AEG221_498_4500)
    ForceAnimation(character, 90104)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    AND_15.Add(FlagDisabled(3708))
    AND_15.Add(FlagDisabled(3709))
    
    MAIN.Await(AND_15)
    
    Restart()


@RestartOnRest(11103712)
def Event_11103712(_, character: uint):
    """Event 11103712"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(3709))
    AND_1.Add(FlagDisabled(11109279))
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90103)
    EnableNetworkFlag(11102719)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(3709))
    
    Restart()


@RestartOnRest(11103713)
def Event_11103713():
    """Event 11103713"""
    if FlagEnabled(11109266):
        return
    AwaitFlagEnabled(flag=1041389415)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=10903, flag=1041389417, bit_count=10)
    StoreItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=10913, flag=1041389427, bit_count=10)
    DisableFlag(1041389415)
    EnableFlag(1041389416)
    Restart()


@RestartOnRest(11103714)
def Event_11103714(_, entity: uint):
    """Event 11103714"""
    if FlagDisabled(11109265):
        return
    AND_1.Add(FlagEnabled(11109266))
    AND_1.Add(FlagDisabled(11109267))
    if AND_1:
        return
    if FlagDisabled(1041389411):
        return
    AND_2.Add(FlagEnabled(3063))
    AND_2.Add(FlagDisabled(11109268))
    if AND_2:
        return
    AND_3.Add(FlagEnabled(11109268))
    AND_3.Add(FlagDisabled(35009306))
    if AND_3:
        return
    AND_4.Add(FlagEnabled(11109268))
    AND_4.Add(FlagEnabled(4247))
    AND_4.Add(FlagDisabled(11109270))
    if AND_4:
        return
    AND_5.Add(FlagEnabled(11109268))
    AND_5.Add(FlagEnabled(4248))
    AND_5.Add(FlagDisabled(11109272))
    if AND_5:
        return
    AND_6.Add(FlagEnabled(11109272))
    AND_6.Add(FlagEnabled(4249))
    AND_6.Add(FlagDisabled(11109271))
    if AND_6:
        return
    AND_10.Add(FlagEnabled(3708))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=11102700))
    AND_11.Add(FlagEnabled(3709))
    AND_11.Add(FlagEnabled(11109279))
    AND_11.Add(CharacterInsideRegion(character=PLAYER, region=11102700))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    AwaitConditionTrue(OR_10)
    EnableRandomFlagInRange(flag_range=(11102710, 11102716))
    GotoIfFlagEnabled(Label.L1, flag=11102710)
    GotoIfFlagEnabled(Label.L2, flag=11102711)
    GotoIfFlagEnabled(Label.L3, flag=11102712)
    GotoIfFlagRangeAnyEnabled(Label.L20, flag_range=(11102713, 11102716))

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(entity, 90202)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(entity, 90203)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(entity, 90204)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(11103715)
def Event_11103715(_, character: uint):
    """Event 11103715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3440))
    AND_1.Add(FlagEnabled(11109405))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3445))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    
    MAIN.Await(FlagEnabled(3445))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
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
    
    MAIN.Await(FlagDisabled(3445))
    
    Restart()


@RestartOnRest(11103716)
def Event_11103716(_, character: uint):
    """Event 11103716"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3440))
    AND_1.Add(FlagEnabled(11109405))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(11109405)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3447))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    
    MAIN.Await(FlagEnabled(3447))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3440)
    GotoIfFlagEnabled(Label.L2, flag=3441)
    GotoIfFlagEnabled(Label.L3, flag=3442)
    GotoIfFlagEnabled(Label.L4, flag=3443)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
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
    
    MAIN.Await(FlagDisabled(3447))
    
    Restart()


@RestartOnRest(11103720)
def Event_11103720(_, character: uint):
    """Event 11103720"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(11100730)
def Event_11100730(_, character: uint, asset: uint):
    """Event 11100730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=4047)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAssetInvulnerability(asset)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(4047))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableCharacter(character)
    EnableBackread(character)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    EnableAsset(asset)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4047))
    
    Restart()


@RestartOnRest(11100731)
def Event_11100731(_, character: uint, asset: uint, entity: uint):
    """Event 11100731"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L8, flag=4048)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(4048))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    ForceAnimation(entity, 2)
    GotoIfFlagRangeAllEnabled(Label.L3, flag_range=(400349, 400349))
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    ForceAnimation(character, 90104)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4048))
    
    Restart()


@RestartOnRest(11100732)
def Event_11100732():
    """Event 11100732"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109609):
        return
    
    MAIN.Await(FlagEnabled(4046))
    
    EnableFlag(11109609)
    EnableFlag(4058)


@RestartOnRest(11100735)
def Event_11100735(_, character: uint):
    """Event 11100735"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L5, flag=4125)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4125))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4125))
    
    Restart()


@RestartOnRest(11100736)
def Event_11100736(_, character: uint):
    """Event 11100736"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4126)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4126))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4126))
    
    Restart()


@RestartOnRest(11100737)
def Event_11100737(_, entity: uint):
    """Event 11100737"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(4126))
    AND_1.Add(FlagEnabled(11109015))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 90207)


@RestartOnRest(11100740)
def Event_11100740(_, character: uint):
    """Event 11100740"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3965)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3965))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3960)
    GotoIfFlagEnabled(Label.L2, flag=3961)
    GotoIfFlagEnabled(Label.L4, flag=3963)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(3965))
    
    Restart()


@RestartOnRest(11100741)
def Event_11100741(_, character: uint):
    """Event 11100741"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3966))
    OR_1.Add(FlagEnabled(3967))
    GotoIfConditionTrue(Label.L6, input_condition=OR_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_2.Add(FlagEnabled(3966))
    OR_2.Add(FlagEnabled(3967))
    AwaitConditionTrue(OR_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3960)
    GotoIfFlagEnabled(Label.L2, flag=3961)
    GotoIfFlagEnabled(Label.L4, flag=3963)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    AND_1.Add(FlagDisabled(3966))
    AND_1.Add(FlagDisabled(3967))
    AwaitConditionTrue(AND_1)
    Restart()


@RestartOnRest(11100745)
def Event_11100745(_, character: uint):
    """Event 11100745"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4205))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    
    MAIN.Await(FlagEnabled(4205))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
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
    
    MAIN.Await(FlagDisabled(4205))
    
    Restart()


@RestartOnRest(11100750)
def Event_11100750(_, character: uint, asset: uint):
    """Event 11100750"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(11109527):
        EnableFlag(11109529)
    if FlagEnabled(11109535):
        IncrementEventValue(11109545, bit_count=5, max_value=2)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L7, flag=3907)
    GotoIfFlagEnabled(Label.L8, flag=3908)
    GotoIfFlagEnabled(Label.L9, flag=3909)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAssetInvulnerability(asset)
    DisableAsset(asset)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3907, 3909)))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3907))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
    DefineLabel(9)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SkipLinesIfFlagEnabled(1, 11109522)
    EnableFlag(400356)
    GotoIfFlagRangeAllEnabled(Label.L3, flag_range=(400356, 400359))
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90106)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAssetInvulnerability(asset)
    DisableAsset(asset)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3908, 3909)))
    
    Restart()


@RestartOnRest(11100755)
def Event_11100755(_, character: uint):
    """Event 11100755"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4245))
    AND_1.Add(FlagEnabled(4246))
    AND_1.Add(FlagDisabled(35009315))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(4245))
    AND_2.Add(FlagEnabled(4246))
    AND_2.Add(FlagDisabled(35009315))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(4245))
    AND_15.Add(FlagEnabled(4246))
    AND_15.Add(FlagDisabled(35009315))
    OR_15.Add(AND_15)
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(11100756)
def Event_11100756(_, character: uint):
    """Event 11100756"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4248))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    
    MAIN.Await(FlagEnabled(4248))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(4248))
    
    Restart()


@RestartOnRest(11100760)
def Event_11100760(_, character: uint):
    """Event 11100760"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    OR_1.Add(FlagEnabled(3966))
    OR_1.Add(FlagEnabled(3967))
    AND_1.Add(FlagEnabled(4226))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    AND_2.Add(FlagEnabled(4226))
    AND_2.Add(FlagEnabled(4223))
    GotoIfConditionTrue(Label.L4, input_condition=AND_2)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3966))
    OR_3.Add(FlagEnabled(3967))
    AND_3.Add(OR_3)
    AND_3.Add(FlagEnabled(4226))
    
    MAIN.Await(AND_3)
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3966))
    OR_15.Add(FlagEnabled(3967))
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(4226))
    
    MAIN.Await(not AND_15)
    
    Restart()


@RestartOnRest(11100761)
def Event_11100761(_, character: uint):
    """Event 11100761"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=4228)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(4228))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=4220)
    GotoIfFlagEnabled(Label.L2, flag=4221)
    GotoIfFlagEnabled(Label.L4, flag=4223)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(4228))
    
    Restart()


@RestartOnRest(11100765)
def Event_11100765(_, character: uint):
    """Event 11100765"""
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(110))
    OR_1.Add(FlagEnabled(11109656))
    AwaitConditionFalse(OR_1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    End()


@RestartOnRest(11103770)
def Event_11103770():
    """Event 11103770"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(11109340))
    AND_1.Add(FlagEnabled(11109558))
    if AND_1:
        return
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(71100, 71108)))
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(73500, 73504)))
    AwaitConditionTrue(OR_1)
    EnableNetworkFlag(11109340)
    EnableNetworkFlag(11109558)
    End()


@RestartOnRest(11103771)
def Event_11103771():
    """Event 11103771"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109559):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(71500, 71508)))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109559)
    End()


@RestartOnRest(11103772)
def Event_11103772():
    """Event 11103772"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109560):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(71250, 71253)))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11109560)
    End()


@NeverRestart(11103775)
def Event_11103775():
    """Event 11103775"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11109786):
        DisableFlag(11109786)
        End()
    if CeremonyActive(ceremony=20):
        return
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=11102020, radius=1.0))
    if not AND_15:
        return
    Wait(0.10000000149011612)
    AND_1.Add(FlagEnabled(1034509254))
    AND_2.Add(FlagEnabled(11109785))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    DisableFlag(11109785)
    DisplayDialog(text=30120, anchor_entity=0, display_distance=5.0, number_buttons=NumberButtons.OneButton)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(1034509254)
    DisplayDialog(text=30130, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    End()


@RestartOnRest(11100790)
def Event_11100790():
    """Event 11100790"""
    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(11102790)
    End()


@RestartOnRest(11100791)
def Event_11100791(_, flag: uint, flag_1: uint):
    """Event 11100791"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    OR_1.Add(FlagEnabled(3968))
    OR_2.Add(FlagEnabled(flag))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFlagDisabled(3, 3968)
    SkipLinesIfFlagEnabled(2, flag)
    EnableFlag(flag_1)
    EnableFlag(11109785)
    End()


@RestartOnRest(11100795)
def Event_11100795():
    """Event 11100795"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9614))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9615))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60540)
    Wait(0.20000000298023224)
    Restart()


@NeverRestart(11100796)
def Event_11100796():
    """Event 11100796"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(182):
        return
    AND_1.Add(FlagDisabled(60020))
    AND_1.Add(FlagDisabled(11109774))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(11109774)
    EnableFlag(11109785)
    AND_2.Add(FlagDisabled(60120))
    AND_2.Add(FlagDisabled(11109775))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(11109775)
    EnableFlag(11109785)
    AND_3.Add(FlagDisabled(60130))
    AND_3.Add(FlagDisabled(11109776))
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(11109776)
    EnableFlag(11109785)
    End()


@NeverRestart(11100797)
def Event_11100797():
    """Event 11100797"""
    if PlayerNotInOwnWorld():
        return
    WaitFramesAfterCutscene(frames=1)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3487, 3489)))
    AND_1.Add(FlagDisabled(60500))
    AND_1.Add(FlagDisabled(11109777))
    if not AND_1:
        return
    EnableFlag(11109777)
    EnableFlag(11109785)
    End()
