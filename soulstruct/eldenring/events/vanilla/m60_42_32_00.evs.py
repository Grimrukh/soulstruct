"""
West Weeping Peninsula (SE) (SW)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .enums.m60_42_32_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, character=Characters.GiantOctopus)
    Event_1042322220()
    Event_1042322230()
    Event_1042322580()
    Event_1042322510(0, asset=Assets.AEG099_290_9000, region=1042322510, flag=1042322500, obj_act_id=1042323900)


@RestartOnRest(1042322220)
def Event_1042322220():
    """Event 1042322220"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=1042322220))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(Characters.WolfPackLeader, 3011)
    Wait(5.0)
    TriggerAISound(ai_sound_param_id=4020, anchor_entity=1042322220, unk_8_12=1)
    End()


@RestartOnRest(1042322230)
def Event_1042322230():
    """Event 1042322230"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=1042322230))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()
    ForceAnimation(Characters.GodrickFootSoldier, 3031)
    End()


@RestartOnRest(1042322500)
def Event_1042322500(_, character: uint):
    """Event 1042322500"""
    AddSpecialEffect(character, 5000)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 5411))
    
    RemoveSpecialEffect(character, 5000)


@RestartOnRest(1042322510)
def Event_1042322510(_, asset: uint, region: uint, flag: uint, obj_act_id: uint):
    """Event 1042322510"""
    DisableNetworkSync()
    GotoIfMultiplayerPending(Label.L1)
    GotoIfMultiplayer(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_1.Add(MultiplayerPending())
    OR_1.Add(Multiplayer())
    
    MAIN.Await(OR_1)
    
    GotoIfMultiplayerPending(Label.L1)
    GotoIfMultiplayer(Label.L1)
    EnableFlag(flag)
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    GotoIfMultiplayerPending(Label.L2)
    GotoIfMultiplayer(Label.L2)
    AND_1.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    GotoIfMultiplayerPending(Label.L2)
    GotoIfMultiplayer(Label.L2)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=True, freeze_player_delay=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    DisableCharacter(PLAYER)
    AND_3.Add(HealthValue(PLAYER) == 0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_3)
    GotoIfMultiplayerPending(Label.L3)
    GotoIfMultiplayer(Label.L3)
    AddSpecialEffect(PLAYER, 4091)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    EnableFlag(11000601)
    GotoIfFlagEnabled(Label.L10, flag=300)
    WarpToMap(game_map=LEYNDELL_ROYAL_CAPITAL, player_start=11002697, unk_8_12=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=11002697)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    WarpToMap(game_map=LEYNDELL_ASHEN_CAPITAL, player_start=11052680, unk_8_12=60)
    SaveRequest()
    SetRespawnPoint(respawn_point=11052680)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)
    Wait(4.400000095367432)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(asset, 2, wait_for_completion=True)
    DisableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=asset, animation_id=2)
    DisableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableAssetActivation(asset, obj_act_id=-1)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131)
    FadeToBlack(strength=0.0, duration=0.0, freeze_player=False, freeze_player_delay=-1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAssetActivation(asset, obj_act_id=-1)
    ForceAnimation(asset, 2, wait_for_completion=True)
    DisableFlag(flag)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetActivation(asset, obj_act_id=-1)
    OR_2.Add(MultiplayerPending())
    AND_2.Add(not OR_2)
    OR_3.Add(Multiplayer())
    AND_2.Add(not OR_3)
    
    MAIN.Await(AND_2)
    
    EnableAssetActivation(asset, obj_act_id=-1)
    Restart()


@RestartOnRest(1042322400)
def Event_1042322400():
    """Event 1042322400"""
    GotoIfFlagDisabled(Label.L0, flag=1042320400)
    DisableAsset(1042321400)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(1042321400, erase_root=False)
    CreateAssetVFX(1042321400, vfx_id=101, dummy_id=6)
    AND_1.Add(FlagEnabled(1042320401))
    AND_1.Add(FlagEnabled(1042320402))
    AND_1.Add(FlagEnabled(1042320403))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042320400)
    DeleteAssetVFX(1042321400)
    DisableAsset(1042321400)


@RestartOnRest(1042322401)
def Event_1042322401(_, flag: uint, asset: uint, asset_1: uint):
    """Event 1042322401"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DestroyAsset(asset)
    CreateAssetVFX(asset_1, vfx_id=90, dummy_id=800056)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(AssetDestroyed(asset))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    CreateAssetVFX(asset_1, vfx_id=90, dummy_id=800056)


@RestartOnRest(1042322402)
def Event_1042322402():
    """Event 1042322402"""
    DisableAsset(1042321400)
    DisableAsset(1042321401)
    DisableAsset(1042321402)
    DisableAsset(1042321403)
    DisableAsset(1042321404)
    DisableAsset(1042321405)
    DisableAsset(1042321406)


@RestartOnRest(1042322403)
def Event_1042322403(
    _,
    character: uint,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    special_effect: int,
):
    """Event 1042322403"""
    AddSpecialEffect(character_1, 10196)
    ForceAnimation(character_1, animation_id, loop=True)
    AND_1.Add(CharacterHasSpecialEffect(character_1, 5080))
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character_1))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Search))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=special_effect, target_count=0)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=2.0)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(character_1, 10196)
    ForceAnimation(character_1, animation_id_1, wait_for_completion=True)
    ReplanAI(character_1)


@RestartOnRest(1042322404)
def Event_1042322404(_, flag: uint, character: uint):
    """Event 1042322404"""
    EnableCharacter(character)
    EnableAnimations(character)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableCharacter(character)
    DisableAnimations(character)


@ContinueOnRest(1042322580)
def Event_1042322580():
    """Event 1042322580"""
    RegisterLadder(start_climbing_flag=1042320580, stop_climbing_flag=1042320851, asset=Assets.AEG110_012_1000)
    RegisterLadder(start_climbing_flag=1042320582, stop_climbing_flag=1042320853, asset=Assets.AEG110_012_1001)
    RegisterLadder(start_climbing_flag=1042320584, stop_climbing_flag=1042320855, asset=Assets.AEG110_012_1002)
