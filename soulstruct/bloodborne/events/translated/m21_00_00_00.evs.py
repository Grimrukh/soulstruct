"""HUNTER'S DREAM

linked:
164

strings:
0: PC情報_拠点到達時
22: ボス_撃破
34: PC情報_ボス撃破_拠点ボス
64: ボス_戦闘開始
80: ボス_撃破時間
96: PC情報_ボス撃破_拠点ボス2
128: ボス_戦闘開始2
146: ボス_撃破時間2
164: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from .anims import c9020
# from .common import GainInsight  # TODO
from .common_entities import *
from .m21_00_entities import *


def Constructor():
    """ 0: Event 0 """
    Event12100010()

    SkipLinesIfFlagDisabled(1, 9400)
    SetRespawnPoint(2102961)

    SkipLinesIfClient(2)
    SkipLinesIfFlagDisabled(1, 6600)
    EnableFlag(12101999)

    SkipLinesIfFlagEnabled(1, 12101999)
    DisableObject(2101100)

    SetNetworkUpdateRate(Characters.PlainDoll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(PLAYER, 110, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 111, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 112, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 113, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 114, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 115, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 116, affect_npc_part_hp=False)

    # ALTAR WARPS
    # Disable all main headstone warp request flags.
    DisableFlag(72100100)
    DisableFlag(72100101)
    DisableFlag(72100102)
    DisableFlag(72102110)
    DisableFlag(72102200)
    DisableFlag(72102201)
    DisableFlag(72102300)
    DisableFlag(72102301)
    DisableFlag(72102302)
    DisableFlag(72102400)
    DisableFlag(72102401)
    DisableFlag(72102410)
    DisableFlag(72102411)
    DisableFlag(72102412)
    DisableFlag(72102413)
    DisableFlag(72102420)
    DisableFlag(72102421)
    DisableFlag(72102422)
    DisableFlag(72102500)
    DisableFlag(72102501)
    DisableFlag(72102502)
    DisableFlag(72102600)
    DisableFlag(72102601)
    DisableFlag(72102602)
    DisableFlag(72102603)
    DisableFlag(72102700)
    DisableFlag(72102701)
    DisableFlag(72102800)
    DisableFlag(72102801)
    DisableFlag(72102802)
    DisableFlag(72102803)
    DisableFlag(72103200)
    DisableFlag(72103201)
    DisableFlag(72103202)
    DisableFlag(72103203)
    DisableFlag(72103300)
    DisableFlag(72103301)
    DisableFlag(72103400)
    DisableFlag(72103401)
    DisableFlag(72103402)
    DisableFlag(72103403)
    DisableFlag(72103500)
    DisableFlag(72103501)
    DisableFlag(72103502)
    DisableFlag(72103600)
    DisableFlag(72103601)
    DisableFlag(72103602)
    MonitorWeaponBuffRemovalRequest()
    # Monitor main headstone activation.
    WarpAtHeadstone(52, 72102110, Characters.UnseenMessengers, WarpPoints.AbandonedOldWorkshop)
    WarpAtHeadstone(0, 72102200, Characters.FrontierMessengers, WarpPoints.HemwickCharnelLane)
    WarpAtHeadstone(1, 72102201, Characters.FrontierMessengers, WarpPoints.WitchsAbode)
    WarpAtHeadstone(5, 72102300, Characters.YharnamMessengers, WarpPoints.OldYharnam)
    WarpAtHeadstone(6, 72102301, Characters.YharnamMessengers, WarpPoints.ChurchOfTheGoodChalice)
    WarpAtHeadstone(7, 72102302, Characters.YharnamMessengers, WarpPoints.GraveyardOfTheDarkbeast)
    WarpAtHeadstone(10, 72102400, Characters.YharnamMessengers, WarpPoints.CathedralWard)
    WarpAtHeadstone(11, 72102401, Characters.YharnamMessengers, WarpPoints.GrandCathedral)
    WarpAtHeadstone(15, 72102410, Characters.YharnamMessengers, WarpPoints.FirstFloorSickroom)
    WarpAtHeadstone(16, 72102411, Characters.YharnamMessengers, WarpPoints.CentralYharnam)
    WarpAtHeadstone(17, 72102412, Characters.YharnamMessengers, WarpPoints.GreatBridge)
    WarpAtHeadstone(18, 72102413, Characters.YharnamMessengers, WarpPoints.TombOfOedon)
    WarpAtHeadstone(20, 72102420, Characters.YharnamMessengers, WarpPoints.UpperCathedralWard)
    WarpAtHeadstone(21, 72102421, Characters.YharnamMessengers, WarpPoints.LumenflowerGardens)
    WarpAtHeadstone(22, 72102422, Characters.YharnamMessengers, WarpPoints.AltarOfDespair)
    WarpAtHeadstone(25, 72102500, Characters.UnseenMessengers, WarpPoints.ForsakenCastleCainhurt)
    WarpAtHeadstone(26, 72102501, Characters.UnseenMessengers, WarpPoints.LogariusSeat)
    WarpAtHeadstone(27, 72102502, Characters.UnseenMessengers, WarpPoints.VilebloodQueensChamber)
    WarpAtHeadstone(30, 72102600, Characters.NightmareMessengers, WarpPoints.NightmareOfMensis)
    WarpAtHeadstone(31, 72102601, Characters.NightmareMessengers, WarpPoints.MergosLoftBase)
    WarpAtHeadstone(32, 72102602, Characters.NightmareMessengers, WarpPoints.MergosLoftMiddle)
    WarpAtHeadstone(33, 72102603, Characters.NightmareMessengers, WarpPoints.WetNursesLunarium)
    WarpAtHeadstone(35, 72102700, Characters.FrontierMessengers, WarpPoints.ForbiddenWoods)
    WarpAtHeadstone(36, 72102701, Characters.FrontierMessengers, WarpPoints.ForbiddenGrave)
    WarpAtHeadstone(40, 72102800, Characters.UnseenMessengers, WarpPoints.YahargulUnseenVillage)
    WarpAtHeadstone(41, 72102801, Characters.UnseenMessengers, WarpPoints.YahargulChapel)
    WarpAtHeadstone(42, 72102802, Characters.UnseenMessengers, WarpPoints.AdventPlaza)
    WarpAtHeadstone(43, 72102803, Characters.UnseenMessengers, WarpPoints.HypogeanGaol)
    WarpAtHeadstone(45, 72103200, Characters.FrontierMessengers, WarpPoints.Byrgenwerth)
    WarpAtHeadstone(46, 72103201, Characters.NightmareMessengers, WarpPoints.LectureBuilding)
    WarpAtHeadstone(47, 72103202, Characters.FrontierMessengers, WarpPoints.MoonsideLake)
    WarpAtHeadstone(48, 72103203, Characters.NightmareMessengers, WarpPoints.LectureBuildingSecondFloor)
    WarpAtHeadstone(50, 72103300, Characters.NightmareMessengers, WarpPoints.NightmareFrontier)
    WarpAtHeadstone(51, 72103301, Characters.NightmareMessengers, WarpPoints.AmygdalasChamber)
    WarpAtHeadstone(55, 72103400, Characters.OldHuntersMessengers, WarpPoints.OldHuntersStart)
    WarpAtHeadstone(56, 72103401, Characters.OldHuntersMessengers, WarpPoints.NightmareChurch)
    WarpAtHeadstone(57, 72103402, Characters.OldHuntersMessengers, WarpPoints.UndergroundCorpsePile)
    WarpAtHeadstone(58, 72103403, Characters.OldHuntersMessengers, WarpPoints.NightmareGrandCathedral)
    WarpAtHeadstone(60, 72103500, Characters.OldHuntersMessengers, WarpPoints.ResearchHall)
    WarpAtHeadstone(61, 72103501, Characters.OldHuntersMessengers, WarpPoints.LumenwoodGarden)
    WarpAtHeadstone(62, 72103502, Characters.OldHuntersMessengers, WarpPoints.AstralClocktower)
    WarpAtHeadstone(65, 72103600, Characters.OldHuntersMessengers, WarpPoints.FishingHamlet)
    WarpAtHeadstone(66, 72103601, Characters.OldHuntersMessengers, WarpPoints.LighthouseHut)
    WarpAtHeadstone(67, 72103602, Characters.OldHuntersMessengers, WarpPoints.Coast)
    # Disable chalice dungeon altar activation flags.
    DisableFlag(72100420)
    DisableFlag(72100421)
    DisableFlag(72100422)
    DisableFlag(72100423)
    DisableFlag(72100424)
    DisableFlag(72100425)
    DisableFlag(72100426)
    ActivateChaliceAltar(0, 72100420, Characters.MakeshiftAltar, CommonFlags.MakeshiftAltarActivated)
    ActivateChaliceAltar(1, 72100421, Characters.ChaliceAltar1, CommonFlags.ChaliceAltar1Activated)
    ActivateChaliceAltar(2, 72100422, Characters.ChaliceAltar2, CommonFlags.ChaliceAltar2Activated)
    ActivateChaliceAltar(3, 72100423, Characters.ChaliceAltar3, CommonFlags.ChaliceAltar3Activated)
    ActivateChaliceAltar(4, 72100424, Characters.ChaliceAltar4, CommonFlags.ChaliceAltar4Activated)
    ActivateChaliceAltar(5, 72100425, Characters.ChaliceAltar5, CommonFlags.ChaliceAltar5Activated)
    ActivateChaliceAltar(6, 72100426, Characters.ChaliceAltar6, CommonFlags.ChaliceAltar6Activated)
    # These trigger flags cause the actual warp to a Chalice Dungeon map.
    # Flags 9020 to 9026 (above) probably activate a check for the dungeon type, then one of these is enabled.
    DisableFlag(72100300)
    DisableFlag(72100301)
    DisableFlag(72100302)
    DisableFlag(72100303)
    DisableFlag(72100304)
    DisableFlag(72100305)
    DisableFlag(72100306)
    DisableFlag(72100307)
    DisableFlag(72100308)
    DisableFlag(72100309)
    WarpToChaliceDungeon(0, 72100300, 2902950, 9001)
    WarpToChaliceDungeon(1, 72100301, 2902951, 9002)
    WarpToChaliceDungeon(2, 72100302, 2902952, 9003)
    WarpToChaliceDungeon(3, 72100303, 2902953, 9004)
    WarpToChaliceDungeon(4, 72100304, 2902954, 9005)
    WarpToChaliceDungeon(5, 72100305, 2902955, 9006)
    WarpToChaliceDungeon(6, 72100306, 2902956, 9007)
    WarpToChaliceDungeon(7, 72100307, 2902957, 9008)
    WarpToChaliceDungeon(8, 72100308, 2902958, 9009)
    WarpToChaliceDungeon(9, 72100309, 2902959, 9010)

    # AREA SETUP
    InitializeWorkshopAppearance()
    InitializeDreamMusic()

    # BOSSES AND ENDINGS
    InitializeBossArena()
    YharnamSunriseEnding()  # Accept Gehrman's offer.
    GehrmanDies()
    PlayGehrmanDeathSound()
    RefuseGehrmansOffer()
    EnterGehrmanBossFog()
    EnterGehrmanBossFogAsSummon()
    StartGehrmanBossBattle()
    ControlGehrmanMusic()
    ToggleGehrmanCamera()
    StopGehrmanBossMusic()
    ActivateGehrmanPhaseTwo()
    GehrmanBuffWearsOff()
    SummonStartGehrmanBattle()
    HonoringWishesEnding()
    ChildhoodsBeginningEnding()
    MoonPresenceDies()
    PlayMoonPresenceDeathSound()
    MoonPresenceBattleCutscene()
    EnterMoonPresenceBossFog()
    EnterMoonPresenceFogAsSummon()
    StartMoonPresenceBossBattle()
    ControlMoonPresenceMusic()
    ToggleMoonPresenceCamera()
    StopMoonPresenceBossMusic()
    SummonStartMoonPresenceBattle()
    ControlMoonPresenceTail(0, 5, 5, 1, 100, 480, 490, 8000)
    ControlMoonPresenceTail(1, 6, 6, 2, 150, 481, 491, 8010)
    ControlMoonPresenceTail(2, 7, 7, 3, 150, 482, 492, 8030)
    ControlMoonPresenceTail(3, 8, 8, 4, 200, 483, 493, 8020)
    ControlMoonPresenceTail(4, 9, 9, 5, 200, 484, 494, 8040)
    MoonPresenceSinHarvest()

    # GATES / DOORS
    OpenGateToField()
    DisplayMessageAtObject(
        0, 7002, Objects.IronGateToField, CommonFlags.WorkshopOnFire, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        1, 7030, Objects.WorkshopFrontDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        2, 7030, Objects.WorkshopBackDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        3, 7030, Objects.WorkshopMiddleDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)

    # FIRST ARRIVAL
    FirstArrivalCutscene()
    LogPlayerEquipmentOnFirstArrival()

    # HEADSTONES
    AnimateHeadstoneMessengers(0, Characters.YharnamMessengers, Flags.YharnamHeadstoneAvailable)
    AnimateHeadstoneMessengers(1, Characters.FrontierMessengers, Flags.FrontierHeadstoneAvailable)
    AnimateHeadstoneMessengers(2, Characters.UnseenMessengers, Flags.UnseenHeadstoneAvailable)
    AnimateHeadstoneMessengers(3, Characters.NightmareMessengers, Flags.NightmareHeadstoneAvailable)
    AnimateOldHuntersHeadstoneMessengers(3, Characters.OldHuntersMessengers, Flags.OldHuntersHeadstoneAvailable)
    EnableYharnamHeadstone()
    EnableFrontierHeadstone()
    EnableUnseenHeadstone()
    EnableNightmareHeadstone()
    EnableOldHuntersHeadstone()

    # BATH MESSENGERS
    InitializeBathMessengers()
    BathMessengerAppearance(0, Goods.SawHunterBadge, Characters.BathShopMessengers1, 1, 10)
    BathMessengerAppearance(1, Goods.CrowHunterBadge, Characters.BathShopMessengers1, 2, 13)
    BathMessengerAppearance(2, Goods.PowderKegHunterBadge, Characters.BathShopMessengers1, 3, 15)
    BathMessengerAppearance(3, Goods.OldHunterBadge, Characters.BathShopMessengers2, 0, 15)
    BathMessengerAppearance(4, Goods.SwordHunterBadge, Characters.BathShopMessengers2, 1, 12)
    BathMessengerAppearance(5, Goods.RadiantSwordHunterBadge, Characters.BathShopMessengers2, 2, 11)
    BathMessengerAppearance(6, Goods.WheelHunterBadge, Characters.BathShopMessengers2, 3, 15)
    BathMessengerAppearance(7, Goods.CainhurstBadge, Characters.BathShopMessengers3, 0, 15)
    BathMessengerAppearance(8, Goods.SparkHunterBadge, Characters.BathShopMessengers3, 1, 15)
    BathMessengerAppearance(9, Goods.CosmicEyeWatcherBadge, Characters.BathShopMessengers3, 2, 15)

    InitializeStoryProgressionFlags()

    InitializeInsightShop()

    # GIFTS
    OfferMeleeWeaponGift()
    OfferGunGift()
    OfferNotebookGift()
    OfferBeckoningBellGift()
    OfferOldHunterBellGift()
    OfferDLCAccessGift()

    # CHALICE DUNGEONS ALTARS
    InitializeMakeshiftAltar()
    InitializeChaliceAltar1()
    InitializeChaliceAltar2()
    InitializeChaliceAltar3()
    InitializeChaliceAltar4()
    InitializeChaliceAltar5()
    InitializeChaliceAltar6()
    AnimateChaliceAltar(0, 94005001, Characters.MakeshiftAltar)
    AnimateChaliceAltar(1, 94105001, Characters.ChaliceAltar1)
    AnimateChaliceAltar(2, 94205001, Characters.ChaliceAltar2)
    AnimateChaliceAltar(3, 94305001, Characters.ChaliceAltar3)
    AnimateChaliceAltar(4, 94405001, Characters.ChaliceAltar4)
    AnimateChaliceAltar(5, 94505001, Characters.ChaliceAltar5)
    AnimateChaliceAltar(6, 94605001, Characters.ChaliceAltar6)

    # PLAIN DOLL
    InitializePlainDoll()
    Event12105200()
    Event12100115()
    Event12100116()
    Event12100117()
    Event12100120()
    Event12100121()
    Event12100123()
    Event12100112()
    Event12100113()
    Event12100114()

    # GEHRMAN (ALLY)
    InitializeGehrmanAlly()
    OpenWorkshopDoors()
    Event12100163()
    Event12100164()
    Event12100165()
    DisableHealthBar(Characters.GehrmanAlly)

    # STUMP MESSENGERS
    StumpMessengersRemoveHats()
    StumpMessengersAppear()
    ChangeStumpMessengerHat(0, 72100141, CommonFlags.RequestMessengerHat1, 20)
    ChangeStumpMessengerHat(1, 72100142, CommonFlags.RequestMessengerHat2, 21)
    ChangeStumpMessengerHat(2, 72100143, CommonFlags.RequestMessengerHat3, 22)
    ChangeStumpMessengerHat(3, 72100144, CommonFlags.RequestMessengerHat4, 23)
    ChangeStumpMessengerHat(4, 72100145, CommonFlags.RequestMessengerHat5, 24)
    ChangeStumpMessengerHat(5, 72100146, CommonFlags.RequestMessengerHat6, 25)
    ChangeStumpMessengerHat(6, 72100147, CommonFlags.RequestMessengerHat7, 26)
    ChangeStumpMessengerHat(7, 72100148, CommonFlags.RequestMessengerHat8, 27)
    ChangeStumpMessengerHat(8, 72100149, CommonFlags.RequestMessengerHat9, 28)
    ChangeStumpMessengerHat(9, 72100150, CommonFlags.RequestMessengerHat10, 0)
    ChangeStumpMessengerHat(10, 72100151, CommonFlags.RequestMessengerHat11, 0)
    ChangeStumpMessengerHat(11, 72100152, CommonFlags.RequestMessengerHat12, 0)
    ChangeStumpMessengerHat(12, 72100153, CommonFlags.RequestMessengerHat13, 0)
    ChangeStumpMessengerHat(13, 72100154, CommonFlags.RequestMessengerHat14, 0)
    ChangeStumpMessengerHat(14, 72100155, CommonFlags.RequestMessengerHat15, 0)
    MonitorMessengerHatPossession(0, Goods.YharnamMessengerHat, CommonFlags.PlayerHasMessengerHat1, 1)
    MonitorMessengerHatPossession(1, Goods.WornMessengerTopHat, CommonFlags.PlayerHasMessengerHat2, 1)
    MonitorMessengerHatPossession(2, Goods.MessengerHeadBandage, CommonFlags.PlayerHasMessengerHat3, 1)
    MonitorMessengerHatPossession(3, Goods.WhiteMessengerRibbon, CommonFlags.PlayerHasMessengerHat4, 0)
    MonitorMessengerHatPossession(4, Goods.RedMessengerRibbon, CommonFlags.PlayerHasMessengerHat5, 0)
    MonitorMessengerHatPossession(5, Goods.MessengerTopHat, CommonFlags.PlayerHasMessengerHat6, 0)
    MonitorMessengerHatPossession(6, Goods.BlackMessengerHat, CommonFlags.PlayerHasMessengerHat7, 0)
    MonitorMessengerHatPossession(7, Goods.BloodyMessengerHeadBandage, CommonFlags.PlayerHasMessengerHat8, 0)
    MonitorMessengerHatPossession(8, Goods.MessengerUrnDance, CommonFlags.PlayerHasMessengerHat9, 0)
    MonitorMessengerHatPossession(9, 4909, 6080, 0)  # unused hat slots, presumably
    MonitorMessengerHatPossession(10, 4910, 6081, 0)
    MonitorMessengerHatPossession(11, 4911, 6082, 0)
    MonitorMessengerHatPossession(12, 4912, 6083, 0)
    MonitorMessengerHatPossession(13, 4913, 6084, 0)
    MonitorMessengerHatPossession(14, 4914, 6085, 0)
    OfferDLCMessengerHats()

    # MULTIPLAYER (probably)
    Event12101100()
    Event12105300()
    AddSpecialEffect(PLAYER, Effects.InvaderBellsDisabled, affect_npc_part_hp=False)
    SkipLinesIfFlagEnabled(1, Flags.GehrmanRefusalCutsceneDone)
    AddSpecialEffect(PLAYER, Effects.SummonBellsDisabled, affect_npc_part_hp=False)
    Event12100330()


def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfFlagDisabled(2, Flags.MeleeWeaponGiftReceived)
    DisableBackread(Characters.MeleeWeaponGiftMessengers)
    DisableBackread(Characters.MeleeWeaponGift)

    SkipLinesIfFlagDisabled(2, Flags.GunGiftReceived)
    DisableBackread(Characters.GunGiftMessengers)
    DisableBackread(Characters.GunGift)

    SkipLinesIfFlagEnabled(2, CommonFlags.WorkshopOnFire)
    DisableBackread(Characters.GehrmanBoss)
    DisableBackread(Characters.MoonPresence)

    SkipLinesIfFlagEnabled(1, Flags.GehrmanRefusalCutsceneDone)
    EnableFlag(2100)

    GotoIfFlagDisabled(Label.L0, 1003)
    DisableFlag(1003)
    DisableFlag(72100110)
    DisableFlag(72100111)
    DisableFlag(72100112)
    DisableFlag(72100113)
    DisableFlag(72100114)
    GotoIfFlagDisabled(Label.L1, CommonFlags.WorkshopOnFire)
    EnableFlag(1002)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(1000)

    # --- 0 --- #
    DefineLabel(0)
    RunEvent(12100100, slot=0, args=(1000, 1019))
    RunEvent(12100101, slot=0, args=(1000, 1019))
    RunEvent(12100140, slot=0, args=(1020, 1039))
    RunEvent(12100141, slot=0, args=(1020, 1039))
    RunEvent(12100142, slot=0, args=(1020, 1039))
    RunEvent(12100143, slot=0, args=(1020, 1039))
    RunEvent(12100144, slot=0, args=(1020, 1039))
    RunEvent(12100145, slot=0, args=(1020, 1039))
    Event12100146()

    # NOTE: All character IDs I haven't replaced here do not exist in the MSB!
    DisableAnimations(Characters.StoragePrompt)
    DisableAnimations(Characters.UpgradePrompt)
    DisableAnimations(2100202)
    DisableAnimations(Characters.MemoryAltarPrompt)
    DisableAnimations(Characters.BathShopMessengers1)
    DisableAnimations(Characters.BathShopMessengers2)
    # `BathShopMessengers3` (2100213) is not included in this big disabling list for some reason.
    DisableAnimations(Characters.InsightShopMessengers2)  # has ID 2100219
    DisableAnimations(Characters.InsightShopMessengers1)
    DisableAnimations(Characters.MeleeWeaponGiftMessengers)
    DisableAnimations(Characters.GunGiftMessengers)
    DisableAnimations(2100217)
    DisableAnimations(Characters.StumpMessengers)
    DisableAnimations(Characters.MeleeWeaponGift)
    DisableAnimations(Characters.GunGift)
    DisableAnimations(2100222)
    DisableAnimations(Characters.BellGiftMessengers)
    DisableAnimations(Characters.OldHuntersMessengers)
    DisableAnimations(Characters.YharnamMessengers)
    DisableAnimations(Characters.FrontierMessengers)
    DisableAnimations(Characters.UnseenMessengers)
    DisableAnimations(Characters.NightmareMessengers)
    DisableAnimations(Characters.MakeshiftAltar)
    DisableAnimations(Characters.ChaliceAltar1)
    DisableAnimations(Characters.ChaliceAltar2)
    DisableAnimations(Characters.ChaliceAltar3)
    DisableAnimations(Characters.ChaliceAltar4)
    DisableAnimations(Characters.ChaliceAltar5)
    DisableAnimations(Characters.ChaliceAltar6)
    DisableGravity(Characters.StoragePrompt)
    DisableGravity(Characters.UpgradePrompt)
    DisableGravity(2100202)
    DisableGravity(Characters.MemoryAltarPrompt)
    DisableGravity(Characters.BathShopMessengers1)
    DisableGravity(Characters.BathShopMessengers2)
    DisableGravity(Characters.InsightShopMessengers2)
    DisableGravity(Characters.InsightShopMessengers1)
    DisableGravity(Characters.MeleeWeaponGiftMessengers)
    DisableGravity(Characters.GunGiftMessengers)
    DisableGravity(2100217)
    DisableGravity(Characters.StumpMessengers)
    DisableGravity(Characters.MeleeWeaponGift)
    DisableGravity(Characters.GunGift)
    DisableGravity(2100222)
    DisableGravity(Characters.BellGiftMessengers)
    DisableGravity(Characters.OldHuntersMessengers)
    DisableGravity(Characters.YharnamMessengers)
    DisableGravity(Characters.FrontierMessengers)
    DisableGravity(Characters.UnseenMessengers)
    DisableGravity(Characters.NightmareMessengers)
    DisableGravity(Characters.MakeshiftAltar)
    DisableGravity(Characters.ChaliceAltar1)
    DisableGravity(Characters.ChaliceAltar2)
    DisableGravity(Characters.ChaliceAltar3)
    DisableGravity(Characters.ChaliceAltar4)
    DisableGravity(Characters.ChaliceAltar5)
    DisableGravity(Characters.ChaliceAltar6)
    DisableCharacterCollision(Characters.StoragePrompt)
    DisableCharacterCollision(Characters.UpgradePrompt)
    DisableCharacterCollision(2100202)
    DisableCharacterCollision(Characters.MemoryAltarPrompt)
    DisableCharacterCollision(Characters.BathShopMessengers1)
    DisableCharacterCollision(Characters.BathShopMessengers2)
    DisableCharacterCollision(Characters.InsightShopMessengers2)
    DisableCharacterCollision(Characters.InsightShopMessengers1)
    DisableCharacterCollision(Characters.MeleeWeaponGiftMessengers)
    DisableCharacterCollision(Characters.GunGiftMessengers)
    DisableCharacterCollision(2100217)
    DisableCharacterCollision(Characters.StumpMessengers)
    DisableCharacterCollision(Characters.MeleeWeaponGift)
    DisableCharacterCollision(Characters.GunGift)
    DisableCharacterCollision(2100222)
    DisableCharacterCollision(Characters.BellGiftMessengers)
    DisableCharacterCollision(Characters.OldHuntersMessengers)
    DisableCharacterCollision(Characters.YharnamMessengers)
    DisableCharacterCollision(Characters.FrontierMessengers)
    DisableCharacterCollision(Characters.UnseenMessengers)
    DisableCharacterCollision(Characters.NightmareMessengers)
    DisableCharacterCollision(Characters.MakeshiftAltar)
    DisableCharacterCollision(Characters.ChaliceAltar1)
    DisableCharacterCollision(Characters.ChaliceAltar2)
    DisableCharacterCollision(Characters.ChaliceAltar3)
    DisableCharacterCollision(Characters.ChaliceAltar4)
    DisableCharacterCollision(Characters.ChaliceAltar5)
    DisableCharacterCollision(Characters.ChaliceAltar6)
    SkipLinesIfFlagDisabled(2, 12411000)
    DisableBackread(Characters.GehrmanBoss)
    DisableBackread(Characters.MoonPresence)


def FirstArrivalCutscene():
    """ 9401: Plays cutscene of first arrival in Hunter's Dream. """
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventFlagEnabled()
    EnableFlag(CommonFlags.CutsceneActive)
    PlayCutscene(Cutscenes.FirstArrival, skippable=True, fade_out=True, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableFlag(12417810)


def HonoringWishesEnding():
    """ 12100000: Defeat Gehrman, but be captivated by the Moon Presence (three cords not consumed). """
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, Flags.GehrmanDead)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, CommonFlags.ThreeCordsConsumed)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DeleteVFX(2103300, erase_root_only=True)
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    DeleteVFX(2103510, erase_root_only=True)
    DeleteVFX(2103511, erase_root_only=True)
    DeleteVFX(2103512, erase_root_only=True)
    DeleteVFX(2103513, erase_root_only=True)
    DeleteVFX(2103514, erase_root_only=True)
    DeleteVFX(2103515, erase_root_only=True)
    DeleteVFX(2103516, erase_root_only=True)
    DeleteVFX(2103517, erase_root_only=True)
    DeleteVFX(2103518, erase_root_only=True)
    DeleteVFX(2103519, erase_root_only=True)
    DeleteVFX(2103520, erase_root_only=True)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    PlayCutscene(Cutscenes.HonoringWishesEnding, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    AwardAchievement(Achievements.HonoringWishesEnding)
    MonitorToolAndBadgePossessionForNewGamePlus()
    Event12100451()
    Event12100452()
    WaitFrames(1)
    IncrementNewGameCycle(1)
    EnableFlag(6604)
    EnableFlag(6601)
    EnableFlag(6603)
    EnableFlag(CommonFlags.HonoringWishesEnding)


def ChildhoodsBeginningEnding():
    """ 12100002: Defeat Moon Presence. """
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, Flags.MoonPresenceDead)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    DeleteVFX(2103300, erase_root_only=True)  # burning workshop VFX
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    GotoIfPlayerGender(Label.L0, Gender.Male)
    PlayCutscene(Cutscenes.ChildhoodsBeginningEndingFemale, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(Cutscenes.ChildhoodsBeginningEndingMale, skippable=True, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    AwardAchievement(Achievements.ChildhoodsBeginningEnding)
    MonitorToolAndBadgePossessionForNewGamePlus()
    Event12100451()
    Event12100452()
    WaitFrames(1)
    IncrementNewGameCycle(1)
    EnableFlag(6604)
    EnableFlag(6602)
    EnableFlag(6603)
    EnableFlag(CommonFlags.ChildhoodsBeginningEnding)


def Event12100010():
    """ 12100010: Event 12100010 """
    IfFlagDisabled(1, CommonFlags.CentralYharnamVisited)
    IfCharacterInsideRegion(1, PLAYER, region=2102100)
    IfConditionTrue(0, input_condition=1)
    DisableObject(Objects.WorkshopFrontDoorClosed)
    EnableObject(Objects.WorkshopFrontDoorOpen)
    DisableObject(Objects.WorkshopBackDoorClosed)
    EnableObject(Objects.WorkshopBackDoorOpen)
    DisableObject(Objects.WorkshopMiddleDoorClosed)
    EnableObject(Objects.WorkshopMiddleDoorOpen)


def MonitorMessengerHatPossession(_, good: int, flag: int, do_disable_flag: int):
    """ 12100020: `flag` is enabled if player has `good` (excluding storage). If `do_disable_flag` == 1, `flag` is
    disabled before the check. """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfEqual(1, left=do_disable_flag, right=0)
    DisableFlag(flag)
    IfPlayerHasGood(0, good, including_box=False)
    EnableFlag(flag)


def Event12100100(_, arg_0_3: int, arg_4_7: int):
    """ 12100100: Event 12100100 """
    IfFlagDisabled(1, 1003)
    IfFlagEnabled(1, CommonFlags.WorkshopOnFire)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1002)


def Event12100101(_, arg_0_3: int, arg_4_7: int):
    """ 12100101: Event 12100101 """
    IfCharacterDead(0, Characters.PlainDoll)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1003)
    SaveRequest()


