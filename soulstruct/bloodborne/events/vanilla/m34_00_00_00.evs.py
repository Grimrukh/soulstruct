"""
linked:
110

strings:
0: ボス_撃破
12: PC情報_ボス撃破_ルドウイーク
46: ボス_戦闘開始
62: ボス戦_撃破時間
80: PC情報_ボス撃破_教区長Ω
110: N:\\SPRJ\\data\\Param\\event\\common.emevd
186: 
188: 
190: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    GotoIfFlagEnabled(Label.L0, flag=13400999)
    RunEvent(7000, slot=55, args=(3400950, 3401950, 999, 13407800))
    RunEvent(7000, slot=56, args=(3400951, 3401951, 999, 13407820))
    RunEvent(7000, slot=57, args=(3400952, 3401952, 13401800, 13407840))
    RunEvent(7000, slot=58, args=(3400953, 3401953, 13401850, 13407860))
    RunEvent(7100, slot=55, args=(73400200, 3401950))
    RunEvent(7100, slot=56, args=(73400201, 3401951))
    RunEvent(7100, slot=57, args=(73400202, 3401952))
    RunEvent(7100, slot=58, args=(73400203, 3401953))
    RunEvent(7200, slot=55, args=(73400100, 3401950, 2102953))
    RunEvent(7200, slot=56, args=(73400101, 3401951, 2102953))
    RunEvent(7200, slot=57, args=(73400102, 3401952, 2102953))
    RunEvent(7200, slot=58, args=(73400103, 3401953, 2102953))
    RunEvent(7300, slot=55, args=(72103400, 3401950))
    RunEvent(7300, slot=56, args=(72103401, 3401951))
    RunEvent(7300, slot=57, args=(72103402, 3401952))
    RunEvent(7300, slot=58, args=(72103403, 3401953))
    DisableObject(3401999)
    DeleteVFX(3403999, erase_root_only=False)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(3400950)
    DisableCharacter(3400951)
    DisableCharacter(3400952)
    DisableCharacter(3400953)
    DisableObject(3401950)
    DisableObject(3401951)
    DisableObject(3401952)
    DisableObject(3401953)
    SetRespawnPoint(respawn_point=3402955)
    EnableFlag(9401)
    EnableFlag(9404)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(3400)
    DisableFlag(3401)
    DisableFlag(3402)
    EnableFlag(3403)
    SkipLinesIfFlagDisabled(4, 13401800)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    SkipLinesIfFlagDisabled(4, 13401852)
    DisableFlag(3400)
    DisableFlag(3401)
    EnableFlag(3402)
    DisableFlag(3403)
    SkipLinesIfFlagDisabled(4, 13401850)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    Event_13400010()
    Event_13401000()
    RegisterLadder(start_climbing_flag=13400000, stop_climbing_flag=13400001, obj=3401000)
    RegisterLadder(start_climbing_flag=13400002, stop_climbing_flag=13400003, obj=3401001)
    Event_13401500()
    Event_13404700(0, character=3400790, flag=13404701, flag_1=13404711, flag_2=3400, flag_3=999)
    Event_13404700(5, character=3400791, flag=13404702, flag_1=13404712, flag_2=3400, flag_3=999)
    Event_13404710(0, character=3400790, flag=13404701, flag_1=13404711, flag_2=13404721)
    Event_13404710(5, character=3400701, flag=13404702, flag_1=13404712, flag_2=13404722)
    Event_13404720(0, character=3400790, flag=13404701, flag_1=13404711, flag_2=13404721)
    Event_13404720(5, character=3400791, flag=13404702, flag_1=13404712, flag_2=13404722)
    Event_13404730(
        0,
        character=3400790,
        flag=13404701,
        flag_1=13404711,
        flag_2=3400,
        flag_3=13404810,
        flag_4=999,
        flag_5=999,
        flag_6=13404712
    )
    Event_13404730(
        5,
        character=3400791,
        flag=13404702,
        flag_1=13404712,
        flag_2=3400,
        flag_3=13404810,
        flag_4=999,
        flag_5=999,
        flag_6=13404711
    )
    Event_13404740()
    Event_13404742()
    Event_13401800()
    Event_13404811()
    Event_13401801()
    Event_13404800()
    Event_13404801()
    Event_13404802()
    Event_13404803()
    Event_13404804()
    Event_13404805()
    Event_13404806()
    Event_13404807()
    Event_13401802()
    Event_13401803()
    Event_13404820()
    Event_13404821()
    Event_13404822()
    Event_13404823()
    Event_13404840()
    Event_13401804()
    SkipLinesIfFlagEnabled(8, 13400999)
    Event_13404824()
    Event_13404825()
    Event_13404830(
        0,
        npc_part_id=3400,
        npc_part_id_1=3400,
        part_index=1,
        part_health=300,
        special_effect_id=480,
        animation_id=7001,
        frames=152
    )
    Event_13404830(
        1,
        npc_part_id=3401,
        npc_part_id_1=3401,
        part_index=2,
        part_health=150,
        special_effect_id=482,
        animation_id=7004,
        frames=72
    )
    Event_13404830(
        2,
        npc_part_id=3402,
        npc_part_id_1=3402,
        part_index=3,
        part_health=150,
        special_effect_id=481,
        animation_id=7002,
        frames=72
    )
    Event_13404835()
    Event_13404841()
    SkipLines(3)
    Event_13404830(
        0,
        npc_part_id=3400,
        npc_part_id_1=3400,
        part_index=1,
        part_health=400,
        special_effect_id=480,
        animation_id=7001,
        frames=152
    )
    Event_13404830(
        1,
        npc_part_id=3401,
        npc_part_id_1=3401,
        part_index=2,
        part_health=200,
        special_effect_id=482,
        animation_id=7004,
        frames=72
    )
    Event_13404830(
        2,
        npc_part_id=3402,
        npc_part_id_1=3402,
        part_index=3,
        part_health=200,
        special_effect_id=481,
        animation_id=7002,
        frames=72
    )
    Event_13401850()
    Event_13404861()
    Event_13401851()
    Event_13404850()
    Event_13404851()
    Event_13404852()
    Event_13404853()
    Event_13404854()
    Event_13404855()
    Event_13404856()
    Event_13404857()
    Event_13404870(
        0,
        npc_part_id=3450,
        npc_part_id_1=3450,
        part_index=1,
        special_effect_id=480,
        special_effect_id_1=490,
        part_health=60,
        animation_id=8020
    )
    Event_13404870(
        1,
        npc_part_id=3451,
        npc_part_id_1=3451,
        part_index=2,
        special_effect_id=481,
        special_effect_id_1=491,
        part_health=150,
        animation_id=8000
    )
    Event_13404870(
        2,
        npc_part_id=3452,
        npc_part_id_1=3452,
        part_index=3,
        special_effect_id=482,
        special_effect_id_1=492,
        part_health=150,
        animation_id=8010
    )
    Event_13404870(
        3,
        npc_part_id=3453,
        npc_part_id_1=3453,
        part_index=4,
        special_effect_id=483,
        special_effect_id_1=493,
        part_health=250,
        animation_id=8030
    )
    Event_13404870(
        4,
        npc_part_id=3454,
        npc_part_id_1=3454,
        part_index=5,
        special_effect_id=484,
        special_effect_id_1=494,
        part_health=250,
        animation_id=8040
    )
    Event_13404875()
    Event_13401853()
    Event_13401200(0, action_button_id=3400950, anchor_entity=3401020, flag=13401211)
    Event_13401210(0, obj=3401010, obj_act_id=13400000, animation_id=1, obj_act_id_1=3400000)
    Event_13401210(1, obj=3401020, obj_act_id=13400001, animation_id=1, obj_act_id_1=3400010)
    Event_13401220()
    Event_13400100()
    Event_13400220(0, character=3400680, flag=53401710)
    Event_13400220(1, character=3400681, flag=53401720)
    Event_13405103()
    Event_13400310(0, character=3400590, region=3402341)
    Event_13400320()
    Event_13404799()
    Event_13405100(0, obj=3401400, region=3402531, region_1=3402554)
    Event_13405105(
        0,
        region=3402370,
        entity=3401350,
        obj__source_entity=3401351,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0
    )
    Event_13405115(
        0,
        obj__source_entity=3401366,
        flag=13405130,
        frames=0,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        1,
        obj__source_entity=3401356,
        flag=13405131,
        frames=0,
        frames_1=60,
        behavior_id=6284,
        behavior_id_1=6285,
        behavior_id_2=6286,
        behavior_id_3=6287
    )
    Event_13405115(
        2,
        obj__source_entity=3401359,
        flag=13405132,
        frames=0,
        frames_1=70,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        3,
        obj__source_entity=3401363,
        flag=13405132,
        frames=20,
        frames_1=80,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        4,
        obj__source_entity=3401364,
        flag=13405132,
        frames=10,
        frames_1=40,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        5,
        obj__source_entity=3401365,
        flag=13405132,
        frames=30,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        6,
        obj__source_entity=3401364,
        flag=13405133,
        frames=10,
        frames_1=60,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        7,
        obj__source_entity=3401359,
        flag=13405135,
        frames=20,
        frames_1=40,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        9,
        obj__source_entity=3401363,
        flag=13405135,
        frames=10,
        frames_1=70,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        10,
        obj__source_entity=3401364,
        flag=13405135,
        frames=17,
        frames_1=60,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405115(
        11,
        obj__source_entity=3401365,
        flag=13405135,
        frames=6,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405113(
        0,
        obj__source_entity=3401360,
        flag=13405136,
        frames=6,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283
    )
    Event_13405140(1, character=3400207, region=3402510, flag=13405132, region_1=3402371, entity=3401367, frames=30)
    Event_13405140(2, character=3400207, region=3402376, flag=13405133, region_1=3402371, entity=3401367, frames=10)
    Event_13405140(4, character=3400210, region=3402377, flag=13405136, region_1=3402374, entity=3401368, frames=20)
    Event_13405145(0, region=3402374, entity=3401368, flag=13405130)
    Event_13405145(1, region=3402372, entity=3401357, flag=13405131)
    Event_13405145(2, region=3402371, entity=3401367, flag=13405135)
    Event_13405145(3, region=3402374, entity=3401368, flag=13405136)
    Event_13405155(0, region=3402515)
    Event_13405160(0, obj__source_entity=3401330)
    Event_13405160(1, obj__source_entity=3401331)
    Event_13405160(2, obj__source_entity=3401332)
    Event_13405160(3, obj__source_entity=3401333)
    Event_13405160(4, obj__source_entity=3401334)
    Event_13405160(5, obj__source_entity=3401335)
    Event_13405160(6, obj__source_entity=3401336)
    Event_13405160(7, obj__source_entity=3401337)
    Event_13405160(8, obj__source_entity=3401338)
    Event_13405160(9, obj__source_entity=3401339)
    Event_13405160(10, obj__source_entity=3401340)
    Event_13405160(11, obj__source_entity=3401341)
    Event_13405160(12, obj__source_entity=3401342)
    Event_13405160(13, obj__source_entity=3401343)
    Event_13405160(14, obj__source_entity=3401344)
    Event_13405110()
    Event_13405112()
    Event_13405200(0, character=3400300, region=3402600, animation_id=3004, region_1=3402601)
    Event_13400330(0, character=3400650)
    Event_13405211(1, region=3402301)
    Event_13405211(2, region=3402302)
    Event_13405220(0, 3400152, 7015, 109900, 7016, 109955, 0, 0.0, 1.0)
    Event_13405220(2, 3400154, 7015, 109900, 7016, 109955, 0, 0.0, 1.0)
    Event_13405220(16, 3400315, 7001, 400010, 7002, 400010, 3402555, 0.0, 0.0)
    Event_13405220(17, 3400169, 7015, 109900, 7016, 109955, 0, 0.0, 2.0)
    Event_13405220(18, 3400170, 7015, 109900, 7016, 109955, 0, 0.0, 2.0)
    Event_13405220(19, 3400171, 7015, 109900, 7016, 109955, 0, 0.0, 2.0)
    Event_13405220(20, 3400172, 7015, 109900, 7016, 109955, 0, 0.0, 2.0)
    Event_13405220(3, 3400350, 7000, 6550, 0, 6550, 0, 0.0, 0.0)
    Event_13405550(4, 3400141, 7000, 109900, 7002, 109950, 2.0, 3.0)
    Event_13405550(5, 3400146, 7000, 109900, 7002, 109950, 2.0, 4.0)
    Event_13405550(7, 3400147, 7003, 109900, 7005, 109953, 4.0, 6.0)
    Event_13405550(8, 3400148, 7006, 109900, 7008, 109953, 0.0, 0.0)
    Event_13405300(1, 3400208, 0, 3.0, 0.0)
    Event_13405300(2, 3400209, 0, 3.0, 0.0)
    Event_13405300(3, 3400207, 0, 3.0, 0.0)
    Event_13405300(4, 3400210, 0, 3.0, 0.0)
    Event_13405300(7, 3400160, 3402506, 10.0, 0.0)
    Event_13405300(8, 3400309, 3402508, 10.0, 2.0)
    Event_13405300(9, 3400280, 3402510, 10.0, 0.0)
    Event_13405300(10, 3400281, 3402510, 10.0, 0.0)
    Event_13405300(15, 3400664, 3402536, 10.0, 0.0)
    Event_13405300(16, 3400510, 3402539, 10.0, 0.0)
    Event_13405300(17, 3400550, 3402538, 10.0, 0.0)
    Event_13405300(18, 3400580, 3402544, 5.0, 0.0)
    Event_13405350(0, 3400405, 3402512, 0, 3403303, 0.0, 0)
    Event_13405350(1, 3400204, 3402315, 0, 3403353, 0.0, 0)
    Event_13405350(2, 3400253, 3402315, 0, 3403354, 0.0, 0)
    Event_13405350(3, 3400508, 3402504, 0, 3403335, 0.0, 0)
    Event_13405350(4, 3400203, 3402504, 0, 3403335, 1.0, 0)
    Event_13405350(5, 3400200, 3402534, 0, 3403351, 0.0, 1)
    Event_13405350(6, 3400105, 3402512, 0, 3403356, 0.0, 1)
    Event_13405350(7, 3400106, 3402512, 0, 3403356, 4.0, 1)
    Event_13405350(8, 3400202, 3402505, 0, 3403339, 0.0, 0)
    Event_13405350(9, 3400252, 3402505, 0, 3403339, 0.0, 0)
    Event_13405350(10, 3400411, 3402360, 0, 3403310, 0.0, 0)
    Event_13405350(11, 3400601, 3402650, 0, 3403347, 0.0, 0)
    Event_13405350(12, 3400552, 3402558, 0, 3403348, 0.0, 0)
    Event_13405350(13, 3400105, 3402559, 0, 3403305, 0.0, 1)
    Event_13405350(14, 3400106, 3402559, 0, 3403305, 2.0, 1)
    Event_13405350(15, 3400665, 3402315, 0, 3403336, 0.0, 0)
    Event_13405350(16, 3400601, 3402555, 0, 3403347, 0.0, 1)
    Event_13405350(17, 3400137, 3402502, 0, 3403301, 1.0, 0)
    Event_13405350(18, 3400107, 3402513, 0, 3403352, 0.0, 1)
    Event_13405350(19, 3400412, 3402553, 0, 3403343, 0.0, 0)
    Event_13405350(20, 3400165, 3402526, 0, 3403311, 0.0, 0)
    Event_13405350(24, 3400166, 3402526, 0, 3403311, 0.0, 0)
    Event_13405350(25, 3400167, 3402526, 0, 3403311, 0.0, 0)
    Event_13405350(26, 3400168, 3402526, 0, 3403311, 0.0, 0)
    Event_13405350(27, 3400611, 3402561, 0, 3403315, 2.0, 0)
    Event_13405350(34, 3400158, 3402560, 0, 3403304, 0.0, 0)
    Event_13405350(35, 3400159, 3402560, 0, 3403304, 0.0, 0)
    Event_13405350(36, 3400160, 3402560, 0, 3403304, 0.0, 0)
    Event_13405350(37, 3400161, 3402560, 0, 3403304, 0.0, 0)
    Event_13405350(38, 3400162, 3402560, 0, 3403304, 0.0, 0)
    Event_13405350(39, 3400403, 3402517, 0, 3403302, 8.0, 1)
    Event_13405350(40, 3400303, 3402517, 0, 3403309, 16.0, 1)
    Event_13405350(41, 3400205, 3402304, 0, 3403307, 0.0, 1)
    Event_13405350(42, 3400206, 3402304, 0, 3403308, 0.0, 1)
    Event_13405350(43, 3400111, 3402552, 0, 3403355, 0.0, 1)
    Event_13405350(44, 3400112, 3402511, 0, 3403355, 0.0, 1)
    Event_13405350(45, 3400113, 3402511, 0, 3403355, 4.0, 1)
    Event_13405350(46, 3400130, 3402517, 0, 3403301, 8.0, 0)
    Event_13405350(47, 3400131, 3402500, 0, 3403306, 2.0, 0)
    Event_13405350(48, 3400132, 3402517, 0, 3403301, 9.0, 0)
    Event_13405350(49, 3400133, 3402517, 0, 3403301, 9.0, 0)
    Event_13405350(50, 3400134, 3402517, 0, 3403301, 8.0, 0)
    Event_13405350(51, 3400135, 3402502, 0, 3403301, 2.0, 0)
    Event_13405350(52, 3400137, 3402517, 0, 3403301, 9.0, 0)
    Event_13405350(53, 3400140, 3402517, 0, 3403301, 2.0, 0)
    Event_13405350(54, 3400149, 3402517, 0, 3403301, 7.0, 0)
    Event_13405350(55, 3400178, 3402517, 0, 3403314, 15.0, 1)
    Event_13405350(56, 3400179, 3402517, 0, 3403314, 15.0, 1)
    Event_13405350(57, 3400180, 3402517, 0, 3403314, 15.0, 1)
    Event_13405350(58, 3400181, 3402517, 0, 3403314, 9.0, 1)
    Event_13405350(59, 3400182, 3402517, 0, 3403314, 15.0, 1)
    Event_13405350(60, 3400183, 3402517, 0, 3403314, 15.0, 1)
    Event_13405350(61, 3400139, 3402508, 0, 3403358, 0.0, 0)
    Event_13405350(62, 3400136, 3402508, 0, 3403358, 0.0, 0)
    Event_13405350(63, 3400173, 3402500, 0, 3403312, 0.0, 0)
    Event_13405350(64, 3400610, 3402503, 0, 3403313, 0.0, 0)
    Event_13405350(65, 3400204, 3402316, 0, 3403353, 0.0, 0)
    Event_13405350(66, 3400253, 3402316, 0, 3403354, 0.0, 0)
    Event_13405350(21, 3400401, 3402535, 0, 3403331, 0.0, 0)
    Event_13405350(22, 3400143, 3402537, 0, 3403340, 0.0, 0)
    Event_13405350(23, 3400145, 3402537, 0, 3403340, 2.0, 0)
    Event_13405350(28, 3400110, 3402545, 0, 3403341, 5.0, 1)
    Event_13405350(29, 3400109, 3402545, 0, 3403341, 1.0, 1)
    Event_13405350(30, 3400144, 3402537, 0, 3403340, 0.0, 0)
    Event_13405350(32, 3400550, 3402555, 0, 3403346, 0.0, 0)
    Event_13405350(33, 3400580, 3402544, 0, 3403342, 0.0, 1)
    Event_13405510(1, character=3400141)
    Event_13405510(2, character=3400142)
    Event_13405510(3, character=3400143)
    Event_13405510(4, character=3400144)
    Event_13405510(5, character=3400145)
    Event_13405510(6, character=3400146)
    Event_13405510(7, character=3400147)
    Event_13405510(8, character=3400148)
    Event_13405610(0, character=3400169)
    Event_13405610(1, character=3400170)
    Event_13405610(2, character=3400171)
    Event_13405610(3, character=3400172)
    Event_13405520(1, character=3400141, region=3402541)
    Event_13405520(2, character=3400142, region=3402541)
    Event_13405520(3, character=3400143, region=3402541)
    Event_13405520(4, character=3400144, region=3402541)
    Event_13405520(5, character=3400145, region=3402541)
    Event_13405520(6, character=3400146, region=3402541)
    Event_13405520(7, character=3400147, region=3402541)
    Event_13405520(8, character=3400148, region=3402541)
    Event_13405530(0, character=3400143, region=3402549)
    Event_13405530(1, character=3400144, region=3402549)
    Event_13405530(2, character=3400145, region=3402549)
    Event_13405540(1, 3400142, 3403340, 2, 1, 0.0)
    Event_13405540(2, 3400155, 3403345, 2, 1, 2.0)
    Event_13405540(3, 3400316, 3403344, 4, 0, 0.0)
    Event_13405640(0, 3400404, 7000, 400028, 7001, 400028, 0.0, 0.0)
    Event_13405680(0, 3400165, 3400166, 13.0)
    Event_13405680(1, 3400165, 3400167, 13.0)
    Event_13405680(2, 3400165, 3400168, 13.0)
    Event_13405216(0, 3400509, 3402542, 0, 3403338, 1.0, 0)
    Event_13405480(0, 3400207, 3402515, 3.0, 3010, 0.0, 0)
    Event_13405480(1, 3400105, 3402512, 5.0, 7002, 0.0, 1)
    Event_13405480(2, 3400106, 3402512, 5.0, 7003, 4.0, 1)
    Event_13405480(3, 3400107, 3402513, 3.0, 7004, 0.0, 0)
    Event_13405480(4, 3400505, 3402553, 3.0, 700, 1.0, 0)
    Event_13405480(5, 3400506, 3402553, 3.0, 700, 0.0, 0)
    Event_13405480(6, 3400282, 3402303, 3.0, 3006, 0.0, 0)
    Event_13405480(8, 3400507, 3402553, 3.0, 605, 0.0, 0)
    Event_13405480(9, 3400468, 3402562, 0.0, 3001, 1.0, 0)
    Event_13405480(10, 3400469, 3402562, 0.0, 3001, 0.0, 0)
    Event_13405480(13, 3400472, 3402562, 0.0, 3001, 2.0, 0)
    Event_13405480(11, 3400315, 3402540, 1.0, 702, 2.0, 0)
    Event_13405480(12, 3400409, 3402552, 1.0, 3012, 0.0, 0)
    Event_13400930()
    Event_13400900(2, character=3400902, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1710)
    Event_13400900(3, character=3400903, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1711)
    Event_13400910(2, attacked_entity=3400902, flag=73400420)
    Event_13400910(3, attacked_entity=3400903, flag=73400421)
    Event_13400920(2, character=3400902, flag=73400420, first_flag=1710, last_flag=1729, flag_1=1725)
    Event_13400920(3, character=3400903, flag=73400421, first_flag=1710, last_flag=1729, flag_1=1726)
    Event_13400970(0, character=3400910)
    Event_13400970(1, character=3400911)
    Event_13400980(0, flag=73400424, item_lot_param_id=43211)
    Event_13400953(0, flag=1710, flag_1=73400430, item_lot_param_id=43200)
    Event_13400953(1, flag=1711, flag_1=73400431, item_lot_param_id=43210)
    Event_13400995(0, flag=13400970, item_lot_param_id=43800, item_lot_param_id_1=43802, flag_1=6671)
    Event_13400980(1, flag=13400971, item_lot_param_id=43810)
    GotoIfFlagEnabled(Label.L2, flag=13400999)
    Event_13400941()
    Event_13400942(0, flag=73400512)
    Event_13400943(0, attacked_entity=3400900)
    Event_13400944()
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(3400900)

    # --- 3 --- #
    DefineLabel(3)
    Event_13400951(0, character=3400902, flag=73400422, flag_1=1720)
    Event_13400951(1, character=3400903, flag=73400423, flag_1=1721)
    DeleteVFX(3403911, erase_root_only=False)
    DeleteVFX(3403912, erase_root_only=False)
    DeleteVFX(3403913, erase_root_only=False)
    DeleteVFX(3403914, erase_root_only=False)
    DeleteVFX(3403915, erase_root_only=False)
    DeleteVFX(3403916, erase_root_only=False)
    Event_13404401(0, flag=13404441, vfx_id=3403911, flag_1=13404421, flag_2=13404431, flag_3=13401800, flag_4=6001)
    Event_13404402(0, flag=13404442, vfx_id=3403912, flag_1=13404422, flag_2=13404432, flag_3=13401800, flag_4=13404421)
    Event_13404403(0, flag=13404443, vfx_id=3403913, flag_1=13404423, flag_2=13404433, flag_3=13401800, flag_4=13404421)
    Event_13404404(0, flag=13404444, vfx_id=3403914, flag_1=13404424, flag_2=13404434, flag_3=13401800, flag_4=13404421)
    Event_13404405(0, flag=13404445, vfx_id=3403915, flag_1=13404425, flag_2=13404435, flag_3=13401850, flag_4=13404421)
    Event_13404406(0, flag=13404446, vfx_id=3403916, flag_1=13404426, flag_2=13404436, flag_3=13401850, flag_4=13404421)
    Event_13404410(
        1,
        sign_type=0,
        character=3400921,
        region=3402921,
        summon_flag=13404421,
        dismissal_flag=13404431,
        flag=13404441,
        flag_1=13401800,
        action_button_id=10567
    )
    Event_13404410(
        2,
        sign_type=6,
        character=3400922,
        region=3402922,
        summon_flag=13404422,
        dismissal_flag=13404432,
        flag=13404442,
        flag_1=13401800,
        action_button_id=10562
    )
    Event_13404410(
        3,
        sign_type=6,
        character=3400923,
        region=3402923,
        summon_flag=13404423,
        dismissal_flag=13404433,
        flag=13404443,
        flag_1=13401800,
        action_button_id=10563
    )
    Event_13404410(
        4,
        sign_type=5,
        character=3400924,
        region=3402924,
        summon_flag=13404424,
        dismissal_flag=13404434,
        flag=13404444,
        flag_1=13401800,
        action_button_id=10565
    )
    Event_13404410(
        5,
        sign_type=6,
        character=3400925,
        region=3402925,
        summon_flag=13404425,
        dismissal_flag=13404435,
        flag=13404445,
        flag_1=13401850,
        action_button_id=10562
    )
    Event_13404410(
        6,
        sign_type=6,
        character=3400926,
        region=3402926,
        summon_flag=13404426,
        dismissal_flag=13404436,
        flag=13404446,
        flag_1=13401850,
        action_button_id=10563
    )
    Event_13404450(1, character=3400921, region=3402930, flag=13404421, flag_1=13404431, flag_2=13404808)
    Event_13404450(2, character=3400922, region=3402931, flag=13404422, flag_1=13404432, flag_2=13404808)
    Event_13404450(3, character=3400923, region=3402931, flag=13404423, flag_1=13404433, flag_2=13404808)
    Event_13404450(4, character=3400924, region=3402932, flag=13404424, flag_1=13404434, flag_2=13404808)
    Event_13404450(5, character=3400925, region=3402935, flag=13404425, flag_1=13404435, flag_2=13404858)
    Event_13404450(6, character=3400926, region=3402935, flag=13404426, flag_1=13404436, flag_2=13404858)
    Event_13404460(
        1,
        character=3400921,
        region=3402930,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404451,
        region_3=3402801
    )
    Event_13404460(
        2,
        character=3400922,
        region=3402931,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404452,
        region_3=3402801
    )
    Event_13404460(
        3,
        character=3400923,
        region=3402931,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404453,
        region_3=3402801
    )
    Event_13404460(
        4,
        character=3400924,
        region=3402932,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404454,
        region_3=3402801
    )
    Event_13404460(
        5,
        character=3400925,
        region=3402935,
        region_1=3402850,
        region_2=3402851,
        animation=101130,
        flag=13404455,
        region_3=3402851
    )
    Event_13404460(
        6,
        character=3400926,
        region=3402935,
        region_1=3402850,
        region_2=3402851,
        animation=101130,
        flag=13404456,
        region_3=3402851
    )
    Event_13404490(0, character=3400925, flag=13404425, flag_1=13404435, flag_2=13404858)
    Event_13404490(1, character=3400926, flag=13404426, flag_1=13404436, flag_2=13404858)
    SetEventPoint(3400911, region=3402910, reaction_range=0.0)
    Event_13401250(0, other_entity=3401250, animation_id=0)
    Event_13401250(1, other_entity=3401251, animation_id=0)
    Event_13401250(2, other_entity=3401252, animation_id=0)
    Event_13401250(3, other_entity=3401253, animation_id=0)
    Event_13401250(4, other_entity=3401254, animation_id=0)
    Event_13401250(5, other_entity=3401255, animation_id=0)
    Event_13401250(6, other_entity=3401256, animation_id=0)
    Event_13401250(7, other_entity=3401257, animation_id=0)
    Event_13401250(8, other_entity=3401258, animation_id=0)
    Event_13401250(9, other_entity=3401259, animation_id=0)
    Event_13401250(10, other_entity=3401260, animation_id=0)
    Event_13401250(11, other_entity=3401261, animation_id=0)
    Event_13401250(12, other_entity=3401262, animation_id=0)
    Event_13401250(13, other_entity=3401263, animation_id=0)
    Event_13401250(14, other_entity=3401264, animation_id=0)
    Event_13401250(15, other_entity=3401265, animation_id=0)
    Event_13401250(16, other_entity=3401266, animation_id=0)
    Event_13401250(17, other_entity=3401267, animation_id=0)
    Event_13401250(18, other_entity=3401268, animation_id=0)
    Event_13401250(19, other_entity=3401269, animation_id=0)
    Event_13401250(20, other_entity=3401270, animation_id=0)
    Event_13401250(21, other_entity=3401271, animation_id=0)
    Event_13401250(22, other_entity=3401272, animation_id=0)
    Event_13401250(23, other_entity=3401273, animation_id=0)
    Event_13401250(24, other_entity=3401274, animation_id=0)
    Event_13401250(25, other_entity=3401275, animation_id=0)
    Event_13401250(26, other_entity=3401276, animation_id=0)
    Event_13401250(27, other_entity=3401277, animation_id=0)
    Event_13401250(28, other_entity=3401278, animation_id=0)
    Event_13401250(29, other_entity=3401279, animation_id=0)
    Event_13401250(30, other_entity=3401280, animation_id=0)
    Event_13401250(31, other_entity=3401281, animation_id=0)
    Event_13401250(32, other_entity=3401282, animation_id=0)
    Event_13401250(33, other_entity=3401283, animation_id=0)
    Event_13401250(34, other_entity=3401284, animation_id=0)
    Event_13401250(35, other_entity=3401285, animation_id=0)
    Event_13401250(36, other_entity=3401286, animation_id=0)
    Event_13401250(37, other_entity=3401287, animation_id=0)
    Event_13401250(38, other_entity=3401288, animation_id=0)
    Event_13401250(39, other_entity=3401289, animation_id=0)
    Event_13401250(40, other_entity=3401290, animation_id=0)
    Event_13401250(41, other_entity=3401291, animation_id=0)
    Event_13401250(42, other_entity=3401292, animation_id=0)
    Event_13401250(43, other_entity=3401293, animation_id=0)
    Event_13401350(0, other_entity=3401294, animation_id=0, region=3402547)
    Event_13401350(1, other_entity=3401295, animation_id=0, region=3402547)
    Event_13401350(2, other_entity=3401296, animation_id=0, region=3402547)
    Event_13401350(3, other_entity=3401297, animation_id=0, region=3402547)
    Event_13401350(4, other_entity=3401298, animation_id=0, region=3402547)
    Event_13401350(5, other_entity=3401299, animation_id=0, region=3402547)
    Event_13401350(6, other_entity=3401300, animation_id=0, region=3402547)
    Event_13401350(7, other_entity=3401301, animation_id=0, region=3402547)
    Event_13401350(8, other_entity=3401302, animation_id=0, region=3402547)
    Event_13401350(9, other_entity=3401303, animation_id=0, region=3402547)
    Event_13401350(10, other_entity=3401304, animation_id=0, region=3402547)
    Event_13400998()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_13400940()
    Event_13400950(0, 3400902, 3400903)


@NeverRestart(13400010)
def Event_13400010():
    """Event 13400010"""
    DisableNetworkSync()
    DisableObject(3401801)
    DeleteVFX(3403801)
    IfConnectingMultiplayer(-1)
    IfMultiplayer(-1)
    IfFlagDisabled(-1, 9471)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(3401801)
    CreateVFX(3403801)
    IfConnectingMultiplayer(-2)
    IfMultiplayer(-2)
    IfConditionFalse(1, input_condition=-2)
    IfFlagEnabled(1, 9471)
    IfConditionTrue(0, input_condition=1)
    Restart()


@RestartOnRest(13400998)
def Event_13400998():
    """Event 13400998"""
    GotoIfFlagEnabled(Label.L0, flag=13400999)
    DisableCharacter(3400316)
    DisableCharacter(3400509)
    DisableCharacter(3400550)
    DisableCharacter(3400143)
    DisableCharacter(3400144)
    DisableCharacter(3400142)
    DisableCharacter(3400141)
    DisableCharacter(3400145)
    DisableCharacter(3400146)
    DisableCharacter(3400147)
    DisableCharacter(3400148)
    DisableCharacter(3400155)
    DisableCharacter(3400452)
    DisableCharacter(3400453)
    DisableCharacter(3400461)
    DisableCharacter(3400462)
    DisableCharacter(3400470)
    DisableCharacter(3400471)
    DisableObject(3401180)
    DisableObject(3401181)
    DisableObject(3401182)
    DisableObject(3401183)
    DisableObject(3401184)
    DisableObject(3401185)
    DisableObject(3401186)
    DisableObject(3401187)
    DisableObject(3401188)
    DisableObject(3401189)
    DisableObject(3401190)
    DisableObject(3401191)
    DisableObject(3401192)
    DisableObject(3401193)
    DisableObject(3401194)
    DisableTreasure(obj=3401180)
    DisableTreasure(obj=3401181)
    DisableTreasure(obj=3401182)
    DisableTreasure(obj=3401183)
    DisableTreasure(obj=3401184)
    DisableTreasure(obj=3401185)
    DisableTreasure(obj=3401186)
    DisableTreasure(obj=3401187)
    DisableTreasure(obj=3401188)
    DisableTreasure(obj=3401189)
    DisableTreasure(obj=3401190)
    DisableTreasure(obj=3401191)
    DisableTreasure(obj=3401192)
    DisableTreasure(obj=3401193)
    DisableCharacter(3400920)
    DeleteVFX(3403910)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(3400601)
    DisableCharacter(3400552)
    DisableCharacter(3400511)
    DisableCharacter(3400409)
    DisableCharacter(3400412)
    DisableCharacter(3400413)
    DisableCharacter(3400510)
    DisableCharacter(3400465)
    DisableCharacter(3400466)
    DisableCharacter(3400467)
    DisableCharacter(3400468)
    DisableCharacter(3400469)
    DisableCharacter(3400655)
    DisableObject(3401195)
    DisableObject(3401196)
    DisableObject(3401197)
    DisableObject(3401198)
    DisableObject(3401199)
    DisableObject(3401200)
    DisableObject(3401201)
    DisableObject(3401202)
    DisableObject(3401203)
    DisableObject(3401204)
    DisableObject(3401205)
    DisableObject(3401206)
    DisableObject(3401207)
    DisableTreasure(obj=3401195)
    DisableTreasure(obj=3401196)
    DisableTreasure(obj=3401197)
    DisableTreasure(obj=3401198)
    DisableTreasure(obj=3401199)
    DisableTreasure(obj=3401200)
    DisableTreasure(obj=3401201)
    DisableTreasure(obj=3401202)
    DisableTreasure(obj=3401203)
    DisableTreasure(obj=3401204)
    DisableTreasure(obj=3401205)
    DisableTreasure(obj=3401206)
    DisableTreasure(obj=3401207)


@NeverRestart(13401250)
def Event_13401250(_, other_entity: int, animation_id: int):
    """Event 13401250"""
    DisableNetworkSync()
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=other_entity, radius=5.0)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(other_entity, 6, wait_for_completion=True)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=other_entity, radius=5.0)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(other_entity, animation_id, wait_for_completion=True)
    Restart()


@NeverRestart(13401350)
def Event_13401350(_, other_entity: int, animation_id: int, region: int):
    """Event 13401350"""
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=region)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(other_entity, 6, wait_for_completion=True)
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=other_entity, radius=5.0)

    # --- 0 --- #
    DefineLabel(0)
    WaitRandomFrames(min_frames=0, max_frames=75)
    ForceAnimation(other_entity, animation_id, wait_for_completion=True)
    Restart()


@NeverRestart(13401500)
def Event_13401500():
    """Event 13401500"""
    GotoIfFlagEnabled(Label.L0, flag=9469)
    DisableObject(3400600)
    IfFlagEnabled(0, 9469)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=3404200)
    DisableMapPiece(map_piece_id=3404201)
    DisableMapPiece(map_piece_id=3404202)
    DisableMapPiece(map_piece_id=3404203)
    DeleteVFX(3403600)
    DeleteVFX(3403601)
    DeleteVFX(3403602)
    EnableObject(3400600)


@NeverRestart(13401000)
def Event_13401000():
    """Event 13401000"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 12401000)
    DisableFlag(12401000)
    AddSpecialEffect(PLAYER, 110)
    AddSpecialEffect(PLAYER, 111)
    AddSpecialEffect(PLAYER, 112)
    AddSpecialEffect(PLAYER, 113)
    AddSpecialEffect(PLAYER, 114)
    AddSpecialEffect(PLAYER, 115)
    AddSpecialEffect(PLAYER, 116)
    SetRespawnPoint(respawn_point=3402958)
    EndIfThisEventFlagEnabled()
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest(13404700)
def Event_13404700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13404700"""
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(flag)
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    IfOnline(1)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfInsideMap(1, game_map=HUNTERS_NIGHTMARE)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    SkipLinesIfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(
        2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, flag_3)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13404710)
def Event_13404710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404710"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfInsideMap(1, game_map=HUNTERS_NIGHTMARE)
    IfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest(13404720)
def Event_13404720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404720"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_2)
    IfFlagEnabled(-1, flag_1)
    IfClientTypeCountComparison(
        -1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfOutsideMap(-1, game_map=HUNTERS_NIGHTMARE)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(character, 9100)
    ReplanAI(character)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(13404730)
def Event_13404730(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
):
    """Event 13404730"""
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    IfFlagEnabled(-15, flag_3)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_5)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(-1, flag_3)
    IfFlagEnabled(-1, 13404860)
    IfFlagEnabled(-1, flag_6)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-1)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@RestartOnRest(13404740)
def Event_13404740():
    """Event 13404740"""
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3404000)
    IfPlayerStandingOnCollision(-1, 3404001)
    IfPlayerStandingOnCollision(-1, 3404002)
    IfPlayerStandingOnCollision(-1, 3404003)
    IfPlayerStandingOnCollision(-1, 3404004)
    IfPlayerStandingOnCollision(-1, 3404005)
    IfPlayerStandingOnCollision(-1, 3404006)
    IfPlayerStandingOnCollision(-1, 3404007)
    IfPlayerStandingOnCollision(-1, 3404008)
    IfPlayerStandingOnCollision(-1, 3404009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13404741)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3404000)
    IfPlayerStandingOnCollision(-2, 3404001)
    IfPlayerStandingOnCollision(-2, 3404002)
    IfPlayerStandingOnCollision(-2, 3404003)
    IfPlayerStandingOnCollision(-2, 3404004)
    IfPlayerStandingOnCollision(-2, 3404005)
    IfPlayerStandingOnCollision(-2, 3404006)
    IfPlayerStandingOnCollision(-2, 3404007)
    IfPlayerStandingOnCollision(-2, 3404008)
    IfPlayerStandingOnCollision(-2, 3404009)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13404741)
    Restart()


@RestartOnRest(13404742)
def Event_13404742():
    """Event 13404742"""
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3404020)
    IfPlayerStandingOnCollision(-1, 3404021)
    IfPlayerStandingOnCollision(-1, 3404022)
    IfPlayerStandingOnCollision(-1, 3404023)
    IfPlayerStandingOnCollision(-1, 3404024)
    IfPlayerStandingOnCollision(-1, 3404025)
    IfPlayerStandingOnCollision(-1, 3404026)
    IfPlayerStandingOnCollision(-1, 3404027)
    IfPlayerStandingOnCollision(-1, 3404028)
    IfPlayerStandingOnCollision(-1, 3404029)
    IfPlayerStandingOnCollision(-1, 3404030)
    IfPlayerStandingOnCollision(-1, 3404031)
    IfPlayerStandingOnCollision(-1, 3404032)
    IfPlayerStandingOnCollision(-1, 3404033)
    IfPlayerStandingOnCollision(-1, 3404034)
    IfPlayerStandingOnCollision(-1, 3404035)
    IfPlayerStandingOnCollision(-1, 3404036)
    IfPlayerStandingOnCollision(-1, 3404037)
    IfPlayerStandingOnCollision(-1, 3404038)
    IfPlayerStandingOnCollision(-1, 3404039)
    IfPlayerStandingOnCollision(-1, 3404040)
    IfPlayerStandingOnCollision(-1, 3404041)
    IfPlayerStandingOnCollision(-1, 3404042)
    IfPlayerStandingOnCollision(-1, 3404043)
    IfPlayerStandingOnCollision(-1, 3404044)
    IfPlayerStandingOnCollision(-1, 3404045)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13404743)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3404020)
    IfPlayerStandingOnCollision(-2, 3404021)
    IfPlayerStandingOnCollision(-2, 3404022)
    IfPlayerStandingOnCollision(-2, 3404023)
    IfPlayerStandingOnCollision(-2, 3404024)
    IfPlayerStandingOnCollision(-2, 3404025)
    IfPlayerStandingOnCollision(-2, 3404026)
    IfPlayerStandingOnCollision(-2, 3404027)
    IfPlayerStandingOnCollision(-2, 3404028)
    IfPlayerStandingOnCollision(-2, 3404029)
    IfPlayerStandingOnCollision(-2, 3404030)
    IfPlayerStandingOnCollision(-2, 3404031)
    IfPlayerStandingOnCollision(-2, 3404032)
    IfPlayerStandingOnCollision(-2, 3404033)
    IfPlayerStandingOnCollision(-2, 3404034)
    IfPlayerStandingOnCollision(-2, 3404035)
    IfPlayerStandingOnCollision(-2, 3404036)
    IfPlayerStandingOnCollision(-2, 3404037)
    IfPlayerStandingOnCollision(-2, 3404038)
    IfPlayerStandingOnCollision(-2, 3404039)
    IfPlayerStandingOnCollision(-2, 3404040)
    IfPlayerStandingOnCollision(-2, 3404041)
    IfPlayerStandingOnCollision(-2, 3404042)
    IfPlayerStandingOnCollision(-2, 3404043)
    IfPlayerStandingOnCollision(-2, 3404044)
    IfPlayerStandingOnCollision(-2, 3404045)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13404743)
    Restart()


@NeverRestart(13401800)
def Event_13401800():
    """Event 13401800"""
    GotoIfFlagDisabled(Label.L0, flag=9471)
    DisableCharacter(3400800)
    DisableCharacter(3400801)
    Kill(3400800)
    Kill(3400801)
    DisableObject(3401800)
    DeleteVFX(3403800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 3400800)
    IfConditionTrue(-1, input_condition=1)
    SkipLinesIfFlagEnabled(2, 13400999)
    IfCharacterDead(2, 3400801)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401800)
    DeleteVFX(3403800)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    KillBoss(game_area_param_id=3400800)
    SkipLines(1)
    KillBoss(game_area_param_id=3400801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    SkipLinesIfFlagDisabled(4, 13400999)
    Wait(3.0)
    PlayCutscene(34000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Unknown_2003_27(arg1=0)
    AwardAchievement(achievement_id=36)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagEnabled(2, 6674)
    AwardItemLot(3401800, host_only=False)
    SkipLines(1)
    AwardItemLot(3401802, host_only=False)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    EnableFlag(9471)
    StopPlayLogMeasurement(measurement_id=9340000)
    StopPlayLogMeasurement(measurement_id=9340001)
    StopPlayLogMeasurement(measurement_id=9340010)
    CreatePlayLog(name=0)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=12,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(13404811)
def Event_13404811():
    """Event 13404811"""
    EndIfFlagEnabled(9471)
    EndIfFlagEnabled(13401801)
    DisableCharacter(3400800)
    IfFlagDisabled(1, 13401800)
    IfFlagDisabled(1, 13401801)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3402805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404810)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)


@NeverRestart(13401801)
def Event_13401801():
    """Event 13401801"""
    EndIfFlagEnabled(9471)
    EndIfThisEventFlagEnabled()
    IfCharacterType(1, PLAYER, character_type=CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagDisabled(2, 13401800)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(2, 13404811)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3402805)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(34000020, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(34000020, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(1)
    PlayCutscene(34000020, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(13404808)
    EnableCharacter(3400800)
    EndIfFlagEnabled(9344)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9344)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@NeverRestart(13401802)
def Event_13401802():
    """Event 13401802"""
    EndIfFlagEnabled(13401803)
    EndIfFlagEnabled(13401800)
    EnableInvincibility(3400810)
    IfFlagEnabled(0, 13401801)
    AddSpecialEffect(3400810, 5401)
    DisableInvincibility(3400810)
    ForceAnimation(3400810, 3000)
    IfCharacterAlive(1, 3400810)
    IfFlagEnabled(1, 13401800)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3400810, 7000)


@RestartOnRest(13401803)
def Event_13401803():
    """Event 13401803"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DropMandatoryTreasure(3400810)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3400810)
    Wait(0.0)


