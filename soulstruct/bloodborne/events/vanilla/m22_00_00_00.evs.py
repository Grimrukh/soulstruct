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


def Constructor():
    """ 0: Event 0 """
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
    CreateObjectVFX(900110, obj=2201000, model_point=750)
    CreateObjectVFX(900110, obj=2201003, model_point=750)
    CreateObjectVFX(900110, obj=2201004, model_point=750)
    CreateHazard(
        12200050,
        2201000,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12200051,
        2201003,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12200052,
        2201004,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    RegisterLadder(start_climbing_flag=12200000, stop_climbing_flag=12200001, obj=2201100)
    StartPlayLogMeasurement(2200000, 0, overwrite=False)
    StartPlayLogMeasurement(2200001, 18, overwrite=True)
    CreateProjectileOwner(2200420)
    CreateProjectileOwner(2200421)
    CreateProjectileOwner(2200422)
    AICommand(2200310, command_id=200, slot=0)
    AICommand(2200311, command_id=200, slot=0)
    RunEvent(12204892)
    RunEvent(12204893)
    RunEvent(12201800)
    RunEvent(12201801)
    RunEvent(12201802)
    RunEvent(12201803)
    RunEvent(12204890)
    RunEvent(12204891)
    RunEvent(12204802)
    RunEvent(12204803)
    RunEvent(12204804)
    RunEvent(12204805)
    RunEvent(12204807)
    RunEvent(12201804)
    RunEvent(12204808, slot=0, args=(2200800, 12204848))
    RunEvent(12204808, slot=1, args=(2200801, 12204849))
    RunEvent(12204810)
    RunEvent(12204811)
    RunEvent(12204812, slot=0, args=(2200800, 2200801, 2202810, 12204848))
    RunEvent(12204812, slot=1, args=(2200801, 2200800, 2202815, 12204849))
    RunEvent(
        12204814,
        slot=0,
        args=(2200800, 12204850, 12204853, 12204850, 12204851, 12204852, 12204853, 12204848),
        arg_types="iIIiiiii",
    )
    RunEvent(
        12204814,
        slot=1,
        args=(2200801, 12204855, 12204858, 12204855, 12204856, 12204857, 12204858, 12204849),
        arg_types="iIIiiiii",
    )
    RunEvent(12204820, slot=0, args=(2200800, 12204850, 2202810, 2202812, 12204854))
    RunEvent(12204820, slot=1, args=(2200800, 12204851, 2202811, 2202810, 12204854))
    RunEvent(12204820, slot=2, args=(2200800, 12204852, 2202812, 2202817, 12204854))
    RunEvent(12204820, slot=3, args=(2200800, 12204853, 2202817, 2202811, 12204854))
    RunEvent(12204820, slot=4, args=(2200801, 12204855, 2202813, 2202814, 12204859))
    RunEvent(12204820, slot=5, args=(2200801, 12204856, 2202814, 2202815, 12204859))
    RunEvent(12204820, slot=6, args=(2200801, 12204857, 2202815, 2202816, 12204859))
    RunEvent(12204820, slot=7, args=(2200801, 12204858, 2202816, 2202813, 12204859))
    RunEvent(12204830, slot=0, args=(2200800, 12204854, 12204848))
    RunEvent(12204830, slot=1, args=(2200801, 12204859, 12204849))
    RunEvent(12204832, slot=0, args=(2200810,))
    RunEvent(12204832, slot=1, args=(2200811,))
    RunEvent(12204832, slot=2, args=(2200812,))
    RunEvent(12204835, slot=0, args=(2200810, 12204870))
    RunEvent(12204835, slot=1, args=(2200811, 12204871))
    RunEvent(12204835, slot=2, args=(2200812, 12204872))
    RunEvent(12204838)
    RunEvent(12204839)
    RunEvent(12204840)
    RunEvent(12204841)
    RunEvent(12204842)
    RunEvent(12204843)
    RunEvent(12204844)
    RunEvent(12200100)
    RunEvent(12200101)
    RunEvent(12200110)
    RunEvent(12200111)
    RunEvent(12200112)
    RunEvent(12200120)
    RunEvent(12200122)
    RunEvent(12200123)
    RunEvent(12200121)
    RunEvent(12200124)
    RunEvent(12200130)
    RunEvent(12200131)
    RunEvent(12200132)
    RunEvent(12200150, slot=0, args=(2200261, 2202660))
    RunEvent(12200150, slot=1, args=(2200250, 2202661))
    RunEvent(12200150, slot=2, args=(2200251, 2202662))
    RunEvent(12200150, slot=3, args=(2200260, 2202663))
    RunEvent(12200150, slot=4, args=(2200201, 2202664))
    RunEvent(12200150, slot=5, args=(2200205, 2202665))
    RunEvent(12200150, slot=6, args=(2200204, 2202666))
    RunEvent(12200150, slot=7, args=(2200252, 2202667))
    RunEvent(12200150, slot=8, args=(2200335, 2202668))
    RunEvent(12200150, slot=9, args=(2200330, 2202669))
    RunEvent(12200150, slot=10, args=(2200331, 2202670))
    RunEvent(12200150, slot=11, args=(2200332, 2202671))
    RunEvent(12200150, slot=12, args=(2200333, 2202672))
    RunEvent(12200150, slot=13, args=(2200334, 2202673))
    RunEvent(12200150, slot=14, args=(2200280, 2202674))
    RunEvent(12200150, slot=15, args=(2200340, 2202675))
    RunEvent(12200150, slot=16, args=(2200341, 2202676))
    RunEvent(12200150, slot=17, args=(2200273, 2202677))
    RunEvent(12200150, slot=18, args=(2200270, 2202678))
    RunEvent(12200150, slot=19, args=(2200271, 2202679))
    RunEvent(12200150, slot=20, args=(2200272, 2202680))
    RunEvent(12200150, slot=21, args=(2200202, 2202681))
    RunEvent(12200150, slot=22, args=(2200311, 2202682))
    RunEvent(12200150, slot=23, args=(2200120, 2202683))
    RunEvent(12200300)
    RunEvent(12200310, slot=0, args=(2201050, 12200900, 9942))
    RunEvent(12200210, slot=0, args=(2201010, 7.0, 0, 2202020, 10), arg_types="ifiii")
    RunEvent(12200210, slot=1, args=(2201011, 7.0, 30, 2202020, 10), arg_types="ifiii")
    RunEvent(12200210, slot=2, args=(2201016, 7.0, 15, 2202020, 10), arg_types="ifiii")
    RunEvent(12200210, slot=3, args=(2201017, 7.0, 0, 2202020, 10), arg_types="ifiii")
    RunEvent(12200210, slot=4, args=(2201018, 7.0, 5, 2202020, 10), arg_types="ifiii")
    RunEvent(12200210, slot=5, args=(2201012, 10.0, 10, 2202021, 11), arg_types="ifiii")
    RunEvent(12200210, slot=6, args=(2201013, 10.0, 0, 2202021, 11), arg_types="ifiii")
    RunEvent(12200210, slot=7, args=(2201014, 10.0, 30, 2202021, 11), arg_types="ifiii")
    RunEvent(12200210, slot=8, args=(2201015, 10.0, 0, 2202021, 11), arg_types="ifiii")
    RunEvent(12200220, slot=0, args=(2200111, 52200990))
    RunEvent(12200220, slot=1, args=(2200170, 52200980))
    RunEvent(12200220, slot=2, args=(2200110, 52200970))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6631)
    EnableFlag(12201999)
    SkipLinesIfFlagEnabled(5, 12201999)
    EnableObject(2201150)
    DisableObject(2201151)
    EnableTreasure(2201150)
    DisableTreasure(2201151)
    SkipLines(4)
    DisableObject(2201150)
    EnableObject(2201151)
    DisableTreasure(2201150)
    EnableTreasure(2201151)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6309)
    EnableFlag(12201998)
    SkipLinesIfFlagEnabled(5, 12201998)
    EnableObject(2201500)
    DisableObject(2201501)
    EnableTreasure(2201500)
    DisableTreasure(2201501)
    SkipLines(4)
    DisableObject(2201500)
    EnableObject(2201501)
    DisableTreasure(2201500)
    EnableTreasure(2201501)
    RunEvent(12200990)
    RunEvent(12204000, slot=0, args=(2200500, 20.0), arg_types="if")
    RunEvent(12204000, slot=1, args=(2200501, 20.0), arg_types="if")
    RunEvent(12204000, slot=2, args=(2200502, 20.0), arg_types="if")
    RunEvent(12204000, slot=3, args=(2200503, 20.0), arg_types="if")
    RunEvent(12204000, slot=4, args=(2200504, 20.0), arg_types="if")
    RunEvent(12204000, slot=5, args=(2200505, 20.0), arg_types="if")
    RunEvent(12204000, slot=6, args=(2200506, 20.0), arg_types="if")
    RunEvent(12204000, slot=7, args=(2200507, 20.0), arg_types="if")
    RunEvent(12204000, slot=8, args=(2200508, 20.0), arg_types="if")
    RunEvent(12205000)
    RunEvent(12205001)
    RunEvent(12205002)
    RunEvent(12205003)
    RunEvent(12205040)
    RunEvent(12205041)
    RunEvent(12205020)
    RunEvent(12205030)
    RunEvent(12205031)
    RunEvent(12205060)
    RunEvent(12205050)
    RunEvent(12205051)
    RunEvent(12205070)
    RunEvent(12205080)
    RunEvent(12205010, slot=0, args=(2200240, 2200130, 2202070, 2202370, 2202080, 12205015))
    RunEvent(12205010, slot=1, args=(2200223, 2200310, 2202071, 2202371, 2202171, 12205016))
    RunEvent(12205015, slot=0, args=(2200130, 2202370, 4294967295, 12205010))
    RunEvent(12205015, slot=1, args=(2200310, 2202371, 200, 12205011))
    RunEvent(12205100, slot=0, args=(2200202, 2202130, 3.0, 12205105, 50), arg_types="iifii")
    RunEvent(12205100, slot=1, args=(2200200, 2202150, 3.0, 12205106, 50), arg_types="iifii")
    RunEvent(12205100, slot=2, args=(2200201, 2202151, 3.0, 12205107, 60), arg_types="iifii")
    RunEvent(12205100, slot=3, args=(2200204, 2202152, 5.0, 12205108, 50), arg_types="iifii")
    RunEvent(12205105, slot=0, args=(2200202, 2202130, 3007, 3.0), arg_types="iiif")
    RunEvent(12205105, slot=1, args=(2200200, 2202150, 3009, 2.5), arg_types="iiif")
    RunEvent(12205105, slot=2, args=(2200201, 2202154, 3022, 2.0), arg_types="iiif")
    RunEvent(12205105, slot=3, args=(2200204, 2202153, 3011, 2.700000047683716), arg_types="iiif")
    RunEvent(12205110, slot=0, args=(2200203, 2202140, 3.0, 3006), arg_types="iifi")
    RunEvent(12205120, slot=0, args=(2200211, 2202160, 5.0, 2202161), arg_types="iifi")
    RunEvent(12205120, slot=1, args=(2200212, 2202160, 5.0, 2202161), arg_types="iifi")
    RunEvent(12205120, slot=2, args=(2200213, 2202160, 5.0, 2202161), arg_types="iifi")
    RunEvent(12205120, slot=3, args=(2200223, 2202170, 15.0, 2202171), arg_types="iifi")
    RunEvent(12205120, slot=4, args=(2200224, 2202170, 15.0, 2202171), arg_types="iifi")
    RunEvent(12205120, slot=5, args=(2200230, 2202180, 6.0, 2202180), arg_types="iifi")
    RunEvent(12205120, slot=6, args=(2200231, 2202180, 6.0, 2202180), arg_types="iifi")
    RunEvent(12205120, slot=7, args=(2200232, 2202180, 6.0, 2202180), arg_types="iifi")
    RunEvent(12205120, slot=8, args=(2200240, 2202190, 15.0, 2202191), arg_types="iifi")
    RunEvent(12205120, slot=9, args=(2200250, 2202200, 10.0, 2202201), arg_types="iifi")
    RunEvent(12205120, slot=10, args=(2200251, 2202200, 10.0, 2202201), arg_types="iifi")
    RunEvent(12205120, slot=11, args=(2200252, 2202200, 10.0, 2202201), arg_types="iifi")
    RunEvent(12205120, slot=12, args=(2200260, 2202200, 10.0, 2202201), arg_types="iifi")
    RunEvent(12205120, slot=13, args=(2200261, 2202200, 10.0, 2202201), arg_types="iifi")
    RunEvent(12205120, slot=14, args=(2200270, 2202220, 10.0, 2202221), arg_types="iifi")
    RunEvent(12205120, slot=15, args=(2200271, 2202220, 10.0, 2202221), arg_types="iifi")
    RunEvent(12205120, slot=16, args=(2200272, 2202220, 10.0, 2202221), arg_types="iifi")
    RunEvent(12205120, slot=17, args=(2200290, 2202230, 8.0, 2202231), arg_types="iifi")
    RunEvent(12205120, slot=18, args=(2200291, 2202230, 8.0, 2202231), arg_types="iifi")
    RunEvent(12205120, slot=19, args=(2200292, 2202230, 8.0, 2202231), arg_types="iifi")
    RunEvent(12205120, slot=20, args=(2200280, 2202240, 5.0, 2202240), arg_types="iifi")
    RunEvent(12205120, slot=21, args=(2200412, 2202260, 5.0, 2202260), arg_types="iifi")
    RunEvent(12205120, slot=22, args=(2200310, 2202170, 15.0, 2202171), arg_types="iifi")
    RunEvent(12205120, slot=23, args=(2200450, 2202270, 15.0, 2202271), arg_types="iifi")
    RunEvent(12205120, slot=24, args=(2200460, 2202310, 15.0, 2202310), arg_types="iifi")
    RunEvent(12205120, slot=25, args=(2200470, 2202430, 3.0, 2202431), arg_types="iifi")
    RunEvent(12205120, slot=26, args=(2200430, 2202170, 7.0, 2202171), arg_types="iifi")
    RunEvent(12205150, slot=0, args=(2200100, 7014, 0, 0.0), arg_types="iiif")
    RunEvent(12205150, slot=1, args=(2200301, 7010, 7011, 7.0), arg_types="iiif")
    RunEvent(12205150, slot=2, args=(2200303, 7012, 7013, 0.0), arg_types="iiif")
    RunEvent(12205150, slot=3, args=(2200300, 7014, 0, 0.0), arg_types="iiif")
    RunEvent(12205150, slot=4, args=(2200212, 7014, 0, 0.0), arg_types="iiif")
    RunEvent(12205160, slot=0, args=(2202040, 2201401, 2200410, 2200400))
    RunEvent(12205160, slot=1, args=(2202041, 2201406, 2200411, 2200401))
    RunEvent(12205170, slot=0, args=(2201400, 2200420))
    RunEvent(12205170, slot=1, args=(2201401, 2200420))
    RunEvent(12205170, slot=2, args=(2201402, 2200420))
    RunEvent(12205170, slot=3, args=(2201403, 2200420))
    RunEvent(12205170, slot=4, args=(2201404, 2200420))
    RunEvent(12205170, slot=5, args=(2201405, 2200420))
    RunEvent(12205170, slot=6, args=(2201406, 2200420))
    RunEvent(12205170, slot=7, args=(2201407, 2200422))
    RunEvent(12205170, slot=8, args=(2201408, 2200422))
    RunEvent(12205170, slot=9, args=(2201409, 2200422))
    RunEvent(12205170, slot=10, args=(2201410, 2200421))
    RunEvent(12205170, slot=11, args=(2201411, 2200421))
    RunEvent(12205170, slot=12, args=(2201412, 2200421))
    RunEvent(12205170, slot=13, args=(2201413, 2200421))
    RunEvent(12205170, slot=14, args=(2201414, 2200421))
    RunEvent(12205170, slot=15, args=(2201415, 2200421))
    RunEvent(12205170, slot=16, args=(2201416, 2200421))
    RunEvent(12205170, slot=17, args=(2201417, 2200421))
    RunEvent(12205170, slot=18, args=(2201418, 2200421))
    RunEvent(12205170, slot=19, args=(2201419, 2200421))
    RunEvent(12205170, slot=20, args=(2201420, 2200420))
    RunEvent(12205170, slot=21, args=(2201421, 2200420))
    RunEvent(12205170, slot=22, args=(2201422, 2200421))
    RunEvent(12205170, slot=23, args=(2201423, 2200421))
    RunEvent(12205170, slot=24, args=(2201424, 2200421))
    RunEvent(12205170, slot=25, args=(2201425, 2200421))
    RunEvent(12205170, slot=26, args=(2201426, 2200421))
    RunEvent(12205170, slot=27, args=(2201427, 2200421))
    RunEvent(12205200, slot=0, args=(2200200,))
    RunEvent(12205200, slot=1, args=(2200201,))
    RunEvent(12205200, slot=2, args=(2200202,))
    RunEvent(12205200, slot=3, args=(2200204,))
    RunEvent(12205200, slot=4, args=(2200205,))
    RunEvent(12205200, slot=5, args=(2200251,))
    RunEvent(12205200, slot=6, args=(2200270,))
    RunEvent(12205200, slot=7, args=(2200271,))
    RunEvent(12205210, slot=0, args=(2200320,))
    RunEvent(12205210, slot=1, args=(2200321,))
    RunEvent(12205220, slot=0, args=(2200240, 2202282, 3006, 2202302))
    RunEvent(12205220, slot=1, args=(2200250, 2202280, 7001, 2202300))
    RunEvent(12205220, slot=2, args=(2200250, 2202281, 7001, 2202301))
    RunEvent(12205220, slot=3, args=(2200252, 2202279, 3006, 2202299))
    RunEvent(12205220, slot=4, args=(2200251, 2202278, 7001, 2202298))
    RunEvent(12205220, slot=5, args=(2200450, 2202283, 7014, 2202283))
    RunEvent(12205230, slot=0, args=(2200330, 114093))
    RunEvent(12205230, slot=1, args=(2200331, 114094))
    RunEvent(12205230, slot=2, args=(2200332, 114094))
    RunEvent(12205230, slot=3, args=(2200333, 114093))
    RunEvent(12205230, slot=4, args=(2200334, 114094))
    RunEvent(12205240, slot=0, args=(2200340,))
    RunEvent(12205240, slot=1, args=(2200341,))
    RunEvent(12205260, slot=0, args=(2200110, 2202630, 12205265, 12205270))
    RunEvent(12205260, slot=1, args=(2200111, 2202632, 12205266, 12205271))
    RunEvent(12205265, slot=0, args=(2200110, 2202631, 2202380, 12205260, 12205270))
    RunEvent(12205265, slot=1, args=(2200111, 2202633, 2202381, 12205261, 12205271))
    RunEvent(12205270, slot=0, args=(2200110, 2202380, 12205265, 2202630, 2202381, 12205260))
    RunEvent(12205270, slot=1, args=(2200111, 2202381, 12205266, 2202633, 2202382, 12205261))
    RunEvent(12205300, slot=0, args=(2203300, 1439, 6001, 9802))


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2203950)
    DisableGravity(2203950)
    DisableCharacterCollision(2203950)
    DisableAnimations(2203951)
    DisableGravity(2203951)
    DisableCharacterCollision(2203951)
    RunEvent(12204010)


