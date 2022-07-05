"""
linked:
140

strings:
0: PC情報_大学到達時
22: クリア時間_通し
40: クリア時間_1プレイ
62: ボス戦_撃破時間
80: ボス_撃破
92: PC情報_ボス撃破_白痴の蜘蛛
124: ボス_戦闘開始
140: N:\\SPRJ\\data\\Param\\event\\common.emevd
216: 
218: 
220: 
222: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=45, args=(3200950, 3201950, 999, 13207800))
    RunEvent(7000, slot=46, args=(3200951, 3201951, 999, 13207820))
    RunEvent(7000, slot=47, args=(3200952, 3201952, 13201803, 13207840))
    RunEvent(7000, slot=48, args=(3200953, 3201953, 999, 13207860))
    RunEvent(7100, slot=45, args=(73200200, 3201950))
    RunEvent(7100, slot=46, args=(73200201, 3201951))
    RunEvent(7100, slot=47, args=(73200202, 3201952))
    RunEvent(7100, slot=48, args=(73200203, 3201953))
    RunEvent(7200, slot=45, args=(73200100, 3201950, 2102951))
    RunEvent(7200, slot=46, args=(73200101, 3201951, 2102953))
    RunEvent(7200, slot=47, args=(73200102, 3201952, 2102951))
    RunEvent(7200, slot=48, args=(73200103, 3201953, 2102953))
    RunEvent(7300, slot=45, args=(72103200, 3201950))
    RunEvent(7300, slot=46, args=(72103201, 3201951))
    RunEvent(7300, slot=47, args=(72103202, 3201952))
    RunEvent(7300, slot=48, args=(72103203, 3201953))
    RunEvent(7600, slot=70, args=(3201999, 3203999))
    RunEvent(9200, slot=9, args=(3203900,))
    RunEvent(9220, slot=8, args=(3200710, 13204220, 13204221, 3200, 32, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=8, args=(3200710, 13204220, 13204221, 13204222, 32, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=8, args=(3200710, 13204220, 13204221, 13204222, 32, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=8, args=(3200710, 13204220, 13204221, 3200, 13204800, 32, 0), arg_types="iiiiiBB")
    RegisterLadder(start_climbing_flag=13200000, stop_climbing_flag=13200001, obj=3201130)
    RegisterLadder(start_climbing_flag=13200002, stop_climbing_flag=13200003, obj=3201131)
    Event_13200990()
    Event_13200950()
    Event_13200960()
    CreateObjectVFX(3201000, vfx_id=200, model_point=900130)
    CreateObjectVFX(3201001, vfx_id=200, model_point=900130)
    CreateObjectVFX(3201002, vfx_id=200, model_point=900130)
    CreateObjectVFX(3201003, vfx_id=200, model_point=900130)
    CreateObjectVFX(3201004, vfx_id=200, model_point=900130)
    CreateObjectVFX(3201005, vfx_id=200, model_point=900130)
    DeleteVFX(3203910, erase_root_only=False)
    DeleteVFX(3203911, erase_root_only=False)
    DeleteVFX(3203912, erase_root_only=False)
    Event_13204400(0, flag=13204440, vfx_id=3203910, flag_1=13204420, flag_2=13204430, flag_3=13201800, flag_4=6001)
    Event_13204401(0, flag=13204441, vfx_id=3203911, flag_1=13204421, flag_2=13204431, flag_3=13201800, flag_4=13204420)
    Event_13204402(0, flag=13204442, vfx_id=3203912, flag_1=13204422, flag_2=13204432, flag_3=13201800, flag_4=13204420)
    Event_13204410(
        0,
        sign_type=0,
        character=3200910,
        region=3202910,
        summon_flag=13204420,
        dismissal_flag=13204430,
        flag=13204440,
        flag_1=13201800,
        action_button_id=10566
    )
    Event_13204410(
        1,
        sign_type=5,
        character=3200911,
        region=3202913,
        summon_flag=13204421,
        dismissal_flag=13204431,
        flag=13204441,
        flag_1=13201800,
        action_button_id=10565
    )
    Event_13204410(
        2,
        sign_type=5,
        character=3200912,
        region=3202914,
        summon_flag=13204422,
        dismissal_flag=13204432,
        flag=13204442,
        flag_1=13201800,
        action_button_id=10561
    )
    Event_13204450(0, character=3200910, region=3202911, flag=13204420, flag_1=13204430, flag_2=13204800)
    Event_13204450(1, character=3200911, region=3202915, flag=13204421, flag_1=13204431, flag_2=13204800)
    Event_13204450(2, character=3200912, region=3202916, flag=13204422, flag_1=13204432, flag_2=13204800)
    Event_13204460(
        0,
        character=3200910,
        region=3202911,
        region_1=3202800,
        region_2=3202809,
        animation=101130,
        flag=13204450,
        region_3=3202809
    )
    Event_13204460(
        1,
        character=3200911,
        region=3202915,
        region_1=3202800,
        region_2=3202809,
        animation=101130,
        flag=13204451,
        region_3=3202809
    )
    Event_13204460(
        2,
        character=3200912,
        region=3202916,
        region_1=3202800,
        region_2=3202809,
        animation=101130,
        flag=13204452,
        region_3=3202809
    )
    Event_13204470(0, character=3200910)
    Event_13204470(1, character=3200911)
    Event_13204470(2, character=3200912)
    Event_13204832()
    Event_13204833()
    Event_13204834()
    Event_13201800()
    Event_13201801()
    Event_13201802()
    Event_13201803()
    Event_13204830()
    Event_13204831()
    Event_13204802()
    Event_13204803()
    Event_13204804()
    Event_13204805()
    Event_13204807()
    Event_13204808()
    Event_13204809()
    Event_13204810()
    Event_13204820()
    Event_13204821()
    Event_13201804()
    Event_13204000(0, character=3200200, flag=13204802)
    Event_13204000(1, character=3200201, flag=13204802)
    Event_13204000(2, character=3200202, flag=13204802)
    Event_13204000(3, character=3200203, flag=13204802)
    Event_13204000(4, character=3200204, flag=13204802)
    Event_13204000(5, character=3200205, flag=13204802)
    Event_13204000(6, character=3200206, flag=13204802)
    Event_13204000(7, character=3200207, flag=13204802)
    Event_13204000(8, character=3200208, flag=13204802)
    Event_13204000(9, character=3200209, flag=13204802)
    Event_13204000(10, character=3200210, flag=13204811)
    Event_13204000(11, character=3200211, flag=13204811)
    Event_13204000(12, character=3200212, flag=13204811)
    Event_13204000(13, character=3200213, flag=13204811)
    Event_13204000(14, character=3200214, flag=13204811)
    Event_13204000(15, character=3200215, flag=13204811)
    Event_13204000(16, character=3200216, flag=13204811)
    Event_13204000(17, character=3200217, flag=13204811)
    Event_13204000(18, character=3200218, flag=13204811)
    Event_13204000(19, character=3200219, flag=13204811)
    Event_13204000(20, character=3200220, flag=13204812)
    Event_13204000(21, character=3200221, flag=13204812)
    Event_13204000(22, character=3200222, flag=13204812)
    Event_13204000(23, character=3200223, flag=13204812)
    Event_13204000(24, character=3200224, flag=13204812)
    Event_13204000(25, character=3200225, flag=13204812)
    Event_13204000(26, character=3200226, flag=13204812)
    Event_13204000(27, character=3200227, flag=13204812)
    Event_13204000(28, character=3200228, flag=13204812)
    Event_13204000(29, character=3200229, flag=13204812)
    Event_13204050(0, character=3200200, flag=13204802)
    Event_13204050(1, character=3200201, flag=13204802)
    Event_13204050(2, character=3200202, flag=13204802)
    Event_13204050(3, character=3200203, flag=13204802)
    Event_13204050(4, character=3200204, flag=13204802)
    Event_13204050(5, character=3200205, flag=13204802)
    Event_13204050(6, character=3200206, flag=13204802)
    Event_13204050(7, character=3200207, flag=13204802)
    Event_13204050(8, character=3200208, flag=13204802)
    Event_13204050(9, character=3200209, flag=13204802)
    Event_13204050(10, character=3200210, flag=13204811)
    Event_13204050(11, character=3200211, flag=13204811)
    Event_13204050(12, character=3200212, flag=13204811)
    Event_13204050(13, character=3200213, flag=13204811)
    Event_13204050(14, character=3200214, flag=13204811)
    Event_13204050(15, character=3200215, flag=13204811)
    Event_13204050(16, character=3200216, flag=13204811)
    Event_13204050(17, character=3200217, flag=13204811)
    Event_13204050(18, character=3200218, flag=13204811)
    Event_13204050(19, character=3200219, flag=13204811)
    Event_13204050(20, character=3200220, flag=13204812)
    Event_13204050(21, character=3200221, flag=13204812)
    Event_13204050(22, character=3200222, flag=13204812)
    Event_13204050(23, character=3200223, flag=13204812)
    Event_13204050(24, character=3200224, flag=13204812)
    Event_13204050(25, character=3200225, flag=13204812)
    Event_13204050(26, character=3200226, flag=13204812)
    Event_13204050(27, character=3200227, flag=13204812)
    Event_13204050(28, character=3200228, flag=13204812)
    Event_13204050(29, character=3200229, flag=13204812)
    Event_13204730(0, character=3200200)
    Event_13204730(1, character=3200201)
    Event_13204730(2, character=3200202)
    Event_13204730(3, character=3200203)
    Event_13204730(4, character=3200204)
    Event_13204730(5, character=3200205)
    Event_13204730(6, character=3200206)
    Event_13204730(7, character=3200207)
    Event_13204730(8, character=3200208)
    Event_13204730(9, character=3200209)
    Event_13204730(10, character=3200210)
    Event_13204730(11, character=3200211)
    Event_13204730(12, character=3200212)
    Event_13204730(13, character=3200213)
    Event_13204730(14, character=3200214)
    Event_13204730(15, character=3200215)
    Event_13204730(16, character=3200216)
    Event_13204730(17, character=3200217)
    Event_13204730(18, character=3200218)
    Event_13204730(19, character=3200219)
    Event_13204730(20, character=3200220)
    Event_13204730(21, character=3200221)
    Event_13204730(22, character=3200222)
    Event_13204730(23, character=3200223)
    Event_13204730(24, character=3200224)
    Event_13204730(25, character=3200225)
    Event_13204730(26, character=3200226)
    Event_13204730(27, character=3200227)
    Event_13204730(28, character=3200228)
    Event_13204730(29, character=3200229)
    Event_13200010(0, obj=3201110, animation_id=1, obj_act_id=13200100, obj_1=3201100, obj_act_id_1=100)
    Event_13200020(0, action_button_id=7030, action_button_id_1=7031, entity=3201110, flag=13200010)
    Event_13200030(0, entity=3201100, action_button_id=7100, text=10010172, flag=13200010)
    Event_13200040(0, obj=3201120, obj_act_id=13200120, animation_id=1, obj_act_id_1=3200040)
    Event_13200040(1, obj=3201122, obj_act_id=13200122, animation_id=1, obj_act_id_1=31)
    Event_13200040(2, obj=3201201, obj_act_id=13200203, animation_id=1, obj_act_id_1=31)
    Event_13200040(3, obj=3201210, obj_act_id=13200211, animation_id=1, obj_act_id_1=31)
    Event_13200050(0, action_button_id=7030, entity=3201122, flag=13200041)
    Event_13200050(1, action_button_id=7030, entity=3201201, flag=13200042)
    Event_13200055(0, action_button_id=7030, entity=3201210, flag=13200043)
    Event_13200060(
        0,
        obj=3201200,
        obj_act_id=13200200,
        obj_act_id_1=13200201,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        2,
        obj=3201202,
        obj_act_id=13200204,
        obj_act_id_1=13200205,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        3,
        obj=3201203,
        obj_act_id=13200206,
        obj_act_id_1=13200207,
        animation_id=1,
        obj_act_id_2=3200030,
        obj_act_id_3=31
    )
    Event_13200060(
        4,
        obj=3201204,
        obj_act_id=13200208,
        obj_act_id_1=13200209,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        6,
        obj=3201211,
        obj_act_id=13200212,
        obj_act_id_1=13200213,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        7,
        obj=3201212,
        obj_act_id=13200214,
        obj_act_id_1=13200215,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        8,
        obj=3201213,
        obj_act_id=13200216,
        obj_act_id_1=13200217,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        9,
        obj=3201214,
        obj_act_id=13200218,
        obj_act_id_1=13200219,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        10,
        obj=3201220,
        obj_act_id=13200220,
        obj_act_id_1=13200221,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        11,
        obj=3201221,
        obj_act_id=13200222,
        obj_act_id_1=13200223,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        12,
        obj=3201222,
        obj_act_id=13200224,
        obj_act_id_1=13200225,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        13,
        obj=3201223,
        obj_act_id=13200226,
        obj_act_id_1=13200227,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        14,
        obj=3201224,
        obj_act_id=13200228,
        obj_act_id_1=13200229,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        17,
        obj=3201232,
        obj_act_id=13200234,
        obj_act_id_1=13200235,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        18,
        obj=3201233,
        obj_act_id=13200236,
        obj_act_id_1=13200237,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200060(
        19,
        obj=3201234,
        obj_act_id=13200238,
        obj_act_id_1=13200239,
        animation_id=1,
        obj_act_id_2=30,
        obj_act_id_3=31
    )
    Event_13200200(0, obj=3201050, obj_act_id=13200050)
    Event_13200200(1, obj=3201051, obj_act_id=13200051)
    Event_13200200(3, obj=3201053, obj_act_id=13200053)
    Event_13200200(4, obj=3201054, obj_act_id=13200054)
    Event_13200200(10, obj=3201060, obj_act_id=13200060)
    Event_13200200(12, obj=3201062, obj_act_id=13200062)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6325)
    EnableFlag(13201999)
    SkipLinesIfFlagEnabled(5, 13201999)
    EnableObject(3201500)
    DisableObject(3201501)
    EnableTreasure(obj=3201500)
    DisableTreasure(obj=3201501)
    SkipLines(4)
    DisableObject(3201500)
    EnableObject(3201501)
    DisableTreasure(obj=3201500)
    EnableTreasure(obj=3201501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6326)
    EnableFlag(13201998)
    SkipLinesIfFlagEnabled(6, 13201998)
    EnableObject(3201064)
    DisableObject(3201065)
    EnableObjectActivation(3201064, obj_act_id=9942)
    DisableObjectActivation(3201065, obj_act_id=9942)
    Event_13200200(14, obj=3201064, obj_act_id=13200064)
    SkipLines(5)
    DisableObject(3201064)
    EnableObject(3201065)
    DisableObjectActivation(3201064, obj_act_id=9942)
    EnableObjectActivation(3201065, obj_act_id=9942)
    Event_13200200(15, obj=3201065, obj_act_id=13200065)
    Event_13204100(0, entity=3201000, action_button_id=7407, text=10012007)
    Event_13204100(1, entity=3201001, action_button_id=7408, text=10012008)
    Event_13204100(2, entity=3201002, action_button_id=7409, text=10012009)
    Event_13204100(3, entity=3201003, action_button_id=7410, text=10012010)
    Event_13204100(4, entity=3201004, action_button_id=7411, text=10012011)
    Event_13204100(5, entity=3201005, action_button_id=7412, text=10012012)
    Event_13200400()
    Event_13200500(0, character=3200110)
    Event_13205000(0, 3200500, 3202500, 0, 2.0, 3203500)
    Event_13205000(1, 3200501, 3202501, 0, 2.0, 3203501)
    Event_13205000(11, 3200315, 3202315, 0, 2.0, 3203315)
    Event_13205000(12, 3200337, 3202337, 0, 2.0, 3203337)
    Event_13205000(13, 3200340, 3202337, 0, 2.0, 3203340)
    Event_13205000(14, 3200341, 3202337, 0, 2.0, 3203341)
    Event_13205000(15, 3200345, 3202337, 0, 2.0, 3203345)
    Event_13205000(16, 3200343, 3202342, 0, 2.0, 3203343)
    Event_13205000(17, 3200110, 3202110, 0, 2.0, 3203110)
    Event_13205000(18, 3200620, 3202620, 0, 2.0, 3203620)
    Event_13205200()
    Event_13205040(0, 3200505, 3202505, 2.0, 0.0, 3202506)
    Event_13205040(1, 3200508, 3202505, 2.0, 1.0, 3202507)
    Event_13205080(0, character=3200333, region=3202334, animation_id=7000, animation_id_1=7001, left=0, flag=0)
    Event_13205080(1, character=3200336, region=3202336, animation_id=7002, animation_id_1=7003, left=1, flag=53200110)
    Event_13205080(2, character=3200342, region=3202342, animation_id=7000, animation_id_1=7001, left=0, flag=0)
    Event_13205080(3, character=3200346, region=3202315, animation_id=7000, animation_id_1=7001, left=0, flag=0)
    Event_13205100(0, character=3200300, region=0)
    Event_13205100(1, character=3200301, region=0)
    Event_13205100(2, character=3200302, region=0)
    Event_13205100(3, character=3200303, region=0)
    Event_13205100(4, character=3200304, region=0)
    Event_13205100(5, character=3200305, region=0)
    Event_13205100(6, character=3200306, region=0)
    Event_13205100(7, character=3200307, region=0)
    Event_13205100(8, character=3200308, region=0)
    Event_13205100(9, character=3200309, region=0)
    Event_13205100(10, character=3200310, region=0)
    Event_13205100(11, character=3200311, region=0)
    Event_13205100(12, character=3200312, region=0)
    Event_13205100(13, character=3200313, region=0)
    Event_13205100(14, character=3200314, region=0)
    Event_13205100(16, character=3200316, region=0)
    Event_13205100(17, character=3200317, region=0)
    Event_13205100(18, character=3200318, region=0)
    Event_13205100(19, character=3200319, region=0)
    Event_13205100(20, character=3200320, region=0)
    Event_13205100(21, character=3200321, region=0)
    Event_13205100(22, character=3200322, region=0)
    Event_13205100(23, character=3200323, region=0)
    Event_13205100(24, character=3200324, region=0)
    Event_13205100(25, character=3200325, region=0)
    Event_13205100(26, character=3200326, region=0)
    Event_13205100(27, character=3200327, region=0)
    Event_13205100(28, character=3200328, region=0)
    Event_13205100(29, character=3200329, region=0)
    Event_13205100(30, character=3200330, region=0)
    Event_13205100(31, character=3200331, region=0)
    Event_13205140(0, character=3200347, region=3202347)
    Event_13205600(
        0,
        npc_part_id=3290,
        npc_part_id_1=3290,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=13205700,
        flag_1=13205760,
        character=3200420
    )
    Event_13205600(
        1,
        npc_part_id=3291,
        npc_part_id_1=3291,
        part_index=9,
        animation_id=7022,
        special_effect_id=5907,
        flag=13205700,
        flag_1=13205760,
        character=3200420
    )
    Event_13205600(
        2,
        npc_part_id=3292,
        npc_part_id_1=3292,
        part_index=10,
        animation_id=7023,
        special_effect_id=5907,
        flag=13205700,
        flag_1=13205760,
        character=3200420
    )
    Event_13205600(
        3,
        npc_part_id=3290,
        npc_part_id_1=3290,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=13205701,
        flag_1=13205761,
        character=3200421
    )
    Event_13205600(
        4,
        npc_part_id=3291,
        npc_part_id_1=3291,
        part_index=9,
        animation_id=7022,
        special_effect_id=5907,
        flag=13205701,
        flag_1=13205761,
        character=3200421
    )
    Event_13205600(
        5,
        npc_part_id=3292,
        npc_part_id_1=3292,
        part_index=10,
        animation_id=7023,
        special_effect_id=5907,
        flag=13205701,
        flag_1=13205761,
        character=3200421
    )
    Event_13205630(
        0,
        npc_part_id=3290,
        npc_part_id_1=3290,
        part_index=8,
        part_health=40,
        flag=13205700,
        character=3200420
    )
    Event_13205630(
        1,
        npc_part_id=3291,
        npc_part_id_1=3291,
        part_index=9,
        part_health=40,
        flag=13205700,
        character=3200420
    )
    Event_13205630(
        2,
        npc_part_id=3292,
        npc_part_id_1=3292,
        part_index=10,
        part_health=40,
        flag=13205700,
        character=3200420
    )
    Event_13205630(
        3,
        npc_part_id=3290,
        npc_part_id_1=3290,
        part_index=8,
        part_health=40,
        flag=13205701,
        character=3200421
    )
    Event_13205630(
        4,
        npc_part_id=3291,
        npc_part_id_1=3291,
        part_index=9,
        part_health=40,
        flag=13205701,
        character=3200421
    )
    Event_13205630(
        5,
        npc_part_id=3292,
        npc_part_id_1=3292,
        part_index=10,
        part_health=40,
        flag=13205701,
        character=3200421
    )
    Event_13205660(0, tae_event_id=30, tae_event_id_1=40, flag=13205760, character=3200420, bit_index=1, bit_index_1=11)
    Event_13205660(1, tae_event_id=50, tae_event_id_1=40, flag=13205760, character=3200420, bit_index=2, bit_index_1=12)
    Event_13205660(2, tae_event_id=60, tae_event_id_1=40, flag=13205760, character=3200420, bit_index=3, bit_index_1=13)
    Event_13205660(3, tae_event_id=30, tae_event_id_1=40, flag=13205761, character=3200421, bit_index=1, bit_index_1=11)
    Event_13205660(4, tae_event_id=50, tae_event_id_1=40, flag=13205761, character=3200421, bit_index=2, bit_index_1=12)
    Event_13205660(5, tae_event_id=60, tae_event_id_1=40, flag=13205761, character=3200421, bit_index=3, bit_index_1=13)
    Event_13200310()
    Event_13200311()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13200100()
    Event_13200102()
    Event_13200103()
    Event_13200105()
    Event_13200106()
    Event_13200107()
    Event_13200108()
    Event_13200109()
    Event_13200110()
    Event_13200120()
    Event_13200121()
    SkipLinesIfFlagDisabled(3, 1420)
    DisableGravity(3200101)
    DisableCharacterCollision(3200101)
    Event_13200102()


@NeverRestart(13200010)
def Event_13200010(_, obj: int, animation_id: int, obj_act_id: int, obj_1: int, obj_act_id_1: int):
    """Event 13200010"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id_1)
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    Wait(0.0)


