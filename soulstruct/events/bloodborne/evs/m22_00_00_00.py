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
236: N:\\SPRJ\\data\\Param\\event\\common.events
312: 
314: 
316: 
318: 
"""
from soulstruct.events.bloodborne import *


@NeverRestart
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
    RunEvent(9220, slot=0, args=(2200710, 12204220, 12204221, 2200, 22, 0), arg_types='iiiiBB')
    RunEvent(9240, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22, 0), arg_types='iiiiBB')
    RunEvent(9260, slot=0, args=(2200710, 12204220, 12204221, 12204222, 22, 0), arg_types='iiiiBB')
    RunEvent(9280, slot=0, args=(2200710, 12204220, 12204221, 2200, 12204800, 22, 0), arg_types='iiiiiBB')
    CreateObjectFX(900110, obj=2201000, model_point=750)
    CreateObjectFX(900110, obj=2201003, model_point=750)
    CreateObjectFX(900110, obj=2201004, model_point=750)
    CreateHazard(12200050, 2201000, model_point=100, behavior_param_id=6010, target_type=DamageTargetType.Character, radius=0.5, life=0.0, repetition_time=1.0)
    CreateHazard(12200051, 2201003, model_point=100, behavior_param_id=6010, target_type=DamageTargetType.Character, radius=0.5, life=0.0, repetition_time=1.0)
    CreateHazard(12200052, 2201004, model_point=100, behavior_param_id=6010, target_type=DamageTargetType.Character, radius=0.5, life=0.0, repetition_time=1.0)
    RegisterLadder(start_climbing_flag=12200000, stop_climbing_flag=12200001, obj=2201100)
    StartPlayLogMeasurement(2200000, 0, overwrite=False)
    StartPlayLogMeasurement(2200001, 18, overwrite=True)
    CreateSpawner(2200420)
    CreateSpawner(2200421)
    CreateSpawner(2200422)
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
    RunEvent(12204814, slot=0, args=(2200800, 12204850, 12204853, 12204850, 12204851, 12204852, 12204853, 12204848), arg_types='iIIiiiii')
    RunEvent(12204814, slot=1, args=(2200801, 12204855, 12204858, 12204855, 12204856, 12204857, 12204858, 12204849), arg_types='iIIiiiii')
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
    RunEvent(12200210, slot=0, args=(2201010, 7.0, 0, 2202020, 10), arg_types='ifiii')
    RunEvent(12200210, slot=1, args=(2201011, 7.0, 30, 2202020, 10), arg_types='ifiii')
    RunEvent(12200210, slot=2, args=(2201016, 7.0, 15, 2202020, 10), arg_types='ifiii')
    RunEvent(12200210, slot=3, args=(2201017, 7.0, 0, 2202020, 10), arg_types='ifiii')
    RunEvent(12200210, slot=4, args=(2201018, 7.0, 5, 2202020, 10), arg_types='ifiii')
    RunEvent(12200210, slot=5, args=(2201012, 10.0, 10, 2202021, 11), arg_types='ifiii')
    RunEvent(12200210, slot=6, args=(2201013, 10.0, 0, 2202021, 11), arg_types='ifiii')
    RunEvent(12200210, slot=7, args=(2201014, 10.0, 30, 2202021, 11), arg_types='ifiii')
    RunEvent(12200210, slot=8, args=(2201015, 10.0, 0, 2202021, 11), arg_types='ifiii')
    RunEvent(12200220, slot=0, args=(2200111, 52200990))
    RunEvent(12200220, slot=1, args=(2200170, 52200980))
    RunEvent(12200220, slot=2, args=(2200110, 52200970))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6631)
    EnableFlag(12201999)
    SkipLinesIfFlagOn(5, 12201999)
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
    SkipLinesIfFlagOff(1, 6309)
    EnableFlag(12201998)
    SkipLinesIfFlagOn(5, 12201998)
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
    RunEvent(12204000, slot=0, args=(2200500, 20.0), arg_types='if')
    RunEvent(12204000, slot=1, args=(2200501, 20.0), arg_types='if')
    RunEvent(12204000, slot=2, args=(2200502, 20.0), arg_types='if')
    RunEvent(12204000, slot=3, args=(2200503, 20.0), arg_types='if')
    RunEvent(12204000, slot=4, args=(2200504, 20.0), arg_types='if')
    RunEvent(12204000, slot=5, args=(2200505, 20.0), arg_types='if')
    RunEvent(12204000, slot=6, args=(2200506, 20.0), arg_types='if')
    RunEvent(12204000, slot=7, args=(2200507, 20.0), arg_types='if')
    RunEvent(12204000, slot=8, args=(2200508, 20.0), arg_types='if')
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
    RunEvent(12205100, slot=0, args=(2200202, 2202130, 3.0, 12205105, 50), arg_types='iifii')
    RunEvent(12205100, slot=1, args=(2200200, 2202150, 3.0, 12205106, 50), arg_types='iifii')
    RunEvent(12205100, slot=2, args=(2200201, 2202151, 3.0, 12205107, 60), arg_types='iifii')
    RunEvent(12205100, slot=3, args=(2200204, 2202152, 5.0, 12205108, 50), arg_types='iifii')
    RunEvent(12205105, slot=0, args=(2200202, 2202130, 3007, 3.0), arg_types='iiif')
    RunEvent(12205105, slot=1, args=(2200200, 2202150, 3009, 2.5), arg_types='iiif')
    RunEvent(12205105, slot=2, args=(2200201, 2202154, 3022, 2.0), arg_types='iiif')
    RunEvent(12205105, slot=3, args=(2200204, 2202153, 3011, 2.700000047683716), arg_types='iiif')
    RunEvent(12205110, slot=0, args=(2200203, 2202140, 3.0, 3006), arg_types='iifi')
    RunEvent(12205120, slot=0, args=(2200211, 2202160, 5.0, 2202161), arg_types='iifi')
    RunEvent(12205120, slot=1, args=(2200212, 2202160, 5.0, 2202161), arg_types='iifi')
    RunEvent(12205120, slot=2, args=(2200213, 2202160, 5.0, 2202161), arg_types='iifi')
    RunEvent(12205120, slot=3, args=(2200223, 2202170, 15.0, 2202171), arg_types='iifi')
    RunEvent(12205120, slot=4, args=(2200224, 2202170, 15.0, 2202171), arg_types='iifi')
    RunEvent(12205120, slot=5, args=(2200230, 2202180, 6.0, 2202180), arg_types='iifi')
    RunEvent(12205120, slot=6, args=(2200231, 2202180, 6.0, 2202180), arg_types='iifi')
    RunEvent(12205120, slot=7, args=(2200232, 2202180, 6.0, 2202180), arg_types='iifi')
    RunEvent(12205120, slot=8, args=(2200240, 2202190, 15.0, 2202191), arg_types='iifi')
    RunEvent(12205120, slot=9, args=(2200250, 2202200, 10.0, 2202201), arg_types='iifi')
    RunEvent(12205120, slot=10, args=(2200251, 2202200, 10.0, 2202201), arg_types='iifi')
    RunEvent(12205120, slot=11, args=(2200252, 2202200, 10.0, 2202201), arg_types='iifi')
    RunEvent(12205120, slot=12, args=(2200260, 2202200, 10.0, 2202201), arg_types='iifi')
    RunEvent(12205120, slot=13, args=(2200261, 2202200, 10.0, 2202201), arg_types='iifi')
    RunEvent(12205120, slot=14, args=(2200270, 2202220, 10.0, 2202221), arg_types='iifi')
    RunEvent(12205120, slot=15, args=(2200271, 2202220, 10.0, 2202221), arg_types='iifi')
    RunEvent(12205120, slot=16, args=(2200272, 2202220, 10.0, 2202221), arg_types='iifi')
    RunEvent(12205120, slot=17, args=(2200290, 2202230, 8.0, 2202231), arg_types='iifi')
    RunEvent(12205120, slot=18, args=(2200291, 2202230, 8.0, 2202231), arg_types='iifi')
    RunEvent(12205120, slot=19, args=(2200292, 2202230, 8.0, 2202231), arg_types='iifi')
    RunEvent(12205120, slot=20, args=(2200280, 2202240, 5.0, 2202240), arg_types='iifi')
    RunEvent(12205120, slot=21, args=(2200412, 2202260, 5.0, 2202260), arg_types='iifi')
    RunEvent(12205120, slot=22, args=(2200310, 2202170, 15.0, 2202171), arg_types='iifi')
    RunEvent(12205120, slot=23, args=(2200450, 2202270, 15.0, 2202271), arg_types='iifi')
    RunEvent(12205120, slot=24, args=(2200460, 2202310, 15.0, 2202310), arg_types='iifi')
    RunEvent(12205120, slot=25, args=(2200470, 2202430, 3.0, 2202431), arg_types='iifi')
    RunEvent(12205120, slot=26, args=(2200430, 2202170, 7.0, 2202171), arg_types='iifi')
    RunEvent(12205150, slot=0, args=(2200100, 7014, 0, 0.0), arg_types='iiif')
    RunEvent(12205150, slot=1, args=(2200301, 7010, 7011, 7.0), arg_types='iiif')
    RunEvent(12205150, slot=2, args=(2200303, 7012, 7013, 0.0), arg_types='iiif')
    RunEvent(12205150, slot=3, args=(2200300, 7014, 0, 0.0), arg_types='iiif')
    RunEvent(12205150, slot=4, args=(2200212, 7014, 0, 0.0), arg_types='iiif')
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


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2203950)
    DisableGravity(2203950)
    DisableCollision(2203950)
    DisableAnimations(2203951)
    DisableGravity(2203951)
    DisableCollision(2203951)
    RunEvent(12204010)


@NeverRestart
def Event12201800():
    """ 12201800: Event 12201800 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2203802)
    DisableMapSound(2203803)
    DisableCharacter(2200800)
    Kill(2200800, award_souls=False)
    DisableCharacter(2200801)
    Kill(2200801, award_souls=False)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteFX(2203800, erase_root_only=True)
    DeleteFX(2203801, erase_root_only=True)
    End()
    Label(0)
    IfCharacterDead(1, 2200800)
    IfCharacterDead(1, 2200801)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2201800)
    DisableObject(2201801)
    DeleteFX(2203800, erase_root_only=True)
    DeleteFX(2203801, erase_root_only=True)
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
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event12201801():
    """ 12201801: Event 12201801 """
    DisableNetworkSync()
    EndIfFlagOn(12201800)
    IfFlagOn(1, 12201800)
    IfCharacterBackreadDisabled(2, 2200800)
    IfHealthLessThanOrEqual(2, 2200800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2202800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


@NeverRestart
def Event12201802():
    """ 12201802: Event 12201802 """
    EndIfFlagOn(12201800)
    EndIfThisEventOn()
    DisableCharacter(2200800)
    IfFlagOff(1, 12201800)
    IfThisEventOff(1)
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
    EndIfFlagOn(9338)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9338)


