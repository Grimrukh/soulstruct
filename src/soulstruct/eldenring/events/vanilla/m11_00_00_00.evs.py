"""
Leyndell, Royal Capital

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
from .enums.m11_00_00_00_enums import *
from .enums.m10_00_00_00_enums import Characters as m10_00_00_00_Characters
from .enums.m60_45_52_00_enums import Assets as m60_45_52_00_Assets


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=11000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=11000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=11000004, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=11000005, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=11000006, asset=11001956)
    RegisterGrace(grace_flag=11000007, asset=Assets.AEG099_060_9007)
    RegisterGrace(grace_flag=11000008, asset=Assets.AEG099_060_9008)
    RegisterGrace(grace_flag=11000009, asset=Assets.AEG099_060_9009)
    CommonFunc_9005810(
        0,
        flag=11000500,
        grace_flag=11000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_9005810(
        0,
        flag=11000850,
        grace_flag=11000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    Event_11002800()
    Event_11002810()
    Event_11002811()
    Event_11002829()
    Event_11002850()
    Event_11002860()
    Event_11002859()
    Event_11002500()
    Event_11002501()
    Event_11002502()
    Event_11002503()
    CommonFunc_90005501(
        0,
        flag=11000510,
        flag_1=11000511,
        left=0,
        asset=Assets.AEG227_000_0500,
        asset_1=Assets.AEG227_050_0500,
        asset_2=Assets.AEG227_050_0501,
        flag_2=11000512,
    )
    CommonFunc_90005501(
        0,
        flag=11000515,
        flag_1=11000516,
        left=0,
        asset=Assets.AEG227_001_0500,
        asset_1=Assets.AEG227_050_0502,
        asset_2=Assets.AEG227_050_0503,
        flag_2=11000517,
    )
    CommonFunc_90005501(
        0,
        flag=11000520,
        flag_1=11000521,
        left=0,
        asset=Assets.AEG227_002_0500,
        asset_1=Assets.AEG227_050_0504,
        asset_2=Assets.AEG227_050_0505,
        flag_2=11000522,
    )
    CommonFunc_90005501(
        0,
        flag=11000525,
        flag_1=11000526,
        left=0,
        asset=Assets.AEG227_003_0500,
        asset_1=Assets.AEG227_051_0500,
        asset_2=Assets.AEG227_051_0501,
        flag_2=11000527,
    )
    CommonFunc_90005501(
        0,
        flag=11000530,
        flag_1=11000531,
        left=0,
        asset=Assets.AEG227_090_0500,
        asset_1=Assets.AEG227_052_0503,
        asset_2=Assets.AEG227_052_0502,
        flag_2=11000532,
    )
    CommonFunc_90005501(
        0,
        flag=11000535,
        flag_1=11000536,
        left=1,
        asset=Assets.AEG227_090_0501,
        asset_1=Assets.AEG227_052_0500,
        asset_2=Assets.AEG227_052_0501,
        flag_2=11000537,
    )
    CommonFunc_90005501(
        0,
        flag=11000610,
        flag_1=11000611,
        left=2,
        asset=Assets.AEG227_001_0501,
        asset_1=Assets.AEG227_050_0507,
        asset_2=m60_45_52_00_Assets.AEG227_050_2001,
        flag_2=11000612,
    )
    Event_11002510()
    Event_11000602()
    CommonFunc_90005513(
        0,
        flag=11000540,
        asset=Assets.AEG227_040_0500,
        asset_1=11001541,
        obj_act_id=11003541,
        obj_act_id_1=1227050,
        animation_id=1,
        animation_id_1=2,
    )
    Event_11002546(
        0,
        flag=11000546,
        asset=Assets.AEG227_012_0501,
        asset_1=Assets.AEG227_050_0509,
        obj_act_id=11003547,
        obj_act_id_1=1227050,
        animation_id=1,
        animation_id_1=2,
    )
    Event_11002547()
    CommonFunc_90005511(
        0,
        flag=11000560,
        asset=Assets.AEG227_010_0500,
        obj_act_id=11003560,
        obj_act_id_1=227010,
        left=0,
    )
    CommonFunc_90005512(0, flag=11000560, region=11002560, region_1=11002561)
    CommonFunc_90005511(
        0,
        flag=11000562,
        asset=Assets.AEG227_010_0501,
        obj_act_id=11003562,
        obj_act_id_1=227010,
        left=0,
    )
    CommonFunc_90005512(0, flag=11000562, region=11002562, region_1=11002563)
    CommonFunc_90005511(
        0,
        flag=11000564,
        asset=Assets.AEG227_070_0500,
        obj_act_id=11003564,
        obj_act_id_1=227070,
        left=0,
    )
    Event_11002540()
    Event_11000600()
    Event_11002601()
    Event_11002603()
    Event_11002580()
    CommonFunc_90005520(
        0,
        flag=11000576,
        asset=Assets.AEG227_027_0500,
        start_climbing_flag=11002576,
        stop_climbing_flag=11002577,
    )
    CommonFunc_90005520(
        0,
        flag=11000578,
        asset=Assets.AEG227_029_0500,
        start_climbing_flag=11002578,
        stop_climbing_flag=11002579,
    )
    Event_11002690()
    Event_11002691(0, asset=Assets.AEG228_098_1038)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=34,
        block_id=15,
        cc_id=0,
        dd_id=0,
        player_start=34152692,
        unk_8_12=11000000,
        flag=11002692,
        left_flag=11002693,
        cancel_flag__right_flag=11002694,
        left=11000600,
        text=30040,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005632(0, flag=580050, asset=Assets.AEG099_389_4500, item_lot=80050)
    CommonFunc_90005570(0, flag=60822, gesture_param_id=52, asset=Assets.AEG099_600_9001, left=0, left_1=1, right=0)
    Event_11002698()
    Event_11002697()
    Event_11002699()
    Event_11002604()
    Event_11002203(0, character=Characters.SmallOracleEnvoy3, region=11002216)
    Event_11002205(0, character=Characters.SmallOracleEnvoy3, region=11002215)
    Event_11002207(0, character=Characters.SmallOracleEnvoy3, flag=11002216)
    Event_11002209(0, character=Characters.SmallOracleEnvoy3, flag=11002215)
    Event_11002203(1, character=Characters.SmallOracleEnvoy5, region=11002218)
    Event_11002205(1, character=Characters.SmallOracleEnvoy5, region=11002217)
    Event_11002207(1, character=Characters.SmallOracleEnvoy5, flag=11002218)
    Event_11002209(1, character=Characters.SmallOracleEnvoy5, flag=11002217)
    Event_11002260(
        5,
        character=Characters.Commoner0,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        6,
        character=Characters.Commoner1,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        7,
        character=Characters.Commoner2,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        8,
        character=Characters.Commoner3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        9,
        character=Characters.Commoner4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        10,
        character=Characters.Commoner5,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        11,
        character=Characters.Commoner6,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        12,
        character=Characters.Commoner7,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        13,
        character=Characters.Commoner8,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        14,
        character=Characters.Commoner9,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        15,
        character=Characters.Commoner10,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        16,
        character=Characters.Commoner11,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        17,
        character=11000277,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        18,
        character=11000278,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        19,
        character=11000279,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        20,
        character=11000280,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        21,
        character=Characters.Commoner12,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        22,
        character=Characters.Commoner13,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        23,
        character=Characters.Commoner14,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        24,
        character=Characters.Commoner15,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        25,
        character=Characters.Commoner16,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        26,
        character=11000286,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        27,
        character=11000287,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        28,
        character=11000288,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    Event_11002260(
        29,
        character=11000289,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
        left_4=0,
    )
    CommonFunc_90005300(0, flag=11000393, character=Characters.Gargoyle2, item_lot=11001187, seconds=2.0, left=0)
    Event_11002402(
        2,
        character=Characters.DepravedPerfumer1,
        animation_id=30000,
        animation_id_1=20000,
        region=11002243,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
        left_4=1,
    )
    Event_11002402(
        0,
        character=Characters.DepravedPerfumer3,
        animation_id=30000,
        animation_id_1=20000,
        region=11002254,
        seconds=2.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
        left_4=1,
    )
    Event_11002402(
        1,
        character=Characters.DepravedPerfumer8,
        animation_id=30000,
        animation_id_1=20000,
        region=11002259,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=1,
        left_3=1,
        left_4=1,
    )
    Event_11002317(0, character=Characters.LeyndellKnight8, region=11002359, seconds=0.0, radius=5.0)
    Event_11002317(1, character=Characters.DepravedPerfumer9, region=11002359, seconds=0.0, radius=10.0)
    CommonFunc_90005300(0, flag=11000389, character=Characters.ErdtreeAvatar, item_lot=11001198, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000399, character=Characters.LionGuardian, item_lot=11000185, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000495, character=Characters.CrucibleKnight0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000496, character=Characters.CrucibleKnight1, item_lot=0, seconds=0.0, left=0)
    Event_11002497(0, character=Characters.UlceratedTreeSpirit, region=11002497, seconds=0.0)
    CommonFunc_90005300(
        0,
        flag=11000497,
        character=Characters.UlceratedTreeSpirit,
        item_lot=11001193,
        seconds=0.0,
        left=0,
    )
    Event_11002402(
        4,
        character=Characters.LeonineMisbegotten0,
        animation_id=30001,
        animation_id_1=20001,
        region=11002625,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=1,
        left_3=1,
        left_4=1,
    )
    CommonFunc_90005300(0, flag=11000498, character=Characters.GuardianGolem, item_lot=0, seconds=2.0, left=0)
    CommonFunc_90005300(0, flag=11000499, character=11000499, item_lot=11000195, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000484, character=Characters.BlackKnifeAssassin, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000665, character=Characters.Scarab0, item_lot=40370, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000666, character=Characters.Scarab1, item_lot=40372, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000667, character=11000667, item_lot=40374, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=11000299, character=11000299, item_lot=11001000, seconds=0.0, left=0)
    CommonFunc_9005811(0, flag=11000850, asset=11001930, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=11001931, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=11001932, vfx_id=5, right=0)
    CommonFunc_90005795(
        0,
        flag=7605,
        flag_1=0,
        flag_2=11009500,
        left_flag=11002141,
        cancel_flag__right_flag=11002142,
        message=80605,
        action_button_id=9000,
        asset=Assets.AEG099_090_9002,
        vfx_id=30010,
    )
    if CeremonyActive(ceremony=20):
        Event_11002155(
            0,
            flag=7605,
            character=Characters.VargramtheRagingWolf,
            character_1=Characters.ErrantSorcererWilhelm,
            banner_type=5,
            region=11002141,
        )
        Event_11002145()
    CommonFunc_90005780(
        0,
        flag=11000800,
        summon_flag=11002164,
        dismissal_flag=11002165,
        character=Characters.Melina,
        sign_type=20,
        region=11002164,
        right=0,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=11000800, flag_1=11002164, flag_2=11002165, character=Characters.Melina)
    CommonFunc_90005782(
        0,
        flag=11002164,
        region=11002805,
        character=Characters.Melina,
        target_entity=11002800,
        region_1=11002809,
        animation=20029,
    )
    CommonFunc_90005780(
        0,
        flag=11000800,
        summon_flag=11002168,
        dismissal_flag=11002169,
        character=Characters.DungEater,
        sign_type=20,
        region=11002761,
        right=35009317,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=11000800, flag_1=11002168, flag_2=11002169, character=Characters.DungEater)
    CommonFunc_90005782(
        0,
        flag=11002168,
        region=11002805,
        character=Characters.DungEater,
        target_entity=11002800,
        region_1=11002809,
        animation=0,
    )
    CommonFunc_90005703(
        0,
        character=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3942,
        flag_2=1039409251,
        flag_3=3941,
        first_flag=3940,
        last_flag=3943,
        right=0,
    )
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.DemiHumanShaman,
        flag=3941,
        flag_1=3940,
        flag_2=1039409251,
        right=3,
    )
    CommonFunc_90005702(0, character=Characters.DemiHumanShaman, flag=3943, first_flag=3940, last_flag=3944)
    Event_11003710(0, character=Characters.DemiHumanShaman)
    Event_11003711(0, entity=Characters.DemiHumanShaman)
    Event_11003715(0, character=Characters.DefeatedMorgott)
    Event_11003720(0, character=Characters.BrotherCorhyn)
    CommonFunc_90005704(0, attacked_entity=Characters.BrotherCorhyn, flag=4201, flag_1=4200, flag_2=11009451, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.BrotherCorhyn,
        flag=4201,
        flag_1=4202,
        flag_2=11009451,
        flag_3=4201,
        first_flag=4200,
        last_flag=4204,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.BrotherCorhyn, flag=4203, first_flag=4200, last_flag=4204)
    Event_11003721(0, character=Characters.Goldmask)
    Event_11003722(0, character=Characters.Goldmask)
    Event_11003723(0, other_entity=Characters.TalkDummy13)
    Event_11003724()
    Event_11003725(0, character=11000705)
    CommonFunc_90005701(0, attacked_entity=11000705, flag=4701, flag_1=4702, flag_2=11009301, right=3)
    CommonFunc_90005700(
        0,
        character=11000705,
        flag=4701,
        flag_1=4702,
        flag_2=11009301,
        value=0.6499999761581421,
        first_flag=4700,
        last_flag=4704,
        right=-1,
    )
    CommonFunc_90005702(0, character=11000705, flag=4703, first_flag=4700, last_flag=4704)
    Event_11003730()
    CommonFunc_90005774(0, flag=7605, item_lot=11001985, flag_1=11001985)
    Event_11003740()
    Event_11003741()
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy6, flag=11002740)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy2, flag=11002741)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy3, flag=11002742)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy4, flag=11002743)
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy5, flag=11002744)
    CommonFunc_90005775(0, world_map_point_param_id=85495300, flag=11109687, distance=-1.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(11000705)
    DisableBackread(Characters.DemiHumanShaman)
    DisableBackread(Characters.Goldmask)
    DisableBackread(Characters.DefeatedMorgott)
    DisableBackread(Characters.BrotherCorhyn)
    DisableBackread(Characters.RecusantBernahl)
    DisableBackread(Characters.VargramtheRagingWolf)
    DisableBackread(Characters.ErrantSorcererWilhelm)
    DisableHealthBar(Characters.Dummy1)
    Event_11000519()
    CommonFunc_90005201(
        0,
        character=Characters.SmallOracleEnvoy0,
        animation_id=30000,
        animation_id_1=20000,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy1,
        animation_id=30000,
        animation_id_1=20000,
        region=11002202,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy2,
        animation_id=30000,
        animation_id_1=20000,
        region=11002202,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.SmallOracleEnvoy4,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallOracleEnvoy6, region=11002208, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallOracleEnvoy7, region=11002208, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.SmallOracleEnvoy8,
        animation_id=30000,
        animation_id_1=20000,
        region=11002208,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp0,
        animation_id=30010,
        animation_id_1=20010,
        region=11002220,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp1,
        animation_id=30010,
        animation_id_1=20010,
        region=11002220,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp2, region=11002222, seconds=0.0, animation_id=3004)
    CommonFunc_90005200(
        0,
        character=Characters.Imp3,
        animation_id=30010,
        animation_id_1=20010,
        region=11002223,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp4,
        animation_id=30010,
        animation_id_1=20010,
        region=11002224,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp5,
        animation_id=30010,
        animation_id_1=20010,
        region=11002224,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=11002226,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp7,
        animation_id=30002,
        animation_id_1=20002,
        region=11002227,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallOracleEnvoy9,
        animation_id=30000,
        animation_id_1=20000,
        region=11002393,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallOracleEnvoy10,
        animation_id=30000,
        animation_id_1=20000,
        region=11002393,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallOracleEnvoy11,
        animation_id=30000,
        animation_id_1=20000,
        region=11002393,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallOracleEnvoy12, region=11002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallOracleEnvoy13, region=11002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallOracleEnvoy14, region=11002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page0, region=11002240, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page4, region=11002246, seconds=0.0, animation_id=-1)
    CommonFunc_90005210(
        0,
        character=Characters.Page1,
        animation_id=30000,
        animation_id_1=20000,
        region=11002242,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Page2, region=11002243, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Page3, region=11002244, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=11000247, region=11002247, seconds=0.0, animation_id=3012)
    CommonFunc_90005250(0, character=Characters.Page5, region=11002248, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.DepravedPerfumer0,
        animation_id=30000,
        animation_id_1=20000,
        region=11002250,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.DepravedPerfumer1, region=11002243, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.DepravedPerfumer2, region=11002243, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.DepravedPerfumer4, region=11002255, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.DepravedPerfumer5,
        animation_id=30002,
        animation_id_1=20002,
        region=11002256,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.DepravedPerfumer6,
        animation_id=30002,
        animation_id_1=20002,
        region=11002625,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.DepravedPerfumer7, region=11002625, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.DepravedPerfumer10,
        animation_id=30000,
        animation_id_1=20000,
        region=11002345,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DepravedPerfumer11,
        region=11002496,
        radius=9.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Commoner25,
        animation_id=30000,
        animation_id_1=20000,
        region=11002340,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Commoner26,
        animation_id=30000,
        animation_id_1=20000,
        region=11002340,
        seconds=2.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=11000343,
        animation_id=30000,
        animation_id_1=20000,
        region=11002340,
        seconds=1.5,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Commoner17, region=11002330, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner18, region=11002330, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Commoner19, region=11002330, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(
        0,
        character=Characters.Commoner20,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner21,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner22,
        animation_id=30001,
        animation_id_1=20001,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Commoner23,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.TallOracleEnvoy,
        animation_id=30000,
        animation_id_1=20000,
        region=11002390,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Gargoyle0, region=11002206, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Gargoyle1, region=11002230, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Gargoyle2,
        animation_id=30000,
        animation_id_1=20000,
        region=11002393,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Gargoyle3, region=11002394, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier0,
        animation_id=30010,
        animation_id_1=20010,
        region=11002401,
        seconds=1.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier1,
        animation_id=30010,
        animation_id_1=20010,
        region=11002353,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier2, region=11002353, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier3,
        animation_id=30010,
        animation_id_1=20010,
        region=11002358,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier4,
        animation_id=30010,
        animation_id_1=20010,
        region=11002358,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier9, region=11002407, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier10, region=11002407, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier11, region=11002259, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier12,
        animation_id=30010,
        animation_id_1=20010,
        region=11002259,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellFootSoldier13,
        animation_id=30010,
        animation_id_1=20010,
        region=11002410,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier14, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier15, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier16, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier17, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier18, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier19, region=11002326, seconds=0.0, animation_id=3026)
    CommonFunc_90005250(0, character=Characters.LeyndellFootSoldier20, region=11002327, seconds=0.0, animation_id=3012)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellSoldier0,
        animation_id=30002,
        animation_id_1=20002,
        region=11002350,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier1, region=11002350, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellSoldier2,
        animation_id=30002,
        animation_id_1=20002,
        region=11002259,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier3, region=11002353, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier4, region=11002354, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier5, region=11002354, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellSoldier6,
        animation_id=30003,
        animation_id_1=20003,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellSoldier7,
        animation_id=30004,
        animation_id_1=20004,
        region=0,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier8, region=11002358, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.LeyndellSoldier9,
        animation_id=30004,
        animation_id_1=20004,
        region=11002359,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier10, region=11002360, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=11000361,
        animation_id=30003,
        animation_id_1=20003,
        region=11002359,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier11, region=11002405, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier12, region=11002405, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellSoldier14, region=11002407, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.LeyndellKnight0,
        animation_id=30000,
        animation_id_1=20000,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellKnight1, region=11002401, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight4, region=11002404, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight14, region=11002405, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight6, region=11002406, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight7, region=11002407, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=11000409, region=11002405, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=11000410, region=11002410, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellKnight9,
        animation_id=30000,
        animation_id_1=20000,
        region=11002411,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.LeyndellKnight10, region=11002412, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight11, region=11002413, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight12, region=11002414, seconds=0.0, animation_id=3029)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight13, region=11002415, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight5, region=11002416, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.LeyndellKnight15, region=11002416, seconds=0.0, animation_id=-1)
    CommonFunc_90005210(
        0,
        character=Characters.ErdtreeAvatar,
        animation_id=30000,
        animation_id_1=20000,
        region=11002389,
        radius=35.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.IronVirgin1, region=11002493, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.IronVirgin0, region=11002494, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CrucibleKnight0, region=11002495, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CrucibleKnight1, region=11002496, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=11002430, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse1,
        animation_id=30000,
        animation_id_1=20000,
        region=11002431,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30001,
        animation_id_1=20001,
        region=11002433,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse3,
        animation_id=30002,
        animation_id_1=20002,
        region=11002433,
        seconds=6.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30002,
        animation_id_1=20002,
        region=11002435,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30005,
        animation_id_1=20005,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse6,
        animation_id=30001,
        animation_id_1=20001,
        region=11002435,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse7,
        animation_id=30005,
        animation_id_1=20005,
        region=11002295,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30005,
        animation_id_1=20005,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton0,
        animation_id=30017,
        animation_id_1=20017,
        region=11002295,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton1,
        animation_id=30017,
        animation_id_1=20017,
        region=11002295,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton2,
        animation_id=30018,
        animation_id_1=20018,
        region=11002297,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Rat0, region=11002455, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat1, region=11002455, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Rat2, region=11002471, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=11000459, region=11002471, seconds=0.0, animation_id=3009)
    CommonFunc_90005250(0, character=Characters.Omenkiller, region=11002469, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout0,
        animation_id=30000,
        animation_id_1=20000,
        region=11002425,
        radius=3.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.AlbinauricLookout1,
        animation_id=30005,
        animation_id_1=20005,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout2,
        animation_id=30004,
        animation_id_1=20004,
        region=11002425,
        radius=3.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout3,
        animation_id=30006,
        animation_id_1=20006,
        region=11002425,
        radius=3.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout4,
        animation_id=30000,
        animation_id_1=20000,
        region=11002464,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricLookout5,
        animation_id=30004,
        animation_id_1=20004,
        region=11002464,
        radius=2.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper0,
        animation_id=30003,
        animation_id_1=20003,
        region=11002470,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper1,
        animation_id=30002,
        animation_id_1=20002,
        region=11002471,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=11000472,
        animation_id=30003,
        animation_id_1=20003,
        region=11002466,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper2,
        animation_id=30003,
        animation_id_1=20003,
        region=11002466,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper3,
        animation_id=30005,
        animation_id_1=20005,
        region=11002480,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper4,
        animation_id=30003,
        animation_id_1=20003,
        region=11002476,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper5,
        animation_id=30005,
        animation_id_1=20005,
        region=11002476,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LesserFingercreeper6,
        animation_id=30005,
        animation_id_1=20005,
        region=11002480,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Fingercreeper,
        animation_id=30003,
        animation_id_1=20003,
        region=11002480,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten0,
        animation_id=30001,
        animation_id_1=20001,
        region=11002620,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten1,
        animation_id=30001,
        animation_id_1=20001,
        region=11002620,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten3,
        animation_id=30003,
        animation_id_1=20003,
        region=11002625,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten4,
        animation_id=30002,
        animation_id_1=20002,
        region=11002625,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Misbegotten5, region=11002625, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Misbegotten6, region=11002630, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten7,
        animation_id=30000,
        animation_id_1=20000,
        region=11002631,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten8,
        animation_id=30000,
        animation_id_1=20000,
        region=11002631,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten9,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten10,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten11,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten12,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten13,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten14,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Misbegotten15,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Misbegotten16,
        animation_id=30001,
        animation_id_1=20001,
        region=11002645,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.ScalyMisbegotten0,
        animation_id=30000,
        animation_id_1=20000,
        region=11002631,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.ScalyMisbegotten1,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeonineMisbegotten1,
        animation_id=30000,
        animation_id_1=20000,
        region=11002398,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallerDog0,
        animation_id=30000,
        animation_id_1=20000,
        region=11002650,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallerDog1, region=11002650, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Dog0,
        animation_id=30000,
        animation_id_1=20000,
        region=11002650,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallerDog3,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.SmallerDog4,
        animation_id=30000,
        animation_id_1=20000,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallerDog6,
        animation_id=30000,
        animation_id_1=20000,
        region=11002645,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.SmallerDog7, region=11002645, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=11000658, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Dog1,
        animation_id=30001,
        animation_id_1=20001,
        region=11002398,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.SmallerDog11, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Dog1, region=11002488, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian0,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian1,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.ErdtreeGuardian2,
        animation_id=30000,
        animation_id_1=20000,
        region=11002672,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian3,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian4,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.ErdtreeGuardian9,
        animation_id=30001,
        animation_id_1=20001,
        region=11002681,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.ErdtreeGuardian10,
        animation_id=30001,
        animation_id_1=20001,
        region=11002682,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian11,
        animation_id=30001,
        animation_id_1=20001,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.ErdtreeGuardian12,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.GraveWardenDuelist1, region=11002486, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=11000488, region=11002488, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=11000489, region=11002499, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GuardianGolem, region=11002498, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.LionGuardian,
        animation_id=30000,
        animation_id_1=20000,
        region=11002256,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=11000499, region=11002499, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.BlackKnifeAssassin, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Scarab0, region=11002496, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Scarab1, region=11002425, seconds=0.0, animation_id=-1)
    EnableFlag(11008542)
    if FlagDisabled(11008544):
        EnableFlag(11008544)


@ContinueOnRest(11002500)
def Event_11002500():
    """Event 11002500"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9500, entity=Assets.AEG099_090_9000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=ALL_PLAYERS, anchor_entity=Assets.AEG099_090_9000, button_type=ButtonType.Yes_or_No)
    EnableFlag(11000500)
    Wait(3.0)
    Restart()


