"""
Mohgwyn Palace

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
from .entities.m12_05_00_00_entities import *
from .entities.m60_35_45_00_entities import Characters as m60_35_Characters


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=71251, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=71252, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=71253, asset=Assets.AEG099_060_9003)
    CommonFunc_9005810(
        0,
        flag=12050800,
        grace_flag=12050000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_12052800()
    Event_12052810()
    Event_12052811()
    Event_12052849()
    Event_12052847()
    Event_12052848()
    Event_12052820()
    Event_12052821()
    Event_12052822()
    Event_12052823()
    Event_12052824()
    Event_12052825()
    Event_12052826()
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric0,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric2,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric3,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric4,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric5,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric6,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric7,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005251(0, 12050208, 40.0, 0.0, -1)
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric9,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric11,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric12,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005251(0, 12050213, 50.0, 0.0, -1)
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric14,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric15,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric16,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Albinauric17,
        animation_id=30003,
        animation_id_1=20003,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(0, character=12050218, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=12050219, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005271(0, 12050200, 0.0, -1)
    CommonFunc_90005271(0, 12050202, 0.0, -1)
    CommonFunc_90005271(0, 12050203, 0.0, -1)
    CommonFunc_90005271(0, 12050204, 0.0, -1)
    CommonFunc_90005271(0, 12050205, 0.0, -1)
    CommonFunc_90005271(0, 12050206, 0.0, -1)
    CommonFunc_90005271(0, 12050207, 0.0, -1)
    CommonFunc_90005271(0, 12050209, 0.0, -1)
    CommonFunc_90005271(0, 12050211, 0.0, -1)
    CommonFunc_90005271(0, 12050212, 0.0, -1)
    CommonFunc_90005271(0, 12050214, 0.0, -1)
    CommonFunc_90005271(0, 12050215, 0.0, -1)
    CommonFunc_90005271(0, 12050216, 0.0, -1)
    CommonFunc_90005271(0, 12050217, 0.0, -1)
    CommonFunc_90005271(0, 12050218, 0.0, -1)
    CommonFunc_90005271(0, 12050219, 0.0, -1)
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric18,
        animation_id=30002,
        animation_id_1=20002,
        region=12052224,
        radius=1.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric19,
        animation_id=30002,
        animation_id_1=20002,
        region=12052224,
        radius=1.0,
        seconds=4.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric20,
        animation_id=30002,
        animation_id_1=20002,
        region=12052224,
        radius=1.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric21,
        animation_id=30002,
        animation_id_1=20002,
        region=12052224,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric22,
        animation_id=30002,
        animation_id_1=20002,
        region=12052224,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 12055220, 12052220, 0.0, -1)
    CommonFunc_90005211(
        0,
        character=Characters.Albinauric23,
        animation_id=30001,
        animation_id_1=20001,
        region=12052232,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=12050233,
        animation_id=30001,
        animation_id_1=20001,
        region=12052232,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 12050240, 12052240, 0.0, -1)
    CommonFunc_90005250(0, 12050241, 12052240, 0.0, -1)
    CommonFunc_90005271(0, 12055240, 0.0, -1)
    Event_12052250(
        0,
        character=Characters.Albinauric2_0,
        frames=0,
        entity=Characters.GiantSkeletonTorso0,
        animation_id=30010,
        animation_id_1=20010,
    )
    Event_12052251(
        1,
        character=Characters.Albinauric2_1,
        frames=1,
        entity=Characters.GiantSkeletonTorso1,
        animation_id=30012,
        animation_id_1=20012,
    )
    Event_12052251(
        2,
        character=Characters.Albinauric2_2,
        frames=1,
        entity=Characters.GiantSkeletonTorso2,
        animation_id=30011,
        animation_id_1=20011,
    )
    Event_12052251(
        3,
        character=Characters.Albinauric2_3,
        frames=1,
        entity=Characters.GiantSkeletonTorso3,
        animation_id=30010,
        animation_id_1=20010,
    )
    CommonFunc_90005251(0, 12055260, 20.0, 0.0, -1)
    CommonFunc_90005251(0, 12055268, 20.0, 0.0, -1)
    CommonFunc_90005251(0, 12055270, 40.0, 1.5, -1)
    CommonFunc_90005251(0, 12055261, 15.0, 0.0, -1)
    CommonFunc_90005251(0, 12050261, 25.0, 0.0, -1)
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse1,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30006,
        animation_id_1=20006,
        radius=20.0,
        seconds=7.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse3,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse6,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse7,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse10,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse11,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse12,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse13,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse14,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse15,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse16,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse17,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse18,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse19,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse20,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse21,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse22,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse23,
        animation_id=30006,
        animation_id_1=20006,
        region=12052297,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse24,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse25,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse26,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse27,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse28,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse29,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse30,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse31,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse32,
        animation_id=30006,
        animation_id_1=20006,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(0, 12050310, 12052311, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050311, 12052314, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050312, 12052314, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050313, 12052311, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050314, 12052311, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050315, 12052311, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050316, 12052311, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050317, 12052312, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050318, 12052312, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050319, 12052312, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050320, 12052313, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050321, 12052313, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050322, 12052313, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050323, 12052313, 1.0, 0.0, -1)
    CommonFunc_90005261(0, 12050324, 12052313, 1.0, 0.0, -1)
    CommonFunc_90005261(0, character=12050342, region=12052342, radius=20.0, seconds=0.0, animation_id=20000)
    Event_12052200()
    CommonFunc_90005250(0, 12050346, 12052346, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.SanguineNoble0,
        animation_id=30000,
        animation_id_1=20000,
        region=12052350,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, 12050351, 12052351, 0.0, -1)
    CommonFunc_90005200(
        0,
        character=Characters.SanguineNoble2,
        animation_id=30000,
        animation_id_1=20000,
        region=12052352,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SanguineNoble3,
        animation_id=30000,
        animation_id_1=20000,
        region=12052353,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_12052360(0, character=Characters.GiantSkeletonTorso0, character_1=Characters.Albinauric2_0)
    Event_12052360(1, character=Characters.GiantSkeletonTorso1, character_1=Characters.Albinauric2_1)
    Event_12052360(2, character=Characters.GiantSkeletonTorso2, character_1=Characters.Albinauric2_2)
    Event_12052360(3, character=Characters.GiantSkeletonTorso3, character_1=Characters.Albinauric2_3)
    CommonFunc_90005251(0, 12050370, 60.0, 0.0, -1)
    CommonFunc_90005300(0, flag=12050400, character=12050400, item_lot_param_id=40680, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12050401, character=12050401, item_lot_param_id=40682, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12050402, character=12050402, item_lot_param_id=40684, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12050403, character=Characters.Scarab, item_lot_param_id=40686, seconds=1.5, left=0)
    CommonFunc_90005790(
        0,
        right=12050800,
        flag=12050410,
        summon_flag=12052410,
        dismissal_flag=12052411,
        character=Characters.NamelessWhiteMask0,
        sign_type=21,
        region=12052410,
        region_1=12052411,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=12050410, flag_1=12052410, flag_2=12052411, character=Characters.NamelessWhiteMask0)
    CommonFunc_90005792(
        0,
        flag=12050410,
        flag_1=12052410,
        flag_2=12052411,
        character=Characters.NamelessWhiteMask0,
        item_lot_param_id=0,
        seconds=0.0,
    )
    CommonFunc_90005790(
        0,
        right=12050800,
        flag=12050412,
        summon_flag=12052412,
        dismissal_flag=12052413,
        character=Characters.NamelessWhiteMask1,
        sign_type=22,
        region=12052412,
        region_1=12052413,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=12050412, flag_1=12052412, flag_2=12052413, character=Characters.NamelessWhiteMask1)
    CommonFunc_90005792(
        0,
        flag=12050412,
        flag_1=12052412,
        flag_2=12052413,
        character=Characters.NamelessWhiteMask1,
        item_lot_param_id=12050950,
        seconds=0.0,
    )
    CommonFunc_90005790(
        0,
        right=12050800,
        flag=12050414,
        summon_flag=12052414,
        dismissal_flag=12052415,
        character=Characters.NamelessWhiteMask2,
        sign_type=23,
        region=12052414,
        region_1=12052415,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=12050414, flag_1=12052414, flag_2=12052415, character=Characters.NamelessWhiteMask2)
    CommonFunc_90005792(
        0,
        flag=12050414,
        flag_1=12052414,
        flag_2=12052415,
        character=Characters.NamelessWhiteMask2,
        item_lot_param_id=0,
        seconds=0.0,
    )
    CommonFunc_90005501(
        0,
        flag=12050510,
        flag_1=12050511,
        left=0,
        asset=Assets.AEG239_013_0500,
        asset_1=Assets.AEG239_021_0500,
        asset_2=Assets.AEG239_023_0500,
        flag_2=12050512,
    )
    Event_12052510()
    Event_12052680()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9004, vfx_id=100, model_point=800, right=0)
    Event_12052601(0, source_entity=Assets.AEG099_048_9000, seconds=0.0)
    Event_12052601(1, source_entity=Assets.AEG099_048_9001, seconds=1.0)
    Event_12052601(5, source_entity=Assets.AEG099_048_9005, seconds=4.0)
    Event_12052601(6, source_entity=Assets.AEG099_048_9006, seconds=3.0)
    Event_12052601(7, source_entity=12051607, seconds=2.0)
    Event_12052601(8, source_entity=12051608, seconds=1.5)
    Event_12052601(9, source_entity=Assets.AEG099_048_9009, seconds=0.5)
    Event_12052601(11, source_entity=Assets.AEG099_048_9011, seconds=3.0)
    Event_12052620(0, asset=Assets.AEG099_090_9000, flag=12050410, flag_1=12052410, region=12052411)
    Event_12052620(1, asset=Assets.AEG099_090_9002, flag=12050412, flag_1=12052412, region=12052413)
    Event_12052620(2, asset=Assets.AEG099_090_9003, flag=12050414, flag_1=12052414, region=12052415)
    Event_12052201()
    CommonFunc_90005795(
        0,
        flag=7601,
        flag_1=0,
        flag_2=1042369259,
        left_flag=12052141,
        cancel_flag__right_flag=12052142,
        message=80601,
        action_button_id=9000,
        asset=Assets.AEG099_090_9001,
        model_point=30010,
    )
    SkipLinesIfCeremonyInactive(line_count=2, ceremony=20)
    CommonFunc_90005796(0, flag=7601, character=Characters.WhiteMaskVarre0, banner_type=5, region=12052141)
    Event_1039532145()
    Event_12052690()
    Event_12053700(0, character=Characters.Mohg, character_1=0, flag=9112, flag_1=12052805, distance=145.0)
    Event_12053701(0, character=Characters.Mohg)
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4811,
        flag_1=4812,
        flag_2=12059106,
        flag_3=4811,
        first_flag=4810,
        last_flag=4814,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4811, flag_1=4810, flag_2=12059106, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4813, first_flag=4810, last_flag=4814)
    CommonFunc_90005725(
        0,
        flag=4810,
        flag_1=4811,
        flag_2=4813,
        flag_3=12059105,
        character=Characters.Merchant,
        character_1=m60_35_Characters.NomadMule,
        asset=12056700,
    )
    Event_12053710(0, character=Characters.WhiteMaskVarre1)
    Event_12053711(0, character=Characters.WhiteMaskVarre1)
    Event_12053712()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9001,
        action_button_id=4350,
        item_lot_param_id=100360,
        first_flag=400036,
        last_flag=400037,
        flag=12059166,
        model_point=0,
    )
    CommonFunc_90005702(0, 12050702, 3183, 3180, 3184)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(12050700)
    DisableBackread(12050701)
    DisableBackread(Characters.WhiteMaskVarre1)
    DisableBackread(Characters.WhiteMaskVarre0)
    DisableBackread(Characters.Merchant)
    DisableBackread(12050715)


@RestartOnRest(1039532145)
def Event_1039532145():
    """Event 1039532145"""
    ReturnIfCeremonyState(event_return_type=EventReturnType.End, state=False, ceremony=20)
    EnableBackread(Characters.WhiteMaskVarre0)
    SetTeamType(Characters.WhiteMaskVarre0, TeamType.Human)
    DeleteAssetVFX(12056710)
    CreateAssetVFX(12056710, vfx_id=200, model_point=806700)


@RestartOnRest(12052600)
def Event_12052600():
    """Event 12052600"""
    SetTeamType(Characters.Dummy2, TeamType.Boss)
    CreateProjectileOwner(entity=Characters.Dummy2)


@RestartOnRest(12052601)
def Event_12052601(_, source_entity: uint, seconds: float):
    """Event 12052601"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    DisableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy2,
            source_entity=source_entity,
            model_point=-1,
            behavior_id=802900060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L10)
    ShootProjectile(
        owner_entity=Characters.Dummy2,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802900070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    WaitRandomSeconds(min_seconds=6.0, max_seconds=10.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(12052620)
def Event_12052620(_, asset: uint, flag: uint, flag_1: uint, region: uint):
    """Event 12052620"""
    if FlagEnabled(flag):
        return
    CreateAssetVFX(asset, vfx_id=100, model_point=812610)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(OR_1)
    AND_14.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_14.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_14)
    
    DeleteAssetVFX(asset)
    WaitFrames(frames=1)
    CreateAssetVFX(asset, vfx_id=100, model_point=812611)
    Wait(4.0)
    DeleteAssetVFX(asset)


@RestartOnRest(12052200)
def Event_12052200():
    """Event 12052200"""
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.MohgwynMonstrousCrow0)
    ForceAnimation(Characters.MohgwynMonstrousCrow0, 30013, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=12052343))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.MohgwynMonstrousCrow0, radius=20.0))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(Characters.MohgwynMonstrousCrow0))
    OR_11.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 5080))
    OR_11.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 5450))
    AND_1.Add(OR_11)
    AND_4.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.MohgwynMonstrousCrow0, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.MohgwynMonstrousCrow0, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.MohgwynMonstrousCrow0, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.MohgwynMonstrousCrow0, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.MohgwynMonstrousCrow0, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.MohgwynMonstrousCrow0, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.MohgwynMonstrousCrow0, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.MohgwynMonstrousCrow0, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(
        Characters.MohgwynMonstrousCrow0,
        is_fixed=True,
        update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames,
    )
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=Characters.MohgwynMonstrousCrow0, state=True)
    ForceAnimation(Characters.MohgwynMonstrousCrow0, 20000, loop=True)
    Wait(3.0)
    SetNetworkUpdateRate(Characters.MohgwynMonstrousCrow0, is_fixed=False, update_rate=CharacterUpdateRate.Never)