def InitializePlainDoll():
    """ 12100110: Event 12100110 """
    DisableFlag(72100105)
    DisableFlag(72100106)
    DisableFlag(72100107)
    DisableFlag(12100510)
    IfFlagDisabled(-1, 9401)
    IfPlayerInsightAmountEqual(-1, 0)
    GotoIfConditionTrue(Label.L9, input_condition=-1)
    EnableFlag(12100105)
    EnableFlag(9404)
    IfFlagEnabled(1, 13501800)
    IfFlagDisabled(1, 72100116)
    IfConditionTrue(-2, input_condition=1)
    IfFlagEnabled(2, 13601800)
    IfFlagDisabled(2, 72100117)
    IfFlagEnabled(-3, 1026)
    IfFlagEnabled(-3, 1027)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-2, input_condition=2)
    EndIfConditionTrue(-2)
    EndIfFlagEnabled(1000)
    GotoIfFlagEnabled(Label.L0, 1001)
    EndIfFlagEnabled(1002)
    GotoIfFlagEnabled(Label.L4, 1003)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 100)
    DisableFlagRange((12100500, 12100509))
    EnableRandomFlagInRange((12100500, 12100509))
    SkipLinesIfFlagDisabled(1, Flags.OldHuntersHeadstoneAvailable)
    DisableFlagRange((12100501, 12100502))
    GotoIfFlagEnabled(Label.L1, 12100500)
    GotoIfFlagEnabled(Label.L2, 12100501)
    GotoIfFlagEnabled(Label.L3, 12100502)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(Characters.PlainDoll, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9009, loop=True)
    Goto(Label.L8)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(12100510)
    Move(Characters.PlainDoll, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9000, loop=True)
    Goto(Label.L8)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(12100510)
    SkipLinesIfFlagEnabled(2, 6600)
    DisableFlag(12100502)
    End()
    Move(Characters.PlainDoll, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9000, loop=True)
    Goto(Label.L8)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L5, 12100500)
    GotoIfFlagEnabled(Label.L6, 12100501)
    GotoIfFlagEnabled(Label.L7, 12100502)
    Move(Characters.PlainDoll, destination=2102300, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 5 --- #
    DefineLabel(5)
    Move(Characters.PlainDoll, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 6 --- #
    DefineLabel(6)
    Move(Characters.PlainDoll, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 7 --- #
    DefineLabel(7)
    Move(Characters.PlainDoll, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 8 --- #
    DefineLabel(8)
    Event12100111()
    End()

    # --- 9 --- #
    DefineLabel(9)
    Move(Characters.PlainDoll, destination=2102304, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9011, loop=True)
    EnableFlag(12105100)


def Event12100111():
    """ 12100111: Event 12100111 """
    GotoIfFlagEnabled(Label.L0, 12100500)
    GotoIfFlagEnabled(Label.L1, 12100501)
    GotoIfFlagEnabled(Label.L1, 12100502)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72100105)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagDisabled(CommonFlags.BloodMoonPhase)
    SkipLinesIfFlagEnabled(3, 102)
    DisableFlagRange((12100520, 12100524))
    EnableRandomFlagInRange((12100520, 12100524))
    EndIfFlagDisabled(12100520)
    EnableFlag(72100105)
    End()


def Event12100112():
    """ 12100112: Event 12100112 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72100100)
    GotoIfFlagEnabled(Label.L0, 1003)
    GotoIfFlagEnabled(Label.L1, 12105100)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.PlainDoll, radius=1.0)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(2, PLAYER)
    IfEntityWithinDistance(2, PLAYER, Characters.PlainDoll, radius=1.0)
    IfConditionTrue(-1, input_condition=2)
    IfFramesElapsed(-1, 89)
    IfConditionTrue(0, input_condition=-1)

    # --- 2 --- #
    DefineLabel(2)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101270, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfEntityWithinDistance(3, PLAYER, Characters.PlainDoll, radius=1.5)
    GotoIfConditionTrue(Label.L3, input_condition=3)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfEntityWithinDistance(4, PLAYER, Characters.PlainDoll, radius=1.5)
    IfConditionTrue(-2, input_condition=4)
    IfFramesElapsed(-2, 89)
    IfConditionTrue(0, input_condition=-2)

    # --- 3 --- #
    DefineLabel(3)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101280, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101282)
    WaitFrames(25)
    DisableFlag(72100101)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHuman(5, PLAYER)
    IfEntityWithinDistance(5, PLAYER, Characters.PlainDoll, radius=2.0)
    GotoIfConditionTrue(Label.L4, input_condition=5)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(6, PLAYER)
    IfEntityWithinDistance(6, PLAYER, Characters.PlainDoll, radius=2.0)
    IfConditionTrue(0, input_condition=6)

    # --- 4 --- #
    DefineLabel(4)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101270, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()


def Event12100113():
    """ 12100113: Event 12100113 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(1)
    IfHealthEqual(-1, Characters.PlainDoll, 0.0)
    IfFlagEnabled(-1, 12105100)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    EnableFlag(72100102)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 72100100)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7021, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100102)
    WaitFrames(89)
    ForceAnimation(Characters.PlainDoll, 9010, loop=True)
    IfFlagDisabled(0, 72100100)
    ForceAnimation(Characters.PlainDoll, 7020)
    DisableFlag(72100102)
    WaitFrames(92)
    Restart()


def Event12100114():
    """ 12100114: Event 12100114 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 7500)
    CreateTemporaryVFX(178, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=1)
    DisableFlag(7500)
    Restart()


def Event12100115():
    """ 12100115: Event 12100115 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(2)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.PlainDoll, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthEqual(-1, Characters.PlainDoll, 0.0)
    IfFlagEnabled(-1, 12105100)
    IfFlagEnabled(-1, 72100105)
    EndIfConditionTrue(-1)
    IfCharacterHasSpecialEffect(2, Characters.PlainDoll, 151)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7010, wait_for_completion=False)
    WaitFrames(89)
    IfCharacterHasSpecialEffect(3, Characters.PlainDoll, 152)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7012, wait_for_completion=False)
    WaitFrames(0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)