@ContinueOnRest(11002501)
def Event_11002501():
    """Event 11002501"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11000501):
        return
    AND_1.Add(FlagEnabled(11000800))
    AND_1.Add(FlagDisabled(11000501))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(FlagEnabled(11000800))
    AND_2.Add(FlagEnabled(11000500))
    AND_2.Add(FlagEnabled(9000))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    EnableFlag(11000501)
    Restart()


@ContinueOnRest(11002502)
def Event_11002502():
    """Event 11002502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11000500):
        return
    AND_1.Add(FlagEnabled(11002802))
    AND_2.Add(FlagEnabled(11000800))
    AND_2.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_9.Add(AND_1)
    OR_9.Add(AND_2)
    
    MAIN.Await(OR_9)
    
    SetWeather(weather=Weather.Rain, duration=-1.0, immediate_change=False)
    Wait(3.0)
    AND_1.Add(FlagEnabled(11002802))
    AND_2.Add(FlagEnabled(11000800))
    AND_2.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_9.Add(AND_1)
    OR_9.Add(AND_2)
    
    MAIN.Await(not OR_9)
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    Wait(3.0)
    Restart()


@ContinueOnRest(11002503)
def Event_11002503():
    """Event 11002503"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(11000501):
        return
    AND_10.Add(PlayerInOwnWorld())
    AND_10.Add(FlagEnabled(11000800))
    AND_10.Add(FlagDisabled(11000501))
    AND_10.Add(ActionButtonParamActivated(action_button_id=10000, entity=Assets.AEG099_001_9000))
    OR_10.Add(Multiplayer())
    OR_10.Add(MultiplayerPending())
    AND_10.Add(not OR_10)
    
    MAIN.Await(AND_10)
    
    FaceEntityAndForceAnimation(PLAYER, 11002800, animation=60060, wait_for_completion=True)
    BanishInvaders(unknown=0)
    Restart()


@ContinueOnRest(11000519)
def Event_11000519():
    """Event 11000519"""
    if FlagEnabled(300):
        EnableFlag(11000530)
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(11000510)
    EnableFlag(11000520)
    EnableFlag(11000525)


@ContinueOnRest(11000602)
def Event_11000602():
    """Event 11000602"""
    if FlagDisabled(300):
        return
    DisableAssetActivation(Assets.AEG227_052_0503, obj_act_id=-1)
    AND_1.Add(FlagEnabled(300))
    AND_1.Add(ActionButtonParamActivated(action_button_id=8320, entity=Assets.AEG227_090_0500))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=99995010, anchor_entity=Assets.AEG227_090_0500, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@RestartOnRest(11002145)
def Event_11002145():
    """Event 11002145"""
    if CeremonyInactive(ceremony=20):
        return
    EnableBackread(Characters.VargramtheRagingWolf)
    EnableBackread(Characters.ErrantSorcererWilhelm)
    EnableBackread(Characters.RecusantBernahl)
    SetTeamType(Characters.VargramtheRagingWolf, TeamType.Human)
    SetTeamType(Characters.ErrantSorcererWilhelm, TeamType.Human)
    SetTeamType(Characters.RecusantBernahl, TeamType.Enemy)
    DeleteAssetVFX(11006700)
    CreateAssetVFX(11006700, dummy_id=200, vfx_id=806700)


@RestartOnRest(11002155)
def Event_11002155(
    _,
    flag: Flag | int,
    character: Character | int,
    character_1: Character | int,
    banner_type: uchar,
    region: Region | int,
):
    """Event 11002155"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterDead(character))
    AND_1.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisplayBanner(banner_type)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    AddSpecialEffect(ALL_PLAYERS, 4821)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(11002203)
