from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory

from .constants import ALL_MAPS_NO_CHALICE, get_map
from .msb import MSB


class MapStudioDirectory(_BaseMapStudioDirectory):
    """Bloodborne `MapStudio` directory.

    TODO: Chalice dungeons (m29) are currently not supported.

    Unlike Dark Souls, it is possible that the copy of Bloodborne you have access to could have a different patch level,
    which may affect the latest version of each MSB you have. Currently, this class only supports the latest patch 1.09,
    which means the following non-zero MSB versions are asserted:
        m23_00_00_01
        m24_00_00_01
        m24_01_00_11
        m24_02_00_01
        m27_00_00_01
        m28_00_00_01
        m32_00_00_01

    You can always rename your MSB file to this latest version until it is properly supported by Soulstruct (which may
    never happen).
    """

    MSB_CLASS = MSB
    ALL_MAPS = ALL_MAPS_NO_CHALICE
    GET_MAP = staticmethod(get_map)
    IS_DCX = True

    HuntersDream: MSB
    AbandonedOldWorkshop: MSB
    HemwickCharnelLane: MSB
    OldYharnam: MSB
    CathedralWard: MSB
    CentralYharnam: MSB
    UpperCathedralWard: MSB  # and Altar of Despair
    CastleCainhurst: MSB
    NightmareOfMensis: MSB
    ForbiddenWoods: MSB
    Yahargul: MSB
    # ChaliceDungeon: MSB
    Byrgenwerth: MSB  # and Lecture Building
    NightmareFrontier: MSB
    HuntersNightmare: MSB
    ResearchHall: MSB
    FishingHamlet: MSB
