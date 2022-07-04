"""
linked:
236

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_アイコレクター
88: ボス_戦闘開始
104: ボス戦_撃破時間
122: ギミック_m22_最初の門を開けた
158: ギミック_m22_SC開通
186: ギミック_エレベーター起動
214: PC情報_墓地街到達
236: N:\\SPRJ\\data\\Param\\event\\common.emevd
312: 
314: 
316: 
318: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=0, args=(2200950, 2201950, 999, 12207800))
    RunEvent(7000, slot=1, args=(2200951, 2201951, 12201800, 12207820))
    RunEvent(7100, slot=0, args=(72200200, 2201950))
    RunEvent(7100, slot=1, args=(72200201, 2201951))
    RunEvent(7200, slot=0, args=(72200100, 2201950, 2102951))
    RunEvent(7200, slot=1, args=(72200101, 2201951, 2102951))
    RunEvent(7300, slot=0, args=(72102200, 2201950))
    RunEvent(7300, slot=1, args=(72102201, 2201951))
    RunEvent(7600, slot=0, args=(2201999, 2203999))
    RunEvent(9200, slot=0, args=(2203900,))
    RunEvent(9220, slot=0, args=(2200710, 12204220, 12204221, 2200, 22, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=0, args=(2200710, 12204220, 12204221, 2200, 12204800, 22, 0), arg_types="iiiiiBB")
    CreateObjectVFX(2201000, vfx_id=750, model_point=900110)
    CreateObjectVFX(2201003, vfx_id=750, model_point=900110)
    CreateObjectVFX(2201004, vfx_id=750, model_point=900110)
    CreateHazard(
        obj_flag=12200050,
        obj=2201000,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12200051,
        obj=2201003,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12200052,
        obj=2201004,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    RegisterLadder(start_climbing_flag=12200000, stop_climbing_flag=12200001, obj=2201100)
    StartPlayLogMeasurement(measurement_id=2200000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2200001, name=18, overwrite=True)
    CreateProjectileOwner(entity=2200420)
    CreateProjectileOwner(entity=2200421)
    CreateProjectileOwner(entity=2200422)
    AICommand(2200310, command_id=200, command_slot=0)
    AICommand(2200311, command_id=200, command_slot=0)
    Event_12204892()
    Event_12204893()
    Event_12201800()
    Event_12201801()
    Event_12201802()
    Event_12201803()
    Event_12204890()
    Event_12204891()
    Event_12204802()
    Event_12204803()
    Event_12204804()
    Event_12204805()
    Event_12204807()
    Event_12201804()
    Event_12204808(0, character=2200800, flag=12204848)
    Event_12204808(1, character=2200801, flag=12204849)
    Event_12204810()
    Event_12204811()
    Event_12204812(0, character=2200800, character_1=2200801, destination=2202810, flag=12204848)
    Event_12204812(1, character=2200801, character_1=2200800, destination=2202815, flag=12204849)
    Event_12204814(
        0,
        character=2200800,
        first_flag=12204850,
        last_flag=12204853,
        first_flag_1=12204850,
        flag=12204851,
        flag_1=12204852,
        last_flag_1=12204853,
        flag_2=12204848
    )
    Event_12204814(
        1,
        character=2200801,
        first_flag=12204855,
        last_flag=12204858,
        first_flag_1=12204855,
        flag=12204856,
        flag_1=12204857,
        last_flag_1=12204858,
        flag_2=12204849
    )
    Event_12204820(0, character=2200800, flag=12204850, region=2202810, destination=2202812, flag_1=12204854)
    Event_12204820(1, character=2200800, flag=12204851, region=2202811, destination=2202810, flag_1=12204854)
    Event_12204820(2, character=2200800, flag=12204852, region=2202812, destination=2202817, flag_1=12204854)
    Event_12204820(3, character=2200800, flag=12204853, region=2202817, destination=2202811, flag_1=12204854)
    Event_12204820(4, character=2200801, flag=12204855, region=2202813, destination=2202814, flag_1=12204859)
    Event_12204820(5, character=2200801, flag=12204856, region=2202814, destination=2202815, flag_1=12204859)
    Event_12204820(6, character=2200801, flag=12204857, region=2202815, destination=2202816, flag_1=12204859)
    Event_12204820(7, character=2200801, flag=12204858, region=2202816, destination=2202813, flag_1=12204859)
    Event_12204830(0, character=2200800, flag=12204854, flag_1=12204848)
    Event_12204830(1, character=2200801, flag=12204859, flag_1=12204849)
    Event_12204832(0, character=2200810)
    Event_12204832(1, character=2200811)
    Event_12204832(2, character=2200812)
    Event_12204835(0, character=2200810, flag=12204870)
    Event_12204835(1, character=2200811, flag=12204871)
    Event_12204835(2, character=2200812, flag=12204872)
    Event_12204838()
    Event_12204839()
    Event_12204840()
    Event_12204841()
    Event_12204842()
    Event_12204843()
    Event_12204844()
    Event_12200100()
    Event_12200101()
    Event_12200110()
    Event_12200111()
    Event_12200112()
    Event_12200120()
    Event_12200122()
    Event_12200123()
    Event_12200121()
    Event_12200124()
    Event_12200130()
    Event_12200131()
    Event_12200132()
    Event_12200150(0, character=2200261, destination=2202660)
    Event_12200150(1, character=2200250, destination=2202661)
    Event_12200150(2, character=2200251, destination=2202662)
    Event_12200150(3, character=2200260, destination=2202663)
    Event_12200150(4, character=2200201, destination=2202664)
    Event_12200150(5, character=2200205, destination=2202665)
    Event_12200150(6, character=2200204, destination=2202666)
    Event_12200150(7, character=2200252, destination=2202667)
    Event_12200150(8, character=2200335, destination=2202668)
    Event_12200150(9, character=2200330, destination=2202669)
    Event_12200150(10, character=2200331, destination=2202670)
    Event_12200150(11, character=2200332, destination=2202671)
    Event_12200150(12, character=2200333, destination=2202672)
    Event_12200150(13, character=2200334, destination=2202673)
    Event_12200150(14, character=2200280, destination=2202674)
    Event_12200150(15, character=2200340, destination=2202675)
    Event_12200150(16, character=2200341, destination=2202676)
    Event_12200150(17, character=2200273, destination=2202677)
    Event_12200150(18, character=2200270, destination=2202678)
    Event_12200150(19, character=2200271, destination=2202679)
    Event_12200150(20, character=2200272, destination=2202680)
    Event_12200150(21, character=2200202, destination=2202681)
    Event_12200150(22, character=2200311, destination=2202682)
    Event_12200150(23, character=2200120, destination=2202683)
    Event_12200300()
    Event_12200310(0, obj=2201050, obj_act_id=12200900, obj_act_id_1=9942)
    Event_12200210(0, 2201010, 7.0, 0, 2202020, 10)
    Event_12200210(1, 2201011, 7.0, 30, 2202020, 10)
    Event_12200210(2, 2201016, 7.0, 15, 2202020, 10)
    Event_12200210(3, 2201017, 7.0, 0, 2202020, 10)
    Event_12200210(4, 2201018, 7.0, 5, 2202020, 10)
    Event_12200210(5, 2201012, 10.0, 10, 2202021, 11)
    Event_12200210(6, 2201013, 10.0, 0, 2202021, 11)
    Event_12200210(7, 2201014, 10.0, 30, 2202021, 11)
    Event_12200210(8, 2201015, 10.0, 0, 2202021, 11)
    Event_12200220(0, character=2200111, flag=52200990)
    Event_12200220(1, character=2200170, flag=52200980)
    Event_12200220(2, character=2200110, flag=52200970)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6631)
    EnableFlag(12201999)
    SkipLinesIfFlagEnabled(5, 12201999)
    EnableObject(2201150)
    DisableObject(2201151)
    EnableTreasure(obj=2201150)
    DisableTreasure(obj=2201151)
    SkipLines(4)
    DisableObject(2201150)
    EnableObject(2201151)
    DisableTreasure(obj=2201150)
    EnableTreasure(obj=2201151)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6309)
    EnableFlag(12201998)
    SkipLinesIfFlagEnabled(5, 12201998)
    EnableObject(2201500)
    DisableObject(2201501)
    EnableTreasure(obj=2201500)
    DisableTreasure(obj=2201501)
    SkipLines(4)
    DisableObject(2201500)
    EnableObject(2201501)
    DisableTreasure(obj=2201500)
    EnableTreasure(obj=2201501)
    Event_12200990()
    Event_12204000(0, 2200500, 20.0)
    Event_12204000(1, 2200501, 20.0)
    Event_12204000(2, 2200502, 20.0)
    Event_12204000(3, 2200503, 20.0)
    Event_12204000(4, 2200504, 20.0)
    Event_12204000(5, 2200505, 20.0)
    Event_12204000(6, 2200506, 20.0)
    Event_12204000(7, 2200507, 20.0)
    Event_12204000(8, 2200508, 20.0)
    Event_12205000()
    Event_12205001()
    Event_12205002()
    Event_12205003()
    Event_12205040()
    Event_12205041()
    Event_12205020()
    Event_12205030()
    Event_12205031()
    Event_12205060()
    Event_12205050()
    Event_12205051()
    Event_12205070()
    Event_12205080()
    Event_12205010(
        0,
        character=2200240,
        character_1=2200130,
        region=2202070,
        region_1=2202370,
        region_2=2202080,
        flag=12205015
    )
    Event_12205010(
        1,
        character=2200223,
        character_1=2200310,
        region=2202071,
        region_1=2202371,
        region_2=2202171,
        flag=12205016
    )
    Event_12205015(0, 2200130, 2202370, -1, 12205010)
    Event_12205015(1, character=2200310, region=2202371, command_id=200, flag=12205011)
    Event_12205100(0, 2200202, 2202130, 3.0, 12205105, 50)
    Event_12205100(1, 2200200, 2202150, 3.0, 12205106, 50)
    Event_12205100(2, 2200201, 2202151, 3.0, 12205107, 60)
    Event_12205100(3, 2200204, 2202152, 5.0, 12205108, 50)
    Event_12205105(0, 2200202, 2202130, 3007, 3.0)
    Event_12205105(1, 2200200, 2202150, 3009, 2.5)
    Event_12205105(2, 2200201, 2202154, 3022, 2.0)
    Event_12205105(3, 2200204, 2202153, 3011, 2.700000047683716)
    Event_12205110(0, 2200203, 2202140, 3.0, 3006)
    Event_12205120(0, 2200211, 2202160, 5.0, 2202161)
    Event_12205120(1, 2200212, 2202160, 5.0, 2202161)
    Event_12205120(2, 2200213, 2202160, 5.0, 2202161)
    Event_12205120(3, 2200223, 2202170, 15.0, 2202171)
    Event_12205120(4, 2200224, 2202170, 15.0, 2202171)
    Event_12205120(5, 2200230, 2202180, 6.0, 2202180)
    Event_12205120(6, 2200231, 2202180, 6.0, 2202180)
    Event_12205120(7, 2200232, 2202180, 6.0, 2202180)
    Event_12205120(8, 2200240, 2202190, 15.0, 2202191)
    Event_12205120(9, 2200250, 2202200, 10.0, 2202201)
    Event_12205120(10, 2200251, 2202200, 10.0, 2202201)
    Event_12205120(11, 2200252, 2202200, 10.0, 2202201)
    Event_12205120(12, 2200260, 2202200, 10.0, 2202201)
    Event_12205120(13, 2200261, 2202200, 10.0, 2202201)
    Event_12205120(14, 2200270, 2202220, 10.0, 2202221)
    Event_12205120(15, 2200271, 2202220, 10.0, 2202221)
    Event_12205120(16, 2200272, 2202220, 10.0, 2202221)
    Event_12205120(17, 2200290, 2202230, 8.0, 2202231)
    Event_12205120(18, 2200291, 2202230, 8.0, 2202231)
    Event_12205120(19, 2200292, 2202230, 8.0, 2202231)
    Event_12205120(20, 2200280, 2202240, 5.0, 2202240)
    Event_12205120(21, 2200412, 2202260, 5.0, 2202260)
    Event_12205120(22, 2200310, 2202170, 15.0, 2202171)
    Event_12205120(23, 2200450, 2202270, 15.0, 2202271)
    Event_12205120(24, 2200460, 2202310, 15.0, 2202310)
    Event_12205120(25, 2200470, 2202430, 3.0, 2202431)
    Event_12205120(26, 2200430, 2202170, 7.0, 2202171)
    Event_12205150(0, 2200100, 7014, 0, 0.0)
    Event_12205150(1, 2200301, 7010, 7011, 7.0)
    Event_12205150(2, 2200303, 7012, 7013, 0.0)
    Event_12205150(3, 2200300, 7014, 0, 0.0)
    Event_12205150(4, 2200212, 7014, 0, 0.0)
    Event_12205160(0, region=2202040, obj=2201401, character=2200410, region_1=2200400)
    Event_12205160(1, region=2202041, obj=2201406, character=2200411, region_1=2200401)
    Event_12205170(0, obj__projectile_id=2201400, owner_entity=2200420)
    Event_12205170(1, obj__projectile_id=2201401, owner_entity=2200420)
    Event_12205170(2, obj__projectile_id=2201402, owner_entity=2200420)
    Event_12205170(3, obj__projectile_id=2201403, owner_entity=2200420)
    Event_12205170(4, obj__projectile_id=2201404, owner_entity=2200420)
    Event_12205170(5, obj__projectile_id=2201405, owner_entity=2200420)
    Event_12205170(6, obj__projectile_id=2201406, owner_entity=2200420)
    Event_12205170(7, obj__projectile_id=2201407, owner_entity=2200422)
    Event_12205170(8, obj__projectile_id=2201408, owner_entity=2200422)
    Event_12205170(9, obj__projectile_id=2201409, owner_entity=2200422)
    Event_12205170(10, obj__projectile_id=2201410, owner_entity=2200421)
    Event_12205170(11, obj__projectile_id=2201411, owner_entity=2200421)
    Event_12205170(12, obj__projectile_id=2201412, owner_entity=2200421)
    Event_12205170(13, obj__projectile_id=2201413, owner_entity=2200421)
    Event_12205170(14, obj__projectile_id=2201414, owner_entity=2200421)
    Event_12205170(15, obj__projectile_id=2201415, owner_entity=2200421)
    Event_12205170(16, obj__projectile_id=2201416, owner_entity=2200421)
    Event_12205170(17, obj__projectile_id=2201417, owner_entity=2200421)
    Event_12205170(18, obj__projectile_id=2201418, owner_entity=2200421)
    Event_12205170(19, obj__projectile_id=2201419, owner_entity=2200421)
    Event_12205170(20, obj__projectile_id=2201420, owner_entity=2200420)
    Event_12205170(21, obj__projectile_id=2201421, owner_entity=2200420)
    Event_12205170(22, obj__projectile_id=2201422, owner_entity=2200421)
    Event_12205170(23, obj__projectile_id=2201423, owner_entity=2200421)
    Event_12205170(24, obj__projectile_id=2201424, owner_entity=2200421)
    Event_12205170(25, obj__projectile_id=2201425, owner_entity=2200421)
    Event_12205170(26, obj__projectile_id=2201426, owner_entity=2200421)
    Event_12205170(27, obj__projectile_id=2201427, owner_entity=2200421)
    Event_12205200(0, character=2200200)
    Event_12205200(1, character=2200201)
    Event_12205200(2, character=2200202)
    Event_12205200(3, character=2200204)
    Event_12205200(4, character=2200205)
    Event_12205200(5, character=2200251)
    Event_12205200(6, character=2200270)
    Event_12205200(7, character=2200271)
    Event_12205210(0, character=2200320)
    Event_12205210(1, character=2200321)
    Event_12205220(0, character=2200240, region=2202282, animation_id=3006, region_1=2202302)
    Event_12205220(1, character=2200250, region=2202280, animation_id=7001, region_1=2202300)
    Event_12205220(2, character=2200250, region=2202281, animation_id=7001, region_1=2202301)
    Event_12205220(3, character=2200252, region=2202279, animation_id=3006, region_1=2202299)
    Event_12205220(4, character=2200251, region=2202278, animation_id=7001, region_1=2202298)
    Event_12205220(5, character=2200450, region=2202283, animation_id=7014, region_1=2202283)
    Event_12205230(0, character=2200330, ai_param_id=114093)
    Event_12205230(1, character=2200331, ai_param_id=114094)
    Event_12205230(2, character=2200332, ai_param_id=114094)
    Event_12205230(3, character=2200333, ai_param_id=114093)
    Event_12205230(4, character=2200334, ai_param_id=114094)
    Event_12205240(0, character=2200340)
    Event_12205240(1, character=2200341)
    Event_12205260(0, character=2200110, region=2202630, flag=12205265, flag_1=12205270)
    Event_12205260(1, character=2200111, region=2202632, flag=12205266, flag_1=12205271)
    Event_12205265(0, character=2200110, region=2202631, region_1=2202380, event_id=12205260, event_id_1=12205270)
    Event_12205265(1, character=2200111, region=2202633, region_1=2202381, event_id=12205261, event_id_1=12205271)
    Event_12205270(
        0,
        character=2200110,
        region=2202380,
        flag=12205265,
        region_1=2202630,
        region_2=2202381,
        event_id=12205260
    )
    Event_12205270(
        1,
        character=2200111,
        region=2202381,
        flag=12205266,
        region_1=2202633,
        region_2=2202382,
        event_id=12205261
    )
    Event_12205300(0, 2203300, 1439, 6001, 9802)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2203950)
    DisableGravity(2203950)
    DisableCharacterCollision(2203950)
    DisableAnimations(2203951)
    DisableGravity(2203951)
    DisableCharacterCollision(2203951)
    Event_12204010()


@NeverRestart(12201800)
def Event_12201800():
    """Event 12201800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2203802)
    DisableSoundEvent(sound_id=2203803)
    DisableCharacter(2200800)
    Kill(2200800)
    DisableCharacter(2200801)
    Kill(2200801)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteVFX(2203800)
    DeleteVFX(2203801)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 2200800)
    IfCharacterDead(1, 2200801)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteVFX(2203800)
    DeleteVFX(2203801)
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2200800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    AwardAchievement(achievement_id=23)
    AwardItemLot(21002950, host_only=False)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(72400512)
    EnableFlag(2200)
    EnableFlag(9452)
    EnableFlag(5911)
    StopPlayLogMeasurement(measurement_id=2200000)
    StopPlayLogMeasurement(measurement_id=2200001)
    StopPlayLogMeasurement(measurement_id=2200010)
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