@NeverRestart(13200020)
def Event_13200020(_, action_button_id: int, action_button_id_1: int, entity: int, flag: int):
    """Event 13200020"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=entity)
    IfActionButtonParamActivated(2, action_button_id=action_button_id_1, entity=entity)
    IfFlagEnabled(3, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    DisplayDialog(text=10010160, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13200030)
def Event_13200030(_, entity: int, action_button_id: int, text: int, flag: int):
    """Event 13200030"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13200040)
def Event_13200040(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 13200040"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(13200050)
def Event_13200050(_, action_button_id: int, entity: int, flag: int):
    """Event 13200050"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(text=10010161, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(13200055)
def Event_13200055(_, action_button_id: int, entity: int, flag: int):
    """Event 13200055"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(1, 1420)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(text=10010161, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@NeverRestart(13200060)
def Event_13200060(
    _,
    obj: int,
    obj_act_id: int,
    obj_act_id_1: int,
    animation_id: int,
    obj_act_id_2: int,
    obj_act_id_3: int,
):
    """Event 13200060"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_3)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=obj_act_id)
    IfObjectActivated(2, obj_act_id=obj_act_id_1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    SkipLines(1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_3)


@NeverRestart(13200100)
def Event_13200100():
    """Event 13200100"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(13200101)
    EndIfFlagDisabled(1420)
    DisableAnimations(3200101)
    IfCharacterInsideRegion(0, PLAYER, region=3202850)
    EnableFlag(13200101)
    EnableAnimations(3200101)
    IfCharacterOutsideRegion(0, PLAYER, region=3202850)
    Restart()


@NeverRestart(13200102)
def Event_13200102():
    """Event 13200102"""
    GotoIfFlagEnabled(Label.L0, flag=1431)
    GotoIfFlagEnabled(Label.L0, flag=1430)
    GotoIfFlagEnabled(Label.L0, flag=1423)
    GotoIfFlagEnabled(Label.L0, flag=1422)
    GotoIfFlagEnabled(Label.L0, flag=1421)
    GotoIfFlagEnabled(Label.L1, flag=1420)

    # --- 0 --- #
    DefineLabel(0)
    PostDestruction(3201300)
    PostDestruction(3201301)
    PostDestruction(3201302)
    PostDestruction(3201303)
    PostDestruction(3201304)
    PostDestruction(3201305)
    PostDestruction(3201306)
    PostDestruction(3201307)
    PostDestruction(3201308)
    PostDestruction(3201309)
    PostDestruction(3201310)
    PostDestruction(3201311)
    PostDestruction(3201312)
    PostDestruction(3201313)
    PostDestruction(3201314)
    PostDestruction(3201315)
    PostDestruction(3201316)
    PostDestruction(3201317)
    PostDestruction(3201318)
    PostDestruction(3201319)
    PostDestruction(3201320)
    SetNest(3200101, region=3202852)
    Move(3200101, destination=3202852, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(3200101, 5327)
    AddSpecialEffect(3200101, 5403)
    IfFlagEnabled(-1, 1423)
    IfFlagEnabled(-1, 1432)
    SkipLinesIfConditionFalse(1, -1)
    DisableBackread(3200101)
    SkipLinesIfFlagDisabled(1, 1431)
    DropMandatoryTreasure(3200101)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(3200101, 7010, loop=True)
    Move(3200101, destination=3202851, destination_type=CoordEntityType.Region, short_move=True)
    DisableObjectActivation(3201210, obj_act_id=31)


@NeverRestart(13200103)
def Event_13200103():
    """Event 13200103"""
    EndIfFlagRangeAnyEnabled(flag_range=(1421, 1437))
    DisableFlag(73200327)
    IfFlagEnabled(1, 1420)
    IfFlagEnabled(1, 73200327)
    IfAttackedWithDamageType(2, attacked_entity=3200101, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    EnableFlag(13200104)
    SetNest(3200101, region=3202852)
    AddSpecialEffect(3200101, 5327)
    ForceAnimation(3200101, 7011)
    WaitFrames(frames=54)
    EnableGravity(3200101)
    EnableCharacterCollision(3200101)
    EnableObjectActivation(3201210, obj_act_id=31)


@NeverRestart(13200105)
def Event_13200105():
    """Event 13200105"""
    IfFlagEnabled(1, 1420)
    IfFlagEnabled(-1, 73200321)
    IfFlagEnabled(2, 13200104)
    IfFlagEnabled(2, 73200321)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1421)
    SaveRequest()


@NeverRestart(13200106)
def Event_13200106():
    """Event 13200106"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 13200101)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3200101, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, slot=0, args=(2,))


@NeverRestart(13200107)
def Event_13200107():
    """Event 13200107"""
    IfFlagEnabled(1, 9466)
    IfFlagEnabled(1, 9461)
    IfFlagEnabled(1, 1421)
    IfFlagEnabled(1, 73200324)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1422)


@NeverRestart(13200108)
def Event_13200108():
    """Event 13200108"""
    EndIfFlagEnabled(1430)
    EndIfFlagEnabled(1431)
    IfFlagEnabled(-1, 1421)
    IfFlagEnabled(-1, 1422)
    IfConditionTrue(1, input_condition=-1)
    IfHealthLessThan(1, 3200101, value=0.5)
    IfAttacked(1, attacked_entity=3200101, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3200101, 3000)
    DisableFlagRange((1420, 1437))
    EnableFlag(1430)
    SaveRequest()


@NeverRestart(13200109)
def Event_13200109():
    """Event 13200109"""
    EndIfFlagEnabled(1431)
    SetTeamType(3200101, TeamType.FriendlyNPC)
    IfFlagEnabled(0, 1430)
    SetTeamType(3200101, TeamType.HostileNPC)


@NeverRestart(13200110)
def Event_13200110():
    """Event 13200110"""
    GotoIfFlagDisabled(Label.L0, flag=1431)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200101)
    DisableFlagRange((1420, 1437))
    EnableFlag(1431)
    SaveRequest()


@NeverRestart(13200120)
def Event_13200120():
    """Event 13200120"""
    GotoIfFlagDisabled(Label.L0, flag=1061)
    DisableCharacter(3200100)
    DropMandatoryTreasure(3200100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200100)
    DisableFlagRange((1060, 1079))
    EnableFlag(1061)
    SaveRequest()


@NeverRestart(13200121)
def Event_13200121():
    """Event 13200121"""
    EndIfFlagEnabled(1061)
    IfFlagEnabled(1, 73200300)
    IfCharacterHasSpecialEffect(1, 3200100, 151)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(73200300)
    ForceAnimation(3200100, 7010)
    SkipLinesIfThisEventFlagEnabled(1)
    RunEvent(9350, slot=0, args=(2,))
    Restart()


@NeverRestart(13200200)
def Event_13200200(_, obj: int, obj_act_id: int):
    """Event 13200200"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(13200310)
def Event_13200310():
    """Event 13200310"""
    IfObjectActivated(0, obj_act_id=13200124)
    CreateTemporaryVFX(vfx_id=932201, anchor_entity=3202001, anchor_type=CoordEntityType.Region)
    Wait(6.0)
    WarpPlayerToRespawnPoint(2602959)


@NeverRestart(13200311)
def Event_13200311():
    """Event 13200311"""
    IfObjectActivated(0, obj_act_id=13200123)
    CreateTemporaryVFX(vfx_id=932201, anchor_entity=3202000, anchor_type=CoordEntityType.Region)
    Wait(6.0)
    WarpPlayerToRespawnPoint(3302959)


@NeverRestart(13200400)
def Event_13200400():
    """Event 13200400"""
    EndIfFlagEnabled(53200810)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    CreateObjectVFX(3201010, vfx_id=200, model_point=900201)
    IfActionButtonParamActivated(0, action_button_id=3200010, entity=3201010)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3200810, host_only=False)
    DeleteObjectVFX(3201010)


@NeverRestart(13200500)
def Event_13200500(_, character: int):
    """Event 13200500"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    Wait(0.0)


@NeverRestart(13200990)
def Event_13200990():
    """Event 13200990"""
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 3204000)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=0,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@NeverRestart(13201800)
def Event_13201800():
    """Event 13201800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=3203802)
    DisableSoundEvent(sound_id=3203803)
    DisableCharacter(3200800)
    Kill(3200800)
    DisableObject(3201800)
    DeleteVFX(3203800, erase_root_only=False)
    DisableMapCollision(collision=3204010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3201800)
    DeleteVFX(3203800)
    DisableMapCollision(collision=3204010)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=3200800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=17)
    AwardItemLot(51001900, host_only=False)
    EnableFlag(3200)
    EnableFlag(9465)
    StartPlayLogMeasurement(measurement_id=3200000, name=22, overwrite=False)
    StartPlayLogMeasurement(measurement_id=3200001, name=40, overwrite=False)
    StartPlayLogMeasurement(measurement_id=3200010, name=62, overwrite=False)
    CreatePlayLog(name=80)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=92,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=92,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=92,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=92,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(13201801)
