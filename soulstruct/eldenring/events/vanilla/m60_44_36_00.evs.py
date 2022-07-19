"""
East Limgrave (SW) (SW)

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
from .entities.m60_44_36_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=1044360800,
        grace_flag=76120,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_1044362800()
    Event_1044362810()
    Event_1044362849()
    CommonFunc_90005300(0, flag=1044360220, character=Characters.Scarab, item_lot_param_id=40112, seconds=0.0, left=0)
    Event_1044362500()
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.SorceressSellen,
        flag=3461,
        flag_1=3460,
        flag_2=1044369201,
        right=3,
    )
    RunCommonEvent(
        1044363711,
        slot=0,
        args=(1044360700, 3461, 3462, 1044369201, 0.6499999761581421, 3460, 3463, -1),
        arg_types="IIIIfIIi",
    )
    Event_1044363710(0, character=Characters.SorceressSellen)
    Event_1044363712(0, entity=Characters.SorceressSellen)
    Event_1044363713()
    Event_1044363714(0, entity=Characters.SorceressSellen)
    CommonFunc_90005709(0, attacked_entity=Characters.SorceressSellen, model_point=905, vfx_id=603001)
    CommonFunc_90005709(0, 1044360700, 200, 603051)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.SorceressSellen)
    DisableBackread(Characters.TalkDummy0)
    CommonFunc_90005251(0, character=Characters.GiantMirandaFlower, radius=30.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.MirandaFlower0, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.MirandaFlower1, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.MirandaFlower2, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1044360211, region=1044362211, radius=1.0, seconds=0.0, animation_id=1701)
    CommonFunc_90005261(
        0,
        character=Characters.LargeCrab0,
        region=1044362211,
        radius=1.0,
        seconds=0.5,
        animation_id=1701,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LargeCrab1,
        region=1044362211,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=1701,
    )
    CommonFunc_90005261(
        0,
        character=1044360214,
        region=1044362211,
        radius=1.0,
        seconds=0.699999988079071,
        animation_id=1701,
    )
    CommonFunc_90005261(0, character=1044360200, region=1044362200, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(0, 1044360200, 30014, 20014, 1044362200, 10.0, 0.0, 0, 0, 0, 0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005421(0, character=Characters.CaravanDummy, asset=Assets.AEG100_101_9000, flag=1044368301)
    CommonFunc_90005422(0, flag=1044368301, asset=Assets.AEG100_100_9000, obj_act_id=1044363301)
    CommonFunc_90005424(
        0,
        asset=Assets.AEG100_100_9000,
        character=Characters.Troll0,
        character_1=Characters.Troll1,
        character_2=Characters.CaravanDummy,
        asset_1=Assets.AEG100_101_9000,
    )
    CommonFunc_90005423(0, character=Characters.Troll0)
    CommonFunc_90005423(0, character=Characters.Troll1)
    Event_1044362300()


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005420(0, 1044360300, 1044361300, 1044361301, 1044360301, 1044360302, 1044360303, 0.0)


@RestartOnRest(1044362500)
def Event_1044362500():
    """Event 1044362500"""
    EnableAssetInvulnerability(Assets.AEG700_031_1001)


@RestartOnRest(1044362300)
def Event_1044362300():
    """Event 1044362300"""
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=150,
        behavior_param_id=100700,
        target_type=DamageTargetType.Character,
        radius=3.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=200,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=201,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=202,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=203,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=204,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )
    CreateHazard(
        asset_flag=1044361301,
        asset=Assets.AEG100_100_9000,
        model_point=205,
        behavior_param_id=100701,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.0,
        repetition_time=10.0,
    )


@RestartOnRest(1044362650)
def Event_1044362650(_, tutorial_param_id: int, flag: uint, flag_1: uint, flag_2: uint):
    """Event 1044362650"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag_2, bit_count=1)


@RestartOnRest(1044362651)
def Event_1044362651(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1044362651"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=EAST_LIMGRAVE_SW_SW))
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9120, flag=flag_1, bit_count=1)


