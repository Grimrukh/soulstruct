"""
Belurat, Tower Settlement

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
    Event_20002150()
    CommonFunc_9005810(
        0,
        flag=20000800,
        grace_flag=20000000,
        character=20000950,
        asset=20001950,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005100(
        0,
        flag=72000,
        flag_1=72000,
        asset=20001980,
        source_flag=77800,
        value=0,
        flag_2=78800,
        flag_3=78801,
        flag_4=78802,
        flag_5=78803,
        flag_6=78804,
        flag_7=78805,
        flag_8=78806,
        flag_9=78807,
        flag_10=78808,
        flag_11=78809,
    )
    RegisterGrace(grace_flag=20000001, asset=20001951)
    RegisterGrace(grace_flag=20000002, asset=20001952)
    RegisterGrace(grace_flag=20000003, asset=20001953)
    Event_20002800()
    Event_20002811()
    Event_20002810()
    Event_20002845()
    Event_20002849()
    Event_20002820()
    Event_20002830()
    Event_20002831(0, special_effect=20011221, special_effect_1=501000)
    Event_20002831(1, special_effect=20011222, special_effect_1=501001)
    Event_20002831(2, special_effect=20011223, special_effect_1=501002)
    Event_20002831(3, special_effect=20011224, special_effect_1=501003)
    Event_20002831(4, special_effect=20011225, special_effect_1=501004)
    Event_20002831(5, special_effect=20011226, special_effect_1=501005)
    Event_20002831(6, special_effect=20011227, special_effect_1=501006)
    Event_20002831(7, special_effect=20011228, special_effect_1=501007)
    Event_20002831(8, special_effect=20011229, special_effect_1=501008)
    Event_20002831(9, special_effect=20011230, special_effect_1=501009)
    Event_20002831(10, special_effect=20011231, special_effect_1=501010)
    Event_20002831(11, special_effect=20011232, special_effect_1=501011)
    Event_20002831(12, special_effect=20011233, special_effect_1=501012)
    CommonFunc_90005501(
        0,
        flag=20000510,
        flag_1=20000511,
        left=0,
        asset=20001510,
        asset_1=20001511,
        asset_2=20001512,
        flag_2=20000512,
    )
    CommonFunc_90005501(
        0,
        flag=20000515,
        flag_1=20000516,
        left=0,
        asset=20001515,
        asset_1=20001516,
        asset_2=20001517,
        flag_2=20000517,
    )
    CommonFunc_90005501(
        0,
        flag=20000520,
        flag_1=20000521,
        left=0,
        asset=20001520,
        asset_1=20001521,
        asset_2=20001522,
        flag_2=20000522,
    )
    CommonFunc_90005501(
        0,
        flag=20000525,
        flag_1=20000526,
        left=0,
        asset=20001525,
        asset_1=20001526,
        asset_2=20001527,
        flag_2=20000527,
    )
    Event_20002510()
    CommonFunc_90005510(
        0,
        flag=20008562,
        asset=20001562,
        obj_act_id=20003562,
        obj_act_id_1=417007,
        text=20208004,
        left=0,
    )
    CommonFunc_90005510(
        0,
        flag=20008564,
        asset=20001564,
        obj_act_id=20003564,
        obj_act_id_1=1417014,
        text=20208013,
        left=0,
    )
    CommonFunc_90005511(0, flag=20008566, asset=20001566, obj_act_id=20003566, obj_act_id_1=417014, left=0)
    CommonFunc_90005511(0, flag=20008560, asset=20001560, obj_act_id=20003560, obj_act_id_1=2417014, left=0)
    CommonFunc_90005512(0, flag=20008560, region=20002560, region_1=20002561)
    RunCommonEvent(
        20002610,
        slot=0,
        args=(20008540, 20001540, 20001541, 20003541, 417009, 10, 2, 20001540, 417011),
        arg_types="IIIIiiiIi",
    )
    Event_20002580()
    Event_20002500()
    Event_20002502()
    CommonFunc_900005580(0, flag=580600, asset=20001600, flag_1=9146)
    CommonFunc_90005301(0, flag=20000410, character=20000410, item_lot__unk1=20001991, seconds=0.0, unk1=0)
    CommonFunc_90005301(0, flag=20000403, character=20000403, item_lot__unk1=20001993, seconds=0.0, unk1=0)
    CommonFunc_90005780(
        0,
        flag=20000800,
        summon_flag=20002160,
        dismissal_flag=20002161,
        character=20000740,
        sign_type=20,
        region=20002741,
        right=2046429390,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=20000800, flag_1=20002160, flag_2=20002161, character=20000740)
    CommonFunc_90005784(
        0,
        flag=20002160,
        flag_1=20002805,
        character=20000740,
        region=20002800,
        region_1=20002809,
        animation=0,
    )
    CommonFunc_90005754(
        0,
        flag=4870,
        first_flag=4870,
        last_flag=4874,
        flag_1=4875,
        region=20002701,
        flag_2=20000180,
        flag_3=4343,
        right=4860,
        character=20000700,
        right_1=20002181,
        distance=100.0,
        flag_4=20002182,
        right_2=0,
        flag_5=0,
        right_3=0,
    )
    CommonFunc_90005755(0, flag=4870, flag_1=4875, right=0, flag_2=4860, flag_3=4861, max_value__value=2)
    CommonFunc_90005790(
        0,
        right=0,
        flag=20000180,
        summon_flag=20002181,
        dismissal_flag=20002182,
        character=20000700,
        sign_type=23,
        region=20002700,
        region_1=20002701,
        seconds=0.0,
        right_1=4870,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=20000180, flag_1=20002181, flag_2=20002182, character=20000700)
    CommonFunc_90005792(0, flag=20000180, flag_1=20002181, flag_2=20002182, character=20000700, item_lot=0, seconds=0.0)
    Event_20002199(
        0,
        flag=20000180,
        flag_1=20002181,
        flag_2=20002182,
        character=20000700,
        other_entity=20002700,
        region=20002182,
        left=0,
    )
    CommonFunc_90005768(0, flag=20000180, item_lot=106920, flag_1=400694, item_lot_1=106930, flag_2=400696, flag_3=4860)
    CommonFunc_90005748(0, entity=20001720, action_button_id=206020, text=1030020, display_distance=30.0, flag=4910)
    Event_20000702(
        0,
        flag=20009263,
        flag_1=20009291,
        flag_2=20009265,
        flag_3=20009292,
        flag_4=20009294,
        flag_5=20009289,
        flag_6=20009293,
        flag_7=20009280,
        flag_8=20009281,
        flag_9=20009286,
        flag_10=21010800,
        flag_11=4480,
        flag_12=20009290,
        flag_13=20009271,
        flag_14=20009295,
        flag_15=20009285,
        flag_16=20000801,
        flag_17=20002739,
        flag_18=20009284,
        flag_19=20009299,
    )
    Event_20000700(
        0,
        character=20000710,
        flag=4485,
        flag_1=4480,
        flag_2=4483,
        distance=34.0,
        flag_3=20009289,
        character_1=20000711,
    )
    Event_20000701(0, flag=20009286, flag_1=20002725, seconds=5.0)
    Event_20000703(
        0,
        character=20000710,
        flag=20009286,
        flag_1=4483,
        flag_2=20002724,
        flag_3=20009282,
        flag_4=20009289,
        flag_5=20009296,
        first_flag=4480,
        last_flag=4484,
        flag_6=20002740,
        seconds=10.0,
        flag_7=20009288,
        flag_8=20002747,
        special_effect=9615,
    )
    Event_20000704(0, region=20002710, flag=20002723, flag_1=4480, flag_2=20009289)
    Event_20000705(
        0,
        character=20000710,
        flag=20009286,
        flag_1=4480,
        flag_2=20002712,
        flag_3=20002713,
        flag_4=20002711,
        radius=10.0,
        animation_id=20002,
        flag_5=20009271,
        flag_6=21010800,
        flag_7=20009263,
        flag_8=20002747,
    )
    Event_20000706(
        0,
        character=20000710,
        flag=20000800,
        flag_1=20002747,
        first_flag=4480,
        flag_2=20009288,
        flag_3=20002742,
        flag_4=20002740,
        flag_5=4483,
        last_flag=4484,
        seconds=1.0,
        seconds_1=10.0,
        flag_6=20009286,
    )
    Event_20000707(
        0,
        character=20000710,
        flag=20009287,
        flag_1=20009295,
        flag_2=20009271,
        flag_3=20009281,
        flag_4=20009289,
        animation_id=930000,
        animation_id_1=930005,
        animation_id_2=930010,
        animation_id_3=930015,
        flag_5=4480,
        flag_6=20000800,
        flag_7=21010800,
        flag_8=20009286,
    )
    Event_20000708(
        0,
        attacked_entity=20000710,
        flag=20009290,
        flag_1=20002743,
        animation_id=20002,
        flag_2=20002736,
        flag_3=20009271,
        flag_4=20002718,
        flag_5=20009263,
    )
    Event_20000709(
        0,
        attacked_entity=20000710,
        flag=20009289,
        flag_1=20002740,
        special_effect=20012900,
        special_effect_1=20012901,
        character=20000711,
    )
    Event_20000710(
        0,
        attacked_entity=20000710,
        flag=20009289,
        flag_1=20002740,
        seconds=5.0,
        flag_2=4485,
        special_effect=20012900,
        character=20000711,
    )
    Event_20000711(
        0,
        entity=20000710,
        flag=4480,
        flag_1=20009289,
        flag_2=20002719,
        flag_3=20002743,
        animation_id=20000,
        seconds=5.5,
    )
    Event_20000712(0, entity=20000710, flag=4480, flag_1=20009289, flag_2=20002718, seconds=28.0, radius=12.0)
    Event_20000713(
        0,
        entity=20000710,
        flag=20002736,
        flag_1=20002718,
        flag_2=4480,
        flag_3=21010800,
        radius=5.0,
        radius_1=12.0,
    )
    Event_20000714(0, character=20000710, flag=4480, flag_1=20009289, flag_2=20009288, special_effect=9615)
    Event_20000731(0, character=20000710, flag=20002748)
    Event_20000732(
        0,
        asset=20001710,
        action_button_id=4350,
        item_lot=107210,
        first_flag=400720,
        last_flag=400721,
        flag=20009288,
        vfx_id=6101,
        vfx_id_1=6100,
        flag_1=400721,
    )
    CommonFunc_90005750(
        0,
        asset=20001710,
        action_button_id=4350,
        item_lot=107230,
        first_flag=400723,
        last_flag=400723,
        flag=20009293,
        vfx_id=0,
    )
    CommonFunc_90005702(0, character=20000710, flag=4483, first_flag=4480, last_flag=4484)
    CommonFunc_90005744(0, entity=20000710, flag=20002730, flag_1=20009298, animation_id=20001)
    CommonFunc_90005744(1, entity=20000710, flag=20002731, flag_1=20009298, animation_id=20002)
    CommonFunc_90005744(2, entity=20000710, flag=20002732, flag_1=20009298, animation_id=20003)
    CommonFunc_90005744(3, entity=20000710, flag=20002733, flag_1=20009298, animation_id=20010)
    CommonFunc_90005744(4, entity=20000710, flag=20002734, flag_1=20009298, animation_id=20011)
    CommonFunc_90005744(5, entity=20000710, flag=20002735, flag_1=20009298, animation_id=20015)
    CommonFunc_90005744(6, entity=20000710, flag=20002737, flag_1=20009298, animation_id=20004)
    CommonFunc_90005744(7, entity=20000710, flag=20002722, flag_1=20009298, animation_id=20022)
    Event_20000730(0, character=20000710, flag=4480, flag_1=21010800, flag_2=20009285)
    CommonFunc_90005747(
        0,
        flag=20009278,
        flag_1=4485,
        flag_2=20002715,
        seconds=5.0,
        flag_3=20002714,
        flag_4=20002728,
        seconds_1=5.0,
    )
    CommonFunc_90005747(
        1,
        flag=20009290,
        flag_1=4485,
        flag_2=20002727,
        seconds=5.0,
        flag_3=20002726,
        flag_4=20002738,
        seconds_1=10.0,
    )
    CommonFunc_90005747(
        2,
        flag=20009289,
        flag_1=4485,
        flag_2=20002746,
        seconds=45.0,
        flag_3=20002745,
        flag_4=20002728,
        seconds_1=45.0,
    )
    CommonFunc_90005747(
        3,
        flag=20009289,
        flag_1=4485,
        flag_2=20002717,
        seconds=60.0,
        flag_3=20002716,
        flag_4=20002728,
        seconds_1=60.0,
    )
    Event_20000725(0, flag=4927, flag_1=2046429390)
    Event_20000726(
        0,
        flag=20002160,
        flag_1=20002161,
        flag_2=20002810,
        flag_3=2046422723,
        flag_4=2046429370,
        flag_5=20000800,
    )
    Event_20000720(
        0,
        region=20002701,
        flag=20002701,
        flag_1=20000180,
        flag_2=20002182,
        flag_3=4860,
        seconds=6.0,
        flag_4=20002181,
        first_flag=4870,
        last_flag=4874,
        flag_5=4870,
        flag_6=20002703,
    )
    CommonFunc_90005737(0, flag=20000180, flag_1=20002703)
    CommonFunc_90005706(0, character=20000730, animation_id=30019, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_20000519()
    CommonFunc_90005221(0, character=20000267, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000268, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005201(
        0,
        character=20000200,
        animation_id=30005,
        animation_id_1=20005,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=20000201,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=20000203,
        animation_id=30005,
        animation_id_1=20005,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000206,
        animation_id=30008,
        animation_id_1=20008,
        region=20002207,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000207,
        animation_id=30008,
        animation_id_1=20008,
        region=20002207,
        radius=0.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000208,
        animation_id=30005,
        animation_id_1=20005,
        region=20002208,
        radius=0.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000209,
        animation_id=30005,
        animation_id_1=20005,
        region=20002208,
        radius=0.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000211,
        animation_id=30005,
        animation_id_1=20005,
        region=20002208,
        radius=0.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000213,
        animation_id=30005,
        animation_id_1=20005,
        region=20002208,
        radius=0.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=20000217, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000219, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000220, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=20000223, region=20002223, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000224, region=20002224, radius=1.0, seconds=2.0, animation_id=0)
    CommonFunc_90005221(1, character=20000231, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(2, character=20000232, animation_id=30013, animation_id_1=20013, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=20000233,
        animation_id=30002,
        animation_id_1=20002,
        region=20002233,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000234,
        animation_id=30002,
        animation_id_1=20002,
        region=20002233,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000235,
        animation_id=30002,
        animation_id_1=20002,
        region=20002233,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000238,
        animation_id=30000,
        animation_id_1=20000,
        region=20002233,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000236,
        animation_id=30002,
        animation_id_1=20002,
        region=20002236,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000239,
        animation_id=30002,
        animation_id_1=20002,
        region=20002236,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000240, region=20002240, radius=2.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005201(
        0,
        character=20000241,
        animation_id=30001,
        animation_id_1=20001,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000242, region=20002301, radius=1.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(0, character=20000244, region=20002244, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000245, region=20002245, radius=1.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005261(0, character=20000243, region=20002243, radius=2.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005211(
        0,
        character=20000250,
        animation_id=30000,
        animation_id_1=20000,
        region=20002250,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000251, region=20002251, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=20000253, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000254, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000255, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000256, animation_id=30005, animation_id_1=20005, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000257, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000258, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000259, animation_id=30002, animation_id_1=20002, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000260, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000261, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20000264, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005201(
        0,
        character=20000273,
        animation_id=30002,
        animation_id_1=20002,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=20000274,
        animation_id=30000,
        animation_id_1=20000,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000281, region=20002281, radius=1.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=20000283, region=20002283, radius=1.0, seconds=0.0, animation_id=3033)
    CommonFunc_90005211(
        0,
        character=20000284,
        animation_id=30009,
        animation_id_1=20009,
        region=20002284,
        radius=1.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000285, region=20002285, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000293, region=20002293, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000288,
        animation_id=30009,
        animation_id_1=20009,
        region=20002288,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000290, region=20002290, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000300,
        animation_id=30009,
        animation_id_1=20009,
        region=20002300,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000301,
        animation_id=30009,
        animation_id_1=20009,
        region=20002301,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000292,
        animation_id=30000,
        animation_id_1=20000,
        region=20002292,
        radius=2.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=20000294, radius=30.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000302, region=20002302, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000303,
        animation_id=30009,
        animation_id_1=20009,
        region=20002303,
        radius=1.0,
        seconds=5.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000304,
        animation_id=30000,
        animation_id_1=20000,
        region=20002303,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000305, region=20002305, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20005270, region=20002270, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000321, region=20002321, radius=2.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005211(
        0,
        character=20000322,
        animation_id=30000,
        animation_id_1=20000,
        region=20002322,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000323, region=20002323, radius=2.0, seconds=0.0, animation_id=3003)
    CommonFunc_90005261(0, character=20000324, region=20002324, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000325,
        animation_id=30000,
        animation_id_1=20000,
        region=20002325,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000328,
        animation_id=30001,
        animation_id_1=20001,
        region=20002328,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000326,
        animation_id=30000,
        animation_id_1=20000,
        region=20002326,
        radius=1.0,
        seconds=0.20000000298023224,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000330,
        animation_id=30000,
        animation_id_1=20000,
        region=20002330,
        radius=1.0,
        seconds=2.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000332,
        animation_id=30000,
        animation_id_1=20000,
        region=20002330,
        radius=1.0,
        seconds=2.5999999046325684,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000334,
        animation_id=30000,
        animation_id_1=20000,
        region=20002330,
        radius=1.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000331,
        animation_id=30000,
        animation_id_1=20000,
        region=20002331,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000333,
        animation_id=30000,
        animation_id_1=20000,
        region=20002331,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000335, region=20002335, radius=1.0, seconds=1.5, animation_id=0)
    CommonFunc_90005261(0, character=20000336, region=20002335, radius=1.0, seconds=1.5, animation_id=0)
    CommonFunc_90005261(0, character=20000338, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000340, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000341, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000342, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000343, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000344, region=20002335, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000345, region=20002335, radius=1.0, seconds=1.5, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000346,
        animation_id=30001,
        animation_id_1=20001,
        region=20002460,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000347,
        animation_id=30000,
        animation_id_1=20000,
        region=20002460,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000348,
        animation_id=30001,
        animation_id_1=20001,
        region=20002460,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000349,
        animation_id=30000,
        animation_id_1=20000,
        region=20002460,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000460,
        animation_id=30000,
        animation_id_1=20000,
        region=20002460,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000461, region=20002460, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000462, region=20002460, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000463, region=20002460, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000465, region=20002465, radius=1.0, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005261(0, character=20000466, region=20002465, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000467, region=20002465, radius=1.0, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005261(0, character=20000468, region=20002465, radius=1.0, seconds=0.20000000298023224, animation_id=0)
    CommonFunc_90005261(0, character=20000469, region=20002465, radius=1.0, seconds=0.30000001192092896, animation_id=0)
    CommonFunc_90005211(
        0,
        character=20000353,
        animation_id=30002,
        animation_id_1=20002,
        region=20002353,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000354,
        animation_id=30002,
        animation_id_1=20002,
        region=20002353,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000351,
        animation_id=30005,
        animation_id_1=20005,
        region=20002351,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000352,
        animation_id=30005,
        animation_id_1=20005,
        region=20002351,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=20000355,
        animation_id=30001,
        animation_id_1=20001,
        radius=2.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000359, region=20002359, radius=1.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005211(
        0,
        character=20000360,
        animation_id=30002,
        animation_id_1=20002,
        region=20002360,
        radius=1.0,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000361,
        animation_id=30002,
        animation_id_1=20002,
        region=20002360,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=20000362,
        animation_id=30005,
        animation_id_1=20005,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000363, region=20002363, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=20000379, region=20002379, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000389, region=20002379, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000391, region=20002379, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000392, region=20002379, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000393, region=20002379, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=20000365,
        animation_id=30003,
        animation_id_1=20003,
        region=20002365,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000366,
        animation_id=30003,
        animation_id_1=20003,
        region=20002365,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000371,
        animation_id=30003,
        animation_id_1=20003,
        region=20002365,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000372,
        animation_id=30003,
        animation_id_1=20003,
        region=20002365,
        radius=1.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000367,
        animation_id=30002,
        animation_id_1=20002,
        region=20002367,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000373,
        animation_id=30002,
        animation_id_1=20002,
        region=20002367,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000376, region=20002368, radius=1.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=20000378, region=20002384, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000384, region=20002384, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000385, region=20002384, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000398, region=20002384, radius=1.0, seconds=0.5, animation_id=0)
    CommonFunc_90005261(0, character=20000399, region=20002384, radius=1.0, seconds=0.5, animation_id=0)
    CommonFunc_90005261(0, character=20000386, region=20002386, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000394, region=20002386, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=20000400, region=20002400, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000401, region=20002401, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20000402, region=20002402, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=20000410,
        animation_id=30002,
        animation_id_1=20002,
        region=20002410,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000420, region=20002420, radius=1.5, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=20000430,
        animation_id=30001,
        animation_id_1=20001,
        region=20002430,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000431,
        animation_id=30000,
        animation_id_1=20000,
        region=20002431,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20000432,
        animation_id=30000,
        animation_id_1=20000,
        region=20002432,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20000433, region=20002433, radius=1.5, seconds=0.0, animation_id=-1)
    Event_20002550()


@RestartOnRest(20002150)
def Event_20002150():
    """Event 20002150"""
    GotoIfFlagEnabled(Label.L0, flag=330)
    DisableAsset(20006650)
    DisableCharacter(20005650)
    DisableAnimations(20005650)
    DisableMapCollision(collision=20004650)
    DisableMapCollision(collision=20004651)
    DisableMapCollision(collision=20004652)
    DisableMapCollision(collision=20004653)
    DisableMapCollision(collision=20004655)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(20006660)
    DisableMapCollision(collision=20004660)


@RestartOnRest(20002199)
def Event_20002199(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: Character | int,
    other_entity: uint,
    region: Region | int,
    left: int,
):
    """Event 20002199"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    if UnsignedEqual(left=region, right=0):
        AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=110.0))
    else:
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfValueEqual(5, left=left, right=2)
    SkipLinesIfValueEqual(2, left=left, right=1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=180.0))
    SkipLines(3)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=360.0))
    SkipLines(1)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=720.0))
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=20002199))
    OR_10.Add(AND_1)
    OR_10.Add(AND_2)
    OR_10.Add(AND_3)
    OR_10.Add(AND_4)
    
    MAIN.Await(OR_10)
    
    if FlagEnabled(flag):
        return
    SendNPCSummonHome(character=character)
    End()
    OR_11.Add(FlagDisabled(flag_2))


