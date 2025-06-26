"""
Specimen Storehouse

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
        flag=21010800,
        grace_flag=21010000,
        character=21010950,
        asset=21011950,
        enemy_block_distance=0.0,
    )
    CommonFunc_90005102(
        0,
        flag=76945,
        flag_1=72110,
        asset=21011980,
        source_flag=77900,
        value=0,
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
    RegisterGrace(grace_flag=21010001, asset=21011951, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21010002, asset=21011952, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21010003, asset=21011953, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21010004, asset=21011954, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21010006, asset=21011956, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21010007, asset=21011957, enemy_block_distance=0.0)
    Event_21012800()
    Event_21012810()
    Event_21012811()
    Event_21012848()
    Event_21012847()
    Event_21012849()
    Event_21012820(0, special_effect=20010650, dummy_id=50, animation_id=3000)
    Event_21012820(1, special_effect=20010651, dummy_id=50, animation_id=3001)
    Event_21012820(2, special_effect=20010652, dummy_id=50, animation_id=3002)
    Event_21012820(3, special_effect=20010653, dummy_id=50, animation_id=3003)
    Event_21012820(4, special_effect=20010654, dummy_id=50, animation_id=3004)
    Event_21012825(0, special_effect=20010660, dummy_id=20, animation_id=20010)
    Event_21012825(1, special_effect=20010661, dummy_id=20, animation_id=20011)
    Event_21012825(2, special_effect=20010662, dummy_id=20, animation_id=20012)
    Event_21012825(3, special_effect=20010663, dummy_id=20, animation_id=20013)
    Event_21012825(4, special_effect=20010664, dummy_id=20, animation_id=20014)
    Event_21012830(0, special_effect=20010642, dummy_id=42, animation_id=3002, character=21010822)
    Event_21012830(1, special_effect=20010643, dummy_id=43, animation_id=3003, character=21010823)
    Event_21012830(2, special_effect=20010644, dummy_id=44, animation_id=3004, character=21010824)
    Event_21012830(3, special_effect=20010645, dummy_id=45, animation_id=3005, character=21010825)
    Event_21012830(4, special_effect=20010646, dummy_id=46, animation_id=3006, character=21010826)
    Event_21012830(5, special_effect=20010647, dummy_id=47, animation_id=3007, character=21010827)
    Event_21012836(0, character=21010822)
    Event_21012836(1, character=21010823)
    Event_21012836(2, character=21010824)
    Event_21012836(3, character=21010825)
    Event_21012836(4, character=21010826)
    Event_21012836(5, character=21010827)
    Event_21012842()
    Event_21012843(0, special_effect=20010677, locked_camera_id__normal_camera_id=5131, character=21010800)
    Event_21012843(1, special_effect=20010678, locked_camera_id__normal_camera_id=5142, character=21010810)
    Event_21012843(2, special_effect=20010679, locked_camera_id__normal_camera_id=5143, character=21010810)
    Event_21012844()
    Event_21012846()
    Event_21012845()
    CommonFunc_90005795(
        0,
        flag=7621,
        flag_1=0,
        flag_2=2048459295,
        left_flag=21012141,
        cancel_flag__right_flag=21012142,
        message=2080601,
        action_button_id=209051,
        asset=21011735,
        vfx_id=30010,
    )
    if CeremonyActive(ceremony=40):
        CommonFunc_90005799(
            0,
            flag=7621,
            character=21010735,
            banner_type=5,
            region=21012140,
            flag_1=21012749,
            character_1=21010736,
        )
    Event_21012144()
    CommonFunc_90005795(
        0,
        flag=7622,
        flag_1=0,
        flag_2=2048459298,
        left_flag=21012151,
        cancel_flag__right_flag=21012152,
        message=2080602,
        action_button_id=209052,
        asset=21011745,
        vfx_id=30000,
    )
    if CeremonyActive(ceremony=50):
        CommonFunc_90005798(0, flag=7622, character=21010745, banner_type=7, region=21012150, flag_1=21012759)
    Event_21012154()
    Event_21012170(0, flag=21012161, character=21010700, character_1=21010709)
    Event_21012171(
        0,
        flag=21010800,
        flag_1=21012160,
        copy_draw_parent=21010700,
        character=21010709,
        asset=21011170,
        flag_2=2048459220,
        message=2080870,
        left_flag=21012178,
        cancel_flag__right_flag=21012179,
    )
    Event_21012172(
        0,
        flag=21010800,
        flag_1=21012160,
        flag_2=21012161,
        character=21010700,
        text=4080870,
        text_1=4080871,
        animation_id=90200,
        asset=21011170,
    )
    Event_21012173(0, flag=21010800, flag_1=21012161, character=21010700, text=4080872, text_1=4080872)
    Event_21012174(0, flag=21010800, flag_1=21012161, character=21010700, right=21012703)
    Event_21012170(10, flag=21012165, character=21010760, character_1=21010769)
    Event_21012171(
        10,
        flag=21010800,
        flag_1=21012164,
        copy_draw_parent=21010760,
        character=21010769,
        asset=21011174,
        flag_2=2051459750,
        message=2080880,
        left_flag=21012188,
        cancel_flag__right_flag=21012189,
    )
    Event_21012172(
        10,
        flag=21010800,
        flag_1=21012164,
        flag_2=21012165,
        character=21010760,
        text=4080880,
        text_1=4080881,
        animation_id=63010,
        asset=21011174,
    )
    Event_21012173(10, flag=21010800, flag_1=21012165, character=21010760, text=4080882, text_1=4080882)
    Event_21012174(10, flag=21010800, flag_1=21012165, character=21010760, right=0)
    CommonFunc_90005301(0, flag=21010459, character=21010459, item_lot__unk1=21011991, seconds=0.0, unk1=2)
    CommonFunc_90005201(
        0,
        character=21010200,
        animation_id=30004,
        animation_id_1=20004,
        radius=6.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010201, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=21010202,
        animation_id=30004,
        animation_id_1=20004,
        region=21012202,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010202,
        animation_id=30004,
        animation_id_1=20004,
        region=21012202,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010204, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010205, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=21010206, region=21012206, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=21010207, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=21010208,
        animation_id=30004,
        animation_id_1=20004,
        region=21012208,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010209,
        animation_id=30004,
        animation_id_1=20004,
        region=21012209,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010210,
        animation_id=30004,
        animation_id_1=20004,
        region=21012209,
        radius=1.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010211, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010212, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010213, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010214, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010215, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010216, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005251(0, character=21010217, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010218, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010219, region=21012219, radius=1.0, seconds=1.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=21010219,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010225, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010226, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=21010228,
        animation_id=30004,
        animation_id_1=20004,
        region=21012453,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010229,
        animation_id=30004,
        animation_id_1=20004,
        region=21012453,
        radius=1.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010230,
        animation_id=30004,
        animation_id_1=20004,
        region=21012453,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010236, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010237, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010238, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010239, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=21010241, region=21012241, radius=1.0, seconds=0.10000000149011612, animation_id=0)
    CommonFunc_90005261(0, character=21010242, region=21012241, radius=1.0, seconds=0.6000000238418579, animation_id=0)
    CommonFunc_90005261(0, character=21010243, region=21012241, radius=1.0, seconds=0.30000001192092896, animation_id=0)
    CommonFunc_90005251(0, character=21010244, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010245, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010246, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010247, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21010248,
        animation_id=30004,
        animation_id_1=20004,
        region=21012248,
        radius=1.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010249,
        animation_id=30004,
        animation_id_1=20004,
        region=21012249,
        radius=1.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=21010250, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010251, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010252, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21010254,
        animation_id=30004,
        animation_id_1=20004,
        region=21012254,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010255,
        animation_id=30004,
        animation_id_1=20004,
        region=21012254,
        radius=1.0,
        seconds=0.699999988079071,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010256,
        animation_id=30004,
        animation_id_1=20004,
        region=21012256,
        radius=1.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010257,
        animation_id=30004,
        animation_id_1=20004,
        region=21012257,
        radius=2.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010258,
        animation_id=30004,
        animation_id_1=20004,
        region=21012258,
        radius=2.0,
        seconds=0.20000000298023224,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010259,
        animation_id=30004,
        animation_id_1=20004,
        region=21012259,
        radius=2.0,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21010261, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010263, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21010265, animation_id=30004, animation_id_1=20004, seconds=0.0, left=0)
    CommonFunc_90005201(
        0,
        character=21010266,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010267,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010268,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=21010269, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010270, region=21012270, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010271, region=21012270, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010272, region=21012270, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=21010273,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010274,
        animation_id=30004,
        animation_id_1=20004,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21010280, region=21012219, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=21010285,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010286,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010287,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=21010288, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005201(
        0,
        character=21010289,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010290,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010291,
        animation_id=30004,
        animation_id_1=20004,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=21010292, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21010300,
        animation_id=30000,
        animation_id_1=20000,
        region=21012300,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21010303, region=21012303, radius=1.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005263(0, character=21010305, region=21012305, radius=2.0, seconds=0.0, animation_id=3010, region_1=0)
    CommonFunc_90005211(
        0,
        character=21010306,
        animation_id=30000,
        animation_id_1=20000,
        region=21012306,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21010307, region=21012307, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010308, region=21012308, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010308, region=0, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010309, region=21012309, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010310, region=21012309, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21010360,
        animation_id=30019,
        animation_id_1=20019,
        region=21012360,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21010363, region=21012363, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010364, region=21012363, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21010367,
        animation_id=30000,
        animation_id_1=20000,
        region=21012367,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010368,
        animation_id=30000,
        animation_id_1=20000,
        region=21012367,
        radius=0.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010369,
        animation_id=30000,
        animation_id_1=20000,
        region=21012367,
        radius=0.0,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010370,
        animation_id=30000,
        animation_id_1=20000,
        region=21012370,
        radius=1.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21010371,
        animation_id=30000,
        animation_id_1=20000,
        region=21012371,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010372,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=21010373,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21010450, region=21012450, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010451, region=21012451, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010452, region=21012452, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010453, region=21012453, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010454, region=21012454, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010455, region=21012455, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010456, region=21012456, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010457, region=21012457, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010458, region=21012458, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010459, region=21012459, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010460, region=21012460, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010461, radius=3.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010462, region=21012462, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010464, region=21012464, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21010465, region=21012465, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21010461, radius=3.0, seconds=0.0, animation_id=0)
    Event_21012550()
    Event_21012500()
    CommonFunc_90005501(
        0,
        flag=21010510,
        flag_1=21010511,
        left=0,
        asset=21011510,
        asset_1=21011511,
        asset_2=21011512,
        flag_2=21010512,
    )
    CommonFunc_90005501(
        0,
        flag=21010515,
        flag_1=21010516,
        left=0,
        asset=21011515,
        asset_1=21011516,
        asset_2=21011517,
        flag_2=21010517,
    )
    CommonFunc_90005504(0, flag=21010520, flag_1=21010521, left=0, entity=21011520, flag_2=21010522)
    CommonFunc_90005504(0, flag=21010525, flag_1=21010526, left=0, entity=21011525, flag_2=21010527)
    CommonFunc_90005504(0, flag=21010530, flag_1=21010531, left=0, entity=21011530, flag_2=21010532)
    Event_21012510()
    Event_21012570(0, flag=21010570, entity=21011570, asset=21010571, obj_act_id=21013571)
    Event_21012576()
    Event_21012580()
    CommonFunc_900005580(0, flag=580600, asset=21011600, flag_1=9146)
    Event_21012699()
    Event_21010705(
        0,
        character=21010701,
        flag=4368,
        flag_1=21019214,
        animation_id=90101,
        animation_id_1=90102,
        flag_2=4360,
        flag_3=4363,
        flag_4=4898,
        flag_5=21019215,
        flag_6=21019226,
    )
    Event_21010706(0, flag=21019225, flag_1=21019226)
    Event_21010700(
        0,
        character=21010700,
        flag=21012178,
        distance=80.0,
        flag_1=21012700,
        flag_2=21010800,
        flag_3=21012702,
        seconds=1.0,
    )
    Event_21010701(0, character=21010700, flag=21012701, flag_1=21010800)
    Event_21010702(0, flag=21019215, flag_1=21012702, flag_2=21010800, flag_3=2048459220)
    Event_21010703(
        0,
        flag=21010800,
        flag_1=2048459210,
        flag_2=2048459220,
        flag_3=2051459708,
        flag_4=2051459719,
        flag_5=2051459720,
        flag_6=25000800,
        flag_7=2051459750,
        flag_8=21012178,
        flag_9=21012188,
        flag_10=4363,
        region=21012800,
    )
    Event_21010704(0, flag=2048459223, flag_1=21010800, flag_2=2048459220, flag_3=21012805, flag_4=21019205)
    Event_21010715(
        0,
        character=21010710,
        flag=4400,
        flag_1=4401,
        flag_2=4402,
        flag_3=4403,
        flag_4=4406,
        animation_id=90101,
        flag_5=4899,
        flag_6=21019302,
        flag_7=21019316,
        flag_8=21019317,
        flag_9=21019318,
        flag_10=21019320,
        flag_11=7621,
        flag_12=4928,
    )
    CommonFunc_90005704(0, attacked_entity=21010710, flag=4401, flag_1=4400, flag_2=21019301, right=3)
    CommonFunc_90005703(
        0,
        character=21010710,
        flag=4401,
        flag_1=4402,
        flag_2=21019301,
        flag_3=4401,
        first_flag=4400,
        last_flag=4404,
        right=0,
    )
    CommonFunc_90005702(0, character=21010710, flag=4403, first_flag=4400, last_flag=4404)
    CommonFunc_90005744(0, entity=21010710, flag=21019317, flag_1=21019317, animation_id=90202)
    CommonFunc_90005744(0, entity=21010710, flag=21012720, flag_1=4899, animation_id=90307)
    CommonFunc_90005750(
        0,
        asset=21011710,
        action_button_id=4350,
        item_lot=106200,
        first_flag=400620,
        last_flag=400620,
        flag=21019328,
        vfx_id=6102,
    )
    CommonFunc_90005750(
        0,
        asset=21011710,
        action_button_id=4350,
        item_lot=106210,
        first_flag=400622,
        last_flag=400623,
        flag=21019331,
        vfx_id=6102,
    )
    CommonFunc_90005750(
        0,
        asset=21011710,
        action_button_id=4350,
        item_lot=106230,
        first_flag=400625,
        last_flag=400625,
        flag=21019332,
        vfx_id=6102,
    )
    Event_21010716(
        0,
        flag=21019329,
        asset=21011710,
        character=21010710,
        flag_1=21019331,
        flag_2=21019332,
        flag_3=21019310,
        flag_4=21019328,
        flag_5=21019317,
    )
    Event_21010720(
        0,
        character=21010720,
        flag=4426,
        animation_id=90101,
        flag_1=21019352,
        first_flag=4420,
        flag_2=4421,
        flag_3=4423,
        flag_4=4897,
        distance=60.0,
        flag_5=4891,
        last_flag=4424,
        left=21012720,
        flag_6=21019373,
    )
    Event_21010721(
        0,
        flag=21012731,
        flag_1=21012732,
        flag_2=21012737,
        seconds=2.799999952316284,
        seconds_1=2.799999952316284,
    )
    Event_21010722(
        0,
        attacked_entity=21010720,
        flag=21012738,
        flag_1=21012739,
        flag_2=21019355,
        flag_3=21019356,
        flag_4=4420,
        flag_5=4897,
    )
    Event_21010723(0, flag=4423, flag_1=4891)
    Event_21010724(0, flag=4420, flag_1=21012732, seconds=60.0)
    Event_21010735(0, entity=21010720, flag=21019377, radius=30.0, flag_1=4420, flag_2=4897)
    Event_21010736(0, flag=4420, flag_1=4897, flag_2=21019377, flag_3=21019378, flag_4=21012785, seconds=60.0)
    Event_21010737(0, character=21010720, radius=40.0, radius_1=60.0, flag=4420, flag_1=4897, flag_2=4425)
    CommonFunc_90005747(
        0,
        flag=21012735,
        flag_1=4426,
        flag_2=21012734,
        seconds=5.0,
        flag_3=21012733,
        flag_4=21012736,
        seconds_1=60.0,
    )
    CommonFunc_90005703(
        0,
        character=21010720,
        flag=4421,
        flag_1=4422,
        flag_2=21019351,
        flag_3=4421,
        first_flag=4420,
        last_flag=4424,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=21010720, flag=4421, flag_1=4420, flag_2=21019351, right=3)
    CommonFunc_90005702(0, character=21010720, flag=4423, first_flag=4420, last_flag=4424)
    CommonFunc_90005744(0, entity=21010720, flag=21019370, flag_1=21019370, animation_id=90200)
    CommonFunc_90005744(0, entity=21010720, flag=21012781, flag_1=4897, animation_id=90307)
    CommonFunc_90005750(
        0,
        asset=21011720,
        action_button_id=4350,
        item_lot=106010,
        first_flag=400602,
        last_flag=400602,
        flag=21019373,
        vfx_id=6102,
    )
    Event_21010726(
        0,
        flag=7621,
        flag_1=4403,
        first_flag=4400,
        last_flag=4404,
        flag_2=21019328,
        flag_3=21019314,
        flag_4=4893,
    )
    Event_21010727(0, character=21010735, flag=21012764, flag_1=7621)
    Event_21010729(0, flag=21012748, character=21010730, flag_1=21012746, flag_2=7621)
    Event_21010729(1, flag=21012765, character=21010735, flag_1=21012766, flag_2=7621)
    CommonFunc_90005769(
        0,
        character=21010735,
        flag=21012763,
        character_1=21010730,
        flag_1=21012742,
        flag_2=21012749,
        flag_3=7621,
        flag_4=7622,
    )
    CommonFunc_90005776(0, flag=400622, flag_1=7621, item_lot=106210)
    Event_21010740(0, character=21010735, character_1=21001730, ceremony=40)
    Event_21010727(1, character=21010745, flag=21012755, flag_1=7622)
    Event_21010729(2, flag=21012778, character=21010740, flag_1=21012775, flag_2=7622)
    Event_21010729(3, flag=21012757, character=21010745, flag_1=21012756, flag_2=7622)
    CommonFunc_90005769(
        0,
        character=21010745,
        flag=21012752,
        character_1=21010740,
        flag_1=21012772,
        flag_2=21012759,
        flag_3=7621,
        flag_4=7622,
    )
    CommonFunc_90005776(0, flag=400595, flag_1=7622, item_lot=105930)
    Event_21010740(1, character=21010745, character_1=21001740, ceremony=50)
    Event_21010725(0, flag=2048459295, flag_1=2048459298, flag_2=4400)
    Event_21010734(0, flag=21012805, flag_1=2048459284)
    Event_21010707(0, character=21010770, flag=21010800, character_1=21010800, flag_1=21019205)
    CommonFunc_90005715(0, character=21010800, character_1=0, flag=21010800, flag_1=21012805, distance=105.0)
    CommonFunc_90005748(0, entity=21011750, action_button_id=206020, text=1030051, display_distance=30.0, flag=4921)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_21010050()


@ContinueOnRest(21010050)
def Event_21010050():
    """Event 21010050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(21010510)
    EnableFlag(21010515)
    EnableFlag(21010572)