def Event_11002203(_, character: Character | int, region: uint):
    """Event 11002203"""
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(HealthValue(character) <= 0)
    if AND_15:
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(region)
    Wait(8.0)
    DisableNetworkFlag(region)
    Restart()


@RestartOnRest(11002205)
def Event_11002205(_, character: Character | int, region: uint):
    """Event 11002205"""
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(HealthValue(character) <= 0)
    if AND_15:
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(region)
    Wait(8.0)
    DisableNetworkFlag(region)
    Restart()


@RestartOnRest(11002207)
def Event_11002207(_, character: uint, flag: Flag | int):
    """Event 11002207"""
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(HealthValue(character) <= 0)
    if AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(0.8999999761581421)
    ForceAnimation(character, 30002, loop=True)
    Wait(8.0)
    Restart()


@RestartOnRest(11002209)
def Event_11002209(_, character: uint, flag: Flag | int):
    """Event 11002209"""
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(HealthValue(character) <= 0)
    if AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(0.8999999761581421)
    ForceAnimation(character, 30001, loop=True)
    Wait(8.0)
    Restart()


@RestartOnRest(11002260)
def Event_11002260(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 11002260"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterHasSpecialEffect(character, 14405))
    OR_3.Add(CharacterHasSpecialEffect(character, 14406))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    AND_9.Add(UnsignedEqual(left=left_4, right=0))
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


@RestartOnRest(11002317)
def Event_11002317(_, character: uint, region: Region | int, seconds: float, radius: float):
    """Event 11002317"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_3.Add(CharacterHasSpecialEffect(PLAYER, 10004))
    AND_3.Add(OR_3)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_3)
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(11002360)
def Event_11002360(
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
):
    """Event 11002360"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_3.Add(CharacterHasSpecialEffect(PLAYER, 10000))
    AND_3.Add(OR_3)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_3)
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
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
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