def Event_13201801():
    """Event 13201801"""
    DisableNetworkSync()
    EndIfFlagEnabled(13201800)
    IfFlagEnabled(1, 13201800)
    IfCharacterBackreadDisabled(2, 3200800)
    IfHealthLessThanOrEqual(2, 3200800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(3202800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(13201802)
def Event_13201802():
    """Event 13201802"""
    EndIfFlagEnabled(13201800)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 13201800)
    IfThisEventFlagDisabled(1)
    IfAttackedWithDamageType(1, attacked_entity=3200800)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13204800)
    EndIfFlagEnabled(9303)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(9303)


@RestartOnRest(13201803)
def Event_13201803():
    """Event 13201803"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3200801)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(3200801)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfConditionFalse(1, 1)
    SetNetworkUpdateAuthority(3200801, authority_level=UpdateAuthority.Forced)
    GotoIfFlagEnabled(Label.L1, flag=13201800)
    IfCharacterHuman(2, PLAYER)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    IfFlagEnabled(0, 13201800)
    IfCharacterHuman(3, PLAYER)
    IfCharacterInsideRegion(3, PLAYER, region=3202811)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3202812)
    IfCharacterHuman(5, PLAYER)
    IfCharacterInsideRegion(5, PLAYER, region=3202813)
    IfCharacterHuman(6, PLAYER)
    IfCharacterInsideRegion(6, PLAYER, region=3202814)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, condition=3)
    SkipLinesIfFinishedConditionTrue(5, condition=4)
    SkipLinesIfFinishedConditionTrue(2, condition=5)
    Move(3200801, destination=3202815, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202816, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202817, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202818, destination_type=CoordEntityType.Region, short_move=True)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(3200801, 7001)
    IfCharacterHuman(8, PLAYER)
    IfEntityWithinDistance(8, entity=PLAYER, other_entity=3200801, radius=12.0)
    IfConditionTrue(0, input_condition=8)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutsceneAndSetTimePeriod(cutscene=32000000, cutscene_flags=0, player_id=10000, time_period_id=3)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(70002802)
    WarpPlayerToRespawnPoint(2802958)
    End()

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@NeverRestart(13201804)
def Event_13201804():
    """Event 13201804"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13204800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(13204800)
    EnableFlag(13201802)