@NeverRestart(13401804)
def Event_13401804():
    """Event 13401804"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13404808)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(3400800)
    EnableFlag(13404808)
    EnableFlag(13401801)


@NeverRestart(13404800)
def Event_13404800():
    """Event 13404800"""
    EndIfFlagEnabled(9471)
    GotoIfFlagEnabled(Label.L0, flag=13401801)
    SkipLinesIfClient(2)
    DisableObject(3401800)
    DeleteVFX(3403800, erase_root_only=False)
    IfFlagDisabled(1, 13401800)
    IfFlagEnabled(1, 13401801)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3401800)
    CreateVFX(3403800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13401800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=3400800, entity=3401800)
    IfFlagEnabled(3, 13401800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3402801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(13404808)
    Restart()


@NeverRestart(13404801)
def Event_13404801():
    """Event 13404801"""
    DisableNetworkSync()
    EndIfFlagEnabled(9471)
    IfFlagDisabled(1, 13401800)
    IfFlagEnabled(1, 13401801)
    IfFlagEnabled(1, 13404808)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=3400800, entity=3401800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3402801)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(13404809)
    Restart()


@NeverRestart(13404802)
def Event_13404802():
    """Event 13404802"""
    EndIfFlagEnabled(9471)
    DisableAI(3400800)
    DisableAI(3400801)
    DisableHealthBar(3400800)
    DisableHealthBar(3400801)
    ReferDamageToEntity(3400800, target_entity=3400801)
    SkipLinesIfFlagDisabled(2, 13400999)
    AddSpecialEffect(3400800, 8040)
    AddSpecialEffect(3400801, 8040)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13404808)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13404810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3400801, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13404810)
    EnableFlag(13404808)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400801)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400801)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagEnabled(5, 13404825)
    EnableAI(3400800)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.EveryTwoFrames)
    EnableBossHealthBar(3400800, name=451000)
    SkipLines(4)
    EnableAI(3400801)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3400801, name=451005)
    CreatePlayLog(name=46)
    StartPlayLogMeasurement(measurement_id=3400010, name=62, overwrite=True)


@NeverRestart(13404803)
def Event_13404803():
    """Event 13404803"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3403802)
    DisableSoundEvent(sound_id=3403803)
    EndIfFlagEnabled(9471)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, 13401800)
    IfFlagEnabled(1, 13404802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13404809)
    IfCharacterInsideRegion(1, PLAYER, region=3402802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3403802)
    IfFlagEnabled(2, 13404824)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13401800)
    IfFlagEnabled(2, 13404802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13404809)
    IfCharacterInsideRegion(2, PLAYER, region=3402802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3403802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3403803)


