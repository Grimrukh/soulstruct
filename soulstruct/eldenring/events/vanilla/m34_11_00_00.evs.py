"""
Divine Tower of Liurnia

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
from .entities.m34_11_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=34110000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=34110001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=34110002, asset=Assets.AEG099_060_9002)
    CommonFunc_90005501(
        0,
        flag=34110510,
        flag_1=34111510,
        left=1,
        asset=Assets.AEG027_061_0501,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=34110511,
    )
    CommonFunc_90005501(
        0,
        flag=34110515,
        flag_1=34111515,
        left=0,
        asset=Assets.AEG027_061_0500,
        asset_1=Assets.AEG027_002_0502,
        asset_2=Assets.AEG027_002_0503,
        flag_2=34110516,
    )
    CommonFunc_90005501(
        0,
        flag=34110520,
        flag_1=34111520,
        left=0,
        asset=Assets.AEG027_058_5500,
        asset_1=34111521,
        asset_2=34111522,
        flag_2=34110521,
    )
    CommonFunc_90005508(
        0,
        flag=34110525,
        flag_1=34111525,
        left=0,
        entity=Assets.AEG027_070_0500,
        asset=Assets.AEG027_203_0501,
        asset_1=Assets.AEG027_203_0500,
        flag_2=34110526,
    )
    Event_34112510()
    Event_34112580()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9004, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005300(
        0,
        flag=34110280,
        character=Characters.GodskinNoble,
        item_lot=34110400,
        seconds=0.0,
        left=0,
    )
    Event_34112400()
    Event_34112410()
    Event_34112420()
    Event_34112430()
    Event_34112440(0, region=34112440, region_1=34112450)
    Event_34112440(1, region=34112441, region_1=34112451)
    Event_34112440(2, region=34112442, region_1=34112452)
    Event_34112440(3, region=34112443, region_1=34112453)
    Event_34112440(4, region=34112444, region_1=34112454)
    Event_34112440(5, region=34112445, region_1=34112455)
    Event_34112440(6, region=34112446, region_1=34112456)
    Event_34112440(7, region=34112447, region_1=34112457)
    Event_34112448()
    Event_34112449()
    Event_34112459()
    CommonFunc_90005300(
        0,
        flag=34110710,
        character=Characters.PreceptorMiriam0,
        item_lot=34110700,
        seconds=0.0,
        left=0,
    )
    Event_34112460()
    Event_34112465()
    CommonFunc_90005300(
        0,
        flag=34110711,
        character=Characters.PreceptorMiriam1,
        item_lot=34110710,
        seconds=0.0,
        left=0,
    )
    Event_34112475(0, flag=34112485, character=Characters.PreceptorMiriam0, region=34112411)
    Event_34112475(1, flag=34112486, character=Characters.PreceptorMiriam0, region=34112421)
    Event_34112475(2, flag=34112487, character=Characters.PreceptorMiriam0, region=34112431)
    Event_34112475(3, flag=34112488, character=Characters.PreceptorMiriam1, region=34112466)
    CommonFunc_90005706(0, 34110700, 930023, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_34112150()
    Event_34112151()
    DisableBackread(Characters.WanderingNoble24)
    Event_34112519()
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper0, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper1, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper2, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper3, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper4, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper5, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper6, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper7, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper8, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper9, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.LesserFingercreeper10, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper11, region=34112230, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper12, region=34112230, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper13, region=34112230, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper14, region=34112235, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper15, region=34112235, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper16, region=34112235, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper17, region=34112465, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper18, region=34112465, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper19, region=34112245, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper20, region=34112245, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LesserFingercreeper21, region=34112245, seconds=0.0, animation_id=-1)
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble0,
        animation_id=30004,
        animation_id_1=20004,
        region=34112200,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble1,
        animation_id=30004,
        animation_id_1=20004,
        region=34112200,
        radius=5.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble2,
        animation_id=30004,
        animation_id_1=20004,
        region=34112400,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble3,
        animation_id=30004,
        animation_id_1=20004,
        region=34112400,
        radius=15.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble4,
        animation_id=30004,
        animation_id_1=20004,
        region=34112405,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble5,
        animation_id=30004,
        animation_id_1=20004,
        region=34112405,
        radius=20.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble6,
        animation_id=30004,
        animation_id_1=20004,
        region=34112405,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble7,
        animation_id=30004,
        animation_id_1=20004,
        region=34112405,
        radius=20.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble8,
        animation_id=30004,
        animation_id_1=20004,
        region=34112405,
        radius=30.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble9,
        animation_id=30004,
        animation_id_1=20004,
        region=34112409,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble10,
        animation_id=30004,
        animation_id_1=20004,
        region=34112410,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble11,
        animation_id=30004,
        animation_id_1=20004,
        region=34112410,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble12,
        animation_id=30004,
        animation_id_1=20004,
        region=34112410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble13,
        animation_id=30004,
        animation_id_1=20004,
        region=34112441,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble14,
        animation_id=30004,
        animation_id_1=20004,
        region=34112441,
        radius=15.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble15,
        animation_id=30004,
        animation_id_1=20004,
        region=34112441,
        radius=15.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble16,
        animation_id=30004,
        animation_id_1=20004,
        region=34112442,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble17,
        animation_id=30004,
        animation_id_1=20004,
        region=34112443,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.WanderingNoble18,
        animation_id=30004,
        animation_id_1=20004,
        region=34112443,
        radius=20.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble19,
        animation_id=30004,
        animation_id_1=20004,
        region=34112445,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble20,
        animation_id=30004,
        animation_id_1=20004,
        region=34112445,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble21,
        animation_id=30004,
        animation_id_1=20004,
        region=34112445,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble22,
        animation_id=30004,
        animation_id_1=20004,
        region=34112445,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WanderingNoble23,
        animation_id=30004,
        animation_id_1=20004,
        region=34112445,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RayaLucariaSoldier0,
        animation_id=30006,
        animation_id_1=20006,
        region=34112465,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.RayaLucariaSoldier1,
        animation_id=30006,
        animation_id_1=20006,
        region=34112475,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 34110452, 30006, 20006, 34112475, 0.0, 0, 0, 0, 0)


@RestartOnRest(34112150)
def Event_34112150():
    """Event 34112150"""
    GotoIfFlagEnabled(Label.L0, flag=370)
    EnableCharacter(34115150)
    EnableAnimations(34115150)
    DisableCharacter(34115160)
    DisableAnimations(34115160)
    EnableAsset(34116150)
    DisableAsset(34116160)
    EnableMapCollision(collision=34114150)
    EnableMapCollision(collision=34114151)
    EnableMapCollision(collision=34114152)
    EnableMapCollision(collision=34114153)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9720, entity=Assets.AEG099_090_9000))
    
    MAIN.Await(AND_1)
    
    AND_9.Add(PlayerInOwnWorld())
    AND_9.Add(PlayerHasGood(8111))
    GotoIfConditionTrue(Label.L1, input_condition=AND_9)
    Wait(0.10000000149011612)
    if PlayerInOwnWorld():
        DisplayDialog(text=20040, anchor_entity=Assets.AEG099_090_9000, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(370)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutscene(34110000, cutscene_flags=0, player_id=10000)
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=34110000,
            cutscene_flags=0,
            move_to_region=34112505,
            map_id=34110000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(asset=Assets.AEG022_214_3000, animation_id=1)
    RemoveGoodFromPlayer(item=8111, quantity=1)
    DisableCharacter(34115150)
    DisableAnimations(34115150)
    EnableCharacter(34115160)
    EnableAnimations(34115160)
    DisableAsset(34116150)
    EnableAsset(34116160)
    DisableMapCollision(collision=34114150)
    DisableMapCollision(collision=34114151)
    DisableMapCollision(collision=34114152)
    DisableMapCollision(collision=34114153)
    if FlagEnabled(34110510):
        DisableAssetActivation(Assets.AEG027_002_0501, obj_act_id=27002)
    if FlagEnabled(34110510):
        ForceAnimation(Assets.AEG027_061_5500, 10)
    if FlagEnabled(34110515):
        ForceAnimation(34111615, 10)
    WaitFrames(frames=1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(34115150)
    DisableAnimations(34115150)
    EnableCharacter(34115160)
    EnableAnimations(34115160)
    DisableAsset(34116150)
    EnableAsset(34116160)
    DisableMapCollision(collision=34114150)
    DisableMapCollision(collision=34114151)
    DisableMapCollision(collision=34114152)
    DisableMapCollision(collision=34114153)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9721, entity=Assets.AEG099_090_9000))
    
    MAIN.Await(AND_1)
    
    DisableNetworkFlag(370)
    EnableAsset(34116150)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutscene(34110001, cutscene_flags=0, player_id=10000)
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=34110001,
            cutscene_flags=0,
            move_to_region=34112505,
            map_id=34110000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    EndOfAnimation(asset=Assets.AEG022_214_3000, animation_id=0)
    EnableFlag(34112155)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=8111, flag=34112155, bit_count=1)
    EnableCharacter(34115150)
    EnableAnimations(34115150)
    DisableCharacter(34115160)
    DisableAnimations(34115160)
    EnableAsset(34116150)
    DisableAsset(34116160)
    EnableMapCollision(collision=34114150)
    EnableMapCollision(collision=34114151)
    EnableMapCollision(collision=34114152)
    EnableMapCollision(collision=34114153)
    if FlagEnabled(34110510):
        EnableAssetActivation(Assets.AEG027_002_0501, obj_act_id=27002)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(34112151)
def Event_34112151():
    """Event 34112151"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9730, entity=Assets.AEG099_090_9001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=34110010,
            cutscene_flags=0,
            move_to_region=34112160,
            map_id=34110000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=34110010,
            cutscene_flags=0,
            move_to_region=34112160,
            map_id=34110000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    WaitFramesAfterCutscene(frames=1)
    SetCameraAngle(x_angle=-0.23999999463558197, y_angle=-104.94999694824219)
    EnableFlag(34110520)
    Restart()


