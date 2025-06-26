__all__ = [
    "STORMVEIL_CASTLE",
    "CHAPEL_OF_ANTICIPATION",
    "LEYNDELL_ROYAL_CAPITAL",
    "LEYNDELL_ASHEN_CAPITAL",
    "ROUNDTABLE_HOLD",
    "AINSEL_RIVER",
    "SIOFRA_RIVER",
    "DEEPROOT_DEPTHS",
    "ASTEL_ARENA",
    "MOHGWYN_PALACE",
    "SIOFRA_RIVER_START",
    "ANCESTOR_SPIRIT_ARENA",
    "REGAL_ANCESTOR_ARENA",
    "CRUMBLING_FARUM_AZULA",
    "RAYA_LUCARIA",
    "HALIGTREE",
    "VOLCANO_MANOR",
    "STRANDED_GRAVEYARD",
    "STONE_PLATFORM",
    "SHUNNING_GROUNDS",
    "RUIN_STREWN_PRECIPICE",
]

from soulstruct.darksouls1ptde.game_types.map_types import Map

# region Legacy/Unique Dungeons
STORMVEIL_CASTLE = Map(
    10, 0, 0, 0,
    name="StormveilCastle",
    variable_name="STORMVEIL_CASTLE",
    verbose_name="Stormveil Castle",
)
CHAPEL_OF_ANTICIPATION = Map(
    10, 1, 0, 0,
    name="ChapelOfAnticipation",
    variable_name="CHAPEL_OF_ANTICIPATION",
    verbose_name="Chapel of Anticipation",
)
LEYNDELL_ROYAL_CAPITAL = Map(
    11, 0, 0, 0,
    name="LeyndellRoyalCapital",
    variable_name="LEYNDELL_ROYAL_CAPITAL",
    verbose_name="Leyndell, Royal Capital",
)
LEYNDELL_ASHEN_CAPITAL = Map(
    11, 5, 0, 0,
    name="LeyndellAshenCapital",
    variable_name="LEYNDELL_ASHEN_CAPITAL",
    verbose_name="Leyndell, Ashen Capital",
)
ROUNDTABLE_HOLD = Map(
    11, 10, 0, 0,
    name="RoundtableHold",
    variable_name="ROUNDTABLE_HOLD",
    verbose_name="Roundtable Hold",
)
AINSEL_RIVER = Map(
    12, 1, 0, 0,
    name="AinselRiver",
    variable_name="AINSEL_RIVER",
    verbose_name="Ainsel River",
)
SIOFRA_RIVER = Map(
    12, 2, 0, 0,
    name="SiofraRiver",
    variable_name="SIOFRA_RIVER",
    verbose_name="Siofra River",
)
DEEPROOT_DEPTHS = Map(
    12, 3, 0, 0,
    name="DeeprootDepths",
    variable_name="DEEPROOT_DEPTHS",
    verbose_name="Deeproot Depths",
)
ASTEL_ARENA = Map(
    12, 4, 0, 0,
    name="AstelArena",
    variable_name="ASTEL_ARENA",
    verbose_name="Astel Arena",
)
MOHGWYN_PALACE = Map(
    12, 5, 0, 0,
    name="MohgwynPalace",
    variable_name="MOHGWYN_PALACE",
    verbose_name="Mohgwyn Palace",
)
SIOFRA_RIVER_START = Map(
    # Sites of Grace: Siofra River Well Depths and Nokron, Eternal City
    12, 7, 0, 0,
    name="SiofraRiverStart",
    variable_name="SIOFRA_RIVER_START",
    verbose_name="Siofra River (Start)",
)
ANCESTOR_SPIRIT_ARENA = Map(
    12, 8, 0, 0,
    name="AncestorSpiritArena",
    variable_name="ANCESTOR_SPIRIT_ARENA",
    verbose_name="Ancestor Spirit Arena",
)
REGAL_ANCESTOR_ARENA = Map(
    12, 9, 0, 0,
    name="RegalAncestorArena",
    variable_name="REGAL_ANCESTOR_ARENA",
    verbose_name="Regal Ancestor Arena",
)
CRUMBLING_FARUM_AZULA = Map(
    13, 0, 0, 0,
    name="CrumblingFarumAzula",
    variable_name="CRUMBLING_FARUM_AZULA",
    verbose_name="Crumbling Farum Azula",
)
RAYA_LUCARIA = Map(
    14, 0, 0, 0,
    name="RayaLucaria",
    variable_name="RAYA_LUCARIA",
    verbose_name="Academy of Raya Lucaria",
)
HALIGTREE = Map(
    15, 0, 0, 0,
    name="Haligtree",
    variable_name="HALIGTREE",
    verbose_name="Miquella's Haligtree",
)
VOLCANO_MANOR = Map(
    16, 0, 0, 0,
    name="VolcanoManor",
    variable_name="VOLCANO_MANOR",
    verbose_name="Volcano Manor",
)
STRANDED_GRAVEYARD = Map(
    18, 0, 0, 0,
    name="StrandedGraveyard",
    variable_name="STRANDED_GRAVEYARD",
    verbose_name="Stranded Graveyard",  # Tutorial area
)
STONE_PLATFORM = Map(
    19, 0, 0, 0,
    name="StonePlatform",
    variable_name="STONE_PLATFORM",
    verbose_name="Stone Platform",  # End of game
)
SHUNNING_GROUNDS = Map(
    35, 0, 0, 0,
    name="ShunningGrounds",
    variable_name="SHUNNING_GROUNDS",
    verbose_name="Subterranean Shunning-Grounds",
)
RUIN_STREWN_PRECIPICE = Map(
    39, 20, 0, 0,
    name="RuinStrewnPrecipice",
    variable_name="RUIN_STREWN_PRECIPICE",
    verbose_name="Ruin-Strewn Precipice",
)
# endregion