@RestartOnRest(11002370)
def Event_11002370(_, character: Character | int):
    """Event 11002370"""
    Kill(character)


@RestartOnRest(11002397)
def Event_11002397(_, character: uint, region: Region | int, seconds: float):
    """Event 11002397"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, 30001, loop=True)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(HasAIStatus(Characters.DepravedPerfumer6, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.DepravedPerfumer7, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.Misbegotten3, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.Misbegotten4, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.Misbegotten5, ai_status=AIStatusType.Battle))
    AND_2.Add(OR_3)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(AND_2)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    ForceAnimation(character, 20001)
    ChangePatrolBehavior(character, patrol_information_id=11003397)
    AddSpecialEffect(character, 5000)


@RestartOnRest(11002402)
def Event_11002402(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
    left_4: uint,
):
    """Event 11002402"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    AND_9.Add(UnsignedEqual(left=left_4, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    if UnsignedNotEqual(left=left_4, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
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


@RestartOnRest(11002497)
def Event_11002497(_, character: uint, region: Region | int, seconds: float):
    """Event 11002497"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, 30002)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=20.0))
    AND_1.Add(AND_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20002)


@ContinueOnRest(11002510)
def Event_11002510():
    """Event 11002510"""
    CommonFunc_90005500(
        0,
        flag=11000510,
        flag_1=11000511,
        left=0,
        asset=Assets.AEG227_000_0500,
        asset_1=Assets.AEG227_050_0500,
        obj_act_id=11003511,
        asset_2=Assets.AEG227_050_0501,
        obj_act_id_1=11003512,
        region=11002511,
        region_1=11002512,
        flag_2=11000512,
        flag_3=11000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=11000515,
        flag_1=11000516,
        left=0,
        asset=Assets.AEG227_001_0500,
        asset_1=Assets.AEG227_050_0502,
        obj_act_id=11003516,
        asset_2=Assets.AEG227_050_0503,
        obj_act_id_1=11003517,
        region=11002516,
        region_1=11002517,
        flag_2=11000517,
        flag_3=11000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=11000520,
        flag_1=11000521,
        left=0,
        asset=Assets.AEG227_002_0500,
        asset_1=Assets.AEG227_050_0504,
        obj_act_id=11003521,
        asset_2=Assets.AEG227_050_0505,
        obj_act_id_1=11003522,
        region=11002521,
        region_1=11002522,
        flag_2=11000522,
        flag_3=11000523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=11000525,
        flag_1=11000526,
        left=0,
        asset=Assets.AEG227_003_0500,
        asset_1=Assets.AEG227_051_0500,
        obj_act_id=11003526,
        asset_2=Assets.AEG227_051_0501,
        obj_act_id_1=11003527,
        region=11002526,
        region_1=11002527,
        flag_2=11000527,
        flag_3=11000528,
        left_1=0,
    )
    if FlagDisabled(300):
        CommonFunc_90005505(
            0,
            flag=11000530,
            flag_1=11000531,
            left=0,
            asset=Assets.AEG227_090_0500,
            asset_1=Assets.AEG227_052_0503,
            obj_act_id=11003531,
            asset_2=Assets.AEG227_052_0502,
            obj_act_id_1=11003532,
            flag_2=11000532,
            flag_3=11000533,
            left_1=0,
        )
    CommonFunc_90005505(
        0,
        flag=11000535,
        flag_1=11000536,
        left=1,
        asset=Assets.AEG227_090_0501,
        asset_1=Assets.AEG227_052_0500,
        obj_act_id=11003536,
        asset_2=Assets.AEG227_052_0501,
        obj_act_id_1=11003537,
        flag_2=11000537,
        flag_3=11000538,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=11000610,
        flag_1=11000611,
        left=2,
        asset=Assets.AEG227_001_0501,
        asset_1=Assets.AEG227_050_0507,
        obj_act_id=11003611,
        asset_2=m60_45_52_00_Assets.AEG227_050_2001,
        obj_act_id_1=11003612,
        region=11002611,
        region_1=11002612,
        flag_2=11000612,
        flag_3=11000613,
        left_1=0,
    )


@RestartOnRest(11002540)
def Event_11002540():
    """Event 11002540"""
    EndOfAnimation(asset=Assets.AEG227_011_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG227_033_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG227_033_0501, animation_id=2)
    EndOfAnimation(asset=Assets.AEG227_012_0502, animation_id=2)


@RestartOnRest(11002546)
def Event_11002546(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
):
    """Event 11002546"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    DisableAssetActivation(asset, obj_act_id=227012)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    ForceAnimation(asset, animation_id)
    DisableAssetActivation(asset, obj_act_id=227012)


