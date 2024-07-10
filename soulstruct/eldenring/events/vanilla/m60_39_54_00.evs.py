"""
West Altus Plateau (NE) (SE)

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
from .enums.m60_39_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039540000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1039540001, asset=Assets.AEG099_060_9001)
    CommonFunc_9005810(
        0,
        flag=1039540800,
        grace_flag=1039540002,
        character=Characters.TalkDummy2,
        asset=Assets.AEG099_060_9002,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005632(0, flag=580020, asset=Assets.AEG099_386_2000, item_lot=80020)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse6,
        region=1039542213,
        radius=1.0,
        seconds=0.0,
        animation_id=3002,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse11,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542657,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PerfumerTricia3, region=1039542610, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse7,
        region=1039542559,
        radius=0.0,
        seconds=0.0,
        animation_id=3037,
    )
    CommonFunc_90005200(
        0,
        character=1039540615,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug6,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug1,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug4,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug5,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug7,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Slug13,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542615,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1039540630,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542272,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1039540631,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542272,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=1039540632,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542272,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse13,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542616,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse14,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542616,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542616,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Basilisk3, region=1039542667, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.Basilisk4, region=1039542668, seconds=0.5, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Basilisk5, region=1039542668, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk6,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542670,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk8,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542672,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Basilisk7, region=1039542671, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.PerfumerTricia0, region=1039542551, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.PerfumerTricia1, region=1039542552, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.PutridCorpse1, region=1039542206, seconds=0.0, animation_id=3035)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=1039542203, seconds=0.0, animation_id=3036)
    CommonFunc_90005250(0, character=1039540553, region=1039542553, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.PutridCorpse3, region=1039542209, seconds=0.0, animation_id=3016)
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542226,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse27,
        animation_id=30002,
        animation_id_1=20002,
        region=1039542226,
        radius=2.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse29,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542226,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Revenant1,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542303,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.RevenantFollower0, region=1039542504, seconds=2.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse15,
        region=1039542618,
        radius=1.0,
        seconds=0.0,
        animation_id=3002,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse16,
        region=1039542617,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=3002,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse18,
        region=1039542619,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse19,
        region=1039542619,
        radius=1.0,
        seconds=0.800000011920929,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse20,
        region=1039542619,
        radius=1.0,
        seconds=0.800000011920929,
        animation_id=-1,
    )
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight0,
        animation_id=30001,
        animation_id_1=20001,
        region=1039542310,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse21,
        region=1039542250,
        radius=1.0,
        seconds=0.0,
        animation_id=3036,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse17,
        region=1039542227,
        radius=1.0,
        seconds=0.0,
        animation_id=3038,
    )
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse22,
        region=1039542679,
        radius=1.0,
        seconds=0.0,
        animation_id=3002,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse8,
        animation_id=30005,
        animation_id_1=20005,
        region=1039542350,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse9,
        animation_id=30005,
        animation_id_1=20005,
        region=1039542350,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse10,
        animation_id=30005,
        animation_id_1=20005,
        region=1039542350,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.PutridCorpseBare,
        animation_id=30006,
        animation_id_1=20006,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30002,
        animation_id_1=20002,
        region=1039542207,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.RevenantFollower1, region=1039542296, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse23,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse24,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542207,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse25,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542207,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse26,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542207,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Revenant0,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542298,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.PerfumerTricia2, region=1039542555, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.SmallerDog1,
        animation_id=30002,
        animation_id_1=20002,
        region=1039542330,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallerDog0,
        animation_id=30002,
        animation_id_1=20002,
        region=1039542330,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=1039540337, region=1039542330, seconds=0.0, animation_id=3005)
    CommonFunc_90005250(0, character=Characters.WanderingNoble1, region=1039542341, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.WanderingNoble0, region=1039542340, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.Page0, region=1039542320, seconds=0.0, animation_id=3009)
    CommonFunc_90005250(0, character=Characters.WanderingNoble2, region=1039542342, seconds=1.0, animation_id=3000)
    Event_1039542200(0, character=1039540361, region=1039542311, seconds=0.0, animation_id=3005)
    CommonFunc_90005250(0, character=Characters.CleanrotKnight1, region=1039542311, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=1039540338, region=1039542338, seconds=0.0, animation_id=3000)
    CommonFunc_90005250(0, character=Characters.WanderingNoble3, region=1039542343, seconds=0.0, animation_id=3006)
    CommonFunc_90005250(0, character=Characters.Page1, region=1039542322, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.CleanrotKnight2, region=1039542312, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=1039540370, region=1039542636, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540371, region=1039542636, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540372, region=1039542636, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540400, region=1039542654, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540401, region=1039542654, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540402, region=1039542654, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540403, region=1039542654, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540404, region=1039542860, radius=1.0, seconds=10.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540680, region=1039542860, radius=1.0, seconds=2.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540681, region=1039542860, radius=1.0, seconds=4.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540682, region=1039542860, radius=1.0, seconds=0.0, animation_id=-1)
    AddSpecialEffect(1039540680, 4801)
    AddSpecialEffect(1039540681, 4801)
    CommonFunc_90005261(
        0,
        character=1039540420,
        region=1039542639,
        radius=1.0,
        seconds=0.30000001192092896,
        animation_id=3002,
    )
    CommonFunc_90005261(0, character=1039540430, region=1039542615, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540431, region=1039542615, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540440, region=1039542641, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540441, region=1039542641, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540442, region=1039542641, radius=1.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(
        0,
        character=1039540443,
        region=1039542641,
        radius=1.0,
        seconds=0.6000000238418579,
        animation_id=3017,
    )
    CommonFunc_90005261(0, character=1039540444, region=1039542641, radius=1.0, seconds=0.0, animation_id=3017)
    CommonFunc_90005261(0, character=1039540445, region=1039542641, radius=1.0, seconds=4.0, animation_id=3017)
    CommonFunc_90005261(
        0,
        character=1039540446,
        region=1039542641,
        radius=1.0,
        seconds=0.20000000298023224,
        animation_id=3017,
    )
    CommonFunc_90005261(
        0,
        character=1039540447,
        region=1039542641,
        radius=1.0,
        seconds=0.6000000238418579,
        animation_id=3002,
    )
    CommonFunc_90005261(
        0,
        character=1039540448,
        region=1039542641,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=3016,
    )
    CommonFunc_90005261(0, character=1039540449, region=1039542641, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540440, region=1039542642, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540441, region=1039542642, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540442, region=1039542642, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=1039540443,
        region=1039542642,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=1039540444, region=1039542642, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=1039540445,
        region=1039542642,
        radius=1.0,
        seconds=1.2000000476837158,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=1039540446,
        region=1039542642,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=1039540447,
        region=1039542642,
        radius=1.0,
        seconds=0.6000000238418579,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=1039540448,
        region=1039542642,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=1039540449, region=1039542642, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540470, region=1039542658, radius=1.0, seconds=3.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039540471, region=1039542680, radius=1.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(
        0,
        character=Characters.SmallerDog4,
        region=1039542658,
        radius=1.0,
        seconds=0.0,
        animation_id=5012,
    )
    AddSpecialEffect(1039540453, 8081)
    CommonFunc_90005261(0, character=1039540650, region=1039542706, radius=1.0, seconds=5.0, animation_id=3009)
    CommonFunc_90005261(0, character=1039540651, region=1039542706, radius=1.0, seconds=1.0, animation_id=3009)
    CommonFunc_90005261(
        0,
        character=Characters.SmallerDog4,
        region=1039542706,
        radius=1.0,
        seconds=0.0,
        animation_id=5012,
    )
    AddSpecialEffect(1039540515, 4801)
    AddSpecialEffect(1039540650, 5000)
    AddSpecialEffect(1039540650, 4801)
    AddSpecialEffect(1039540650, 8081)
    AddSpecialEffect(1039540655, 4801)
    AddSpecialEffect(1039540655, 5000)
    AddSpecialEffect(1039540655, 8081)
    AddSpecialEffect(1039540655, 8087)
    AddSpecialEffect(Characters.SmallerDog4, 4801)
    CommonFunc_90005261(0, character=1039540655, region=1039542655, radius=1.0, seconds=0.0, animation_id=20)
    CommonFunc_90005261(0, character=1039540656, region=1039542655, radius=1.0, seconds=0.0, animation_id=3008)
    AddSpecialEffect(1039540655, 4801)
    AddSpecialEffect(1039540656, 4801)
    CommonFunc_90005261(
        0,
        character=Characters.PerfumerTricia2,
        region=1039542704,
        radius=5.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=1039540556, region=1039542704, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005501(
        0,
        flag=1039540510,
        flag_1=1039540511,
        left=5,
        asset=Assets.AEG030_858_2001,
        asset_1=Assets.AEG099_026_2001,
        asset_2=Assets.AEG099_026_2000,
        flag_2=1039540512,
    )
    Event_1039542510()
    Event_1039542800()
    Event_1039542810()
    Event_1039542849()
    Event_1039542811()
    CommonFunc_90005261(0, character=1039544680, region=1039546680, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039544681, region=1039546680, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039544650, region=1039546680, radius=1.0, seconds=0.0, animation_id=-1)
    AddSpecialEffect(1039544680, 8087)
    AddSpecialEffect(1039544681, 8087)
    AddSpecialEffect(1039544680, 5000)
    AddSpecialEffect(1039544681, 5000)
    AddSpecialEffect(1039544600, 8033)
    AddSpecialEffect(1039544601, 8033)
    AddSpecialEffect(1039544602, 8033)
    AddSpecialEffect(1039544603, 8033)
    AddSpecialEffect(1039544604, 8033)
    AddSpecialEffect(1039544605, 8033)
    AddSpecialEffect(1039544606, 8033)
    AddSpecialEffect(1039544600, 8035)
    AddSpecialEffect(1039544601, 8035)
    AddSpecialEffect(1039544602, 8035)
    AddSpecialEffect(1039544603, 8035)
    AddSpecialEffect(1039544604, 8035)
    AddSpecialEffect(1039544605, 8035)
    AddSpecialEffect(1039544606, 8035)
    CommonFunc_90005261(0, character=1039544252, region=1039546250, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.PutridCorpse28,
        region=1039546250,
        radius=1.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=1039544254, region=1039546250, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1039544550, region=1039546550, radius=1.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005261(0, character=1039544551, region=1039546550, radius=1.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005261(0, character=1039544552, region=1039546550, radius=1.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005261(0, character=1039544553, region=1039546550, radius=1.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005261(0, character=1039544695, region=1039546695, radius=1.0, seconds=0.0, animation_id=3008)
    CommonFunc_90005250(0, character=Characters.Basilisk0, region=1039542380, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk2,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542393,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Basilisk9,
        animation_id=30000,
        animation_id_1=20000,
        region=1039542393,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Slug10, region=1039542627, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Slug11, region=1039542627, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Slug12, region=1039542627, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Slug0, region=1039542607, seconds=3.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Slug8, region=1039542607, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Slug9, region=1039542607, seconds=8.0, animation_id=0)
    Event_1039542283(0, character=1039540283)
    Event_1039542520(0, asset_flag=1039542650, asset=1039541260)
    Event_1039542520(1, asset_flag=1039542651, asset=1039541261)
    Event_1039542520(2, asset_flag=1039545650, asset=1039546260)
    Event_1039542520(3, asset_flag=1039545651, asset=1039546261)
    Event_1039542580()
    CommonFunc_90005520(
        0,
        flag=1039540592,
        asset=Assets.AEG030_015_2000,
        start_climbing_flag=1039540593,
        stop_climbing_flag=1039540863,
    )
    CommonFunc_90005520(
        0,
        flag=1039540594,
        asset=Assets.AEG030_016_2000,
        start_climbing_flag=1039540595,
        stop_climbing_flag=1039540865,
    )
    Event_1039542498()
    Event_1039542499()
    Event_1039542283(0, character=1039540236)
    Event_1039542283(1, character=1039540238)
    Event_1039542283(2, character=1039540241)
    Event_1039542283(3, character=1039540242)
    Event_1039542283(4, character=1039540244)
    Event_1039542283(5, character=1039540245)
    Event_1039543700(0, character=Characters.Patches)
    Event_1039543702(0, character=Characters.Patches, flag=1039549206)
    CommonFunc_90005702(0, character=Characters.Patches, flag=3683, first_flag=3680, last_flag=3684)
    CommonFunc_90005706(0, character=Characters.WanderingNoble4, animation_id=930025, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Patches)
    DisableBackread(Characters.WanderingNoble4)


@RestartOnRest(1039542498)
def Event_1039542498():
    """Event 1039542498"""
    GotoIfFlagDisabled(Label.L0, flag=1039540592)
    RemoveNavmeshFaceFlag(navmesh_id=1039542498, navmesh_type=NavmeshFlag.Disable)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddNavmeshFaceFlag(navmesh_id=1039542498, navmesh_type=NavmeshFlag.Disable)
    
    MAIN.Await(FlagEnabled(1039540592))
    
    RemoveNavmeshFaceFlag(navmesh_id=1039542498, navmesh_type=NavmeshFlag.Disable)
    End()


@RestartOnRest(1039542811)
def Event_1039542811():
    """Event 1039542811"""
    if FlagEnabled(1039540800):
        return
    AND_1.Add(HealthRatio(Characters.BellBearingHunter) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(1039542802)


@RestartOnRest(1039542499)
def Event_1039542499():
    """Event 1039542499"""
    GotoIfFlagDisabled(Label.L0, flag=1039540594)
    RemoveNavmeshFaceFlag(navmesh_id=1039542499, navmesh_type=NavmeshFlag.Disable)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddNavmeshFaceFlag(navmesh_id=1039542499, navmesh_type=NavmeshFlag.Disable)
    
    MAIN.Await(FlagEnabled(1039540594))
    
    RemoveNavmeshFaceFlag(navmesh_id=1039542499, navmesh_type=NavmeshFlag.Disable)
    End()


@RestartOnRest(1039542290)
def Event_1039542290(_, character: Character | int):
    """Event 1039542290"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 90000)
    EnableThisNetworkSlotFlag()