@RestartOnRest(21012144)
def Event_21012144():
    """Event 21012144"""
    if CeremonyInactive(ceremony=40):
        return
    DisableHealthBar(21010736)
    DisableFlag(1099002100)
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.Start)
    OR_3.Add(CharacterProportionDead(character=21010735))
    
    MAIN.Await(OR_3)
    
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.NormalFadeOut)


@RestartOnRest(21012154)
def Event_21012154():
    """Event 21012154"""
    if CeremonyInactive(ceremony=50):
        return
    DisableFlag(1099002100)
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.Start)
    OR_3.Add(CharacterProportionDead(character=21010745))
    
    MAIN.Await(OR_3)
    
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.NormalFadeOut)


@RestartOnRest(21012170)
def Event_21012170(_, flag: Flag | int, character: uint, character_1: uint):
    """Event 21012170"""
    AddSpecialEffect(character_1, 20004380)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    if FlagEnabled(flag):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)


@RestartOnRest(21012171)
def Event_21012171(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    copy_draw_parent: uint,
    character: Character | int,
    asset: uint,
    flag_2: Flag | int,
    message: EventText | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 21012171"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    SetTeamType(character, TeamType.NoTeam)
    Wait(1.0)
    CreateAssetVFX(asset, dummy_id=100, vfx_id=30001)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        dummy_id=236,
        copy_draw_parent=copy_draw_parent,
    )
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=209060, entity=asset))
    OR_10.Add(AND_2)
    OR_10.Add(FlagEnabled(flag))
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagDisabled(flag_2))
    OR_10.Add(AND_3)
    
    MAIN.Await(OR_10)
    
    if FlagDisabled(flag_2):
        DeleteAssetVFX(asset, erase_root=False)
        DisableCharacter(character)
        End()
    if FlagEnabled(flag):
        DeleteAssetVFX(asset, erase_root=False)
        DisableCharacter(character)
        End()
    AwaitDialogResponse(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagDisabled(left_flag):
        return RESTART
    DisableCharacter(character)
    DisplayNetworkMessage(text=4080100, unk_4_5=False)
    Wait(1.0)
    EnableNetworkFlag(flag_1)


@RestartOnRest(21012172)
def Event_21012172(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    text: EventText | int,
    text_1: EventText | int,
    animation_id: int,
    asset: Asset | int,
):
    """Event 21012172"""
    if FlagEnabled(flag):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfPlayerNotInOwnWorld(2)
    DisplayNetworkMessage(text=text, unk_4_5=False)
    SkipLinesIfPlayerInOwnWorld(1)
    DisplayNetworkMessage(text=text_1, unk_4_5=False)
    EnableCharacter(character)
    EnableAnimations(character)
    SetBackreadStateAlternate(character, True)
    EnableAI(character)
    DeleteAssetVFX(asset)
    if UnsignedNotEqual(left=21010700, right=character):
        CreateAssetVFX(asset, dummy_id=100, vfx_id=30320)
    EnableInvincibility(character)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    if UnsignedNotEqual(left=21010700, right=character):
        DeleteAssetVFX(asset)
    DisableInvincibility(character)
    EnableNetworkFlag(flag_2)


@RestartOnRest(21012173)
def Event_21012173(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    character: Character | int,
    text: EventText | int,
    text_1: EventText | int,
):
    """Event 21012173"""
    if FlagEnabled(flag):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfPlayerNotInOwnWorld(2)
    DisplayNetworkMessage(text=text, unk_4_5=False)
    SkipLinesIfPlayerInOwnWorld(1)
    DisplayNetworkMessage(text=text_1, unk_4_5=False)
    SetBackreadStateAlternate(character, False)
    DisableNetworkFlag(flag_1)


@RestartOnRest(21012174)
def Event_21012174(_, flag: Flag | int, flag_1: Flag | int, character: uint, right: Flag | int):
    """Event 21012174"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableAI(character)
    SetBackreadStateAlternate(character, False)
    if UnsignedNotEqual(left=0, right=right):
        AND_2.Add(FlagEnabled(right))
    
        MAIN.Await(AND_2)
    Wait(3.0)
    AddSpecialEffect(character, 18677)
    DisableAnimations(character)
    DisableNetworkFlag(flag_1)


@RestartOnRest(21012500)
def Event_21012500():
    """Event 21012500"""
    AND_10.Add(FlagEnabled(21010500))
    OR_10.Add(FlagEnabled(72112))
    OR_10.Add(FlagEnabled(72113))
    AND_10.Add(OR_10)
    GotoIfConditionFalse(Label.L0, input_condition=AND_10)
    ForceAnimation(21011500, 20, skip_transition=True)
    EnableTreasure(asset=21011509)
    DisableAssetActivation(21011501, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(21011500, 10, skip_transition=True)
    DisableTreasure(asset=21011509)
    CreateAssetVFX(21011500, dummy_id=90, vfx_id=6102)
    AND_1.Add(AssetActivated(obj_act_id=21013501))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(21010500)
    DisableAssetActivation(21011501, obj_act_id=-1)
    ForceAnimation(21011500, 12, wait_for_completion=True, skip_transition=True)
    EnableTreasure(asset=21011509)
    DeleteAssetVFX(21011500)


@ContinueOnRest(21012510)
def Event_21012510():
    """Event 21012510"""
    CommonFunc_90005500(
        0,
        flag=21010510,
        flag_1=21010511,
        left=0,
        asset=21011510,
        asset_1=21011511,
        obj_act_id=21013511,
        asset_2=21011512,
        obj_act_id_1=21013512,
        region=21012511,
        region_1=21012512,
        flag_2=21010512,
        flag_3=21010513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21010515,
        flag_1=21010516,
        left=0,
        asset=21011515,
        asset_1=21011516,
        obj_act_id=21013516,
        asset_2=21011517,
        obj_act_id_1=21013517,
        region=21012516,
        region_1=21012517,
        flag_2=21010517,
        flag_3=21010518,
        left_1=0,
    )
    CommonFunc_90005503(
        0,
        flag=21010520,
        flag_1=21010521,
        left=0,
        asset=21011520,
        asset__region=21012521,
        region=21012522,
        region_1=21012523,
        region_2=21012524,
        flag_2=21010522,
        flag_3=0,
        left_1=0,
    )
    CommonFunc_90005503(
        0,
        flag=21010525,
        flag_1=21010526,
        left=0,
        asset=21011525,
        asset__region=21012526,
        region=21012527,
        region_1=21012528,
        region_2=21012529,
        flag_2=21010527,
        flag_3=0,
        left_1=0,
    )
    CommonFunc_90005503(
        0,
        flag=21010530,
        flag_1=21010531,
        left=0,
        asset=21011530,
        asset__region=21012531,
        region=21012532,
        region_1=21012533,
        region_2=21012534,
        flag_2=21010532,
        flag_3=0,
        left_1=0,
    )


@RestartOnRest(21012550)
def Event_21012550():
    """Event 21012550"""
    EnableAssetInvulnerability(21011550)
    EnableAssetInvulnerability(21011551)
    EnableAssetInvulnerability(21011552)


@RestartOnRest(21012570)
def Event_21012570(_, flag: Flag | int, entity: uint, asset: Asset | int, obj_act_id: uint):
    """Event 21012570"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 10, skip_transition=True)
    DisableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, 20, skip_transition=True)
    AND_1.Add(AssetActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    DisableAssetActivation(asset, obj_act_id=-1)
    ForceAnimation(entity, 21, skip_transition=True)


@RestartOnRest(21012576)
def Event_21012576():
    """Event 21012576"""
    GotoIfFlagDisabled(Label.L0, flag=21010576)
    ForceAnimation(21011576, 20, skip_transition=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(21011576, 10, skip_transition=True)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=21012576))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 102334))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    Wait(1.7000000476837158)
    EnableNetworkFlag(21010576)
    ForceAnimation(21011576, 12, skip_transition=True)