@RestartOnRest(34112152)
def Event_34112152():
    """Event 34112152"""
    MAIN.Await(FlagDisabled(34110520))
    
    EndOfAnimation(asset=Assets.AEG027_058_5500, animation_id=10)


@ContinueOnRest(34112510)
def Event_34112510():
    """Event 34112510"""
    Event_34112900(
        0,
        flag=34110510,
        flag_1=34111510,
        left=1,
        asset=Assets.AEG027_061_0501,
        asset_1=Assets.AEG027_002_0500,
        obj_act_id=34113511,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=34113512,
        region=34112511,
        region_1=34112512,
        flag_2=34110511,
        flag_3=34112512,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=34110515,
        flag_1=34111515,
        left=0,
        asset=Assets.AEG027_061_0500,
        asset_1=Assets.AEG027_002_0502,
        obj_act_id=34113516,
        asset_2=Assets.AEG027_002_0503,
        obj_act_id_1=34113517,
        region=34112516,
        region_1=34112517,
        flag_2=34110516,
        flag_3=34112517,
        left_1=0,
    )
    Event_34112910(
        0,
        flag=34110520,
        flag_1=34111520,
        left=0,
        asset=Assets.AEG027_058_5500,
        asset_1=0,
        obj_act_id=0,
        asset_2=0,
        obj_act_id_1=0,
        region=34112521,
        region_1=34112522,
        flag_2=34110521,
        flag_3=0,
        left_1=0,
    )
    CommonFunc_90005507(
        0,
        34110525,
        34111525,
        0,
        34111525,
        34111526,
        34112528,
        34111527,
        34112529,
        34112526,
        34112527,
        34110526,
        34112527,
        0,
    )


