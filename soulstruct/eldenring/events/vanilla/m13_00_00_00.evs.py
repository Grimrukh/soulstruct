"""
Crumbling Farum Azula

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
from .entities.m13_00_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=13000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=13000004, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=13000005, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=13000006, asset=Assets.AEG099_060_9006)
    RegisterGrace(grace_flag=13000007, asset=Assets.AEG099_060_9007)
    RegisterGrace(grace_flag=13000008, asset=Assets.AEG099_060_9008)
    RegisterGrace(grace_flag=13000009, asset=Assets.AEG099_060_9009)
    RegisterGrace(grace_flag=13000010, asset=Assets.AEG099_060_9010)
    Event_13002805()
    CommonFunc_9005810(
        0,
        flag=13000830,
        grace_flag=13000001,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9001,
        enemy_block_distance=5.0,
    )
    CommonFunc_9005810(
        0,
        flag=13000850,
        grace_flag=13000002,
        character=Characters.TalkDummy2,
        asset=Assets.AEG099_060_9002,
        enemy_block_distance=5.0,
    )
    Event_13002500()
    Event_13002800()
    Event_13002810()
    Event_13002811()
    Event_13002829()
    Event_13002820()
    Event_13002827()
    Event_13002828()
    Event_13002819()
    Event_13002830()
    Event_13002834()
    Event_13002835()
    Event_13002840()
    Event_13002841()
    Event_13002849()
    Event_13002850()
    Event_13002860()
    Event_13002861()
    Event_13002865()
    Event_13002890(
        0,
        flag=13002944,
        character=Characters.GodskinApostle0,
        character_1=Characters.GodskinNoble,
        special_effect=15504,
    )
    Event_13002891(
        0,
        flag=13002944,
        spawner=13003851,
        character=Characters.GodskinNoble,
        special_effect=15506,
        character_1=Characters.GodskinApostle0,
        flag_1=13002873,
    )
    Event_13002890(
        1,
        flag=13002945,
        character=Characters.GodskinNoble,
        character_1=Characters.GodskinApostle0,
        special_effect=15454,
    )
    Event_13002891(
        1,
        flag=13002945,
        spawner=13003852,
        character=Characters.GodskinApostle0,
        special_effect=15456,
        character_1=Characters.GodskinNoble,
        flag_1=13002874,
    )
    Event_13002892()
    Event_13002236(0, region=13002314, character=Characters.BeastmanofFarumAzula29)
    CommonFunc_90005300(0, flag=13000340, character=13000340, item_lot=40770, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000341, character=Characters.Scarab, item_lot=40772, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000342, character=13000342, item_lot=40774, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000343, character=13000343, item_lot=40776, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000369, character=Characters.WormfaceLarge, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000490, character=Characters.AncientDragon0, item_lot=13002091, seconds=0.0, left=0)
    Event_13002493(0, character=Characters.AncientDragon0, region=13002641, region_1=13002640)
    Event_13002646(0, flag=13000492, region=13002492, character=Characters.AncientDragon1, seconds=10.0)
    CommonFunc_90005300(0, flag=13000494, character=Characters.AncientDragon2, item_lot=0, seconds=0.0, left=0)
    Event_13002493(2, character=Characters.AncientDragon2, region=13002645, region_1=13002494)
    Event_13002646(1, flag=13000494, region=13002646, character=Characters.AncientDragon2, seconds=10.0)
    Event_13002610()
    CommonFunc_90005300(0, flag=13000495, character=Characters.AncientDragon3, item_lot=13002093, seconds=0.0, left=0)
    Event_13002646(2, flag=13000495, region=13002495, character=Characters.AncientDragon3, seconds=1.0)
    CommonFunc_90005300(0, flag=13000701, character=Characters.AncientDragon4, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000702, character=Characters.AncientDragon5, item_lot=0, seconds=0.0, left=0)
    Event_13002493(3, character=Characters.AncientDragon5, region=13002497, region_1=13002493)
    CommonFunc_90005300(0, flag=13000295, character=Characters.CrucibleKnight0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=13000296, character=Characters.CrucibleKnight1, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(
        0,
        flag=13000496,
        character=Characters.DraconicTreeSentinel,
        item_lot=13002095,
        seconds=2.0,
        left=0,
    )
    Event_13002580()
    Event_13002510()
    CommonFunc_90005501(
        0,
        flag=13000510,
        flag_1=13000511,
        left=0,
        asset=Assets.AEG247_002_0500,
        asset_1=Assets.AEG247_003_0500,
        asset_2=Assets.AEG247_003_0501,
        flag_2=13000512,
    )
    CommonFunc_90005501(
        0,
        flag=13000515,
        flag_1=13000516,
        left=0,
        asset=Assets.AEG247_045_0500,
        asset_1=Assets.AEG247_003_0505,
        asset_2=Assets.AEG247_003_0504,
        flag_2=13000517,
    )
    CommonFunc_90005501(
        0,
        flag=13000520,
        flag_1=13000521,
        left=0,
        asset=Assets.AEG247_004_0500,
        asset_1=Assets.AEG247_003_0502,
        asset_2=Assets.AEG247_003_0503,
        flag_2=13000522,
    )
    CommonFunc_90005501(
        0,
        flag=13000525,
        flag_1=13000526,
        left=1,
        asset=Assets.AEG247_005_0501,
        asset_1=Assets.AEG247_003_0506,
        asset_2=Assets.AEG247_003_0507,
        flag_2=13000527,
    )
    CommonFunc_90005501(
        0,
        flag=13000530,
        flag_1=13000531,
        left=2,
        asset=Assets.AEG247_005_0502,
        asset_1=Assets.AEG247_003_0509,
        asset_2=Assets.AEG247_003_0508,
        flag_2=13000532,
    )
    Event_13002600(0, entity=Characters.Dummy0, region=13002600, anchor_entity=13002120, seconds=0.0)
    Event_13002600(1, entity=Characters.Dummy0, region=13002600, anchor_entity=13002121, seconds=1.0)
    Event_13002600(2, entity=Characters.Dummy0, region=13002600, anchor_entity=13002122, seconds=3.0)
    Event_13002600(3, entity=Characters.Dummy0, region=13002600, anchor_entity=13002123, seconds=5.0)
    Event_13002600(4, entity=Characters.Dummy0, region=13002600, anchor_entity=13002124, seconds=6.0)
    Event_13002600(5, entity=Characters.Dummy0, region=13002600, anchor_entity=13002125, seconds=9.0)
    Event_13002600(6, entity=Characters.Dummy0, region=13002600, anchor_entity=13002126, seconds=1.0)
    Event_13002600(7, entity=Characters.Dummy0, region=13002600, anchor_entity=13002127, seconds=2.5)
    Event_13002600(8, entity=Characters.Dummy0, region=13002600, anchor_entity=13002128, seconds=7.0)
    CommonFunc_90005620(
        0,
        flag=13000570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=13002570,
        cancel_flag__right_flag=13002571,
        right=13002572,
    )
    CommonFunc_90005621(0, flag=13000570, asset=Assets.AEG099_270_9000)
    CommonFunc_90005780(
        0,
        flag=13000850,
        summon_flag=13002160,
        dismissal_flag=13002161,
        character=Characters.RecusantBernahl1,
        sign_type=20,
        region=13002721,
        right=13002720,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=13000850, flag_1=13002160, flag_2=13002161, character=Characters.RecusantBernahl1)
    Event_13002859()
    CommonFunc_90005780(
        0,
        flag=13000850,
        summon_flag=13002164,
        dismissal_flag=13002165,
        character=Characters.RecusantBernahl2,
        sign_type=20,
        region=13002726,
        right=13002721,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=13000850, flag_1=13002164, flag_2=13002165, character=Characters.RecusantBernahl2)
    CommonFunc_90005782(
        0,
        flag=13002164,
        region=13002855,
        character=Characters.RecusantBernahl2,
        target_entity=13002853,
        region_1=13002869,
        animation=0,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=13000180,
        summon_flag=13002181,
        dismissal_flag=13002182,
        character=Characters.RecusantBernahl0,
        sign_type=22,
        region=13002180,
        region_1=13002181,
        seconds=0.0,
        right_1=13009300,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=13000180, flag_1=13002181, flag_2=13002182, character=Characters.RecusantBernahl0)
    CommonFunc_90005792(
        0,
        flag=13000180,
        flag_1=13002181,
        flag_2=13002182,
        character=Characters.RecusantBernahl0,
        item_lot=102920,
        seconds=0.0,
    )
    RunCommonEvent(
        13002660,
        slot=0,
        args=(13000180, 13002181, 13002182, 13000710, 13002180, 13002183, 0),
        arg_types="IIIIIIi",
    )
    Event_13003700()
    CommonFunc_90005704(0, attacked_entity=Characters.LivingPot, flag=13009256, flag_1=3660, flag_2=13009251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot,
        flag=3661,
        flag_1=3662,
        flag_2=13009251,
        flag_3=13009256,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.LivingPot, flag=3663, first_flag=3660, last_flag=3663)
    Event_13003710(0, character=Characters.LivingPot)
    Event_13003711(0, character=Characters.LivingPot)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9009,
        action_button_id=4110,
        item_lot=101740,
        first_flag=400174,
        last_flag=400174,
        flag=13009254,
        model_point=0,
    )
    Event_13003720()
    Event_13003721()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13000519()
    CommonFunc_90005201(
        0,
        character=Characters.BeastmanofFarumAzula0,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.BeastmanofFarumAzula1,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.BeastmanofFarumAzula2,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.BeastmanofFarumAzula35,
        animation_id=30003,
        animation_id_1=20003,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula3,
        region=13002203,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula4, region=13002201, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula33, region=13002201, seconds=3.5, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula15, region=13002217, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula16,
        animation_id=30004,
        animation_id_1=20004,
        region=13002217,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula5,
        region=13002205,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula7,
        region=13002209,
        radius=10.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005211(
        0,
        character=Characters.BeastmanofFarumAzula6,
        animation_id=30003,
        animation_id_1=20003,
        region=13002207,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula8, region=13002210, seconds=0.0, animation_id=3001)
    CommonFunc_90005251(0, character=Characters.BeastmanofFarumAzula8, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula9, region=13002207, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula10, region=13002207, seconds=1.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.BeastmanofFarumAzula10, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula11, region=13002212, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula12, region=13002215, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula13, region=13002215, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula14, region=13002215, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula17, region=13002214, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula34, region=13002214, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula18, region=13002220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula19, region=13002222, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula20, region=13002223, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula21,
        region=13002225,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005210(
        0,
        character=Characters.BeastmanofFarumAzula22,
        animation_id=30004,
        animation_id_1=20004,
        region=13002227,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula23, region=13002228, seconds=0.0, animation_id=3002)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula24, region=13002230, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula25,
        animation_id=30004,
        animation_id_1=20004,
        region=13002231,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula26, region=13002230, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula28, region=13002234, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula27,
        animation_id=30003,
        animation_id_1=20003,
        region=13002233,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula29,
        region=13002235,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005251(0, character=Characters.BeastmanofFarumAzula30, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.BeastmanofFarumAzula31,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula32, region=13002245, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula39,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula40,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula41,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula42,
        animation_id=30004,
        animation_id_1=20004,
        region=13002269,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.BeastmanofFarumAzula43, radius=40.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula36, region=13002296, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula37, region=13002296, seconds=1.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula38, region=13002296, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.BeastmanofFarumAzula47,
        region=13002278,
        radius=30.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula44, region=13002277, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula45, region=13002277, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BeastmanofFarumAzula46, region=13002277, seconds=0.0, animation_id=-1)
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula48,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.BeastmanofFarumAzula49,
        animation_id=30004,
        animation_id_1=20004,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula50,
        animation_id=30004,
        animation_id_1=20004,
        region=13002289,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula51,
        animation_id=30004,
        animation_id_1=20004,
        region=13002289,
        seconds=1.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BeastmanofFarumAzula52,
        animation_id=30004,
        animation_id_1=20004,
        region=13002289,
        seconds=0.5,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Skeleton5, region=13002412, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Skeleton7, region=13002412, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Skeleton0, region=13002412, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Skeleton4, region=13002408, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton2,
        animation_id=30017,
        animation_id_1=20017,
        region=13002412,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton3,
        animation_id=30017,
        animation_id_1=20017,
        region=13002412,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Skeleton8, region=13002416, seconds=0.0, animation_id=3014)
    CommonFunc_90005251(0, character=Characters.Skeleton9, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=13000418, region=13002418, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=13000419, region=13002418, seconds=0.5, animation_id=3003)
    CommonFunc_90005261(0, character=Characters.Skeleton10, region=13002420, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton11,
        animation_id=30018,
        animation_id_1=20018,
        region=13002421,
        seconds=5.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton12,
        animation_id=30018,
        animation_id_1=20018,
        region=13002421,
        seconds=7.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton13,
        animation_id=30018,
        animation_id_1=20018,
        region=13002421,
        seconds=8.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton14,
        animation_id=30017,
        animation_id_1=20017,
        region=13002435,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Skeleton15, region=13002435, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton17,
        animation_id=30017,
        animation_id_1=20017,
        region=13002446,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton22,
        animation_id=30014,
        animation_id_1=20014,
        region=13002446,
        seconds=3.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton23,
        animation_id=30014,
        animation_id_1=20014,
        region=13002446,
        seconds=1.5,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Dummy1, region=13002323, radius=35.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Dummy2, region=13002323, radius=35.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton24,
        animation_id=30017,
        animation_id_1=20017,
        region=13002456,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton25,
        animation_id=30018,
        animation_id_1=20018,
        region=13002459,
        seconds=1.5,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton26,
        animation_id=30018,
        animation_id_1=20018,
        region=13002459,
        seconds=2.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton27,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton29,
        animation_id=30018,
        animation_id_1=20018,
        region=13002459,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton32,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton33,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton30,
        animation_id=30018,
        animation_id_1=20018,
        region=13002463,
        seconds=3.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Skeleton31,
        animation_id=30018,
        animation_id_1=20018,
        region=13002463,
        seconds=4.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(
        0,
        character=Characters.Skeleton34,
        animation_id=30018,
        animation_id_1=20018,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005251(0, character=Characters.Skeleton28, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.UndeadAzulaBeastman1, region=13002481, seconds=0.0, animation_id=3003)
    CommonFunc_90005250(0, character=Characters.UndeadAzulaBeastman2, region=13002418, seconds=0.5, animation_id=3003)
    CommonFunc_90005200(
        0,
        character=Characters.UndeadAzulaBeastman3,
        animation_id=30017,
        animation_id_1=20017,
        region=13002435,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.UndeadAzulaBeastman5,
        animation_id=30017,
        animation_id_1=20017,
        region=13002435,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.UndeadAzulaBeastman6,
        animation_id=30017,
        animation_id_1=20017,
        region=13002488,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.UndeadAzulaBeastman7,
        region=13002488,
        radius=2.0,
        seconds=0.5,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.FarumAzulaDog2_0,
        animation_id=30001,
        animation_id_1=20001,
        region=13002300,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.FarumAzulaDog2_1,
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
        character=Characters.FarumAzulaDog2_2,
        animation_id=30000,
        animation_id_1=20000,
        region=13002311,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.FarumAzulaDog2_3,
        animation_id=30000,
        animation_id_1=20000,
        region=13002311,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FarumAzulaDog2_4,
        region=13002314,
        radius=20.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.FarumAzulaDog2_5,
        animation_id=30000,
        animation_id_1=20000,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.FarumAzulaDog2_5,
        animation_id=30000,
        animation_id_1=20000,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.FarumAzulaDog2_6,
        animation_id=30001,
        animation_id_1=20001,
        region=13002456,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=13000330, region=13002355, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=13000331, region=13002355, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle0,
        animation_id=30001,
        animation_id_1=20001,
        region=13002350,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle1,
        animation_id=30000,
        animation_id_1=3009,
        region=13002350,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BladedTalonEagle2, region=13002352, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle2,
        animation_id=30000,
        animation_id_1=20000,
        region=13002352,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle3,
        animation_id=30000,
        animation_id_1=20000,
        region=13002355,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle4,
        animation_id=30001,
        animation_id_1=20001,
        region=13002355,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.BladedTalonEagle5,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.BladedTalonEagle6,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=Characters.BladedTalonEagle7,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        radius=9.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle8,
        animation_id=30000,
        animation_id_1=20000,
        region=13002356,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle9,
        animation_id=30001,
        animation_id_1=20001,
        region=13002356,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle10,
        animation_id=30001,
        animation_id_1=20001,
        region=13002362,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle11,
        animation_id=30001,
        animation_id_1=20001,
        region=13002362,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle12,
        animation_id=30000,
        animation_id_1=20000,
        region=13002362,
        seconds=1.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.BladedTalonEagle13,
        animation_id=30001,
        animation_id_1=20001,
        region=13002365,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.BladedTalonEagle14,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.BanishedKnight0, region=13002381, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight1, region=13002382, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight2, region=13002384, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.BanishedKnight3, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=13000380, region=13002380, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=13000383, region=13002380, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight8, region=13002390, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.BanishedKnight4, radius=55.0, seconds=6.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight6, region=13002388, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight7, region=13002389, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight10, region=13002392, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight11, region=13002395, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=13000396, region=13002396, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.BanishedKnight13, region=13002398, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Wormface1,
        animation_id=30000,
        animation_id_1=20000,
        region=13002372,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface2,
        animation_id=30000,
        animation_id_1=20000,
        region=13002372,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface3,
        animation_id=30001,
        animation_id_1=20001,
        region=13002300,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface6,
        animation_id=30001,
        animation_id_1=20001,
        region=13002372,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Wormface4, region=13002374, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Wormface5,
        animation_id=30000,
        animation_id_1=20000,
        region=13002375,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Wormface7, region=13002377, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Wormface8,
        animation_id=30000,
        animation_id_1=20000,
        region=13002369,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Wormface9,
        animation_id=30000,
        animation_id_1=20000,
        region=13002369,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.WormfaceLarge,
        animation_id=30001,
        animation_id_1=20001,
        region=13002369,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.AncientDragon0,
        animation_id=30019,
        animation_id_1=20019,
        region=13002490,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.AncientDragon2,
        animation_id=30019,
        animation_id_1=20019,
        region=13002494,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.AncientDragon3, region=13002495, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.AncientDragon5,
        animation_id=30010,
        animation_id_1=20010,
        region=13002498,
        seconds=0.0,
        left=0,
        left_1=1,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CrucibleKnight0, region=13002295, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CrucibleKnight1, region=13002296, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.DraconicTreeSentinel,
        region=13002496,
        radius=40.0,
        seconds=0.0,
        animation_id=-1,
    )


@ContinueOnRest(13002500)
def Event_13002500():
    """Event 13002500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13000500):
        return
    AND_1.Add(InsideMap(game_map=CRUMBLING_FARUM_AZULA))
    AND_1.Add(FlagEnabled(110))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=13002502))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(9000))
    
    MAIN.Await(AND_2)
    
    EnableFlag(13000500)
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)


