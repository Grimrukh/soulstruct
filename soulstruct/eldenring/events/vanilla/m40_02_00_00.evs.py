"""
m40_02_00_00

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
    CommonFunc_900005610(0, asset=40021500, dummy_id=100, vfx_id=800, right=0)
    RegisterGrace(grace_flag=40020000, asset=40021950)
    Event_2052432845()
    Event_40022580()
    CommonFunc_90005501(
        0,
        flag=40020510,
        flag_1=40020511,
        left=3,
        asset=40021510,
        asset_1=40021511,
        asset_2=40021512,
        flag_2=40020512,
    )
    CommonFunc_90005501(
        0,
        flag=40020515,
        flag_1=40020516,
        left=4,
        asset=40021515,
        asset_1=40021516,
        asset_2=40021517,
        flag_2=40020517,
    )
    CommonFunc_90005501(
        0,
        flag=40020520,
        flag_1=40020521,
        left=4,
        asset=40021520,
        asset_1=40021521,
        asset_2=40021522,
        flag_2=40020522,
    )
    CommonFunc_90005501(
        0,
        flag=40020525,
        flag_1=40020526,
        left=5,
        asset=40021525,
        asset_1=40021526,
        asset_2=40021527,
        flag_2=40020527,
    )
    Event_40022510()
    Event_40022610(
        0,
        flag=40020600,
        asset=40021601,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        1,
        flag=40020600,
        asset=40021602,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        2,
        flag=40020600,
        asset=40021603,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        3,
        flag=40020600,
        asset=40021604,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        4,
        flag=40020600,
        asset=40021605,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        5,
        flag=40020600,
        asset=40021606,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        6,
        flag=40020600,
        asset=40021607,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        7,
        flag=40020600,
        asset=40021608,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        8,
        flag=40020600,
        asset=40021609,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        9,
        flag=40020600,
        asset=40021610,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        10,
        flag=40020600,
        asset=40021611,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        11,
        flag=40020600,
        asset=40021612,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        12,
        flag=40020600,
        asset=40021613,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        13,
        flag=40020600,
        asset=40021614,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        14,
        flag=40020600,
        asset=40021615,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        15,
        flag=40020600,
        asset=40021616,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        16,
        flag=40020600,
        asset=40021617,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        17,
        flag=40020600,
        asset=40021618,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        18,
        flag=40020600,
        asset=40021619,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        19,
        flag=40020600,
        asset=40021620,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        20,
        flag=40020600,
        asset=40021621,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        21,
        flag=40020600,
        asset=40021622,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        22,
        flag=40020600,
        asset=40021623,
        asset_1=40021600,
        obj_act_id=40023600,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        23,
        flag=40020630,
        asset=40021631,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        24,
        flag=40020630,
        asset=40021632,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        25,
        flag=40020630,
        asset=40021633,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        26,
        flag=40020630,
        asset=40021634,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        27,
        flag=40020630,
        asset=40021635,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        28,
        flag=40020630,
        asset=40021636,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        29,
        flag=40020630,
        asset=40021637,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        30,
        flag=40020630,
        asset=40021638,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        31,
        flag=40020630,
        asset=40021639,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        32,
        flag=40020630,
        asset=40021640,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        33,
        flag=40020630,
        asset=40021641,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        34,
        flag=40020630,
        asset=40021642,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        35,
        flag=40020630,
        asset=40021643,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        36,
        flag=40020630,
        asset=40021644,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        37,
        flag=40020630,
        asset=40021645,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        38,
        flag=40020630,
        asset=40021646,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        39,
        flag=40020630,
        asset=40021647,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        40,
        flag=40020630,
        asset=40021648,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        41,
        flag=40020630,
        asset=40021649,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        42,
        flag=40020630,
        asset=40021650,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        43,
        flag=40020630,
        asset=40021651,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        44,
        flag=40020630,
        asset=40021652,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        45,
        flag=40020630,
        asset=40021653,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        46,
        flag=40020630,
        asset=40021654,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        47,
        flag=40020630,
        asset=40021655,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        48,
        flag=40020630,
        asset=40021656,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        49,
        flag=40020630,
        asset=40021657,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        50,
        flag=40020630,
        asset=40021658,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        51,
        flag=40020630,
        asset=40021659,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        52,
        flag=40020630,
        asset=40021660,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        53,
        flag=40020630,
        asset=40021661,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        54,
        flag=40020630,
        asset=40021662,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        55,
        flag=40020630,
        asset=40021663,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        56,
        flag=40020630,
        asset=40021664,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        57,
        flag=40020630,
        asset=40021665,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        58,
        flag=40020630,
        asset=40021666,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840015,
    )
    Event_40022610(
        59,
        flag=40020630,
        asset=40021670,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840016,
    )
    Event_40022610(
        60,
        flag=40020630,
        asset=40021671,
        asset_1=40021630,
        obj_act_id=40023630,
        obj_act_id_1=447115,
        vfx_id=840016,
    )
    Event_40022400()
    Event_40022401()
    Event_40022460()
    Event_40022461()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_40020519()
    CommonFunc_90005250(0, character=40020200, region=40022200, seconds=0.0, animation_id=1709)
    CommonFunc_90005201(
        0,
        character=40020205,
        animation_id=30010,
        animation_id_1=20010,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=40020207,
        animation_id=30010,
        animation_id_1=20010,
        radius=50.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=40020208,
        animation_id=30011,
        animation_id_1=20016,
        region=40022208,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=40020213,
        animation_id=30010,
        animation_id_1=20010,
        region=40022213,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=40020216,
        animation_id=30010,
        animation_id_1=20010,
        region=40022216,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=40020300, region=40022300, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=40020220, radius=12.0, seconds=0.5, animation_id=0)
    CommonFunc_90005200(
        0,
        character=40020221,
        animation_id=30002,
        animation_id_1=20002,
        region=40022221,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=40020222,
        animation_id=30001,
        animation_id_1=20001,
        region=40022222,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=40020310, region=40022310, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=40020225, region=40022225, radius=2.0, seconds=0.0, animation_id=1709)
    CommonFunc_90005201(
        0,
        character=40020227,
        animation_id=30010,
        animation_id_1=20010,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=40020317, region=40022317, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=40020290, radius=60.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005200(
        0,
        character=40020244,
        animation_id=30011,
        animation_id_1=20016,
        region=40022244,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    RunCommonEvent(
        400222410,
        slot=0,
        args=(40020240, 30010, 20010, 40022240, 1.0, 0.0, 0, 0, 0, 0, 40020460),
        arg_types="IiiIffIIIII",
    )
    CommonFunc_90005200(
        0,
        character=40020241,
        animation_id=30010,
        animation_id_1=20010,
        region=40022241,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=40020247,
        animation_id=30001,
        animation_id_1=20001,
        region=40022247,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(40022510)
def Event_40022510():
    """Event 40022510"""
    CommonFunc_90005500(
        0,
        flag=40020510,
        flag_1=40020511,
        left=3,
        asset=40021510,
        asset_1=40021511,
        obj_act_id=40023511,
        asset_2=40021512,
        obj_act_id_1=40023512,
        region=40022511,
        region_1=40022512,
        flag_2=40020512,
        flag_3=40020513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=40020515,
        flag_1=40020516,
        left=4,
        asset=40021515,
        asset_1=40021516,
        obj_act_id=40023516,
        asset_2=40021517,
        obj_act_id_1=40023517,
        region=40022516,
        region_1=40022517,
        flag_2=40020517,
        flag_3=40020518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=40020520,
        flag_1=40020521,
        left=4,
        asset=40021520,
        asset_1=40021521,
        obj_act_id=40023521,
        asset_2=40021522,
        obj_act_id_1=40023522,
        region=40022521,
        region_1=40022522,
        flag_2=40020522,
        flag_3=40020523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=40020525,
        flag_1=40020526,
        left=5,
        asset=40021525,
        asset_1=40021526,
        obj_act_id=40023526,
        asset_2=40021527,
        obj_act_id_1=40023527,
        region=40022526,
        region_1=40022527,
        flag_2=40020527,
        flag_3=40020528,
        left_1=0,
    )


@ContinueOnRest(40020519)
def Event_40020519():
    """Event 40020519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(40020510)
    EnableFlag(40020515)
    EnableFlag(40020520)
    EnableFlag(40020525)


