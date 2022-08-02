"""
Hunter's Nightmare

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


@ContinueOnRest(0)
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

    # --- Label 0 --- #
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

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(3400)
    DisableFlag(3401)
    DisableFlag(3402)
    EnableFlag(3403)
    if FlagEnabled(13401800):
        EnableFlag(3400)
        EnableFlag(3401)
        EnableFlag(3402)
        EnableFlag(3403)
    if FlagEnabled(13401852):
        DisableFlag(3400)
        DisableFlag(3401)
        EnableFlag(3402)
        DisableFlag(3403)
    if FlagEnabled(13401850):
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
        flag_6=13404712,
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
        flag_6=13404711,
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
    if FlagDisabled(13400999):
        Event_13404824()
        Event_13404825()
        Event_13404830(
            0,
            npc_part_id=3400,
            npc_part_id_1=3400,
            part_index=1,
            part_health=300,
            special_effect=480,
            animation_id=7001,
            frames=152,
        )
        Event_13404830(
            1,
            npc_part_id=3401,
            npc_part_id_1=3401,
            part_index=2,
            part_health=150,
            special_effect=482,
            animation_id=7004,
            frames=72,
        )
        Event_13404830(
            2,
            npc_part_id=3402,
            npc_part_id_1=3402,
            part_index=3,
            part_health=150,
            special_effect=481,
            animation_id=7002,
            frames=72,
        )
        Event_13404835()
        Event_13404841()
    else:
        Event_13404830(
            0,
            npc_part_id=3400,
            npc_part_id_1=3400,
            part_index=1,
            part_health=400,
            special_effect=480,
            animation_id=7001,
            frames=152,
        )
        Event_13404830(
            1,
            npc_part_id=3401,
            npc_part_id_1=3401,
            part_index=2,
            part_health=200,
            special_effect=482,
            animation_id=7004,
            frames=72,
        )
        Event_13404830(
            2,
            npc_part_id=3402,
            npc_part_id_1=3402,
            part_index=3,
            part_health=200,
            special_effect=481,
            animation_id=7002,
            frames=72,
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
        special_effect=480,
        special_effect_1=490,
        part_health=60,
        animation_id=8020,
    )
    Event_13404870(
        1,
        npc_part_id=3451,
        npc_part_id_1=3451,
        part_index=2,
        special_effect=481,
        special_effect_1=491,
        part_health=150,
        animation_id=8000,
    )
    Event_13404870(
        2,
        npc_part_id=3452,
        npc_part_id_1=3452,
        part_index=3,
        special_effect=482,
        special_effect_1=492,
        part_health=150,
        animation_id=8010,
    )
    Event_13404870(
        3,
        npc_part_id=3453,
        npc_part_id_1=3453,
        part_index=4,
        special_effect=483,
        special_effect_1=493,
        part_health=250,
        animation_id=8030,
    )
    Event_13404870(
        4,
        npc_part_id=3454,
        npc_part_id_1=3454,
        part_index=5,
        special_effect=484,
        special_effect_1=494,
        part_health=250,
        animation_id=8040,
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
    Event_13405105(0, region=3402370, entity=3401350, obj=3401351, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    Event_13405115(
        0,
        obj=3401366,
        flag=13405130,
        frames=0,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        1,
        obj=3401356,
        flag=13405131,
        frames=0,
        frames_1=60,
        behavior_id=6284,
        behavior_id_1=6285,
        behavior_id_2=6286,
        behavior_id_3=6287,
    )
    Event_13405115(
        2,
        obj=3401359,
        flag=13405132,
        frames=0,
        frames_1=70,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        3,
        obj=3401363,
        flag=13405132,
        frames=20,
        frames_1=80,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        4,
        obj=3401364,
        flag=13405132,
        frames=10,
        frames_1=40,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        5,
        obj=3401365,
        flag=13405132,
        frames=30,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        6,
        obj=3401364,
        flag=13405133,
        frames=10,
        frames_1=60,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        7,
        obj=3401359,
        flag=13405135,
        frames=20,
        frames_1=40,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        9,
        obj=3401363,
        flag=13405135,
        frames=10,
        frames_1=70,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        10,
        obj=3401364,
        flag=13405135,
        frames=17,
        frames_1=60,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405115(
        11,
        obj=3401365,
        flag=13405135,
        frames=6,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405113(
        0,
        obj=3401360,
        flag=13405136,
        frames=6,
        frames_1=50,
        behavior_id=6280,
        behavior_id_1=6281,
        behavior_id_2=6282,
        behavior_id_3=6283,
    )
    Event_13405140(1, character=3400207, region=3402510, flag=13405132, region_1=3402371, entity=3401367, frames=30)
    Event_13405140(2, character=3400207, region=3402376, flag=13405133, region_1=3402371, entity=3401367, frames=10)
    Event_13405140(4, character=3400210, region=3402377, flag=13405136, region_1=3402374, entity=3401368, frames=20)
    Event_13405145(0, region=3402374, entity=3401368, flag=13405130)
    Event_13405145(1, region=3402372, entity=3401357, flag=13405131)
    Event_13405145(2, region=3402371, entity=3401367, flag=13405135)
    Event_13405145(3, region=3402374, entity=3401368, flag=13405136)
    Event_13405155(0, region=3402515)
    Event_13405160(0, obj=3401330)
    Event_13405160(1, obj=3401331)
    Event_13405160(2, obj=3401332)
    Event_13405160(3, obj=3401333)
    Event_13405160(4, obj=3401334)
    Event_13405160(5, obj=3401335)
    Event_13405160(6, obj=3401336)
    Event_13405160(7, obj=3401337)
    Event_13405160(8, obj=3401338)
    Event_13405160(9, obj=3401339)
    Event_13405160(10, obj=3401340)
    Event_13405160(11, obj=3401341)
    Event_13405160(12, obj=3401342)
    Event_13405160(13, obj=3401343)
    Event_13405160(14, obj=3401344)
    Event_13405110()
    Event_13405112()
    Event_13405200(0, character=3400300, region=3402600, animation_id=3004, region_1=3402601)
    Event_13400330(0, character=3400650)
    Event_13405211(1, region=3402301)
    Event_13405211(2, region=3402302)
    Event_13405220(
        0,
        character=3400152,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13405220(
        2,
        character=3400154,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=1.0,
    )
    Event_13405220(
        16,
        character=3400315,
        animation_id=7001,
        ai_param_id=400010,
        animation=7002,
        ai_param_id_1=400010,
        region=3402555,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13405220(
        17,
        character=3400169,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=2.0,
    )
    Event_13405220(
        18,
        character=3400170,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=2.0,
    )
    Event_13405220(
        19,
        character=3400171,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=2.0,
    )
    Event_13405220(
        20,
        character=3400172,
        animation_id=7015,
        ai_param_id=109900,
        animation=7016,
        ai_param_id_1=109955,
        region=0,
        min_seconds=0.0,
        max_seconds=2.0,
    )
    Event_13405220(
        3,
        character=3400350,
        animation_id=7000,
        ai_param_id=6550,
        animation=0,
        ai_param_id_1=6550,
        region=0,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13405550(
        4,
        character=3400141,
        animation_id=7000,
        ai_param_id=109900,
        animation=7002,
        ai_param_id_1=109950,
        min_seconds=2.0,
        max_seconds=3.0,
    )
    Event_13405550(
        5,
        character=3400146,
        animation_id=7000,
        ai_param_id=109900,
        animation=7002,
        ai_param_id_1=109950,
        min_seconds=2.0,
        max_seconds=4.0,
    )
    Event_13405550(
        7,
        character=3400147,
        animation_id=7003,
        ai_param_id=109900,
        animation=7005,
        ai_param_id_1=109953,
        min_seconds=4.0,
        max_seconds=6.0,
    )
    Event_13405550(
        8,
        character=3400148,
        animation_id=7006,
        ai_param_id=109900,
        animation=7008,
        ai_param_id_1=109953,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13405300(1, character=3400208, region=0, radius=3.0, seconds=0.0)
    Event_13405300(2, character=3400209, region=0, radius=3.0, seconds=0.0)
    Event_13405300(3, character=3400207, region=0, radius=3.0, seconds=0.0)
    Event_13405300(4, character=3400210, region=0, radius=3.0, seconds=0.0)
    Event_13405300(7, character=3400160, region=3402506, radius=10.0, seconds=0.0)
    Event_13405300(8, character=3400309, region=3402508, radius=10.0, seconds=2.0)
    Event_13405300(9, character=3400280, region=3402510, radius=10.0, seconds=0.0)
    Event_13405300(10, character=3400281, region=3402510, radius=10.0, seconds=0.0)
    Event_13405300(15, character=3400664, region=3402536, radius=10.0, seconds=0.0)
    Event_13405300(16, character=3400510, region=3402539, radius=10.0, seconds=0.0)
    Event_13405300(17, character=3400550, region=3402538, radius=10.0, seconds=0.0)
    Event_13405300(18, character=3400580, region=3402544, radius=5.0, seconds=0.0)
    Event_13405350(0, character=3400405, region=3402512, region_1=0, patrol_information_id=3403303, seconds=0.0, left=0)
    Event_13405350(1, character=3400204, region=3402315, region_1=0, patrol_information_id=3403353, seconds=0.0, left=0)
    Event_13405350(2, character=3400253, region=3402315, region_1=0, patrol_information_id=3403354, seconds=0.0, left=0)
    Event_13405350(3, character=3400508, region=3402504, region_1=0, patrol_information_id=3403335, seconds=0.0, left=0)
    Event_13405350(4, character=3400203, region=3402504, region_1=0, patrol_information_id=3403335, seconds=1.0, left=0)
    Event_13405350(5, character=3400200, region=3402534, region_1=0, patrol_information_id=3403351, seconds=0.0, left=1)
    Event_13405350(6, character=3400105, region=3402512, region_1=0, patrol_information_id=3403356, seconds=0.0, left=1)
    Event_13405350(7, character=3400106, region=3402512, region_1=0, patrol_information_id=3403356, seconds=4.0, left=1)
    Event_13405350(8, character=3400202, region=3402505, region_1=0, patrol_information_id=3403339, seconds=0.0, left=0)
    Event_13405350(9, character=3400252, region=3402505, region_1=0, patrol_information_id=3403339, seconds=0.0, left=0)
    Event_13405350(
        10,
        character=3400411,
        region=3402360,
        region_1=0,
        patrol_information_id=3403310,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        11,
        character=3400601,
        region=3402650,
        region_1=0,
        patrol_information_id=3403347,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        12,
        character=3400552,
        region=3402558,
        region_1=0,
        patrol_information_id=3403348,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        13,
        character=3400105,
        region=3402559,
        region_1=0,
        patrol_information_id=3403305,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        14,
        character=3400106,
        region=3402559,
        region_1=0,
        patrol_information_id=3403305,
        seconds=2.0,
        left=1,
    )
    Event_13405350(
        15,
        character=3400665,
        region=3402315,
        region_1=0,
        patrol_information_id=3403336,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        16,
        character=3400601,
        region=3402555,
        region_1=0,
        patrol_information_id=3403347,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        17,
        character=3400137,
        region=3402502,
        region_1=0,
        patrol_information_id=3403301,
        seconds=1.0,
        left=0,
    )
    Event_13405350(
        18,
        character=3400107,
        region=3402513,
        region_1=0,
        patrol_information_id=3403352,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        19,
        character=3400412,
        region=3402553,
        region_1=0,
        patrol_information_id=3403343,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        20,
        character=3400165,
        region=3402526,
        region_1=0,
        patrol_information_id=3403311,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        24,
        character=3400166,
        region=3402526,
        region_1=0,
        patrol_information_id=3403311,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        25,
        character=3400167,
        region=3402526,
        region_1=0,
        patrol_information_id=3403311,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        26,
        character=3400168,
        region=3402526,
        region_1=0,
        patrol_information_id=3403311,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        27,
        character=3400611,
        region=3402561,
        region_1=0,
        patrol_information_id=3403315,
        seconds=2.0,
        left=0,
    )
    Event_13405350(
        34,
        character=3400158,
        region=3402560,
        region_1=0,
        patrol_information_id=3403304,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        35,
        character=3400159,
        region=3402560,
        region_1=0,
        patrol_information_id=3403304,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        36,
        character=3400160,
        region=3402560,
        region_1=0,
        patrol_information_id=3403304,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        37,
        character=3400161,
        region=3402560,
        region_1=0,
        patrol_information_id=3403304,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        38,
        character=3400162,
        region=3402560,
        region_1=0,
        patrol_information_id=3403304,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        39,
        character=3400403,
        region=3402517,
        region_1=0,
        patrol_information_id=3403302,
        seconds=8.0,
        left=1,
    )
    Event_13405350(
        40,
        character=3400303,
        region=3402517,
        region_1=0,
        patrol_information_id=3403309,
        seconds=16.0,
        left=1,
    )
    Event_13405350(
        41,
        character=3400205,
        region=3402304,
        region_1=0,
        patrol_information_id=3403307,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        42,
        character=3400206,
        region=3402304,
        region_1=0,
        patrol_information_id=3403308,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        43,
        character=3400111,
        region=3402552,
        region_1=0,
        patrol_information_id=3403355,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        44,
        character=3400112,
        region=3402511,
        region_1=0,
        patrol_information_id=3403355,
        seconds=0.0,
        left=1,
    )
    Event_13405350(
        45,
        character=3400113,
        region=3402511,
        region_1=0,
        patrol_information_id=3403355,
        seconds=4.0,
        left=1,
    )
    Event_13405350(
        46,
        character=3400130,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=8.0,
        left=0,
    )
    Event_13405350(
        47,
        character=3400131,
        region=3402500,
        region_1=0,
        patrol_information_id=3403306,
        seconds=2.0,
        left=0,
    )
    Event_13405350(
        48,
        character=3400132,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=9.0,
        left=0,
    )
    Event_13405350(
        49,
        character=3400133,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=9.0,
        left=0,
    )
    Event_13405350(
        50,
        character=3400134,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=8.0,
        left=0,
    )
    Event_13405350(
        51,
        character=3400135,
        region=3402502,
        region_1=0,
        patrol_information_id=3403301,
        seconds=2.0,
        left=0,
    )
    Event_13405350(
        52,
        character=3400137,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=9.0,
        left=0,
    )
    Event_13405350(
        53,
        character=3400140,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=2.0,
        left=0,
    )
    Event_13405350(
        54,
        character=3400149,
        region=3402517,
        region_1=0,
        patrol_information_id=3403301,
        seconds=7.0,
        left=0,
    )
    Event_13405350(
        55,
        character=3400178,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=15.0,
        left=1,
    )
    Event_13405350(
        56,
        character=3400179,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=15.0,
        left=1,
    )
    Event_13405350(
        57,
        character=3400180,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=15.0,
        left=1,
    )
    Event_13405350(
        58,
        character=3400181,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=9.0,
        left=1,
    )
    Event_13405350(
        59,
        character=3400182,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=15.0,
        left=1,
    )
    Event_13405350(
        60,
        character=3400183,
        region=3402517,
        region_1=0,
        patrol_information_id=3403314,
        seconds=15.0,
        left=1,
    )
    Event_13405350(
        61,
        character=3400139,
        region=3402508,
        region_1=0,
        patrol_information_id=3403358,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        62,
        character=3400136,
        region=3402508,
        region_1=0,
        patrol_information_id=3403358,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        63,
        character=3400173,
        region=3402500,
        region_1=0,
        patrol_information_id=3403312,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        64,
        character=3400610,
        region=3402503,
        region_1=0,
        patrol_information_id=3403313,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        65,
        character=3400204,
        region=3402316,
        region_1=0,
        patrol_information_id=3403353,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        66,
        character=3400253,
        region=3402316,
        region_1=0,
        patrol_information_id=3403354,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        21,
        character=3400401,
        region=3402535,
        region_1=0,
        patrol_information_id=3403331,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        22,
        character=3400143,
        region=3402537,
        region_1=0,
        patrol_information_id=3403340,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        23,
        character=3400145,
        region=3402537,
        region_1=0,
        patrol_information_id=3403340,
        seconds=2.0,
        left=0,
    )
    Event_13405350(
        28,
        character=3400110,
        region=3402545,
        region_1=0,
        patrol_information_id=3403341,
        seconds=5.0,
        left=1,
    )
    Event_13405350(
        29,
        character=3400109,
        region=3402545,
        region_1=0,
        patrol_information_id=3403341,
        seconds=1.0,
        left=1,
    )
    Event_13405350(
        30,
        character=3400144,
        region=3402537,
        region_1=0,
        patrol_information_id=3403340,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        32,
        character=3400550,
        region=3402555,
        region_1=0,
        patrol_information_id=3403346,
        seconds=0.0,
        left=0,
    )
    Event_13405350(
        33,
        character=3400580,
        region=3402544,
        region_1=0,
        patrol_information_id=3403342,
        seconds=0.0,
        left=1,
    )
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
    Event_13405540(1, character=3400142, patrol_information_id=3403340, value=2, left=1, seconds=0.0)
    Event_13405540(2, character=3400155, patrol_information_id=3403345, value=2, left=1, seconds=2.0)
    Event_13405540(3, character=3400316, patrol_information_id=3403344, value=4, left=0, seconds=0.0)
    Event_13405640(
        0,
        character=3400404,
        animation_id=7000,
        ai_param_id=400028,
        animation=7001,
        ai_param_id_1=400028,
        min_seconds=0.0,
        max_seconds=0.0,
    )
    Event_13405680(0, character=3400165, character_1=3400166, radius=13.0)
    Event_13405680(1, character=3400165, character_1=3400167, radius=13.0)
    Event_13405680(2, character=3400165, character_1=3400168, radius=13.0)
    Event_13405216(0, character=3400509, region=3402542, region_1=0, patrol_information_id=3403338, seconds=1.0, left=0)
    Event_13405480(0, character=3400207, region=3402515, radius=3.0, animation_id=3010, seconds=0.0, state=0)
    Event_13405480(1, character=3400105, region=3402512, radius=5.0, animation_id=7002, seconds=0.0, state=1)
    Event_13405480(2, character=3400106, region=3402512, radius=5.0, animation_id=7003, seconds=4.0, state=1)
    Event_13405480(3, character=3400107, region=3402513, radius=3.0, animation_id=7004, seconds=0.0, state=0)
    Event_13405480(4, character=3400505, region=3402553, radius=3.0, animation_id=700, seconds=1.0, state=0)
    Event_13405480(5, character=3400506, region=3402553, radius=3.0, animation_id=700, seconds=0.0, state=0)
    Event_13405480(6, character=3400282, region=3402303, radius=3.0, animation_id=3006, seconds=0.0, state=0)
    Event_13405480(8, character=3400507, region=3402553, radius=3.0, animation_id=605, seconds=0.0, state=0)
    Event_13405480(9, character=3400468, region=3402562, radius=0.0, animation_id=3001, seconds=1.0, state=0)
    Event_13405480(10, character=3400469, region=3402562, radius=0.0, animation_id=3001, seconds=0.0, state=0)
    Event_13405480(13, character=3400472, region=3402562, radius=0.0, animation_id=3001, seconds=2.0, state=0)
    Event_13405480(11, character=3400315, region=3402540, radius=1.0, animation_id=702, seconds=2.0, state=0)
    Event_13405480(12, character=3400409, region=3402552, radius=1.0, animation_id=3012, seconds=0.0, state=0)
    Event_13400930()
    Event_13400900(2, character=3400902, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1710)
    Event_13400900(3, character=3400903, first_flag=1710, last_flag=1729, last_flag_1=1719, flag=1711)
    Event_13400910(2, attacked_entity=3400902, flag=73400420)
    Event_13400910(3, attacked_entity=3400903, flag=73400421)
    Event_13400920(2, character=3400902, flag=73400420, first_flag=1710, last_flag=1729, flag_1=1725)
    Event_13400920(3, character=3400903, flag=73400421, first_flag=1710, last_flag=1729, flag_1=1726)
    Event_13400970(0, character=3400910)
    Event_13400970(1, character=3400911)
    Event_13400980(0, flag=73400424, item_lot=43211)
    Event_13400953(0, flag=1710, flag_1=73400430, item_lot=43200)
    Event_13400953(1, flag=1711, flag_1=73400431, item_lot=43210)
    Event_13400995(0, flag=13400970, item_lot=43800, item_lot_1=43802, flag_1=6671)
    Event_13400980(1, flag=13400971, item_lot=43810)
    GotoIfFlagEnabled(Label.L2, flag=13400999)
    Event_13400941()
    Event_13400942(0, flag=73400512)
    Event_13400943(0, attacked_entity=3400900)
    Event_13400944()
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(3400900)

    # --- Label 3 --- #
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
        action_button_id=10567,
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
        action_button_id=10562,
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
        action_button_id=10563,
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
        action_button_id=10565,
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
        action_button_id=10562,
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
        action_button_id=10563,
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
        region_3=3402801,
    )
    Event_13404460(
        2,
        character=3400922,
        region=3402931,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404452,
        region_3=3402801,
    )
    Event_13404460(
        3,
        character=3400923,
        region=3402931,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404453,
        region_3=3402801,
    )
    Event_13404460(
        4,
        character=3400924,
        region=3402932,
        region_1=3402800,
        region_2=3402801,
        animation=101130,
        flag=13404454,
        region_3=3402801,
    )
    Event_13404460(
        5,
        character=3400925,
        region=3402935,
        region_1=3402850,
        region_2=3402851,
        animation=101130,
        flag=13404455,
        region_3=3402851,
    )
    Event_13404460(
        6,
        character=3400926,
        region=3402935,
        region_1=3402850,
        region_2=3402851,
        animation=101130,
        flag=13404456,
        region_3=3402851,
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


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13400940()
    Event_13400950(0, character=3400902, character_1=3400903)


@ContinueOnRest(13400010)
def Event_13400010():
    """Event 13400010"""
    DisableNetworkSync()
    DisableObject(3401801)
    DeleteVFX(3403801)
    OR_1.Add(ConnectingMultiplayer())
    OR_1.Add(Multiplayer())
    OR_1.Add(FlagDisabled(9471))
    
    MAIN.Await(OR_1)
    
    EnableObject(3401801)
    CreateVFX(3403801)
    OR_2.Add(ConnectingMultiplayer())
    OR_2.Add(Multiplayer())
    AND_1.Add(not OR_2)
    AND_1.Add(FlagEnabled(9471))
    
    MAIN.Await(AND_1)
    
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

    # --- Label 0 --- #
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


@ContinueOnRest(13401250)
def Event_13401250(_, other_entity: int, animation_id: int):
    """Event 13401250"""
    DisableNetworkSync()
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(other_entity, 6, wait_for_completion=True)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(other_entity, animation_id, wait_for_completion=True)
    Restart()


@ContinueOnRest(13401350)
def Event_13401350(_, other_entity: int, animation_id: int, region: int):
    """Event 13401350"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(other_entity, 6, wait_for_completion=True)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))

    # --- Label 0 --- #
    DefineLabel(0)
    WaitRandomFrames(min_frames=0, max_frames=75)
    ForceAnimation(other_entity, animation_id, wait_for_completion=True)
    Restart()