def Event12201800():
    """ 12201800: Event 12201800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2203802)
    DisableSoundEvent(2203803)
    DisableCharacter(2200800)
    Kill(2200800, award_souls=False)
    DisableCharacter(2200801)
    Kill(2200801, award_souls=False)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteVFX(2203800, erase_root_only=True)
    DeleteVFX(2203801, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 2200800)
    IfCharacterDead(1, 2200801)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteVFX(2203800, erase_root_only=True)
    DeleteVFX(2203801, erase_root_only=True)
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=0)
    Wait(3.0)
    KillBoss(2200800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    AwardAchievement(23)
    AwardItemLot(21002950, host_only=False)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(72400512)
    EnableFlag(2200)
    EnableFlag(9452)
    EnableFlag(5911)
    StopPlayLogMeasurement(2200000)
    StopPlayLogMeasurement(2200001)
    StopPlayLogMeasurement(2200010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 52, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event12201801():
    """ 12201801: Event 12201801 """
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(1, 12201800)
    IfCharacterBackreadDisabled(2, 2200800)
    IfHealthLessThanOrEqual(2, 2200800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2202800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def Event12201802():
    """ 12201802: Event 12201802 """
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
    IfPlayerInsightAmountEqual(2, 0)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionTrue(1, 2)
    ForceAnimation(2200800, 3011)
    EnableFlag(12204800)
    EndIfFlagEnabled(9338)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9338)


def Event12201803():
    """ 12201803: Event 12201803 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSpawner(2205000)
    DisableSpawner(2205001)
    DisableSpawner(2205002)
    DisableBackread(2200810)
    DisableBackread(2200811)
    DisableBackread(2200812)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12201800)
    DisableSpawner(2205000)
    DisableSpawner(2205001)
    DisableSpawner(2205002)
    Kill(2200810, award_souls=False)
    Kill(2200811, award_souls=False)
    Kill(2200812, award_souls=False)


