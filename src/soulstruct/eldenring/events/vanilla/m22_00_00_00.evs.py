"""
Stone Coffin Fissure

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
    CommonFunc_9005810(
        0,
        flag=22000800,
        grace_flag=22000000,
        character=22000950,
        asset=22001950,
        enemy_block_distance=5.0,
    )
    RegisterGrace(grace_flag=22000001, asset=22001951)
    RegisterGrace(grace_flag=22000002, asset=22001952)
    RegisterGrace(grace_flag=22000003, asset=22001953)
    RegisterGrace(grace_flag=22000004, asset=22001954)
    Event_22000800()
    Event_22002810()
    Event_22002811()
    Event_22002815()
    Event_22002816()
    Event_22002820()
    Event_22002849()
    Event_22002470()
    Event_22002471(0, character=22000705)
    Event_22002472()
    Event_22002473(0, character=22000705)
    Event_22002474(0, character=22000705)
    Event_22002496(0, character=22000706)
    Event_22002497(0, character=22000706)
    CommonFunc_90005615(0, region=22002699, left=0)
    CommonFunc_900005610(0, asset=22001620, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_900005580(0, flag=580600, asset=22001622, flag_1=9146)
    Event_22002500()
    CommonFunc_90005690(0, region=22002600)
    CommonFunc_90005691(0, region=22002600)
    CommonFunc_90005690(0, region=22002601)
    CommonFunc_90005691(0, region=22002601)
    Event_22002501()
    Event_22000702(
        0,
        flag=4460,
        flag_1=4900,
        flag_2=22000800,
        flag_3=22009209,
        flag_4=22002481,
        flag_5=22009207,
        flag_6=22009208,
        flag_7=22000496,
        flag_8=22009205,
        flag_9=4478,
        flag_10=4928,
        flag_11=2048439205,
    )
    Event_22000700(
        0,
        character=22000700,
        flag=4460,
        flag_1=4463,
        flag_2=4466,
        distance=35.0,
        animation_id=90101,
        flag_3=4900,
        flag_4=22009219,
        flag_5=22009210,
        flag_6=22009211,
        flag_7=22009212,
        flag_8=22009222,
        flag_9=22009208,
        flag_10=22000496,
        flag_11=4928,
    )
    CommonFunc_90005774(0, flag=22000496, item_lot=106310, flag_1=400632)
    Event_22000701(
        0,
        character=22000701,
        flag=4460,
        flag_1=4463,
        flag_2=4467,
        distance=17.0,
        animation_id=90102,
        flag_3=22009231,
        animation_id_1=90103,
        flag_4=4900,
        flag_5=22009233,
        flag_6=4470,
        animation_id_2=90104,
        flag_7=4928,
    )
    Event_22000703(
        0,
        entity=22000701,
        flag=22009237,
        radius=5.0,
        flag_1=22009237,
        flag_2=22009231,
        animation_id=90201,
        flag_3=4894,
    )
    Event_22000705(
        0,
        character=22000710,
        flag=4285,
        flag_1=4286,
        animation_id=930000,
        animation_id_1=930001,
        flag_2=20010800,
    )
    Event_22000708(
        0,
        flag=22002710,
        flag_1=22002711,
        left=22002712,
        character=22000710,
        dummy_id=231,
        asset=22001710,
        dummy_id_1=231,
        radius=0.3499999940395355,
        animation=90215,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
        seconds=2.4000000953674316,
        flag_2=22002713,
        flag_3=22002714,
        flag_4=22009285,
        seconds_1=0.10000000149011612,
    )
    Event_22000709(0, flag=22002714, flag_1=22009286, seconds=0.10000000149011612)
    Event_22000707(
        0,
        flag=4286,
        special_effect=9913,
        flag_1=22009260,
        flag_2=22009261,
        flag_3=22009262,
        flag_4=22009263,
        flag_5=22009264,
        flag_6=22009265,
        flag_7=22009280,
        flag_8=22009281,
        flag_9=22009282,
        flag_10=22009283,
        flag_11=20010800,
        flag_12=4880,
        flag_13=22009275,
    )
    Event_22000715(0, flag=4286, special_effect=9913, flag_1=22009287)
    Event_22000716(0, flag=22009287, special_effect=9711)
    Event_22000717(0, flag=20010800, flag_1=22009275, flag_2=4298, region=22002699)
    CommonFunc_90005750(
        0,
        asset=22000711,
        action_button_id=4350,
        item_lot=107400,
        first_flag=400740,
        last_flag=400740,
        flag=4286,
        vfx_id=6103,
    )
    CommonFunc_90005748(0, entity=22001700, action_button_id=206020, text=1030029, display_distance=30.0, flag=4919)
    CommonFunc_90005706(0, character=22000730, animation_id=30018, left=0)
    CommonFunc_90005706(0, character=22000731, animation_id=30015, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005250(0, character=22000450, region=22002450, seconds=0.0, animation_id=0)
    CommonFunc_90005301(0, flag=22000460, character=22000460, item_lot__unk1=22000900, seconds=0.0, unk1=0)
    CommonFunc_90005211(
        0,
        character=22000460,
        animation_id=30001,
        animation_id_1=20001,
        region=22002460,
        radius=30.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000400,
        animation_id=30005,
        animation_id_1=20005,
        region=22002400,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000401,
        animation_id=30005,
        animation_id_1=20005,
        region=22002402,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000407,
        animation_id=30003,
        animation_id_1=20003,
        region=22002406,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000408,
        animation_id=30003,
        animation_id_1=20003,
        region=22002408,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000409,
        animation_id=30003,
        animation_id_1=20003,
        region=22002411,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000410,
        animation_id=30005,
        animation_id_1=20005,
        region=22002408,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000411,
        animation_id=30003,
        animation_id_1=20003,
        region=22002411,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000415,
        animation_id=30005,
        animation_id_1=20005,
        region=22002415,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000413,
        animation_id=30003,
        animation_id_1=20003,
        region=22002413,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000420,
        animation_id=30000,
        animation_id_1=20000,
        region=22002420,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=22000422, region=22002420, seconds=0.0, animation_id=3020)
    CommonFunc_90005250(0, character=22000425, region=22002425, seconds=0.0, animation_id=3020)
    CommonFunc_90005211(
        0,
        character=22000426,
        animation_id=30000,
        animation_id_1=20000,
        region=22002426,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000427,
        animation_id=30001,
        animation_id_1=20001,
        region=22002427,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000429,
        animation_id=30001,
        animation_id_1=20001,
        region=22002429,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000430,
        animation_id=30003,
        animation_id_1=20003,
        region=22002431,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000431,
        animation_id=30003,
        animation_id_1=20003,
        region=22002431,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=22000432, region=22002431, seconds=0.4000000059604645, animation_id=0)
    CommonFunc_90005210(
        0,
        character=22000433,
        animation_id=30003,
        animation_id_1=20003,
        region=22002431,
        radius=10.0,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000440,
        animation_id=30003,
        animation_id_1=20003,
        region=22002440,
        radius=30.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000441,
        animation_id=30003,
        animation_id_1=20003,
        region=22002440,
        radius=30.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000442,
        animation_id=30003,
        animation_id_1=20003,
        region=22002442,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000443,
        animation_id=30003,
        animation_id_1=20003,
        region=22002442,
        radius=15.0,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000444,
        animation_id=30003,
        animation_id_1=20003,
        region=22002442,
        radius=15.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000445,
        animation_id=30003,
        animation_id_1=20003,
        region=22002442,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000302,
        animation_id=30001,
        animation_id_1=20001,
        region=22002302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000303,
        animation_id=30001,
        animation_id_1=20001,
        region=22002303,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000304,
        animation_id=30000,
        animation_id_1=20000,
        region=22002302,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000310,
        animation_id=30000,
        animation_id_1=20000,
        region=22002310,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000311,
        animation_id=30000,
        animation_id_1=20000,
        region=22002310,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000315,
        animation_id=30000,
        animation_id_1=20000,
        region=22002310,
        seconds=1.7999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000317,
        animation_id=30000,
        animation_id_1=20000,
        region=22002310,
        seconds=2.200000047683716,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=22000312, region=22002312, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=22000313,
        animation_id=30000,
        animation_id_1=20000,
        region=22002312,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=22000314, region=22002312, seconds=0.20000000298023224, animation_id=0)
    CommonFunc_90005200(
        0,
        character=22000316,
        animation_id=30000,
        animation_id_1=20000,
        region=22002312,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=22000318, region=22002312, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=22000320,
        animation_id=30000,
        animation_id_1=20000,
        region=22002320,
        seconds=1.899999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000321,
        animation_id=30001,
        animation_id_1=20001,
        region=22002320,
        seconds=1.2999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000322,
        animation_id=30000,
        animation_id_1=20000,
        region=22002320,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000323,
        animation_id=30000,
        animation_id_1=20000,
        region=22002320,
        seconds=1.7999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000324,
        animation_id=30001,
        animation_id_1=20001,
        region=22002320,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000325,
        animation_id=30001,
        animation_id_1=20001,
        region=22002320,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000326,
        animation_id=30000,
        animation_id_1=20000,
        region=22002320,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=22000327,
        animation_id=30001,
        animation_id_1=20001,
        region=22002320,
        radius=18.5,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000340,
        animation_id=30000,
        animation_id_1=20000,
        region=22002340,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000341,
        animation_id=30000,
        animation_id_1=20000,
        region=22002340,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000342,
        animation_id=30001,
        animation_id_1=20001,
        region=22002340,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=22000347,
        animation_id=30000,
        animation_id_1=20000,
        region=22002347,
        radius=10.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005210(
        0,
        character=22000348,
        animation_id=30000,
        animation_id_1=20000,
        region=22002347,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    RemoveSpecialEffect(22000200, 14902)
    RemoveSpecialEffect(22000201, 14902)
    RemoveSpecialEffect(22000202, 14902)
    RemoveSpecialEffect(22000203, 14902)
    RemoveSpecialEffect(22000210, 14902)
    RemoveSpecialEffect(22000211, 14902)
    RemoveSpecialEffect(22000212, 14902)
    RemoveSpecialEffect(22000214, 14902)
    RemoveSpecialEffect(22000215, 14902)
    RemoveSpecialEffect(22000218, 14902)
    RemoveSpecialEffect(22000219, 14902)
    RemoveSpecialEffect(22000220, 14902)
    RemoveSpecialEffect(22000221, 14902)
    RemoveSpecialEffect(22000222, 14902)
    RemoveSpecialEffect(22000227, 14902)
    RemoveSpecialEffect(22000228, 14902)
    RemoveSpecialEffect(22000242, 14902)
    RemoveSpecialEffect(22000246, 14902)
    RemoveSpecialEffect(22000247, 14902)
    RemoveSpecialEffect(22000251, 14902)
    RemoveSpecialEffect(22000275, 14902)
    RemoveSpecialEffect(22000276, 14902)
    RemoveSpecialEffect(22000277, 14902)
    RemoveSpecialEffect(22000201, 14902)
    CommonFunc_90005220(
        0,
        character=22000201,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    RemoveSpecialEffect(22000202, 14902)
    CommonFunc_90005220(
        0,
        character=22000202,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000210,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000211,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000214,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000215,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000220,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000221,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005220(
        0,
        character=22000222,
        animation_id=30000,
        animation_id_1=20000,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
    )
    CommonFunc_90005200(
        0,
        character=22000225,
        animation_id=30000,
        animation_id_1=20005,
        region=22002225,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=22000240,
        animation_id=30000,
        animation_id_1=20005,
        region=22002240,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005260(0, character=22000241, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000243, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000244, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000245, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000248, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000249, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000250, region=22002241, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=22000252,
        animation_id=30000,
        animation_id_1=20005,
        region=22002252,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005260(0, character=22000255, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000256, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000257, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000258, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000259, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000260, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000261, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000262, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000263, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000264, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(0, character=22000265, region=22002255, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=22000278, region=22002278, seconds=0.0, animation_id=0)
    CommonFunc_90005260(0, character=22000279, region=22002278, radius=6.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=22000280,
        animation_id=30000,
        animation_id_1=20005,
        region=22002280,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005260(0, character=22000281, region=22002278, radius=6.5, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=22000282, region=22002278, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=22000283, region=22002278, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=22000350, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000351, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000352, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000353, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000354, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000360, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000361, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000362, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000363, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000364, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000365, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000370, animation_id=30005, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000371, animation_id=30005, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000372, animation_id=30005, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000373, animation_id=30005, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000374, animation_id=30005, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000380, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000381, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000382, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000383, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000384, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000390, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000391, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000392, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000393, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=22000394, animation_id=30004, animation_id_1=-1, seconds=0.0, left=0)
    Event_22002300(0, character=22000300, region=22002300)
    Event_22002300(1, character=22000302, region=22002302)
    Event_22002300(2, character=22000303, region=22002302)
    Event_22002300(3, character=22000304, region=22002302)
    Event_22002300(4, character=22000305, region=22002302)
    Event_22002300(5, character=22000306, region=22002302)
    Event_22002300(6, character=22000307, region=22002302)
    Event_22002300(7, character=22000320, region=22002320)
    Event_22002300(8, character=22000321, region=22002320)
    Event_22002300(9, character=22000322, region=22002320)
    Event_22002300(10, character=22000323, region=22002320)
    Event_22002300(11, character=22000324, region=22002320)
    Event_22002300(12, character=22000325, region=22002320)
    Event_22002300(13, character=22000326, region=22002320)
    Event_22002300(14, character=22000327, region=22002320)
    Event_22002300(15, character=22000328, region=22002320)


@RestartOnRest(22002225)
def Event_22002225(_, flag: Flag | int, character: uint, region: Region | int):
    """Event 22002225"""
    AND_15.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(1, AND_15)
    End()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    if ThisEventSlotFlagDisabled():
        ForceAnimation(character, 30000, loop=True)
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_9)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(FlagDisabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(character, 20000, loop=True)
    EnableAI(character)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_10.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_10)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    GotoIfConditionFalse(Label.L10, input_condition=AND_2)
    DisableNetworkFlag(flag)
    ForceAnimation(character, 20010, wait_for_completion=True)
    ForceAnimation(character, 30000, loop=True)
    DisableAI(character)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitRealFrames(frames=1)
    Restart()


@RestartOnRest(22002470)
def Event_22002470():
    """Event 22002470"""
    if FlagEnabled(22000800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L10, flag=22009209)
    DisableFlag(22002488)
    DisableFlag(22002489)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(22009209))
    AND_3.Add(ActionButtonParamActivated(action_button_id=209522, entity=22001480))
    OR_1.Add(FlagEnabled(22000800))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(22000800):
        return
    AwaitDialogResponse(
        message=2080810,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=22001480,
        display_distance=3.0,
        left_flag=22002488,
        right_flag=22002489,
        cancel_flag=22002489,
    )
    if FlagDisabled(22002488):
        return RESTART

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    Wait(1.0)
    EnableNetworkFlag(22002481)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    
    MAIN.Await(FlagEnabled(22009209))
    
    Restart()


@RestartOnRest(22002471)
def Event_22002471(_, character: uint):
    """Event 22002471"""
    GotoIfFlagDisabled(Label.L10, flag=22000800)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableCharacterCollision(character)
    DisableGravity(character)
    DisableAI(character)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagDisabled(Label.L20, flag=22009209)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    EnableCharacter(character)
    AddSpecialEffect(character, 20004380)
    DisableAnimations(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_1.Add(FlagEnabled(22009209))
    AND_1.Add(FlagEnabled(22002481))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(22000800):
        DisableCharacter(character)
        DisableAnimations(character)
        DisableCharacterCollision(character)
        DisableGravity(character)
        DisableAI(character)
        End()
    if PlayerInOwnWorld():
        DisplayNetworkMessage(text=4080100, unk_4_5=False)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    DeleteAssetVFX(22001480)
    CreateAssetVFX(22001480, dummy_id=100, vfx_id=30320)
    RemoveSpecialEffect(character, 20004380)
    AddSpecialEffect(character, 18677)
    EnableInvincibility(character)
    Wait(1.0)
    RemoveSpecialEffect(character, 18677)
    ForceAnimation(character, 63010, wait_for_completion=True)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.WhitePhantom)
    SetCharacterEventTarget(character, entity=22000800)
    SkipLinesIfPlayerNotInOwnWorld(2)
    DisplayNetworkMessage(text=4080810, unk_4_5=False)
    SkipLinesIfPlayerInOwnWorld(1)
    DisplayNetworkMessage(text=4080811, unk_4_5=False)
    DeleteAssetVFX(22001480)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    
    MAIN.Await(FlagEnabled(22009209))
    
    Restart()


@RestartOnRest(22002472)
def Event_22002472():
    """Event 22002472"""
    GotoIfFlagEnabled(Label.L2, flag=22000800)
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(22009209))
    
    DeleteAssetVFX(22001480)
    CreateAssetVFX(22001480, dummy_id=100, vfx_id=30001)
    OR_1.Add(FlagEnabled(22002481))
    OR_1.Add(FlagEnabled(22000800))
    
    MAIN.Await(OR_1)
    
    DeleteAssetVFX(22001480)
    End()


@RestartOnRest(22002473)
def Event_22002473(_, character: uint):
    """Event 22002473"""
    if FlagEnabled(22000800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=22002481)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(22009209))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=22001480, radius=1.5))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=22000800)
    GotoIfFlagEnabled(Label.L1, flag=22002481)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAI(character)
    AddSpecialEffect(character, 20004380)
    WaitFrames(frames=1)
    DisableAnimations(character)
    WaitFrames(frames=1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=22001480, radius=1.5))
    OR_2.Add(AND_2)
    OR_2.Add(FlagDisabled(22009209))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=22000800)
    GotoIfFlagEnabled(Label.L1, flag=22002481)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(22002474)
def Event_22002474(_, character: uint):
    """Event 22002474"""
    if FlagEnabled(22000800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(22009209))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(FlagEnabled(22002481))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(FlagEnabled(22000800))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.0)
    AND_3.Add(FlagEnabled(22002481))
    AND_5.Add(FlagDisabled(22002481))
    AND_5.Add(FlagEnabled(22000800))
    OR_3.Add(AND_1)
    OR_3.Add(AND_3)
    OR_3.Add(AND_5)
    
    MAIN.Await(OR_3)
    
    if LastResult(AND_5):
        return
    AND_9.Add(HealthRatio(character) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_9)
    DisplayNetworkMessage(text=4080812, unk_4_5=False)
    End()
    Wait(4.0)
    SetTeamType(character, TeamType.NoTeam)
    DisableAnimations(character)
    EnableInvincibility(character)
    AddSpecialEffect(character, 18677)
    ReplanAI(character)
    ClearTargetList(character)
    Wait(3.0)
    DisableAI(character)
    DisableInvincibility(character)
    ResetAnimation(character, disable_interpolation=True)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_10.Add(HealthRatio(character) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_10)
    DisplayNetworkMessage(text=4080812, unk_4_5=False)
    End()


@RestartOnRest(22002496)
def Event_22002496(_, character: uint):
    """Event 22002496"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    EnableImmortality(character)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    DisableAsset(22001496)
    if FlagEnabled(22000496):
        return
    AddSpecialEffect(character, 18677)
    EnableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    AND_1.Add(FlagEnabled(22009208))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=22002496))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=22002497))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    EnableFlag(22002708)
    EnableAsset(22001496)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    CreateAssetVFX(22001497, dummy_id=100, vfx_id=30330)
    RemoveSpecialEffect(character, 4380)
    RemoveSpecialEffect(character, 18677)
    EnableCharacter(character)
    EnableInvincibility(character)
    Move(character, destination=22002180, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 63010, wait_for_completion=True)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.HostileNPC)
    SetCharacterEventTarget(character, entity=PLAYER)
    DisplayNetworkMessage(text=4080820, unk_4_5=False)
    DeleteAssetVFX(22001497)
    End()