@ContinueOnRest(13401500)
def Event_13401500():
    """Event 13401500"""
    GotoIfFlagEnabled(Label.L0, flag=9469)
    DisableObject(3400600)
    
    MAIN.Await(FlagEnabled(9469))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=3404200)
    DisableMapPiece(map_piece_id=3404201)
    DisableMapPiece(map_piece_id=3404202)
    DisableMapPiece(map_piece_id=3404203)
    DeleteVFX(3403600)
    DeleteVFX(3403601)
    DeleteVFX(3403602)
    EnableObject(3400600)


@ContinueOnRest(13401000)
def Event_13401000():
    """Event 13401000"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(12401000))
    
    DisableFlag(12401000)
    AddSpecialEffect(PLAYER, 110)
    AddSpecialEffect(PLAYER, 111)
    AddSpecialEffect(PLAYER, 112)
    AddSpecialEffect(PLAYER, 113)
    AddSpecialEffect(PLAYER, 114)
    AddSpecialEffect(PLAYER, 115)
    AddSpecialEffect(PLAYER, 116)
    SetRespawnPoint(respawn_point=3402958)
    if ThisEventFlagEnabled():
        return
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest(13404700)
def Event_13404700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13404700"""
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag):
        return
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    AND_1.Add(Online())
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(InsideMap(game_map=HUNTERS_NIGHTMARE))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(PlayerLevel() >= 30)
    if FlagEnabled(flag_3):
        AND_2.Add(ClientTypeCountComparison(
            client_type=ClientType.Coop,
            comparison_type=ComparisonType.GreaterThanOrEqual,
            value=1,
        ))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 9025))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    if FlagEnabled(flag_3):
        DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13404710)
