
__all__ = [
    "BELURAT_TOWER_SETTLEMENT",
    "ENIR_ILIM",
    "SHADOW_KEEP",
    "SPECIMEN_STOREHOUSE",
    "BRIDGE_TO_RAUH_RUINS",
    "STONE_COFFIN_FISSURE",
    "METYR_ARENA",
    "MIDNAS_MANSE",
]

from soulstruct.base.game_types.map_types import Map

BELURAT_TOWER_SETTLEMENT = Map(
    20, 0, 0, 0,
    name="BeluratTowerSettlement",
    variable_name="BELURAT_TOWER_SETTLEMENT",
    verbose_name="Belurat, Tower Settlement",
)
ENIR_ILIM = Map(
    20, 1, 0, 0,
    name="EnirIlim",
    variable_name="ENIR_ILIM",
    verbose_name="Enir-Ilim",
)
SHADOW_KEEP = Map(  # includes Church District
    21, 0, 0, 0,
    name="ShadowKeep",
    variable_name="SHADOW_KEEP",
    verbose_name="Shadow Keep",
)
SPECIMEN_STOREHOUSE = Map(
    21, 1, 0, 0,
    name="SpecimenStorehouse",
    variable_name="SPECIMEN_STOREHOUSE",
    verbose_name="Specimen Storehouse",
)
BRIDGE_TO_RAUH_RUINS = Map(
    21, 2, 0, 0,
    name="BridgeToRauhRuins",
    variable_name="BRIDGE_TO_RAUH_RUINS",
    verbose_name="Bridge to Rauh Ruins",
)
STONE_COFFIN_FISSURE = Map(
    22, 0, 0, 0,
    name="StoneCoffinFissure",
    variable_name="STONE_COFFIN_FISSURE",
    verbose_name="Stone Coffin Fissure",
)
METYR_ARENA = Map(
    25, 0, 0, 0,
    name="MetyrArena",
    variable_name="METYR_ARENA",
    verbose_name="Metyr, Mother of Fingers Arena",
)
MIDNAS_MANSE = Map(
    28, 0, 0, 0,
    name="MidnasManse",
    variable_name="MIDNAS_MANSE",
    verbose_name="Midna's Manse",
)