def Event12201804():
    """ 12201804: Event 12201804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12204800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2200800)
    EnableFlag(12204800)
    EnableFlag(12201802)


def Event12204890():
    """ 12204890: Event 12204890 """
    EndIfFlagEnabled(12201800)
    GotoIfFlagEnabled(Label.L0, 12201802)
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
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2202801)
    IfTimeElapsed(5, 2.0)
    IfCharacterHuman(5, PLAYER)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12204800)
    Restart()


def Event12204891():
    """ 12204891: Event 12204891 """
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagDisabled(1, 12201800)
    IfFlagEnabled(1, 12201802)
    IfFlagEnabled(1, 12204800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=2200800, entity=2201800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2202801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12204801)
    Restart()


def Event12204892():
    """ 12204892: Event 12204892 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2201800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12204893():
    """ 12204893: Event 12204893 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 2201800, radius=2.0)
    IfEntityWithinDistance(1, PLAYER, 2201800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event12204802():
    """ 12204802: Event 12204802 """
    EndIfFlagEnabled(12201800)
    DisableAI(2200800)
    DisableHealthBar(2200800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12204800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200800, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2200800)
    EnableBossHealthBar(2200800, name=210000, slot=0)
    CreatePlayLog(88)
    StartPlayLogMeasurement(2200010, 104, overwrite=True)


def Event12204803():
    """ 12204803: Event 12204803 """
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2203802)
    DisableSoundEvent(2203803)
    IfFlagDisabled(1, 12201800)
    IfFlagEnabled(1, 12204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12204801)
    IfCharacterInsideRegion(1, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2203802)
    IfHealthValueEqual(-1, 2200800, 1)
    IfHealthValueEqual(-1, 2200801, 1)
    IfConditionTrue(2, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12201800)
    IfFlagEnabled(2, 12204802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12204801)
    IfCharacterInsideRegion(2, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2203802)
    WaitFrames(0)
    EnableBossMusic(2203803)


def Event12204804():
    """ 12204804: Event 12204804 """
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12204800)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfFlagEnabled(2, 12204801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=1)


def Event12204805():
    """ 12204805: Event 12204805 """
    DisableNetworkSync()
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(0, 12201800)
    DisableBossMusic(2203802)
    DisableBossMusic(2203803)
    DisableBossMusic(-1)


def Event12204807():
    """ 12204807: Event 12204807 """
    EndIfFlagEnabled(12201800)
    IfHealthValueEqual(-1, 2200800, 1)
    IfHealthValueEqual(-1, 2200801, 1)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2200800, command_id=100, slot=0)
    AICommand(2200801, command_id=100, slot=0)
    Wait(10.0)
    IfCharacterDead(1, 2200800)
    IfCharacterDead(1, 2200801)
    EndIfConditionTrue(1)
    EnableBossHealthBar(2200801, name=210000, slot=1)


def Event12204808(_, arg_0_3: int, arg_4_7: int):
    """ 12204808: Event 12204808 """
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfEntityBeyondDistance(1, PLAYER, arg_0_3, radius=12.0)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=10)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 5686, affect_npc_parts_hp=False)

    # --- 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=6.0)
    IfFlagDisabled(2, arg_4_7)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 5688, affect_npc_parts_hp=False)
    Restart()


def Event12204810():
    """ 12204810: Event 12204810 """
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200801)
    DisableHealthBar(2200801)
    DisableCharacter(2200801)
    IfHealthLessThanOrEqual(0, 2200800, 0.5)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200801, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2200801, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200801)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2200801, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200801)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableCharacter(2200801)
    EnableAI(2200801)


def Event12204811():
    """ 12204811: Event 12204811 """
    EndIfFlagEnabled(12201800)
    GotoIfThisEventFlagEnabled(Label.L0)
    SetAIParamID(2200800, 210021)
    IfCharacterDead(-1, 2200810)
    IfAttackedWithDamageType(-1, attacked_entity=2200800)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2200800, 210020)


def Event12204812(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12204812: Event 12204812 """
    EndIfFlagEnabled(12201800)
    EnableImmortality(arg_0_3)
    IfHealthValueEqual(3, arg_0_3, 1)
    IfHealthValueLessThan(3, arg_4_7, 1)
    IfHealthValueEqual(4, arg_0_3, 1)
    IfHealthValueEqual(4, arg_4_7, 1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    Wait(0.0)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(arg_0_3, 7000)
    WaitFrames(75)
    ForceAnimation(arg_0_3, 7001, loop=True)
    IfTimeElapsed(1, 45.0)
    IfHealthValueEqual(2, arg_4_7, 1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    AddSpecialEffect(arg_0_3, 5686, affect_npc_part_hp=False)
    Wait(3.0)
    DisableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(arg_0_3, 5698, affect_npc_part_hp=False)
    Wait(3.0)
    EnableCharacter(arg_0_3)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Kill(arg_0_3, award_souls=False)
    Kill(arg_4_7, award_souls=False)


def Event12204814(
    _,
    arg_0_3: int,
    arg_4_7: uint,
    arg_8_11: uint,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12204814: Event 12204814 """
    EndIfFlagEnabled(12201800)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=30)
    AddSpecialEffect(arg_0_3, 5686, affect_npc_part_hp=False)
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfHealthValueNotEqual(1, arg_0_3, 1)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    EnableRandomFlagInRange((arg_4_7, arg_8_11))
    GotoIfFlagDisabled(Label.L1, arg_12_15)
    DisableFlagRange((arg_12_15, arg_24_27))
    EnableFlag(arg_12_15)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, arg_16_19)
    DisableFlagRange((arg_12_15, arg_24_27))
    EnableFlag(arg_16_19)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, arg_20_23)
    DisableFlagRange((arg_12_15, arg_24_27))
    EnableFlag(arg_20_23)
    Goto(Label.L0)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L0, arg_24_27)
    DisableFlagRange((arg_12_15, arg_24_27))
    EnableFlag(arg_24_27)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, arg_12_15)
    IfFlagEnabled(-1, arg_16_19)
    IfFlagEnabled(-1, arg_20_23)
    IfFlagEnabled(-1, arg_24_27)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_28_31)
    Restart()


def Event12204820(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12204820: Event 12204820 """
    EndIfFlagEnabled(12201800)
    IfFlagEnabled(0, arg_4_7)
    DisableFlag(arg_4_7)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_8_11)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_16_19)
    Restart()


def Event12204830(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12204830: Event 12204830 """
    EndIfFlagEnabled(12201800)
    DisableNetworkSync()
    IfFlagEnabled(0, arg_4_7)
    Wait(2.0)
    EnableCharacter(arg_0_3)
    ReplanAI(arg_0_3)
    DisableFlag(arg_8_11)
    DisableFlag(arg_4_7)
    Restart()


def Event12204832(_, arg_0_3: int):
    """ 12204832: Event 12204832 """
    EndIfFlagEnabled(12201800)
    IfCharacterDead(0, arg_0_3)
    IncrementEventValue(12204860, bit_count=10, max_value=10)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    Restart()


def Event12204835(_, arg_0_3: int, arg_4_7: int):
    """ 12204835: Event 12204835 """
    EndIfFlagEnabled(12201800)
    IfCharacterDead(0, arg_0_3)
    EnableFlag(arg_4_7)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    DisableFlag(arg_4_7)
    Restart()


def Event12204838():
    """ 12204838: Event 12204838 """
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
    EnableSpawner(2205000)
    IfCharacterHasTAEEvent(0, 2200810, tae_event_id=10)
    DisableSpawner(2205000)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=2)
    EnableSpawner(2205001)
    IfCharacterHasTAEEvent(0, 2200811, tae_event_id=10)
    DisableSpawner(2205001)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    EnableSpawner(2205002)
    IfCharacterHasTAEEvent(0, 2200812, tae_event_id=10)
    DisableSpawner(2205002)
    Restart()


@RestartOnRest
def Event12204839():
    """ 12204839: Event 12204839 """
    EndIfFlagEnabled(12201800)
    IfFlagDisabled(1, 12204845)
    IfConditionTrue(0, input_condition=1)
    IfHealthValueEqual(-1, 2200800, 1)
    IfHealthValueEqual(-1, 2200801, 1)
    IfConditionTrue(-2, input_condition=-1)
    IfFlagEnabled(-2, 12204812)
    IfFlagEnabled(2, 12201802)
    IfThisEventFlagDisabled(2)
    IfFlagDisabled(2, 12201810)
    IfEventValueEqual(3, 12204860, bit_count=10, value=3)
    IfFlagDisabled(3, 12204875)
    IfHealthLessThanOrEqual(4, 2200800, 0.30000001192092896)
    IfEventValueComparison(4, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfFlagDisabled(4, 12204875)
    IfHealthLessThanOrEqual(5, 2200801, 0.5)
    IfEventValueComparison(5, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfFlagDisabled(5, 12204875)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfEventValueComparison(6, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=5)
    IfHealthValueEqual(-4, 2200800, 1)
    IfHealthValueEqual(-4, 2200801, 1)
    IfConditionTrue(7, input_condition=-4)
    IfEventValueComparison(7, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=4)
    IfEventValueComparison(7, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    IfConditionTrue(-5, input_condition=6)
    IfConditionTrue(-5, input_condition=7)
    IfConditionTrue(-6, input_condition=-2)
    IfConditionTrue(-6, input_condition=2)
    IfConditionTrue(-6, input_condition=-3)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)

    # --- 1 --- #
    DefineLabel(1)
    IfHealthValueEqual(8, 2200800, 1)
    IfHealthValueNotEqual(9, 2200800, 1)
    IfConditionTrue(-7, input_condition=8)
    IfConditionTrue(-7, input_condition=9)
    GotoIfConditionTrue(Label.L2, input_condition=8)
    ResetAnimation(2200800, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(2200800, 3011)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    ResetAnimation(2200801, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(2200801, 3011)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=-5)
    WaitFrames(65)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(2205001)
    WaitFrames(35)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(2205002)
    End()

    # --- 4 --- #
    DefineLabel(4)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(2205000)
    EnableFlag(12204876)
    EnableFlag(12201810)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(2205001)
    EnableFlag(12204875)
    Restart()

    # --- 6 --- #
    DefineLabel(6)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(2205002)
    End()


@RestartOnRest
def Event12204840():
    """ 12204840: Event 12204840 """
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(5, 12204845)
    IfConditionTrue(0, input_condition=5)
    IfEventValueComparison(1, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    IfFlagEnabled(2, 12204870)
    IfEventValueComparison(2, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfHealthValueEqual(5, 2200800, 1)
    IfHealthValueEqual(5, 2200801, 1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    IfHealthValueEqual(3, 2200800, 1)
    IfHealthValueNotEqual(4, 2200800, 1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=3)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200801, command_id=10, slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200800, command_id=10, slot=2)
    ReplanAI(2200800)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagDisabled(0, 12204870)
    AICommand(2200800, command_id=-1, slot=2)
    ReplanAI(2200800)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204880)


@RestartOnRest
def Event12204841():
    """ 12204841: Event 12204841 """
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 12204880)
    IfEventValueComparison(1, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=5)
    IfEventValueComparison(2, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=4)
    IfFlagEnabled(2, 12204870)
    IfEventValueComparison(3, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=4)
    IfFlagEnabled(3, 12204871)
    IfHealthValueEqual(6, 2200800, 1)
    IfHealthValueEqual(6, 2200801, 1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    IfHealthValueEqual(4, 2200800, 1)
    IfHealthValueNotEqual(5, 2200800, 1)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=4)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200801, command_id=10, slot=2)
    ReplanAI(2200801)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200800, command_id=10, slot=2)
    ReplanAI(2200800)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagDisabled(4, 12204870)
    IfFlagDisabled(4, 12204871)
    IfConditionTrue(0, input_condition=4)
    AICommand(2200800, command_id=-1, slot=2)
    ReplanAI(2200800)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12204881)


@RestartOnRest
def Event12204842():
    """ 12204842: Event 12204842 """
    EndIfFlagEnabled(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 12204881)
    IfFlagEnabled(-1, 12204870)
    IfFlagEnabled(-1, 12204871)
    IfFlagEnabled(-1, 12204872)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=15.0, max_seconds=25.0)
    AICommand(2200800, command_id=10, slot=2)
    AICommand(2200801, command_id=10, slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    IfFlagDisabled(1, 12204870)
    IfFlagDisabled(1, 12204871)
    IfFlagDisabled(1, 12204872)
    IfConditionTrue(0, input_condition=1)
    AICommand(2200800, command_id=-1, slot=2)
    AICommand(2200801, command_id=-1, slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    Restart()


@RestartOnRest
def Event12204843():
    """ 12204843: Event 12204843 """
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
    DisableSpawner(2205000)


@RestartOnRest
def Event12204844():
    """ 12204844: Event 12204844 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountLessThanOrEqual(0, 0)
    EnableFlag(12204845)
    IfPlayerInsightAmountGreaterThanOrEqual(0, 1)
    DisableFlag(12204845)
    Restart()


def Event12200100():
    """ 12200100: Event 12200100 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2201001, 1)
    DisableObjectActivation(2201001, obj_act_id=2200010)
    NotifyDoorEventSoundDampening(2201001, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200101)
    CreatePlayLog(122)
    Wait(0.0)


def Event12200101():
    """ 12200101: Event 12200101 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2201060, 0)
    DisableObjectActivation(2201060, obj_act_id=2200030)
    NotifyDoorEventSoundDampening(2201060, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200500)
    Wait(0.0)


def Event12200110():
    """ 12200110: Event 12200110 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(2201002, 1)
    DisableObjectActivation(2201220, obj_act_id=100)
    NotifyDoorEventSoundDampening(2201002, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12200112)
    CreatePlayLog(158)
    DisableObjectActivation(2201220, obj_act_id=100)
    ForceAnimation(2201002, 1)
    Wait(0.0)


def Event12200111():
    """ 12200111: Event 12200111 """
    DisableNetworkSync()
    EndIfFlagEnabled(12200110)
    IfActionButtonParam(1, action_button_id=2200000, entity=2201002)
    IfActionButtonParam(2, action_button_id=2200001, entity=2201002)
    IfFlagEnabled(3, 12200110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    DisplayDialog(
        10010160,
        anchor_entity=2201002,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12200112():
    """ 12200112: Event 12200112 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12200110)
    IfActionButtonParam(1, action_button_id=7100, entity=2201220)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=2201220,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12200120():
    """ 12200120: Event 12200120 """
    IfFlagEnabled(1, 12200125)
    IfFlagDisabled(2, 12200125)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    EndOfAnimation(2201210, 0)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2201210, 4)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, 12200121)
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)

    # --- 2 --- #
    DefineLabel(2)


