__all__ = [
    "COMMON",
    "COMMON_FUNC",
    "HIGH_WALL_OF_LOTHRIC",
    "LOTHRIC_CASTLE",
    "UNDEAD_SETTLEMENT",
    "ARCHDRAGON_PEAK",
    "FARRON_KEEP",
    "GRAND_ARCHIVES",
    "CATHEDRAL_OF_THE_DEEP",
    "IRITHYLL",
    "CATACOMBS_OF_CARTHUS",
    "PROFANED_CAPITAL",
    "FIRELINK_SHRINE",
    "KILN_OF_THE_FIRST_FLAME",
    "PAINTED_WORLD_OF_ARIANDEL",
    "ARENA_GRAND_ROOF",
    "ARENA_KILN_OF_FLAME",
    "DREG_HEAP",
    "RINGED_CITY",
    "ARENA_DRAGON_RUINS",
    "ARENA_ROUND_PLAZA",
    "ALL_MAPS",
    "ALL_MSB_FILE_NAMES",
]

from soulstruct.constants.utilities import get_map as _get_map_base
from soulstruct.game_types import Map


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
COMMON_FUNC = Map(
    None,
    None,
    name="CommonFunc",
    emevd_file_stem="common_func",
    msb_file_stem=None,
    ai_file_stem=None,
    esd_file_stem=None,
    variable_name=None,
    verbose_name="CommonFunc",
)
HIGH_WALL_OF_LOTHRIC = Map(
    30, 0, name="HighWallOfLothric", variable_name="HIGH_WALL_OF_LOTHRIC", verbose_name="High Wall of Lothric"
)
LOTHRIC_CASTLE = Map(
    30, 1, name="LothricCastle", variable_name="LOTHRIC_CASTLE", verbose_name="Lothric Castle / Consumed King's Garden"
)
UNDEAD_SETTLEMENT = Map(
    31, 0, name="UndeadSettlement", variable_name="UNDEAD_SETTLEMENT", verbose_name="Undead Settlement"
)
ARCHDRAGON_PEAK = Map(32, 0, name="ArchdragonPeak", variable_name="ARCHDRAGON_PEAK", verbose_name="Archdragon Peak")
FARRON_KEEP = Map(
    33, 0, name="FarronKeep", variable_name="FARRON_KEEP", verbose_name="Farron Keep / Road of Sacrifices"
)
GRAND_ARCHIVES = Map(34, 1, name="GrandArchives", variable_name="GRAND_ARCHIVES", verbose_name="Grand Archives")
CATHEDRAL_OF_THE_DEEP = Map(
    35, 0, name="CathedralOfTheDeep", variable_name="CATHEDRAL_OF_THE_DEEP", verbose_name="Cathedral of the Deep"
)
IRITHYLL = Map(37, 0, name="Irithyll", variable_name="IRITHYLL", verbose_name="Irithyll / Anor Londo")
CATACOMBS_OF_CARTHUS = Map(
    38,
    0,
    name="CatacombsOfCarthus",
    variable_name="CATACOMBS_OF_CARTHUS",
    verbose_name="Catacombs of Carthus / Smouldering Lake",
)
PROFANED_CAPITAL = Map(
    39, 0, name="ProfanedCapital", variable_name="PROFANED_CAPITAL", verbose_name="Profaned Capital / Irithyll Dungeon"
)
# Firelink Shrine includes Untended Graves (uses different event layers).
FIRELINK_SHRINE = Map(
    40, 0, name="FirelinkShrine", variable_name="FIRELINK_SHRINE", verbose_name="Firelink Shrine / Cemetery of Ash"
)
KILN_OF_THE_FIRST_FLAME = Map(
    41, 0, name="KilnOfTheFirstFlame", variable_name="KILN_OF_THE_FIRST_FLAME", verbose_name="Kiln of the First Flame"
)
PAINTED_WORLD_OF_ARIANDEL = Map(
    45,
    0,
    name="PaintedWorldOfAriandel",
    variable_name="PAINTED_WORLD_OF_ARIANDEL",
    verbose_name="Painted World of Ariandel",
)
ARENA_GRAND_ROOF = Map(
    46, 0, name="ArenaGrandRoof", variable_name="ARENA_GRAND_ROOF", verbose_name="Arena (Grand Roof)"
)
ARENA_KILN_OF_FLAME = Map(
    47, 0, name="ArenaKilnOfFlame", variable_name="ARENA_KILN_OF_FLAME", verbose_name="Arena (Kiln of Flame)"
)
DREG_HEAP = Map(50, 0, name="DregHeap", variable_name="DREG_HEAP", verbose_name="Dreg Heap")
RINGED_CITY = Map(51, 0, name="RingedCity", variable_name="RINGED_CITY", verbose_name="Ringed City")
ARENA_DRAGON_RUINS = Map(
    53, 0, name="ArenaDragonRuins", variable_name="ARENA_DRAGON_RUINS", verbose_name="Arena (Dragon Ruins)"
)
ARENA_ROUND_PLAZA = Map(
    54, 0, name="ArenaRoundPlaza", variable_name="ARENA_ROUND_PLAZA", verbose_name="Arena (Round Plaza)"
)

ALL_MAPS = [
    COMMON,
    COMMON_FUNC,
    HIGH_WALL_OF_LOTHRIC,
    LOTHRIC_CASTLE,
    UNDEAD_SETTLEMENT,
    ARCHDRAGON_PEAK,
    FARRON_KEEP,
    GRAND_ARCHIVES,
    CATHEDRAL_OF_THE_DEEP,
    IRITHYLL,
    CATACOMBS_OF_CARTHUS,
    PROFANED_CAPITAL,
    FIRELINK_SHRINE,
    KILN_OF_THE_FIRST_FLAME,
    PAINTED_WORLD_OF_ARIANDEL,
    DREG_HEAP,
    RINGED_CITY,
    ARENA_GRAND_ROOF,
    ARENA_KILN_OF_FLAME,
    ARENA_DRAGON_RUINS,
    ARENA_ROUND_PLAZA,
]

ALL_MSB_FILE_NAMES = [m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem]


def get_map(source, block_id=None):
    return _get_map_base(source, block_id=block_id, game_maps=ALL_MAPS)