def Event12100116():
    """ 12100116: Event 12100116 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72100108)
    DisableFlag(72100108)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 151)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7011, wait_for_completion=False)
    WaitFrames(89)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(2, Characters.PlainDoll, 152)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7013, wait_for_completion=False)
    WaitFrames(0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHasSpecialEffect(3, Characters.PlainDoll, 153)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7019, wait_for_completion=False)
    WaitFrames(89)

    # --- 2 --- #
    DefineLabel(2)
    Wait(0.0)


def Event12100117():
    """ 12100117: Event 12100117 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 160)
    IfFlagEnabled(1, 12100118)
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(2, PLAYER, 161)
    IfCharacterHasSpecialEffect(3, PLAYER, 162)
    IfCharacterHasSpecialEffect(4, PLAYER, 163)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7001, wait_for_completion=False)
    WaitFrames(1)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7000, wait_for_completion=False)
    WaitFrames(1)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7026, wait_for_completion=False)
    WaitFrames(39)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7025, wait_for_completion=False)
    Restart()


def Event12100120():
    """ 12100120: Event 12100120 """
    EndIfThisEventFlagEnabled()


def Event12100121():
    """ 12100121: Event 12100121 """
    IfPlayerHasGood(0, Goods.SmallHairOrnament, including_box=True)
    EnableFlag(12100122)
    IfPlayerDoesNotHaveGood(0, Goods.SmallHairOrnament, including_box=True)
    DisableFlag(12100122)
    Restart()


def Event12100123():
    """ 12100123: Event 12100123 """
    DisableNetworkSync()
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100114)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 160)
    IfFlagEnabled(1, 72100114)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.PlainDoll, 7030)
    IfFlagEnabled(0, 72100112)
    AwardItemLot(ItemLots.DollGift, host_only=False)
    RemoveGoodFromPlayer(Goods.SmallHairOrnament, quantity=1)


def Event12100140(_, arg_0_3: int, arg_4_7: int):
    """ 12100140: Event 12100140 """
    IfFlagEnabled(1, 1020)
    IfFlagEnabled(1, CommonFlags.CentralYharnamVisited)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1021)


def Event12100141(_, arg_0_3: int, arg_4_7: int):
    """ 12100141: Event 12100141 """
    IfFlagEnabled(1, 1022)
    IfFlagEnabled(1, 9800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1023)


def Event12100142(_, arg_0_3: int, arg_4_7: int):
    """ 12100142: Event 12100142 """
    IfFlagEnabled(1, 1024)
    IfFlagEnabled(-1, 12301800)
    IfFlagEnabled(-1, 9801)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1025)


def Event12100143(_, arg_0_3: int, arg_4_7: int):
    """ 12100143: Event 12100143 """
    IfFlagDisabled(1, 1029)
    IfFlagDisabled(1, 1030)
    IfFlagEnabled(1, CommonFlags.WorkshopOnFire)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1028)


def Event12100144(_, arg_0_3: int, arg_4_7: int):
    """ 12100144: Event 12100144 """
    IfFlagDisabled(1, 1030)
    IfFlagEnabled(1, Flags.GehrmanRefusalCutsceneDone)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1029)
    SaveRequest()


def Event12100145(_, arg_0_3: int, arg_4_7: int):
    """ 12100145: Event 12100145 """
    IfFlagEnabled(0, Flags.GehrmanDead)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1030)
    SaveRequest()