@NeverRestart(13404804)
def Event_13404804():
    """Event 13404804"""
    DisableNetworkSync()
    EndIfFlagEnabled(9471)
    IfFlagEnabled(0, 13404825)
    IfCharacterAlive(3, 3400801)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=3400801, radius=9.0)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(4, 3400801)
    IfEntityBeyondDistance(4, entity=PLAYER, other_entity=3400801, radius=12.0)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


@NeverRestart(13404805)
def Event_13404805():
    """Event 13404805"""
    DisableNetworkSync()
    EndIfFlagEnabled(9471)
    IfFlagEnabled(0, 13401800)
    DisableBossMusic(sound_id=3403802)
    DisableBossMusic(sound_id=3403803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13404806)
def Event_13404806():
    """Event 13404806"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3401800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13404807)
def Event_13404807():
    """Event 13404807"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3401800, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3401800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13404820)
def Event_13404820():
    """Event 13404820"""
    EndIfFlagEnabled(9471)
    IfFlagEnabled(1, 13400999)
    IfHealthLessThan(1, 3400800, value=0.8999999761581421)
    IfConditionTrue(-1, input_condition=1)
    IfFlagDisabled(2, 13400999)
    IfHealthLessThan(2, 3400800, value=0.8999999761581421)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterHasTAEEvent(3, 3400800, tae_event_id=10)
    IfCharacterHasTAEEvent(4, 3400800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(3400800, command_id=100, command_slot=0)
    IfCharacterHasTAEEvent(0, 3400800, tae_event_id=20)
    AICommand(3400800, command_id=-1, command_slot=0)


@NeverRestart(13404821)
def Event_13404821():
    """Event 13404821"""
    EndIfFlagEnabled(9471)
    IfFlagEnabled(1, 13400999)
    IfHealthLessThan(1, 3400800, value=0.800000011920929)
    IfConditionTrue(-1, input_condition=1)
    IfFlagDisabled(2, 13400999)
    IfHealthLessThan(2, 3400800, value=0.8500000238418579)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagEnabled(3, 13404820)
    IfCharacterHasTAEEvent(4, 3400800, tae_event_id=30)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(3400800, command_id=101, command_slot=0)
    IfCharacterHasTAEEvent(0, 3400800, tae_event_id=30)
    AICommand(3400800, command_id=-1, command_slot=0)


@NeverRestart(13404822)
def Event_13404822():
    """Event 13404822"""
    EndIfFlagEnabled(9471)
    IfFlagEnabled(1, 13400999)
    IfHealthLessThan(1, 3400800, value=0.699999988079071)
    IfConditionTrue(-1, input_condition=1)
    IfFlagDisabled(2, 13400999)
    IfHealthLessThan(2, 3400800, value=0.800000011920929)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagEnabled(3, 13404821)
    IfCharacterHasTAEEvent(4, 3400800, tae_event_id=40)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(3400800, command_id=102, command_slot=0)
    IfCharacterHasTAEEvent(0, 3400800, tae_event_id=40)
    AICommand(3400800, command_id=-1, command_slot=0)


@NeverRestart(13404823)
def Event_13404823():
    """Event 13404823"""
    EndIfFlagEnabled(9471)
    IfFlagEnabled(1, 13400999)
    IfHealthLessThan(1, 3400800, value=0.5)
    IfConditionTrue(-1, input_condition=1)
    IfFlagDisabled(2, 13400999)
    IfHealthLessThan(2, 3400800, value=0.75)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagEnabled(3, 13404822)
    IfCharacterHasTAEEvent(4, 3400800, tae_event_id=50)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(3400800, command_id=103, command_slot=0)
    IfCharacterHasTAEEvent(0, 3400800, tae_event_id=50)
    AICommand(3400800, command_id=-1, command_slot=0)


@NeverRestart(13404824)
def Event_13404824():
    """Event 13404824"""
    EndIfFlagEnabled(9471)
    EndIfFlagEnabled(13404825)
    IfHealthLessThan(1, 3400800, value=0.5)
    IfHealthGreaterThan(1, 3400800, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)


@NeverRestart(13404825)
def Event_13404825():
    """Event 13404825"""
    EndIfFlagEnabled(9471)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3400800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(3400801)
    DisableAnimations(3400801)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13404824)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(34000030, cutscene_flags=0, player_id=10000, move_to_region=3402807, game_map=HUNTERS_NIGHTMARE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        34000030,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3402807,
        game_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(1)
    PlayCutscene(34000030, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableBossHealthBar(3400800, name=451000)
    DisableFlag(9180)
    DisableCharacter(3400800)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    MoveToEntity(3400800, destination=3402900, destination_type=CoordEntityType.Region)
    Move(3400801, destination=3402806, destination_type=CoordEntityType.Region, copy_draw_parent=3400800)
    EnableGravity(3400801)
    EnableAnimations(3400801)
    ForceAnimation(3400801, 7000)
    WaitFrames(frames=96)
    CancelSpecialEffect(3400801, 5300)
    AddSpecialEffect(3400801, 5333)
    EnableAI(3400801)
    EnableBossHealthBar(3400801, name=451005)


@NeverRestart(13404830)
def Event_13404830(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    animation_id: int,
    frames: int,
):
    """Event 13404830"""
    EndIfFlagEnabled(9471)
    CreateNPCPart(3400800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(3400800, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, 3400800, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(-1, 3400800, value=0.0)
    IfFlagEnabled(-1, 13404825)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=-1)
    CreateNPCPart(3400800, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999, damage_correction=1.5)
    SetNPCPartEffects(3400800, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    ForceAnimation(3400800, animation_id)
    AddSpecialEffect(3400800, special_effect_id)
    WaitFrames(frames=frames)
    IfFramesElapsed(3, frames=frames)
    IfHealthLessThanOrEqual(-3, 3400800, value=0.0)
    IfFlagEnabled(-3, 13404825)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=-3)
    IfConditionTrue(0, input_condition=-4)
    EndIfFinishedConditionTrue(input_condition=-3)
    ReplanAI(3400800)
    IfTimeElapsed(4, seconds=5.0)
    IfHealthLessThanOrEqual(-5, 3400800, value=0.0)
    IfFlagEnabled(-5, 13404825)
    IfConditionTrue(-6, input_condition=4)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)
    EndIfFinishedConditionTrue(input_condition=-5)
    SetNPCPartHealth(3400800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    CancelSpecialEffect(3400800, special_effect_id)
    WaitFrames(frames=10)
    IfFramesElapsed(5, frames=10)
    IfHealthLessThanOrEqual(-7, 3400800, value=0.0)
    IfFlagEnabled(-7, 13404825)
    IfConditionTrue(-8, input_condition=5)
    IfConditionTrue(-8, input_condition=-7)
    IfConditionTrue(0, input_condition=-8)
    EndIfFinishedConditionTrue(input_condition=-7)
    Restart()


@NeverRestart(13404835)
def Event_13404835():
    """Event 13404835"""
    EndIfFlagEnabled(9471)
    IfHealthLessThan(1, 3400801, value=0.3499999940395355)
    IfHealthGreaterThan(1, 3400801, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3400801, 7002)
    AICommand(3400801, command_id=110, command_slot=0)
    ReplanAI(3400801)
    IfHealthLessThan(3, 3400801, value=0.06700000166893005)
    IfHealthGreaterThan(3, 3400801, value=0.0)
    IfConditionTrue(0, input_condition=3)
    ForceAnimation(3400801, 7003)
    IfHealthLessThan(4, 3400801, value=0.032999999821186066)
    IfHealthGreaterThan(4, 3400801, value=0.0)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(3400801, 7002)


@NeverRestart(13404840)
def Event_13404840():
    """Event 13404840"""
    EndIfFlagEnabled(9471)
    IfCharacterHasTAEEvent(0, 3400800, tae_event_id=100)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableCharacter(3400800)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(vfx_id=645114, anchor_entity=PLAYER, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(1.2000000476837158)
    EnableCharacter(3400800)
    Move(3400800, destination=PLAYER, destination_type=CoordEntityType.Character, model_point=236, short_move=True)
    ForceAnimation(3400800, 3017)
    Restart()


@NeverRestart(13404841)
def Event_13404841():
    """Event 13404841"""
    EndIfFlagEnabled(9471)
    IfCharacterHasTAEEvent(0, 3400801, tae_event_id=300)
    AICommand(3400801, command_id=-1, command_slot=0)
    ReplanAI(3400801)


@NeverRestart(13401850)
def Event_13401850():
    """Event 13401850"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=3403802)
    DisableSoundEvent(sound_id=3403803)
    DisableCharacter(3400850)
    Kill(3400850, award_souls=True)
    DisableObject(3401850)
    DeleteVFX(3403850)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3400850)
    EnableFlag(3400)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401850)
    DeleteVFX(3403850)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=3400850)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(achievement_id=39)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagEnabled(2, 6673)
    AwardItemLot(3401850, host_only=False)
    SkipLines(1)
    AwardItemLot(3401852, host_only=False)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    StopPlayLogMeasurement(measurement_id=3400020)
    StopPlayLogMeasurement(measurement_id=3400021)
    StopPlayLogMeasurement(measurement_id=3400030)
    CreatePlayLog(name=0)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=80,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=80,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=80,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=80,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@RestartOnRest(13404861)
def Event_13404861():
    """Event 13404861"""
    EndIfFlagEnabled(13401850)
    GotoIfFlagDisabled(Label.L0, flag=13401851)
    Move(3400850, destination=3402853, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(3400850)
    DisableGravity(3400850)
    EnableInvincibility(3400850)
    ForceAnimation(3400850, 7002, loop=True)
    IfFlagDisabled(1, 13401850)
    IfFlagDisabled(1, 13401851)
    IfPlayerHasGood(1, 4014)
    IfCharacterInsideRegion(1, PLAYER, region=3402855)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404860)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)


@RestartOnRest(13401851)
def Event_13401851():
    """Event 13401851"""
    EndIfFlagEnabled(13401850)
    EndIfThisEventFlagEnabled()
    IfCharacterType(1, PLAYER, character_type=CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagDisabled(2, 13401850)
    IfFlagDisabled(2, 13401851)
    IfFlagEnabled(2, 13404861)
    IfPlayerHasGood(2, 4014)
    IfCharacterInsideRegion(2, PLAYER, region=3402855)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(34000010, cutscene_flags=0, player_id=10000, move_to_region=3402856, game_map=HUNTERS_NIGHTMARE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        34000010,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3402856,
        game_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(1)
    PlayCutscene(34000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(13404858)
    Move(3400850, destination=3402853, destination_type=CoordEntityType.Region, short_move=True)
    EnableGravity(3400850)
    DisableInvincibility(3400850)
    EnableCharacterCollision(3400850)
    ForceAnimation(3400850, 3029)
    EndIfFlagEnabled(9302)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9302)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


@NeverRestart(13401853)
def Event_13401853():
    """Event 13401853"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13404858)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableGravity(3400850)
    DisableInvincibility(3400850)
    EnableCharacterCollision(3400850)
    EnableFlag(13404858)
    EnableFlag(13401851)


@NeverRestart(13404850)
def Event_13404850():
    """Event 13404850"""
    EndIfFlagEnabled(13401850)
    GotoIfFlagEnabled(Label.L0, flag=13401851)
    SkipLinesIfClient(2)
    DisableObject(3401850)
    DeleteVFX(3403850, erase_root_only=False)
    IfFlagDisabled(1, 13401850)
    IfFlagEnabled(1, 13401851)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(3401850)
    CreateVFX(3403850)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfActionButtonParamActivated(3, action_button_id=3400850, entity=3401850)
    IfFlagDisabled(3, 13401850)
    IfFlagEnabled(4, 13401850)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    IfCharacterHuman(5, PLAYER)
    IfCharacterInsideRegion(5, PLAYER, region=3402851)
    IfCharacterHuman(6, PLAYER)
    IfTimeElapsed(6, seconds=2.0)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, condition=6)
    EnableFlag(13404858)
    Restart()


@NeverRestart(13404851)
def Event_13404851():
    """Event 13404851"""
    DisableNetworkSync()
    EndIfFlagEnabled(13401850)
    IfFlagDisabled(1, 13401850)
    IfFlagEnabled(1, 13401851)
    IfFlagEnabled(1, 13404858)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=3400850, entity=3401850)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3402851)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(13404859)
    Restart()


@RestartOnRest(13404852)
def Event_13404852():
    """Event 13404852"""
    EndIfFlagEnabled(13401850)
    DisableAI(3400850)
    DisableHealthBar(3400850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 13404858)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13404860)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400850, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13404860)
    EnableFlag(13404858)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400850, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400850)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400850, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400850)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3400850)
    EnableBossHealthBar(3400850, name=450000)
    CreatePlayLog(name=46)
    StartPlayLogMeasurement(measurement_id=3400030, name=62, overwrite=True)