@NeverRestart
def Event12201803():
    """ 12201803: Event 12201803 """
    GotoIfThisEventOff(Label.L0)
    DisableSpawner(2205000)
    DisableSpawner(2205001)
    DisableSpawner(2205002)
    DisableBackread(2200810)
    DisableBackread(2200811)
    DisableBackread(2200812)
    End()
    Label(0)
    IfFlagOn(0, 12201800)
    DisableSpawner(2205000)
    DisableSpawner(2205001)
    DisableSpawner(2205002)
    Kill(2200810, award_souls=False)
    Kill(2200811, award_souls=False)
    Kill(2200812, award_souls=False)


@NeverRestart
def Event12201804():
    """ 12201804: Event 12201804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12204800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2200800)
    EnableFlag(12204800)
    EnableFlag(12201802)


@NeverRestart
def Event12204890():
    """ 12204890: Event 12204890 """
    EndIfFlagOn(12201800)
    GotoIfFlagOn(Label.L0, 12201802)
    SkipLinesIfClient(2)
    DisableObject(2201800)
    DeleteFX(2203800, erase_root_only=False)
    DisableObject(2201801)
    DeleteFX(2203801, erase_root_only=False)
    IfFlagOff(1, 12201800)
    IfFlagOn(1, 12201802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2201800)
    EnableObject(2201801)
    CreateFX(2203800)
    CreateFX(2203801)
    Label(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2200800, region=2201800)
    IfFlagOff(2, 12201800)
    IfFlagOn(3, 12201800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130, wait_for_completion=False)
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


@NeverRestart
def Event12204891():
    """ 12204891: Event 12204891 """
    DisableNetworkSync()
    EndIfFlagOn(12201800)
    IfFlagOff(1, 12201800)
    IfFlagOn(1, 12201802)
    IfFlagOn(1, 12204800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2200800, region=2201800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2202800, animation=101130, wait_for_completion=False)
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


@NeverRestart
def Event12204892():
    """ 12204892: Event 12204892 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2201800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12204893():
    """ 12204893: Event 12204893 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2201800, radius=2.0)
    IfEntityWithinDistance(1, 10000, 2201800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12204802():
    """ 12204802: Event 12204802 """
    EndIfFlagOn(12201800)
    DisableAI(2200800)
    DisableHealthBar(2200800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12204800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200800, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12204800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2200800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200800)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2200800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200800)
    Goto(Label.L4)
    Label(4)
    EnableAI(2200800)
    EnableBossHealthBar(2200800, name=210000, slot=0)
    CreatePlayLog(88)
    StartPlayLogMeasurement(2200010, 104, overwrite=True)


@NeverRestart
def Event12204803():
    """ 12204803: Event 12204803 """
    DisableNetworkSync()
    EndIfFlagOn(12201800)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2203802)
    DisableMapSound(2203803)
    IfFlagOff(1, 12201800)
    IfFlagOn(1, 12204802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12204801)
    IfCharacterInsideRegion(1, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2203802, state=True)
    IfHealthValueEqual(-1, 2200800, 1)
    IfHealthValueEqual(-1, 2200801, 1)
    IfConditionTrue(2, input_condition=-1)
    Label(0)
    IfFlagOff(2, 12201800)
    IfFlagOn(2, 12204802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12204801)
    IfCharacterInsideRegion(2, PLAYER, region=2202801)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2203802, state=False)
    WaitFrames(0)
    SetBossMusicState(2203803, state=True)


@NeverRestart
def Event12204804():
    """ 12204804: Event 12204804 """
    EndIfFlagOn(12201800)
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12204800)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfFlagOn(2, 12204801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=HEMWICK_CHARNEL_LANE, camera_slot=1)


@NeverRestart
def Event12204805():
    """ 12204805: Event 12204805 """
    DisableNetworkSync()
    EndIfFlagOn(12201800)
    IfFlagOn(0, 12201800)
    SetBossMusicState(2203802, state=False)
    SetBossMusicState(2203803, state=False)
    SetBossMusicState(-1, state=False)


@NeverRestart
def Event12204807():
    """ 12204807: Event 12204807 """
    EndIfFlagOn(12201800)
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


@NeverRestart
def Event12204808(ARG_0_3: int, ARG_4_7: int):
    """ 12204808: Event 12204808 """
    EndIfFlagOn(12201800)
    DisableNetworkSync()
    IfEntityBeyondDistance(1, 10000, ARG_0_3, radius=12.0)
    IfHasTAEEvent(3, ARG_0_3, tae_event_id=10)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect_WithUnknownEffect(ARG_0_3, 5686, affect_npc_parts_hp=False)
    Label(0)
    IfEntityWithinDistance(2, 10000, ARG_0_3, radius=6.0)
    IfFlagOff(2, ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect_WithUnknownEffect(ARG_0_3, 5688, affect_npc_parts_hp=False)
    Restart()


@NeverRestart
def Event12204810():
    """ 12204810: Event 12204810 """
    EndIfFlagOn(12201800)
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200801)
    DisableHealthBar(2200801)
    DisableCharacter(2200801)
    IfHealthLessThanOrEqual(0, 2200800, 0.5)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2200801, UpdateAuthority.Forced)
    Label(0)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2200801, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200801)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2200801, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2200801)
    Goto(Label.L4)
    Label(4)
    EnableCharacter(2200801)
    EnableAI(2200801)


@NeverRestart
def Event12204811():
    """ 12204811: Event 12204811 """
    EndIfFlagOn(12201800)
    GotoIfThisEventOn(Label.L0)
    SetAIParamID(2200800, 210021)
    IfCharacterDead(-1, 2200810)
    IfDamageType(-1, attacked_entity=2200800, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    SetAIParamID(2200800, 210020)


@NeverRestart
def Event12204812(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12204812: Event 12204812 """
    EndIfFlagOn(12201800)
    EnableImmortality(ARG_0_3)
    IfHealthValueEqual(3, ARG_0_3, 1)
    IfHealthValueLessThan(3, ARG_4_7, 1)
    IfHealthValueEqual(4, ARG_0_3, 1)
    IfHealthValueEqual(4, ARG_4_7, 1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    Wait(0.0)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(ARG_0_3, 7000)
    WaitFrames(75)
    ForceAnimation(ARG_0_3, 7001, loop=True)
    IfTimeElapsed(1, 45.0)
    IfHealthValueEqual(2, ARG_4_7, 1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    AddSpecialEffect(ARG_0_3, 5686, affect_npc_part_hp=False)
    Wait(3.0)
    DisableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 0)
    Move(ARG_0_3, destination=ARG_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    AddSpecialEffect(ARG_0_3, 5698, affect_npc_part_hp=False)
    Wait(3.0)
    EnableCharacter(ARG_0_3)
    ReplanAI(ARG_0_3)
    DisableFlag(ARG_12_15)
    Restart()
    Label(0)
    Kill(ARG_0_3, award_souls=False)
    Kill(ARG_4_7, award_souls=False)


@NeverRestart
def Event12204814(ARG_0_3: int, ARG_4_7: uint, ARG_8_11: uint, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 12204814: Event 12204814 """
    EndIfFlagOn(12201800)
    IfHasTAEEvent(0, ARG_0_3, tae_event_id=30)
    AddSpecialEffect(ARG_0_3, 5686, affect_npc_part_hp=False)
    IfHasTAEEvent(1, ARG_0_3, tae_event_id=10)
    IfHealthValueNotEqual(1, ARG_0_3, 1)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    EnableRandomFlagInRange((ARG_4_7, ARG_8_11))
    GotoIfFlagOff(Label.L1, ARG_12_15)
    DisableFlagRange((ARG_12_15, ARG_24_27))
    EnableFlag(ARG_12_15)
    Goto(Label.L0)
    Label(1)
    GotoIfFlagOff(Label.L2, ARG_16_19)
    DisableFlagRange((ARG_12_15, ARG_24_27))
    EnableFlag(ARG_16_19)
    Goto(Label.L0)
    Label(2)
    GotoIfFlagOff(Label.L3, ARG_20_23)
    DisableFlagRange((ARG_12_15, ARG_24_27))
    EnableFlag(ARG_20_23)
    Goto(Label.L0)
    Label(3)
    GotoIfFlagOff(Label.L0, ARG_24_27)
    DisableFlagRange((ARG_12_15, ARG_24_27))
    EnableFlag(ARG_24_27)
    Label(0)
    IfFlagOn(-1, ARG_12_15)
    IfFlagOn(-1, ARG_16_19)
    IfFlagOn(-1, ARG_20_23)
    IfFlagOn(-1, ARG_24_27)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_28_31)
    Restart()


@NeverRestart
def Event12204820(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12204820: Event 12204820 """
    EndIfFlagOn(12201800)
    IfFlagOn(0, ARG_4_7)
    DisableFlag(ARG_4_7)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_8_11)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableCharacter(ARG_0_3)
    Move(ARG_0_3, destination=ARG_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Goto(Label.L1)
    Label(0)
    DisableCharacter(ARG_0_3)
    Move(ARG_0_3, destination=ARG_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Label(1)
    EnableFlag(ARG_16_19)
    Restart()


@NeverRestart
def Event12204830(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12204830: Event 12204830 """
    EndIfFlagOn(12201800)
    DisableNetworkSync()
    IfFlagOn(0, ARG_4_7)
    Wait(2.0)
    EnableCharacter(ARG_0_3)
    ReplanAI(ARG_0_3)
    DisableFlag(ARG_8_11)
    DisableFlag(ARG_4_7)
    Restart()


@NeverRestart
def Event12204832(ARG_0_3: int):
    """ 12204832: Event 12204832 """
    EndIfFlagOn(12201800)
    IfCharacterDead(0, ARG_0_3)
    IncrementEventValue(12204860, bit_count=10, max_value=10)
    IfHasTAEEvent(0, ARG_0_3, tae_event_id=10)
    Restart()


@NeverRestart
def Event12204835(ARG_0_3: int, ARG_4_7: int):
    """ 12204835: Event 12204835 """
    EndIfFlagOn(12201800)
    IfCharacterDead(0, ARG_0_3)
    EnableFlag(ARG_4_7)
    IfHasTAEEvent(0, ARG_0_3, tae_event_id=10)
    DisableFlag(ARG_4_7)
    Restart()


@NeverRestart
def Event12204838():
    """ 12204838: Event 12204838 """
    EndIfFlagOn(12201800)
    IfFlagOff(4, 12204845)
    IfConditionTrue(0, input_condition=4)
    IfHasTAEEvent(-1, 2200800, tae_event_id=20)
    IfHasTAEEvent(-1, 2200801, tae_event_id=20)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 12204870)
    IfHasTAEEvent(-2, 2200800, tae_event_id=20)
    IfHasTAEEvent(-2, 2200801, tae_event_id=20)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOn(2, 12204871)
    IfHasTAEEvent(-3, 2200800, tae_event_id=20)
    IfHasTAEEvent(-3, 2200801, tae_event_id=20)
    IfConditionTrue(3, input_condition=-3)
    IfFlagOn(3, 12204872)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    EnableSpawner(2205000)
    IfHasTAEEvent(0, 2200810, tae_event_id=10)
    DisableSpawner(2205000)
    Restart()
    Label(0)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=2)
    EnableSpawner(2205001)
    IfHasTAEEvent(0, 2200811, tae_event_id=10)
    DisableSpawner(2205001)
    Restart()
    Label(1)
    EnableSpawner(2205002)
    IfHasTAEEvent(0, 2200812, tae_event_id=10)
    DisableSpawner(2205002)
    Restart()


@RestartOnRest
def Event12204839():
    """ 12204839: Event 12204839 """
    EndIfFlagOn(12201800)
    IfFlagOff(1, 12204845)
    IfConditionTrue(0, input_condition=1)
    IfHealthValueEqual(-1, 2200800, 1)
    IfHealthValueEqual(-1, 2200801, 1)
    IfConditionTrue(-2, input_condition=-1)
    IfFlagOn(-2, 12204812)
    IfFlagOn(2, 12201802)
    IfThisEventOff(2)
    IfFlagOff(2, 12201810)
    IfEventValueEqual(3, 12204860, bit_count=10, value=3)
    IfFlagOff(3, 12204875)
    IfHealthLessThanOrEqual(4, 2200800, 0.30000001192092896)
    IfEventValueComparison(4, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfFlagOff(4, 12204875)
    IfHealthLessThanOrEqual(5, 2200801, 0.5)
    IfEventValueComparison(5, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfFlagOff(5, 12204875)
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
    Label(1)
    IfHealthValueEqual(8, 2200800, 1)
    IfHealthValueNotEqual(9, 2200800, 1)
    IfConditionTrue(-7, input_condition=8)
    IfConditionTrue(-7, input_condition=9)
    GotoIfConditionTrue(Label.L2, input_condition=8)
    ResetAnimation(2200800, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(2200800, 3011)
    Goto(Label.L3)
    Label(2)
    ResetAnimation(2200801, disable_interpolation=False)
    Wait(0.10000000149011612)
    ForceAnimation(2200801, 3011)
    Label(3)
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
    Label(4)
    ForceAnimation(2200810, 6200)
    EnableCharacter(2200810)
    EnableAnimations(2200810)
    DisableSpawner(2205000)
    EnableFlag(12204876)
    EnableFlag(12201810)
    Restart()
    Label(5)
    ForceAnimation(2200811, 6200)
    EnableCharacter(2200811)
    EnableAnimations(2200811)
    DisableSpawner(2205001)
    EnableFlag(12204875)
    Restart()
    Label(6)
    ForceAnimation(2200812, 6200)
    EnableCharacter(2200812)
    EnableAnimations(2200812)
    DisableSpawner(2205002)
    End()


@RestartOnRest
def Event12204840():
    """ 12204840: Event 12204840 """
    EndIfFlagOn(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOff(5, 12204845)
    IfConditionTrue(0, input_condition=5)
    IfEventValueComparison(1, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    IfFlagOn(2, 12204870)
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
    Label(1)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=15.0)
    AICommand(2200800, command_id=10, slot=2)
    ReplanAI(2200800)
    Label(2)
    IfFlagOff(0, 12204870)
    AICommand(2200800, command_id=-1, slot=2)
    ReplanAI(2200800)
    Restart()
    Label(0)
    EnableFlag(12204880)


@RestartOnRest
def Event12204841():
    """ 12204841: Event 12204841 """
    EndIfFlagOn(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 12204880)
    IfEventValueComparison(1, 12204860, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=5)
    IfEventValueComparison(2, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=4)
    IfFlagOn(2, 12204870)
    IfEventValueComparison(3, 12204860, bit_count=10, comparison_type=ComparisonType.LessThanOrEqual, value=4)
    IfFlagOn(3, 12204871)
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
    Label(1)
    WaitRandomSeconds(min_seconds=10.0, max_seconds=20.0)
    AICommand(2200800, command_id=10, slot=2)
    ReplanAI(2200800)
    Label(2)
    IfFlagOff(4, 12204870)
    IfFlagOff(4, 12204871)
    IfConditionTrue(0, input_condition=4)
    AICommand(2200800, command_id=-1, slot=2)
    ReplanAI(2200800)
    Restart()
    Label(0)
    EnableFlag(12204881)


@RestartOnRest
def Event12204842():
    """ 12204842: Event 12204842 """
    EndIfFlagOn(12201800)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 12204881)
    IfFlagOn(-1, 12204870)
    IfFlagOn(-1, 12204871)
    IfFlagOn(-1, 12204872)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=15.0, max_seconds=25.0)
    AICommand(2200800, command_id=10, slot=2)
    AICommand(2200801, command_id=10, slot=2)
    ReplanAI(2200800)
    ReplanAI(2200801)
    IfFlagOff(1, 12204870)
    IfFlagOff(1, 12204871)
    IfFlagOff(1, 12204872)
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
    IfFlagOff(1, 12201810)
    EndIfConditionTrue(1)
    GotoIfThisEventOn(Label.L0)
    IfFlagOff(0, 12204845)
    Label(0)
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


@NeverRestart
def Event12200100():
    """ 12200100: Event 12200100 """
    GotoIfThisEventOff(Label.L0)
    EndOfAnimation(2201001, 1)
    DisableObjectActivation(2201001, obj_act_id=2200010)
    NotifyDoorEventSoundDampening(2201001, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=12200101)
    CreatePlayLog(122)
    Wait(0.0)


@NeverRestart
def Event12200101():
    """ 12200101: Event 12200101 """
    GotoIfThisEventOff(Label.L0)
    EndOfAnimation(2201060, 0)
    DisableObjectActivation(2201060, obj_act_id=2200030)
    NotifyDoorEventSoundDampening(2201060, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=12200500)
    Wait(0.0)


@NeverRestart
def Event12200110():
    """ 12200110: Event 12200110 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(2201002, 1)
    DisableObjectActivation(2201220, obj_act_id=100)
    NotifyDoorEventSoundDampening(2201002, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=12200112)
    CreatePlayLog(158)
    DisableObjectActivation(2201220, obj_act_id=100)
    ForceAnimation(2201002, 1)
    Wait(0.0)


@NeverRestart
def Event12200111():
    """ 12200111: Event 12200111 """
    DisableNetworkSync()
    EndIfFlagOn(12200110)
    IfActionButtonInRegion(1, action_button_id=2200000, region=2201002)
    IfActionButtonInRegion(2, action_button_id=2200001, region=2201002)
    IfFlagOn(3, 12200110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    DisplayDialog(10010160, anchor_entity=2201002, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart
def Event12200112():
    """ 12200112: Event 12200112 """
    DisableNetworkSync()
    IfFlagOn(1, 12200110)
    IfActionButtonInRegion(1, action_button_id=7100, region=2201220)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=2201220, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart
def Event12200120():
    """ 12200120: Event 12200120 """
    IfFlagOn(1, 12200125)
    IfFlagOff(2, 12200125)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    EndOfAnimation(2201210, 0)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)
    Goto(Label.L1)
    Label(0)
    EndOfAnimation(2201210, 4)
    EnableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    Label(1)
    GotoIfFlagOn(Label.L2, 12200121)
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    Label(2)


@NeverRestart
def Event12200121():
    """ 12200121: Event 12200121 """
    EndIfThisEventSlotOn()
    DisableObjectActivation(2201200, obj_act_id=100)
    DisableObjectActivation(2201201, obj_act_id=100)
    IfCharacterInsideRegion(0, PLAYER, region=2202010)
    CreatePlayLog(186)
    DisableObjectActivation(2201200, obj_act_id=100)
    EnableObjectActivation(2201201, obj_act_id=100)


@NeverRestart
def Event12200122():
    """ 12200122: Event 12200122 """
    IfFlagOff(3, 12200125)
    IfFlagOn(3, 12200126)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOff(1, 12200125)
    IfFlagOff(1, 12200126)
    IfCharacterInsideRegion(1, PLAYER, region=2202000)
    IfFlagOff(2, 12200125)
    IfFlagOff(2, 12200126)
    IfObjectActivated(2, obj_act_id=12200128)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
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


@NeverRestart
def Event12200123():
    """ 12200123: Event 12200123 """
    IfFlagOn(3, 12200125)
    IfFlagOn(3, 12200126)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(1, 12200125)
    IfFlagOff(1, 12200126)
    IfCharacterInsideRegion(1, PLAYER, region=2202001)
    IfFlagOn(2, 12200125)
    IfFlagOff(2, 12200126)
    IfObjectActivated(2, obj_act_id=12200127)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
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


@NeverRestart
def Event12200124():
    """ 12200124: Event 12200124 """
    DisableNetworkSync()
    IfFlagOff(1, 12200121)
    IfActionButtonInRegion(1, action_button_id=7100, region=2201200)
    IfFlagOff(2, 12200121)
    IfActionButtonInRegion(2, action_button_id=7100, region=2201201)
    IfFlagOff(3, 12200126)
    IfFlagOff(3, 12200125)
    IfActionButtonInRegion(3, action_button_id=7100, region=2201200)
    IfFlagOff(4, 12200126)
    IfFlagOn(4, 12200125)
    IfActionButtonInRegion(4, action_button_id=7100, region=2201201)
    IfFlagOn(5, 12200126)
    IfActionButtonInRegion(5, action_button_id=7100, region=2201200)
    IfFlagOn(6, 12200126)
    IfActionButtonInRegion(6, action_button_id=7100, region=2201201)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event12200130():
    """ 12200130: Event 12200130 """
    DisableCharacter(2201310)
    DisableObject(2201300)
    DisableHealthBar(2201310)
    EndIfFlagOn(12507810)
    GotoIfThisEventOn(Label.L0)
    IfPlayerHasGood(1, 4003, including_box=False)
    IfFlagOn(1, 12201800)
    IfCharacterInsideRegion(1, PLAYER, region=2202410)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(22000030, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(12204020)
    Label(0)
    EnableCharacter(2201310)
    EnableObject(2201300)
    DisableHealthBar(2201310)


@RestartOnRest
def Event12200131():
    """ 12200131: Event 12200131 """
    EndIfFlagOn(12507810)
    IfFlagOn(1, 12200130)
    IfCharacterAlive(1, 2201310)
    IfActionButtonInRegion(1, action_button_id=2200010, region=2201300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(22000040, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    MovePlayerToRespawnPoint(2502959)


@RestartOnRest
def Event12200132():
    """ 12200132: Event 12200132 """
    EndIfFlagOn(12507810)
    IfHealthLessThanOrEqual(0, 2201310, 0.0)
    StopEvent(12200131, slot=0)


@RestartOnRest
def Event12200150(ARG_0_3: int, ARG_4_7: int):
    """ 12200150: Event 12200150 """
    EndIfFlagOn(12200130)
    IfFlagOn(0, 12204020)
    IfCharacterInsideRegion(1, ARG_0_3, region=2202640)
    EndIfConditionFalse(1)
    Move(ARG_0_3, destination=ARG_4_7, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)


@RestartOnRest
def Event12200210(ARG_0_3: int, ARG_4_7: float, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12200210: Event 12200210 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(ARG_0_3, ARG_16_19)
    DisableObject(ARG_0_3)
    End()
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-1, ARG_0_3, 10000, radius=ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(ARG_8_11)
    ForceAnimation(ARG_0_3, ARG_16_19, wait_for_completion=True)
    DisableObject(ARG_0_3)


@RestartOnRest
def Event12200220(ARG_0_3: int, ARG_4_7: int):
    """ 12200220: Event 12200220 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(ARG_0_3)
    End()
    Label(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@NeverRestart
def Event12200300():
    """ 12200300: Event 12200300 """
    GotoIfFlagOn(Label.L2, 9802)
    GotoIfFlagOn(Label.L1, 9801)
    GotoIfFlagOn(Label.L0, 9800)
    Label(0)
    EnableMapPart(2206000)
    DisableMapPart(2206001)
    Goto(Label.L3)
    Label(1)
    DisableMapPart(2206000)
    EnableMapPart(2206001)
    Goto(Label.L3)
    Label(2)
    DisableMapPart(2206000)
    EnableMapPart(2206001)
    Label(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart
def Event12200310(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12200310: Event 12200310 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_8_11)
    EnableTreasure(ARG_0_3)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@RestartOnRest
def Event12204000(ARG_0_3: int, ARG_4_7: float):
    """ 12204000: Event 12204000 """
    GotoIfFlagOn(Label.L0, 12204011)
    DisableCharacter(ARG_0_3)
    End()
    Label(0)
    DisableCharacter(ARG_0_3)
    IfFlagOn(-1, 9801)
    IfFlagOn(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=ARG_4_7)
    IfCharacterHuman(1, PLAYER)
    IfThisEventSlotOn(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 6200)


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
    EndIfFlagOn(12205001)
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2202061)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    StopEvent(12205001, slot=0)
    EnableAI(2200120)
    SetNest(2200120, 2202360)
    AICommand(2200120, command_id=10, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205001():
    """ 12205001: Event 12205001 """
    EndIfFlagOn(12205000)
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200120)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202062)
    IfCharacterInsideRegion(-2, PLAYER, region=2202060)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, 10000, 2200120, radius=10.0)
    IfAttacked(-3, 2200120, attacking_character=10000)
    IfConditionTrue(0, input_condition=-3)
    Label(0)
    StopEvent(12205000, slot=0)
    EnableAI(2200120)


@RestartOnRest
def Event12205002():
    """ 12205002: Event 12205002 """
    GotoIfThisEventOn(Label.L0)
    IfCharacterInsideRegion(1, 2200120, region=2202360)
    IfHasAIStatus(1, 2200120, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2200120, 3006)
    Label(0)
    AICommand(2200120, command_id=-1, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205003():
    """ 12205003: Event 12205003 """
    EndIfThisEventOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 10000, 2200120, radius=4.0)
    IfConditionTrue(-2, input_condition=1)
    IfDamageType(-2, attacked_entity=2200120, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHasAIStatus(-2, 2200120, ai_status=AIStatusType.Battle)
    IfFlagOn(-2, 12205002)
    IfConditionTrue(0, input_condition=-2)
    AICommand(2200120, command_id=-1, slot=0)
    ReplanAI(2200120)


@RestartOnRest
def Event12205010(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12205010: Event 12205010 """
    EndIfFlagOn(ARG_20_23)
    GotoIfThisEventSlotOn(Label.L0)
    DisableAI(ARG_4_7)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_8_11)
    IfHasAIStatus(1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, ARG_4_7, 10000, radius=7.0)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=ARG_16_19)
    IfDamageType(4, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    EnableAI(ARG_4_7)
    SetNest(ARG_4_7, ARG_12_15)
    AICommand(ARG_4_7, command_id=20, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event12205015(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205015: Event 12205015 """
    EndIfThisEventSlotOn()
    IfFlagOn(0, ARG_12_15)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=7.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, ARG_0_3, region=ARG_4_7)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-2)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12205040():
    """ 12205040: Event 12205040 """
    EndIfFlagOn(12205041)
    GotoIfThisEventOn(Label.L0)
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
    Label(0)
    AddSpecialEffect(2200211, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(2200211, patrol_information_id=2203030)
    ReplanAI(2200211)


@RestartOnRest
def Event12205041():
    """ 12205041: Event 12205041 """
    EndIfThisEventOn()
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
    GotoIfThisEventOn(Label.L0)
    ForceAnimation(2200140, 7004, loop=True)
    SetAIParamID(2200140, 261091)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionFalse(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=2202080)
    IfHasAIStatus(2, 2200140, ai_status=AIStatusType.Alert)
    IfEntityWithinDistance(2, 2200140, 10000, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    SetAIParamID(2200140, 261003)
    ForceAnimation(2200140, 7005)


@RestartOnRest
def Event12205030():
    """ 12205030: Event 12205030 """
    GotoIfThisEventOn(Label.L0)
    IfCharacterInsideRegion(1, PLAYER, region=2202090)
    IfEntityWithinDistance(2, 10000, 2200150, radius=10.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    Label(0)
    SetNest(2200150, 2202390)
    AICommand(2200150, command_id=10, slot=0)
    ReplanAI(2200150)


@RestartOnRest
def Event12205031():
    """ 12205031: Event 12205031 """
    EndIfThisEventOn()
    IfCharacterInsideRegion(1, 2200150, region=2202390)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(2, 10000, 2200150, radius=3.5)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    ResetAnimation(2200150, disable_interpolation=False)
    RotateToFaceEntity(2200150, 10000, animation=3001, wait_for_completion=False)
    Label(0)
    AICommand(2200150, command_id=-1, slot=0)
    ReplanAI(2200150)


@RestartOnRest
def Event12205050():
    """ 12205050: Event 12205050 """
    EndIfFlagOn(12205051)
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200280)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200280, 10000, radius=3.0)
    IfDamageType(2, attacked_entity=2200280, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHasAIStatus(3, 2200270, ai_status=AIStatusType.Battle)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    EnableAI(2200280)
    EndIfFinishedConditionFalse(3)
    Wait(5.0)
    SetNest(2200280, 2209005)
    AICommand(2200280, command_id=10, slot=0)
    ReplanAI(2200280)


@RestartOnRest
def Event12205051():
    """ 12205051: Event 12205051 """
    GotoIfThisEventOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200280, 10000, radius=5.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, 2200280, region=2209005)
    IfDamageType(-2, attacked_entity=2200280, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    AICommand(2200280, command_id=-1, slot=0)
    ReplanAI(2200280)


@RestartOnRest
def Event12205060():
    """ 12205060: Event 12205060 """
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200170)
    DisableGravity(2200170)
    EnableInvincibility(2200170)
    IfObjectDestroyed(-1, 2201030)
    IfObjectDestroyed(-1, 2201031)
    IfObjectDestroyed(-1, 2201032)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    DisableInvincibility(2200170)
    EnableGravity(2200170)
    EnableAI(2200170)
    ReplanAI(2200170)


@RestartOnRest
def Event12205070():
    """ 12205070: Event 12205070 """
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200411)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2200411, 100000, radius=10.0)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, 2200160, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, 2200161, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    EnableAI(2200411)
    ReplanAI(2200411)


@RestartOnRest
def Event12205080():
    """ 12205080: Event 12205080 """
    GotoIfThisEventOn(Label.L0)
    DisableAI(2200205)
    IfCharacterInsideRegion(1, PLAYER, region=2202155)
    IfCharacterInsideRegion(2, PLAYER, region=2202156)
    IfAttacked(3, 2200205, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2200205, 10000, animation=3012, wait_for_completion=False)
    Label(0)
    WaitFrames(35)
    EnableAI(2200205)


@RestartOnRest
def Event12205100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int, ARG_16_19: int):
    """ 12205100: Event 12205100 """
    EndIfFlagOn(ARG_12_15)
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, 10000, ARG_0_3, radius=ARG_8_11)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    SetCharacterEventTarget(ARG_0_3, 10000)
    AICommand(ARG_0_3, command_id=ARG_16_19, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12205105(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 12205105: Event 12205105 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=ARG_12_15)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, 10000, ARG_0_3, radius=ARG_12_15)
    IfCharacterOutsideRegion(2, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_8_11, wait_for_completion=False)
    Label(1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12205110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 12205110: Event 12205110 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_12_15, wait_for_completion=False)
    EnableAI(ARG_0_3)
    End()
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12205120(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 12205120: Event 12205120 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfAttacked(2, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12205150(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 12205150: Event 12205150 """
    EndIfThisEventSlotOn()
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Alert)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(ARG_0_3, ARG_8_11)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12205160(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205160: Event 12205160 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfObjectNotDestroyed(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(ARG_8_11, ARG_12_15)
    AICommand(ARG_8_11, command_id=100, slot=0)
    ReplanAI(ARG_8_11)
    IfHasTAEEvent(0, ARG_8_11, tae_event_id=100)
    AICommand(ARG_8_11, command_id=-1, slot=0)
    ReplanAI(ARG_8_11)
    Restart()


@RestartOnRest
def Event12205170(ARG_0_3: int, ARG_4_7: int):
    """ 12205170: Event 12205170 """
    GotoIfThisEventSlotOff(Label.L1)
    PostDestruction(ARG_0_3, slot=1)
    End()
    Label(1)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Fire)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Magic)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Lightning)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Blunt)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Slash)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, ARG_0_3, ComparisonType.LessThanOrEqual, 999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(owner_entity=ARG_4_7, projectile_id=ARG_0_3, model_point=-1, behavior_id=6051, launch_angle_x=270, launch_angle_y=0, launch_angle_z=0)
    DestroyObject(ARG_0_3, slot=1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()
    Label(0)
    ShootProjectile(owner_entity=ARG_4_7, projectile_id=ARG_0_3, model_point=-1, behavior_id=6055, launch_angle_x=270, launch_angle_y=0, launch_angle_z=0)
    ShootProjectile(owner_entity=ARG_4_7, projectile_id=ARG_0_3, model_point=-1, behavior_id=6071, launch_angle_x=0, launch_angle_y=90, launch_angle_z=0)
    DestroyObject(ARG_0_3, slot=1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@RestartOnRest
def Event12205200(ARG_0_3: int):
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
    AICommand(ARG_0_3, command_id=100, slot=0)
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
    AICommand(ARG_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12205210(ARG_0_3: int):
    """ 12205210: Event 12205210 """
    EndIfThisEventSlotOn()
    ForceAnimation(ARG_0_3, 9003, loop=True)
    SetAIParamID(ARG_0_3, 117007)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(2, ARG_0_3, ai_status=AIStatusType.Alert)
    IfEntityWithinDistance(2, ARG_0_3, 10000, radius=5.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfAttacked(3, ARG_0_3, attacking_character=10000)
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
    IfEntityWithinDistance(8, ARG_0_3, 10000, radius=3.0)
    IfConditionTrue(8, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(ARG_0_3, 117000)
    ForceAnimation(ARG_0_3, 9060)


@RestartOnRest
def Event12205220(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205220: Event 12205220 """
    IfCharacterBackreadEnabled(1, ARG_0_3)
    IfHasAIStatus(1, ARG_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfHealthLessThanOrEqual(3, ARG_0_3, 0.0)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(3)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    ForceAnimation(ARG_0_3, ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Alert)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfCharacterOutsideRegion(2, ARG_0_3, region=ARG_12_15)
    IfHealthLessThanOrEqual(4, ARG_0_3, 0.0)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    RestartIfFinishedConditionTrue(2)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    ForceAnimation(ARG_0_3, 0, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12205230(ARG_0_3: int, ARG_4_7: int):
    """ 12205230: Event 12205230 """
    SetAIParamID(ARG_0_3, 114097)
    ReplanAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202620)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=10.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-3)
    SetAIParamID(ARG_0_3, ARG_4_7)
    ReplanAI(ARG_0_3)
    IfAllPlayersOutsideRegion(1, region=2202620)
    IfHasAIStatus(1, ARG_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    Restart()


@RestartOnRest
def Event12205240(ARG_0_3: int):
    """ 12205240: Event 12205240 """
    GotoIfThisEventSlotOn(Label.L1)
    DisableAI(ARG_0_3)
    GotoIfFlagOff(Label.L0, 12200110)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2202250)
    IfCharacterInsideRegion(-2, PLAYER, region=2202251)
    IfCharacterInsideRegion(-2, PLAYER, region=2202252)
    IfCharacterInsideRegion(-2, PLAYER, region=2202253)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfEntityWithinDistance(-3, 10000, ARG_0_3, radius=5.0)
    IfAttacked(-3, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-3)
    Goto(Label.L1)
    Label(0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(-5, PLAYER, region=2202250)
    IfCharacterInsideRegion(-5, PLAYER, region=2202251)
    IfCharacterInsideRegion(-5, PLAYER, region=2202253)
    IfConditionTrue(2, input_condition=-5)
    IfConditionTrue(-6, input_condition=2)
    IfEntityWithinDistance(-6, 10000, ARG_0_3, radius=5.0)
    IfAttacked(-6, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-5)
    Label(1)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12205250(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205250: Event 12205250 """
    IfCharacterAlive(1, ARG_8_11)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfHasAIStatus(1, ARG_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=30, slot=0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, ARG_0_3, 10000, radius=10.0)
    IfConditionTrue(-2, input_condition=2)
    IfCharacterInsideRegion(-2, ARG_8_11, region=ARG_12_15)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-2)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterOutsideRegion(0, ARG_0_3, region=ARG_4_7)
    Restart()


@RestartOnRest
def Event12205260(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205260: Event 12205260 """
    EndIfFlagOn(ARG_8_11)
    EndIfFlagOn(ARG_12_15)
    GotoIfThisEventSlotOn(Label.L0)
    DisableAI(ARG_0_3)
    AddSpecialEffect(ARG_0_3, 5000, affect_npc_part_hp=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(-2, ARG_0_3, 10000, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfDamageType(-3, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    Label(0)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12205265(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12205265: Event 12205265 """
    EndIfFlagOn(ARG_12_15)
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-2, ARG_0_3, region=ARG_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(ARG_12_15, slot=0)
    StopEvent(ARG_16_19, slot=0)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    ForceAnimation(ARG_0_3, 3000)


@RestartOnRest
def Event12205270(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12205270: Event 12205270 """
    EndIfFlagOn(ARG_8_11)
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, ARG_0_3, region=ARG_16_19)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-2)
    StopEvent(ARG_20_23, slot=0)
    EnableAI(ARG_0_3)
    SetNest(ARG_0_3, ARG_4_7)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12205300(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12205300: Event 12205300 """
    DisableMapSound(ARG_0_3)
    DeleteFX(2203040, erase_root_only=False)
    EndIfFlagOn(ARG_12_15)
    CreateFX(2203040)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(ARG_0_3)
    IfFlagOn(-1, ARG_4_7)
    IfFlagOn(-1, ARG_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableMapSound(ARG_0_3)
    Restart()


@NeverRestart
def Event12200990():
    """ 12200990: Event 12200990 """
    EndIfThisEventOn()
    IfStandingOnHitbox(0, 2203500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 214, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 214, PlayLogMultiplayerType.HostOnly)
