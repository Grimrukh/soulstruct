"""
South Caelid (SE) (SE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_51_36_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1051362580()
    CommonFunc_9005810(
        0,
        flag=1051360800,
        grace_flag=1051360000,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9002,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005100(
        0,
        flag=76458,
        flag_1=76419,
        asset=Assets.AEG099_090_9001,
        source_flag=77410,
        value=4,
        flag_2=78410,
        flag_3=78411,
        flag_4=78412,
        flag_5=78413,
        flag_6=78414,
        flag_7=78415,
        flag_8=78416,
        flag_9=78417,
        flag_10=78418,
        flag_11=78419,
    )
    RegisterGrace(grace_flag=1051360001, asset=Assets.AEG099_060_9000, enemy_block_distance=10.0)
    CommonFunc_90005100(
        0,
        flag=76458,
        flag_1=76420,
        asset=Assets.AEG099_090_9000,
        source_flag=77410,
        value=3,
        flag_2=78410,
        flag_3=78411,
        flag_4=78412,
        flag_5=78413,
        flag_6=78414,
        flag_7=78415,
        flag_8=78416,
        flag_9=78417,
        flag_10=78418,
        flag_11=78419,
    )
    if FlagEnabled(57):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362501,
            asset=Assets.AEG007_505_2001,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(57):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004070,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004060,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004050,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004040,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004030,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004020,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004010,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005695(
            0,
            asset__asset_flag=1051362503,
            asset=Assets.AEG007_505_2003,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802004000,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    Event_1051362216(
        0,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004000,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=50,
    )
    Event_1051362216(
        1,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004010,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=51,
    )
    Event_1051362216(
        2,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004020,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=52,
    )
    Event_1051362216(
        3,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004030,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=53,
    )
    Event_1051362216(
        4,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004040,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=54,
    )
    Event_1051362216(
        5,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004050,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=55,
    )
    Event_1051362216(
        6,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004060,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=56,
    )
    Event_1051362216(
        7,
        asset__asset_flag=1051362500,
        asset=Assets.AEG007_505_2000,
        dummy_id_start=200,
        dummy_id_end=0,
        behavior_param_id__behaviour_id=802004070,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
        flag=57,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9004, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9005, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9006, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9007, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9008, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=50,
        cc_id=36,
        dd_id=0,
        player_start=1050360600,
        unk_8_12=0,
        flag=1051362650,
        left_flag=1051362651,
        cancel_flag__right_flag=1051362652,
        left=9410,
        text=30040,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1051362800()
    Event_1051362810()
    Event_1051362849()
    Event_1051362630(0, asset=Assets.AEG003_129_2006)
    Event_1051362630(1, asset=Assets.AEG003_130_2002)
    Event_1051362630(2, asset=Assets.AEG007_463_2009)
    Event_1051362630(3, asset=Assets.AEG007_464_2009)
    Event_1051362210()
    Event_1051362215()
    Event_1051362200()
    Event_1051362220()
    Event_1051362230()
    CommonFunc_90005261(
        0,
        character=Characters.IronVirgin,
        region=1051362200,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005251(0, character=Characters.Commoner0, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commoner1, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005300(
        0,
        flag=1051360291,
        character=Characters.LionGuardian0,
        item_lot=1051360700,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005300(
        0,
        flag=1051360292,
        character=Characters.LionGuardian1,
        item_lot=1051360800,
        seconds=0.0,
        left=0,
    )
    Event_1051362340(0, character=Characters.Troll)
    CommonFunc_90005250(0, character=Characters.RadahnSoldier, region=1051362422, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnFootSoldier0, region=1051362422, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnFootSoldier1, region=1051362422, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RadahnFootSoldier2, region=1051362422, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.MadPumpkinHead, region=1051362490, seconds=0.0, animation_id=-1)
    CommonFunc_90005501(
        0,
        flag=1051360510,
        flag_1=1051360511,
        left=0,
        asset=Assets.AEG030_858_2000,
        asset_1=Assets.AEG099_026_2000,
        asset_2=Assets.AEG099_026_2001,
        flag_2=1051360512,
    )
    Event_1051362510()
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy0,
        character_1=Characters.RadahnFootSoldier3,
        asset=Assets.AEG110_181_2000,
        asset_1=0,
        obj_act_id=0,
        region=1051362400,
        left=1,
    )
    CommonFunc_90005490(
        0,
        character=Characters.BulletDummy1,
        character_1=Characters.RadahnFootSoldier4,
        asset=Assets.AEG110_181_2001,
        asset_1=0,
        obj_act_id=0,
        region=1051362402,
        left=1,
    )
    CommonFunc_90005511(
        0,
        flag=1051360560,
        asset=Assets.AEG030_933_2005,
        obj_act_id=1051363560,
        obj_act_id_1=99020,
        left=0,
    )
    CommonFunc_90005512(0, flag=1051360560, region=1051362560, region_1=1051362561)
    RunCommonEvent(1051362560, slot=0, args=(1051361562,))
    RunCommonEvent(1051362560, slot=1, args=(1051361564,))
    RunCommonEvent(1051362560, slot=2, args=(1051361566,))
    RunCommonEvent(1051362560, slot=3, args=(1051361568,))
    Event_1051363710(0, character=Characters.LivingPot)
    Event_1051363711()
    Event_1051360720(0, character=Characters.Blaidd)
    Event_1051360721()
    Event_1051363725(0, asset__character=Characters.WitchHunterJerren0)
    Event_1051363726(0, asset__character=Characters.WitchHunterJerren1)
    Event_1051363727()
    CommonFunc_90005708(0, character=Characters.WitchHunterJerren0, flag=3360, left=1051362700)
    Event_1051360730(0, character=Characters.Human, animation_id=0, left=1)
    Event_1051360730(1, character=Characters.Okina, animation_id=90100, left=1)
    Event_1051360730(2, character=Characters.FingerMaidenTherolina, animation_id=90101, left=0)
    Event_1051360734(0, character=Characters.FingerMaidenTherolina)
    Event_1051360735(0, character=Characters.GreatHornedTragoth, animation_id=0, left=1)
    Event_1051362500()
    Event_1051362490(0, region=1051362710)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WitchHunterJerren0)
    DisableBackread(Characters.WitchHunterJerren1)
    DisableBackread(1051360702)
    DisableBackread(Characters.LivingPot)
    DisableBackread(Characters.Human)
    DisableBackread(Characters.Blaidd)
    DisableBackread(Characters.GreatHornedTragoth)
    DisableBackread(Characters.Okina)
    DisableBackread(Characters.FingerMaidenTherolina)
    EnableAssetInvulnerability(Assets.AEG030_930_2000)
    Event_1051362519()


@RestartOnRest(1051362200)
def Event_1051362200():
    """Event 1051362200"""
    if FlagEnabled(9413):
        EnableCharacter(1051365200)
        EnableAsset(Assets.AEG110_181_2000)
        EnableAsset(Assets.AEG110_181_2001)
        End()
    if FlagDisabled(9410):
        return
    
    MAIN.Await(FlagEnabled(9410))
    
    DisableCharacter(1051365200)
    DisableAsset(Assets.AEG110_181_2000)
    DisableAsset(Assets.AEG110_181_2001)


@RestartOnRest(1051362210)
def Event_1051362210():
    """Event 1051362210"""
    OR_1.Add(FlagDisabled(9410))
    OR_1.Add(FlagEnabled(9413))
    if OR_1:
        return
    DisableAsset(Assets.AEG099_001_9000)
    DisableAsset(Assets.AEG099_001_9001)


@RestartOnRest(1051362215)
def Event_1051362215():
    """Event 1051362215"""
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9413))
    if AND_1:
        return
    DisableAsset(Assets.AEG007_505_2000)


@RestartOnRest(1051362216)
def Event_1051362216(
    _,
    asset__asset_flag: uint,
    asset: Asset | int,
    dummy_id_start: int,
    dummy_id_end: int,
    behavior_param_id__behaviour_id: int,
    radius: float,
    life: float,
    repetition_time: float,
    flag: Flag | int,
):
    """Event 1051362216"""
    if FlagDisabled(flag):
        return
    RemoveAssetFlag(asset_flag=asset__asset_flag)
    OR_1.Add(FlagDisabled(9410))
    OR_1.Add(FlagEnabled(9413))
    if OR_1:
        return
    if AssetDestroyed(asset):
        return
    if ValueEqual(left=0, right=dummy_id_end):
        CreateHazard(
            asset_flag=asset__asset_flag,
            asset=asset,
            dummy_id=dummy_id_start,
            behavior_param_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )
    else:
        CreateBigHazardousAsset(
            asset_flag=asset__asset_flag,
            asset=asset,
            dummy_id_start=dummy_id_start,
            dummy_id_end=dummy_id_end,
            behaviour_id=behavior_param_id__behaviour_id,
            target_type=DamageTargetType.Character,
            radius=radius,
            life=life,
            repetition_time=repetition_time,
        )
    
    MAIN.Await(AssetDestroyed(asset__asset_flag))
    
    RemoveAssetFlag(asset_flag=asset__asset_flag)


@RestartOnRest(1051362220)
def Event_1051362220():
    """Event 1051362220"""
    DisableAsset(Assets.AEG099_001_9002)
    DeleteAssetVFX(Assets.AEG099_001_9002)
    EndOfAnimation(asset=Assets.AEG030_419_2000, animation_id=0)
    AND_9.Add(FlagEnabled(1051360230))
    GotoIfConditionTrue(Label.L2, input_condition=AND_9)
    OR_9.Add(FlagEnabled(9412))
    OR_9.Add(FlagEnabled(9413))
    OR_9.Add(FlagEnabled(1252380800))
    if OR_9:
        return
    GotoIfFlagEnabled(Label.L1, flag=9411)
    
    MAIN.Await(FlagEnabled(9411))
    
    EnableFlag(9021)
    PlayCutscene(60510000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitRealFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(asset=Assets.AEG030_419_2000, animation_id=2)
    EnableAsset(Assets.AEG099_001_9002)
    CreateAssetVFX(Assets.AEG099_001_9002, dummy_id=101, vfx_id=5)
    SetCurrentTime(
        time=(3, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EndOfAnimation(asset=Assets.AEG030_419_2000, animation_id=2)
    End()


@RestartOnRest(1051362230)
def Event_1051362230():
    """Event 1051362230"""
    if FlagEnabled(1051360230):
        return
    AND_1.Add(FlagEnabled(9412))
    AND_1.Add(FlagEnabled(1051360800))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1051362230))
    
    MAIN.Await(AND_1)
    
    EndOfAnimation(asset=Assets.AEG030_419_2000, animation_id=2)
    EnableFlag(1051360230)
    End()


@RestartOnRest(1051362340)
def Event_1051362340(_, character: Character | int):
    """Event 1051362340"""
    if FlagEnabled(1051362340):
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1051362340))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Troll))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableFlag(1051362340)
    EnableAI(character)
    ForceAnimation(Characters.Troll, 20016, wait_for_completion=True)
    SetNest(Characters.Troll, region=1051362341)


@RestartOnRest(1051362490)
def Event_1051362490(_, region: Region | int):
    """Event 1051362490"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(ALL_PLAYERS, 9621)
    Wait(0.10000000149011612)
    AND_3.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region))
    
    MAIN.Await(AND_3)
    
    Wait(0.10000000149011612)
    AND_4.Add(FlagEnabled(9410))
    AND_4.Add(FlagDisabled(9413))
    AND_4.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=1051362500))
    SkipLinesIfConditionTrue(1, AND_4)
    RemoveSpecialEffect(ALL_PLAYERS, 9621)
    Restart()