@NeverRestart(12201801)
def Event_12201801():
    """Event 12201801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(1, 12201800)
    IfCharacterBackreadDisabled(2, 2200800)
    IfHealthLessThanOrEqual(2, 2200800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2202800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12201802)
def Event_12201802():
    """Event 12201802"""
    EndIfFlagEnabled(12201800)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2200800)
    IfFlagDisabled(1, 12201800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2202805)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2200800)
    Wait(0.10000000149011612)
    IfPlayerInsightAmountEqual(2, value=0)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionTrue(1, 2)
    ForceAnimation(2200800, 3011)
    EnableFlag(12204800)
    EndIfFlagEnabled(9338)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9338)


@NeverRestart(12201803)
def Event_12201803():
    """Event 12201803"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSpawner(entity=2205000)
    DisableSpawner(entity=2205001)
    DisableSpawner(entity=2205002)
    DisableBackread(2200810)
    DisableBackread(2200811)
    DisableBackread(2200812)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12201800)
    DisableSpawner(entity=2205000)
    DisableSpawner(entity=2205001)
    DisableSpawner(entity=2205002)
    Kill(2200810)
    Kill(2200811)
    Kill(2200812)


@NeverRestart(12201804)
def Event_12201804():
    """Event 12201804"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12204800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2200800)
    EnableFlag(12204800)
    EnableFlag(12201802)


@NeverRestart(12204890)
def Event_12204890():
    """Event 12204890"""
    EndIfFlagEnabled(12201800)
    GotoIfFlagEnabled(Label.L0, flag=12201802)
    SkipLinesIfClient(2)
    DisableObject(2201800)
    DeleteVFX(2203800, erase_root_only=False)
    DisableObject(2201801)
    DeleteVFX(2203801, erase_root_only=False)
    IfFlagDisabled(1, 12201800)
    IfFlagEnabled(1, 12201802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2201800)
    EnableObject(2201801)
    CreateVFX(2203800)
    CreateVFX(2203801)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2200800, entity=2201800)
    IfFlagDisabled(2, 12201800)
    IfFlagEnabled(3, 12201800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2202801)
    IfTimeElapsed(5, seconds=2.0)
    IfCharacterHuman(5, PLAYER)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12204800)
    Restart()


@NeverRestart(12204891)
def Event_12204891():
    """Event 12204891"""
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagDisabled(1, 12201800)
    IfFlagEnabled(1, 12201802)
    IfFlagEnabled(1, 12204800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=2200800, entity=2201800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2202801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12204801)
    Restart()


@NeverRestart(12204892)
def Event_12204892():
    """Event 12204892"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2201800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12204893)
