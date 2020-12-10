"""YAHAR'GUL

linked:
298

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: 生贄の街_テレポーター使用_00
74: 生贄の街_テレポーター使用_01
108: 生贄の街_テレポーター領域侵入_00
146: 生贄の街_テレポーター領域侵入_01
184: 
186: ボス_撃破
198: PC情報_ボス撃破_なりそこないの邪神
238: ボス_戦闘開始
254: ボス戦_撃破時間
272: PC情報_生贄の街到達時
298: N:\\SPRJ\\data\\Param\\event\\common.emevd
374: 
376: 
378: 
380: 
382: 
"""
from soulstruct.events.bloodborne import *
from .common_entities import *
from .m28_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RegisterLadder(start_climbing_flag=12800350, stop_climbing_flag=12800351, obj=2801250)
    RunEvent(7600, slot=60, args=(2801999, 2803999))
    RunEvent(7600, slot=61, args=(2801998, 2803998))
    RunEvent(7000, slot=40, args=(2800950, 2801950, 999, 12807800))
    RunEvent(7000, slot=41, args=(2800951, 2801951, Flags.OneRebornDead, 12807820))
    SkipLinesIfFlagOn(1, 9802)
    RunEvent(7000, slot=42, args=(2800952, 2801952, 999, 12807840))
    RunEvent(7000, slot=43, args=(2800953, 2801953, 999, 12807860))
    RunEvent(7100, slot=40, args=(72800200, 2801950))
    RunEvent(7100, slot=41, args=(72800201, 2801951))
    SkipLinesIfFlagOn(1, 9802)
    RunEvent(7100, slot=42, args=(72800202, 2801952))
    RunEvent(7100, slot=43, args=(72800203, 2801953))
    RunEvent(7200, slot=40, args=(72800100, 2801950, 2102952))
    RunEvent(7200, slot=41, args=(72800101, 2801951, 2102952))
    SkipLinesIfFlagOn(1, 9802)
    RunEvent(7200, slot=42, args=(72800102, 2801952, 2102952))
    RunEvent(7200, slot=43, args=(72800103, 2801953, 2102953))
    RunEvent(7300, slot=40, args=(72102800, 2801950))
    RunEvent(7300, slot=41, args=(72102801, 2801951))
    SkipLinesIfFlagOn(1, 9802)
    RunEvent(7300, slot=42, args=(72102802, 2801952))
    RunEvent(7300, slot=43, args=(72102803, 2801953))
    Event12800140()
    RunEvent(9200, slot=8, args=(2803900,))
    Event12800160()
    RunEvent(9220, slot=7, args=(2800710, 12804220, 12804221, 2800, 28, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=7, args=(2800710, 12804220, 12804221, 12804222, 28, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=7, args=(2800710, 12804220, 12804221, 12804222, 28, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=7, args=(2800710, 12804220, 12804221, 2800, 12804223, 28, 0), arg_types="iiiiiBB")
    Event12800999()
    Event12800435()
    Event12800436()
    Event12800400()
    Event12800401()
    Event12800402()
    Event12800403()
    CreateObjectFX(900130, obj=2801010, model_point=200)
    StartPlayLogMeasurement(2800000, 0, overwrite=True)
    StartPlayLogMeasurement(2800001, 18, overwrite=True)
    Event12800990()
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6322)
    EnableFlag(12801999)
    SkipLinesIfFlagOn(5, 12801999)
    EnableObject(2801550)
    DisableObject(2801551)
    EnableTreasure(2801550)
    DisableTreasure(2801551)
    SkipLines(4)
    DisableObject(2801550)
    EnableObject(2801551)
    DisableTreasure(2801550)
    EnableTreasure(2801551)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagOff(1, 6323)
    EnableFlag(12801998)
    SkipLinesIfFlagOn(5, 12801998)
    EnableObject(2801552)
    DisableObject(2801553)
    EnableTreasure(2801552)
    DisableTreasure(2801553)
    SkipLines(4)
    DisableObject(2801552)
    EnableObject(2801553)
    DisableTreasure(2801552)
    EnableTreasure(2801553)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagOff(1, 6324)
    EnableFlag(12801997)
    SkipLinesIfFlagOn(5, 12801997)
    EnableObject(2801554)
    DisableObject(2801555)
    EnableTreasure(2801554)
    DisableTreasure(2801555)
    SkipLines(4)
    DisableObject(2801554)
    EnableObject(2801555)
    DisableTreasure(2801554)
    EnableTreasure(2801555)
    Event12800901()
    Event12800902()
    Event12800903()
    Event12800904()
    Event12800905()
    Event12800906()
    Event12800908()
    Event12800909()
    Event12800910()
    DeleteFX(2803920, erase_root_only=False)
    DeleteFX(2803921, erase_root_only=False)
    RunEvent(12804400, slot=0, args=(12804440, 2803920, 12804420, 12804430, Flags.OneRebornDead, 12804421))
    RunEvent(12804401, slot=0, args=(12804441, 2803921, 12804421, 12804431, Flags.OneRebornDead, 12804420))
    RunEvent(12804410, slot=0, args=(5, 2800910, 2802910, 12804420, 12804430, 12804440, Flags.OneRebornDead, 10564))
    RunEvent(12804410, slot=1, args=(0, 2800911, 2802913, 12804421, 12804431, 12804441, Flags.OneRebornDead, 10568))
    RunEvent(12804450, slot=0, args=(2800910, 2802911, 12804420, 12804430, Flags.OneRebornFogEntered))
    RunEvent(12804450, slot=1, args=(2800911, 2802914, 12804421, 12804431, Flags.OneRebornFogEntered))
    RunEvent(12804460, slot=0, args=(2800910, 2802911, 2802800, 2802801, 101130, 12804450, 2802801))
    RunEvent(12804460, slot=1, args=(2800911, 2802914, 2802800, 2802801, 101130, 12804451, 2802801))

    # THE ONE REBORN
    Event12804882()
    Event12804883()
    OneRebornDies()
    PlayOneRebornDeathSound()
    OneRebornFirstTime()
    EnterOneRebornFog()
    EnterOneRebornFogAsSummon()
    StartOneRebornBattle()
    ControlOneRebornMusic()
    ControlOneRebornCamera()
    StopOneRebornMusic()
    KeepOneRebornHumanPartAttached()
    MonitorOneRebornStunned()
    SummonStartOneRebornBattle()
    OneRebornLimbDamage(0, 2800, 2800, 1, 100, 480, 490, 7000)
    OneRebornLimbDamage(1, 2801, 2801, 2, 200, 481, 491, 7001)
    OneRebornLimbDamage(2, 2802, 2802, 3, 200, 482, 492, 7002)
    OneRebornLimbDamage(3, 2803, 2803, 4, 100, 483, 493, 7003)
    OneRebornLimbDamage(4, 2804, 2804, 5, 200, 484, 494, 7004)
    OneRebornLimbDamage(5, 2805, 2805, 6, 200, 485, 495, 7005)
    OneRebornLimbDamage(6, 2806, 2806, 7, 100, 486, 496, 7006)
    OneRebornSingleRainOfFlesh()
    OneRebornExplosion()
    OneRebornFootBlast1()
    OneRebornFootBlast2()
    OneRebornFootBlast3()
    OneRebornFootBlast4()
    OneRebornRepeatedRainOfFlesh()
    OneRebornSummonsRepeatedRainOfFlesh()
    OneRebornBuffMaidenDies(0, Characters.OneRebornMaiden2)
    OneRebornBuffMaidenDies(1, Characters.OneRebornMaiden5)
    CountDeadOneRebornMaidens(0, Characters.OneRebornMaiden1)  # counted in event 12804860
    CountDeadOneRebornMaidens(2, Characters.OneRebornMaiden2)
    CountDeadOneRebornMaidens(4, Characters.OneRebornMaiden3)
    CountDeadOneRebornMaidens(5, Characters.OneRebornMaiden4)
    CountDeadOneRebornMaidens(7, Characters.OneRebornMaiden5)
    CountDeadOneRebornMaidens(9, Characters.OneRebornMaiden6)
    OneRebornTakesFirstDamage()
    OneRebornPhaseTwoTrigger()

    RunEvent(12800100, slot=0, args=(2801350, 12800250))
    RunEvent(12800100, slot=1, args=(2801351, 12800251))
    RunEvent(12800100, slot=2, args=(2801352, 12800252))
    RunEvent(12800100, slot=3, args=(2801353, 12800253))
    RunEvent(12800100, slot=4, args=(2801354, 12800254))
    RunEvent(12800100, slot=5, args=(2801355, 12800255))
    RunEvent(12800120, slot=0, args=(2801010, 7413, 10012013))
    RunEvent(12800480, slot=0, args=(2801200, 12800201, 1, 31))
    RunEvent(12800480, slot=1, args=(2801202, 12800202, 1, 30))
    RunEvent(12800480, slot=2, args=(2801203, 12800203, 1, 30))
    RunEvent(12800480, slot=3, args=(2801206, 12800206, 1, 30))
    RunEvent(12800480, slot=4, args=(2801208, 12800209, 1, 2800020))
    RunEvent(12800490, slot=0, args=(7030, 2801200, 12800480))
    RunEvent(12800490, slot=1, args=(7031, 2801202, 12800481))
    RunEvent(12800490, slot=2, args=(7031, 2801203, 12800482))
    RunEvent(12800490, slot=3, args=(7031, 2801206, 12800483))
    RunEvent(12800490, slot=4, args=(7030, 2801208, 12800484))
    Event12800430()
    Event12800431()
    Event12800432()
    RunEvent(12800433, slot=0, args=(2800740,))
    RunEvent(12800433, slot=1, args=(2800745,))
    RunEvent(12805160, slot=0, args=(2800244, 2802230, 1.0), arg_types="iif")
    RunEvent(12805160, slot=1, args=(2800245, 2802230, 1.0), arg_types="iif")
    RunEvent(12805160, slot=2, args=(2800243, 2802230, 1.0), arg_types="iif")
    RunEvent(12805180, slot=2, args=(2800210, 2802270))
    RunEvent(12805470, slot=0, args=(11, 11, 7, 7003, 5907, 12805655, 12805665, 2800210), arg_types="hihiiiii")
    RunEvent(12805470, slot=1, args=(12, 12, 8, 7000, 5907, 12805655, 12805665, 2800210), arg_types="hihiiiii")
    RunEvent(12805480, slot=0, args=(11, 11, 7, 80, 12805655, 2800210), arg_types="hihiii")
    RunEvent(12805480, slot=1, args=(12, 12, 8, 80, 12805655, 2800210), arg_types="hihiii")
    RunEvent(12805490, slot=0, args=(10, 40, 12805665, 2800210))
    RunEvent(12805490, slot=1, args=(30, 40, 12805665, 2800210))
    RunEvent(12800500, slot=1, args=(2800721, 52800980))
    RunEvent(12800500, slot=2, args=(2800722, 52800970))
    RunEvent(12800500, slot=0, args=(2800720, 52800990))
    RunEvent(12800500, slot=3, args=(2800723, 52800960))
    GotoIfFlagOff(Label.L4, 9802)
    RunEvent(12800600, slot=0, args=(12804700, 12800610, 12800611, 12800612, 2801400, 2801401, 2801402))
    RunEvent(12800601, slot=0, args=(12804700, 12800610, 12800611, 12800612))
    RunEvent(12800602, slot=0, args=(12804700, 12800610, 12800611, 12800612, 2802102, 12800280))
    RunEvent(12800604, slot=0, args=(12804700, 12800610, 12800611, 12800612, 2802101, 12800281))
    RunEvent(12800606, slot=0, args=(12804700, 12800610, 12800612, 2801401, 2801402))
    RunEvent(12800607, slot=0, args=(12800612, 2802100, 2801401, 2801402))
    RunEvent(12800470, slot=0, args=(2800742, 7000))
    RunEvent(12800470, slot=1, args=(2800743, 7001))
    RunEvent(12800470, slot=2, args=(2800744, 7003))
    RunEvent(12800460, slot=0, args=(2801100, 2802001, 40), arg_types="iis")
    RunEvent(12800460, slot=1, args=(2801101, 2802000, 74), arg_types="iis")
    RunEvent(12800620, slot=0, args=(2802880, 108), arg_types="is")
    RunEvent(12800620, slot=1, args=(2802881, 146), arg_types="is")
    RunEvent(12800700, slot=0, args=(2800700,))
    RunEvent(12800700, slot=1, args=(2800701,))
    RunEvent(12800700, slot=2, args=(2800702,))
    RunEvent(12805500, slot=0, args=(2800482, 2802483, 2803482, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=1, args=(2800483, 2802483, 2803483, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=2, args=(2800562, 2802562, 2803562, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=3, args=(2800570, 2802570, 2803570, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=4, args=(2800571, 2802570, 2803571, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=5, args=(2800540, 2802540, 2803540, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=6, args=(2800542, 2802542, 2803542, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=7, args=(2800543, 2802543, 2803543, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=8, args=(2800301, 2802301, 2803301, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=9, args=(2800308, 2802602, 2803308, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=10, args=(2800309, 2802602, 2803309, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=11, args=(2800310, 2802602, 2803310, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=12, args=(2800311, 2802602, 2803311, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=13, args=(2800312, 2802602, 2803312, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=14, args=(2800313, 2802602, 2803313, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=15, args=(2800314, 2802602, 2803314, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=16, args=(2800315, 2802602, 2803315, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=17, args=(2800316, 2802502, 2803316, 1.0), arg_types="iiif")
    RunEvent(12805500, slot=18, args=(2800317, 2802502, 2803317, 3.0), arg_types="iiif")
    RunEvent(12805500, slot=19, args=(2800404, 2802507, 2803404, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=20, args=(2800405, 2802507, 2803405, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=21, args=(2800406, 2802507, 2803406, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=22, args=(2800407, 2802507, 2803407, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=23, args=(2800461, 2802461, 2803461, 0.0), arg_types="iiif")
    RunEvent(12805600, slot=0, args=(2800400, 7010, 261800, 7011, 261800, 2802400, 12805042, 1))
    RunEvent(12805600, slot=1, args=(2800401, 7012, 261840, 7013, 261840, 2802400, 12805042, 1))
    RunEvent(12805600, slot=2, args=(2800402, 7011, 261811, 0, 261811, 2802400, 12805042, 1))
    RunEvent(12805600, slot=3, args=(2800403, 7012, 261810, 7013, 261810, 2802400, 12805042, 1))
    RunEvent(12805600, slot=4, args=(2800408, 7010, 261800, 7011, 261800, 0, 12805042, 0))
    RunEvent(12805600, slot=6, args=(2800410, 7010, 261840, 7011, 261840, 0, 12805042, 0))
    RunEvent(12805600, slot=7, args=(2800411, 7012, 261810, 7013, 261810, 0, 12805042, 0))
    RunEvent(12805600, slot=10, args=(2800382, 7010, 264801, 7011, 264800, 0, 12805042, 0))
    RunEvent(12805600, slot=30, args=(2800318, 0, 263851, 3013, 263850, 0, 12805040, 1))
    RunEvent(12805600, slot=31, args=(2800305, 0, 263851, 3013, 263850, 0, 12805040, 1))
    RunEvent(12805650, slot=0, args=(2800400, 2802400, 2802401, 10, 12805660))
    RunEvent(12805650, slot=1, args=(2800401, 2802400, 2802402, 10, 12805661))
    RunEvent(12805650, slot=2, args=(2800402, 2802400, 2802403, 10, 12805662))
    RunEvent(12805650, slot=3, args=(2800403, 2802400, 2802404, 10, 12805663))
    RunEvent(12805650, slot=4, args=(2800480, 2802480, 2802481, 10, 12805664))
    RunEvent(12805650, slot=6, args=(2800329, 2802329, 2802330, 10, 12805666))
    RunEvent(12805660, slot=0, args=(2800400, 2802401))
    RunEvent(12805660, slot=1, args=(2800401, 2802402))
    RunEvent(12805660, slot=2, args=(2800402, 2802403))
    RunEvent(12805660, slot=3, args=(2800403, 2802404))
    RunEvent(12805660, slot=4, args=(2800480, 2802481))
    RunEvent(12805660, slot=6, args=(2800329, 2802330))
    RunEvent(12805670, slot=0, args=(2800400, 10, 12805660, 0, 0.0), arg_types="iiiif")
    RunEvent(12805670, slot=1, args=(2800401, 10, 12805661, 0, 0.0), arg_types="iiiif")
    RunEvent(12805670, slot=2, args=(2800402, 10, 12805662, 0, 0.0), arg_types="iiiif")
    RunEvent(12805670, slot=3, args=(2800403, 10, 12805663, 0, 0.0), arg_types="iiiif")
    RunEvent(12805670, slot=4, args=(2800480, 10, 12805664, 0, 0.0), arg_types="iiiif")
    RunEvent(12805670, slot=6, args=(2800329, 10, 12805666, 1, 2.0), arg_types="iiiif")
    RunEvent(12805680, slot=0, args=(2800501, 2802506, 1.0), arg_types="iif")
    DisableSpawner(2803000)
    DisableSpawner(2803001)
    DisableSpawner(2803002)
    DisableSpawner(2803003)
    DisableSpawner(2803004)
    DisableSpawner(2803005)
    DisableSpawner(2803006)
    DisableSpawner(2803007)
    DisableSpawner(2803008)
    DisableSpawner(2803009)
    DisableSpawner(2803010)
    DisableSpawner(2803011)
    DisableSpawner(2803012)
    DisableSpawner(2803013)
    DisableSpawner(2803014)
    DisableSpawner(2803015)
    DisableSpawner(2803016)
    DisableSpawner(2803017)
    DisableSpawner(2803018)
    DisableSpawner(2803019)
    DisableSpawner(2803020)
    DisableSpawner(2803021)
    DisableSpawner(2803022)
    DisableSpawner(2803023)
    DisableSpawner(2803024)
    DisableSpawner(2803025)
    DisableSpawner(2803026)
    DisableSpawner(2803028)
    DisableSpawner(2803080)
    DisableSpawner(2803082)
    DisableSpawner(2803083)
    DisableSpawner(2803084)
    DisableSpawner(2803100)
    DisableSpawner(2803101)
    DisableSpawner(2803102)
    DisableSpawner(2803103)
    DisableSpawner(2803104)
    DisableSpawner(2803105)
    DisableSpawner(2803106)
    DisableSpawner(2803107)
    DisableSpawner(2803108)
    DisableSpawner(2803110)
    DisableSpawner(2803111)
    DisableSpawner(2803160)
    DisableSpawner(2803161)
    DisableSpawner(2803162)
    DisableSpawner(2803163)
    DisableSpawner(2803180)
    DisableSpawner(2803181)
    DisableSpawner(2803182)
    DisableSpawner(2803183)
    RunEvent(12804500, slot=2, args=(12805030, 2803002, 12805040, 2800302, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=3, args=(12805030, 2803003, 12805040, 2800303, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=1, args=(9802, 2803001, 12805040, 2800301, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=0, args=(9802, 2803000, 12805040, 2800300, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=160, args=(9802, 2803160, 12805040, 2800460, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=4, args=(9802, 2803004, 12805044, 2800304, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=5, args=(9802, 2803005, 12805044, 2800305, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=6, args=(9802, 2803006, 12805044, 2800306, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=7, args=(9802, 2803007, 12805044, 2800307, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=182, args=(9802, 2803182, 12805044, 2800482, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=183, args=(9802, 2803183, 12805044, 2800483, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=8, args=(9802, 2803008, 12805040, 2800308, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=9, args=(9802, 2803009, 12805040, 2800309, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=10, args=(9802, 2803010, 12805040, 2800310, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=11, args=(9802, 2803011, 12805040, 2800311, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=12, args=(9802, 2803012, 12805040, 2800312, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=13, args=(9802, 2803013, 12805040, 2800313, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=14, args=(9802, 2803014, 12805040, 2800314, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=15, args=(9802, 2803015, 12805040, 2800315, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=16, args=(12805031, 2803016, 12805040, 2800316, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=17, args=(12805031, 2803017, 12805040, 2800317, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=18, args=(9802, 2803018, 12805040, 2800318, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=20, args=(12805021, 2803020, 12805041, 2800320, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=21, args=(12805021, 2803021, 12805041, 2800321, 0, 0, 0.5), arg_types="iiiiiif")
    RunEvent(12804500, slot=80, args=(12805021, 2803080, 12805041, 2800380, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=19, args=(12805022, 2803019, 12805041, 2800319, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=162, args=(12805022, 2803162, 12805041, 2800462, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=100, args=(9802, 2803100, 12805042, 2800400, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=101, args=(9802, 2803101, 12805042, 2800401, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=102, args=(9802, 2803102, 12805042, 2800402, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=103, args=(9802, 2803103, 12805042, 2800403, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=108, args=(9802, 2803108, 12805042, 2800408, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=110, args=(9802, 2803110, 12805042, 2800410, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=111, args=(9802, 2803111, 12805042, 2800411, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=82, args=(9802, 2803082, 12805042, 2800382, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=83, args=(9802, 2803083, 12805042, 2800383, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=161, args=(9802, 2803161, 12805042, 2800461, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=104, args=(9802, 2803104, 12805042, 2800404, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=105, args=(9802, 2803105, 12805042, 2800405, 0, 0, 0.5), arg_types="iiiiiif")
    RunEvent(12804500, slot=106, args=(9802, 2803106, 12805042, 2800406, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=107, args=(9802, 2803107, 12805042, 2800407, 0, 0, 1.5), arg_types="iiiiiif")
    RunEvent(12804500, slot=22, args=(12805023, 2803022, 12805043, 2800322, 0, 0, 0.5), arg_types="iiiiiif")
    RunEvent(12804500, slot=23, args=(12805023, 2803023, 12805043, 2800323, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=84, args=(12805023, 2803084, 12805043, 2800384, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=24, args=(9802, 2803024, 12805043, 2800324, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=25, args=(9802, 2803025, 12805043, 2800325, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=180, args=(9802, 2803180, 12805043, 2800480, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=181, args=(9802, 2803181, 12805043, 2800481, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=26, args=(12805033, 2803026, 12805045, 2800326, 0, 0, 0.0), arg_types="iiiiiif")
    RunEvent(12804500, slot=27, args=(12805033, 2803027, 12805045, 2800327, 0, 0, 0.5), arg_types="iiiiiif")
    RunEvent(12804500, slot=28, args=(12805025, 2803028, 12805045, 2800328, 0, 0, 1.0), arg_types="iiiiiif")
    RunEvent(12805020, slot=0, args=(2800500, 2802504))
    RunEvent(12805020, slot=1, args=(2800501, 2802505))
    RunEvent(12805020, slot=2, args=(2800501, 2802506))
    RunEvent(12805020, slot=3, args=(2800503, 2802509))
    RunEvent(12805020, slot=4, args=(2800504, 2802514))
    RunEvent(12805020, slot=5, args=(2800505, 2802513))
    RunEvent(12805030, slot=0, args=(2802500, 2802501, 12805030, 12805040))
    RunEvent(12805030, slot=1, args=(2802502, 2802503, 12805031, 12805040))
    RunEvent(12805030, slot=2, args=(2802507, 2802508, 12805032, 12805042))
    RunEvent(12805030, slot=3, args=(2802511, 2802512, 12805033, 12805045))
    RunEvent(12805040, slot=0, args=(2800500,))
    RunEvent(12805040, slot=1, args=(2800501,))
    RunEvent(12805040, slot=2, args=(2800502,))
    RunEvent(12805040, slot=3, args=(2800503,))
    RunEvent(12805040, slot=4, args=(2800504,))
    RunEvent(12805040, slot=5, args=(2800505,))
    RunEvent(12805700, slot=0, args=(2800500, 2800300, 0, 0))
    RunEvent(12805700, slot=1, args=(2800500, 2800301, 0, 0))
    RunEvent(12805700, slot=2, args=(2800500, 2800302, 0, 0))
    RunEvent(12805700, slot=3, args=(2800500, 2800303, 0, 0))
    RunEvent(12805700, slot=4, args=(2800504, 2800304, 0, 0))
    RunEvent(12805700, slot=5, args=(2800504, 2800305, 0, 0))
    RunEvent(12805700, slot=6, args=(2800504, 2800306, 0, 0))
    RunEvent(12805700, slot=7, args=(2800504, 2800307, 0, 0))
    RunEvent(12805700, slot=8, args=(2800500, 2800308, 0, 0))
    RunEvent(12805700, slot=9, args=(2800500, 2800309, 0, 0))
    RunEvent(12805700, slot=10, args=(2800500, 2800310, 0, 0))
    RunEvent(12805700, slot=11, args=(2800500, 2800311, 0, 0))
    RunEvent(12805700, slot=12, args=(2800500, 2800312, 0, 0))
    RunEvent(12805700, slot=13, args=(2800500, 2800313, 0, 0))
    RunEvent(12805700, slot=14, args=(2800500, 2800314, 0, 0))
    RunEvent(12805700, slot=15, args=(2800500, 2800315, 0, 0))
    RunEvent(12805700, slot=16, args=(2800500, 2800316, 0, 0))
    RunEvent(12805700, slot=17, args=(2800500, 2800317, 0, 0))
    RunEvent(12805700, slot=18, args=(2800500, 2800318, 0, 0))
    RunEvent(12805700, slot=19, args=(2800501, 2800319, 0, 0))
    RunEvent(12805700, slot=20, args=(2800501, 2800320, 0, 0))
    RunEvent(12805700, slot=21, args=(2800501, 2800321, 0, 0))
    RunEvent(12805700, slot=22, args=(2800503, 2800322, 0, 0))
    RunEvent(12805700, slot=23, args=(2800503, 2800323, 0, 0))
    RunEvent(12805700, slot=24, args=(2800503, 2800324, 0, 0))
    RunEvent(12805700, slot=25, args=(2800503, 2800325, 0, 0))
    RunEvent(12805700, slot=26, args=(2800505, 2800326, 0, 0))
    RunEvent(12805700, slot=27, args=(2800505, 2800327, 0, 0))
    RunEvent(12805700, slot=28, args=(2800505, 2800328, 0, 0))
    RunEvent(12805700, slot=80, args=(2800501, 2800380, 0, 0))
    RunEvent(12805700, slot=82, args=(2800502, 2800382, 0, 0))
    RunEvent(12805700, slot=83, args=(2800502, 2800383, 0, 0))
    RunEvent(12805700, slot=84, args=(2800503, 2800384, 0, 0))
    RunEvent(12805700, slot=100, args=(2800502, 2800400, 0, 0))
    RunEvent(12805700, slot=101, args=(2800502, 2800401, 0, 0))
    RunEvent(12805700, slot=102, args=(2800502, 2800402, 0, 0))
    RunEvent(12805700, slot=103, args=(2800502, 2800403, 0, 0))
    RunEvent(12805700, slot=104, args=(2800502, 2800404, 0, 0))
    RunEvent(12805700, slot=105, args=(2800502, 2800405, 0, 0))
    RunEvent(12805700, slot=106, args=(2800502, 2800406, 0, 0))
    RunEvent(12805700, slot=107, args=(2800502, 2800407, 0, 0))
    RunEvent(12805700, slot=108, args=(2800502, 2800408, 0, 0))
    RunEvent(12805700, slot=110, args=(2800502, 2800410, 0, 0))
    RunEvent(12805700, slot=111, args=(2800502, 2800411, 0, 0))
    RunEvent(12805700, slot=160, args=(2800500, 2800460, 0, 0))
    RunEvent(12805700, slot=161, args=(2800502, 2800461, 0, 0))
    RunEvent(12805700, slot=162, args=(2800501, 2800462, 0, 0))
    RunEvent(12805700, slot=180, args=(2800503, 2800480, 0, 0))
    RunEvent(12805700, slot=181, args=(2800503, 2800481, 0, 0))
    RunEvent(12805700, slot=182, args=(2800504, 2800482, 0, 0))
    RunEvent(12805700, slot=183, args=(2800504, 2800483, 0, 0))
    RunEvent(12804000, slot=0, args=(2800300,))
    RunEvent(12804000, slot=1, args=(2800301,))
    RunEvent(12804000, slot=2, args=(2800302,))
    RunEvent(12804000, slot=3, args=(2800303,))
    RunEvent(12804000, slot=4, args=(2800304,))
    RunEvent(12804000, slot=5, args=(2800305,))
    RunEvent(12804000, slot=6, args=(2800306,))
    RunEvent(12804000, slot=7, args=(2800307,))
    RunEvent(12804000, slot=8, args=(2800308,))
    RunEvent(12804000, slot=9, args=(2800309,))
    RunEvent(12804000, slot=10, args=(2800310,))
    RunEvent(12804000, slot=11, args=(2800311,))
    RunEvent(12804000, slot=12, args=(2800312,))
    RunEvent(12804000, slot=13, args=(2800313,))
    RunEvent(12804000, slot=14, args=(2800314,))
    RunEvent(12804000, slot=15, args=(2800315,))
    RunEvent(12804000, slot=16, args=(2800316,))
    RunEvent(12804000, slot=17, args=(2800317,))
    RunEvent(12804000, slot=18, args=(2800318,))
    RunEvent(12804000, slot=19, args=(2800319,))
    RunEvent(12804000, slot=20, args=(2800320,))
    RunEvent(12804000, slot=21, args=(2800321,))
    RunEvent(12804000, slot=22, args=(2800322,))
    RunEvent(12804000, slot=23, args=(2800323,))
    RunEvent(12804000, slot=24, args=(2800324,))
    RunEvent(12804000, slot=25, args=(2800325,))
    RunEvent(12804000, slot=26, args=(2800326,))
    RunEvent(12804000, slot=27, args=(2800327,))
    RunEvent(12804000, slot=28, args=(2800328,))
    RunEvent(12804000, slot=80, args=(2800380,))
    RunEvent(12804000, slot=82, args=(2800382,))
    RunEvent(12804000, slot=83, args=(2800383,))
    RunEvent(12804000, slot=84, args=(2800384,))
    RunEvent(12804000, slot=100, args=(2800400,))
    RunEvent(12804000, slot=101, args=(2800401,))
    RunEvent(12804000, slot=102, args=(2800402,))
    RunEvent(12804000, slot=103, args=(2800403,))
    RunEvent(12804000, slot=104, args=(2800404,))
    RunEvent(12804000, slot=105, args=(2800405,))
    RunEvent(12804000, slot=106, args=(2800406,))
    RunEvent(12804000, slot=107, args=(2800407,))
    RunEvent(12804000, slot=108, args=(2800408,))
    RunEvent(12804000, slot=110, args=(2800410,))
    RunEvent(12804000, slot=111, args=(2800411,))
    RunEvent(12804000, slot=160, args=(2800460,))
    RunEvent(12804000, slot=161, args=(2800461,))
    RunEvent(12804000, slot=162, args=(2800462,))
    RunEvent(12804000, slot=180, args=(2800480,))
    RunEvent(12804000, slot=181, args=(2800481,))
    RunEvent(12804000, slot=182, args=(2800482,))
    RunEvent(12804000, slot=183, args=(2800483,))
    Event12805918()
    RunEvent(12805900, slot=0, args=(2800562,))
    RunEvent(12805900, slot=1, args=(2800563,))
    RunEvent(12805900, slot=2, args=(2800564,))
    RunEvent(12805900, slot=4, args=(2800566,))
    RunEvent(12805900, slot=5, args=(2800567,))
    RunEvent(12805900, slot=7, args=(2800569,))
    RunEvent(12805900, slot=8, args=(2800570,))
    RunEvent(12805900, slot=9, args=(2800571,))
    RunEvent(12805900, slot=10, args=(2800572,))
    RunEvent(12805900, slot=11, args=(2800573,))
    RunEvent(12805920, slot=0, args=(2801600, 12805942))
    RunEvent(12805920, slot=1, args=(2801601, 12805947))
    RunEvent(12805920, slot=2, args=(2801602, 12805952))
    RunEvent(12805920, slot=3, args=(2801603, 12805957))
    RunEvent(12805930, slot=0, args=(12805940, 12805942, 2801600))
    RunEvent(12805930, slot=1, args=(12805945, 12805947, 2801601))
    RunEvent(12805930, slot=2, args=(12805950, 12805952, 2801602))
    RunEvent(12805930, slot=3, args=(12805955, 12805957, 2801603))
    Event12805050()
    Goto(Label.L5)

    # --- 4 --- #
    DefineLabel(4)
    Event12800608()
    RunEvent(12805460, slot=4, args=(2800104, 7012, 7013, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805460, slot=5, args=(2800105, 7014, 7015, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805460, slot=6, args=(2800106, 7010, 7011, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805460, slot=7, args=(2800107, 7012, 7013, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805460, slot=8, args=(2800108, 7014, 7015, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805460, slot=9, args=(2800109, 7010, 7011, 2.0, 263899, 263890), arg_types="iiifii")
    RunEvent(12805500, slot=30, args=(2800160, 2802160, 2803160, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=31, args=(2800140, 2802140, 2803140, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=32, args=(2800141, 2802140, 2803141, 0.0), arg_types="iiif")
    RunEvent(12805500, slot=33, args=(2800200, 2802200, 2803200, 0.0), arg_types="iiif")
    RunEvent(12805550, slot=6, args=(2800608, 2802608, 8.0), arg_types="iif")
    RunEvent(12805650, slot=6, args=(2800160, 2802160, 2802161, 10, 12805666))
    RunEvent(12805660, slot=6, args=(2800160, 2802161))
    RunEvent(12805670, slot=6, args=(2800160, 10, 12805666, 0, 0.0), arg_types="iiiif")

    # --- 5 --- #
    DefineLabel(5)


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2800740)
    DisableGravity(2800740)
    DisableCharacterCollision(2800740)
    SetNetworkUpdateRate(2800740, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800741)
    DisableGravity(2800741)
    DisableCharacterCollision(2800741)
    SetNetworkUpdateRate(2800741, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800742)
    DisableGravity(2800742)
    DisableCharacterCollision(2800742)
    SetNetworkUpdateRate(2800742, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800743)
    DisableGravity(2800743)
    DisableCharacterCollision(2800743)
    SetNetworkUpdateRate(2800743, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800744)
    DisableGravity(2800744)
    DisableCharacterCollision(2800744)
    SetNetworkUpdateRate(2800744, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800745)
    DisableGravity(2800745)
    DisableCharacterCollision(2800745)
    SetNetworkUpdateRate(2800745, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.On)
    DisableAnimations(2800990)
    DisableGravity(2800990)
    DisableCharacterCollision(2800990)
    SetNetworkUpdateRate(2800990, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(2800990, state=True)
    DisableAnimations(2800991)
    DisableGravity(2800991)
    DisableCharacterCollision(2800991)
    SetNetworkUpdateRate(2800991, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(2800991, state=True)
    Event12800911()


@RestartOnRest
def Event12804500(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: float
):
    """ 12804500: Event 12804500 """
    GotoIfFlagOn(Label.L1, arg_8_11)
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableCharacter(arg_12_15)
    IfFlagOn(0, arg_0_3)
    Wait(arg_24_27)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_12_15, 6200, wait_for_completion=True)

    # --- 0 --- #
    DefineLabel(0)
    EnableSpawner(arg_4_7)
    IfFlagOn(1, arg_8_11)
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfFlagOn(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)

    # --- 1 --- #
    DefineLabel(1)
    DisableSpawner(arg_4_7)


@RestartOnRest
def Event12805020(_, arg_0_3: int, arg_4_7: int):
    """ 12805020: Event 12805020 """
    EndIfThisEventSlotOn()
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 3010)
    IfHasTAEEvent(0, arg_0_3, tae_event_id=30)
    Wait(0.0)


@RestartOnRest
def Event12805030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12805030: Event 12805030 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHuman(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfFlagOff(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006003)
    WaitFrames(20)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    EnableFlag(arg_8_11)
    WaitFrames(13)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(9)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(11)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(9)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(6)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(9)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(8)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)
    WaitFrames(11)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.c_CharacterMotion, sound_id=105006102)


@RestartOnRest
def Event12805040(_, arg_0_3: int):
    """ 12805040: Event 12805040 """
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


@RestartOnRest
def Event12805050():
    """ 12805050: Event 12805050 """
    GotoIfThisEventOn(Label.L0)
    DisableAI(2800563)
    IfCharacterBackreadEnabled(0, 2800563)
    Move(2800563, destination=2802564, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(2800563, 7005, loop=True)
    ForceAnimation(2801965, 1, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2802563)
    IfConditionTrue(0, input_condition=1)
    Move(2800563, destination=2802564, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(2800563, 7006)
    ForceAnimation(2801965, 2, wait_for_completion=True)
    EnableAI(2800563)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2801965, 3, loop=True)
    SetNest(2800563, 2802565)


def Event12805140(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12805140: Event 12805140 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacking_character=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


def Event12805160(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12805160: Event 12805160 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacking_character=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12805180(_, arg_0_3: int, arg_4_7: int):
    """ 12805180: Event 12805180 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=4.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacking_character=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12805460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 12805460: Event 12805460 """
    GotoIfThisEventSlotOff(Label.L0)
    SetAIParamID(arg_0_3, arg_20_23)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_16_19)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_20_23)
    EnableGravity(arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11)


@RestartOnRest
def Event12805470(
    _,
    arg_0_1: short,
    arg_4_7: int,
    arg_8_9: short,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12805470: Event 12805470 """
    IfFlagOn(0, arg_20_23)
    IfCharacterPartHealthLessThanOrEqual(1, arg_28_31, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, arg_28_31, 0.0)
    IfFlagOn(2, arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, arg_20_23)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_hp=1, overwrite_max=False)
    Restart()
    CreateNPCPart(
        arg_28_31,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=999999,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_special_effect_id=65, material_fx_id=65)
    ResetAnimation(arg_28_31, disable_interpolation=False)
    ForceAnimation(arg_28_31, arg_12_15)
    IfHasTAEEvent(0, arg_28_31, tae_event_id=400)
    AddSpecialEffect(arg_28_31, arg_16_19, affect_npc_part_hp=False)
    DisableFlag(arg_24_27)
    IfHasTAEEvent(0, arg_28_31, tae_event_id=300)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_hp=80, overwrite_max=True)
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_special_effect_id=64, material_fx_id=64)
    CancelSpecialEffect(arg_28_31, arg_16_19)
    AICommand(arg_28_31, command_id=-1, slot=0)
    ReplanAI(arg_28_31)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12805480(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12805480: Event 12805480 """
    IfCharacterBackreadEnabled(1, arg_20_23)
    IfEntityWithinDistance(1, arg_20_23, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_20_23,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_20_23, npc_part_id=arg_4_7, material_special_effect_id=64, material_fx_id=64)
    EnableFlag(arg_16_19)


@RestartOnRest
def Event12805490(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12805490: Event 12805490 """
    IfHasTAEEvent(0, arg_12_15, tae_event_id=arg_0_3)
    EnableFlag(arg_8_11)
    IfHasTAEEvent(0, arg_12_15, tae_event_id=arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


@RestartOnRest
def Event12805500(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 12805500: Event 12805500 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Wait(arg_12_15)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_8_11)
    ReplanAI(arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterAlive(0, arg_0_3)
    Restart()


@RestartOnRest
def Event12805550(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12805550: Event 12805550 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12805570(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12805570: Event 12805570 """
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    DisableAI(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Wait(15.0)
    EnableAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_8_11)
    DisableAI(arg_0_3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Wait(15.0)
    EnableAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12805600(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12805600: Event 12805600 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(2, arg_24_27)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    SkipLinesIfEqual(2, left=arg_28_31, right=1)
    ForceAnimation(arg_0_3, arg_12_15)
    SkipLines(1)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 0)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event12805650(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12805650: Event 12805650 """
    EndIfFlagOn(arg_16_19)
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    AICommand(arg_0_3, command_id=arg_12_15, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12805660(_, arg_0_3: int, arg_4_7: int):
    """ 12805660: Event 12805660 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12805670(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 12805670: Event 12805670 """
    EndIfFlagOn(arg_8_11)
    GotoIfValueComparison(Label.L0, ComparisonType.Equal, left=arg_12_15, right=1)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_16_19)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Normal)
    IfFlagOn(4, arg_8_11)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(4)
    AICommand(arg_0_3, command_id=arg_4_7, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12805680(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12805680: Event 12805680 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacking_character=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12805700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12805700: Event 12805700 """
    GotoIfThisEventSlotOff(Label.L0)
    AddSpecialEffect(arg_4_7, 4672, affect_npc_part_hp=False)
    CancelSpecialEffect(arg_4_7, 4671)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_8_11, right=1)
    IfCharacterDead(0, arg_0_3)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    AddSpecialEffect(arg_4_7, 4672, affect_npc_part_hp=False)
    CancelSpecialEffect(arg_4_7, 4671)
    WaitFrames(1)
    ForceAnimation(arg_4_7, 7025, wait_for_completion=True)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterDead(2, arg_0_3)
    IfCharacterDead(2, arg_12_15)
    IfConditionTrue(0, input_condition=2)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    AddSpecialEffect(arg_4_7, 4672, affect_npc_part_hp=False)
    CancelSpecialEffect(arg_4_7, 4671)
    WaitFrames(1)
    ForceAnimation(arg_4_7, 7025, wait_for_completion=True)

    # --- 2 --- #
    DefineLabel(2)
    IfCharacterDead(0, arg_4_7)
    IfCharacterAlive(0, arg_4_7)
    Restart()


@RestartOnRest
def Event12805900(_, arg_0_3: int):
    """ 12805900: Event 12805900 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5510)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7010)
    AddSpecialEffect(arg_0_3, 5511, affect_npc_part_hp=False)
    Wait(1.899999976158142)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12805918():
    """ 12805918: Event 12805918 """
    SetTeamType(2800560, TeamType.Boss)
    CreateProjectileOwner(2800560)


@RestartOnRest
def Event12805920(_, arg_0_3: int, arg_4_7: int):
    """ 12805920: Event 12805920 """
    GotoIfFlagOff(Label.L0, arg_4_7)
    DeleteObjectFX(arg_0_3, erase_root=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfThisEventSlotOn(1)
    CreateObjectFX(928020, obj=arg_0_3, model_point=100)
    ShootProjectile(
        owner_entity=2800560,
        projectile_id=arg_0_3,
        model_point=100,
        behavior_id=6032,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    Restart()


@RestartOnRest
def Event12805930(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12805930: Event 12805930 """
    EndIfFlagOn(arg_4_7)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5510)
    IfCharacterHasSpecialEffect(-1, 2800562, 5510)
    IfCharacterHasSpecialEffect(-1, 2800563, 5510)
    IfCharacterHasSpecialEffect(-1, 2800564, 5510)
    IfCharacterHasSpecialEffect(-1, 2800566, 5510)
    IfCharacterHasSpecialEffect(-1, 2800567, 5510)
    IfCharacterHasSpecialEffect(-1, 2800569, 5510)
    IfCharacterHasSpecialEffect(-1, 2800570, 5510)
    IfCharacterHasSpecialEffect(-1, 2800571, 5510)
    IfCharacterHasSpecialEffect(-1, 2800572, 5510)
    IfCharacterHasSpecialEffect(-1, 2800573, 5510)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(-2, PLAYER, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800562, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800563, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800564, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800566, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800567, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800569, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800570, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800571, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800572, arg_8_11, radius=2.0)
    IfEntityWithinDistance(-2, 2800573, arg_8_11, radius=2.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(arg_0_3, bit_count=2, max_value=3)
    IfEventValueEqual(1, arg_0_3, bit_count=2, value=3)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(arg_4_7)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event12804000(_, arg_0_3: int):
    """ 12804000: Event 12804000 """
    DisableNetworkSync()
    GotoIfThisEventSlotOn(Label.L0)
    CancelSpecialEffect(arg_0_3, 4673)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(1.0)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    IfCharacterAlive(0, arg_0_3)
    AddSpecialEffect(arg_0_3, 5025, affect_npc_part_hp=False)
    Restart()


def Event12800100(_, arg_0_3: int, arg_4_7: int):
    """ 12800100: Event 12800100 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event12800120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12800120: Event 12800120 """
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=arg_4_7, entity=arg_0_3)
    DisplayDialog(
        arg_8_11,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12800140():
    """ 12800140: Event 12800140 """
    EndIfThisEventOn()
    EndIfClient()
    IfFlagOn(1, 13201803)
    IfFramesElapsed(1, 55)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13207850)
    DisplayDialog(
        10012014,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )


def Event12800160():
    """ 12800160: Event 12800160 """
    DisableNetworkSync()
    IfFlagOff(1, 9802)
    IfInsideMap(1, game_map=YAHARGUL)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 9120, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 9121, affect_npc_part_hp=False)
    IfFlagOff(2, 9802)
    IfInsideMap(2, game_map=YAHARGUL)
    IfConditionFalse(0, input_condition=2)
    CancelSpecialEffect(PLAYER, 9120)
    CancelSpecialEffect(PLAYER, 9121)
    Restart()


@RestartOnRest
def Event12800400():
    """ 12800400: Event 12800400 """
    EnableFlag(2800)
    GotoIfFlagOn(Label.L2, 9802)
    GotoIfFlagOn(Label.L1, 9801)
    GotoIfFlagOn(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2804000)
    DisableMapPiece(2804001)
    DisableMapPiece(2804002)
    DisableObject(2801000)
    DeleteFX(2803910, erase_root_only=False)
    DeleteFX(2803911, erase_root_only=False)
    Goto(Label.L4)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(2804000)
    EnableMapPiece(2804001)
    DisableMapPiece(2804002)
    DeleteFX(2803911, erase_root_only=False)

    # --- 4 --- #
    DefineLabel(4)
    DisableObject(2801000)
    DisableObject(2801052)
    DisableObject(2801140)
    DisableObject(2801141)
    DisableObject(2801142)
    DisableObject(2801143)
    DisableObject(2801144)
    DisableObject(2801145)
    DisableCharacter(2800740)
    DisableCharacter(2800741)
    DisableCharacter(2800742)
    DisableCharacter(2800743)
    DisableCharacter(2800744)
    DisableBackread(2800700)
    DisableBackread(2800701)
    DisableBackread(2800702)
    DisableBackread(2800500)
    DisableBackread(2800501)
    DisableBackread(2800502)
    DisableBackread(2800503)
    DisableBackread(2800504)
    DisableBackread(2800505)
    DisableBackread(2800480)
    DisableBackread(2800481)
    DisableBackread(2800482)
    DisableBackread(2800483)
    DisableBackread(2800400)
    DisableBackread(2800401)
    DisableBackread(2800402)
    DisableBackread(2800403)
    DisableBackread(2800404)
    DisableBackread(2800405)
    DisableBackread(2800406)
    DisableBackread(2800407)
    DisableBackread(2800408)
    DisableBackread(2800410)
    DisableBackread(2800411)
    DisableBackread(2800460)
    DisableBackread(2800461)
    DisableBackread(2800462)
    DisableBackread(2800300)
    DisableBackread(2800301)
    DisableBackread(2800302)
    DisableBackread(2800303)
    DisableBackread(2800304)
    DisableBackread(2800305)
    DisableBackread(2800306)
    DisableBackread(2800307)
    DisableBackread(2800308)
    DisableBackread(2800309)
    DisableBackread(2800310)
    DisableBackread(2800311)
    DisableBackread(2800312)
    DisableBackread(2800313)
    DisableBackread(2800314)
    DisableBackread(2800315)
    DisableBackread(2800316)
    DisableBackread(2800317)
    DisableBackread(2800318)
    DisableBackread(2800319)
    DisableBackread(2800320)
    DisableBackread(2800321)
    DisableBackread(2800322)
    DisableBackread(2800323)
    DisableBackread(2800324)
    DisableBackread(2800325)
    DisableBackread(2800326)
    DisableBackread(2800327)
    DisableBackread(2800328)
    DisableBackread(2800329)
    DisableBackread(2800380)
    DisableBackread(2800382)
    DisableBackread(2800383)
    DisableBackread(2800384)
    DisableBackread(2800560)
    DisableBackread(2800562)
    DisableBackread(2800563)
    DisableBackread(2800564)
    DisableBackread(2800566)
    DisableBackread(2800567)
    DisableBackread(2800569)
    DisableBackread(2800570)
    DisableBackread(2800571)
    DisableBackread(2800572)
    DisableBackread(2800573)
    DisableBackread(2800540)
    DisableBackread(2800541)
    DisableBackread(2800542)
    DisableBackread(2800543)
    DisableBackread(2800544)
    DisableBackread(2800721)
    DisableBackread(2800722)
    DisableObject(2801600)
    DisableObject(2801601)
    DisableObject(2801602)
    DisableObject(2801603)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagOff(2, Flags.OneRebornDead)
    EnableFlag(2800)
    SkipLines(1)
    DisableFlag(2800)
    DisableMapPiece(2804000)
    DisableMapPiece(2804001)
    EnableMapPiece(2804002)
    EnableObject(2801000)
    DeleteFX(2803910, erase_root_only=False)
    EnableObject(2801052)
    DisableObject(2801952)
    DisableCharacter(2800952)
    DisableCharacter(2803952)
    EnableFlag(70002802)
    EnableTreasure(2801140)
    EnableTreasure(2801141)
    EnableTreasure(2801142)
    EnableTreasure(2801143)
    EnableTreasure(2801144)
    EnableTreasure(2801145)
    DisableBackread(2800140)
    DisableBackread(2800141)
    DisableBackread(2800142)
    DisableBackread(2800143)
    DisableBackread(2800144)
    DisableBackread(2800145)
    DisableBackread(2800160)
    DisableBackread(2800161)
    DisableBackread(2800162)
    DisableBackread(2800163)
    DisableBackread(2800104)
    DisableBackread(2800105)
    DisableBackread(2800106)
    DisableBackread(2800107)
    DisableBackread(2800108)
    DisableBackread(2800109)
    DisableBackread(2800180)
    DisableBackread(2800181)
    DisableBackread(2800182)
    DisableBackread(2800183)
    DisableBackread(2800184)
    DisableBackread(2800185)
    DisableBackread(2800186)
    DisableBackread(2800187)
    DisableBackread(2800188)
    DisableBackread(2800189)
    DisableBackread(2800190)
    DisableBackread(2800191)
    DisableBackread(2800200)
    DisableBackread(2800201)
    DisableBackread(2800720)
    DisableBackread(2800723)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12800401():
    """ 12800401: Event 12800401 """
    IfFlagOn(-1, 9802)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 40)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2800745, 5686, affect_npc_part_hp=False)
    EnableFlag(12800435)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.Off)
    DisableFlag(12800435)


@RestartOnRest
def Event12800402():
    """ 12800402: Event 12800402 """
    GotoIfFlagOff(Label.L0, 9802)
    EndOfAnimation(2801300, 1)
    NotifyDoorEventSoundDampening(2801300, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=2800000, entity=2801300)
    DisplayDialog(
        CommonEventTexts.Locked,
        anchor_entity=2801300,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12800403():
    """ 12800403: Event 12800403 """
    GotoIfFlagOff(Label.L0, 9802)
    EndOfAnimation(2801150, 1)
    NotifyDoorEventSoundDampening(2801150, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=2800001, entity=2801150)
    DisplayDialog(
        CommonEventTexts.Locked,
        anchor_entity=2801150,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12800430():
    """ 12800430: Event 12800430 """
    EndIfClient()
    IfActionButtonParam(0, action_button_id=2800020, entity=2801500)
    Move(PLAYER, destination=2801500, destination_type=CoordEntityType.Object, model_point=220, short_move=True)
    ForceAnimation(PLAYER, 101169)
    WaitFrames(180)
    WarpPlayerToRespawnPoint(3202959)


def Event12800431():
    """ 12800431: Event 12800431 """
    IfHasTAEEvent(1, 2800745, tae_event_id=10)
    IfPlayerHasGood(1, 4310, including_box=False)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(PLAYER)
    WaitFrames(30)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    GotoIfMultiplayer(Label.L0)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(28000040, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(28001040, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(28000040, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(28001040, skippable=False, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableFlag(12800434)
    WarpPlayerToRespawnPoint(3202958)


@RestartOnRest
def Event12800432():
    """ 12800432: Event 12800432 """
    IfFlagOn(1, 12800435)
    IfHasTAEEvent(1, 2800745, tae_event_id=20)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2800745, 5687, affect_npc_part_hp=False)
    CancelSpecialEffect(2800745, 5686)
    IfHasTAEEvent(2, 2800745, tae_event_id=30)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(2800745, 5686, affect_npc_part_hp=False)
    CancelSpecialEffect(2800745, 5687)
    Restart()


@RestartOnRest
def Event12800433(_, arg_0_3: int):
    """ 12800433: Event 12800433 """
    DisableNetworkSync()
    IfHasTAEEvent(1, arg_0_3, tae_event_id=700)
    IfCharacterHasSpecialEffect(1, PLAYER, 5577)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.YouLose)
    Restart()


def Event12800435():
    """ 12800435: Event 12800435 """
    DisableNetworkSync()
    DisableSoundEvent(2803600)
    IfFlagOff(1, 9802)
    IfInsideMap(1, game_map=YAHARGUL)
    IfCharacterOutsideRegion(1, PLAYER, region=2802650)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(2803600)
    IfFlagOn(-1, 9802)
    IfOutsideMap(-1, game_map=YAHARGUL)
    IfCharacterInsideRegion(-1, PLAYER, region=2802650)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(2803600)
    Restart()


def Event12800436():
    """ 12800436: Event 12800436 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=2802020)
    IfFlagOff(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(2803600)
    IfCharacterInsideRegion(2, PLAYER, region=2802021)
    IfFlagOff(2, 9802)
    IfConditionTrue(0, input_condition=2)
    EnableSoundEvent(2803600)
    Restart()


def Event12800460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12800460: Event 12800460 """
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=2800030, entity=arg_0_3)
    CreatePlayLog(arg_8_11)
    ForceAnimation(PLAYER, 101167)
    WaitFrames(150)
    PlayCutsceneAndMovePlayer_Dummy(arg_4_7, YAHARGUL)
    WaitFrames(1)
    ForceAnimation(PLAYER, 101168)
    WaitFrames(120)
    Restart()


def Event12800470(_, arg_0_3: int, arg_4_7: int):
    """ 12800470: Event 12800470 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfFlagOn(0, 0)
    Wait(10.0)


def Event12800480(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12800480: Event 12800480 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event12800490(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12800490: Event 12800490 """
    DisableNetworkSync()
    EndIfFlagOn(arg_8_11)
    IfActionButtonParam(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        10010161,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)


@RestartOnRest
def Event12800500(_, arg_0_3: int, arg_4_7: int):
    """ 12800500: Event 12800500 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


def Event12800600(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12800600: Event 12800600 """
    GotoIfFlagOn(Label.L0, arg_12_15)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 3)
    DisableObjectActivation(arg_20_23, obj_act_id=100)
    DisableObjectActivation(arg_24_27, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(1, arg_4_7)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 3)
    EnableObjectActivation(arg_20_23, obj_act_id=100)
    DisableObjectActivation(arg_24_27, obj_act_id=100)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 13)
    DisableObjectActivation(arg_20_23, obj_act_id=100)
    EnableObjectActivation(arg_24_27, obj_act_id=100)

    # --- 2 --- #
    DefineLabel(2)
    End()
    DisableFlag(arg_0_3)


def Event12800601(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12800601: Event 12800601 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, arg_12_15)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(2, arg_4_7)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(arg_8_11)
    SkipLines(1)
    EnableFlag(arg_8_11)
    IfCharacterHuman(3, PLAYER)
    IfFlagOn(3, arg_12_15)
    IfFlagOff(3, arg_0_3)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event12800602(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12800602: Event 12800602 """
    IfFlagOn(3, arg_0_3)
    IfFlagOn(3, arg_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2801400, 12)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(1, arg_12_15)
    IfFlagOff(1, arg_0_3)
    IfFlagOff(1, arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfObjectActivated(-1, obj_act_id=arg_20_23)
    IfFlagChange(2, arg_8_11)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    ForceAnimation(2801400, 11, wait_for_completion=True)
    ForceAnimation(2801400, 12, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=2802101)
    ForceAnimation(2801400, 13, wait_for_completion=True)
    DisableObjectActivation(2801401, obj_act_id=100)
    EnableObjectActivation(2801402, obj_act_id=100)
    DisableFlag(arg_0_3)
    Restart()


def Event12800604(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12800604: Event 12800604 """
    IfFlagOn(3, arg_0_3)
    IfFlagOff(3, arg_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2801400, 2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(1, arg_12_15)
    IfFlagOff(1, arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfObjectActivated(-1, obj_act_id=arg_20_23)
    IfFlagChange(2, arg_8_11)
    IfFlagOff(2, arg_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    ForceAnimation(2801400, 1, wait_for_completion=True)
    ForceAnimation(2801400, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=2802102)
    ForceAnimation(2801400, 3, wait_for_completion=True)
    EnableObjectActivation(2801401, obj_act_id=100)
    DisableObjectActivation(2801402, obj_act_id=100)
    DisableFlag(arg_0_3)
    Restart()


def Event12800606(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12800606: Event 12800606 """
    DisableNetworkSync()
    IfFlagOff(1, arg_8_11)
    IfActionButtonParam(1, action_button_id=7100, entity=arg_12_15)
    IfFlagOff(2, arg_8_11)
    IfActionButtonParam(2, action_button_id=7100, entity=arg_16_19)
    IfFlagOn(3, arg_0_3)
    IfActionButtonParam(3, action_button_id=7100, entity=arg_12_15)
    IfFlagOn(4, arg_0_3)
    IfActionButtonParam(4, action_button_id=7100, entity=arg_16_19)
    IfFlagOn(5, arg_4_7)
    IfActionButtonParam(5, action_button_id=7100, entity=arg_12_15)
    IfFlagOff(6, arg_4_7)
    IfActionButtonParam(6, action_button_id=7100, entity=arg_16_19)
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
    Restart()


def Event12800607(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12800607: Event 12800607 """
    EndIfFlagOn(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableObjectActivation(arg_8_11, obj_act_id=100)
    DisableObjectActivation(arg_12_15, obj_act_id=100)
    EnableFlag(arg_0_3)


def Event12800608():
    """ 12800608: Event 12800608 """
    EndOfAnimation(2801400, 0)
    DisableObjectActivation(2801401, obj_act_id=100)
    DisableObjectActivation(2801402, obj_act_id=100)
    IfActionButtonParam(0, action_button_id=7100, entity=2801402)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12800620(_, arg_0_3: int, arg_4_7: int):
    """ 12800620: Event 12800620 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    CreatePlayLog(arg_4_7)


def Event12800700(_, arg_0_3: int):
    """ 12800700: Event 12800700 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


@RestartOnRest
def Event12800999():
    """ 12800999: Event 12800999 """
    DisableCharacter(2800509)
    SetBackreadStateAlternate(2800509, state=True)


def OneRebornDies():
    """ 12801800: Event 12801800 """
    GotoIfThisEventOff(Label.L0)
    DisableSoundEvent(2803802)
    DisableSoundEvent(2803803)
    DisableSoundEvent(2803804)
    DisableCharacter(Characters.OneRebornMain)
    DisableCharacter(Characters.OneRebornHumanPart)
    DisableCharacter(Characters.OneRebornBulletCreator)
    DisableCharacter(Characters.OneRebornHealthPool)
    Kill(Characters.OneRebornMain, award_souls=False)
    Kill(Characters.OneRebornHumanPart, award_souls=False)
    Kill(Characters.OneRebornBulletCreator, award_souls=False)
    Kill(Characters.OneRebornHealthPool, award_souls=False)
    DisableBackread(Characters.OneRebornMaiden1)
    DisableBackread(Characters.OneRebornMaiden2)
    DisableBackread(Characters.OneRebornMaiden3)
    DisableBackread(Characters.OneRebornMaiden4)
    DisableBackread(Characters.OneRebornMaiden5)
    DisableBackread(Characters.OneRebornMaiden6)
    DisableObject(Objects.OneRebornFog1)
    DisableObject(Objects.OneRebornFog2)
    DeleteFX(FX.OneRebornFog1, erase_root_only=False)
    DeleteFX(FX.OneRebornFog2, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthLessThanOrEqual(0, Characters.OneRebornHealthPool, 0.0)
    ResetAnimation(Characters.OneRebornMain, disable_interpolation=True)
    ResetAnimation(Characters.OneRebornHumanPart, disable_interpolation=True)
    Kill(Characters.OneRebornMain, award_souls=False)
    Kill(Characters.OneRebornHumanPart, award_souls=False)
    IfCharacterDead(0, Characters.OneRebornMain)
    Kill(Characters.OneRebornMaiden1, award_souls=True)
    Kill(Characters.OneRebornMaiden2, award_souls=True)
    Kill(Characters.OneRebornMaiden3, award_souls=True)
    Kill(Characters.OneRebornMaiden4, award_souls=True)
    Kill(Characters.OneRebornMaiden5, award_souls=True)
    Kill(Characters.OneRebornMaiden6, award_souls=True)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.OneRebornFog1)
    DisableObject(Objects.OneRebornFog2)
    DeleteFX(FX.OneRebornFog1, erase_root_only=True)
    DeleteFX(FX.OneRebornFog2, erase_root_only=True)
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.OneRebornHealthPool)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    AwardAchievement(18)
    AwardItemLot(50700000, host_only=False)
    EnableFlag(2800)
    EnableFlag(9464)
    CreatePlayLog(186)
    StopPlayLogMeasurement(2800000)
    StopPlayLogMeasurement(2800001)
    StopPlayLogMeasurement(2800010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 198, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 198, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 198, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 198, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayOneRebornDeathSound():
    """ 12801801: Event 12801801 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornDead)
    IfCharacterBackreadDisabled(2, Characters.OneRebornMain)
    IfHealthLessThanOrEqual(2, Characters.OneRebornHealthPool, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2802800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def OneRebornFirstTime():
    """ 12801802: Event 12801802 """
    EndIfFlagOn(Flags.OneRebornDead)
    EndIfThisEventOn()
    DisableCharacter(Characters.OneRebornMain)
    DisableCharacter(Characters.OneRebornHumanPart)
    IfFlagOff(1, Flags.OneRebornDead)
    IfThisEventSlotOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2802805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12804223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    DeleteFX(2803911, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(Cutscenes.OneRebornAppears, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(Cutscenes.OneRebornAppears, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    CreateFX(2803911)
    EnableFlag(Flags.OneRebornFogEntered)
    EnableCharacter(Characters.OneRebornMain)
    EnableCharacter(Characters.OneRebornHumanPart)
    EndIfFlagOn(9305)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9305)


def SummonStartOneRebornBattle():
    """ 12801803: Event 12801803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, Flags.OneRebornFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.OneRebornMain)
    EnableCharacter(Characters.OneRebornHumanPart)
    EnableFlag(Flags.OneRebornFogEntered)
    EnableFlag(Flags.OneRebornFirstTimeDone)


def EnterOneRebornFog():
    """ 12804880: Event 12804880 """
    EndIfFlagOn(Flags.OneRebornDead)
    GotoIfFlagOn(Label.L0, Flags.OneRebornFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.OneRebornFog1)
    DeleteFX(FX.OneRebornFog1, erase_root_only=False)
    DisableObject(Objects.OneRebornFog2)
    DeleteFX(FX.OneRebornFog2, erase_root_only=False)
    IfFlagOff(1, Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.OneRebornFog1)
    CreateFX(FX.OneRebornFog1)
    EnableObject(Objects.OneRebornFog2)
    CreateFX(FX.OneRebornFog2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, Flags.OneRebornDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2800800, entity=Objects.OneRebornFog1)
    IfFlagOn(3, Flags.OneRebornDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2802800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2802801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.OneRebornFogEntered)
    Restart()


def EnterOneRebornFogAsSummon():
    """ 12804881: Event 12804881 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOff(1, Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornFirstTimeDone)
    IfFlagOn(1, Flags.OneRebornFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=2800800, entity=Objects.OneRebornFog1)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2802800, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2802801)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12804801)
    Restart()


def Event12804882():
    """ 12804882: Event 12804882 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.OneRebornFog1, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12804883():
    """ 12804883: Event 12804883 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.OneRebornFog1, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.OneRebornFog1, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartOneRebornBattle():
    """ 12804802: Event 12804802 """
    EndIfFlagOn(Flags.OneRebornDead)
    DisableAI(Characters.OneRebornMain)
    DisableAI(Characters.OneRebornHumanPart)
    DisableAI(Characters.OneRebornBulletCreator)
    DisableAI(Characters.OneRebornHealthPool)
    DisableAI(Characters.OneRebornMaiden1)
    DisableAI(Characters.OneRebornMaiden2)
    DisableAI(Characters.OneRebornMaiden3)
    DisableAI(Characters.OneRebornMaiden4)
    DisableAI(Characters.OneRebornMaiden5)
    DisableAI(Characters.OneRebornMaiden6)
    DisableHealthBar(Characters.OneRebornMain)
    DisableHealthBar(Characters.OneRebornHumanPart)
    DisableHealthBar(Characters.OneRebornBulletCreator)
    DisableHealthBar(Characters.OneRebornHealthPool)
    DisableGravity(Characters.OneRebornHumanPart)
    DisableGravity(Characters.OneRebornBulletCreator)
    DisableGravity(Characters.OneRebornHealthPool)
    EnableImmortality(Characters.OneRebornMain)
    EnableImmortality(Characters.OneRebornHumanPart)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, Flags.OneRebornFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 12804223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.OneRebornMain, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.OneRebornHumanPart, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.OneRebornBulletCreator, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.OneRebornHealthPool, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12804223)
    EnableFlag(Flags.OneRebornFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.OneRebornMain, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornHumanPart, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornBulletCreator, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornHealthPool, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornMain)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornHumanPart)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornBulletCreator)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornHealthPool)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.OneRebornMain, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornHumanPart, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornBulletCreator, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OneRebornHealthPool, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornMain)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornHumanPart)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornBulletCreator)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OneRebornHealthPool)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.OneRebornMain)
    EnableAI(Characters.OneRebornHumanPart)
    EnableAI(Characters.OneRebornBulletCreator)
    EnableAI(Characters.OneRebornHealthPool)
    EnableAI(Characters.OneRebornMaiden1)
    EnableAI(Characters.OneRebornMaiden2)
    EnableAI(Characters.OneRebornMaiden3)
    EnableAI(Characters.OneRebornMaiden4)
    EnableAI(Characters.OneRebornMaiden5)
    EnableAI(Characters.OneRebornMaiden6)
    EnableBossHealthBar(Characters.OneRebornHealthPool, name=507000, slot=0)
    ReferDamageToEntity(Characters.OneRebornMain, Characters.OneRebornHealthPool)
    ReferDamageToEntity(Characters.OneRebornHumanPart, Characters.OneRebornHealthPool)
    SetCharacterEventTarget(Characters.OneRebornMain, Characters.OneRebornHealthPool)
    SetCharacterEventTarget(Characters.OneRebornHumanPart, Characters.OneRebornHealthPool)
    CreatePlayLog(238)
    StartPlayLogMeasurement(2800010, 254, overwrite=True)


def ControlOneRebornMusic():
    """ 12804803: Event 12804803 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.OneRebornDead)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(2803802)
    DisableSoundEvent(2803803)
    IfFlagOff(1, Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12804801)
    IfCharacterInsideRegion(1, PLAYER, region=2802802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(2803804)
    EnableBossMusic(2803802)
    IfHasTAEEvent(2, Characters.OneRebornMain, tae_event_id=300)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, Flags.OneRebornDead)
    IfFlagOn(2, Flags.OneRebornBattleStarted)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12804801)
    IfCharacterInsideRegion(2, PLAYER, region=2802802)
    IfConditionTrue(0, input_condition=2)
    DisableSoundEvent(2803804)
    DisableBossMusic(2803802)
    WaitFrames(0)
    EnableBossMusic(2803803)


def ControlOneRebornCamera():
    """ 12804804: Event 12804804 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.OneRebornDead)
    IfHealthGreaterThan(1, Characters.OneRebornHealthPool, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.OneRebornMain, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=1)
    IfHealthGreaterThan(2, Characters.OneRebornHealthPool, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.OneRebornMain, radius=12.5)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=0)
    Restart()


def StopOneRebornMusic():
    """ 12804805: Event 12804805 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(0, Flags.OneRebornDead)
    DisableBossMusic(2803802)
    DisableBossMusic(2803803)
    DisableBossMusic(-1)


def KeepOneRebornHumanPartAttached():
    """ 12804806: Event 12804806 """
    EndIfFlagOn(Flags.OneRebornDead)
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterBackreadEnabled(0, Characters.OneRebornMain)
    DisableGravity(Characters.OneRebornHumanPart)
    Wait(1.0)

    # --- 0 --- #
    DefineLabel(0)
    Move(
        Characters.OneRebornHumanPart,
        destination=Characters.OneRebornMain,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=Characters.OneRebornHumanPart,
    )
    Restart()


def MonitorOneRebornStunned():
    """ 12804807: The flag managed here is only checked once. Everything else just checks the effect directly. """
    EndIfFlagOn(Flags.OneRebornDead)
    IfCharacterHasSpecialEffect(0, Characters.OneRebornMain, Effects.OneRebornStunned)
    EnableFlag(Flags.OneRebornStunned)
    IfCharacterDoesNotHaveSpecialEffect(0, Characters.OneRebornMain, Effects.OneRebornStunned)
    DisableFlag(Flags.OneRebornStunned)
    Restart()


def OneRebornLimbDamage(
    _, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12804820: Event 12804820 """
    EndIfFlagOn(Flags.OneRebornDead)
    CreateNPCPart(
        Characters.OneRebornMain,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.OneRebornMain, npc_part_id=arg_4_7, material_special_effect_id=59, material_fx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, Characters.OneRebornMain, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, Characters.OneRebornMain, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOff(2, Flags.OneRebornStunned)  # only use of this flag (rather than the actual effect)
    SetNPCPartHealth(Characters.OneRebornMain, npc_part_id=arg_4_7, desired_hp=50, overwrite_max=False)
    Restart()
    CreateNPCPart(
        Characters.OneRebornMain,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.OneRebornMain, npc_part_id=arg_4_7, material_special_effect_id=60, material_fx_id=60)
    ResetAnimation(Characters.OneRebornMain, disable_interpolation=False)
    ResetAnimation(Characters.OneRebornHumanPart, disable_interpolation=False)
    ForceAnimation(Characters.OneRebornMain, arg_24_27)
    ForceAnimation(Characters.OneRebornHumanPart, 7000)
    AddSpecialEffect(Characters.OneRebornMain, arg_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.OneRebornMain, arg_20_23)
    IfCharacterHasSpecialEffect(3, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 3)
    ReplanAI(Characters.OneRebornMain)
    Wait(30.0)
    IfCharacterHasSpecialEffect(4, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 4)
    ReplanAI(Characters.OneRebornMain)
    IfHasTAEEvent(0, Characters.OneRebornMain, tae_event_id=300)
    CreateNPCPart(
        Characters.OneRebornMain,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.OneRebornMain, npc_part_id=arg_4_7, material_special_effect_id=59, material_fx_id=59)
    AddSpecialEffect(Characters.OneRebornMain, arg_20_23, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.OneRebornMain, arg_16_19)
    IfCharacterHasSpecialEffect(5, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 5)
    ReplanAI(Characters.OneRebornMain)
    WaitFrames(10)
    Restart()


def OneRebornSingleRainOfFlesh():
    """ 12804830: Event 12804830 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=200, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornExplosion():
    """ 12804831: Event 12804831 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=20)
    IfConditionTrue(0, input_condition=1)
    Move(Characters.OneRebornBulletCreator, destination=Characters.OneRebornMain, model_point=100, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=210, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornFootBlast1():
    """ 12804832: Event 12804832 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=30)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.OneRebornMain, 5585, affect_npc_part_hp=False)
    IfTimeElapsed(0, 1.100000023841858)
    CancelSpecialEffect(Characters.OneRebornMain, 5585)
    Move(Characters.OneRebornBulletCreator, destination=Characters.OneRebornMain, model_point=10, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=220, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornFootBlast2():
    """ 12804834: Event 12804834 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=40)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.OneRebornMain, 5586, affect_npc_part_hp=False)
    IfTimeElapsed(0, 1.100000023841858)
    CancelSpecialEffect(Characters.OneRebornMain, 5586)
    Move(Characters.OneRebornBulletCreator, destination=Characters.OneRebornMain, model_point=15, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=220, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornFootBlast3():
    """ 12804835: Event 12804835 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=50)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.OneRebornMain, 5587, affect_npc_part_hp=False)
    IfTimeElapsed(0, 1.100000023841858)
    CancelSpecialEffect(Characters.OneRebornMain, 5587)
    Move(Characters.OneRebornBulletCreator, destination=Characters.OneRebornMain, model_point=50, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=220, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornFootBlast4():
    """ 12804836: Event 12804836 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=60)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(Characters.OneRebornMain, 5588, affect_npc_part_hp=False)
    IfTimeElapsed(0, 1.100000023841858)
    CancelSpecialEffect(Characters.OneRebornMain, 5588)
    Move(Characters.OneRebornBulletCreator, destination=Characters.OneRebornMain, model_point=55, short_move=True)
    AICommand(Characters.OneRebornBulletCreator, command_id=220, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Restart()


def OneRebornRepeatedRainOfFlesh():
    """ 12804837: Event 12804837 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterTargeting(1, Characters.OneRebornHumanPart, PLAYER)
    IfHasTAEEvent(1, Characters.OneRebornHumanPart, tae_event_id=100)
    IfConditionTrue(0, input_condition=1)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=100, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Wait(0.800000011920929)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=100, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Wait(1.0)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=100, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Wait(1.2000000476837158)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=100, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Wait(1.399999976158142)
    Move(Characters.OneRebornBulletCreator, destination=PLAYER, model_point=246, short_move=True)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=100, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    WaitFrames(1)
    AICommand(Characters.OneRebornBulletCreator, command_id=-1, slot=0)
    ReplanAI(Characters.OneRebornBulletCreator)
    Wait(1.600000023841858)
    Restart()


@RestartOnRest
def OneRebornSummonsRepeatedRainOfFlesh():
    """ 12804838: Event 12804838 """
    EndIfFlagOn(Flags.OneRebornDead)
    IfHasTAEEvent(0, Characters.OneRebornMain, tae_event_id=100)
    ForceAnimation(Characters.OneRebornHumanPart, 3000)
    AICommand(Characters.OneRebornHumanPart, command_id=1, slot=1)
    ReplanAI(Characters.OneRebornHumanPart)
    IfHasTAEEvent(0, Characters.OneRebornMain, tae_event_id=300)
    IfCharacterHasSpecialEffect(1, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 1)
    ReplanAI(Characters.OneRebornMain)
    Wait(10.0)
    AICommand(Characters.OneRebornHumanPart, command_id=-1, slot=1)
    ReplanAI(Characters.OneRebornHumanPart)
    Restart()


@RestartOnRest
def OneRebornBuffMaidenDies(_, maiden: int):
    """ 12804840: One Reborn gets AI command 1 for 30 seconds after this Maiden is killed. """
    EndIfFlagOn(Flags.OneRebornDead)
    SetCharacterEventTarget(maiden, Characters.OneRebornHumanPart)
    EndIfThisEventSlotOn()
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterDead(1, maiden)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.OneRebornHumanPart, 7010)
    AICommand(Characters.OneRebornMain, command_id=1, slot=2)
    AICommand(Characters.OneRebornHumanPart, command_id=1, slot=2)
    IfCharacterHasSpecialEffect(2, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 2)
    ReplanAI(Characters.OneRebornMain)
    ReplanAI(Characters.OneRebornHumanPart)
    Wait(30.0)
    AICommand(Characters.OneRebornMain, command_id=-1, slot=2)
    AICommand(Characters.OneRebornHumanPart, command_id=-1, slot=2)
    IfCharacterHasSpecialEffect(3, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 3)
    ReplanAI(Characters.OneRebornMain)
    ReplanAI(Characters.OneRebornHumanPart)


@RestartOnRest
def CountDeadOneRebornMaidens(_, one_reborn_maiden: int):
    """ 12804850: Event 12804850 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfCharacterDead(1, one_reborn_maiden)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(12804860, bit_count=4, max_value=10)


@RestartOnRest
def OneRebornTakesFirstDamage():
    """ 12804870: The One Reborn and all Maidens receive AI command 1 when One Reborn's health goes below 100%. """
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfHealthLessThan(1, Characters.OneRebornHealthPool, 1.0)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, Flags.OneRebornPhaseTwo)
    AICommand(Characters.OneRebornMain, command_id=1, slot=0)
    AICommand(Characters.OneRebornHumanPart, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden1, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden2, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden3, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden4, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden5, command_id=1, slot=0)
    AICommand(Characters.OneRebornMaiden6, command_id=1, slot=0)
    IfCharacterHasSpecialEffect(2, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 2)
    ReplanAI(Characters.OneRebornMain)
    ReplanAI(Characters.OneRebornHumanPart)
    ReplanAI(Characters.OneRebornMaiden1)
    ReplanAI(Characters.OneRebornMaiden2)
    ReplanAI(Characters.OneRebornMaiden3)
    ReplanAI(Characters.OneRebornMaiden4)
    ReplanAI(Characters.OneRebornMaiden5)
    ReplanAI(Characters.OneRebornMaiden6)


@RestartOnRest
def OneRebornPhaseTwoTrigger():
    """ 12804871: The One Reborn goes to phase two at 50% health or when 3+ Maidens are killed. """
    IfFlagOn(1, Flags.OneRebornBattleStarted)
    IfHealthLessThan(-1, Characters.OneRebornHealthPool, 0.5)
    IfEventValueComparison(-1, 12804860, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.OneRebornMain, command_id=2, slot=0)
    AICommand(Characters.OneRebornHumanPart, command_id=2, slot=0)
    AICommand(Characters.OneRebornMain, command_id=1, slot=1)
    IfCharacterHasSpecialEffect(2, Characters.OneRebornMain, Effects.OneRebornStunned)
    SkipLinesIfConditionTrue(1, 2)
    ReplanAI(Characters.OneRebornMain)


def Event12800990():
    """ 12800990: Event 12800990 """
    EndIfThisEventOn()
    IfStandingOnCollision(0, 2803500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 272, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 272, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 272, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 272, PlayLogMultiplayerType.HostOnly)


def Event12800901():
    """ 12800901: Event 12800901 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1315)
    EndIfFlagOn(1310)
    IfCharacterDead(0, 2800670)
    DisableFlagRange((1300, 1319))
    EnableFlag(1315)
    SaveRequest()


def Event12800902():
    """ 12800902: Event 12800902 """
    IfFlagOn(0, 72800312)
    DisableFlag(72800312)
    DisableFlagRange((1300, 1319))
    EnableFlag(1301)
    ForceAnimation(2800670, 103107, loop=True, skip_transition=True)
    SaveRequest()


def Event12800903():
    """ 12800903: Event 12800903 """
    IfFlagOn(0, 72800314)
    DisableFlag(72800314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1313)


def Event12800904():
    """ 12800904: Event 12800904 """
    IfFlagOn(0, 72800315)
    DisableFlag(72800315)
    DisableFlagRange((1300, 1319))
    EnableFlag(1314)


def Event12800905():
    """ 12800905: Event 12800905 """
    IfFlagOn(0, 72800316)
    DisableFlag(72800316)
    DisableFlagRange((1300, 1319))
    EnableFlag(1311)


def Event12800906():
    """ 12800906: Event 12800906 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72800310)
    IfCharacterInsideRegion(0, PLAYER, region=2802450)
    EnableFlag(72800310)
    IfCharacterOutsideRegion(0, PLAYER, region=2802450)
    Restart()


def Event12800908():
    """ 12800908: Event 12800908 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2800670, attacking_character=-1)
    IfHealthNotEqual(1, 2800670, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2800670, 103093)
    Restart()


def Event12800909():
    """ 12800909: Event 12800909 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOff(1, 1310)
    IfHealthEqual(1, 2800670, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2800670, 103094)


def Event12800910():
    """ 12800910: Event 12800910 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2800670, 151)
    IfHealthNotEqual(1, 2800670, 0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L0, 1300)
    ForceAnimation(2800670, 103091)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2800670, 103092)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(5)
    Restart()


def Event12800911():
    """ 12800911: Event 12800911 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L4, input_condition=15)
    GotoIfFlagOff(Label.L0, 1313)
    DisableFlagRange((1300, 1319))
    EnableFlag(1304)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOff(Label.L1, 1314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1309)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagOff(Label.L2, 1311)
    GotoIfFlagOff(Label.L4, 72800317)
    GotoIfFlagOff(Label.L5, 72800318)
    DisableFlagRange((1300, 1319))
    EnableFlag(1310)
    Goto(Label.L2)

    # --- 4 --- #
    DefineLabel(4)
    EnableFlag(72800317)
    Goto(Label.L2)

    # --- 5 --- #
    DefineLabel(5)
    EnableFlag(72800318)
    Goto(Label.L2)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagOn(-1, 1300)
    IfFlagOn(-1, 1301)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 9802)
    GotoIfConditionFalse(Label.L3, input_condition=1)
    DisableFlagRange((1300, 1319))
    EnableFlag(1316)
    Goto(Label.L3)

    # --- 3 --- #
    DefineLabel(3)
    DisableFlag(72800308)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagOn(Label.L0, 1300)
    GotoIfFlagOn(Label.L1, 1301)
    GotoIfFlagOn(Label.L1, 1311)
    GotoIfFlagOn(Label.L2, 1310)
    GotoIfFlagOn(Label.L3, 1315)
    GotoIfFlagOn(Label.L1, 1313)
    GotoIfFlagOn(Label.L1, 1314)
    DisableBackread(2800670)
    DisableBackread(2800671)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2800670)
    DisableBackread(2800671)
    ForceAnimation(2800670, 103092, loop=True, skip_transition=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2800670)
    DisableBackread(2800671)
    ForceAnimation(2800670, 103091, loop=True, skip_transition=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2800670)
    EnableBackread(2800671)
    EzstateAIRequest(2800671, command_id=6, slot=1)
    DropMandatoryTreasure(2800671)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableBackread(2800670)
    DisableBackread(2800671)
    Move(2800670, destination=2802452, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EzstateAIRequest(2800670, command_id=7, slot=1)
    WaitFrames(1)
    DropMandatoryTreasure(2800670)
    End()


def Event12800920(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12800920: Event 12800920 """
    EndIfClient()
    EndIfThisEventSlotOn()
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    CreateObjectFX(900201, obj=arg_12_15, model_point=200)
    IfActionButtonParam(0, action_button_id=7500, entity=arg_12_15)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(arg_16_19, host_only=False)
    DeleteObjectFX(arg_12_15, erase_root=True)


@RestartOnRest
def Event12804450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12804450: Event 12804450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagOn(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOn(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12804400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12804400: Event 12804400 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(1, 9802)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(1, 13501900)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(2, 9802)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOn(1, 13501900)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12804401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12804401: Event 12804401 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(1, 9802)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(2, 9802)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12804410(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12804410: Event 12804410 """
    SkipLinesIfFlagOn(1, arg_12_15)
    DisableCharacter(arg_4_7)
    SkipLinesIfFlagOn(3, arg_16_19)
    IfClient(1)
    IfFlagOn(1, arg_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_4_7)
    EndIfFlagOn(arg_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(arg_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfFlagOn(2, arg_20_23)
    IfFlagOff(2, arg_24_27)
    IfActionButtonParam(2, action_button_id=arg_28_31, entity=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(arg_0_3, arg_4_7, arg_8_11, summon_flag=arg_12_15, dismissal_flag=arg_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12804460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12804460: Event 12804460 """
    EndIfClient()
    IfFlagOn(1, arg_20_23)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    RotateToFaceEntity(arg_0_3, arg_8_11, animation=arg_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(arg_0_3, region=arg_8_11, reaction_range=1.0)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_24_27)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetCharacterEventTarget(arg_0_3, Characters.OneRebornMain)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