@RestartOnRest(1051362500)
def Event_1051362500():
    """Event 1051362500"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=9413)
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=1051362500))
    AND_1.Add(FlagEnabled(9410))
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=9413)
    AddSpecialEffect(ALL_PLAYERS, 9621)
    Wait(0.10000000149011612)
    OR_2.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=1051362500))
    OR_2.Add(Invasion())
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    if CharacterOutsideRegion(character=ALL_PLAYERS, region=1051362710):
        RemoveSpecialEffect(ALL_PLAYERS, 9621)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(ALL_PLAYERS, 9621)
    End()


@ContinueOnRest(1051362510)
def Event_1051362510():
    """Event 1051362510"""
    CommonFunc_90005500(
        0,
        flag=1051360510,
        flag_1=1051360511,
        left=0,
        asset=Assets.AEG030_858_2000,
        asset_1=Assets.AEG099_026_2000,
        obj_act_id=1051363511,
        asset_2=Assets.AEG099_026_2001,
        obj_act_id_1=1051363512,
        region=1051362511,
        region_1=1051362512,
        flag_2=1051360512,
        flag_3=1051360513,
        left_1=0,
    )


@ContinueOnRest(1051362519)
def Event_1051362519():
    """Event 1051362519"""
    if FlagEnabled(1051360514):
        return
    EnableFlag(1051360514)
    DisableFlag(1051360519)
    EnableFlag(1051360510)


@ContinueOnRest(1051362560)
def Event_1051362560(_, asset: Asset | int):
    """Event 1051362560"""
    GotoIfFlagEnabled(Label.L0, flag=9413)
    GotoIfFlagEnabled(Label.L1, flag=9410)

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=asset, animation_id=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(9413):
        return
    EndOfAnimation(asset=asset, animation_id=2)


@RestartOnRest(1051362580)
def Event_1051362580():
    """Event 1051362580"""
    RegisterLadder(start_climbing_flag=1051360580, stop_climbing_flag=1051360581, asset=Assets.AEG030_845_2000)
    RegisterLadder(start_climbing_flag=1051360582, stop_climbing_flag=1051360583, asset=Assets.AEG030_844_2000)
    RegisterLadder(start_climbing_flag=1051360584, stop_climbing_flag=1051360585, asset=Assets.AEG030_844_2001)
    RegisterLadder(start_climbing_flag=1051360588, stop_climbing_flag=1051360589, asset=Assets.AEG030_822_2002)
    RegisterLadder(start_climbing_flag=1051360590, stop_climbing_flag=1051360591, asset=Assets.AEG110_183_2000)
    RegisterLadder(start_climbing_flag=1051360592, stop_climbing_flag=1051360593, asset=Assets.AEG110_184_2001)
    RegisterLadder(start_climbing_flag=1051360594, stop_climbing_flag=1051360595, asset=Assets.AEG110_184_2002)


@RestartOnRest(1051362630)
def Event_1051362630(_, asset: Asset | int):
    """Event 1051362630"""
    DisableAsset(asset)


@RestartOnRest(1051362650)
def Event_1051362650(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    asset: Asset | int,
    source_flag: Flag | int,
    value: uint,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 1051362650"""
    MAIN.Await(FlagEnabled(1051360800))
    
    DeleteAssetVFX(asset, erase_root=False)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L3, flag=flag)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    DisableFlag(flag_5)
    DisableFlag(flag_6)
    DisableFlag(flag_7)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    AND_10.Add(EventValue(flag=source_flag, bit_count=3) > value)
    if AND_10:
        return
    if FlagDisabled(9000):
        CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(9000))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return RESTART
    AND_11.Add(EventValue(flag=source_flag, bit_count=3) > value)
    if AND_11:
        return RESTART
    CreateAssetVFX(asset, dummy_id=100, vfx_id=6400)
    if UnsignedEqual(left=value, right=0):
        EnableFlag(flag_2)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=0,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_2)
    if UnsignedEqual(left=value, right=1):
        EnableFlag(flag_3)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=1,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_3)
    if UnsignedEqual(left=value, right=2):
        EnableFlag(flag_4)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=2,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_4)
    if UnsignedEqual(left=value, right=3):
        EnableFlag(flag_5)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=3,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_5)
    if UnsignedEqual(left=value, right=4):
        EnableFlag(flag_6)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=4,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_6)
    if UnsignedEqual(left=value, right=5):
        EnableFlag(flag_7)
        EventValueOperation(
            source_flag=source_flag,
            source_flag_bit_count=3,
            operand=5,
            target_flag=0,
            target_flag_bit_count=1,
            calculation_type=CalculationType.Assign,
        )
    else:
        DisableFlag(flag_7)
    OR_2.Add(EventValue(flag=source_flag, bit_count=3) != value)
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1051362800)
def Event_1051362800():
    """Event 1051362800"""
    if FlagEnabled(1051360800):
        return
    AND_3.Add(FlagEnabled(9410))
    AND_3.Add(FlagDisabled(9413))
    if AND_3:
        return
    AND_1.Add(HealthValue(Characters.CrucibleKnight) <= 0)
    AND_1.Add(HealthValue(Characters.LeonineMisbegotten) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.CrucibleKnight, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.CrucibleKnight))
    AND_2.Add(CharacterDead(Characters.LeonineMisbegotten))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=Characters.CrucibleKnight, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(1051360800)
    EnableFlag(9183)
    if PlayerInOwnWorld():
        EnableFlag(61183)


