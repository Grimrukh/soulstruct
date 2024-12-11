"""
Bridge to Rauh Ruins

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
    RegisterGrace(grace_flag=21020001, asset=21021951, enemy_block_distance=0.0)
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=72120,
        asset=21021981,
        source_flag=77900,
        value=1,
        flag_2=78900,
        flag_3=78901,
        flag_4=78902,
        flag_5=78903,
        flag_6=78904,
        flag_7=78905,
        flag_8=78906,
        flag_9=78907,
        flag_10=78908,
        flag_11=78909,
        flag_12=9146,
    )
    Event_21022450()
    CommonFunc_90005501(
        0,
        flag=21020510,
        flag_1=21020511,
        left=0,
        asset=21021510,
        asset_1=21021511,
        asset_2=21021512,
        flag_2=21020512,
    )
    Event_21022510()
    CommonFunc_90005525(0, flag=21020570, asset=21021570)
    CommonFunc_90005511(0, flag=21020560, asset=21021560, obj_act_id=21023560, obj_act_id_1=427036, left=0)
    CommonFunc_900005610(0, asset=21020490, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=21020491, dummy_id=100, vfx_id=800, right=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005301(0, flag=21020450, character=21020450, item_lot__unk1=21021991, seconds=0.0, unk1=2)
    CommonFunc_90005261(0, character=21020202, region=21022202, radius=1.0, seconds=0.0, animation_id=3009)
    CommonFunc_90005261(0, character=21020204, region=21022204, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005445(
        0,
        character=21020207,
        animation_id=30004,
        animation_id_1=20004,
        region=21022207,
        seconds=1.7999999523162842,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
        asset=21021207,
    )
    CommonFunc_90005211(
        0,
        character=21020209,
        animation_id=30000,
        animation_id_1=20000,
        region=21022209,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21020215, region=21022215, radius=1.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(
        0,
        character=21020230,
        region=21022230,
        radius=1.0,
        seconds=0.10000000149011612,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=21020250,
        animation_id=30000,
        animation_id_1=20000,
        region=21022230,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020251,
        animation_id=30000,
        animation_id_1=20000,
        region=21022230,
        radius=1.0,
        seconds=1.100000023841858,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020252,
        animation_id=30000,
        animation_id_1=20000,
        region=21022230,
        radius=1.0,
        seconds=5.099999904632568,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020253,
        animation_id=30000,
        animation_id_1=20000,
        region=21022230,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020256,
        animation_id=30000,
        animation_id_1=20000,
        region=21022256,
        radius=1.0,
        seconds=1.100000023841858,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020257,
        animation_id=30000,
        animation_id_1=20000,
        region=21022256,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020258,
        animation_id=30000,
        animation_id_1=20000,
        region=21022258,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21020259,
        animation_id=30000,
        animation_id_1=20000,
        region=21022258,
        radius=1.0,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21020270, region=21022270, radius=1.0, seconds=0.0, animation_id=3004)
    CommonFunc_90005261(0, character=21020450, region=21022450, radius=1.0, seconds=0.0, animation_id=0)


@ContinueOnRest(21020050)
def Event_21020050():
    """Event 21020050"""
    if ThisEventSlotFlagEnabled():
        return


@RestartOnRest(21022450)
def Event_21022450():
    """Event 21022450"""
    AND_1.Add(CharacterDead(21020450))
    if AND_1:
        return
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21022450))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 20011739)
    Wait(2.5)
    Restart()


@ContinueOnRest(21022510)
def Event_21022510():
    """Event 21022510"""
    CommonFunc_90005500(
        0,
        flag=21020510,
        flag_1=21020511,
        left=0,
        asset=21021510,
        asset_1=21021511,
        obj_act_id=21023511,
        asset_2=21021512,
        obj_act_id_1=21023512,
        region=21022511,
        region_1=21022512,
        flag_2=21020512,
        flag_3=21020513,
        left_1=0,
    )


@RestartOnRest(21022920)
def Event_21022920(_, asset: uint, asset_1: uint):
    """Event 21022920"""
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
