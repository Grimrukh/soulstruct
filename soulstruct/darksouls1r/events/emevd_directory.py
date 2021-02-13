from soulstruct.base.events.emevd_directory import EMEVDDirectory as _BaseEMEVDDirectory
from .emevd import EMEVD
from ..maps.constants import ALL_MAPS, get_map


class EMEVDDirectory(_BaseEMEVDDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
    IS_DCX = True  # only difference to DS1PTDE
    EMEVD_CLASS = EMEVD

    Common: EMEVD
    Depths: EMEVD
    UndeadBurg: EMEVD  # and Undead Parish
    FirelinkShrine: EMEVD
    PaintedWorld: EMEVD
    DarkrootGarden: EMEVD  # and Darkroot Basin
    Oolacile: EMEVD  # and all DLC
    Catacombs: EMEVD
    TombOfTheGiants: EMEVD
    AshLake: EMEVD  # and Great Hollow
    Blighttown: EMEVD
    LostIzalith: EMEVD  # and Demon Ruins
    SensFortress: EMEVD
    AnorLondo: EMEVD
    NewLondoRuins: EMEVD  # and Valley of Drakes
    DukesArchives: EMEVD
    KilnOfTheFirstFlame: EMEVD
    UndeadAsylum: EMEVD
