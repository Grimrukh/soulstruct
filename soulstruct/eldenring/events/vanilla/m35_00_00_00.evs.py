"""
Subterranean Shunning-Grounds

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
from .enums.m35_00_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=35000001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=35000002, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=35000003, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=35000004, asset=Assets.AEG099_060_9004)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    CommonFunc_9005810(
        0,
        flag=35000800,
        grace_flag=35000000,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_35002500()
    Event_35002504()
    Event_35002506()
    Event_35002508()
    CommonFunc_90005300(0, flag=35000800, character=Characters.Mohg, item_lot=0, seconds=0.0, left=0)
    Event_35002800()
    Event_35002810()
    Event_35002849()
    Event_35002850()
    Event_35002860()
    Event_35002899()
    Event_35002490(0, flag=35008203, asset=35001490, flag_1=35000800)
    CommonFunc_90005501(
        0,
        flag=35000510,
        flag_1=35000511,
        left=0,
        asset=Assets.AEG027_017_0500,
        asset_1=Assets.AEG027_002_0501,
        asset_2=Assets.AEG027_002_0500,
        flag_2=35000512,
    )
    CommonFunc_90005501(
        0,
        flag=35000515,
        flag_1=35000516,
        left=0,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0505,
        asset_2=Assets.AEG027_002_0504,
        flag_2=35000517,
    )
    Event_35002510()
    CommonFunc_90005525(0, flag=35000570, asset=35001570)
    CommonFunc_90005525(1, flag=35000571, asset=35001571)
    CommonFunc_90005525(2, flag=35000572, asset=35001572)
    CommonFunc_90005525(3, flag=35000573, asset=35001573)
    CommonFunc_90005525(4, flag=35000574, asset=35001574)
    CommonFunc_90005540(
        0,
        flag=35000530,
        asset=Assets.AEG027_015_0500,
        asset_1=Assets.AEG027_002_0502,
        obj_act_id=35003531,
        obj_act_id_1=-1,
        animation_id=1,
        animation_id_1=2,
    )
    CommonFunc_90005540(
        0,
        flag=35000565,
        asset=Assets.AEG027_018_0500,
        asset_1=Assets.AEG027_002_0503,
        obj_act_id=35003533,
        obj_act_id_1=-1,
        animation_id=1,
        animation_id_1=2,
    )
    CommonFunc_90005540(
        0,
        flag=35000566,
        asset=Assets.AEG027_018_0501,
        asset_1=Assets.AEG027_002_0507,
        obj_act_id=35003535,
        obj_act_id_1=-1,
        animation_id=1,
        animation_id_1=2,
    )
    CommonFunc_90005511(0, flag=35000560, asset=Assets.AEG027_019_0500, obj_act_id=35003560, obj_act_id_1=27019, left=0)
    CommonFunc_90005512(0, flag=35000560, region=35002560, region_1=35002561)
    CommonFunc_90005511(0, flag=35000562, asset=Assets.AEG027_019_0501, obj_act_id=35003562, obj_act_id_1=27019, left=0)
    CommonFunc_90005512(0, flag=35000562, region=35002562, region_1=35002563)
    CommonFunc_90005510(
        0,
        flag=35000564,
        asset=Assets.AEG027_019_0502,
        obj_act_id=35003564,
        obj_act_id_1=1027019,
        text=208197,
        left=0,
    )
    CommonFunc_90005515(0, flag=35008542, anchor_entity=Assets.AEG027_031_0500)
    Event_35002580()
    CommonFunc_90005520(
        0,
        flag=35000598,
        asset=Assets.AEG027_032_0500,
        start_climbing_flag=35002598,
        stop_climbing_flag=35002599,
    )
    Event_35002498()
    CommonFunc_90005690(0, region=35002507)
    CommonFunc_90005691(0, region=35002507)
    Event_35002820()
    CommonFunc_90005650(
        0,
        flag=35000640,
        asset=Assets.AEG027_041_0501,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=35003641,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=35000640, anchor_entity=Assets.AEG027_041_0501)
    CommonFunc_90005680(
        0,
        flag=35000670,
        flag_1=35000671,
        flag_2=35000672,
        flag_3=35000673,
        asset=Assets.AEG027_003_0500,
    )
    CommonFunc_90005680(
        0,
        flag=35000675,
        flag_1=35000676,
        flag_2=35000677,
        flag_3=35000678,
        asset=Assets.AEG027_003_0501,
    )
    Event_35002642()
    Event_35002680()
    CommonFunc_90005646(
        0,
        flag=35000850,
        left_flag=35002840,
        cancel_flag__right_flag=35002841,
        asset=Assets.AEG099_065_9000,
        player_start=35002840,
        area_id=35,
        block_id=0,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, flag=35002800, asset=35001695, model_point=5)
    CommonFunc_90005780(
        0,
        flag=35000800,
        summon_flag=35002160,
        dismissal_flag=35002161,
        character=Characters.DungEater2,
        sign_type=20,
        region=35002721,
        right=35009318,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=35000800, flag_1=35002160, flag_2=35002161, character=Characters.DungEater2)
    CommonFunc_90005784(
        0,
        flag=35002160,
        flag_1=35002805,
        character=Characters.DungEater2,
        region=35002800,
        region_1=35002808,
        animation=0,
    )
    Event_35000700(0, character=Characters.Hyetta, asset=Assets.AEG099_090_9006)
    CommonFunc_90005740(
        0,
        flag=35002705,
        flag_1=35002706,
        left=35002707,
        character=Characters.Hyetta,
        model_point=701,
        asset=Assets.AEG099_090_9003,
        model_point_1=701,
        radius=0.4000000059604645,
        animation=90202,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
    )
    CommonFunc_90005741(
        0,
        flag=35002708,
        flag_1=35002709,
        left=35002707,
        character=Characters.Hyetta,
        animation__animation_id=90202,
        left_1=1,
        animation_id=-1,
        special_effect=0,
        seconds=0.0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9007,
        action_button_id=4110,
        item_lot=100890,
        first_flag=400089,
        last_flag=400089,
        flag=35009211,
        model_point=0,
    )
    Event_35000703(0, seconds=7.5)
    Event_35003720(0, character=Characters.DungEater1)
    CommonFunc_90005704(0, attacked_entity=Characters.DungEater1, flag=4241, flag_1=4240, flag_2=35009251, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.DungEater1,
        flag=4241,
        flag_1=4242,
        flag_2=35009251,
        flag_3=4241,
        first_flag=4240,
        last_flag=4244,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.DungEater1, flag=4243, first_flag=4240, last_flag=4244)
    Event_35003721(0, character=Characters.DungEater0)
    Event_35003722(0, entity=Characters.DungEater0)
    CommonFunc_90005702(0, character=Characters.DungEater0, flag=4243, first_flag=4240, last_flag=4244)
    Event_35003724(
        0,
        asset=Assets.AEG099_090_9002,
        action_button_id=6440,
        item_lot=4920,
        first_flag=9504,
        last_flag=9504,
        flag=35009333,
        model_point=806782,
    )
    Event_35003723()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=103820,
        first_flag=400381,
        last_flag=400382,
        flag=35009336,
        model_point=0,
    )
    Event_35003725()
    Event_35003726()
    Event_35003727()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=113820,
        first_flag=400382,
        last_flag=400382,
        flag=35009337,
        model_point=0,
    )
    Event_35003730()
    CommonFunc_90005771(0, other_entity=Characters.TalkDummy0, flag=35002730)
    CommonFunc_90005771(0, other_entity=Characters.Dummy2, flag=35002731)
    Event_35003790()
    Event_35003500(0, region=35002700)
    Event_35002361()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Hyetta)
    DisableBackread(35000710)
    DisableBackread(35000711)
    DisableBackread(35000712)
    DisableBackread(Characters.DungEater1)
    DisableBackread(Characters.DungEater0)
    Event_35000050()
    Event_35000519()
    Event_35002600()
    CommonFunc_90005261(0, character=Characters.Imp0, region=35002200, radius=2.0, seconds=0.0, animation_id=-1)
    Event_35002200()
    CommonFunc_90005211(
        0,
        character=Characters.Imp1,
        animation_id=30009,
        animation_id_1=20009,
        region=35002201,
        radius=2.5,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp2,
        animation_id=30002,
        animation_id_1=20002,
        region=35002202,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002203()
    CommonFunc_90005211(
        0,
        character=Characters.Imp4,
        animation_id=30000,
        animation_id_1=20000,
        region=35002204,
        radius=0.0,
        seconds=11.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp5,
        animation_id=30004,
        animation_id_1=20004,
        region=35002205,
        radius=2.0,
        seconds=8.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp6, region=35002226, radius=2.0, seconds=0.0, animation_id=3006)
    CommonFunc_90005211(
        0,
        character=Characters.Imp7,
        animation_id=30004,
        animation_id_1=20004,
        region=35002205,
        radius=2.0,
        seconds=3.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp8,
        animation_id=30002,
        animation_id_1=20002,
        region=35002208,
        radius=1.0,
        seconds=4.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002208()
    CommonFunc_90005211(
        0,
        character=Characters.Imp9,
        animation_id=30010,
        animation_id_1=20010,
        region=35002209,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp10,
        animation_id=30004,
        animation_id_1=20004,
        region=35002210,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Imp11, region=35002211, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=Characters.Imp12,
        animation_id=30010,
        animation_id_1=20010,
        region=35002212,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp13,
        animation_id=30000,
        animation_id_1=20000,
        region=35002213,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp14,
        animation_id=30010,
        animation_id_1=20010,
        region=35002214,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp15,
        animation_id=30010,
        animation_id_1=20010,
        region=35002215,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002215()
    CommonFunc_90005211(
        0,
        character=Characters.Imp16,
        animation_id=30004,
        animation_id_1=20004,
        region=35002217,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp17,
        animation_id=30004,
        animation_id_1=20004,
        region=35002217,
        radius=2.0,
        seconds=0.30000001192092896,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp18,
        animation_id=30002,
        animation_id_1=20002,
        region=35002218,
        radius=0.5,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Imp19,
        animation_id=30000,
        animation_id_1=20000,
        region=35002219,
        radius=0.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002220(
        0,
        character=Characters.SmallLivingPot0,
        animation_id=30001,
        animation_id_1=20001,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002220(
        1,
        character=Characters.SmallLivingPot1,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002220(
        2,
        character=Characters.SmallLivingPot2,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002220(
        3,
        character=Characters.SmallLivingPot3,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002220(
        4,
        character=Characters.LivingPot,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002226(
        0,
        character=35000426,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.5,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002226(
        1,
        character=35000427,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.5,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002226(
        2,
        character=35000428,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=35000385, region=35002385, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=35000386,
        animation_id=30003,
        animation_id_1=20003,
        region=35002386,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=35000387,
        animation_id=30004,
        animation_id_1=20004,
        region=35002387,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Rat0, region=35002230, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat1, region=35002230, radius=0.5, seconds=0.5, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat2, region=35002230, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Rat3,
        region=35002230,
        radius=0.5,
        seconds=0.20000000298023224,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Rat4, region=35002230, radius=0.5, seconds=0.0, animation_id=0)
    Event_35002230(0, character=Characters.Rat0, seconds=10.0)
    Event_35002230(1, character=Characters.Rat1, seconds=15.0)
    Event_35002230(2, character=Characters.Rat2, seconds=12.0)
    Event_35002230(3, character=Characters.Rat3, seconds=16.0)
    Event_35002230(4, character=Characters.Rat4, seconds=17.0)
    CommonFunc_90005261(0, character=Characters.Rat5, region=35002235, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Rat6, region=35002236, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Rat7, region=35002237, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat8, region=35002237, radius=2.0, seconds=0.0, animation_id=0)
    Event_35002239(0, character=Characters.Rat9, region=35002239, radius=0.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(0, character=Characters.Rat10, region=35002240, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Rat11, region=35002243, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.GiantRat, region=35002248, radius=2.0, seconds=0.0, animation_id=0)
    Event_35002240(0, character=Characters.Rat11)
    Event_35002240(1, character=Characters.GiantRat)
    CommonFunc_90005261(0, character=Characters.Commoner0, region=0, radius=1.5, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Commoner1, region=35002286, radius=0.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Commoner2, region=35002288, radius=0.5, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(0, character=35000260, region=35002260, radius=2.0, seconds=3.0, animation_id=3037)
    Event_35002261(
        0,
        character=Characters.RevenantFollower0,
        region=35002261,
        radius=3.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005251(0, character=Characters.RevenantFollower1, radius=1.0, seconds=0.0, animation_id=0)
    Event_35002261(
        1,
        character=Characters.RevenantFollower2,
        region=35002263,
        radius=3.0,
        seconds=0.0,
        animation_id=3022,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=35002380,
        radius=4.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower4,
        region=35002267,
        radius=4.0,
        seconds=0.0,
        animation_id=3022,
    )
    Event_35002261(
        2,
        character=Characters.RevenantFollower5,
        region=35002268,
        radius=3.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower6,
        region=35002269,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower0,
        region=35002271,
        radius=3.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower1,
        region=35002272,
        radius=3.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower2,
        region=35002275,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.MirandaFlower3,
        region=35002276,
        radius=2.0,
        seconds=0.5,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=35000277, region=35002276, radius=2.0, seconds=0.5, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower4,
        animation_id=30000,
        animation_id_1=20000,
        region=35002278,
        radius=3.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.MirandaFlower5,
        animation_id=30000,
        animation_id_1=20000,
        region=35002278,
        radius=3.0,
        seconds=0.800000011920929,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FrenziedNomad0,
        region=35002390,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.FrenziedNomad1,
        region=35002390,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_35002390(0, character=Characters.FrenziedNomad0)
    Event_35002390(1, character=Characters.FrenziedNomad1)
    Event_35002392(0, character=Characters.FrenziedNomad2, animation_id=30013)
    Event_35002392(1, character=Characters.FrenziedNomad3, animation_id=30013)
    Event_35002392(2, character=Characters.FrenziedNomad4, animation_id=30013)
    Event_35002392(3, character=Characters.FrenziedNomad5, animation_id=30013)
    Event_35002392(4, character=Characters.FrenziedNomad6, animation_id=30013)
    Event_35002392(5, character=Characters.FrenziedNomad7, animation_id=30013)
    Event_35002392(6, character=Characters.FrenziedNomad8, animation_id=30012)
    Event_35002392(7, character=Characters.FrenziedNomad9, animation_id=30013)
    CommonFunc_90005271(0, character=Characters.FrenziedNomad9, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Basilisk0, region=35002290, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Basilisk1, region=35002290, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.Basilisk2,
        region=35002290,
        radius=3.0,
        seconds=0.800000011920929,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Basilisk3, region=35002293, radius=3.0, seconds=0.0, animation_id=3001)
    Event_35002290(0, character=Characters.Basilisk0)
    Event_35002290(1, character=Characters.Basilisk1)
    Event_35002290(2, character=Characters.Basilisk2)
    CommonFunc_90005261(0, character=Characters.Basilisk4, region=35002296, radius=3.0, seconds=0.0, animation_id=0)
    Event_35002296(0, character=Characters.Basilisk4)
    Event_35002297(0, character=Characters.Basilisk5, region=35002297, radius=4.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005261(0, character=Characters.Basilisk6, region=35002298, radius=3.0, seconds=1.5, animation_id=0)
    Event_35002298()
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellFootSoldier0,
        region=35002380,
        radius=2.0,
        seconds=0.0,
        animation_id=1800,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellFootSoldier1,
        region=35002380,
        radius=2.0,
        seconds=0.0,
        animation_id=1800,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellFootSoldier2,
        region=35002380,
        radius=2.0,
        seconds=0.0,
        animation_id=1800,
    )
    CommonFunc_90005261(
        0,
        character=Characters.LeyndellFootSoldier3,
        region=35002384,
        radius=1.0,
        seconds=0.0,
        animation_id=1800,
    )
    Event_35002258(0, character=Characters.LeyndellFootSoldier2)
    Event_35002258(1, character=Characters.Slug6)
    CommonFunc_90005261(0, character=Characters.PutridCorpse0, region=35002370, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.PutridCorpse1, region=0, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=35000372, region=35002372, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(0, character=Characters.PutridCorpse3, region=35002275, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30005,
        animation_id_1=20005,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005261(0, character=Characters.PutridCorpse5, region=0, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Slug1, region=35002301, radius=2.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(0, character=Characters.Slug6, region=35002307, radius=0.0, seconds=1.5, animation_id=3003)
    CommonFunc_90005211(
        0,
        character=Characters.Slug13,
        animation_id=30000,
        animation_id_1=20000,
        region=35002314,
        radius=2.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Slug25, region=35002327, radius=2.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(
        0,
        character=Characters.Slug26,
        region=35002327,
        radius=2.0,
        seconds=0.4000000059604645,
        animation_id=3003,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Slug27,
        region=35002327,
        radius=2.0,
        seconds=0.6000000238418579,
        animation_id=3003,
    )
    Event_35002320(0, character=Characters.Slug0, animation_id=30001)
    Event_35002320(1, character=35000302, animation_id=30001)
    Event_35002320(2, character=Characters.Slug2, animation_id=30001)
    Event_35002320(3, character=Characters.Slug3, animation_id=30000)
    Event_35002320(4, character=Characters.Slug4, animation_id=30001)
    Event_35002320(5, character=Characters.Slug5, animation_id=30000)
    Event_35002320(6, character=Characters.Slug7, animation_id=30000)
    Event_35002320(7, character=Characters.Slug8, animation_id=30000)
    Event_35002320(8, character=Characters.Slug9, animation_id=30000)
    Event_35002320(9, character=Characters.Slug10, animation_id=30000)
    Event_35002320(10, character=Characters.Slug11, animation_id=30001)
    Event_35002320(11, character=Characters.Slug12, animation_id=30000)
    Event_35002320(12, character=Characters.Slug14, animation_id=30000)
    Event_35002320(13, character=Characters.Slug15, animation_id=30000)
    Event_35002320(14, character=Characters.Slug16, animation_id=30001)
    Event_35002320(15, character=Characters.Slug17, animation_id=30001)
    Event_35002320(16, character=Characters.Slug18, animation_id=30000)
    Event_35002320(17, character=Characters.Slug19, animation_id=30000)
    Event_35002320(18, character=Characters.Slug20, animation_id=30000)
    Event_35002320(19, character=Characters.Slug21, animation_id=30001)
    Event_35002320(20, character=35000323, animation_id=30001)
    Event_35002320(21, character=Characters.Slug22, animation_id=30000)
    Event_35002320(22, character=Characters.Slug23, animation_id=30000)
    Event_35002320(23, character=Characters.Slug24, animation_id=30000)
    CommonFunc_90005271(0, character=Characters.Slug43, seconds=0.0, animation_id=0)
    CommonFunc_90005271(0, character=Characters.Slug44, seconds=0.0, animation_id=0)
    CommonFunc_90005271(0, character=Characters.Slug45, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Snail,
        animation_id=30002,
        animation_id_1=20002,
        region=35002250,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002250()
    Event_35002251()
    Event_35002253()
    CommonFunc_90005261(0, character=Characters.Scarab5, region=35002495, radius=0.5, seconds=0.5, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Scarab6, region=35002496, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Scarab7,
        animation_id=30003,
        animation_id_1=20003,
        region=35002497,
        radius=1.0,
        seconds=6.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Scarab0, region=35002490, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Scarab1, region=35002491, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Scarab2, region=35002492, radius=0.5, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.Scarab3,
        animation_id=30003,
        animation_id_1=20003,
        region=35002493,
        radius=1.5,
        seconds=2.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Scarab4,
        animation_id=30003,
        animation_id_1=20003,
        region=35002494,
        radius=0.5,
        seconds=1.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=35000495, character=Characters.Scarab5, item_lot=35000970, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000496, character=Characters.Scarab6, item_lot=35000980, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000497, character=Characters.Scarab7, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000490, character=Characters.Scarab0, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000491, character=Characters.Scarab1, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000492, character=Characters.Scarab2, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000493, character=Characters.Scarab3, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=35000494, character=Characters.Scarab4, item_lot=0, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=Characters.Omen0,
        animation_id=30000,
        animation_id_1=20000,
        region=35002360,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Omen1,
        animation_id=30000,
        animation_id_1=20000,
        region=35002361,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Omen1, region=35002361, seconds=0.20000000298023224, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Omen2, region=35002362, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Omen3, region=35002363, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.Omen5, region=35002366, radius=3.0, seconds=0.0, animation_id=3024)
    Event_35002365(
        0,
        character=Characters.Omen4,
        region=35002364,
        radius=2.0,
        seconds=0.5,
        animation_id=1700,
        character_1=Characters.Omen6,
    )
    Event_35002365(
        1,
        character=Characters.Omen6,
        region=35002364,
        radius=2.0,
        seconds=0.5,
        animation_id=1700,
        character_1=Characters.Omen4,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Omen7,
        animation_id=30000,
        animation_id_1=20000,
        region=35002369,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaFlower0,
        region=35002280,
        radius=3.0,
        seconds=0.0,
        animation_id=3002,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaFlower1,
        region=35002281,
        radius=3.0,
        seconds=1.5,
        animation_id=3001,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaFlower2,
        region=35002282,
        radius=3.0,
        seconds=0.0,
        animation_id=3003,
    )
    CommonFunc_90005261(
        0,
        character=Characters.GiantMirandaFlower3,
        region=35002284,
        radius=3.0,
        seconds=3.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.Revenant,
        animation_id=30000,
        animation_id_1=20000,
        region=35002258,
        radius=2.0,
        seconds=7.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002400()
    CommonFunc_90005211(
        0,
        character=Characters.GiantLobster1,
        animation_id=30000,
        animation_id_1=20000,
        region=35002401,
        radius=3.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002401()
    CommonFunc_90005211(
        0,
        character=Characters.Fingercreeper,
        animation_id=30000,
        animation_id_1=20000,
        region=35002416,
        radius=1.0,
        seconds=0.699999988079071,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002410(
        0,
        character=Characters.LesserFingercreeper0,
        animation_id=30005,
        animation_id_1=20005,
        region=35002410,
        radius=5.0,
        seconds=4.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002410(
        1,
        character=Characters.LesserFingercreeper1,
        animation_id=30005,
        animation_id_1=20005,
        region=35002410,
        radius=5.0,
        seconds=4.300000190734863,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002410(
        2,
        character=Characters.LesserFingercreeper2,
        animation_id=30005,
        animation_id_1=20005,
        region=35002410,
        radius=5.0,
        seconds=5.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002411()
    Event_35002430(
        0,
        character=Characters.PutridCorpse8,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002430(
        1,
        character=Characters.PutridCorpse7,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002430(
        3,
        character=35000436,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002430(
        4,
        character=35000435,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002430(
        5,
        character=35000434,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002430(
        7,
        character=35000433,
        animation_id=0,
        animation_id_1=3016,
        region=35002431,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare1,
        animation_id=30000,
        animation_id_1=20000,
        region=35002430,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse6,
        animation_id=30000,
        animation_id_1=20000,
        region=35002430,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_35002440(0, character=35005431)
    Event_35002440(3, character=35000439)
    Event_35002440(4, character=35000440)
    Event_35002430(
        8,
        character=Characters.PutridCorpse15,
        animation_id=0,
        animation_id_1=3016,
        region=35002448,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse21,
        region=35002454,
        radius=1.0,
        seconds=0.0,
        animation_id=3030,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse22,
        region=35002454,
        radius=1.0,
        seconds=0.5,
        animation_id=3031,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse11,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse14,
        animation_id=30002,
        animation_id_1=20002,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse13,
        animation_id=30002,
        animation_id_1=20002,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpse12,
        animation_id=30001,
        animation_id_1=20001,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=35005435, region=35002614, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.PutridCorpse16, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000439, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000440, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000441, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000442, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000447, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=35000458, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.PutridCorpse18, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30000,
        animation_id_1=20000,
        region=35002475,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpseBare0,
        animation_id=30000,
        animation_id_1=20000,
        region=35002475,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse10,
        animation_id=30000,
        animation_id_1=20000,
        region=35002475,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse17,
        animation_id=30006,
        animation_id_1=20006,
        region=35002222,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse19,
        animation_id=30006,
        animation_id_1=20006,
        region=35002222,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PutridCorpse18, region=35002222, seconds=0.0, animation_id=3023)
    CommonFunc_90005250(0, character=Characters.PutridCorpse16, region=35002449, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse23,
        animation_id=30001,
        animation_id_1=20001,
        region=35002456,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse24,
        animation_id=30002,
        animation_id_1=20002,
        region=35002456,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=35000458,
        animation_id=30001,
        animation_id_1=20001,
        region=35002456,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Omen9,
        animation_id=30000,
        animation_id_1=20000,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Omen11, region=35002365, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.Omen11,
        animation_id=30000,
        animation_id_1=20000,
        region=35002365,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Omen5,
        animation_id=30000,
        animation_id_1=20000,
        region=35002366,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Omen6, region=35002366, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Omen10, region=35002483, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Omen8, region=35002483, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Omen12, region=35002483, seconds=0.0, animation_id=-1)


@ContinueOnRest(35000050)
def Event_35000050():
    """Event 35000050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(35000670)
    DisableFlag(35000675)