def Event_13404710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404710"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(InsideMap(game_map=HUNTERS_NIGHTMARE))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest(13404720)
def Event_13404720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404720"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(ClientTypeCountComparison(
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    ))
    OR_1.Add(OutsideMap(game_map=HUNTERS_NIGHTMARE))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RemoveSpecialEffect(PLAYER, 9020)
    RemoveSpecialEffect(character, 9100)
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
    OR_15.Add(FlagEnabled(flag_1))
    OR_15.Add(FlagEnabled(flag_2))
    OR_15.Add(FlagEnabled(flag_3))
    if OR_15:
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_5))
    AND_2.Add(HealthRatio(character) == 0.0)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(13404860))
    OR_1.Add(FlagEnabled(flag_6))
    OR_2.Add(AND_2)
    OR_2.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@RestartOnRest(13404740)
def Event_13404740():
    """Event 13404740"""
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(PlayerStandingOnCollision(3404000))
    OR_1.Add(PlayerStandingOnCollision(3404001))
    OR_1.Add(PlayerStandingOnCollision(3404002))
    OR_1.Add(PlayerStandingOnCollision(3404003))
    OR_1.Add(PlayerStandingOnCollision(3404004))
    OR_1.Add(PlayerStandingOnCollision(3404005))
    OR_1.Add(PlayerStandingOnCollision(3404006))
    OR_1.Add(PlayerStandingOnCollision(3404007))
    OR_1.Add(PlayerStandingOnCollision(3404008))
    OR_1.Add(PlayerStandingOnCollision(3404009))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13404741)
    AND_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(PlayerStandingOnCollision(3404000))
    OR_2.Add(PlayerStandingOnCollision(3404001))
    OR_2.Add(PlayerStandingOnCollision(3404002))
    OR_2.Add(PlayerStandingOnCollision(3404003))
    OR_2.Add(PlayerStandingOnCollision(3404004))
    OR_2.Add(PlayerStandingOnCollision(3404005))
    OR_2.Add(PlayerStandingOnCollision(3404006))
    OR_2.Add(PlayerStandingOnCollision(3404007))
    OR_2.Add(PlayerStandingOnCollision(3404008))
    OR_2.Add(PlayerStandingOnCollision(3404009))
    AND_2.Add(not OR_1)
    
    MAIN.Await(AND_2)
    
    DisableFlag(13404741)
    Restart()


