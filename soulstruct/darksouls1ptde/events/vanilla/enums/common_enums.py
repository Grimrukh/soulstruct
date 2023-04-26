from soulstruct.darksouls1ptde.game_types import *


class CommonFlags(Flag):
    GapingDragonDead = 2
    BellGargoylesDead = 3
    CrossbreedPriscillaDead = 4
    SifDead = 5
    PinwheelDead = 6
    NitoDead = 7
    # Flag 8 unused.
    QuelaagDead = 9
    BedOfChaosDead = 10
    IronGolemDead = 11
    OrnsteinSmoughDead = 12
    FourKingsDead = 13
    SeathDead = 14
    GwynLordOfCinderDead = 15
    AsylumDemonDead = 16

    FairLadyDead = 140

    RiteOfKindlingObtained = 257

    BlighttownDoorOpened = 590

    BonfireWarpingUnblocked = 706
    BonfireWarpOptionDisplayed = 710
    PreventGravelordInvasions = 735

    NewGameFlagsInitialized = 909

    VamosDead = 1342

    CiaranGivenSoul = 1862
    CiaranDead = 1864

    GravelordInvasionActive = 5000

    SolaireHumanityFlag = 8310
    LaurentiusHumanityFlag = 8390
    DomnhallHumanityFlag = 8430
    LautrecHumanityFlag = 8462
    KirkHumanityFlag = 8956

    TaurusDemonDead = 11010901
    CapraDemonDead = 11010902

    MoonlightButterflyDead = 11200900

    DarkAnorLondo = 11510400

    InArchivesPrison = 11705170

    LordvesselFull = 11800211

    TutorialComplete = 11810000


class CommonEventText(EventText):
    ArrivalInLordran = 10010600
    RiteOfKindlingTip = 10010610
    LordvesselWarpTip = 10010620


class CommonGoods(GoodParam):
    GravelordNitoLordSoul = 2500
    BedOfChaosLordSoul = 2501
    FourKingsLordSoul = 2502
    SeathLordSoul = 2503
    # Good 2504 ('Demon Flame') is missing, but is still used to trigger some unused Darkmoon Knightess dialogue.
    Lordvessel = 2510


class CommonItemLots(ItemLotParam):
    GapingDragonReward = 2500
    CapraDemonReward = 2510
    CrossbreedPriscillaReward = 2520
    MoonlightButterflyReward = 2530
    SifReward = 2540
    HumanityLot = 9000
    TwinHumanitiesLot = 9020
    HomewardBoneLot = 9030


class PlayerAnimations(PlayerAnimation):
    LightBonfire = 7114
    Crouching = 7610
    GetUp = 7801
    KneelingDownOneLeg = 7895
    StayKneelingDownOneLeg = 7896
    GettingUpFromKneelingDownOneLeg = 7897


class CharacterStoryFlagRanges:
    Solaire = FlagRange(1000, 1029)
    DarkmoonKnightess = FlagRange(1030, 1059)
    Oscar = FlagRange(1060, 1089)
    Logan = FlagRange(1090, 1109)
    Griggs = FlagRange(1110, 1119)
    Dusk = FlagRange(1120, 1139)
    Anastacia = FlagRange(1140, 1169)
    Rhea = FlagRange(1170, 1189)
    Petrus = FlagRange(1190, 1209)
    Vince = FlagRange(1210, 1219)
    Nico = FlagRange(1220, 1229)
    Gwynevere = FlagRange(1230, 1239)
    Gwyndolin = FlagRange(1240, 1249)
    Laurentius = FlagRange(1250, 1259)
    FairLady = FlagRange(1270, 1279)
    Eingyi = FlagRange(1280, 1289)
    Quelana = FlagRange(1290, 1309)
    Ingward = FlagRange(1310, 1319)
    Andre = FlagRange(1320, 1339)
    Vamos = FlagRange(1340, 1359)
    GiantBlacksmith = FlagRange(1360, 1379)
    Rickert = FlagRange(1380, 1399)
    MaleUndeadMerchant = FlagRange(1400, 1409)
    FemaleUndeadMerchant = FlagRange(1410, 1419)
    CrestfallenMerchant = FlagRange(1420, 1429)
    Domnhall = FlagRange(1430, 1459)
    CrestfallenWarrior = FlagRange(1460, 1489)
    Siegmeyer = FlagRange(1490, 1539)
    Sieglinde = FlagRange(1540, 1569)
    Lautrec = FlagRange(1570, 1599)
    Shiva = FlagRange(1600, 1619)
    Patches = FlagRange(1620, 1639)
    Frampt = FlagRange(1640, 1669)
    Kaathe = FlagRange(1670, 1679)
    Priscilla = FlagRange(1690, 1699)
    Oswald = FlagRange(1700, 1709)
    Alvina = FlagRange(1710, 1729)
    ShivaBodyguard = FlagRange(1760, 1769)
    # FlagRange(1770, 1779)  # Appears to be unused
    # FlagRange(1780, 1789)  # Appears to be unused
    HawkeyeGough = FlagRange(1820, 1839)
    MarvellousChester = FlagRange(1840, 1859)
    Ciaran = FlagRange(1860, 1869)
    Elizabeth = FlagRange(1870, 1889)


class CharacterStoryFlags:
    class MarvellousChester(Flag):
        Friendly = 1840
        Hostile = 1841
        Dead = 1842

    class Ciaran(Flag):
        MissingBeforeArtoriasDefeated = 1860
        AtGravestone = 1861
        GivenSoulOfArtorias = 1862
        Hostile = 1863
        Dead = 1864
        NotGivenSoulOfArtorias = 1865

    class Elizabeth(Flag):
        Alive = 1870
        Dead = 1872