@RestartOnRest(35002498)
def Event_35002498():
    """Event 35002498"""
    GotoIfFlagEnabled(Label.L0, flag=35000598)
    EnableNavmeshType(navmesh_id=35002498, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(FlagEnabled(35000598))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNavmeshType(navmesh_id=35002498, navmesh_type=NavmeshType.Solid)
    End()


@ContinueOnRest(35002500)
def Event_35002500():
    """Event 35002500"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=35000501)
    GotoIfFlagDisabled(Label.L0, flag=35000500)
    EndOfAnimation(asset=Assets.AEG027_170_0500, animation_id=1)
    EnableAsset(Assets.AEG027_165_0500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(Assets.AEG027_165_0500)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasHeadArmorEquipped(armor=PLAYER))
    AND_1.Add(PlayerHasBodyArmorEquipped(armor=10100))
    AND_1.Add(PlayerHasArmsArmorEquipped(armor=10200))
    AND_1.Add(PlayerHasLegsArmorEquipped(armor=10300))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9640, entity=Assets.AEG027_170_0500))
    
    MAIN.Await(AND_1)
    
    EnableFlag(35000500)
    EnableFlag(108)
    if FlagEnabled(110):
        EnableFlag(109)
    EnableFlag(7500)
    EnableFlag(35000501)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=35000000,
        cutscene_flags=0,
        move_to_region=35002500,
        map_id=35000000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    WaitFramesAfterCutscene(frames=1)
    DisableFlag(35000501)
    EndOfAnimation(asset=Assets.AEG027_170_0500, animation_id=1)
    EnableAsset(Assets.AEG027_165_0500)
    EnableFlag(9431)
    EnableFlag(9430)


@ContinueOnRest(35002504)
def Event_35002504():
    """Event 35002504"""
    GotoIfFlagDisabled(Label.L0, flag=35000504)
    DisableAsset(Assets.AEG099_002_9000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=35002504)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    CreateAssetVFX(Assets.AEG099_002_9000, vfx_id=101, model_point=1540)
    EnableNetworkFlag(35002504)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9505, entity=Assets.AEG099_002_9000))
    AND_2.Add(FlagEnabled(400001))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20005, anchor_entity=Assets.AEG099_002_9000, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(35000504)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    DisableAsset(Assets.AEG099_002_9000)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteAssetVFX(Assets.AEG099_002_9000)
    CreateAssetVFX(Assets.AEG099_002_9000, vfx_id=101, model_point=1540)
    End()


@RestartOnRest(35002506)
def Event_35002506():
    """Event 35002506"""
    GotoIfFlagDisabled(Label.L0, flag=35000506)
    DisableAsset(Assets.AEG027_050_0500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002506))
    
    MAIN.Await(AND_1)
    
    Wait(0.15000000596046448)
    OR_2.Add(CharacterDead(PLAYER))
    OR_2.Add(HealthValue(PLAYER) == 0)
    if OR_2:
        return
    DestroyAsset(Assets.AEG027_050_0500)
    EnableFlag(35000506)


@RestartOnRest(35002508)
def Event_35002508():
    """Event 35002508"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=35000506)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=35002508))
    
    AddSpecialEffect(PLAYER, 4080)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=35002508))
    
    RemoveSpecialEffect(PLAYER, 4080)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@RestartOnRest(35002600)