@ContinueOnRest(20002500)
def Event_20002500():
    """Event 20002500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(330):
        return
    AND_1.Add(FlagDisabled(330))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209502, entity=20001500))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=2020002, anchor_entity=20001500, button_type=ButtonType.Yes_or_No)
    Wait(3.0)
    Restart()


@ContinueOnRest(20002502)
def Event_20002502():
    """Event 20002502"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(20010500):
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=20012500))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=20002500))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(330))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(9000))
    OR_2.Add(AND_2)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=20012500))
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=20002500))
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    AND_4.Add(CharacterOutsideRegion(character=PLAYER, region=20012500))
    AND_4.Add(CharacterOutsideRegion(character=PLAYER, region=20002500))
    if AND_4:
        return RESTART
    EnableFlag(20010500)


@ContinueOnRest(20002510)
def Event_20002510():
    """Event 20002510"""
    CommonFunc_90005500(
        0,
        flag=20000510,
        flag_1=20000511,
        left=0,
        asset=20001510,
        asset_1=20001511,
        obj_act_id=20003511,
        asset_2=20001512,
        obj_act_id_1=20003512,
        region=20002511,
        region_1=20002512,
        flag_2=20000512,
        flag_3=20000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20000515,
        flag_1=20000516,
        left=0,
        asset=20001515,
        asset_1=20001516,
        obj_act_id=20003516,
        asset_2=20001517,
        obj_act_id_1=20003517,
        region=20002516,
        region_1=20002517,
        flag_2=20000517,
        flag_3=20000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20000520,
        flag_1=20000521,
        left=0,
        asset=20001520,
        asset_1=20001521,
        obj_act_id=20003521,
        asset_2=20001522,
        obj_act_id_1=20003522,
        region=20002521,
        region_1=20002522,
        flag_2=20000522,
        flag_3=20000523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20000525,
        flag_1=20000526,
        left=0,
        asset=20001525,
        asset_1=20001526,
        obj_act_id=20003526,
        asset_2=20001527,
        obj_act_id_1=20003527,
        region=20002526,
        region_1=20002527,
        flag_2=20000527,
        flag_3=20000528,
        left_1=0,
    )