@ContinueOnRest(34112519)
def Event_34112519():
    """Event 34112519"""
    if ThisEventSlotFlagEnabled():
        return
    if CharacterInsideRegion(character=PLAYER, region=34112152):
        return
    EnableFlag(34110520)
    DisableThisSlotFlag()


@RestartOnRest(34112580)
def Event_34112580():
    """Event 34112580"""
    RegisterLadder(start_climbing_flag=34110530, stop_climbing_flag=34110531, asset=Assets.AEG027_222_0500)
    RegisterLadder(start_climbing_flag=34110532, stop_climbing_flag=34110533, asset=Assets.AEG027_221_0500)


@ContinueOnRest(34112900)
def Event_34112900(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    asset: uint,
    asset_1: uint,
    obj_act_id: uint,
    asset_2: uint,
    obj_act_id_1: uint,
    region: uint,
    region_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 34112900"""
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfPlayerNotInOwnWorld(5)
    SkipLinesIfFlagDisabled(2, 370)
    DisableAssetActivation(asset_2, obj_act_id=-1)
    SkipLines(1)
    EnableAssetActivation(asset_2, obj_act_id=-1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(FlagDisabled(flag))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(AND_3)
    AND_11.Add(OR_4)
    AND_11.Add(FlagDisabled(370))
    
    MAIN.Await(AND_11)
    
    if PlayerInOwnWorld():
        DisableAssetActivation(asset_2, obj_act_id=-1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_2)
        DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(asset_2, 3, skip_transition=True)
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_10.Add(AllPlayersOutsideRegion(region=region_1))
    OR_10.Add(FlagEnabled(flag))
    AND_10.Add(AssetBackreadEnabled(asset=asset))
    AND_10.Add(OR_10)
    
    MAIN.Await(AND_10)
    
    GotoIfPlayerNotInOwnWorld(Label.L3)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableAssetActivation(asset_1, obj_act_id=-1)
        DisableAssetActivation(asset_2, obj_act_id=-1)
    OR_5.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagEnabled(flag))
    AND_7.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(AND_7)
    AND_12.Add(OR_8)
    AND_12.Add(FlagDisabled(370))
    
    MAIN.Await(AND_12)
    
    if PlayerInOwnWorld():
        DisableAssetActivation(asset_1, obj_act_id=-1)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_2)
        EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(asset_1, 3, skip_transition=True)
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    OR_11.Add(AllPlayersOutsideRegion(region=region))
    OR_11.Add(FlagDisabled(flag))
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    AND_2.Add(OR_11)
    
    MAIN.Await(AND_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L6)
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@ContinueOnRest(34112910)
def Event_34112910(
    _,
    flag: uint,
    flag_1: uint,
    left: uint,
    asset: uint,
    asset_1: uint,
    obj_act_id: uint,
    asset_2: uint,
    obj_act_id_1: uint,
    region: uint,
    region_1: uint,
    flag_2: uint,
    flag_3: uint,
    left_1: uint,
):
    """Event 34112910"""
    if CharacterInsideRegion(character=PLAYER, region=34112152):
        return
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableAssetActivation(asset_2, obj_act_id=-1)
    DisableAssetActivation(asset_1, obj_act_id=-1)
    OR_1.Add(AssetActivated(obj_act_id=obj_act_id_1))
    OR_2.Add(FlagDisabled(flag))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_3.Add(FlagEnabled(left_1))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableAssetActivation(asset_2, obj_act_id=-1)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag)
    DisableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 21, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 1000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 2000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 3000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 4000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 5000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 6000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 7000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 8000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 9000021, wait_for_completion=True, skip_transition=True)
    Goto(Label.L11)
    ForceAnimation(asset, 10000021, wait_for_completion=True, skip_transition=True)

    # --- Label 11 --- #
    DefineLabel(11)
    ForceAnimation(asset_2, 3, skip_transition=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag_3)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_10.Add(AllPlayersOutsideRegion(region=region_1))
    OR_10.Add(FlagEnabled(flag))
    AND_1.Add(AssetBackreadEnabled(asset=asset))
    AND_1.Add(OR_10)
    
    MAIN.Await(AND_1)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L3, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, skip_transition=True)
    Goto(Label.L12)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 1000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 2000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 3000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 4000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 5000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 6000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 7000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 8000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 9000110, wait_for_completion=True, skip_transition=True)
    Goto(Label.L12)
    ForceAnimation(asset, 10000110, wait_for_completion=True, skip_transition=True)

    # --- Label 12 --- #
    DefineLabel(12)
    SaveRequest()
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableAssetActivation(asset_1, obj_act_id=-1)
    DisableAssetActivation(asset_2, obj_act_id=-1)
    OR_5.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_6.Add(FlagEnabled(flag))
    AND_7.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4800))
    if UnsignedNotEqual(left=left_1, right=0):
        AND_7.Add(FlagEnabled(left_1))
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    OR_8.Add(AND_7)
    
    MAIN.Await(OR_8)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableAssetActivation(asset_1, obj_act_id=-1)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag_2)
    EnableNetworkFlag(flag)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=OR_5)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag_3)
    Wait(2.0)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 12, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 1000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 2000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 3000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 4000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 5000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 6000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 7000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 8000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 9000012, wait_for_completion=True, skip_transition=True)
    Goto(Label.L14)
    ForceAnimation(asset, 10000012, wait_for_completion=True, skip_transition=True)

    # --- Label 14 --- #
    DefineLabel(14)
    ForceAnimation(asset_1, 3, skip_transition=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag_3)

    # --- Label 5 --- #
    DefineLabel(5)
    OR_11.Add(AllPlayersOutsideRegion(region=region))
    OR_11.Add(FlagDisabled(flag))
    AND_2.Add(AssetBackreadEnabled(asset=asset))
    AND_2.Add(OR_11)
    
    MAIN.Await(AND_2)
    
    GotoIfMapDoesNotHaveUpdatePermission(Label.L6, unk_state=False, game_map=(0, 0, 0, 0))
    DisableNetworkFlag(flag_2)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, skip_transition=True)
    Goto(Label.L15)

    # --- Label 6 --- #
    DefineLabel(6)
    SkipLinesIfUnsignedEqual(29, left=left, right=10)
    SkipLinesIfUnsignedEqual(26, left=left, right=9)
    SkipLinesIfUnsignedEqual(23, left=left, right=8)
    SkipLinesIfUnsignedEqual(20, left=left, right=7)
    SkipLinesIfUnsignedEqual(17, left=left, right=6)
    SkipLinesIfUnsignedEqual(14, left=left, right=5)
    SkipLinesIfUnsignedEqual(11, left=left, right=4)
    SkipLinesIfUnsignedEqual(8, left=left, right=3)
    SkipLinesIfUnsignedEqual(5, left=left, right=2)
    SkipLinesIfUnsignedEqual(2, left=left, right=1)
    ForceAnimation(asset, 120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 1000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 2000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 3000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 4000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 5000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 6000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 7000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 8000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 9000120, wait_for_completion=True, skip_transition=True)
    Goto(Label.L15)
    ForceAnimation(asset, 10000120, wait_for_completion=True, skip_transition=True)

    # --- Label 15 --- #
    DefineLabel(15)
    SaveRequest()
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Restart()


@RestartOnRest(34112400)
def Event_34112400():
    """Event 34112400"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(Characters.PreceptorMiriam0)
    DisableAnimations(Characters.PreceptorMiriam0)
    SetCharacterFadeOnEnable(character=Characters.PreceptorMiriam0, state=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34112400))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    EnableCharacter(Characters.PreceptorMiriam0)
    EnableAnimations(Characters.PreceptorMiriam0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112410)