def Event_35002600():
    """Event 35002600"""
    GotoIfFlagDisabled(Label.L0, flag=300)
    DisableCharacter(35005230)
    DisableAnimations(35005230)
    DisableAsset(Assets.AEG099_610_9000)
    DisableTreasure(asset=Assets.AEG099_610_9000)
    EnableAsset(Assets.AEG099_610_9031)
    EnableTreasure(asset=Assets.AEG099_610_9031)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(35008540):
        EnableFlag(35008540)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG023_315_1000)
    EnableAsset(Assets.AEG099_610_9000)
    EnableTreasure(asset=Assets.AEG099_610_9000)
    DisableAsset(Assets.AEG099_610_9031)
    DisableTreasure(asset=Assets.AEG099_610_9031)


@ContinueOnRest(35002510)
def Event_35002510():
    """Event 35002510"""
    CommonFunc_90005500(
        0,
        flag=35000510,
        flag_1=35000511,
        left=0,
        asset=Assets.AEG027_017_0500,
        asset_1=Assets.AEG027_002_0501,
        obj_act_id=35003511,
        asset_2=Assets.AEG027_002_0500,
        obj_act_id_1=35003512,
        region=35002511,
        region_1=35002512,
        flag_2=35000512,
        flag_3=35000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=35000515,
        flag_1=35000516,
        left=0,
        asset=Assets.AEG027_016_0500,
        asset_1=Assets.AEG027_002_0505,
        obj_act_id=35003516,
        asset_2=Assets.AEG027_002_0504,
        obj_act_id_1=35003517,
        region=35002516,
        region_1=35002517,
        flag_2=35000517,
        flag_3=35000518,
        left_1=0,
    )
    CommonFunc_90005681(0, flag=35000670, flag_1=35000671, flag_2=35000672, flag_3=35000673, attacked_entity=35001670)
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103370,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103360,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103350,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103340,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103330,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103320,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103310,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=35000672,
            source_entity=Assets.AEG027_003_0500,
            region=35002670,
            owner_entity=Characters.TalkDummy4,
            behavior_id=801103300,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    CommonFunc_90005681(0, flag=35000675, flag_1=35000676, flag_2=35000677, flag_3=35000678, attacked_entity=35001675)
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103370,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103360,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103350,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103340,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103330,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103320,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103310,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(
            0,
            flag=35000677,
            source_entity=Assets.AEG027_003_0501,
            region=35002675,
            owner_entity=Characters.TalkDummy5,
            behavior_id=801103300,
            behavior_id_1=801103305,
            model_point=102,
            model_point_1=0,
            model_point_2=0,
            model_point_3=0,
        )