@ContinueOnRest(20000519)
def Event_20000519():
    """Event 20000519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(20000510)
    DisableFlag(20000515)
    EnableFlag(20000520)
    EnableFlag(20000525)


@RestartOnRest(20002550)
def Event_20002550():
    """Event 20002550"""
    EnableAssetInvulnerability(20001550)


@ContinueOnRest(20002580)
def Event_20002580():
    """Event 20002580"""
    RegisterLadder(start_climbing_flag=20000580, stop_climbing_flag=20000581, asset=20001580)
    RegisterLadder(start_climbing_flag=20000582, stop_climbing_flag=20000583, asset=20001582)
    RegisterLadder(start_climbing_flag=20000584, stop_climbing_flag=20000585, asset=20001584)
    RegisterLadder(start_climbing_flag=20000586, stop_climbing_flag=20000587, asset=20001586)


@RestartOnRest(20002610)
def Event_20002610(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
    asset_2: Asset | int,
    obj_act_id_2: int,
):
    """Event 20002610"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset_2, obj_act_id=obj_act_id_2)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    Wait(1.0)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset_2, obj_act_id=obj_act_id_2)
    ForceAnimation(asset, animation_id)


@RestartOnRest(20002800)
def Event_20002800():
    """Event 20002800"""
    if FlagEnabled(20000800):
        return
    
    MAIN.Await(HealthValue(20000800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(20008000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(20000800))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(20000800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=20000800, banner_type=BannerType.LegendFelled)
    MoveAssetToCharacter(20001811, character=20000800)
    EnableTreasure(asset=20001811)
    EnableNetworkFlag(20000800)
    EnableFlag(9140)
    if PlayerInOwnWorld():
        EnableFlag(61140)


@RestartOnRest(20002810)
def Event_20002810():
    """Event 20002810"""
    GotoIfFlagDisabled(Label.L0, flag=20000800)
    DisableCharacter(20000800)
    DisableAnimations(20000800)
    Kill(20000800)
    DisableAsset(20001810)
    EnableTreasure(asset=20001811)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(20000800)
    DisableTreasure(asset=20001811)
    DisableAnimations(20000800)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=20000801)
    DisableCharacter(20000800)
    SetCharacterFadeOnEnable(character=20000800, state=False)
    OR_1.Add(FlagEnabled(20002805))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=20002801))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    SkipLinesIfPlayerNotInOwnWorld(5)
    SkipLinesIfFlagEnabled(2, 20002739)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=20000000,
        cutscene_flags=0,
        move_to_region=20002811,
        map_id=20000000,
        player_id=10000,
        unk_20_24=20000000,
        unk_24_25=False,
    )
    SkipLines(1)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=20000001,
        cutscene_flags=0,
        move_to_region=20002811,
        map_id=20000000,
        player_id=10000,
        unk_20_24=20000000,
        unk_24_25=False,
    )
    SkipLines(4)
    if FlagDisabled(20002739):
        PlayCutscene(20000000, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(20000001, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    DisableAsset(20001810)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=4.019999980926514, y_angle=-161.8300018310547)
    EnableCharacter(20000800)
    ForceAnimation(20000800, 20010)
    EnableNetworkFlag(20000801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(20001810)
    AND_2.Add(FlagEnabled(20002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=20002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAnimations(20000800)
    EnableAI(20000800)
    SetNetworkUpdateRate(20000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(20000800, name=905210000)


@RestartOnRest(20002811)
def Event_20002811():
    """Event 20002811"""
    if FlagEnabled(20000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(20000800, 20011239))
    
    MAIN.Await(AND_1)
    
    EnableFlag(20002802)


@RestartOnRest(20002820)
def Event_20002820():
    """Event 20002820"""
    GotoIfFlagDisabled(Label.L0, flag=20000800)
    SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    RemoveSpecialEffect(PLAYER, 20004220)
    RemoveSpecialEffect(PLAYER, 20004221)
    RemoveSpecialEffect(PLAYER, 20004222)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L3, flag=20002820)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011210):
        SetWeather(weather=Weather.ScatteredRain, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004220)
        Goto(Label.L2)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011211):
        SetWeather(weather=Weather.HeavySnow, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004221)
        Goto(Label.L2)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011212):
        SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004222)
        Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(CharacterHasSpecialEffect(20000800, 20011210))
    OR_1.Add(CharacterHasSpecialEffect(20000800, 20011211))
    OR_1.Add(CharacterHasSpecialEffect(20000800, 20011212))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(20000800, 20011236))
    OR_2.Add(AND_1)
    OR_2.Add(FlagEnabled(20000800))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(PLAYER, 20004220)
    RemoveSpecialEffect(PLAYER, 20004221)
    RemoveSpecialEffect(PLAYER, 20004222)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011210):
        SetWeather(weather=Weather.ScatteredRain, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004220)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011211):
        SetWeather(weather=Weather.HeavySnow, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004221)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20000800, special_effect=20011212):
        SetWeather(weather=Weather.PuffyClouds, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004222)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@RestartOnRest(20002830)
