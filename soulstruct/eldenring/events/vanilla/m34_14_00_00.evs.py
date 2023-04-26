"""
Divine Tower of East Altus

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
from .enums.m34_14_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34140000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=34140001, asset=Assets.AEG099_060_9001)
    Event_34142850()
    Event_34140860()
    Event_34142899()
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellSoldier,
        region=34142300,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_34142250(
        0,
        flag=34140250,
        flag_1=34142250,
        anchor_entity=Characters.Scarab,
        character=Characters.ExtraLargeScarab,
        left=1,
        item_lot=34140720,
    )
    Event_34142251(
        0,
        character=34140250,
        flag=34142250,
        character_1=Characters.Scarab,
        character_2=Characters.ExtraLargeScarab,
        left=1,
    )
    Event_34142252(0, flag=34140250, seconds=0.0, character=Characters.Scarab, seconds_1=0.0)
    Event_34142870()
    Event_34142865()
    Event_34142875()
    Event_34142510()
    CommonFunc_90005501(
        0,
        flag=34140510,
        flag_1=34140511,
        left=4,
        asset=Assets.AEG027_033_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=34140512,
    )
    CommonFunc_90005508(
        0,
        flag=34140515,
        flag_1=34141515,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0501,
        asset_1=Assets.AEG027_203_0500,
        flag_2=34140517,
    )
    CommonFunc_90005110(
        0,
        flag=193,
        flag_1=9104,
        asset=Assets.AEG099_991_9000,
        item_lot=34140700,
        item=8150,
        model_point=806932,
        action_button_id=9082,
        animation_id=60521,
        left=0,
    )
    CommonFunc_90005110(
        0,
        flag=195,
        flag_1=9112,
        asset=Assets.AEG099_991_9001,
        item_lot=34140710,
        item=8152,
        model_point=806938,
        action_button_id=9084,
        animation_id=60524,
        left=0,
    )
    CommonFunc_91005600(0, flag=34142800, asset=34141695, model_point=5)
    Event_34142550()
    Event_34140700()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(34140700)
    Event_34140519()


@RestartOnRest(34142250)
def Event_34142250(_, flag: uint, flag_1: uint, anchor_entity: uint, character: uint, left: int, item_lot: int):
    """Event 34142250"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(1.0)
    if PlayerNotInOwnWorld():
        return
    if ValueNotEqual(left=item_lot, right=0):
        AwardItemLot(item_lot, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(34142251)
def Event_34142251(_, character: uint, flag: uint, character_1: uint, character_2: uint, left: int):
    """Event 34142251"""
    EnableImmortality(character_1)
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    DisableGravity(character_2)
    DisableAI(character_2)
    SetCharacterFadeOnEnable(character=character_2, state=True)
    AND_1.Add(CharacterHasSpecialEffect(character_1, 12610))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character_1, True)
    SetBackreadStateAlternate(character_2, True)
    Move(
        character_2,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character_1,
    )
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=641912, anchor_entity=character_1, model_point=10, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=641911, anchor_entity=character_1, model_point=10, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(0.20000000298023224)
    DisableCharacter(character)
    EnableCharacter(character_2)
    EnableGravity(character_2)
    EnableAnimations(character_2)
    EnableAI(character_2)
    DisableCharacter(character_1)
    SetBackreadStateAlternate(character_1, False)
    SetBackreadStateAlternate(character_2, False)
    ForceAnimation(character_2, 20026, wait_for_completion=True)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag)
    End()


@RestartOnRest(34142252)
def Event_34142252(_, flag: uint, seconds: float, character: uint, seconds_1: float):
    """Event 34142252"""
    if FlagEnabled(flag):
        return
    AND_1.Add(HealthValue(character) == 1)
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(character)
    AddSpecialEffect(character, 12614)
    End()
    Wait(seconds)
    Wait(seconds_1)


@ContinueOnRest(34142510)
def Event_34142510():
    """Event 34142510"""
    CommonFunc_90005500(
        0,
        flag=34140510,
        flag_1=34140511,
        left=4,
        asset=Assets.AEG027_033_0500,
        asset_1=Assets.AEG027_002_0500,
        obj_act_id=34143511,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=34143512,
        region=34142511,
        region_1=34142512,
        flag_2=34140512,
        flag_3=34140513,
        left_1=0,
    )
    CommonFunc_90005507(
        0,
        flag=34140515,
        flag_1=34141515,
        left=0,
        asset=Assets.AEG027_070_0500,
        entity=Assets.AEG027_203_0501,
        region=34142518,
        entity_1=Assets.AEG027_203_0500,
        region_1=34142519,
        region_2=34142516,
        region_3=34142517,
        flag_2=34140517,
        flag_3=34142517,
        left_1=0,
    )