@RestartOnRest(22002497)
def Event_22002497(_, character: uint):
    """Event 22002497"""
    if FlagEnabled(character):
        return
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.0)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    Wait(5.0)
    EnableFlag(22000496)
    DisplayNetworkMessage(text=4080822, unk_4_5=False)
    KillBossAndDisplayBanner(character=character, banner_type=BannerType.DuelistVanquished)
    DisableAsset(22001496)
    End()


@RestartOnRest(22002500)
def Event_22002500():
    """Event 22002500"""
    GotoIfFlagDisabled(Label.L0, flag=22000500)
    DisableAsset(22001500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_2)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=22002500))
    
    MAIN.Await(AND_1)
    
    Wait(0.20000000298023224)
    DestroyAsset(22001500)
    EnableFlag(22000500)


@RestartOnRest(22002501)
def Event_22002501():
    """Event 22002501"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=22002603))
    
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)
    WaitRealFrames(frames=2)
    AddSpecialEffect(PLAYER, 19935)


@RestartOnRest(22002300)
def Event_22002300(_, character: Character | int, region: Region | int):
    """Event 22002300"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4080)
    AddSpecialEffect(character, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4080)
    RemoveSpecialEffect(character, 4085)
    Restart()


@RestartOnRest(22000800)
def Event_22000800():
    """Event 22000800"""
    if FlagEnabled(22000800):
        return
    
    MAIN.Await(HealthValue(22000800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(22008000, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(22000800))
    
    Kill(22000801)
    DisableCharacter(22000801)
    DisableAnimations(22000801)
    KillBossAndDisplayBanner(character=22000800, banner_type=BannerType.LegendFelled)
    EnableFlag(22000800)
    EnableFlag(9148)
    if PlayerInOwnWorld():
        EnableFlag(61148)


@RestartOnRest(22002810)
def Event_22002810():
    """Event 22002810"""
    GotoIfFlagDisabled(Label.L0, flag=22000800)
    DisableCharacter(22000800)
    DisableAnimations(22000800)
    Kill(22000800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(22000800)
    DisableAsset(22001801)
    ForceAnimation(22000800, 30010, loop=True)
    SetLockOnPoint(character=22000800, lock_on_dummy_id=221, state=False)
    SetLockOnPoint(character=22000801, lock_on_dummy_id=220, state=False)
    ReferDamageToEntity(22000801, target_entity=22000800)
    GotoIfFlagEnabled(Label.L1, flag=22000802)
    AND_1.Add(FlagEnabled(22002805))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=22002804))
    OR_1.Add(AttackedWithDamageType(attacked_entity=22000800, attacker=PLAYER))
    OR_1.Add(CharacterHasStateInfo(character=22000800, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=22000800, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=22000800, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=22000800, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=22000800, state_info=260))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(22000802)
    Wait(1.5)
    ForceAnimation(22000800, 20010)
    Wait(2.5999999046325684)
    AddSpecialEffect(22000800, 20010097)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_10.Add(FlagEnabled(22002805))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=22002802))
    
    MAIN.Await(AND_10)
    
    Wait(1.0)
    ForceAnimation(22000800, 20010)
    Wait(2.5999999046325684)
    AddSpecialEffect(22000800, 20010098)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(22000800)
    Wait(3.0)
    EnableBossHealthBar(22000800, name=905020000)
    EnableNetworkFlag(22002801)
    EnableAsset(22001801)


