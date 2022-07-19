"""
Stranded Graveyard

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
from .entities.m18_00_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    GotoIfPlayerNotInOwnWorld(Label.L0)
    Event_18000020()
    Event_18000021()
    Event_18000022()
    Event_18002023()

    # --- Label 0 --- #
    DefineLabel(0)
    Event_18000050()
    RegisterGrace(grace_flag=18000000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=18000001, asset=Assets.AEG099_060_9001)
    Event_18002800()
    Event_18002810()
    Event_18000820()
    CommonFunc_90005646(
        0,
        flag=18000800,
        left_flag=18002190,
        cancel_flag__right_flag=18002191,
        asset=18001190,
        player_start=18002190,
        area_id=18,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    Event_18002850()
    Event_18002860()
    Event_18000870()
    Event_18002400()
    Event_18002440(
        0,
        asset_flag=18000600,
        asset=Assets.AEG024_240_9004,
        asset_1=Assets.AEG024_241_9000,
        flag=18002600,
        seconds=2.3299999237060547,
    )
    Event_18002440(
        1,
        asset_flag=18000601,
        asset=Assets.AEG024_240_9005,
        asset_1=Assets.AEG024_241_9001,
        flag=18002601,
        seconds=2.2799999713897705,
    )
    Event_18002440(
        2,
        asset_flag=18000602,
        asset=Assets.AEG024_240_9006,
        asset_1=Assets.AEG024_241_9002,
        flag=18002602,
        seconds=2.2799999713897705,
    )
    Event_18002450(0, asset_flag=18000600, asset=Assets.AEG024_240_9004, flag=18002600)
    Event_18002450(1, asset_flag=18000601, asset=Assets.AEG024_240_9005, flag=18002601)
    Event_18002450(2, asset_flag=18000602, asset=Assets.AEG024_240_9006, flag=18002602)
    Event_18002410()
    Event_18002411(
        0,
        region=18002431,
        patrol_information_id=18003420,
        region_1=18002421,
        patrol_information_id_1=18003421,
        region_2=0,
        patrol_information_id_2=0,
    )
    Event_18002411(
        1,
        region=18002432,
        patrol_information_id=18003421,
        region_1=18002422,
        patrol_information_id_1=18003422,
        region_2=0,
        patrol_information_id_2=0,
    )
    Event_18002411(
        2,
        region=18002433,
        patrol_information_id=18003422,
        region_1=18002423,
        patrol_information_id_1=18003423,
        region_2=0,
        patrol_information_id_2=0,
    )
    Event_18002411(
        3,
        region=18002434,
        patrol_information_id=18003423,
        region_1=18002424,
        patrol_information_id_1=18003424,
        region_2=0,
        patrol_information_id_2=0,
    )
    Event_18002411(
        4,
        region=18002435,
        patrol_information_id=18003424,
        region_1=18002425,
        patrol_information_id_1=18003425,
        region_2=18002426,
        patrol_information_id_2=18003426,
    )
    CommonFunc_90005680(
        0,
        flag=18000530,
        flag_1=18000531,
        flag_2=18000532,
        flag_3=18000533,
        asset=Assets.AEG027_156_9000,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005501(
        0,
        flag=18000510,
        flag_1=18001510,
        left=0,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0504,
        asset_2=Assets.AEG027_002_0501,
        flag_2=18000511,
    )
    CommonFunc_90005501(
        0,
        flag=18000515,
        flag_1=18001515,
        left=1,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0503,
        asset_2=Assets.AEG027_002_0502,
        flag_2=18000516,
    )
    Event_18002510()
    CommonFunc_90005511(
        0,
        flag=18000542,
        asset=Assets.AEG027_039_0500,
        obj_act_id=18003542,
        obj_act_id_1=227010,
        left=0,
    )
    CommonFunc_90005512(0, flag=18000542, region=18002542, region_1=18002543)
    Event_18002580()
    CommonFunc_90005646(
        0,
        flag=18000800,
        left_flag=18002840,
        cancel_flag__right_flag=18002841,
        asset=Assets.AEG099_065_9000,
        player_start=18002840,
        area_id=18,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_90005620(
        0,
        flag=18000570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=18002570,
        cancel_flag__right_flag=18002571,
        right=18002572,
    )
    Event_18002569(0, flag=18000570, asset=Assets.AEG099_271_9000)
    CommonFunc_90005570(0, flag=60809, gesture_param_id=9, asset=Assets.AEG099_610_9009, left=0, left_1=1, right=0)
    Event_18002270(0, entity=18000270)
    Event_18002650(0, region=18002650, tutorial_param_id=1010, flag=710010)
    Event_18002640(0, region=18002651, tutorial_param_id=1020, flag=710020, item=9100, flag_1=69000)
    Event_18002640(1, region=18002656, tutorial_param_id=1070, flag=710070, item=9112, flag_1=69120)
    Event_18002640(2, region=18002663, tutorial_param_id=1140, flag=710140, item=9103, flag_1=69030)
    CommonFunc_90005261(
        0,
        character=Characters.WanderingNoble3,
        region=18002202,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_18002640(3, region=18002665, tutorial_param_id=1160, flag=710160, item=9104, flag_1=69040)
    Event_18002640(4, region=18002667, tutorial_param_id=1190, flag=710190, item=9105, flag_1=69050)
    Event_18002640(5, region=18002670, tutorial_param_id=1200, flag=710200, item=9129, flag_1=69290)
    Event_18002640(6, region=18002668, tutorial_param_id=1210, flag=710210, item=9138, flag_1=69380)
    Event_18002640(7, region=18002659, tutorial_param_id=1100, flag=710100, item=9140, flag_1=69400)
    Event_18002651(0, region=18002652, tutorial_param_id=1030, flag=710030)
    Event_18002651(1, region=18002653, tutorial_param_id=1040, flag=710040)
    Event_18002651(2, region=18002657, tutorial_param_id=1080, flag=710080)
    Event_18002651(3, region=18002658, tutorial_param_id=1090, flag=710090)
    Event_18002651(5, region=18002660, tutorial_param_id=1110, flag=710110)
    Event_18002651(7, region=18002664, tutorial_param_id=1150, flag=710150)
    Event_18002651(8, region=18002666, tutorial_param_id=1170, flag=710170)
    Event_18002654(0, region=18002654, tutorial_param_id=1050, flag=710050)
    Event_18002655(0, region=18002655, tutorial_param_id=1060, flag=18000655, flag_1=710060)
    Event_18002662(0, region=18002662, tutorial_param_id=1130, flag=18000662, flag_1=710130)
    Event_18002663(0, tutorial_param_id=1180, flag=710180, item=9106, flag_1=69060, entity=Characters.GodrickSoldier1)
    Event_18002665(0, flag=710660, tutorial_param_id=1660, item=9122, flag_1=69220)
    Event_18002200(
        0,
        character=Characters.GodrickSoldier0,
        region=18002201,
        patrol_information_id=18003200,
        flag=18002200,
    )
    Event_18002211(0, other_entity=Characters.WanderingNoble0, flag=18002211)
    Event_18002211(1, other_entity=Characters.WanderingNoble4, flag=18000220)
    Event_18002671(0, flag=710010)
    Event_18002671(1, flag=710020)
    Event_18002671(2, flag=710030)
    Event_18002671(3, flag=710040)
    Event_18002671(4, flag=710050)
    Event_18002671(5, flag=18000655)
    Event_18002671(6, flag=18000662)
    Event_18002671(7, flag=710070)
    Event_18002671(8, flag=710080)
    Event_18002671(9, flag=710090)
    Event_18002671(10, flag=710100)
    Event_18002671(11, flag=710110)
    Event_18002671(12, flag=710120)
    Event_18002671(13, flag=710140)
    Event_18002671(14, flag=710150)
    Event_18002671(15, flag=710160)
    Event_18002671(16, flag=710170)
    Event_18002671(17, flag=710000)
    Event_18002671(18, flag=710110)
    Event_18002671(19, flag=710110)
    Event_18002671(20, flag=710210)
    Event_18002671(21, flag=710200)
    Event_18002671(22, flag=710190)
    Event_18002250(0, character=Characters.GodrickSoldier1, special_effect_id=8041)
    Event_18002250(1, character=Characters.WanderingNoble2, special_effect_id=8040)
    Event_18002690()
    CommonFunc_90005706(0, 18000701, 30025, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Commoner)
    CommonFunc_90005251(0, character=Characters.WanderingNoble1, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=18000300, region=18002300, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.CastleGuard, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.BanishedKnight, radius=8.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Imp0, radius=4.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005251(0, character=Characters.Imp1, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Imp2, radius=5.0, seconds=2.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.GraftedScion0,
        animation_id=30002,
        animation_id_1=20002,
        region=18002350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.GraftedScion1,
        animation_id=30002,
        animation_id_1=20002,
        region=18002350,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(
        0,
        flag=18000350,
        character=Characters.GraftedScion0,
        item_lot_param_id=18002000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=18000351,
        character=Characters.GraftedScion1,
        item_lot_param_id=18002010,
        seconds=0.0,
        left=0,
    )
    Event_18002520()


@RestartOnRest(18000020)
def Event_18000020():
    """Event 18000020"""
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(ThisEventSlotFlagEnabled())
    AND_15.Add(FlagDisabled(60000))
    GotoIfConditionTrue(Label.L0, input_condition=AND_15)
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(10010020))
    AND_1.Add(InsideMap(game_map=STRANDED_GRAVEYARD))
    
    MAIN.Await(AND_1)
    
    EnableFlag(101)
    SetRespawnPoint(respawn_point=18002020)
    SaveRequest()
    DisableImmortality(PLAYER)
    EqualRecovery()
    Unknown_2004_61(unk_0_4=9999)
    AddSpecialEffect(PLAYER, 4291)
    AddSpecialEffect(PLAYER, 4790)
    if FlagDisabled(2000):
        return
    EnableFlag(9021)
    PlayCutscene(60430000, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SetCameraAngle(x_angle=6.980000019073486, y_angle=106.95999908447266)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_10.Add(PlayerHasGood(201))
    OR_10.Add(PlayerHasGood(203))
    OR_10.Add(PlayerHasGood(205))
    OR_10.Add(PlayerHasGood(207))
    OR_10.Add(PlayerHasGood(209))
    OR_10.Add(PlayerHasGood(211))
    OR_10.Add(PlayerHasGood(213))
    OR_10.Add(PlayerHasGood(215))
    OR_10.Add(PlayerHasGood(217))
    OR_10.Add(PlayerHasGood(219))
    OR_11.Add(PlayerHasGood(221))
    OR_11.Add(PlayerHasGood(223))
    OR_11.Add(PlayerHasGood(225))
    OR_11.Add(PlayerHasGood(227))
    OR_11.Add(PlayerHasGood(229))
    OR_11.Add(PlayerHasGood(221))
    OR_11.Add(PlayerHasGood(223))
    OR_11.Add(PlayerHasGood(225))
    OR_11.Add(PlayerHasGood(227))
    OR_11.Add(PlayerHasGood(229))
    AND_10.Add(OR_10)
    AND_11.Add(OR_11)
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    AwardItemLot(2000, host_only=True)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableFlag(60000)


@RestartOnRest(18000021)
def Event_18000021():
    """Event 18000021"""
    DisableNetworkSync()
    if FlagEnabled(102):
        return
    if FlagEnabled(2002):
        return
    SetCurrentTime(
        time=(10, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )
    FreezeTime()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1042368540))
    
    MAIN.Await(AND_1)
    
    UnfreezeTime()
    EnableFlag(71801)
    DisableThisSlotFlag()
    EnableFlag(102)
    SetWeather(weather=Weather.Default, duration=3600.0, immediate_change=False)


@RestartOnRest(18000022)
def Event_18000022():
    """Event 18000022"""
    if FlagEnabled(18000021):
        return
    if FlagEnabled(102):
        return
    if FlagEnabled(2002):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=18002022))
    
    SetCurrentTime(
        time=(10, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(18002023)
def Event_18002023():
    """Event 18002023"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(710820):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=18002680))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710820)


