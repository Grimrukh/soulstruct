"""
linked:
300

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_死と闇レッサー
88: ボス_戦闘開始
104: ボス戦_撃破時間
122: トラップロード_闇魔法_解除状態
156: トラップロード_闇魔法_発動状態
190: PC情報_ボス撃破_トラップロード中ボス
232: トラップロード_中ボス戦_撃破時間
268: PC情報_トラップロード到達時
300: N:\\SPRJ\\data\\Param\\event\\common.emevd
376: 
378: 
380: 
382: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=30, args=(2600950, 2601950, 999, 12607800))
    RunEvent(7000, slot=31, args=(2600951, 2601951, 12601800, 12607820))
    RunEvent(7000, slot=32, args=(2600952, 2601952, 999, 12607840))
    RunEvent(7000, slot=33, args=(2600953, 2601953, 999, 12607860))
    RunEvent(7100, slot=30, args=(72600200, 2601950))
    RunEvent(7100, slot=31, args=(72600201, 2601951))
    RunEvent(7100, slot=32, args=(72600202, 2601952))
    RunEvent(7100, slot=33, args=(72600203, 2601953))
    RunEvent(7200, slot=30, args=(72600100, 2601950, 2102953))
    RunEvent(7200, slot=31, args=(72600101, 2601951, 2102953))
    RunEvent(7200, slot=32, args=(72600102, 2601952, 2102953))
    RunEvent(7200, slot=33, args=(72600103, 2601953, 2102953))
    RunEvent(7300, slot=30, args=(72102600, 2601950))
    RunEvent(7300, slot=31, args=(72102601, 2601951))
    RunEvent(7300, slot=32, args=(72102602, 2601952))
    RunEvent(7300, slot=33, args=(72102603, 2601953))
    RunEvent(9200, slot=6, args=(2603900,))
    StartPlayLogMeasurement(measurement_id=2600000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2600001, name=18, overwrite=True)
    Event_12600990()
    Event_12604700(0, character=2600700, flag=12604701, flag_1=12604711, flag_2=2600, flag_3=12604741, flag_4=12601700)
    Event_12604700(5, character=2600701, flag=12604702, flag_1=12604712, flag_2=2601, flag_3=12604743, flag_4=12601701)
    Event_12604710(0, character=2600700, flag=12604701, flag_1=12604711, flag_2=12604721, flag_3=12604741)
    Event_12604710(5, character=2600701, flag=12604702, flag_1=12604712, flag_2=12604722, flag_3=12604743)
    Event_12604720(0, character=2600700, flag=12604701, flag_1=12604711, flag_2=12604721, flag_3=12604741)
    Event_12604720(5, character=2600701, flag=12604702, flag_1=12604712, flag_2=12604722, flag_3=12604743)
    Event_12604730(
        0,
        character=2600700,
        flag=12604701,
        flag_1=12604711,
        flag_2=2600,
        flag_3=12604731,
        flag_4=12601700,
        flag_5=12604741
    )
    Event_12604730(
        5,
        character=2600701,
        flag=12604702,
        flag_1=12604712,
        flag_2=2601,
        flag_3=12604732,
        flag_4=12601701,
        flag_5=12604743
    )
    Event_12604740()
    Event_12604742()
    Event_12604847()
    Event_12604848()
    Event_12601800()
    Event_12601801()
    Event_12601802()
    Event_12604845()
    Event_12604846()
    Event_12604802()
    Event_12604803()
    Event_12604804()
    Event_12604805()
    Event_12604807()
    Event_12601803()
    Event_12604820(0, character=2600800, first_flag=12605880, last_flag=12605885)
    Event_12604830(0, character=2600800, flag=12605880, region=2602830, destination=2602831)
    Event_12604830(1, character=2600800, flag=12605881, region=2602831, destination=2602832)
    Event_12604830(2, character=2600800, flag=12605882, region=2602832, destination=2602830)
    Event_12604830(3, character=2600800, flag=12605883, region=2602833, destination=2602834)
    Event_12604830(4, character=2600800, flag=12605884, region=2602834, destination=2602835)
    Event_12604830(5, character=2600800, flag=12605885, region=2602835, destination=2602833)
    Event_12604806()
    Event_12604810()
    Event_12604840()
    Event_12604815()
    Event_12604862()
    Event_12604863()
    Event_12601850()
    Event_12601851()
    Event_12601852()
    Event_12601853()
    Event_12604860()
    Event_12604861()
    Event_12604852()
    Event_12604853()
    Event_12604854()
    Event_12604855()
    Event_12604856()
    Event_12604985()
    Event_12604986()
    Event_12601854()
    Event_12601855()
    Event_12604870(
        0,
        region=2602040,
        region_1=2602042,
        region_2=2602041,
        region_3=2602042,
        region_4=2602042,
        flag=12604942,
        flag_1=12604941,
        flag_2=12604942
    )
    Event_12604870(
        1,
        region=2602041,
        region_1=2602043,
        region_2=2602040,
        region_3=2602043,
        region_4=2602043,
        flag=12604943,
        flag_1=12604940,
        flag_2=12604943
    )
    Event_12604870(
        2,
        region=2602042,
        region_1=2602040,
        region_2=2602044,
        region_3=2602040,
        region_4=2602044,
        flag=12604940,
        flag_1=12604944,
        flag_2=12604940
    )
    Event_12604870(
        3,
        region=2602043,
        region_1=2602046,
        region_2=2602045,
        region_3=2602041,
        region_4=2602046,
        flag=12604946,
        flag_1=12604945,
        flag_2=12604941
    )
    Event_12604870(
        4,
        region=2602044,
        region_1=2602042,
        region_2=2602042,
        region_3=2602045,
        region_4=2602042,
        flag=12604942,
        flag_1=12604942,
        flag_2=12604945
    )
    Event_12604870(
        5,
        region=2602045,
        region_1=2602043,
        region_2=2602043,
        region_3=2602044,
        region_4=2602043,
        flag=12604943,
        flag_1=12604943,
        flag_2=12604944
    )
    Event_12604877()
    Event_12604888()
    Event_12604878()
    Event_12604880(
        0,
        region=2602060,
        region_1=2602062,
        region_2=2602061,
        region_3=2602062,
        flag=12604952,
        flag_1=12604951,
        flag_2=12604952,
        region_4=2602070
    )
    Event_12604880(
        1,
        region=2602061,
        region_1=2602065,
        region_2=2602060,
        region_3=2602065,
        flag=12604955,
        flag_1=12604950,
        flag_2=12604955,
        region_4=2602070
    )
    Event_12604880(
        2,
        region=2602062,
        region_1=2602063,
        region_2=2602063,
        region_3=2602060,
        flag=12604953,
        flag_1=12604953,
        flag_2=12604950,
        region_4=2602070
    )
    Event_12604880(
        3,
        region=2602063,
        region_1=2602064,
        region_2=2602064,
        region_3=2602064,
        flag=12604954,
        flag_1=12604954,
        flag_2=12604954,
        region_4=2602070
    )
    Event_12604880(
        4,
        region=2602065,
        region_1=2602066,
        region_2=2602067,
        region_3=2602061,
        flag=12604956,
        flag_1=12604957,
        flag_2=12604951,
        region_4=2602079
    )
    Event_12604880(
        5,
        region=2602067,
        region_1=2602065,
        region_2=2602065,
        region_3=2602068,
        flag=12604955,
        flag_1=12604955,
        flag_2=12604958,
        region_4=2602070
    )
    Event_12604880(
        6,
        region=2602068,
        region_1=2602069,
        region_2=2602069,
        region_3=2602067,
        flag=12604959,
        flag_1=12604959,
        flag_2=12604957,
        region_4=2602070
    )
    Event_12604880(
        7,
        region=2602059,
        region_1=2602065,
        region_2=2602065,
        region_3=2602065,
        flag=12604955,
        flag_1=12604955,
        flag_2=12604955,
        region_4=2602070
    )
    Event_12604956()
    Event_12604879()
    Event_12604930()
    Event_12604889()
    Event_12604890(1, character=2600161, flag=12601850, flag_1=12604857)
    Event_12604890(2, character=2600162, flag=12601850, flag_1=12604857)
    Event_12604890(3, character=2600163, flag=12601850, flag_1=12604857)
    Event_12604890(4, character=2600164, flag=12601850, flag_1=12604857)
    Event_12604890(5, character=2600165, flag=12601850, flag_1=12604857)
    Event_12604890(7, character=2600167, flag=12601850, flag_1=12604857)
    Event_12604890(9, character=2600169, flag=12601850, flag_1=12604857)
    Event_12604890(10, character=2600170, flag=12601850, flag_1=12604857)
    Event_12604890(11, character=2600171, flag=12601850, flag_1=12604857)
    Event_12604890(12, character=2600172, flag=12601850, flag_1=12604857)
    Event_12604890(13, character=2600173, flag=12601850, flag_1=12604857)
    Event_12604890(15, character=2600175, flag=12601850, flag_1=12604857)
    Event_12604890(16, character=2600176, flag=12601850, flag_1=12604857)
    Event_12604890(17, character=2600177, flag=12601850, flag_1=12604857)
    Event_12604890(18, character=2600178, flag=12601850, flag_1=12604857)
    Event_12604890(19, character=2600179, flag=12601850, flag_1=12604857)
    Event_12604910(1, character=2600161, flag=12601850)
    Event_12604910(2, character=2600162, flag=12601850)
    Event_12604910(3, character=2600163, flag=12601850)
    Event_12604910(4, character=2600164, flag=12601850)
    Event_12604910(5, character=2600165, flag=12601850)
    Event_12604910(7, character=2600167, flag=12601850)
    Event_12604910(9, character=2600169, flag=12601850)
    Event_12604910(10, character=2600170, flag=12601850)
    Event_12604910(11, character=2600171, flag=12601850)
    Event_12604910(12, character=2600172, flag=12601850)
    Event_12604910(13, character=2600173, flag=12601850)
    Event_12604910(15, character=2600175, flag=12601850)
    Event_12604910(16, character=2600176, flag=12601850)
    Event_12604910(17, character=2600177, flag=12601850)
    Event_12604910(18, character=2600178, flag=12601850)
    Event_12604910(19, character=2600179, flag=12601850)
    Event_12604931(0, flag=12604946, flag_1=12604856)
    Event_12604931(1, flag=12604956, flag_1=12601850)
    Event_12604960(0, region=2602040)
    Event_12604960(1, region=2602041)
    Event_12604960(2, region=2602042)
    Event_12604960(3, region=2602043)
    Event_12604960(4, region=2602044)
    Event_12604960(5, region=2602045)
    Event_12604960(6, region=2602046)
    Event_12604970(0, region=2602060)
    Event_12604970(1, region=2602061)
    Event_12604970(2, region=2602062)
    Event_12604970(3, region=2602063)
    Event_12604970(4, region=2602064)
    Event_12604970(5, region=2602065)
    Event_12604970(6, region=2602066)
    Event_12604970(7, region=2602067)
    Event_12604970(8, region=2602068)
    Event_12604970(9, region=2602059)
    Event_12604980(
        0,
        tae_event_id=20,
        first_flag=72600307,
        last_flag=72600311,
        first_flag_1=72600307,
        last_flag_1=72600311,
        flag=72600311,
        flag_1=72600306
    )
    Event_12604980(
        1,
        tae_event_id=10,
        first_flag=72600312,
        last_flag=72600316,
        first_flag_1=72600312,
        last_flag_1=72600316,
        flag=72600316,
        flag_1=72600306
    )
    Event_12600020(0, character=2600100, character_1=2600101)
    Event_12600021()
    Event_12600025()
    Event_12600026()
    Event_12600027()
    Event_12600028()
    Event_12600029()
    Event_12600500(0, character=2600720)
    Event_12600030()
    Event_12600031()
    DisableSoundEvent(sound_id=2603100)
    Event_12600010(0, region=2602301, sound_id=260000001, left=0)
    Event_12600010(1, region=2602302, sound_id=260000001, left=0)
    Event_12600010(2, region=2602303, sound_id=260000001, left=0)
    Event_12600010(3, region=2602304, sound_id=260000001, left=0)
    Event_12600010(4, region=2602305, sound_id=260000001, left=0)
    Event_12600010(5, region=2602310, sound_id=2603100, left=1)
    Event_12600130(0, character=10000)
    Event_12600130(1, character=10000)
    Event_12600130(2, character=10000)
    Event_12600130(3, character=2600104)
    Event_12600130(4, character=2600113)
    Event_12600130(5, character=2600150)
    Event_12600130(6, character=2600153)
    Event_12600130(7, character=2600155)
    Event_12600130(8, character=2600201)
    Event_12600130(9, character=2600180)
    Event_12600130(10, character=2600181)
    Event_12600130(11, character=2600182)
    Event_12600130(12, character=2600183)
    Event_12600130(13, character=2600103)
    Event_12600150(0, character=10000)
    Event_12600150(1, character=2600104)
    Event_12600150(2, character=2600113)
    Event_12600150(3, character=2600150)
    Event_12600150(4, character=2600153)
    Event_12600150(5, character=2600155)
    Event_12600150(6, character=2600201)
    Event_12600150(7, character=2600180)
    Event_12600150(8, character=2600181)
    Event_12600150(9, character=2600182)
    Event_12600150(10, character=2600183)
    Event_12600150(11, character=2600103)
    Event_12601294()
    Event_12601295(0, entity=2601211, flag=12601294, flag_1=12605250, flag_2=12601250, state=0)
    Event_12601295(1, entity=2601212, flag=12601294, flag_1=12605250, flag_2=12601250, state=1)
    Event_12601295(2, entity=2601221, flag=12601331, flag_1=12605251, flag_2=12601251, state=0)
    Event_12601295(3, entity=2601222, flag=12601331, flag_1=12605251, flag_2=12601251, state=1)
    Event_12601295(4, entity=2601231, flag=12601294, flag_1=12605252, flag_2=12601252, state=0)
    Event_12601295(5, entity=2601232, flag=12601294, flag_1=12605252, flag_2=12601252, state=1)
    Event_12601295(6, entity=2601241, flag=12601323, flag_1=12605256, flag_2=12601256, state=1)
    Event_12601295(7, entity=2601242, flag=12601323, flag_1=12605256, flag_2=12601256, state=0)
    Event_12601295(8, entity=2601281, flag=12601334, flag_1=12605253, flag_2=12601254, state=0)
    Event_12601295(9, entity=2601282, flag=12601334, flag_1=12605253, flag_2=12601254, state=1)
    Event_12601295(10, entity=2601291, flag=12601335, flag_1=12605254, flag_2=12601255, state=0)
    Event_12601295(11, entity=2601292, flag=12601335, flag_1=12605254, flag_2=12601255, state=1)
    Event_12601340(0, flag=12601331, flag_1=12601251, obj=2601221)
    Event_12601340(1, flag=12601334, flag_1=12601254, obj=2601281)
    Event_12601340(2, flag=12601335, flag_1=12601255, obj=2601291)
    Event_12601310(0, flag=12601250, obj=2601210, obj_1=2601211, obj_2=2601212, flag_1=12601294)
    Event_12601310(1, flag=12601251, obj=2601220, obj_1=2601221, obj_2=2601222, flag_1=12601331)
    Event_12601310(2, flag=12601252, obj=2601230, obj_1=2601231, obj_2=2601232, flag_1=12601294)
    Event_12601315(0, flag=12601256, obj=2601240, obj_1=2601241, obj_2=2601242, flag_1=12601323)
    Event_12601310(3, flag=12601254, obj=2601280, obj_1=2601281, obj_2=2601282, flag_1=12601334)
    Event_12601310(4, flag=12601255, obj=2601290, obj_1=2601291, obj_2=2601292, flag_1=12601335)
    Event_12601320(
        0,
        flag=12605250,
        flag_1=12601250,
        region=2602211,
        region_1=2602212,
        obj=2601211,
        obj_1=2601212,
        entity=2601210,
        obj_act_id=12601211
    )
    Event_12601330(
        0,
        flag=12605250,
        flag_1=12601250,
        region=2602211,
        region_1=2602212,
        obj=2601211,
        obj_1=2601212,
        entity=2601210,
        obj_act_id=12601211
    )
    Event_12601320(
        1,
        flag=12605251,
        flag_1=12601251,
        region=2602221,
        region_1=2602222,
        obj=2601221,
        obj_1=2601222,
        entity=2601220,
        obj_act_id=12601221
    )
    Event_12601330(
        1,
        flag=12605251,
        flag_1=12601251,
        region=2602221,
        region_1=2602222,
        obj=2601221,
        obj_1=2601222,
        entity=2601220,
        obj_act_id=12601221
    )
    Event_12601320(
        2,
        flag=12605252,
        flag_1=12601252,
        region=2602231,
        region_1=2602232,
        obj=2601231,
        obj_1=2601232,
        entity=2601230,
        obj_act_id=12601231
    )
    Event_12601330(
        2,
        flag=12605252,
        flag_1=12601252,
        region=2602231,
        region_1=2602232,
        obj=2601231,
        obj_1=2601232,
        entity=2601230,
        obj_act_id=12601231
    )
    Event_12601320(
        3,
        flag=12605256,
        flag_1=12601256,
        region=2602252,
        region_1=2602251,
        obj=2601242,
        obj_1=2601241,
        entity=2601240,
        obj_act_id=12601241
    )
    Event_12601330(
        3,
        flag=12605256,
        flag_1=12601256,
        region=2602252,
        region_1=2602251,
        obj=2601242,
        obj_1=2601241,
        entity=2601240,
        obj_act_id=12601241
    )
    Event_12601320(
        4,
        flag=12605253,
        flag_1=12601254,
        region=2602281,
        region_1=2602282,
        obj=2601281,
        obj_1=2601282,
        entity=2601280,
        obj_act_id=12601281
    )
    Event_12601330(
        4,
        flag=12605253,
        flag_1=12601254,
        region=2602281,
        region_1=2602282,
        obj=2601281,
        obj_1=2601282,
        entity=2601280,
        obj_act_id=12601281
    )
    Event_12601320(
        5,
        flag=12605254,
        flag_1=12601255,
        region=2602291,
        region_1=2602292,
        obj=2601291,
        obj_1=2601292,
        entity=2601290,
        obj_act_id=12601291
    )
    Event_12601330(
        5,
        flag=12605254,
        flag_1=12601255,
        region=2602291,
        region_1=2602292,
        obj=2601291,
        obj_1=2601292,
        entity=2601290,
        obj_act_id=12601291
    )
    Event_12601351(0, flag=12601850, obj=2601260, obj_1=2601261)
    Event_12601352()
    Event_12605200(0, character__set_draw_parent=2600300, character=2600310)
    Event_12605200(1, character__set_draw_parent=2600301, character=2600311)
    Event_12605200(2, character__set_draw_parent=2600302, character=2600312)
    Event_12605200(3, character__set_draw_parent=2600303, character=2600313)
    Event_12600080(0, attacked_entity=2600183, animation_id=7011, animation_id_1=7013, animation_id_2=7014)
    Event_12600040(0, region=2602001, character=2600105, region_1=2602004, character_1=10000, region_2=2602015)
    Event_12600041(0, character=2600105)
    Event_12600041(1, character=2600111)
    Event_12600041(2, character=2600106)
    Event_12600041(3, character=2600195)
    Event_12600041(4, character=2600196)
    Event_12600041(5, character=2600197)
    Event_12600047(1, character=2600109)
    Event_12600047(2, character=2600110)
    Event_12600047(3, character=2600198)
    Event_12600180(0, character=2600106, item_lot_param_id=22502610)
    Event_12600400(0, character=2600400, flag=52600990)
    Event_12600400(1, character=2600401, flag=52600980)
    Event_12600400(2, character=2600402, flag=52600970)
    Event_12600400(3, character=2600403, flag=52600960)
    Event_12600400(4, character=2600404, flag=52600950)
    Event_12600410()
    Event_12600050(0, character=2600134, region=2602020)
    Event_12600050(1, character=2600135, region=2602020)
    Event_12600050(2, character=2600136, region=2602020)
    Event_12600050(3, character=2600137, region=2602020)
    Event_12600050(4, character=2600138, region=2602031)
    Event_12600050(5, character=2600139, region=2602031)
    Event_12600050(6, character=2600140, region=2602020)
    Event_12600050(7, character=2600141, region=2602031)
    Event_12600050(8, character=2600102, region=2602020)
    Event_12600035(0, character__targeting_character=2600104)
    Event_12600035(1, character__targeting_character=2600201)
    Event_12600035(2, character__targeting_character=2600190)
    Event_12600035(3, character__targeting_character=2600220)
    Event_12600035(4, character__targeting_character=2600221)
    Event_12600190(0, character=2600191, left=2600192)
    Event_12600190(1, character=2600192, left=2600191)
    Event_12600110(0, character=2600104, character_1=2600210, character_2=2600211)
    Event_12600110(1, character=2600113, character_1=2600212, character_2=2600213)
    Event_12600110(2, character=2600201, character_1=2600214, character_2=2600215)
    Event_12600110(3, character=2600103, character_1=2600216, character_2=2600217)
    Event_12600070(0, 2600114, 2602012, 16.0)
    Event_12600070(3, 2600117, 2602013, 15.0)
    Event_12600070(4, 2600118, 2602014, 15.0)
    Event_12600070(5, 2600119, 2602014, 15.0)
    Event_12600105(
        0,
        attacked_entity=2600123,
        animation_id=7010,
        animation_id_1=7011,
        character=2600120,
        character_1=2600121,
        character_2=2600122
    )
    Event_12600105(
        1,
        attacked_entity=2600145,
        animation_id=7010,
        animation_id_1=7011,
        character=2600125,
        character_1=2600126,
        character_2=0
    )
    Event_12600060(0, character=2600120, animation_id=9001, animation_id_1=9060)
    Event_12600060(1, character=2600121, animation_id=9000, animation_id_1=9060)
    Event_12600060(2, character=2600122, animation_id=9000, animation_id_1=9060)
    Event_12600060(3, character=2600125, animation_id=9000, animation_id_1=9060)
    Event_12600060(4, character=2600126, animation_id=9001, animation_id_1=9060)
    Event_12600060(5, character=2600129, animation_id=9000, animation_id_1=9060)
    Event_12600090(0, character=2600107, region=2602008)
    Event_12600090(1, character=2600108, region=2602009)
    Event_12600090(2, character=2600116, region=2602009)
    Event_12600090(3, character=2600202, region=2602005)
    Event_12600120(0, obj_act_id=12601000, obj=2601005)
    Event_12600120(1, obj_act_id=12601001, obj=2601006)
    Event_12600120(2, obj_act_id=12601002, obj=2601007)
    Event_12600120(3, obj_act_id=12601003, obj=2601009)
    Event_12600125(0, obj=2601008, item_lot_param_id=2600570)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6314)
    EnableFlag(12601999)
    SkipLinesIfFlagEnabled(5, 12601999)
    EnableObject(2601500)
    DisableObject(2601501)
    EnableTreasure(obj=2601500)
    DisableTreasure(obj=2601501)
    SkipLines(4)
    DisableObject(2601500)
    EnableObject(2601501)
    DisableTreasure(obj=2601500)
    EnableTreasure(obj=2601501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6315)
    EnableFlag(12601998)
    SkipLinesIfFlagEnabled(5, 12601998)
    EnableObject(2601502)
    DisableObject(2601503)
    EnableTreasure(obj=2601502)
    DisableTreasure(obj=2601503)
    SkipLines(4)
    DisableObject(2601502)
    EnableObject(2601503)
    DisableTreasure(obj=2601502)
    EnableTreasure(obj=2601503)
    Event_12601050()
    Event_12601051()
    Event_12600701()
    Event_12600703()


@RestartOnRest(12604700)
def Event_12604700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12604700"""
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
    IfFlagEnabled(1, flag_3)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    SkipLinesIfFlagDisabled(1, flag_4)
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
    SkipLinesIfFlagDisabled(1, flag_4)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    WaitFrames(frames=59)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(12604710)
