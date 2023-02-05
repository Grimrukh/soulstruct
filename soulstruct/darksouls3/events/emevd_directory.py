from __future__ import annotations

__all__ = ["EMEVDDirectory"]

from soulstruct.base.events.emevd_directory import EMEVDDirectory as _BaseEMEVDDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.darksouls3.events.emevd.core import EMEVD
from soulstruct.darksouls3.maps.constants import *


class EMEVDDirectory(_BaseEMEVDDirectory):
    FILE_CLASS = EMEVD
    COMMON_FUNC = COMMON_FUNC
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)

    Common = map_property(COMMON)  # type: EMEVD
    CommonFunc = map_property(COMMON_FUNC)  # type: EMEVD
    HighWallOfLothric = map_property(HIGH_WALL_OF_LOTHRIC)  # type: EMEVD
    LothricCastle = map_property(LOTHRIC_CASTLE)  # type: EMEVD
    UndeadSettlement = map_property(UNDEAD_SETTLEMENT)  # type: EMEVD
    ArchdragonPeak = map_property(ARCHDRAGON_PEAK)  # type: EMEVD
    FarronKeep = map_property(FARRON_KEEP)  # type: EMEVD
    GrandArchives = map_property(GRAND_ARCHIVES)  # type: EMEVD
    CathedralOfTheDeep = map_property(CATHEDRAL_OF_THE_DEEP)  # type: EMEVD
    Irithyll = map_property(IRITHYLL)  # type: EMEVD
    CatacombsOfCarthus = map_property(CATACOMBS_OF_CARTHUS)  # type: EMEVD
    ProfanedCapital = map_property(PROFANED_CAPITAL)  # type: EMEVD
    FirelinkShrine = map_property(FIRELINK_SHRINE)  # type: EMEVD
    KilnOfTheFirstFlame = map_property(KILN_OF_THE_FIRST_FLAME)  # type: EMEVD
    PaintedWorldOfAriandel = map_property(PAINTED_WORLD_OF_ARIANDEL)  # type: EMEVD
    DregHeap = map_property(ARENA_GRAND_ROOF)  # type: EMEVD
    RingedCity = map_property(ARENA_KILN_OF_FLAME)  # type: EMEVD
    ArenaGrandRoof = map_property(DREG_HEAP)  # type: EMEVD
    ArenaKilnOfFlame = map_property(RINGED_CITY)  # type: EMEVD
    ArenaDragonRuins = map_property(ARENA_DRAGON_RUINS)  # type: EMEVD
    ArenaRoundPlaza = map_property(ARENA_ROUND_PLAZA)  # type: EMEVD
