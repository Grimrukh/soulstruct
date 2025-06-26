from __future__ import annotations

__all__ = ["MapStudioDirectory"]

import typing as tp
from dataclasses import field

from soulstruct.base.game_file_directory import map_property
from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory

from .constants import *
from .msb import MSB


class MapStudioDirectory(_BaseMapStudioDirectory):
    """Elden Ring `MapStudio` directory.
    
    WARNING: These MSBs and their entries are huge, and some MSBs may each take multiple seconds to load from binary.
    It's recommended you convert to JSON (even just for vanilla source maps) for large projects.

    (On my decently powerful CPU, it took 3 minutes to load all maps from binary, and only 1 minute from JSON.)

    TODO: Copied these maps from EMEVD, but some are missing ('empty tiles').
    """
    FILE_CLASS: tp.ClassVar = MSB
    ALL_MAPS: tp.ClassVar = tuple(m for m in ALL_MAPS if m.msb_file_stem)
    GET_MAP: tp.ClassVar = staticmethod(get_map)

    # Type hint override.
    files: dict[str, MSB] = field(default_factory=dict)

    # TODO: These don't have EMEVD (or are test/demo maps). Could still support them here, though.
    QUIETLY_IGNORED_FILE_STEMS: tp.ClassVar = {
        "m10_00_00_99",
        "m10_01_00_99",
        "m11_00_00_99",
        "m11_05_00_99",
        "m11_10_00_99",
        "m11_70_00_00",
        "m11_71_00_00",
        "m11_71_00_99",
        "m11_72_00_00",
        "m12_01_00_99",
        "m12_02_00_99",
        "m12_03_00_99",
        "m13_00_00_99",
        "m14_00_00_99",
        "m15_00_00_99",
        "m16_00_00_99",
        "m19_00_00_99",
        "m19_70_00_00",
        "m34_10_00_99",
        "m34_11_00_99",
        "m34_12_00_99",
        "m34_13_00_99",
        "m34_14_00_99",
        "m34_15_00_99",
        "m39_20_00_99",
        "m45_00_00_00",
        "m45_00_00_99",
        "m45_01_00_00",
        "m45_01_00_99",
        "m45_02_00_00",
        "m45_02_00_99",
        "m60_00_00_99",
        "m60_09_14_02",
        "m60_10_10_12",
        "m60_10_11_02",
        "m60_10_14_02",
        "m60_10_15_02",
        "m60_11_10_12",
        "m60_11_11_02",
        "m60_11_15_02",
        "m60_12_11_02",
        "m60_12_15_02",
        "m60_12_16_02",
        "m60_13_11_02",
        "m60_13_12_02",
        "m60_13_15_02",
        "m60_14_12_02",
        "m60_14_13_02",
        "m60_14_14_02",
        "m60_14_15_02",
        "m60_16_24_01",
        "m60_19_18_01",
        "m60_19_28_01",
        "m60_20_21_01",
        "m60_20_22_01",
        "m60_20_23_01",
        "m60_20_24_01",
        "m60_20_28_01",
        "m60_20_29_01",
        "m60_20_30_01",
        "m60_21_20_11",
        "m60_21_21_01",
        "m60_21_22_01",
        "m60_21_23_01",
        "m60_21_24_01",
        "m60_21_28_01",
        "m60_21_29_01",
        "m60_21_30_01",
        "m60_21_31_01",
        "m60_22_19_11",
        "m60_22_21_01",
        "m60_22_22_01",
        "m60_22_23_01",
        "m60_22_24_01",
        "m60_22_27_01",
        "m60_22_27_11",
        "m60_22_28_01",
        "m60_22_29_01",
        "m60_22_30_01",
        "m60_22_31_01",
        "m60_23_17_01",
        "m60_23_18_11",
        "m60_23_19_11",
        "m60_23_21_11",
        "m60_23_22_01",
        "m60_23_23_01",
        "m60_23_24_01",
        "m60_23_26_01",
        "m60_23_26_11",
        "m60_23_27_11",
        "m60_23_30_01",
        "m60_23_31_01",
        "m60_24_21_01",
        "m60_24_22_01",
        "m60_24_23_01",
        "m60_24_24_01",
        "m60_24_30_01",
        "m60_24_31_01",
        "m60_24_32_01",
        "m60_25_22_01",
        "m60_25_23_01",
        "m60_25_24_01",
        "m60_25_25_01",
        "m60_25_30_01",
        "m60_25_31_01",
        "m60_26_22_01",
        "m60_26_23_01",
        "m60_26_24_01",
        "m60_26_25_01",
        "m60_26_30_01",
        "m60_27_24_01",
        "m60_27_25_01",
        "m60_27_29_01",
        "m60_27_30_01",
        "m60_28_24_01",
        "m60_28_25_01",
        "m60_28_26_01",
        "m60_28_27_01",
        "m60_28_28_01",
        "m60_28_29_01",
        "m60_28_30_01",
        "m60_32_41_00",
        "m60_32_42_00",
        "m60_32_43_00",
        "m60_32_44_00",
        "m60_32_45_00",
        "m60_32_46_00",
        "m60_32_47_00",
        "m60_32_48_00",
        "m60_33_48_00",
        "m60_34_40_00",
        "m60_34_52_00",
        "m60_34_53_00",
        "m60_34_54_00",
        "m60_34_55_00",
        "m60_35_40_00",
        "m60_35_55_00",
        "m60_36_40_00",
        "m60_36_55_00",
        "m60_37_40_00",
        "m60_38_38_00",
        "m60_38_55_00",
        "m60_39_36_00",
        "m60_39_37_00",
        "m60_39_38_00",
        "m60_39_47_00",
        "m60_39_55_00",
        "m60_39_56_00",
        "m60_40_32_00",
        "m60_40_34_00",
        "m60_40_35_00",
        "m60_40_36_00",
        "m60_40_37_00",
        "m60_40_41_00",
        "m60_40_42_00",
        "m60_40_43_00",
        "m60_40_44_00",
        "m60_40_45_00",
        "m60_40_46_00",
        "m60_40_47_00",
        "m60_40_48_00",
        "m60_40_49_00",
        "m60_40_56_00",
        "m60_41_40_00",
        "m60_41_41_00",
        "m60_41_42_00",
        "m60_41_43_00",
        "m60_41_44_00",
        "m60_41_45_00",
        "m60_41_46_00",
        "m60_41_47_00",
        "m60_41_48_00",
        "m60_41_49_00",
        "m60_41_56_00",
        "m60_41_57_00",
        "m60_41_58_00",
        "m60_41_59_00",
        "m60_41_60_00",
        "m60_41_61_00",
        "m60_42_30_00",
        "m60_42_31_00",
        "m60_42_41_00",
        "m60_42_42_00",
        "m60_42_43_00",
        "m60_42_44_00",
        "m60_42_45_00",
        "m60_42_46_00",
        "m60_42_47_00",
        "m60_42_48_00",
        "m60_42_49_00",
        "m60_42_56_00",
        "m60_42_57_00",
        "m60_42_58_00",
        "m60_42_59_00",
        "m60_42_60_00",
        "m60_42_61_00",
        "m60_42_62_00",
        "m60_43_41_00",
        "m60_43_42_00",
        "m60_43_43_00",
        "m60_43_44_00",
        "m60_43_45_00",
        "m60_43_46_00",
        "m60_43_47_00",
        "m60_43_48_00",
        "m60_43_49_00",
        "m60_43_55_00",
        "m60_43_56_00",
        "m60_43_57_00",
        "m60_43_58_00",
        "m60_43_59_00",
        "m60_43_60_00",
        "m60_43_61_00",
        "m60_43_62_00",
        "m60_44_30_00",
        "m60_44_36_10",
        "m60_44_37_10",
        "m60_44_38_10",
        "m60_44_39_10",
        "m60_44_40_00",
        "m60_44_41_00",
        "m60_44_42_00",
        "m60_44_43_00",
        "m60_44_44_00",
        "m60_44_45_00",
        "m60_44_46_00",
        "m60_44_47_00",
        "m60_44_48_00",
        "m60_44_49_00",
        "m60_44_50_00",
        "m60_44_51_00",
        "m60_44_52_10",
        "m60_44_53_10",
        "m60_44_54_00",
        "m60_44_54_10",
        "m60_44_55_00",
        "m60_44_55_10",
        "m60_44_56_00",
        "m60_44_57_00",
        "m60_44_58_00",
        "m60_44_59_00",
        "m60_44_60_00",
        "m60_44_61_00",
        "m60_44_62_00",
        "m60_45_31_00",
        "m60_45_37_10",
        "m60_45_38_10",
        "m60_45_39_10",
        "m60_45_41_00",
        "m60_45_42_00",
        "m60_45_43_00",
        "m60_45_44_00",
        "m60_45_45_00",
        "m60_45_46_00",
        "m60_45_47_00",
        "m60_45_48_00",
        "m60_45_49_00",
        "m60_45_50_00",
        "m60_45_53_10",
        "m60_45_54_00",
        "m60_45_54_10",
        "m60_45_55_00",
        "m60_45_55_10",
        "m60_45_56_00",
        "m60_45_57_00",
        "m60_45_58_00",
        "m60_45_59_00",
        "m60_45_60_00",
        "m60_45_61_00",
        "m60_45_62_00",
        "m60_45_63_00",
        "m60_46_34_00",
        "m60_46_35_00",
        "m60_46_36_10",
        "m60_46_37_10",
        "m60_46_38_10",
        "m60_46_39_10",
        "m60_46_41_00",
        "m60_46_42_00",
        "m60_46_43_00",
        "m60_46_44_00",
        "m60_46_45_00",
        "m60_46_46_00",
        "m60_46_47_00",
        "m60_46_48_00",
        "m60_46_49_00",
        "m60_46_50_00",
        "m60_46_51_00",
        "m60_46_52_00",
        "m60_46_52_10",
        "m60_46_53_00",
        "m60_46_53_10",
        "m60_46_54_00",
        "m60_46_54_10",
        "m60_46_55_10",
        "m60_46_56_00",
        "m60_46_58_00",
        "m60_46_59_00",
        "m60_46_60_00",
        "m60_46_61_00",
        "m60_46_62_00",
        "m60_46_63_00",
        "m60_47_36_00",
        "m60_47_36_10",
        "m60_47_37_10",
        "m60_47_38_10",
        "m60_47_39_10",
        "m60_47_43_00",
        "m60_47_44_00",
        "m60_47_45_00",
        "m60_47_46_00",
        "m60_47_47_00",
        "m60_47_48_00",
        "m60_47_49_00",
        "m60_47_50_00",
        "m60_47_52_00",
        "m60_47_52_10",
        "m60_47_53_00",
        "m60_47_53_10",
        "m60_47_54_00",
        "m60_47_54_10",
        "m60_47_55_10",
        "m60_47_59_00",
        "m60_47_60_00",
        "m60_47_61_00",
        "m60_47_62_00",
        "m60_47_63_00",
        "m60_48_42_00",
        "m60_48_43_00",
        "m60_48_44_00",
        "m60_48_45_00",
        "m60_48_46_00",
        "m60_48_47_00",
        "m60_48_48_00",
        "m60_48_49_00",
        "m60_48_50_00",
        "m60_48_52_00",
        "m60_48_53_00",
        "m60_48_59_00",
        "m60_48_60_00",
        "m60_48_61_00",
        "m60_48_62_00",
        "m60_48_63_00",
        "m60_48_64_00",
        "m60_49_42_00",
        "m60_49_43_00",
        "m60_49_44_00",
        "m60_49_45_00",
        "m60_49_46_00",
        "m60_49_47_00",
        "m60_49_48_00",
        "m60_49_49_00",
        "m60_49_50_00",
        "m60_49_51_00",
        "m60_49_58_00",
        "m60_49_59_00",
        "m60_49_60_00",
        "m60_49_61_00",
        "m60_49_62_00",
        "m60_49_63_00",
        "m60_50_42_00",
        "m60_50_43_00",
        "m60_50_44_00",
        "m60_50_45_00",
        "m60_50_46_00",
        "m60_50_47_00",
        "m60_50_48_00",
        "m60_50_49_00",
        "m60_50_50_00",
        "m60_50_51_00",
        "m60_50_52_00",
        "m60_50_58_00",
        "m60_50_59_00",
        "m60_50_60_00",
        "m60_50_61_00",
        "m60_50_62_00",
        "m60_51_44_00",
        "m60_51_45_00",
        "m60_51_46_00",
        "m60_51_47_00",
        "m60_51_48_00",
        "m60_51_49_00",
        "m60_51_50_00",
        "m60_51_51_00",
        "m60_51_59_00",
        "m60_51_60_00",
        "m60_51_61_00",
        "m60_52_36_00",
        "m60_52_44_00",
        "m60_52_45_00",
        "m60_52_46_00",
        "m60_52_47_00",
        "m60_52_48_00",
        "m60_52_49_00",
        "m60_52_50_00",
        "m60_52_51_00",
        "m60_52_59_00",
        "m60_52_60_00",
        "m60_52_61_00",
        "m60_53_36_00",
        "m60_53_37_00",
        "m60_53_40_00",
        "m60_53_41_00",
        "m60_53_42_00",
        "m60_53_43_00",
        "m60_53_44_00",
        "m60_53_45_00",
        "m60_53_46_00",
        "m60_53_47_00",
        "m60_53_48_00",
        "m60_53_49_00",
        "m60_53_50_00",
        "m60_53_51_00",
        "m60_53_59_00",
        "m60_53_60_00",
        "m60_53_61_00",
        "m60_54_48_00",
        "m60_54_49_00",
        "m60_54_50_00",
        "m60_54_51_00",
        "m60_54_52_00",
        "m60_54_54_00",
        "m60_54_58_00",
        "m60_54_59_00",
        "m60_54_60_00",
        "m60_54_61_00",
        "m60_55_48_00",
        "m60_55_49_00",
        "m60_55_50_00",
        "m60_55_51_00",
        "m60_55_52_00",
        "m60_55_53_00",
        "m60_55_54_00",
        "m60_55_55_00",
        "m60_55_56_00",
        "m60_55_57_00",
        "m60_55_58_00",
        "m60_55_59_00",
        "m60_55_60_00",
        "m60_55_61_00",
        "m60_56_49_00",
        "m60_56_50_00",
        "m60_56_51_00",
        "m60_56_52_00",
        "m60_56_53_00",
        "m60_56_54_00",
        "m60_56_55_00",
        "m60_56_56_00",
        "m60_56_57_00",
        "m60_56_58_00",
        "m60_56_59_00",
        "m60_56_60_00",
        "m60_56_61_00",
        "m60_57_50_00",
        "m60_57_51_00",
        "m60_57_52_00",
        "m60_57_53_00",
        "m60_57_54_00",
        "m60_57_55_00",
        "m60_57_56_00",
        "m60_57_57_00",
        "m60_57_58_00",
        "m60_57_59_00",
        "m60_57_60_00",
        "m60_57_61_00",
    }

    StormveilCastle = map_property(STORMVEIL_CASTLE)  # type: MSB
    ChapelOfAnticipation = map_property(CHAPEL_OF_ANTICIPATION)  # type: MSB
    LeyndellRoyalCapital = map_property(LEYNDELL_ROYAL_CAPITAL)  # type: MSB
    LeyndellAshenCapital = map_property(LEYNDELL_ASHEN_CAPITAL)  # type: MSB
    RoundtableHold = map_property(ROUNDTABLE_HOLD)  # type: MSB
    AinselRiver = map_property(AINSEL_RIVER)  # type: MSB
    SiofraRiver = map_property(SIOFRA_RIVER)  # type: MSB
    DeeprootDepths = map_property(DEEPROOT_DEPTHS)  # type: MSB
    AstelArena = map_property(ASTEL_ARENA)  # type: MSB
    MohgwynPalace = map_property(MOHGWYN_PALACE)  # type: MSB
    SiofraRiverStart = map_property(SIOFRA_RIVER_START)  # type: MSB
    AncestorSpiritArena = map_property(ANCESTOR_SPIRIT_ARENA)  # type: MSB
    RegalAncestorArena = map_property(REGAL_ANCESTOR_ARENA)  # type: MSB
    CrumblingFarumAzula = map_property(CRUMBLING_FARUM_AZULA)  # type: MSB
    RayaLucaria = map_property(RAYA_LUCARIA)  # type: MSB
    Haligtree = map_property(HALIGTREE)  # type: MSB
    VolcanoManor = map_property(VOLCANO_MANOR)  # type: MSB
    StrandedGraveyard = map_property(STRANDED_GRAVEYARD)  # type: MSB
    StonePlatform = map_property(STONE_PLATFORM)  # type: MSB
    ShunningGrounds = map_property(SHUNNING_GROUNDS)  # type: MSB
    RuinStrewnPrecipice = map_property(RUIN_STREWN_PRECIPICE)  # type: MSB

    TombswardCatacombs = map_property(TOMBSWARD_CATACOMBS)  # type: MSB
    ImpalersCatacombs = map_property(IMPALERS_CATACOMBS)  # type: MSB
    StormfootCatacombs = map_property(STORMFOOT_CATACOMBS)  # type: MSB
    RoadsEndCatacombs = map_property(ROADS_END_CATACOMBS)  # type: MSB
    MurkwaterCatacombs = map_property(MURKWATER_CATACOMBS)  # type: MSB
    BlackKnifeCatacombs = map_property(BLACK_KNIFE_CATACOMBS)  # type: MSB
    CliffbottomCatacombs = map_property(CLIFFBOTTOM_CATACOMBS)  # type: MSB
    WyndhamCatacombs = map_property(WYNDHAM_CATACOMBS)  # type: MSB
    SaintedHerosGrave = map_property(SAINTED_HEROS_GRAVE)  # type: MSB
    GelmirHerosGrave = map_property(GELMIR_HEROS_GRAVE)  # type: MSB
    AurizaHerosGrave = map_property(AURIZA_HEROS_GRAVE)  # type: MSB
    DeathtouchedCatacombs = map_property(DEATHTOUCHED_CATACOMBS)  # type: MSB
    UnsightlyCatacombs = map_property(UNSIGHTLY_CATACOMBS)  # type: MSB
    AurizaSideTomb = map_property(AURIZA_SIDE_TOMB)  # type: MSB
    MinorErdtreeCatacombs = map_property(MINOR_ERDTREE_CATACOMBS)  # type: MSB
    CaelidCatacombs = map_property(CAELID_CATACOMBS)  # type: MSB
    WarDeadCatacombs = map_property(WAR_DEAD_CATACOMBS)  # type: MSB
    GiantConqueringHerosGrave = map_property(GIANT_CONQUERING_HEROS_GRAVE)  # type: MSB
    GiantsMountaintopCatacombs = map_property(GIANTS_MOUNTAINTOP_CATACOMBS)  # type: MSB
    ConsecratedSnowfieldCatacombs = map_property(CONSECRATED_SNOWFIELD_CATACOMBS)  # type: MSB
    HiddenPathToTheHaligtree = map_property(HIDDEN_PATH_TO_THE_HALIGTREE)  # type: MSB

    MurkwaterCave = map_property(MURKWATER_CAVE)  # type: MSB
    EarthboreCave = map_property(EARTHBORE_CAVE)  # type: MSB
    TombswardCave = map_property(TOMBSWARD_CAVE)  # type: MSB
    GrovesideCave = map_property(GROVESIDE_CAVE)  # type: MSB
    StillwaterCave = map_property(STILLWATER_CAVE)  # type: MSB
    LakesideCrystalCave = map_property(LAKESIDE_CRYSTAL_CAVE)  # type: MSB
    AcademyCrystalCave = map_property(ACADEMY_CRYSTAL_CAVE)  # type: MSB
    SeethewaterCave = map_property(SEETHEWATER_CAVE)  # type: MSB
    VolcanoCave = map_property(VOLCANO_CAVE)  # type: MSB
    DragonbarrowCave = map_property(DRAGONBARROW_CAVE)  # type: MSB
    SelliaHideaway = map_property(SELLIA_HIDEAWAY)  # type: MSB
    CaveOfTheForlorn = map_property(CAVE_OF_THE_FORLORN)  # type: MSB
    CoastalCave = map_property(COASTAL_CAVE)  # type: MSB
    HighroadCave = map_property(HIGHROAD_CAVE)  # type: MSB
    PerfumersGrotto = map_property(PERFUMERS_GROTTO)  # type: MSB
    SagesCave = map_property(SAGES_CAVE)  # type: MSB
    AbandonedCave = map_property(ABANDONED_CAVE)  # type: MSB
    GaolCave = map_property(GAOL_CAVE)  # type: MSB
    SpiritcallerCave = map_property(SPIRITCALLER_CAVE)  # type: MSB

    MorneTunnel = map_property(MORNE_TUNNEL)  # type: MSB
    LimgraveTunnels = map_property(LIMGRAVE_TUNNELS)  # type: MSB
    RayaLucariaCrystalTunnel = map_property(RAYA_LUCARIA_CRYSTAL_TUNNEL)  # type: MSB
    OldAltusTunnel = map_property(OLD_ALTUS_TUNNEL)  # type: MSB
    AltusTunnel = map_property(ALTUS_TUNNEL)  # type: MSB
    GaelTunnel = map_property(GAEL_TUNNEL)  # type: MSB
    SelliaCrystalTunnel = map_property(SELLIA_CRYSTAL_TUNNEL)  # type: MSB
    YeloughAnixTunnel = map_property(YELOUGH_ANIX_TUNNEL)  # type: MSB

    DivineTowerOfLimgrave = map_property(DIVINE_TOWER_OF_LIMGRAVE)  # type: MSB
    DivineTowerOfLiurnia = map_property(DIVINE_TOWER_OF_LIURNIA)  # type: MSB
    DivineTowerOfWestAltus = map_property(DIVINE_TOWER_OF_WEST_ALTUS)  # type: MSB
    DivineTowerOfCaelid = map_property(DIVINE_TOWER_OF_CAELID)  # type: MSB
    DivineTowerOfEastAltus = map_property(DIVINE_TOWER_OF_EAST_ALTUS)  # type: MSB
    IsolatedDivineTower = map_property(ISOLATED_DIVINE_TOWER)  # type: MSB

    SouthwestLiurnia = map_property(SOUTHWEST_LIURNIA)  # type: MSB
    SouthwestLiurnia_SW = map_property(SOUTHWEST_LIURNIA_SW)  # type: MSB
    SouthwestLiurnia_SW_SE = map_property(SOUTHWEST_LIURNIA_SW_SE)  # type: MSB
    SouthwestLiurnia_SW_NE = map_property(SOUTHWEST_LIURNIA_SW_NE)  # type: MSB
    SouthwestLiurnia_NW = map_property(SOUTHWEST_LIURNIA_NW)  # type: MSB
    SouthwestLiurnia_NW_SE = map_property(SOUTHWEST_LIURNIA_NW_SE)  # type: MSB
    SouthwestLiurnia_NW_NE = map_property(SOUTHWEST_LIURNIA_NW_NE)  # type: MSB
    SouthwestLiurnia_SE = map_property(SOUTHWEST_LIURNIA_SE)  # type: MSB
    SouthwestLiurnia_SE_NW = map_property(SOUTHWEST_LIURNIA_SE_NW)  # type: MSB
    SouthwestLiurnia_SE_NE = map_property(SOUTHWEST_LIURNIA_SE_NE)  # type: MSB
    SouthwestLiurnia_NE = map_property(SOUTHWEST_LIURNIA_NE)  # type: MSB
    SouthwestLiurnia_NE_SW = map_property(SOUTHWEST_LIURNIA_NE_SW)  # type: MSB
    SouthwestLiurnia_NE_NW = map_property(SOUTHWEST_LIURNIA_NE_NW)  # type: MSB
    SouthwestLiurnia_NE_SE = map_property(SOUTHWEST_LIURNIA_NE_SE)  # type: MSB
    SouthwestLiurnia_NE_NE = map_property(SOUTHWEST_LIURNIA_NE_NE)  # type: MSB
    WestLiurnia = map_property(WEST_LIURNIA)  # type: MSB
    WestLiurnia_SW = map_property(WEST_LIURNIA_SW)  # type: MSB
    WestLiurnia_SW_SE = map_property(WEST_LIURNIA_SW_SE)  # type: MSB
    WestLiurnia_SW_NE = map_property(WEST_LIURNIA_SW_NE)  # type: MSB
    WestLiurnia_NW = map_property(WEST_LIURNIA_NW)  # type: MSB
    WestLiurnia_NW_SE = map_property(WEST_LIURNIA_NW_SE)  # type: MSB
    WestLiurnia_NW_NE = map_property(WEST_LIURNIA_NW_NE)  # type: MSB
    WestLiurnia_SE = map_property(WEST_LIURNIA_SE)  # type: MSB
    WestLiurnia_SE_SW = map_property(WEST_LIURNIA_SE_SW)  # type: MSB
    WestLiurnia_SE_NW = map_property(WEST_LIURNIA_SE_NW)  # type: MSB
    WestLiurnia_SE_SE = map_property(WEST_LIURNIA_SE_SE)  # type: MSB
    WestLiurnia_SE_NE = map_property(WEST_LIURNIA_SE_NE)  # type: MSB
    WestLiurnia_NE = map_property(WEST_LIURNIA_NE)  # type: MSB
    WestLiurnia_NE_SW = map_property(WEST_LIURNIA_NE_SW)  # type: MSB
    WestLiurnia_NE_NW = map_property(WEST_LIURNIA_NE_NW)  # type: MSB
    WestLiurnia_NE_SE = map_property(WEST_LIURNIA_NE_SE)  # type: MSB
    WestLiurnia_NE_NE = map_property(WEST_LIURNIA_NE_NE)  # type: MSB
    NorthwestLiurnia = map_property(NORTHWEST_LIURNIA)  # type: MSB
    NorthwestLiurnia_SE = map_property(NORTHWEST_LIURNIA_SE)  # type: MSB
    NorthwestLiurnia_SE_SW = map_property(NORTHWEST_LIURNIA_SE_SW)  # type: MSB
    NorthwestLiurnia_SE_NW = map_property(NORTHWEST_LIURNIA_SE_NW)  # type: MSB
    NorthwestLiurnia_SE_SE = map_property(NORTHWEST_LIURNIA_SE_SE)  # type: MSB
    NorthwestLiurnia_SE_NE = map_property(NORTHWEST_LIURNIA_SE_NE)  # type: MSB
    NorthwestLiurnia_NE = map_property(NORTHWEST_LIURNIA_NE)  # type: MSB
    NorthwestLiurnia_NE_SW = map_property(NORTHWEST_LIURNIA_NE_SW)  # type: MSB
    NorthwestLiurnia_NE_NW = map_property(NORTHWEST_LIURNIA_NE_NW)  # type: MSB
    NorthwestLiurnia_NE_SE = map_property(NORTHWEST_LIURNIA_NE_SE)  # type: MSB
    NorthwestLiurnia_NE_NE = map_property(NORTHWEST_LIURNIA_NE_NE)  # type: MSB
    FarWestAltusPlateau = map_property(FAR_WEST_ALTUS_PLATEAU)  # type: MSB
    FarWestAltusPlateau_SE = map_property(FAR_WEST_ALTUS_PLATEAU_SE)  # type: MSB
    FarWestAltusPlateau_SE_SE = map_property(FAR_WEST_ALTUS_PLATEAU_SE_SE)  # type: MSB
    FarWestAltusPlateau_SE_NE = map_property(FAR_WEST_ALTUS_PLATEAU_SE_NE)  # type: MSB
    FarWestAltusPlateau_NE = map_property(FAR_WEST_ALTUS_PLATEAU_NE)  # type: MSB
    FarWestAltusPlateau_NE_SE = map_property(FAR_WEST_ALTUS_PLATEAU_NE_SE)  # type: MSB
    FarWestLimgrave = map_property(FAR_WEST_LIMGRAVE)  # type: MSB
    FarWestLimgrave_NE = map_property(FAR_WEST_LIMGRAVE_NE)  # type: MSB
    FarWestLimgrave_NE_NW = map_property(FAR_WEST_LIMGRAVE_NE_NW)  # type: MSB
    FarWestLimgrave_NE_NE = map_property(FAR_WEST_LIMGRAVE_NE_NE)  # type: MSB
    SoutheastLiurnia = map_property(SOUTHEAST_LIURNIA)  # type: MSB
    SoutheastLiurnia_SW = map_property(SOUTHEAST_LIURNIA_SW)  # type: MSB
    SoutheastLiurnia_SW_NW = map_property(SOUTHEAST_LIURNIA_SW_NW)  # type: MSB
    SoutheastLiurnia_SW_NE = map_property(SOUTHEAST_LIURNIA_SW_NE)  # type: MSB
    SoutheastLiurnia_NW = map_property(SOUTHEAST_LIURNIA_NW)  # type: MSB
    SoutheastLiurnia_NW_SW = map_property(SOUTHEAST_LIURNIA_NW_SW)  # type: MSB
    SoutheastLiurnia_NW_NW = map_property(SOUTHEAST_LIURNIA_NW_NW)  # type: MSB
    SoutheastLiurnia_NW_SE = map_property(SOUTHEAST_LIURNIA_NW_SE)  # type: MSB
    SoutheastLiurnia_NW_NE = map_property(SOUTHEAST_LIURNIA_NW_NE)  # type: MSB
    SoutheastLiurnia_SE = map_property(SOUTHEAST_LIURNIA_SE)  # type: MSB
    SoutheastLiurnia_SE_SW = map_property(SOUTHEAST_LIURNIA_SE_SW)  # type: MSB
    SoutheastLiurnia_SE_NW = map_property(SOUTHEAST_LIURNIA_SE_NW)  # type: MSB
    SoutheastLiurnia_SE_SE = map_property(SOUTHEAST_LIURNIA_SE_SE)  # type: MSB
    SoutheastLiurnia_SE_NE = map_property(SOUTHEAST_LIURNIA_SE_NE)  # type: MSB
    SoutheastLiurnia_NE = map_property(SOUTHEAST_LIURNIA_NE)  # type: MSB
    SoutheastLiurnia_NE_SW = map_property(SOUTHEAST_LIURNIA_NE_SW)  # type: MSB
    SoutheastLiurnia_NE_NW = map_property(SOUTHEAST_LIURNIA_NE_NW)  # type: MSB
    SoutheastLiurnia_NE_SE = map_property(SOUTHEAST_LIURNIA_NE_SE)  # type: MSB
    SoutheastLiurnia_NE_NE = map_property(SOUTHEAST_LIURNIA_NE_NE)  # type: MSB
    EastLiurnia = map_property(EAST_LIURNIA)  # type: MSB
    EastLiurnia_SW = map_property(EAST_LIURNIA_SW)  # type: MSB
    EastLiurnia_SW_SW = map_property(EAST_LIURNIA_SW_SW)  # type: MSB
    EastLiurnia_SW_NW = map_property(EAST_LIURNIA_SW_NW)  # type: MSB
    EastLiurnia_SW_SE = map_property(EAST_LIURNIA_SW_SE)  # type: MSB
    EastLiurnia_SW_NE = map_property(EAST_LIURNIA_SW_NE)  # type: MSB
    EastLiurnia_NW = map_property(EAST_LIURNIA_NW)  # type: MSB
    EastLiurnia_NW_SW = map_property(EAST_LIURNIA_NW_SW)  # type: MSB
    EastLiurnia_NW_NW = map_property(EAST_LIURNIA_NW_NW)  # type: MSB
    EastLiurnia_NW_SE = map_property(EAST_LIURNIA_NW_SE)  # type: MSB
    EastLiurnia_NW_NE = map_property(EAST_LIURNIA_NW_NE)  # type: MSB
    EastLiurnia_SE = map_property(EAST_LIURNIA_SE)  # type: MSB
    EastLiurnia_SE_SW = map_property(EAST_LIURNIA_SE_SW)  # type: MSB
    EastLiurnia_SE_NW = map_property(EAST_LIURNIA_SE_NW)  # type: MSB
    EastLiurnia_SE_SE = map_property(EAST_LIURNIA_SE_SE)  # type: MSB
    EastLiurnia_SE_NE = map_property(EAST_LIURNIA_SE_NE)  # type: MSB
    EastLiurnia_NE = map_property(EAST_LIURNIA_NE)  # type: MSB
    EastLiurnia_NE_SW = map_property(EAST_LIURNIA_NE_SW)  # type: MSB
    EastLiurnia_NE_NW = map_property(EAST_LIURNIA_NE_NW)  # type: MSB
    EastLiurnia_NE_SE = map_property(EAST_LIURNIA_NE_SE)  # type: MSB
    LiurniaToAltusPlateau = map_property(LIURNIA_TO_ALTUS_PLATEAU)  # type: MSB
    LiurniaToAltusPlateau_SW = map_property(LIURNIA_TO_ALTUS_PLATEAU_SW)  # type: MSB
    LiurniaToAltusPlateau_SW_SW = map_property(LIURNIA_TO_ALTUS_PLATEAU_SW_SW)  # type: MSB
    LiurniaToAltusPlateau_SW_NW = map_property(LIURNIA_TO_ALTUS_PLATEAU_SW_NW)  # type: MSB
    LiurniaToAltusPlateau_SW_SE = map_property(LIURNIA_TO_ALTUS_PLATEAU_SW_SE)  # type: MSB
    LiurniaToAltusPlateau_SW_NE = map_property(LIURNIA_TO_ALTUS_PLATEAU_SW_NE)  # type: MSB
    LiurniaToAltusPlateau_NW = map_property(LIURNIA_TO_ALTUS_PLATEAU_NW)  # type: MSB
    LiurniaToAltusPlateau_NW_SW = map_property(LIURNIA_TO_ALTUS_PLATEAU_NW_SW)  # type: MSB
    LiurniaToAltusPlateau_NW_NW = map_property(LIURNIA_TO_ALTUS_PLATEAU_NW_NW)  # type: MSB
    LiurniaToAltusPlateau_NW_SE = map_property(LIURNIA_TO_ALTUS_PLATEAU_NW_SE)  # type: MSB
    LiurniaToAltusPlateau_NW_NE = map_property(LIURNIA_TO_ALTUS_PLATEAU_NW_NE)  # type: MSB
    LiurniaToAltusPlateau_SE = map_property(LIURNIA_TO_ALTUS_PLATEAU_SE)  # type: MSB
    LiurniaToAltusPlateau_SE_SW = map_property(LIURNIA_TO_ALTUS_PLATEAU_SE_SW)  # type: MSB
    LiurniaToAltusPlateau_SE_NW = map_property(LIURNIA_TO_ALTUS_PLATEAU_SE_NW)  # type: MSB
    LiurniaToAltusPlateau_SE_SE = map_property(LIURNIA_TO_ALTUS_PLATEAU_SE_SE)  # type: MSB
    LiurniaToAltusPlateau_SE_NE = map_property(LIURNIA_TO_ALTUS_PLATEAU_SE_NE)  # type: MSB
    LiurniaToAltusPlateau_NE = map_property(LIURNIA_TO_ALTUS_PLATEAU_NE)  # type: MSB
    LiurniaToAltusPlateau_NE_SW = map_property(LIURNIA_TO_ALTUS_PLATEAU_NE_SW)  # type: MSB
    LiurniaToAltusPlateau_NE_NW = map_property(LIURNIA_TO_ALTUS_PLATEAU_NE_NW)  # type: MSB
    LiurniaToAltusPlateau_NE_SE = map_property(LIURNIA_TO_ALTUS_PLATEAU_NE_SE)  # type: MSB
    LiurniaToAltusPlateau_NE_NE = map_property(LIURNIA_TO_ALTUS_PLATEAU_NE_NE)  # type: MSB
    WestAltusPlateau = map_property(WEST_ALTUS_PLATEAU)  # type: MSB
    WestAltusPlateau_SW = map_property(WEST_ALTUS_PLATEAU_SW)  # type: MSB
    WestAltusPlateau_SW_SW = map_property(WEST_ALTUS_PLATEAU_SW_SW)  # type: MSB
    WestAltusPlateau_SW_NW = map_property(WEST_ALTUS_PLATEAU_SW_NW)  # type: MSB
    WestAltusPlateau_SW_SE = map_property(WEST_ALTUS_PLATEAU_SW_SE)  # type: MSB
    WestAltusPlateau_SW_NE = map_property(WEST_ALTUS_PLATEAU_SW_NE)  # type: MSB
    WestAltusPlateau_NW = map_property(WEST_ALTUS_PLATEAU_NW)  # type: MSB
    WestAltusPlateau_NW_SW = map_property(WEST_ALTUS_PLATEAU_NW_SW)  # type: MSB
    WestAltusPlateau_NW_SE = map_property(WEST_ALTUS_PLATEAU_NW_SE)  # type: MSB
    WestAltusPlateau_NW_NE = map_property(WEST_ALTUS_PLATEAU_NW_NE)  # type: MSB
    WestAltusPlateau_SE = map_property(WEST_ALTUS_PLATEAU_SE)  # type: MSB
    WestAltusPlateau_SE_SW = map_property(WEST_ALTUS_PLATEAU_SE_SW)  # type: MSB
    WestAltusPlateau_SE_NW = map_property(WEST_ALTUS_PLATEAU_SE_NW)  # type: MSB
    WestAltusPlateau_SE_SE = map_property(WEST_ALTUS_PLATEAU_SE_SE)  # type: MSB
    WestAltusPlateau_SE_NE = map_property(WEST_ALTUS_PLATEAU_SE_NE)  # type: MSB
    WestAltusPlateau_NE = map_property(WEST_ALTUS_PLATEAU_NE)  # type: MSB
    WestAltusPlateau_NE_SW = map_property(WEST_ALTUS_PLATEAU_NE_SW)  # type: MSB
    WestAltusPlateau_NE_SE = map_property(WEST_ALTUS_PLATEAU_NE_SE)  # type: MSB
    SouthWeepingPeninsula = map_property(SOUTH_WEEPING_PENINSULA)  # type: MSB
    SouthWeepingPeninsula_NE = map_property(SOUTH_WEEPING_PENINSULA_NE)  # type: MSB
    SouthWeepingPeninsula_NE_SE = map_property(SOUTH_WEEPING_PENINSULA_NE_SE)  # type: MSB
    SouthWeepingPeninsula_NE_NE = map_property(SOUTH_WEEPING_PENINSULA_NE_NE)  # type: MSB
    WestWeepingPeninsula = map_property(WEST_WEEPING_PENINSULA)  # type: MSB
    WestWeepingPeninsula_SW = map_property(WEST_WEEPING_PENINSULA_SW)  # type: MSB
    WestWeepingPeninsula_SW_NW = map_property(WEST_WEEPING_PENINSULA_SW_NW)  # type: MSB
    WestWeepingPeninsula_SW_SE = map_property(WEST_WEEPING_PENINSULA_SW_SE)  # type: MSB
    WestWeepingPeninsula_SW_NE = map_property(WEST_WEEPING_PENINSULA_SW_NE)  # type: MSB
    WestWeepingPeninsula_NW = map_property(WEST_WEEPING_PENINSULA_NW)  # type: MSB
    WestWeepingPeninsula_NW_SE = map_property(WEST_WEEPING_PENINSULA_NW_SE)  # type: MSB
    WestWeepingPeninsula_NW_NE = map_property(WEST_WEEPING_PENINSULA_NW_NE)  # type: MSB
    WestWeepingPeninsula_SE = map_property(WEST_WEEPING_PENINSULA_SE)  # type: MSB
    WestWeepingPeninsula_SE_SW = map_property(WEST_WEEPING_PENINSULA_SE_SW)  # type: MSB
    WestWeepingPeninsula_SE_NW = map_property(WEST_WEEPING_PENINSULA_SE_NW)  # type: MSB
    WestWeepingPeninsula_SE_SE = map_property(WEST_WEEPING_PENINSULA_SE_SE)  # type: MSB
    WestWeepingPeninsula_SE_NE = map_property(WEST_WEEPING_PENINSULA_SE_NE)  # type: MSB
    WestWeepingPeninsula_NE = map_property(WEST_WEEPING_PENINSULA_NE)  # type: MSB
    WestWeepingPeninsula_NE_SW = map_property(WEST_WEEPING_PENINSULA_NE_SW)  # type: MSB
    WestWeepingPeninsula_NE_NW = map_property(WEST_WEEPING_PENINSULA_NE_NW)  # type: MSB
    WestWeepingPeninsula_NE_SE = map_property(WEST_WEEPING_PENINSULA_NE_SE)  # type: MSB
    WestWeepingPeninsula_NE_NE = map_property(WEST_WEEPING_PENINSULA_NE_NE)  # type: MSB
    WestLimgrave = map_property(WEST_LIMGRAVE)  # type: MSB
    WestLimgrave_SW = map_property(WEST_LIMGRAVE_SW)  # type: MSB
    WestLimgrave_SW_SE = map_property(WEST_LIMGRAVE_SW_SE)  # type: MSB
    WestLimgrave_SW_NE = map_property(WEST_LIMGRAVE_SW_NE)  # type: MSB
    WestLimgrave_NW = map_property(WEST_LIMGRAVE_NW)  # type: MSB
    WestLimgrave_NW_SW = map_property(WEST_LIMGRAVE_NW_SW)  # type: MSB
    WestLimgrave_NW_NW = map_property(WEST_LIMGRAVE_NW_NW)  # type: MSB
    WestLimgrave_NW_SE = map_property(WEST_LIMGRAVE_NW_SE)  # type: MSB
    WestLimgrave_NW_NE = map_property(WEST_LIMGRAVE_NW_NE)  # type: MSB
    WestLimgrave_SE = map_property(WEST_LIMGRAVE_SE)  # type: MSB
    WestLimgrave_SE_SW = map_property(WEST_LIMGRAVE_SE_SW)  # type: MSB
    WestLimgrave_SE_NW = map_property(WEST_LIMGRAVE_SE_NW)  # type: MSB
    WestLimgrave_SE_SE = map_property(WEST_LIMGRAVE_SE_SE)  # type: MSB
    WestLimgrave_SE_NE = map_property(WEST_LIMGRAVE_SE_NE)  # type: MSB
    WestLimgrave_NE = map_property(WEST_LIMGRAVE_NE)  # type: MSB
    WestLimgrave_NE_SW = map_property(WEST_LIMGRAVE_NE_SW)  # type: MSB
    WestLimgrave_NE_NW = map_property(WEST_LIMGRAVE_NE_NW)  # type: MSB
    WestLimgrave_NE_SE = map_property(WEST_LIMGRAVE_NE_SE)  # type: MSB
    WestLimgrave_NE_NE = map_property(WEST_LIMGRAVE_NE_NE)  # type: MSB
    NorthwestLimgraveCoast = map_property(NORTHWEST_LIMGRAVE_COAST)  # type: MSB
    NorthwestLimgraveCoast_SW = map_property(NORTHWEST_LIMGRAVE_COAST_SW)  # type: MSB
    NorthwestLimgraveCoast_SW_SW = map_property(NORTHWEST_LIMGRAVE_COAST_SW_SW)  # type: MSB
    NorthwestLimgraveCoast_SE = map_property(NORTHWEST_LIMGRAVE_COAST_SE)  # type: MSB
    NorthwestLimgraveCoast_SE_SW = map_property(NORTHWEST_LIMGRAVE_COAST_SE_SW)  # type: MSB
    NorthwestLimgraveCoast_SE_SE = map_property(NORTHWEST_LIMGRAVE_COAST_SE_SE)  # type: MSB
    SouthAltusPlateau = map_property(SOUTH_ALTUS_PLATEAU)  # type: MSB
    SouthAltusPlateau_NW = map_property(SOUTH_ALTUS_PLATEAU_NW)  # type: MSB
    SouthAltusPlateau_NW_SW = map_property(SOUTH_ALTUS_PLATEAU_NW_SW)  # type: MSB
    SouthAltusPlateau_NW_NW = map_property(SOUTH_ALTUS_PLATEAU_NW_NW)  # type: MSB
    SouthAltusPlateau_NW_SE = map_property(SOUTH_ALTUS_PLATEAU_NW_SE)  # type: MSB
    SouthAltusPlateau_NW_NE = map_property(SOUTH_ALTUS_PLATEAU_NW_NE)  # type: MSB
    SouthAltusPlateau_NE = map_property(SOUTH_ALTUS_PLATEAU_NE)  # type: MSB
    SouthAltusPlateau_NE_SW = map_property(SOUTH_ALTUS_PLATEAU_NE_SW)  # type: MSB
    SouthAltusPlateau_NE_NW = map_property(SOUTH_ALTUS_PLATEAU_NE_NW)  # type: MSB
    SouthAltusPlateau_NE_SE = map_property(SOUTH_ALTUS_PLATEAU_NE_SE)  # type: MSB
    SouthAltusPlateau_NE_NE = map_property(SOUTH_ALTUS_PLATEAU_NE_NE)  # type: MSB
    NorthAltusPlateau = map_property(NORTH_ALTUS_PLATEAU)  # type: MSB
    NorthAltusPlateau_SW = map_property(NORTH_ALTUS_PLATEAU_SW)  # type: MSB
    NorthAltusPlateau_SW_SW = map_property(NORTH_ALTUS_PLATEAU_SW_SW)  # type: MSB
    NorthAltusPlateau_SW_NW = map_property(NORTH_ALTUS_PLATEAU_SW_NW)  # type: MSB
    NorthAltusPlateau_SW_SE = map_property(NORTH_ALTUS_PLATEAU_SW_SE)  # type: MSB
    NorthAltusPlateau_SW_NE = map_property(NORTH_ALTUS_PLATEAU_SW_NE)  # type: MSB
    NorthAltusPlateau_NW = map_property(NORTH_ALTUS_PLATEAU_NW)  # type: MSB
    NorthAltusPlateau_NW_SW = map_property(NORTH_ALTUS_PLATEAU_NW_SW)  # type: MSB
    NorthAltusPlateau_NW_NW = map_property(NORTH_ALTUS_PLATEAU_NW_NW)  # type: MSB
    NorthAltusPlateau_NW_SE = map_property(NORTH_ALTUS_PLATEAU_NW_SE)  # type: MSB
    NorthAltusPlateau_NW_NE = map_property(NORTH_ALTUS_PLATEAU_NW_NE)  # type: MSB
    NorthAltusPlateau_SE = map_property(NORTH_ALTUS_PLATEAU_SE)  # type: MSB
    NorthAltusPlateau_SE_SW = map_property(NORTH_ALTUS_PLATEAU_SE_SW)  # type: MSB
    NorthAltusPlateau_SE_NW = map_property(NORTH_ALTUS_PLATEAU_SE_NW)  # type: MSB
    NorthAltusPlateau_SE_SE = map_property(NORTH_ALTUS_PLATEAU_SE_SE)  # type: MSB
    NorthAltusPlateau_SE_NE = map_property(NORTH_ALTUS_PLATEAU_SE_NE)  # type: MSB
    NorthAltusPlateau_NE = map_property(NORTH_ALTUS_PLATEAU_NE)  # type: MSB
    NorthAltusPlateau_NE_SW = map_property(NORTH_ALTUS_PLATEAU_NE_SW)  # type: MSB
    NorthAltusPlateau_NE_NW = map_property(NORTH_ALTUS_PLATEAU_NE_NW)  # type: MSB
    NorthAltusPlateau_NE_SE = map_property(NORTH_ALTUS_PLATEAU_NE_SE)  # type: MSB
    SoutheastWeepingPeninsulaCoast = map_property(SOUTHEAST_WEEPING_PENINSULA_COAST)  # type: MSB
    SoutheastWeepingPeninsulaCoast_NW = map_property(SOUTHEAST_WEEPING_PENINSULA_COAST_NW)  # type: MSB
    SoutheastWeepingPeninsulaCoast_NW_NW = map_property(SOUTHEAST_WEEPING_PENINSULA_COAST_NW_NW)  # type: MSB
    EastWeepingPeninsula = map_property(EAST_WEEPING_PENINSULA)  # type: MSB
    EastWeepingPeninsula_SW = map_property(EAST_WEEPING_PENINSULA_SW)  # type: MSB
    EastWeepingPeninsula_SW_SW = map_property(EAST_WEEPING_PENINSULA_SW_SW)  # type: MSB
    EastWeepingPeninsula_SW_NW = map_property(EAST_WEEPING_PENINSULA_SW_NW)  # type: MSB
    EastWeepingPeninsula_SW_SE = map_property(EAST_WEEPING_PENINSULA_SW_SE)  # type: MSB
    EastWeepingPeninsula_SW_NE = map_property(EAST_WEEPING_PENINSULA_SW_NE)  # type: MSB
    EastWeepingPeninsula_NW = map_property(EAST_WEEPING_PENINSULA_NW)  # type: MSB
    EastWeepingPeninsula_NW_SW = map_property(EAST_WEEPING_PENINSULA_NW_SW)  # type: MSB
    EastWeepingPeninsula_NW_NW = map_property(EAST_WEEPING_PENINSULA_NW_NW)  # type: MSB
    EastWeepingPeninsula_NW_SE = map_property(EAST_WEEPING_PENINSULA_NW_SE)  # type: MSB
    EastWeepingPeninsula_NW_NE = map_property(EAST_WEEPING_PENINSULA_NW_NE)  # type: MSB
    EastLimgrave = map_property(EAST_LIMGRAVE)  # type: MSB
    EastLimgrave_SW = map_property(EAST_LIMGRAVE_SW)  # type: MSB
    EastLimgrave_SW_SW = map_property(EAST_LIMGRAVE_SW_SW)  # type: MSB
    EastLimgrave_SW_NW = map_property(EAST_LIMGRAVE_SW_NW)  # type: MSB
    EastLimgrave_SW_SE = map_property(EAST_LIMGRAVE_SW_SE)  # type: MSB
    EastLimgrave_SW_NE = map_property(EAST_LIMGRAVE_SW_NE)  # type: MSB
    EastLimgrave_NW = map_property(EAST_LIMGRAVE_NW)  # type: MSB
    EastLimgrave_NW_SW = map_property(EAST_LIMGRAVE_NW_SW)  # type: MSB
    EastLimgrave_NW_NW = map_property(EAST_LIMGRAVE_NW_NW)  # type: MSB
    EastLimgrave_NW_SE = map_property(EAST_LIMGRAVE_NW_SE)  # type: MSB
    EastLimgrave_NW_NE = map_property(EAST_LIMGRAVE_NW_NE)  # type: MSB
    EastLimgrave_SE = map_property(EAST_LIMGRAVE_SE)  # type: MSB
    EastLimgrave_SE_SW = map_property(EAST_LIMGRAVE_SE_SW)  # type: MSB
    EastLimgrave_SE_NW = map_property(EAST_LIMGRAVE_SE_NW)  # type: MSB
    EastLimgrave_SE_NE = map_property(EAST_LIMGRAVE_SE_NE)  # type: MSB
    EastLimgrave_NE = map_property(EAST_LIMGRAVE_NE)  # type: MSB
    EastLimgrave_NE_SW = map_property(EAST_LIMGRAVE_NE_SW)  # type: MSB
    EastLimgrave_NE_NW = map_property(EAST_LIMGRAVE_NE_NW)  # type: MSB
    EastLimgrave_NE_SE = map_property(EAST_LIMGRAVE_NE_SE)  # type: MSB
    EastLimgrave_NE_NE = map_property(EAST_LIMGRAVE_NE_NE)  # type: MSB
    NorthwestCaelid = map_property(NORTHWEST_CAELID)  # type: MSB
    NorthwestCaelid_SW = map_property(NORTHWEST_CAELID_SW)  # type: MSB
    NorthwestCaelid_SW_SE = map_property(NORTHWEST_CAELID_SW_SE)  # type: MSB
    NorthwestCaelid_SE = map_property(NORTHWEST_CAELID_SE)  # type: MSB
    NorthwestCaelid_SE_SW = map_property(NORTHWEST_CAELID_SE_SW)  # type: MSB
    NorthwestCaelid_SE_SE = map_property(NORTHWEST_CAELID_SE_SE)  # type: MSB
    NorthwestCaelid_SE_NE = map_property(NORTHWEST_CAELID_SE_NE)  # type: MSB
    NorthwestCaelid_NE = map_property(NORTHWEST_CAELID_NE)  # type: MSB
    NorthwestCaelid_NE_SE = map_property(NORTHWEST_CAELID_NE_SE)  # type: MSB
    SoutheastAltusPlateau = map_property(SOUTHEAST_ALTUS_PLATEAU)  # type: MSB
    SoutheastAltusPlateau_NW = map_property(SOUTHEAST_ALTUS_PLATEAU_NW)  # type: MSB
    SoutheastAltusPlateau_NW_NE = map_property(SOUTHEAST_ALTUS_PLATEAU_NW_NE)  # type: MSB
    SoutheastAltusPlateau_NE = map_property(SOUTHEAST_ALTUS_PLATEAU_NE)  # type: MSB
    SoutheastAltusPlateau_NE_NE = map_property(SOUTHEAST_ALTUS_PLATEAU_NE_NE)  # type: MSB
    NortheastAltusPlateau = map_property(NORTHEAST_ALTUS_PLATEAU)  # type: MSB
    NortheastAltusPlateau_SW = map_property(NORTHEAST_ALTUS_PLATEAU_SW)  # type: MSB
    NortheastAltusPlateau_SW_SW = map_property(NORTHEAST_ALTUS_PLATEAU_SW_SW)  # type: MSB
    NortheastAltusPlateau_SW_NW = map_property(NORTHEAST_ALTUS_PLATEAU_SW_NW)  # type: MSB
    NortheastAltusPlateau_SW_SE = map_property(NORTHEAST_ALTUS_PLATEAU_SW_SE)  # type: MSB
    NortheastAltusPlateau_SW_NE = map_property(NORTHEAST_ALTUS_PLATEAU_SW_NE)  # type: MSB
    NortheastAltusPlateau_NE = map_property(NORTHEAST_ALTUS_PLATEAU_NE)  # type: MSB
    NortheastAltusPlateau_NE_NW = map_property(NORTHEAST_ALTUS_PLATEAU_NE_NW)  # type: MSB
    NortheastAltusPlateau_NE_NE = map_property(NORTHEAST_ALTUS_PLATEAU_NE_NE)  # type: MSB
    WestConsecratedSnowfield = map_property(WEST_CONSECRATED_SNOWFIELD)  # type: MSB
    WestConsecratedSnowfield_SE = map_property(WEST_CONSECRATED_SNOWFIELD_SE)  # type: MSB
    WestConsecratedSnowfield_SE_NW = map_property(WEST_CONSECRATED_SNOWFIELD_SE_NW)  # type: MSB
    WestConsecratedSnowfield_SE_SE = map_property(WEST_CONSECRATED_SNOWFIELD_SE_SE)  # type: MSB
    WestConsecratedSnowfield_SE_NE = map_property(WEST_CONSECRATED_SNOWFIELD_SE_NE)  # type: MSB
    WestConsecratedSnowfield_NE = map_property(WEST_CONSECRATED_SNOWFIELD_NE)  # type: MSB
    WestConsecratedSnowfield_NE_SE = map_property(WEST_CONSECRATED_SNOWFIELD_NE_SE)  # type: MSB
    FarSouthCaelid = map_property(FAR_SOUTH_CAELID)  # type: MSB
    FarSouthCaelid_NE = map_property(FAR_SOUTH_CAELID_NE)  # type: MSB
    FarSouthCaelid_NE_NE = map_property(FAR_SOUTH_CAELID_NE_NE)  # type: MSB
    SouthCaelid = map_property(SOUTH_CAELID)  # type: MSB
    SouthCaelid_SW = map_property(SOUTH_CAELID_SW)  # type: MSB
    SouthCaelid_SW_SW = map_property(SOUTH_CAELID_SW_SW)  # type: MSB
    SouthCaelid_SW_NW = map_property(SOUTH_CAELID_SW_NW)  # type: MSB
    SouthCaelid_SW_SE = map_property(SOUTH_CAELID_SW_SE)  # type: MSB
    SouthCaelid_SW_NE = map_property(SOUTH_CAELID_SW_NE)  # type: MSB
    SouthCaelid_NW = map_property(SOUTH_CAELID_NW)  # type: MSB
    SouthCaelid_NW_SW = map_property(SOUTH_CAELID_NW_SW)  # type: MSB
    SouthCaelid_NW_NW = map_property(SOUTH_CAELID_NW_NW)  # type: MSB
    SouthCaelid_NW_SE = map_property(SOUTH_CAELID_NW_SE)  # type: MSB
    SouthCaelid_NW_NE = map_property(SOUTH_CAELID_NW_NE)  # type: MSB
    SouthCaelid_SE = map_property(SOUTH_CAELID_SE)  # type: MSB
    SouthCaelid_SE_SW = map_property(SOUTH_CAELID_SE_SW)  # type: MSB
    SouthCaelid_SE_NW = map_property(SOUTH_CAELID_SE_NW)  # type: MSB
    SouthCaelid_SE_SE = map_property(SOUTH_CAELID_SE_SE)  # type: MSB
    SouthCaelid_SE_NE = map_property(SOUTH_CAELID_SE_NE)  # type: MSB
    SouthCaelid_NE = map_property(SOUTH_CAELID_NE)  # type: MSB
    SouthCaelid_NE_SW = map_property(SOUTH_CAELID_NE_SW)  # type: MSB
    SouthCaelid_NE_NW = map_property(SOUTH_CAELID_NE_NW)  # type: MSB
    SouthCaelid_NE_SE = map_property(SOUTH_CAELID_NE_SE)  # type: MSB
    SouthCaelid_NE_NE = map_property(SOUTH_CAELID_NE_NE)  # type: MSB
    NorthCaelid = map_property(NORTH_CAELID)  # type: MSB
    NorthCaelid_SW = map_property(NORTH_CAELID_SW)  # type: MSB
    NorthCaelid_SW_SW = map_property(NORTH_CAELID_SW_SW)  # type: MSB
    NorthCaelid_SW_NW = map_property(NORTH_CAELID_SW_NW)  # type: MSB
    NorthCaelid_SW_SE = map_property(NORTH_CAELID_SW_SE)  # type: MSB
    NorthCaelid_SW_NE = map_property(NORTH_CAELID_SW_NE)  # type: MSB
    NorthCaelid_SE = map_property(NORTH_CAELID_SE)  # type: MSB
    NorthCaelid_SE_SW = map_property(NORTH_CAELID_SE_SW)  # type: MSB
    NorthCaelid_SE_NW = map_property(NORTH_CAELID_SE_NW)  # type: MSB
    NorthCaelid_SE_SE = map_property(NORTH_CAELID_SE_SE)  # type: MSB
    NorthCaelid_SE_NE = map_property(NORTH_CAELID_SE_NE)  # type: MSB
    NorthCaelid_NE = map_property(NORTH_CAELID_NE)  # type: MSB
    NorthCaelid_NE_SE = map_property(NORTH_CAELID_NE_SE)  # type: MSB
    NorthCaelid_NE_NE = map_property(NORTH_CAELID_NE_NE)  # type: MSB
    ForbiddenLands = map_property(FORBIDDEN_LANDS)  # type: MSB
    ForbiddenLands_NW = map_property(FORBIDDEN_LANDS_NW)  # type: MSB
    ForbiddenLands_NW_NW = map_property(FORBIDDEN_LANDS_NW_NW)  # type: MSB
    SouthwestMountaintops = map_property(SOUTHWEST_MOUNTAINTOPS)  # type: MSB
    SouthwestMountaintops_SW = map_property(SOUTHWEST_MOUNTAINTOPS_SW)  # type: MSB
    SouthwestMountaintops_SW_SE = map_property(SOUTHWEST_MOUNTAINTOPS_SW_SE)  # type: MSB
    SouthwestMountaintops_SW_NE = map_property(SOUTHWEST_MOUNTAINTOPS_SW_NE)  # type: MSB
    SouthwestMountaintops_NW = map_property(SOUTHWEST_MOUNTAINTOPS_NW)  # type: MSB
    SouthwestMountaintops_NW_SW = map_property(SOUTHWEST_MOUNTAINTOPS_NW_SW)  # type: MSB
    SouthwestMountaintops_NW_NW = map_property(SOUTHWEST_MOUNTAINTOPS_NW_NW)  # type: MSB
    SouthwestMountaintops_NW_SE = map_property(SOUTHWEST_MOUNTAINTOPS_NW_SE)  # type: MSB
    SouthwestMountaintops_NW_NE = map_property(SOUTHWEST_MOUNTAINTOPS_NW_NE)  # type: MSB
    SouthwestMountaintops_SE = map_property(SOUTHWEST_MOUNTAINTOPS_SE)  # type: MSB
    SouthwestMountaintops_SE_NW = map_property(SOUTHWEST_MOUNTAINTOPS_SE_NW)  # type: MSB
    SouthwestMountaintops_SE_SE = map_property(SOUTHWEST_MOUNTAINTOPS_SE_SE)  # type: MSB
    SouthwestMountaintops_SE_NE = map_property(SOUTHWEST_MOUNTAINTOPS_SE_NE)  # type: MSB
    SouthwestMountaintops_NE = map_property(SOUTHWEST_MOUNTAINTOPS_NE)  # type: MSB
    SouthwestMountaintops_NE_SW = map_property(SOUTHWEST_MOUNTAINTOPS_NE_SW)  # type: MSB
    SouthwestMountaintops_NE_NW = map_property(SOUTHWEST_MOUNTAINTOPS_NE_NW)  # type: MSB
    SouthwestMountaintops_NE_SE = map_property(SOUTHWEST_MOUNTAINTOPS_NE_SE)  # type: MSB
    SouthwestMountaintops_NE_NE = map_property(SOUTHWEST_MOUNTAINTOPS_NE_NE)  # type: MSB
    NorthwestMountaintops = map_property(NORTHWEST_MOUNTAINTOPS)  # type: MSB
    NorthwestMountaintops_SW = map_property(NORTHWEST_MOUNTAINTOPS_SW)  # type: MSB
    NorthwestMountaintops_SW_SW = map_property(NORTHWEST_MOUNTAINTOPS_SW_SW)  # type: MSB
    NorthwestMountaintops_SW_NW = map_property(NORTHWEST_MOUNTAINTOPS_SW_NW)  # type: MSB
    NorthwestMountaintops_SW_SE = map_property(NORTHWEST_MOUNTAINTOPS_SW_SE)  # type: MSB
    NorthwestMountaintops_SW_NE = map_property(NORTHWEST_MOUNTAINTOPS_SW_NE)  # type: MSB
    NorthwestMountaintops_NW = map_property(NORTHWEST_MOUNTAINTOPS_NW)  # type: MSB
    NorthwestMountaintops_NW_SW = map_property(NORTHWEST_MOUNTAINTOPS_NW_SW)  # type: MSB
    NorthwestMountaintops_SE = map_property(NORTHWEST_MOUNTAINTOPS_SE)  # type: MSB
    NorthwestMountaintops_SE_SW = map_property(NORTHWEST_MOUNTAINTOPS_SE_SW)  # type: MSB
    NorthwestMountaintops_SE_NW = map_property(NORTHWEST_MOUNTAINTOPS_SE_NW)  # type: MSB
    NorthwestMountaintops_SE_SE = map_property(NORTHWEST_MOUNTAINTOPS_SE_SE)  # type: MSB
    NorthwestMountaintops_SE_NE = map_property(NORTHWEST_MOUNTAINTOPS_SE_NE)  # type: MSB
    NorthwestMountaintops_NE = map_property(NORTHWEST_MOUNTAINTOPS_NE)  # type: MSB
    NorthwestMountaintops_NE_SE = map_property(NORTHWEST_MOUNTAINTOPS_NE_SE)  # type: MSB
    SoutheastCaelid = map_property(SOUTHEAST_CAELID)  # type: MSB
    SoutheastCaelid_SW = map_property(SOUTHEAST_CAELID_SW)  # type: MSB
    SoutheastCaelid_SW_NW = map_property(SOUTHEAST_CAELID_SW_NW)  # type: MSB
    SoutheastCaelid_NW = map_property(SOUTHEAST_CAELID_NW)  # type: MSB
    SoutheastCaelid_NW_SW = map_property(SOUTHEAST_CAELID_NW_SW)  # type: MSB
    SoutheastCaelid_NW_NW = map_property(SOUTHEAST_CAELID_NW_NW)  # type: MSB
    SoutheastCaelid_NW_SE = map_property(SOUTHEAST_CAELID_NW_SE)  # type: MSB
    SoutheastCaelid_NW_NE = map_property(SOUTHEAST_CAELID_NW_NE)  # type: MSB
    NortheastCaelid = map_property(NORTHEAST_CAELID)  # type: MSB
    NortheastCaelid_SW = map_property(NORTHEAST_CAELID_SW)  # type: MSB
    NortheastCaelid_SW_SW = map_property(NORTHEAST_CAELID_SW_SW)  # type: MSB
    NortheastCaelid_SW_NW = map_property(NORTHEAST_CAELID_SW_NW)  # type: MSB
    NortheastCaelid_NW = map_property(NORTHEAST_CAELID_NW)  # type: MSB
    NortheastCaelid_NW_SW = map_property(NORTHEAST_CAELID_NW_SW)  # type: MSB
    NortheastCaelid_NW_NW = map_property(NORTHEAST_CAELID_NW_NW)  # type: MSB
    SoutheastMountaintops = map_property(SOUTHEAST_MOUNTAINTOPS)  # type: MSB
    SoutheastMountaintops_SW = map_property(SOUTHEAST_MOUNTAINTOPS_SW)  # type: MSB
    SoutheastMountaintops_SW_SW = map_property(SOUTHEAST_MOUNTAINTOPS_SW_SW)  # type: MSB
    SoutheastMountaintops_SW_NW = map_property(SOUTHEAST_MOUNTAINTOPS_SW_NW)  # type: MSB
    SoutheastMountaintops_SW_SE = map_property(SOUTHEAST_MOUNTAINTOPS_SW_SE)  # type: MSB
    SoutheastMountaintops_SW_NE = map_property(SOUTHEAST_MOUNTAINTOPS_SW_NE)  # type: MSB
    SoutheastMountaintops_NW = map_property(SOUTHEAST_MOUNTAINTOPS_NW)  # type: MSB
    SoutheastMountaintops_NW_SW = map_property(SOUTHEAST_MOUNTAINTOPS_NW_SW)  # type: MSB
    SoutheastMountaintops_NW_NW = map_property(SOUTHEAST_MOUNTAINTOPS_NW_NW)  # type: MSB
    SoutheastMountaintops_NW_SE = map_property(SOUTHEAST_MOUNTAINTOPS_NW_SE)  # type: MSB
    SoutheastMountaintops_NW_NE = map_property(SOUTHEAST_MOUNTAINTOPS_NW_NE)  # type: MSB
    SoutheastMountaintops_SE = map_property(SOUTHEAST_MOUNTAINTOPS_SE)  # type: MSB
    SoutheastMountaintops_SE_NW = map_property(SOUTHEAST_MOUNTAINTOPS_SE_NW)  # type: MSB
    SoutheastMountaintops_NE = map_property(SOUTHEAST_MOUNTAINTOPS_NE)  # type: MSB
    SoutheastMountaintops_NE_NW = map_property(SOUTHEAST_MOUNTAINTOPS_NE_NW)  # type: MSB
    NortheastMountaintops = map_property(NORTHEAST_MOUNTAINTOPS)  # type: MSB
    NortheastMountaintops_SW = map_property(NORTHEAST_MOUNTAINTOPS_SW)  # type: MSB
    NortheastMountaintops_SW_SW = map_property(NORTHEAST_MOUNTAINTOPS_SW_SW)  # type: MSB
    NortheastMountaintops_SW_NW = map_property(NORTHEAST_MOUNTAINTOPS_SW_NW)  # type: MSB
    NortheastMountaintops_SW_SE = map_property(NORTHEAST_MOUNTAINTOPS_SW_SE)  # type: MSB
    NortheastMountaintops_SW_NE = map_property(NORTHEAST_MOUNTAINTOPS_SW_NE)  # type: MSB
    NortheastMountaintops_NW = map_property(NORTHEAST_MOUNTAINTOPS_NW)  # type: MSB
    NortheastMountaintops_NW_SW = map_property(NORTHEAST_MOUNTAINTOPS_NW_SW)  # type: MSB
    NortheastMountaintops_NW_SE = map_property(NORTHEAST_MOUNTAINTOPS_NW_SE)  # type: MSB
    NortheastMountaintops_SE = map_property(NORTHEAST_MOUNTAINTOPS_SE)  # type: MSB
    NortheastMountaintops_SE_SW = map_property(NORTHEAST_MOUNTAINTOPS_SE_SW)  # type: MSB
    NortheastMountaintops_SE_NW = map_property(NORTHEAST_MOUNTAINTOPS_SE_NW)  # type: MSB
    EastLimgraveMeteor = map_property(EAST_LIMGRAVE_METEOR)  # type: MSB
    EastLimgraveMeteor_SW = map_property(EAST_LIMGRAVE_METEOR_SW)  # type: MSB
    EastLimgraveMeteor_SW_SE = map_property(EAST_LIMGRAVE_METEOR_SW_SE)  # type: MSB
    NortheastAltusPlateauAshen = map_property(NORTHEAST_ALTUS_PLATEAU_ASHEN)  # type: MSB
    NortheastAltusPlateauAshen_SW = map_property(NORTHEAST_ALTUS_PLATEAU_ASHEN_SW)  # type: MSB
    NortheastAltusPlateauAshen_SW_SE = map_property(NORTHEAST_ALTUS_PLATEAU_ASHEN_SW_SE)  # type: MSB