def Event_34112410():
    """Event 34112410"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    SetCharacterFadeOnEnable(character=Characters.PreceptorMiriam0, state=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(Characters.PreceptorMiriam0) <= 0.800000011920929)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.PreceptorMiriam0, 19385))
    AND_1.Add(HealthValue(Characters.PreceptorMiriam0) > 0)
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    AddSpecialEffect(Characters.PreceptorMiriam0, 4240)
    Wait(0.5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.PreceptorMiriam0,
        special_effect=19385,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    EnableNetworkFlag(34112485)
    End()
    Move(
        Characters.PreceptorMiriam0,
        destination=34112411,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam0,
    )
    SetNest(Characters.PreceptorMiriam0, region=34112411)
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    AddSpecialEffect(Characters.PreceptorMiriam0, 4241)
    End()


@RestartOnRest(34112420)
def Event_34112420():
    """Event 34112420"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    SetCharacterFadeOnEnable(character=Characters.PreceptorMiriam0, state=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(Characters.PreceptorMiriam0) <= 0.6000000238418579)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.PreceptorMiriam0, 19385))
    AND_1.Add(HealthValue(Characters.PreceptorMiriam0) > 0)
    AND_1.Add(FlagEnabled(34112410))
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    AddSpecialEffect(Characters.PreceptorMiriam0, 4240)
    Wait(0.5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.PreceptorMiriam0,
        special_effect=19385,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    EnableNetworkFlag(34112486)
    End()
    Move(
        Characters.PreceptorMiriam0,
        destination=34112421,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam0,
    )
    SetNest(Characters.PreceptorMiriam0, region=34112421)
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    AddSpecialEffect(Characters.PreceptorMiriam0, 4241)
    End()


@RestartOnRest(34112430)
def Event_34112430():
    """Event 34112430"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    SetCharacterFadeOnEnable(character=Characters.PreceptorMiriam0, state=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(Characters.PreceptorMiriam0) <= 0.4000000059604645)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.PreceptorMiriam0, 19385))
    AND_1.Add(HealthValue(Characters.PreceptorMiriam0) > 0)
    AND_1.Add(FlagEnabled(34112420))
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    AddSpecialEffect(Characters.PreceptorMiriam0, 4240)
    Wait(0.5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.PreceptorMiriam0,
        special_effect=19385,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    EnableNetworkFlag(34112487)
    End()
    Move(
        Characters.PreceptorMiriam0,
        destination=34112431,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam0,
    )
    SetNest(Characters.PreceptorMiriam0, region=34112431)
    Wait(1.0)
    ReplanAI(Characters.PreceptorMiriam0)
    Wait(0.10000000149011612)
    DisableAI(Characters.PreceptorMiriam0)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    End()


@RestartOnRest(34112439)
def Event_34112439():
    """Event 34112439"""
    if FlagEnabled(34110710):
        return
    
    MAIN.Await(FlagRangeAllEnabled(flag_range=(34112440, 34112447)))
    
    DisableCharacter(Characters.PreceptorMiriam0)


@RestartOnRest(34112440)
def Event_34112440(_, region: uint, region_1: uint):
    """Event 34112440"""
    if FlagEnabled(34110710):
        return
    if FlagEnabled(34112448):
        return
    if FlagEnabled(34112459):
        return
    SetCharacterFadeOnEnable(character=Characters.PreceptorMiriam0, state=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagEnabled(34112410))
    AND_1.Add(FlagEnabled(34112420))
    AND_1.Add(FlagEnabled(34112430))
    AND_1.Add(FlagDisabled(34112448))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.PreceptorMiriam0, 19385))
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    if FlagEnabled(34112459):
        return
    AddSpecialEffect(Characters.PreceptorMiriam0, 4240)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam0,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=2,
        character=Characters.PreceptorMiriam0,
        special_effect=19385,
    )
    AddSpecialEffect(Characters.PreceptorMiriam0, 4241)
    Restart()
    Move(
        Characters.PreceptorMiriam0,
        destination=region_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam0,
    )
    SetNest(Characters.PreceptorMiriam0, region=region_1)
    AddSpecialEffect(Characters.PreceptorMiriam0, 4241)
    Wait(4.0)
    Restart()


@RestartOnRest(34112448)
def Event_34112448():
    """Event 34112448"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34112448))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(Characters.PreceptorMiriam0)
    AddSpecialEffect(Characters.PreceptorMiriam0, 8082)
    DisableThisSlotFlag()


@RestartOnRest(34112449)
def Event_34112449():
    """Event 34112449"""
    if FlagEnabled(34110710):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34112449))
    AND_1.Add(FlagEnabled(34112410))
    AND_1.Add(FlagEnabled(34112420))
    AND_1.Add(FlagEnabled(34112430))
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam0, lock_on_model_point=220, state=True)
    EnableAI(Characters.PreceptorMiriam0)
    SetAIParamID(Characters.PreceptorMiriam0, ai_param_id=523520200)
    DisableThisSlotFlag()