@NeverRestart(13204000)
def Event_13204000(_, character: int, flag: int):
    """Event 13204000"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableGravity(character)
    IfFlagEnabled(1, flag)
    IfRandomTimeElapsed(-1, min_seconds=2.0, max_seconds=3.0)
    IfCharacterWhitePhantom(2, PLAYER)
    IfTimeElapsed(2, seconds=3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(character)
    RotateToFaceEntity(character, PLAYER, animation=7000, wait_for_completion=True)
    EnableGravity(character)


@NeverRestart(13204050)
def Event_13204050(_, character: int, flag: int):
    """Event 13204050"""
    GotoIfFlagDisabled(Label.L0, flag=13201800)
    DisableCharacter(character)
    Kill(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag)
    IfCharacterDead(1, 3200800)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=0.0, max_seconds=1.0)
    Kill(character)


@NeverRestart(13204100)
def Event_13204100(_, entity: int, action_button_id: int, text: int):
    """Event 13204100"""
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=action_button_id, entity=entity)
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(13204730)
def Event_13204730(_, character: int):
    """Event 13204730"""
    EndIfFlagEnabled(13201800)
    IfFlagEnabled(0, 13204802)
    SetCharacterEventTarget(character, region=3200800)


@NeverRestart(13204830)
def Event_13204830():
    """Event 13204830"""
    EndIfFlagEnabled(13201800)
    GotoIfFlagEnabled(Label.L0, flag=13201802)
    SkipLinesIfClient(2)
    DisableObject(3201800)
    DeleteVFX(3203800, erase_root_only=False)
    DisableMapCollision(collision=3204010)
    IfFlagDisabled(1, 13201800)
    IfFlagEnabled(1, 13201802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3201800)
    CreateVFX(3203800)
    EnableMapCollision(collision=3204010)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13201800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=3200800, entity=3201800)
    IfFlagEnabled(3, 13201800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 3202800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3202809)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@NeverRestart(13204831)
def Event_13204831():
    """Event 13204831"""
    DisableNetworkSync()
    EndIfFlagEnabled(13201800)
    IfFlagDisabled(1, 13201800)
    IfFlagEnabled(1, 13201802)
    IfFlagEnabled(1, 13204800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=3200800, entity=3201800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3202800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3202801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(13204832)
def Event_13204832():
    """Event 13204832"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3201800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13204833)
