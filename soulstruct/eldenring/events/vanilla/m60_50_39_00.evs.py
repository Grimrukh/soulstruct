"""
South Caelid (NE) (NW)

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
from .entities.m60_50_39_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1050392210(0, character=Characters.GiantBall0, asset=Assets.AEG099_090_9001, region=1050392290)
    Event_1050392210(1, character=Characters.GiantBall1, asset=Assets.AEG099_090_9002, region=1050392291)
    Event_1050392580(0, start_climbing_flag=50390580, stop_climbing_flag=50390851, asset=Assets.AEG110_069_2000)
    CommonFunc_90005525(0, flag=1050390620, asset=Assets.AEG004_998_1000)
    CommonFunc_90005632(0, flag=580060, asset=Assets.AEG099_391_2000, item_lot=80060)
    Event_1050392300(0, asset=Assets.AEG099_252_2000, flag=1050390200)
    Event_1050392300(1, asset=Assets.AEG099_252_2001, flag=1050390200)
    Event_1050392301(2, asset=Assets.AEG099_253_2000, flag=1050390201)
    Event_1050392303(0, asset=Assets.AEG099_047_2001, flag=1050390201)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar0, radius=11.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar3, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar4, radius=7.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar6, region=1050392208, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.RayaLucariaScholar7, radius=8.0, seconds=0.0, animation_id=-1)
    Event_1050392200(0, character=Characters.RayaLucariaScholar0, special_effect_id=14807)
    Event_1050392200(1, character=Characters.RayaLucariaScholar1, special_effect_id=14808)
    Event_1050392200(4, character=Characters.RayaLucariaScholar2, special_effect_id=14808)
    Event_1050392200(5, character=Characters.RayaLucariaScholar3, special_effect_id=14807)
    Event_1050392200(6, character=Characters.RayaLucariaScholar4, special_effect_id=14807)
    Event_1050392200(7, character=Characters.RayaLucariaScholar5, special_effect_id=14807)
    Event_1050392200(8, character=Characters.RayaLucariaScholar6, special_effect_id=14807)
    Event_1050392200(9, character=Characters.RayaLucariaScholar7, special_effect_id=14807)
    Event_1050392200(10, character=Characters.RayaLucariaScholar8, special_effect_id=14807)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton0,
        animation_id=30014,
        animation_id_1=20014,
        region=1050392350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton1,
        animation_id=30014,
        animation_id_1=20014,
        region=1050392350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_1050392200(11, character=Characters.WanderingNoble0, special_effect_id=10113)
    Event_1050392200(12, character=Characters.WanderingNoble4, special_effect_id=14807)
    Event_1050392200(13, character=Characters.WanderingNoble9, special_effect_id=14807)
    Event_1050392200(14, character=Characters.WanderingNoble10, special_effect_id=14807)
    Event_1050392201(0, character=Characters.WanderingNoble1, special_effect_id=10113, seconds=4.0, seconds_1=3.0)
    Event_1050392201(1, character=Characters.WanderingNoble2, special_effect_id=10113, seconds=5.0, seconds_1=4.0)
    Event_1050392201(2, character=Characters.WanderingNoble3, special_effect_id=10113, seconds=6.0, seconds_1=2.0)
    Event_1050392201(3, character=Characters.WanderingNoble5, special_effect_id=10113, seconds=4.0, seconds_1=4.0)
    Event_1050392201(4, character=Characters.WanderingNoble6, special_effect_id=10113, seconds=6.0, seconds_1=3.0)
    Event_1050392201(5, character=Characters.WanderingNoble7, special_effect_id=10113, seconds=5.0, seconds_1=3.0)
    Event_1050392201(6, character=Characters.WanderingNoble8, special_effect_id=10113, seconds=6.0, seconds_1=4.0)
    CommonFunc_90005200(
        0,
        character=Characters.GraveSkeleton,
        animation_id=30016,
        animation_id_1=20016,
        region=1050392350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 1050390400, 1050392400, 0.0, -1)


@RestartOnRest(1050392200)
def Event_1050392200(_, character: uint, special_effect_id: int):
    """Event 1050392200"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1050392201)
def Event_1050392201(_, character: uint, special_effect_id: int, seconds: float, seconds_1: float):
    """Event 1050392201"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)
    Wait(seconds)
    RemoveSpecialEffect(character, special_effect_id)
    Wait(seconds_1)
    Restart()


@RestartOnRest(1050392210)
def Event_1050392210(_, character: uint, asset: uint, region: uint):
    """Event 1050392210"""
    DisableCharacter(character)
    if FlagEnabled(region):
        return
    AND_3.Add(CharacterDead(character))
    if AND_3:
        return
    DisableHealthBar(character)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    CreateAssetVFX(asset, vfx_id=100, model_point=620383)
    EnableCharacter(character)
    EnableNetworkFlag(region)
    Wait(2.0)
    DeleteAssetVFX(asset)
    ForceAnimation(character, 20001)
    Wait(1.899999976158142)
    ForceAnimation(character, 20004)
    Wait(2.0)
    ForceAnimation(character, 20004)
    Wait(1.0)
    DisableCharacter(character)
    Kill(character)
    End()


@ContinueOnRest(1050392300)
def Event_1050392300(_, asset: uint, flag: uint):
    """Event 1050392300"""
    EnableNetworkSync()
    CreateAssetVFX(asset, vfx_id=200, model_point=1502)
    
    MAIN.Await(FlagEnabled(flag))
    
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(asset)
    DeleteAssetVFX(asset)


@ContinueOnRest(1050392301)
def Event_1050392301(_, asset: uint, flag: uint):
    """Event 1050392301"""
    EnableNetworkSync()
    CreateAssetVFX(asset, vfx_id=200, model_point=1501)
    
    MAIN.Await(FlagEnabled(flag))
    
    PlaySoundEffect(asset, 1500, sound_type=SoundType.s_SFX)
    DisableAsset(asset)
    DeleteAssetVFX(asset)


@ContinueOnRest(1050392303)
def Event_1050392303(_, asset: uint, flag: uint):
    """Event 1050392303"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9520, entity=asset))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, asset, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    DisplayDialog(text=30000, anchor_entity=asset)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=100, model_point=806031)
    End()


@ContinueOnRest(1050392580)
def Event_1050392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, asset: uint):
    """Event 1050392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, asset=asset)