@RestartOnRest(21012699)
def Event_21012699():
    """Event 21012699"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4923):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=21012699))
    
    MAIN.Await(AND_1)
    
    EnableFlag(4923)


@RestartOnRest(21012580)
def Event_21012580():
    """Event 21012580"""
    RegisterLadder(start_climbing_flag=21010580, stop_climbing_flag=21010581, asset=21011580)
    RegisterLadder(start_climbing_flag=21010582, stop_climbing_flag=21010583, asset=21011582)
    RegisterLadder(start_climbing_flag=21010584, stop_climbing_flag=21010585, asset=21011584)
    RegisterLadder(start_climbing_flag=21010586, stop_climbing_flag=21010587, asset=21011586)
    RegisterLadder(start_climbing_flag=21010588, stop_climbing_flag=21010589, asset=21011588)


@RestartOnRest(21012800)
def Event_21012800():
    """Event 21012800"""
    if FlagEnabled(21010800):
        return
    
    MAIN.Await(HealthValue(21010800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(21010800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(21010800))
    
    KillBossAndDisplayBanner(character=21010800, banner_type=BannerType.DemigodFelled)
    DisableMapCollision(collision=21013891)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(21010800)
    EnableFlag(9146)
    if PlayerInOwnWorld():
        EnableFlag(61146)
    if FlagEnabled(72120):
        EnableFlag(78901)
    if FlagEnabled(76940):
        EnableFlag(78902)
    if FlagEnabled(76941):
        EnableFlag(78903)
    if FlagEnabled(76942):
        EnableFlag(78904)
    if FlagEnabled(76943):
        EnableFlag(78905)
    if FlagEnabled(76945):
        EnableFlag(78906)


@RestartOnRest(21012810)
def Event_21012810():
    """Event 21012810"""
    GotoIfFlagDisabled(Label.L0, flag=21010800)
    DisableCharacter(21015800)
    DisableAnimations(21015800)
    Kill(21015800)
    DisableMapCollision(collision=21013891)
    EndOfAnimation(asset=21011810, animation_id=0)
    EndOfAnimation(asset=21011811, animation_id=0)
    EndOfAnimation(asset=21011812, animation_id=0)
    EndOfAnimation(asset=21011813, animation_id=0)
    EndOfAnimation(asset=21011814, animation_id=0)
    EndOfAnimation(asset=21011815, animation_id=0)
    EndOfAnimation(asset=21011816, animation_id=0)
    EndOfAnimation(asset=21011817, animation_id=0)
    EndOfAnimation(asset=21011818, animation_id=0)
    EndOfAnimation(asset=21011819, animation_id=0)
    EndOfAnimation(asset=21011820, animation_id=0)
    EndOfAnimation(asset=21011821, animation_id=0)
    EndOfAnimation(asset=21011822, animation_id=0)
    EndOfAnimation(asset=21011823, animation_id=0)
    EndOfAnimation(asset=21011824, animation_id=0)
    EndOfAnimation(asset=21011825, animation_id=0)
    EndOfAnimation(asset=21011826, animation_id=0)
    EndOfAnimation(asset=21011827, animation_id=0)
    EndOfAnimation(asset=21011828, animation_id=0)
    EndOfAnimation(asset=21011829, animation_id=0)
    EndOfAnimation(asset=21011830, animation_id=0)
    EndOfAnimation(asset=21011831, animation_id=0)
    EndOfAnimation(asset=21011832, animation_id=0)
    EndOfAnimation(asset=21011833, animation_id=0)
    EndOfAnimation(asset=21011834, animation_id=0)
    EndOfAnimation(asset=21011835, animation_id=0)
    EndOfAnimation(asset=21011836, animation_id=0)
    EndOfAnimation(asset=21011837, animation_id=0)
    EndOfAnimation(asset=21011838, animation_id=0)
    EndOfAnimation(asset=21011839, animation_id=0)
    EndOfAnimation(asset=21011840, animation_id=0)
    EndOfAnimation(asset=21011841, animation_id=0)
    EndOfAnimation(asset=21011842, animation_id=0)
    EndOfAnimation(asset=21011843, animation_id=0)
    EndOfAnimation(asset=21011844, animation_id=0)
    EndOfAnimation(asset=21011845, animation_id=0)
    EndOfAnimation(asset=21011846, animation_id=0)
    EndOfAnimation(asset=21011847, animation_id=0)
    EndOfAnimation(asset=21011848, animation_id=0)
    EndOfAnimation(asset=21011849, animation_id=0)
    EndOfAnimation(asset=21011850, animation_id=0)
    EndOfAnimation(asset=21011851, animation_id=0)
    EndOfAnimation(asset=21011852, animation_id=0)
    EndOfAnimation(asset=21011853, animation_id=0)
    EndOfAnimation(asset=21011854, animation_id=0)
    EndOfAnimation(asset=21011855, animation_id=0)
    EndOfAnimation(asset=21011856, animation_id=0)
    EndOfAnimation(asset=21011857, animation_id=0)
    EndOfAnimation(asset=21011858, animation_id=0)
    EndOfAnimation(asset=21011859, animation_id=0)
    EndOfAnimation(asset=21011860, animation_id=0)
    EndOfAnimation(asset=21011861, animation_id=0)
    EndOfAnimation(asset=21011862, animation_id=0)
    EndOfAnimation(asset=21011863, animation_id=0)
    EndOfAnimation(asset=21011864, animation_id=0)
    EndOfAnimation(asset=21011865, animation_id=0)
    EndOfAnimation(asset=21011866, animation_id=0)
    EndOfAnimation(asset=21011867, animation_id=0)
    EndOfAnimation(asset=21011868, animation_id=0)
    EndOfAnimation(asset=21011869, animation_id=0)
    EndOfAnimation(asset=21011870, animation_id=0)
    EndOfAnimation(asset=21011871, animation_id=0)
    EndOfAnimation(asset=21011872, animation_id=0)
    EndOfAnimation(asset=21011873, animation_id=0)
    EndOfAnimation(asset=21011874, animation_id=0)
    EndOfAnimation(asset=21011875, animation_id=0)
    EndOfAnimation(asset=21011876, animation_id=0)
    EndOfAnimation(asset=21011877, animation_id=0)
    EndOfAnimation(asset=21011878, animation_id=0)
    EndOfAnimation(asset=21011879, animation_id=0)
    EndOfAnimation(asset=21011880, animation_id=0)
    EndOfAnimation(asset=21011881, animation_id=0)
    EndOfAnimation(asset=21011882, animation_id=0)
    EndOfAnimation(asset=21011883, animation_id=0)
    EndOfAnimation(asset=21011884, animation_id=0)
    EndOfAnimation(asset=21011885, animation_id=0)
    EndOfAnimation(asset=21011886, animation_id=0)
    EndOfAnimation(asset=21011887, animation_id=0)
    EndOfAnimation(asset=21011888, animation_id=0)
    EndOfAnimation(asset=21011889, animation_id=0)
    EndOfAnimation(asset=21011890, animation_id=0)
    EndOfAnimation(asset=21011891, animation_id=0)
    EndOfAnimation(asset=21011892, animation_id=0)
    EndOfAnimation(asset=21011893, animation_id=0)
    EndOfAnimation(asset=21011894, animation_id=0)
    EndOfAnimation(asset=21011895, animation_id=0)
    EndOfAnimation(asset=21011896, animation_id=0)
    EndOfAnimation(asset=21011897, animation_id=0)
    EndOfAnimation(asset=21011898, animation_id=0)
    EndOfAnimation(asset=21011899, animation_id=0)
    EndOfAnimation(asset=21013810, animation_id=0)
    EndOfAnimation(asset=21013811, animation_id=0)
    EndOfAnimation(asset=21013812, animation_id=0)
    EndOfAnimation(asset=21013813, animation_id=0)
    EndOfAnimation(asset=21013814, animation_id=0)
    EndOfAnimation(asset=21013815, animation_id=0)
    EndOfAnimation(asset=21013816, animation_id=0)
    EndOfAnimation(asset=21013817, animation_id=0)
    EndOfAnimation(asset=21013818, animation_id=0)
    EndOfAnimation(asset=21013819, animation_id=0)
    EndOfAnimation(asset=21013820, animation_id=0)
    EndOfAnimation(asset=21013821, animation_id=0)
    EndOfAnimation(asset=21013822, animation_id=0)
    EndOfAnimation(asset=21013823, animation_id=0)
    EndOfAnimation(asset=21013824, animation_id=0)
    EndOfAnimation(asset=21013825, animation_id=0)
    EndOfAnimation(asset=21013826, animation_id=0)
    EndOfAnimation(asset=21013827, animation_id=0)
    EndOfAnimation(asset=21013828, animation_id=0)
    EndOfAnimation(asset=21013829, animation_id=0)
    EndOfAnimation(asset=21013830, animation_id=0)
    EndOfAnimation(asset=21013831, animation_id=0)
    EndOfAnimation(asset=21013832, animation_id=0)
    EndOfAnimation(asset=21013833, animation_id=0)
    EndOfAnimation(asset=21013834, animation_id=0)
    EndOfAnimation(asset=21013835, animation_id=0)
    EndOfAnimation(asset=21013836, animation_id=0)
    EndOfAnimation(asset=21013837, animation_id=0)
    EndOfAnimation(asset=21013838, animation_id=0)
    EndOfAnimation(asset=21013839, animation_id=0)
    EndOfAnimation(asset=21013840, animation_id=0)
    EndOfAnimation(asset=21013841, animation_id=0)
    EndOfAnimation(asset=21013842, animation_id=0)
    EndOfAnimation(asset=21013843, animation_id=0)
    EndOfAnimation(asset=21013844, animation_id=0)
    EndOfAnimation(asset=21013845, animation_id=0)
    EndOfAnimation(asset=21013846, animation_id=0)
    EndOfAnimation(asset=21013847, animation_id=0)
    EndOfAnimation(asset=21013848, animation_id=0)
    EndOfAnimation(asset=21013849, animation_id=0)
    EndOfAnimation(asset=21013850, animation_id=0)
    EndOfAnimation(asset=21013851, animation_id=0)
    EndOfAnimation(asset=21013852, animation_id=0)
    EndOfAnimation(asset=21013853, animation_id=0)
    EndOfAnimation(asset=21013854, animation_id=0)
    EndOfAnimation(asset=21013855, animation_id=0)
    EndOfAnimation(asset=21013856, animation_id=0)
    EndOfAnimation(asset=21013857, animation_id=0)
    EndOfAnimation(asset=21013858, animation_id=0)
    EndOfAnimation(asset=21013859, animation_id=0)
    EndOfAnimation(asset=21013860, animation_id=0)
    EndOfAnimation(asset=21013861, animation_id=0)
    EndOfAnimation(asset=21013862, animation_id=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(21015800)
    DisableMapCollision(collision=21013891)
    DisableGravity(21010800)
    DisableAnimations(21010800)
    DisableHealthBar(21010800)
    EnableImmortality(21010801)
    DisableCharacter(21010810)
    DisableAnimations(21010810)
    EnableImmortality(21010810)
    ReferDamageToEntity(21010810, target_entity=21010800)
    DisableHealthBar(21010810)
    DisableCharacter(21010820)
    DisableAnimations(21010820)
    EnableImmortality(21010820)
    DisableCharacter(21010821)
    DisableAnimations(21010821)
    EnableImmortality(21010821)
    DisableCharacter(21010822)
    DisableAnimations(21010822)
    EnableImmortality(21010822)
    DisableCharacter(21010823)
    DisableAnimations(21010823)
    EnableImmortality(21010823)
    DisableCharacter(21010824)
    DisableAnimations(21010824)
    EnableImmortality(21010824)
    DisableCharacter(21010825)
    DisableAnimations(21010825)
    EnableImmortality(21010825)
    DisableCharacter(21010826)
    DisableAnimations(21010826)
    EnableImmortality(21010826)
    DisableCharacter(21010827)
    DisableAnimations(21010827)
    EnableImmortality(21010827)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(21015800, authority_level=UpdateAuthority.Forced)
    GotoIfFlagEnabled(Label.L1, flag=21010801)
    Move(21010801, destination=21012810, destination_type=CoordEntityType.Region, short_move=True)
    WaitRealFrames(frames=1)
    AddSpecialEffect(21010110, 9531)
    DisableAnimations(21010801)
    SetLockOnPoint(character=21010801, lock_on_dummy_id=220, state=False)
    ForceAnimation(21010801, 30025)
    EndOfAnimation(asset=21011810, animation_id=10)
    EndOfAnimation(asset=21011811, animation_id=10)
    EndOfAnimation(asset=21011812, animation_id=10)
    EndOfAnimation(asset=21011813, animation_id=10)
    EndOfAnimation(asset=21011814, animation_id=10)
    EndOfAnimation(asset=21011815, animation_id=10)
    EndOfAnimation(asset=21011816, animation_id=10)
    EndOfAnimation(asset=21011817, animation_id=10)
    EndOfAnimation(asset=21011818, animation_id=10)
    EndOfAnimation(asset=21011819, animation_id=10)
    EndOfAnimation(asset=21011820, animation_id=10)
    EndOfAnimation(asset=21011821, animation_id=10)
    EndOfAnimation(asset=21011822, animation_id=10)
    EndOfAnimation(asset=21011823, animation_id=10)
    EndOfAnimation(asset=21011824, animation_id=10)
    EndOfAnimation(asset=21011825, animation_id=10)
    EndOfAnimation(asset=21011826, animation_id=10)
    EndOfAnimation(asset=21011827, animation_id=10)
    EndOfAnimation(asset=21011828, animation_id=10)
    EndOfAnimation(asset=21011829, animation_id=10)
    EndOfAnimation(asset=21011830, animation_id=10)
    EndOfAnimation(asset=21011831, animation_id=10)
    EndOfAnimation(asset=21011832, animation_id=10)
    EndOfAnimation(asset=21011833, animation_id=10)
    EndOfAnimation(asset=21011834, animation_id=10)
    EndOfAnimation(asset=21011835, animation_id=10)
    EndOfAnimation(asset=21011836, animation_id=10)
    EndOfAnimation(asset=21011837, animation_id=10)
    EndOfAnimation(asset=21011838, animation_id=10)
    EndOfAnimation(asset=21011839, animation_id=10)
    EndOfAnimation(asset=21011840, animation_id=10)
    EndOfAnimation(asset=21011841, animation_id=10)
    EndOfAnimation(asset=21011842, animation_id=10)
    EndOfAnimation(asset=21011843, animation_id=10)
    EndOfAnimation(asset=21011844, animation_id=10)
    EndOfAnimation(asset=21011845, animation_id=10)
    EndOfAnimation(asset=21011846, animation_id=10)
    EndOfAnimation(asset=21011847, animation_id=10)
    EndOfAnimation(asset=21011848, animation_id=10)
    EndOfAnimation(asset=21011849, animation_id=10)
    EndOfAnimation(asset=21011850, animation_id=10)
    EndOfAnimation(asset=21011851, animation_id=10)
    EndOfAnimation(asset=21011852, animation_id=10)
    EndOfAnimation(asset=21011853, animation_id=10)
    EndOfAnimation(asset=21011854, animation_id=10)
    EndOfAnimation(asset=21011855, animation_id=10)
    EndOfAnimation(asset=21011856, animation_id=10)
    EndOfAnimation(asset=21011857, animation_id=10)
    EndOfAnimation(asset=21011858, animation_id=10)
    EndOfAnimation(asset=21011859, animation_id=10)
    EndOfAnimation(asset=21011860, animation_id=10)
    EndOfAnimation(asset=21011861, animation_id=10)
    EndOfAnimation(asset=21011862, animation_id=10)
    EndOfAnimation(asset=21011863, animation_id=10)
    EndOfAnimation(asset=21011864, animation_id=10)
    EndOfAnimation(asset=21011865, animation_id=10)
    EndOfAnimation(asset=21011866, animation_id=10)
    EndOfAnimation(asset=21011867, animation_id=10)
    EndOfAnimation(asset=21011868, animation_id=10)
    EndOfAnimation(asset=21011869, animation_id=10)
    EndOfAnimation(asset=21011870, animation_id=10)
    EndOfAnimation(asset=21011871, animation_id=10)
    EndOfAnimation(asset=21011872, animation_id=10)
    EndOfAnimation(asset=21011873, animation_id=10)
    EndOfAnimation(asset=21011874, animation_id=10)
    EndOfAnimation(asset=21011875, animation_id=10)
    EndOfAnimation(asset=21011876, animation_id=10)
    EndOfAnimation(asset=21011877, animation_id=10)
    EndOfAnimation(asset=21011878, animation_id=10)
    EndOfAnimation(asset=21011879, animation_id=10)
    EndOfAnimation(asset=21011880, animation_id=10)
    EndOfAnimation(asset=21011881, animation_id=10)
    EndOfAnimation(asset=21011882, animation_id=10)
    EndOfAnimation(asset=21011883, animation_id=10)
    EndOfAnimation(asset=21011884, animation_id=10)
    EndOfAnimation(asset=21011885, animation_id=10)
    EndOfAnimation(asset=21011886, animation_id=10)
    EndOfAnimation(asset=21011887, animation_id=10)
    EndOfAnimation(asset=21011888, animation_id=10)
    EndOfAnimation(asset=21011889, animation_id=10)
    EndOfAnimation(asset=21011890, animation_id=10)
    EndOfAnimation(asset=21011891, animation_id=10)
    EndOfAnimation(asset=21011892, animation_id=10)
    EndOfAnimation(asset=21011893, animation_id=10)
    EndOfAnimation(asset=21011894, animation_id=10)
    EndOfAnimation(asset=21011895, animation_id=10)
    EndOfAnimation(asset=21011896, animation_id=10)
    EndOfAnimation(asset=21011897, animation_id=10)
    EndOfAnimation(asset=21011898, animation_id=10)
    EndOfAnimation(asset=21011899, animation_id=10)
    EndOfAnimation(asset=21013810, animation_id=10)
    EndOfAnimation(asset=21013811, animation_id=10)
    EndOfAnimation(asset=21013812, animation_id=10)
    EndOfAnimation(asset=21013813, animation_id=10)
    EndOfAnimation(asset=21013814, animation_id=10)
    EndOfAnimation(asset=21013815, animation_id=10)
    EndOfAnimation(asset=21013816, animation_id=10)
    EndOfAnimation(asset=21013817, animation_id=10)
    EndOfAnimation(asset=21013818, animation_id=10)
    EndOfAnimation(asset=21013819, animation_id=10)
    EndOfAnimation(asset=21013820, animation_id=10)
    EndOfAnimation(asset=21013821, animation_id=10)
    EndOfAnimation(asset=21013822, animation_id=10)
    EndOfAnimation(asset=21013823, animation_id=10)
    EndOfAnimation(asset=21013824, animation_id=10)
    EndOfAnimation(asset=21013825, animation_id=10)
    EndOfAnimation(asset=21013826, animation_id=10)
    EndOfAnimation(asset=21013827, animation_id=10)
    EndOfAnimation(asset=21013828, animation_id=10)
    EndOfAnimation(asset=21013829, animation_id=10)
    EndOfAnimation(asset=21013830, animation_id=10)
    EndOfAnimation(asset=21013831, animation_id=10)
    EndOfAnimation(asset=21013832, animation_id=10)
    EndOfAnimation(asset=21013833, animation_id=10)
    EndOfAnimation(asset=21013834, animation_id=10)
    EndOfAnimation(asset=21013835, animation_id=10)
    EndOfAnimation(asset=21013836, animation_id=10)
    EndOfAnimation(asset=21013837, animation_id=10)
    EndOfAnimation(asset=21013838, animation_id=10)
    EndOfAnimation(asset=21013839, animation_id=10)
    EndOfAnimation(asset=21013840, animation_id=10)
    EndOfAnimation(asset=21013841, animation_id=10)
    EndOfAnimation(asset=21013842, animation_id=10)
    EndOfAnimation(asset=21013843, animation_id=10)
    EndOfAnimation(asset=21013844, animation_id=10)
    EndOfAnimation(asset=21013845, animation_id=10)
    EndOfAnimation(asset=21013846, animation_id=10)
    EndOfAnimation(asset=21013847, animation_id=10)
    EndOfAnimation(asset=21013848, animation_id=10)
    EndOfAnimation(asset=21013849, animation_id=10)
    EndOfAnimation(asset=21013850, animation_id=10)
    EndOfAnimation(asset=21013851, animation_id=10)
    EndOfAnimation(asset=21013852, animation_id=10)
    EndOfAnimation(asset=21013853, animation_id=10)
    EndOfAnimation(asset=21013854, animation_id=10)
    EndOfAnimation(asset=21013855, animation_id=10)
    EndOfAnimation(asset=21013856, animation_id=10)
    EndOfAnimation(asset=21013857, animation_id=10)
    EndOfAnimation(asset=21013858, animation_id=10)
    EndOfAnimation(asset=21013859, animation_id=10)
    EndOfAnimation(asset=21013860, animation_id=10)
    EndOfAnimation(asset=21013861, animation_id=10)
    EndOfAnimation(asset=21013862, animation_id=10)
    DeleteVFX(21012863, erase_root_only=False)
    DeleteVFX(21012864, erase_root_only=False)
    DeleteVFX(21012865, erase_root_only=False)
    DeleteVFX(21012866, erase_root_only=False)
    DeleteVFX(21012867, erase_root_only=False)
    DeleteVFX(21012868, erase_root_only=False)
    DeleteVFX(21012869, erase_root_only=False)
    DeleteVFX(21012870, erase_root_only=False)
    DeleteVFX(21012871, erase_root_only=False)
    DeleteVFX(21012872, erase_root_only=False)
    DeleteVFX(21012873, erase_root_only=False)
    DeleteVFX(21012874, erase_root_only=False)
    DeleteVFX(21012875, erase_root_only=False)
    DeleteVFX(21012876, erase_root_only=False)
    DeleteVFX(21012877, erase_root_only=False)
    DeleteVFX(21012878, erase_root_only=False)
    DeleteVFX(21012879, erase_root_only=False)
    DeleteVFX(21012880, erase_root_only=False)
    DeleteVFX(21012881, erase_root_only=False)
    DeleteVFX(21012882, erase_root_only=False)
    DeleteVFX(21012883, erase_root_only=False)
    DeleteVFX(21012884, erase_root_only=False)
    DeleteVFX(21012885, erase_root_only=False)
    DeleteVFX(21012886, erase_root_only=False)
    DeleteVFX(21012887, erase_root_only=False)
    DeleteVFX(21012888, erase_root_only=False)
    DeleteVFX(21012889, erase_root_only=False)
    DeleteVFX(21012890, erase_root_only=False)
    DeleteVFX(21012891, erase_root_only=False)
    DeleteVFX(21012892, erase_root_only=False)
    DeleteVFX(21012893, erase_root_only=False)
    DeleteVFX(21012894, erase_root_only=False)
    DeleteVFX(21012895, erase_root_only=False)
    DeleteVFX(21012896, erase_root_only=False)
    DeleteVFX(21012897, erase_root_only=False)
    DeleteVFX(21012898, erase_root_only=False)
    DeleteVFX(21012899, erase_root_only=False)
    GotoIfFlagEnabled(Label.L3, flag=21018542)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=21013542))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=21010801, attacker=PLAYER))
    
    MAIN.Await(OR_1)

    # --- Label 3 --- #
    DefineLabel(3)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=530100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=640100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=641100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=360100))
    OR_10.Add(PlayerHasBodyArmorEquipped(armor=361100))
    SkipLinesIfConditionTrue(3, OR_10)
    EnableFlag(780030)
    DisableFlag(780031)
    SkipLines(2)
    DisableFlag(780030)
    EnableFlag(780031)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=21010000,
            cutscene_flags=0,
            move_to_region=21012811,
            map_id=21010000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(21010000, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    EnableNetworkFlag(21010801)
    DeactivateGparamOverride(change_duration=0.0)
    EndOfAnimation(asset=21011810, animation_id=0)
    EndOfAnimation(asset=21011811, animation_id=0)
    EndOfAnimation(asset=21011812, animation_id=0)
    EndOfAnimation(asset=21011813, animation_id=0)
    EndOfAnimation(asset=21011814, animation_id=0)
    EndOfAnimation(asset=21011815, animation_id=0)
    EndOfAnimation(asset=21011816, animation_id=0)
    EndOfAnimation(asset=21011817, animation_id=0)
    EndOfAnimation(asset=21011818, animation_id=0)
    EndOfAnimation(asset=21011819, animation_id=0)
    EndOfAnimation(asset=21011820, animation_id=0)
    EndOfAnimation(asset=21011821, animation_id=0)
    EndOfAnimation(asset=21011822, animation_id=0)
    EndOfAnimation(asset=21011823, animation_id=0)
    EndOfAnimation(asset=21011824, animation_id=0)
    EndOfAnimation(asset=21011825, animation_id=0)
    EndOfAnimation(asset=21011826, animation_id=0)
    EndOfAnimation(asset=21011827, animation_id=0)
    EndOfAnimation(asset=21011828, animation_id=0)
    EndOfAnimation(asset=21011829, animation_id=0)
    EndOfAnimation(asset=21011830, animation_id=0)
    EndOfAnimation(asset=21011831, animation_id=0)
    EndOfAnimation(asset=21011832, animation_id=0)
    EndOfAnimation(asset=21011833, animation_id=0)
    EndOfAnimation(asset=21011834, animation_id=0)
    EndOfAnimation(asset=21011835, animation_id=0)
    EndOfAnimation(asset=21011836, animation_id=0)
    EndOfAnimation(asset=21011837, animation_id=0)
    EndOfAnimation(asset=21011838, animation_id=0)
    EndOfAnimation(asset=21011839, animation_id=0)
    EndOfAnimation(asset=21011840, animation_id=0)
    EndOfAnimation(asset=21011841, animation_id=0)
    EndOfAnimation(asset=21011842, animation_id=0)
    EndOfAnimation(asset=21011843, animation_id=0)
    EndOfAnimation(asset=21011844, animation_id=0)
    EndOfAnimation(asset=21011845, animation_id=0)
    EndOfAnimation(asset=21011846, animation_id=0)
    EndOfAnimation(asset=21011847, animation_id=0)
    EndOfAnimation(asset=21011848, animation_id=0)
    EndOfAnimation(asset=21011849, animation_id=0)
    EndOfAnimation(asset=21011850, animation_id=0)
    EndOfAnimation(asset=21011851, animation_id=0)
    EndOfAnimation(asset=21011852, animation_id=0)
    EndOfAnimation(asset=21011853, animation_id=0)
    EndOfAnimation(asset=21011854, animation_id=0)
    EndOfAnimation(asset=21011855, animation_id=0)
    EndOfAnimation(asset=21011856, animation_id=0)
    EndOfAnimation(asset=21011857, animation_id=0)
    EndOfAnimation(asset=21011858, animation_id=0)
    EndOfAnimation(asset=21011859, animation_id=0)
    EndOfAnimation(asset=21011860, animation_id=0)
    EndOfAnimation(asset=21011861, animation_id=0)
    EndOfAnimation(asset=21011862, animation_id=0)
    EndOfAnimation(asset=21011863, animation_id=0)
    EndOfAnimation(asset=21011864, animation_id=0)
    EndOfAnimation(asset=21011865, animation_id=0)
    EndOfAnimation(asset=21011866, animation_id=0)
    EndOfAnimation(asset=21011867, animation_id=0)
    EndOfAnimation(asset=21011868, animation_id=0)
    EndOfAnimation(asset=21011869, animation_id=0)
    EndOfAnimation(asset=21011870, animation_id=0)
    EndOfAnimation(asset=21011871, animation_id=0)
    EndOfAnimation(asset=21011872, animation_id=0)
    EndOfAnimation(asset=21011873, animation_id=0)
    EndOfAnimation(asset=21011874, animation_id=0)
    EndOfAnimation(asset=21011875, animation_id=0)
    EndOfAnimation(asset=21011876, animation_id=0)
    EndOfAnimation(asset=21011877, animation_id=0)
    EndOfAnimation(asset=21011878, animation_id=0)
    EndOfAnimation(asset=21011879, animation_id=0)
    EndOfAnimation(asset=21011880, animation_id=0)
    EndOfAnimation(asset=21011881, animation_id=0)
    EndOfAnimation(asset=21011882, animation_id=0)
    EndOfAnimation(asset=21011883, animation_id=0)
    EndOfAnimation(asset=21011884, animation_id=0)
    EndOfAnimation(asset=21011885, animation_id=0)
    EndOfAnimation(asset=21011886, animation_id=0)
    EndOfAnimation(asset=21011887, animation_id=0)
    EndOfAnimation(asset=21011888, animation_id=0)
    EndOfAnimation(asset=21011889, animation_id=0)
    EndOfAnimation(asset=21011890, animation_id=0)
    EndOfAnimation(asset=21011891, animation_id=0)
    EndOfAnimation(asset=21011892, animation_id=0)
    EndOfAnimation(asset=21011893, animation_id=0)
    EndOfAnimation(asset=21011894, animation_id=0)
    EndOfAnimation(asset=21011895, animation_id=0)
    EndOfAnimation(asset=21011896, animation_id=0)
    EndOfAnimation(asset=21011897, animation_id=0)
    EndOfAnimation(asset=21011898, animation_id=0)
    EndOfAnimation(asset=21011899, animation_id=0)
    EndOfAnimation(asset=21013810, animation_id=0)
    EndOfAnimation(asset=21013811, animation_id=0)
    EndOfAnimation(asset=21013812, animation_id=0)
    EndOfAnimation(asset=21013813, animation_id=0)
    EndOfAnimation(asset=21013814, animation_id=0)
    EndOfAnimation(asset=21013815, animation_id=0)
    EndOfAnimation(asset=21013816, animation_id=0)
    EndOfAnimation(asset=21013817, animation_id=0)
    EndOfAnimation(asset=21013818, animation_id=0)
    EndOfAnimation(asset=21013819, animation_id=0)
    EndOfAnimation(asset=21013820, animation_id=0)
    EndOfAnimation(asset=21013821, animation_id=0)
    EndOfAnimation(asset=21013822, animation_id=0)
    EndOfAnimation(asset=21013823, animation_id=0)
    EndOfAnimation(asset=21013824, animation_id=0)
    EndOfAnimation(asset=21013825, animation_id=0)
    EndOfAnimation(asset=21013826, animation_id=0)
    EndOfAnimation(asset=21013827, animation_id=0)
    EndOfAnimation(asset=21013828, animation_id=0)
    EndOfAnimation(asset=21013829, animation_id=0)
    EndOfAnimation(asset=21013830, animation_id=0)
    EndOfAnimation(asset=21013831, animation_id=0)
    EndOfAnimation(asset=21013832, animation_id=0)
    EndOfAnimation(asset=21013833, animation_id=0)
    EndOfAnimation(asset=21013834, animation_id=0)
    EndOfAnimation(asset=21013835, animation_id=0)
    EndOfAnimation(asset=21013836, animation_id=0)
    EndOfAnimation(asset=21013837, animation_id=0)
    EndOfAnimation(asset=21013838, animation_id=0)
    EndOfAnimation(asset=21013839, animation_id=0)
    EndOfAnimation(asset=21013840, animation_id=0)
    EndOfAnimation(asset=21013841, animation_id=0)
    EndOfAnimation(asset=21013842, animation_id=0)
    EndOfAnimation(asset=21013843, animation_id=0)
    EndOfAnimation(asset=21013844, animation_id=0)
    EndOfAnimation(asset=21013845, animation_id=0)
    EndOfAnimation(asset=21013846, animation_id=0)
    EndOfAnimation(asset=21013847, animation_id=0)
    EndOfAnimation(asset=21013848, animation_id=0)
    EndOfAnimation(asset=21013849, animation_id=0)
    EndOfAnimation(asset=21013850, animation_id=0)
    EndOfAnimation(asset=21013851, animation_id=0)
    EndOfAnimation(asset=21013852, animation_id=0)
    EndOfAnimation(asset=21013853, animation_id=0)
    EndOfAnimation(asset=21013854, animation_id=0)
    EndOfAnimation(asset=21013855, animation_id=0)
    EndOfAnimation(asset=21013856, animation_id=0)
    EndOfAnimation(asset=21013857, animation_id=0)
    EndOfAnimation(asset=21013858, animation_id=0)
    EndOfAnimation(asset=21013859, animation_id=0)
    EndOfAnimation(asset=21013860, animation_id=0)
    EndOfAnimation(asset=21013861, animation_id=0)
    EndOfAnimation(asset=21013862, animation_id=0)
    CreateVFX(21012863)
    CreateVFX(21012864)
    CreateVFX(21012865)
    CreateVFX(21012866)
    CreateVFX(21012867)
    CreateVFX(21012868)
    CreateVFX(21012869)
    CreateVFX(21012870)
    CreateVFX(21012871)
    CreateVFX(21012872)
    CreateVFX(21012873)
    CreateVFX(21012874)
    CreateVFX(21012875)
    CreateVFX(21012876)
    CreateVFX(21012877)
    CreateVFX(21012878)
    CreateVFX(21012879)
    CreateVFX(21012880)
    CreateVFX(21012881)
    CreateVFX(21012882)
    CreateVFX(21012883)
    CreateVFX(21012884)
    CreateVFX(21012885)
    CreateVFX(21012886)
    CreateVFX(21012887)
    CreateVFX(21012888)
    CreateVFX(21012889)
    CreateVFX(21012890)
    CreateVFX(21012891)
    CreateVFX(21012892)
    CreateVFX(21012893)
    CreateVFX(21012894)
    CreateVFX(21012895)
    CreateVFX(21012896)
    CreateVFX(21012897)
    CreateVFX(21012898)
    CreateVFX(21012899)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=4.889999866485596, y_angle=166.0)
    EnableAnimations(21010801)
    SetLockOnPoint(character=21010801, lock_on_dummy_id=220, state=True)
    ForceAnimation(21010801, 20025)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(asset=21011810, animation_id=0)
    EndOfAnimation(asset=21011811, animation_id=0)
    EndOfAnimation(asset=21011812, animation_id=0)
    EndOfAnimation(asset=21011813, animation_id=0)
    EndOfAnimation(asset=21011814, animation_id=0)
    EndOfAnimation(asset=21011815, animation_id=0)
    EndOfAnimation(asset=21011816, animation_id=0)
    EndOfAnimation(asset=21011817, animation_id=0)
    EndOfAnimation(asset=21011818, animation_id=0)
    EndOfAnimation(asset=21011819, animation_id=0)
    EndOfAnimation(asset=21011820, animation_id=0)
    EndOfAnimation(asset=21011821, animation_id=0)
    EndOfAnimation(asset=21011822, animation_id=0)
    EndOfAnimation(asset=21011823, animation_id=0)
    EndOfAnimation(asset=21011824, animation_id=0)
    EndOfAnimation(asset=21011825, animation_id=0)
    EndOfAnimation(asset=21011826, animation_id=0)
    EndOfAnimation(asset=21011827, animation_id=0)
    EndOfAnimation(asset=21011828, animation_id=0)
    EndOfAnimation(asset=21011829, animation_id=0)
    EndOfAnimation(asset=21011830, animation_id=0)
    EndOfAnimation(asset=21011831, animation_id=0)
    EndOfAnimation(asset=21011832, animation_id=0)
    EndOfAnimation(asset=21011833, animation_id=0)
    EndOfAnimation(asset=21011834, animation_id=0)
    EndOfAnimation(asset=21011835, animation_id=0)
    EndOfAnimation(asset=21011836, animation_id=0)
    EndOfAnimation(asset=21011837, animation_id=0)
    EndOfAnimation(asset=21011838, animation_id=0)
    EndOfAnimation(asset=21011839, animation_id=0)
    EndOfAnimation(asset=21011840, animation_id=0)
    EndOfAnimation(asset=21011841, animation_id=0)
    EndOfAnimation(asset=21011842, animation_id=0)
    EndOfAnimation(asset=21011843, animation_id=0)
    EndOfAnimation(asset=21011844, animation_id=0)
    EndOfAnimation(asset=21011845, animation_id=0)
    EndOfAnimation(asset=21011846, animation_id=0)
    EndOfAnimation(asset=21011847, animation_id=0)
    EndOfAnimation(asset=21011848, animation_id=0)
    EndOfAnimation(asset=21011849, animation_id=0)
    EndOfAnimation(asset=21011850, animation_id=0)
    EndOfAnimation(asset=21011851, animation_id=0)
    EndOfAnimation(asset=21011852, animation_id=0)
    EndOfAnimation(asset=21011853, animation_id=0)
    EndOfAnimation(asset=21011854, animation_id=0)
    EndOfAnimation(asset=21011855, animation_id=0)
    EndOfAnimation(asset=21011856, animation_id=0)
    EndOfAnimation(asset=21011857, animation_id=0)
    EndOfAnimation(asset=21011858, animation_id=0)
    EndOfAnimation(asset=21011859, animation_id=0)
    EndOfAnimation(asset=21011860, animation_id=0)
    EndOfAnimation(asset=21011861, animation_id=0)
    EndOfAnimation(asset=21011862, animation_id=0)
    EndOfAnimation(asset=21011863, animation_id=0)
    EndOfAnimation(asset=21011864, animation_id=0)
    EndOfAnimation(asset=21011865, animation_id=0)
    EndOfAnimation(asset=21011866, animation_id=0)
    EndOfAnimation(asset=21011867, animation_id=0)
    EndOfAnimation(asset=21011868, animation_id=0)
    EndOfAnimation(asset=21011869, animation_id=0)
    EndOfAnimation(asset=21011870, animation_id=0)
    EndOfAnimation(asset=21011871, animation_id=0)
    EndOfAnimation(asset=21011872, animation_id=0)
    EndOfAnimation(asset=21011873, animation_id=0)
    EndOfAnimation(asset=21011874, animation_id=0)
    EndOfAnimation(asset=21011875, animation_id=0)
    EndOfAnimation(asset=21011876, animation_id=0)
    EndOfAnimation(asset=21011877, animation_id=0)
    EndOfAnimation(asset=21011878, animation_id=0)
    EndOfAnimation(asset=21011879, animation_id=0)
    EndOfAnimation(asset=21011880, animation_id=0)
    EndOfAnimation(asset=21011881, animation_id=0)
    EndOfAnimation(asset=21011882, animation_id=0)
    EndOfAnimation(asset=21011883, animation_id=0)
    EndOfAnimation(asset=21011884, animation_id=0)
    EndOfAnimation(asset=21011885, animation_id=0)
    EndOfAnimation(asset=21011886, animation_id=0)
    EndOfAnimation(asset=21011887, animation_id=0)
    EndOfAnimation(asset=21011888, animation_id=0)
    EndOfAnimation(asset=21011889, animation_id=0)
    EndOfAnimation(asset=21011890, animation_id=0)
    EndOfAnimation(asset=21011891, animation_id=0)
    EndOfAnimation(asset=21011892, animation_id=0)
    EndOfAnimation(asset=21011893, animation_id=0)
    EndOfAnimation(asset=21011894, animation_id=0)
    EndOfAnimation(asset=21011895, animation_id=0)
    EndOfAnimation(asset=21011896, animation_id=0)
    EndOfAnimation(asset=21011897, animation_id=0)
    EndOfAnimation(asset=21011898, animation_id=0)
    EndOfAnimation(asset=21011899, animation_id=0)
    EndOfAnimation(asset=21013810, animation_id=0)
    EndOfAnimation(asset=21013811, animation_id=0)
    EndOfAnimation(asset=21013812, animation_id=0)
    EndOfAnimation(asset=21013813, animation_id=0)
    EndOfAnimation(asset=21013814, animation_id=0)
    EndOfAnimation(asset=21013815, animation_id=0)
    EndOfAnimation(asset=21013816, animation_id=0)
    EndOfAnimation(asset=21013817, animation_id=0)
    EndOfAnimation(asset=21013818, animation_id=0)
    EndOfAnimation(asset=21013819, animation_id=0)
    EndOfAnimation(asset=21013820, animation_id=0)
    EndOfAnimation(asset=21013821, animation_id=0)
    EndOfAnimation(asset=21013822, animation_id=0)
    EndOfAnimation(asset=21013823, animation_id=0)
    EndOfAnimation(asset=21013824, animation_id=0)
    EndOfAnimation(asset=21013825, animation_id=0)
    EndOfAnimation(asset=21013826, animation_id=0)
    EndOfAnimation(asset=21013827, animation_id=0)
    EndOfAnimation(asset=21013828, animation_id=0)
    EndOfAnimation(asset=21013829, animation_id=0)
    EndOfAnimation(asset=21013830, animation_id=0)
    EndOfAnimation(asset=21013831, animation_id=0)
    EndOfAnimation(asset=21013832, animation_id=0)
    EndOfAnimation(asset=21013833, animation_id=0)
    EndOfAnimation(asset=21013834, animation_id=0)
    EndOfAnimation(asset=21013835, animation_id=0)
    EndOfAnimation(asset=21013836, animation_id=0)
    EndOfAnimation(asset=21013837, animation_id=0)
    EndOfAnimation(asset=21013838, animation_id=0)
    EndOfAnimation(asset=21013839, animation_id=0)
    EndOfAnimation(asset=21013840, animation_id=0)
    EndOfAnimation(asset=21013841, animation_id=0)
    EndOfAnimation(asset=21013842, animation_id=0)
    EndOfAnimation(asset=21013843, animation_id=0)
    EndOfAnimation(asset=21013844, animation_id=0)
    EndOfAnimation(asset=21013845, animation_id=0)
    EndOfAnimation(asset=21013846, animation_id=0)
    EndOfAnimation(asset=21013847, animation_id=0)
    EndOfAnimation(asset=21013848, animation_id=0)
    EndOfAnimation(asset=21013849, animation_id=0)
    EndOfAnimation(asset=21013850, animation_id=0)
    EndOfAnimation(asset=21013851, animation_id=0)
    EndOfAnimation(asset=21013852, animation_id=0)
    EndOfAnimation(asset=21013853, animation_id=0)
    EndOfAnimation(asset=21013854, animation_id=0)
    EndOfAnimation(asset=21013855, animation_id=0)
    EndOfAnimation(asset=21013856, animation_id=0)
    EndOfAnimation(asset=21013857, animation_id=0)
    EndOfAnimation(asset=21013858, animation_id=0)
    EndOfAnimation(asset=21013859, animation_id=0)
    EndOfAnimation(asset=21013860, animation_id=0)
    EndOfAnimation(asset=21013861, animation_id=0)
    EndOfAnimation(asset=21013862, animation_id=0)
    CreateVFX(21012863)
    CreateVFX(21012864)
    CreateVFX(21012865)
    CreateVFX(21012866)
    CreateVFX(21012867)
    CreateVFX(21012868)
    CreateVFX(21012869)
    CreateVFX(21012870)
    CreateVFX(21012871)
    CreateVFX(21012872)
    CreateVFX(21012873)
    CreateVFX(21012874)
    CreateVFX(21012875)
    CreateVFX(21012876)
    CreateVFX(21012877)
    CreateVFX(21012878)
    CreateVFX(21012879)
    CreateVFX(21012880)
    CreateVFX(21012881)
    CreateVFX(21012882)
    CreateVFX(21012883)
    CreateVFX(21012884)
    CreateVFX(21012885)
    CreateVFX(21012886)
    CreateVFX(21012887)
    CreateVFX(21012888)
    CreateVFX(21012889)
    CreateVFX(21012890)
    CreateVFX(21012891)
    CreateVFX(21012892)
    CreateVFX(21012893)
    CreateVFX(21012894)
    CreateVFX(21012895)
    CreateVFX(21012896)
    AND_2.Add(FlagEnabled(21012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ReferDamageToEntity(21010801, target_entity=21010800)
    EnableAI(21010801)
    SetNetworkUpdateRate(21010801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(21010110, 9532)
    Wait(0.5)
    EnableBossHealthBar(21010801, name=905130000)


@RestartOnRest(21012811)
def Event_21012811():
    """Event 21012811"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(HealthRatio(21010801) <= 0.5)
    
    MAIN.Await(AND_1)
    
    DisableAnimations(21010801)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=21010010,
            cutscene_flags=0,
            move_to_region=21012816,
            map_id=21010000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(21010010, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    EnableFlag(21012802)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=3.559999942779541, y_angle=165.3699951171875)
    DisableCharacter(21010801)
    EnableCharacter(21010800)
    EnableAI(21010800)
    EnableAnimations(21010800)
    EnableGravity(21010800)
    Move(21010800, destination=21012815, destination_type=CoordEntityType.Region, short_move=True)
    EnableBossHealthBar(21010800, name=905130001)
    SetDisplayMask(21010800, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(21010800, bit_index=11, switch_type=OnOffChange.On)
    SetDisplayMask(21010800, bit_index=12, switch_type=OnOffChange.On)
    SetDisplayMask(21010800, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(21010800, bit_index=21, switch_type=OnOffChange.Off)
    AddSpecialEffect(21010800, 20010612)
    EnableMapCollision(collision=21013891)
    ForceAnimation(21010800, 20003)
    WaitFrames(frames=1)
    ReplanAI(21010800)


@RestartOnRest(21012820)
def Event_21012820(_, special_effect: int, dummy_id: int, animation_id: int):
    """Event 21012820"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(FlagEnabled(21012802))
    AND_1.Add(FlagDisabled(21013820))
    AND_1.Add(CharacterHasSpecialEffect(21010800, special_effect))
    
    MAIN.Await(AND_1)
    
    DisableAnimations(21010800)
    DisableAI(21010800)
    EnableCharacter(21010810)
    EnableAnimations(21010810)
    EnableAI(21010810)
    Move(
        21010810,
        destination=21010800,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=21010800,
    )
    GotoIfCharacterHasSpecialEffect(Label.L0, character=21010800, special_effect=20010652)
    ForceAnimation(21010800, 30010, loop=True)
    ForceAnimation(21010810, animation_id)
    EnableNetworkFlag(21013820)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21012820))
    SkipLinesIfConditionFalse(1, AND_2)
    Move(
        21010810,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        dummy_id=703,
        copy_draw_parent=PLAYER,
    )
    SkipLinesIfConditionTrue(1, AND_2)
    Move(
        21010810,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=PLAYER,
    )
    ForceAnimation(21010800, 30011)
    ForceAnimation(21010810, 3002)
    EnableNetworkFlag(21013820)
    Wait(2.0)
    ForceAnimation(21010800, 30010, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@RestartOnRest(21012825)
def Event_21012825(_, special_effect: int, dummy_id: int, animation_id: int):
    """Event 21012825"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(FlagEnabled(21013820))
    AND_1.Add(CharacterHasSpecialEffect(21010810, special_effect))
    
    MAIN.Await(AND_1)
    
    Move(
        21010800,
        destination=21010810,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=21010810,
    )
    GotoIfCharacterInsideRegion(Label.L0, character=21010800, region=21012825)
    Move(21010800, destination=21012815, destination_type=CoordEntityType.Region, copy_draw_parent=21010800)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAnimations(21010800)
    EnableAI(21010800)
    DisableAnimations(21010810)
    DisableNetworkFlag(21013820)
    ForceAnimation(21010800, animation_id)
    Wait(1.0)
    DisableCharacter(21010810)
    Restart()


@RestartOnRest(21012830)
def Event_21012830(_, special_effect: int, dummy_id: int, animation_id: int, character: uint):
    """Event 21012830"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(FlagEnabled(21012802))
    AND_1.Add(CharacterHasSpecialEffect(21010800, special_effect))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)
    Move(
        character,
        destination=21010800,
        destination_type=CoordEntityType.Character,
        dummy_id=dummy_id,
        copy_draw_parent=21010800,
    )
    ForceAnimation(character, animation_id)
    Restart()


@RestartOnRest(21012836)
def Event_21012836(_, character: uint):
    """Event 21012836"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 20010649))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableAnimations(character)
    Restart()


@RestartOnRest(21012842)
def Event_21012842():
    """Event 21012842"""
    if FlagEnabled(21010800):
        return
    DisableImmortality(21010800)
    AND_1.Add(FlagEnabled(21013820))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(21010800)
    Move(
        21010800,
        destination=21010810,
        destination_type=CoordEntityType.Character,
        dummy_id=40,
        copy_draw_parent=21010810,
    )
    Restart()


@RestartOnRest(21012843)
def Event_21012843(_, special_effect: int, locked_camera_id__normal_camera_id: int, character: Character | int):
    """Event 21012843"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=21010800)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(21012810))
    if PlayerInOwnWorld():
        AND_2.Add(FlagEnabled(21012805))
    else:
        AND_2.Add(FlagEnabled(21012806))
    
    MAIN.Await(AND_2)
    
    ChangeCamera(normal_camera_id=5130, locked_camera_id=5130)
    GotoIfFlagDisabled(Label.L1, flag=21010800)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(FlagEnabled(21010800))
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagDisabled(Label.L2, flag=21010800)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    ChangeCamera(
        normal_camera_id=locked_camera_id__normal_camera_id,
        locked_camera_id=locked_camera_id__normal_camera_id,
    )
    OR_2.Add(FlagEnabled(21010800))
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(21012844)
def Event_21012844():
    """Event 21012844"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=21012844))
    AND_1.Add(FlagEnabled(21012802))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(21010800, 20010635)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=21012844))
    AND_2.Add(FlagEnabled(21012802))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(21010800, 20010636)
    Restart()