def Event_13204833():
    """Event 13204833"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3201800, radius=2.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3201800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13204834)
def Event_13204834():
    """Event 13204834"""
    IfEntityWithinDistance(0, entity=3200110, other_entity=3201800, radius=2.0)
    SetGravityAndCollisionExcludingOwnWorld(character=3200110, state=False)
    IfEntityBeyondDistance(0, entity=3200110, other_entity=3201800, radius=2.0)
    SetGravityAndCollisionExcludingOwnWorld(character=3200110, state=True)
    Restart()


@NeverRestart(13204802)
def Event_13204802():
    """Event 13204802"""
    EndIfFlagEnabled(13201800)
    DisableAI(3200800)
    DisableHealthBar(3200800)
    EnableImmortality(3200800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(1, 13201802)
    IfFlagEnabled(1, 13204800)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3200800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13204800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3200800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3200800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3200800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3200800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3200800)
    DisableImmortality(3200800)
    AddSpecialEffect(3200800, 3011, affect_npc_part_hp=True)
    EnableBossHealthBar(3200800, name=510000)
    SetNetworkUpdateRate(3200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(name=124)
    StartPlayLogMeasurement(measurement_id=3200010, name=62, overwrite=True)


@NeverRestart(13204803)
def Event_13204803():
    """Event 13204803"""
    DisableNetworkSync()
    EndIfFlagEnabled(13201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=3203802)
    DisableSoundEvent(sound_id=3203803)
    IfFlagDisabled(1, 13201800)
    IfFlagEnabled(1, 13204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13204801)
    IfCharacterInsideRegion(1, PLAYER, region=3202801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3203802)
    IfCharacterHasTAEEvent(2, 3200800, tae_event_id=10)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13201800)
    IfFlagEnabled(2, 13204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13204801)
    IfCharacterInsideRegion(2, PLAYER, region=3202801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3203802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3203803)


@NeverRestart(13204804)
def Event_13204804():
    """Event 13204804"""
    DisableNetworkSync()
    EndIfFlagEnabled(13201800)
    IfHealthGreaterThan(1, 3200800, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3200800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=1)
    IfHealthGreaterThan(2, 3200800, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=3200800, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=0)
    Restart()


@NeverRestart(13204805)
def Event_13204805():
    """Event 13204805"""
    DisableNetworkSync()
    EndIfFlagEnabled(13201800)
    IfFlagEnabled(0, 13201800)
    DisableBossMusic(sound_id=3203802)
    DisableBossMusic(sound_id=3203803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13204807)
def Event_13204807():
    """Event 13204807"""
    EndIfFlagEnabled(13201800)
    IfHealthLessThanOrEqual(0, 3200800, value=0.75)
    AICommand(3200800, command_id=100, command_slot=0)
    ReplanAI(3200800)
    IfCharacterHasTAEEvent(0, 3200800, tae_event_id=10)
    DisableCharacter(3200800)
    Wait(3.0)
    Move(3200800, destination=3202806, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3200800)
    ForceAnimation(3200800, 3021)
    AICommand(3200800, command_id=101, command_slot=0)
    ReplanAI(3200800)
    EnableFlag(13204811)
    IfHealthLessThanOrEqual(0, 3200800, value=0.5)
    AICommand(3200800, command_id=110, command_slot=0)
    ReplanAI(3200800)
    IfCharacterHasTAEEvent(0, 3200800, tae_event_id=10)
    DisableCharacter(3200800)
    Wait(3.0)
    Move(3200800, destination=3202807, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3200800)
    ForceAnimation(3200800, 3021)
    AICommand(3200800, command_id=111, command_slot=0)
    ReplanAI(3200800)
    EnableFlag(13204812)


@NeverRestart(13204808)
def Event_13204808():
    """Event 13204808"""
    EndIfFlagEnabled(13201800)
    CreateNPCPart(3200800, npc_part_id=3201, part_index=NPCPartType.Part2, part_health=100)
    SetNPCPartEffects(3200800, npc_part_id=3201, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(2, 3200800, value=0.0)
    IfCharacterHasTAEEvent(3, 3200800, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7000)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(5, 3200800, value=0.0)
    IfCharacterHasTAEEvent(6, 3200800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7001)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=25, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(8, 3200800, value=0.0)
    IfCharacterHasTAEEvent(9, 3200800, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7002)
    CreateNPCPart(
        3200800,
        npc_part_id=3201,
        part_index=NPCPartType.Part2,
        part_health=9999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(3200800, npc_part_id=3201, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(3200800)
    IfTimeElapsed(0, seconds=30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=-1, overwrite_max=True)
    ReplanAI(2420800)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13204809)
def Event_13204809():
    """Event 13204809"""
    EndIfFlagEnabled(13201800)
    CreateNPCPart(3200800, npc_part_id=3202, part_index=NPCPartType.Part3, part_health=100)
    SetNPCPartEffects(3200800, npc_part_id=3202, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, 3200800, npc_part_id=3202, value=0)
    IfHealthLessThanOrEqual(2, 3200800, value=0.0)
    IfCharacterHasTAEEvent(3, 3200800, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7005)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, 3200800, npc_part_id=3202, value=0)
    IfHealthLessThanOrEqual(5, 3200800, value=0.0)
    IfCharacterHasTAEEvent(6, 3200800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7006)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=25, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, 3200800, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, 3200800, value=0.0)
    IfCharacterHasTAEEvent(9, 3200800, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(3200800)
    ForceAnimation(3200800, 7007)
    CreateNPCPart(
        3200800,
        npc_part_id=3202,
        part_index=NPCPartType.Part3,
        part_health=9999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(3200800, npc_part_id=3202, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(3200800)
    IfTimeElapsed(0, seconds=30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=-1, overwrite_max=True)
    ReplanAI(2420800)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13204810)
def Event_13204810():
    """Event 13204810"""
    EndIfFlagEnabled(13201800)
    CreateNPCPart(
        3200800,
        npc_part_id=3200,
        part_index=NPCPartType.Part1,
        part_health=50,
        damage_correction=0.5,
        body_damage_correction=0.5,
    )
    SetNPCPartEffects(3200800, npc_part_id=3200, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(0, 3200800, npc_part_id=3200, value=0)
    Restart()


@NeverRestart(13204820)
def Event_13204820():
    """Event 13204820"""
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3202800)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    EnableInvincibility(PLAYER)
    CreateTemporaryVFX(vfx_id=932210, anchor_entity=PLAYER, model_point=246, anchor_type=CoordEntityType.Character)

    # --- 0 --- #
    DefineLabel(0)
    Wait(5.0)
    DisableInvincibility(PLAYER)
    SkipLinesIfFlagDisabled(1, 13201802)
    EnableFlag(13204800)
    Restart()


@NeverRestart(13204821)
def Event_13204821():
    """Event 13204821"""
    DisableNetworkSync()
    IfFlagEnabled(1, 13204800)
    IfCharacterInsideRegion(1, PLAYER, region=3202800)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    CreateTemporaryVFX(vfx_id=932210, anchor_entity=PLAYER, model_point=246, anchor_type=CoordEntityType.Character)
    Wait(5.0)
    DisableInvincibility(PLAYER)
    EnableFlag(13204801)
    Restart()


@RestartOnRest(13205000)
def Event_13205000(_, character: int, region: int, region_1: int, radius: float, patrol_information_id: int):
    """Event 13205000"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ChangePatrolBehavior(character, patrol_information_id=-1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_1)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13205040)
