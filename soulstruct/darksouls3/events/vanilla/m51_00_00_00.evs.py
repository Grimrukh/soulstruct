"""
Ringed City

linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_20005500(0, flag=15100850, bonfire_flag=15100001, character=5100951, obj=5101951)
    RegisterBonfire(bonfire_flag=15100000, obj=5101950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15100002, obj=5101952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15100003, obj=5101953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15100004, obj=5101954, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15100005, obj=5101955, reaction_distance=5.0)
    Event_15105800()
    Event_15105810()
    Event_15105811()
    Event_15105812()
    Event_15105813()
    Event_15105814()
    Event_15105815()
    Event_15105920(
        0,
        value=0,
        value_1=20,
        special_effect_id=9800,
        special_effect_id_1=9801,
        special_effect_id_2=9802,
        special_effect_id_3=9803,
        special_effect_id_4=10000,
        special_effect_id_5=10001,
        special_effect_id_6=10002,
        special_effect_id_7=10003,
    )
    Event_15105920(
        1,
        value=20,
        value_1=30,
        special_effect_id=9810,
        special_effect_id_1=9811,
        special_effect_id_2=9812,
        special_effect_id_3=9813,
        special_effect_id_4=10010,
        special_effect_id_5=10011,
        special_effect_id_6=10012,
        special_effect_id_7=10013,
    )
    Event_15105920(
        2,
        value=30,
        value_1=40,
        special_effect_id=9820,
        special_effect_id_1=9821,
        special_effect_id_2=9822,
        special_effect_id_3=9823,
        special_effect_id_4=10020,
        special_effect_id_5=10021,
        special_effect_id_6=10022,
        special_effect_id_7=10023,
    )
    Event_15105920(
        3,
        value=40,
        value_1=50,
        special_effect_id=9830,
        special_effect_id_1=9831,
        special_effect_id_2=9832,
        special_effect_id_3=9833,
        special_effect_id_4=10030,
        special_effect_id_5=10031,
        special_effect_id_6=10032,
        special_effect_id_7=10033,
    )
    Event_15105920(
        4,
        value=50,
        value_1=60,
        special_effect_id=9840,
        special_effect_id_1=9841,
        special_effect_id_2=9842,
        special_effect_id_3=9843,
        special_effect_id_4=10040,
        special_effect_id_5=10041,
        special_effect_id_6=10042,
        special_effect_id_7=10043,
    )
    Event_15105920(
        5,
        value=60,
        value_1=70,
        special_effect_id=9850,
        special_effect_id_1=9851,
        special_effect_id_2=9852,
        special_effect_id_3=9853,
        special_effect_id_4=10050,
        special_effect_id_5=10051,
        special_effect_id_6=10052,
        special_effect_id_7=10053,
    )
    Event_15105920(
        6,
        value=70,
        value_1=80,
        special_effect_id=9860,
        special_effect_id_1=9861,
        special_effect_id_2=9862,
        special_effect_id_3=9863,
        special_effect_id_4=10060,
        special_effect_id_5=10061,
        special_effect_id_6=10062,
        special_effect_id_7=10063,
    )
    Event_15105920(
        7,
        value=80,
        value_1=90,
        special_effect_id=9870,
        special_effect_id_1=9871,
        special_effect_id_2=9872,
        special_effect_id_3=9873,
        special_effect_id_4=10070,
        special_effect_id_5=10071,
        special_effect_id_6=10072,
        special_effect_id_7=10073,
    )
    Event_15105920(
        8,
        value=90,
        value_1=100,
        special_effect_id=9880,
        special_effect_id_1=9881,
        special_effect_id_2=9882,
        special_effect_id_3=9883,
        special_effect_id_4=10080,
        special_effect_id_5=10081,
        special_effect_id_6=10082,
        special_effect_id_7=10083,
    )
    Event_15105920(
        9,
        value=100,
        value_1=120,
        special_effect_id=9890,
        special_effect_id_1=9891,
        special_effect_id_2=9892,
        special_effect_id_3=9893,
        special_effect_id_4=10090,
        special_effect_id_5=10091,
        special_effect_id_6=10092,
        special_effect_id_7=10093,
    )
    Event_15105920(
        10,
        value=120,
        value_1=150,
        special_effect_id=9900,
        special_effect_id_1=9901,
        special_effect_id_2=9902,
        special_effect_id_3=9903,
        special_effect_id_4=10100,
        special_effect_id_5=10101,
        special_effect_id_6=10102,
        special_effect_id_7=10103,
    )
    Event_15105920(
        11,
        value=150,
        value_1=180,
        special_effect_id=9910,
        special_effect_id_1=9911,
        special_effect_id_2=9912,
        special_effect_id_3=9913,
        special_effect_id_4=10110,
        special_effect_id_5=10111,
        special_effect_id_6=10112,
        special_effect_id_7=10113,
    )
    Event_15105920(
        12,
        value=180,
        value_1=230,
        special_effect_id=9920,
        special_effect_id_1=9921,
        special_effect_id_2=9922,
        special_effect_id_3=9923,
        special_effect_id_4=10120,
        special_effect_id_5=10121,
        special_effect_id_6=10122,
        special_effect_id_7=10123,
    )
    Event_15105920(
        13,
        value=230,
        value_1=280,
        special_effect_id=9930,
        special_effect_id_1=9931,
        special_effect_id_2=9932,
        special_effect_id_3=9933,
        special_effect_id_4=10130,
        special_effect_id_5=10131,
        special_effect_id_6=10132,
        special_effect_id_7=10133,
    )
    Event_15105920(
        14,
        value=280,
        value_1=350,
        special_effect_id=9940,
        special_effect_id_1=9941,
        special_effect_id_2=9942,
        special_effect_id_3=9943,
        special_effect_id_4=10140,
        special_effect_id_5=10141,
        special_effect_id_6=10142,
        special_effect_id_7=10143,
    )
    Event_15105920(
        15,
        value=350,
        value_1=450,
        special_effect_id=9950,
        special_effect_id_1=9951,
        special_effect_id_2=9952,
        special_effect_id_3=9953,
        special_effect_id_4=10150,
        special_effect_id_5=10151,
        special_effect_id_6=10152,
        special_effect_id_7=10153,
    )
    Event_15105920(
        16,
        value=450,
        value_1=600,
        special_effect_id=9960,
        special_effect_id_1=9961,
        special_effect_id_2=9962,
        special_effect_id_3=9963,
        special_effect_id_4=10160,
        special_effect_id_5=10161,
        special_effect_id_6=10162,
        special_effect_id_7=10163,
    )
    Event_15105920(
        17,
        value=600,
        value_1=750,
        special_effect_id=9970,
        special_effect_id_1=9971,
        special_effect_id_2=9972,
        special_effect_id_3=9973,
        special_effect_id_4=10170,
        special_effect_id_5=10171,
        special_effect_id_6=10172,
        special_effect_id_7=10173,
    )
    Event_15105920(
        18,
        value=750,
        value_1=900,
        special_effect_id=9980,
        special_effect_id_1=9981,
        special_effect_id_2=9982,
        special_effect_id_3=9983,
        special_effect_id_4=10180,
        special_effect_id_5=10181,
        special_effect_id_6=10182,
        special_effect_id_7=10183,
    )
    Event_15105940(0, value=0, value_1=20, special_effect_id=10200, special_effect_id_1=10400)
    Event_15105940(1, value=20, value_1=30, special_effect_id=10205, special_effect_id_1=10405)
    Event_15105940(2, value=30, value_1=40, special_effect_id=10210, special_effect_id_1=10410)
    Event_15105940(3, value=40, value_1=50, special_effect_id=10215, special_effect_id_1=10415)
    Event_15105940(4, value=50, value_1=60, special_effect_id=10220, special_effect_id_1=10420)
    Event_15105940(5, value=60, value_1=70, special_effect_id=10225, special_effect_id_1=10425)
    Event_15105940(6, value=70, value_1=80, special_effect_id=10230, special_effect_id_1=10430)
    Event_15105940(7, value=80, value_1=90, special_effect_id=10235, special_effect_id_1=10435)
    Event_15105940(8, value=90, value_1=100, special_effect_id=10240, special_effect_id_1=10440)
    Event_15105940(9, value=100, value_1=120, special_effect_id=10245, special_effect_id_1=10445)
    Event_15105940(10, value=120, value_1=150, special_effect_id=10250, special_effect_id_1=10450)
    Event_15105940(11, value=150, value_1=180, special_effect_id=10255, special_effect_id_1=10455)
    Event_15105940(12, value=180, value_1=230, special_effect_id=10260, special_effect_id_1=10460)
    Event_15105940(13, value=230, value_1=280, special_effect_id=10265, special_effect_id_1=10465)
    Event_15105940(14, value=280, value_1=350, special_effect_id=10270, special_effect_id_1=10470)
    Event_15105940(15, value=350, value_1=450, special_effect_id=10275, special_effect_id_1=10475)
    Event_15105940(16, value=450, value_1=600, special_effect_id=10280, special_effect_id_1=10480)
    Event_15105940(17, value=600, value_1=750, special_effect_id=10285, special_effect_id_1=10485)
    Event_15105940(18, value=750, value_1=900, special_effect_id=10290, special_effect_id_1=10490)
    Event_15105960(0, value=0, value_1=20, special_effect_id=10200, special_effect_id_1=10400, flag=15100724)
    Event_15105960(1, value=20, value_1=30, special_effect_id=10205, special_effect_id_1=10405, flag=15100724)
    Event_15105960(2, value=30, value_1=40, special_effect_id=10210, special_effect_id_1=10410, flag=15100724)
    Event_15105960(3, value=40, value_1=50, special_effect_id=10215, special_effect_id_1=10415, flag=15100724)
    Event_15105960(4, value=50, value_1=60, special_effect_id=10220, special_effect_id_1=10420, flag=15100724)
    Event_15105960(5, value=60, value_1=70, special_effect_id=10225, special_effect_id_1=10425, flag=15100724)
    Event_15105960(6, value=70, value_1=80, special_effect_id=10230, special_effect_id_1=10430, flag=15100724)
    Event_15105960(7, value=80, value_1=90, special_effect_id=10235, special_effect_id_1=10435, flag=15100724)
    Event_15105960(8, value=90, value_1=100, special_effect_id=10240, special_effect_id_1=10440, flag=15100724)
    Event_15105960(9, value=100, value_1=120, special_effect_id=10245, special_effect_id_1=10445, flag=15100724)
    Event_15105960(10, value=120, value_1=150, special_effect_id=10250, special_effect_id_1=10450, flag=15100724)
    Event_15105960(11, value=150, value_1=180, special_effect_id=10255, special_effect_id_1=10455, flag=15100724)
    Event_15105960(12, value=180, value_1=230, special_effect_id=10260, special_effect_id_1=10460, flag=15100724)
    Event_15105960(13, value=230, value_1=280, special_effect_id=10265, special_effect_id_1=10465, flag=15100724)
    Event_15105960(14, value=280, value_1=350, special_effect_id=10270, special_effect_id_1=10470, flag=15100724)
    Event_15105960(15, value=350, value_1=450, special_effect_id=10275, special_effect_id_1=10475, flag=15100724)
    Event_15105960(16, value=450, value_1=600, special_effect_id=10280, special_effect_id_1=10480, flag=15100724)
    Event_15105960(17, value=600, value_1=750, special_effect_id=10285, special_effect_id_1=10485, flag=15100724)
    Event_15105960(18, value=750, value_1=900, special_effect_id=10290, special_effect_id_1=10490, flag=15100724)
    Event_15105820()
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    Event_15105830()
    Event_15105845()
    Event_15105846()
    Event_15105847()
    Event_15105831()
    Event_15105849()
    Event_15105850()
    Event_15105860()
    Event_15105861()
    Event_15105862()
    Event_15105888()
    Event_15105889()
    CommonFunc_20005840(0, other_entity=5101850)
    CommonFunc_20005841(0, other_entity=5101850)
    Event_15105890()
    Event_15105895()
    Event_15105201()
    Event_15105212()
    Event_15105232()
    Event_15105234()
    Event_15105235()
    Event_15105220()
    Event_15105221()
    Event_15105237()
    Event_15105238()
    Event_15105300()
    Event_15105301()
    Event_15105302()
    Event_15105303()
    Event_15105310(0, character=5100300, character_1=5100301)
    Event_15105310(1, character=5100310, character_1=5100311)
    Event_15105310(2, character=5100320, character_1=5100321)
    Event_15105350(
        0,
        flag=15105355,
        special_effect_id=16443,
        seconds=0.0,
        region=5102309,
        region_1=0,
        region_2=0,
        region_3=0,
    )
    Event_15105350(
        1,
        flag=15105356,
        special_effect_id=16444,
        seconds=0.0,
        region=5102325,
        region_1=5102326,
        region_2=0,
        region_3=0,
    )
    Event_15105350(
        2,
        flag=15105357,
        special_effect_id=16443,
        seconds=0.0,
        region=5102309,
        region_1=0,
        region_2=0,
        region_3=0,
    )
    Event_15105350(
        4,
        flag=15105358,
        special_effect_id=16444,
        seconds=0.0,
        region=5102325,
        region_1=5102326,
        region_2=0,
        region_3=0,
    )
    Event_15105340(
        0,
        character=5100300,
        special_effect_id=16288,
        radius=150.0,
        region=5102305,
        region_1=5102306,
        region_2=0,
        region_3=0,
        region_4=0,
    )
    Event_15105340(
        1,
        character=5100310,
        special_effect_id=16403,
        radius=250.0,
        region=5102315,
        region_1=0,
        region_2=0,
        region_3=0,
        region_4=0,
    )
    Event_15105340(
        2,
        character=5100320,
        special_effect_id=16413,
        radius=50.0,
        region=5102325,
        region_1=5102326,
        region_2=5102327,
        region_3=0,
        region_4=0,
    )
    Event_15105305()
    CommonFunc_20005132(0, character=5100310, radius=70.0, region=5102310)
    CommonFunc_20005130(0, character=5100320, radius=30.0, region=5102320)
    CommonFunc_20005351(0, character=5100300, item_lot_param_id=62800110, flag=55100983, seconds=2.799999952316284)
    CommonFunc_20005351(0, character=5100310, item_lot_param_id=62800010, flag=55100982, seconds=2.799999952316284)
    CommonFunc_20005351(0, character=5100320, item_lot_param_id=62800210, flag=55100984, seconds=2.799999952316284)
    CommonFunc_20005351(0, character=5100240, item_lot_param_id=62600230, flag=55100980, seconds=2.0)
    CommonFunc_20005114(0, character=5100242, region=5102242, seconds=1.2000000476837158)
    CommonFunc_20005132(0, character=5100243, radius=3.0, region=5102243)
    CommonFunc_20005132(0, character=5100244, radius=3.0, region=5102243)
    CommonFunc_20005132(0, character=5100245, radius=3.0, region=5102245)
    CommonFunc_20005132(0, character=5100246, radius=10.0, region=5102246)
    CommonFunc_20005119(
        0,
        character=5100247,
        region=5102247,
        region_1=5102248,
        region_2=5102254,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005132(0, character=5100249, radius=8.0, region=5102249)
    CommonFunc_20005132(0, character=5100250, radius=3.0, region=5102250)
    CommonFunc_20005132(0, character=5100251, radius=3.0, region=5102251)
    CommonFunc_20005132(0, character=5100252, radius=3.0, region=5102252)
    CommonFunc_20005132(0, character=5100253, radius=3.0, region=5102253)
    Event_15105460(0, character=5100252, region=5102252, region_1=0, region_2=0, region_3=0, region_4=0)
    Event_15105460(1, character=5100253, region=5102253, region_1=0, region_2=0, region_3=0, region_4=0)
    Event_15105280(
        0,
        character=5100280,
        animation_id=700,
        animation_id_1=1700,
        character_1=5100300,
        seconds=0.0,
        region=5102280,
        region_1=0,
    )
    Event_15105280(
        1,
        character=5100281,
        animation_id=700,
        animation_id_1=1700,
        character_1=5100300,
        seconds=10.0,
        region=5102281,
        region_1=0,
    )
    Event_15105280(
        2,
        character=5100282,
        animation_id=700,
        animation_id_1=1700,
        character_1=5100300,
        seconds=0.0,
        region=5102282,
        region_1=0,
    )
    CommonFunc_20005219(
        0,
        character=5100260,
        animation_id=701,
        animation_id_1=1701,
        radius=3.0,
        region=5102260,
        seconds=7.0,
    )
    CommonFunc_20005132(0, character=5100261, radius=30.0, region=5102261)
    CommonFunc_20005132(0, character=5100263, radius=30.0, region=5102261)
    CommonFunc_20005132(0, character=5100264, radius=30.0, region=5102261)
    CommonFunc_20005219(
        0,
        character=5100265,
        animation_id=701,
        animation_id_1=1701,
        radius=3.0,
        region=5102260,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5100266,
        animation_id=701,
        animation_id_1=1701,
        radius=3.0,
        region=5102260,
        seconds=1.5,
    )
    Event_15105470(0, character=5100260, region=5102269, region_1=0, region_2=0, region_3=0, region_4=0)
    Event_15105470(1, character=5100261, region=5102265, region_1=5102266, region_2=0, region_3=0, region_4=0)
    Event_15105470(
        3,
        character=5100263,
        region=5102265,
        region_1=5102266,
        region_2=5102267,
        region_3=5102268,
        region_4=0,
    )
    Event_15105470(
        4,
        character=5100264,
        region=5102265,
        region_1=5102266,
        region_2=5102267,
        region_3=5102268,
        region_4=0,
    )
    Event_15105470(5, character=5100265, region=5102268, region_1=5102269, region_2=0, region_3=0, region_4=0)
    Event_15105470(6, character=5100266, region=5102268, region_1=5102269, region_2=0, region_3=0, region_4=0)
    CommonFunc_20005202(0, character=5100400, animation_id=707, animation_id_1=20005, region=5102400)
    CommonFunc_20005120(0, character=5100401, radius=3.0)
    CommonFunc_20005205(0, character=5100402, animation_id=704, animation_id_1=1704, region=5102402, seconds=5.0)
    CommonFunc_20005205(0, character=5100403, animation_id=707, animation_id_1=1707, region=5102403, seconds=5.0)
    CommonFunc_20005205(0, character=5100404, animation_id=704, animation_id_1=1704, region=5102403, seconds=0.0)
    CommonFunc_20005111(0, character=5100405, animation_id=20003, region=5102401)
    CommonFunc_20005110(0, character=5100406, region=5102405)
    Event_15105440()
    CommonFunc_20005205(
        0,
        character=5100407,
        animation_id=707,
        animation_id_1=20005,
        region=5102409,
        seconds=0.20000000298023224,
    )
    CommonFunc_20005111(0, character=5100408, animation_id=3006, region=5102404)
    CommonFunc_20005210(0, character=5100409, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005205(0, character=5100410, animation_id=707, animation_id_1=20005, region=5102406, seconds=0.0)
    CommonFunc_20005110(0, character=5100411, region=5102411)
    CommonFunc_20005212(0, character=5100412, animation_id=701, animation_id_1=1701, radius=2.0, region=5102411)
    CommonFunc_20005212(0, character=5100413, animation_id=701, animation_id_1=1701, radius=2.0, region=5102411)
    CommonFunc_20005205(0, character=5100414, animation_id=707, animation_id_1=20005, region=5102412, seconds=3.0)
    CommonFunc_20005134(0, character=5100415, animation_id=3002, radius=1.0, region=5102412)
    CommonFunc_20005227(
        0,
        character=5100416,
        animation_id=701,
        animation_id_1=1701,
        radius=9.800000190734863,
        seconds=2.0,
    )
    CommonFunc_20005134(0, character=5100417, animation_id=3002, radius=1.0, region=5102414)
    CommonFunc_20005134(0, character=5100418, animation_id=3002, radius=3.0, region=5102415)
    CommonFunc_20005217(0, character=5100419, animation_id=703, animation_id_1=20001, radius=5102415.0, region=0)
    CommonFunc_20005213(0, character=5100422, animation_id=701, animation_id_1=1701, radius=1.0, region=5102418)
    CommonFunc_20005221(0, character=5100423, animation_id=701, animation_id_1=1701, radius=6.0)
    CommonFunc_20005207(
        0,
        character=5100424,
        animation_id=703,
        animation_id_1=20001,
        region=5102417,
        seconds=2.0,
        animation_id_2=1704,
        region_1=5102416,
        seconds_1=2.0,
    )
    CommonFunc_20005207(
        0,
        character=5100425,
        animation_id=707,
        animation_id_1=20005,
        region=5102417,
        seconds=3.0,
        animation_id_2=1708,
        region_1=5102416,
        seconds_1=3.0,
    )
    CommonFunc_20005132(0, character=5100426, radius=3.0, region=5102416)
    CommonFunc_20005210(0, character=5100428, animation_id=701, animation_id_1=1701, radius=2.0)
    CommonFunc_20005133(0, character=5100432, animation_id=3002, radius=3.0, region=5102419)
    CommonFunc_20005207(
        0,
        character=5100434,
        animation_id=707,
        animation_id_1=20005,
        region=5102421,
        seconds=0.0,
        animation_id_2=1708,
        region_1=5102428,
        seconds_1=3.0,
    )
    CommonFunc_20005214(0, character=5100435, animation_id=701, animation_id_1=1701, radius=0.5)
    CommonFunc_20005214(0, character=5100436, animation_id=701, animation_id_1=1701, radius=0.5)
    CommonFunc_20005202(0, character=5100437, animation_id=701, animation_id_1=1701, region=5102424)
    CommonFunc_20005202(0, character=5100438, animation_id=707, animation_id_1=20005, region=5102425)
    CommonFunc_20005219(
        0,
        character=5100439,
        animation_id=703,
        animation_id_1=20001,
        radius=2.0,
        region=5102433,
        seconds=0.5,
    )
    CommonFunc_20005119(
        0,
        character=5100440,
        region=5102431,
        region_1=5102432,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005207(
        0,
        character=5100441,
        animation_id=704,
        animation_id_1=20001,
        region=5102426,
        seconds=3.0,
        animation_id_2=1704,
        region_1=5102427,
        seconds_1=0.0,
    )
    CommonFunc_20005215(0, character=5100442, animation_id=707, animation_id_1=1707, radius=1.0, seconds=0.0)
    CommonFunc_20005221(0, character=5100444, animation_id=701, animation_id_1=1701, radius=1.0)
    CommonFunc_20005221(0, character=5100445, animation_id=701, animation_id_1=1701, radius=1.0)
    CommonFunc_20005221(0, character=5100446, animation_id=701, animation_id_1=1701, radius=1.0)
    CommonFunc_20005221(0, character=5100447, animation_id=701, animation_id_1=1701, radius=1.0)
    CommonFunc_20005221(0, character=5100448, animation_id=701, animation_id_1=1701, radius=1.0)
    CommonFunc_20005207(
        0,
        character=5100449,
        animation_id=704,
        animation_id_1=20001,
        region=5102429,
        seconds=3.0,
        animation_id_2=1704,
        region_1=5102430,
        seconds_1=0.0,
    )
    CommonFunc_20005221(0, character=5100461, animation_id=701, animation_id_1=1701, radius=6.0)
    CommonFunc_20005205(0, character=5100462, animation_id=707, animation_id_1=20005, region=5102440, seconds=4.0)
    CommonFunc_20005120(0, character=5100469, radius=25.0)
    CommonFunc_20005119(
        0,
        character=5100501,
        region=5102451,
        region_1=5102454,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005331(0, character=5100501)
    CommonFunc_20005132(0, character=5100502, radius=1.0, region=5102451)
    CommonFunc_20005220(0, character=5100503, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=5100504, animation_id=700, animation_id_1=1700)
    CommonFunc_20005132(0, character=5100506, radius=1.0, region=5102451)
    CommonFunc_20005331(0, character=5100506)
    CommonFunc_20005132(0, character=5100518, radius=8.0, region=5102461)
    CommonFunc_20005219(
        0,
        character=5100514,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5102460,
        seconds=2.0,
    )
    CommonFunc_20005219(
        0,
        character=5100515,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5102460,
        seconds=0.5,
    )
    CommonFunc_20005219(
        0,
        character=5100516,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5102460,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5100517,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5102460,
        seconds=2.0999999046325684,
    )
    CommonFunc_20005331(0, character=5100514)
    CommonFunc_20005331(0, character=5100515)
    CommonFunc_20005331(0, character=5100516)
    CommonFunc_20005331(0, character=5100517)
    CommonFunc_20005210(0, character=5100340, animation_id=704, animation_id_1=1704, radius=4.5)
    CommonFunc_20005210(0, character=5100341, animation_id=701, animation_id_1=1701, radius=14.0)
    CommonFunc_20005221(0, character=5100342, animation_id=702, animation_id_1=1702, radius=12.0)
    CommonFunc_20005221(0, character=5100343, animation_id=702, animation_id_1=1702, radius=14.0)
    CommonFunc_20005201(0, character=5100344, animation_id=702, animation_id_1=1702, region=5102341, seconds=2.5)
    CommonFunc_20005201(0, character=5100345, animation_id=702, animation_id_1=1702, region=5102341, seconds=1.5)
    CommonFunc_20005201(0, character=5100346, animation_id=702, animation_id_1=1702, region=5102341, seconds=5.0)
    CommonFunc_20005201(0, character=5100347, animation_id=702, animation_id_1=1702, region=5102341, seconds=2.0)
    CommonFunc_20005210(0, character=5100348, animation_id=702, animation_id_1=1702, radius=5.0)
    CommonFunc_20005213(0, character=5100349, animation_id=702, animation_id_1=1702, radius=5.0, region=5102346)
    CommonFunc_20005200(0, character=5100350, animation_id=702, animation_id_1=1702, region=5102342)
    CommonFunc_20005210(0, character=5100351, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005210(0, character=5100352, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005210(0, character=5100353, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005222(
        0,
        character=5100354,
        animation_id=704,
        animation_id_1=1704,
        radius=10.0,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005222(
        0,
        character=5100355,
        animation_id=704,
        animation_id_1=1704,
        radius=20.0,
        seconds=2.299999952316284,
    )
    CommonFunc_20005200(0, character=5100357, animation_id=702, animation_id_1=1702, region=5102345)
    CommonFunc_20005213(0, character=5100358, animation_id=702, animation_id_1=1702, radius=4.0, region=5102347)
    CommonFunc_20005221(0, character=5100359, animation_id=702, animation_id_1=1702, radius=10.0)
    CommonFunc_20005120(0, character=5100360, radius=12.0)
    CommonFunc_20005120(0, character=5100361, radius=12.0)
    CommonFunc_20005120(0, character=5100362, radius=12.0)
    CommonFunc_20005201(0, character=5100369, animation_id=702, animation_id_1=1702, region=5102342, seconds=1.0)
    CommonFunc_20005201(0, character=5100370, animation_id=702, animation_id_1=1702, region=5102342, seconds=1.5)
    CommonFunc_20005201(
        0,
        character=5100371,
        animation_id=702,
        animation_id_1=1702,
        region=5102342,
        seconds=0.800000011920929,
    )
    CommonFunc_20005201(0, character=5100372, animation_id=702, animation_id_1=1702, region=5102342, seconds=2.0)
    CommonFunc_20005201(
        0,
        character=5100387,
        animation_id=702,
        animation_id_1=1702,
        region=5102345,
        seconds=0.20000000298023224,
    )
    CommonFunc_20005201(
        0,
        character=5100388,
        animation_id=702,
        animation_id_1=1702,
        region=5102345,
        seconds=0.6000000238418579,
    )
    CommonFunc_20005201(
        0,
        character=5100389,
        animation_id=702,
        animation_id_1=1702,
        region=5102345,
        seconds=0.800000011920929,
    )
    Event_15105420(
        0,
        character=5100390,
        animation_id=702,
        animation_id_1=1702,
        radius=2.0,
        entity=5100358,
        radius_1=4.0,
        seconds=0.699999988079071,
    )
    Event_15105420(
        1,
        character=5100391,
        animation_id=702,
        animation_id_1=1702,
        radius=2.0,
        entity=5100358,
        radius_1=4.0,
        seconds=0.6000000238418579,
    )
    Event_15105420(
        2,
        character=5100392,
        animation_id=702,
        animation_id_1=1702,
        radius=2.0,
        entity=5100358,
        radius_1=4.0,
        seconds=0.800000011920929,
    )
    Event_15105420(
        3,
        character=5100393,
        animation_id=702,
        animation_id_1=1702,
        radius=2.0,
        entity=5100358,
        radius_1=4.0,
        seconds=1.0,
    )
    Event_15105420(
        4,
        character=5100394,
        animation_id=702,
        animation_id_1=1702,
        radius=2.0,
        entity=5100358,
        radius_1=4.0,
        seconds=1.2000000476837158,
    )
    Event_15105360(0, character=5100360, region=5102360)
    Event_15105360(1, character=5100361, region=5102361)
    Event_15105360(2, character=5100362, region=5102362)
    Event_15105360(3, character=5100365, region=5102365)
    Event_15105360(4, character=5100366, region=5102366)
    Event_15105360(5, character=5100367, region=5102367)
    Event_15105360(6, character=5100368, region=5102368)
    Event_15105360(7, character=5100380, region=5102380)
    Event_15105360(8, character=5100383, region=5102383)
    Event_15105360(9, character=5100384, region=5102384)
    Event_15105360(10, character=5100385, region=5102385)
    Event_15105360(11, character=5100386, region=5102386)
    Event_15105380(0, character=5100369, region=5102369, character_1=5100350)
    Event_15105380(1, character=5100370, region=5102370, character_1=5100350)
    Event_15105380(2, character=5100371, region=5102371, character_1=5100350)
    Event_15105380(3, character=5100372, region=5102372, character_1=5100350)
    Event_15105380(4, character=5100387, region=5102387, character_1=5100357)
    Event_15105380(5, character=5100388, region=5102388, character_1=5100357)
    Event_15105380(6, character=5100389, region=5102389, character_1=5100357)
    Event_15105380(7, character=5100390, region=5102390, character_1=5100358)
    Event_15105380(8, character=5100391, region=5102391, character_1=5100358)
    Event_15105380(9, character=5100392, region=5102392, character_1=5100358)
    Event_15105380(10, character=5100393, region=5102393, character_1=5100358)
    Event_15105380(11, character=5100394, region=5102394, character_1=5100358)
    Event_15105400(0, character=5100363, region=5102363, character_1=5100310, special_effect=16447)
    Event_15105400(1, character=5100364, region=5102364, character_1=5100310, special_effect=16447)
    Event_15105400(2, character=5100395, region=5102395, character_1=5100310, special_effect=16447)
    Event_15105400(3, character=5100396, region=5102396, character_1=5100310, special_effect=16447)
    Event_15105400(4, character=5100397, region=5102397, character_1=5100310, special_effect=16447)
    Event_15105400(5, character=5100398, region=5102398, character_1=5100310, special_effect=16447)
    Event_15105400(6, character=5100399, region=5102399, character_1=5100310, special_effect=16447)
    CommonFunc_20005331(0, character=5100373)
    CommonFunc_20005331(0, character=5100374)
    CommonFunc_20005331(0, character=5100375)
    CommonFunc_20005331(0, character=5100376)
    CommonFunc_20005210(0, character=5100550, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005210(0, character=5100551, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005111(0, character=5100552, animation_id=3026, region=5102490)
    CommonFunc_20005210(0, character=5100553, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005210(0, character=5100554, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005221(0, character=5100555, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=5100556, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005221(0, character=5100557, animation_id=700, animation_id_1=1700, radius=13.0)
    CommonFunc_20005342(0, flag=15100285, character=5100285)
    Event_15105450(0, character=5100285, animation_id=700, animation_id_1=1700, radius=45.0)
    CommonFunc_20005400(0, character=5100298)
    CommonFunc_20000343(0, flag=15100298, character=5100298, flag_1=55100985)
    CommonFunc_20005341(0, flag=15100290, character=5100290, item_lot_param_id=21509800)
    CommonFunc_20005341(0, flag=15100291, character=5100291, item_lot_param_id=21509810)
    CommonFunc_20005341(0, flag=15100292, character=5100292, item_lot_param_id=21509820)
    CommonFunc_20005341(0, flag=15100293, character=5100293, item_lot_param_id=21509830)
    CommonFunc_20005341(0, flag=15100294, character=5100294, item_lot_param_id=21509840)
    CommonFunc_20005341(0, flag=15100295, character=5100295, item_lot_param_id=21509850)
    CommonFunc_20005341(0, flag=15100296, character=5100296, item_lot_param_id=21509860)
    CommonFunc_20005132(0, character=5100490, radius=1.0, region=5102454)
    CommonFunc_20005132(0, character=5100491, radius=2.0, region=5102342)
    CommonFunc_20005132(0, character=5100492, radius=2.0, region=5102345)
    Event_15105480(0, character=5100493, radius=2.0, attacked_entity=5100358, radius_1=6.0, seconds=1.0)
    CommonFunc_20005620(0, flag=15100510, flag_1=15101510, entity=5101510, obj=5101511, obj_1=5101512, flag_2=15101511)
    CommonFunc_20005622(0, flag=15100515, flag_1=15101515, entity=5101515, obj=5101516, obj_1=5101517, flag_2=15101516)
    Event_15105510()
    CommonFunc_20005614(0, entity=4501570, flag=64500570)
    CommonFunc_20005610(0, flag=15100610, region=5102610, region_1=5102611)
    CommonFunc_20005611(0, flag=15100610, obj_act_id=5103610, obj=5101610, obj_act_id_1=510310)
    CommonFunc_20005610(0, flag=15100612, region=5102612, region_1=5102613)
    CommonFunc_20005611(0, flag=15100612, obj_act_id=5103612, obj=5101612, obj_act_id_1=510310)
    CommonFunc_20005650(0, flag=15100630, obj=5101630)
    CommonFunc_20005650(0, flag=15100631, obj=5101631)
    CommonFunc_20005650(0, flag=15100632, obj=5101632)
    CommonFunc_20005650(0, flag=15100633, obj=5101633)
    CommonFunc_20005650(0, flag=15100634, obj=5101634)
    Event_15105520(
        0,
        flag=15100520,
        obj=5101520,
        start_climbing_flag=15100521,
        stop_climbing_flag=15100522,
        chameleon_vfx_id=439131,
        region=5102520,
    )
    Event_15105525()
    Event_15105505()
    Event_15105506()
    Event_15105508()
    Event_15105580()
    CommonFunc_20005527(0, flag=55100670, item_lot_param_id=5100670, obj=5101680, left=2, action_button_id=9701)
    CommonFunc_20005527(0, flag=55100900, item_lot_param_id=5100900, obj=5101684, left=1, action_button_id=9701)
    CommonFunc_20005527(0, flag=55100910, item_lot_param_id=5100910, obj=5101685, left=1, action_button_id=9701)
    CommonFunc_20005527(0, flag=55100910, item_lot_param_id=5100920, obj=5101686, left=1, action_button_id=9701)
    Event_15105530()
    CommonFunc_20005701(
        0,
        left=15100850,
        summon_flag=15104190,
        dismissal_flag=15105190,
        character=5100190,
        region=5102190,
        left_1=70000031,
    )
    CommonFunc_20005720(0, flag=15104190, flag_1=15105190, flag_2=15100850, character=5100190)
    CommonFunc_20005716(
        0,
        flag=15104190,
        flag_1=15105855,
        character=5100190,
        region=5102856,
        region_1=5102855,
        flag_2=15105851,
    )
    CommonFunc_20005715(
        0,
        flag=15104190,
        flag_1=15105855,
        character=5100190,
        region=5102856,
        flag_2=15105851,
        region_1=5102857,
        region_2=0,
    )
    Event_15105507(0, character=5100190)
    CommonFunc_20005701(
        0,
        left=15100800,
        summon_flag=15104192,
        dismissal_flag=15105192,
        character=5100192,
        region=5102192,
        left_1=70000030,
    )
    CommonFunc_20005720(0, flag=15104192, flag_1=15105192, flag_2=15100800, character=5100192)
    CommonFunc_20005710(0, flag=15104192, flag_1=15105805, character=5100192, region=5102806, region_1=5102805)
    CommonFunc_20005752(
        0,
        flag=15100890,
        flag_1=15100170,
        summon_flag=15104170,
        dismissal_flag=15105170,
        character=5100170,
        region=5102170,
        region_1=5102171,
        seconds=1.0,
        left=0,
        region_2=5102180,
        region_3=0,
        region_4=0,
    )
    CommonFunc_20005721(0, flag=15104170, flag_1=15105170, flag_2=15100170, character=5100170)
    CommonFunc_20005760(0, flag=15100170, flag_1=15104170, flag_2=15105170, character=5100170)
    CommonFunc_20005341(0, flag=15100170, character=5100170, item_lot_param_id=59600)
    CommonFunc_20005752(
        0,
        flag=15100890,
        flag_1=15100172,
        summon_flag=15104172,
        dismissal_flag=15105172,
        character=5100172,
        region=5102172,
        region_1=5102173,
        seconds=0.0,
        left=0,
        region_2=5102182,
        region_3=5102183,
        region_4=5102184,
    )
    CommonFunc_20005721(0, flag=15104172, flag_1=15105172, flag_2=15100172, character=5100172)
    CommonFunc_20005760(0, flag=15100172, flag_1=15104172, flag_2=15105172, character=5100172)
    CommonFunc_20005341(0, flag=15100172, character=5100172, item_lot_param_id=59700)
    Event_15105490()
    CommonFunc_20005752(
        0,
        flag=15100890,
        flag_1=15100174,
        summon_flag=15104174,
        dismissal_flag=15105174,
        character=5100174,
        region=5102174,
        region_1=5102160,
        seconds=0.0,
        left=0,
        region_2=5102161,
        region_3=5102162,
        region_4=5102163,
    )
    CommonFunc_20005721(0, flag=15104174, flag_1=15105174, flag_2=15100174, character=5100174)
    CommonFunc_20005760(0, flag=15100174, flag_1=15104174, flag_2=15105174, character=5100174)
    CommonFunc_20005341(0, flag=15100174, character=5100174, item_lot_param_id=59800)
    CommonFunc_20006031(0, flag=75100131, region=5102700)
    CommonFunc_20006002(0, character=5100810, flag=1918, first_flag=1915, last_flag=1919)
    Event_15105703(0, character=5100810, flag=15105003, radius=7.0)
    Event_15105704(0, character=5100810)
    Event_15105705(0, character=5100810)
    Event_15105711(0, character=5100705, character_1=5100706, animation_id=91210, obj=5101706, destination=5102707)
    Event_15105712(0, character=5100706, character_1=5100707, animation_id=91150, obj=5101706)
    Event_15105713(0, character=5100707, region=5102705, move_to_region=5102706)
    Event_15105714(0, character=5100705)
    Event_15105715(0, character=5100705)
    Event_15105716(0, entity=5100705)
    Event_15105717(0, character=5100706, obj=5101706)
    CommonFunc_20006002(0, character=5100705, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006002(0, character=5100706, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006002(0, character=5100707, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006000(
        0,
        character=5100705,
        flag=1816,
        flag_1=1817,
        flag_2=75100240,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5100706,
        flag=1816,
        flag_1=1817,
        flag_2=75100241,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5100707,
        flag=1816,
        flag_1=1817,
        flag_2=75100242,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=5100705, flag=1816, flag_1=1817, flag_2=75100240, right=3)
    CommonFunc_20006001(0, attacked_entity=5100706, flag=1816, flag_1=1817, flag_2=75100241, right=3)
    CommonFunc_20006001(0, attacked_entity=5100707, flag=1816, flag_1=1817, flag_2=75100242, right=3)
    CommonFunc_20006030(
        0,
        obj=5101705,
        action_button_id=4000,
        right=2,
        item_lot_param_id=66230,
        first_flag=50006623,
        last_flag=50006624,
        flag=1811,
    )
    CommonFunc_20006040(0, character=5100706, destination=5102707, special_effect=159)
    Event_15105721(0, character=5100710, character_1=5100190)
    Event_15105723()
    Event_15105724()
    CommonFunc_20006002(0, character=5100710, flag=1838, first_flag=1835, last_flag=1839)
    CommonFunc_20006002(0, character=5100715, flag=1898, first_flag=1895, last_flag=1899)
    CommonFunc_20006002(0, character=5100720, flag=1843, first_flag=1840, last_flag=1844)
    CommonFunc_20006002(0, character=5100721, flag=1848, first_flag=1845, last_flag=1849)
    CommonFunc_20006002(0, character=5100722, flag=1853, first_flag=1850, last_flag=1854)
    CommonFunc_20006000(
        0,
        character=5100720,
        flag=1841,
        flag_1=1842,
        flag_2=75000290,
        value=0.6499999761581421,
        first_flag=1840,
        last_flag=1844,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5100721,
        flag=1846,
        flag_1=1847,
        flag_2=75000291,
        value=0.6499999761581421,
        first_flag=1845,
        last_flag=1849,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5100722,
        flag=1851,
        flag_1=1852,
        flag_2=75000292,
        value=0.6499999761581421,
        first_flag=1850,
        last_flag=1854,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=5100720, flag=1841, flag_1=1842, flag_2=75000290, right=3)
    CommonFunc_20006001(0, attacked_entity=5100721, flag=1846, flag_1=1847, flag_2=75000291, right=3)
    CommonFunc_20006001(0, attacked_entity=5100722, flag=1851, flag_1=1852, flag_2=75000292, right=3)
    CommonFunc_20006040(0, character=5100720, destination=5102720, special_effect=159)
    CommonFunc_20006010(0, 75100952, 69003)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_151005100()
    Event_15105848()
    Event_15100519()
    Event_15105200()
    Event_15105500()
    DisableSoundEvent(sound_id=5104801)
    DisableSoundEvent(sound_id=5104802)
    DisableSoundEvent(sound_id=5104851)
    DisableSoundEvent(sound_id=5104852)
    Event_15105309()
    SetMultiplayerBuffs_NonBoss(character=5100200, state=True)
    DisableCharacterCollision(5100200)
    DisableGravity(5100200)
    Event_15105700()
    Event_15105710(
        0,
        character=5100705,
        character_1=5100706,
        character_2=5100707,
        animation_id=91170,
        animation_id_1=91210,
        animation_id_2=91150,
        obj=5101706,
        destination=5102707,
    )
    Event_15105720(0, 5100710, -1)
    Event_15105730(0, 5100715, -1)
    Event_15105740(
        0,
        character=5100720,
        first_flag=1840,
        flag=1841,
        flag_1=1843,
        last_flag=1844,
        flag_2=75000252,
        animation_id=30000,
    )
    Event_15105740(1, 5100721, 1845, 1846, 1848, 1849, 75000262, -1)
    Event_15105740(2, 5100722, 1850, 1851, 1853, 1854, 75000272, -1)
    DisableAnimations(5100790)
    DisableGravity(5100790)
    DisableCharacterCollision(5100790)


@NeverRestart(151005100)
def Event_151005100():
    """Event 151005100"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(9610):
        return
    DisableFlag(15100800)
    DisableFlag(15100801)
    DisableFlagRange((15105800, 15105849))
    DisableFlag(50002341)
    DisableFlagRange((1900, 1919))
    EnableFlag(1900)
    EnableFlag(1915)
    DisableFlag(9610)
    if FlagEnabled(9611):
        return
    DisableFlag(9611)