@RestartOnRest(12052201)
def Event_12052201():
    """Event 12052201"""
    if ThisEventSlotFlagEnabled():
        return
    CreateTemporaryVFX(vfx_id=30010, anchor_entity=12052700, anchor_type=CoordEntityType.Region)


@RestartOnRest(12052250)
def Event_12052250(_, character: uint, frames: int, entity: uint, animation_id: int, animation_id_1: int):
    """Event 12052250"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(entity, animation_id, loop=True, wait_for_completion=True)
    AND_14.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_14)
    
    ForceAnimation(character, 3007, loop=True, wait_for_completion=True)
    ForceAnimation(entity, animation_id_1, loop=True, wait_for_completion=True)
    End()
    WaitFrames(frames=frames)


@RestartOnRest(12052251)
def Event_12052251(_, character: uint, frames: int, entity: uint, animation_id: int, animation_id_1: int):
    """Event 12052251"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(entity, animation_id, loop=True, wait_for_completion=True)
    AND_14.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_14)
    
    ForceAnimation(character, 3007, loop=True, wait_for_completion=True)
    ForceAnimation(entity, animation_id_1, loop=True, wait_for_completion=True)
    End()
    WaitFrames(frames=frames)


@RestartOnRest(12052360)
def Event_12052360(_, character: uint, character_1: uint):
    """Event 12052360"""
    OR_15.Add(CharacterDead(character_1))
    OR_15.Add(HealthRatio(character_1) <= 0.5)
    SkipLinesIfConditionFalse(2, OR_15)
    Kill(character)
    End()
    OR_12.Add(CharacterDead(character_1))
    OR_12.Add(HealthRatio(character_1) <= 0.5)
    
    MAIN.Await(OR_12)
    
    Kill(character)
    End()