def Event_12204893():
    """Event 12204893"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2201800, radius=2.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2201800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12204802)
def Event_12204802():
    """Event 12204802"""
    EndIfFlagEnabled(12201800)
    DisableAI(2200800)
    DisableHealthBar(2200800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12204800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2200800)
    EnableBossHealthBar(2200800, name=210000)
    CreatePlayLog(name=88)
    StartPlayLogMeasurement(measurement_id=2200010, name=104, overwrite=True)


@NeverRestart(12204803)
def Event_12204803():
    """Event 12204803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2203802)
    DisableSoundEvent(sound_id=2203803)
    IfFlagDisabled(1, 12201800)
    IfFlagEnabled(1, 12204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12204801)
    IfCharacterInsideRegion(1, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2203802)
    IfHealthValueEqual(-1, 2200800, value=1)
    IfHealthValueEqual(-1, 2200801, value=1)
    IfConditionTrue(2, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12201800)
    IfFlagEnabled(2, 12204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12204801)
    IfCharacterInsideRegion(2, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2203802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2203803)


@NeverRestart(12204804)
def Event_12204804():
    """Event 12204804"""
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12204800)
    IfCharacterWhitePhantom(2, PLAYER)
    IfFlagEnabled(2, 12204801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=1)


@NeverRestart(12204805)
def Event_12204805():
    """Event 12204805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(0, 12201800)
    DisableBossMusic(sound_id=2203802)
    DisableBossMusic(sound_id=2203803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12204807)
def Event_12204807():
    """Event 12204807"""
    EndIfFlagEnabled(12201800)
    IfHealthValueEqual(-1, 2200800, value=1)
    IfHealthValueEqual(-1, 2200801, value=1)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2200800, command_id=100, command_slot=0)
    AICommand(2200801, command_id=100, command_slot=0)
    Wait(10.0)
    IfCharacterDead(1, 2200800)
    IfCharacterDead(1, 2200801)
    EndIfConditionTrue(1)
    EnableBossHealthBar(2200801, name=210000, bar_slot=1)


@NeverRestart(12204808)
def Event_12204808(_, character: int, flag: int):
    """Event 12204808"""
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=character, radius=12.0)
    IfCharacterHasTAEEvent(3, character, tae_event_id=10)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect_WithUnknownEffect(character, 5686)

    # --- 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=6.0)
    IfFlagDisabled(2, flag)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect_WithUnknownEffect(character, 5688)
    Restart()


@NeverRestart(12204810)
def Event_12204810():
    """Event 12204810"""
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200801)
    DisableHealthBar(2200801)
    DisableCharacter(2200801)
    IfHealthLessThanOrEqual(0, 2200800, value=0.5)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200801, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200801)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200801)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableCharacter(2200801)
    EnableAI(2200801)


@NeverRestart(12204811)
def Event_12204811():
    """Event 12204811"""
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    SetAIParamID(2200800, ai_param_id=210021)
    IfCharacterDead(-1, 2200810)
    IfAttackedWithDamageType(-1, attacked_entity=2200800)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2200800, ai_param_id=210020)


@NeverRestart(12204812)
def Event_12204812(_, character: int, character_1: int, destination: int, flag: int):
    """Event 12204812"""
    EndIfFlagEnabled(12201800)
    EnableImmortality(character)
    IfHealthValueEqual(3, character, value=1)
    IfHealthValueLessThan(3, character_1, value=1)
    IfHealthValueEqual(4, character, value=1)
    IfHealthValueEqual(4, character_1, value=1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    Wait(0.0)
    ResetAnimation(character)
    Wait(0.10000000149011612)
    ForceAnimation(character, 7000)
    WaitFrames(frames=75)
    ForceAnimation(character, 7001, loop=True)
    IfTimeElapsed(1, seconds=45.0)
    IfHealthValueEqual(2, character_1, value=1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    AddSpecialEffect(character, 5686)
    Wait(3.0)
    DisableCharacter(character)
    ForceAnimation(character, 0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(character, 5698)
    Wait(3.0)
    EnableCharacter(character)
    ReplanAI(character)
    DisableFlag(flag)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Kill(character)
    Kill(character_1)


@NeverRestart(12204814)
def Event_12204814(
    _,
    character: int,
    first_flag: uint,
    last_flag: uint,
    first_flag_1: int,
    flag: int,
    flag_1: int,
    last_flag_1: int,
    flag_2: int,
):
    """Event 12204814"""
    EndIfFlagEnabled(12201800)
    IfCharacterHasTAEEvent(0, character, tae_event_id=30)
    AddSpecialEffect(character, 5686)
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfHealthValueNotEqual(1, character, value=1)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfFlagDisabled(Label.L1, flag=first_flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(first_flag_1)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=flag)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(flag)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, flag=flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(flag_1)
    Goto(Label.L0)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L0, flag=last_flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(last_flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, first_flag_1)
    IfFlagEnabled(-1, flag)
    IfFlagEnabled(-1, flag_1)
    IfFlagEnabled(-1, last_flag_1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_2)
    Restart()


@NeverRestart(12204820)
def Event_12204820(_, character: int, flag: int, region: int, destination: int, flag_1: int):
    """Event 12204820"""
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    IfCharacterInsideRegion(1, character, region=region)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    Restart()


@NeverRestart(12204830)
def Event_12204830(_, character: int, flag: int, flag_1: int):
    """Event 12204830"""
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    Wait(2.0)
    EnableCharacter(character)
    ReplanAI(character)
    DisableFlag(flag_1)
    DisableFlag(flag)
    Restart()


@NeverRestart(12204832)
def Event_12204832(_, character: int):
    """Event 12204832"""
    EndIfFlagEnabled(12201800)
    IfCharacterDead(0, character)
    IncrementEventValue(12204860, bit_count=10, max_value=10)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    Restart()


@NeverRestart(12204835)
def Event_12204835(_, character: int, flag: int):
    """Event 12204835"""
    EndIfFlagEnabled(12201800)
    IfCharacterDead(0, character)
    EnableFlag(flag)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    DisableFlag(flag)
    Restart()


@NeverRestart(12204838)
def Event_12204838():
    """Event 12204838"""
    EndIfFlagEnabled(12201800)
    IfFlagDisabled(4, 12204845)
    IfConditionTrue(0, input_condition=4)
    IfCharacterHasTAEEvent(-1, 2200800, tae_event_id=20)
    IfCharacterHasTAEEvent(-1, 2200801, tae_event_id=20)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 12204870)
    IfCharacterHasTAEEvent(-2, 2200800, tae_event_id=20)
    IfCharacterHasTAEEvent(-2, 2200801, tae_event_id=20)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 12204871)
    IfCharacterHasTAEEvent(-3, 2200800, tae_event_id=20)
    IfCharacterHasTAEEvent(-3, 2200801, tae_event_id=20)
    IfConditionTrue(3, input_condition=-3)
    IfFlagEnabled(3, 12204872)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    EnableSpawner(entity=2205000)
    IfCharacterHasTAEEvent(0, 2200810, tae_event_id=10)
    DisableSpawner(entity=2205000)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=2)
    EnableSpawner(entity=2205001)
    IfCharacterHasTAEEvent(0, 2200811, tae_event_id=10)
    DisableSpawner(entity=2205001)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    EnableSpawner(entity=2205002)
    IfCharacterHasTAEEvent(0, 2200812, tae_event_id=10)
    DisableSpawner(entity=2205002)
    Restart()


@RestartOnRest(12204839)
def Event_12204839():
    """Event 12204839"""
    EndIfFlagEnabled(12201800)
    IfFlagDisabled(1, 12204845)
    IfConditionTrue(0, input_condition=1)
    IfHealthValueEqual(-1, 2200800, value=1)
    IfHealthValueEqual(-1, 2200801, value=1)
    IfConditionTrue(-2, input_condition=-1)
    IfFlagEnabled(-2, 12204812)
    IfFlagEnabled(2, 12201802)
    IfThisEventFlagDisabled(2)
    IfFlagDisabled(2, 12201810)
    IfEventValueEqual(3, flag=12204860, bit_count=10, value=3)
    IfFlagDisabled(3, 12204875)
    IfHealthLessThanOrEqual(4, 2200800, value=0.30000001192092896)
    IfEventValueLessThanOrEqual(4, flag=12204860, bit_count=10, value=2)
    IfFlagDisabled(4, 12204875)
    IfHealthLessThanOrEqual(5, 2200801, value=0.5)
    IfEventValueLessThanOrEqual(5, flag=12204860, bit_count=10, value=2)
    IfFlagDisabled(5, 12204875)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfEventValueGreaterThanOrEqual(6, flag=12204860, bit_count=10, value=5)
    IfHealthValueEqual(-4, 2200800, value=1)
    IfHealthValueEqual(-4, 2200801, value=1)
    IfConditionTrue(7, input_condition=-4)
    IfEventValueLessThanOrEqual(7, flag=12204860, bit_count=10, value=4)
    IfEventValueGreaterThanOrEqual(7, flag=12204860, bit_count=10, value=3)
    IfConditionTrue(-5, input_condition=6)
    IfConditionTrue(-5, input_condition=7)
    IfConditionTrue(-6, input_condition=-2)
    IfConditionTrue(-6, input_condition=2)
    IfConditionTrue(-6, input_condition=-3)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)

    # --- 1 --- #
    DefineLabel(1)
    IfHealthValueEqual(8, 2200800, value=1)
    IfHealthValueNotEqual(9, 2200800, value=1)
    IfConditionTrue(-7, input_condition=8)
    IfConditionTrue(-7, input_condition=9)
    GotoIfConditionTrue(Label.L2, input_condition=8)
    ResetAnimation(2200800)
    Wait(0.10000000149011612)
    ForceAnimation(2200800, 3011)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    ResetAnimation(2200801)
    Wait(0.10000000149011612)
    ForceAnimation(2200801, 3011)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=-5)
    WaitFrames(frames=65)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(entity=2205001)
    WaitFrames(frames=35)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(entity=2205002)
    End()

    # --- 4 --- #
    DefineLabel(4)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(entity=2205000)
    EnableFlag(12204876)
    EnableFlag(12201810)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(entity=2205001)
    EnableFlag(12204875)
    Restart()

    # --- 6 --- #
    DefineLabel(6)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(entity=2205002)
    End()


@RestartOnRest(12204840)
def Event_12204840():
    """Event 12204840"""
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(5, 12204845)
    IfConditionTrue(0, input_condition=5)
    IfEventValueGreaterThanOrEqual(1, flag=12204860, bit_count=10, value=3)
    IfFlagEnabled(2, 12204870)
    IfEventValueLessThanOrEqual(2, flag=12204860, bit_count=10, value=2)
    IfHealthValueEqual(5, 2200800, value=1)
    IfHealthValueEqual(5, 2200801, value=1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    IfHealthValueEqual(3, 2200800, value=1)
    IfHealthValueNotEqual(4, 2200800, value=1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=3)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200800, command_id=10, command_slot=2)
    ReplanAI(2200800)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagDisabled(0, 12204870)
    AICommand(2200800, command_id=-1, command_slot=2)
    ReplanAI(2200800)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204880)


@RestartOnRest(12204841)
def Event_12204841():
    """Event 12204841"""
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 12204880)
    IfEventValueGreaterThanOrEqual(1, flag=12204860, bit_count=10, value=5)
    IfEventValueLessThanOrEqual(2, flag=12204860, bit_count=10, value=4)
    IfFlagEnabled(2, 12204870)
    IfEventValueLessThanOrEqual(3, flag=12204860, bit_count=10, value=4)
    IfFlagEnabled(3, 12204871)
    IfHealthValueEqual(6, 2200800, value=1)
    IfHealthValueEqual(6, 2200801, value=1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    IfHealthValueEqual(4, 2200800, value=1)
    IfHealthValueNotEqual(5, 2200800, value=1)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=4)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200800, command_id=10, command_slot=2)
    ReplanAI(2200800)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagDisabled(4, 12204870)
    IfFlagDisabled(4, 12204871)
    IfConditionTrue(0, input_condition=4)
    AICommand(2200800, command_id=-1, command_slot=2)
    ReplanAI(2200800)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204881)


@RestartOnRest(12204842)
def Event_12204842():
    """Event 12204842"""
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 12204881)
    IfFlagEnabled(-1, 12204870)
    IfFlagEnabled(-1, 12204871)
    IfFlagEnabled(-1, 12204872)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=15.0, max_seconds=25.0)
    AICommand(2200800, command_id=10, command_slot=2)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    IfFlagDisabled(1, 12204870)
    IfFlagDisabled(1, 12204871)
    IfFlagDisabled(1, 12204872)
    IfConditionTrue(0, input_condition=1)
    AICommand(2200800, command_id=-1, command_slot=2)
    AICommand(2200801, command_id=-1, command_slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    Restart()


@RestartOnRest(12204843)
def Event_12204843():
    """Event 12204843"""
    Wait(1.0)
    DisableCharacter(2200810)
    DisableCharacter(2200811)
    DisableCharacter(2200812)
    DisableAnimations(2200810)
    DisableAnimations(2200811)
    DisableAnimations(2200812)
    IfFlagDisabled(1, 12201810)
    EndIfConditionTrue(1)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(0, 12204845)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2200800, 3011)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(entity=2205000)


@RestartOnRest(12204844)
def Event_12204844():
    """Event 12204844"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountLessThanOrEqual(0, value=0)
    EnableFlag(12204845)
    IfPlayerInsightAmountGreaterThanOrEqual(0, value=1)
    DisableFlag(12204845)
    Restart()