def Event12100146():
    """ 12100146: Event 12100146 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SetDistanceLimitForConversationStateChanges(Characters.GehrmanBoss, distance=17.0)
    IfFlagEnabled(0, 1029)
    SetDistanceLimitForConversationStateChanges(Characters.GehrmanBoss, distance=80.0)


def InitializeGehrmanAlly():
    """ 12100160: Event 12100160 """
    DisableFlag(72100133)
    DisableFlag(72100134)
    DisableFlag(72100135)
    DisableFlagRange((12105800, 12105809))
    IfCharacterBackreadEnabled(0, Characters.GehrmanAlly)
    GotoIfFlagEnabled(Label.L0, 1020)
    GotoIfFlagEnabled(Label.L1, 1021)
    GotoIfFlagEnabled(Label.L0, 1022)
    GotoIfFlagEnabled(Label.L1, 1023)
    GotoIfFlagEnabled(Label.L0, 1024)
    GotoIfFlagEnabled(Label.L1, 1025)
    GotoIfFlagEnabled(Label.L0, 1026)
    GotoIfFlagEnabled(Label.L0, 1027)
    GotoIfFlagEnabled(Label.L2, 1028)
    GotoIfFlagEnabled(Label.L3, 1029)
    GotoIfFlagEnabled(Label.L3, 1030)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.GehrmanAlly)
    Event12100161()
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(Characters.GehrmanAlly, destination=2102310, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(Characters.GehrmanAlly, 9002, loop=True)
    Move(Characters.GehrmanAlly, destination=2102312, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(Characters.GehrmanAlly)


def Event12100161():
    """ 12100161: Event 12100161 """
    IfFlagEnabled(1, 13601800)
    IfFlagDisabled(1, 72100117)
    EndIfConditionTrue(1)
    GotoIfFlagEnabled(Label.L1, 1027)
    GotoIfFlagEnabled(Label.L0, 1026)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange((12105800, 12105804))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagDisabled(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)


def OpenWorkshopDoors():
    """ 12100162: Event 12100162 """
    GotoIfFlagDisabled(Label.L0, CommonFlags.CentralYharnamVisited)
    DisableObject(Objects.WorkshopFrontDoorClosed)
    EnableObject(Objects.WorkshopFrontDoorOpen)
    DisableObject(Objects.WorkshopBackDoorClosed)
    EnableObject(Objects.WorkshopBackDoorOpen)
    DisableObject(Objects.WorkshopMiddleDoorClosed)
    EnableObject(Objects.WorkshopMiddleDoorOpen)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(Objects.WorkshopFrontDoorClosed)
    DisableObject(Objects.WorkshopFrontDoorOpen)
    EnableObject(Objects.WorkshopBackDoorClosed)
    DisableObject(Objects.WorkshopBackDoorOpen)
    EnableObject(Objects.WorkshopMiddleDoorClosed)
    DisableObject(Objects.WorkshopMiddleDoorOpen)


@RestartOnRest
def Event12100163():
    """ 12100163: Event 12100163 """
    DisableFlag(12100163)
    IfFlagDisabled(1, 1028)
    IfFlagDisabled(1, 1029)
    IfFlagDisabled(1, 1030)
    IfCharacterHasTAEEvent(1, Characters.GehrmanAlly, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12100163)


def Event12100164():
    """ 12100164: Event 12100164 """
    DisableSoapstoneMessage(2103000)
    DisableSoapstoneMessage(2103001)
    SkipLinesIfFlagDisabled(2, 1024)
    SkipLinesIfFlagEnabled(1, 5000)
    EnableSoapstoneMessage(2103000)
    IfFlagEnabled(-1, 1026)
    IfFlagEnabled(-1, 1027)
    SkipLinesIfConditionFalse(2, -1)
    SkipLinesIfFlagEnabled(1, 52400480)
    EnableSoapstoneMessage(2103001)


def Event12100165():
    """ 12100165: Event 12100165 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100136)
    IfFlagEnabled(0, 72100136)
    ForceAnimation(Characters.GehrmanAlly, 7000)
    WaitFrames(129)
    ForceAnimation(Characters.GehrmanAlly, 9003, loop=True)


def YharnamSunriseEnding():
    """ 12100180: Yharnam Sunrise ending. Accept Gehrman's offer. """
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(0, Flags.GehrmanOfferAccepted)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    DeleteVFX(2103300, erase_root_only=True)
    DeleteVFX(2103500, erase_root_only=True)
    DeleteVFX(2103501, erase_root_only=True)
    DeleteVFX(2103502, erase_root_only=True)
    DeleteVFX(2103503, erase_root_only=True)
    DeleteVFX(2103504, erase_root_only=True)
    DeleteVFX(2103505, erase_root_only=True)
    DeleteVFX(2103506, erase_root_only=True)
    DeleteVFX(2103507, erase_root_only=True)
    IncrementNewGameCycle(1)
    GotoIfPlayerGender(Label.L0, Gender.Male)
    PlayCutscene(Cutscenes.YharnamSunriseEndingFemale, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(Cutscenes.YharnamSunriseEndingMale, skippable=True, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    AwardAchievement(Achievements.YharnamSunriseEnding)
    EnableFlag(6604)
    MonitorToolAndBadgePossessionForNewGamePlus()
    Event12100451()
    Event12100452()
    WaitFrames(1)
    EnableFlag(CommonFlags.YharnamSunriseEnding)
    EnableFlag(6600)
    EnableFlag(6603)


def InitializeWorkshopAppearance():
    """ 12100300: I think this initializes the state of the workshop (e.g. fire), based on story progression. """
    GotoIfFlagEnabled(Label.L5, Flags.MoonPresenceBattleCutsceneDone)
    GotoIfFlagEnabled(Label.L4, CommonFlags.WorkshopOnFire)
    # The remaining story progression flags all have the same result (fire disabled).
    GotoIfFlagEnabled(Label.L3, CommonFlags.BloodMoonPhase)
    GotoIfFlagEnabled(Label.L2, 9801)
    GotoIfFlagEnabled(Label.L1, 9800)
    GotoIfFlagDisabled(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(Objects.NormalMoonSky)
    DisableObject(Objects.BloodMoonSky)
    EnableObject(Objects.NormalMoon)
    DisableObject(Objects.BloodMoon)
    DeleteVFX(2103300, erase_root_only=False)  # Workshop fire VFX.
    DeleteVFX(2103500, erase_root_only=False)
    DeleteVFX(2103501, erase_root_only=False)
    DeleteVFX(2103502, erase_root_only=False)
    DeleteVFX(2103503, erase_root_only=False)
    DeleteVFX(2103504, erase_root_only=False)
    DeleteVFX(2103505, erase_root_only=False)
    DeleteVFX(2103506, erase_root_only=False)
    DeleteVFX(2103507, erase_root_only=False)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(Objects.NormalMoonSky)
    DisableObject(Objects.BloodMoonSky)
    EnableObject(Objects.NormalMoon)
    DisableObject(Objects.BloodMoon)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableObject(Objects.NormalMoonSky)
    EnableObject(Objects.BloodMoonSky)
    DisableObject(Objects.NormalMoon)
    EnableObject(Objects.BloodMoon)


def InitializeDreamMusic():
    """ 12100310: Determine which music should play (if any). """
    GotoIfFlagEnabled(Label.L1, CommonFlags.WorkshopOnFire)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 50)
    IfFlagEnabled(-1, CommonFlags.BloodMoonPhase)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    EnableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(Music.NormalMusic)
    EnableSoundEvent(Music.BloodMoonMusic)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)


def Event12100330():
    """ 12100330: Event 12100330 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(-1, 5051)
    IfFlagEnabled(-1, 6660)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(5051)
    EnableFlag(6660)


def Event12100350(_, arg_0_3: int, arg_4_7: int):
    """ 12100350: UNUSED (no chests in Hunter's Dream). """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def OpenGateToField():
    """ 12100400: Opens iron gate to Gehrman battle if workshop is on fire. """
    EndIfFlagDisabled(CommonFlags.WorkshopOnFire)
    EndOfAnimation(Objects.IronGateToField, 1)


def DisplayMessageAtObject(_, action_button_id: int, obj: int, manual_trigger_flag: int, message: int):
    """ 12100410: Display a message if an object is activated or a certain flag enabled. """
    DisableNetworkSync()
    IfActionButtonParamActivated(-1, action_button_id=action_button_id, entity=obj)
    IfFlagEnabled(-1, manual_trigger_flag)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(manual_trigger_flag)
    DisplayDialog(
        message,
        anchor_entity=obj,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def MonitorToolAndBadgePossessionForNewGamePlus():
    """ 12100450: Enables appropriate flags if player has tools/badges in their inventory.

    Only called after an ending cutscene, hence why it's probably for NG+.
    """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerDoesNotHaveGood(1, Goods.BloodGemWorkshopTool, including_box=False)
    SkipLinesIfConditionTrue(1, 1)
    EnableFlag(6630)
    IfPlayerDoesNotHaveGood(2, Goods.RuneWorkshopTool, including_box=False)
    SkipLinesIfConditionTrue(1, 2)
    EnableFlag(6631)
    IfPlayerDoesNotHaveGood(3, Goods.ShortRitualRootChalice, including_box=False)
    SkipLinesIfConditionTrue(1, 3)
    EnableFlag(6632)
    IfPlayerDoesNotHaveGood(4, Goods.WorkshopHazeExtractor, including_box=False)
    SkipLinesIfConditionTrue(1, 4)
    EnableFlag(6633)
    IfPlayerDoesNotHaveGood(5, Goods.SawHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 5)
    EnableFlag(6640)
    IfPlayerDoesNotHaveGood(6, Goods.PowderKegHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 6)
    EnableFlag(6641)
    IfPlayerDoesNotHaveGood(7, Goods.OldHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 7)
    EnableFlag(6642)
    IfPlayerDoesNotHaveGood(8, Goods.CrowHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 8)
    EnableFlag(6643)
    IfPlayerDoesNotHaveGood(9, Goods.SparkHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 9)
    EnableFlag(6644)
    IfPlayerDoesNotHaveGood(10, Goods.SwordHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 10)
    EnableFlag(6645)
    IfPlayerDoesNotHaveGood(11, Goods.RadiantSwordHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 11)
    EnableFlag(6646)
    IfPlayerDoesNotHaveGood(12, Goods.WheelHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 12)
    EnableFlag(6647)
    IfPlayerDoesNotHaveGood(13, Goods.CosmicEyeWatcherBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 13)
    EnableFlag(6648)
    IfPlayerDoesNotHaveGood(14, Goods.CainhurstBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 14)
    EnableFlag(6649)
    End()


def Event12100451():
    """ 12100451: Event 12100451 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 50000400)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6300)
    IfFlagEnabled(2, 50000600)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6301)
    IfFlagEnabled(3, 50000800)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6302)
    IfFlagEnabled(4, 50001100)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6303)
    IfFlagEnabled(5, 50001300)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6304)
    IfFlagEnabled(6, 50001610)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6305)
    IfFlagEnabled(7, 50002110)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6306)
    IfFlagEnabled(8, 50003400)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6307)
    IfFlagEnabled(9, 50003500)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6308)
    IfFlagEnabled(10, 52200380)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6309)
    IfFlagEnabled(11, 52420640)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6310)
    IfFlagEnabled(12, 52420690)
    SkipLinesIfConditionFalse(1, 12)
    EnableFlag(6311)
    IfFlagEnabled(13, 52410640)
    SkipLinesIfConditionFalse(1, 13)
    EnableFlag(6312)
    IfFlagEnabled(14, 52420120)
    SkipLinesIfConditionFalse(1, 14)
    EnableFlag(6313)
    IfFlagEnabled(15, 52600390)
    SkipLinesIfConditionFalse(1, 15)
    EnableFlag(6314)
    IfFlagEnabled(-1, 52600300)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6315)
    IfFlagEnabled(-2, 52700180)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6316)
    IfFlagEnabled(-3, 52700200)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6317)
    IfFlagEnabled(-4, 52700380)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6318)
    IfFlagEnabled(-5, 52700540)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6319)
    IfFlagEnabled(-6, 52700570)
    SkipLinesIfConditionFalse(1, -6)
    EnableFlag(6320)
    IfFlagEnabled(-7, 52700950)
    SkipLinesIfConditionFalse(1, -7)
    EnableFlag(6321)
    IfFlagEnabled(-8, 52800050)
    SkipLinesIfConditionFalse(1, -8)
    EnableFlag(6322)
    IfFlagEnabled(-9, 52800140)
    SkipLinesIfConditionFalse(1, -9)
    EnableFlag(6323)
    IfFlagEnabled(-10, 52800350)
    SkipLinesIfConditionFalse(1, -10)
    EnableFlag(6324)
    IfFlagEnabled(-11, 53200010)
    SkipLinesIfConditionFalse(1, -11)
    EnableFlag(6325)
    IfFlagEnabled(-12, 53200640)
    SkipLinesIfConditionFalse(1, -12)
    EnableFlag(6326)
    IfFlagEnabled(-13, 53300110)
    SkipLinesIfConditionFalse(1, -13)
    EnableFlag(6327)
    IfFlagEnabled(-14, 53300150)
    SkipLinesIfConditionFalse(1, -14)
    EnableFlag(6328)
    IfFlagEnabled(-15, 53300320)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(6329)


def Event12100452():
    """ 12100452: Event 12100452 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 53300420)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6330)
    IfFlagEnabled(2, 53300480)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6331)
    IfFlagEnabled(3, 9458)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6332)
    IfFlagEnabled(4, 12400861)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6333)
    IfFlagEnabled(5, 50003100)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6334)
    IfFlagEnabled(6, 50001500)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6335)
    IfFlagEnabled(7, 52605000)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6336)
    IfFlagEnabled(8, 50000200)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6340)
    IfFlagEnabled(9, 50001820)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6341)
    IfFlagEnabled(10, 50001910)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6342)
    IfFlagEnabled(11, 50002260)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6677)


def LogPlayerEquipmentOnFirstArrival():
    """ 12100990: Event 12100990 """
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2103600)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 0, PlayLogMultiplayerType.HostOnly)


def InitializeBossArena():
    """ 12100800: Initializes boss characters and boss fog as needed. """
    GotoIfFlagDisabled(Label.L0, Flags.MoonPresenceDead)

    # Moon Presence (and Gehrman) dead.
    DisableCharacter(Characters.MoonPresence)
    DisableCharacter(Characters.GehrmanBoss)
    SkipLinesIfClient(2)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, Flags.MoonPresenceBattleCutsceneDone)
    DisableCharacter(Characters.GehrmanBoss)
    End()

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, Flags.GehrmanDead)
    DisableCharacter(Characters.MoonPresence)
    DisableCharacter(Characters.GehrmanBoss)
    SkipLinesIfClient(2)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    End()

    # --- 2 --- # Gehrman is waiting to be fought.
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, Flags.GehrmanRefusalCutsceneDone)
    DisableCharacter(Characters.MoonPresence)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(Characters.MoonPresence)
    DisableCharacter(Characters.GehrmanBoss)
    SkipLinesIfClient(2)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)