@RestartOnRest(11002547)
def Event_11002547():
    """Event 11002547"""
    if FlagEnabled(11000546):
        return
    
    MAIN.Await(FlagEnabled(11008546))
    
    EnableNetworkFlag(11000546)
    DisableAssetActivation(Assets.AEG227_050_0509, obj_act_id=1227050)


@RestartOnRest(11002580)
def Event_11002580():
    """Event 11002580"""
    RegisterLadder(start_climbing_flag=11000580, stop_climbing_flag=11000581, asset=Assets.AEG227_020_0500)
    RegisterLadder(start_climbing_flag=11000582, stop_climbing_flag=11000583, asset=Assets.AEG227_021_0500)
    RegisterLadder(start_climbing_flag=11000584, stop_climbing_flag=11000585, asset=Assets.AEG227_022_0500)
    RegisterLadder(start_climbing_flag=11000586, stop_climbing_flag=11000587, asset=Assets.AEG227_023_0500)
    RegisterLadder(start_climbing_flag=11000588, stop_climbing_flag=11000589, asset=Assets.AEG227_024_0500)
    RegisterLadder(start_climbing_flag=11000590, stop_climbing_flag=11000591, asset=Assets.AEG227_025_0500)
    RegisterLadder(start_climbing_flag=11000592, stop_climbing_flag=11000593, asset=Assets.AEG227_026_0500)
    RegisterLadder(start_climbing_flag=11000594, stop_climbing_flag=11000595, asset=11001594)
    RegisterLadder(start_climbing_flag=11000596, stop_climbing_flag=11000597, asset=Assets.AEG227_031_0500)