@ContinueOnRest(35000519)
def Event_35000519():
    """Event 35000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(35000510)
    DisableFlag(35000520)


@ContinueOnRest(35002679)
def Event_35002679():
    """Event 35002679"""
    CommonFunc_90005681(0, flag=35000670, flag_1=35000671, flag_2=35000672, flag_3=35000672, attacked_entity=35001670)


@RestartOnRest(35002490)
def Event_35002490(_, flag: uint, asset: uint, flag_1: uint):
    """Event 35002490"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(35002200)
def Event_35002200():
    """Event 35002200"""
    OR_15.Add(CharacterDead(Characters.Imp0))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(Characters.Imp0, 17155)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=Characters.Imp0, other_entity=PLAYER, radius=2.0))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Imp0))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(Characters.Imp0, 17155)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002203)
def Event_35002203():
    """Event 35002203"""
    OR_15.Add(CharacterDead(Characters.Imp3))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    ForceAnimation(Characters.Imp3, 30002)
    DisableAI(Characters.Imp3)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002203))
    AND_10.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_10.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_2.Add(AND_9)
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=35002220))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(Characters.Imp3, 20002, loop=True)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(Characters.Imp3, 20004, loop=True)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(Characters.Imp3)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002208)
def Event_35002208():
    """Event 35002208"""
    OR_15.Add(CharacterDead(Characters.Imp8))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(Characters.Imp8, 8081)
    AddSpecialEffect(Characters.Imp8, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=Characters.Imp8, other_entity=PLAYER, radius=2.0))
    OR_2.Add(AND_1)
    OR_2.Add(CharacterInsideRegion(character=Characters.Imp8, region=35002206))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Imp8))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(Characters.Imp8, 8081)
    RemoveSpecialEffect(Characters.Imp8, 8082)
    RemoveSpecialEffect(Characters.Imp8, 5000)
    AddSpecialEffect(Characters.Imp8, 17153)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002215)