@RestartOnRest(13002580)
def Event_13002580():
    """Event 13002580"""
    RegisterLadder(start_climbing_flag=13000580, stop_climbing_flag=13000581, asset=Assets.AEG247_001_0500)
    RegisterLadder(start_climbing_flag=13000582, stop_climbing_flag=13000583, asset=Assets.AEG247_000_0500)
    RegisterLadder(start_climbing_flag=13000584, stop_climbing_flag=13000585, asset=Assets.AEG247_008_0500)
    RegisterLadder(start_climbing_flag=13000586, stop_climbing_flag=13000587, asset=Assets.AEG247_006_0500)
    RegisterLadder(start_climbing_flag=13000588, stop_climbing_flag=13000589, asset=Assets.AEG247_007_0500)
    RegisterLadder(start_climbing_flag=13000590, stop_climbing_flag=13000591, asset=Assets.AEG247_011_0500)


@ContinueOnRest(13002510)
def Event_13002510():
    """Event 13002510"""
    CommonFunc_90005500(
        0,
        flag=13000510,
        flag_1=13000511,
        left=0,
        asset=Assets.AEG247_002_0500,
        asset_1=Assets.AEG247_003_0500,
        obj_act_id=13003511,
        asset_2=Assets.AEG247_003_0501,
        obj_act_id_1=13003512,
        region=13002511,
        region_1=13002512,
        flag_2=13000512,
        flag_3=13000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000515,
        flag_1=13000516,
        left=0,
        asset=Assets.AEG247_045_0500,
        asset_1=Assets.AEG247_003_0505,
        obj_act_id=13003516,
        asset_2=Assets.AEG247_003_0504,
        obj_act_id_1=13003517,
        region=13002516,
        region_1=13002517,
        flag_2=13000517,
        flag_3=13000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000520,
        flag_1=13000521,
        left=0,
        asset=Assets.AEG247_004_0500,
        asset_1=Assets.AEG247_003_0502,
        obj_act_id=13003521,
        asset_2=Assets.AEG247_003_0503,
        obj_act_id_1=13003522,
        region=13002521,
        region_1=13002522,
        flag_2=13000522,
        flag_3=13000523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000525,
        flag_1=13000526,
        left=1,
        asset=Assets.AEG247_005_0501,
        asset_1=Assets.AEG247_003_0506,
        obj_act_id=13003526,
        asset_2=Assets.AEG247_003_0507,
        obj_act_id_1=13003527,
        region=13002526,
        region_1=13002527,
        flag_2=13000527,
        flag_3=13000528,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=13000530,
        flag_1=13000531,
        left=2,
        asset=Assets.AEG247_005_0502,
        asset_1=Assets.AEG247_003_0509,
        obj_act_id=13003531,
        asset_2=Assets.AEG247_003_0508,
        obj_act_id_1=13003532,
        region=13002531,
        region_1=13002532,
        flag_2=13000532,
        flag_3=13000533,
        left_1=0,
    )