@NeverRestart(13404853)
def Event_13404853():
    """Event 13404853"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3403852)
    DisableSoundEvent(sound_id=3403853)
    EndIfFlagEnabled(13401850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, 13401850)
    IfFlagEnabled(1, 13404852)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13404859)
    IfCharacterInsideRegion(1, PLAYER, region=3402852)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=3403852)
    IfCharacterHasTAEEvent(2, 3400850, tae_event_id=400)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 13401850)
    IfFlagEnabled(2, 13404852)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13404859)
    IfCharacterInsideRegion(2, PLAYER, region=3402852)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=3403852)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3403853)


@NeverRestart(13404854)
def Event_13404854():
    """Event 13404854"""
    DisableNetworkSync()
    EndIfFlagEnabled(13401850)
    IfCharacterAlive(1, 3400850)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3400850, radius=14.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(2, 3400850)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=3400850, radius=17.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


@NeverRestart(13404855)
def Event_13404855():
    """Event 13404855"""
    DisableNetworkSync()
    EndIfFlagEnabled(13401850)
    IfFlagEnabled(0, 13401850)
    DisableBossMusic(sound_id=3403852)
    DisableBossMusic(sound_id=3403853)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13404856)
def Event_13404856():
    """Event 13404856"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3401850, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13404857)