@RestartOnRest(18000050)
def Event_18000050():
    """Event 18000050"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(2030):
        return
    DisableAssetActivation(Assets.AEG027_039_0500, obj_act_id=-1)
    OR_1.Add(FlagEnabled(2030))
    OR_2.Add(ActionButtonParamActivated(action_button_id=7200, entity=Assets.AEG027_039_0500))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionFalse(Label.L0, input_condition=OR_2)
    DisplayFullScreenMessage(text=2000)
    Wait(1.0)
    if FlagDisabled(2030):
        return RESTART

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetActivation(Assets.AEG027_039_0500, obj_act_id=-1)


@RestartOnRest(18002200)
def Event_18002200(_, character: uint, region: uint, patrol_information_id: uint, flag: uint):
    """Event 18002200"""
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EnableFlag(flag)


@RestartOnRest(18002211)
def Event_18002211(_, other_entity: uint, flag: uint):
    """Event 18002211"""
    if FlagEnabled(flag):
        return
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(other_entity, 3001, wait_for_completion=True)
    EnableFlag(flag)


@RestartOnRest(18002250)
def Event_18002250(_, character: uint, special_effect_id: int):
    """Event 18002250"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(18002270)
def Event_18002270(_, entity: uint):
    """Event 18002270"""
    ForceAnimation(entity, 930025)
    End()