@ContinueOnRest(21012845)
def Event_21012845():
    """Event 21012845"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(FlagEnabled(21013820))
    AND_1.Add(AttackedWithDamageType(attacked_entity=21010800, attacker=PLAYER))
    AND_1.Add(HealthValue(21010800) == 1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(21010800, 20010616)


@RestartOnRest(21012846)
def Event_21012846():
    """Event 21012846"""
    if FlagEnabled(21010800):
        return
    AND_1.Add(CharacterInsideRegion(character=21010800, region=21012844))
    AND_1.Add(FlagEnabled(21012802))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(21010800, 20010637)
    AND_2.Add(CharacterOutsideRegion(character=21010800, region=21012844))
    AND_2.Add(FlagEnabled(21012802))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(21010800, 20010638)
    Restart()


@RestartOnRest(21012847)
def Event_21012847():
    """Event 21012847"""
    if FlagEnabled(21010801):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=21012847))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(21010801):
        return
    ActivateGparamOverride(gparam_sub_id=2, change_duration=3.0)
    AND_2.Add(PlayerInOwnWorld())
    OR_2.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=21012847))
    OR_2.Add(FlagEnabled(21010801))
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    if FlagEnabled(21010801):
        return
    DeactivateGparamOverride(change_duration=3.0)
    Restart()


@RestartOnRest(21012848)
def Event_21012848():
    """Event 21012848"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(21010800))
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=21012848))
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(ALL_PLAYERS, 9621)
    Wait(0.10000000149011612)
    OR_2.Add(FlagDisabled(21010800))
    OR_2.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=21012848))
    OR_2.Add(Invasion())
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    RemoveSpecialEffect(ALL_PLAYERS, 9621)
    Restart()