@ContinueOnRest(13000519)
def Event_13000519():
    """Event 13000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13000510)
    EnableThisSlotFlag()


@RestartOnRest(13002236)
def Event_13002236(_, region: uint, character: uint):
    """Event 13002236"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(character)
    Restart()


@RestartOnRest(13002490)
def Event_13002490(_, character: uint, region: uint, animation_id: int, flag: uint):
    """Event 13002490"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, animation_id)


@RestartOnRest(13002493)
def Event_13002493(_, character: uint, region: uint, region_1: uint):
    """Event 13002493"""
    RemoveSpecialEffect(character, 18941)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 18941)
    Wait(4.0)
    Restart()


@RestartOnRest(13002646)
def Event_13002646(_, flag: uint, region: uint, character: uint, seconds: float):
    """Event 13002646"""
    if FlagEnabled(flag):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    ForceAnimation(character, 20001)
    Wait(6.0)
    DisableCharacter(character)
    EnableThisSlotFlag()


@RestartOnRest(13002660)
def Event_13002660(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    character: uint,
    other_entity: uint,
    region: uint,
    left: int,
):
    """Event 13002660"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=110.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)
    
    MAIN.Await(OR_10)
    
    if FlagEnabled(flag):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_2))


@RestartOnRest(13002800)
def Event_13002800():
    """Event 13002800"""
    GotoIfFlagDisabled(Label.L0, flag=13000800)
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L1, flag=118)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthValue(Characters.BeastClergyman1) <= 0)
    
    Kill(Characters.BeastClergyman0)
    Kill(Characters.BeastClergyman1)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.BeastClergyman1))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(13000800))
    
    MAIN.Await(OR_2)
    
    SetBackreadStateAlternate(Characters.BeastClergyman1, True)
    KillBossAndDisplayBanner(character=Characters.BeastClergyman1, banner_type=BannerType.LegendFelled)
    EnableNetworkFlag(13000800)
    EnableFlag(9116)
    if PlayerInOwnWorld():
        EnableFlag(61116)
    if PlayerNotInOwnWorld():
        return
    if PlayerInOwnWorld():
        return


