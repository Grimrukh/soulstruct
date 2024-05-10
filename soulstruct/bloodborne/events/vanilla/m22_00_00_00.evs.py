"""
Hemwick Charnel Lane

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


@ContinueOnRest(0)
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
    RunEvent(9220, slot=0, args=(2200710, 12204220, 12204221, 2200, 22))
    RunEvent(9240, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22))
    RunEvent(9260, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22))
    RunEvent(9280, slot=0, args=(2200710, 12204220, 12204221, 2200, 12204800, 22))
    CreateObjectVFX(2201000, vfx_id=750, dummy_id=900110)
    CreateObjectVFX(2201003, vfx_id=750, dummy_id=900110)
    CreateObjectVFX(2201004, vfx_id=750, dummy_id=900110)
    CreateHazard(
        obj_flag=12200050,
        obj=2201000,
        dummy_id=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12200051,
        obj=2201003,
        dummy_id=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12200052,
        obj=2201004,
        dummy_id=100,
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
        flag_2=12204848,
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
        flag_2=12204849,
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
    Event_12200210(0, obj=2201010, radius=7.0, frames=0, region=2202020, animation_id=10)
    Event_12200210(1, obj=2201011, radius=7.0, frames=30, region=2202020, animation_id=10)
    Event_12200210(2, obj=2201016, radius=7.0, frames=15, region=2202020, animation_id=10)
    Event_12200210(3, obj=2201017, radius=7.0, frames=0, region=2202020, animation_id=10)
    Event_12200210(4, obj=2201018, radius=7.0, frames=5, region=2202020, animation_id=10)
    Event_12200210(5, obj=2201012, radius=10.0, frames=10, region=2202021, animation_id=11)
    Event_12200210(6, obj=2201013, radius=10.0, frames=0, region=2202021, animation_id=11)
    Event_12200210(7, obj=2201014, radius=10.0, frames=30, region=2202021, animation_id=11)
    Event_12200210(8, obj=2201015, radius=10.0, frames=0, region=2202021, animation_id=11)
    Event_12200220(0, character=2200111, flag=52200990)
    Event_12200220(1, character=2200170, flag=52200980)
    Event_12200220(2, character=2200110, flag=52200970)
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6631):
        EnableFlag(12201999)
    if FlagDisabled(12201999):
        EnableObject(2201150)
        DisableObject(2201151)
        EnableTreasure(obj=2201150)
        DisableTreasure(obj=2201151)
    else:
        DisableObject(2201150)
        EnableObject(2201151)
        DisableTreasure(obj=2201150)
        EnableTreasure(obj=2201151)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6309):
        EnableFlag(12201998)
    if FlagDisabled(12201998):
        EnableObject(2201500)
        DisableObject(2201501)
        EnableTreasure(obj=2201500)
        DisableTreasure(obj=2201501)
    else:
        DisableObject(2201500)
        EnableObject(2201501)
        DisableTreasure(obj=2201500)
        EnableTreasure(obj=2201501)
    Event_12200990()
    Event_12204000(0, character=2200500, radius=20.0)
    Event_12204000(1, character=2200501, radius=20.0)
    Event_12204000(2, character=2200502, radius=20.0)
    Event_12204000(3, character=2200503, radius=20.0)
    Event_12204000(4, character=2200504, radius=20.0)
    Event_12204000(5, character=2200505, radius=20.0)
    Event_12204000(6, character=2200506, radius=20.0)
    Event_12204000(7, character=2200507, radius=20.0)
    Event_12204000(8, character=2200508, radius=20.0)
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
        flag=12205015,
    )
    Event_12205010(
        1,
        character=2200223,
        character_1=2200310,
        region=2202071,
        region_1=2202371,
        region_2=2202171,
        flag=12205016,
    )
    Event_12205015(0, character=2200130, region=2202370, command_id=-1, flag=12205010)
    Event_12205015(1, character=2200310, region=2202371, command_id=200, flag=12205011)
    Event_12205100(0, character=2200202, region=2202130, radius=3.0, flag=12205105, command_id=50)
    Event_12205100(1, character=2200200, region=2202150, radius=3.0, flag=12205106, command_id=50)
    Event_12205100(2, character=2200201, region=2202151, radius=3.0, flag=12205107, command_id=60)
    Event_12205100(3, character=2200204, region=2202152, radius=5.0, flag=12205108, command_id=50)
    Event_12205105(0, character=2200202, region=2202130, animation=3007, radius=3.0)
    Event_12205105(1, character=2200200, region=2202150, animation=3009, radius=2.5)
    Event_12205105(2, character=2200201, region=2202154, animation=3022, radius=2.0)
    Event_12205105(3, character=2200204, region=2202153, animation=3011, radius=2.700000047683716)
    Event_12205110(0, character=2200203, region=2202140, radius=3.0, animation=3006)
    Event_12205120(0, character=2200211, region=2202160, radius=5.0, region_1=2202161)
    Event_12205120(1, character=2200212, region=2202160, radius=5.0, region_1=2202161)
    Event_12205120(2, character=2200213, region=2202160, radius=5.0, region_1=2202161)
    Event_12205120(3, character=2200223, region=2202170, radius=15.0, region_1=2202171)
    Event_12205120(4, character=2200224, region=2202170, radius=15.0, region_1=2202171)
    Event_12205120(5, character=2200230, region=2202180, radius=6.0, region_1=2202180)
    Event_12205120(6, character=2200231, region=2202180, radius=6.0, region_1=2202180)
    Event_12205120(7, character=2200232, region=2202180, radius=6.0, region_1=2202180)
    Event_12205120(8, character=2200240, region=2202190, radius=15.0, region_1=2202191)
    Event_12205120(9, character=2200250, region=2202200, radius=10.0, region_1=2202201)
    Event_12205120(10, character=2200251, region=2202200, radius=10.0, region_1=2202201)
    Event_12205120(11, character=2200252, region=2202200, radius=10.0, region_1=2202201)
    Event_12205120(12, character=2200260, region=2202200, radius=10.0, region_1=2202201)
    Event_12205120(13, character=2200261, region=2202200, radius=10.0, region_1=2202201)
    Event_12205120(14, character=2200270, region=2202220, radius=10.0, region_1=2202221)
    Event_12205120(15, character=2200271, region=2202220, radius=10.0, region_1=2202221)
    Event_12205120(16, character=2200272, region=2202220, radius=10.0, region_1=2202221)
    Event_12205120(17, character=2200290, region=2202230, radius=8.0, region_1=2202231)
    Event_12205120(18, character=2200291, region=2202230, radius=8.0, region_1=2202231)
    Event_12205120(19, character=2200292, region=2202230, radius=8.0, region_1=2202231)
    Event_12205120(20, character=2200280, region=2202240, radius=5.0, region_1=2202240)
    Event_12205120(21, character=2200412, region=2202260, radius=5.0, region_1=2202260)
    Event_12205120(22, character=2200310, region=2202170, radius=15.0, region_1=2202171)
    Event_12205120(23, character=2200450, region=2202270, radius=15.0, region_1=2202271)
    Event_12205120(24, character=2200460, region=2202310, radius=15.0, region_1=2202310)
    Event_12205120(25, character=2200470, region=2202430, radius=3.0, region_1=2202431)
    Event_12205120(26, character=2200430, region=2202170, radius=7.0, region_1=2202171)
    Event_12205150(0, character=2200100, animation_id=7014, animation_id_1=0, radius=0.0)
    Event_12205150(1, character=2200301, animation_id=7010, animation_id_1=7011, radius=7.0)
    Event_12205150(2, character=2200303, animation_id=7012, animation_id_1=7013, radius=0.0)
    Event_12205150(3, character=2200300, animation_id=7014, animation_id_1=0, radius=0.0)
    Event_12205150(4, character=2200212, animation_id=7014, animation_id_1=0, radius=0.0)
    Event_12205160(0, region=2202040, obj=2201401, character=2200410, entity=2200400)
    Event_12205160(1, region=2202041, obj=2201406, character=2200411, entity=2200401)
    Event_12205170(0, obj=2201400, owner_entity=2200420)
    Event_12205170(1, obj=2201401, owner_entity=2200420)
    Event_12205170(2, obj=2201402, owner_entity=2200420)
    Event_12205170(3, obj=2201403, owner_entity=2200420)
    Event_12205170(4, obj=2201404, owner_entity=2200420)
    Event_12205170(5, obj=2201405, owner_entity=2200420)
    Event_12205170(6, obj=2201406, owner_entity=2200420)
    Event_12205170(7, obj=2201407, owner_entity=2200422)
    Event_12205170(8, obj=2201408, owner_entity=2200422)
    Event_12205170(9, obj=2201409, owner_entity=2200422)
    Event_12205170(10, obj=2201410, owner_entity=2200421)
    Event_12205170(11, obj=2201411, owner_entity=2200421)
    Event_12205170(12, obj=2201412, owner_entity=2200421)
    Event_12205170(13, obj=2201413, owner_entity=2200421)
    Event_12205170(14, obj=2201414, owner_entity=2200421)
    Event_12205170(15, obj=2201415, owner_entity=2200421)
    Event_12205170(16, obj=2201416, owner_entity=2200421)
    Event_12205170(17, obj=2201417, owner_entity=2200421)
    Event_12205170(18, obj=2201418, owner_entity=2200421)
    Event_12205170(19, obj=2201419, owner_entity=2200421)
    Event_12205170(20, obj=2201420, owner_entity=2200420)
    Event_12205170(21, obj=2201421, owner_entity=2200420)
    Event_12205170(22, obj=2201422, owner_entity=2200421)
    Event_12205170(23, obj=2201423, owner_entity=2200421)
    Event_12205170(24, obj=2201424, owner_entity=2200421)
    Event_12205170(25, obj=2201425, owner_entity=2200421)
    Event_12205170(26, obj=2201426, owner_entity=2200421)
    Event_12205170(27, obj=2201427, owner_entity=2200421)
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
        event_id=12205260,
    )
    Event_12205270(
        1,
        character=2200111,
        region=2202381,
        flag=12205266,
        region_1=2202633,
        region_2=2202382,
        event_id=12205261,
    )
    Event_12205300(0, sound_id=2203300, flag=1439, flag_1=6001, flag_2=9802)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2203950)
    DisableGravity(2203950)
    DisableCharacterCollision(2203950)
    DisableAnimations(2203951)
    DisableGravity(2203951)
    DisableCharacterCollision(2203951)
    Event_12204010()


@ContinueOnRest(12201800)
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

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(2200800))
    AND_1.Add(CharacterDead(2200801))
    
    MAIN.Await(AND_1)
    
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
    
    MAIN.Await(CharacterHuman(PLAYER))
    
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

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(12201801)
def Event_12201801():
    """Event 12201801"""
    DisableNetworkSync()
    if FlagEnabled(12201800):
        return
    AND_1.Add(FlagEnabled(12201800))
    AND_2.Add(CharacterBackreadDisabled(2200800))
    AND_2.Add(HealthRatio(2200800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_1)
    PlaySoundEffect(2202800, 0, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12201802)
def Event_12201802():
    """Event 12201802"""
    if FlagEnabled(12201800):
        return
    if ThisEventFlagEnabled():
        return
    DisableCharacter(2200800)
    AND_1.Add(FlagDisabled(12201800))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202805))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(2200800)
    Wait(0.10000000149011612)
    AND_2.Add(PlayerInsightAmount() == 0)
    AND_2.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionTrue(1, AND_2)
    ForceAnimation(2200800, 3011)
    EnableFlag(12204800)
    if FlagEnabled(9338):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9338)


@ContinueOnRest(12201803)
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(12201800))
    
    DisableSpawner(entity=2205000)
    DisableSpawner(entity=2205001)
    DisableSpawner(entity=2205002)
    Kill(2200810)
    Kill(2200811)
    Kill(2200812)


@ContinueOnRest(12201804)
def Event_12201804():
    """Event 12201804"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12204800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(2200800)
    EnableFlag(12204800)
    EnableFlag(12201802)