def Event_13205040(_, character: int, region: int, radius: float, seconds: float, region_1: int):
    """Event 13205040"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    EnableAI(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Wait(seconds)
    EnableAI(character)
    SetNest(character, region=region_1)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region_1)
    ForceAnimation(character, 3013)
    WaitFrames(frames=34)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13205050)
def Event_13205050(_, character: int, region: int, patrol_information_id: int):
    """Event 13205050"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ChangePatrolBehavior(character, patrol_information_id=-1)
    IfCharacterInsideRegion(0, character, region=region)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13205060)
def Event_13205060(_, character: int, region: int, patrol_information_id: int):
    """Event 13205060"""
    IfCharacterInsideRegion(-1, character, region=region)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(13205080)
def Event_13205080(_, character: int, region: int, animation_id: int, animation_id_1: int, left: int, flag: int):
    """Event 13205080"""
    EndIfThisEventSlotFlagEnabled()
    DisableGravity(character)
    DisableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    SkipLinesIfEqual(1, left=left, right=0)
    IfFlagEnabled(1, flag)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableGravity(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    EnableCharacterCollision(character)


@RestartOnRest(13205100)
def Event_13205100(_, character: int, region: int):
    """Event 13205100"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, 7004, loop=True)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7005)
    WaitFrames(frames=59)
    RotateToFaceEntity(character, PLAYER, animation=3011)


@RestartOnRest(13205140)
def Event_13205140(_, character: int, region: int):
    """Event 13205140"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfAttackedWithDamageType(2, attacked_entity=character)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    RotateToFaceEntity(character, PLAYER, animation=3002)


@RestartOnRest(13205200)
def Event_13205200():
    """Event 13205200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableCharacter(3200621)
    IfHealthEqual(1, 3200620, value=0.0)
    IfCharacterHasTAEEvent(1, 3200620, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(
        3200621,
        destination=3200620,
        destination_type=CoordEntityType.Character,
        model_point=90,
        copy_draw_parent=3200620,
    )
    EnableCharacter(3200621)

    # --- 0 --- #
    DefineLabel(0)
    DropMandatoryTreasure(3200621)


@RestartOnRest(13205300)
def Event_13205300(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 13205300"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=30)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(0, character, npc_part_id=npc_part_id_1, value=0)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 9930)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    Restart()


@NeverRestart(13205600)
def Event_13205600(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    animation_id: int,
    special_effect_id: int,
    flag: int,
    flag_1: int,
    character: int,
):
    """Event 13205600"""
    IfFlagEnabled(0, flag)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=npc_part_id_1, value=0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(1, flag_1)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfFlagEnabled(2, flag)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=1, overwrite_max=False)
    Restart()
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=999999)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    IfCharacterHasTAEEvent(0, character, tae_event_id=400)
    AddSpecialEffect(character, special_effect_id)
    DisableFlag(flag_1)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    CancelSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13205630)
def Event_13205630(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    flag: int,
    character: int,
):
    """Event 13205630"""
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(flag)


@NeverRestart(13205660)
def Event_13205660(
    _,
    tae_event_id: int,
    tae_event_id_1: int,
    flag: int,
    character: int,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 13205660"""
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id)
    EnableFlag(flag)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id_1)
    DisableFlag(flag)
    Restart()