@RestartOnRest(18002400)
def Event_18002400():
    """Event 18002400"""
    if FlagEnabled(18000400):
        DisableCharacter(Characters.MercilessChariot)
        DisableAnimations(Characters.MercilessChariot)
        DisableAI(Characters.MercilessChariot)
        End()
    
    MAIN.Await(InsideMap(game_map=STRANDED_GRAVEYARD))
    
    DisableInvincibility(Characters.MercilessChariot)
    EnableImmortality(Characters.MercilessChariot)
    SetLockOnPoint(character=Characters.MercilessChariot, lock_on_model_point=220, state=False)
    DisableHealthBar(Characters.MercilessChariot)
    AddSpecialEffect(Characters.MercilessChariot, 5000)
    SetNetworkUpdateRate(Characters.MercilessChariot, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(Characters.MercilessChariot, True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(Characters.MercilessChariot, authority_level=UpdateAuthority.Forced)


@RestartOnRest(18002410)
def Event_18002410():
    """Event 18002410"""
    if FlagEnabled(18000400):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(18002411, 18002411)) >= 0)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=18002400))
    
    MAIN.Await(AND_1)
    
    ChangePatrolBehavior(Characters.MercilessChariot, patrol_information_id=18003420)
    WaitFrames(frames=1)


@RestartOnRest(18002411)
def Event_18002411(
    _,
    region: uint,
    patrol_information_id: uint,
    region_1: uint,
    patrol_information_id_1: uint,
    region_2: uint,
    patrol_information_id_2: uint,
):
    """Event 18002411"""
    if FlagEnabled(18000400):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.MercilessChariot, region=region))
    
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region_1)
    if UnsignedNotEqual(left=0, right=region_2):
        GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_2)
    ChangePatrolBehavior(Characters.MercilessChariot, patrol_information_id=patrol_information_id)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangePatrolBehavior(Characters.MercilessChariot, patrol_information_id=patrol_information_id_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(Characters.MercilessChariot, patrol_information_id=patrol_information_id_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(CharacterOutsideRegion(character=Characters.MercilessChariot, region=region))
    
    Restart()


@RestartOnRest(18002440)
def Event_18002440(_, asset_flag: uint, asset: uint, asset_1: uint, flag: uint, seconds: float):
    """Event 18002440"""
    if FlagEnabled(flag):
        DisableAsset(asset)
        RemoveAssetFlag(asset_flag=asset_flag)
        DisableAsset(asset_1)
        End()
    EnableAsset(asset)
    
    MAIN.Await(AssetDestroyed(asset_1))
    
    DestroyAsset(asset, request_slot=0)
    RemoveAssetFlag(asset_flag=asset_flag)
    CreateHazard(
        asset_flag=asset_flag,
        asset=asset,
        model_point=200,
        behavior_param_id=200500,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=0.10000000149011612,
    )
    EnableFlag(flag)
    Wait(seconds)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=Characters.MercilessChariot, special_effect=19300)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301800,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301830,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301840,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301850,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301860,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301870,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    DisableAsset(asset)
    RemoveAssetFlag(asset_flag=asset_flag)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(18002450)
def Event_18002450(_, asset_flag: uint, asset: uint, flag: uint):
    """Event 18002450"""
    if FlagEnabled(18000400):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.MercilessChariot, 19300))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301800,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301810,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301820,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301830,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301840,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301850,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301860,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.TalkDummy4,
            source_entity=asset,
            model_point=200,
            behavior_id=803301870,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    DisableAsset(asset)
    RemoveAssetFlag(asset_flag=asset_flag)
    DisableImmortality(Characters.MercilessChariot)
    Kill(Characters.MercilessChariot, award_runes=True)
    RemoveSpecialEffect(Characters.MercilessChariot, 19300)
    Wait(3.0)
    if FlagEnabled(18000400):
        return
    if PlayerInOwnWorld():
        AwardItemLot(18000900, host_only=True)
    EnableFlag(18000400)


