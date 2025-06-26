from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    9401: ("FirstArrivalCutscene", "Plays cutscene of first arrival in Hunter's Dream."),
    12100000: ("HonoringWishesEnding", "Defeat Gehrman, but be captivated by the Moon Presence (three cords not consumed)."),
    12100002: ("ChildhoodsBeginningEnding", "Defeat Moon Presence."),
    12100020: ("MonitorMessengerHatPossession", "`flag` is enabled if player has `good` (excluding storage). If `do_disable_flag` == 1, `flag` is disabled before the check."),
    12100110: ("InitializePlainDoll", ""),
    12100146: ("SetGehrmanBossTalkDistance", ""),
    12100160: ("InitializeGehrmanAlly", ""),
    12100162: ("OpenWorkshopDoors", ""),
    12100180: ("YharnamSunriseEnding", "Accept Gehrman's offer without fighting him."),
    12100300: ("InitializeWorkshopAppearance", "Set Workshop appearance based on story progression."),
    12100310: ("InitializeDreamMusic", "Determine which music should play (if any)."),
    12100350: ("OpenChest", "NOTE: There are no chests in the Hunter's Dream."),
    12100400: ("OpenGateToField", "Open iron gate to Gehrman battle if Workshop is on fire."),
    12100410: ("DisplayMessageAtObject", "Display a message if an object is activated or a certain flag enabled."),
    12100450: ("MonitorToolAndBadgePossessionForNewGamePlus", "Enables appropriate flags if player has tools/badges. Only called after ending cutscene."),
    12100990: ("LogPlayerEquipmentOnFirstArrival", ""),
    12100800: ("InitializeBossArena", "Initialize boss characters/fog as needed."),
    12101800: ("GehrmanDies", "Gehrman is killed in battle."),
    12101801: ("PlayGehrmanDeathSound", "Play a 'CharacterMotion' sound (0) when Gehrman dies."),
    12101802: ("RefuseGehrmansOffer", "Refuse Gehrman's offer and play his battle intro cutscene."),
    12101803: ("SummonStartGehrmanBattle", "Catches things up if the Gehrman battle flag is enabled."),
    12104810: ("EnterGehrmanBossFog", ""),
    12104811: ("EnterGehrmanBossFogAsSummon", ""),
    12104802: ("StartGehrmanBossBattle", "Apply multiplayer buffs and activate AI/health bar."),
    12104803: ("ControlGehrmanMusic", "Control boss music and control phase change."),
    12104804: ("ToggleGehrmanCamera", "Change camera when Gehrman is close."),
    12104805: ("StopGehrmanBossMusic", "Stop boss music when Gehrman dies."),
    12104807: ("ActivateGehrmanPhaseTwo", "Tell Gehrman to change AI state for phase two."),
    12104808: ("GehrmanBuffWearsOff", "Educated guess. Waits for TAE event 20 and cancels SpEffect 5526."),
    12100850: ("MoonPresenceDies", "Moon Presence is defeated."),
    12101850: ("PlayMoonPresenceDeathSound", ""),
    12101852: ("MoonPresenceBattleCutscene", "Moon Presence arrives after Gehrman dies if three cords have been consumed."),
    12101853: ("SummonStartMoonPresenceBattle", ""),
    12104880: ("EnterMoonPresenceBossFog", ""),
    12104881: ("EnterMoonPresenceFogAsSummon", ""),
    12104852: ("StartMoonPresenceBossBattle", ""),
    12104853: ("ControlMoonPresenceMusic", ""),
    12104854: ("ToggleMoonPresenceCamera", ""),
    12104855: ("StopMoonPresenceBossMusic", ""),
    12104860: ("ControlMoonPresenceTail", ""),
    12104870: ("MoonPresenceSinHarvest", "Active player immortality temporarily after 'sin harvest' 1 HP attack."),
    12105000: ("AnimateHeadstoneMessengers", "Wake up messengers at a given headstone."),
    12105004: ("AnimateOldHuntersHeadstoneMessengers", "Variant of 12105000 that also moves and gives a SpEffect to the messengers."),
    12105010: ("InitializeMakeshiftAltar", ""),
    12105011: ("InitializeChaliceAltar1", ""),
    12105012: ("InitializeChaliceAltar2", ""),
    12105013: ("InitializeChaliceAltar3", ""),
    12105014: ("InitializeChaliceAltar4", ""),
    12105015: ("InitializeChaliceAltar5", ""),
    12105016: ("InitializeChaliceAltar6", ""),
    12105020: ("EnableYharnamHeadstone", "Animates messengers at headstone if any lanterns are available. Flag 12417810 (Iosefka's Clinic) is enabled on first arrival at Hunter's Dream."),
    12105021: ("EnableFrontierHeadstone", ""),
    12105022: ("EnableUnseenHeadstone", ""),
    12105023: ("EnableNightmareHeadstone", ""),
    12105024: ("EnableOldHuntersHeadstone", ""),
    12105040: ("InitializeBathShopMessengers", ""),
    12101000: ("BathShopMessengerAppearance", "Change bath shop messenger appearances based on badges unlocked."),
    12101010: ("InitializeStoryProgressionFlags", "Enables flags in (5900, 5904) range based on story progression."),
    12105043: ("InitializeInsightShop", "Shop messenger awakens when player has 1+ insight."),
    12101020: ("OfferMeleeWeaponGift", ""),
    12101021: ("OfferGunGift", ""),
    12101022: ("OfferNotebookGift", ""),
    12101024: ("OfferBeckoningBellGift", ""),
    12101026: ("OfferOldHunterBellGift", ""),
    12101028: ("OfferEyeOfBloodDrunkHunterGift", ""),
    12105060: ("StumpMessengersRemoveHats", ""),
    12105062: ("StumpMessengersAppear", ""),
    12105064: ("OfferDLCMessengerHats", ""),
    12105070: ("ChangeStumpMessengerHat", "Stump messengers hide, flip display mask bits, and re-emerge."),
    12105210: ("MonitorWeaponBuffRemovalRequest", ""),
    12105310: ("AnimateChaliceAltar", ""),
    12107000: ("WarpAtHeadstone", "Activate a main headstone warp."),
    12107100: ("ActivateChaliceAltar", ""),
    12107200: ("WarpToChaliceDungeon", ""),
}


