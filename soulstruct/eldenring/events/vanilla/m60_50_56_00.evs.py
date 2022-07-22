"""
Northwest Mountaintops (SE) (SW)

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
from .entities.m60_50_56_00_entities import *
from .entities.m60_50_57_00_entities import Characters as m60_50_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=Characters.GreatWyrmTheodorix, name=904911600, npc_threat_level=5)
    CommonFunc_90005861(
        0,
        flag=1050560800,
        left=0,
        character=Characters.GreatWyrmTheodorix,
        left_1=1,
        item_lot__item_lot_param_id=30550,
        text=30065,
        seconds=0.0,
    )
    Event_1050562200(0, attacker__character=1050565200, region=1050562200)
    Event_1050562580()
    CommonFunc_90005620(
        0,
        flag=1050560570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1050562570,
        cancel_flag__right_flag=1050562571,
        right=1050562572,
    )
    CommonFunc_90005621(0, flag=1050560570, asset=Assets.AEG099_272_9000)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=50,
        cc_id=56,
        dd_id=0,
        player_start=1050562510,
        unk_8_12=0,
        flag=1050562511,
        left_flag=1050562512,
        cancel_flag__right_flag=1050562513,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005633(
        0,
        character=580330,
        flag=580030,
        character_1=Characters.WanderingNoble,
        animation_id=30016,
        animation_id_1=20016,
        asset=Assets.AEG099_166_9000,
        asset_1=Assets.AEG099_990_9001,
    )
    Event_1050562555(0, character=Characters.WanderingNoble)
    Event_1050562250(
        0,
        flag=1050560250,
        asset=1050566250,
        character=Characters.Imp0,
        character_1=Characters.Imp1,
        character_2=35000,
        special_effect=17170,
        special_effect_1=17171,
    )
    Event_1050562260(0, anchor_entity=Assets.AEG099_251_9000)
    Event_1050562260(1, anchor_entity=Assets.AEG099_251_9001)
    Event_1050562260(2, anchor_entity=Assets.AEG099_251_9002)
    CommonFunc_90005300(0, flag=1050560300, character=Characters.RedWolf, item_lot_param_id=0, seconds=0.0, left=0)
    CommonFunc_90005560(0, flag=1050560500, asset=Assets.AEG099_635_9000, left=0)
    CommonFunc_90005795(
        0,
        flag=7604,
        flag_1=0,
        flag_2=1050569000,
        left_flag=1050562141,
        cancel_flag__right_flag=1050562142,
        message=80604,
        action_button_id=9000,
        asset=Assets.AEG099_090_9001,
        model_point=30010,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=20)
    CommonFunc_90005796(0, flag=7604, character=Characters.JunoHoslow, banner_type=5, region=1050562141)
    Event_1050562145()
    Event_1050562400()
    Event_1050563700()
    CommonFunc_90005774(0, 7604, 1050560700, 1050567700)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.JunoHoslow)


@RestartOnRest(1050562145)
def Event_1050562145():
    """Event 1050562145"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    EnableBackread(Characters.JunoHoslow)
    SetTeamType(Characters.JunoHoslow, TeamType.Human)
    DisableCharacter(m60_50_Characters.GiantSkeletonTorso)
    DisableAnimations(m60_50_Characters.GiantSkeletonTorso)
    DeleteAssetVFX(1050566700)
    CreateAssetVFX(1050566700, vfx_id=200, model_point=806700)


@RestartOnRest(1050562200)
def Event_1050562200(_, attacker__character: uint, region: uint):
    """Event 1050562200"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1050562200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1050562200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(1050562555)
def Event_1050562555(_, character: uint):
    """Event 1050562555"""
    DisableGravity(character)


@RestartOnRest(1050562580)
def Event_1050562580():
    """Event 1050562580"""
    RegisterLadder(start_climbing_flag=1050560580, stop_climbing_flag=1050560581, asset=Assets.AEG110_119_2000)


@RestartOnRest(1050562250)
def Event_1050562250(
    _,
    flag: uint,
    asset: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    special_effect: int,
    special_effect_1: int,
):
    """Event 1050562250"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EnableSpawner(entity=1050563250)
    EnableSpawner(entity=1050563251)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, vfx_id=200, model_point=1500)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect_1))
    AND_1.Add(HealthRatio(character) <= 0.0)
    OR_1.Add(AND_1)
    AND_2.Add(CharacterHasSpecialEffect(character_1, special_effect))
    AND_2.Add(CharacterHasSpecialEffect(character_1, special_effect_1))
    AND_2.Add(HealthRatio(character_1) <= 0.0)
    OR_1.Add(AND_2)
    AND_3.Add(CharacterHasSpecialEffect(character_2, special_effect))
    AND_3.Add(CharacterHasSpecialEffect(character_2, special_effect_1))
    AND_3.Add(HealthRatio(character_2) <= 0.0)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(flag)
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=1050563250)
    DisableSpawner(entity=1050563251)
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisplayDialog(text=20210, anchor_entity=0, display_distance=5.0)
    DisableSpawner(entity=1050563250)
    DisableSpawner(entity=1050563251)
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1050562260)
def Event_1050562260(_, anchor_entity: uint):
    """Event 1050562260"""
    DisableNetworkSync()
    if FlagEnabled(1050560250):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9320, entity=anchor_entity))
    OR_1.Add(FlagEnabled(1050560250))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1050560250):
        return
    DisplayDialog(text=20200, anchor_entity=anchor_entity)
    Wait(1.0)
    Restart()


@RestartOnRest(1050562400)
def Event_1050562400():
    """Event 1050562400"""
    DisableNetworkSync()
    AwaitFlagEnabled(flag=1050562140)
    AddSpecialEffect(Characters.TalkDummy, 9531)
    AwaitFlagDisabled(flag=1050562140)
    AddSpecialEffect(Characters.TalkDummy, 9532)
    Wait(1.0)
    Restart()


@RestartOnRest(1050563700)
def Event_1050563700():
    """Event 1050563700"""
    WaitFrames(frames=1)
    if FlagDisabled(400075):
        return
    EnableFlag(1050569000)
    End()