@NeverRestart(18002510)
def Event_18002510():
    """Event 18002510"""
    CommonFunc_90005500(
        0,
        flag=18000510,
        flag_1=18001510,
        left=0,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0504,
        obj_act_id=18003511,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=18003512,
        region=18002511,
        region_1=18002512,
        flag_2=18000511,
        flag_3=18002512,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=18000515,
        flag_1=18001515,
        left=1,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0503,
        obj_act_id=18003516,
        asset_2=Assets.AEG027_002_0502,
        obj_act_id_1=18003517,
        region=18002516,
        region_1=18002517,
        flag_2=18000516,
        flag_3=18002517,
        left_1=0,
    )
    CommonFunc_90005681(
        0,
        flag=18000530,
        flag_1=18000531,
        flag_2=18000532,
        flag_3=18000533,
        attacked_entity=Assets.AEG027_156_9000,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100770,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100760,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100750,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100740,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100730,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100720,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=18000532,
            source_entity=Assets.AEG027_156_9000,
            region=18002530,
            owner_entity=Characters.TalkDummy3,
            behavior_id=801100710,
            behavior_id_1=801100705,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(0, 18000532, 18001530, 18002530, 18000530, 801100700, 801100705, 102, 0, 0, 0)


@NeverRestart(18002520)
def Event_18002520():
    """Event 18002520"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(18000530)


@NeverRestart(18002569)
def Event_18002569(_, flag: uint, asset: uint):
    """Event 18002569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=101, model_point=806043)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@RestartOnRest(18002580)
