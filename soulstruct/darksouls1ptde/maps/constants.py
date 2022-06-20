__all__ = [
    "COMMON",
    "DEPTHS",
    "UNDEAD_BURG",
    "FIRELINK_SHRINE",
    "PAINTED_WORLD",
    "DARKROOT_GARDEN",
    "OOLACILE",
    "CATACOMBS",
    "TOMB_OF_THE_GIANTS",
    "ASH_LAKE",
    "BLIGHTTOWN",
    "LOST_IZALITH",
    "SENS_FORTRESS",
    "ANOR_LONDO",
    "NEW_LONDO_RUINS",
    "DUKES_ARCHIVES",
    "KILN_OF_THE_FIRST_FLAME",
    "UNDEAD_ASYLUM",
    "ALL_MAPS",
    "get_map",
    "get_map_variable_name",
]

from soulstruct.base.maps.utilities import get_map as _get_map_base
from soulstruct.game_types.msb_types import Map

COMMON = Map(
    None,
    None,
    name="Common",
    emevd_file_stem="common",
    msb_file_stem=None,
    ai_file_stem="aiCommon",
    esd_file_stem=None,
    variable_name="COMMON",
    verbose_name="Common",
)
DEPTHS = Map(
    10,
    0,
    name="Depths",
    variable_name="DEPTHS",
    ffxbnd_file_name="FRPG_SfxBnd_m10_00",
)
UNDEAD_BURG = Map(
    10,
    1,
    name="UndeadBurg",
    variable_name="UNDEAD_BURG",
    verbose_name="Undead Burg / Parish",
    ffxbnd_file_name="FRPG_SfxBnd_m10_01",
)
FIRELINK_SHRINE = Map(
    10,
    2,
    name="FirelinkShrine",
    variable_name="FIRELINK_SHRINE",
    verbose_name="Firelink Shrine",
    ffxbnd_file_name="FRPG_SfxBnd_m10_02",
)
PAINTED_WORLD = Map(
    11,
    0,
    name="PaintedWorld",
    variable_name="PAINTED_WORLD",
    verbose_name="Painted World",
    ffxbnd_file_name="FRPG_SfxBnd_m11",
)
DARKROOT_GARDEN = Map(
    12,
    0,
    name="DarkrootGarden",
    msb_file_stem="m12_00_00_01",
    variable_name="DARKROOT_GARDEN",
    verbose_name="Darkroot Garden / Basin",
    ffxbnd_file_name="FRPG_SfxBnd_m12_00",
)
OOLACILE = Map(
    12,
    1,
    name="Oolacile",
    variable_name="OOLACILE",
    verbose_name="Oolacile / Chasm of the Abyss",
    ffxbnd_file_name="FRPG_SfxBnd_m12_01",
)
CATACOMBS = Map(
    13,
    0,
    name="Catacombs",
    variable_name="CATACOMBS",
    ffxbnd_file_name="FRPG_SfxBnd_m13_00",
)
TOMB_OF_THE_GIANTS = Map(
    13,
    1,
    name="TombOfTheGiants",
    variable_name="TOMB_OF_THE_GIANTS",
    verbose_name="Tomb of the Giants",
    ffxbnd_file_name="FRPG_SfxBnd_m13_01",
)
ASH_LAKE = Map(
    13,
    2,
    name="AshLake",
    variable_name="ASH_LAKE",
    verbose_name="Great Hollow / Ash Lake",
    ffxbnd_file_name="FRPG_SfxBnd_m13_02",
)
BLIGHTTOWN = Map(
    14,
    0,
    name="Blighttown",
    variable_name="BLIGHTTOWN",
    verbose_name="Blighttown / Quelaag's Domain",
    ffxbnd_file_name="FRPG_SfxBnd_m14_00",
)
LOST_IZALITH = Map(
    14,
    1,
    name="LostIzalith",
    variable_name="LOST_IZALITH",
    verbose_name="Demon Ruins / Lost Izalith",
    ffxbnd_file_name="FRPG_SfxBnd_m14_01",
)
SENS_FORTRESS = Map(
    15,
    0,
    name="SensFortress",
    variable_name="SENS_FORTRESS",
    verbose_name="Sen's Fortress",
    ffxbnd_file_name="FRPG_SfxBnd_m15_00",
)
ANOR_LONDO = Map(
    15,
    1,
    name="AnorLondo",
    variable_name="ANOR_LONDO",
    verbose_name="Anor Londo",
    ffxbnd_file_name="FRPG_SfxBnd_m15_01",
)
NEW_LONDO_RUINS = Map(
    16,
    0,
    name="NewLondoRuins",
    variable_name="NEW_LONDO_RUINS",
    verbose_name="New Londo Ruins / Valley of Drakes",
    ffxbnd_file_name="FRPG_SfxBnd_m16",
)
DUKES_ARCHIVES = Map(
    17,
    0,
    name="DukesArchives",
    variable_name="DUKES_ARCHIVES",
    verbose_name="Duke's Archives / Crystal Cave",
    ffxbnd_file_name="FRPG_SfxBnd_m17",
)
KILN_OF_THE_FIRST_FLAME = Map(
    18,
    0,
    name="KilnOfTheFirstFlame",
    variable_name="KILN_OF_THE_FIRST_FLAME",
    verbose_name="Kiln of the First Flame",
    ffxbnd_file_name="FRPG_SfxBnd_m18_00",
)
UNDEAD_ASYLUM = Map(
    18,
    1,
    name="UndeadAsylum",
    variable_name="UNDEAD_ASYLUM",
    verbose_name="Undead Asylum",
    ffxbnd_file_name="FRPG_SfxBnd_m18_01",
)

ALL_MAPS = (
    COMMON,
    DEPTHS,
    UNDEAD_BURG,
    FIRELINK_SHRINE,
    PAINTED_WORLD,
    DARKROOT_GARDEN,
    OOLACILE,
    CATACOMBS,
    TOMB_OF_THE_GIANTS,
    ASH_LAKE,
    BLIGHTTOWN,
    LOST_IZALITH,
    SENS_FORTRESS,
    ANOR_LONDO,
    NEW_LONDO_RUINS,
    DUKES_ARCHIVES,
    KILN_OF_THE_FIRST_FLAME,
    UNDEAD_ASYLUM,
)


def get_map(source, block_id=None):
    return _get_map_base(source, block_id=block_id, game_maps=ALL_MAPS)


# TODO: implement for other games (adding CC and DD if appropriate).
def get_map_variable_name(area_id: int, block_id: int):
    try:
        return get_map(area_id, block_id).variable_name
    except (KeyError, ValueError):
        return f"({area_id}, {block_id})"