def GehrmanDies():
    """ 12101800: Gehrman is killed in his boss battle. """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableSoundEvent(Music.GehrmanPhase1Music)
    DisableSoundEvent(Music.GehrmanPhase2Music)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(Flags.GehrmanBattleWon)
    IfHealthEqual(0, Characters.GehrmanBoss, 0.0)
    EnableFlag(Flags.GehrmanBattleWon)
    IfCharacterDead(1, Characters.GehrmanBoss)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFlagEnabled(2, CommonFlags.ThreeCordsConsumed)
    KillBoss(Characters.GehrmanBoss)
    SkipLines(1)
    HandleMinibossDefeat(Characters.GehrmanBoss)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    SkipLinesIfFlagEnabled(2, 6642)
    AwardItemLot(15000, host_only=False)
    SkipLines(1)
    AwardItemLot(15005, host_only=False)
    StopPlayLogMeasurement(2100000)
    StopPlayLogMeasurement(2100001)
    StopPlayLogMeasurement(2100010)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 34, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayGehrmanDeathSound():
    """ 12101801: Play a `CharacterMotion` sound (0) when Gehrman dies. """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfFlagEnabled(1, Flags.GehrmanDead)
    IfCharacterBackreadDisabled(2, Characters.GehrmanBoss)
    IfHealthLessThanOrEqual(2, Characters.GehrmanBoss, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=Regions.BossFogRotateTarget, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def RefuseGehrmansOffer():
    """ 12101802: Refuse Gehrman's offer, play the one-time cutscene, and start the boss battle. """
    EndIfFlagEnabled(Flags.GehrmanDead)
    EndIfThisEventFlagEnabled()

    DisableCharacter(Characters.GehrmanBoss)
    DisableFlag(Flags.GehrmanOfferRefused)
    IfFlagEnabled(0, Flags.GehrmanOfferRefused)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    PlayCutscene(
        Cutscenes.GehrmanBossBattleStarts, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=2102808,
        move_to_map=HUNTERS_DREAM,
    )
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableCharacter(Characters.GehrmanBoss)
    DisableCharacter(Characters.GehrmanAlly)
    EnableFlag(Flags.GehrmanBattleFogEntered)
    DisableFlag(2100)
    EndIfFlagEnabled(CommonFlags.InsightGained_GehrmanBattle)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(CommonFlags.InsightGained_GehrmanBattle)


def SummonStartGehrmanBattle():
    """ 12101803: Catches things up if the active battle flag is enabled elsewhere, presumably. """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.GehrmanBattleFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.GehrmanBoss)
    DisableCharacter(Characters.GehrmanAlly)
    EnableFlag(Flags.GehrmanBattleFogEntered)
    EnableFlag(Flags.GehrmanRefusalCutsceneDone)


def EnterGehrmanBossFog():
    """ 12104810: Event 12104810 """
    EndIfFlagEnabled(Flags.GehrmanDead)
    GotoIfFlagEnabled(Label.L0, Flags.GehrmanRefusalCutsceneDone)
    IfFlagDisabled(1, Flags.GehrmanDead)
    IfFlagEnabled(1, Flags.GehrmanRefusalCutsceneDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.BossFog)
    CreateVFX(VFX.BossFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.GehrmanDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=Characters.GehrmanBoss, entity=Objects.BossFog)
    IfFlagEnabled(3, Flags.GehrmanDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, Regions.BossFogRotateTarget, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.GehrmanBattleFogEntered)
    Restart()


def EnterGehrmanBossFogAsSummon():
    """ 12104811: Event 12104811 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfFlagDisabled(1, Flags.GehrmanDead)
    IfFlagEnabled(1, Flags.GehrmanRefusalCutsceneDone)
    IfFlagEnabled(1, Flags.GehrmanBattleFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=Characters.GehrmanBoss, entity=Objects.BossFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Regions.BossFogRotateTarget, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(Flags.GehrmanBattleStartedForSummon)
    Restart()


def StartGehrmanBossBattle():
    """ 12104802: Apply multiplayer buffs to Gehrman and activate his AI and health bar. """
    EndIfFlagEnabled(Flags.GehrmanDead)
    DisableAI(Characters.GehrmanBoss)
    DisableHealthBar(Characters.GehrmanBoss)
    EnableInvincibility(Characters.GehrmanBoss)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.GehrmanBattleFogEntered)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.GehrmanBoss, UpdateAuthority.Normal)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.GehrmanBattleFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.GehrmanBoss, 7500, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GehrmanBoss)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.GehrmanBoss, 7501, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GehrmanBoss)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.GehrmanBoss)
    EnableBossHealthBar(Characters.GehrmanBoss, name=BossNames.Gehrman, slot=0)
    DisableInvincibility(Characters.GehrmanBoss)
    SetCharacterEventTarget(Characters.GehrmanBoss, 2100801)
    CreatePlayLog(64)
    StartPlayLogMeasurement(2100010, 80, overwrite=True)


def ControlGehrmanMusic():
    """ 12104803: Enables Gehrman music, including second phase. """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GehrmanDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(Music.GehrmanPhase1Music)
    DisableSoundEvent(Music.GehrmanPhase2Music)
    IfFlagDisabled(1, Flags.GehrmanDead)
    IfFlagEnabled(1, Flags.GehrmanBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, Flags.GehrmanBattleStartedForSummon)
    IfCharacterInsideRegion(1, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    EnableBossMusic(Music.GehrmanPhase1Music)
    IfCharacterHasTAEEvent(2, Characters.GehrmanBoss, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.GehrmanDead)
    IfFlagEnabled(2, Flags.GehrmanBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, Flags.GehrmanBattleStartedForSummon)
    IfCharacterInsideRegion(2, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(Music.GehrmanPhase1Music)
    WaitFrames(0)
    EnableBossMusic(Music.GehrmanPhase2Music)


def ToggleGehrmanCamera():
    """ 12104804: Change camera when Gehrman gets closer than 8 units. """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfHealthGreaterThan(1, Characters.GehrmanBoss, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.GehrmanBoss, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.GehrmanBoss, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.GehrmanBoss, radius=10.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


def StopGehrmanBossMusic():
    """ 12104805: Stops boss music as soon as boss health reaches zero. """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfFlagEnabled(0, Flags.GehrmanBattleWon)
    DisableBossMusic(Music.GehrmanPhase1Music)
    DisableBossMusic(Music.GehrmanPhase2Music)
    DisableBossMusic(-1)


def ActivateGehrmanPhaseTwo():
    """ 12104807: Instructs Gehrman to extend his Burial Blade for phase two. """
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfHealthLessThan(0, Characters.GehrmanBoss, 0.5)
    AICommand(Characters.GehrmanBoss, command_id=100, slot=0)
    IfCharacterHasTAEEvent(0, Characters.GehrmanBoss, tae_event_id=100)
    CancelSpecialEffect(Characters.GehrmanBoss, 5305)
    AICommand(Characters.GehrmanBoss, command_id=-1, slot=0)
    ReplanAI(Characters.GehrmanBoss)
    Wait(0.10000000149011612)
    AICommand(Characters.GehrmanBoss, command_id=1, slot=1)


def GehrmanBuffWearsOff():
    """ 12104808: Educated guess. Waits for TAE event 20 and cancels effect 5526. """
    EndIfFlagEnabled(Flags.GehrmanDead)
    IfCharacterHasTAEEvent(0, Characters.GehrmanBoss, tae_event_id=20)
    CancelSpecialEffect(Characters.GehrmanBoss, 5526)
    Wait(0.10000000149011612)
    Restart()


def MoonPresenceDies():
    """ 12101850: Moon Presence is killed in battle. """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableSoundEvent(Music.MoonPresencePhase1Music)
    DisableSoundEvent(Music.MoonPresencePhase2Music)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.MoonPresence)
    EnableFlag(12104859)
    DisplayBanner(BannerType.NightmareSlain)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.MoonPresence)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(5,))
    StopPlayLogMeasurement(2100011)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 96, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayMoonPresenceDeathSound():
    """ 12101851: Event 12101851 """
    DisableNetworkSync()
    EndIfFlagEnabled(12101850)
    IfFlagEnabled(1, 12101850)
    IfCharacterBackreadDisabled(2, Characters.MoonPresence)
    IfHealthLessThanOrEqual(2, Characters.MoonPresence, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=Regions.BossFogRotateTarget, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def MoonPresenceBattleCutscene():
    """ 12101852: Moon Presence arrives after Gehrman dies, if three cords have been consumed. """
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    EndIfThisEventFlagEnabled()

    IfFlagEnabled(1, Flags.GehrmanDead)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2103601)
    IfPlayerStandingOnCollision(-1, 2103602)
    IfPlayerStandingOnCollision(-1, 2103603)
    IfPlayerStandingOnCollision(-1, 2103604)
    IfPlayerStandingOnCollision(-1, 2103605)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, CommonFlags.ThreeCordsConsumed)
    IfConditionTrue(0, input_condition=1)

    Wait(3.0)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    DeleteVFX(2103510, erase_root_only=True)
    DeleteVFX(2103511, erase_root_only=True)
    DeleteVFX(2103512, erase_root_only=True)
    DeleteVFX(2103513, erase_root_only=True)
    DeleteVFX(2103514, erase_root_only=True)
    DeleteVFX(2103515, erase_root_only=True)
    DeleteVFX(2103516, erase_root_only=True)
    DeleteVFX(2103517, erase_root_only=True)
    DeleteVFX(2103518, erase_root_only=True)
    DeleteVFX(2103519, erase_root_only=True)
    DeleteVFX(2103520, erase_root_only=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        Cutscenes.MoonPresenceBattleStarts, skippable=True, fade_out=False, player_id=PLAYER,
        move_to_region=Regions.MoonPresenceBattlePlayerStart,
        move_to_map=HUNTERS_DREAM,
    )
    SkipLines(1)
    PlayCutscene(
        Cutscenes.MoonPresenceBattleStarts, skippable=False, fade_out=False, player_id=PLAYER,
        move_to_region=Regions.MoonPresenceBattlePlayerStart,
        move_to_map=HUNTERS_DREAM,
    )
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    CreateVFX(2103510)
    CreateVFX(2103511)
    CreateVFX(2103512)
    CreateVFX(2103513)
    CreateVFX(2103514)
    CreateVFX(2103515)
    CreateVFX(2103516)
    CreateVFX(2103517)
    CreateVFX(2103518)
    CreateVFX(2103519)
    CreateVFX(2103520)
    DisableObject(Objects.NormalMoonSky)
    EnableObject(Objects.BloodMoonSky)
    DisableObject(Objects.NormalMoon)
    EnableObject(Objects.BloodMoon)
    EnableCharacter(Characters.MoonPresence)
    EnableFlag(Flags.MoonPresenceBattleActive)
    EndIfFlagEnabled(9307)
    RunEvent(9350, 0, args=(5,))
    EnableFlag(9307)


def SummonStartMoonPresenceBattle():
    """ 12101853: Event 12101853 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.MoonPresenceBattleActive)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableObject(Objects.NormalMoonSky)
    EnableObject(Objects.BloodMoonSky)
    DisableObject(Objects.NormalMoon)
    EnableObject(Objects.BloodMoon)
    EnableCharacter(Characters.MoonPresence)
    EnableFlag(Flags.MoonPresenceBattleActive)
    EnableFlag(Flags.MoonPresenceBattleCutsceneDone)


def EnterMoonPresenceBossFog():
    """ 12104880: Event 12104880 """
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    GotoIfFlagEnabled(Label.L0, Flags.MoonPresenceBattleCutsceneDone)
    IfFlagDisabled(1, Flags.MoonPresenceDead)
    IfFlagEnabled(1, Flags.MoonPresenceBattleCutsceneDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.BossFog)
    CreateVFX(VFX.BossFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.MoonPresenceDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=Characters.GehrmanBoss, entity=Objects.BossFog)
    IfFlagEnabled(3, Flags.MoonPresenceDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, Regions.BossFogRotateTarget, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2102801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.MoonPresenceBattleActive)
    Restart()


