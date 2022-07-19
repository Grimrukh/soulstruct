"""
Southwest Liurnia (NE) (SE)

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
from .entities.m60_35_42_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1035422150()
    RegisterGrace(grace_flag=1035420000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005870(0, character=Characters.Omenkiller, name=904820600, npc_threat_level=5)
    CommonFunc_90005860(
        0,
        flag=1035420800,
        left=0,
        character=Characters.Omenkiller,
        left_1=0,
        item_lot__item_lot_param_id=30225,
        seconds=0.0,
    )
    CommonFunc_90005300(0, flag=1035420220, character=Characters.Scarab, item_lot_param_id=40208, seconds=0.0, left=0)
    CommonFunc_90005780(
        0,
        flag=1035420800,
        summon_flag=1035422160,
        dismissal_flag=1035422161,
        character=Characters.NepheliLoux,
        sign_type=20,
        region=1035422700,
        right=1034429209,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1035420800, flag_1=1035422160, flag_2=1035422161, character=Characters.NepheliLoux)
    CommonFunc_90005783(
        0,
        flag=1035420800,
        flag_1=1035422160,
        flag_2=1035422161,
        character=Characters.NepheliLoux,
        other_entity=1035422700,
        region=1035422160,
        left=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.AlbinauricLookout0,
        flag=3541,
        flag_1=3540,
        flag_2=1035429201,
        right=3,
    )
    CommonFunc_90005703(0, 1035420700, 3541, 3542, 1035429201, 3541, 3540, 3544, -1)
    CommonFunc_90005702(0, character=Characters.AlbinauricLookout0, flag=3543, first_flag=3540, last_flag=3544)
    Event_1035423700(0, character=Characters.AlbinauricLookout0, asset=Assets.AEG110_334_9000)
    Event_1035420701(0, character=Characters.AlbinauricLookout0, asset=Assets.AEG110_334_9000)
    Event_1035423702(0, character=Characters.AlbinauricLookout0)
    Event_1035423703(0, entity=Characters.AlbinauricLookout0)
    Event_1035420710(0, character=Characters.Ranni)
    CommonFunc_90005704(0, attacked_entity=Characters.Ranni, flag=3741, flag_1=3740, flag_2=1035429251, right=3)
    CommonFunc_90005707(
        0,
        character=Characters.Ranni,
        flag=3741,
        flag_1=3742,
        flag_2=1035429251,
        flag_3=3741,
        first_flag=3740,
        last_flag=3743,
        right=0,
        animation_id=20007,
        left=1035422712,
        flag_4=1035422713,
    )
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, model_point=905, vfx_id=603000)
    CommonFunc_90005709(0, attacked_entity=Characters.Ranni, model_point=960, vfx_id=603050)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4350,
        item_lot_param_id=103930,
        first_flag=400393,
        last_flag=400393,
        flag=1035429255,
        model_point=0,
    )
    Event_1035420711(0, entity=Characters.Ranni)
    Event_1035420712()
    Event_1035422151()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.AlbinauricLookout0)
    DisableBackread(1035420705)
    DisableBackread(Characters.Ranni)
    CommonFunc_90005260(0, 1035420800, 1035422800, 42.0, 0.0, -1)
    CommonFunc_90005250(0, 1035420201, 1035422204, 0.0, -1)
    CommonFunc_90005251(0, 1035420202, 8.0, 0.0, -1)
    CommonFunc_90005251(0, 1035420203, 8.0, 0.0, -1)
    CommonFunc_90005250(0, 1035420204, 1035422204, 0.0, -1)
    CommonFunc_90005201(
        0,
        character=1035420205,
        animation_id=30004,
        animation_id_1=20004,
        radius=8.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 1035420206, 1035422204, 0.0, -1)
    CommonFunc_90005250(0, 1035420207, 1035422204, 0.0, -1)
    CommonFunc_90005251(0, 1035420208, 5.0, 0.0, -1)
    CommonFunc_90005250(0, 1035420209, 1035422204, 0.0, -1)
    CommonFunc_90005250(0, 1035420210, 1035422204, 0.0, -1)
    CommonFunc_90005250(0, 1035420211, 1035422204, 0.0, -1)
    CommonFunc_90005250(0, 1035420212, 1035422204, 0.0, -1)
    CommonFunc_90005250(0, 1035420315, 1035422315, 0.0, -1)
    CommonFunc_90005250(0, 1035420317, 1035422317, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.LargeCrabSnow0,
        animation_id=30003,
        animation_id_1=20003,
        region=1035422370,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1035420374, 30003, 20003, 1035422374, 0.0, 0, 0, 0, 0)


@NeverRestart(1035422150)
def Event_1035422150():
    """Event 1035422150"""
    GotoIfFlagDisabled(Label.L0, flag=1035420150)
    ForceAnimation(1035420150, 30011)
    EnableInvincibility(1035420150)
    SetDisplayMask(1042350150, bit_index=10, switch_type=OnOffChange.Off)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableNetworkConnectedFlagRange(flag_range=(780000, 780009))
    ForceAnimation(1035420150, 30010)
    EnableInvincibility(1035420150)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9630, entity=Assets.AEG099_090_9000))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L10)
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=90100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=91100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=630100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=631100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=890100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=900100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=901100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=902100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=903100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=960100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=961100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=962100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=990100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=991100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1000100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=963100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=964100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=220100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=221100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1990100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1991100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=290100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=291100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=292100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=390100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=430100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1010100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=1011100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=293100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=294100))
    OR_10.Add(PlayerHasArmsArmorEquipped(armor=260200))
    OR_10.Add(PlayerHasArmsArmorEquipped(armor=1070200))
    OR_10.Add(PlayerHasArmsArmorEquipped(armor=1890200))
    SkipLinesIfConditionTrue(3, OR_10)
    EnableNetworkFlag(780000)
    DisableNetworkFlag(780001)
    Goto(Label.L10)
    DisableNetworkFlag(780000)
    EnableNetworkFlag(780001)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=12060000,
            cutscene_flags=0,
            move_to_region=1035422152,
            map_id=60354200,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(12060000, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SetCameraAngle(x_angle=34.79999923706055, y_angle=-136.3699951171875)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        ForceAnimation(PLAYER, 67100)
    DisableNetworkConnectedFlagRange(flag_range=(780000, 780009))
    RemoveGoodFromPlayer(item=8121, quantity=1)
    EnableFlag(1035420150)


@NeverRestart(1035422151)
def Event_1035422151():
    """Event 1035422151"""
    GotoIfFlagDisabled(Label.L0, flag=1035420150)
    DisableAsset(Assets.AEG110_243_2000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(FlagEnabled(1035420150))
    
    MAIN.Await(AND_1)
    
    DisableAsset(Assets.AEG110_243_2000)


@NeverRestart(1035420200)
def Event_1035420200():
    """Event 1035420200"""
    AND_2.Add(OutsideMap(game_map=SOUTHWEST_LIURNIA_NE_SE))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=1035422300))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=1035422300))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetWeather(weather=Weather.HeavyFog, duration=-1.0, immediate_change=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=True)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(1.0)
    Restart()


@RestartOnRest(1035423700)
def Event_1035423700(_, character: uint, asset: uint):
    """Event 1035423700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3540):
        DisableFlag(1035429205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3545)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    OR_3.Add(FlagEnabled(3545))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3540)
    GotoIfFlagEnabled(Label.L2, flag=3541)
    GotoIfFlagEnabled(Label.L3, flag=3542)
    GotoIfFlagEnabled(Label.L4, flag=3543)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L11, flag=1035420701)
    Goto(Label.L12)

    # --- Label 11 --- #
    DefineLabel(11)
    EnableBackread(character)
    DisableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableAsset(asset)
    DisableAnimations(character)
    ForceAnimation(character, 930022)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 12 --- #
    DefineLabel(12)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930020)
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
    OR_4.Add(FlagEnabled(3545))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1035420701)