@RestartOnRest(1044362652)
def Event_1044362652(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 1044362652"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9530))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=EAST_LIMGRAVE_SW_SW))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1044362654)
def Event_1044362654(_, tutorial_param_id: int, flag: uint):
    """Event 1044362654"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    OR_15.Add(PlayerHasWeapon(33000000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(33210000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(34000000, including_storage=True))
    OR_15.Add(PlayerHasWeapon(34040000, including_storage=True))
    if OR_15:
        return
    OR_1.Add(PlayerHasWeapon(33000000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(33210000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(34000000, including_storage=True))
    OR_1.Add(PlayerHasWeapon(34040000, including_storage=True))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=EAST_LIMGRAVE_SW_SW))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    Wait(1.0)
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9101, flag=flag, bit_count=1)


@RestartOnRest(1044363700)
def Event_1044363700(
    _,
    asset__character: uint,
    asset__character_1: uint,
    asset__character_2: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1044363700"""
    WaitFrames(frames=1)
    DisableFlag(flag)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableCharacter(asset__character)
    EnableCharacter(asset__character_1)
    EnableAsset(asset__character_2)
    EnableBackread(asset__character)
    EnableBackread(asset__character_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableCharacter(asset__character)
    DisableCharacter(asset__character_1)
    DisableAsset(asset__character_2)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(asset__character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(asset__character)
    DropMandatoryTreasure(asset__character_1)
    DisableCharacter(asset__character)
    DisableCharacter(asset__character_1)
    DisableAsset(asset__character)
    DisableAsset(asset__character_1)
    DisableAsset(asset__character_2)
    DisableBackread(asset__character)
    DisableBackread(asset__character_2)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()


@RestartOnRest(1044363701)
def Event_1044363701(_, flag: uint, flag_1: uint, flag_2: uint, first_flag: uint, last_flag: uint):
    """Event 1044363701"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagDisabled(flag_1):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(first_flag)
        End()
    if FlagEnabled(flag_2):
        return
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_2)


@RestartOnRest(1044363702)
def Event_1044363702(_, character: uint, flag: uint, first_flag: uint, flag_1: uint, last_flag: uint, flag_2: uint):
    """Event 1044363702"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(first_flag))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)


@RestartOnRest(1044363710)
def Event_1044363710(_, character: uint):
    """Event 1044363710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3460):
        DisableFlag(1041339253)

    # --- Label 19 --- #
    DefineLabel(19)
    AND_1.Add(FlagEnabled(3465))
    AND_1.Add(FlagDisabled(1044369231))
    GotoIfConditionTrue(Label.L6, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    AND_2.Add(FlagEnabled(3465))
    AND_2.Add(FlagDisabled(1044369231))
    AwaitConditionTrue(AND_2)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3460)
    GotoIfFlagEnabled(Label.L2, flag=3461)
    GotoIfFlagEnabled(Label.L4, flag=3463)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90105)
    DisableInvincibility(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_5.Add(FlagEnabled(3465))
    AND_5.Add(FlagDisabled(1044369231))
    AwaitConditionFalse(AND_5)
    Restart()


@RestartOnRest(1044363711)
def Event_1044363711(
    _,
    character: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    value: float,
    first_flag: uint,
    last_flag: uint,
    right: int,
):
    """Event 1044363711"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagDisabled(3000))
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=40000))
    AND_2.Add(OR_1)
    AND_2.Add(HealthRatio(character) < value)
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(flag_2))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()


@RestartOnRest(1044363712)
def Event_1044363712(_, entity: uint):
    """Event 1044363712"""
    if FlagEnabled(3461):
        return
    AwaitFlagEnabled(flag=3461)
    ForceAnimation(entity, 90207)
    End()


@RestartOnRest(1044363713)
def Event_1044363713():
    """Event 1044363713"""
    AND_1.Add(FlagEnabled(1044369236))
    AND_1.Add(FlagEnabled(1044369230))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(100500, 100749)) >= 3)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1044369237)
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(100500, 100749)) >= 6)
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1044369235)

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@NeverRestart(1044363714)
def Event_1044363714(_, entity: uint):
    """Event 1044363714"""
    if FlagDisabled(3465):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1044369231))
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=20000, radius=50.0))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(3478)
    End()


@RestartOnRest(1044362800)
def Event_1044362800():
    """Event 1044362800"""
    if FlagEnabled(1044360800):
        return
    
    MAIN.Await(HealthValue(Characters.MadPumpkinHead) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.MadPumpkinHead, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.MadPumpkinHead))
    
    KillBossAndDisplayBanner(character=Characters.MadPumpkinHead, banner_type=BannerType.EnemyFelled)
    EnableAssetActivation(Assets.AEG004_970_1000, obj_act_id=-1)
    EnableFlag(1044360800)


@RestartOnRest(1044362810)
def Event_1044362810():
    """Event 1044362810"""
    GotoIfFlagDisabled(Label.L0, flag=1044360800)
    DisableCharacter(Characters.MadPumpkinHead)
    DisableAnimations(Characters.MadPumpkinHead)
    Kill(Characters.MadPumpkinHead)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.MadPumpkinHead)
    AND_2.Add(FlagEnabled(1044362805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1044362800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.MadPumpkinHead)
    SetNetworkUpdateRate(Characters.MadPumpkinHead, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.MadPumpkinHead, name=904340540)
    DisableAssetActivation(Assets.AEG004_970_1000, obj_act_id=-1)


@RestartOnRest(1044362849)
def Event_1044362849():
    """Event 1044362849"""
    CommonFunc_9005800(
        0,
        flag=1044360800,
        entity=Assets.AEG099_001_9000,
        region=1044362800,
        flag_1=1044362805,
        character=1044365800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1044360800,
        entity=Assets.AEG099_001_9000,
        region=1044362800,
        flag_1=1044362805,
        flag_2=1044362806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1044360800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(
        0,
        flag=1044360800,
        bgm_boss_conv_param_id=920900,
        flag_1=1044362805,
        flag_2=1044362806,
        right=0,
        flag_3=1044362802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, 1044360800, 1044361801, 3, 0, 0)