@RestartOnRest(11000600)
def Event_11000600():
    """Event 11000600"""
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    WaitFrames(frames=2)
    DisableAssetActivation(Assets.AEG227_052_0500, obj_act_id=-1)
    AND_1.Add(FlagEnabled(11000535))
    AND_1.Add(FlagDisabled(11000537))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagEnabled():
        return
    EnableThisNetworkSlotFlag()
    End()


@RestartOnRest(11002601)
def Event_11002601():
    """Event 11002601"""
    MAIN.Await(FlagEnabled(11000601))
    
    ForceAnimation(PLAYER, 60131)
    EnableFlag(9080)
    DisableFlag(11000601)


@ContinueOnRest(11002603)
def Event_11002603():
    """Event 11002603"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(11000603):
        return
    AND_1.Add(FlagEnabled(11000603))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=11002500))
    
    MAIN.Await(AND_1)
    
    SetCameraAngle(x_angle=11.899999618530273, y_angle=1.1100000143051147)
    DisableFlag(11000603)


@RestartOnRest(11002604)
def Event_11002604():
    """Event 11002604"""
    MAIN.Await(FlagEnabled(11008556))
    
    EnableFlag(11058556)


@RestartOnRest(11002690)
def Event_11002690():
    """Event 11002690"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        DeleteVFX(11003690, erase_root_only=False)
    AND_1.Add(InsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=11002690))
    
    MAIN.Await(AND_1)
    
    CreateVFX(11003690)
    Wait(1.0)
    OR_1.Add(OutsideMap(game_map=LEYNDELL_ROYAL_CAPITAL))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=11002690))
    
    MAIN.Await(OR_1)
    
    DeleteVFX(11003690)
    Wait(1.0)
    Restart()


@RestartOnRest(11002691)
def Event_11002691(_, asset: Asset | int):
    """Event 11002691"""
    EnableAssetInvulnerability(asset)


@RestartOnRest(11002696)
def Event_11002696():
    """Event 11002696"""
    if FlagEnabled(11007992):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9531, entity=11001696))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(11001010, host_only=False)
    End()


@RestartOnRest(11002697)
def Event_11002697():
    """Event 11002697"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(710880))
    AND_1.Add(FlagDisabled(69480))
    AND_1.Add(FlagDisabled(2051))
    AND_1.Add(FlagDisabled(2052))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    DisplayTutorialMessage(tutorial_param_id=1880, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69480):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9153, flag=710880, bit_count=1)
    EnableFlag(69480)


@RestartOnRest(11002698)
def Event_11002698():
    """Event 11002698"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(710850))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=11002698))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(710850)
    EnableFlag(60350)
    if FlagDisabled(6080):
        EnableFlag(6080)
        StartPS5Activity(activity_id=7)
    WaitFrames(frames=1)
    DisplayTutorialMessage(tutorial_param_id=1850, unk_4_5=True, unk_5_6=True)
    if FlagDisabled(69450):
        GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9150, flag=710850, bit_count=1)
    WaitFrames(frames=1)
    EnableFlag(69450)


@ContinueOnRest(11002699)
def Event_11002699():
    """Event 11002699"""
    if FlagEnabled(11008556):
        return
    GotoIfMultiplayer(Label.L0)
    GotoIfMultiplayerPending(Label.L0)
    EnableAssetActivation(11001699, obj_act_id=227030)
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    
    MAIN.Await(OR_1)
    
    DisableAssetActivation(11001699, obj_act_id=227030)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAssetActivation(11001699, obj_act_id=227030)
    OR_2.Add(Multiplayer())
    OR_2.Add(MultiplayerPending())
    
    MAIN.Await(not OR_2)
    
    EnableAssetActivation(11001699, obj_act_id=227030)
    Restart()