@RestartOnRest(21012849)
def Event_21012849():
    """Event 21012849"""
    CommonFunc_9005800(
        0,
        flag=21010800,
        entity=21011800,
        region=21012800,
        flag_1=21012805,
        character=21015800,
        action_button_id=10000,
        left=21010801,
        region_1=21012801,
    )
    CommonFunc_9005801(
        0,
        flag=21010800,
        entity=21011800,
        region=21012800,
        flag_1=21012805,
        flag_2=21012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=21010800, asset=21011800, vfx_id=5, right=21010801)
    CommonFunc_9005811(0, flag=21010800, asset=21011801, vfx_id=0, right=0)
    CommonFunc_9005822(
        0,
        flag=21010800,
        bgm_boss_conv_param_id=513000,
        flag_1=21012805,
        flag_2=21012806,
        right=0,
        flag_3=21012802,
        left=1,
        left_1=0,
    )


@RestartOnRest(21012920)
def Event_21012920(_, asset: uint, asset_1: uint):
    """Event 21012920"""
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


@RestartOnRest(21010700)
def Event_21010700(
    _,
    character: Character | int,
    flag: Flag | int,
    distance: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds: float,
):
    """Event 21010700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(seconds)
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(flag_1)
    EnableFlag(flag_3)
    End()


@RestartOnRest(21010701)
def Event_21010701(_, character: Character | int, flag: Flag | int, flag_1: Flag | int):
    """Event 21010701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    AND_1.Add(HealthValue(character) != 0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    End()


@RestartOnRest(21010702)
def Event_21010702(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 21010702"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableFlag(flag_3)
    if FlagDisabled(flag_1):
        return
    EnableFlag(flag)
    End()


@RestartOnRest(21010703)
def Event_21010703(
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
    region: Region | int,
):
    """Event 21010703"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_10.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_10.Add(FlagEnabled(21012805))
    
    MAIN.Await(OR_10)
    
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag_10))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(flag_2)
    SkipLines(1)
    DisableFlag(flag_2)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag_4))
    OR_1.Add(FlagEnabled(flag_5))
    AND_2.Add(FlagDisabled(flag_6))
    AND_2.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag_7)
    SkipLines(1)
    DisableFlag(flag_7)
    OR_2.Add(FlagEnabled(flag_8))
    OR_2.Add(FlagEnabled(flag_9))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag_8):
        DisableFlag(flag_7)
    else:
        DisableFlag(flag_2)
    End()


@RestartOnRest(21010704)
def Event_21010704(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int, flag_4: Flag | int):
    """Event 21010704"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagEnabled(flag_3))
    AwaitConditionTrue(AND_1)
    EnableFlag(flag)
    EnableFlag(flag_4)
    End()


@RestartOnRest(21010705)
def Event_21010705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    animation_id_1: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 21010705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_6))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_6))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(7, flag_4)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SkipLinesIfFlagEnabled(2, flag_5)
    ForceAnimation(character, animation_id_1)
    SkipLines(1)
    ForceAnimation(character, animation_id)
    SetTeamType(character, TeamType.NoTeam)
    if FlagEnabled(flag_3):
        DropMandatoryTreasure(character)
    WaitRealFrames(frames=1)
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
    AND_3.Add(FlagDisabled(flag_1))
    AND_3.Add(FlagDisabled(flag_6))
    
    MAIN.Await(not AND_3)
    
    Restart()


