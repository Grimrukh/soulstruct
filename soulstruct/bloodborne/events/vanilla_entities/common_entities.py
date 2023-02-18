from soulstruct.bloodborne.game_types import *
from enum import IntEnum


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    3500: ("Event3500", "Event 3500"),
    3503: ("Event3503", "Event 3503"),
    6002: ("Event6002", "Event 6002"),
    5500: ("Event5500", "Event 5500"),
    6680: ("Event6680", "Event 6680"),
    6681: ("Event6681", "Event 6681"),
    6682: ("Event6682", "Event 6682"),
    6683: ("Event6683", "Event 6683"),
    6684: ("Event6684", "Event 6684"),
    6685: ("Event6685", "Event 6685"),
    6686: ("Event6686", "Event 6686"),
    6687: ("Event6687", "Event 6687"),
    6688: ("Event6688", "Event 6688"),
    6689: ("Event6689", "Event 6689"),
    6690: ("Event6690", "Event 6690"),
    6691: ("Event6691", "Event 6691"),
    6692: ("Event6692", "Event 6692"),
    6693: ("Event6693", "Event 6693"),
    6694: ("Event6694", "Event 6694"),
    6695: ("Event6695", "Event 6695"),
    6696: ("Event6696", "Event 6696"),
    6697: ("Event6697", "Event 6697"),
    6788: ("Event6788", "Event 6788"),
    6789: ("Event6789", "Event 6789"),
    6809: ("Event6809", "Event 6809"),
    6815: ("Event6815", "Event 6815"),
    6816: ("Event6816", "Event 6816"),
    7000: ("ToggleLantern", "Event 7000"),
    7100: ("LightLantern", "Event 7100"),
    7200: ("ReturnToHuntersDream", "Event 7200"),
    7300: ("ArriveAtLantern", "Event 7300"),
    7600: ("Event7600", "Event 7600"),
    9030: ("Event9030", "Event 9030"),
    9035: ("Event9035", "Event 9035"),
    9040: ("Event9040", "Event 9040"),
    9100: ("Event9100", "Event 9100"),
    9110: ("Event9110", "Event 9110"),
    9181: ("Event9181", "Event 9181"),
    9182: ("Event9182", "Event 9182"),
    9183: ("Event9183", "Event 9183"),
    9186: ("Event9186", "Event 9186"),
    9190: ("Event9190", "Event 9190"),
    9191: ("Event9191", "Event 9191"),
    9192: ("Event9192", "Event 9192"),
    9193: ("Event9193", "Event 9193"),
    9198: ("Event9198", "Event 9198"),
    9200: ("Event9200", "Event 9200"),
    9215: ("Event9215", "Event 9215"),
    9220: ("Event9220", "Event 9220"),
    9240: ("Event9240", "Event 9240"),
    9260: ("Event9260", "Event 9260"),
    9280: ("Event9280", "Event 9280"),
    9350: ("GainInsight", "Grants the player up to 9 insight by repeatedly applying SpEffect 4680."),
    9360: ("Event9360", "Event 9360"),
    9400: ("Event9400", "Event 9400"),
    9404: ("Event9404", "Event 9404"),
    9410: ("Event9410", "Event 9410"),
    9421: ("Event9421", "Event 9421"),
    9422: ("Event9422", "Event 9422"),
    9440: ("Event9440", "Event 9440"),
    9480: ("Event9480", "Event 9480"),
    9500: ("Event9500", "Event 9500"),
    9700: ("Event9700", "Event 9700"),
    9701: ("Event9701", "Event 9701"),
    9702: ("Event9702", "Event 9702"),
    9703: ("Event9703", "Event 9703"),
    9710: ("Event9710", "Event 9710"),
    9720: ("Event9720", "Event 9720"),
    9721: ("Event9721", "Event 9721"),
    9722: ("Event9722", "Event 9722"),
    9723: ("Event9723", "Event 9723"),
    9755: ("Event9755", "Event 9755"),
    9756: ("Event9756", "Event 9756"),
    9770: ("Event9770", "Event 9770"),
    9780: ("Event9780", "Event 9780"),
    9781: ("Event9781", "Event 9781"),
    9782: ("Event9782", "Event 9782"),
    9909: ("Event9909", "Event 9909"),
    9905: ("Event9905", "Event 9905"),
    9910: ("Event9910", "Event 9910"),
}


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
    BloodStarvedBeastDefeated = 22
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