@NeverRestart(12200100)
def Event_12200100():
    """Event 12200100"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201001, animation_id=1)
    DisableObjectActivation(2201001, obj_act_id=2200010)
    NotifyDoorEventSoundDampening(obj=2201001, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200101)
    CreatePlayLog(name=122)
    Wait(0.0)


@NeverRestart(12200101)
def Event_12200101():
    """Event 12200101"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201060, animation_id=0)
    DisableObjectActivation(2201060, obj_act_id=2200030)
    NotifyDoorEventSoundDampening(obj=2201060, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200500)
    Wait(0.0)


@NeverRestart(12200110)
def Event_12200110():
    """Event 12200110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201002, animation_id=1)
    DisableObjectActivation(2201220, obj_act_id=100)
    NotifyDoorEventSoundDampening(obj=2201002, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200112)
    CreatePlayLog(name=158)
    DisableObjectActivation(2201220, obj_act_id=100)
    ForceAnimation(2201002, 1)
    Wait(0.0)


@NeverRestart(12200111)
def Event_12200111():
    """Event 12200111"""
    DisableNetworkSync()
    EndIfFlagEnabled(12200110)
    IfActionButtonParam(1, action_button_id=2200000, entity=2201002)
    IfActionButtonParam(2, action_button_id=2200001, entity=2201002)
    IfFlagEnabled(3, 12200110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    DisplayDialog(text=10010160, anchor_entity=2201002, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12200112)
def Event_12200112():
    """Event 12200112"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12200110)
    IfActionButtonParam(1, action_button_id=7100, entity=2201220)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, anchor_entity=2201220, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12200120)