def EnterMoonPresenceFogAsSummon():
    """ 12104881: Event 12104881 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    IfFlagDisabled(1, Flags.MoonPresenceDead)
    IfFlagEnabled(1, Flags.MoonPresenceBattleCutsceneDone)
    IfFlagEnabled(1, Flags.MoonPresenceBattleActive)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=Characters.GehrmanBoss, entity=Objects.BossFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Regions.BossFogRotateTarget, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12104851)
    Restart()


def StartMoonPresenceBossBattle():
    """ 12104852: Event 12104852 """
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    DisableAI(Characters.MoonPresence)
    DisableHealthBar(Characters.MoonPresence)
    EnableInvincibility(Characters.MoonPresence)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.MoonPresenceBattleActive)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.MoonPresence, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.MoonPresenceBattleActive)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.MoonPresence, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MoonPresence)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.MoonPresence, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MoonPresence)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.MoonPresence)
    EnableBossHealthBar(Characters.MoonPresence, name=540000, slot=0)
    DisableInvincibility(Characters.MoonPresence)
    CreatePlayLog(128)
    StartPlayLogMeasurement(2100011, 146, overwrite=True)


def ControlMoonPresenceMusic():
    """ 12104853: Enable Moon Presence music, including second phase. """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(Music.MoonPresencePhase1Music)
    DisableSoundEvent(Music.MoonPresencePhase2Music)
    IfFlagDisabled(1, Flags.MoonPresenceDead)
    IfFlagEnabled(1, Flags.MoonPresenceBattleCutsceneDone)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12104851)
    IfCharacterInsideRegion(1, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    EnableBossMusic(Music.MoonPresencePhase1Music)
    IfCharacterHasTAEEvent(0, Characters.MoonPresence, tae_event_id=500)
    IfFlagDisabled(2, Flags.MoonPresenceDead)
    IfFlagEnabled(2, Flags.MoonPresenceBattleCutsceneDone)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12104851)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(Music.MoonPresencePhase1Music)
    WaitFrames(0)
    EnableBossMusic(Music.MoonPresencePhase2Music)


def ToggleMoonPresenceCamera():
    """ 12104854: Event 12104854 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    IfHealthGreaterThan(1, Characters.MoonPresence, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.MoonPresence, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.MoonPresence, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.MoonPresence, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


def StopMoonPresenceBossMusic():
    """ 12104855: Event 12104855 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MoonPresenceDead)
    IfFlagEnabled(0, 12104859)
    DisableBossMusic(Music.MoonPresencePhase1Music)
    DisableBossMusic(Music.MoonPresencePhase2Music)
    DisableBossMusic(-1)


def ControlMoonPresenceTail(
    _, part_id: short, monitor_part_id: int, part_index: short, part_health: int, limb_broken_speffect: int,
    limb_unbroken_speffect: int, wounded_animation: int,
):
    """ 12104860: Event 12104860 """
    EndIfFlagEnabled(Flags.MoonPresenceDead)

    CreateNPCPart(
        Characters.MoonPresence,
        npc_part_id=part_id,
        part_index=part_index,
        part_health=part_health,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(
        Characters.MoonPresence, npc_part_id=monitor_part_id, material_sfx_id=59, material_vfx_id=59
    )

    IfCharacterPartHealthLessThanOrEqual(2, Characters.MoonPresence, npc_part_id=monitor_part_id, value=0)
    IfHealthLessThanOrEqual(3, Characters.MoonPresence, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)

    EndIfFinishedConditionTrue(3)

    CreateNPCPart(
        Characters.MoonPresence,
        npc_part_id=part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(
        Characters.MoonPresence, npc_part_id=monitor_part_id, material_sfx_id=60, material_vfx_id=60
    )
    ResetAnimation(Characters.MoonPresence, disable_interpolation=False)
    ForceAnimation(Characters.MoonPresence, wounded_animation)
    AddSpecialEffect(Characters.MoonPresence, limb_broken_speffect, affect_npc_part_hp=False)
    CancelSpecialEffect(Characters.MoonPresence, limb_unbroken_speffect)
    ReplanAI(Characters.MoonPresence)

    Wait(30.0)

    AICommand(Characters.MoonPresence, command_id=10, slot=1)
    ReplanAI(Characters.MoonPresence)
    IfCharacterHasTAEEvent(0, Characters.MoonPresence, tae_event_id=300)
    SetNPCPartHealth(Characters.MoonPresence, npc_part_id=monitor_part_id, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.MoonPresence, limb_unbroken_speffect, affect_npc_part_hp=False)
    CancelSpecialEffect(Characters.MoonPresence, limb_broken_speffect)
    AICommand(Characters.MoonPresence, command_id=-1, slot=1)
    ReplanAI(Characters.MoonPresence)
    WaitFrames(10)
    return RESTART


def MoonPresenceSinHarvest():
    """ 12104870: Activate player immortality temporarily after "sin harvest" 1 HP attack by Moon Presence. """
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, Characters.MoonPresence, tae_event_id=10)
    EnableImmortality(PLAYER)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5570)
    IfFramesElapsed(-1, 70)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(5)
    DisableImmortality(PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=PLAYER, attacker=Characters.MoonPresence,
                             damage_type=DamageType.Unspecified)
    IfTimeElapsed(-1, 10.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 5572)
    Restart()


@RestartOnRest
def AnimateHeadstoneMessengers(_, headstone_messengers: Character, headstone_active_flag: Flag):
    """ 12105000: Wake up messengers of a given headstone. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7000)
    WaitFrames(109)
    ForceAnimation(headstone_messengers, c9020.WaitingGrouped, loop=True)
    IfFlagDisabled(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7002)
    WaitFrames(74)
    return RESTART