@RestartOnRest(22002811)
def Event_22002811():
    """Event 22002811"""
    if FlagEnabled(22000800):
        return
    AND_1.Add(HealthRatio(22000800) <= 0.6499999761581421)
    AND_1.Add(CharacterHasSpecialEffect(22000800, 20010050))
    
    MAIN.Await(AND_1)
    
    EnableFlag(22002802)


@RestartOnRest(22002815)
def Event_22002815():
    """Event 22002815"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L1, flag=22000802)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=22002815))
    
    SetBossMusic(bgm_boss_conv_param_id=502000, state=BossMusicState.NormalFadeOut)
    
    MAIN.Await(FlagEnabled(22000802))
    
    EnableFlag(22002815)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=22002815))
    
    EnableFlag(22002815)


@RestartOnRest(22002816)
def Event_22002816():
    """Event 22002816"""
    if FlagEnabled(22000800):
        return
    AND_1.Add(FlagEnabled(22002805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=22002802))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(22000800, True)
    SetNetworkUpdateRate(22000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(22002820)
def Event_22002820():
    """Event 22002820"""
    if FlagEnabled(22000802):
        return
    AddSpecialEffect(22000100, 9531)
    AwaitFlagEnabled(flag=22000802)
    AddSpecialEffect(22000100, 9532)


@RestartOnRest(22002849)
def Event_22002849():
    """Event 22002849"""
    CommonFunc_9005800(
        0,
        flag=22000800,
        entity=22001800,
        region=22002800,
        flag_1=22002805,
        character=22005800,
        action_button_id=10000,
        left=22000801,
        region_1=22002801,
    )
    CommonFunc_9005801(
        0,
        flag=22000800,
        entity=22001800,
        region=22002800,
        flag_1=22002805,
        flag_2=22002806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=22000800, asset=22001800, vfx_id=1580, right=22000801)
    CommonFunc_9005811(0, flag=22000800, asset=22001801, vfx_id=5, right=22002801)
    CommonFunc_9005822(
        0,
        flag=22000800,
        bgm_boss_conv_param_id=502000,
        flag_1=22002805,
        flag_2=22002806,
        right=22002815,
        flag_3=22002802,
        left=0,
        left_1=0,
    )


@RestartOnRest(22000700)
def Event_22000700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    animation_id: int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
):
    """Event 22000700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=flag_11)
    SkipLinesIfFlagDisabled(5, flag_8)
    SkipLinesIfFlagEnabled(4, flag_10)
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9607))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9608))
    
    MAIN.Await(AND_5)
    
    EnableFlag(flag_9)
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_2.Add(FlagEnabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableInvincibility(character)
    WaitRealFrames(frames=1)
    AND_10.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_10)
    
    Move(character, destination=22002701, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=1)
    SetCharacterTalkRange(character=character, distance=distance)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id)
    GotoIfFlagDisabled(Label.L20, flag=flag_4)
    if FlagDisabled(flag_5):
        EnableFlag(flag_5)
        Goto(Label.L20)
    if FlagDisabled(flag_6):
        EnableFlag(flag_6)
        Goto(Label.L20)
    EnableFlag(flag_7)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_15.Add(FlagEnabled(flag_2))
    AND_15.Add(FlagDisabled(flag_3))
    OR_15.Add(AND_15)
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(22000701)
def Event_22000701(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    animation_id: int,
    flag_3: Flag | int,
    animation_id_1: int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    animation_id_2: int,
    flag_7: Flag | int,
):
    """Event 22000701"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_4.Add(FlagEnabled(flag_2))
    AND_4.Add(FlagEnabled(flag_7))
    GotoIfConditionTrue(Label.L20, input_condition=AND_4)
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_6))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag_4))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    OR_2.Add(FlagEnabled(flag_2))
    OR_2.Add(FlagEnabled(flag_6))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag_4))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L4, flag=flag_1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableInvincibility(character)
    WaitRealFrames(frames=1)
    AND_5.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_5)
    
    Move(character, destination=22002701, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=1)
    if FlagEnabled(flag_6):
        ForceAnimation(character, animation_id_2, loop=True)
        Goto(Label.L20)
    SetCharacterTalkRange(character=character, distance=distance)
    DisableFlag(flag_5)
    if FlagEnabled(flag_3):
        ForceAnimation(character, animation_id_1, loop=True)
        EnableFlag(flag_5)
        Goto(Label.L20)
    if ValueNotEqual(left=-1, right=animation_id):
        ForceAnimation(character, animation_id, loop=True)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_14.Add(FlagEnabled(flag_2))
    OR_14.Add(FlagEnabled(flag_6))
    AND_15.Add(OR_14)
    AND_15.Add(FlagDisabled(flag_4))
    OR_15.Add(AND_15)
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(22000702)
def Event_22000702(
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
):
    """Event 22000702"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    GotoIfFlagEnabled(Label.L10, flag=flag_10)
    GotoIfFlagDisabled(Label.L1, flag=flag_2)
    GotoIfFlagDisabled(Label.L2, flag=flag_7)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagDisabled(flag_11):
        return
    EnableFlag(flag_3)
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag_4):
        EnableFlag(flag_5)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(FlagEnabled(flag_7))
    
    DisableFlag(flag_6)
    EnableFlag(flag_8)
    EnableFlag(flag_9)
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_3)
    DisableFlag(flag_6)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag_3)
    DisableFlag(flag_6)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()