@ContinueOnRest(12204890)
def Event_12204890():
    """Event 12204890"""
    if FlagEnabled(12201800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12201802)
    SkipLinesIfClient(2)
    DisableObject(2201800)
    DeleteVFX(2203800, erase_root_only=False)
    DisableObject(2201801)
    DeleteVFX(2203801, erase_root_only=False)
    AND_1.Add(FlagDisabled(12201800))
    AND_1.Add(FlagEnabled(12201802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2201800)
    EnableObject(2201801)
    CreateVFX(2203800)
    CreateVFX(2203801)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2200800, entity=2201800))
    AND_2.Add(FlagDisabled(12201800))
    AND_3.Add(FlagEnabled(12201800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2202801))
    AND_5.Add(TimeElapsed(seconds=2.0))
    AND_5.Add(CharacterHuman(PLAYER))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_5)
    EnableFlag(12204800)
    Restart()


@ContinueOnRest(12204891)
def Event_12204891():
    """Event 12204891"""
    DisableNetworkSync()
    if FlagEnabled(12201800):
        return
    AND_1.Add(FlagDisabled(12201800))
    AND_1.Add(FlagEnabled(12201802))
    AND_1.Add(FlagEnabled(12204800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2200800, entity=2201800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2202801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    EnableFlag(12204801)
    Restart()


@ContinueOnRest(12204892)
def Event_12204892():
    """Event 12204892"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2201800, radius=2.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12204893)
def Event_12204893():
    """Event 12204893"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2201800, radius=2.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2201800, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12204802)
def Event_12204802():
    """Event 12204802"""
    if FlagEnabled(12201800):
        return
    DisableAI(2200800)
    DisableHealthBar(2200800)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(12204800))
    
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200800, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12204800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200800)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200800)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2200800)
    EnableBossHealthBar(2200800, name=210000)
    CreatePlayLog(name=88)
    StartPlayLogMeasurement(measurement_id=2200010, name=104, overwrite=True)