def Event_20002830():
    """Event 20002830"""
    if FlagEnabled(20000800):
        return
    AND_10.Add(PlayerNotInOwnWorld())
    if AND_10:
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 20011220))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501000))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501001))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501002))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501003))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501004))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501005))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501006))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501007))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501008))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501009))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501010))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501011))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501012))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 20011246)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501000):
        AddSpecialEffect(20000800, 20011221)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501001):
        AddSpecialEffect(20000800, 20011222)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501002):
        AddSpecialEffect(20000800, 20011223)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501003):
        AddSpecialEffect(20000800, 20011224)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501004):
        AddSpecialEffect(20000800, 20011225)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501005):
        AddSpecialEffect(20000800, 20011226)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501006):
        AddSpecialEffect(20000800, 20011227)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501007):
        AddSpecialEffect(20000800, 20011228)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501008):
        AddSpecialEffect(20000800, 20011229)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501009):
        AddSpecialEffect(20000800, 20011230)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501010):
        AddSpecialEffect(20000800, 20011231)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501011):
        AddSpecialEffect(20000800, 20011232)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501012):
        AddSpecialEffect(20000800, 20011233)
        Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest(20002831)
def Event_20002831(_, special_effect: int, special_effect_1: int):
    """Event 20002831"""
    if FlagEnabled(20000800):
        return
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 20011220))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect_1))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 20011246)
    if PlayerInOwnWorld():
        AddSpecialEffect(20000800, special_effect)
    Wait(1.0)
    Restart()