def Event_12200120():
    """Event 12200120"""
    IfFlagEnabled(1, 12200125)
    IfFlagDisabled(2, 12200125)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    EndOfAnimation(obj=2201210, animation_id=0)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2201210, animation_id=4)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=12200121)
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- 2 --- #
    DefineLabel(2)


@NeverRestart(12200121)
def Event_12200121():
    """Event 12200121"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    IfCharacterInsideRegion(0, PLAYER, region=2202010)
    CreatePlayLog(name=186)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)


@NeverRestart(12200122)
def Event_12200122():
    """Event 12200122"""
    IfFlagDisabled(3, 12200125)
    IfFlagEnabled(3, 12200126)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagDisabled(1, 12200125)
    IfFlagDisabled(1, 12200126)
    IfCharacterInsideRegion(1, PLAYER, region=2202000)
    IfFlagDisabled(2, 12200125)
    IfFlagDisabled(2, 12200126)
    IfObjectActivated(2, obj_act_id=12200128)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12200126)
    ForceAnimation(2201210, 1)
    WaitFrames(frames=15)
    ForceAnimation(2201210, 2)
    WaitFrames(frames=150)
    IfAllPlayersOutsideRegion(0, region=2202001)
    ForceAnimation(2201210, 3)
    WaitFrames(frames=30)
    EnableFlag(12200125)
    DisableFlag(12200126)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    Restart()


@NeverRestart(12200123)
def Event_12200123():
    """Event 12200123"""
    IfFlagEnabled(3, 12200125)
    IfFlagEnabled(3, 12200126)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(1, 12200125)
    IfFlagDisabled(1, 12200126)
    IfCharacterInsideRegion(1, PLAYER, region=2202001)
    IfFlagEnabled(2, 12200125)
    IfFlagDisabled(2, 12200126)
    IfObjectActivated(2, obj_act_id=12200127)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12200126)
    ForceAnimation(2201210, 5)
    WaitFrames(frames=15)
    ForceAnimation(2201210, 6)
    WaitFrames(frames=150)
    IfAllPlayersOutsideRegion(0, region=2202000)
    ForceAnimation(2201210, 7)
    WaitFrames(frames=30)
    DisableFlag(12200125)
    DisableFlag(12200126)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Restart()


@NeverRestart(12200124)
def Event_12200124():
    """Event 12200124"""
    DisableNetworkSync()
    IfFlagDisabled(1, 12200121)
    IfActionButtonParam(1, action_button_id=7100, entity=2201200)
    IfFlagDisabled(2, 12200121)
    IfActionButtonParam(2, action_button_id=7100, entity=2201201)
    IfFlagDisabled(3, 12200126)
    IfFlagDisabled(3, 12200125)
    IfActionButtonParam(3, action_button_id=7100, entity=2201200)
    IfFlagDisabled(4, 12200126)
    IfFlagEnabled(4, 12200125)
    IfActionButtonParam(4, action_button_id=7100, entity=2201201)
    IfFlagEnabled(5, 12200126)
    IfActionButtonParam(5, action_button_id=7100, entity=2201200)
    IfFlagEnabled(6, 12200126)
    IfActionButtonParam(6, action_button_id=7100, entity=2201201)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@RestartOnRest(12200130)
def Event_12200130():
    """Event 12200130"""
    DisableCharacter(2201310)
    DisableObject(2201300)
    DisableHealthBar(2201310)
    EndIfFlagEnabled(12507810)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfPlayerHasGood(1, 4003)
    IfFlagEnabled(1, 12201800)
    IfCharacterInsideRegion(1, PLAYER, region=2202410)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(22000030, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12204020)

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(2201310)
    EnableObject(2201300)
    DisableHealthBar(2201310)


@RestartOnRest(12200131)
def Event_12200131():
    """Event 12200131"""
    EndIfFlagEnabled(12507810)
    IfFlagEnabled(1, 12200130)
    IfCharacterAlive(1, 2201310)
    IfActionButtonParam(1, action_button_id=2200010, entity=2201300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(22000040, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    WarpPlayerToRespawnPoint(2502959)


@RestartOnRest(12200132)
def Event_12200132():
    """Event 12200132"""
    EndIfFlagEnabled(12507810)
    IfHealthLessThanOrEqual(0, 2201310, value=0.0)
    StopEvent(event_id=12200131)


@RestartOnRest(12200150)
def Event_12200150(_, character: int, destination: int):
    """Event 12200150"""
    EndIfFlagEnabled(12200130)
    IfFlagEnabled(0, 12204020)
    IfCharacterInsideRegion(1, character, region=2202640)
    EndIfConditionFalse(1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=0)


@RestartOnRest(12200210)
def Event_12200210(_, obj: int, radius: float, frames: int, region: int, animation_id: int):
    """Event 12200210"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObject(obj)
    End()
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfEntityWithinDistance(-1, entity=obj, other_entity=PLAYER, radius=radius)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=frames)
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@RestartOnRest(12200220)
def Event_12200220(_, character: int, flag: int):
    """Event 12200220"""
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