def Event_35002215():
    """Event 35002215"""
    OR_15.Add(CharacterDead(Characters.Imp15))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002216))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Imp15))
    
    MAIN.Await(OR_2)
    
    ForceAnimation(Characters.Imp15, 3006)
    RemoveSpecialEffect(Characters.Imp15, 8081)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002220)
def Event_35002220(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 35002220"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.SmallLivingPot0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.SmallLivingPot1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.SmallLivingPot2))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.SmallLivingPot3))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.LivingPot))
    OR_3.Add(HasAIStatus(Characters.SmallLivingPot0, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.SmallLivingPot1, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.SmallLivingPot2, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.SmallLivingPot3, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(Characters.LivingPot, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    OR_5.Add(AND_1)
    OR_5.Add(OR_2)
    OR_5.Add(OR_3)
    
    MAIN.Await(OR_5)
    
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


@RestartOnRest(35002226)
def Event_35002226(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 35002226"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=35002426))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000426))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000427))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000428))
    OR_3.Add(HasAIStatus(35000426, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(35000427, ai_status=AIStatusType.Battle))
    OR_3.Add(HasAIStatus(35000428, ai_status=AIStatusType.Battle))
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
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_2)
    OR_5.Add(OR_3)
    OR_5.Add(AND_4)
    OR_5.Add(AND_5)
    OR_5.Add(AND_6)
    OR_5.Add(AND_7)
    OR_5.Add(AND_8)
    
    MAIN.Await(OR_5)
    
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
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


@RestartOnRest(35002230)
def Event_35002230(_, character: uint, seconds: float):
    """Event 35002230"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002230))
    OR_5.Add(AND_1)
    
    MAIN.Await(OR_5)
    
    Wait(seconds)
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    RemoveSpecialEffect(character, 5000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002239)
def Event_35002239(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002239"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    EnableCharacter(character)
    EnableAnimations(character)


@RestartOnRest(35002240)
def Event_35002240(_, character: uint):
    """Event 35002240"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    RemoveSpecialEffect(character, 5000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002250)
def Event_35002250():
    """Event 35002250"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002380))
    AND_2.Add(AND_1)
    AND_2.Add(CharacterHasSpecialEffect(Characters.Snail, 15007))
    
    MAIN.Await(AND_2)
    
    EnableSpawner(entity=35003380)
    EnableSpawner(entity=35003381)
    EnableSpawner(entity=35003382)
    EnableSpawner(entity=35003383)
    EnableSpawner(entity=35003388)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002251)
def Event_35002251():
    """Event 35002251"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002380))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15007))
    OR_5.Add(AND_1)
    OR_5.Add(AttackedWithDamageType(attacked_entity=35000350))
    
    MAIN.Await(OR_5)
    
    DisableSpawner(entity=35003380)
    DisableSpawner(entity=35003381)
    DisableSpawner(entity=35003382)
    DisableSpawner(entity=35003383)
    DisableSpawner(entity=35003388)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002253)
def Event_35002253():
    """Event 35002253"""
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    
    MAIN.Await(CharacterDead(Characters.Snail))
    
    Kill(Characters.LeyndellFootSoldier0, award_runes=True)
    Kill(Characters.LeyndellFootSoldier1, award_runes=True)
    Kill(Characters.LeyndellFootSoldier2, award_runes=True)
    Kill(Characters.LeyndellFootSoldier2, award_runes=True)
    Kill(Characters.LeyndellFootSoldier3, award_runes=True)
    Kill(Characters.LeyndellSoldier, award_runes=True)
    DisableSpawner(entity=35003380)
    DisableSpawner(entity=35003381)
    DisableSpawner(entity=35003382)
    DisableSpawner(entity=35003383)
    DisableSpawner(entity=35003388)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002258)
def Event_35002258(_, character: uint):
    """Event 35002258"""
    OR_15.Add(CharacterDead(character))
    if OR_15:
        return
    AddSpecialEffect(character, 8092)
    Restart()


@RestartOnRest(35002261)
def Event_35002261(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002261"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(35002290)
def Event_35002290(_, character: uint):
    """Event 35002290"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AddSpecialEffect(character, 5000)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=4.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    RemoveSpecialEffect(character, 5000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002296)
def Event_35002296(_, character: uint):
    """Event 35002296"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=4.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002297)
def Event_35002297(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 35002297"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(35002298)
def Event_35002298():
    """Event 35002298"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(HasAIStatus(Characters.Basilisk6, ai_status=AIStatusType.Battle))
    OR_2.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Basilisk6))
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_1)
    Wait(0.5)
    if ValueNotEqual(left=3001, right=-1):
        ForceAnimation(Characters.Basilisk6, 3001, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(35002320)
def Event_35002320(_, character: uint, animation_id: int):
    """Event 35002320"""
    OR_15.Add(CharacterDead(character))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    DisableAI(character)
    ForceAnimation(character, animation_id)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002361)
def Event_35002361():
    """Event 35002361"""

    # --- Label 0 --- #
    DefineLabel(0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002358))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    DisableAI(Characters.Omen1)
    SetNest(Characters.Omen1, region=35002359)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002357))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableAI(Characters.Omen1)
    GotoIfFlagEnabled(Label.L0, flag=35002361)


@RestartOnRest(35002365)
def Event_35002365(
    _,
    character: uint,
    region: uint,
    radius: float,
    seconds: float,
    animation_id: int,
    character_1: uint,
):
    """Event 35002365"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1))
    OR_2.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    OR_5.Add(AttackedWithDamageType(attacked_entity=character))
    OR_5.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_2)
    
    MAIN.Await(OR_5)
    
    EnableThisNetworkSlotFlag()
    GotoIfFinishedConditionFalse(Label.L1, input_condition=OR_2)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)


@RestartOnRest(35002390)
def Event_35002390(_, character: uint):
    """Event 35002390"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)
    EnableThisNetworkSlotFlag()


@RestartOnRest(35002392)
def Event_35002392(_, character: uint, animation_id: int):
    """Event 35002392"""
    DisableAI(character)
    ForceAnimation(character, animation_id)


@RestartOnRest(35002400)
def Event_35002400():
    """Event 35002400"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=35002400))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.GiantLobster0, radius=3.0))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000385))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    RemoveSpecialEffect(Characters.GiantLobster0, 8085)


@RestartOnRest(35002401)
def Event_35002401():
    """Event 35002401"""
    AddSpecialEffect(Characters.GiantLobster1, 8092)


@RestartOnRest(35002410)
def Event_35002410(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 35002410"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_2.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.Fingercreeper))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.LesserFingercreeper0))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.LesserFingercreeper1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.LesserFingercreeper2))
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
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(OR_2)
    OR_5.Add(AND_4)
    OR_5.Add(AND_5)
    OR_5.Add(AND_6)
    OR_5.Add(AND_7)
    OR_5.Add(AND_8)
    
    MAIN.Await(OR_5)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        ForceAnimation(character, animation_id_1, loop=True)
    EnableCharacterCollision(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(35002411)
def Event_35002411():
    """Event 35002411"""
    if FlagDisabled(11109959):
        return
    DisableCharacter(Characters.Fingercreeper)
    DisableCharacter(Characters.LesserFingercreeper0)
    DisableCharacter(Characters.LesserFingercreeper1)
    DisableCharacter(Characters.LesserFingercreeper2)


@RestartOnRest(35002430)
def Event_35002430(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 35002430"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
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


@RestartOnRest(35002440)
def Event_35002440(_, character: uint):
    """Event 35002440"""
    Kill(character)


@RestartOnRest(35003500)
def Event_35003500(_, region: uint):
    """Event 35003500"""
    DisableNetworkSync()
    AND_2.Add(CharacterInsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(20000, 9621)
    Wait(0.10000000149011612)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterOutsideRegion(character=20000, region=region))
    
    MAIN.Await(AND_3)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(20000, 9621)
    Restart()


@ContinueOnRest(35002530)
def Event_35002530():
    """Event 35002530"""
    GotoIfFlagEnabled(Label.L0, flag=35000530)
    EndOfAnimation(asset=Assets.AEG027_015_0500, animation_id=0)
    DisableAssetActivation(Assets.AEG027_002_0502, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=35003531))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(35000350)
    DisableAssetActivation(Assets.AEG027_002_0502, obj_act_id=-1)
    ForceAnimation(35001350, 1)


@ContinueOnRest(35002642)
def Event_35002642():
    """Event 35002642"""
    DisableAssetActivation(Assets.AEG027_041_0502, obj_act_id=27041)
    EndOfAnimation(asset=Assets.AEG027_041_0502, animation_id=1)
    End()


@RestartOnRest(35002580)
def Event_35002580():
    """Event 35002580"""
    RegisterLadder(start_climbing_flag=35000580, stop_climbing_flag=35000581, asset=Assets.AEG027_210_0503)
    RegisterLadder(start_climbing_flag=35000582, stop_climbing_flag=35000583, asset=Assets.AEG027_210_0502)
    RegisterLadder(start_climbing_flag=35000584, stop_climbing_flag=35000585, asset=Assets.AEG027_212_0501)
    RegisterLadder(start_climbing_flag=35000586, stop_climbing_flag=35000587, asset=Assets.AEG027_209_0500)
    RegisterLadder(start_climbing_flag=35000588, stop_climbing_flag=35000589, asset=Assets.AEG027_212_0500)
    RegisterLadder(start_climbing_flag=35000590, stop_climbing_flag=35000591, asset=Assets.AEG027_210_0500)
    RegisterLadder(start_climbing_flag=35000592, stop_climbing_flag=35000593, asset=Assets.AEG027_210_0501)


@RestartOnRest(35002680)
def Event_35002680():
    """Event 35002680"""
    RegisterLadder(start_climbing_flag=35000680, stop_climbing_flag=35000681, asset=Assets.AEG027_211_0500)


@RestartOnRest(35002800)
def Event_35002800():
    """Event 35002800"""
    if FlagEnabled(35000800):
        return
    
    MAIN.Await(HealthValue(Characters.Mohg) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.Mohg, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Mohg))
    
    KillBossAndDisplayBanner(character=Characters.Mohg, banner_type=BannerType.GreatEnemyFelled)
    EnableAssetActivation(35001660, obj_act_id=-1)
    EnableFlag(35000800)
    EnableFlag(9125)
    if PlayerInOwnWorld():
        EnableFlag(61125)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002825, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002826, anchor_type=CoordEntityType.Region)


@RestartOnRest(35002810)
def Event_35002810():
    """Event 35002810"""
    GotoIfFlagDisabled(Label.L0, flag=35000800)
    DisableCharacter(Characters.Mohg)
    DisableAnimations(Characters.Mohg)
    Kill(Characters.Mohg)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002825, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=800370, anchor_entity=35002826, anchor_type=CoordEntityType.Region)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Mohg)
    DisableAssetActivation(35001660, obj_act_id=-1)
    GotoIfFlagEnabled(Label.L1, flag=35000801)
    AddSpecialEffect(Characters.Dummy0, 9531)
    ForceAnimation(Characters.Mohg, 30001)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002802))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.Mohg, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(35000801)
    DisableHealthBar(Characters.Mohg)
    ForceAnimation(Characters.Mohg, 20001)
    Wait(3.0)
    AddSpecialEffect(Characters.Dummy0, 9532)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(35002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=35002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkUpdateRate(Characters.Mohg, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Mohg, name=904800002, bar_slot=1)
    Wait(1.0)
    EnableAI(Characters.Mohg)
    if FlagEnabled(35000800):
        return
    AND_1.Add(HealthRatio(Characters.Mohg) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(35002802)


@RestartOnRest(35002820)
def Event_35002820():
    """Event 35002820"""
    GotoIfFlagDisabled(Label.L0, flag=35000820)
    ForceAnimation(Assets.AEG027_137_0500, 2, wait_for_completion=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(Assets.AEG027_137_0500, 0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(35002800))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=35002820))
    AND_1.Add(AttackedWithDamageType(attacked_entity=35001820, attacker=20000))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Assets.AEG027_137_0500, 1, wait_for_completion=True)
    EnableFlag(35000820)
    End()