@RestartOnRest(21010706)
def Event_21010706(_, flag: Flag | int, flag_1: Flag | int):
    """Event 21010706"""
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag):
        EnableFlag(flag_1)
    End()


@RestartOnRest(21010707)
def Event_21010707(_, character: Character | int, flag: Flag | int, character_1: uint, flag_1: Flag | int):
    """Event 21010707"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    EnableInvincibility(character)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(HealthValue(character_1) <= 0)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag_1):
        EnableNetworkFlag(flag_1)
    EnableCharacter(character)
    WaitRealFrames(frames=1)
    Move(character, destination=character_1, destination_type=CoordEntityType.Character, dummy_id=6, short_move=True)
    Wait(20.0)
    DisableCharacter(character)


@RestartOnRest(21010715)
def Event_21010715(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    animation_id: int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
):
    """Event 21010715"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(FlagEnabled(flag_6))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(flag_6)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L20, flag=flag_12)
    DisableFlag(flag_9)
    AND_6.Add(FlagEnabled(flag_4))
    AND_6.Add(FlagDisabled(flag_5))
    GotoIfConditionTrue(Label.L0, input_condition=AND_6)
    
    MAIN.Await(AND_6)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    AND_1.Add(FlagEnabled(flag_7))
    AND_1.Add(FlagDisabled(flag_8))
    AND_1.Add(FlagEnabled(flag_10))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag_9)
    ForceAnimation(character, animation_id)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    if FlagDisabled(flag_11):
        DropMandatoryTreasure(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_4))
    OR_10.Add(FlagEnabled(flag_5))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(21010716)