@RestartOnRest(1039542283)
def Event_1039542283(_, character: Character | int):
    """Event 1039542283"""
    Kill(character)
    End()


@ContinueOnRest(1039542580)
def Event_1039542580():
    """Event 1039542580"""
    RegisterLadder(start_climbing_flag=1039540580, stop_climbing_flag=1039540851, asset=1039541580)
    RegisterLadder(start_climbing_flag=1039540582, stop_climbing_flag=1039540853, asset=Assets.AEG030_863_2001)
    RegisterLadder(start_climbing_flag=1039540584, stop_climbing_flag=1039540855, asset=Assets.AEG030_834_2002)
    RegisterLadder(start_climbing_flag=1039540586, stop_climbing_flag=1039540857, asset=Assets.AEG030_822_2005)
    RegisterLadder(start_climbing_flag=1039540588, stop_climbing_flag=1039540859, asset=1039541588)
    RegisterLadder(start_climbing_flag=1039540590, stop_climbing_flag=1039540861, asset=Assets.AEG030_017_2000)
    RegisterLadder(start_climbing_flag=1039540598, stop_climbing_flag=1039540869, asset=Assets.AEG007_275_2000)
    RegisterLadder(start_climbing_flag=1039540596, stop_climbing_flag=1039540863, asset=Assets.AEG030_860_2002)