@RestartOnRest(34112459)
def Event_34112459():
    """Event 34112459"""
    if FlagEnabled(34110710):
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=Characters.PreceptorMiriam0, attacker=PLAYER))
    AND_1.Add(FlagEnabled(34112410))
    AND_1.Add(FlagEnabled(34112420))
    AND_1.Add(FlagEnabled(34112430))
    
    MAIN.Await(AND_1)
    
    DisableThisSlotFlag()


@RestartOnRest(34112460)
def Event_34112460():
    """Event 34112460"""
    if FlagEnabled(34110711):
        return
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(Characters.PreceptorMiriam1)
    DisableAnimations(Characters.PreceptorMiriam1)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34112460))
    AND_1.Add(FlagEnabled(370))
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    EnableCharacter(Characters.PreceptorMiriam1)
    EnableAnimations(Characters.PreceptorMiriam1)
    DisableThisSlotFlag()


@RestartOnRest(34112465)
def Event_34112465():
    """Event 34112465"""
    if FlagEnabled(34110711):
        return
    if FlagEnabled(34112496):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(Characters.PreceptorMiriam1) <= 0.30000001192092896)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.PreceptorMiriam0, 19385))
    AND_1.Add(HealthValue(Characters.PreceptorMiriam1) > 0)
    AND_1.Add(FlagDisabled(34112496))
    
    MAIN.Await(AND_1)
    
    OR_15.Add(HealthValue(Characters.PreceptorMiriam1) == 0)
    if OR_15:
        return
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=150,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=152,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=153,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=154,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=155,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=156,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600920,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=157,
        anchor_type=CoordEntityType.Character,
    )
    CreateTemporaryVFX(
        vfx_id=600921,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=151,
        anchor_type=CoordEntityType.Character,
    )
    Wait(0.5)
    AddSpecialEffect(Characters.PreceptorMiriam0, 4240)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.PreceptorMiriam1,
        special_effect=19385,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=True)
    EnableNetworkFlag(34112488)
    End()
    Move(
        Characters.PreceptorMiriam1,
        destination=34112466,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam1,
    )
    SetNest(Characters.PreceptorMiriam1, region=34112466)
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()
    AddSpecialEffect(Characters.PreceptorMiriam0, 4241)