@RestartOnRest(13404742)
def Event_13404742():
    """Event 13404742"""
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(PlayerStandingOnCollision(3404020))
    OR_1.Add(PlayerStandingOnCollision(3404021))
    OR_1.Add(PlayerStandingOnCollision(3404022))
    OR_1.Add(PlayerStandingOnCollision(3404023))
    OR_1.Add(PlayerStandingOnCollision(3404024))
    OR_1.Add(PlayerStandingOnCollision(3404025))
    OR_1.Add(PlayerStandingOnCollision(3404026))
    OR_1.Add(PlayerStandingOnCollision(3404027))
    OR_1.Add(PlayerStandingOnCollision(3404028))
    OR_1.Add(PlayerStandingOnCollision(3404029))
    OR_1.Add(PlayerStandingOnCollision(3404030))
    OR_1.Add(PlayerStandingOnCollision(3404031))
    OR_1.Add(PlayerStandingOnCollision(3404032))
    OR_1.Add(PlayerStandingOnCollision(3404033))
    OR_1.Add(PlayerStandingOnCollision(3404034))
    OR_1.Add(PlayerStandingOnCollision(3404035))
    OR_1.Add(PlayerStandingOnCollision(3404036))
    OR_1.Add(PlayerStandingOnCollision(3404037))
    OR_1.Add(PlayerStandingOnCollision(3404038))
    OR_1.Add(PlayerStandingOnCollision(3404039))
    OR_1.Add(PlayerStandingOnCollision(3404040))
    OR_1.Add(PlayerStandingOnCollision(3404041))
    OR_1.Add(PlayerStandingOnCollision(3404042))
    OR_1.Add(PlayerStandingOnCollision(3404043))
    OR_1.Add(PlayerStandingOnCollision(3404044))
    OR_1.Add(PlayerStandingOnCollision(3404045))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(13404743)
    AND_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(PlayerStandingOnCollision(3404020))
    OR_2.Add(PlayerStandingOnCollision(3404021))
    OR_2.Add(PlayerStandingOnCollision(3404022))
    OR_2.Add(PlayerStandingOnCollision(3404023))
    OR_2.Add(PlayerStandingOnCollision(3404024))
    OR_2.Add(PlayerStandingOnCollision(3404025))
    OR_2.Add(PlayerStandingOnCollision(3404026))
    OR_2.Add(PlayerStandingOnCollision(3404027))
    OR_2.Add(PlayerStandingOnCollision(3404028))
    OR_2.Add(PlayerStandingOnCollision(3404029))
    OR_2.Add(PlayerStandingOnCollision(3404030))
    OR_2.Add(PlayerStandingOnCollision(3404031))
    OR_2.Add(PlayerStandingOnCollision(3404032))
    OR_2.Add(PlayerStandingOnCollision(3404033))
    OR_2.Add(PlayerStandingOnCollision(3404034))
    OR_2.Add(PlayerStandingOnCollision(3404035))
    OR_2.Add(PlayerStandingOnCollision(3404036))
    OR_2.Add(PlayerStandingOnCollision(3404037))
    OR_2.Add(PlayerStandingOnCollision(3404038))
    OR_2.Add(PlayerStandingOnCollision(3404039))
    OR_2.Add(PlayerStandingOnCollision(3404040))
    OR_2.Add(PlayerStandingOnCollision(3404041))
    OR_2.Add(PlayerStandingOnCollision(3404042))
    OR_2.Add(PlayerStandingOnCollision(3404043))
    OR_2.Add(PlayerStandingOnCollision(3404044))
    OR_2.Add(PlayerStandingOnCollision(3404045))
    AND_2.Add(not OR_2)
    
    MAIN.Await(AND_2)
    
    DisableFlag(13404743)
    Restart()


@ContinueOnRest(13401800)
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

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(3400800))
    OR_1.Add(AND_1)
    if FlagDisabled(13400999):
        AND_2.Add(CharacterDead(3400801))
        OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401800)
    DeleteVFX(3403800)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    KillBoss(game_area_param_id=3400800)
    SkipLines(1)
    KillBoss(game_area_param_id=3400801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    if FlagEnabled(13400999):
        Wait(3.0)
        PlayCutscene(34000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
        WaitFrames(frames=1)
        Unknown_2003_27(arg1=0)
    AwardAchievement(achievement_id=36)
    RunEvent(9350, slot=0, args=(3,))
    if FlagDisabled(6674):
        AwardItemLot(3401800, host_only=False)
    else:
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

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(13404811)
def Event_13404811():
    """Event 13404811"""
    if FlagEnabled(9471):
        return
    if FlagEnabled(13401801):
        return
    DisableCharacter(3400800)
    AND_1.Add(FlagDisabled(13401800))
    AND_1.Add(FlagDisabled(13401801))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3402805))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404810)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    EnableFlag(9180)


@ContinueOnRest(13401801)
def Event_13401801():
    """Event 13401801"""
    if FlagEnabled(9471):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagDisabled(13401800))
    AND_2.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(13404811))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402805))
    
    MAIN.Await(AND_2)
    
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
    if FlagEnabled(9344):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9344)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(6001))
    
    Wait(0.0)


@ContinueOnRest(13401802)
def Event_13401802():
    """Event 13401802"""
    if FlagEnabled(13401803):
        return
    if FlagEnabled(13401800):
        return
    EnableInvincibility(3400810)
    
    MAIN.Await(FlagEnabled(13401801))
    
    AddSpecialEffect(3400810, 5401)
    DisableInvincibility(3400810)
    ForceAnimation(3400810, 3000)
    AND_1.Add(CharacterAlive(3400810))
    AND_1.Add(FlagEnabled(13401800))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3400810, 7000)


@RestartOnRest(13401803)
def Event_13401803():
    """Event 13401803"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DropMandatoryTreasure(3400810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(3400810))
    
    Wait(0.0)


@ContinueOnRest(13401804)
def Event_13401804():
    """Event 13401804"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13404808))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(3400800)
    EnableFlag(13404808)
    EnableFlag(13401801)


@ContinueOnRest(13404800)
def Event_13404800():
    """Event 13404800"""
    if FlagEnabled(9471):
        return
    GotoIfFlagEnabled(Label.L0, flag=13401801)
    SkipLinesIfClient(2)
    DisableObject(3401800)
    DeleteVFX(3403800, erase_root_only=False)
    AND_1.Add(FlagDisabled(13401800))
    AND_1.Add(FlagEnabled(13401801))
    
    MAIN.Await(AND_1)
    
    EnableObject(3401800)
    CreateVFX(3403800)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13401800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=3400800, entity=3401800))
    AND_3.Add(FlagEnabled(13401800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=3402801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(13404808)
    Restart()


@ContinueOnRest(13404801)
def Event_13404801():
    """Event 13404801"""
    DisableNetworkSync()
    if FlagEnabled(9471):
        return
    AND_1.Add(FlagDisabled(13401800))
    AND_1.Add(FlagEnabled(13401801))
    AND_1.Add(FlagEnabled(13404808))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3400800, entity=3401800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402801))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(13404809)
    Restart()


@ContinueOnRest(13404802)
def Event_13404802():
    """Event 13404802"""
    if FlagEnabled(9471):
        return
    DisableAI(3400800)
    DisableAI(3400801)
    DisableHealthBar(3400800)
    DisableHealthBar(3400801)
    ReferDamageToEntity(3400800, target_entity=3400801)
    if FlagEnabled(13400999):
        AddSpecialEffect(3400800, 8040)
        AddSpecialEffect(3400801, 8040)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(13404808))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(13404810):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3400801, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13404810)
    EnableFlag(13404808)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400801)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400801)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagDisabled(13404825):
        EnableAI(3400800)
        SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.EveryTwoFrames)
        EnableBossHealthBar(3400800, name=451000)
    else:
        EnableAI(3400801)
        SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
        SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
        EnableBossHealthBar(3400801, name=451005)
    CreatePlayLog(name=46)
    StartPlayLogMeasurement(measurement_id=3400010, name=62, overwrite=True)


@ContinueOnRest(13404803)
def Event_13404803():
    """Event 13404803"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3403802)
    DisableSoundEvent(sound_id=3403803)
    if FlagEnabled(9471):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagDisabled(13401800))
    AND_1.Add(FlagEnabled(13404802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(13404809))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3402802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=3403802)
    AND_2.Add(FlagEnabled(13404824))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13401800))
    AND_2.Add(FlagEnabled(13404802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(13404809))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=3403802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3403803)


@ContinueOnRest(13404804)
def Event_13404804():
    """Event 13404804"""
    DisableNetworkSync()
    if FlagEnabled(9471):
        return
    
    MAIN.Await(FlagEnabled(13404825))
    
    AND_3.Add(CharacterAlive(3400801))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=3400801, radius=9.0))
    
    MAIN.Await(AND_3)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    AND_4.Add(CharacterAlive(3400801))
    AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3400801, radius=12.0))
    
    MAIN.Await(AND_4)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


@ContinueOnRest(13404805)
def Event_13404805():
    """Event 13404805"""
    DisableNetworkSync()
    if FlagEnabled(9471):
        return
    
    MAIN.Await(FlagEnabled(13401800))
    
    DisableBossMusic(sound_id=3403802)
    DisableBossMusic(sound_id=3403803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(13404806)
def Event_13404806():
    """Event 13404806"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3401800, radius=6.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(13404807)