@RestartOnRest(12052680)
def Event_12052680():
    """Event 12052680"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        DeleteVFX(12053680, erase_root_only=False)
    OR_1.Add(PlayerStandingOnCollision(12054681))
    OR_1.Add(PlayerStandingOnCollision(12054682))
    OR_1.Add(PlayerStandingOnCollision(12054683))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12052680))
    
    MAIN.Await(AND_1)
    
    CreateVFX(12053680)
    Wait(1.0)
    OR_2.Add(CharacterOutsideRegion(character=PLAYER, region=12052680))
    OR_2.Add(PlayerStandingOnCollision(12054681))
    OR_2.Add(PlayerStandingOnCollision(12054682))
    OR_2.Add(PlayerStandingOnCollision(12054683))
    
    MAIN.Await(OR_2)
    
    DeleteVFX(12053680)
    Wait(1.0)
    Restart()


@RestartOnRest(12052690)
def Event_12052690():
    """Event 12052690"""
    DisableNetworkSync()
    AwaitFlagEnabled(flag=12052140)
    AddSpecialEffect(Characters.TalkDummy5, 9531)
    AwaitFlagDisabled(flag=12052140)
    AddSpecialEffect(Characters.TalkDummy5, 9532)
    Wait(1.0)
    Restart()


@RestartOnRest(12052800)
def Event_12052800():
    """Event 12052800"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(HealthValue(Characters.Mohg) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Mohg, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.Mohg))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(12050800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=Characters.Mohg, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    EnableFlag(12050800)
    EnableFlag(9112)
    if PlayerInOwnWorld():
        EnableFlag(61112)