def Event_1035420701(_, character: uint, asset: uint):
    """Event 1035420701"""
    DisableAsset(Assets.AEG099_090_9020)
    GotoIfFlagEnabled(Label.L1, flag=1035420701)
    EnableAsset(Assets.AEG099_090_9020)
    CreateAssetVFX(Assets.AEG099_090_9020, vfx_id=100, model_point=600904)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1035420701)
    DisableGravity(character)
    DisableAnimations(character)
    EnableCharacterCollision(character)
    ForceAnimation(asset, 1)
    Wait(1.0)
    DeleteAssetVFX(Assets.AEG099_090_9020)
    ForceAnimation(character, 20042)
    EnableCharacter(character)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=302603, anchor_entity=character, model_point=220, anchor_type=CoordEntityType.Character)
    Wait(1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
    WaitFrames(frames=1)
    EnableGravity(character)
    EnableAnimations(character)
    DisableCharacterCollision(character)
    End()


@RestartOnRest(1035423702)
def Event_1035423702(_, character: uint):
    """Event 1035423702"""
    WaitFrames(frames=1)
    if FlagDisabled(3540):
        return
    if FlagDisabled(3545):
        return
    
    MAIN.Await(FlagEnabled(1035429210))
    
    DisableAnimations(character)
    ForceAnimation(character, 20054)
    Wait(5.0)
    DisableNetworkConnectedFlagRange(flag_range=(3540, 3544))
    EnableNetworkFlag(3543)
    SaveRequest()
    Wait(5.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1035423703)
def Event_1035423703(_, entity: uint):
    """Event 1035423703"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3545):
        return
    if FlagDisabled(3540):
        return
    
    MAIN.Await(FlagEnabled(3541))
    
    ForceAnimation(entity, 20052)
    Restart()


@RestartOnRest(1035420710)
def Event_1035420710(_, character: uint):
    """Event 1035420710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3740):
        DisableFlag(1035429252)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L10, flag=3750)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3750))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=3740)
    GotoIfFlagEnabled(Label.L1, flag=3741)
    GotoIfFlagEnabled(Label.L2, flag=3742)
    GotoIfFlagEnabled(Label.L3, flag=3743)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    if FlagDisabled(1035422714):
        ForceAnimation(character, 930002)
    else:
        ForceAnimation(character, 20009)
        SetCharacterFadeOnEnable(character=character, state=False)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    EnableImmortality(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3750))
    
    Restart()