@RestartOnRest(34112475)
def Event_34112475(_, flag: uint, character: uint, region: uint):
    """Event 34112475"""
    if FlagEnabled(character):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 19385))
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    AddSpecialEffect(character, 4240)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=150, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=151, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=152, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=153, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=154, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=155, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=156, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600920, anchor_entity=character, model_point=157, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=600921, anchor_entity=character, model_point=151, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    OR_15.Add(HealthValue(character) == 0)
    if OR_15:
        return
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    SetNest(character, region=region)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    AddSpecialEffect(character, 4241)


@RestartOnRest(34112492)
def Event_34112492():
    """Event 34112492"""
    OR_1.Add(FlagEnabled(34110711))
    OR_1.Add(ThisEventSlotFlagEnabled())
    if OR_1:
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=34112482))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=34112483))
    
    MAIN.Await(OR_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=806910,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=220,
        anchor_type=CoordEntityType.Character,
    )
    Move(
        Characters.PreceptorMiriam1,
        destination=34112492,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam1,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112493)
def Event_34112493():
    """Event 34112493"""
    OR_1.Add(FlagEnabled(34110711))
    OR_1.Add(ThisEventSlotFlagEnabled())
    if OR_1:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=34112490))
    
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=806910,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=220,
        anchor_type=CoordEntityType.Character,
    )
    Move(
        Characters.PreceptorMiriam1,
        destination=34112493,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam1,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112496)