class Flags(Flag):
    InsightShopOpen = 12100320

    MeleeWeaponGiftReceived = 12101020
    GunGiftReceived = 12101021

    GehrmanDead = 12101800
    GehrmanRefusalCutsceneDone = 12101802
    MoonPresenceDead = 12101850
    MoonPresenceBattleCutsceneDone = 12101852

    GehrmanBattleFogEntered = 12104800
    GehrmanBattleStartedForSummon = 12104801
    GehrmanBattleStarted = 12104802
    GehrmanBattleWon = 12104809
    MoonPresenceBattleActive = 12104850

    YharnamHeadstoneAvailable = 12105030
    FrontierHeadstoneAvailable = 12105031
    UnseenHeadstoneAvailable = 12105032
    NightmareHeadstoneAvailable = 12105033
    OldHuntersHeadstoneAvailable = 12105034
    StumpMessengersActive = 12105063

    GehrmanOfferAccepted = 72100130
    GehrmanOfferRefused = 72100131


class Characters(Character):
    BathShopMessengers1 = 2100211
    BathShopMessengers2 = 2100212
    BathShopMessengers3 = 2100213
    InsightShopMessengers1 = 2100214
    MeleeWeaponGiftMessengers = 2100215
    GunGiftMessengers = 2100216
    StumpMessengers = 2100218
    InsightShopMessengers2 = 2100219
    StoragePrompt = 2100200
    UpgradePrompt = 2100201
    MemoryAltarPrompt = 2100203
    MeleeWeaponGift = 2100220  # looks like an overlay of the three starting weapons
    GunGift = 2100221  # looks like an overlay of the two starting guns
    BellGiftMessengers = 2100230
    OldHuntersMessengers = 2100231  # also give you the Eye of a Blood-Drunk Hunter
    NearStumpMessengers = 2100232
    PlainDoll = 2100700
    GehrmanAlly = 2100600
    GehrmanBoss = 2100800
    MoonPresence = 2100810
    YharnamMessengers = 2100950
    FrontierMessengers = 2100951
    UnseenMessengers = 2100952
    NightmareMessengers = 2100953
    MakeshiftAltar = 2100954  # first altar in row, for Short Ritual Root Chalice
    ChaliceAltar1 = 2100955
    ChaliceAltar2 = 2100956
    ChaliceAltar3 = 2100957
    ChaliceAltar4 = 2100958
    ChaliceAltar5 = 2100959
    ChaliceAltar6 = 2100960  # called "Final Ritual Altar" in-game