@RestartOnRest(15105200)
def Event_15105200():
    """Event 15105200"""
    GotoIfFlagDisabled(Label.L0, flag=15100200)
    DisableCharacter(5100200)
    DisableAnimations(5100200)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(5100200)
    DisableGravity(5100200)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100200, authority_level=UpdateAuthority.Forced)
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(InsideMap(game_map=RINGED_CITY))
    
    GotoIfFlagEnabled(Label.L1, flag=15100210)
    ForceAnimation(5100200, 30000, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=15100230)
    AddSpecialEffect(5100200, 5404)
    ForceAnimation(5100200, 30003, loop=True, unknown2=1.0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=5102232))
    GotoIfFlagDisabled(Label.L3, flag=15100234)
    ForceAnimation(5100200, 30002, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(5100200, 30001, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(InsideMap(game_map=RINGED_CITY))
    
    SetNetworkUpdateRate(5100200, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L11, flag=15100210)
    ForceAnimation(5100200, 30000, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkUpdateRate(5100200, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    AND_14.Add(CharacterDoesNotHaveSpecialEffect(5100200, 16559))
    GotoIfConditionTrue(Label.L14, input_condition=AND_14)
    ForceAnimation(5100200, 20002, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkUpdateRate(5100200, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 14 --- #
    DefineLabel(14)
    GotoIfFlagDisabled(Label.L12, flag=15100230)
    AddSpecialEffect(5100200, 5404)
    ForceAnimation(5100200, 30003, loop=True, unknown2=1.0)
    SetNetworkUpdateRate(5100200, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 12 --- #
    DefineLabel(12)
    AND_13.Add(CharacterDoesNotHaveSpecialEffect(5100200, 5027))
    GotoIfConditionTrue(Label.L13, input_condition=AND_13)
    ForceAnimation(5100200, 30002, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkUpdateRate(5100200, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 13 --- #
    DefineLabel(13)
    ForceAnimation(5100200, 30001, loop=True, skip_transition=True, unknown2=1.0)
    SetNetworkUpdateRate(5100200, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()


@NeverRestart(15105201)
def Event_15105201():
    """Event 15105201"""
    Event_15105210()
    Event_15105230()
    Event_15105231()
    Event_15105236()


@RestartOnRest(15105210)
def Event_15105210():
    """Event 15105210"""
    if FlagEnabled(15100200):
        return
    if FlagEnabled(15100210):
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102210))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102211))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(5100200, 5025))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(15100210)
    ForceAnimation(5100200, 20001, wait_for_completion=True, unknown2=1.0)
    ForceAnimation(5100200, 30001, unknown2=1.0)


@RestartOnRest(15105212)
def Event_15105212():
    """Event 15105212"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    if FlagEnabled(15100210):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102212))
    AND_1.Add(FlagDisabled(15100210))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(5100200)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=5102212))
    AND_2.Add(FlagDisabled(15100210))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(5100200, 5026))
    
    MAIN.Await(OR_2)
    
    EnableCharacter(5100200)
    Restart()


@RestartOnRest(15105220)
def Event_15105220():
    """Event 15105220"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(5100200, 5400))
    OR_1.Add(CharacterHasSpecialEffect(5100200, 5405))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102224))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102225))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102226))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102227))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 16556)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(15105221)