@RestartOnRest(20002845)
def Event_20002845():
    """Event 20002845"""
    GotoIfFlagDisabled(Label.L0, flag=20000801)
    DisableAsset(20001810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(20000801))
    
    DisableAsset(20001810)
    End()


@RestartOnRest(20002849)
def Event_20002849():
    """Event 20002849"""
    CommonFunc_9005800(
        0,
        flag=20000800,
        entity=20001800,
        region=20002800,
        flag_1=20002805,
        character=20005800,
        action_button_id=10000,
        left=20000801,
        region_1=20002801,
    )
    CommonFunc_9005801(
        0,
        flag=20000800,
        entity=20001800,
        region=20002800,
        flag_1=20002805,
        flag_2=20002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=20000800, asset=20001800, vfx_id=4, right=20000801)
    CommonFunc_9005811(0, flag=20000800, asset=20001801, vfx_id=4, right=20000801)
    CommonFunc_9005822(
        0,
        flag=20000800,
        bgm_boss_conv_param_id=521000,
        flag_1=20002805,
        flag_2=20002806,
        right=0,
        flag_3=20002802,
        left=0,
        left_1=0,
    )


@RestartOnRest(20000700)
def Event_20000700(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    flag_3: Flag | int,
    character_1: Character | int,
):
    """Event 20000700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    SetBackreadStateAlternate(character, False)
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L4, flag=flag_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    Move(character, destination=20002711, destination_type=CoordEntityType.Region, short_move=True)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    EnableImmortality(character)
    SetCharacterTalkRange(character=character, distance=distance)
    if FlagEnabled(flag_3):
        SetTeamType(character, TeamType.NoTeam)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_3.Add(FlagEnabled(flag))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(20000701)
def Event_20000701(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 20000701"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag_1):
        return RESTART
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(20000702)
def Event_20000702(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
    flag_14: Flag | int,
    flag_15: Flag | int,
    flag_16: Flag | int,
    flag_17: Flag | int,
    flag_18: Flag | int,
    flag_19: Flag | int,
):
    """Event 20000702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_5):
        return
    if FlagDisabled(flag_11):
        return
    if FlagEnabled(flag):
        EnableFlag(flag_1)
    if FlagEnabled(flag_2):
        EnableFlag(flag_3)
    if FlagEnabled(flag_4):
        EnableFlag(flag_5)
        EnableFlag(flag_6)
    if FlagEnabled(flag_7):
        EnableFlag(flag_8)
    AND_1.Add(FlagDisabled(flag_9))
    AND_1.Add(FlagEnabled(flag_10))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag_5)
    if FlagEnabled(flag):
        EnableFlag(flag_13)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_10))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag_12)
    DisableFlag(flag_13)
    if FlagEnabled(flag_14):
        EnableFlag(flag_15)
    AND_3.Add(FlagDisabled(flag_16))
    AND_3.Add(FlagEnabled(flag_14))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_17)
    if FlagEnabled(flag_18):
        EnableFlag(flag_19)
        DisableFlag(flag_18)
    End()


