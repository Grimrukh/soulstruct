from soulstruct.game_types import Map

__all__ = [
    "COMMON", "DEPTHS", "UNDEAD_BURG", "FIRELINK_SHRINE", "PAINTED_WORLD", "DARKROOT_GARDEN", "OOLACILE", "CATACOMBS",
    "TOMB_OF_THE_GIANTS", "ASH_LAKE", "BLIGHTTOWN", "LOST_IZALITH", "SENS_FORTRESS", "ANOR_LONDO", "NEW_LONDO_RUINS",
    "DUKES_ARCHIVES", "KILN_OF_THE_FIRST_FLAME", "UNDEAD_ASYLUM",

    "ALL_MAPS", "ALL_MSB_FILE_NAMES", "MAP_NAMES", "VERBOSE_MAP_NAMES",
]

class COMMON:
    """Dummy class that allows COMMON to be treated like a `Map` instance in scripts."""
    emevd_file_name = 'common'
    msb_file_name = None


DEPTHS = Map(10, 0)
UNDEAD_BURG = Map(10, 1)
FIRELINK_SHRINE = Map(10, 2)
PAINTED_WORLD = Map(11, 0)
DARKROOT_GARDEN = Map(12, 0, msb_file_name='m12_00_00_01')
OOLACILE = Map(12, 1)
CATACOMBS = Map(13, 0)
TOMB_OF_THE_GIANTS = Map(13, 1)
ASH_LAKE = Map(13, 2)
BLIGHTTOWN = Map(14, 0)
LOST_IZALITH = Map(14, 1)
SENS_FORTRESS = Map(15, 0)
ANOR_LONDO = Map(15, 1)
NEW_LONDO_RUINS = Map(16, 0)
DUKES_ARCHIVES = Map(17, 0)
KILN_OF_THE_FIRST_FLAME = Map(18, 0)
UNDEAD_ASYLUM = Map(18, 1)

ALL_MAPS = [COMMON, DEPTHS, UNDEAD_BURG, FIRELINK_SHRINE, PAINTED_WORLD, DARKROOT_GARDEN, OOLACILE, CATACOMBS,
            TOMB_OF_THE_GIANTS, ASH_LAKE, BLIGHTTOWN, LOST_IZALITH, SENS_FORTRESS, ANOR_LONDO,
            NEW_LONDO_RUINS, DUKES_ARCHIVES, KILN_OF_THE_FIRST_FLAME, UNDEAD_ASYLUM]

ALL_MSB_FILE_NAMES = [m.msb_file_name for m in ALL_MAPS if m.msb_file_name]

MAP_NAMES = {
    (10, 0): "DEPTHS",
    (10, 1): "UNDEAD_BURG",
    (10, 2): "FIRELINK_SHRINE",
    (11, 0): "PAINTED_WORLD",
    (12, 0): "DARKROOT_GARDEN",
    (12, 1): "OOLACILE",
    (13, 0): "CATACOMBS",
    (13, 1): "TOMB_OF_THE_GIANTS",
    (13, 2): "ASH_LAKE",
    (14, 0): "BLIGHTTOWN",
    (14, 1): "LOST_IZALITH",
    (15, 0): "SENS_FORTRESS",
    (15, 1): "ANOR_LONDO",
    (16, 0): "NEW_LONDO_RUINS",
    (17, 0): "DUKES_ARCHIVES",
    (18, 0): "KILN_OF_THE_FIRST_FLAME",
    (18, 1): "UNDEAD_ASYLUM",
}

VERBOSE_MAP_NAMES = {
    (10, 0): "Depths",
    (10, 1): "Undead Burg/Parish",
    (10, 2): "Firelink Shrine",
    (11, 0): "Painted World",
    (12, 0): "Darkroot Garden/Basin",
    (12, 1): "Oolacile, Chasm of the Abyss",
    (13, 0): "Catacombs",
    (13, 1): "Tomb of the Giants",
    (13, 2): "Great Hollow, Ash Lake",
    (14, 0): "Blighttown, Quelaag's Domain",
    (14, 1): "Demon Ruins, Lost Izalith",
    (15, 0): "Sen's Fortress",
    (15, 1): "Anor Londo",
    (16, 0): "New Londo Ruins, Valley of Drakes",
    (17, 0): "Duke's Archives, Crystal Cave",
    (18, 0): "Kiln of the First Flame",
    (18, 1): "Undead Asylum",
}