def Event_15105221():
    """Event 15105221"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(5100200, 5404))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102220))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5102221))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 16556)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(15105215)
def Event_15105215():
    """Event 15105215"""
    if FlagEnabled(15100200):
        return
    if ThisEventSlotFlagDisabled():
        AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102220))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102221))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102222))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(15105202))
    AND_1.Add(CharacterHasSpecialEffect(5100200, 5026))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(5100200, 20003, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(15105216)
def Event_15105216():
    """Event 15105216"""
    if FlagEnabled(15100200):
        return
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102220))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102221))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(15105202))
    AND_1.Add(CharacterHasSpecialEffect(5100200, 5027))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(5100200, 20005, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(15105230)
def Event_15105230():
    """Event 15105230"""
    if FlagEnabled(15100200):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102230))
    AND_1.Add(CharacterHasSpecialEffect(5100200, 5027))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(5100200, 20011, wait_for_completion=True, unknown2=1.0)
    EnableFlag(15100230)
    Restart()


@RestartOnRest(15105231)
def Event_15105231():
    """Event 15105231"""
    if FlagEnabled(15100200):
        return
    AND_1.Add(HealthRatio(5100200) <= 0.20000000298023224)
    OR_1.Add(AND_1)
    AND_9.Add(OR_1)
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(5100200, 16210))
    
    MAIN.Await(AND_9)
    
    WaitFrames(frames=1)
    ForceAnimation(5100200, 20002, wait_for_completion=True, unknown2=1.0)


@RestartOnRest(15105232)
def Event_15105232():
    """Event 15105232"""
    if FlagEnabled(15100200):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(5100200, 5028))
    
    SetNetworkConnectedFlagState(flag=15100200, state=FlagSetting.On)


@RestartOnRest(15105234)
def Event_15105234():
    """Event 15105234"""
    if FlagEnabled(15100234):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102232))
    
    MAIN.Await(AND_1)
    
    EnableFlag(15100234)


@RestartOnRest(15105235)
def Event_15105235():
    """Event 15105235"""
    DisableNetworkSync()
    if FlagEnabled(15100200):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102235))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=5100200, radius=35.0))
    AND_1.Add(FlagDisabled(15100200))
    AND_1.Add(FlagEnabled(15100230))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=6214, locked_camera_id=6214)
    Wait(0.5)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102235))
    OR_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5100200, radius=35.0))
    OR_1.Add(FlagEnabled(15100200))
    OR_1.Add(FlagDisabled(15100230))
    
    MAIN.Await(OR_1)
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    Restart()


@RestartOnRest(15105236)
def Event_15105236():
    """Event 15105236"""
    if FlagEnabled(15100200):
        return
    AND_1.Add(FlagEnabled(15100230))
    AND_1.Add(CharacterHasSpecialEffect(5100200, 16553))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(15100200))
    
    MAIN.Await(OR_1)
    
    DisableFlag(15100230)
    Restart()


@RestartOnRest(15105237)
def Event_15105237():
    """Event 15105237"""
    if FlagEnabled(15100200):
        return
    AND_1.Add(FlagEnabled(15100230))
    AND_1.Add(CharacterBackreadEnabled(5100200))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(5100200, npc_part_id=10, part_index=NPCPartType.Part1, part_health=99999)
    SetNPCPartEffects(5100850, npc_part_id=10, material_sfx_id=110, material_vfx_id=110)


@RestartOnRest(15105238)
def Event_15105238():
    """Event 15105238"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102223))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(5100200, 16558)
    Wait(1.7999999523162842)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=5102223))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(5100200, 16558)
    Wait(1.7999999523162842)
    Restart()