@RestartOnRest(12052810)
def Event_12052810():
    """Event 12052810"""
    GotoIfFlagDisabled(Label.L0, flag=12050800)
    DisableCharacter(Characters.Mohg)
    DisableAnimations(Characters.Mohg)
    Kill(Characters.Mohg)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Mohg)
    GotoIfFlagEnabled(Label.L1, flag=12050801)
    DisableCharacter(Characters.Mohg)
    DisableAnimations(Characters.Mohg)
    SetCharacterFadeOnEnable(character=Characters.Mohg, state=False)
    EnableAsset(Assets.AEG231_036_4000)
    DisableAsset(Assets.AEG231_037_4000)
    DisableAsset(Assets.AEG231_038_4000)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12052801))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Mohg, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(12050801)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=12050020,
            cutscene_flags=0,
            move_to_region=12052805,
            map_id=12050000,
            player_id=10000,
            unk_20_24=12050000,
            unk_24_25=False,
        )
    else:
        PlayCutscene(12050020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableNetworkFlag(12050802)
    EnableCharacter(Characters.Mohg)
    EnableAnimations(Characters.Mohg)
    ForceAnimation(Characters.Mohg, 20020)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAnimations(Characters.Mohg)
    AND_2.Add(FlagEnabled(12052805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12052800))
    
    MAIN.Await(AND_2)
    
    EnableAnimations(Characters.Mohg)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAsset(Assets.AEG231_037_4000)
    DisableAsset(Assets.AEG231_038_4000)
    EnableAI(Characters.Mohg)
    SetNetworkUpdateRate(Characters.Mohg, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Mohg, name=904800000)


@RestartOnRest(12052811)
def Event_12052811():
    """Event 12052811"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10630))
    
    EnableFlag(12052802)


@RestartOnRest(12052820)
def Event_12052820():
    """Event 12052820"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10641))
    
    AddSpecialEffect(PLAYER, 10650)


@RestartOnRest(12052821)
def Event_12052821():
    """Event 12052821"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10642))
    
    AddSpecialEffect(PLAYER, 10651)


@RestartOnRest(12052822)
def Event_12052822():
    """Event 12052822"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10643))
    
    AddSpecialEffect(PLAYER, 10652)


@RestartOnRest(12052823)
def Event_12052823():
    """Event 12052823"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10645))
    
    AddSpecialEffect(PLAYER, 10660)
    AddSpecialEffect(PLAYER, 10665)


@RestartOnRest(12052824)
def Event_12052824():
    """Event 12052824"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10646))
    
    AddSpecialEffect(PLAYER, 10661)
    AddSpecialEffect(PLAYER, 10666)


@RestartOnRest(12052825)
def Event_12052825():
    """Event 12052825"""
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Mohg, 10647))
    
    AddSpecialEffect(PLAYER, 10662)
    AddSpecialEffect(PLAYER, 10667)


