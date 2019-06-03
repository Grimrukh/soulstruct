from soulstruct.emevd import game_types as dt


class COMMON_FLAGS(dt.Flag):
    GapingDragonDead = 2
    BellGargoylesDead = 3
    CrossbreedPriscillaDead = 4
    SifDead = 5
    PinwheelDead = 6
    NitoDead = 7
    # Flag 8 missing.
    QuelaagDead = 9
    BedOfChaosDead = 10
    IronGolemDead = 11
    # Flag 12 missing.
    FourKingsDead = 13
    SeathDead = 14
    GwynLordOfCinderDead = 15
    AsylumDemonDead = 16
    FairLadyDead = 140
    RiteOfKindlingObtained = 257
    WarpOptionPermitted = 706
    WarpOptionDisplayed = 710

    NewGameFlagsInitialized = 909

    VamosDead = 1342

    CiaranGivenSoul = 1862
    CiaranDead = 1864

    TaurusDemonDead = 11010901
    CapraDemonDead = 11010902

    MoonlightButterflyDead = 11200900

    DarkAnorLondo = 11510400

    InArchivesPrison = 11705170

    LordvesselFull = 11800211
    TutorialComplete = 11810000


class NPC_FLAG_RANGES:  # TODO
    Solaire = dt.FlagRange(1000, 1029)
    dt.FlagRange(1030, 1059)
    dt.FlagRange(1060, 1089)
    dt.FlagRange(1090, 1109)
    dt.FlagRange(1110, 1119)
    dt.FlagRange(1120, 1139)
    dt.FlagRange(1140, 1169)
    dt.FlagRange(1170, 1189)
    dt.FlagRange(1190, 1209)
    dt.FlagRange(1210, 1219)
    dt.FlagRange(1220, 1229)
    dt.FlagRange(1230, 1239)
    dt.FlagRange(1240, 1249)
    dt.FlagRange(1250, 1259)
    dt.FlagRange(1270, 1279)
    dt.FlagRange(1280, 1289)
    dt.FlagRange(1290, 1309)
    dt.FlagRange(1310, 1319)
    dt.FlagRange(1320, 1339)
    dt.FlagRange(1340, 1359)
    dt.FlagRange(1360, 1379)
    dt.FlagRange(1380, 1399)
    dt.FlagRange(1400, 1409)
    dt.FlagRange(1410, 1419)
    dt.FlagRange(1420, 1429)
    dt.FlagRange(1430, 1459)
    dt.FlagRange(1460, 1489)
    dt.FlagRange(1490, 1539)
    dt.FlagRange(1540, 1569)
    dt.FlagRange(1570, 1599)
    dt.FlagRange(1600, 1619)
    Patches = dt.FlagRange(1620, 1639)
    dt.FlagRange(1640, 1669)
    dt.FlagRange(1670, 1679)
    dt.FlagRange(1690, 1699)
    dt.FlagRange(1700, 1709)
    dt.FlagRange(1710, 1729)
    dt.FlagRange(1760, 1769)
    dt.FlagRange(1770, 1779)
    dt.FlagRange(1780, 1789)


class COMMON_TEXT(dt.Text):
    ArrivalInLordran = 10010600
    RiteOfKindlingTip = 10010610
    LordvesselWarpTip = 10010620


class COMMON_GOODS(dt.Good):
    GravelordNitoLordSoul = 2500
    BedOfChaosLordSoul = 2501
    FourKingsLordSoul = 2502
    # Note 2503 is missing, though strangely, it looks like 2504 is unused in the params...
    SeathLordSoul = 2504
    Lordvessel = 2510


class COMMON_ITEM_LOTS(dt.ItemLot):
    GapingDragonReward = 2500
    CapraDemonReward = 2510
    CrossbreedPriscillaReward = 2520
    MoonlightButterflyReward = 2530
    SifReward = 2540
    HumanityLot = 9000
    TwinHumanitiesLot = 9020
    HomewardBoneLot = 9030