@RestartOnRest(15105280)
def Event_15105280(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    character_1: int,
    seconds: float,
    region: int,
    region_1: int,
):
    """Event 15105280"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterHasSpecialEffect(character, 5450))
    AND_2.Add(CharacterAlive(character_1))
    AND_2.Add(OR_1)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    Wait(seconds)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_3:
        return
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(15105283)
def Event_15105283(_, character: int, character_1: int, character_2: int, destination: int):
    """Event 15105283"""
    AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16433))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    AND_2.Add(CharacterAlive(character_1))
    if AND_2:
        return RESTART
    MakeEnemyAppear(character=character_2)
    WaitFrames(frames=1)
    EnableGravity(character_1)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Restart()


@NeverRestart(15105300)
def Event_15105300():
    """Event 15105300"""
    Event_15105315(
        0,
        character__region=5100300,
        character=5100301,
        special_effect__special_effect_id=16280,
        special_effect=16288,
    )
    Event_15105320(
        1,
        character=5100300,
        character_1=5100301,
        special_effect__special_effect_id=16282,
        special_effect=16280,
    )
    Event_15105320(
        2,
        character=5100300,
        character_1=5100301,
        special_effect__special_effect_id=16283,
        special_effect=16280,
    )
    Event_15105320(4, character=5100300, character_1=5100301, special_effect__special_effect_id=16285, special_effect=0)
    Event_15105315(
        1,
        character__region=5100310,
        character=5100311,
        special_effect__special_effect_id=16400,
        special_effect=16403,
    )
    Event_15105320(
        6,
        character=5100310,
        character_1=5100311,
        special_effect__special_effect_id=16282,
        special_effect=16400,
    )
    Event_15105320(
        7,
        character=5100310,
        character_1=5100311,
        special_effect__special_effect_id=16283,
        special_effect=16400,
    )
    Event_15105315(
        2,
        character__region=5100320,
        character=5100321,
        special_effect__special_effect_id=16410,
        special_effect=16413,
    )
    Event_15105320(
        11,
        character=5100320,
        character_1=5100321,
        special_effect__special_effect_id=16282,
        special_effect=16410,
    )
    Event_15105320(12, 5100320, 5100321, 16283, 16410)


@RestartOnRest(15105301)
def Event_15105301():
    """Event 15105301"""
    DisableNetworkSync()
    SetNetworkUpdateRate(5100300, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102300))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102301))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102302))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102303))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(5100300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102300))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102301))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102302))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102303))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(15105302)
def Event_15105302():
    """Event 15105302"""
    DisableNetworkSync()
    SetNetworkUpdateRate(5100310, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102310))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102311))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102312))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(5100310, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102310))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102311))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102312))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(15105303)
def Event_15105303():
    """Event 15105303"""
    DisableNetworkSync()
    SetNetworkUpdateRate(5100320, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102321))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102325))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102326))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(5100320, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102321))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102325))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102326))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(15105305)
def Event_15105305():
    """Event 15105305"""
    RemoveSpecialEffect(5100310, 16460)
    AND_1.Add(HasAIStatus(5100310, ai_status=AIStatusType.Battle))
    AND_1.Add(HasAIStatus(5100310, ai_status=AIStatusType.Caution))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(5100310, 16460))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(5100310, 16460)
    AND_2.Add(HasAIStatus(5100310, ai_status=AIStatusType.Normal))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(5100310, 16460))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(15105306)
def Event_15105306(_, character: int, special_effect_id: int, region: int, region_1: int, region_2: int, region_3: int):
    """Event 15105306"""
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_2, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_3)
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    AND_4.Add(AllPlayersOutsideRegion(region=region))
    if ValueNotEqual(left=region_1, right=0):
        AND_4.Add(AllPlayersOutsideRegion(region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        AND_4.Add(AllPlayersOutsideRegion(region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        AND_4.Add(AllPlayersOutsideRegion(region=region_3))
    if AND_4:
        return RESTART
    AddSpecialEffect(character, special_effect_id)
    Wait(5.0)
    Restart()


@RestartOnRest(15105308)
def Event_15105308():
    """Event 15105308"""
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=5102330))
    AND_2.Add(AllPlayersOutsideRegion(region=5102331))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(5100810, 16289)
    Wait(5.0)
    Restart()


@RestartOnRest(15105309)
def Event_15105309():
    """Event 15105309"""
    DisableCharacterCollision(5100300)
    DisableGravity(5100300)
    SetLockOnPoint(character=5100300, lock_on_model_point=221, state=False)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100300, authority_level=UpdateAuthority.Forced)
    DisableCharacterCollision(5100320)
    DisableGravity(5100320)
    SetLockOnPoint(character=5100320, lock_on_model_point=221, state=False)


@RestartOnRest(15105310)
def Event_15105310(_, character: int, character_1: int):
    """Event 15105310"""
    DisableNetworkSync()
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.EveryFiveFrames)
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_2.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(15105315)
def Event_15105315(
    _,
    character__region: int,
    character: int,
    special_effect__special_effect_id: int,
    special_effect: int,
):
    """Event 15105315"""
    RemoveSpecialEffect(PLAYER, special_effect__special_effect_id)
    AND_8.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_8.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_8.Add(AND_8)
    OR_8.Add(CharacterHuman(PLAYER))
    OR_8.Add(CharacterHollow(PLAYER))
    OR_8.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 16443))
    AND_1.Add(CharacterHasSpecialEffect(character, 16450))
    AND_1.Add(CharacterAlive(character__region))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect__special_effect_id))
    AND_2.Add(OR_1)
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 16444))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, special_effect))
    AND_9.Add(AND_2)
    AND_9.Add(OR_3)
    AND_9.Add(OR_8)
    
    MAIN.Await(AND_9)
    
    SetCharacterEventTarget(character, region=character__region)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    Move(
        character,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=260,
        copy_draw_parent=PLAYER,
    )
    Wait(0.800000011920929)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=260,
        copy_draw_parent=character__region,
    )
    WaitFrames(frames=1)
    AddSpecialEffect(character, 16451)
    Wait(7.0)
    AddSpecialEffect(character__region, 16434)
    Restart()


@RestartOnRest(15105320)
def Event_15105320(_, character: int, character_1: int, special_effect__special_effect_id: int, special_effect: int):
    """Event 15105320"""
    RemoveSpecialEffect(character_1, special_effect__special_effect_id)
    if ValueNotEqual(left=special_effect, right=0):
        AND_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect__special_effect_id))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character_1, special_effect__special_effect_id)
    Wait(1.2000000476837158)
    Restart()


@RestartOnRest(15105340)
def Event_15105340(
    _,
    character: int,
    special_effect_id: int,
    radius: float,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
):
    """Event 15105340"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=0, right=region_1):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=0, right=region_2):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=0, right=region_3):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=0, right=region_4):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, special_effect_id)
    Wait(1.600000023841858)
    Restart()