@NeverRestart(12200300)
def Event_12200300():
    """Event 12200300"""
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2206000)
    DisableMapPiece(map_piece_id=2206001)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2206000)
    EnableMapPiece(map_piece_id=2206001)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableMapPiece(map_piece_id=2206000)
    EnableMapPiece(map_piece_id=2206001)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9800)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9801)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(12200310)
def Event_12200310(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12200310"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12204000)
def Event_12204000(_, character: int, radius: float):
    """Event 12204000"""
    GotoIfFlagEnabled(Label.L0, flag=12204011)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    IfFlagEnabled(-1, 9801)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterHuman(1, PLAYER)
    IfThisEventSlotFlagEnabled(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableCharacter(character)
    ForceAnimation(character, 6200)


@RestartOnRest(12204010)
def Event_12204010():
    """Event 12204010"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountGreaterThanOrEqual(2, value=15)
    EndIfConditionFalse(2)
    EnableFlag(12204011)


@RestartOnRest(12205000)
def Event_12205000():
    """Event 12205000"""
    EndIfFlagEnabled(12205001)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2202061)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12205001)
    EnableAI(2200120)
    SetNest(2200120, region=2202360)
    AICommand(2200120, command_id=10, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205001)
def Event_12205001():
    """Event 12205001"""
    EndIfFlagEnabled(12205000)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202062)
    IfCharacterInsideRegion(-2, PLAYER, region=2202060)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, entity=PLAYER, other_entity=2200120, radius=10.0)
    IfAttacked(-3, attacked_entity=2200120, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12205000)
    EnableAI(2200120)


@RestartOnRest(12205002)
def Event_12205002():
    """Event 12205002"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, 2200120, region=2202360)
    IfHasAIStatus(1, 2200120, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2200120, 3006)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200120, command_id=-1, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205003)
def Event_12205003():
    """Event 12205003"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2200120, radius=4.0)
    IfConditionTrue(-2, input_condition=1)
    IfAttackedWithDamageType(-2, attacked_entity=2200120)
    IfHasAIStatus(-2, 2200120, ai_status=AIStatusType.Battle)
    IfFlagEnabled(-2, 12205002)
    IfConditionTrue(0, input_condition=-2)
    AICommand(2200120, command_id=-1, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205010)
def Event_12205010(_, character: int, character_1: int, region: int, region_1: int, region_2: int, flag: int):
    """Event 12205010"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character_1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, entity=character_1, other_entity=PLAYER, radius=7.0)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=region_2)
    IfAttackedWithDamageType(4, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(character_1)
    SetNest(character_1, region=region_1)
    AICommand(character_1, command_id=20, command_slot=0)
    ReplanAI(character_1)


@RestartOnRest(12205015)
def Event_12205015(_, character: int, region: int, command_id: int, flag: int):
    """Event 12205015"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, flag)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=7.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, character, region=region)
    IfAttackedWithDamageType(-2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205040)
def Event_12205040():
    """Event 12205040"""
    EndIfFlagEnabled(12205041)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfHasAIStatus(2, 2200212, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, 2200212)
    IfHasAIStatus(3, 2200303, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, 2200303)
    IfHasAIStatus(4, 2200300, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, 2200300)
    IfHasAIStatus(5, 2200100, ai_status=AIStatusType.Battle)
    IfCharacterAlive(5, 2200100)
    IfHasAIStatus(6, 2200213, ai_status=AIStatusType.Battle)
    IfCharacterAlive(6, 2200213)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=2202320)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect(2200211, 5000)
    ChangePatrolBehavior(2200211, patrol_information_id=2203030)
    ReplanAI(2200211)


@RestartOnRest(12205041)
def Event_12205041():
    """Event 12205041"""
    EndIfThisEventFlagEnabled()
    IfHasAIStatus(-1, 2200211, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, 2200211, region=2202320)
    IfConditionTrue(0, input_condition=-1)
    IfHasAIStatus(0, 2200211, ai_status=AIStatusType.Normal)
    CancelSpecialEffect(2200211, 5000)
    ChangePatrolBehavior(2200211, patrol_information_id=2203031)
    ReplanAI(2200211)


@RestartOnRest(12205020)
def Event_12205020():
    """Event 12205020"""
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(2200140, 7004, loop=True)
    SetAIParamID(2200140, ai_param_id=261091)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionFalse(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=2202080)
    IfHasAIStatus(2, 2200140, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(2, entity=2200140, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2200140, ai_param_id=261003)
    ForceAnimation(2200140, 7005)


@RestartOnRest(12205030)
def Event_12205030():
    """Event 12205030"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, PLAYER, region=2202090)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2200150, radius=10.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2200150, region=2202390)
    AICommand(2200150, command_id=10, command_slot=0)
    ReplanAI(2200150)


@RestartOnRest(12205031)
def Event_12205031():
    """Event 12205031"""
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(1, 2200150, region=2202390)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2200150, radius=3.5)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    ResetAnimation(2200150)
    RotateToFaceEntity(2200150, PLAYER, animation=3001)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200150, command_id=-1, command_slot=0)
    ReplanAI(2200150)