@NeverRestart(13200950)
def Event_13200950():
    """Event 13200950"""
    IfCharacterHuman(1, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    IfPlayerStandingOnCollision(2, 3204001)
    IfFlagEnabled(2, 12800434)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(12800434)
    AddSpecialEffect(PLAYER, 110)
    AddSpecialEffect(PLAYER, 111)
    AddSpecialEffect(PLAYER, 112)
    AddSpecialEffect(PLAYER, 113)
    AddSpecialEffect(PLAYER, 114)
    AddSpecialEffect(PLAYER, 115)
    AddSpecialEffect(PLAYER, 116)
    EndIfThisEventFlagEnabled()
    RunEvent(9350, slot=0, args=(2,))
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@NeverRestart(13200960)
def Event_13200960():
    """Event 13200960"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    IfPlayerStandingOnCollision(-1, 3204001)
    IfPlayerStandingOnCollision(-1, 3204002)
    IfConditionTrue(0, input_condition=-1)
    AwardAchievement(achievement_id=13)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@RestartOnRest(13204450)
def Event_13204450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 13204450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@NeverRestart(13204470)
def Event_13204470(_, character: int):
    """Event 13204470"""
    IfCharacterInsideRegion(0, character, region=3202800)
    EnableInvincibility(character)

    # --- 0 --- #
    DefineLabel(0)
    Wait(5.0)
    DisableInvincibility(character)


@RestartOnRest(13204400)
def Event_13204400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13204400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(1, 13204421)
    IfFlagDisabled(1, 13204422)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(2, 13204421)
    IfFlagDisabled(2, 13204422)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13204401)
def Event_13204401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13204401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagDisabled(1, 6813)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagDisabled(2, 6813)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13204402)
def Event_13204402(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13204402"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(-4, 12410803)
    IfFlagEnabled(-4, 12410804)
    IfConditionTrue(1, input_condition=-4)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(-5, 12410803)
    IfFlagEnabled(-5, 12410804)
    IfConditionTrue(2, input_condition=-5)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13204410)
def Event_13204410(
    _,
    sign_type: int,
    character: int,
    region: int,
    summon_flag: int,
    dismissal_flag: int,
    flag: int,
    flag_1: int,
    action_button_id: int,
):
    """Event 13204410"""
    SetBackreadStateAlternate(character, True)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfFlagEnabled(1, summon_flag)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    IfClient(1)
    IfFlagEnabled(1, summon_flag)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(character)
    EndIfFlagEnabled(flag_1)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, summon_flag)
    IfFlagDisabled(2, dismissal_flag)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest(13204460)
def Event_13204460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 13204460"""
    EndIfClient()
    IfFlagEnabled(1, flag)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    IfCharacterInsideRegion(2, character, region=region_2)
    RestartIfConditionFalse(2)
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(0, character, region=region_3)
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