def Event_12604710(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12604710"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_3)
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


@RestartOnRest(12604720)
def Event_12604720(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12604720"""
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
    IfFlagDisabled(-1, flag_3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(character, 9100)
    ReplanAI(character)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(12604730)
def Event_12604730(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int):
    """Event 12604730"""
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    IfFlagEnabled(-15, flag_3)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_5)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(3, flag_3)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
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


@RestartOnRest(12604740)
def Event_12604740():
    """Event 12604740"""
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604000)
    IfPlayerStandingOnCollision(-1, 2604001)
    IfPlayerStandingOnCollision(-1, 2604002)
    IfPlayerStandingOnCollision(-1, 2604003)
    IfPlayerStandingOnCollision(-1, 2604004)
    IfPlayerStandingOnCollision(-1, 2604005)
    IfPlayerStandingOnCollision(-1, 2604006)
    IfPlayerStandingOnCollision(-1, 2604007)
    IfPlayerStandingOnCollision(-1, 2604008)
    IfPlayerStandingOnCollision(-1, 2604009)
    IfPlayerStandingOnCollision(-1, 2604010)
    IfPlayerStandingOnCollision(-1, 2604011)
    IfPlayerStandingOnCollision(-1, 2604012)
    IfPlayerStandingOnCollision(-1, 2604013)
    IfPlayerStandingOnCollision(-1, 2604014)
    IfPlayerStandingOnCollision(-1, 2604015)
    IfPlayerStandingOnCollision(-1, 2604016)
    IfPlayerStandingOnCollision(-1, 2604017)
    IfPlayerStandingOnCollision(-1, 2604018)
    IfPlayerStandingOnCollision(-1, 2604019)
    IfPlayerStandingOnCollision(-1, 2604020)
    IfPlayerStandingOnCollision(-1, 2604021)
    IfPlayerStandingOnCollision(-1, 2604022)
    IfPlayerStandingOnCollision(-1, 2604023)
    IfPlayerStandingOnCollision(-1, 2604024)
    IfPlayerStandingOnCollision(-1, 2604025)
    IfPlayerStandingOnCollision(-1, 2604026)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12604741)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604000)
    IfPlayerStandingOnCollision(-1, 2604001)
    IfPlayerStandingOnCollision(-1, 2604002)
    IfPlayerStandingOnCollision(-1, 2604003)
    IfPlayerStandingOnCollision(-1, 2604004)
    IfPlayerStandingOnCollision(-1, 2604005)
    IfPlayerStandingOnCollision(-1, 2604006)
    IfPlayerStandingOnCollision(-1, 2604007)
    IfPlayerStandingOnCollision(-1, 2604008)
    IfPlayerStandingOnCollision(-1, 2604009)
    IfPlayerStandingOnCollision(-1, 2604010)
    IfPlayerStandingOnCollision(-1, 2604011)
    IfPlayerStandingOnCollision(-1, 2604012)
    IfPlayerStandingOnCollision(-1, 2604013)
    IfPlayerStandingOnCollision(-1, 2604014)
    IfPlayerStandingOnCollision(-1, 2604015)
    IfPlayerStandingOnCollision(-1, 2604016)
    IfPlayerStandingOnCollision(-1, 2604017)
    IfPlayerStandingOnCollision(-1, 2604018)
    IfPlayerStandingOnCollision(-1, 2604019)
    IfPlayerStandingOnCollision(-1, 2604020)
    IfPlayerStandingOnCollision(-1, 2604021)
    IfPlayerStandingOnCollision(-1, 2604022)
    IfPlayerStandingOnCollision(-1, 2604023)
    IfPlayerStandingOnCollision(-1, 2604024)
    IfPlayerStandingOnCollision(-1, 2604025)
    IfPlayerStandingOnCollision(-1, 2604026)
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12604741)
    Restart()


@RestartOnRest(12604742)
def Event_12604742():
    """Event 12604742"""
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604100)
    IfPlayerStandingOnCollision(-1, 2604101)
    IfPlayerStandingOnCollision(-1, 2604102)
    IfPlayerStandingOnCollision(-1, 2604103)
    IfPlayerStandingOnCollision(-1, 2604104)
    IfPlayerStandingOnCollision(-1, 2604105)
    IfPlayerStandingOnCollision(-1, 2604106)
    IfPlayerStandingOnCollision(-1, 2604107)
    IfPlayerStandingOnCollision(-1, 2604108)
    IfPlayerStandingOnCollision(-1, 2604109)
    IfPlayerStandingOnCollision(-1, 2604110)
    IfPlayerStandingOnCollision(-1, 2604111)
    IfPlayerStandingOnCollision(-1, 2604112)
    IfPlayerStandingOnCollision(-1, 2604113)
    IfPlayerStandingOnCollision(-1, 2604114)
    IfPlayerStandingOnCollision(-1, 2604115)
    IfPlayerStandingOnCollision(-1, 2604116)
    IfPlayerStandingOnCollision(-1, 2604117)
    IfPlayerStandingOnCollision(-1, 2604118)
    IfPlayerStandingOnCollision(-1, 2604119)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12604743)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604100)
    IfPlayerStandingOnCollision(-1, 2604101)
    IfPlayerStandingOnCollision(-1, 2604102)
    IfPlayerStandingOnCollision(-1, 2604103)
    IfPlayerStandingOnCollision(-1, 2604104)
    IfPlayerStandingOnCollision(-1, 2604105)
    IfPlayerStandingOnCollision(-1, 2604106)
    IfPlayerStandingOnCollision(-1, 2604107)
    IfPlayerStandingOnCollision(-1, 2604108)
    IfPlayerStandingOnCollision(-1, 2604109)
    IfPlayerStandingOnCollision(-1, 2604110)
    IfPlayerStandingOnCollision(-1, 2604111)
    IfPlayerStandingOnCollision(-1, 2604112)
    IfPlayerStandingOnCollision(-1, 2604113)
    IfPlayerStandingOnCollision(-1, 2604114)
    IfPlayerStandingOnCollision(-1, 2604115)
    IfPlayerStandingOnCollision(-1, 2604116)
    IfPlayerStandingOnCollision(-1, 2604117)
    IfPlayerStandingOnCollision(-1, 2604118)
    IfPlayerStandingOnCollision(-1, 2604119)
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12604743)
    Restart()


@NeverRestart(12601800)
def Event_12601800():
    """Event 12601800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2603802)
    DisableSoundEvent(sound_id=2603803)
    DisableCharacter(2600800)
    DisableCharacter(2600801)
    DisableCharacter(2600802)
    DisableObject(2601800)
    DeleteVFX(2603800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthLessThanOrEqual(0, 2600802, value=0.0)
    ResetAnimation(2600800, disable_interpolation=True)
    ResetAnimation(2600801, disable_interpolation=True)
    Kill(2600800)
    Kill(2600801)
    IfCharacterDead(0, 2600800)
    EnableFlag(12604808)
    Wait(3.0)
    PlaySoundEffect(2602300, 260000004, sound_type=SoundType.a_Ambient)
    Wait(18.0)
    DisplayBanner(BannerType.NightmareSlain)
    DisableObject(2601800)
    DeleteVFX(2603800)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=0)
    CancelSpecialEffect(PLAYER, 5630)
    Wait(3.0)
    KillBoss(game_area_param_id=2600803)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=20)
    AwardItemLot(55100000, host_only=False)
    EnableFlag(2601)
    EnableFlag(9462)
    StopPlayLogMeasurement(measurement_id=2600000)
    StopPlayLogMeasurement(measurement_id=2600001)
    StopPlayLogMeasurement(measurement_id=2600010)
    CreatePlayLog(name=40)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12601801)