def Event_13404857():
    """Event 13404857"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=3401850, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=3401850, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@RestartOnRest(13404870)
def Event_13404870(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    special_effect_id: int,
    special_effect_id_1: int,
    part_health: int,
    animation_id: int,
):
    """Event 13404870"""
    EndIfFlagEnabled(13401850)
    CreateNPCPart(3400850, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(3400850, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(1, 3400850, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(2, 3400850, value=0.0)
    IfCharacterHasSpecialEffect(3, 3400850, 5402)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(3400850, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999)
    SetNPCPartEffects(3400850, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    ForceAnimation(3400850, animation_id)
    AddSpecialEffect(3400850, special_effect_id)
    CancelSpecialEffect(3400850, special_effect_id_1)
    ReplanAI(3400850)
    IfTimeElapsed(4, seconds=30.0)
    IfCharacterHasSpecialEffect(5, 3400850, 5402)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    AICommand(3400850, command_id=100, command_slot=1)
    ReplanAI(3400850)
    IfCharacterHasTAEEvent(6, 3400850, tae_event_id=300)
    IfCharacterHasSpecialEffect(7, 3400850, 5402)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=7)
    SetNPCPartHealth(3400850, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    CancelSpecialEffect(3400850, special_effect_id)
    AddSpecialEffect(3400850, special_effect_id_1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(3400850, command_id=-1, command_slot=1)
    ReplanAI(3400850)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(13404875)
def Event_13404875():
    """Event 13404875"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasTAEEvent(0, 3400850, tae_event_id=400)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(3400850, bit_index=10, switch_type=OnOffChange.Off)