def Event_13404807():
    """Event 13404807"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3401800, radius=6.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3401800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(13404820)
def Event_13404820():
    """Event 13404820"""
    if FlagEnabled(9471):
        return
    AND_1.Add(FlagEnabled(13400999))
    AND_1.Add(HealthRatio(3400800) < 0.8999999761581421)
    OR_1.Add(AND_1)
    AND_2.Add(FlagDisabled(13400999))
    AND_2.Add(HealthRatio(3400800) < 0.8999999761581421)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterHasTAEEvent(3400800, tae_event_id=10))
    AND_4.Add(CharacterHasTAEEvent(3400800, tae_event_id=20))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    AICommand(3400800, command_id=100, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(3400800, tae_event_id=20))
    
    AICommand(3400800, command_id=-1, command_slot=0)


@ContinueOnRest(13404821)
def Event_13404821():
    """Event 13404821"""
    if FlagEnabled(9471):
        return
    AND_1.Add(FlagEnabled(13400999))
    AND_1.Add(HealthRatio(3400800) < 0.800000011920929)
    OR_1.Add(AND_1)
    AND_2.Add(FlagDisabled(13400999))
    AND_2.Add(HealthRatio(3400800) < 0.8500000238418579)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterHasTAEEvent(3400800, tae_event_id=10))
    AND_3.Add(FlagEnabled(13404820))
    AND_4.Add(CharacterHasTAEEvent(3400800, tae_event_id=30))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    AICommand(3400800, command_id=101, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(3400800, tae_event_id=30))
    
    AICommand(3400800, command_id=-1, command_slot=0)


@ContinueOnRest(13404822)
def Event_13404822():
    """Event 13404822"""
    if FlagEnabled(9471):
        return
    AND_1.Add(FlagEnabled(13400999))
    AND_1.Add(HealthRatio(3400800) < 0.699999988079071)
    OR_1.Add(AND_1)
    AND_2.Add(FlagDisabled(13400999))
    AND_2.Add(HealthRatio(3400800) < 0.800000011920929)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterHasTAEEvent(3400800, tae_event_id=10))
    AND_3.Add(FlagEnabled(13404821))
    AND_4.Add(CharacterHasTAEEvent(3400800, tae_event_id=40))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    AICommand(3400800, command_id=102, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(3400800, tae_event_id=40))
    
    AICommand(3400800, command_id=-1, command_slot=0)


@ContinueOnRest(13404823)
def Event_13404823():
    """Event 13404823"""
    if FlagEnabled(9471):
        return
    AND_1.Add(FlagEnabled(13400999))
    AND_1.Add(HealthRatio(3400800) < 0.5)
    OR_1.Add(AND_1)
    AND_2.Add(FlagDisabled(13400999))
    AND_2.Add(HealthRatio(3400800) < 0.75)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterHasTAEEvent(3400800, tae_event_id=10))
    AND_3.Add(FlagEnabled(13404822))
    AND_4.Add(CharacterHasTAEEvent(3400800, tae_event_id=50))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    AICommand(3400800, command_id=103, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(3400800, tae_event_id=50))
    
    AICommand(3400800, command_id=-1, command_slot=0)


@ContinueOnRest(13404824)
def Event_13404824():
    """Event 13404824"""
    if FlagEnabled(9471):
        return
    if FlagEnabled(13404825):
        return
    AND_1.Add(HealthRatio(3400800) < 0.5)
    AND_1.Add(HealthRatio(3400800) > 0.0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(9180)


@ContinueOnRest(13404825)
def Event_13404825():
    """Event 13404825"""
    if FlagEnabled(9471):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(3400800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(3400801)
    DisableAnimations(3400801)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13404824))
    
    MAIN.Await(AND_1)
    
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
    RemoveSpecialEffect(3400801, 5300)
    AddSpecialEffect(3400801, 5333)
    EnableAI(3400801)
    EnableBossHealthBar(3400801, name=451005)


@ContinueOnRest(13404830)
def Event_13404830(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect: int,
    animation_id: int,
    frames: int,
):
    """Event 13404830"""
    if FlagEnabled(9471):
        return
    CreateNPCPart(3400800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(3400800, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    AND_2.Add(CharacterPartHealth(3400800, npc_part_id=npc_part_id_1) <= 0)
    OR_1.Add(HealthRatio(3400800) <= 0.0)
    OR_1.Add(FlagEnabled(13404825))
    OR_2.Add(AND_2)
    OR_2.Add(OR_1)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=OR_1)
    CreateNPCPart(3400800, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999, damage_correction=1.5)
    SetNPCPartEffects(3400800, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    ForceAnimation(3400800, animation_id)
    AddSpecialEffect(3400800, special_effect)
    WaitFrames(frames=frames)
    AND_3.Add(FramesElapsed(frames=frames))
    OR_3.Add(HealthRatio(3400800) <= 0.0)
    OR_3.Add(FlagEnabled(13404825))
    OR_4.Add(AND_3)
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    EndIfFinishedConditionTrue(input_condition=OR_3)
    ReplanAI(3400800)
    AND_4.Add(TimeElapsed(seconds=5.0))
    OR_5.Add(HealthRatio(3400800) <= 0.0)
    OR_5.Add(FlagEnabled(13404825))
    OR_6.Add(AND_4)
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)
    
    EndIfFinishedConditionTrue(input_condition=OR_5)
    SetNPCPartHealth(3400800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    RemoveSpecialEffect(3400800, special_effect)
    WaitFrames(frames=10)
    AND_5.Add(FramesElapsed(frames=10))
    OR_7.Add(HealthRatio(3400800) <= 0.0)
    OR_7.Add(FlagEnabled(13404825))
    OR_8.Add(AND_5)
    OR_8.Add(OR_7)
    
    MAIN.Await(OR_8)
    
    EndIfFinishedConditionTrue(input_condition=OR_7)
    Restart()


@ContinueOnRest(13404835)
def Event_13404835():
    """Event 13404835"""
    if FlagEnabled(9471):
        return
    AND_1.Add(HealthRatio(3400801) < 0.3499999940395355)
    AND_1.Add(HealthRatio(3400801) > 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3400801, 7002)
    AICommand(3400801, command_id=110, command_slot=0)
    ReplanAI(3400801)
    AND_3.Add(HealthRatio(3400801) < 0.06700000166893005)
    AND_3.Add(HealthRatio(3400801) > 0.0)
    
    MAIN.Await(AND_3)
    
    ForceAnimation(3400801, 7003)
    AND_4.Add(HealthRatio(3400801) < 0.032999999821186066)
    AND_4.Add(HealthRatio(3400801) > 0.0)
    
    MAIN.Await(AND_4)
    
    ForceAnimation(3400801, 7002)


@ContinueOnRest(13404840)
def Event_13404840():
    """Event 13404840"""
    if FlagEnabled(9471):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3400800, tae_event_id=100))
    
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


@ContinueOnRest(13404841)
def Event_13404841():
    """Event 13404841"""
    if FlagEnabled(9471):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3400801, tae_event_id=300))
    
    AICommand(3400801, command_id=-1, command_slot=0)
    ReplanAI(3400801)


@ContinueOnRest(13401850)
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(3400850))
    
    EnableFlag(3400)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401850)
    DeleteVFX(3403850)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=3400850)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    AwardAchievement(achievement_id=39)
    RunEvent(9350, slot=0, args=(3,))
    if FlagDisabled(6673):
        AwardItemLot(3401850, host_only=False)
    else:
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

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@RestartOnRest(13404861)
def Event_13404861():
    """Event 13404861"""
    if FlagEnabled(13401850):
        return
    GotoIfFlagDisabled(Label.L0, flag=13401851)
    Move(3400850, destination=3402853, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(3400850)
    DisableGravity(3400850)
    EnableInvincibility(3400850)
    ForceAnimation(3400850, 7002, loop=True)
    AND_1.Add(FlagDisabled(13401850))
    AND_1.Add(FlagDisabled(13401851))
    AND_1.Add(PlayerHasGood(4014))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3402855))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404860)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    EnableFlag(9180)


@RestartOnRest(13401851)
def Event_13401851():
    """Event 13401851"""
    if FlagEnabled(13401850):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagDisabled(13401850))
    AND_2.Add(FlagDisabled(13401851))
    AND_2.Add(FlagEnabled(13404861))
    AND_2.Add(PlayerHasGood(4014))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402855))
    
    MAIN.Await(AND_2)
    
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
    if FlagEnabled(9302):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9302)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(6001))
    
    Wait(0.0)


@ContinueOnRest(13401853)
def Event_13401853():
    """Event 13401853"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13404858))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableGravity(3400850)
    DisableInvincibility(3400850)
    EnableCharacterCollision(3400850)
    EnableFlag(13404858)
    EnableFlag(13401851)