def Event_18002580():
    """Event 18002580"""
    RegisterLadder(start_climbing_flag=18000580, stop_climbing_flag=18000581, asset=Assets.AEG027_009_0500)


@RestartOnRest(18002640)
def Event_18002640(_, region: uint, tutorial_param_id: int, flag: uint, item: int, flag_1: uint):
    """Event 18002640"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002650)
def Event_18002650(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(HealthRatio(PLAYER) < 100.0)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002651)
def Event_18002651(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002651"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002654)
def Event_18002654(_, region: uint, tutorial_param_id: int, flag: uint):
    """Event 18002654"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerDoesNotHaveWeapon(33000000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33040000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33050000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33060000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33090000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33120000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33130000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33170000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33180000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33190000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33200000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33210000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33230000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33240000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33250000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33260000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33270000))
    AND_1.Add(PlayerDoesNotHaveWeapon(33280000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34000000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34010000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34020000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34030000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34040000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34060000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34070000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34080000))
    AND_1.Add(PlayerDoesNotHaveWeapon(34090000))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)


@RestartOnRest(18002655)
def Event_18002655(_, region: uint, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 18002655"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(PlayerHasWeapon(33000000))
    OR_1.Add(PlayerHasWeapon(33040000))
    OR_1.Add(PlayerHasWeapon(33050000))
    OR_1.Add(PlayerHasWeapon(33060000))
    OR_1.Add(PlayerHasWeapon(33090000))
    OR_1.Add(PlayerHasWeapon(33120000))
    OR_1.Add(PlayerHasWeapon(33130000))
    OR_1.Add(PlayerHasWeapon(33170000))
    OR_1.Add(PlayerHasWeapon(33180000))
    OR_1.Add(PlayerHasWeapon(33190000))
    OR_1.Add(PlayerHasWeapon(33200000))
    OR_1.Add(PlayerHasWeapon(33210000))
    OR_1.Add(PlayerHasWeapon(33230000))
    OR_1.Add(PlayerHasWeapon(33240000))
    OR_1.Add(PlayerHasWeapon(33250000))
    OR_1.Add(PlayerHasWeapon(33260000))
    OR_1.Add(PlayerHasWeapon(33270000))
    OR_1.Add(PlayerHasWeapon(33280000))
    OR_1.Add(PlayerHasWeapon(34000000))
    OR_1.Add(PlayerHasWeapon(34010000))
    OR_1.Add(PlayerHasWeapon(34020000))
    OR_1.Add(PlayerHasWeapon(34030000))
    OR_1.Add(PlayerHasWeapon(34040000))
    OR_1.Add(PlayerHasWeapon(34060000))
    OR_1.Add(PlayerHasWeapon(34070000))
    OR_1.Add(PlayerHasWeapon(34080000))
    OR_1.Add(PlayerHasWeapon(34090000))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag_1)