@ContinueOnRest(12204803)
def Event_12204803():
    """Event 12204803"""
    DisableNetworkSync()
    if FlagEnabled(12201800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2203802)
    DisableSoundEvent(sound_id=2203803)
    AND_1.Add(FlagDisabled(12201800))
    AND_1.Add(FlagEnabled(12204802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12204801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202801))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2203802)
    OR_1.Add(HealthValue(2200800) == 1)
    OR_1.Add(HealthValue(2200801) == 1)
    AND_2.Add(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12201800))
    AND_2.Add(FlagEnabled(12204802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12204801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2202801))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2203802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2203803)


@ContinueOnRest(12204804)
def Event_12204804():
    """Event 12204804"""
    if FlagEnabled(12201800):
        return
    DisableNetworkSync()
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12204800))
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(FlagEnabled(12204801))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=1)


@ContinueOnRest(12204805)
def Event_12204805():
    """Event 12204805"""
    DisableNetworkSync()
    if FlagEnabled(12201800):
        return
    
    MAIN.Await(FlagEnabled(12201800))
    
    DisableBossMusic(sound_id=2203802)
    DisableBossMusic(sound_id=2203803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12204807)
def Event_12204807():
    """Event 12204807"""
    if FlagEnabled(12201800):
        return
    OR_1.Add(HealthValue(2200800) == 1)
    OR_1.Add(HealthValue(2200801) == 1)
    
    MAIN.Await(OR_1)
    
    AICommand(2200800, command_id=100, command_slot=0)
    AICommand(2200801, command_id=100, command_slot=0)
    Wait(10.0)
    AND_1.Add(CharacterDead(2200800))
    AND_1.Add(CharacterDead(2200801))
    if AND_1:
        return
    EnableBossHealthBar(2200801, name=210000, bar_slot=1)


@ContinueOnRest(12204808)
def Event_12204808(_, character: int, flag: int):
    """Event 12204808"""
    if FlagEnabled(12201800):
        return
    DisableNetworkSync()
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=12.0))
    AND_3.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    OR_1.Add(AND_1)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect_WithUnknownEffect(character, 5686)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=6.0))
    AND_2.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect_WithUnknownEffect(character, 5688)
    Restart()


@ContinueOnRest(12204810)
def Event_12204810():
    """Event 12204810"""
    if FlagEnabled(12201800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200801)
    DisableHealthBar(2200801)
    DisableCharacter(2200801)
    
    MAIN.Await(HealthRatio(2200800) <= 0.5)
    
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200801, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200801, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200801)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200801, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2200801)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(2200801)
    EnableAI(2200801)


@ContinueOnRest(12204811)
def Event_12204811():
    """Event 12204811"""
    if FlagEnabled(12201800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    SetAIParamID(2200800, ai_param_id=210021)
    OR_1.Add(CharacterDead(2200810))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2200800))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(2200800, ai_param_id=210020)


@ContinueOnRest(12204812)
def Event_12204812(_, character: int, character_1: int, destination: int, flag: int):
    """Event 12204812"""
    if FlagEnabled(12201800):
        return
    EnableImmortality(character)
    AND_3.Add(HealthValue(character) == 1)
    AND_3.Add(HealthValue(character_1) < 1)
    AND_4.Add(HealthValue(character) == 1)
    AND_4.Add(HealthValue(character_1) == 1)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_4)
    Wait(0.0)
    ResetAnimation(character)
    Wait(0.10000000149011612)
    ForceAnimation(character, 7000)
    WaitFrames(frames=75)
    ForceAnimation(character, 7001, loop=True)
    AND_1.Add(TimeElapsed(seconds=45.0))
    AND_2.Add(HealthValue(character_1) == 1)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_2)
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

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)
    Kill(character_1)