@RestartOnRest(11002800)
def Event_11002800():
    """Event 11002800"""
    if FlagEnabled(11000800):
        return
    
    MAIN.Await(HealthValue(Characters.Margit) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(11008000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Margit))
    
    KillBossAndDisplayBanner(character=Characters.Margit, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    DisableAsset(Assets.AEG220_800_3500)
    EnableMapCollision(collision=11004821)
    WaitFrames(frames=1)
    DisableMapCollision(collision=11004820)
    EnableFlag(11000800)
    EnableFlag(9104)
    if PlayerInOwnWorld():
        EnableFlag(61104)
    if FlagDisabled(10000850):
        EnableFlag(10000850)
    if FlagDisabled(9100):
        EnableFlag(9100)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SkipLinesIfFlagEnabled(1, 61100)
    EnableFlag(61100)
    if FlagDisabled(10000850):
        DisableCharacter(m10_00_00_00_Characters.Margit)
        DisableAnimations(m10_00_00_00_Characters.Margit)
        Kill(m10_00_00_00_Characters.Margit)
    if PlayerNotInOwnWorld():
        return
    SetRespawnPoint(respawn_point=11002020)
    SaveRequest()


@RestartOnRest(11002810)
def Event_11002810():
    """Event 11002810"""
    GotoIfFlagDisabled(Label.L0, flag=11000800)
    DisableCharacter(11005800)
    DisableAnimations(11005800)
    Kill(11005800)
    DisableAsset(Assets.AEG220_800_3500)
    DisableMapCollision(collision=11004820)
    DisableAsset(11006830)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(11005800)
    DisableAsset(Assets.AEG220_800_3500)
    DisableMapCollision(collision=11004820)
    DisableAnimations(Characters.Margit)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=11000801)
    Move(
        Characters.Margit,
        destination=11002810,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.Margit,
    )
    ForceAnimation(Characters.Margit, 30000)
    AND_1.Add(FlagEnabled(11002805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=11002800))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=11000040,
            cutscene_flags=0,
            move_to_region=11002812,
            map_id=11000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(11000040, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    EnableNetworkFlag(11000801)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=14.420000076293945, y_angle=-37.689998626708984)
    DisableAsset(11006830)
    Move(Characters.Margit, destination=11002811, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.Margit, 20000)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(11006830)
    AND_2.Add(FlagEnabled(11002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=11002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAnimations(Characters.Margit)
    EnableAI(11005800)
    SetNetworkUpdateRate(11005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Margit, name=902130002)


@RestartOnRest(11002811)
def Event_11002811():
    """Event 11002811"""
    if FlagEnabled(11000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.Margit, 16205))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11002802)
    EnableAsset(Assets.AEG220_800_3500)
    EnableMapCollision(collision=11004820)
    WaitFrames(frames=1)
    DisableMapCollision(collision=11004821)
    EnableBossHealthBar(Characters.Margit, name=902130003)


@RestartOnRest(11002829)
def Event_11002829():
    """Event 11002829"""
    CommonFunc_9005800(
        0,
        flag=11000800,
        entity=Assets.AEG099_001_9000,
        region=11002800,
        flag_1=11002805,
        character=11005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=11000800,
        entity=Assets.AEG099_001_9000,
        region=11002800,
        flag_1=11002805,
        flag_2=11002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=11000501, asset=Assets.AEG099_001_9000, vfx_id=17, right=0)
    CommonFunc_9005811(0, flag=11000800, asset=Assets.AEG099_002_9001, vfx_id=18, right=11000801)
    CommonFunc_9005822(
        0,
        flag=11000800,
        bgm_boss_conv_param_id=213001,
        flag_1=11002805,
        flag_2=11002806,
        right=0,
        flag_3=11002802,
        left=0,
        left_1=0,
    )


@RestartOnRest(11002850)
def Event_11002850():
    """Event 11002850"""
    if FlagEnabled(11000850):
        return
    
    MAIN.Await(HealthValue(Characters.Godfrey) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(11008050, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Godfrey))
    
    KillBossAndDisplayBanner(character=Characters.Godfrey, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(11000850)
    EnableFlag(9105)
    if PlayerInOwnWorld():
        EnableFlag(61105)


@RestartOnRest(11002860)
def Event_11002860():
    """Event 11002860"""
    GotoIfFlagDisabled(Label.L0, flag=11000850)
    DisableCharacter(11005850)
    DisableAnimations(11005850)
    Kill(11005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(11005850)
    GotoIfFlagEnabled(Label.L1, flag=11000851)
    ForceAnimation(Characters.Godfrey, 30000, loop=True)
    DisableCharacter(Characters.Godfrey)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=Characters.Godfrey, other_entity=PLAYER, radius=25.0))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=m10_00_00_00_Characters.Margit))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(11000851)
    ForceAnimation(Characters.Godfrey, 20000)
    EnableCharacter(Characters.Godfrey)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(11002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=11002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.Godfrey)
    SetNetworkUpdateRate(11005850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Godfrey, name=904720002)


@RestartOnRest(11002861)
def Event_11002861():
    """Event 11002861"""
    if FlagEnabled(11000850):
        return
    AND_1.Add(HealthRatio(Characters.Godfrey) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11002852)


@RestartOnRest(11002859)
def Event_11002859():
    """Event 11002859"""
    CommonFunc_9005800(
        0,
        flag=11000850,
        entity=Assets.AEG099_001_9003,
        region=11002850,
        flag_1=11002855,
        character=11005850,
        action_button_id=10000,
        left=11000851,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=11000850,
        entity=Assets.AEG099_001_9003,
        region=11002850,
        flag_1=11002855,
        flag_2=11002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9003, vfx_id=4, right=11000851)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9004, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9005, vfx_id=4, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9006, vfx_id=4, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_002_9000, vfx_id=19, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9007, vfx_id=5, right=0)
    CommonFunc_9005811(0, flag=11000850, asset=Assets.AEG099_001_9008, vfx_id=5, right=0)
    CommonFunc_9005822(
        0,
        flag=11000850,
        bgm_boss_conv_param_id=472001,
        flag_1=11002855,
        flag_2=11002856,
        right=0,
        flag_3=11002852,
        left=0,
        left_1=0,
    )


@RestartOnRest(11002910)
def Event_11002910():
    """Event 11002910"""
    AND_1.Add(FlagEnabled(11000800))
    AND_1.Add(FlagEnabled(130))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(11001920)
    CreateAssetVFX(11001920, dummy_id=100, vfx_id=30)


@ContinueOnRest(11002920)
def Event_11002920(_, flag: Flag | int, anchor_entity: uint):
    """Event 11002920"""
    DisableNetworkSync()
    OR_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=anchor_entity))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=10010170, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(11003710)