def Event_34112496():
    """Event 34112496"""
    if FlagEnabled(34110711):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=34112482))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=34112483))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=False)
    Wait(1.0)
    CreateTemporaryVFX(
        vfx_id=806910,
        anchor_entity=Characters.PreceptorMiriam1,
        model_point=220,
        anchor_type=CoordEntityType.Character,
    )
    Move(
        Characters.PreceptorMiriam1,
        destination=34112496,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.PreceptorMiriam1,
    )
    SetLockOnPoint(character=Characters.PreceptorMiriam1, lock_on_model_point=220, state=True)
    DisableThisSlotFlag()


@RestartOnRest(34112499)
def Event_34112499():
    """Event 34112499"""
    AddSpecialEffect(Characters.PreceptorMiriam0, 8090)
    AddSpecialEffect(Characters.PreceptorMiriam1, 8090)
    AddSpecialEffect(34110712, 8090)


@RestartOnRest(34112690)
def Event_34112690():
    """Event 34112690"""
    DisableNetworkSync()
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=34112690)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=34112691)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(WeatherState(weather=Weather.RainyClouds, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    SetWeather(weather=Weather.RainyClouds, duration=-1.0, immediate_change=False)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(WeatherState(weather=Weather.HeavyFog, unk_4_8=0.0, unk_8_12=0.0))
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    SetWeather(weather=Weather.HeavyFog, duration=-1.0, immediate_change=False)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(34112800)
def Event_34112800():
    """Event 34112800"""
    if FlagEnabled(34110800):
        return
    
    MAIN.Await(HealthValue(34110800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(34110800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(34110800))
    
    KillBossAndDisplayBanner(character=34110800, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(34110800)


@RestartOnRest(34112810)
def Event_34112810():
    """Event 34112810"""
    GotoIfFlagDisabled(Label.L0, flag=34110800)
    DisableCharacter(34110800)
    DisableAnimations(34110800)
    Kill(34110800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34110800)
    DisableAnimations(34110800)
    AND_1.Add(FlagEnabled(34112805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=34112800))
    OR_1.Add(AttackedWithDamageType(attacked_entity=34110800, attacker=PLAYER))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(34110800)
    EnableAnimations(34110800)
    SetNetworkUpdateRate(34110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34110800)


@RestartOnRest(34112849)
def Event_34112849():
    """Event 34112849"""
    CommonFunc_9005800(
        0,
        flag=34110800,
        entity=34111800,
        region=34112800,
        flag_1=34112805,
        character=34115800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=34110800,
        entity=34111800,
        region=34112800,
        flag_1=34112805,
        flag_2=34112806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=34110800, asset=34111800, model_point=3, right=0)
    CommonFunc_9005822(0, 34110800, 930000, 34112805, 34112806, 0, 34112802, 0, 0)