@RestartOnRest(13002805)
def Event_13002805():
    """Event 13002805"""
    GotoIfFlagEnabled(Label.L0, flag=13000800)
    DisableCharacter(Characters.TalkDummy0)
    DisableAsset(Assets.AEG099_060_9000)
    Wait(1.0)
    
    MAIN.Await(FlagEnabled(13000800))
    
    Wait(4.0)
    Wait(7.800000190734863)
    CreateTemporaryVFX(
        vfx_id=1060,
        anchor_entity=Assets.AEG099_060_9000,
        model_point=200,
        anchor_type=CoordEntityType.Asset,
    )
    Wait(0.5)
    EnableCharacter(Characters.TalkDummy0)
    EnableAsset(Assets.AEG099_060_9000)

    # --- Label 0 --- #
    DefineLabel(0)
    RegisterGrace(grace_flag=13000000, asset=Assets.AEG099_060_9000, reaction_distance=5.0, reaction_angle=180.0)


@RestartOnRest(13002810)
def Event_13002810():
    """Event 13002810"""
    GotoIfFlagDisabled(Label.L0, flag=13000800)
    DisableCharacter(Characters.BeastClergyman1)
    DisableCharacter(Characters.BeastClergyman0)
    DisableAnimations(Characters.BeastClergyman1)
    DisableAnimations(Characters.BeastClergyman0)
    Kill(Characters.BeastClergyman1)
    Kill(Characters.BeastClergyman0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BeastClergyman0)
    DisableAI(Characters.BeastClergyman1)
    DisableHealthBar(Characters.BeastClergyman1)
    DisableCharacter(Characters.BeastClergyman1)
    DisableGravity(Characters.BeastClergyman1)
    DisableAnimations(Characters.BeastClergyman1)
    GotoIfFlagEnabled(Label.L1, flag=13000801)
    ForceAnimation(Characters.BeastClergyman0, 30018, loop=True)
    AND_1.Add(FlagEnabled(13002805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002800))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    ForceAnimation(Characters.BeastClergyman0, 20038, loop=True)
    EnableNetworkFlag(13000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(13002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=13002800))
    
    MAIN.Await(AND_2)
    
    EnableFlag(13002803)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.BeastClergyman1)
    ReferDamageToEntity(Characters.BeastClergyman0, target_entity=Characters.BeastClergyman1)
    EnableAI(Characters.BeastClergyman0)
    SetNetworkUpdateRate(Characters.BeastClergyman0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.BeastClergyman1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BeastClergyman0, name=902110000)