@RestartOnRest(20000703)
def Event_20000703(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_6: Flag | int,
    seconds: float,
    flag_7: Flag | int,
    flag_8: Flag | int,
    special_effect: int,
):
    """Event 20000703"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_5)
    if FlagEnabled(flag_4):
        return
    if FlagEnabled(flag_1):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_8))
    AND_1.Add(OR_1)
    AND_1.Add(HealthValue(character) == 1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_2)
    EnableFlag(flag_5)
    AwaitFlagEnabled(flag=flag_3)
    DisableImmortality(character)
    Kill(character, award_runes=True)
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)
    DisableFlag(flag_5)
    EnableFlag(flag_6)
    EnableFlag(flag_7)
    Wait(seconds)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(20000704)
def Event_20000704(_, region: Region | int, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20000704"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    
    EnableFlag(flag)
    
    MAIN.Await(CharacterOutsideRegion(character=ALL_PLAYERS, region=region))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(20000705)
def Event_20000705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    radius: float,
    animation_id: int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 20000705"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_8))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    OR_2.Add(FlagEnabled(flag_3))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_3)
    AwaitFlagEnabled(flag=flag_4)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    AND_2.Add(TimeElapsed(seconds=5.0))
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_2)
    EnableFlag(flag_2)
    DisableFlag(flag_3)
    AND_3.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=character, radius=radius))
    AND_3.Add(FlagDisabled(flag_6))
    AND_3.Add(FlagEnabled(flag_7))
    AND_3.Add(HealthValue(character) != 0)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(flag_5)
    ForceAnimation(character, animation_id)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(20000706)
def Event_20000706(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    first_flag: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    last_flag: Flag | int,
    seconds: float,
    seconds_1: float,
    flag_6: Flag | int,
):
    """Event 20000706"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(first_flag):
        return
    if FlagEnabled(flag_6):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagDisabled(Label.L1, flag=flag_3)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(character, 9638)
    EnableImmortality(character)
    DisableFlag(flag_3)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 9638)
    DisableImmortality(character)
    EnableFlag(flag_3)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(seconds)
    DisableAnimations(character)
    EnableFlag(flag_2)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_5)
    Wait(seconds_1)
    DisableCharacter(character)
    DisableBackread(character)
    End()
    EnableFlag(flag_4)