@RestartOnRest(1051362810)
def Event_1051362810():
    """Event 1051362810"""
    GotoIfFlagDisabled(Label.L0, flag=1051360800)
    DisableCharacter(Characters.CrucibleKnight)
    DisableAnimations(Characters.CrucibleKnight)
    Kill(Characters.CrucibleKnight)
    DisableCharacter(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    Kill(Characters.LeonineMisbegotten)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L5, flag=9410)
    GotoIfFlagEnabled(Label.L5, flag=9413)
    DisableCharacter(Characters.CrucibleKnight)
    DisableAnimations(Characters.CrucibleKnight)
    Kill(Characters.CrucibleKnight)
    DisableCharacter(Characters.LeonineMisbegotten)
    DisableAnimations(Characters.LeonineMisbegotten)
    Kill(Characters.LeonineMisbegotten)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableAI(Characters.LeonineMisbegotten)
    DisableAI(Characters.CrucibleKnight)
    AND_2.Add(FlagEnabled(1051362805))
    AND_2.Add(OR_15)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1051362800))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.LeonineMisbegotten)
    SetNetworkUpdateRate(Characters.LeonineMisbegotten, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.LeonineMisbegotten, name=903460501)
    OR_1.Add(HealthRatio(Characters.LeonineMisbegotten) < 0.5)
    OR_1.Add(CharacterDead(Characters.LeonineMisbegotten))
    OR_1.Add(TimeElapsed(seconds=30.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.CrucibleKnight, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.CrucibleKnight, 20011)
    EnableAI(Characters.CrucibleKnight)
    SetNetworkUpdateRate(Characters.CrucibleKnight, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.CrucibleKnight, name=902500500, bar_slot=1)
    SetNest(Characters.CrucibleKnight, region=1051362299)


@RestartOnRest(1051362849)
def Event_1051362849():
    """Event 1051362849"""
    AND_3.Add(FlagEnabled(9410))
    AND_3.Add(FlagDisabled(9413))
    if AND_3:
        return
    CommonFunc_9005800(
        0,
        flag=1051360800,
        entity=Assets.AEG099_001_9000,
        region=1051362800,
        flag_1=1051362805,
        character=1051365800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1051360800,
        entity=Assets.AEG099_001_9000,
        region=1051362800,
        flag_1=1051362805,
        flag_2=1051362806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1051360800, asset=Assets.AEG099_001_9000, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=1051360800, asset=Assets.AEG099_001_9001, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1051360800,
        bgm_boss_conv_param_id=920200,
        flag_1=1051362805,
        flag_2=1051362806,
        right=0,
        flag_3=1051362802,
        left=0,
        left_1=0,
    )


@RestartOnRest(1051363700)
def Event_1051363700():
    """Event 1051363700"""
    AND_1.Add(FlagEnabled(1051362702))
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9411))
    AwaitConditionTrue(AND_1)
    PlayCutscene(60510000, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    EnableFlag(9411)
    End()


@RestartOnRest(1051363710)
def Event_1051363710(_, character: uint):
    """Event 1051363710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3667)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3667))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
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
    
    MAIN.Await(FlagDisabled(3667))
    
    Restart()


@RestartOnRest(1051363711)
def Event_1051363711():
    """Event 1051363711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9412):
        return
    AND_1.Add(FlagEnabled(9410))
    AwaitConditionTrue(AND_1)
    EnableFlag(3678)
    End()