def Event_12601801():
    """Event 12601801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601800)
    IfFlagEnabled(1, 12601800)
    IfCharacterBackreadDisabled(2, 2600800)
    IfHealthLessThanOrEqual(2, 2600802, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2602800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12601802)
def Event_12601802():
    """Event 12601802"""
    EndIfFlagEnabled(12601800)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2600800)
    DisableCharacter(2600801)
    EnableObjectInvulnerability(2601856)
    IfFlagDisabled(1, 12601800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2602805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12604732)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    DisableSoundEvent(sound_id=2603100)
    WaitFrames(frames=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(26000010, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(26000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    DisableObjectInvulnerability(2601856)
    PostDestruction(2601856)
    EnableFlag(12604800)
    EnableCharacter(2600800)
    EndIfFlagEnabled(9306)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(9306)


@NeverRestart(12601803)
def Event_12601803():
    """Event 12601803"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12604800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableObjectInvulnerability(2601856)
    PostDestruction(2601856)
    EnableCharacter(2600800)
    EnableFlag(12604800)
    EnableFlag(12601802)


@NeverRestart(12604845)
def Event_12604845():
    """Event 12604845"""
    EndIfFlagEnabled(12601800)
    GotoIfFlagEnabled(Label.L0, flag=12601802)
    SkipLinesIfClient(2)
    DisableObject(2601800)
    DeleteVFX(2603800, erase_root_only=False)
    IfFlagDisabled(1, 12601800)
    IfFlagEnabled(1, 12601802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2601800)
    CreateVFX(2603800)

    # --- 0 --- #
    DefineLabel(0)
    PostDestruction(2601856)
    IfFlagDisabled(2, 12601800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2600800, entity=2601800)
    IfFlagEnabled(3, 12601800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2602800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2602801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12604800)
    Restart()