@RestartOnRest(20000707)
def Event_20000707(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    animation_id_3: int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 20000707"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_5):
        return
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L0, flag=flag_6)
    GotoIfFlagEnabled(Label.L1, flag=flag_6)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_4):
        ForceAnimation(character, animation_id_1)
        EnableHealthBar(character)
        End()
    if FlagEnabled(flag_1):
        ForceAnimation(character, animation_id_3)
        DisableHealthBar(character)
        Goto(Label.L4)
    if FlagDisabled(flag):
        ForceAnimation(character, animation_id_1)
        EnableHealthBar(character)
        Goto(Label.L4)
    ForceAnimation(character, animation_id)
    EnableHealthBar(character)
    Goto(Label.L4)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=flag_7)
    GotoIfFlagEnabled(Label.L3, flag=flag_7)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(flag_8):
        ForceAnimation(character, animation_id_1)
        EnableHealthBar(character)
        End()
    if FlagDisabled(flag_2):
        ForceAnimation(character, animation_id)
        EnableHealthBar(character)
        End()
    ForceAnimation(character, animation_id_2)
    EnableHealthBar(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag_4))
    OR_1.Add(FlagDisabled(flag_8))
    SkipLinesIfConditionFalse(3, OR_1)
    ForceAnimation(character, animation_id_1)
    EnableHealthBar(character)
    End()
    ForceAnimation(character, animation_id)
    EnableHealthBar(character)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    
    MAIN.Await(FlagEnabled(flag_6))
    
    ForceAnimation(character, animation_id_1)
    EnableHealthBar(character)
    End()