@RestartOnRest(13002811)
def Event_13002811():
    """Event 13002811"""
    if FlagEnabled(13000800):
        return
    AND_1.Add(HealthRatio(Characters.BeastClergyman0) <= 0.550000011920929)
    
    MAIN.Await(AND_1)
    
    OR_15.Add(HealthValue(PLAYER) <= 0)
    OR_15.Add(CharacterInsideRegion(character=PLAYER, region=13002815))
    if OR_15:
        return
    SetCharacterFadeOnEnable(character=Characters.BeastClergyman1, state=False)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=13000040,
            cutscene_flags=0,
            move_to_region=13002820,
            map_id=13000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(13000040, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(13002802)
    DisableCharacter(Characters.BeastClergyman0)
    SetNetworkUpdateRate(Characters.BeastClergyman0, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    DisableAI(Characters.BeastClergyman0)
    ForceAnimation(Characters.BeastClergyman1, 20015)
    Move(
        Characters.BeastClergyman1,
        destination=13002825,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.BeastClergyman1,
    )
    EnableGravity(Characters.BeastClergyman1)
    EnableAnimations(Characters.BeastClergyman1)
    EnableAI(Characters.BeastClergyman1)
    SetNetworkUpdateRate(Characters.BeastClergyman1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BeastClergyman1, name=902110001)


@RestartOnRest(13002819)
def Event_13002819():
    """Event 13002819"""
    MAIN.Await(CharacterHasSpecialEffect(Characters.BeastClergyman1, 15272))
    
    Move(
        Characters.BeastClergyman1,
        destination=13002825,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.BeastClergyman1,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(13002820)
def Event_13002820():
    """Event 13002820"""
    AND_1.Add(HealthRatio(Characters.BeastClergyman1) != 0.0)
    AND_1.Add(FlagEnabled(13002821))
    if FlagEnabled(13002822):
        SetEventPoint(Characters.BeastClergyman1, region=13002810, reaction_range=200.0)
    if FlagEnabled(13002823):
        SetEventPoint(Characters.BeastClergyman1, region=13002811, reaction_range=200.0)
    if FlagEnabled(13002824):
        SetEventPoint(Characters.BeastClergyman1, region=13002812, reaction_range=200.0)
    DisableFlag(13002821)
    Restart()


@RestartOnRest(13002827)
def Event_13002827():
    """Event 13002827"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.BeastClergyman1, 15270))
    AND_1.Add(FlagDisabled(13002826))
    OR_1.Add(CharacterInsideRegion(character=Characters.BeastClergyman1, region=13002840))
    OR_1.Add(CharacterInsideRegion(character=Characters.BeastClergyman1, region=13002841))
    OR_1.Add(CharacterInsideRegion(character=Characters.BeastClergyman1, region=13002842))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.BeastClergyman1, 15270)
    EnableFlag(13002826)
    Restart()


@RestartOnRest(13002828)
def Event_13002828():
    """Event 13002828"""
    AND_1.Add(FlagEnabled(13002826))
    AND_1.Add(CharacterOutsideRegion(character=Characters.BeastClergyman1, region=13002840))
    AND_1.Add(CharacterOutsideRegion(character=Characters.BeastClergyman1, region=13002841))
    AND_1.Add(CharacterOutsideRegion(character=Characters.BeastClergyman1, region=13002842))
    
    MAIN.Await(AND_1)
    
    DisableFlag(13002826)
    Restart()


@RestartOnRest(13002829)
def Event_13002829():
    """Event 13002829"""
    CommonFunc_9005800(
        0,
        flag=13000800,
        entity=Assets.AEG099_002_9000,
        region=13002800,
        flag_1=13002805,
        character=13005800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=13000800,
        entity=Assets.AEG099_002_9000,
        region=13002800,
        flag_1=13002805,
        flag_2=13002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=13000800, asset=Assets.AEG099_002_9000, model_point=4, right=0)
    CommonFunc_9005822(
        0,
        flag=13000800,
        bgm_boss_conv_param_id=211000,
        flag_1=13002805,
        flag_2=13002806,
        right=0,
        flag_3=13002802,
        left=1,
        left_1=1,
    )


@RestartOnRest(13002830)
def Event_13002830():
    """Event 13002830"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(HealthValue(Characters.DragonlordPlacidusax) <= 0)
    
    Kill(Characters.DragonlordPlacidusax)
    Wait(4.0)
    PlaySoundEffect(13008000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.DragonlordPlacidusax))
    
    KillBossAndDisplayBanner(character=Characters.DragonlordPlacidusax, banner_type=BannerType.LegendFelled)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    EnableFlag(13000830)
    EnableFlag(9115)
    if PlayerInOwnWorld():
        EnableFlag(61115)
    if PlayerInOwnWorld():
        EnableFlag(71301)


@RestartOnRest(13002834)
def Event_13002834():
    """Event 13002834"""
    if FlagEnabled(13000830):
        return
    GotoIfPlayerInOwnWorld(Label.L0)
    GotoIfFlagDisabled(Label.L0, flag=13002834)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=20000,
        destination_type=CoordEntityType.Region,
        destination=13002836,
        model_point=-1,
        copy_draw_parent=20000,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9740, entity=Assets.AEG099_090_9006))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=Assets.AEG099_090_9006,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        short_move=True,
    )
    ForceAnimation(PLAYER, 67010)
    Wait(3.0)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
            cutscene_id=13000010,
            cutscene_flags=0,
            move_to_region=13002834,
            map_id=13000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
            change_weather=True,
            weather=Weather.FlatClouds,
        )
    else:
        PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
            cutscene_id=13000010,
            cutscene_flags=CutsceneFlags.Unskippable,
            move_to_region=13002836,
            map_id=13000000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
            change_weather=True,
            weather=Weather.FlatClouds,
        )
    WaitFramesAfterCutscene(frames=1)
    EnableThisNetworkSlotFlag()
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)