@ContinueOnRest(13404850)
def Event_13404850():
    """Event 13404850"""
    if FlagEnabled(13401850):
        return
    GotoIfFlagEnabled(Label.L0, flag=13401851)
    SkipLinesIfClient(2)
    DisableObject(3401850)
    DeleteVFX(3403850, erase_root_only=False)
    AND_1.Add(FlagDisabled(13401850))
    AND_1.Add(FlagEnabled(13401851))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableObject(3401850)
    CreateVFX(3403850)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterHuman(PLAYER))
    AND_3.Add(ActionButtonParamActivated(action_button_id=3400850, entity=3401850))
    AND_3.Add(FlagDisabled(13401850))
    AND_4.Add(FlagEnabled(13401850))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=3402851))
    AND_6.Add(CharacterHuman(PLAYER))
    AND_6.Add(TimeElapsed(seconds=2.0))
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_6)
    EnableFlag(13404858)
    Restart()


@ContinueOnRest(13404851)
def Event_13404851():
    """Event 13404851"""
    DisableNetworkSync()
    if FlagEnabled(13401850):
        return
    AND_1.Add(FlagDisabled(13401850))
    AND_1.Add(FlagEnabled(13401851))
    AND_1.Add(FlagEnabled(13404858))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3400850, entity=3401850))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402851))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(13404859)
    Restart()


@RestartOnRest(13404852)
def Event_13404852():
    """Event 13404852"""
    if FlagEnabled(13401850):
        return
    DisableAI(3400850)
    DisableHealthBar(3400850)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(13404858))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(13404860):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400850, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13404860)
    EnableFlag(13404858)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400850, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400850)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400850, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3400850)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(3400850)
    EnableBossHealthBar(3400850, name=450000)
    CreatePlayLog(name=46)
    StartPlayLogMeasurement(measurement_id=3400030, name=62, overwrite=True)


@ContinueOnRest(13404853)
def Event_13404853():
    """Event 13404853"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=3403852)
    DisableSoundEvent(sound_id=3403853)
    if FlagEnabled(13401850):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagDisabled(13401850))
    AND_1.Add(FlagEnabled(13404852))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(13404859))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3402852))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=3403852)
    AND_2.Add(CharacterHasTAEEvent(3400850, tae_event_id=400))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13401850))
    AND_2.Add(FlagEnabled(13404852))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(13404859))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3402852))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=3403852)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3403853)


@ContinueOnRest(13404854)
def Event_13404854():
    """Event 13404854"""
    DisableNetworkSync()
    if FlagEnabled(13401850):
        return
    AND_1.Add(CharacterAlive(3400850))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3400850, radius=14.0))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    AND_2.Add(CharacterAlive(3400850))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3400850, radius=17.0))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


@ContinueOnRest(13404855)
def Event_13404855():
    """Event 13404855"""
    DisableNetworkSync()
    if FlagEnabled(13401850):
        return
    
    MAIN.Await(FlagEnabled(13401850))
    
    DisableBossMusic(sound_id=3403852)
    DisableBossMusic(sound_id=3403853)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(13404856)
def Event_13404856():
    """Event 13404856"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3401850, radius=6.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(13404857)
def Event_13404857():
    """Event 13404857"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3401850, radius=6.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3401850, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@RestartOnRest(13404870)
def Event_13404870(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    special_effect: int,
    special_effect_1: int,
    part_health: int,
    animation_id: int,
):
    """Event 13404870"""
    if FlagEnabled(13401850):
        return
    CreateNPCPart(3400850, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(3400850, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    AND_1.Add(CharacterPartHealth(3400850, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(3400850) <= 0.0)
    AND_3.Add(CharacterHasSpecialEffect(3400850, 5402))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    EndIfFinishedConditionTrue(input_condition=AND_3)
    CreateNPCPart(3400850, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999)
    SetNPCPartEffects(3400850, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    ForceAnimation(3400850, animation_id)
    AddSpecialEffect(3400850, special_effect)
    RemoveSpecialEffect(3400850, special_effect_1)
    ReplanAI(3400850)
    AND_4.Add(TimeElapsed(seconds=30.0))
    AND_5.Add(CharacterHasSpecialEffect(3400850, 5402))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_5)
    AICommand(3400850, command_id=100, command_slot=1)
    ReplanAI(3400850)
    AND_6.Add(CharacterHasTAEEvent(3400850, tae_event_id=300))
    AND_7.Add(CharacterHasSpecialEffect(3400850, 5402))
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_7)
    SetNPCPartHealth(3400850, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    RemoveSpecialEffect(3400850, special_effect)
    AddSpecialEffect(3400850, special_effect_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(3400850, command_id=-1, command_slot=1)
    ReplanAI(3400850)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(13404875)
def Event_13404875():
    """Event 13404875"""
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasTAEEvent(3400850, tae_event_id=400))

    # --- Label 0 --- #
    DefineLabel(0)
    SetCollisionMask(3400850, bit_index=10, switch_type=OnOffChange.Off)


@ContinueOnRest(13401200)
def Event_13401200(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 13401200"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


@ContinueOnRest(13401210)
def Event_13401210(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 13401210"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@ContinueOnRest(13401220)
def Event_13401220():
    """Event 13401220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=3401100, animation_id=1)
    DisableObjectActivation(3401110, obj_act_id=3400020)
    NotifyDoorEventSoundDampening(obj=3401100, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=13400002))
    
    DisableObjectActivation(3401110, obj_act_id=3400020)
    ForceAnimation(3401100, 1)
    Wait(0.0)


@ContinueOnRest(13400100)
def Event_13400100():
    """Event 13400100"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    
    MAIN.Await(PlayerStandingOnCollision(3404000))
    
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest(13400220)
def Event_13400220(_, character: int, flag: int):
    """Event 13400220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(0.0)


@RestartOnRest(13400310)
def Event_13400310(_, character: int, region: int):
    """Event 13400310"""
    DisableGravity(character)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    ForceAnimation(character, 7004, loop=True, skip_transition=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 7005, loop=True)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 7003, wait_for_completion=True)


@RestartOnRest(13400320)
def Event_13400320():
    """Event 13400320"""
    if FlagEnabled(9470):
        return
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    CreateObjectVFX(3401500, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3400100, entity=3401500))
    
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(0.0)


@RestartOnRest(13404799)
def Event_13404799():
    """Event 13404799"""
    CreateProjectileOwner(entity=3400799)