@RestartOnRest(20000708)
def Event_20000708(
    _,
    attacked_entity: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 20000708"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    OR_15.Add(FlagEnabled(flag_2))
    OR_15.Add(FlagEnabled(flag_4))
    AND_15.Add(FlagEnabled(flag_5))
    AND_15.Add(OR_15)
    
    MAIN.Await(AND_15)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag_3)
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_4))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultFalse(3, input_condition=AND_2)
    DisableFlag(flag_2)
    DisableFlag(flag_4)
    Restart()
    ForceAnimation(attacked_entity, animation_id)
    DisableFlag(flag_2)
    EnableFlag(flag_3)
    Restart()


@RestartOnRest(20000709)
def Event_20000709(
    _,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    special_effect: int,
    special_effect_1: int,
    character: Character | int,
):
    """Event 20000709"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    AND_1.Add(FlagEnabled(flag_1))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, special_effect_1)
    DisableFlag(flag_1)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, special_effect)
    Restart()


@RestartOnRest(20000710)
def Event_20000710(
    _,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    flag_2: Flag | int,
    special_effect: int,
    character: Character | int,
):
    """Event 20000710"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_2):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    OR_3.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    AND_2.Add(TimeElapsed(seconds=seconds))
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    Restart()
    EnableFlag(flag_1)
    Restart()


@RestartOnRest(20000711)
def Event_20000711(
    _,
    entity: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    animation_id: int,
    seconds: float,
):
    """Event 20000711"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    DisableFlag(flag_3)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    EnableFlag(flag_3)
    ForceAnimation(entity, animation_id)
    Wait(seconds)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    Restart()


@RestartOnRest(20000712)
def Event_20000712(
    _,
    entity: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    radius: float,
):
    """Event 20000712"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    AwaitFlagEnabled(flag=flag_2)
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(EntityBeyondDistance(entity=entity, other_entity=ALL_PLAYERS, radius=radius))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(20000713)
def Event_20000713(
    _,
    entity: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    radius: float,
    radius_1: float,
):
    """Event 20000713"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_2):
        return
    if FlagEnabled(flag_3):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(EntityBeyondDistance(entity=entity, other_entity=ALL_PLAYERS, radius=radius))
    OR_2.Add(FlagDisabled(flag))
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(EntityBeyondDistance(entity=entity, other_entity=ALL_PLAYERS, radius=radius_1))
    OR_3.Add(FlagDisabled(flag_1))
    
    MAIN.Await(OR_3)
    
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(20000714)
def Event_20000714(_, character: uint, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, special_effect: int):
    """Event 20000714"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    EnableFlag(flag_2)
    DisableAnimations(character)
    End()


@RestartOnRest(20000720)
def Event_20000720(
    _,
    region: Region | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds: float,
    flag_4: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 20000720"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_4.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_4.Add(FlagRangeAllDisabled(flag_range=(first_flag, last_flag)))
    OR_4.Add(FlagEnabled(flag_5))
    AND_4.Add(OR_4)
    AND_4.Add(FlagDisabled(flag_6))
    
    MAIN.Await(AND_4)
    
    WaitFrames(frames=1)
    AND_1.Add(EventValue(flag=flag_3, bit_count=4) == 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)
    
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(FlagEnabled(flag_4))
    OR_3.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag)
    End()


@RestartOnRest(20000725)
def Event_20000725(_, flag: Flag | int, flag_1: Flag | int):
    """Event 20000725"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        EnableFlag(flag_1)
    else:
        DisableFlag(flag_1)
    End()


@RestartOnRest(20000726)
def Event_20000726(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 20000726"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_5):
        return
    GotoIfFlagDisabled(Label.L0, flag=flag_3)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_3)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(flag_3))
    AND_2.Add(FlagEnabled(flag_5))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag_4)
    End()


@RestartOnRest(20000730)
def Event_20000730(_, character: Character | int, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20000730"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableHealthBar(character)


@RestartOnRest(20000731)
def Event_20000731(_, character: Character | int, flag: Flag | int):
    """Event 20000731"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        SetBackreadStateAlternate(character, True)
    else:
        SetBackreadStateAlternate(character, False)
    Restart()


@RestartOnRest(20000732)
def Event_20000732(
    _,
    asset: uint,
    action_button_id: int,
    item_lot: int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    vfx_id: int,
    vfx_id_1: int,
    flag_1: Flag | int,
):
    """Event 20000732"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagRangeAnyDisabled(flag_range=(first_flag, last_flag)))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(flag_1):
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id)
    else:
        CreateAssetVFX(asset, dummy_id=90, vfx_id=vfx_id_1)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_2)
    DeleteAssetVFX(asset)
    AwardItemLot(item_lot, host_only=True)
    EzstateAIRequest(PLAYER, command_id=60070, command_slot=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    Restart()