@RestartOnRest(35002849)
def Event_35002849():
    """Event 35002849"""
    CommonFunc_9005800(
        0,
        flag=35000800,
        entity=Assets.AEG099_001_9000,
        region=35002800,
        flag_1=35002805,
        character=35005800,
        action_button_id=10000,
        left=35000801,
        region_1=35002802,
    )
    CommonFunc_9005801(
        0,
        flag=35000800,
        entity=Assets.AEG099_001_9000,
        region=35002800,
        flag_1=35002805,
        flag_2=35002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=35000800, asset=Assets.AEG099_001_9000, model_point=5, right=35000801)
    CommonFunc_9005812(0, flag=35000800, asset=Assets.AEG099_001_9001, model_point=5, right=35000801, model_point_1=5)
    CommonFunc_9005822(
        0,
        flag=35000800,
        bgm_boss_conv_param_id=921600,
        flag_1=35002805,
        flag_2=35002806,
        right=0,
        flag_3=35002802,
        left=0,
        left_1=1,
    )


@RestartOnRest(35002850)
def Event_35002850():
    """Event 35002850"""
    if FlagEnabled(35000850):
        return
    
    MAIN.Await(HealthValue(Characters.EsgarPriestofBlood) <= 0)
    
    Kill(35005850)
    Wait(4.0)
    PlaySoundEffect(Characters.EsgarPriestofBlood, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.EsgarPriestofBlood))
    
    KillBossAndDisplayBanner(character=Characters.EsgarPriestofBlood, banner_type=BannerType.EnemyFelled)
    EnableFlag(35000850)
    EnableFlag(9222)
    EnableFlag(61222)