@ContinueOnRest(12204814)
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
    if FlagEnabled(12201800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=30))
    
    AddSpecialEffect(character, 5686)
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_1.Add(HealthValue(character) != 1)
    
    MAIN.Await(AND_1)
    
    GotoIfClient(Label.L0)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfFlagDisabled(Label.L1, flag=first_flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(first_flag_1)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=flag)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(flag)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, flag=flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(flag_1)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L0, flag=last_flag_1)
    DisableFlagRange((first_flag_1, last_flag_1))
    EnableFlag(last_flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(first_flag_1))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(last_flag_1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_2)
    Restart()


@ContinueOnRest(12204820)
def Event_12204820(_, character: int, flag: int, region: int, destination: int, flag_1: int):
    """Event 12204820"""
    if FlagEnabled(12201800):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    AND_1.Add(CharacterInsideRegion(character, region=region))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)
    Restart()


@ContinueOnRest(12204830)
def Event_12204830(_, character: int, flag: int, flag_1: int):
    """Event 12204830"""
    if FlagEnabled(12201800):
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(2.0)
    EnableCharacter(character)
    ReplanAI(character)
    DisableFlag(flag_1)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12204832)
def Event_12204832(_, character: int):
    """Event 12204832"""
    if FlagEnabled(12201800):
        return
    
    MAIN.Await(CharacterDead(character))
    
    IncrementEventValue(12204860, bit_count=10, max_value=10)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=10))
    
    Restart()


@ContinueOnRest(12204835)
def Event_12204835(_, character: int, flag: int):
    """Event 12204835"""
    if FlagEnabled(12201800):
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableFlag(flag)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=10))
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12204838)
def Event_12204838():
    """Event 12204838"""
    if FlagEnabled(12201800):
        return
    AND_4.Add(FlagDisabled(12204845))
    
    MAIN.Await(AND_4)
    
    OR_1.Add(CharacterHasTAEEvent(2200800, tae_event_id=20))
    OR_1.Add(CharacterHasTAEEvent(2200801, tae_event_id=20))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(12204870))
    OR_2.Add(CharacterHasTAEEvent(2200800, tae_event_id=20))
    OR_2.Add(CharacterHasTAEEvent(2200801, tae_event_id=20))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(12204871))
    OR_3.Add(CharacterHasTAEEvent(2200800, tae_event_id=20))
    OR_3.Add(CharacterHasTAEEvent(2200801, tae_event_id=20))
    AND_3.Add(OR_3)
    AND_3.Add(FlagEnabled(12204872))
    OR_4.Add(AND_1)
    OR_4.Add(AND_2)
    OR_4.Add(AND_3)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_1)
    EnableSpawner(entity=2205000)
    
    MAIN.Await(CharacterHasTAEEvent(2200810, tae_event_id=10))
    
    DisableSpawner(entity=2205000)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_2)
    EnableSpawner(entity=2205001)
    
    MAIN.Await(CharacterHasTAEEvent(2200811, tae_event_id=10))
    
    DisableSpawner(entity=2205001)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableSpawner(entity=2205002)
    
    MAIN.Await(CharacterHasTAEEvent(2200812, tae_event_id=10))
    
    DisableSpawner(entity=2205002)
    Restart()


@RestartOnRest(12204839)
def Event_12204839():
    """Event 12204839"""
    if FlagEnabled(12201800):
        return
    AND_1.Add(FlagDisabled(12204845))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(HealthValue(2200800) == 1)
    OR_1.Add(HealthValue(2200801) == 1)
    OR_2.Add(OR_1)
    OR_2.Add(FlagEnabled(12204812))
    AND_2.Add(FlagEnabled(12201802))
    AND_2.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(12201810))
    AND_3.Add(EventValue(flag=12204860, bit_count=10) == 3)
    AND_3.Add(FlagDisabled(12204875))
    AND_4.Add(HealthRatio(2200800) <= 0.30000001192092896)
    AND_4.Add(EventValue(flag=12204860, bit_count=10) <= 2)
    AND_4.Add(FlagDisabled(12204875))
    AND_5.Add(HealthRatio(2200801) <= 0.5)
    AND_5.Add(EventValue(flag=12204860, bit_count=10) <= 2)
    AND_5.Add(FlagDisabled(12204875))
    OR_3.Add(AND_3)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    AND_6.Add(EventValue(flag=12204860, bit_count=10) >= 5)
    OR_4.Add(HealthValue(2200800) == 1)
    OR_4.Add(HealthValue(2200801) == 1)
    AND_7.Add(OR_4)
    AND_7.Add(EventValue(flag=12204860, bit_count=10) <= 4)
    AND_7.Add(EventValue(flag=12204860, bit_count=10) >= 3)
    OR_5.Add(AND_6)
    OR_5.Add(AND_7)
    OR_6.Add(OR_2)
    OR_6.Add(AND_2)
    OR_6.Add(OR_3)
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_8.Add(HealthValue(2200800) == 1)
    AND_9.Add(HealthValue(2200800) != 1)
    OR_7.Add(AND_8)
    OR_7.Add(AND_9)
    GotoIfConditionTrue(Label.L2, input_condition=AND_8)
    ResetAnimation(2200800)
    Wait(0.10000000149011612)
    ForceAnimation(2200800, 3011)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    ResetAnimation(2200801)
    Wait(0.10000000149011612)
    ForceAnimation(2200801, 3011)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfLastConditionResultTrue(Label.L4, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L5, input_condition=OR_3)
    GotoIfLastConditionResultTrue(Label.L6, input_condition=OR_5)
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

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(entity=2205000)
    EnableFlag(12204876)
    EnableFlag(12201810)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(entity=2205001)
    EnableFlag(12204875)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(entity=2205002)
    End()


