__all__ = [
    "COMMON",
    "HUNTERS_DREAM",
    "ABANDONED_OLD_WORKSHOP",
    "HEMWICK_CHARNEL_LANE",
    "OLD_YHARNAM",
    "CATHEDRAL_WARD",
    "CENTRAL_YHARNAM",
    "UPPER_CATHEDRAL_WARD",
    "CASTLE_CAINHURST",
    "NIGHTMARE_OF_MENSIS",
    "FORBIDDEN_WOODS",
    "YAHARGUL",
    "CHALICE_DUNGEON",
    "UNKNOWN_MAP_30",  # referenced by some unused `MSBMapConnection` instances
    "BYRGENWERTH",
    "NIGHTMARE_FRONTIER",
    "HUNTERS_NIGHTMARE",
    "RESEARCH_HALL",
    "FISHING_HAMLET",
    "ALL_MAPS",
    "ALL_MAPS_NO_CHALICE",
    "ALL_MSB_FILE_NAMES",
    "get_map",
]

from soulstruct.maps.utilities import get_map as _get_map_base
from soulstruct.game_types.msb_types import Map

COMMON = Map(
    None,
    None,
    name="Common",
    emevd_file_stem="common",
    msb_file_stem=None,
    ai_file_stem="aiCommon",  # TODO: May not be correct.
    esd_file_stem=None,
    variable_name="COMMON",
    verbose_name="Common",
)
HUNTERS_DREAM = Map(
    21,
    0,
    name="HuntersDream",
    variable_name="HUNTERS_DREAM",
    verbose_name="Hunter's Dream",
)
ABANDONED_OLD_WORKSHOP = Map(
    21,
    1,
    name="AbandonedOldWorkshop",
    variable_name="ABANDONED_OLD_WORKSHOP",
    verbose_name="Abandoned Old Workshop",
)
HEMWICK_CHARNEL_LANE = Map(
    22,
    0,
    name="HemwickCharnelLane",
    variable_name="HEMWICK_CHARNEL_LANE",
    verbose_name="Hemwick Charnel Lane",
)
OLD_YHARNAM = Map(
    23,
    0,
    name="OldYharnam",
    variable_name="OLD_YHARNAM",
    verbose_name="Old Yharnam",
)
CATHEDRAL_WARD = Map(
    24,
    0,
    name="CathedralWard",
    variable_name="CATHEDRAL_WARD",
    verbose_name="Cathedral Ward",
)
CENTRAL_YHARNAM = Map(
    24,
    1,
    name="CentralYharnam",
    variable_name="CENTRAL_YHARNAM",
    verbose_name="Central Yharnam / Iosekfa's Clinic",
)
UPPER_CATHEDRAL_WARD = Map(
    24,
    2,
    name="UpperCathedralWard",
    variable_name="UPPER_CATHEDRAL_WARD",
    verbose_name="Upper Cathedral Ward / Healing Church Workshop",
)
CASTLE_CAINHURST = Map(
    25,
    0,
    name="CastleCainhurst",
    variable_name="CASTLE_CAINHURST",
    verbose_name="Castle Cainhurst",
)
NIGHTMARE_OF_MENSIS = Map(
    26,
    0,
    name="NightmareOfMensis",
    variable_name="NIGHTMARE_OF_MENSIS",
    verbose_name="Nightmare of Mensis",
)
FORBIDDEN_WOODS = Map(
    27,
    0,
    name="ForbiddenWoods",
    variable_name="FORBIDDEN_WOODS",
    verbose_name="Forbidden Woods",
)
YAHARGUL = Map(
    28,
    0,
    name="Yahargul",
    variable_name="YAHARGUL",
    verbose_name="Yahar'gul, Unseen Village",
)
CHALICE_DUNGEON = Map(
    29,
    0,
    emevd_file_stem="m29",
    name="ChaliceDungeon",
    variable_name="CHALICE_DUNGEON",
    verbose_name="Chalice Dungeon",
)
UNKNOWN_MAP_30 = Map(  # Referenced by one vanilla (cut) MapConnection at the start of Castle Cainhurst.
    30,
    0,
    emevd_file_stem=None,
    name="UnknownMap30",
    variable_name="UNKNOWN_MAP_30",
    verbose_name="Unknown Map (30, 0)",
)
BYRGENWERTH = Map(
    32,
    0,
    name="Byrgenwerth",
    variable_name="BYRGENWERTH",
    verbose_name="Byrgenwerth / Lecture Building",
)
NIGHTMARE_FRONTIER = Map(
    33,
    0,
    name="NightmareFrontier",
    variable_name="NIGHTMARE_FRONTIER",
    verbose_name="Nightmare Frontier",
)
HUNTERS_NIGHTMARE = Map(
    34,
    0,
    name="HuntersNightmare",
    variable_name="HUNTERS_NIGHTMARE",
    verbose_name="Hunter's Nightmare",
)
RESEARCH_HALL = Map(
    35,
    0,
    name="ResearchHall",
    variable_name="RESEARCH_HALL",
    verbose_name="Research Hall",
)
FISHING_HAMLET = Map(
    36,
    0,
    name="FishingHamlet",
    variable_name="FISHING_HAMLET",
    verbose_name="Fishing Hamlet",
)

ALL_MAPS = [
    COMMON,
    HUNTERS_DREAM,
    ABANDONED_OLD_WORKSHOP,
    HEMWICK_CHARNEL_LANE,
    OLD_YHARNAM,
    CATHEDRAL_WARD,
    CENTRAL_YHARNAM,
    UPPER_CATHEDRAL_WARD,
    CASTLE_CAINHURST,
    NIGHTMARE_OF_MENSIS,
    FORBIDDEN_WOODS,
    YAHARGUL,
    CHALICE_DUNGEON,
    BYRGENWERTH,
    NIGHTMARE_FRONTIER,
    HUNTERS_NIGHTMARE,
    RESEARCH_HALL,
    FISHING_HAMLET,
]

ALL_MAPS_NO_CHALICE = [
    COMMON,
    HUNTERS_DREAM,
    ABANDONED_OLD_WORKSHOP,
    HEMWICK_CHARNEL_LANE,
    OLD_YHARNAM,
    CATHEDRAL_WARD,
    CENTRAL_YHARNAM,
    UPPER_CATHEDRAL_WARD,
    CASTLE_CAINHURST,
    NIGHTMARE_OF_MENSIS,
    FORBIDDEN_WOODS,
    YAHARGUL,
    BYRGENWERTH,
    NIGHTMARE_FRONTIER,
    HUNTERS_NIGHTMARE,
    RESEARCH_HALL,
    FISHING_HAMLET,
]

ALL_MSB_FILE_NAMES = [m.msb_file_stem for m in ALL_MAPS if m.msb_file_stem]


def get_map(source, block_id=None):
    if source in {30, (30, 0), (30, 1)}:
        # Reference to missing map m30_00_00_00 in Castle Cainhurst (m25_00_00_00).
        return UNKNOWN_MAP_30
    return _get_map_base(source, block_id=block_id, game_maps=ALL_MAPS)