@RestartOnRest(35002860)
def Event_35002860():
    """Event 35002860"""
    GotoIfFlagDisabled(Label.L0, flag=35000850)
    DisableCharacter(35005850)
    DisableAnimations(35005850)
    Kill(35005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.EsgarPriestofBlood)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(35002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=35002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.EsgarPriestofBlood)
    SetNetworkUpdateRate(Characters.EsgarPriestofBlood, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.EsgarPriestofBlood, name=138600)


@RestartOnRest(35002899)
def Event_35002899():
    """Event 35002899"""
    CommonFunc_9005800(
        0,
        flag=35000850,
        entity=Assets.AEG099_002_9100,
        region=35002850,
        flag_1=35002855,
        character=35005850,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=35000850,
        entity=Assets.AEG099_002_9100,
        region=35002850,
        flag_1=35002855,
        flag_2=35002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=35000850, asset=Assets.AEG099_002_9100, model_point=5, right=0)
    CommonFunc_9005822(
        0,
        flag=35000850,
        bgm_boss_conv_param_id=921700,
        flag_1=35002855,
        flag_2=35002856,
        right=0,
        flag_3=35002852,
        left=0,
        left_1=0,
    )


@RestartOnRest(35000700)
def Event_35000700(_, character: uint, asset: uint):
    """Event 35000700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    DeleteAssetVFX(asset)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3380):
        DisableFlag(1036499202)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L12, flag=3392)
    GotoIfFlagEnabled(Label.L13, flag=3393)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(3392, 3393)))
    
    Restart()

    # --- Label 12 --- #
    DefineLabel(12)
    GotoIfFlagEnabled(Label.L0, flag=3380)
    GotoIfFlagEnabled(Label.L1, flag=3381)
    GotoIfFlagEnabled(Label.L3, flag=3383)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    if FlagDisabled(35000701):
        ForceAnimation(character, 90103)
    else:
        ForceAnimation(character, 90108)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3392))
    
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    DisableCharacter(character)
    DisableBackread(character)
    CreateAssetVFX(asset, vfx_id=100, model_point=600930)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3393))
    
    Restart()


@RestartOnRest(35000702)
def Event_35000702(_, asset: uint, character: uint):
    """Event 35000702"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(35009209))
    
    MoveAssetToCharacter(asset, character=character)