@RestartOnRest(13002835)
def Event_13002835():
    """Event 13002835"""
    GotoIfFlagDisabled(Label.L3, flag=13000830)
    DisableCharacter(13005830)
    DisableAnimations(13005830)
    Kill(13005830)
    EnableFlag(71301)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableAI(Characters.DragonlordPlacidusax)
    CreateNPCPart(Characters.DragonlordPlacidusax, npc_part_id=0, part_index=NPCPartType.Part1, part_health=9999)
    CreateNPCPart(Characters.DragonlordPlacidusax, npc_part_id=1, part_index=NPCPartType.Part2, part_health=9999)
    SetNPCPartEffects(
        Characters.DragonlordPlacidusax,
        npc_part_id=0,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetNPCPartEffects(
        Characters.DragonlordPlacidusax,
        npc_part_id=1,
        material_sfx_id=173,
        material_vfx_id=173,
        unk_16_20=139,
        unk_20_24=139,
        unk_24_28=0,
    )
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.DragonlordPlacidusax, lock_on_model_point=225, state=False)
    SetCharacterEventTarget(Characters.DragonlordPlacidusax, entity=Characters.TalkDummy15)
    SetBackreadStateAlternate(Characters.DragonlordPlacidusax, True)
    ForceAnimation(Characters.DragonlordPlacidusax, 30000, loop=True)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002831))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DragonlordPlacidusax))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.DragonlordPlacidusax, state_info=260))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.DragonlordPlacidusax, 20000)
    EnableAI(Characters.DragonlordPlacidusax)
    SetNetworkUpdateRate(Characters.DragonlordPlacidusax, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DragonlordPlacidusax, name=904520000)
    ActivateMultiplayerBuffs(13005830)
    if PlayerNotInOwnWorld():
        return
    EnableNetworkFlag(13002835)
    SetNetworkUpdateAuthority(13005830, authority_level=UpdateAuthority.Forced)
    NotifyBossBattleStart()


@RestartOnRest(13002840)
def Event_13002840():
    """Event 13002840"""
    if FlagEnabled(13000830):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.DragonlordPlacidusax, 5029))
    
    MAIN.Await(AND_1)
    
    SetWeather(weather=Weather.WindyRain, duration=-1.0, immediate_change=False)
    EnableFlag(13002832)


@RestartOnRest(13002841)
def Event_13002841():
    """Event 13002841"""
    if FlagEnabled(13000830):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(Characters.DragonlordPlacidusax, 5025))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4521)
    Wait(1.0)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.DragonlordPlacidusax, 5025))
    
    MAIN.Await(AND_2)
    
    ChangeCamera(normal_camera_id=4525, locked_camera_id=4520)
    Wait(1.0)
    Restart()