@NeverRestart(12604846)
def Event_12604846():
    """Event 12604846"""
    DisableNetworkSync()
    IfFlagDisabled(1, 12601800)
    IfFlagEnabled(1, 12601802)
    IfFlagEnabled(1, 12604800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2600800, entity=2601800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2602800, animation=101130, wait_for_completion=True)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2602801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12604801)
    Restart()


@NeverRestart(12604847)
def Event_12604847():
    """Event 12604847"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2601800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12604848)
def Event_12604848():
    """Event 12604848"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2601800, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2601800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12604802)
def Event_12604802():
    """Event 12604802"""
    EndIfFlagEnabled(12601800)
    DisableAI(2600800)
    DisableAI(2600801)
    DisableAI(2600802)
    DisableHealthBar(2600800)
    DisableHealthBar(2600801)
    DisableHealthBar(2600802)
    DisableGravity(2600802)
    EnableImmortality(2600800)
    EnableImmortality(2600801)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12604800)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12604732)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2600800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2600801, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2600802, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12604732)
    EnableFlag(12604800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2600800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2600801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2600802, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600802)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2600800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2600801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2600802, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600802)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2600800)
    EnableAI(2600801)
    EnableBossHealthBar(2600802, name=551000)
    ReferDamageToEntity(2600800, target_entity=2600802)
    ReferDamageToEntity(2600801, target_entity=2600802)
    CreatePlayLog(name=88)
    StartPlayLogMeasurement(measurement_id=2600010, name=104, overwrite=True)


@NeverRestart(12604803)
def Event_12604803():
    """Event 12604803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2603802)
    DisableSoundEvent(sound_id=2603803)
    IfFlagDisabled(1, 12601800)
    IfFlagEnabled(1, 12604802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12604801)
    IfCharacterInsideRegion(1, PLAYER, region=2602801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2603802)
    EnableFlag(12604815)
    IfHealthLessThan(0, 2600802, value=0.699999988079071)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12601800)
    IfFlagEnabled(2, 12604802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12604801)
    IfCharacterInsideRegion(2, PLAYER, region=2602801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2603802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2603803)


@NeverRestart(12604804)
def Event_12604804():
    """Event 12604804"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601800)
    IfFlagEnabled(1, 12604800)
    IfCharacterAlive(1, 2600803)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=1)


@NeverRestart(12604805)
def Event_12604805():
    """Event 12604805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601800)
    IfFlagEnabled(0, 12604808)
    DisableBossMusic(sound_id=2603802)
    DisableBossMusic(sound_id=2603803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12604806)
def Event_12604806():
    """Event 12604806"""
    DisableCharacter(2600801)
    DisableGravity(2600801)
    DisableCharacterCollision(2600801)


@NeverRestart(12604807)
def Event_12604807():
    """Event 12604807"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12604802)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5630)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(name=122)
    IfFlagEnabled(2, 12604802)
    IfCharacterHasSpecialEffect(2, PLAYER, 5630)
    IfConditionTrue(0, input_condition=2)
    CreatePlayLog(name=156)
    Restart()


@NeverRestart(12604810)
def Event_12604810():
    """Event 12604810"""
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    AddSpecialEffect(2600800, 5631)
    AICommand(2600800, command_id=100, command_slot=0)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 5630)
    AICommand(2600800, command_id=110, command_slot=0)
    Restart()


@NeverRestart(12604815)
def Event_12604815():
    """Event 12604815"""
    DisableNetworkSync()
    IfThisEventFlagEnabled(1)
    IfFlagEnabled(2, 12601800)
    IfHealthLessThanOrEqual(3, 2600800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EndIfFinishedConditionTrue(input_condition=3)
    PlaySoundEffect(2600800, 260000003, sound_type=SoundType.a_Ambient)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=10.0)
    Restart()


@NeverRestart(12604820)
def Event_12604820(_, character: int, first_flag: uint, last_flag: uint):
    """Event 12604820"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    Wait(1.0)
    Restart()


@NeverRestart(12604830)
def Event_12604830(_, character: int, flag: int, region: int, destination: int):
    """Event 12604830"""
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    IfCharacterInsideRegion(1, character, region=region)
    SkipLinesIfConditionTrue(3, 1)
    DisableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SkipLines(2)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Wait(2.0)
    EnableCharacter(character)
    RequestAnimation(character, animation_id=7000, wait_for_completion=True)
    Restart()


@NeverRestart(12604840)
def Event_12604840():
    """Event 12604840"""
    IfFlagEnabled(1, 12604803)
    IfCharacterHasTAEEvent(1, 2600800, tae_event_id=20)
    IfCharacterHasSpecialEffect(1, 2600800, 5631)
    IfConditionTrue(0, input_condition=1)
    MoveObjectToCharacter(2601857, character=PLAYER, model_point=245)
    WaitFrames(frames=1)
    EnableCharacter(2600801)
    ResetAnimation(2600801)
    DisableFlagRange((12604841, 12604844))
    EnableRandomFlagInRange(flag_range=(12604841, 12604844))
    GotoIfFlagEnabled(Label.L0, flag=12604841)
    GotoIfFlagEnabled(Label.L1, flag=12604842)
    GotoIfFlagEnabled(Label.L2, flag=12604843)
    GotoIfFlagEnabled(Label.L3, flag=12604844)

    # --- 0 --- #
    DefineLabel(0)
    Move(2600801, destination=2601857, destination_type=CoordEntityType.Object, model_point=4, short_move=True)
    Goto(Label.L4)

    # --- 1 --- #
    DefineLabel(1)
    Move(2600801, destination=2601857, destination_type=CoordEntityType.Object, model_point=104, short_move=True)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    Move(2600801, destination=2601857, destination_type=CoordEntityType.Object, model_point=10, short_move=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    Move(2600801, destination=2601857, destination_type=CoordEntityType.Object, model_point=110, short_move=True)

    # --- 4 --- #
    DefineLabel(4)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=655105, anchor_entity=2600801, model_point=220, anchor_type=CoordEntityType.Character)
    ReplanAI(2600801)
    AICommand(2600801, command_id=100, command_slot=0)
    AddSpecialEffect(2600801, 5631)
    IfCharacterHasTAEEvent(-1, 2600801, tae_event_id=20)
    IfAttackedWithDamageType(-1, attacked_entity=2600801, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    CreateTemporaryVFX(vfx_id=655105, anchor_entity=2600801, model_point=220, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=10)
    DisableCharacter(2600801)
    Restart()


@NeverRestart(12601850)
def Event_12601850():
    """Event 12601850"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2603852)
    DisableSoundEvent(sound_id=2603853)
    DisableCharacter(2600850)
    Kill(2600850)
    DisableObject(2601850)
    DisableObject(2601851)
    DisableObject(2601859)
    DeleteVFX(2603850, erase_root_only=False)
    DeleteVFX(2603851, erase_root_only=False)
    DeleteVFX(2603859, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthEqual(0, 2600850, value=0.0)
    EnableFlag(12604858)
    IfCharacterDead(0, 2600850)
    EnableFlag(12604857)
    IfFlagEnabled(0, 72600301)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2601850)
    DisableObject(2601851)
    DisableObject(2601859)
    DeleteVFX(2603850)
    DeleteVFX(2603851)
    DeleteVFX(2603859)
    SetBackreadStateAlternate(2600850, False)
    SetNetworkUpdateRate(2600850, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(3.0)
    KillBoss(game_area_param_id=2600850)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    AwardAchievement(achievement_id=19)
    AwardItemLot(21000, host_only=False)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(2600)
    EnableFlag(9461)
    DisableFlagRange((1080, 1099))
    EnableFlag(1082)
    CreatePlayLog(name=40)
    StopPlayLogMeasurement(measurement_id=2601000)
    StopPlayLogMeasurement(measurement_id=2601001)
    StopPlayLogMeasurement(measurement_id=2601010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=190,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=190,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=190,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=190,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12601851)
def Event_12601851():
    """Event 12601851"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(1, 12601800)
    IfCharacterBackreadDisabled(2, 2600850)
    IfHealthLessThanOrEqual(2, 2600850, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2602850, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12601852)
def Event_12601852():
    """Event 12601852"""
    EndIfFlagEnabled(12601850)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2600850)
    IfFlagDisabled(1, 12601850)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2600850, radius=32.0)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12604731)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(26000060, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(26000060, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12604850)
    EnableCharacter(2600850)
    EnableObject(2601850)
    CreateVFX(2603850)
    EnableObject(2601859)
    CreateVFX(2603859)
    EndIfFlagEnabled(9342)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(9342)


@NeverRestart(12601853)
def Event_12601853():
    """Event 12601853"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=2601852, animation_id=2)
    DisableObjectActivation(2601251, obj_act_id=2600000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2601251, obj_act_id=2600000)
    IfFlagEnabled(0, 12601850)
    EndIfFlagDisabled(12604879)
    EnableObjectActivation(2601251, obj_act_id=2600000)
    IfObjectActivated(0, obj_act_id=12601261)
    ForceAnimation(2601852, 1)


@NeverRestart(12601854)
def Event_12601854():
    """Event 12601854"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2601250, animation_id=1)
    EndOfAnimation(obj=2601852, animation_id=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfClient()
    IfFlagEnabled(1, 12601850)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2602853)
    IfCharacterInsideRegion(-1, PLAYER, region=2602854)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L1, flag=12604879)
    PlayCutscene(26000000, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=2601250, animation_id=1)
    ForceAnimation(2601852, 2)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    PlayCutscene(26000005, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=2601250, animation_id=1)

    # --- 2 --- #
    DefineLabel(2)
    DisableFlag(9180)


@NeverRestart(12601855)
def Event_12601855():
    """Event 12601855"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12604850)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12604850)
    EnableCharacter(2600850)
    EnableObject(2601850)
    CreateVFX(2603850)
    EnableObject(2601859)
    CreateVFX(2603859)
    EnableFlag(12604850)
    EnableFlag(12601852)


@NeverRestart(12604860)
def Event_12604860():
    """Event 12604860"""
    EndIfFlagEnabled(12601850)
    GotoIfFlagEnabled(Label.L0, flag=12601852)
    SkipLinesIfClient(2)
    DisableObject(2601850)
    DeleteVFX(2603850, erase_root_only=False)
    DisableObject(2601859)
    DeleteVFX(2603859, erase_root_only=False)
    IfFlagDisabled(1, 12601850)
    IfFlagEnabled(1, 12601852)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2601850)
    CreateVFX(2603850)
    EnableObject(2601859)
    CreateVFX(2603859)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12601850)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2600850, entity=2601850)
    IfFlagEnabled(3, 12601850)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2602850, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2602851)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12604850)
    Restart()