@RestartOnRest(15105350)
def Event_15105350(
    _,
    flag: int,
    special_effect_id: int,
    seconds: float,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
):
    """Event 15105350"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    
    MAIN.Await(OR_1)
    
    OR_2.Add(TimeElapsed(seconds=seconds))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_3))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=AND_2)
    EnableFlag(flag)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, special_effect_id)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=region_3))
    OR_3.Add(AND_3)
    OR_3.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(OR_3)
    
    RestartIfFinishedConditionFalse(input_condition=AND_3)
    DisableFlag(flag)
    Restart()


@RestartOnRest(15105360)
def Event_15105360(_, character: int, region: int):
    """Event 15105360"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 16341)
    SetEventPoint(character, region=region, reaction_range=3.0)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 16341)


@RestartOnRest(15105380)
def Event_15105380(_, character: int, region: int, character_1: int):
    """Event 15105380"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterDead(character_1))

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 16341)
    SetEventPoint(character, region=region, reaction_range=3.0)


@RestartOnRest(15105400)
def Event_15105400(_, character: int, region: int, character_1: int, special_effect: int):
    """Event 15105400"""
    AddSpecialEffect(character, 16348)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasSpecialEffect(character_1, special_effect))
    
    AddSpecialEffect(character, 16349)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 16341)
    SetEventPoint(character, region=region, reaction_range=3.0)


@RestartOnRest(15105420)
def Event_15105420(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    entity: int,
    radius_1: float,
    seconds: float,
):
    """Event 15105420"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterHasSpecialEffect(character, 5450))
    AND_2.Add(EntityWithinDistance(entity=entity, other_entity=character, radius=radius_1))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_3:
        return
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    Wait(seconds)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(15105440)
def Event_15105440():
    """Event 15105440"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character=5100406, region=5102408))

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(5100406, 5000)


@RestartOnRest(15105450)
def Event_15105450(_, character: int, animation_id: int, animation_id_1: int, radius: float):
    """Event 15105450"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)


@RestartOnRest(15105460)
def Event_15105460(_, character: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 15105460"""
    DisableNetworkSync()
    AND_9.Add(CharacterDead(character))
    if AND_9:
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterDead(character))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(15105470)
def Event_15105470(_, character: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 15105470"""
    DisableNetworkSync()
    AND_9.Add(CharacterDead(character))
    if AND_9:
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.5)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterDead(character))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(0.30000001192092896)
    Restart()


@RestartOnRest(15105480)
def Event_15105480(_, character: int, radius: float, attacked_entity: int, radius_1: float, seconds: float):
    """Event 15105480"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(EntityWithinDistance(entity=attacked_entity, other_entity=character, radius=radius_1))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(Attacked(attacked_entity=attacked_entity, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(15105490)
def Event_15105490():
    """Event 15105490"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(15104172))
    AND_1.Add(FlagDisabled(15105172))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102185))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(5100172, ai_param_id=22240)
    if ThisEventSlotFlagDisabled():
        ReplanAI(5100172)


@RestartOnRest(15105500)
def Event_15105500():
    """Event 15105500"""
    GotoIfFlagDisabled(Label.L0, flag=15100500)
    DisableCharacter(5100890)
    DisableAnimations(5100890)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(5100890)
    DisableCharacterCollision(5100890)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9390, entity=5100890))
    
    MAIN.Await(AND_1)
    
    EnableFlag(15100500)
    EnableFlag(15110001)
    SetRespawnPoint(respawn_point=5112110)
    SaveRequest()
    PlayCutscene(51010000, cutscene_flags=0, player_id=10000, move_to_region=5112110, game_map=(51, 1))
    WaitFrames(frames=1)


@RestartOnRest(15105505)
def Event_15105505():
    """Event 15105505"""
    if FlagEnabled(15100200):
        return
    if PlayerNotInOwnWorld():
        return
    Wait(0.5)
    EnableObject(5101850)
    CreateObjectVFX(5101850, vfx_id=101, model_point=2)
    
    MAIN.Await(FlagEnabled(15100200))
    
    DisableObject(5101850)
    DeleteObjectVFX(5101850)


@RestartOnRest(15105506)
def Event_15105506():
    """Event 15105506"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102852))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4050)
    AddSpecialEffect(PLAYER, 4070)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=5102852))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 4050)
    RemoveSpecialEffect(PLAYER, 4070)
    Restart()


@RestartOnRest(15105507)
def Event_15105507(_, character: int):
    """Event 15105507"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=character, region=5102852))
    
    AddSpecialEffect(character, 4050)
    AddSpecialEffect(character, 4070)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=5102852))
    
    RemoveSpecialEffect(character, 4050)
    RemoveSpecialEffect(character, 4070)
    Restart()