@RestartOnRest(13002846)
def Event_13002846(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 13002846"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_2)
    Restart()


@RestartOnRest(13002849)
def Event_13002849():
    """Event 13002849"""
    Event_13002846(0, flag=13000830, flag_1=13002835, flag_2=13002836)
    CommonFunc_9005822(
        0,
        flag=13000830,
        bgm_boss_conv_param_id=452000,
        flag_1=13002835,
        flag_2=13002836,
        right=0,
        flag_3=13002832,
        left=0,
        left_1=1,
    )


@RestartOnRest(13002850)
def Event_13002850():
    """Event 13002850"""
    if FlagEnabled(13000850):
        return
    
    MAIN.Await(HealthValue(Characters.GodskinApostle1) <= 0)
    
    Kill(Characters.GodskinApostle0)
    Kill(Characters.GodskinNoble)
    EnableFlag(13002854)
    Wait(4.0)
    PlaySoundEffect(Characters.GodskinApostle1, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.GodskinApostle1))
    
    KillBossAndDisplayBanner(character=Characters.GodskinApostle1, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(13000850)
    EnableFlag(9114)
    if PlayerInOwnWorld():
        EnableFlag(61114)


@ContinueOnRest(13002859)
def Event_13002859():
    """Event 13002859"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(13002160))
    AND_1.Add(FlagEnabled(13002855))
    
    MAIN.Await(AND_1)
    
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=13002852)
    AICommand(Characters.RecusantBernahl1, command_id=10, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetEventPoint(Characters.RecusantBernahl1, region=13002850, reaction_range=0.0)
    
    MAIN.Await(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002859))
    
    RotateToFaceEntity(Characters.RecusantBernahl1, 13002850, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002850))
    
    MAIN.Await(OR_5)
    
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(Characters.RecusantBernahl1, command_id=-1, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetNetworkUpdateRate(Characters.RecusantBernahl1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(Characters.RecusantBernahl1, command_id=10, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetEventPoint(Characters.RecusantBernahl1, region=13002852, reaction_range=0.0)
    
    MAIN.Await(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002859))
    
    RotateToFaceEntity(Characters.RecusantBernahl1, 13002852, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=Characters.RecusantBernahl1, region=13002852))
    
    MAIN.Await(OR_5)
    
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(Characters.RecusantBernahl1, command_id=-1, command_slot=0)
    ReplanAI(Characters.RecusantBernahl1)
    SetNetworkUpdateRate(Characters.RecusantBernahl1, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(13002860)
def Event_13002860():
    """Event 13002860"""
    GotoIfFlagDisabled(Label.L6, flag=13000850)
    DisableCharacter(Characters.GodskinApostle1)
    DisableCharacter(Characters.GodskinApostle0)
    DisableCharacter(Characters.GodskinNoble)
    DisableAnimations(Characters.GodskinApostle1)
    DisableAnimations(Characters.GodskinApostle0)
    DisableAnimations(Characters.GodskinNoble)
    Kill(Characters.GodskinApostle1)
    Kill(Characters.GodskinApostle0)
    Kill(Characters.GodskinNoble)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableAI(Characters.GodskinApostle0)
    DisableAI(Characters.GodskinNoble)
    DisableCharacter(Characters.GodskinApostle1)
    DisableGravity(Characters.GodskinApostle1)
    DisableAnimations(Characters.GodskinApostle1)
    GotoIfFlagEnabled(Label.L7, flag=13000851)
    DisableCharacter(Characters.GodskinApostle0)
    DisableCharacter(Characters.GodskinNoble)
    ForceAnimation(Characters.GodskinApostle0, 30001, loop=True)
    ForceAnimation(Characters.GodskinNoble, 30001, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002851))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinApostle0, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.GodskinNoble, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(13000851)
    EnableCharacter(Characters.GodskinApostle0)
    EnableCharacter(Characters.GodskinNoble)
    ForceAnimation(Characters.GodskinApostle0, 20001)
    ForceAnimation(Characters.GodskinNoble, 20001)
    Goto(Label.L8)

    # --- Label 7 --- #
    DefineLabel(7)
    OR_2.Add(FlagEnabled(13002855))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002850))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002852))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002853))
    
    MAIN.Await(OR_2)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(Characters.GodskinApostle1)
    DisableAI(Characters.GodskinApostle1)
    EnableAI(Characters.GodskinApostle0)
    EnableAI(Characters.GodskinNoble)
    SetNetworkUpdateRate(Characters.GodskinApostle1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.GodskinApostle0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.GodskinNoble, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(13005851, target_entity=Characters.GodskinApostle1)
    EnableBossHealthBar(Characters.GodskinApostle1, name=903575000)


@RestartOnRest(13002861)
def Event_13002861():
    """Event 13002861"""
    if FlagEnabled(13000850):
        return
    OR_1.Add(HealthRatio(Characters.GodskinApostle1) <= 0.5)
    OR_1.Add(FlagEnabled(13002873))
    OR_1.Add(FlagEnabled(13002874))
    
    MAIN.Await(OR_1)
    
    EnableFlag(13002852)


@RestartOnRest(13002890)
def Event_13002890(_, flag: uint, character: uint, character_1: uint, special_effect: int):
    """Event 13002890"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13000850):
        return
    if FlagEnabled(13002854):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    Wait(20.0)
    OR_1.Add(HealthValue(character_1) > 0)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, special_effect)
    EnableNetworkFlag(flag)
    Restart()


@RestartOnRest(13002891)
def Event_13002891(_, flag: uint, spawner: uint, character: uint, special_effect: int, character_1: uint, flag_1: uint):
    """Event 13002891"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13000850):
        return
    if FlagEnabled(13002854):
        return
    OR_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(CharacterDead(character))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(13000850):
        return
    if FlagEnabled(13002854):
        return
    ForceSpawnerToSpawn(spawner=spawner)
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_1)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(13002892)
def Event_13002892():
    """Event 13002892"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13000850):
        return
    if FlagEnabled(13002854):
        return
    AND_1.Add(CharacterDead(Characters.GodskinApostle0))
    AND_1.Add(CharacterDead(Characters.GodskinNoble))
    AND_1.Add(FlagDisabled(13002944))
    AND_1.Add(FlagDisabled(13002945))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(13000850):
        return
    Wait(10.0)
    if FlagEnabled(13000850):
        return
    if FlagEnabled(13002854):
        return
    EnableRandomFlagInRange(flag_range=(13002875, 13002876))
    GotoIfFlagEnabled(Label.L0, flag=13002875)
    GotoIfFlagEnabled(Label.L1, flag=13002876)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceSpawnerToSpawn(spawner=13003851)
    EnableFlag(13002873)
    DisableFlag(13002875)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceSpawnerToSpawn(spawner=13003852)
    EnableFlag(13002874)
    DisableFlag(13002876)
    Restart()


@RestartOnRest(13002865)
def Event_13002865():
    """Event 13002865"""
    CommonFunc_9005800(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9000,
        region=13002850,
        flag_1=13002855,
        character=13005850,
        action_button_id=10000,
        left=13000851,
        region_1=13002851,
    )
    CommonFunc_9005800(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9003,
        region=13002852,
        flag_1=13002855,
        character=13005850,
        action_button_id=10000,
        left=13000851,
        region_1=13002851,
    )
    CommonFunc_9005800(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9002,
        region=13002853,
        flag_1=13002855,
        character=13005850,
        action_button_id=10000,
        left=13000851,
        region_1=13002851,
    )
    CommonFunc_9005801(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9000,
        region=13002850,
        flag_1=13002855,
        flag_2=13002856,
        action_button_id=10000,
    )
    CommonFunc_9005801(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9003,
        region=13002852,
        flag_1=13002855,
        flag_2=13002856,
        action_button_id=10000,
    )
    CommonFunc_9005801(
        0,
        flag=13000850,
        entity=Assets.AEG099_001_9002,
        region=13002853,
        flag_1=13002855,
        flag_2=13002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=13000850, asset=Assets.AEG099_001_9000, model_point=5, right=13000851)
    CommonFunc_9005811(0, flag=13000850, asset=Assets.AEG099_001_9003, model_point=5, right=13000851)
    CommonFunc_9005811(0, flag=13000850, asset=Assets.AEG099_001_9002, model_point=5, right=13000851)
    CommonFunc_9005811(0, flag=13000850, asset=Assets.AEG099_001_9001, model_point=5, right=13000851)
    CommonFunc_9005811(0, flag=13000850, asset=Assets.AEG099_001_9004, model_point=5, right=13000851)
    CommonFunc_9005822(
        0,
        flag=13000850,
        bgm_boss_conv_param_id=356000,
        flag_1=13002855,
        flag_2=13002856,
        right=0,
        flag_3=13002852,
        left=0,
        left_1=0,
    )