@RestartOnRest(1039542200)
def Event_1039542200(_, character: uint, region: Region | int, seconds: float, animation_id: int):
    """Event 1039542200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AddSpecialEffect(character, 8081)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
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
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    Wait(5.0)
    RemoveSpecialEffect(character, 8081)
    RemoveSpecialEffect(character, 8082)


@RestartOnRest(1039542849)
def Event_1039542849():
    """Event 1039542849"""
    CommonFunc_9005800(
        0,
        flag=1039540800,
        entity=Assets.AEG099_002_9000,
        region=1039542800,
        flag_1=1039542805,
        character=1039545800,
        action_button_id=10000,
        left=0,
        region_1=1039542800,
    )
    CommonFunc_9005801(
        0,
        flag=1039540800,
        entity=Assets.AEG099_002_9000,
        region=1039542800,
        flag_1=1039542805,
        flag_2=1039542806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1039540800, asset=Assets.AEG099_002_9000, vfx_id=5, right=0)
    CommonFunc_9005822(
        0,
        flag=1039540800,
        bgm_boss_conv_param_id=921000,
        flag_1=1039542805,
        flag_2=1039542806,
        right=0,
        flag_3=1039542802,
        left=0,
        left_1=0,
    )


@RestartOnRest(1039542800)
def Event_1039542800():
    """Event 1039542800"""
    if FlagEnabled(1039540800):
        return
    
    MAIN.Await(HealthRatio(Characters.BellBearingHunter) <= 0.0)
    
    CreateVFX(1039540820)
    CreateVFX(1039540821)
    CreateVFX(1039540822)
    Wait(4.0)
    PlaySoundEffect(Characters.BellBearingHunter, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.BellBearingHunter))
    
    KillBossAndDisplayBanner(character=Characters.BellBearingHunter, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(1039540800)
    EnableFlag(9182)
    if PlayerInOwnWorld():
        EnableFlag(61182)


@RestartOnRest(1039542810)
def Event_1039542810():
    """Event 1039542810"""
    GotoIfFlagDisabled(Label.L0, flag=1039540800)
    DisableCharacter(Characters.BellBearingHunter)
    DisableAnimations(Characters.BellBearingHunter)
    Kill(Characters.BellBearingHunter)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.BellBearingHunter)
    AND_2.Add(FlagEnabled(1039542805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=1039542800))
    
    MAIN.Await(AND_2)
    
    SetNetworkUpdateRate(Characters.BellBearingHunter, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.BellBearingHunter, name=903100500)
    Wait(1.75)
    EnableAI(Characters.BellBearingHunter)


@RestartOnRest(1039542720)
def Event_1039542720(_, character: Character | int, region: Region | int, seconds: float):
    """Event 1039542720"""
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=region))
    GotoIfConditionTrue(Label.L1, input_condition=AND_5)
    AddSpecialEffect(character, 530)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(seconds)
    RemoveSpecialEffect(character, 530)
    End()


@ContinueOnRest(1039542510)
def Event_1039542510():
    """Event 1039542510"""
    CommonFunc_90005500(
        0,
        flag=1039540510,
        flag_1=1039540511,
        left=5,
        asset=Assets.AEG030_858_2001,
        asset_1=Assets.AEG099_026_2001,
        obj_act_id=1039543511,
        asset_2=Assets.AEG099_026_2000,
        obj_act_id_1=1039543512,
        region=1039542511,
        region_1=1039542512,
        flag_2=1039540512,
        flag_3=1039540513,
        left_1=0,
    )


@RestartOnRest(1039542520)
def Event_1039542520(_, asset_flag: Flag | int, asset: uint):
    """Event 1039542520"""
    WaitFrames(frames=1)
    if AssetDestroyed(asset):
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=asset, damage_type=DamageType.Fire))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=800140, anchor_entity=asset, dummy_id=200, anchor_type=CoordEntityType.Asset)
    CreateHazard(
        asset_flag=asset_flag,
        asset=asset,
        dummy_id=200,
        behavior_param_id=200100,
        target_type=DamageTargetType.Character,
        radius=3.5,
        life=0.800000011920929,
        repetition_time=0.0,
    )


@RestartOnRest(1039543700)
def Event_1039543700(_, character: uint):
    """Event 1039543700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3680):
        DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3690)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagEnabled(3690))
    
    MAIN.Await(OR_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90103)
    if FlagEnabled(1039549206):
        ForceAnimation(character, 90104)
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
    OR_4.Add(FlagEnabled(3690))
    
    MAIN.Await(not OR_4)
    
    Restart()


@RestartOnRest(1039543702)
def Event_1039543702(_, character: Character | int, flag: Flag | int):
    """Event 1039543702"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3690):
        return
    GotoIfFlagEnabled(Label.L1, flag=flag)
    
    MAIN.Await(FlagEnabled(flag))

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 9705)
    End()


@RestartOnRest(1039543709)
def Event_1039543709(_, character: Character | int):
    """Event 1039543709"""
    DisableCharacter(character)
    DisableBackread(character)
    End()