@RestartOnRest(15105508)
def Event_15105508():
    """Event 15105508"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5102853))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4520)
    Wait(0.800000011920929)
    Restart()


@NeverRestart(15105510)
def Event_15105510():
    """Event 15105510"""
    CommonFunc_20005621(
        0,
        flag=15100510,
        flag_1=15101510,
        obj=5101510,
        obj_1=5101511,
        obj_act_id=5103511,
        obj_2=5101512,
        obj_act_id_1=5103512,
        region=5102511,
        region_1=5102512,
        flag_2=15101511,
        flag_3=15104510,
        left=0,
    )
    CommonFunc_20005623(
        0,
        15100515,
        15101515,
        5101515,
        5101516,
        5103516,
        5101517,
        5103517,
        5102516,
        5102517,
        15101516,
        15104515,
        0,
    )


@RestartOnRest(15100519)
def Event_15100519():
    """Event 15100519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(15100510)
    EnableFlag(15100515)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)


@RestartOnRest(15105520)
def Event_15105520(
    _,
    flag: int,
    obj: int,
    start_climbing_flag: int,
    stop_climbing_flag: int,
    chameleon_vfx_id: int,
    region: int,
):
    """Event 15105520"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterChameleonState(character=PLAYER, chameleon_vfx_id=chameleon_vfx_id, is_transformed=True))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    ForceAnimation(obj, 1, wait_for_completion=True, unknown2=1.0)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)


@RestartOnRest(15105525)
def Event_15105525():
    """Event 15105525"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(15100520))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9391, entity=5101525))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10012810, anchor_entity=5101525, number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


@RestartOnRest(15105530)
def Event_15105530():
    """Event 15105530"""
    GotoIfPlayerInOwnWorld(Label.L0)
    DisableObject(5101393)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(InsideMap(game_map=DREG_HEAP))
    
    DisableObject(5101300)
    EnableObject(5101393)
    
    MAIN.Await(InsideMap(game_map=RINGED_CITY))
    
    EnableObject(5101300)
    DisableObject(5101393)
    Restart()


@RestartOnRest(15105580)
def Event_15105580():
    """Event 15105580"""
    RegisterLadder(start_climbing_flag=15100580, stop_climbing_flag=15100581, obj=5101580)
    RegisterLadder(start_climbing_flag=15100582, stop_climbing_flag=15100583, obj=5101582)
    RegisterLadder(start_climbing_flag=15100584, stop_climbing_flag=15100585, obj=5101584)
    RegisterLadder(start_climbing_flag=15100586, stop_climbing_flag=15100587, obj=5101586)
    RegisterLadder(start_climbing_flag=15100588, stop_climbing_flag=15100589, obj=5101588)
    RegisterLadder(start_climbing_flag=15100590, stop_climbing_flag=15100591, obj=5101590)
    RegisterLadder(start_climbing_flag=15100592, stop_climbing_flag=15100593, obj=5101592)
    RegisterLadder(start_climbing_flag=15100594, stop_climbing_flag=15100595, obj=5101594)
    RegisterLadder(start_climbing_flag=15100596, stop_climbing_flag=15100597, obj=5101596)
    RegisterLadder(start_climbing_flag=15100598, stop_climbing_flag=15100599, obj=5101598)


@RestartOnRest(15105800)
def Event_15105800():
    """Event 15105800"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(FlagDisabled(2100))
    AND_1.Add(FlagEnabled(15104830))
    AND_2.Add(FlagEnabled(2100))
    AND_2.Add(HealthRatio(5100800) == 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    Kill(5100801)
    Kill(5100803)
    Kill(5100804)
    Wait(2.0)
    PlaySoundEffect(5100800, 777777777, sound_type=SoundType.s_SFX)
    Wait(1.0)
    HandleBossDefeatAndDisplayBanner(boss=5100800, banner=BannerType.HeirOfFireDestroyed)
    EnableFlag(15100800)
    EnableFlag(6325)
    EnableFlag(9325)


@RestartOnRest(15105810)
def Event_15105810():
    """Event 15105810"""
    GotoIfFlagDisabled(Label.L0, flag=15100800)
    DisableCharacter(5100800)
    DisableAnimations(5100800)
    Kill(5100800)
    DisableCharacter(5100801)
    DisableAnimations(5100801)
    Kill(5100801)
    DisableCharacter(5100810)
    DisableAnimations(5100810)
    Kill(5100810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=5100810, distance=100.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100810, authority_level=UpdateAuthority.Forced)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    AND_1.Add(FlagEnabled(15105805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102800))
    
    MAIN.Await(AND_1)
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    EnableFlag(15100801)
    if PlayerNotInOwnWorld():
        return
    Wait(46.0)
    SetNetworkConnectedFlagState(flag=9600, state=FlagSetting.On)


@RestartOnRest(15105811)
def Event_15105811():
    """Event 15105811"""
    if FlagEnabled(15100800):
        return
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    ActivateMultiplayerBuffs(5100801)
    SetNetworkUpdateRate(5100801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableCharacter(5100801)
    DisableAnimations(5100801)
    DisableAI(5100801)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100801, authority_level=UpdateAuthority.Forced)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(75100132))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(5100801)
    EnableAnimations(5100801)
    CreateTemporaryVFX(vfx_id=30340, anchor_entity=5100801, model_point=236, anchor_type=CoordEntityType.Character)
    ForceAnimation(5100801, 63010, unknown2=1.0)
    EnableAI(5100801)

    # --- Label 1 --- #
    DefineLabel(1)
    ActivateMultiplayerBuffs(5100801)
    SetNetworkUpdateRate(5100801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkConnectedFlagState(flag=15105811, state=FlagSetting.On)
    Wait(15.0)
    Kill(5100810, award_souls=True)
    EnableFlag(15104811)
    End()


@RestartOnRest(15105812)
def Event_15105812():
    """Event 15105812"""
    if FlagEnabled(15100800):
        return
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNetworkUpdateRate(5100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableHealthBar(5100800)
    EnableBossHealthBar(5100800, name=906022)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(5100800)
    DisableAnimations(5100800)
    DisableAI(5100800)
    DisableHealthBar(5100800)
    AND_1.Add(FlagEnabled(15104811))
    AND_1.Add(FlagEnabled(2100))
    AND_1.Add(FlagDisabled(15100800))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100800, authority_level=UpdateAuthority.Forced)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=30340, anchor_entity=5100800, model_point=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(5100800)
    EnableAnimations(5100800)
    SetNetworkUpdateRate(5100800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5100800, 63010, unknown2=1.0)
    GotoIfPlayerNotInOwnWorld(Label.L9)
    AND_4.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=3))
    GotoIfConditionTrue(Label.L14, input_condition=AND_4)
    AND_3.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=2))
    GotoIfConditionTrue(Label.L13, input_condition=AND_3)
    AND_2.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=1))
    GotoIfConditionTrue(Label.L12, input_condition=AND_2)
    Goto(Label.L11)

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(5100800, 9150)
    Goto(Label.L9)

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(5100800, 9160)
    Goto(Label.L9)

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(5100800, 9170)
    Goto(Label.L9)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(5100800, 9180)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    if FlagEnabled(15104830):
        AddSpecialEffect(5100800, 17000)
        Goto(Label.L1)
    if FlagEnabled(15104831):
        AddSpecialEffect(5100800, 17001)
        Goto(Label.L1)
    if FlagEnabled(15104832):
        AddSpecialEffect(5100800, 17002)
        Goto(Label.L1)
    if FlagEnabled(15104833):
        AddSpecialEffect(5100800, 17003)
        Goto(Label.L1)
    if FlagEnabled(15104834):
        AddSpecialEffect(5100800, 17004)
        Goto(Label.L1)
    if FlagEnabled(15104835):
        AddSpecialEffect(5100800, 17005)
        Goto(Label.L1)
    if FlagEnabled(15104836):
        AddSpecialEffect(5100800, 17006)
        Goto(Label.L1)
    if FlagEnabled(15104837):
        AddSpecialEffect(5100800, 17007)
        Goto(Label.L1)
    if FlagEnabled(15104838):
        AddSpecialEffect(5100800, 17008)
        Goto(Label.L1)
    if FlagEnabled(15104839):
        AddSpecialEffect(5100800, 17009)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    RemoveSpecialEffect(5100800, 17010)
    SetCharacterEventTarget(5100801, region=5100800)
    SetCharacterEventTarget(5100803, region=5100800)
    SetCharacterEventTarget(5100804, region=5100800)
    EnableBossHealthBar(5100800, name=45000)
    EnableAI(5100800)
    AddSpecialEffect(5100800, 9130)
    EnableFlag(15105804)
    Wait(2.0)
    EnableFlag(15105807)
    End()


@RestartOnRest(15105813)
def Event_15105813():
    """Event 15105813"""
    DisableNetworkSync()
    if FlagEnabled(15100800):
        return
    if FlagEnabled(2100):
        return
    AND_1.Add(CharacterAlive(30000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(15105804)
    SetCharacterEventTarget(5100801, region=30000)
    AddSpecialEffect(30000, 9130)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=15105803, state=FlagSetting.On)
    Wait(2.0)
    EnableBossHealthBar(30000, name=900218)
    EnableFlag(15105807)


@RestartOnRest(15105814)
def Event_15105814():
    """Event 15105814"""
    GotoIfFlagDisabled(Label.L0, flag=15100800)
    DisableCharacter(5100803)
    DisableAnimations(5100803)
    Kill(5100803)
    DisableCharacter(5100804)
    DisableAnimations(5100804)
    Kill(5100804)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(5100803)
    DisableAnimations(5100803)
    DisableAI(5100803)
    DisableCharacter(5100804)
    DisableAnimations(5100804)
    DisableAI(5100804)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100803, authority_level=UpdateAuthority.Forced)
    OR_1.Add(HealthRatio(30000) <= 0.6499999761581421)
    OR_1.Add(HealthRatio(5100800) <= 0.6499999761581421)
    
    MAIN.Await(OR_1)
    
    EnableFlag(15105802)
    Wait(2.4000000953674316)
    CreateTemporaryVFX(vfx_id=30340, anchor_entity=5100803, model_point=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(5100803)
    EnableAnimations(5100803)
    ForceAnimation(5100803, 63010, unknown2=1.0)
    EnableAI(5100803)
    ActivateMultiplayerBuffs(5100803)
    SetNetworkUpdateRate(5100803, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkUpdateAuthority(5100803, authority_level=UpdateAuthority.Forced)
    if FlagDisabled(2100):
        SetCharacterEventTarget(5100803, region=30000)
    else:
        SetCharacterEventTarget(5100803, region=5100800)
    AND_4.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=3))
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    AND_3.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=2))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_2.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=1))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    End()

    # --- Label 3 --- #
    DefineLabel(3)

    # --- Label 4 --- #
    DefineLabel(4)
    End()


@RestartOnRest(15105815)
def Event_15105815():
    """Event 15105815"""
    DisableNetworkSync()
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterAlive(30000))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9110))
    
    MAIN.Await(AND_1)
    
    AND_4.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=3))
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    AND_3.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=2))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_2.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=1))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(30000, 9150)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(30000, 9160)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(30000, 9170)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    AddSpecialEffect(30000, 9180)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    AddSpecialEffect(30000, 100)


@RestartOnRest(15105920)
def Event_15105920(
    _,
    value: uint,
    value_1: uint,
    special_effect_id: int,
    special_effect_id_1: int,
    special_effect_id_2: int,
    special_effect_id_3: int,
    special_effect_id_4: int,
    special_effect_id_5: int,
    special_effect_id_6: int,
    special_effect_id_7: int,
):
    """Event 15105920"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(FlagEnabled(15105807))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerLevel() > value)
    AND_1.Add(PlayerLevel() <= value_1)
    
    MAIN.Await(AND_1)
    
    AND_4.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=3))
    GotoIfConditionTrue(Label.L4, input_condition=AND_4)
    AND_3.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=2))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)
    AND_2.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.Equal, value=1))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(15105808):
        AddSpecialEffect(5100800, special_effect_id_4)
        AddSpecialEffect(30000, special_effect_id_4)
        Goto(Label.L9)
    AddSpecialEffect(5100800, special_effect_id)
    AddSpecialEffect(30000, special_effect_id)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(15105808):
        AddSpecialEffect(5100800, special_effect_id_5)
        AddSpecialEffect(30000, special_effect_id_5)
        Goto(Label.L9)
    AddSpecialEffect(5100800, special_effect_id_1)
    AddSpecialEffect(30000, special_effect_id_1)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    if FlagEnabled(15105808):
        AddSpecialEffect(5100800, special_effect_id_6)
        AddSpecialEffect(30000, special_effect_id_6)
        Goto(Label.L9)
    AddSpecialEffect(5100800, special_effect_id_2)
    AddSpecialEffect(30000, special_effect_id_2)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagEnabled(15105808):
        AddSpecialEffect(5100800, special_effect_id_7)
        AddSpecialEffect(30000, special_effect_id_7)
        Goto(Label.L9)
    AddSpecialEffect(5100800, special_effect_id_3)
    AddSpecialEffect(30000, special_effect_id_3)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)


