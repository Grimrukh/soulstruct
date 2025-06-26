"""
Land of Shadow 12-10 SW NW

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005301(0, flag=2048410300, character=2048410300, item_lot__unk1=2048410980, seconds=0.0, unk1=0)
    CommonFunc_90005211(
        0,
        character=2048410204,
        animation_id=30001,
        animation_id_1=20001,
        region=2048412204,
        radius=10.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048410205,
        animation_id=30001,
        animation_id_1=20001,
        region=2048412204,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048410207,
        animation_id=30001,
        animation_id_1=20001,
        region=2048412204,
        radius=10.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005271(0, character=2048410252, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=2048410254, seconds=0.0, animation_id=-1)
    Event_2048412256(0, character=2048410256, region=2048412256)
    Event_2048412256(1, character=2048410257, region=2048412256)
    Event_2048412250(0, character=2048410250)
    Event_2048412250(1, character=2048410251)
    Event_2048412250(2, character=2048410255)
    Event_2048412510()
    CommonFunc_90005501(
        0,
        flag=2048410510,
        flag_1=2048410511,
        left=0,
        asset=2048411510,
        asset_1=2048411511,
        asset_2=2048411512,
        flag_2=2048410512,
    )
    Event_61482920(0, asset=61481920, asset_1=61481921)
    Event_2048412500()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_2048410519()


@ContinueOnRest(2048412510)
def Event_2048412510():
    """Event 2048412510"""
    CommonFunc_90005500(
        0,
        flag=2048410510,
        flag_1=2048410511,
        left=0,
        asset=2048411510,
        asset_1=2048411511,
        obj_act_id=2048413511,
        asset_2=2048411512,
        obj_act_id_1=2048413512,
        region=2048412511,
        region_1=2048412512,
        flag_2=2048410512,
        flag_3=2048410513,
        left_1=0,
    )


@ContinueOnRest(2048410519)
def Event_2048410519():
    """Event 2048410519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableThisSlotFlag()


@RestartOnRest(61482920)
def Event_61482920(_, asset: uint, asset_1: uint):
    """Event 61482920"""
    DeleteAssetVFX(asset)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset, dummy_id=90, vfx_id=6100)
    CreateAssetVFX(asset_1, dummy_id=90, vfx_id=6100)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9000, entity=asset))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9000, entity=asset_1))
    OR_9.Add(AND_1)
    OR_9.Add(AND_2)
    
    MAIN.Await(OR_9)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_2)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Asset,
        destination=asset_1,
        dummy_id=100,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Asset,
        destination=asset,
        dummy_id=100,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(1.0)
    Restart()


@ContinueOnRest(2048412500)
def Event_2048412500():
    """Event 2048412500"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209529, entity=2048411500))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=2062000, anchor_entity=2048411500, button_type=ButtonType.Yes_or_No)
    Wait(3.0)
    Restart()


@RestartOnRest(2048412250)
def Event_2048412250(_, character: Character | int):
    """Event 2048412250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(CharacterHasSpecialEffect(character, 20010336))
    
    MAIN.Await(OR_2)
    
    EnableAI(character)


@RestartOnRest(2048412256)
def Event_2048412256(_, character: Character | int, region: Region | int):
    """Event 2048412256"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(OR_2)
    
    EnableAI(character)