@RestartOnRest(1051360720)
def Event_1051360720(_, character: uint):
    """Event 1051360720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1051369352)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L11, flag=3611)
    GotoIfFlagEnabled(Label.L12, flag=3612)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3611, 3612)))
    
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L2, flag=3602)
    GotoIfFlagEnabled(Label.L3, flag=3603)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(3611, 3612)))
    
    Restart()


@RestartOnRest(1051360721)
def Event_1051360721():
    """Event 1051360721"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9412):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(3605, 3610)))
    AND_1.Add(FlagEnabled(9410))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1051362739)
    EnableFlag(3618)


@RestartOnRest(1051363725)
def Event_1051363725(_, asset__character: uint):
    """Event 1051363725"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3360))
    AND_1.Add(FlagEnabled(1051369203))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1051369203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAssetInvulnerability(Assets.AEG030_930_2000)
    OR_1.Add(FlagEnabled(3365))
    OR_1.Add(FlagEnabled(3367))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3365))
    OR_2.Add(FlagEnabled(3367))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 90100)
    DisableGravity(asset__character)
    EnableAssetInvulnerability(Assets.AEG030_930_2000)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(asset__character)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAsset(asset__character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3365))
    OR_15.Add(FlagEnabled(3367))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1051363726)
def Event_1051363726(_, asset__character: uint):
    """Event 1051363726"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_1.Add(FlagEnabled(3360))
    AND_1.Add(FlagEnabled(1051369203))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1051369203)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    OR_1.Add(FlagEnabled(3366))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(3366))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=3360)
    GotoIfFlagEnabled(Label.L2, flag=3361)
    GotoIfFlagEnabled(Label.L4, flag=3363)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    ForceAnimation(asset__character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(asset__character)
    EnableBackread(asset__character)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(asset__character)
    DisableCharacter(asset__character)
    DisableBackread(asset__character)
    DisableAsset(asset__character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(3366))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(1051363727)
def Event_1051363727():
    """Event 1051363727"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=Characters.WitchHunterJerren1, distance=17.0)
    if FlagEnabled(9413):
        return
    SetCharacterTalkRange(character=Characters.WitchHunterJerren1, distance=80.0)
    AND_1.Add(FlagEnabled(3366))
    AND_1.Add(FlagDisabled(1051362701))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1051362701))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1051362700)
    End()


@RestartOnRest(1051360730)
def Event_1051360730(_, character: uint, animation_id: int, left: uint):
    """Event 1051360730"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    AddSpecialEffect(character, 5005)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9413))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(9410))
    AND_2.Add(FlagDisabled(9413))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id)
    if UnsignedNotEqual(left=left, right=0):
        DisableAnimations(character)
    AND_3.Add(FlagEnabled(9410))
    AND_3.Add(FlagDisabled(9413))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(1051360734)
def Event_1051360734(_, character: uint):
    """Event 1051360734"""
    if PlayerNotInOwnWorld():
        return
    AddSpecialEffect(character, 5005)
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9413))
    AND_1.Add(ActionButtonParamActivated(action_button_id=6000, entity=character))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 90203)
    Wait(2.5)
    if FlagDisabled(60801):
        AwardGesture(gesture_param_id=1)
        EnableFlag(60801)


@RestartOnRest(1051360735)
def Event_1051360735(_, character: uint, animation_id: int, left: uint):
    """Event 1051360735"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    AddSpecialEffect(character, 5005)
    if FlagDisabled(7606):
        EnableNetworkFlag(1051362735)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(9410))
    AND_1.Add(FlagDisabled(9413))
    AND_1.Add(FlagEnabled(1051362735))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(9410))
    AND_2.Add(FlagDisabled(9413))
    AND_2.Add(FlagEnabled(1051362735))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id)
    if UnsignedNotEqual(left=left, right=0):
        DisableAnimations(character)
    AND_3.Add(FlagEnabled(9410))
    AND_3.Add(FlagDisabled(9413))
    AND_3.Add(FlagEnabled(1051362735))
    
    MAIN.Await(not AND_3)
    
    Restart()