@RestartOnRest(15105820)
def Event_15105820():
    """Event 15105820"""
    DisableNetworkSync()
    if FlagEnabled(15100800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerStandingOnCollision(5104810))
    AND_1.Add(FlagDisabled(15105803))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 9020)
    Wait(0.800000011920929)
    Restart()


@RestartOnRest(15105830)
def Event_15105830():
    """Event 15105830"""
    if FlagEnabled(15100800):
        return
    SetNetworkConnectedFlagState(flag=15104830, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104831, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104832, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104833, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104834, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104835, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104836, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104837, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104838, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=15104839, state=FlagSetting.Off)
    if ThisEventSlotFlagDisabled():
        AND_15.Add(HealthRatio(30000) > 0.8999999761581421)
    AND_15.Add(FlagEnabled(15105803))
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    OR_9.Add(HealthRatio(30000) <= 0.8999999761581421)
    
    MAIN.Await(OR_9)
    
    AND_9.Add(HealthRatio(30000) == 1.0)
    if AND_9:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104839, state=FlagSetting.On)
    OR_8.Add(HealthRatio(30000) > 0.8999999761581421)
    OR_8.Add(HealthRatio(30000) <= 0.800000011920929)
    
    MAIN.Await(OR_8)
    
    AND_8.Add(HealthRatio(30000) > 0.8999999761581421)
    if AND_8:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104838, state=FlagSetting.On)
    OR_7.Add(HealthRatio(30000) > 0.800000011920929)
    OR_7.Add(HealthRatio(30000) <= 0.699999988079071)
    
    MAIN.Await(OR_7)
    
    AND_7.Add(HealthRatio(30000) > 0.800000011920929)
    if AND_7:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104837, state=FlagSetting.On)
    OR_6.Add(HealthRatio(30000) > 0.699999988079071)
    OR_6.Add(HealthRatio(30000) <= 0.6000000238418579)
    
    MAIN.Await(OR_6)
    
    AND_6.Add(HealthRatio(30000) > 0.699999988079071)
    if AND_6:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104836, state=FlagSetting.On)
    OR_5.Add(HealthRatio(30000) > 0.6000000238418579)
    OR_5.Add(HealthRatio(30000) <= 0.5)
    
    MAIN.Await(OR_5)
    
    AND_5.Add(HealthRatio(30000) > 0.6000000238418579)
    if AND_5:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104835, state=FlagSetting.On)
    OR_4.Add(HealthRatio(30000) > 0.5)
    OR_4.Add(HealthRatio(30000) <= 0.4000000059604645)
    
    MAIN.Await(OR_4)
    
    AND_4.Add(HealthRatio(30000) > 0.5)
    if AND_4:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104834, state=FlagSetting.On)
    OR_3.Add(HealthRatio(30000) > 0.4000000059604645)
    OR_3.Add(HealthRatio(30000) <= 0.30000001192092896)
    
    MAIN.Await(OR_3)
    
    AND_3.Add(HealthRatio(30000) > 0.4000000059604645)
    if AND_3:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104833, state=FlagSetting.On)
    OR_2.Add(HealthRatio(30000) > 0.30000001192092896)
    OR_2.Add(HealthRatio(30000) <= 0.20000000298023224)
    
    MAIN.Await(OR_2)
    
    AND_2.Add(HealthRatio(30000) > 0.30000001192092896)
    if AND_2:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104832, state=FlagSetting.On)
    OR_1.Add(HealthRatio(30000) > 0.20000000298023224)
    OR_1.Add(HealthRatio(30000) <= 0.10000000149011612)
    
    MAIN.Await(OR_1)
    
    AND_1.Add(HealthRatio(30000) > 0.20000000298023224)
    if AND_1:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104831, state=FlagSetting.On)
    OR_10.Add(HealthRatio(30000) > 0.10000000149011612)
    OR_10.Add(CharacterDead(30000))
    
    MAIN.Await(OR_10)
    
    AND_10.Add(HealthRatio(30000) > 0.10000000149011612)
    if AND_10:
        return RESTART
    SetNetworkConnectedFlagState(flag=15104830, state=FlagSetting.On)
    End()


@RestartOnRest(15105831)
def Event_15105831():
    """Event 15105831"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(15105805))
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=15105831, state=FlagSetting.On)
    WaitFrames(frames=1)


@RestartOnRest(15105940)
def Event_15105940(_, value: uint, value_1: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 15105940"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(CharacterAlive(30000))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerLevel() > value)
    AND_1.Add(PlayerLevel() <= value_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=15105809)
    AddSpecialEffect(30000, special_effect_id)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(30000, special_effect_id_1)
    End()


@RestartOnRest(15105960)
def Event_15105960(_, value: uint, value_1: uint, special_effect_id: int, special_effect_id_1: int, flag: int):
    """Event 15105960"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(FlagEnabled(2100))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerLevel() > value)
    AND_1.Add(PlayerLevel() <= value_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AddSpecialEffect(5100800, special_effect_id)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(5100800, special_effect_id_1)
    AddSpecialEffect(5100800, 18010)
    End()


@RestartOnRest(15105844)
def Event_15105844(_, flag: int, sound_id: int, sound_id_1: int, flag_1: int, flag_2: int):
    """Event 15105844"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterAlive(30000))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9110))
    if not AND_1:
        return
    AND_2.Add(PlayerNotInOwnWorld())
    AND_2.Add(CharacterAlive(30000))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 9110))
    
    MAIN.Await(AND_2)
    
    EnableBossMusic(sound_id=sound_id)
    Unknown_2010_07(sound_id=sound_id_1)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    EnableBossMusic(sound_id=sound_id_1)
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(15105845)
def Event_15105845():
    """Event 15105845"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterAlive(30000))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9110))
    AND_1.Add(FlagEnabled(6831))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=15105808, state=FlagSetting.On)


@RestartOnRest(15105846)
def Event_15105846():
    """Event 15105846"""
    if FlagEnabled(15100800):
        return
    AND_1.Add(PlayerNotInOwnWorld())
    AND_1.Add(CharacterAlive(30000))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9110))
    AND_1.Add(PlayerHasGood(651))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=15105809, state=FlagSetting.On)


@RestartOnRest(15105847)
def Event_15105847():
    """Event 15105847"""
    if FlagEnabled(15100800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(15105805))
    
    MAIN.Await(AND_1)
    
    Wait(20.0)
    SetNetworkConnectedFlagState(flag=2101, state=FlagSetting.On)


@RestartOnRest(15105848)
def Event_15105848():
    """Event 15105848"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(Offline())
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(SteamConnectionState(is_disconnected=True))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L0, flag=2110)
    DisableFlag(2100)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(2101)
    DisableFlag(9600)


@RestartOnRest(15105849)
def Event_15105849():
    """Event 15105849"""
    CommonFunc_20005800(
        0,
        flag=15100800,
        entity=5101800,
        region=5102800,
        flag_1=15105805,
        action_button_id=5101800,
        character=5105800,
        left=0,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=15100800,
        entity=5101800,
        region=5102800,
        flag_1=15105805,
        action_button_id=5101800,
        flag_2=15105806,
    )
    if FlagDisabled(15100801):
        CommonFunc_20001836(
            0,
            flag=15100800,
            flag_1=15105805,
            flag_2=15105806,
            flag_3=15105811,
            sound_id=5104801,
            sound_id_1=5104802,
            flag_4=15105802,
        )
    else:
        CommonFunc_20001836(
            0,
            flag=15100800,
            flag_1=15105805,
            flag_2=15105806,
            flag_3=15105811,
            sound_id=5104801,
            sound_id_1=5104802,
            flag_4=15105802,
        )
    Event_15105844(0, flag=15100800, sound_id=5104801, sound_id_1=5104802, flag_1=15105802, flag_2=15105831)
    CommonFunc_20005820(0, flag=15100800, obj=5101800, model_point=4, left=0)
    CommonFunc_20005820(0, flag=15100800, obj=5101801, model_point=2, left=0)
    CommonFunc_20005820(0, flag=15100800, obj=5101802, model_point=2, left=0)
    CommonFunc_20005810(0, 15100890, 5101800, 5102800, 10000)


@RestartOnRest(15105850)
def Event_15105850():
    """Event 15105850"""
    if FlagEnabled(15100850):
        return
    AND_1.Add(HealthRatio(5100850) == 0.0)
    
    MAIN.Await(AND_1)
    
    Wait(5.5)
    PlaySoundEffect(5100850, 777777777, sound_type=SoundType.s_SFX)
    Wait(1.5)
    HandleBossDefeatAndDisplayBanner(boss=5100850, banner=BannerType.HeirOfFireDestroyed)
    EnableFlag(15100850)
    EnableFlag(6326)
    EnableFlag(9326)


@RestartOnRest(15105860)
def Event_15105860():
    """Event 15105860"""
    GotoIfFlagDisabled(Label.L0, flag=15100850)
    DisableCharacter(5100850)
    DisableAnimations(5100850)
    Kill(5100850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(5100850)
    ForceAnimation(5100850, 700, loop=True, unknown2=1.0)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=15105851)
    if FlagDisabled(15100851):
        AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=5100850, radius=36.0))
    else:
        AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=5100850, radius=120.0))
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=5102851))
    OR_1.Add(AND_9)
    OR_1.Add(HealthRatio(5100850) <= 0.8999999761581421)
    
    MAIN.Await(OR_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(15105855))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5102850))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    BanishInvaders(unknown=0)
    ForceAnimation(5100850, 1700, unknown2=1.0)
    EnableAI(5100850)
    SetNetworkUpdateRate(5100850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(5100850, name=906210)
    EnableFlag(15105851)
    EnableFlag(15100851)
    Wait(6.0)
    EnableFlag(15105853)


@RestartOnRest(15105861)
def Event_15105861():
    """Event 15105861"""
    if FlagEnabled(15100850):
        return
    AND_1.Add(CharacterHasSpecialEffect(5100850, 16581))
    
    MAIN.Await(AND_1)
    
    EnableFlag(15105852)


@RestartOnRest(15105862)
def Event_15105862():
    """Event 15105862"""
    if FlagEnabled(15100850):
        return
    AND_1.Add(CharacterBackreadEnabled(5100850))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(5100850, 16583))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(5100850, npc_part_id=10, part_index=NPCPartType.Part1, part_health=1024)
    SetNPCPartEffects(5100850, npc_part_id=10, material_sfx_id=110, material_vfx_id=110)
    OR_1.Add(CharacterPartHealth(5100850, npc_part_id=10) <= 0)
    AND_2.Add(OR_1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(5100850, 16583))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)
    ForceAnimation(5100850, 20000, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(15105888)
def Event_15105888():
    """Event 15105888"""
    if FlagEnabled(15100850):
        return
    if FlagEnabled(15100851):
        return
    AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=5100850, radius=120.0))
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=5102851))
    
    MAIN.Await(AND_9)
    
    BanishInvaders(unknown=0)


@RestartOnRest(15105889)
def Event_15105889():
    """Event 15105889"""
    CommonFunc_20005800(
        0,
        flag=15100850,
        entity=5101850,
        region=5102850,
        flag_1=15105855,
        action_button_id=5101850,
        character=5105850,
        left=15105851,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=15100850,
        entity=5101850,
        region=5102850,
        flag_1=15105855,
        action_button_id=5101850,
        flag_2=15105856,
    )
    if FlagDisabled(15105851):
        CommonFunc_20001836(
            0,
            flag=15100850,
            flag_1=15105855,
            flag_2=15105856,
            flag_3=15105853,
            sound_id=5104851,
            sound_id_1=5104852,
            flag_4=15105852,
        )
    else:
        CommonFunc_20005831(
            0,
            flag=15100850,
            flag_1=15105855,
            flag_2=15105856,
            region=5102850,
            sound_id=5104851,
            sound_id_1=5104852,
            flag_3=15105852,
        )
    CommonFunc_20005820(0, flag=15100850, obj=5101850, model_point=2, left=15105851)
    CommonFunc_20005839(
        0,
        flag=15100850,
        entity=5100850,
        radius=12.0,
        locked_camera_id__normal_camera_id=6213,
        locked_camera_id__normal_camera_id_1=6212,
        flag_1=15105855,
        flag_2=15105856,
        region=5102870,
    )
    CommonFunc_20005810(0, 15100890, 5101850, 5102850, 10000)


@RestartOnRest(15105890)
def Event_15105890():
    """Event 15105890"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(15100800))
    AND_1.Add(FlagEnabled(15100850))
    AND_1.Add(FlagEnabled(15100890))
    if AND_1:
        return
    DisableFlag(15100890)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(15100800))
    AND_2.Add(FlagEnabled(15100850))
    OR_1.Add(AND_2)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(15100800))
    AND_3.Add(FlagDisabled(15100850))
    AND_3.Add(FlagDisabled(15100200))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(15100890)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(FlagEnabled(15100800))
    AND_4.Add(FlagDisabled(15100850))
    AND_4.Add(FlagEnabled(15100200))
    
    MAIN.Await(AND_4)
    
    Restart()