@RestartOnRest(1035420711)
def Event_1035420711(_, entity: uint):
    """Event 1035420711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1034509406):
        return
    
    MAIN.Await(FlagEnabled(1034509406))
    
    ForceAnimation(entity, 20007)
    Wait(6.0)
    EnableFlag(1035429255)


@RestartOnRest(1035420712)
def Event_1035420712():
    """Event 1035420712"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1035420150):
        return
    
    MAIN.Await(FlagEnabled(1035420150))
    
    EnableFlag(3758)
    EnableNetworkFlag(1035422714)


@RestartOnRest(1035420720)
def Event_1035420720(_, character: uint, asset: uint):
    """Event 1035420720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagDisabled(4220):
        DisableFlag(10009703)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(4227))
    OR_1.Add(FlagDisabled(1035422160))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(asset)
    AND_2.Add(FlagEnabled(4227))
    OR_2.Add(FlagDisabled(1035422160))
    AND_2.Add(OR_2)
    AwaitConditionTrue(AND_2)
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
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAsset(asset)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagDisabled(4227))
    OR_15.Add(FlagEnabled(1035422160))
    AwaitConditionTrue(OR_15)
    Restart()


@RestartOnRest(1035420721)
def Event_1035420721():
    """Event 1035420721"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(4221, 4223)))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1034429209)
    End()