@RestartOnRest
def AnimateOldHuntersHeadstoneMessengers(_, headstone_messengers: Character, headstone_active_flag: Flag):
    """ 12105004: Variant of 12105000 that also moves and gives a special effect to the messengers.

    Note that the only instance of this is run with slot 3 for some reason.
    """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, headstone_active_flag)
    Move(headstone_messengers, destination=2102305, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(headstone_messengers, 5401, affect_npc_part_hp=False)
    ForceAnimation(headstone_messengers, 7000)
    WaitFrames(109)
    ForceAnimation(headstone_messengers, c9020.WaitingGrouped, loop=True)
    IfFlagDisabled(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7002)
    WaitFrames(74)
    Restart()


@RestartOnRest
def InitializeMakeshiftAltar():
    """ 12105010: Event 12105010 """
    DisableObject(2101200)
    DisableObject(2101201)
    DisableObject(2101202)
    DisableObject(2101203)
    DisableObject(2101204)
    DisableObject(2101205)
    DisableObject(2101206)
    DisableObject(2101207)
    DisableObject(2101208)
    IfFlagEnabled(10, 94005500)
    IfFlagRangeAnyEnabled(10, (94005100, 94005101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94005500)
    IfFlagRangeAnyEnabled(11, (94005103, 94005104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94005500)
    IfFlagEnabled(12, 94005102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94005503)
    GotoIfFlagEnabled(Label.L4, 94005504)
    GotoIfFlagEnabled(Label.L5, 94005505)
    GotoIfFlagEnabled(Label.L6, 94005502)
    GotoIfFlagEnabled(Label.L7, 94005507)
    GotoIfFlagEnabled(Label.L8, 94005501)
    IfFlagEnabled(1, 94005500)
    IfFlagRangeAnyEnabled(1, (94005100, 94005101))
    IfFlagEnabled(2, 94005500)
    IfFlagRangeAnyEnabled(2, (94005103, 94005104))
    IfFlagEnabled(3, 94005500)
    IfFlagEnabled(3, 94005102)
    IfFlagEnabled(4, 94005503)
    IfFlagEnabled(5, 94005504)
    IfFlagEnabled(6, 94005505)
    IfFlagEnabled(7, 94005502)
    IfFlagEnabled(8, 94005507)
    IfFlagEnabled(9, 94005501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.MakeshiftAltar, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101200)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101201)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101202)
    IfFlagDisabled(0, 94005500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101203)
    IfFlagDisabled(0, 94005503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101204)
    IfFlagDisabled(0, 94005504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101205)
    IfFlagDisabled(0, 94005505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101206)
    IfFlagDisabled(0, 94005502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101207)
    IfFlagDisabled(0, 94005507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101208)
    IfFlagDisabled(0, 94005501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.MakeshiftAltar, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar1():
    """ 12105011: Event 12105011 """
    DisableObject(2101210)
    DisableObject(2101211)
    DisableObject(2101212)
    DisableObject(2101213)
    DisableObject(2101214)
    DisableObject(2101215)
    DisableObject(2101216)
    DisableObject(2101217)
    DisableObject(2101218)
    IfFlagEnabled(10, 94105500)
    IfFlagRangeAnyEnabled(10, (94105100, 94105101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94105500)
    IfFlagRangeAnyEnabled(11, (94105103, 94105104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94105500)
    IfFlagEnabled(12, 94105102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94105503)
    GotoIfFlagEnabled(Label.L4, 94105504)
    GotoIfFlagEnabled(Label.L5, 94105505)
    GotoIfFlagEnabled(Label.L6, 94105502)
    GotoIfFlagEnabled(Label.L7, 94105507)
    GotoIfFlagEnabled(Label.L8, 94105501)
    IfFlagEnabled(1, 94105500)
    IfFlagRangeAnyEnabled(1, (94105100, 94105101))
    IfFlagEnabled(2, 94105500)
    IfFlagRangeAnyEnabled(2, (94105103, 94105104))
    IfFlagEnabled(3, 94105500)
    IfFlagEnabled(3, 94105102)
    IfFlagEnabled(4, 94105503)
    IfFlagEnabled(5, 94105504)
    IfFlagEnabled(6, 94105505)
    IfFlagEnabled(7, 94105502)
    IfFlagEnabled(8, 94105507)
    IfFlagEnabled(9, 94105501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar1, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101210)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101211)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101212)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101213)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101214)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101215)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101216)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101217)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101218)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagDisabled(0, 94105501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar1, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar2():
    """ 12105012: Event 12105012 """
    DisableObject(2101220)
    DisableObject(2101221)
    DisableObject(2101222)
    DisableObject(2101223)
    DisableObject(2101224)
    DisableObject(2101225)
    DisableObject(2101226)
    DisableObject(2101227)
    DisableObject(2101228)
    IfFlagEnabled(10, 94205500)
    IfFlagRangeAnyEnabled(10, (94205100, 94205101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94205500)
    IfFlagRangeAnyEnabled(11, (94205103, 94205104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94205500)
    IfFlagEnabled(12, 94205102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94205503)
    GotoIfFlagEnabled(Label.L4, 94205504)
    GotoIfFlagEnabled(Label.L5, 94205505)
    GotoIfFlagEnabled(Label.L6, 94205502)
    GotoIfFlagEnabled(Label.L7, 94205507)
    GotoIfFlagEnabled(Label.L8, 94205501)
    IfFlagEnabled(1, 94205500)
    IfFlagRangeAnyEnabled(1, (94205100, 94205101))
    IfFlagEnabled(2, 94205500)
    IfFlagRangeAnyEnabled(2, (94205103, 94205104))
    IfFlagEnabled(3, 94205500)
    IfFlagEnabled(3, 94205102)
    IfFlagEnabled(4, 94205503)
    IfFlagEnabled(5, 94205504)
    IfFlagEnabled(6, 94205505)
    IfFlagEnabled(7, 94205502)
    IfFlagEnabled(8, 94205507)
    IfFlagEnabled(9, 94205501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar2, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101220)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101221)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101222)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101223)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101224)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101225)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101226)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101227)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101228)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagDisabled(0, 94205501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar2, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar3():
    """ 12105013: Event 12105013 """
    DisableObject(2101230)
    DisableObject(2101231)
    DisableObject(2101232)
    DisableObject(2101233)
    DisableObject(2101234)
    DisableObject(2101235)
    DisableObject(2101236)
    DisableObject(2101237)
    DisableObject(2101238)
    IfFlagEnabled(10, 94305500)
    IfFlagRangeAnyEnabled(10, (94305100, 94305101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94305500)
    IfFlagRangeAnyEnabled(11, (94305103, 94305104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94305500)
    IfFlagEnabled(12, 94305102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94305503)
    GotoIfFlagEnabled(Label.L4, 94305504)
    GotoIfFlagEnabled(Label.L5, 94305505)
    GotoIfFlagEnabled(Label.L6, 94305502)
    GotoIfFlagEnabled(Label.L7, 94305507)
    GotoIfFlagEnabled(Label.L8, 94305501)
    IfFlagEnabled(1, 94305500)
    IfFlagRangeAnyEnabled(1, (94305100, 94305101))
    IfFlagEnabled(2, 94305500)
    IfFlagRangeAnyEnabled(2, (94305103, 94305104))
    IfFlagEnabled(3, 94305500)
    IfFlagEnabled(3, 94305102)
    IfFlagEnabled(4, 94305503)
    IfFlagEnabled(5, 94305504)
    IfFlagEnabled(6, 94305505)
    IfFlagEnabled(7, 94305502)
    IfFlagEnabled(8, 94305507)
    IfFlagEnabled(9, 94305501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar3, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101230)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101231)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101232)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101233)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101234)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101235)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101236)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101237)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101238)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagDisabled(0, 94305501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar3, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar4():
    """ 12105014: Event 12105014 """
    DisableObject(2101240)
    DisableObject(2101241)
    DisableObject(2101242)
    DisableObject(2101243)
    DisableObject(2101244)
    DisableObject(2101245)
    DisableObject(2101246)
    DisableObject(2101247)
    DisableObject(2101248)
    IfFlagEnabled(10, 94405500)
    IfFlagRangeAnyEnabled(10, (94405100, 94405101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94405500)
    IfFlagRangeAnyEnabled(11, (94405103, 94405104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94405500)
    IfFlagEnabled(12, 94405102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94405503)
    GotoIfFlagEnabled(Label.L4, 94405504)
    GotoIfFlagEnabled(Label.L5, 94405505)
    GotoIfFlagEnabled(Label.L6, 94405502)
    GotoIfFlagEnabled(Label.L7, 94405507)
    GotoIfFlagEnabled(Label.L8, 94405501)
    IfFlagEnabled(1, 94405500)
    IfFlagRangeAnyEnabled(1, (94405100, 94405101))
    IfFlagEnabled(2, 94405500)
    IfFlagRangeAnyEnabled(2, (94405103, 94405104))
    IfFlagEnabled(3, 94405500)
    IfFlagEnabled(3, 94405102)
    IfFlagEnabled(4, 94405503)
    IfFlagEnabled(5, 94405504)
    IfFlagEnabled(6, 94405505)
    IfFlagEnabled(7, 94405502)
    IfFlagEnabled(8, 94405507)
    IfFlagEnabled(9, 94405501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar4, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101240)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101241)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101242)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101243)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101244)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101245)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101246)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101247)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101248)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagDisabled(0, 94405501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar4, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar5():
    """ 12105015: Event 12105015 """
    DisableObject(2101250)
    DisableObject(2101251)
    DisableObject(2101252)
    DisableObject(2101253)
    DisableObject(2101254)
    DisableObject(2101255)
    DisableObject(2101256)
    DisableObject(2101257)
    DisableObject(2101258)
    IfFlagEnabled(10, 94505500)
    IfFlagRangeAnyEnabled(10, (94505100, 94505101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94505500)
    IfFlagRangeAnyEnabled(11, (94505103, 94505104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94505500)
    IfFlagEnabled(12, 94505102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94505503)
    GotoIfFlagEnabled(Label.L4, 94505504)
    GotoIfFlagEnabled(Label.L5, 94505505)
    GotoIfFlagEnabled(Label.L6, 94505502)
    GotoIfFlagEnabled(Label.L7, 94505507)
    GotoIfFlagEnabled(Label.L8, 94505501)
    IfFlagEnabled(1, 94505500)
    IfFlagRangeAnyEnabled(1, (94505100, 94505101))
    IfFlagEnabled(2, 94505500)
    IfFlagRangeAnyEnabled(2, (94505103, 94505104))
    IfFlagEnabled(3, 94505500)
    IfFlagEnabled(3, 94505102)
    IfFlagEnabled(4, 94505503)
    IfFlagEnabled(5, 94505504)
    IfFlagEnabled(6, 94505505)
    IfFlagEnabled(7, 94505502)
    IfFlagEnabled(8, 94505507)
    IfFlagEnabled(9, 94505501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar5, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101250)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101251)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101252)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101253)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101254)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101255)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101256)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101257)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101258)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagDisabled(0, 94505501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar5, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar6():
    """ 12105016: Event 12105016 """
    DisableObject(2101260)
    DisableObject(2101261)
    DisableObject(2101262)
    DisableObject(2101263)
    DisableObject(2101264)
    DisableObject(2101265)
    DisableObject(2101266)
    DisableObject(2101267)
    DisableObject(2101268)
    IfFlagEnabled(10, 94605500)
    IfFlagRangeAnyEnabled(10, (94605100, 94605101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagEnabled(11, 94605500)
    IfFlagRangeAnyEnabled(11, (94605103, 94605104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagEnabled(12, 94605500)
    IfFlagEnabled(12, 94605102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagEnabled(Label.L3, 94605503)
    GotoIfFlagEnabled(Label.L4, 94605504)
    GotoIfFlagEnabled(Label.L5, 94605505)
    GotoIfFlagEnabled(Label.L6, 94605502)
    GotoIfFlagEnabled(Label.L7, 94605507)
    GotoIfFlagEnabled(Label.L8, 94605501)
    IfFlagEnabled(1, 94605500)
    IfFlagRangeAnyEnabled(1, (94605100, 94605101))
    IfFlagEnabled(2, 94605500)
    IfFlagRangeAnyEnabled(2, (94605103, 94605104))
    IfFlagEnabled(3, 94605500)
    IfFlagEnabled(3, 94605102)
    IfFlagEnabled(4, 94605503)
    IfFlagEnabled(5, 94605504)
    IfFlagEnabled(6, 94605505)
    IfFlagEnabled(7, 94605502)
    IfFlagEnabled(8, 94605507)
    IfFlagEnabled(9, 94605501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar6, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101260)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101261)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101262)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101263)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101264)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101265)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101266)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101267)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101268)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagDisabled(0, 94605501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar6, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def EnableYharnamHeadstone():
    """ 12105020: Animates messengers at given headstone if any lanterns are available.

    Only flag 12417810 is enabled anywhere in EMEVD, after arriving in the Hunter's Dream for the first time, which is
    the automatic lantern lit in Iosekfa's Clinic.
    """
    IfFlagEnabled(-1, 12417810)
    IfFlagEnabled(-1, 12417830)
    IfFlagEnabled(-1, 12417850)
    IfFlagEnabled(-1, 12417870)
    IfFlagEnabled(-1, 12407810)
    IfFlagEnabled(-1, 12407830)
    IfFlagEnabled(-1, 12427810)
    IfFlagEnabled(-1, 12427830)
    IfFlagEnabled(-1, 12427850)
    IfFlagEnabled(-1, 12307810)
    IfFlagEnabled(-1, 12307830)
    IfFlagEnabled(-1, 12307850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(Flags.YharnamHeadstoneAvailable)
    IfFlagEnabled(-2, 12417810)
    IfFlagEnabled(-2, 12417830)
    IfFlagEnabled(-2, 12417850)
    IfFlagEnabled(-2, 12417870)
    IfFlagEnabled(-2, 12407810)
    IfFlagEnabled(-2, 12407830)
    IfFlagEnabled(-2, 12427810)
    IfFlagEnabled(-2, 12427830)
    IfFlagEnabled(-2, 12427850)
    IfFlagEnabled(-2, 12307810)
    IfFlagEnabled(-2, 12307830)
    IfFlagEnabled(-2, 12307850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(Flags.YharnamHeadstoneAvailable)
    Restart()


@RestartOnRest
def EnableFrontierHeadstone():
    """ 12105021: Event 12105021 """
    IfFlagEnabled(-1, 12207810)
    IfFlagEnabled(-1, 12207830)
    IfFlagEnabled(-1, 12707810)
    IfFlagEnabled(-1, 12707830)
    IfFlagEnabled(-1, 13207810)
    IfFlagEnabled(-1, 13207850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(Flags.FrontierHeadstoneAvailable)
    IfFlagEnabled(-2, 12207810)
    IfFlagEnabled(-2, 12207830)
    IfFlagEnabled(-2, 12707810)
    IfFlagEnabled(-2, 12707830)
    IfFlagEnabled(-2, 13207810)
    IfFlagEnabled(-2, 13207850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(Flags.FrontierHeadstoneAvailable)
    Restart()


@RestartOnRest
def EnableUnseenHeadstone():
    """ 12105022: Event 12105022 """
    IfFlagEnabled(-1, 12807810)
    IfFlagEnabled(-1, 12807830)
    IfFlagEnabled(-1, 12807850)
    IfFlagEnabled(-1, 12807870)
    IfFlagEnabled(-1, 12507810)
    IfFlagEnabled(-1, 12507830)
    IfFlagEnabled(-1, 12507850)
    IfFlagEnabled(-1, 12117810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(Flags.UnseenHeadstoneAvailable)
    IfFlagEnabled(-2, 12807810)
    IfFlagEnabled(-2, 12807830)
    IfFlagEnabled(-2, 12807850)
    IfFlagEnabled(-2, 12807870)
    IfFlagEnabled(-2, 12507810)
    IfFlagEnabled(-2, 12507830)
    IfFlagEnabled(-2, 12507850)
    IfFlagEnabled(-2, 12117810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(Flags.UnseenHeadstoneAvailable)
    Restart()


@RestartOnRest
def EnableNightmareHeadstone():
    """ 12105023: Event 12105023 """
    IfFlagEnabled(-1, 13207830)
    IfFlagEnabled(-1, 13207870)
    IfFlagEnabled(-1, 13307810)
    IfFlagEnabled(-1, 13307830)
    IfFlagEnabled(-1, 12607810)
    IfFlagEnabled(-1, 12607830)
    IfFlagEnabled(-1, 12607850)
    IfFlagEnabled(-1, 12607870)
    IfFlagEnabled(-1, 13307810)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(Flags.NightmareHeadstoneAvailable)
    IfFlagEnabled(-2, 13207830)
    IfFlagEnabled(-2, 13207870)
    IfFlagEnabled(-2, 13307810)
    IfFlagEnabled(-2, 13307830)
    IfFlagEnabled(-2, 12607810)
    IfFlagEnabled(-2, 12607830)
    IfFlagEnabled(-2, 12607850)
    IfFlagEnabled(-2, 12607870)
    IfFlagEnabled(-2, 13307810)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(Flags.NightmareHeadstoneAvailable)
    Restart()


@RestartOnRest
def EnableOldHuntersHeadstone():
    """ 12105024: Event 12105024 """
    IfFlagEnabled(-1, 13407810)
    IfFlagEnabled(-1, 13407830)
    IfFlagEnabled(-1, 13407850)
    IfFlagEnabled(-1, 13407870)
    IfFlagEnabled(-1, 13507810)
    IfFlagEnabled(-1, 13507830)
    IfFlagEnabled(-1, 13507850)
    IfFlagEnabled(-1, 13607810)
    IfFlagEnabled(-1, 13607830)
    IfFlagEnabled(-1, 13607850)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(Flags.OldHuntersHeadstoneAvailable)
    IfFlagEnabled(-2, 13407810)
    IfFlagEnabled(-2, 13407830)
    IfFlagEnabled(-2, 13407850)
    IfFlagEnabled(-2, 13407870)
    IfFlagEnabled(-2, 13507810)
    IfFlagEnabled(-2, 13507830)
    IfFlagEnabled(-2, 13507850)
    IfFlagEnabled(-2, 13607810)
    IfFlagEnabled(-2, 13607830)
    IfFlagEnabled(-2, 13607850)
    IfConditionFalse(0, input_condition=-2)
    DisableFlag(Flags.OldHuntersHeadstoneAvailable)
    Restart()


@RestartOnRest
def InitializeBathMessengers():
    """ 12105040: Event 12105040 """
    ForceAnimation(Characters.BathShopMessengers1, c9020.WaitingGrouped, loop=True)
    ForceAnimation(Characters.BathShopMessengers2, 7002, loop=True)
    ForceAnimation(Characters.BathShopMessengers3, 7041, loop=True)
    IfFlagEnabled(0, 12105041)
    ForceAnimation(Characters.BathShopMessengers1, 7005)
    ForceAnimation(Characters.BathShopMessengers2, 7006)
    ForceAnimation(Characters.BathShopMessengers3, 7045)
    WaitFrames(29)
    ForceAnimation(Characters.BathShopMessengers1, c9020.Disappear, loop=True)
    ForceAnimation(Characters.BathShopMessengers2, c9020.Appear, loop=True)
    ForceAnimation(Characters.BathShopMessengers3, 7043, loop=True)
    IfFlagDisabled(0, 12105041)
    ForceAnimation(Characters.BathShopMessengers1, 7007)
    ForceAnimation(Characters.BathShopMessengers2, 7008)
    ForceAnimation(Characters.BathShopMessengers3, 7047)
    WaitFrames(28)
    Restart()


def BathMessengerAppearance(_, required_badge: int, messenger: int, mask_bit_index_1: uchar, mask_bit_index_2: uchar):
    """ 12101000: Change bath messenger appearance when certain badges are unlocked. """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, messenger)
    SetDisplayMask(messenger, bit_index=mask_bit_index_1, switch_type=OnOffChange.On)
    SetDisplayMask(messenger, bit_index=mask_bit_index_2, switch_type=OnOffChange.On)
    IfPlayerHasGood(0, required_badge, including_box=False)
    SetDisplayMask(messenger, bit_index=mask_bit_index_1, switch_type=OnOffChange.Off)
    SetDisplayMask(messenger, bit_index=mask_bit_index_2, switch_type=OnOffChange.Off)


def InitializeStoryProgressionFlags():
    """ 12101010: Enables flags in 5900-5904 range depending on story progression. """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfFlagDisabled(1, 9800)
    EnableFlag(5900)
    SkipLinesIfFlagDisabled(1, 9801)
    EnableFlag(5901)
    SkipLinesIfFlagDisabled(1, CommonFlags.BloodMoonPhase)
    EnableFlag(5902)
    SkipLinesIfFlagDisabled(1, CommonFlags.OneRebornDead)
    EnableFlag(5903)
    SkipLinesIfFlagDisabled(1, CommonFlags.WetNurseDead)
    EnableFlag(5904)
    SkipLinesIfFlagDisabled(1, 6603)
    EnableFlagRange((5900, 5904))


@RestartOnRest
def InitializeInsightShop():
    """ 12105043: Second Insight shop messenger wakes up when player has 1 insight. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, Flags.InsightShopOpen)
    ForceAnimation(Characters.InsightShopMessengers2, 7030, loop=True)
    EndIfClient()
    IfPlayerInsightAmountGreaterThanOrEqual(0, 1)
    EnableFlag(Flags.InsightShopOpen)
    ForceAnimation(Characters.InsightShopMessengers2, 7031)  # doll wakes up
    WaitFrames(30)
    EnableFlag(12105045)  # flag probably used in Doll ESD
    WaitFrames(79)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12105045)
    ForceAnimation(Characters.InsightShopMessengers2, 7032, loop=True)
    IfFlagEnabled(0, 12105044)
    ForceAnimation(Characters.InsightShopMessengers2, 7034)
    WaitFrames(29)
    ForceAnimation(Characters.InsightShopMessengers2, 7035, loop=True)
    IfFlagDisabled(0, 12105044)
    ForceAnimation(Characters.InsightShopMessengers2, 7036)
    WaitFrames(28)
    return RESTART


def OfferMeleeWeaponGift():
    """ 12101020: Event 12101020 """
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(Characters.MeleeWeaponGiftMessengers, 7013, loop=True)
    ForceAnimation(Characters.MeleeWeaponGift, 7013, loop=True)
    IfCharacterBackreadEnabled(1, Characters.MeleeWeaponGiftMessengers)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.MeleeWeaponGiftMessengers, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.MeleeWeaponGiftMessengers, 7014)
    ForceAnimation(Characters.MeleeWeaponGift, 7014)
    WaitFrames(30)
    EnableFlag(12105050)
    WaitFrames(79)
    ForceAnimation(Characters.MeleeWeaponGiftMessengers, 7011, loop=True)
    ForceAnimation(Characters.MeleeWeaponGift, 7011, loop=True)
    IfFlagEnabled(-1, 72101000)
    IfFlagEnabled(-1, 72101001)
    IfFlagEnabled(-1, 72101002)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(12105050)
    EnableFlag(12101020)
    ForceAnimation(Characters.MeleeWeaponGiftMessengers, 7012)
    ForceAnimation(Characters.MeleeWeaponGift, 7012)
    WaitFrames(49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(Characters.MeleeWeaponGiftMessengers)
    DisableBackread(Characters.MeleeWeaponGift)


def OfferGunGift():
    """ 12101021: Event 12101021 """
    GotoIfThisEventFlagEnabled(Label.L0)
    ForceAnimation(Characters.GunGiftMessengers, 7023, loop=True)
    ForceAnimation(Characters.GunGift, 7023, loop=True)
    IfCharacterBackreadEnabled(1, Characters.GunGiftMessengers)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.GunGiftMessengers, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.GunGiftMessengers, 7024)
    ForceAnimation(Characters.GunGift, 7024)
    WaitFrames(30)
    EnableFlag(12105051)
    WaitFrames(79)
    ForceAnimation(Characters.GunGiftMessengers, 7021, loop=True)
    ForceAnimation(Characters.GunGift, 7021, loop=True)
    IfFlagEnabled(-1, 72101010)
    IfFlagEnabled(-1, 72101011)
    IfConditionTrue(0, input_condition=-1)
    EventValueOperation(12104010, 8, 10, 0, 1, CalculationType.Assign)
    StoreItemAmountSpecifiedByFlagValue(ItemType.Good, 900, 12104020, 8)
    EventValueOperation(12104010, 8, 0, 12104020, 8, CalculationType.Subtract)
    IfEventValueEqual(0, 0, bit_count=1, value=0)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    GivePlayerItemAmountSpecifiedByFlagValue(ItemType.Good, 900, 12104010, 8)
    DisableFlag(12105051)
    EnableFlag(12101021)
    ForceAnimation(Characters.GunGiftMessengers, 7022)
    ForceAnimation(Characters.GunGift, 7022)
    WaitFrames(49)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(Characters.GunGiftMessengers)
    DisableBackread(Characters.GunGift)


def OfferNotebookGift():
    """ 12101022: Awards Notebook to player. """
    GotoIfFlagEnabled(Label.L0, 6620)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingHidden, loop=True)
    IfCharacterBackreadEnabled(1, Characters.BellGiftMessengers)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.BellGiftMessengers, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingAppear)
    WaitFrames(30)
    EnableFlag(12105052)
    WaitFrames(79)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingWaiting, loop=True)
    IfFlagEnabled(0, 12101023)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10000, host_only=False)
    DisableFlag(12105052)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingDisappear)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingHidden, loop=True)


def OfferBeckoningBellGift():
    """ 12101024: Offer Beckoning Bell and Silencing Blank to player. """
    GotoIfFlagEnabled(Label.L0, 6622)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingHidden, loop=True)
    IfCharacterBackreadEnabled(1, Characters.OldHuntersMessengers)
    IfFlagEnabled(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingAppear)
    WaitFrames(30)
    EnableFlag(12105054)
    WaitFrames(79)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingWaiting, loop=True)
    IfFlagEnabled(0, 12101025)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10010, host_only=False)
    DisableFlag(12105054)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingDisappear)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingHidden, loop=True)


def OfferOldHunterBellGift():
    """ 12101026: Offer Old Hunter Bell gift to players. """
    GotoIfFlagEnabled(Label.L0, 6670)
    IfCharacterBackreadEnabled(1, Characters.BellGiftMessengers)
    IfFlagEnabled(1, 12101022)
    IfFlagEnabled(1, 12100105)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingAppear)
    WaitFrames(30)
    EnableFlag(12105056)
    WaitFrames(79)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingWaiting, loop=True)
    IfFlagEnabled(0, 12101027)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10050, host_only=False)
    DisableFlag(12105056)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingDisappear)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingHidden, loop=True)


def OfferDLCAccessGift():
    """ 12101028: Offer Eye of a Blood-Drunk Hunter to player. """
    GotoIfFlagEnabled(Label.L0, 50000100)
    IfCharacterBackreadEnabled(1, Characters.OldHuntersMessengers)
    IfFlagEnabled(1, 12101024)
    IfFlagEnabled(1, 9801)
    IfFlagEnabled(1, 6899)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingAppear)
    WaitFrames(30)
    EnableFlag(12105058)
    WaitFrames(79)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingWaiting, loop=True)
    IfFlagEnabled(0, 12101029)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AwardItemLot(10040, host_only=False)
    DisableFlag(12105058)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingDisappear)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingHidden, loop=True)


def Event12101100():
    """ 12101100: Event 12101100 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 6899)
    IfFlagEnabled(1, 9801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12101101)


@RestartOnRest
def StumpMessengersRemoveHats():
    """ 12105060: Event 12105060 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagEnabled(0, 72100140)
    EnableFlag(12105061)
    DisableFlag(72100140)
    DisableFlagRange((CommonFlags.RequestMessengerHat1, CommonFlags.RequestMessengerHat15))
    RotateToFaceEntity(PLAYER, Characters.StumpMessengers, animation=101310, wait_for_completion=False)
    Wait(1.0)
    ForceAnimation(Characters.StumpMessengers, c9020.Disappear)
    WaitFrames(39)
    SetDisplayMask(Characters.StumpMessengers, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=28, switch_type=OnOffChange.On)
    ForceAnimation(Characters.StumpMessengers, c9020.Appear)
    WaitFrames(49)
    ForceAnimation(Characters.StumpMessengers, c9020.WaitingGrouped, loop=True)
    Restart()


def StumpMessengersAppear():
    """ 12105062: Stump messengers appear if you have any hats in your inventory. """
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L0, Flags.StumpMessengersActive)
    ForceAnimation(Characters.StumpMessengers, 0, loop=True)  # 0 == "hiding"
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat1)
    SetDisplayMask(Characters.StumpMessengers, bit_index=20, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat2)
    SetDisplayMask(Characters.StumpMessengers, bit_index=21, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat3)
    SetDisplayMask(Characters.StumpMessengers, bit_index=22, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat4)
    SetDisplayMask(Characters.StumpMessengers, bit_index=23, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat5)
    SetDisplayMask(Characters.StumpMessengers, bit_index=24, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat6)
    SetDisplayMask(Characters.StumpMessengers, bit_index=25, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat7)
    SetDisplayMask(Characters.StumpMessengers, bit_index=26, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat8)
    SetDisplayMask(Characters.StumpMessengers, bit_index=27, switch_type=OnOffChange.Off)
    SkipLinesIfFlagDisabled(1, CommonFlags.RequestMessengerHat9)
    SetDisplayMask(Characters.StumpMessengers, bit_index=28, switch_type=OnOffChange.Off)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat1)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat2)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat3)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat4)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat5)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat6)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat7)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat8)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat9)
    IfFlagEnabled(-1, 6080)
    IfFlagEnabled(-1, 6081)
    IfFlagEnabled(-1, 6082)
    IfFlagEnabled(-1, 6083)
    IfFlagEnabled(-1, 6084)
    IfFlagEnabled(-1, 6085)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(Characters.StumpMessengers, c9020.Appear)
    WaitFrames(89)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.StumpMessengers, c9020.WaitingGrouped, loop=True)
    IfCharacterHuman(14, PLAYER)
    EndIfConditionFalse(14)
    EnableFlag(Flags.StumpMessengersActive)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat1)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat2)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat3)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat4)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat5)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat6)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat7)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat8)
    IfFlagEnabled(-1, CommonFlags.PlayerHasMessengerHat9)
    IfFlagEnabled(-1, 6080)
    IfFlagEnabled(-1, 6081)
    IfFlagEnabled(-1, 6082)
    IfFlagEnabled(-1, 6083)
    IfFlagEnabled(-1, 6084)
    IfFlagEnabled(-1, 6085)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(Flags.StumpMessengersActive)
    ForceAnimation(Characters.StumpMessengers, c9020.Disappear)
    WaitFrames(39)
    Restart()


def OfferDLCMessengerHats():
    """ 12105064: Offer three DLC messenger hats under certain conditions, near stump messengers. """
    DisableNetworkSync()
    ForceAnimation(Characters.NearStumpMessengers, c9020.OfferingHidden, loop=True)
    EndIfClient()
    IfFlagEnabled(1, 6900)
    IfFlagDisabled(1, CommonFlags.PlayerHasMessengerHat1)
    IfFlagEnabled(2, 6901)
    IfFlagDisabled(2, CommonFlags.PlayerHasMessengerHat2)
    IfFlagEnabled(3, 6902)
    IfFlagDisabled(3, CommonFlags.PlayerHasMessengerHat3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(Characters.NearStumpMessengers, c9020.OfferingAppear)
    WaitFrames(30)
    WaitFrames(79)
    ForceAnimation(Characters.NearStumpMessengers, c9020.OfferingWaiting, loop=True)
    IfCharacterHuman(4, PLAYER)
    IfActionButtonParamActivated(4, action_button_id=6025, entity=Characters.NearStumpMessengers)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFlagEnabled(3, CommonFlags.PlayerHasMessengerHat1)
    SkipLinesIfFlagDisabled(2, 6900)
    AwardItemLot(2100900, host_only=False)
    EnableFlag(CommonFlags.PlayerHasMessengerHat1)
    SkipLinesIfFlagEnabled(3, CommonFlags.PlayerHasMessengerHat2)
    SkipLinesIfFlagDisabled(2, 6901)
    AwardItemLot(2100910, host_only=False)
    EnableFlag(CommonFlags.PlayerHasMessengerHat2)
    SkipLinesIfFlagEnabled(3, CommonFlags.PlayerHasMessengerHat3)
    SkipLinesIfFlagDisabled(2, 6902)
    AwardItemLot(2100920, host_only=False)
    EnableFlag(CommonFlags.PlayerHasMessengerHat3)
    ForceAnimation(Characters.NearStumpMessengers, c9020.OfferingDisappear)
    WaitFrames(74)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.NearStumpMessengers)


@RestartOnRest
def ChangeStumpMessengerHat(_, hat_request_flag: int, hat_active_flag: int, hat_mask_bit_index: uchar):
    """ 12105070: Stump messengers hide, change their display mask to the requested hat, and pop back up. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12105061)
    IfFlagEnabled(0, hat_request_flag)
    EnableFlag(12105061)
    DisableFlag(hat_request_flag)
    DisableFlagRange((CommonFlags.RequestMessengerHat1, CommonFlags.RequestMessengerHat15))
    RotateToFaceEntity(PLAYER, Characters.StumpMessengers, animation=101310, wait_for_completion=False)
    Wait(1.0)
    ForceAnimation(Characters.StumpMessengers, c9020.Disappear)
    WaitFrames(39)
    EnableFlag(hat_active_flag)
    SetDisplayMask(Characters.StumpMessengers, bit_index=20, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=21, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=22, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=23, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=24, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=25, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=26, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=27, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=28, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.StumpMessengers, bit_index=hat_mask_bit_index, switch_type=OnOffChange.Off)
    ForceAnimation(Characters.StumpMessengers, c9020.Appear)
    WaitFrames(49)
    ForceAnimation(Characters.StumpMessengers, c9020.WaitingGrouped, loop=True)
    Restart()


def Event12105200():
    """ 12105200: Enables this flag 1 frame after Plain Doll has effect 153. """
    DisableFlag(12105200)
    IfCharacterHasSpecialEffect(0, Characters.PlainDoll, 153)
    WaitFrames(1)


def MonitorWeaponBuffRemovalRequest():
    """ 12105210: Event 12105210 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, CommonFlags.RequestWeaponBuffRemoval)
    DisableFlag(CommonFlags.RequestWeaponBuffRemoval)
    CancelSpecialEffect(PLAYER, Effects.FirePaper)
    CancelSpecialEffect(PLAYER, Effects.EmptyPhantasmShell)
    CancelSpecialEffect(PLAYER, Effects.BoltPaper)
    Restart()


def Event12105300():
    """ 12105300: Event 12105300 """
    DisableNetworkSync()
    EndIfClient()
    SkipLinesIfFlagDisabled(1, 5020)
    EnableFlag(6228)
    SkipLinesIfFlagDisabled(1, 5021)
    EnableFlag(6235)
    IfFlagEnabled(-1, 5023)
    IfFlagEnabled(-1, 70009200)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6242)
    SkipLinesIfFlagDisabled(1, 5027)
    EnableFlag(6249)
    IfFlagEnabled(-2, 5029)
    IfFlagEnabled(-2, 70009220)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6256)
    SkipLinesIfFlagDisabled(1, 5022)
    EnableFlag(6236)
    IfFlagEnabled(-3, 5025)
    IfFlagEnabled(-3, 70009210)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6243)
    SkipLinesIfFlagDisabled(1, 5028)
    EnableFlag(6251)
    IfFlagEnabled(-4, 5031)
    IfFlagEnabled(-4, 70009230)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6258)
    IfFlagEnabled(-5, 5033)
    IfFlagEnabled(-5, 70009240)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6259)


@RestartOnRest
def AnimateChaliceAltar(_, required_flag: int, altar_chr: int):
    """ 12105310: Event 12105310 """
    IfFlagEnabled(0, required_flag)
    WaitFrames(31)
    ForceAnimation(altar_chr, 7000)
    WaitFrames(109)
    ForceAnimation(altar_chr, c9020.WaitingGrouped, loop=True)
    IfFlagDisabled(0, required_flag)
    ForceAnimation(altar_chr, 7002)
    WaitFrames(74)
    Restart()


def WarpAtHeadstone(_, choice_flag: int, headstone: int, warp_point: int):
    """ 12107000: Activate a headstone warp out into Yharnam, the Nightmare, etc. """
    EndIfClient()
    IfFlagEnabled(0, choice_flag)
    RotateToFaceEntity(PLAYER, headstone, animation=PlayerAnimations.WarpAtHeadstone, wait_for_completion=False)
    Wait(4.0)
    WarpPlayerToRespawnPoint(warp_point)


def ActivateChaliceAltar(_, choice_flag: int, altar_chr: int, ritual_flag: int):
    """ 12107100: Event 12107100 """
    EndIfClient()
    IfFlagEnabled(0, choice_flag)
    Wait(4.0)
    DisableFlag(9020)
    DisableFlag(9021)
    DisableFlag(9022)
    DisableFlag(9023)
    DisableFlag(9024)
    DisableFlag(9025)
    DisableFlag(9026)
    EnableFlag(ritual_flag)
    DisableFlag(choice_flag)
    End()
    RotateToFaceEntity(PLAYER, altar_chr, animation=101164, wait_for_completion=False)


def WarpToChaliceDungeon(_, choice_flag: int, warp_point: int, flag_to_enable: int):
    """ 12107200: Event 12107200 """
    IfFlagEnabled(0, choice_flag)
    DisableFlag(choice_flag)
    WarpPlayerToRespawnPoint(warp_point)
    EnableFlag(flag_to_enable)
