from soulstruct.base.events.emevd_directory import EMEVDDirectory as _BaseEMEVDDirectory
from .emevd import EMEVD
from soulstruct.darksouls3.maps.constants import ALL_MAPS, get_map


# TODO: See http://soulsmodding.wikidot.com/reference:elden-ring-map-list


class EMEVDDirectory(_BaseEMEVDDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
    IS_DCX = True
    EMEVD_CLASS = EMEVD

    Common: EMEVD
    HighWallOfLothric: EMEVD
    LothricCastle: EMEVD
    UndeadSettlement: EMEVD
    ArchdragonPeak: EMEVD
    FarronKeep: EMEVD  # and Road of Sacrifices
    GrandArchives: EMEVD
    CathedralOfTheDeep: EMEVD
    Irithyll: EMEVD
    CatacombsOfCarthus: EMEVD
    ProfanedCapital: EMEVD  # and Irithyll Dungeon
    FirelinkShrine: EMEVD
    KilnOfTheFirstFlame: EMEVD
    PaintedWorldOfAriandel: EMEVD
    DregHeap: EMEVD
    RingedCity: EMEVD
    ArenaGrandRoof: EMEVD
    ArenaKilnOfFlame: EMEVD
    ArenaDragonRuins: EMEVD
    ArenaRoundPlaza: EMEVD