@RestartOnRest(22000703)
def Event_22000703(
    _,
    entity: uint,
    flag: Flag | int,
    radius: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
    animation_id: int,
    flag_3: Flag | int,
):
    """Event 22000703"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(EntityBeyondDistance(entity=entity, other_entity=PLAYER, radius=radius))
    
    MAIN.Await(OR_1)
    
    if PlayerInOwnWorld():
        EnableFlag(flag_1)
        EnableFlag(flag_2)
        EnableFlag(flag_3)
    ForceAnimation(entity, animation_id)
    End()


@RestartOnRest(22000705)
def Event_22000705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_2: Flag | int,
):
    """Event 22000705"""
    DisableNetworkSync()
    WaitFrames(frames=2)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(AND_1)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(flag_1))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    if FlagEnabled(flag_2):
        ForceAnimation(character, animation_id_1)
    else:
        ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.NoTeam)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_3.Add(FlagEnabled(flag))
    OR_3.Add(FlagEnabled(flag_1))
    OR_3.Add(AND_3)
    
    MAIN.Await(not OR_3)
    
    Restart()


@RestartOnRest(22000707)
def Event_22000707(
    _,
    flag: Flag | int,
    special_effect: int,
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
):
    """Event 22000707"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(ALL_PLAYERS, special_effect))
    
    if FlagDisabled(flag_1):
        EnableFlag(flag_1)
        End()
    if FlagDisabled(flag_2):
        EnableFlag(flag_2)
        End()
    if FlagDisabled(flag_3):
        EnableFlag(flag_3)
        End()
    EnableFlag(flag_12)
    if FlagDisabled(flag_4):
        EnableFlag(flag_4)
        EnableFlag(flag_7)
        End()
    if FlagDisabled(flag_5):
        EnableFlag(flag_5)
        EnableFlag(flag_8)
        End()
    EnableFlag(flag_9)
    EnableFlag(flag_6)
    End()
    DisableFlag(flag_10)
    DisableFlag(flag_11)
    DisableFlag(flag_13)