@NeverRestart(13401200)
def Event_13401200(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 13401200"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=anchor_entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


@NeverRestart(13401210)
def Event_13401210(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 13401210"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(13401220)
def Event_13401220():
    """Event 13401220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=3401100, animation_id=1)
    DisableObjectActivation(3401110, obj_act_id=3400020)
    NotifyDoorEventSoundDampening(obj=3401100, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=13400002)
    DisableObjectActivation(3401110, obj_act_id=3400020)
    ForceAnimation(3401100, 1)
    Wait(0.0)


@NeverRestart(13400100)
def Event_13400100():
    """Event 13400100"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerStandingOnCollision(0, 3404000)
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest(13400220)
def Event_13400220(_, character: int, flag: int):
    """Event 13400220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest(13400310)
def Event_13400310(_, character: int, region: int):
    """Event 13400310"""
    DisableGravity(character)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    ForceAnimation(character, 7004, loop=True, skip_transition=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 7005, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7003, wait_for_completion=True)


@RestartOnRest(13400320)
def Event_13400320():
    """Event 13400320"""
    EndIfFlagEnabled(9470)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(3401500, vfx_id=200, model_point=900201)
    IfActionButtonParamActivated(0, action_button_id=3400100, entity=3401500)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3401810, host_only=False)
    DeleteObjectVFX(3401500)


@RestartOnRest(13400330)
def Event_13400330(_, character: int):
    """Event 13400330"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    Wait(0.0)


@RestartOnRest(13404799)
def Event_13404799():
    """Event 13404799"""
    CreateProjectileOwner(entity=3400799)


@RestartOnRest(13405100)
def Event_13405100(_, obj: int, region: int, region_1: int):
    """Event 13405100"""
    WaitFrames(frames=1)
    IfCharacterDead(-10, 3400206)
    IfCharacterDead(-10, 3400205)
    IfObjectDestroyed(-10, 3401401)
    IfThisEventSlotFlagEnabled(-10)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=13405101)
    DeleteObjectVFX(obj)
    EnableObject(3401401)
    DisableObject(obj)
    DestroyObject(3401401)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableObject(3401401)
    ForceAnimation(obj, 0, loop=True)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfCharacterInsideRegion(2, PLAYER, region=region_1)
    IfFlagEnabled(3, 13405101)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(13405101)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    IfEntityWithinDistance(-3, entity=obj, other_entity=PLAYER, radius=22.0)
    IfTimeElapsed(-3, seconds=4.0)
    IfConditionTrue(0, input_condition=-3)

    # --- 2 --- #
    DefineLabel(2)
    CreateObjectVFX(obj, vfx_id=100, model_point=900260)
    CreateHazard(
        obj_flag=13405101,
        obj=obj,
        model_point=100,
        behavior_param_id=6291,
        target_type=DamageTargetType.Character,
        radius=1.600000023841858,
        life=9999.0,
        repetition_time=0.0,
    )
    PlaySoundEffect(3402531, 411005001, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=30)
    ForceAnimation(obj, 1, wait_for_completion=True)
    ForceAnimation(obj, 2, loop=True)
    RemoveObjectFlag(obj_flag=13405101)
    DeleteObjectVFX(obj)
    EnableObject(3401401)
    DisableObject(obj)
    DestroyObject(3401401)


@RestartOnRest(13405103)
def Event_13405103():
    """Event 13405103"""
    IfThisEventSlotFlagEnabled(-10)
    IfCharacterDead(-10, 3400551)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3401010, 11, loop=True)
    EndOfAnimation(obj=3401010, animation_id=11)
    EnableAI(3400551)
    SetNest(3400551, region=3402310)
    ReplanAI(3400551)
    DisableObjectActivation(3401010, obj_act_id=3400000)
    NotifyDoorEventSoundDampening(obj=3401010, state=DoorState.DoorOpening)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableAI(3400551)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=3402300)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=3400551, radius=7.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=3400551)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(3402300, 340000000, sound_type=SoundType.a_Ambient)
    ForceAnimation(3400551, 7015)
    ForceAnimation(3401010, 10)
    WaitFrames(frames=260)
    EnableAI(3400551)
    SetNest(3400551, region=3402310)
    ReplanAI(3400551)
    DisableObjectActivation(3401010, obj_act_id=3400000)


