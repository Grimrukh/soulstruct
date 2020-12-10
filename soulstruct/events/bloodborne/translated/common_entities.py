from soulstruct.game_types import *
from enum import IntEnum


class CommonFlags(Flag):
    YharnamSunriseEnding = 21
    HonoringWishesEnding = 22
    ChildhoodsBeginningEnding = 23

    MicolashDead_Short = 2600
    WetNurseDead_Short = 2601

    RequestMessengerHat1 = 6011
    RequestMessengerHat2 = 6012
    RequestMessengerHat3 = 6013
    RequestMessengerHat4 = 6014
    RequestMessengerHat5 = 6015
    RequestMessengerHat6 = 6016
    RequestMessengerHat7 = 6017
    RequestMessengerHat8 = 6018
    RequestMessengerHat9 = 6019
    RequestMessengerHat10 = 6020
    RequestMessengerHat11 = 6021
    RequestMessengerHat12 = 6022
    RequestMessengerHat13 = 6023
    RequestMessengerHat14 = 6024
    RequestMessengerHat15 = 6025
    PlayerHasMessengerHat1 = 6071
    PlayerHasMessengerHat2 = 6072
    PlayerHasMessengerHat3 = 6073
    PlayerHasMessengerHat4 = 6074
    PlayerHasMessengerHat5 = 6075
    PlayerHasMessengerHat6 = 6076
    PlayerHasMessengerHat7 = 6077
    PlayerHasMessengerHat8 = 6078
    PlayerHasMessengerHat9 = 6079

    MakeshiftAltarActivated = 9020
    ChaliceAltar1Activated = 9021
    ChaliceAltar2Activated = 9022
    ChaliceAltar3Activated = 9023
    ChaliceAltar4Activated = 9024
    ChaliceAltar5Activated = 9025
    ChaliceAltar6Activated = 9026
    CutsceneActive = 9180
    InsightGained_BloodStarvedBeastBattle = 9339
    InsightGained_DarkbeastPaarlBattle = 9340
    InsightGained_GehrmanBattle = 9343
    HuntersDreamVisited = 9401
    CentralYharnamVisited = 9403  # TODO: probably. Could be a more specific region.
    WorkshopOnFire = 9462  # enabled when Mergo's Wet Nurse is defeated

    EveningPhase = 9800
    NightPhase = 9801
    BloodMoonPhase = 9802  # can't actually find where this is enabled

    ThreeCordsConsumed = 9900

    GehrmanDead = 12101800
    MoonPresenceDead = 12101850
    WetNurseDead = 12601800
    OneRebornDead = 12801800

    RequestWeaponBuffRemoval = 70000100  # monitored in Hunter's Dream


class CommonEventTexts(EventText):
    Locked = 10010171  # or "closed"


class Effects(SpecialEffectParam):
    FirePaper = 2200
    EmptyPhantasmShell = 2210
    BoltPaper = 2220
    FullTransparency = 5686
    SemiTransparency = 5687
    NoTransparency = 5688  # clears the other transparency effects
    SummonBellsDisabled = 9120
    InvaderBellsDisabled = 9121


class Achievements(IntEnum):
    YharnamSunriseEnding = 1
    HonoringWishesEnding = 2
    ChildhoodsBeginningEnding = 3
    DiscoveredAbandonedOldWorkshop = 12
    ShadowsOfYharnamDefeated = 16
    MicolashDefeated = 19
    ClericBeastDefeated = 21
    WitchesOfHemwickDefeated = 23
    LudwigDefeated = 36
    LadyMariaDefeated = 37
    LaurenceDefeated = 39


class PlayerAnimations(PlayerAnimation):
    WarpAtHeadstone = 101164


class WarpPoints(SpawnPointEvent):
    """Note that warp point IDs are NOT necessary ordered as you would expect."""
    AbandonedOldWorkshop = 2112950

    HemwickCharnelLane = 2202950
    WitchsAbode = 2202951  # Witches of Hemwick

    OldYharnam = 2302950
    ChurchOfTheGoodChalice = 2302951  # Blood-starved Beast
    GraveyardOfTheDarkbeast = 2302952  # Darkbeast Paarl

    CathedralWard = 2402950
    GrandCathedral = 2402951  # Vicar Amelia

    FirstFloorSickroom = 2412950
    CentralYharnam = 2412951
    GreatBridge = 2412952  # Cleric Beast
    TombOfOedon = 2412953  # Father Gascoigne

    UpperCathedralWard = 2422950
    AltarOfDespair = 2422951  # Ebrietas
    LumenflowerGardens = 2422952  # Celestial Emissary

    ForsakenCastleCainhurt = 2502950
    VilebloodQueensChamber = 2502951
    LogariusSeat = 2502952  # Martyr Logarius

    NightmareOfMensis = 2602950
    WetNursesLunarium = 2602951  # Mergo's Wet Nurse
    MergosLoftMiddle = 2602952  # Micolash, Host of the Nightmare
    MergosLoftBase = 2602953

    ForbiddenWoods = 2702950
    ForbiddenGrave = 2702951  # Shadows of Yharnam

    YahargulUnseenVillage = 2802950
    AdventPlaza = 2802951  # The One Reborn
    HypogeanGaol = 2802952
    YahargulChapel = 2802953

    Byrgenwerth = 3202950
    LectureBuilding = 3202951
    MoonsideLake = 3202952  # Rom, the Vacuous Spider
    LectureBuildingSecondFloor = 3202953

    NightmareFrontier = 3302950
    AmygdalasChamber = 3302951  # Amygdala

    OldHuntersStart = 3402950
    NightmareChurch = 3402951
    UndergroundCorpsePile = 3402952  # Ludwig
    NightmareGrandCathedral = 3402953  # Laurence

    ResearchHall = 3502950
    LumenwoodGarden = 3502951  # Living Failures
    AstralClocktower = 3502952  # Maria

    FishingHamlet = 3602950
    LighthouseHut = 3602951
    Coast = 3602952  # Orphan of Kos