@RestartOnRest(12205050)
def Event_12205050():
    """Event 12205050"""
    EndIfFlagEnabled(12205051)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200280)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=2200280, other_entity=PLAYER, radius=3.0)
    IfAttackedWithDamageType(2, attacked_entity=2200280)
    IfHasAIStatus(3, 2200270, ai_status=AIStatusType.Battle)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2200280)
    EndIfFinishedConditionFalse(input_condition=3)
    Wait(5.0)
    SetNest(2200280, region=2209005)
    AICommand(2200280, command_id=10, command_slot=0)
    ReplanAI(2200280)


@RestartOnRest(12205051)
def Event_12205051():
    """Event 12205051"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=2200280, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, 2200280, region=2209005)
    IfAttackedWithDamageType(-2, attacked_entity=2200280)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200280, command_id=-1, command_slot=0)
    ReplanAI(2200280)


@RestartOnRest(12205060)
def Event_12205060():
    """Event 12205060"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200170)
    DisableGravity(2200170)
    EnableInvincibility(2200170)
    IfObjectDestroyed(-1, 2201030)
    IfObjectDestroyed(-1, 2201031)
    IfObjectDestroyed(-1, 2201032)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    DisableInvincibility(2200170)
    EnableGravity(2200170)
    EnableAI(2200170)
    ReplanAI(2200170)


@RestartOnRest(12205070)
def Event_12205070():
    """Event 12205070"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200411)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=2200411, other_entity=100000, radius=10.0)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, 2200160, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, 2200161, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2200411)
    ReplanAI(2200411)


@RestartOnRest(12205080)
def Event_12205080():
    """Event 12205080"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200205)
    IfCharacterInsideRegion(1, PLAYER, region=2202155)
    IfCharacterInsideRegion(2, PLAYER, region=2202156)
    IfAttacked(3, attacked_entity=2200205, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2200205, PLAYER, animation=3012)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(frames=35)
    EnableAI(2200205)


@RestartOnRest(12205100)
def Event_12205100(_, character: int, region: int, radius: float, flag: int, command_id: int):
    """Event 12205100"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetCharacterEventTarget(character, region=PLAYER)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205105)
def Event_12205105(_, character: int, region: int, animation: int, radius: float):
    """Event 12205105"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterOutsideRegion(2, character, region=region)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- 1 --- #
    DefineLabel(1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205110)
