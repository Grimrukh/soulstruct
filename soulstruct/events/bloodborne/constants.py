from soulstruct.game_types import Map


class COMMON:
    emevd_file_name = 'common'
    msb_file_name = None


class CHALICE_DUNGEON_COMMON:
    emevd_file_name = 'm29'
    msb_file_name = None


HUNTERS_DREAM = Map(21, 0)
ABANDONED_OLD_WORKSHOP = Map(21, 1)
HEMWICK_CHARNEL_LANE = Map(22, 0)
OLD_YHARNAM = Map(23, 0)
CATHEDRAL_WARD = Map(24, 0)
CENTRAL_YHARNAM = IOSEFKAS_CLINIC = Map(24, 1)
UPPER_CATHEDRAL_WARD = HEALING_CHURCH_WORKSHOP = ALTAR_OF_DESPAIR = Map(24, 2)
FORSAKEN_CASTLE_CAINHURST = CAINHURST = Map(25, 0)
NIGHTMARE_OF_MENSIS = Map(26, 0)
FORBIDDEN_WOODS = Map(27, 0)
YAHARGUL = UNSEEN_VILLAGE = Map(28, 0)
CHALICE_DUNGEON = Map(29, 0)
BYRGENWERTH = LECTURE_BUILDING = MOONSIDE_LAKE = Map(32, 0)
NIGHTMARE_FRONTIER = Map(33, 0)
HUNTERS_NIGHTMARE = Map(34, 0)
RESEARCH_HALL = Map(35, 0)
FISHING_HAMLET = Map(36, 0)

ALL_MAPS = [COMMON, HUNTERS_DREAM, ABANDONED_OLD_WORKSHOP, HEMWICK_CHARNEL_LANE, OLD_YHARNAM, CATHEDRAL_WARD,
            CENTRAL_YHARNAM, UPPER_CATHEDRAL_WARD, FORSAKEN_CASTLE_CAINHURST, NIGHTMARE_OF_MENSIS, FORBIDDEN_WOODS,
            YAHARGUL, BYRGENWERTH, NIGHTMARE_FRONTIER, HUNTERS_NIGHTMARE, RESEARCH_HALL, FISHING_HAMLET,
            CHALICE_DUNGEON_COMMON]

MAP_NAMES = {
    (21, 0): "HUNTERS_DREAM",
    (21, 1): "ABANDONED_OLD_WORKSHOP",
    (22, 0): "HEMWICK_CHARNEL_LANE",
    (23, 0): "OLD_YHARNAM",
    (24, 0): "CATHEDRAL_WARD",
    (24, 1): "CENTRAL_YHARNAM",
    (24, 2): "UPPER_CATHEDRAL_WARD",
    (25, 0): "CAINHURST",
    (26, 0): "NIGHTMARE_OF_MENSIS",
    (27, 0): "FORBIDDEN_WOODS",
    (28, 0): "YAHARGUL",
    (29, 0): "CHALICE_DUNGEON",
    (32, 0): "BYRGENWERTH",
    (33, 0): "NIGHTMARE_FRONTIER",
    (34, 0): "HUNTERS_NIGHTMARE",
    (35, 0): "RESEARCH_HALL",
    (36, 0): "FISHING_HAMLET",
}

VERBOSE_MAP_NAMES = {
    (21, 0): "Hunter's Dream",
    (21, 1): "Abandoned Old Workshop",
    (22, 0): "Hemwick Charnel Lane",
    (23, 0): "Old Yharnam",
    (24, 0): "Cathedral Ward",
    (24, 1): "Central Yharnam/Iosekfa's Clinic",
    (24, 2): "Upper Cathedral Ward/Healing Church Workshop",
    (25, 0): "Forsaken Castle Cainhurst",
    (26, 0): "Nightmare of Mensis",
    (27, 0): "Forbidden Woods",
    (28, 0): "Yahar'gul, Unseen Village",
    (32, 0): "Byrgenwerth/Lecture Building",
    (33, 0): "Nightmare Frontier",
    (34, 0): "Hunter's Nightmare'",
    (35, 0): "Research Hall/Astral Clocktower",
    (36, 0): "Fishing Hamlet",
}
