from soulstruct.base.events.emevd_directory import EMEVDDirectory as _BaseEMEVDDirectory
from soulstruct.bloodborne.events.emevd.core import EMEVD
from soulstruct.bloodborne.maps.constants import ALL_MAPS_NO_CHALICE, get_map


class EMEVDDirectory(_BaseEMEVDDirectory):
    ALL_MAPS = ALL_MAPS_NO_CHALICE
    GET_MAP = staticmethod(get_map)
    IS_DCX = True
    EMEVD_CLASS = EMEVD

    Common: EMEVD
    HuntersDream: EMEVD
    AbandonedOldWorkshop: EMEVD
    HemwickCharnelLane: EMEVD
    OldYharnam: EMEVD
    CathedralWard: EMEVD
    CentralYharnam: EMEVD
    UpperCathedralWard: EMEVD  # and Altar of Despair
    CastleCainhurst: EMEVD
    NightmareOfMensis: EMEVD
    ForbiddenWoods: EMEVD
    Yahargul: EMEVD
    # ChaliceDungeon: EMEVD
    Byrgenwerth: EMEVD  # and Lecture Building
    NightmareFrontier: EMEVD
    HuntersNightmare: EMEVD
    ResearchHall: EMEVD
    FishingHamlet: EMEVD