@NeverRestart(12604861)
def Event_12604861():
    """Event 12604861"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601850)
    IfFlagDisabled(1, 12601850)
    IfFlagEnabled(1, 12601852)
    IfFlagEnabled(1, 12604850)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2600850, entity=2601850)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2602850, animation=101130, wait_for_completion=True)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2602851)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12604851)
    Restart()


@NeverRestart(12604862)
def Event_12604862():
    """Event 12604862"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2601850, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12604863)
def Event_12604863():
    """Event 12604863"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2601850, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2601850, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12604852)
def Event_12604852():
    """Event 12604852"""
    EndIfFlagEnabled(12601850)
    DisableAI(2600850)
    DisableHealthBar(2600850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12604850)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12604731)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2600850, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12604731)
    EnableFlag(12604850)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2600850, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600850)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2600850, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2600850)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    SetBackreadStateAlternate(2600850, True)
    SetNetworkUpdateRate(2600850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(2600850)
    EnableBossHealthBar(2600850, name=899000)
    SetDistanceLimitForConversationStateChanges(character=2600850, distance=100.0)
    AICommand(2600850, command_id=10, command_slot=0)
    CreatePlayLog(name=88)
    StartPlayLogMeasurement(measurement_id=2601010, name=232, overwrite=True)


@NeverRestart(12604853)
def Event_12604853():
    """Event 12604853"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601850)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2603852)
    DisableSoundEvent(sound_id=2603853)
    IfFlagDisabled(1, 12601850)
    IfFlagEnabled(1, 12604852)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12604851)
    IfCharacterInsideRegion(1, PLAYER, region=2602852)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2603852)
    IfFlagEnabled(0, 72600300)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12601850)
    IfFlagEnabled(2, 12604852)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12604851)
    IfCharacterInsideRegion(2, PLAYER, region=2602852)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2603852)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2603853)


@NeverRestart(12604854)
def Event_12604854():
    """Event 12604854"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(1, 12604850)
    IfCharacterDead(1, 2600850)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=1)


@NeverRestart(12604855)
def Event_12604855():
    """Event 12604855"""
    DisableNetworkSync()
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(0, 12604858)
    DisableBossMusic(sound_id=2603852)
    DisableBossMusic(sound_id=2603853)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12604856)
def Event_12604856():
    """Event 12604856"""
    EndIfFlagEnabled(12601850)
    EnableImmortality(2600850)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfHealthLessThanOrEqual(0, 2600850, value=0.5)
    DisableBossHealthBar(2600850, name=899000)
    EnableFlag(12604985)
    IfFlagEnabled(0, 12604986)
    EnableBossHealthBar(2600850, name=899000)
    Move(2600850, destination=2602062, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    ResetAnimation(2600850, disable_interpolation=True)

    # --- 0 --- #
    DefineLabel(0)
    DisableImmortality(2600850)
    SetNest(2600850, region=2602062)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(12604952)
    ReplanAI(2600850)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableObject(2601851)
    DeleteVFX(2603851)


@NeverRestart(12604985)
def Event_12604985():
    """Event 12604985"""
    EndIfFlagEnabled(12601850)
    EndIfFlagEnabled(12604856)
    IfFlagEnabled(1, 12604986)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    EzstateAIRequest(2600850, command_id=12, command_slot=1)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12604986)
def Event_12604986():
    """Event 12604986"""
    EndIfFlagEnabled(12601850)
    EndIfThisEventFlagEnabled()
    IfCharacterHasTAEEvent(0, 2600850, tae_event_id=50)
    StopEvent(event_id=12604985)
    Wait(6.0)
    End()


@NeverRestart(12604870)
def Event_12604870(
    _,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    flag: int,
    flag_1: int,
    flag_2: int,
):
    """Event 12604870"""
    EndIfFlagEnabled(12601850)
    IfFlagDisabled(1, 12604946)
    IfCharacterInsideRegion(1, 2600850, region=region)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2600850, radius=9.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfCharacterInsideRegion(2, PLAYER, region=2602050)
    IfCharacterInsideRegion(3, PLAYER, region=2602051)
    IfCharacterInsideRegion(4, PLAYER, region=2602052)
    IfEntityWithinDistance(5, entity=PLAYER, other_entity=2600850, radius=3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(7, 2600850, region=2602043)
    GotoIfConditionTrue(Label.L7, input_condition=7)
    DisableFlagRange((12604870, 12604873))
    EnableRandomFlagInRange(flag_range=(12604870, 12604873))
    GotoIfFlagEnabled(Label.L8, flag=12604870)

    # --- 7 --- #
    DefineLabel(7)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=5)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(6, 2600850, region=2602042)
    GotoIfConditionTrue(Label.L6, input_condition=6)
    DisableFlagRange((12604870, 12604871))
    EnableRandomFlagInRange(flag_range=(12604870, 12604871))
    GotoIfFlagEnabled(Label.L4, flag=12604870)

    # --- 6 --- #
    DefineLabel(6)
    SetNest(2600850, region=region_1)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag)
    Wait(2.0)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    SetNest(2600850, region=region_4)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag_1)
    Wait(2.0)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    SetNest(2600850, region=region_2)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag_1)
    Wait(2.0)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    SetNest(2600850, region=region_3)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag_2)
    Wait(2.0)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    DisableFlagRange((12604870, 12604871))
    EnableRandomFlagInRange(flag_range=(12604870, 12604871))
    GotoIfFlagEnabled(Label.L5, flag=12604870)
    SetNest(2600850, region=region_2)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag_1)
    Wait(2.0)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    SetNest(2600850, region=region_3)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(flag_2)
    Wait(2.0)
    Restart()

    # --- 8 --- #
    DefineLabel(8)
    SetNest(2600850, region=2602043)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(12604943)
    Wait(2.0)
    Restart()


@NeverRestart(12604877)
def Event_12604877():
    """Event 12604877"""
    EndIfFlagEnabled(12601850)
    IfFlagDisabled(1, 12604856)
    IfHealthLessThan(1, 2600850, value=0.699999988079071)
    IfFlagDisabled(1, 12604946)
    IfFlagDisabled(2, 12604856)
    IfCharacterInsideRegion(2, 2600850, region=2602046)
    IfFlagEnabled(2, 12604946)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetNest(2600850, region=2602046)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(12604946)
    IfCharacterInsideRegion(0, 2600850, region=2602046)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2600850, command_id=-1, command_slot=0)


@NeverRestart(12604878)
def Event_12604878():
    """Event 12604878"""
    EndIfFlagEnabled(12601850)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, 2600850, region=2602064)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, 2600850, region=2602069)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableCharacterCollision(2600850)
    DisableGravity(2600850)
    EnableInvincibility(2600850)
    SkipLinesIfFinishedConditionTrue(1, condition=1)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    CreateTemporaryVFX(vfx_id=926201, anchor_entity=2601853, model_point=800, anchor_type=CoordEntityType.Object)
    ForceAnimation(2600850, 103122, wait_for_completion=True)
    SkipLines(2)
    CreateTemporaryVFX(vfx_id=926201, anchor_entity=2601854, model_point=800, anchor_type=CoordEntityType.Object)
    ForceAnimation(2600850, 103122, wait_for_completion=True)
    Move(2600850, destination=2602073, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    SetNest(2600850, region=2602065)
    WaitFrames(frames=5)
    CreateTemporaryVFX(vfx_id=926201, anchor_entity=2601855, model_point=800, anchor_type=CoordEntityType.Object)
    ForceAnimation(2600850, 103120)
    EnableCharacterCollision(2600850)
    EnableGravity(2600850)
    DisableInvincibility(2600850)
    Restart()


@NeverRestart(12604956)
def Event_12604956():
    """Event 12604956"""
    IfThisEventFlagEnabled(0)
    End()


@NeverRestart(12604879)
def Event_12604879():
    """Event 12604879"""
    GotoIfFlagEnabled(Label.L0, flag=12601850)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, 2600850, region=2602066)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12604879)
    ForceAnimation(2601852, 3)
    Wait(1.0)
    AICommand(2600850, command_id=-1, command_slot=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=0)
    Wait(0.0)


@NeverRestart(12604880)
def Event_12604880(
    _,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    region_4: int,
):
    """Event 12604880"""
    EndIfFlagEnabled(12601850)
    IfFlagDisabled(1, 12604956)
    IfCharacterInsideRegion(1, 2600850, region=region)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2600850, radius=9.0)
    IfFlagDisabled(6, 12604956)
    IfCharacterInsideRegion(6, 2600850, region=region)
    IfCharacterInsideRegion(6, 2600850, region=2602063)
    IfAttackedWithDamageType(6, attacked_entity=2600850)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(5, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=region_4)
    IfCharacterInsideRegion(3, PLAYER, region=2602071)
    IfCharacterInsideRegion(4, PLAYER, region=2602072)
    IfEntityWithinDistance(5, entity=PLAYER, other_entity=2600850, radius=3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(-3, 2600850, region=2602059)
    IfCharacterInsideRegion(-3, 2600850, region=2602063)
    IfCharacterInsideRegion(-3, 2600850, region=2602068)
    IfCharacterInsideRegion(-3, 2600850, region=2602065)
    GotoIfConditionTrue(Label.L9, input_condition=-3)
    DisableFlagRange((12604865, 12604868))
    EnableRandomFlagInRange(flag_range=(12604865, 12604868))
    GotoIfFlagEnabled(Label.L5, flag=12604865)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=5)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2600850, region=region_1)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(flag)
    Wait(2.0)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    SetNest(2600850, region=region_2)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(flag_1)
    Wait(2.0)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    SetNest(2600850, region=region_3)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(flag_2)
    Wait(2.0)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    DisableFlagRange((12604880, 12604881))
    EnableRandomFlagInRange(flag_range=(12604880, 12604881))
    GotoIfFlagEnabled(Label.L4, flag=12604880)
    SetNest(2600850, region=region_2)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(flag_1)
    Wait(2.0)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    SetNest(2600850, region=region_3)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(flag_2)
    Wait(2.0)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    SetNest(2600850, region=2602059)
    AICommand(2600850, command_id=10, command_slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(12604949)
    Wait(2.0)
    Restart()


@NeverRestart(12604888)
def Event_12604888():
    """Event 12604888"""
    EndIfFlagEnabled(12601850)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=2600850)
    IfFlagDisabled(1, 12604946)
    IfFlagDisabled(1, 12604856)
    IfHealthGreaterThan(1, 2600850, value=0.5)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=15)
    RestartIfFlagEnabled(12604946)
    ForceAnimation(2600850, 103120)
    CreateTemporaryVFX(vfx_id=926210, anchor_entity=2600850, model_point=200, anchor_type=CoordEntityType.Character)
    GotoIfFlagEnabled(Label.L0, flag=12604940)
    GotoIfFlagEnabled(Label.L1, flag=12604941)
    GotoIfFlagEnabled(Label.L2, flag=12604942)
    GotoIfFlagEnabled(Label.L3, flag=12604943)
    GotoIfFlagEnabled(Label.L4, flag=12604944)
    GotoIfFlagEnabled(Label.L5, flag=12604945)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Move(2600850, destination=2602040, destination_type=CoordEntityType.Region, set_draw_parent=2604800)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    Move(2600850, destination=2602041, destination_type=CoordEntityType.Region, set_draw_parent=2604800)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    Move(2600850, destination=2602042, destination_type=CoordEntityType.Region, set_draw_parent=2604801)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    Move(2600850, destination=2602043, destination_type=CoordEntityType.Region, set_draw_parent=2604801)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    Move(2600850, destination=2602044, destination_type=CoordEntityType.Region, set_draw_parent=2604802)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    Move(2600850, destination=2602045, destination_type=CoordEntityType.Region, set_draw_parent=2604802)
    Restart()


@NeverRestart(12604889)
def Event_12604889():
    """Event 12604889"""
    EndIfFlagEnabled(12601850)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=2600850)
    IfFlagDisabled(1, 12604956)
    IfFlagEnabled(1, 12604856)
    IfHealthGreaterThan(1, 2600850, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(2, 2600850, region=2602063)
    RestartIfConditionTrue(2)
    WaitFrames(frames=15)
    ForceAnimation(2600850, 103120)
    CreateTemporaryVFX(vfx_id=926210, anchor_entity=2600850, model_point=200, anchor_type=CoordEntityType.Character)
    SkipLinesIfFlagEnabled(10, 12604949)
    SkipLinesIfFlagEnabled(11, 12604950)
    SkipLinesIfFlagEnabled(12, 12604951)
    SkipLinesIfFlagEnabled(13, 12604952)
    SkipLinesIfFlagEnabled(14, 12604953)
    SkipLinesIfFlagEnabled(15, 12604954)
    SkipLinesIfFlagEnabled(16, 12604955)
    SkipLinesIfFlagEnabled(17, 12604956)
    SkipLinesIfFlagEnabled(18, 12604957)
    SkipLinesIfFlagEnabled(19, 12604958)
    SkipLinesIfFlagEnabled(20, 12604959)
    Move(2600850, destination=2602059, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(2600850, destination=2602060, destination_type=CoordEntityType.Region, set_draw_parent=2604812)
    Restart()
    Move(2600850, destination=2602061, destination_type=CoordEntityType.Region, set_draw_parent=2604812)
    Restart()
    Move(2600850, destination=2602062, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(2600850, destination=2602063, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(2600850, destination=2602077, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(2600850, destination=2602065, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(2600850, destination=2602066, destination_type=CoordEntityType.Region, set_draw_parent=2604813)
    Restart()
    Move(2600850, destination=2602067, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(2600850, destination=2602068, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(2600850, destination=2602078, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()


@NeverRestart(12604890)
def Event_12604890(_, character: int, flag: int, flag_1: int):
    """Event 12604890"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableImmortality(character)
    IfFlagEnabled(0, flag_1)
    AddSpecialEffect(character, 5914)
    ForceAnimation(character, 7002)