def Event12200121():
    """ 12200121: Event 12200121 """
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    IfCharacterInsideRegion(0, PLAYER, region=2202010)
    CreatePlayLog(186)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)


def Event12200122():
    """ 12200122: Event 12200122 """
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
    WaitFrames(15)
    ForceAnimation(2201210, 2)
    WaitFrames(150)
    IfAllPlayersOutsideRegion(0, region=2202001)
    ForceAnimation(2201210, 3)
    WaitFrames(30)
    EnableFlag(12200125)
    DisableFlag(12200126)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    Restart()


def Event12200123():
    """ 12200123: Event 12200123 """
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
    WaitFrames(15)
    ForceAnimation(2201210, 6)
    WaitFrames(150)
    IfAllPlayersOutsideRegion(0, region=2202000)
    ForceAnimation(2201210, 7)
    WaitFrames(30)
    DisableFlag(12200125)
    DisableFlag(12200126)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Restart()


def Event12200124():
    """ 12200124: Event 12200124 """
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
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


@RestartOnRest
def Event12200130():
    """ 12200130: Event 12200130 """
    DisableCharacter(2201310)
    DisableObject(2201300)
    DisableHealthBar(2201310)
    EndIfFlagEnabled(12507810)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfPlayerHasGood(1, 4003, including_box=False)
    IfFlagEnabled(1, 12201800)
    IfCharacterInsideRegion(1, PLAYER, region=2202410)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(22000030, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(12204020)

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(2201310)
    EnableObject(2201300)
    DisableHealthBar(2201310)


@RestartOnRest
def Event12200131():
    """ 12200131: Event 12200131 """
    EndIfFlagEnabled(12507810)
    IfFlagEnabled(1, 12200130)
    IfCharacterAlive(1, 2201310)
    IfActionButtonParam(1, action_button_id=2200010, entity=2201300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(22000040, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    WarpPlayerToRespawnPoint(2502959)


@RestartOnRest
def Event12200132():
    """ 12200132: Event 12200132 """
    EndIfFlagEnabled(12507810)
    IfHealthLessThanOrEqual(0, 2201310, 0.0)
    StopEvent(12200131)


@RestartOnRest
def Event12200150(_, arg_0_3: int, arg_4_7: int):
    """ 12200150: Event 12200150 """
    EndIfFlagEnabled(12200130)
    IfFlagEnabled(0, 12204020)
    IfCharacterInsideRegion(1, arg_0_3, region=2202640)
    EndIfConditionFalse(1)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, set_draw_parent=0)


@RestartOnRest
def Event12200210(_, arg_0_3: int, arg_4_7: float, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12200210: Event 12200210 """
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(arg_0_3, arg_16_19)
    DisableObject(arg_0_3)
    End()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(arg_8_11)
    ForceAnimation(arg_0_3, arg_16_19, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest
def Event12200220(_, arg_0_3: int, arg_4_7: int):
    """ 12200220: Event 12200220 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


def Event12200300():
    """ 12200300: Event 12200300 """
    GotoIfFlagEnabled(Label.L2, 9802)
    GotoIfFlagEnabled(Label.L1, 9801)
    GotoIfFlagEnabled(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2206000)
    DisableMapPiece(2206001)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(2206000)
    EnableMapPiece(2206001)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableMapPiece(2206000)
    EnableMapPiece(2206001)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12200310(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12200310: Event 12200310 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event12204000(_, arg_0_3: int, arg_4_7: float):
    """ 12204000: Event 12204000 """
    GotoIfFlagEnabled(Label.L0, 12204011)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(-1, 9801)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_4_7)
    IfCharacterHuman(1, PLAYER)
    IfThisEventSlotFlagEnabled(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 6200)


@RestartOnRest
def Event12204010():
    """ 12204010: Event 12204010 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountGreaterThanOrEqual(2, 15)
    EndIfConditionFalse(2)
    EnableFlag(12204011)


@RestartOnRest
def Event12205000():
    """ 12205000: Event 12205000 """
    EndIfFlagEnabled(12205001)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2202061)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(12205001)
    EnableAI(2200120)
    SetNest(2200120, 2202360)
    AICommand(2200120, command_id=10, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205001():
    """ 12205001: Event 12205001 """
    EndIfFlagEnabled(12205000)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202062)
    IfCharacterInsideRegion(-2, PLAYER, region=2202060)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, PLAYER, 2200120, radius=10.0)
    IfAttacked(-3, 2200120, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(12205000)
    EnableAI(2200120)


@RestartOnRest
def Event12205002():
    """ 12205002: Event 12205002 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, 2200120, region=2202360)
    IfHasAIStatus(1, 2200120, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2200120, 3006)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200120, command_id=-1, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205003():
    """ 12205003: Event 12205003 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, 2200120, radius=4.0)
    IfConditionTrue(-2, input_condition=1)
    IfAttackedWithDamageType(-2, attacked_entity=2200120)
    IfHasAIStatus(-2, 2200120, ai_status=AIStatusType.Battle)
    IfFlagEnabled(-2, 12205002)
    IfConditionTrue(0, input_condition=-2)
    AICommand(2200120, command_id=-1, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12205010: Event 12205010 """
    EndIfFlagEnabled(arg_20_23)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(arg_4_7)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, arg_4_7, PLAYER, radius=7.0)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_16_19)
    IfAttackedWithDamageType(4, attacked_entity=arg_0_3)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(arg_4_7)
    SetNest(arg_4_7, arg_12_15)
    AICommand(arg_4_7, command_id=20, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12205015(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205015: Event 12205015 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, arg_12_15)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=7.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_4_7)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12205040():
    """ 12205040: Event 12205040 """
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
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=2202320)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect(2200211, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(2200211, patrol_information_id=2203030)
    ReplanAI(2200211)


@RestartOnRest
def Event12205041():
    """ 12205041: Event 12205041 """
    EndIfThisEventFlagEnabled()
    IfHasAIStatus(-1, 2200211, ai_status=AIStatusType.Battle)
    IfCharacterInsideRegion(-1, 2200211, region=2202320)
    IfConditionTrue(0, input_condition=-1)
    IfHasAIStatus(0, 2200211, ai_status=AIStatusType.Normal)
    CancelSpecialEffect(2200211, 5000)
    ChangePatrolBehavior(2200211, patrol_information_id=2203031)
    ReplanAI(2200211)


@RestartOnRest
def Event12205020():
    """ 12205020: Event 12205020 """
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(2200140, 7004, loop=True)
    SetAIParamID(2200140, 261091)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionFalse(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=2202080)
    IfHasAIStatus(2, 2200140, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(2, 2200140, PLAYER, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2200140, 261003)
    ForceAnimation(2200140, 7005)


@RestartOnRest
def Event12205030():
    """ 12205030: Event 12205030 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, PLAYER, region=2202090)
    IfEntityWithinDistance(2, PLAYER, 2200150, radius=10.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2200150, 2202390)
    AICommand(2200150, command_id=10, slot=0)
    ReplanAI(2200150)


@RestartOnRest
def Event12205031():
    """ 12205031: Event 12205031 """
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(1, 2200150, region=2202390)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(2, PLAYER, 2200150, radius=3.5)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    ResetAnimation(2200150, disable_interpolation=False)
    RotateToFaceEntity(2200150, PLAYER, animation=3001)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200150, command_id=-1, slot=0)
    ReplanAI(2200150)


@RestartOnRest
def Event12205050():
    """ 12205050: Event 12205050 """
    EndIfFlagEnabled(12205051)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200280)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200280, PLAYER, radius=3.0)
    IfAttackedWithDamageType(2, attacked_entity=2200280)
    IfHasAIStatus(3, 2200270, ai_status=AIStatusType.Battle)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2200280)
    EndIfFinishedConditionFalse(3)
    Wait(5.0)
    SetNest(2200280, 2209005)
    AICommand(2200280, command_id=10, slot=0)
    ReplanAI(2200280)


@RestartOnRest
def Event12205051():
    """ 12205051: Event 12205051 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200280, PLAYER, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, 2200280, region=2209005)
    IfAttackedWithDamageType(-2, attacked_entity=2200280)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2200280, command_id=-1, slot=0)
    ReplanAI(2200280)