@RestartOnRest(13405105)
def Event_13405105(
    _,
    region: int,
    entity: int,
    obj__source_entity: int,
    launch_angle_x: int,
    launch_angle_y: int,
    launch_angle_z: int,
):
    """Event 13405105"""
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(entity, 1, wait_for_completion=True)
    IfObjectNotDestroyed(0, obj__source_entity)
    ForceAnimation(obj__source_entity, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6281,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6282,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6283,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=60)
    IfAllPlayersOutsideRegion(0, region=region)
    ForceAnimation(entity, 0, loop=True)
    Restart()


@RestartOnRest(13405110)
def Event_13405110():
    """Event 13405110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(3400200, ai_param_id=263757)
    ReplanAI(3400200)
    SetAIParamID(3400406, ai_param_id=400002)
    ReplanAI(3400406)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasTAEEvent(0, 3400200, tae_event_id=10)
    ReplanAI(3400406)
    SetAIParamID(3400406, ai_param_id=400018)
    SetAIParamID(3400200, ai_param_id=263757)
    ReplanAI(3400200)
    SkipLinesIfValueEqual(1, left=1, right=0)
    AddSpecialEffect(3400406, 5000)
    ChangePatrolBehavior(3400406, patrol_information_id=3403350)
    Wait(3.0)
    SetAIParamID(3400406, ai_param_id=400002)
    ReplanAI(3400406)


@RestartOnRest(13405112)
def Event_13405112():
    """Event 13405112"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(3401320)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=3402533)
    ForceAnimation(3401352, 1, wait_for_completion=True)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=3401320,
        model_point=10,
        behavior_id=6290,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=80)
    DisableObject(3401320)


@RestartOnRest(13405113)
def Event_13405113(
    _,
    obj__source_entity: int,
    flag: int,
    frames: int,
    frames_1: int,
    behavior_id: int,
    behavior_id_1: int,
    behavior_id_2: int,
    behavior_id_3: int,
):
    """Event 13405113"""
    IfFlagEnabled(1, flag)
    IfObjectNotDestroyed(1, obj__source_entity)
    IfConditionTrue(0, input_condition=1)
    IfFramesElapsed(0, frames=frames)
    ForceAnimation(obj__source_entity, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_1,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_2,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_3,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    IfFramesElapsed(0, frames=frames_1)
    Restart()


@RestartOnRest(13405115)
def Event_13405115(
    _,
    obj__source_entity: int,
    flag: int,
    frames: int,
    frames_1: int,
    behavior_id: int,
    behavior_id_1: int,
    behavior_id_2: int,
    behavior_id_3: int,
):
    """Event 13405115"""
    IfFlagEnabled(1, flag)
    IfObjectNotDestroyed(1, obj__source_entity)
    IfConditionTrue(0, input_condition=1)
    IfFramesElapsed(0, frames=frames)
    ForceAnimation(obj__source_entity, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_2,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id_3,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, frames=2)
    IfFramesElapsed(0, frames=frames_1)
    Restart()


@RestartOnRest(13405140)
def Event_13405140(_, character: int, region: int, flag: int, region_1: int, entity: int, frames: int):
    """Event 13405140"""
    IfCharacterAlive(1, character)
    IfCharacterInsideRegion(1, character, region=region_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(entity, 1, wait_for_completion=True)
    IfFramesElapsed(0, frames=frames)
    IfCharacterAlive(2, character)
    IfCharacterInsideRegion(2, character, region=region_1)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    RestartIfConditionFalse(2)
    EnableFlag(flag)
    IfCharacterDead(-1, character)
    IfCharacterOutsideRegion(-1, character, region=region_1)
    IfCharacterOutsideRegion(-1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=10)
    ForceAnimation(entity, 0, loop=True)
    DisableFlag(flag)
    Restart()


@RestartOnRest(13405145)
def Event_13405145(_, region: int, entity: int, flag: int):
    """Event 13405145"""
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(entity, 1, wait_for_completion=True)
    EnableFlag(flag)
    IfAllPlayersOutsideRegion(0, region=region)
    WaitFrames(frames=10)
    ForceAnimation(entity, 0, loop=True)
    DisableFlag(flag)
    Restart()


@RestartOnRest(13405155)
def Event_13405155(_, region: int):
    """Event 13405155"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(3402515, 411005002, sound_type=SoundType.a_Ambient)


@RestartOnRest(13405160)
def Event_13405160(_, obj__source_entity: int):
    """Event 13405160"""
    EndIfThisEventSlotFlagEnabled()
    IfAttackedWithDamageType(-1, attacked_entity=obj__source_entity, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=obj__source_entity, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=obj__source_entity, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=obj__source_entity, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=obj__source_entity, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=obj__source_entity, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=obj__source_entity, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, obj__source_entity, ComparisonType.LessThanOrEqual, value=999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__source_entity)
    PlaySoundEffect(obj__source_entity, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj__source_entity,
        model_point=-1,
        behavior_id=6292,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(obj__source_entity)
    PlaySoundEffect(obj__source_entity, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(13405200)
def Event_13405200(_, character: int, region: int, animation_id: int, region_1: int):
    """Event 13405200"""
    IfCharacterBackreadEnabled(1, character)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, character, region=region)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfCharacterOutsideRegion(2, character, region=region_1)
    IfHealthLessThanOrEqual(4, character, value=0.0)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    RestartIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(character)
    ForceAnimation(character, 0, wait_for_completion=True)
    Restart()


@RestartOnRest(13405211)
def Event_13405211(_, region: int):
    """Event 13405211"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(region, 340000000, sound_type=SoundType.a_Ambient)


@RestartOnRest(13405216)
def Event_13405216(
    _,
    character: int,
    region: int,
    region_1: int,
    patrol_information_id: int,
    seconds: float,
    left: int,
):
    """Event 13405216"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(-2, 3400316, region=region)
    IfCharacterInsideRegion(-2, 3400316, region=region_1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(1, left=left, right=0)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13405218)
def Event_13405218():
    """Event 13405218"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3402553)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapCollision(collision=3404250)


@RestartOnRest(13405220)
def Event_13405220(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    region: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13405220"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    WaitRandomFrames(min_frames=0, max_frames=180)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
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
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405300)
def Event_13405300(_, character: int, region: int, radius: float, seconds: float):
    """Event 13405300"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(13405350)
def Event_13405350(
    _,
    character: int,
    region: int,
    region_1: int,
    patrol_information_id: int,
    seconds: float,
    left: int,
):
    """Event 13405350"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(1, left=left, right=0)
    AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13405480)
def Event_13405480(_, character: int, region: int, radius: float, animation_id: int, seconds: float, state: uchar):
    """Event 13405480"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetAIState(character, state)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(4, attacked_entity=character)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(3, condition=3)
    SkipLinesIfFinishedConditionTrue(2, condition=4)
    Wait(seconds)
    ForceAnimation(character, animation_id)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(13405510)
def Event_13405510(_, character: int):
    """Event 13405510"""
    IfCharacterDead(0, character)
    IncrementEventValue(13405500, bit_count=4, max_value=15)


@RestartOnRest(13405520)
def Event_13405520(_, character: int, region: int):
    """Event 13405520"""
    IfEventValueGreaterThanOrEqual(0, flag=13405500, bit_count=4, value=4)
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=2)
    ReplanAI(character)


@RestartOnRest(13405530)
def Event_13405530(_, character: int, region: int):
    """Event 13405530"""
    IfEventValueGreaterThanOrEqual(0, flag=13405500, bit_count=4, value=2)
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=3)
    ReplanAI(character)


@RestartOnRest(13405540)
def Event_13405540(_, character: int, patrol_information_id: int, value: uint, left: int, seconds: float):
    """Event 13405540"""
    IfEventValueGreaterThanOrEqual(0, flag=13405500, bit_count=4, value=value)
    SkipLinesIfValueEqual(1, left=left, right=0)
    AddSpecialEffect(character, 5000)
    Wait(seconds)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13405550)
def Event_13405550(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13405550"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfEventValueGreaterThanOrEqual(0, flag=13405500, bit_count=4, value=2)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405570)
def Event_13405570(_, character: int, region: int, region_1: int, command_id: int, command_slot: uchar):
    """Event 13405570"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    SetEventPoint(character, region=region, reaction_range=0.5)
    ReplanAI(character)
    AICommand(character, command_id=command_id, command_slot=command_slot)


@RestartOnRest(13405610)
def Event_13405610(_, character: int):
    """Event 13405610"""
    IfCharacterDead(0, character)
    IncrementEventValue(13405600, bit_count=4, max_value=15)


@RestartOnRest(13405620)
def Event_13405620(_, character: int, region: int):
    """Event 13405620"""
    IfEventValueGreaterThanOrEqual(0, flag=13405600, bit_count=4, value=4)
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=2)
    ReplanAI(character)


@RestartOnRest(13405630)
def Event_13405630(_, character: int, region: int):
    """Event 13405630"""
    IfEventValueGreaterThanOrEqual(0, flag=13405600, bit_count=4, value=2)
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=3)
    ReplanAI(character)