@NeverRestart(12604910)
def Event_12604910(_, character: int, flag: int):
    """Event 12604910"""
    EndIfFlagEnabled(flag)
    EndIfThisEventSlotFlagEnabled()
    DisableGravity(character)
    ForceAnimation(character, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=7.0)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=2)
    CancelSpecialEffect(character, 5914)
    EnableGravity(character)
    ForceAnimation(character, 7001)


@NeverRestart(12604930)
def Event_12604930():
    """Event 12604930"""
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(0, 12604879)
    DisableAI(2600850)
    IfCharacterInsideRegion(-1, PLAYER, region=2602007)
    IfAttackedWithDamageType(-1, attacked_entity=2600850, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2600850)


@NeverRestart(12604931)
def Event_12604931(_, flag: int, flag_1: int):
    """Event 12604931"""
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(1, flag)
    IfAttackedWithDamageType(1, attacked_entity=2600850)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    IfFlagEnabled(2, flag)
    IfAttackedWithDamageType(2, attacked_entity=2600850)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(frames=1)
    IfFlagEnabled(3, flag)
    IfAttackedWithDamageType(3, attacked_entity=2600850)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(frames=1)
    EndIfFlagEnabled(flag_1)
    AICommand(2600850, command_id=-1, command_slot=0)
    ReplanAI(2600850)


@NeverRestart(12604960)
def Event_12604960(_, region: int):
    """Event 12604960"""
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(3, 12604852)
    IfFlagDisabled(3, 72600300)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(72600302)
    IfCharacterInsideRegion(1, 2600850, region=region)
    IfFlagDisabled(1, 72600302)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, seconds=20.0)
    IfCharacterInsideRegion(2, 2600850, region=region)
    IfEntityBeyondDistance(2, entity=2600850, other_entity=PLAYER, radius=15.0)
    RestartIfConditionFalse(2)
    EnableFlag(72600302)
    EnableRandomFlagInRange(flag_range=(72600303, 72600305))
    IfFlagDisabled(0, 72600302)
    DisableFlagRange((72600303, 72600305))
    Restart()


@NeverRestart(12604970)
def Event_12604970(_, region: int):
    """Event 12604970"""
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(3, 12604852)
    IfFlagEnabled(3, 72600300)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(72600302)
    IfCharacterInsideRegion(1, 2600850, region=region)
    IfFlagDisabled(1, 72600302)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, seconds=20.0)
    IfCharacterInsideRegion(2, 2600850, region=region)
    IfEntityBeyondDistance(2, entity=2600850, other_entity=PLAYER, radius=15.0)
    RestartIfConditionFalse(2)
    EnableFlag(72600302)
    GotoIfFlagDisabled(Label.L0, flag=12604879)
    EnableFlag(72600317)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EnableRandomFlagInRange(flag_range=(72600303, 72600305))

    # --- 1 --- #
    DefineLabel(1)
    IfFlagDisabled(0, 72600302)
    DisableFlagRange((72600303, 72600305))
    DisableFlag(72600317)
    Restart()


@NeverRestart(12604980)
def Event_12604980(
    _,
    tae_event_id: int,
    first_flag: int,
    last_flag: int,
    first_flag_1: uint,
    last_flag_1: uint,
    flag: int,
    flag_1: int,
):
    """Event 12604980"""
    EndIfFlagEnabled(12601850)
    IfFlagEnabled(0, 12604852)
    DisableFlagRange((first_flag, last_flag))
    IfCharacterHasTAEEvent(1, 2600850, tae_event_id=tae_event_id)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableRandomFlagInRange(flag_range=(first_flag_1, last_flag_1))
    RestartIfFlagDisabled(flag)
    EnableFlag(flag_1)
    IfFlagDisabled(0, flag_1)
    Restart()


@RestartOnRest(12604000)
def Event_12604000(_, character: int, value: uchar, radius: float):
    """Event 12604000"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    IfPlayerInsightAmountGreaterThanOrEqual(1, value=value)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)


@RestartOnRest(12604005)
def Event_12604005(_, character: int, value: uchar, flag: int):
    """Event 12604005"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, flag)
    IfPlayerInsightAmountLessThanOrEqual(1, value=value)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(character)


@RestartOnRest(12600500)
def Event_12600500(_, character: int):
    """Event 12600500"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DropMandatoryTreasure(character)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    End()


@RestartOnRest(12600020)
def Event_12600020(_, character: int, character_1: int):
    """Event 12600020"""
    DisableGravity(character)
    DisableGravity(character_1)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    SetBackreadStateAlternate(character, True)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    DisableAnimations(character)
    DeleteVFX(2603000, erase_root_only=False)


@RestartOnRest(12600021)
def Event_12600021():
    """Event 12600021"""
    IfCharacterInsideRegion(0, PLAYER, region=2602017)
    Move(2600100, destination=2602019, destination_type=CoordEntityType.Region, short_move=True)
    IfAllPlayersOutsideRegion(0, region=2602017)
    Move(2600100, destination=2602018, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@NeverRestart(12600130)
def Event_12600130(_, character: int):
    """Event 12600130"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(10, character, 4691)
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfCharacterHasSpecialEffect(0, character, 4690)
    Wait(2.0)
    IfCharacterHasSpecialEffect(1, character, 4690)
    IfCharacterDoesNotHaveSpecialEffect(2, character, 4690)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(character, 4691)
    Restart()