def Event_21010716(
    _,
    flag: Flag | int,
    asset: Asset | int,
    character: Character | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 21010716"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag_4):
        return
    MoveAssetToCharacter(asset, character=character, dummy_id=11)
    WaitFrames(frames=2)
    
    MAIN.Await(CharacterDead(character))
    
    if FlagDisabled(flag_3):
        EnableFlag(flag_1)
        End()
    if FlagDisabled(flag_5):
        EnableFlag(flag_2)
        End()
    EnableFlag(flag_1)
    End()


@RestartOnRest(21010720)
def Event_21010720(
    _,
    character: uint,
    flag: Flag | int,
    animation_id: int,
    flag_1: Flag | int,
    first_flag: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    distance: float,
    flag_5: Flag | int,
    last_flag: Flag | int,
    left: uint,
    flag_6: Flag | int,
):
    """Event 21010720"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(first_flag):
        DisableFlag(flag_1)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=first_flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(10, flag_4)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, animation_id)
    WaitRealFrames(frames=1)
    SkipLinesIfUnsignedNotEqual(2, left=left, right=0)
    ResetCharacterPosition(character=character)
    SkipLines(1)
    Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetCharacterTalkRange(character=character, distance=distance)
    AND_5.Add(FlagEnabled(flag_4))
    AND_5.Add(FlagDisabled(flag_5))
    SkipLinesIfConditionFalse(5, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_3)
    DisableCharacter(character)
    DisableBackread(character)
    EnableFlag(flag_6)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(flag_4):
        EnableBackread(character)
        EnableCharacter(character)
        SetTeamType(character, TeamType.HostileNPC)
    WaitRealFrames(frames=1)
    if UnsignedEqual(left=left, right=0):
        ResetCharacterPosition(character=character)
    else:
        Move(character, destination=left, destination_type=CoordEntityType.Region, short_move=True)
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


@RestartOnRest(21010721)
def Event_21010721(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, seconds: float, seconds_1: float):
    """Event 21010721"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_2)
    AND_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_1)
    DisableFlag(flag_2)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag_2)
    
    MAIN.Await(TimeElapsed(seconds=seconds_1))
    
    DisableFlag(flag_2)
    End()