@RestartOnRest(15105895)
def Event_15105895():
    """Event 15105895"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(15100895)
    AND_1.Add(FlagEnabled(15100800))
    AND_1.Add(FlagDisabled(9610))
    
    MAIN.Await(AND_1)
    
    EnableFlag(15100895)
    AND_2.Add(FlagEnabled(9610))
    
    MAIN.Await(AND_2)
    
    Restart()


@NeverRestart(15105700)
def Event_15105700():
    """Event 15105700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagDisabled(9610):
        DisableNetworkConnectedFlagRange(flag_range=(1900, 1919))
        SetNetworkConnectedFlagState(flag=1900, state=FlagSetting.On)
        SetNetworkConnectedFlagState(flag=1915, state=FlagSetting.On)
        Goto(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1915, 1919))
    DisableNetworkConnectedFlagRange(flag_range=(1915, 1919))
    SetNetworkConnectedFlagState(flag=1915, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1916))
    AND_1.Add(FlagEnabled(70001078))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1915, 1919))
    SetNetworkConnectedFlagState(flag=1915, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1918))
    AND_2.Add(FlagDisabled(15100800))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1915, 1919))
    SetNetworkConnectedFlagState(flag=1915, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1900, 1914))
    DisableNetworkConnectedFlagRange(flag_range=(1900, 1914))
    SetNetworkConnectedFlagState(flag=1900, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1900))
    AND_3.Add(FlagEnabled(15100800))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1900, 1914))
    SetNetworkConnectedFlagState(flag=1901, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1915, 1919))
    SetNetworkConnectedFlagState(flag=1918, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1915)

    # --- Label 9 --- #
    DefineLabel(9)
    if FlagEnabled(1900):
        DisableFlag(75100101)
        DisableFlag(75100132)

    # --- Label 10 --- #
    DefineLabel(10)
    End()


@RestartOnRest(15105703)
def Event_15105703(_, character: int, flag: int, radius: float):
    """Event 15105703"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(FlagEnabled(15105805))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Enemy)
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    EnableAI(character)


@RestartOnRest(15105704)
def Event_15105704(_, character: int):
    """Event 15105704"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(75100101))
    
    Wait(30.0)
    if FlagEnabled(15100723):
        Wait(1.600000023841858)
    AND_2.Add(HealthRatio(character) > 0.0)
    if not AND_2:
        return
    ForceAnimation(character, 3030, unknown2=1.0)


@RestartOnRest(15105705)
def Event_15105705(_, character: int):
    """Event 15105705"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(75100101))
    
    Wait(39.0)
    AND_2.Add(HealthRatio(character) > 0.0)
    if not AND_2:
        return
    ForceAnimation(character, 3011, unknown2=1.0)


@NeverRestart(15105710)
def Event_15105710(
    _,
    character: int,
    character_1: int,
    character_2: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    obj: int,
    destination: int,
):
    """Event 15105710"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1815, 1819))
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1816))
    AND_1.Add(FlagEnabled(70001073))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1800, 1814))
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1800, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1815)
    OR_1.Add(FlagEnabled(1801))
    OR_1.Add(FlagEnabled(1803))
    AND_3.Add(FlagEnabled(9324))
    AND_3.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1805, state=FlagSetting.On)
    OR_2.Add(FlagEnabled(1802))
    OR_2.Add(FlagEnabled(1804))
    AND_4.Add(FlagEnabled(9324))
    AND_4.Add(OR_2)
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1806, state=FlagSetting.On)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(1805, 1806)))
    AND_5.Add(FlagEnabled(75000104))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1807, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1807))
    AND_6.Add(FlagEnabled(75100201))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1808, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1808))
    AND_7.Add(FlagDisabled(75100205))
    AND_7.Add(FlagEnabled(75100204))
    AND_7.Add(FlagEnabled(15110801))
    SkipLinesIfConditionFalse(4, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1809, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1817, state=FlagSetting.On)
    AND_8.Add(FlagEnabled(1808))
    AND_8.Add(FlagEnabled(75100206))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1810, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001073)
    DisableFlag(15100717)
    if FlagEnabled(1815):
        DisableFlag(75100220)
    if FlagEnabled(75100202):
        EnableFlag(75100231)
    if FlagEnabled(75100203):
        EnableFlag(75100232)
    OR_4.Add(PlayerHasGood(2153))
    OR_4.Add(FlagEnabled(6500))
    SkipLinesIfConditionFalse(1, OR_4)
    EnableFlag(50006623)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L7, flag=1807)
    GotoIfFlagEnabled(Label.L8, flag=1808)
    GotoIfFlagEnabled(Label.L9, flag=1809)
    GotoIfFlagEnabled(Label.L10, flag=1810)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 7 --- #
    DefineLabel(7)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 8 --- #
    DefineLabel(8)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    DisableCharacterCollision(character_1)
    DisableGravity(character_1)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_2, animation_id_2, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_2, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DropMandatoryTreasure(character_2)
    End()


@NeverRestart(15105711)
def Event_15105711(_, character: int, character_1: int, animation_id: int, obj: int, destination: int):
    """Event 15105711"""
    EndIfFlagRangeAnyEnabled(flag_range=(1808, 1814))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(1807))
    AND_1.Add(FlagEnabled(75100201))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=100.0))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1808, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    DisableCharacterCollision(character_1)
    DisableGravity(character_1)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)


@NeverRestart(15105712)
def Event_15105712(_, character: int, character_1: int, animation_id: int, obj: int):
    """Event 15105712"""
    EndIfFlagRangeAnyEnabled(flag_range=(1809, 1814))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(1808))
    AND_1.Add(FlagEnabled(75100206))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1810, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    DisableObjectInvulnerability(obj)


@NeverRestart(15105713)
def Event_15105713(_, character: int, region: int, move_to_region: int):
    """Event 15105713"""
    EndIfFlagRangeAnyEnabled(flag_range=(1811, 1814))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(1810))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(51000010, cutscene_flags=0, player_id=10000, move_to_region=move_to_region, game_map=RINGED_CITY)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        51000010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=move_to_region,
        game_map=RINGED_CITY,
    )
    SkipLines(1)
    PlayCutscene(51000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1811, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(15105714)
def Event_15105714(_, character: int):
    """Event 15105714"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1807))
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 150))
    
    MAIN.Await(AND_1)
    
    EzstateAIRequest(character, command_id=7300, command_slot=1)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(15105715)
def Event_15105715(_, character: int):
    """Event 15105715"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(75100234)
    AND_1.Add(FlagEnabled(1807))
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 153))
    
    MAIN.Await(AND_1)
    
    EnableFlag(75100234)
    AND_2.Add(FlagEnabled(1807))
    AND_2.Add(FlagEnabled(1815))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 153))
    
    MAIN.Await(not AND_2)
    
    Restart()


@NeverRestart(15105716)
def Event_15105716(_, entity: int):
    """Event 15105716"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(75100235)
    AND_1.Add(FlagEnabled(1807))
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(75100235))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 91200, unknown2=1.0)
    Restart()


@NeverRestart(15105717)
def Event_15105717(_, character: int, obj: int):
    """Event 15105717"""
    GotoIfFlagEnabled(Label.L0, flag=15100717)
    EndIfFlagRangeAnyEnabled(flag_range=(1809, 1814))
    GotoIfPlayerNotInOwnWorld(Label.L1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 159))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 159))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    DestroyObject_NoSlot(obj=obj)
    EnableFlag(15100717)


@NeverRestart(15105720)
def Event_15105720(_, character: int, animation_id: int):
    """Event 15105720"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1835, 1839))
    DisableNetworkConnectedFlagRange(flag_range=(1835, 1839))
    SetNetworkConnectedFlagState(flag=1835, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1836))
    AND_1.Add(FlagEnabled(70001074))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1835, 1839))
    SetNetworkConnectedFlagState(flag=1835, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1820, 1834))
    DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1820, state=FlagSetting.On)
    if FlagEnabled(1821):
        DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1820, state=FlagSetting.On)
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1820, 1821)))
    AND_2.Add(FlagEnabled(9326))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1822, state=FlagSetting.On)
    OR_3.Add(FlagEnabled(15100500))
    OR_3.Add(FlagEnabled(149))
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(1820, 1822)))
    AND_3.Add(OR_3)
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1823, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001074)
    if FlagEnabled(1835):
        DisableFlag(75100170)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableInvincibility(character)
    DisableAnimations(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableAI(character)
    GotoIfFlagEnabled(Label.L0, flag=1820)
    GotoIfFlagEnabled(Label.L2, flag=1822)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(15105721)
def Event_15105721(_, character: int, character_1: int):
    """Event 15105721"""
    EndIfFlagRangeAnyEnabled(flag_range=(1822, 1834))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1835))
    AND_1.Add(FlagEnabled(1820))
    AND_1.Add(FlagEnabled(75100155))
    AND_1.Add(FlagEnabled(15100200))
    AND_1.Add(FlagDisabled(9326))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=10.0))
    AND_1.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1821, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(15105722)
def Event_15105722(_, character: int):
    """Event 15105722"""
    EndIfFlagRangeAnyEnabled(flag_range=(1822, 1834))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1835))
    AND_1.Add(FlagEnabled(1820))
    AND_1.Add(FlagEnabled(9326))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1820, 1834))
    SetNetworkConnectedFlagState(flag=1822, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)


@NeverRestart(15105723)
def Event_15105723():
    """Event 15105723"""
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=15100723, state=FlagSetting.Off)
    AND_1.Add(FlagEnabled(75100956))
    AND_1.Add(FlagEnabled(9326))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=15100723, state=FlagSetting.On)


@NeverRestart(15105724)
def Event_15105724():
    """Event 15105724"""
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=15100724, state=FlagSetting.Off)
    AND_1.Add(FlagEnabled(75100957))
    AND_1.Add(FlagEnabled(9326))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=15100724, state=FlagSetting.On)


@NeverRestart(15105730)
def Event_15105730(_, character: int, animation_id: int):
    """Event 15105730"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1895, 1899))
    DisableNetworkConnectedFlagRange(flag_range=(1895, 1899))
    SetNetworkConnectedFlagState(flag=1895, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1896))
    AND_1.Add(FlagEnabled(70001077))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1895, 1899))
    SetNetworkConnectedFlagState(flag=1895, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1880, 1894))
    DisableNetworkConnectedFlagRange(flag_range=(1880, 1894))
    SetNetworkConnectedFlagState(flag=1880, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1895)
    AND_2.Add(FlagEnabled(1880))
    AND_2.Add(FlagEnabled(15100500))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1880, 1894))
    SetNetworkConnectedFlagState(flag=1881, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001077)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1880)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1898)
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableHealthBar(character)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(15105740)
def Event_15105740(
    _,
    character: int,
    first_flag: int,
    flag: int,
    flag_1: int,
    last_flag: int,
    flag_2: int,
    animation_id: int,
):
    """Event 15105740"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagRangeAllDisabled((first_flag, last_flag)):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        SetNetworkConnectedFlagState(flag=first_flag, state=FlagSetting.On)
    if FlagEnabled(flag):
        DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
        SetNetworkConnectedFlagState(flag=first_flag, state=FlagSetting.On)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(FlagEnabled(flag_1))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=first_flag, state=FlagSetting.On)
    if FlagEnabled(first_flag):
        DisableFlag(flag_2)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L16, flag=flag)
    GotoIfFlagEnabled(Label.L18, flag=flag_1)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    Kill(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(15105900)
def Event_15105900():
    """Event 15105900"""
    DisableCharacter(PLAYER)