@RestartOnRest(12204840)
def Event_12204840():
    """Event 12204840"""
    if FlagEnabled(12201800):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_5.Add(FlagDisabled(12204845))
    
    MAIN.Await(AND_5)
    
    AND_1.Add(EventValue(flag=12204860, bit_count=10) >= 3)
    AND_2.Add(FlagEnabled(12204870))
    AND_2.Add(EventValue(flag=12204860, bit_count=10) <= 2)
    AND_5.Add(HealthValue(2200800) == 1)
    AND_5.Add(HealthValue(2200801) == 1)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_5)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_2)
    AND_3.Add(HealthValue(2200800) == 1)
    AND_4.Add(HealthValue(2200800) != 1)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_3)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200800, command_id=10, command_slot=2)
    ReplanAI(2200800)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(FlagDisabled(12204870))
    
    AICommand(2200800, command_id=-1, command_slot=2)
    ReplanAI(2200800)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12204880)


@RestartOnRest(12204841)
def Event_12204841():
    """Event 12204841"""
    if FlagEnabled(12201800):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(12204880))
    
    AND_1.Add(EventValue(flag=12204860, bit_count=10) >= 5)
    AND_2.Add(EventValue(flag=12204860, bit_count=10) <= 4)
    AND_2.Add(FlagEnabled(12204870))
    AND_3.Add(EventValue(flag=12204860, bit_count=10) <= 4)
    AND_3.Add(FlagEnabled(12204871))
    AND_6.Add(HealthValue(2200800) == 1)
    AND_6.Add(HealthValue(2200801) == 1)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_6)
    AND_4.Add(HealthValue(2200800) == 1)
    AND_5.Add(HealthValue(2200800) != 1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_4)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200800, command_id=10, command_slot=2)
    ReplanAI(2200800)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagDisabled(12204870))
    AND_4.Add(FlagDisabled(12204871))
    
    MAIN.Await(AND_4)
    
    AICommand(2200800, command_id=-1, command_slot=2)
    ReplanAI(2200800)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12204881)


@RestartOnRest(12204842)
def Event_12204842():
    """Event 12204842"""
    if FlagEnabled(12201800):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(12204881))
    
    OR_1.Add(FlagEnabled(12204870))
    OR_1.Add(FlagEnabled(12204871))
    OR_1.Add(FlagEnabled(12204872))
    
    MAIN.Await(OR_1)
    
    WaitRandomSeconds(min_seconds=15.0, max_seconds=25.0)
    AICommand(2200800, command_id=10, command_slot=2)
    AICommand(2200801, command_id=10, command_slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    AND_1.Add(FlagDisabled(12204870))
    AND_1.Add(FlagDisabled(12204871))
    AND_1.Add(FlagDisabled(12204872))
    
    MAIN.Await(AND_1)
    
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
    AND_1.Add(FlagDisabled(12201810))
    if AND_1:
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagDisabled(12204845))

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2200800, 3011)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(entity=2205000)


@RestartOnRest(12204844)
def Event_12204844():
    """Event 12204844"""
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    
    MAIN.Await(PlayerInsightAmount() <= 0)
    
    EnableFlag(12204845)
    
    MAIN.Await(PlayerInsightAmount() >= 1)
    
    DisableFlag(12204845)
    Restart()


@ContinueOnRest(12200100)
def Event_12200100():
    """Event 12200100"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201001, animation_id=1)
    DisableObjectActivation(2201001, obj_act_id=2200010)
    NotifyDoorEventSoundDampening(obj=2201001, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=12200101))
    
    CreatePlayLog(name=122)
    Wait(0.0)


@ContinueOnRest(12200101)
def Event_12200101():
    """Event 12200101"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201060, animation_id=0)
    DisableObjectActivation(2201060, obj_act_id=2200030)
    NotifyDoorEventSoundDampening(obj=2201060, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=12200500))
    
    Wait(0.0)


@ContinueOnRest(12200110)
def Event_12200110():
    """Event 12200110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=2201002, animation_id=1)
    DisableObjectActivation(2201220, obj_act_id=100)
    NotifyDoorEventSoundDampening(obj=2201002, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=12200112))
    
    CreatePlayLog(name=158)
    DisableObjectActivation(2201220, obj_act_id=100)
    ForceAnimation(2201002, 1)
    Wait(0.0)


@ContinueOnRest(12200111)
def Event_12200111():
    """Event 12200111"""
    DisableNetworkSync()
    if FlagEnabled(12200110):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=2200000, entity=2201002))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2200001, entity=2201002))
    AND_3.Add(FlagEnabled(12200110))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
    DisplayDialog(text=10010160, anchor_entity=2201002, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@ContinueOnRest(12200112)
def Event_12200112():
    """Event 12200112"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12200110))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201220))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, anchor_entity=2201220, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@ContinueOnRest(12200120)
def Event_12200120():
    """Event 12200120"""
    AND_1.Add(FlagEnabled(12200125))
    AND_2.Add(FlagDisabled(12200125))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    EndOfAnimation(obj=2201210, animation_id=0)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2201210, animation_id=4)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=12200121)
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- Label 2 --- #
    DefineLabel(2)


@ContinueOnRest(12200121)
def Event_12200121():
    """Event 12200121"""
    if ThisEventSlotFlagEnabled():
        return
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2202010))
    
    CreatePlayLog(name=186)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)


@ContinueOnRest(12200122)
def Event_12200122():
    """Event 12200122"""
    AND_3.Add(FlagDisabled(12200125))
    AND_3.Add(FlagEnabled(12200126))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagDisabled(12200125))
    AND_1.Add(FlagDisabled(12200126))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202000))
    AND_2.Add(FlagDisabled(12200125))
    AND_2.Add(FlagDisabled(12200126))
    AND_2.Add(ObjectActivated(obj_act_id=12200128))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12200126)
    ForceAnimation(2201210, 1)
    WaitFrames(frames=15)
    ForceAnimation(2201210, 2)
    WaitFrames(frames=150)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2202001))
    
    ForceAnimation(2201210, 3)
    WaitFrames(frames=30)
    EnableFlag(12200125)
    DisableFlag(12200126)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    Restart()