@ContinueOnRest(34140519)
def Event_34140519():
    """Event 34140519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(34140510)
    EnableThisSlotFlag()


@RestartOnRest(34142550)
def Event_34142550():
    """Event 34142550"""
    GotoIfFlagDisabled(Label.L0, flag=34140550)
    DisableAsset(Assets.AEG099_239_9000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=34142550)
    DeleteAssetVFX(Assets.AEG099_239_9000)
    CreateAssetVFX(Assets.AEG099_239_9000, vfx_id=101, model_point=1541)
    EnableNetworkFlag(34142550)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9505, entity=Assets.AEG099_239_9000))
    AND_2.Add(FlagEnabled(400001))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20005, anchor_entity=Assets.AEG099_239_9000, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(34140550)
    DeleteAssetVFX(Assets.AEG099_239_9000)
    DisableAsset(Assets.AEG099_239_9000)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteAssetVFX(Assets.AEG099_239_9000)
    CreateAssetVFX(Assets.AEG099_239_9000, vfx_id=101, model_point=1541)
    End()


@RestartOnRest(34142850)
def Event_34142850():
    """Event 34142850"""
    if FlagEnabled(34140850):
        return
    AND_1.Add(HealthValue(Characters.Omen0) <= 0)
    AND_1.Add(HealthValue(Characters.Omen1) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Omen0, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.Omen0))
    AND_2.Add(CharacterDead(Characters.Omen1))
    
    MAIN.Await(AND_2)
    
    Wait(1.5)
    KillBossAndDisplayBanner(character=Characters.Omen0, banner_type=BannerType.EnemyFelled)
    EnableFlag(34140850)
    EnableFlag(9174)
    if PlayerInOwnWorld():
        EnableFlag(10740)
    End()


@RestartOnRest(34140860)
def Event_34140860():
    """Event 34140860"""
    GotoIfFlagDisabled(Label.L0, flag=34140850)
    DisableCharacter(Characters.Omen0)
    DisableAnimations(Characters.Omen0)
    Kill(Characters.Omen0)
    DisableCharacter(Characters.Omen1)
    DisableAnimations(Characters.Omen1)
    Kill(Characters.Omen1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Omen0)
    DisableAI(Characters.Omen1)
    DisableCharacter(Characters.Omen0)
    DisableCharacter(Characters.Omen1)
    GotoIfFlagEnabled(Label.L1, flag=34140851)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34142855))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Omen0, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(34140851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=34142856))
    
    MAIN.Await(AND_2)
    
    Wait(1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(34142855)
    EnableCharacter(Characters.Omen0)
    EnableCharacter(Characters.Omen1)
    EnableAI(Characters.Omen0)
    EnableAI(Characters.Omen1)
    SetNetworkUpdateRate(Characters.Omen0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.Omen1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Omen0, name=902140000, bar_slot=1)
    EnableBossHealthBar(Characters.Omen1, name=902140001)
    EnableThisNetworkSlotFlag()


@RestartOnRest(34142865)
def Event_34142865():
    """Event 34142865"""
    if FlagEnabled(34140865):
        return
    
    MAIN.Await(FlagEnabled(34140850))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(4.0)
    AddSpecialEffect(20000, 8870)
    Wait(2.0)
    EnableFlag(34140865)
    WarpToMap(game_map=DIVINE_TOWER_OF_EAST_ALTUS, player_start=34142852)


@RestartOnRest(34142870)
def Event_34142870():
    """Event 34142870"""
    DisableNetworkSync()
    if FlagEnabled(34140850):
        return
    AND_1.Add(FlagEnabled(34142885))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=34142870))
    
    MAIN.Await(AND_2)
    
    SetWeather(weather=Weather.Fog, duration=10.0, immediate_change=False)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(2.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=34142851,
        model_point=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    SetPlayerPositionDisplay(
        state=False,
        aboveground=True,
        game_map=DIVINE_TOWER_OF_EAST_ALTUS,
        x=481.9800109863281,
        y=26.1299991607666,
        z=-267.3299865722656,
    )


@RestartOnRest(34142875)
def Event_34142875():
    """Event 34142875"""
    if FlagDisabled(34140850):
        return
    MoveRemains(source_region=34142875, destination_region=34142876)


@ContinueOnRest(34142899)
def Event_34142899():
    """Event 34142899"""
    CommonFunc_9005822(
        0,
        flag=34140850,
        bgm_boss_conv_param_id=921200,
        flag_1=34142855,
        flag_2=34142856,
        right=0,
        flag_3=0,
        left=0,
        left_1=0,
    )


@RestartOnRest(34140700)
def Event_34140700():
    """Event 34140700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(34149200):
        return
    
    MAIN.Await(FlagEnabled(11109687))
    
    MAIN.Await(CharacterInsideRegion(character=20000, region=34142700))
    
    EnableFlag(34149200)
