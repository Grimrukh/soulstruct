from soulstruct.base.events.emevd_directory import EMEVDDirectory as _BaseEMEVDDirectory
from soulstruct.darksouls3.events.emevd.core import EMEVD
from soulstruct.darksouls3.maps import COMMON_FUNC, ALL_MAPS, get_map


class EMEVDDirectory(_BaseEMEVDDirectory):
    COMMON_FUNC = COMMON_FUNC
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
    IS_DCX = True
    EMEVD_CLASS = EMEVD

    Common: EMEVD
    CommonFunc: EMEVD
    HighWallOfLothric: EMEVD
    LothricCastle: EMEVD
    UndeadSettlement: EMEVD
    ArchdragonPeak: EMEVD
    FarronKeep: EMEVD
    GrandArchives: EMEVD
    CathedralOfTheDeep: EMEVD
    Irithyll: EMEVD
    CatacombsOfCarthus: EMEVD
    ProfanedCapital: EMEVD
    FirelinkShrine: EMEVD
    KilnOfTheFirstFlame: EMEVD
    PaintedWorldOfAriandel: EMEVD
    DregHeap: EMEVD
    RingedCity: EMEVD
    ArenaGrandRoof: EMEVD
    ArenaKilnOfFlame: EMEVD
    ArenaDragonRuins: EMEVD
    ArenaRoundPlaza: EMEVD