@RestartOnRest(13002600)
def Event_13002600(_, entity: uint, region: uint, anchor_entity: uint, seconds: float):
    """Event 13002600"""
    if FlagEnabled(13000490):
        return
    CreateProjectileOwner(entity=entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    Wait(seconds)
    CreateTemporaryVFX(vfx_id=813600, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(5.0)
    Restart()


@RestartOnRest(13002610)
def Event_13002610():
    """Event 13002610"""
    ForceAnimation(Characters.AncientDragon3, 0)
    OR_15.Add(HasAIStatus(Characters.AncientDragon3, ai_status=AIStatusType.Battle))
    if OR_15:
        return
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_2.Add(FlagEnabled(13000495))
    if OR_2:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=13002619))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        ForceAnimation(Characters.AncientDragon3, 3029)
    else:
        ForceAnimation(Characters.AncientDragon3, 20002)
    EnableThisSlotFlag()
    Wait(2.0)
    OR_10.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_10.Add(FlagEnabled(13000495))
    if OR_10:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy0,
            source_entity=13002610,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.5)
    OR_11.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_11.Add(FlagEnabled(13000495))
    if OR_11:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy1,
            source_entity=13002620,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy2,
            source_entity=13002621,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.5)
    OR_12.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_12.Add(FlagEnabled(13000495))
    if OR_12:
        return
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy3,
            source_entity=13002630,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.BulletDummy4,
            source_entity=13002631,
            model_point=-1,
            behavior_id=803000070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(0.8999999761581421)
    OR_13.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_13.Add(FlagEnabled(13000495))
    if OR_13:
        return
    ForceAnimation(Characters.AncientDragon3, 30000)
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_3.Add(FlagEnabled(13000495))
    GotoIfConditionTrue(Label.L0, input_condition=OR_3)
    Wait(1.0)
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_4.Add(FlagEnabled(13000495))
    GotoIfConditionTrue(Label.L0, input_condition=OR_4)
    Wait(1.0)
    OR_5.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_5.Add(FlagEnabled(13000495))
    GotoIfConditionTrue(Label.L0, input_condition=OR_5)
    Wait(1.0)
    OR_6.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_6.Add(FlagEnabled(13000495))
    GotoIfConditionTrue(Label.L0, input_condition=OR_6)
    Wait(1.0)
    OR_7.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_7.Add(FlagEnabled(13000495))
    GotoIfConditionTrue(Label.L0, input_condition=OR_7)
    Wait(1.0)
    OR_8.Add(CharacterInsideRegion(character=PLAYER, region=13002495))
    OR_8.Add(FlagEnabled(13000495))
    Wait(1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(13003700)
def Event_13003700():
    """Event 13003700"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13002805))
    
    SetCharacterTalkRange(character=Characters.BeastClergyman0, distance=100.0)
    SetCharacterTalkRange(character=Characters.BeastClergyman1, distance=100.0)
    End()


@RestartOnRest(13003710)
def Event_13003710(_, character: uint):
    """Event 13003710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3671)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(Characters.AncientDragon4)
    EnableCharacter(Characters.AncientDragon5)
    if FlagEnabled(13000702):
        DisableCharacter(Characters.AncientDragon5)
    
    MAIN.Await(FlagEnabled(3671))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(13002710)
    GotoIfFlagEnabled(Label.L4, flag=13009257)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930010)
    if FlagEnabled(13009258):
        ForceAnimation(character, 930014)
    DisableCharacter(Characters.AncientDragon4)
    ForceAnimation(Characters.AncientDragon4, 10001)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableCharacter(Characters.AncientDragon4)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(Characters.AncientDragon4)
    DisableCharacter(Characters.AncientDragon5)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3671))
    
    Restart()


@RestartOnRest(13003711)
def Event_13003711(_, character: uint):
    """Event 13003711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(3671))
    AND_1.Add(FlagEnabled(13009256))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=character, distance=200.0)
    GotoIfFlagDisabled(Label.L1, flag=13009258)
    AND_2.Add(FlagEnabled(13009258))
    AND_2.Add(FlagDisabled(13009257))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagEnabled(13009258))
    AND_3.Add(FlagEnabled(13009257))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    EnableImmortality(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3662)
    EnableFlag(400175)
    AND_2.Add(HealthValue(character) == 1)
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(13002712)
    ForceAnimation(character, 20035)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3660)
    SetTeamType(character, TeamType.NoTeam)
    AND_3.Add(FlagEnabled(13009257))
    AwaitConditionTrue(AND_3)
    SetTeamType(character, TeamType.FriendlyNPC)
    DisableImmortality(character)
    OR_1.Add(FlagEnabled(13009260))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(CharacterDead(character))
    AwaitConditionTrue(OR_1)
    AND_4.Add(CharacterDead(character))
    SkipLinesIfConditionTrue(1, AND_4)
    Kill(character, award_runes=True)
    AwardItemLot(101740, host_only=False)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagDisabled(400174):
        EnableFlag(13009254)
    DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
    EnableNetworkFlag(3663)
    End()


@RestartOnRest(13003720)
def Event_13003720():
    """Event 13003720"""
    WaitFrames(frames=1)
    DisableFlag(13009300)
    AND_1.Add(FlagDisabled(16009460))
    AND_1.Add(FlagDisabled(3883))
    if AND_1:
        return
    EnableFlag(13009300)
    End()


@ContinueOnRest(13003721)
def Event_13003721():
    """Event 13003721"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    OR_4.Add(FlagEnabled(13002720))
    OR_4.Add(FlagEnabled(13002721))
    if OR_4:
        return
    if FlagEnabled(13000850):
        return
    if FlagDisabled(3880):
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=13002721, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=13002726, radius=10.0))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13002720)
    DisableFlag(13002721)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(13002720)
    EnableFlag(13002721)
    End()