@RestartOnRest(12052826)
def Event_12052826():
    """Event 12052826"""
    if FlagEnabled(12050800):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.Mohg, 10648))
    OR_1.Add(CharacterDead(Characters.Mohg))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 10653)


@RestartOnRest(12052847)
def Event_12052847():
    """Event 12052847"""
    if FlagEnabled(12050801):
        return
    
    MAIN.Await(FlagEnabled(12050801))
    
    DisableAsset(Assets.AEG231_036_4000)
    DisableAsset(Assets.AEG231_037_4000)
    EnableAsset(Assets.AEG231_038_4000)
    End()


@RestartOnRest(12052848)
def Event_12052848():
    """Event 12052848"""
    GotoIfFlagDisabled(Label.L0, flag=12050803)
    DisableAsset(Assets.AEG231_036_4000)
    EnableAsset(Assets.AEG231_037_4000)
    DisableAsset(Assets.AEG231_038_4000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(12050802))
    
    DisableAsset(Assets.AEG231_036_4000)
    EnableAsset(Assets.AEG231_037_4000)
    DisableAsset(Assets.AEG231_038_4000)
    EnableNetworkFlag(12050803)
    End()


@RestartOnRest(12052849)
def Event_12052849():
    """Event 12052849"""
    CommonFunc_9005811(0, flag=12050800, asset=Assets.AEG099_001_9000, model_point=12, right=12050801)
    CommonFunc_9005811(0, flag=12050800, asset=Assets.AEG099_001_9001, model_point=12, right=12050801)
    CommonFunc_9005822(
        0,
        flag=12050800,
        bgm_boss_conv_param_id=90003101,
        flag_1=12052805,
        flag_2=12052806,
        right=0,
        flag_3=12052802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=12050800,
        entity=Assets.AEG099_002_9000,
        region=12052800,
        flag_1=12052805,
        character=12055800,
        action_button_id=10000,
        left=12050801,
        region_1=12052801,
    )
    CommonFunc_9005801(
        0,
        flag=12050800,
        entity=Assets.AEG099_002_9000,
        region=12052800,
        flag_1=12052805,
        flag_2=12052806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12050800, asset=Assets.AEG099_002_9000, model_point=4, right=12050801)
    CommonFunc_9005822(0, 12050800, 480000, 12052805, 12052806, 0, 12052802, 0, 0)