@RestartOnRest(13405100)
def Event_13405100(_, obj: int, region: int, region_1: int):
    """Event 13405100"""
    WaitFrames(frames=1)
    OR_10.Add(CharacterDead(3400206))
    OR_10.Add(CharacterDead(3400205))
    OR_10.Add(ObjectDestroyed(3401401))
    OR_10.Add(ThisEventSlotFlagEnabled())
    GotoIfConditionTrue(Label.L0, input_condition=OR_10)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=13405101)
    DeleteObjectVFX(obj)
    EnableObject(3401401)
    DisableObject(obj)
    DestroyObject(3401401)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(3401401)
    ForceAnimation(obj, 0, loop=True)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_3.Add(FlagEnabled(13405101))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    EnableFlag(13405101)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_3)
    OR_3.Add(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=22.0))
    OR_3.Add(TimeElapsed(seconds=4.0))
    
    MAIN.Await(OR_3)

    # --- Label 2 --- #
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
    OR_10.Add(ThisEventSlotFlagEnabled())
    OR_10.Add(CharacterDead(3400551))
    GotoIfConditionTrue(Label.L0, input_condition=OR_10)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3401010, 11, loop=True)
    EndOfAnimation(obj=3401010, animation_id=11)
    EnableAI(3400551)
    SetNest(3400551, region=3402310)
    ReplanAI(3400551)
    DisableObjectActivation(3401010, obj_act_id=3400000)
    NotifyDoorEventSoundDampening(obj=3401010, state=DoorState.DoorOpening)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAI(3400551)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=3402300))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=3400551, radius=7.0))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=3400551))
    
    MAIN.Await(OR_3)
    
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
    obj: int,
    launch_angle_x: int,
    launch_angle_y: int,
    launch_angle_z: int,
):
    """Event 13405105"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    
    MAIN.Await(ObjectNotDestroyed(obj))
    
    ForceAnimation(obj, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=6281,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=6282,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=6283,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=2)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=launch_angle_x,
        launch_angle_y=launch_angle_y,
        launch_angle_z=launch_angle_z,
    )
    WaitFrames(frames=60)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterHasTAEEvent(3400200, tae_event_id=10))
    
    ReplanAI(3400406)
    SetAIParamID(3400406, ai_param_id=400018)
    SetAIParamID(3400200, ai_param_id=263757)
    ReplanAI(3400200)
    if ValueNotEqual(left=1, right=0):
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3402533))
    
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
    obj: int,
    flag: int,
    frames: int,
    frames_1: int,
    behavior_id: int,
    behavior_id_1: int,
    behavior_id_2: int,
    behavior_id_3: int,
):
    """Event 13405113"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ObjectNotDestroyed(obj))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(FramesElapsed(frames=frames))
    
    ForceAnimation(obj, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_1,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_2,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_3,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    MAIN.Await(FramesElapsed(frames=frames_1))
    
    Restart()


@RestartOnRest(13405115)
def Event_13405115(
    _,
    obj: int,
    flag: int,
    frames: int,
    frames_1: int,
    behavior_id: int,
    behavior_id_1: int,
    behavior_id_2: int,
    behavior_id_3: int,
):
    """Event 13405115"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ObjectNotDestroyed(obj))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(FramesElapsed(frames=frames))
    
    ForceAnimation(obj, 1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_1,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_2,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id_3,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=200,
        behavior_id=behavior_id,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    
    MAIN.Await(FramesElapsed(frames=2))
    
    MAIN.Await(FramesElapsed(frames=frames_1))
    
    Restart()


@RestartOnRest(13405140)
def Event_13405140(_, character: int, region: int, flag: int, region_1: int, entity: int, frames: int):
    """Event 13405140"""
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterInsideRegion(character, region=region_1))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    
    MAIN.Await(FramesElapsed(frames=frames))
    
    AND_2.Add(CharacterAlive(character))
    AND_2.Add(CharacterInsideRegion(character, region=region_1))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    if not AND_2:
        return RESTART
    EnableFlag(flag)
    OR_1.Add(CharacterDead(character))
    OR_1.Add(CharacterOutsideRegion(character, region=region_1))
    OR_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=10)
    ForceAnimation(entity, 0, loop=True)
    DisableFlag(flag)
    Restart()


@RestartOnRest(13405145)
def Event_13405145(_, region: int, entity: int, flag: int):
    """Event 13405145"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    EnableFlag(flag)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    WaitFrames(frames=10)
    ForceAnimation(entity, 0, loop=True)
    DisableFlag(flag)
    Restart()


@RestartOnRest(13405155)
def Event_13405155(_, region: int):
    """Event 13405155"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    PlaySoundEffect(3402515, 411005002, sound_type=SoundType.a_Ambient)


@RestartOnRest(13405160)
def Event_13405160(_, obj: int):
    """Event 13405160"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Fire))
    OR_1.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.NoType))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Magic))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Lightning))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Blunt))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Slash))
    OR_2.Add(AttackedWithDamageType(attacked_entity=obj, damage_type=DamageType.Thrust))
    AND_2.Add(OR_2)
    AND_2.Add(ObjectHealthValueComparison(obj, ComparisonType.LessThanOrEqual, value=999))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj)
    PlaySoundEffect(obj, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3400799,
        source_entity=obj,
        model_point=-1,
        behavior_id=6292,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(obj)
    PlaySoundEffect(obj, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(13405200)
def Event_13405200(_, character: int, region: int, animation_id: int, region_1: int):
    """Event 13405200"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_3.Add(HealthRatio(character) <= 0.0)
    OR_3.Add(AND_3)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(CharacterOutsideRegion(character, region=region_1))
    AND_4.Add(HealthRatio(character) <= 0.0)
    OR_2.Add(OR_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    RestartIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(character)
    ForceAnimation(character, 0, wait_for_completion=True)
    Restart()


@RestartOnRest(13405211)
def Event_13405211(_, region: int):
    """Event 13405211"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
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
    OR_2.Add(CharacterInsideRegion(3400316, region=region))
    OR_2.Add(CharacterInsideRegion(3400316, region=region_1))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueNotEqual(left=left, right=0):
        AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13405218)
def Event_13405218():
    """Event 13405218"""
    GotoIfThisEventFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3402553))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
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
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405300)
def Event_13405300(_, character: int, region: int, radius: float, seconds: float):
    """Event 13405300"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    AND_2.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
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
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueNotEqual(left=left, right=0):
        AddSpecialEffect(character, 5000)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)


@RestartOnRest(13405480)
def Event_13405480(_, character: int, region: int, radius: float, animation_id: int, seconds: float, state: uchar):
    """Event 13405480"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIState(character, state)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    AND_4.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_4)
    Wait(seconds)
    ForceAnimation(character, animation_id)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(13405510)
def Event_13405510(_, character: int):
    """Event 13405510"""
    MAIN.Await(CharacterDead(character))
    
    IncrementEventValue(13405500, bit_count=4, max_value=15)


@RestartOnRest(13405520)
def Event_13405520(_, character: int, region: int):
    """Event 13405520"""
    MAIN.Await(EventValue(flag=13405500, bit_count=4) >= 4)
    
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=2)
    ReplanAI(character)


@RestartOnRest(13405530)
def Event_13405530(_, character: int, region: int):
    """Event 13405530"""
    MAIN.Await(EventValue(flag=13405500, bit_count=4) >= 2)
    
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=3)
    ReplanAI(character)


@RestartOnRest(13405540)
def Event_13405540(_, character: int, patrol_information_id: int, value: uint, left: int, seconds: float):
    """Event 13405540"""
    MAIN.Await(EventValue(flag=13405500, bit_count=4) >= value)
    
    if ValueNotEqual(left=left, right=0):
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
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(EventValue(flag=13405500, bit_count=4) >= 2)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405570)
def Event_13405570(_, character: int, region: int, region_1: int, command_id: int, command_slot: uchar):
    """Event 13405570"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    SetEventPoint(character, region=region, reaction_range=0.5)
    ReplanAI(character)
    AICommand(character, command_id=command_id, command_slot=command_slot)


@RestartOnRest(13405610)
def Event_13405610(_, character: int):
    """Event 13405610"""
    MAIN.Await(CharacterDead(character))
    
    IncrementEventValue(13405600, bit_count=4, max_value=15)


@RestartOnRest(13405620)
def Event_13405620(_, character: int, region: int):
    """Event 13405620"""
    MAIN.Await(EventValue(flag=13405600, bit_count=4) >= 4)
    
    SetEventPoint(character, region=region, reaction_range=0.5)
    AICommand(character, command_id=100, command_slot=2)
    ReplanAI(character)


@RestartOnRest(13405630)
def Event_13405630(_, character: int, region: int):
    """Event 13405630"""
    MAIN.Await(EventValue(flag=13405600, bit_count=4) >= 2)
    
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
    
    MAIN.Await(EventValue(flag=13405600, bit_count=4) >= 1)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
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
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(EventValue(flag=13405600, bit_count=4) >= 2)
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(13405680)
def Event_13405680(_, character: int, character_1: int, radius: float):
    """Event 13405680"""
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=character_1, radius=radius))
    AND_1.Add(CharacterAlive(character_1))
    AND_1.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_1)
    
    AICommand(character_1, command_id=200, command_slot=1)
    
    MAIN.Await(CharacterHasTAEEvent(character_1, tae_event_id=20))
    
    AddSpecialEffect(character_1, 5645)
    AICommand(character_1, command_id=-1, command_slot=1)
    Restart()


@ContinueOnRest(13400940)
def Event_13400940():
    """Event 13400940"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    GotoIfFlagRangeAnyEnabled(Label.L1, flag_range=(1670, 1689))
    DisableFlagRange((1670, 1689))
    EnableFlag(1680)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(13401800))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(1670, 1674)))
    GotoIfConditionFalse(Label.L2, input_condition=AND_1)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(FlagEnabled(1681))
    OR_1.Add(FlagEnabled(1720))
    OR_1.Add(FlagEnabled(1721))
    AND_2.Add(OR_1)
    AND_2.Add(FlagEnabled(73400513))
    AND_2.Add(FlagEnabled(73400403))
    GotoIfConditionFalse(Label.L3, input_condition=AND_2)
    DisableFlagRange((1670, 1689))
    EnableFlag(1671)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_3.Add(FlagEnabled(13500100))
    OR_2.Add(FlagEnabled(1720))
    OR_2.Add(FlagEnabled(1721))
    OR_2.Add(FlagEnabled(1724))
    OR_2.Add(FlagEnabled(1722))
    AND_3.Add(OR_2)
    AND_3.Add(FlagEnabled(73400403))
    AND_4.Add(FlagEnabled(1681))
    AND_4.Add(FlagDisabled(73400512))
    OR_3.Add(AND_4)
    OR_3.Add(FlagEnabled(1671))
    AND_3.Add(OR_3)
    GotoIfConditionFalse(Label.L4, input_condition=AND_3)
    DisableFlagRange((1670, 1689))
    EnableFlag(1672)

    # --- Label 4 --- #
    DefineLabel(4)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L5, flag=1670)
    GotoIfFlagEnabled(Label.L6, flag=1671)
    GotoIfFlagEnabled(Label.L7, flag=1672)
    GotoIfFlagEnabled(Label.L8, flag=1680)
    GotoIfFlagEnabled(Label.L9, flag=1681)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    End()

    # --- Label 8 --- #
    DefineLabel(8)
    EnableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- Label 9 --- #
    DefineLabel(9)
    EnableBackread(3400900)
    EnableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    EnableImmortality(3400900)
    AND_7.Add(FlagDisabled(50002360))
    AND_7.Add(FlagEnabled(73400512))
    SkipLinesIfConditionFalse(1, AND_7)
    DropMandatoryTreasure(3400906)
    if FlagEnabled(73400512):
        ForceAnimation(3400900, 7002, loop=True, skip_transition=True)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    EnableObject(3400908)
    if FlagDisabled(50002360):
        EnableBackread(3400906)
        EnableCharacter(3400906)
        DropMandatoryTreasure(3400906)
        End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- Label 7 --- #
    DefineLabel(7)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    if FlagDisabled(50002360):
        EnableBackread(3400906)
        EnableCharacter(3400906)
        DropMandatoryTreasure(3400906)
        End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()