@RestartOnRest(13405640)
def Event_13405640(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13405640"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfEventValueGreaterThanOrEqual(0, flag=13405600, bit_count=4, value=1)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ReplanAI(character)


@RestartOnRest(13405650)
def Event_13405650(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation: int,
    ai_param_id_1: int,
    min_seconds: float,
    max_seconds: float,
):
    """Event 13405650"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfEventValueGreaterThanOrEqual(0, flag=13405600, bit_count=4, value=2)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405680)
def Event_13405680(_, character: int, character_1: int, radius: float):
    """Event 13405680"""
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfEntityWithinDistance(1, entity=character, other_entity=character_1, radius=radius)
    IfCharacterAlive(1, character_1)
    IfCharacterBackreadEnabled(1, character_1)
    IfConditionTrue(0, input_condition=1)
    AICommand(character_1, command_id=200, command_slot=1)
    IfCharacterHasTAEEvent(0, character_1, tae_event_id=20)
    AddSpecialEffect(character_1, 5645)
    AICommand(character_1, command_id=-1, command_slot=1)
    Restart()


@NeverRestart(13400940)
def Event_13400940():
    """Event 13400940"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    GotoIfFlagRangeAnyEnabled(Label.L1, flag_range=(1670, 1689))
    DisableFlagRange((1670, 1689))
    EnableFlag(1680)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 13401800)
    IfFlagRangeAllDisabled(1, flag_range=(1670, 1674))
    GotoIfConditionFalse(Label.L2, input_condition=1)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(2, 1681)
    IfFlagEnabled(-1, 1720)
    IfFlagEnabled(-1, 1721)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, 73400513)
    IfFlagEnabled(2, 73400403)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1670, 1689))
    EnableFlag(1671)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(3, 13500100)
    IfFlagEnabled(-2, 1720)
    IfFlagEnabled(-2, 1721)
    IfFlagEnabled(-2, 1724)
    IfFlagEnabled(-2, 1722)
    IfConditionTrue(3, input_condition=-2)
    IfFlagEnabled(3, 73400403)
    IfFlagEnabled(4, 1681)
    IfFlagDisabled(4, 73400512)
    IfConditionTrue(-3, input_condition=4)
    IfFlagEnabled(-3, 1671)
    IfConditionTrue(3, input_condition=-3)
    GotoIfConditionFalse(Label.L4, input_condition=3)
    DisableFlagRange((1670, 1689))
    EnableFlag(1672)

    # --- 4 --- #
    DefineLabel(4)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L5, flag=1670)
    GotoIfFlagEnabled(Label.L6, flag=1671)
    GotoIfFlagEnabled(Label.L7, flag=1672)
    GotoIfFlagEnabled(Label.L8, flag=1680)
    GotoIfFlagEnabled(Label.L9, flag=1681)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    End()

    # --- 8 --- #
    DefineLabel(8)
    EnableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 9 --- #
    DefineLabel(9)
    EnableBackread(3400900)
    EnableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    EnableImmortality(3400900)
    IfFlagDisabled(7, 50002360)
    IfFlagEnabled(7, 73400512)
    SkipLinesIfConditionFalse(1, 7)
    DropMandatoryTreasure(3400906)
    SkipLinesIfFlagDisabled(1, 73400512)
    ForceAnimation(3400900, 7002, loop=True, skip_transition=True)
    End()

    # --- 6 --- #
    DefineLabel(6)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    EnableObject(3400908)
    SkipLinesIfFlagEnabled(4, 50002360)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    DropMandatoryTreasure(3400906)
    End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 7 --- #
    DefineLabel(7)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    SkipLinesIfFlagEnabled(4, 50002360)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    DropMandatoryTreasure(3400906)
    End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()


@NeverRestart(13400941)
def Event_13400941():
    """Event 13400941"""
    EndIfFlagDisabled(1680)
    IfCharacterDead(-1, 3400800)
    IfCharacterDead(-1, 3400801)
    IfConditionTrue(0, input_condition=-1)
    IfAllPlayersOutsideRegion(1, region=3402915)
    IfCharacterOutsideRegion(1, 3400921, region=3402915)
    IfCharacterOutsideRegion(1, 3400922, region=3402915)
    IfCharacterOutsideRegion(1, 3400923, region=3402915)
    IfCharacterOutsideRegion(1, 3400924, region=3402915)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    Move(3400900, destination=3402911, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    IfAllPlayersOutsideRegion(2, region=3402916)
    IfCharacterOutsideRegion(2, 3400921, region=3402916)
    IfCharacterOutsideRegion(2, 3400922, region=3402916)
    IfCharacterOutsideRegion(2, 3400923, region=3402916)
    IfCharacterOutsideRegion(2, 3400924, region=3402916)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    Move(3400900, destination=3402912, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3402917)
    IfCharacterOutsideRegion(3, 3400921, region=3402917)
    IfCharacterOutsideRegion(3, 3400922, region=3402917)
    IfCharacterOutsideRegion(3, 3400923, region=3402917)
    IfCharacterOutsideRegion(3, 3400924, region=3402917)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    Move(3400900, destination=3402913, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    Move(3400900, destination=34029134, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- 8 --- #
    DefineLabel(8)
    EnableCharacter(3400900)
    EnableImmortality(3400900)


@NeverRestart(13400942)
def Event_13400942(_, flag: int):
    """Event 13400942"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventSlotFlagEnabled()
    EndIfFlagRangeAllDisabled(flag_range=(1680, 1681))
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(73400519)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, flag)
    IfFlagEnabled(-1, 73400519)
    IfCharacterDead(-1, 3400900)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(3400906)
    Move(3400906, destination=3400900, destination_type=CoordEntityType.Character, model_point=10, short_move=True)
    WaitFrames(frames=1)
    DropMandatoryTreasure(3400906)
    EndIfFlagEnabled(73400519)
    ForceAnimation(3400900, 7002, loop=True, skip_transition=True)


@NeverRestart(13400943)
def Event_13400943(_, attacked_entity: int):
    """Event 13400943"""
    IfFlagEnabled(-1, 1681)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(1, attacked_entity=attacked_entity, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1670, 1689))
    EnableFlag(1670)
    SaveRequest()
    WaitFrames(frames=1)
    ForceAnimation(attacked_entity, 7010, skip_transition=True)
    WaitFrames(frames=119)
    ForceAnimation(attacked_entity, 7011, loop=True, skip_transition=True)
    EnableFlag(73400519)


@NeverRestart(13400944)
def Event_13400944():
    """Event 13400944"""
    DisableFlag(73400510)
    IfFlagEnabled(-1, 1670)
    IfFlagEnabled(-1, 1671)
    IfFlagEnabled(-1, 1672)
    IfFlagEnabled(-1, 73400512)
    EndIfConditionTrue(-1)
    IfFlagEnabled(0, 73400510)
    IfHealthEqual(-2, 3400900, value=0.0)
    IfFlagEnabled(-2, 73400512)
    IfFlagEnabled(-2, 1670)
    EndIfConditionTrue(-2)
    ForceAnimation(3400900, 7001, loop=True, skip_transition=True)
    IfFlagDisabled(0, 73400510)
    IfHealthEqual(-3, 3400900, value=0.0)
    IfFlagEnabled(-3, 73400512)
    IfFlagEnabled(-3, 1670)
    EndIfConditionTrue(-3)
    ForceAnimation(3400900, 0, loop=True, skip_transition=True)
    Restart()


@NeverRestart(13400900)
def Event_13400900(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13400900"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    IfCharacterDead(1, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(13400910)
def Event_13400910(_, attacked_entity: int, flag: int):
    """Event 13400910"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    EnableFlag(flag)


@NeverRestart(13400920)
def Event_13400920(_, character: int, flag: int, first_flag: int, last_flag: int, flag_1: int):
    """Event 13400920"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfFlagEnabled(-1, flag)
    IfHealthLessThanOrEqual(-1, character, value=0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    SaveRequest()


@NeverRestart(13400930)
def Event_13400930():
    """Event 13400930"""
    DisableAI(3400910)
    IfCharacterInsideRegion(-1, PLAYER, region=3402949)
    IfAttackedWithDamageType(-1, attacked_entity=3400910, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(3400910)


@NeverRestart(13400950)
def Event_13400950(_, character: int, character_1: int):
    """Event 13400950"""
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-15)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)
    Goto(Label.L8)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=1724)
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 1720)
    IfFlagEnabled(-1, 1681)
    IfFlagEnabled(-1, 1671)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 73400403)
    IfFlagEnabled(1, 73400513)
    IfConditionTrue(-2, input_condition=1)
    IfFlagEnabled(2, 1720)
    IfFlagEnabled(2, 73400403)
    IfFlagEnabled(2, 1670)
    IfConditionTrue(-2, input_condition=2)
    GotoIfConditionFalse(Label.L2, input_condition=-2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1721)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAnyEnabled(3, flag_range=(1720, 1721))
    IfFlagEnabled(3, 73400403)
    IfFlagEnabled(3, 13500100)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1722)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagRangeAnyEnabled(4, flag_range=(1720, 1722))
    IfFlagEnabled(4, 73400403)
    IfFlagEnabled(4, 1650)
    GotoIfConditionFalse(Label.L8, input_condition=4)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L0, flag=1720)
    GotoIfFlagEnabled(Label.L1, flag=1725)
    GotoIfFlagEnabled(Label.L2, flag=1710)
    GotoIfFlagEnabled(Label.L3, flag=1721)
    GotoIfFlagEnabled(Label.L4, flag=1726)
    GotoIfFlagEnabled(Label.L5, flag=1711)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103150)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.Ally)
    ForceAnimation(character_1, 103150)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DropMandatoryTreasure(character_1)
    End()


@NeverRestart(13400951)
def Event_13400951(_, character: int, flag: int, flag_1: int):
    """Event 13400951"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(flag)
    EndIfFlagDisabled(flag_1)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterHasSpecialEffect(1, character, 151)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103155)
    IfFlagEnabled(2, flag_1)
    IfFlagDisabled(2, flag)
    IfCharacterHasSpecialEffect(2, character, 152)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(character, 103150)
    Restart()


@NeverRestart(13400953)
def Event_13400953(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 13400953"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag_1)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(13400970)
def Event_13400970(_, character: int):
    """Event 13400970"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    Wait(0.0)


@NeverRestart(13400980)
def Event_13400980(_, flag: int, item_lot_param_id: int):
    """Event 13400980"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(13400990)
def Event_13400990(_, flag: int, item_lot_param_id: int):
    """Event 13400990"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    AwardItemLot(item_lot_param_id, host_only=False)
    Restart()


@NeverRestart(13400995)
def Event_13400995(_, flag: int, item_lot_param_id: int, item_lot_param_id_1: int, flag_1: int):
    """Event 13400995"""
    EndIfFlagEnabled(flag)
    EndIfClient()
    IfFlagEnabled(0, flag)
    SkipLinesIfFlagEnabled(2, flag_1)
    AwardItemLot(item_lot_param_id, host_only=False)
    SkipLines(1)
    AwardItemLot(item_lot_param_id_1, host_only=False)


@RestartOnRest(13404450)
def Event_13404450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13404401)
def Event_13404401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagRangeAllDisabled(1, flag_range=(13404422, 13404426))
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
    IfFlagRangeAllDisabled(2, flag_range=(13404422, 13404426))
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404402)
def Event_13404402(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404402"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(-4, 1800)
    IfFlagEnabled(-4, 1801)
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
    IfFlagEnabled(-5, 1800)
    IfFlagEnabled(-5, 1801)
    IfConditionTrue(2, input_condition=-5)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404403)
def Event_13404403(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404403"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 6813)
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
    IfFlagEnabled(2, 6813)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404404)
def Event_13404404(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404404"""
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


@RestartOnRest(13404405)
def Event_13404405(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404405"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfPlayerHasGood(1, 4014)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(-4, 1800)
    IfFlagEnabled(-4, 1801)
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
    IfPlayerHasGood(2, 4014)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(-5, 1800)
    IfFlagEnabled(-5, 1801)
    IfConditionTrue(2, input_condition=-5)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404406)
def Event_13404406(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404406"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfPlayerHasGood(1, 4014)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 6813)
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
    IfPlayerHasGood(2, 4014)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(2, 6813)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404410)
def Event_13404410(
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
    """Event 13404410"""
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


@RestartOnRest(13404460)
def Event_13404460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 13404460"""
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


@RestartOnRest(13404490)
def Event_13404490(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404490"""
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(character, 35)
    WaitFrames(frames=1)
    Restart()