@ContinueOnRest(12200123)
def Event_12200123():
    """Event 12200123"""
    AND_3.Add(FlagEnabled(12200125))
    AND_3.Add(FlagEnabled(12200126))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagEnabled(12200125))
    AND_1.Add(FlagDisabled(12200126))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202001))
    AND_2.Add(FlagEnabled(12200125))
    AND_2.Add(FlagDisabled(12200126))
    AND_2.Add(ObjectActivated(obj_act_id=12200127))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12200126)
    ForceAnimation(2201210, 5)
    WaitFrames(frames=15)
    ForceAnimation(2201210, 6)
    WaitFrames(frames=150)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2202000))
    
    ForceAnimation(2201210, 7)
    WaitFrames(frames=30)
    DisableFlag(12200125)
    DisableFlag(12200126)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Restart()


@ContinueOnRest(12200124)
def Event_12200124():
    """Event 12200124"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(12200121))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201200))
    AND_2.Add(FlagDisabled(12200121))
    AND_2.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201201))
    AND_3.Add(FlagDisabled(12200126))
    AND_3.Add(FlagDisabled(12200125))
    AND_3.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201200))
    AND_4.Add(FlagDisabled(12200126))
    AND_4.Add(FlagEnabled(12200125))
    AND_4.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201201))
    AND_5.Add(FlagEnabled(12200126))
    AND_5.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201200))
    AND_6.Add(FlagEnabled(12200126))
    AND_6.Add(ActionButtonParamActivated(action_button_id=7100, entity=2201201))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@RestartOnRest(12200130)
def Event_12200130():
    """Event 12200130"""
    DisableCharacter(2201310)
    DisableObject(2201300)
    DisableHealthBar(2201310)
    if FlagEnabled(12507810):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(PlayerHasGood(4003))
    AND_1.Add(FlagEnabled(12201800))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202410))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(22000030, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12204020)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(2201310)
    EnableObject(2201300)
    DisableHealthBar(2201310)


@RestartOnRest(12200131)
def Event_12200131():
    """Event 12200131"""
    if FlagEnabled(12507810):
        return
    AND_1.Add(FlagEnabled(12200130))
    AND_1.Add(CharacterAlive(2201310))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2200010, entity=2201300))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(22000040, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    WarpPlayerToRespawnPoint(2502959)


@RestartOnRest(12200132)
def Event_12200132():
    """Event 12200132"""
    if FlagEnabled(12507810):
        return
    
    MAIN.Await(HealthRatio(2201310) <= 0.0)
    
    StopEvent(event_id=12200131)


@RestartOnRest(12200150)
def Event_12200150(_, character: int, destination: int):
    """Event 12200150"""
    if FlagEnabled(12200130):
        return
    
    MAIN.Await(FlagEnabled(12204020))
    
    AND_1.Add(CharacterInsideRegion(character, region=2202640))
    if not AND_1:
        return
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=0)


@RestartOnRest(12200210)
def Event_12200210(_, obj: int, radius: float, frames: int, region: int, animation_id: int):
    """Event 12200210"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=animation_id)
        DisableObject(obj)
        End()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=radius))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=frames)
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@RestartOnRest(12200220)
def Event_12200220(_, character: int, flag: int):
    """Event 12200220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(0.0)


@ContinueOnRest(12200300)
def Event_12200300():
    """Event 12200300"""
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2206000)
    DisableMapPiece(map_piece_id=2206001)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2206000)
    EnableMapPiece(map_piece_id=2206001)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableMapPiece(map_piece_id=2206000)
    EnableMapPiece(map_piece_id=2206001)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9800))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9801))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9802))
    
    MAIN.Await(OR_1)
    
    Restart()


@ContinueOnRest(12200310)
def Event_12200310(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12200310"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableTreasure(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12204000)
def Event_12204000(_, character: int, radius: float):
    """Event 12204000"""
    GotoIfFlagEnabled(Label.L0, flag=12204011)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    OR_1.Add(FlagEnabled(9801))
    OR_1.Add(FlagEnabled(9802))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_2.Add(ThisEventSlotFlagEnabled())
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableCharacter(character)
    ForceAnimation(character, 6200)


@RestartOnRest(12204010)
def Event_12204010():
    """Event 12204010"""
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    AND_2.Add(PlayerInsightAmount() >= 15)
    if not AND_2:
        return
    EnableFlag(12204011)


@RestartOnRest(12205000)
def Event_12205000():
    """Event 12205000"""
    if FlagEnabled(12205001):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202061))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12205001)
    EnableAI(2200120)
    SetNest(2200120, region=2202360)
    AICommand(2200120, command_id=10, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205001)
def Event_12205001():
    """Event 12205001"""
    if FlagEnabled(12205000):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202062))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202060))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2200120, radius=10.0))
    OR_3.Add(Attacked(attacked_entity=2200120, attacker=PLAYER))
    
    MAIN.Await(OR_3)

    # --- Label 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12205000)
    EnableAI(2200120)


@RestartOnRest(12205002)
def Event_12205002():
    """Event 12205002"""
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(CharacterInsideRegion(2200120, region=2202360))
    AND_1.Add(HasAIStatus(2200120, ai_status=AIStatusType.Normal))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2200120, 3006)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2200120, command_id=-1, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205003)
def Event_12205003():
    """Event 12205003"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2200120, radius=4.0))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=2200120))
    OR_2.Add(HasAIStatus(2200120, ai_status=AIStatusType.Battle))
    OR_2.Add(FlagEnabled(12205002))
    
    MAIN.Await(OR_2)
    
    AICommand(2200120, command_id=-1, command_slot=0)
    ReplanAI(2200120)