@RestartOnRest(22000708)
def Event_22000708(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    seconds: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds_1: float,
):
    """Event 22000708"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_4)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLinesIfConditionFalse(3, AND_1)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    SkipLinesIfConditionFalse(3, AND_15)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    DisableFlag(flag_2)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfValueEqual(5, left=dummy_id, right=0)
    ResetAnimation(PLAYER)
    SkipLinesIfFlagEnabled(3, flag_4)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    Goto(Label.L15)
    EnableFlag(flag_3)
    Wait(seconds_1)

    # --- Label 15 --- #
    DefineLabel(15)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    if ValueNotEqual(left=special_effect, right=-1):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    else:
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(22000709)
def Event_22000709(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 22000709"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(22000715)
def Event_22000715(_, flag: Flag | int, special_effect: int, flag_1: Flag | int):
    """Event 22000715"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(ALL_PLAYERS, special_effect))
    
    EnableFlag(flag_1)
    
    MAIN.Await(HealthValue(ALL_PLAYERS) == 0)
    
    DisableFlag(flag_1)
    End()


@RestartOnRest(22000716)
def Event_22000716(_, flag: Flag | int, special_effect: int):
    """Event 22000716"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    AddSpecialEffect(ALL_PLAYERS, special_effect)
    DisableFlag(flag)
    End()


@RestartOnRest(22000717)
def Event_22000717(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, region: Region | int):
    """Event 22000717"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    End()