@NeverRestart(12600150)
def Event_12600150(_, character: int):
    """Event 12600150"""
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, character, 4690)
    IfCharacterHasSpecialEffect(1, character, 4691)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(character, 4691)
    Restart()


@NeverRestart(12600025)
def Event_12600025():
    """Event 12600025"""
    IfCharacterHuman(1, PLAYER)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(2603000)
    IfCharacterHuman(2, PLAYER)
    IfHasAIStatus(2, 2600100, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=2)
    DeleteVFX(2603000)
    Restart()


@RestartOnRest(12600026)
def Event_12600026():
    """Event 12600026"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=2601271)
    DeleteVFX(2603050, erase_root_only=False)
    DeleteVFX(2603051, erase_root_only=False)
    DeleteVFX(2603052, erase_root_only=False)
    DeleteVFX(2603053, erase_root_only=False)
    DeleteVFX(2603054, erase_root_only=False)
    DeleteVFX(2603055, erase_root_only=False)
    DeleteVFX(2603056, erase_root_only=False)
    DeleteVFX(2603057, erase_root_only=False)
    DeleteVFX(2603058, erase_root_only=False)
    DeleteVFX(2603059, erase_root_only=False)
    DeleteVFX(2603060, erase_root_only=False)
    DeleteVFX(2603061, erase_root_only=False)
    DeleteVFX(2603062, erase_root_only=False)
    DeleteVFX(2603063, erase_root_only=False)
    DeleteVFX(2603064, erase_root_only=False)
    DeleteVFX(2603065, erase_root_only=False)
    DeleteVFX(2603066, erase_root_only=False)
    DeleteVFX(2603067, erase_root_only=False)
    DeleteVFX(2603068, erase_root_only=False)
    EnableFlag(9180)
    WaitFrames(frames=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(26000040, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(26000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    CreateVFX(2603050)
    CreateVFX(2603051)
    CreateVFX(2603052)
    CreateVFX(2603053)
    CreateVFX(2603054)
    CreateVFX(2603055)
    CreateVFX(2603056)
    CreateVFX(2603057)
    CreateVFX(2603058)
    CreateVFX(2603059)
    CreateVFX(2603060)
    CreateVFX(2603061)
    CreateVFX(2603062)
    CreateVFX(2603063)
    CreateVFX(2603064)
    CreateVFX(2603065)
    CreateVFX(2603066)
    CreateVFX(2603067)
    CreateVFX(2603068)

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2601271, obj_act_id=2600000)
    DisableAI(2600100)
    DisableAI(2600101)
    DisableCharacter(2600100)
    DisableCharacter(2600101)
    DeleteVFX(2603000)


@RestartOnRest(12600027)
def Event_12600027():
    """Event 12600027"""
    DisableCharacter(2600129)
    GotoIfThisEventFlagDisabled(Label.L0)
    EnableCharacter(2600129)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12600026)
    EnableCharacter(2600129)


@NeverRestart(12600028)
def Event_12600028():
    """Event 12600028"""
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfFlagEnabled(1, 12600027)
    IfCharacterInsideRegion(1, PLAYER, region=2602022)
    IfCharacterHasSpecialEffect(1, PLAYER, 164)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, flag=6336)
    AwardItemLot(2605000, host_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AwardItemLot(2605005, host_only=False)
    End()


@RestartOnRest(12600029)
def Event_12600029():
    """Event 12600029"""
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfFlagEnabled(1, 12600027)
    IfHealthEqual(1, 2600129, value=0.0)
    IfAttackedWithDamageType(1, attacked_entity=2600129, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(2605010, host_only=False)
    EnableFlag(5913)
    WaitFrames(frames=0)


@NeverRestart(12600010)
def Event_12600010(_, region: int, sound_id: int, left: int):
    """Event 12600010"""
    EndIfFlagEnabled(12601802)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=left, right=1)
    PlaySoundEffect(2602300, sound_id, sound_type=SoundType.a_Ambient)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableSoundEvent(sound_id=sound_id)
    End()


@NeverRestart(12600030)
def Event_12600030():
    """Event 12600030"""
    SetTeamType(2600500, TeamType.FriendlyNPC)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2600500)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=12601800)
    ForceAnimation(2600500, 7005)
    IfFlagEnabled(0, 12601800)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(2600500, 0)
    IfEntityWithinDistance(1, entity=2600500, other_entity=PLAYER, radius=10.0)
    IfHealthGreaterThan(1, 2600500, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(2600500)
    ForceAnimation(2600500, 7006)
    Wait(2.0)
    DisableCharacter(2600500)


@NeverRestart(12600031)
def Event_12600031():
    """Event 12600031"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2600500)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect(2600500, 5915)
    IfAttackedWithDamageType(0, attacked_entity=2600500)
    Kill(2600500)


@NeverRestart(12600035)
def Event_12600035(_, character__targeting_character: int):
    """Event 12600035"""
    ForceAnimation(character__targeting_character, 7000)
    IfCharacterTargeting(-1, targeting_character=character__targeting_character, targeted_character=PLAYER)
    IfHasAIStatus(-1, character__targeting_character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__targeting_character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character__targeting_character, ai_status=AIStatusType.Battle)
    IfAttacked(1, attacked_entity=character__targeting_character, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=1)
    ForceAnimation(character__targeting_character, 7001)


@NeverRestart(12600040)
def Event_12600040(_, region: int, character: int, region_1: int, character_1: int, region_2: int):
    """Event 12600040"""
    DisableAI(character)
    IfCharacterInsideRegion(-2, character_1, region=region)
    IfCharacterInsideRegion(-2, character_1, region=region_2)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(character)
    SetNest(character, region=region_1)
    AICommand(character, command_id=20, command_slot=0)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfHealthLessThan(-1, character, value=1.0)
    IfCharacterInsideRegion(-1, character, region=region_1)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@NeverRestart(12600041)
def Event_12600041(_, character: int):
    """Event 12600041"""
    AddSpecialEffect(character, 5641)
    IfAttackedWithDamageType(0, attacked_entity=character, attacker=PLAYER)
    CancelSpecialEffect(character, 5641)
    ReplanAI(character)


@NeverRestart(12600047)
def Event_12600047(_, character: int):
    """Event 12600047"""
    AICommand(character, command_id=40, command_slot=0)
    IfHasAIStatus(0, 2600202, ai_status=AIStatusType.Battle)
    ReplanAI(character)
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=2602005)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    ReplanAI(character)
    AICommand(character, command_id=-1, command_slot=0)


@NeverRestart(12600180)
def Event_12600180(_, character: int, item_lot_param_id: int):
    """Event 12600180"""
    DisableNetworkSync()
    EndIfClient()
    AddSpecialEffect(character, 5001)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    Wait(60.0)
    MoveObjectToCharacter(2601040, character=character)
    CreateObjectVFX(2601040, vfx_id=200, model_point=900201)
    IfActionButtonParamActivated(1, action_button_id=2600030, entity=2601040)
    IfTimeElapsed(2, seconds=15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DeleteObjectVFX(2601040)
    RestartIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(item_lot_param_id, host_only=False)
    Restart()


@NeverRestart(12600050)
def Event_12600050(_, character: int, region: int):
    """Event 12600050"""
    DisableAI(character)
    ForceAnimation(character, 7000)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=10, max_frames=60)
    ForceAnimation(character, 7001)
    EnableAI(character)


@NeverRestart(12600060)
def Event_12600060(_, character: int, animation_id: int, animation_id_1: int):
    """Event 12600060"""
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ResetAnimation(character)
    ForceAnimation(character, animation_id_1)


@NeverRestart(12600070)
def Event_12600070(_, character: int, region: int, radius: float):
    """Event 12600070"""
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=character, radius=radius)
    SetNest(character, region=region)
    AICommand(character, command_id=20, command_slot=0)
    IfCharacterInsideRegion(0, character, region=region)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@NeverRestart(12600080)
def Event_12600080(_, attacked_entity: int, animation_id: int, animation_id_1: int, animation_id_2: int):
    """Event 12600080"""
    ForceAnimation(attacked_entity, animation_id, loop=True, skip_transition=True)
    IfAttackedWithDamageType(-1, attacked_entity=attacked_entity, attacker=PLAYER)
    IfEntityWithinDistance(-1, entity=attacked_entity, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((12600080, 12600081))
    EnableRandomFlagInRange(flag_range=(12600080, 12600081))
    SkipLinesIfFlagEnabled(1, 12600080)
    SkipLinesIfFlagEnabled(2, 12600081)
    ForceAnimation(attacked_entity, animation_id_1)
    End()
    ForceAnimation(attacked_entity, animation_id_2)
    End()


@NeverRestart(12600090)
def Event_12600090(_, character: int, region: int):
    """Event 12600090"""
    DisableAI(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)


@NeverRestart(12600105)
def Event_12600105(
    _,
    attacked_entity: int,
    animation_id: int,
    animation_id_1: int,
    character: int,
    character_1: int,
    character_2: int,
):
    """Event 12600105"""
    ForceAnimation(attacked_entity, animation_id, loop=True, skip_transition=True)
    IfAttackedWithDamageType(1, attacked_entity=attacked_entity)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, character_1, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, character_2, ai_status=AIStatusType.Battle)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=1)
    IfAttackedWithDamageType(2, attacked_entity=attacked_entity)
    IfTimeElapsed(3, seconds=10.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(attacked_entity, animation_id_1)


@RestartOnRest(12600110)
def Event_12600110(_, character: int, character_1: int, character_2: int):
    """Event 12600110"""
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    WaitFrames(frames=5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    ForceAnimation(character_1, 7000)
    WaitFrames(frames=15)
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=character,
    )
    EnableCharacter(character_2)
    ForceAnimation(character_2, 7000)


@RestartOnRest(12600120)
def Event_12600120(_, obj_act_id: int, obj: int):
    """Event 12600120"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12600125)
def Event_12600125(_, obj: int, item_lot_param_id: int):
    """Event 12600125"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    CreateObjectVFX(obj, vfx_id=200, model_point=900201)
    IfActionButtonParamActivated(0, action_button_id=2600030, entity=obj)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(item_lot_param_id, host_only=False)
    DeleteObjectVFX(obj)


@RestartOnRest(12600190)
def Event_12600190(_, character: int, left: int):
    """Event 12600190"""
    DisableAI(character)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=30.0)
    SkipLinesIfEqual(1, left=left, right=0)
    IfEntityWithinDistance(-1, entity=left, other_entity=PLAYER, radius=30.0)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)