@RestartOnRest(12205010)
def Event_12205010(_, character: int, character_1: int, region: int, region_1: int, region_2: int, flag: int):
    """Event 12205010"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=7.0))
    AND_3.Add(OR_1)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=region_2))
    AND_4.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character_1)
    SetNest(character_1, region=region_1)
    AICommand(character_1, command_id=20, command_slot=0)
    ReplanAI(character_1)


@RestartOnRest(12205015)
def Event_12205015(_, character: int, region: int, command_id: int, flag: int):
    """Event 12205015"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=7.0))
    OR_2.Add(AND_1)
    OR_2.Add(CharacterInsideRegion(character, region=region))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205040)
def Event_12205040():
    """Event 12205040"""
    if FlagEnabled(12205041):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_2.Add(HasAIStatus(2200212, ai_status=AIStatusType.Battle))
    AND_2.Add(CharacterAlive(2200212))
    AND_3.Add(HasAIStatus(2200303, ai_status=AIStatusType.Battle))
    AND_3.Add(CharacterAlive(2200303))
    AND_4.Add(HasAIStatus(2200300, ai_status=AIStatusType.Battle))
    AND_4.Add(CharacterAlive(2200300))
    AND_5.Add(HasAIStatus(2200100, ai_status=AIStatusType.Battle))
    AND_5.Add(CharacterAlive(2200100))
    AND_6.Add(HasAIStatus(2200213, ai_status=AIStatusType.Battle))
    AND_6.Add(CharacterAlive(2200213))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    AND_1.Add(OR_1)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202320))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(2200211, 5000)
    ChangePatrolBehavior(2200211, patrol_information_id=2203030)
    ReplanAI(2200211)


@RestartOnRest(12205041)
def Event_12205041():
    """Event 12205041"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(HasAIStatus(2200211, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterInsideRegion(2200211, region=2202320))
    
    MAIN.Await(OR_1)
    
    MAIN.Await(HasAIStatus(2200211, ai_status=AIStatusType.Normal))
    
    RemoveSpecialEffect(2200211, 5000)
    ChangePatrolBehavior(2200211, patrol_information_id=2203031)
    ReplanAI(2200211)


@RestartOnRest(12205020)
def Event_12205020():
    """Event 12205020"""
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(2200140, 7004, loop=True)
    SetAIParamID(2200140, ai_param_id=261091)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(not OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202080))
    AND_2.Add(HasAIStatus(2200140, ai_status=AIStatusType.Search))
    AND_2.Add(EntityWithinDistance(entity=2200140, other_entity=PLAYER, radius=5.0))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(2200140, ai_param_id=261003)
    ForceAnimation(2200140, 7005)


@RestartOnRest(12205030)
def Event_12205030():
    """Event 12205030"""
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202090))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2200150, radius=10.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(2200150, region=2202390)
    AICommand(2200150, command_id=10, command_slot=0)
    ReplanAI(2200150)


@RestartOnRest(12205031)
def Event_12205031():
    """Event 12205031"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(2200150, region=2202390))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_2)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2200150, radius=3.5))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_2)
    ResetAnimation(2200150)
    RotateToFaceEntity(2200150, PLAYER, animation=3001)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2200150, command_id=-1, command_slot=0)
    ReplanAI(2200150)