class Objects(Object):
    IronGateToField = 2101000
    WorkshopFrontDoorClosed = 2101010
    WorkshopFrontDoorOpen = 2101011
    WorkshopBackDoorClosed = 2101020
    WorkshopBackDoorOpen = 2101021
    WorkshopMiddleDoorClosed = 2101030
    WorkshopMiddleDoorOpen = 2101031
    WorkshopChest = 2101050
    LonelyHeadstone = 2101100  # near Yharnam headstone
    NormalMoon = 2101300
    BloodMoon = 2101301
    NormalMoonSky = 2101310
    BloodMoonSky = 2101311
    BossFog = 2101800


class VFX(VFXEvent):
    BossFog = 2103800


class Cutscenes(Cutscene):
    FirstArrival = 21000000
    YharnamSunriseEndingFemale = 21000010
    YharnamSunriseEndingMale = 21001010
    HonoringWishesEnding = 21000020
    ChildhoodsBeginningEndingFemale = 21000030
    GehrmanBossBattleStarts = 21000040
    MoonPresenceBattleStarts = 21000050
    ChildhoodsBeginningEndingMale = 21001030


class Music(MusicSound):
    GehrmanPhase1Music = 2103802
    GehrmanPhase2Music = 2103803
    MoonPresencePhase1Music = 2103812
    MoonPresencePhase2Music = 2103813
    NormalMusic = 2103900
    BloodMoonMusic = 2103901


class Regions(Region):  # not bothering to specify type
    BossFogRotateTarget = 2102800
    MoonPresenceBattlePlayerStart = 2102809


class BossNames(EventText):
    Gehrman = 804000


class Goods(GoodParam):
    AugurOfEbrietas = 2000
    ACallBeyond = 2010
    BeastRoar = 2020
    LeadElixir = 2030
    ChoirBell = 2050
    OldHunterBone = 2060
    TinyTonitrus = 2070
    ExecutionersGloves = 2080
    ShamanBoneBlade = 2090
    MessengersGift = 2110
    BloodstoneShard = 3000
    TwinBloodstoneShards = 3010
    BloodstoneChunk = 3020
    BloodRock = 3030
    OedonTombKey = 4000
    GoldPendant = 4001
    CainhurstSummons = 4003
    OrphanageKey = 4006
    # Orphanage2FKey = 4007  # cut
    # UniversityKey = 4008  # cut
    IronDoorKey = 4009
    UpperCathedralKey = 4010
    HunterChiefEmblem = 4011
    LectureTheatreKey = 4012
    LunariumKey = 4013

    WorkshopHazeExtractor = 4102
    BloodGemWorkshopTool = 4103
    RuneWorkshopTool = 4104
    ShortRitualRootChalice = 4105

    SawHunterBadge = 4110
    CrowHunterBadge = 4111
    PowderKegHunterBadge = 4112
    OldHunterBadge = 4113
    SwordHunterBadge = 4114
    RadiantSwordHunterBadge = 4115
    WheelHunterBadge = 4116
    CainhurstBadge = 4117
    SparkHunterBadge = 4118
    CosmicEyeWatcherBadge = 4119

    SmallHairOrnament = 4300

    YharnamMessengerHat = 4900
    WornMessengerTopHat = 4901
    MessengerHeadBandage = 4902
    WhiteMessengerRibbon = 4903
    RedMessengerRibbon = 4904
    MessengerTopHat = 4905
    BlackMessengerHat = 4906
    BloodyMessengerHeadBandage = 4907
    MessengerUrnDance = 4908


class ItemLots(ItemLotParam):
    DollGift = 14000