@RestartOnRest(21010722)
def Event_21010722(
    _,
    attacked_entity: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 21010722"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_4):
        return
    if FlagEnabled(flag_5):
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)
    Restart()


@RestartOnRest(21010723)
def Event_21010723(_, flag: Flag | int, flag_1: Flag | int):
    """Event 21010723"""
    if PlayerNotInOwnWorld():
        return
    AwaitFlagEnabled(flag=flag)
    DisableFlag(flag_1)
    End()


@RestartOnRest(21010724)
def Event_21010724(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 21010724"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    AwaitFlagEnabled(flag=flag_1)
    
    MAIN.Await(TimeElapsed(seconds=seconds))
    
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(21010725)
def Event_21010725(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 21010725"""
    if PlayerNotInOwnWorld():
        return
    WaitRealFrames(frames=2)
    DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)


@RestartOnRest(21010726)
def Event_21010726(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 21010726"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)
    EnableNetworkFlag(flag_2)
    DisableNetworkFlag(flag_3)
    DisableNetworkFlag(flag_4)
    SaveRequest()
    EnableFlag(4418)


@RestartOnRest(21010727)
def Event_21010727(_, character: Character | int, flag: Flag | int, flag_1: Flag | int):
    """Event 21010727"""
    WaitFrames(frames=1)
    OR_10.Add(FlagEnabled(flag_1))
    if OR_10:
        return
    AND_4.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_4.Add(CharacterAlive(character))
    
    MAIN.Await(AND_4)
    
    EnableFlag(flag)


@RestartOnRest(21010729)
def Event_21010729(_, flag: Flag | int, character: Character | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 21010729"""
    WaitFrames(frames=1)
    OR_10.Add(FlagEnabled(flag_2))
    if OR_10:
        return
    OR_1.Add(HealthValue(PLAYER) <= 0)
    OR_1.Add(HealthValue(character) <= 0)
    
    MAIN.Await(OR_1)
    
    AND_2.Add(HealthValue(PLAYER) <= 0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    AND_3.Add(HealthValue(character) <= 0)
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_1)


@RestartOnRest(21010734)
def Event_21010734(_, flag: Flag | int, flag_1: Flag | int):
    """Event 21010734"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)


@RestartOnRest(21010735)
def Event_21010735(_, entity: uint, flag: Flag | int, radius: float, flag_1: Flag | int, flag_2: Flag | int):
    """Event 21010735"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    DisableFlag(flag)
    
    MAIN.Await(EntityWithinDistance(entity=entity, other_entity=ALL_PLAYERS, radius=radius))
    
    EnableFlag(flag)
    
    MAIN.Await(EntityBeyondDistance(entity=entity, other_entity=ALL_PLAYERS, radius=radius))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(21010736)
def Event_21010736(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds: float,
):
    """Event 21010736"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        EnableFlag(flag_3)
        EnableFlag(flag_4)
    else:
        DisableFlag(flag_3)
        EnableFlag(flag_4)
        End()
    Wait(seconds)
    DisableFlag(flag_3)
    End()


@RestartOnRest(21010737)
def Event_21010737(
    _,
    character: uint,
    radius: float,
    radius_1: float,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 21010737"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=ALL_PLAYERS, radius=radius))
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=ALL_PLAYERS, radius=radius_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetBackreadStateAlternate(character, True)
    AND_3.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_3)
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SetBackreadStateAlternate(character, False)
    AND_4.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_4)
    
    Restart()


@RestartOnRest(21010740)
def Event_21010740(_, character: Character | int, character_1: Character | int, ceremony: int):
    """Event 21010740"""
    WaitFrames(frames=1)
    if CeremonyInactive(ceremony=ceremony):
        return
    OR_1.Add(HealthValue(character) <= 0)
    OR_1.Add(CharacterDead(character))
    
    MAIN.Await(OR_1)
    
    DisableAI(character_1)
