
__all__ = [
    "FOG_RIFT_CATACOMBS",
    "SCORPION_RIVER_CATACOMBS",
    "DARKLIGHT_CATACOMBS",
    "BELURAT_GAOL",
    "BONNY_GAOL",
    "LAMENTERS_GAOL",
    "RUINED_FORGE_LAVA_INTAKE",
    "m42_01_00_00",
    "RUINED_FORGE_OF_STARFALL_PAST",
    "TAYLEWS_RUINED_FORGE",
    "RIVERMOUTH_CAVE",
    "DRAGONS_PIT",
]

from soulstruct.base.game_types.map_types import Map

FOG_RIFT_CATACOMBS = Map(
    40, 0, 0, 0,
    name="FogRiftCatacombs",
    variable_name="FOG_RIFT_CATACOMBS",
    verbose_name="Fog Rift Catacombs",
)
SCORPION_RIVER_CATACOMBS = Map(
    40, 1, 0, 0,
    name="ScorpionRiverCatacombs",
    variable_name="SCORPION_RIVER_CATACOMBS",
    verbose_name="Scorpion River Catacombs",
)
DARKLIGHT_CATACOMBS = Map(
    40, 2, 0, 0,
    name="DarklightCatacombs",
    variable_name="DARKLIGHT_CATACOMBS",
    verbose_name="Darklight Catacombs",
)

# region Gaols
BELURAT_GAOL = Map(
    41, 0, 0, 0,
    name="BeluratGaol",
    variable_name="BELURAT_GAOL",
    verbose_name="Belurat Gaol",
)
BONNY_GAOL = Map(
    41, 1, 0, 0,
    name="BonnyGaol",
    variable_name="BONNY_GAOL",
    verbose_name="Bonny Gaol",
)
LAMENTERS_GAOL = Map(
    41, 2, 0, 0,
    name="LamentersGaol",
    variable_name="LAMENTERS_GAOL",
    verbose_name="Lamenter's Gaol",
)
# endregion

# region Ruined Forges
RUINED_FORGE_LAVA_INTAKE = Map(
    42, 0, 0, 0,
    name="RuinedForgeLavaIntake",
    variable_name="RUINED_FORGE_LAVA_INTAKE",
    verbose_name="Ruined Forge Lava Intake",
)
m42_01_00_00 = Map(
    42, 1, 0, 0,
    name="m42_01_00_00",
    variable_name="m42_01_00_00",
    verbose_name="m42_01_00_00",
)
RUINED_FORGE_OF_STARFALL_PAST = Map(
    42, 2, 0, 0,
    name="RuinedForgeOfStarfallPast",
    variable_name="RUINED_FORGE_OF_STARFALL_PAST",
    verbose_name="Ruined Forge of Starfall Past",
)
TAYLEWS_RUINED_FORGE = Map(
    42, 3, 0, 0,
    name="TaylewsRuinedForge",
    variable_name="TAYLEWS_RUINED_FORGE",
    verbose_name="Taylew's Ruined Forge",
)
# endregion

RIVERMOUTH_CAVE = Map(
    43, 0, 0, 0,
    name="RivermouthCave",
    variable_name="RIVERMOUTH_CAVE",
    verbose_name="Rivermouth Cave",
)
DRAGONS_PIT = Map(
    43, 1, 0, 0,
    name="DragonsPit",
    variable_name="DRAGONS_PIT",
    verbose_name="Dragon's Pit",
)