@RestartOnRest(18002662)
def Event_18002662(_, region: uint, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 18002662"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(PlayerHasWeapon(40000000))
    OR_1.Add(PlayerHasWeapon(40010000))
    OR_1.Add(PlayerHasWeapon(40020000))
    OR_1.Add(PlayerHasWeapon(40030000))
    OR_1.Add(PlayerHasWeapon(40050000))
    OR_1.Add(PlayerHasWeapon(41000000))
    OR_1.Add(PlayerHasWeapon(41010000))
    OR_1.Add(PlayerHasWeapon(41020000))
    OR_1.Add(PlayerHasWeapon(41030000))
    OR_1.Add(PlayerHasWeapon(41040000))
    OR_1.Add(PlayerHasWeapon(41060000))
    OR_1.Add(PlayerHasWeapon(41070000))
    OR_1.Add(PlayerHasWeapon(42000000))
    OR_1.Add(PlayerHasWeapon(42000000))
    OR_1.Add(PlayerHasWeapon(42030000))
    OR_1.Add(PlayerHasWeapon(42040000))
    OR_1.Add(PlayerHasWeapon(43000000))
    OR_1.Add(PlayerHasWeapon(43020000))
    OR_1.Add(PlayerHasWeapon(43030000))
    OR_1.Add(PlayerHasWeapon(43050000))
    OR_1.Add(PlayerHasWeapon(43060000))
    OR_1.Add(PlayerHasWeapon(43080000))
    OR_1.Add(PlayerHasWeapon(43100000))
    OR_1.Add(PlayerHasWeapon(43110000))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    EnableFlag(flag_1)


@RestartOnRest(18002663)
def Event_18002663(_, tutorial_param_id: int, flag: uint, item: int, flag_1: uint, entity: uint):
    """Event 18002663"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=10.0))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if Multiplayer():
        return
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002665)
def Event_18002665(_, flag: uint, tutorial_param_id: int, item: int, flag_1: uint):
    """Event 18002665"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_1):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=item, flag=flag, bit_count=1)
    EnableFlag(flag_1)


@RestartOnRest(18002671)
def Event_18002671(_, flag: uint):
    """Event 18002671"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=18002671))
    OR_1.Add(OutsideMap(game_map=STRANDED_GRAVEYARD))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)


@RestartOnRest(18002690)
def Event_18002690():
    """Event 18002690"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(18007090):
        return
    
    MAIN.Await(FlagEnabled(18007090))
    
    AwardGesture(gesture_param_id=9)


@RestartOnRest(18002800)
def Event_18002800():
    """Event 18002800"""
    if FlagEnabled(18000800):
        return
    
    MAIN.Await(HealthValue(Characters.UlceratedTreeSpirit) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.UlceratedTreeSpirit, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.UlceratedTreeSpirit))
    
    KillBossAndDisplayBanner(character=Characters.UlceratedTreeSpirit, banner_type=BannerType.EnemyFelled)
    EnableFlag(18000800)
    EnableFlag(9128)
    if PlayerInOwnWorld():
        EnableFlag(61128)