@RestartOnRest(35000703)
def Event_35000703(_, seconds: float):
    """Event 35000703"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=35009209)
    
    MAIN.Await(FlagEnabled(35009209))
    
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(35009211)


@RestartOnRest(35003710)
def Event_35003710(_, character: uint):
    """Event 35003710"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003711)
def Event_35003711(_, character: uint):
    """Event 35003711"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003712)
def Event_35003712(_, character: uint):
    """Event 35003712"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(35003713)
def Event_35003713(_, flag: uint, flag_1: uint, flag_2: uint):
    """Event 35003713"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4705):
        return
    EndIfFlagRangeAnyEnabled(flag_range=(4708, 4710))
    if FlagDisabled(flag_1):
        return
    EnableFlag(flag)
    EnableFlag(4718)
    WaitFrames(frames=1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(35003714)
def Event_35003714(_, region: uint):
    """Event 35003714"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4705):
        return
    if FlagEnabled(4710):
        return
    OR_1.Add(FlagEnabled(35009255))
    OR_1.Add(FlagEnabled(35009254))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(35009261)
    EnableFlag(4718)
    WaitFrames(frames=1)
    EnableFlag(35009250)
    End()


@RestartOnRest(35003715)
def Event_35003715(_, character: uint, flag: uint):
    """Event 35003715"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4703):
        return
    if FlagEnabled(4705):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableAnimations(character)
    Wait(2.0)
    Kill(character, award_runes=True)
    End()


@RestartOnRest(35003720)
def Event_35003720(_, character: uint):
    """Event 35003720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagDisabled(4240):
        DisableFlag(35009303)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(4246))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(4246))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

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
    OR_15.Add(FlagEnabled(4246))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(35003721)
def Event_35003721(_, character: uint):
    """Event 35003721"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_059_9001)
    OR_1.Add(FlagEnabled(4249))
    GotoIfConditionTrue(Label.L5, input_condition=OR_1)
    OR_2.Add(FlagEnabled(4249))
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L4, flag=35009323)
    GotoIfFlagEnabled(Label.L1, flag=4240)
    GotoIfFlagEnabled(Label.L2, flag=4241)
    GotoIfFlagEnabled(Label.L4, flag=4243)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableAsset(Assets.AEG099_059_9001)
    ForceAnimation(character, 90102)
    DisableGravity(character)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableAsset(Assets.AEG099_059_9001)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableBackread(character)
    EnableAsset(Assets.AEG099_059_9001)
    ForceAnimation(character, 90103)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    if FlagEnabled(35009323):
        EnableFlag(35009333)
        EnableAsset(Assets.AEG099_424_9000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(4249))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(35003722)
def Event_35003722(_, entity: uint):
    """Event 35003722"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4243):
        return
    DisableAsset(Assets.AEG099_424_9000)
    AND_1.Add(FlagEnabled(4249))
    OR_1.Add(FlagEnabled(35002725))
    OR_1.Add(FlagEnabled(35002726))
    AND_1.Add(OR_1)
    AwaitConditionTrue(AND_1)
    GotoIfFlagEnabled(Label.L1, flag=35002725)
    GotoIfFlagEnabled(Label.L2, flag=35002726)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(35002725)
    PlayCutscene(35000010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    EnableFlag(35009323)
    DisableFlag(35002726)
    PlayCutscene(35000020, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(35009333)
    ForceAnimation(entity, 90103)
    EnableAsset(Assets.AEG099_424_9000)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    if FlagEnabled(4243):
        return
    Restart()


@RestartOnRest(35003723)
def Event_35003723():
    """Event 35003723"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400382):
        return
    if FlagDisabled(9504):
        return
    EnableNetworkFlag(35009336)
    End()


@ContinueOnRest(35003724)
def Event_35003724(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: uint,
    last_flag: uint,
    flag: uint,
    model_point: int,
):
    """Event 35003724"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    if ValueNotEqual(left=model_point, right=0):
        CreateAssetVFX(asset, vfx_id=90, model_point=model_point)
    else:
        CreateAssetVFX(asset, vfx_id=90, model_point=6101)
    Wait(1.5)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()


@RestartOnRest(35003725)
def Event_35003725():
    """Event 35003725"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(400382):
        return
    if FlagDisabled(4243):
        AND_1.Add(HealthRatio(Characters.DungEater0) < 0.10000000149011612)
        AwaitConditionTrue(AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
    EnableFlag(4243)
    Wait(3.0)
    EnableFlag(35009337)
    End()


@RestartOnRest(35003726)
def Event_35003726():
    """Event 35003726"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4247):
        return
    AwaitFlagEnabled(flag=1045520180)
    DisableNetworkFlag(35009317)
    DisableNetworkFlag(35009318)
    End()


@RestartOnRest(35003727)
def Event_35003727():
    """Event 35003727"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4246):
        return
    AND_1.Add(FlagEnabled(4240))
    AND_1.Add(FlagEnabled(35009306))
    AND_1.Add(EntityWithinDistance(entity=Assets.AEG099_060_9002, other_entity=20000, radius=15.0))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(4258)
    End()


@RestartOnRest(35003730)
def Event_35003730():
    """Event 35003730"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3631):
        return
    if FlagEnabled(3623):
        return
    
    MAIN.Await(FlagEnabled(35000500))
    
    if FlagDisabled(3631):
        return
    GotoIfFlagDisabled(Label.L1, flag=3621)
    EnableFlag(1049539212)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()


@RestartOnRest(35003790)
def Event_35003790():
    """Event 35003790"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(35000500):
        return
    
    MAIN.Await(FlagEnabled(35000500))
    
    if CharacterOutsideRegion(character=20000, region=35002500):
        return
    ForceAnimation(20000, 67020)
    End()