def Event_12205110(_, character: int, region: int, radius: float, animation: int):
    """Event 12205110"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableAI(character)
    End()
    EnableAI(character)


@RestartOnRest(12205120)
def Event_12205120(_, character: int, region: int, radius: float, region_1: int):
    """Event 12205120"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_1)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttacked(2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(character)


@RestartOnRest(12205150)
def Event_12205150(_, character: int, animation_id: int, animation_id_1: int, radius: float):
    """Event 12205150"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, animation_id, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=radius)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(character, animation_id_1)
    ReplanAI(character)


@RestartOnRest(12205160)
def Event_12205160(_, region: int, obj: int, character: int, region_1: int):
    """Event 12205160"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfObjectNotDestroyed(1, obj)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(character, region=region_1)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12205170)
def Event_12205170(_, obj__projectile_id: int, owner_entity: int):
    """Event 12205170"""
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    PostDestruction(obj__projectile_id)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, obj__projectile_id, ComparisonType.LessThanOrEqual, value=999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6071,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(12205200)
def Event_12205200(_, character: int):
    """Event 12205200"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=2202100)
    IfCharacterInsideRegion(-2, PLAYER, region=2202101)
    IfCharacterInsideRegion(-2, PLAYER, region=2202102)
    IfCharacterInsideRegion(-2, PLAYER, region=2202103)
    IfCharacterInsideRegion(-2, PLAYER, region=2202104)
    IfCharacterInsideRegion(-2, PLAYER, region=2202105)
    IfCharacterInsideRegion(-2, PLAYER, region=2202106)
    IfCharacterInsideRegion(-2, PLAYER, region=2202107)
    IfCharacterInsideRegion(-2, PLAYER, region=2202108)
    IfCharacterInsideRegion(-2, PLAYER, region=2202109)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=100, command_slot=0)
    IfAllPlayersOutsideRegion(2, region=2202100)
    IfAllPlayersOutsideRegion(2, region=2202101)
    IfAllPlayersOutsideRegion(2, region=2202102)
    IfAllPlayersOutsideRegion(2, region=2202103)
    IfAllPlayersOutsideRegion(2, region=2202104)
    IfAllPlayersOutsideRegion(2, region=2202105)
    IfAllPlayersOutsideRegion(2, region=2202106)
    IfAllPlayersOutsideRegion(2, region=2202107)
    IfAllPlayersOutsideRegion(2, region=2202108)
    IfAllPlayersOutsideRegion(2, region=2202109)
    IfConditionTrue(0, input_condition=2)
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12205210)
def Event_12205210(_, character: int):
    """Event 12205210"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 9003, loop=True)
    SetAIParamID(character, ai_param_id=117007)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(2, character, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(2, entity=character, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfAttacked(3, attacked_entity=character, attacker=PLAYER)
    IfCharacterDead(4, 2200230)
    IfCharacterDead(4, 2200231)
    IfCharacterDead(4, 2200203)
    IfCharacterDead(5, 2200230)
    IfCharacterDead(5, 2200231)
    IfCharacterDead(5, 2200232)
    IfCharacterDead(6, 2200230)
    IfCharacterDead(6, 2200203)
    IfCharacterDead(6, 2200232)
    IfCharacterDead(7, 2200231)
    IfCharacterDead(7, 2200203)
    IfCharacterDead(7, 2200232)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(8, input_condition=1)
    IfEntityWithinDistance(8, entity=character, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(8, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(character, ai_param_id=117000)
    ForceAnimation(character, 9060)


@RestartOnRest(12205220)
def Event_12205220(_, character: int, region: int, animation_id: int, region_1: int):
    """Event 12205220"""
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


@RestartOnRest(12205230)
def Event_12205230(_, character: int, ai_param_id: int):
    """Event 12205230"""
    SetAIParamID(character, ai_param_id=114097)
    ReplanAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202620)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=10.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ReplanAI(character)
    IfAllPlayersOutsideRegion(1, region=2202620)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    Restart()


@RestartOnRest(12205240)
def Event_12205240(_, character: int):
    """Event 12205240"""
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(character)
    GotoIfFlagDisabled(Label.L0, flag=12200110)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202250)
    IfCharacterInsideRegion(-2, PLAYER, region=2202251)
    IfCharacterInsideRegion(-2, PLAYER, region=2202252)
    IfCharacterInsideRegion(-2, PLAYER, region=2202253)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, entity=PLAYER, other_entity=character, radius=5.0)
    IfAttacked(-3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterWhitePhantom(-4, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(-5, PLAYER, region=2202250)
    IfCharacterInsideRegion(-5, PLAYER, region=2202251)
    IfCharacterInsideRegion(-5, PLAYER, region=2202253)
    IfConditionTrue(2, input_condition=-5)
    IfConditionTrue(-6, input_condition=2)
    IfEntityWithinDistance(-6, entity=PLAYER, other_entity=character, radius=5.0)
    IfAttacked(-6, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-5)

    # --- 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(12205250)
def Event_12205250(_, character: int, region: int, character_1: int, region_1: int):
    """Event 12205250"""
    IfCharacterAlive(1, character_1)
    IfCharacterInsideRegion(1, character, region=region)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=30, command_slot=0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=character, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(-2, input_condition=2)
    IfCharacterInsideRegion(-2, character_1, region=region_1)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(0, input_condition=-2)
    AICommand(character, command_id=-1, command_slot=0)
    IfCharacterOutsideRegion(0, character, region=region)
    Restart()


@RestartOnRest(12205260)
def Event_12205260(_, character: int, region: int, flag: int, flag_1: int):
    """Event 12205260"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_1)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    AddSpecialEffect(character, 5000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=character, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(-3, attacked_entity=character)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(character)


@RestartOnRest(12205265)
def Event_12205265(_, character: int, region: int, region_1: int, event_id: int, event_id_1: int):
    """Event 12205265"""
    EndIfFlagEnabled(event_id)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfCharacterInsideRegion(-2, character, region=region_1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(event_id=event_id)
    StopEvent(event_id=event_id_1)
    ResetAnimation(character)
    ForceAnimation(character, 3000)


@RestartOnRest(12205270)
def Event_12205270(_, character: int, region: int, flag: int, region_1: int, region_2: int, event_id: int):
    """Event 12205270"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, character, region=region_2)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(event_id=event_id)
    EnableAI(character)
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205300)
def Event_12205300(_, sound_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12205300"""
    DisableSoundEvent(sound_id=sound_id)
    DeleteVFX(2203040, erase_root_only=False)
    EndIfFlagEnabled(flag_2)
    CreateVFX(2203040)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=sound_id)
    IfFlagEnabled(-1, flag)
    IfFlagEnabled(-1, flag_1)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(sound_id=sound_id)
    Restart()


@NeverRestart(12200990)
def Event_12200990():
    """Event 12200990"""
    EndIfThisEventFlagEnabled()
    IfStandingOnCollision(0, 2203500)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=214,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=214,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=214,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=214,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