@RestartOnRest(12205050)
def Event_12205050():
    """Event 12205050"""
    if FlagEnabled(12205051):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200280)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=2200280, other_entity=PLAYER, radius=3.0))
    AND_2.Add(AttackedWithDamageType(attacked_entity=2200280))
    AND_3.Add(HasAIStatus(2200270, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(2200280)
    EndIfLastConditionResultFalse(input_condition=AND_3)
    Wait(5.0)
    SetNest(2200280, region=2209005)
    AICommand(2200280, command_id=10, command_slot=0)
    ReplanAI(2200280)


@RestartOnRest(12205051)
def Event_12205051():
    """Event 12205051"""
    GotoIfThisEventFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=2200280, other_entity=PLAYER, radius=5.0))
    OR_2.Add(AND_1)
    OR_2.Add(CharacterInsideRegion(2200280, region=2209005))
    OR_2.Add(AttackedWithDamageType(attacked_entity=2200280))
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
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
    OR_1.Add(ObjectDestroyed(2201030))
    OR_1.Add(ObjectDestroyed(2201031))
    OR_1.Add(ObjectDestroyed(2201032))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
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
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=2200411, other_entity=100000, radius=10.0))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(2200160, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(2200161, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(2200411)
    ReplanAI(2200411)


@RestartOnRest(12205080)
def Event_12205080():
    """Event 12205080"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200205)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2202155))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2202156))
    AND_3.Add(Attacked(attacked_entity=2200205, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_1)
    RotateToFaceEntity(2200205, PLAYER, animation=3012)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=35)
    EnableAI(2200205)


@RestartOnRest(12205100)
def Event_12205100(_, character: int, region: int, radius: float, flag: int, command_id: int):
    """Event 12205100"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterEventTarget(character, entity=PLAYER)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205105)
def Event_12205105(_, character: int, region: int, animation: int, radius: float):
    """Event 12205105"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(CharacterOutsideRegion(character, region=region))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)
    RotateToFaceEntity(character, PLAYER, animation=animation)

    # --- Label 1 --- #
    DefineLabel(1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12205110)
def Event_12205110(_, character: int, region: int, radius: float, animation: int):
    """Event 12205110"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_1)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableAI(character)
    End()
    EnableAI(character)


@RestartOnRest(12205120)
def Event_12205120(_, character: int, region: int, radius: float, region_1: int):
    """Event 12205120"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableAI(character)


@RestartOnRest(12205150)
def Event_12205150(_, character: int, animation_id: int, animation_id_1: int, radius: float):
    """Event 12205150"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_2.Add(AND_1)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    ForceAnimation(character, animation_id_1)
    ReplanAI(character)


@RestartOnRest(12205160)
def Event_12205160(_, region: int, obj: int, character: int, entity: int):
    """Event 12205160"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(ObjectNotDestroyed(obj))
    
    MAIN.Await(AND_1)
    
    SetCharacterEventTarget(character, entity=entity)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=100))
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12205170)
def Event_12205170(_, obj: int, owner_entity: int):
    """Event 12205170"""
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    PostDestruction(obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
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
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        dummy_id=-1,
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
        owner_entity=owner_entity,
        source_entity=obj,
        dummy_id=-1,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=obj,
        dummy_id=-1,
        behavior_id=6071,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(obj)
    PlaySoundEffect(obj, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(12205200)
def Event_12205200(_, character: int):
    """Event 12205200"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202100))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202101))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202102))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202103))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202104))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202105))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202106))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202107))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202108))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202109))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=100, command_slot=0)
    AND_2.Add(AllPlayersOutsideRegion(region=2202100))
    AND_2.Add(AllPlayersOutsideRegion(region=2202101))
    AND_2.Add(AllPlayersOutsideRegion(region=2202102))
    AND_2.Add(AllPlayersOutsideRegion(region=2202103))
    AND_2.Add(AllPlayersOutsideRegion(region=2202104))
    AND_2.Add(AllPlayersOutsideRegion(region=2202105))
    AND_2.Add(AllPlayersOutsideRegion(region=2202106))
    AND_2.Add(AllPlayersOutsideRegion(region=2202107))
    AND_2.Add(AllPlayersOutsideRegion(region=2202108))
    AND_2.Add(AllPlayersOutsideRegion(region=2202109))
    
    MAIN.Await(AND_2)
    
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12205210)
def Event_12205210(_, character: int):
    """Event 12205210"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, 9003, loop=True)
    SetAIParamID(character, ai_param_id=117007)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=5.0))
    AND_2.Add(AND_1)
    AND_3.Add(AND_1)
    AND_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_4.Add(CharacterDead(2200230))
    AND_4.Add(CharacterDead(2200231))
    AND_4.Add(CharacterDead(2200203))
    AND_5.Add(CharacterDead(2200230))
    AND_5.Add(CharacterDead(2200231))
    AND_5.Add(CharacterDead(2200232))
    AND_6.Add(CharacterDead(2200230))
    AND_6.Add(CharacterDead(2200203))
    AND_6.Add(CharacterDead(2200232))
    AND_7.Add(CharacterDead(2200231))
    AND_7.Add(CharacterDead(2200203))
    AND_7.Add(CharacterDead(2200232))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    AND_8.Add(AND_1)
    AND_8.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    AND_8.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    SetAIParamID(character, ai_param_id=117000)
    ForceAnimation(character, 9060)


@RestartOnRest(12205220)
def Event_12205220(_, character: int, region: int, animation_id: int, region_1: int):
    """Event 12205220"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_3.Add(HealthRatio(character) <= 0.0)
    OR_3.Add(AND_3)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
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
    
    EndIfLastConditionResultTrue(input_condition=AND_4)
    RestartIfLastConditionResultTrue(input_condition=AND_2)
    ResetAnimation(character)
    ForceAnimation(character, 0, wait_for_completion=True)
    Restart()


@RestartOnRest(12205230)
def Event_12205230(_, character: int, ai_param_id: int):
    """Event 12205230"""
    SetAIParamID(character, ai_param_id=114097)
    ReplanAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202620))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=10.0))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    SetAIParamID(character, ai_param_id=ai_param_id)
    ReplanAI(character)
    AND_1.Add(AllPlayersOutsideRegion(region=2202620))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    MAIN.Await(AND_1)
    
    Restart()


@RestartOnRest(12205240)
def Event_12205240(_, character: int):
    """Event 12205240"""
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(character)
    GotoIfFlagDisabled(Label.L0, flag=12200110)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202250))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202251))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202252))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2202253))
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_4.Add(CharacterHuman(PLAYER))
    OR_4.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    OR_5.Add(CharacterInsideRegion(PLAYER, region=2202250))
    OR_5.Add(CharacterInsideRegion(PLAYER, region=2202251))
    OR_5.Add(CharacterInsideRegion(PLAYER, region=2202253))
    AND_2.Add(OR_5)
    OR_6.Add(AND_2)
    OR_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    OR_6.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(12205250)
def Event_12205250(_, character: int, region: int, character_1: int, region_1: int):
    """Event 12205250"""
    AND_1.Add(CharacterAlive(character_1))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=30, command_slot=0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterInsideRegion(character_1, region=region_1))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    AICommand(character, command_id=-1, command_slot=0)
    
    MAIN.Await(CharacterOutsideRegion(character, region=region))
    
    Restart()


@RestartOnRest(12205260)
def Event_12205260(_, character: int, region: int, flag: int, flag_1: int):
    """Event 12205260"""
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    AddSpecialEffect(character, 5000)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    AND_1.Add(OR_2)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)


@RestartOnRest(12205265)
def Event_12205265(_, character: int, region: int, region_1: int, event_id: int, event_id_1: int):
    """Event 12205265"""
    if FlagEnabled(event_id):
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character, region=region_1))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    StopEvent(event_id=event_id)
    StopEvent(event_id=event_id_1)
    ResetAnimation(character)
    ForceAnimation(character, 3000)


@RestartOnRest(12205270)
def Event_12205270(_, character: int, region: int, flag: int, region_1: int, region_2: int, event_id: int):
    """Event 12205270"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(AND_1)
    OR_2.Add(CharacterInsideRegion(character, region=region_2))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_2)
    
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
    if FlagEnabled(flag_2):
        return
    CreateVFX(2203040)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=sound_id)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableSoundEvent(sound_id=sound_id)
    Restart()


@ContinueOnRest(12200990)
def Event_12200990():
    """Event 12200990"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2203500))
    
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
