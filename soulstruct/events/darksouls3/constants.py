import soulstruct.game_types as gt

__all__ = [
    "COMMON", "COMMON_FUNC", "HIGH_WALL_OF_LOTHRIC", "LOTHRIC_CASTLE", "UNDEAD_SETTLEMENT", "ARCHDRAGON_PEAK",
    "FARRON_KEEP", "GRAND_ARCHIVES", "CATHEDRAL_OF_THE_DEEP", "IRITHYLL", "CATACOMBS_OF_CARTHUS", "PROFANED_CAPITAL",
    "FIRELINK_SHRINE", "KILN_OF_THE_FIRST_FLAME", "PAINTED_WORLD_OF_ARIANDEL", "ARENA_GRAND_ROOF",
    "ARENA_KILN_OF_FLAME", "DREG_HEAP", "RINGED_CITY", "ARENA_DRAGON_RUINS", "ARENA_ROUND_PLAZA",

    "ALL_MAPS", "VERBOSE_MAP_NAMES",
]


class COMMON:
    emevd_file_name = 'common'
    msb_file_name = None

class COMMON_FUNC:
    emevd_file_name = 'common_func'
    msb_file_name = None


HIGH_WALL_OF_LOTHRIC = gt.Map(30, 0)
LOTHRIC_CASTLE = gt.Map(30, 1)  # includes Consumed King's Garden
UNDEAD_SETTLEMENT = gt.Map(31, 0)
ARCHDRAGON_PEAK = gt.Map(32, 0)
FARRON_KEEP = gt.Map(33, 0)  # includes Road of Sacrifices
GRAND_ARCHIVES = gt.Map(34, 1)
CATHEDRAL_OF_THE_DEEP = gt.Map(35, 0)
IRITHYLL = gt.Map(37, 0)  # includes Anor Londo
CATACOMBS_OF_CARTHUS = gt.Map(38, 0)  # includes Smouldering Lake and Demon Ruins
PROFANED_CAPITAL = gt.Map(39, 0)  # includes Irithyll Dungeon
FIRELINK_SHRINE = gt.Map(40, 0)  # includes Cemetery of Ash and Untended Graves (uses different event layers)
KILN_OF_THE_FIRST_FLAME = gt.Map(41, 0)
PAINTED_WORLD_OF_ARIANDEL = gt.Map(45, 0)
ARENA_GRAND_ROOF = gt.Map(46, 0)
ARENA_KILN_OF_FLAME = gt.Map(47, 0)
DREG_HEAP = gt.Map(50, 0)
RINGED_CITY = gt.Map(51, 0)
ARENA_DRAGON_RUINS = gt.Map(53, 0)
ARENA_ROUND_PLAZA = gt.Map(54, 0)

ALL_MAPS = [COMMON, COMMON_FUNC, HIGH_WALL_OF_LOTHRIC, LOTHRIC_CASTLE, UNDEAD_SETTLEMENT, ARCHDRAGON_PEAK, FARRON_KEEP,
            GRAND_ARCHIVES, CATHEDRAL_OF_THE_DEEP, IRITHYLL, CATACOMBS_OF_CARTHUS, PROFANED_CAPITAL, FIRELINK_SHRINE,
            KILN_OF_THE_FIRST_FLAME, PAINTED_WORLD_OF_ARIANDEL, DREG_HEAP, RINGED_CITY, ARENA_GRAND_ROOF,
            ARENA_KILN_OF_FLAME, ARENA_DRAGON_RUINS, ARENA_ROUND_PLAZA]

MAP_NAMES = {
    (30, 0): "HIGH_WALL_OF_LOTHRIC",
    (30, 1): "LOTHRIC_CASTLE",
    (31, 0): "UNDEAD_SETTLEMENT",
    (32, 0): "ARCHDRAGON_PEAK",
    (33, 0): "FARRON_KEEP",
    (34, 1): "GRAND_ARCHIVES",
    (35, 0): "CATHEDRAL_OF_THE_DEEP",
    (37, 0): "IRITHYLL",
    (38, 0): "CATACOMBS_OF_CARTHUS",
    (39, 0): "IRITHYLL_DUNGEON",
    (40, 0): "FIRELINK_SHRINE",
    (41, 0): "KILN_OF_THE_FIRST_FLAME",
    (45, 0): "PAINTED_WORLD_OF_ARIANDEL",
    (50, 0): "DREG_HEAP",
    (51, 0): "RINGED_CITY",
    (46, 0): "ARENA_GRAND_ROOF",
    (47, 0): "ARENA_KILN_OF_FLAME",
    (53, 0): "ARENA_DRAGON_RUINS",
    (54, 0): "ARENA_ROUND_PLAZA",
}

VERBOSE_MAP_NAMES = {
    (30, 0): "High Wall of Lothric",
    (30, 1): "Lothric Castle",
    (31, 0): "Undead Settlement",
    (32, 0): "Archdragon Peak",
    (33, 0): "Road of Sacrifices/Farron Keep",
    (34, 1): "Grand Archives",
    (35, 0): "Cathedral of the Deep",
    (37, 0): "Irithyll of the Boreal Valley/Anor Londo",
    (38, 0): "Catacombs of Carthus",
    (39, 0): "Irithyll Dungeon/Profaned Capital",
    (40, 0): "Firelink Shrine",
    (41, 0): "Kiln of the First Flame",
    (45, 0): "Painted World of Ariandel",
    (50, 0): "Dreg Heap",
    (51, 0): "Ringed City",
    (46, 0): "Arena (Grand Roof)",
    (47, 0): "Arena (Kiln of Flame)",
    (53, 0): "Arena (Dragon Ruins)",
    (54, 0): "Arena (Round Plaza)",
}
