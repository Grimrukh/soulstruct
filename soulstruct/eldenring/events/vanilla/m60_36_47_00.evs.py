"""
East Liurnia (NW) (NW)

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
from .entities.m60_36_47_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1036472600(
        0,
        anchor_entity=Assets.AEG099_090_9000,
        area_id=60,
        block_id=35,
        cc_id=46,
        dd_id=0,
        player_start=1035462611,
        flag=1035460615,
        target_entity=1036472601,
        animation=60470,
        action_button_id=9522,
    )
    Event_1036472605(0, flag=1036470605, target_entity=1036472606, animation=60471)
    CommonFunc_90005637(0, flag=32020691, character=Characters.WanderingNoble, region=1036471620)
    CommonFunc_90005636(
        0,
        flag=32020691,
        character=Characters.WanderingNoble,
        entity=Assets.AEG099_374_9000,
        special_effect_id=4470,
        destination=1036472620,
        region=1036472621,
        flag_1=1036472620,
        patrol_information_id=1036473620,
        right=-1,
    )


@ContinueOnRest(1036472600)
def Event_1036472600(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    flag: uint,
    target_entity: uint,
    animation: int,
    action_button_id: int,
):
    """Event 1036472600"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    SkipLinesIfConditionTrue(7, OR_1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    AND_9.Add(PlayerHasGood(8109))
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    DisplayDialog(text=20030, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    Wait(2.5)
    EnableFlag(flag)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)


@RestartOnRest(1036472605)
def Event_1036472605(_, flag: uint, target_entity: uint, animation: int):
    """Event 1036472605"""
    if FlagDisabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=animation)
    DisableFlag(flag)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036470700)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005451(0, character=Characters.WalkingMausoleum, asset_group=1036476420)
    CommonFunc_90005452(0, character=Characters.WalkingMausoleum, flag=1236470400)
    CommonFunc_90005454(0, character=Characters.WalkingMausoleum, flag=1236472400, flag_1=1236470400)
    CommonFunc_90005456(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_004_9000,
        asset_1=Assets.AEG300_005_9000,
        flag=1236470400,
    )
    CommonFunc_90005458(0, character=Characters.WalkingMausoleum, asset=Assets.AEG300_015_9000)
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9000,
        model_point=60,
        seconds=0.0,
    )
    CommonFunc_90005453(
        1,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9001,
        model_point=61,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9002,
        model_point=62,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9003,
        model_point=63,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9004,
        model_point=64,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9005,
        model_point=65,
        seconds=0.5,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9006,
        model_point=66,
        seconds=0.6000000238418579,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9007,
        model_point=67,
        seconds=0.699999988079071,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9008,
        model_point=68,
        seconds=0.800000011920929,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9009,
        model_point=69,
        seconds=0.8999999761581421,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9010,
        model_point=70,
        seconds=1.0,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9011,
        model_point=71,
        seconds=0.10000000149011612,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9012,
        model_point=72,
        seconds=0.20000000298023224,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9013,
        model_point=73,
        seconds=0.30000001192092896,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9014,
        model_point=74,
        seconds=0.4000000059604645,
    )
    CommonFunc_90005453(
        0,
        asset__character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_006_9015,
        model_point=75,
        seconds=0.5,
    )
    Event_1036472340()
    Event_1036472490()


@ContinueOnRest(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005450(
        0,
        character=Characters.WalkingMausoleum,
        asset=Assets.AEG300_003_9000,
        asset_1=Assets.AEG300_004_9000,
        asset_2=Assets.AEG300_005_9000,
    )


@RestartOnRest(1036472340)
def Event_1036472340():
    """Event 1036472340"""
    if FlagEnabled(1036470400):
        return
    
    MAIN.Await(CharacterInsideRegion(character=Characters.WalkingMausoleum, region=1036472340))
    
    ChangePatrolBehavior(Characters.WalkingMausoleum, patrol_information_id=1036473340)


@RestartOnRest(1036472490)
def Event_1036472490():
    """Event 1036472490"""
    if FlagDisabled(1036470400):
        return
    DisableAsset(Assets.AEG300_006_9000)
    DisableAsset(Assets.AEG300_006_9001)
    DisableAsset(Assets.AEG300_006_9002)
    DisableAsset(Assets.AEG300_006_9003)
    DisableAsset(Assets.AEG300_006_9004)
    DisableAsset(Assets.AEG300_006_9005)
    DisableAsset(Assets.AEG300_006_9006)
    DisableAsset(Assets.AEG300_006_9007)
    DisableAsset(Assets.AEG300_006_9008)
    DisableAsset(Assets.AEG300_006_9009)
    DisableAsset(Assets.AEG300_006_9010)
    DisableAsset(Assets.AEG300_006_9011)
    DisableAsset(Assets.AEG300_006_9012)
    DisableAsset(Assets.AEG300_006_9013)
    DisableAsset(Assets.AEG300_006_9014)
    DisableAsset(Assets.AEG300_006_9015)