@RestartOnRest
def Event12205060():
    """ 12205060: Event 12205060 """
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


@RestartOnRest
def Event12205070():
    """ 12205070: Event 12205070 """
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200411)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200411, 100000, radius=10.0)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, 2200160, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, 2200161, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2200411)
    ReplanAI(2200411)


@RestartOnRest
def Event12205080():
    """ 12205080: Event 12205080 """
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2200205)
    IfCharacterInsideRegion(1, PLAYER, region=2202155)
    IfCharacterInsideRegion(2, PLAYER, region=2202156)
    IfAttacked(3, 2200205, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2200205, PLAYER, animation=3012)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(35)
    EnableAI(2200205)


@RestartOnRest
def Event12205100(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int):
    """ 12205100: Event 12205100 """
    EndIfFlagEnabled(arg_12_15)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetCharacterEventTarget(arg_0_3, 10000)
    AICommand(arg_0_3, command_id=arg_16_19, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12205105(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 12205105: Event 12205105 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_12_15)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_12_15)
    IfCharacterOutsideRegion(2, arg_0_3, region=arg_4_7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_8_11)

    # --- 1 --- #
    DefineLabel(1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12205110(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12205110: Event 12205110 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15)
    EnableAI(arg_0_3)
    End()
    EnableAI(arg_0_3)


@RestartOnRest
def Event12205120(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12205120: Event 12205120 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttacked(2, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12205150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 12205150: Event 12205150 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(arg_0_3, arg_8_11)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12205160(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205160: Event 12205160 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfObjectNotDestroyed(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(arg_8_11, arg_12_15)
    AICommand(arg_8_11, command_id=100, slot=0)
    ReplanAI(arg_8_11)
    IfCharacterHasTAEEvent(0, arg_8_11, tae_event_id=100)
    AICommand(arg_8_11, command_id=-1, slot=0)
    ReplanAI(arg_8_11)
    Restart()


@RestartOnRest
def Event12205170(_, arg_0_3: int, arg_4_7: int):
    """ 12205170: Event 12205170 """
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    PostDestruction(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, arg_0_3, ComparisonType.LessThanOrEqual, 999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6071,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@RestartOnRest
def Event12205200(_, arg_0_3: int):
    """ 12205200: Event 12205200 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
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
    AICommand(arg_0_3, command_id=100, slot=0)
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
    AICommand(arg_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12205210(_, arg_0_3: int):
    """ 12205210: Event 12205210 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, 9003, loop=True)
    SetAIParamID(arg_0_3, 117007)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=5.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfAttacked(3, arg_0_3, attacker=PLAYER)
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
    IfEntityWithinDistance(8, arg_0_3, PLAYER, radius=3.0)
    IfConditionTrue(8, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(arg_0_3, 117000)
    ForceAnimation(arg_0_3, 9060)


@RestartOnRest
def Event12205220(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205220: Event 12205220 """
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterOutsideRegion(2, arg_0_3, region=arg_12_15)
    IfHealthLessThanOrEqual(4, arg_0_3, 0.0)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    RestartIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12205230(_, arg_0_3: int, arg_4_7: int):
    """ 12205230: Event 12205230 """
    SetAIParamID(arg_0_3, 114097)
    ReplanAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202620)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=10.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(arg_0_3, arg_4_7)
    ReplanAI(arg_0_3)
    IfAllPlayersOutsideRegion(1, region=2202620)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    Restart()


@RestartOnRest
def Event12205240(_, arg_0_3: int):
    """ 12205240: Event 12205240 """
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(arg_0_3)
    GotoIfFlagDisabled(Label.L0, 12200110)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202250)
    IfCharacterInsideRegion(-2, PLAYER, region=2202251)
    IfCharacterInsideRegion(-2, PLAYER, region=2202252)
    IfCharacterInsideRegion(-2, PLAYER, region=2202253)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, PLAYER, arg_0_3, radius=5.0)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(-5, PLAYER, region=2202250)
    IfCharacterInsideRegion(-5, PLAYER, region=2202251)
    IfCharacterInsideRegion(-5, PLAYER, region=2202253)
    IfConditionTrue(2, input_condition=-5)
    IfConditionTrue(-6, input_condition=2)
    IfEntityWithinDistance(-6, PLAYER, arg_0_3, radius=5.0)
    IfAttacked(-6, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-5)

    # --- 1 --- #
    DefineLabel(1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12205250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205250: Event 12205250 """
    IfCharacterAlive(1, arg_8_11)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=30, slot=0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=10.0)
    IfConditionTrue(-2, input_condition=2)
    IfCharacterInsideRegion(-2, arg_8_11, region=arg_12_15)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3)
    IfConditionTrue(0, input_condition=-2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterOutsideRegion(0, arg_0_3, region=arg_4_7)
    Restart()


@RestartOnRest
def Event12205260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205260: Event 12205260 """
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_12_15)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(arg_0_3)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, arg_0_3, PLAYER, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(-3, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12205265(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12205265: Event 12205265 """
    EndIfFlagEnabled(arg_12_15)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(arg_12_15)
    StopEvent(arg_16_19)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 3000)


@RestartOnRest
def Event12205270(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12205270: Event 12205270 """
    EndIfFlagEnabled(arg_8_11)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_16_19)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(arg_20_23)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12205300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12205300: Event 12205300 """
    DisableSoundEvent(arg_0_3)
    DeleteVFX(2203040, erase_root_only=False)
    EndIfFlagEnabled(arg_12_15)
    CreateVFX(2203040)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(arg_0_3)
    IfFlagEnabled(-1, arg_4_7)
    IfFlagEnabled(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(arg_0_3)
    Restart()


def Event12200990():
    """ 12200990: Event 12200990 """
    EndIfThisEventFlagEnabled()
    IfStandingOnCollision(0, 2203500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 214, PlayLogMultiplayerType.HostOnly)