@NeverRestart(12052510)
def Event_12052510():
    """Event 12052510"""
    CommonFunc_90005500(
        0,
        12050510,
        12050511,
        0,
        12051510,
        12051511,
        12053511,
        12051512,
        12053512,
        12052511,
        12052512,
        12050512,
        12050513,
        0,
    )


@RestartOnRest(12053700)
def Event_12053700(_, character: uint, character_1: uint, flag: uint, flag_1: uint, distance: float):
    """Event 12053700"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=character, distance=17.0)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=17.0)
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetCharacterTalkRange(character=character, distance=distance)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(12053701)
def Event_12053701(_, character: uint):
    """Event 12053701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(12050800):
        return
    
    MAIN.Await(CharacterDead(character))
    
    SetBackreadStateAlternate(character, True)
    OR_1.Add(FlagEnabled(12059205))
    OR_1.Add(TimeElapsed(seconds=30.0))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(12053710)
def Event_12053710(_, character: uint):
    """Event 12053710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3180):
        DisableFlag(1042369205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3193)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3193))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3180)
    GotoIfFlagEnabled(Label.L2, flag=3181)
    GotoIfFlagEnabled(Label.L3, flag=3182)
    GotoIfFlagEnabled(Label.L4, flag=3183)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90102)
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
    OR_4.Add(FlagEnabled(3193))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(12053711)
def Event_12053711(_, character: uint):
    """Event 12053711"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3183):
        return
    if FlagDisabled(3193):
        return
    MoveAssetToCharacter(Assets.AEG099_090_9001, character=character)
    
    MAIN.Await(FlagEnabled(12059166))
    
    DisableAnimations(character)
    End()


@RestartOnRest(12053712)
def Event_12053712():
    """Event 12053712"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3192):
        return
    EnableFlag(1042369259)
    End()