def Event_11003710(_, character: uint):
    """Event 11003710"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    if FlagEnabled(3940):
        DisableFlag(1043379353)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L5, flag=3947)
    
    MAIN.Await(FlagEnabled(3947))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(4, 3957)
    SkipLinesIfFlagEnabled(3, 11109819)
    AND_6.Add(FlagEnabled(71102))
    AND_6.Add(FlagEnabled(9000))
    AwaitConditionTrue(AND_6)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    EnableNetworkFlag(11109819)
    EnableNetworkFlag(3957)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3947))
    
    Restart()


@RestartOnRest(11003711)
def Event_11003711(_, entity: uint):
    """Event 11003711"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(3943))
    OR_1.Add(FlagDisabled(3947))
    OR_1.Add(FlagEnabled(1039409259))
    if OR_1:
        return
    AND_1.Add(EntityWithinDistance(entity=entity, other_entity=ALL_PLAYERS, radius=4.0))
    AND_1.Add(CharacterHasSpecialEffect(ALL_PLAYERS, 9690))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1039402710)
    End()


@RestartOnRest(11003715)
def Event_11003715(_, character: uint):
    """Event 11003715"""
    DisableCharacter(character)
    DisableBackread(character)
    SetCharacterTalkRange(character=character, distance=17.0)
    GotoIfFlagEnabled(Label.L0, flag=11000800)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character, distance=120.0)
    EnableCharacter(character)
    EnableBackread(character)
    Move(character, destination=11002721, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 930000)
    if FlagEnabled(11009405):
        ForceAnimation(character, 930002)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AwaitFlagEnabled(flag=11000800)
    SetCharacterTalkRange(character=character, distance=120.0)
    EnableCharacter(character)
    EnableBackread(character)
    Move(
        character,
        destination=Characters.Margit,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        short_move=True,
    )
    ForceAnimation(character, 930000)
    if FlagEnabled(11009405):
        ForceAnimation(character, 930002)
    End()


@RestartOnRest(11003720)
def Event_11003720(_, character: uint):
    """Event 11003720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4200):
        DisableFlag(1040529253)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4208))
    AND_1.Add(FlagEnabled(4209))
    AND_1.Add(FlagEnabled(11009554))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(4208))
    AND_2.Add(FlagEnabled(4209))
    AND_2.Add(FlagEnabled(11009554))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4200)
    GotoIfFlagEnabled(Label.L2, flag=4201)
    GotoIfFlagEnabled(Label.L4, flag=4203)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 90101)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_3.Add(FlagEnabled(4208))
    AND_3.Add(FlagEnabled(4209))
    AND_3.Add(FlagEnabled(11009554))
    OR_3.Add(AND_3)
    
    MAIN.Await(not OR_3)
    
    Restart()


@RestartOnRest(11003721)
def Event_11003721(_, character: uint):
    """Event 11003721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagDisabled(4203))
    AND_1.Add(FlagEnabled(4208))
    AND_2.Add(FlagEnabled(4203))
    AND_2.Add(FlagDisabled(4217))
    AND_2.Add(FlagDisabled(1051569454))
    AND_2.Add(FlagDisabled(11059304))
    AND_3.Add(FlagDisabled(4217))
    AND_3.Add(FlagEnabled(11009554))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930007)
    if FlagEnabled(11009555):
        ForceAnimation(character, 930009)
    DisableNetworkFlag(1040549254)
    EnableNetworkFlag(11009554)
    DisableNetworkFlag(1051569454)
    DisableNetworkFlag(11059304)
    AND_5.Add(FlagDisabled(4203))
    AND_5.Add(FlagEnabled(4208))
    AND_6.Add(FlagEnabled(4203))
    AND_6.Add(FlagDisabled(4217))
    AND_6.Add(FlagDisabled(1051569454))
    AND_6.Add(FlagDisabled(11059304))
    AND_7.Add(FlagDisabled(4217))
    AND_7.Add(FlagEnabled(11009554))
    OR_5.Add(AND_5)
    OR_5.Add(AND_6)
    OR_5.Add(AND_7)
    
    MAIN.Await(not OR_5)
    
    Restart()


@RestartOnRest(11003722)
def Event_11003722(_, character: uint):
    """Event 11003722"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    EnableNetworkFlag(1040542710)
    if FlagEnabled(11009555):
        ForceAnimation(character, 20014, wait_for_completion=True, skip_transition=True)
    if FlagDisabled(11009555):
        ForceAnimation(character, 20013, wait_for_completion=True, skip_transition=True)
    End()


@RestartOnRest(11003723)
def Event_11003723(_, other_entity: uint):
    """Event 11003723"""
    if FlagEnabled(11009556):
        DisableAsset(Assets.AEG228_275_1000)
        End()
    DisableAsset(Assets.AEG228_278_1000)
    EnableNetworkFlag(11009468)
    AND_1.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=4.0))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(ALL_PLAYERS, 1673014))
    AwaitConditionTrue(AND_1)
    CreateTemporaryVFX(vfx_id=811630, anchor_entity=Assets.AEG099_090_9001, anchor_type=CoordEntityType.Asset)
    ForceAnimation(Assets.AEG228_275_1000, 1)
    EnableAsset(Assets.AEG228_278_1000)
    ForceAnimation(Assets.AEG228_278_1000, 1)
    EnableNetworkFlag(11009556)
    EnableNetworkFlag(11009469)
    DisableNetworkFlag(11009468)
    End()


@RestartOnRest(11003724)
def Event_11003724():
    """Event 11003724"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=Characters.BrotherCorhyn, distance=17.0)
    if FlagEnabled(11009460):
        return
    SetCharacterTalkRange(character=Characters.BrotherCorhyn, distance=160.0)
    AND_1.Add(FlagEnabled(4208))
    AND_1.Add(FlagDisabled(11009460))
    AND_1.Add(FlagDisabled(11002734))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=11002740))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(11002733)
    End()


@RestartOnRest(11003725)
def Event_11003725(_, character: uint):
    """Event 11003725"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(4700):
        DisableFlag(1042369283)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=4707)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(4707))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4700)
    GotoIfFlagEnabled(Label.L2, flag=4701)
    GotoIfFlagEnabled(Label.L3, flag=4702)
    GotoIfFlagEnabled(Label.L4, flag=4703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 30003)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagEnabled(4707))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(11003730)
def Event_11003730():
    """Event 11003730"""
    WaitFrames(frames=1)
    DisableFlag(11009500)
    if FlagDisabled(16009458):
        return
    if FlagDisabled(3886):
        return
    EnableFlag(11009500)
    End()


@RestartOnRest(11003740)
def Event_11003740():
    """Event 11003740"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4247):
        return
    AwaitFlagEnabled(flag=1045520180)
    DisableNetworkFlag(35009317)
    DisableNetworkFlag(35009318)
    End()


@RestartOnRest(11003741)
def Event_11003741():
    """Event 11003741"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4246):
        return
    AND_1.Add(FlagEnabled(4240))
    AND_1.Add(FlagEnabled(35009306))
    AND_1.Add(EntityWithinDistance(entity=Assets.AEG099_060_9007, other_entity=ALL_PLAYERS, radius=13.0))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(4258)
    End()