@RestartOnRest(12600400)
def Event_12600400(_, character: int, flag: int):
    """Event 12600400"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest(12600410)
def Event_12600410():
    """Event 12600410"""
    EndIfFlagEnabled(12600403)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(2600403, region=2602029)
    AICommand(2600403, command_id=10, command_slot=0)
    IfCharacterInsideRegion(0, 2600403, region=2602029)
    AICommand(2600403, command_id=-1, command_slot=0)


@RestartOnRest(12600701)
def Event_12600701():
    """Event 12600701"""
    IfFlagEnabled(1, 1080)
    IfFlagEnabled(1, 72600300)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1080, 1099))
    EnableFlag(1081)


@RestartOnRest(12600703)
def Event_12600703():
    """Event 12600703"""
    IfFlagDisabled(0, 1082)
    DisableFlagRange((1080, 1099))
    EnableFlag(1080)
    DisableFlag(72600300)
    DisableFlagRange((72600300, 72600319))


@NeverRestart(12601294)
def Event_12601294():
    """Event 12601294"""
    WaitFrames(frames=0)


@NeverRestart(12601295)
def Event_12601295(_, entity: int, flag: int, flag_1: int, flag_2: int, state: uchar):
    """Event 12601295"""
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=entity)
    IfFlagEnabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=entity)
    IfFlagState(3, state, FlagType.Absolute, flag_2)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=entity)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12601310)
def Event_12601310(_, flag: int, obj: int, obj_1: int, obj_2: int, flag_1: int):
    """Event 12601310"""
    SkipLinesIfFlagEnabled(7, flag)
    EndOfAnimation(obj=obj, animation_id=4)
    Wait(1.0)
    DisableObjectActivation(obj_1, obj_act_id=2600000)
    EnableObjectActivation(obj_2, obj_act_id=2600000)
    EndIfFlagEnabled(flag_1)
    DisableObjectActivation(obj_2, obj_act_id=2600000)
    End()
    EndOfAnimation(obj=obj, animation_id=0)
    Wait(1.0)
    EnableObjectActivation(obj_1, obj_act_id=2600000)
    DisableObjectActivation(obj_2, obj_act_id=2600000)


@NeverRestart(12601315)
def Event_12601315(_, flag: int, obj: int, obj_1: int, obj_2: int, flag_1: int):
    """Event 12601315"""
    SkipLinesIfFlagEnabled(7, flag)
    EndOfAnimation(obj=obj, animation_id=4)
    Wait(1.0)
    EnableObjectActivation(obj_1, obj_act_id=2600000)
    DisableObjectActivation(obj_2, obj_act_id=2600000)
    EndIfFlagEnabled(flag_1)
    DisableObjectActivation(obj_1, obj_act_id=2600000)
    End()
    EndOfAnimation(obj=obj, animation_id=0)
    Wait(1.0)
    DisableObjectActivation(obj_1, obj_act_id=2600000)
    EnableObjectActivation(obj_2, obj_act_id=2600000)


@NeverRestart(12601320)
def Event_12601320(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    obj: int,
    obj_1: int,
    entity: int,
    obj_act_id: int,
):
    """Event 12601320"""
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=2600000)
    ForceAnimation(entity, 5, wait_for_completion=True)
    ForceAnimation(entity, 6, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    ForceAnimation(entity, 7, wait_for_completion=True)
    DisableFlag(flag)
    EnableFlag(flag_1)
    EnableObjectActivation(obj, obj_act_id=2600000)
    Restart()


@NeverRestart(12601330)
def Event_12601330(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    obj: int,
    obj_1: int,
    entity: int,
    obj_act_id: int,
):
    """Event 12601330"""
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    DisableObjectActivation(obj, obj_act_id=2600000)
    ForceAnimation(entity, 1, wait_for_completion=True)
    ForceAnimation(entity, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region)
    ForceAnimation(entity, 3, wait_for_completion=True)
    DisableFlag(flag)
    DisableFlag(flag_1)
    EnableObjectActivation(obj_1, obj_act_id=2600000)
    Restart()


@NeverRestart(12601340)
def Event_12601340(_, flag: int, flag_1: int, obj: int):
    """Event 12601340"""
    EndIfFlagEnabled(flag)
    EnableFlag(flag_1)
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=2600000)


@NeverRestart(12601351)
def Event_12601351(_, flag: int, obj: int, obj_1: int):
    """Event 12601351"""
    SkipLinesIfFlagEnabled(3, flag)
    EndOfAnimation(obj=obj, animation_id=0)
    EndOfAnimation(obj=obj_1, animation_id=1)
    IfFlagEnabled(0, flag)
    SkipLinesIfFlagDisabled(3, 12601253)
    EndOfAnimation(obj=obj, animation_id=2)
    EndOfAnimation(obj=obj_1, animation_id=4)
    End()
    EndOfAnimation(obj=obj, animation_id=4)
    EndOfAnimation(obj=obj_1, animation_id=2)
    End()


@NeverRestart(12601352)
def Event_12601352():
    """Event 12601352"""
    IfFlagEnabled(0, 12601351)
    GotoIfFlagEnabled(Label.L0, flag=12601253)
    IfCharacterInsideRegion(-1, PLAYER, region=2602241)
    IfCharacterInsideRegion(-1, PLAYER, region=2602244)
    IfFlagDisabled(1, 12601253)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(2601261, 6)
    ForceAnimation(2601260, 8, wait_for_completion=True)
    ForceAnimation(2601261, 3)
    ForceAnimation(2601260, 5, wait_for_completion=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(-2, PLAYER, region=2602242)
    IfCharacterInsideRegion(-2, PLAYER, region=2602243)
    IfFlagEnabled(3, 12601253)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(4, input_condition=3)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(2601261, 8)
    ForceAnimation(2601260, 6, wait_for_completion=True)
    ForceAnimation(2601261, 5)
    ForceAnimation(2601260, 3, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterOutsideRegion(5, PLAYER, region=2602241)
    IfCharacterOutsideRegion(5, PLAYER, region=2602242)
    IfCharacterOutsideRegion(5, PLAYER, region=2602243)
    IfCharacterOutsideRegion(5, PLAYER, region=2602244)
    IfConditionTrue(0, input_condition=5)
    GotoIfFlagEnabled(Label.L2, flag=12601253)
    ForceAnimation(2601261, 9)
    ForceAnimation(2601260, 7, wait_for_completion=True)
    EnableFlag(12601253)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(2601261, 7)
    ForceAnimation(2601260, 9, wait_for_completion=True)
    DisableFlag(12601253)
    Restart()


@RestartOnRest(12605200)
def Event_12605200(_, character__set_draw_parent: int, character: int):
    """Event 12605200"""
    DisableGravity(character)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, character__set_draw_parent)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, character__set_draw_parent, value=0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(character)
    End()
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=character__set_draw_parent,
    )
    Restart()


@NeverRestart(12600990)
def Event_12600990():
    """Event 12600990"""
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfPlayerStandingOnCollision(0, 2604000)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=268,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=268,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=268,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=268,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    RunEvent(9350, slot=0, args=(3,))


@NeverRestart(12601050)
def Event_12601050():
    """Event 12601050"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2601050, animation_id=1)
    DisableObjectActivation(2601050, obj_act_id=2600010)
    NotifyDoorEventSoundDampening(obj=2601050, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12600200)
    Wait(0.0)


@NeverRestart(12601051)
def Event_12601051():
    """Event 12601051"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2601051, animation_id=0)
    DisableObjectActivation(2601051, obj_act_id=2600020)
    DisableObjectActivation(2601051, obj_act_id=2600021)
    NotifyDoorEventSoundDampening(obj=2601051, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=12600201)
    IfObjectActivated(-1, obj_act_id=12600202)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectActivation(2601051, obj_act_id=2600020)
    DisableObjectActivation(2601051, obj_act_id=2600021)
    Wait(0.0)


@NeverRestart(12607010)
def Event_12607010(_, flag: int, destination: int):
    """Event 12607010"""
    IfFlagEnabled(0, flag)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(flag)


@NeverRestart(12607020)
def Event_12607020(_, flag: int, respawn_point_id: int, flag_1: int):
    """Event 12607020"""
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    WarpPlayerToRespawnPoint(respawn_point_id)
    EnableFlag(flag_1)


@NeverRestart(12607040)
def Event_12607040():
    """Event 12607040"""
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagDisabled(0, 9210)
    SkipLinesIfFlagDisabled(2, 9001)
    EnableFlag(12607810)
    EnableFlag(12607811)
    SkipLinesIfFlagDisabled(2, 9002)
    EnableFlag(12607830)
    EnableFlag(12607831)
    SkipLinesIfFlagDisabled(2, 9003)
    EnableFlag(12607850)
    EnableFlag(12607851)
    SkipLinesIfFlagDisabled(2, 9004)
    EnableFlag(12607870)
    EnableFlag(12607871)
    SkipLinesIfFlagDisabled(2, 9005)
    EnableFlag(12607890)
    EnableFlag(12607891)
    SkipLinesIfFlagDisabled(2, 9006)
    EnableFlag(12607910)
    EnableFlag(12607911)
    SkipLinesIfFlagDisabled(2, 9007)
    EnableFlag(12607930)
    EnableFlag(12607931)
    SkipLinesIfFlagDisabled(2, 9008)
    EnableFlag(12607950)
    EnableFlag(12607951)
    SkipLinesIfFlagDisabled(2, 9009)
    EnableFlag(12607970)
    EnableFlag(12607971)
    SkipLinesIfFlagDisabled(2, 9010)
    EnableFlag(12607990)
    EnableFlag(12607991)
    DisableFlagRange((9000, 9010))


@NeverRestart(12607050)
def Event_12607050(_, flag: int, character: int, destination: int):
    """Event 12607050"""
    EndIfFlagEnabled(flag)
    DisableGravity(character)
    IfCharacterBackreadEnabled(0, character)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(character, 101165, loop=True)
    Wait(1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagEnabled(0, flag)
    ForceAnimation(character, 101166, wait_for_completion=True)
    DisableCharacter(character)