@ContinueOnRest(40022580)
def Event_40022580():
    """Event 40022580"""
    RegisterLadder(start_climbing_flag=40020580, stop_climbing_flag=40020581, asset=40021580)
    RegisterLadder(start_climbing_flag=40020582, stop_climbing_flag=40020583, asset=40021582)
    RegisterLadder(start_climbing_flag=40020584, stop_climbing_flag=40020585, asset=40021584)
    RegisterLadder(start_climbing_flag=40020586, stop_climbing_flag=40020587, asset=40021586)
    RegisterLadder(start_climbing_flag=40020588, stop_climbing_flag=40020589, asset=40021588)
    RegisterLadder(start_climbing_flag=40020590, stop_climbing_flag=40020591, asset=40021590)
    RegisterLadder(start_climbing_flag=40020592, stop_climbing_flag=40020593, asset=40021592)
    RegisterLadder(start_climbing_flag=40020594, stop_climbing_flag=40020595, asset=40021594)
    RegisterLadder(start_climbing_flag=40020596, stop_climbing_flag=40020597, asset=40021596)


@RestartOnRest(40022610)
def Event_40022610(
    _,
    flag: Flag | int,
    asset: Asset | int,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    vfx_id: int,
):
    """Event 40022610"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    EnableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=vfx_id)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=vfx_id)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    DisableNetworkFlag(flag)
    EnableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(40022400)
def Event_40022400():
    """Event 40022400"""
    GotoIfFlagEnabled(Label.L0, flag=40020400)
    DeleteAssetVFX(40021401)
    DeleteAssetVFX(40021402)
    DeleteAssetVFX(40021403)
    DeleteAssetVFX(40021404)
    DeleteAssetVFX(40021405)
    DeleteAssetVFX(40021406)
    DeleteAssetVFX(40021407)
    DeleteAssetVFX(40021408)
    DeleteAssetVFX(40021409)
    DeleteAssetVFX(40021410)
    DeleteAssetVFX(40021411)
    DeleteAssetVFX(40021412)
    DeleteAssetVFX(40021413)
    DeleteAssetVFX(40021414)
    DeleteAssetVFX(40021415)
    DeleteAssetVFX(40021416)
    DeleteAssetVFX(40021417)
    DeleteAssetVFX(40021418)
    DeleteAssetVFX(40021419)
    DeleteAssetVFX(40021420)
    DeleteAssetVFX(40021421)
    DeleteAssetVFX(40021422)
    DeleteAssetVFX(40021423)
    DeleteAssetVFX(40021424)
    DeleteAssetVFX(40021425)
    DeleteAssetVFX(40021426)
    DeleteAssetVFX(40021430)
    DeleteAssetVFX(40021431)
    DeleteAssetVFX(40021432)
    DeleteAssetVFX(40021433)
    DeleteAssetVFX(40021434)
    DeleteAssetVFX(40021435)
    DeleteAssetVFX(40021436)
    DeleteAssetVFX(40021437)
    DeleteAssetVFX(40021438)
    DeleteAssetVFX(40021439)
    DeleteAssetVFX(40021440)
    DeleteAssetVFX(40021441)
    DeleteAssetVFX(40021442)
    DeleteAssetVFX(40021443)
    DeleteAssetVFX(40021444)
    DeleteAssetVFX(40021445)
    DeleteAssetVFX(40021446)
    DeleteAssetVFX(40021447)
    DeleteAssetVFX(40021448)
    DeleteAssetVFX(40021449)
    DeleteAssetVFX(40021450)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(40021401)
    DeleteAssetVFX(40021402)
    DeleteAssetVFX(40021403)
    DeleteAssetVFX(40021404)
    DeleteAssetVFX(40021405)
    DeleteAssetVFX(40021406)
    DeleteAssetVFX(40021407)
    DeleteAssetVFX(40021408)
    DeleteAssetVFX(40021409)
    DeleteAssetVFX(40021410)
    DeleteAssetVFX(40021411)
    DeleteAssetVFX(40021412)
    DeleteAssetVFX(40021413)
    DeleteAssetVFX(40021414)
    DeleteAssetVFX(40021415)
    DeleteAssetVFX(40021416)
    DeleteAssetVFX(40021417)
    DeleteAssetVFX(40021418)
    DeleteAssetVFX(40021419)
    DeleteAssetVFX(40021420)
    DeleteAssetVFX(40021421)
    DeleteAssetVFX(40021422)
    DeleteAssetVFX(40021423)
    DeleteAssetVFX(40021424)
    DeleteAssetVFX(40021425)
    DeleteAssetVFX(40021426)
    DeleteAssetVFX(40021430)
    DeleteAssetVFX(40021431)
    DeleteAssetVFX(40021432)
    DeleteAssetVFX(40021433)
    DeleteAssetVFX(40021434)
    DeleteAssetVFX(40021435)
    DeleteAssetVFX(40021436)
    DeleteAssetVFX(40021437)
    DeleteAssetVFX(40021438)
    DeleteAssetVFX(40021439)
    DeleteAssetVFX(40021440)
    DeleteAssetVFX(40021441)
    DeleteAssetVFX(40021442)
    DeleteAssetVFX(40021443)
    DeleteAssetVFX(40021444)
    DeleteAssetVFX(40021445)
    DeleteAssetVFX(40021446)
    DeleteAssetVFX(40021447)
    DeleteAssetVFX(40021448)
    DeleteAssetVFX(40021449)
    DeleteAssetVFX(40021450)
    CreateAssetVFX(40021401, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021402, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021403, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021404, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021405, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021406, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021407, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021408, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021409, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021410, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021411, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021412, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021413, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021414, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021415, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021416, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021417, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021418, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021419, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021420, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021421, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021422, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021423, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021424, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021425, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021426, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021430, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021431, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021432, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021433, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021434, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021435, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021436, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021437, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021438, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021439, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021440, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021441, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021442, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021443, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021444, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021445, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021446, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021447, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021448, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021449, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021450, dummy_id=200, vfx_id=840016)
    End()


@RestartOnRest(40022401)
def Event_40022401():
    """Event 40022401"""
    GotoIfFlagEnabled(Label.L0, flag=40020400)
    AND_1.Add(FlagDisabled(40020400))
    AND_1.Add(AssetActivated(obj_act_id=40023400))
    
    MAIN.Await(AND_1)
    
    WaitRealFrames(frames=1)
    EnableNetworkFlag(40020400)
    EnableAssetActivation(40021400, obj_act_id=447115)
    DeleteAssetVFX(40021401)
    DeleteAssetVFX(40021402)
    DeleteAssetVFX(40021403)
    DeleteAssetVFX(40021404)
    DeleteAssetVFX(40021405)
    DeleteAssetVFX(40021406)
    DeleteAssetVFX(40021407)
    DeleteAssetVFX(40021408)
    DeleteAssetVFX(40021409)
    DeleteAssetVFX(40021410)
    DeleteAssetVFX(40021411)
    DeleteAssetVFX(40021412)
    DeleteAssetVFX(40021413)
    DeleteAssetVFX(40021414)
    DeleteAssetVFX(40021415)
    DeleteAssetVFX(40021416)
    DeleteAssetVFX(40021417)
    DeleteAssetVFX(40021418)
    DeleteAssetVFX(40021419)
    DeleteAssetVFX(40021420)
    DeleteAssetVFX(40021421)
    DeleteAssetVFX(40021422)
    DeleteAssetVFX(40021423)
    DeleteAssetVFX(40021424)
    DeleteAssetVFX(40021425)
    DeleteAssetVFX(40021426)
    DeleteAssetVFX(40021430)
    DeleteAssetVFX(40021431)
    DeleteAssetVFX(40021432)
    DeleteAssetVFX(40021433)
    DeleteAssetVFX(40021434)
    DeleteAssetVFX(40021435)
    DeleteAssetVFX(40021436)
    DeleteAssetVFX(40021437)
    DeleteAssetVFX(40021438)
    DeleteAssetVFX(40021439)
    DeleteAssetVFX(40021440)
    DeleteAssetVFX(40021441)
    DeleteAssetVFX(40021442)
    DeleteAssetVFX(40021443)
    DeleteAssetVFX(40021444)
    DeleteAssetVFX(40021445)
    DeleteAssetVFX(40021446)
    DeleteAssetVFX(40021447)
    DeleteAssetVFX(40021448)
    DeleteAssetVFX(40021449)
    DeleteAssetVFX(40021450)
    CreateAssetVFX(40021401, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021402, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021403, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021404, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021405, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021406, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021407, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021408, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021409, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021410, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021411, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021412, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021413, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021414, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021415, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021416, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021417, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021418, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021419, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021420, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021421, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021422, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021423, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021424, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021425, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021426, dummy_id=200, vfx_id=840015)
    CreateAssetVFX(40021430, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021431, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021432, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021433, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021434, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021435, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021436, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021437, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021438, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021439, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021440, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021441, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021442, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021443, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021444, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021445, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021446, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021447, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021448, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021449, dummy_id=200, vfx_id=840016)
    CreateAssetVFX(40021450, dummy_id=200, vfx_id=840016)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(40020400))
    AND_1.Add(AssetActivated(obj_act_id=40023400))
    
    MAIN.Await(AND_1)
    
    WaitRealFrames(frames=1)
    DisableNetworkFlag(40020400)
    EnableAssetActivation(40021400, obj_act_id=447115)
    DeleteAssetVFX(40021401)
    DeleteAssetVFX(40021402)
    DeleteAssetVFX(40021403)
    DeleteAssetVFX(40021404)
    DeleteAssetVFX(40021405)
    DeleteAssetVFX(40021406)
    DeleteAssetVFX(40021407)
    DeleteAssetVFX(40021408)
    DeleteAssetVFX(40021409)
    DeleteAssetVFX(40021410)
    DeleteAssetVFX(40021411)
    DeleteAssetVFX(40021412)
    DeleteAssetVFX(40021413)
    DeleteAssetVFX(40021414)
    DeleteAssetVFX(40021415)
    DeleteAssetVFX(40021416)
    DeleteAssetVFX(40021417)
    DeleteAssetVFX(40021418)
    DeleteAssetVFX(40021419)
    DeleteAssetVFX(40021420)
    DeleteAssetVFX(40021421)
    DeleteAssetVFX(40021422)
    DeleteAssetVFX(40021423)
    DeleteAssetVFX(40021424)
    DeleteAssetVFX(40021425)
    DeleteAssetVFX(40021426)
    DeleteAssetVFX(40021430)
    DeleteAssetVFX(40021431)
    DeleteAssetVFX(40021432)
    DeleteAssetVFX(40021433)
    DeleteAssetVFX(40021434)
    DeleteAssetVFX(40021435)
    DeleteAssetVFX(40021436)
    DeleteAssetVFX(40021437)
    DeleteAssetVFX(40021438)
    DeleteAssetVFX(40021439)
    DeleteAssetVFX(40021440)
    DeleteAssetVFX(40021441)
    DeleteAssetVFX(40021442)
    DeleteAssetVFX(40021443)
    DeleteAssetVFX(40021444)
    DeleteAssetVFX(40021445)
    DeleteAssetVFX(40021446)
    DeleteAssetVFX(40021447)
    DeleteAssetVFX(40021448)
    DeleteAssetVFX(40021449)
    DeleteAssetVFX(40021450)
    Restart()


@RestartOnRest(40022460)
def Event_40022460():
    """Event 40022460"""
    GotoIfFlagEnabled(Label.L0, flag=40020460)
    ForceAnimation(40021460, 0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(40021460, 2)
    End()


@ContinueOnRest(40022461)
def Event_40022461():
    """Event 40022461"""
    if FlagEnabled(40020460):
        return
    AND_13.Add(FlagEnabled(40020460))
    AND_13.Add(FlagEnabled(40022464))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(40020460))
    AND_14.Add(FlagDisabled(40022464))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(40022466))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagEnabled(Label.L0, flag=40020460)
    OR_1.Add(FlagEnabled(40020460))
    AND_2.Add(AssetActivated(obj_act_id=40023400))
    OR_2.Add(AND_2)
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    
    MAIN.Await(OR_4)
    
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(40020460)
        EnableNetworkFlag(40022466)
    EnableFlag(40022464)
    ForceAnimation(40021460, 1, wait_for_completion=True)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        DisableNetworkFlag(40022466)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(40022466))
    
    Restart()


@RestartOnRest(400222410)
def Event_400222410(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    flag: Flag | int,
):
    """Event 400222410"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
        AND_3.Add(FlagEnabled(flag))
        OR_3.Add(AND_3)
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
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
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(40022241)
def Event_40022241(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    flag: Flag | int,
):
    """Event 40022241"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    DisableAI(character)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    AND_9.Add(FlagEnabled(flag))
    AND_9.Add(CharacterBackreadEnabled(character))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_9)
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
    
    MAIN.Await(OR_2)
    
    EnableAI(character)
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    if FlagEnabled(flag):
        return
    AddSpecialEffect(character, 5000)
    ReplanAI(character)
    if UnsignedNotEqual(left=0, right=region):
        MAIN.Await(CharacterInsideRegion(character=character, region=region))
    RemoveSpecialEffect(character, 5000)
    ReplanAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(2052432845)
def Event_2052432845():
    """Event 2052432845"""
    if PlayerInOwnWorld():
        return
    if FlagEnabled(2052430800):
        return
    OR_1.Add(HealthValue(2052430800) <= 0)
    OR_1.Add(FlagEnabled(2052432848))
    
    MAIN.Await(OR_1)
    
    Wait(4.0)
    PlaySoundEffect(2052430800, 888880000, sound_type=SoundType.s_SFX)
    OR_2.Add(CharacterDead(2052430800))
    OR_2.Add(FlagEnabled(2052432848))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=2052430800, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(2052430800)
    if PlayerInOwnWorld():
        EnableFlag(61161)
    EnableFlag(9161)