@ContinueOnRest(13400941)
def Event_13400941():
    """Event 13400941"""
    if FlagDisabled(1680):
        return
    OR_1.Add(CharacterDead(3400800))
    OR_1.Add(CharacterDead(3400801))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(AllPlayersOutsideRegion(region=3402915))
    AND_1.Add(CharacterOutsideRegion(3400921, region=3402915))
    AND_1.Add(CharacterOutsideRegion(3400922, region=3402915))
    AND_1.Add(CharacterOutsideRegion(3400923, region=3402915))
    AND_1.Add(CharacterOutsideRegion(3400924, region=3402915))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    Move(3400900, destination=3402911, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(AllPlayersOutsideRegion(region=3402916))
    AND_2.Add(CharacterOutsideRegion(3400921, region=3402916))
    AND_2.Add(CharacterOutsideRegion(3400922, region=3402916))
    AND_2.Add(CharacterOutsideRegion(3400923, region=3402916))
    AND_2.Add(CharacterOutsideRegion(3400924, region=3402916))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    Move(3400900, destination=3402912, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(AllPlayersOutsideRegion(region=3402917))
    AND_3.Add(CharacterOutsideRegion(3400921, region=3402917))
    AND_3.Add(CharacterOutsideRegion(3400922, region=3402917))
    AND_3.Add(CharacterOutsideRegion(3400923, region=3402917))
    AND_3.Add(CharacterOutsideRegion(3400924, region=3402917))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    Move(3400900, destination=3402913, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(3400900, destination=34029134, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableCharacter(3400900)
    EnableImmortality(3400900)


@ContinueOnRest(13400942)
def Event_13400942(_, flag: int):
    """Event 13400942"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if ThisEventSlotFlagEnabled():
        return
    EndIfFlagRangeAllDisabled(flag_range=(1680, 1681))
    if FlagEnabled(flag):
        return
    if FlagEnabled(73400519):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(73400519))
    OR_1.Add(CharacterDead(3400900))
    
    MAIN.Await(OR_1)
    
    EnableCharacter(3400906)
    Move(3400906, destination=3400900, destination_type=CoordEntityType.Character, model_point=10, short_move=True)
    WaitFrames(frames=1)
    DropMandatoryTreasure(3400906)
    if FlagEnabled(73400519):
        return
    ForceAnimation(3400900, 7002, loop=True, skip_transition=True)


@ContinueOnRest(13400943)
def Event_13400943(_, attacked_entity: int):
    """Event 13400943"""
    OR_1.Add(FlagEnabled(1681))
    AND_1.Add(OR_1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1670, 1689))
    EnableFlag(1670)
    SaveRequest()
    WaitFrames(frames=1)
    ForceAnimation(attacked_entity, 7010, skip_transition=True)
    WaitFrames(frames=119)
    ForceAnimation(attacked_entity, 7011, loop=True, skip_transition=True)
    EnableFlag(73400519)


@ContinueOnRest(13400944)
def Event_13400944():
    """Event 13400944"""
    DisableFlag(73400510)
    OR_1.Add(FlagEnabled(1670))
    OR_1.Add(FlagEnabled(1671))
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(73400512))
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(73400510))
    
    OR_2.Add(HealthRatio(3400900) == 0.0)
    OR_2.Add(FlagEnabled(73400512))
    OR_2.Add(FlagEnabled(1670))
    if OR_2:
        return
    ForceAnimation(3400900, 7001, loop=True, skip_transition=True)
    
    MAIN.Await(FlagDisabled(73400510))
    
    OR_3.Add(HealthRatio(3400900) == 0.0)
    OR_3.Add(FlagEnabled(73400512))
    OR_3.Add(FlagEnabled(1670))
    if OR_3:
        return
    ForceAnimation(3400900, 0, loop=True, skip_transition=True)
    Restart()


@ContinueOnRest(13400900)
def Event_13400900(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 13400900"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    AND_1.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(13400910)
def Event_13400910(_, attacked_entity: int, flag: int):
    """Event 13400910"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    EnableFlag(flag)


@ContinueOnRest(13400920)
def Event_13400920(_, character: int, flag: int, first_flag: int, last_flag: int, flag_1: int):
    """Event 13400920"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    SaveRequest()


@ContinueOnRest(13400930)
def Event_13400930():
    """Event 13400930"""
    DisableAI(3400910)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=3402949))
    OR_1.Add(AttackedWithDamageType(attacked_entity=3400910, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(3400910)


@ContinueOnRest(13400950)
def Event_13400950(_, character: int, character_1: int):
    """Event 13400950"""
    OR_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L9, input_condition=OR_15)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=1724)
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(1720))
    OR_1.Add(FlagEnabled(1681))
    OR_1.Add(FlagEnabled(1671))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(73400403))
    AND_1.Add(FlagEnabled(73400513))
    OR_2.Add(AND_1)
    AND_2.Add(FlagEnabled(1720))
    AND_2.Add(FlagEnabled(73400403))
    AND_2.Add(FlagEnabled(1670))
    OR_2.Add(AND_2)
    GotoIfConditionFalse(Label.L2, input_condition=OR_2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1721)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagRangeAnyEnabled(flag_range=(1720, 1721)))
    AND_3.Add(FlagEnabled(73400403))
    AND_3.Add(FlagEnabled(13500100))
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1722)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1720, 1722)))
    AND_4.Add(FlagEnabled(73400403))
    AND_4.Add(FlagEnabled(1650))
    GotoIfConditionFalse(Label.L8, input_condition=AND_4)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103150)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.Ally)
    ForceAnimation(character_1, 103150)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DropMandatoryTreasure(character_1)
    End()


@ContinueOnRest(13400951)
def Event_13400951(_, character: int, flag: int, flag_1: int):
    """Event 13400951"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    DisableFlag(flag)
    if FlagDisabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(character, 151))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103155)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag))
    AND_2.Add(CharacterHasSpecialEffect(character, 152))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(character, 103150)
    Restart()


@ContinueOnRest(13400953)
def Event_13400953(_, flag: int, flag_1: int, item_lot: int):
    """Event 13400953"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    AwardItemLot(item_lot, host_only=False)


@ContinueOnRest(13400970)
def Event_13400970(_, character: int):
    """Event 13400970"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(0.0)


@ContinueOnRest(13400980)
def Event_13400980(_, flag: int, item_lot: int):
    """Event 13400980"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(item_lot, host_only=False)


@ContinueOnRest(13400990)
def Event_13400990(_, flag: int, item_lot: int):
    """Event 13400990"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    AwardItemLot(item_lot, host_only=False)
    Restart()


@ContinueOnRest(13400995)
def Event_13400995(_, flag: int, item_lot: int, item_lot_1: int, flag_1: int):
    """Event 13400995"""
    if FlagEnabled(flag):
        return
    if Client():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    if FlagDisabled(flag_1):
        AwardItemLot(item_lot, host_only=False)
    else:
        AwardItemLot(item_lot_1, host_only=False)


@RestartOnRest(13404450)
def Event_13404450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404450"""
    if ThisEventSlotFlagEnabled():
        return
    if Client():
        return
    SetEventPoint(character, region=region, reaction_range=1.0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13404401)
def Event_13404401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(13404422, 13404426)))
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(FlagRangeAllDisabled(flag_range=(13404422, 13404426)))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404402)
def Event_13404402(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404402"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_4.Add(FlagEnabled(1800))
    OR_4.Add(FlagEnabled(1801))
    AND_1.Add(OR_4)
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_5.Add(FlagEnabled(1800))
    OR_5.Add(FlagEnabled(1801))
    AND_2.Add(OR_5)
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404403)
def Event_13404403(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404403"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagEnabled(6813))
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_2.Add(FlagEnabled(6813))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404404)
def Event_13404404(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404404"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagDisabled(6813))
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_2.Add(FlagDisabled(6813))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404405)
def Event_13404405(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404405"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(PlayerHasGood(4014))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_4.Add(FlagEnabled(1800))
    OR_4.Add(FlagEnabled(1801))
    AND_1.Add(OR_4)
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(PlayerHasGood(4014))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_5.Add(FlagEnabled(1800))
    OR_5.Add(FlagEnabled(1801))
    AND_2.Add(OR_5)
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(13404406)
def Event_13404406(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13404406"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(PlayerHasGood(4014))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagEnabled(6813))
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(PlayerHasGood(4014))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_2.Add(FlagEnabled(6813))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
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
    if FlagDisabled(summon_flag):
        DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    AND_1.Add(Client())
    AND_1.Add(FlagEnabled(summon_flag))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(character)
    if FlagEnabled(flag_1):
        return
    AND_3.Add(Client())
    SkipLinesIfConditionTrue(1, AND_3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(summon_flag))
    AND_2.Add(FlagDisabled(dismissal_flag))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=character))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    RemoveSpecialEffect(PLAYER, 9005)
    RemoveSpecialEffect(PLAYER, 9025)
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
    if Client():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    AND_2.Add(CharacterInsideRegion(character, region=region_2))
    if not AND_2:
        return RESTART
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region_3))
    
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13404490)
def Event_13404490(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13404490"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect_WithUnknownEffect(character, 35)
    WaitFrames(frames=1)
    Restart()