@RestartOnRest(18002810)
def Event_18002810():
    """Event 18002810"""
    GotoIfFlagDisabled(Label.L0, flag=18000800)
    DisableCharacter(Characters.UlceratedTreeSpirit)
    DisableAnimations(Characters.UlceratedTreeSpirit)
    Kill(Characters.UlceratedTreeSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.UlceratedTreeSpirit)
    AND_2.Add(FlagEnabled(18002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=18002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.UlceratedTreeSpirit)
    SetNetworkUpdateRate(Characters.UlceratedTreeSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.UlceratedTreeSpirit, name=904640000)


@RestartOnRest(18000820)
def Event_18000820():
    """Event 18000820"""
    CommonFunc_9005800(
        0,
        flag=18000800,
        entity=Assets.AEG099_001_9000,
        region=18002800,
        flag_1=18002805,
        character=18005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=18000800,
        entity=Assets.AEG099_001_9000,
        region=18002800,
        flag_1=18002805,
        flag_2=18002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=18000800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 18000800, 920600, 18002805, 18002806, 0, 18002802, 0, 0)


@RestartOnRest(18002850)
def Event_18002850():
    """Event 18002850"""
    if FlagEnabled(18000850):
        return
    
    MAIN.Await(HealthValue(Characters.GodrickSoldier1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.GodrickSoldier1, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GodrickSoldier1))
    
    KillBossAndDisplayBanner(character=Characters.GodrickSoldier1, banner_type=BannerType.EnemyFelled)
    EnableFlag(18000850)


@RestartOnRest(18002860)
def Event_18002860():
    """Event 18002860"""
    GotoIfFlagDisabled(Label.L0, flag=18000850)
    DisableCharacter(Characters.GodrickSoldier1)
    DisableAnimations(Characters.GodrickSoldier1)
    Kill(Characters.GodrickSoldier1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GodrickSoldier1)
    AND_2.Add(FlagEnabled(18002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=18002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.GodrickSoldier1)
    SetNetworkUpdateRate(Characters.GodrickSoldier1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.GodrickSoldier1, name=904311000)


@RestartOnRest(18000870)
def Event_18000870():
    """Event 18000870"""
    CommonFunc_9005800(
        0,
        flag=18000850,
        entity=Assets.AEG099_001_9010,
        region=18002850,
        flag_1=18002855,
        character=18005850,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=18000850,
        entity=Assets.AEG099_001_9010,
        region=18002850,
        flag_1=18002855,
        flag_2=18002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=18000850, asset=Assets.AEG099_001_9010, model_point=3, right=0)
    CommonFunc_9005811(0, flag=18000850, asset=Assets.AEG099_001_9011, model_point=4, right=0)
    CommonFunc_9005822(0, 18000850, 931000, 18002855, 18002856, 0, 18002852, 0, 0)
