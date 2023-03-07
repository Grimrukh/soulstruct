from __future__ import annotations

__all__ = ["MapStudioDirectory"]

import typing as tp

from soulstruct.base.game_file_directory import map_property
from soulstruct.base.maps.map_studio_directory import MapStudioDirectory as _BaseMapStudioDirectory

from .constants import *
from .msb import MSB


class MapStudioDirectory(_BaseMapStudioDirectory):
    """Bloodborne `MapStudio` directory.

    TODO: Chalice Dungeons (m29) are currently not supported.

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

    FILE_CLASS: tp.ClassVar = MSB
    ALL_MAPS: tp.ClassVar = tuple(m for m in ALL_MAPS if m.msb_file_stem)
    GET_MAP: tp.ClassVar = staticmethod(get_map)

    # Type hint override.
    files: dict[str, MSB]

    Common = map_property(COMMON)  # type: MSB
    HuntersDream = map_property(HUNTERS_DREAM)  # type: MSB
    AbandonedOldWorkshop = map_property(ABANDONED_OLD_WORKSHOP)  # type: MSB
    HemwickCharnelLane = map_property(HEMWICK_CHARNEL_LANE)  # type: MSB
    OldYharnam = map_property(OLD_YHARNAM)  # type: MSB
    CathedralWard = map_property(CATHEDRAL_WARD)  # type: MSB
    CentralYharnam = map_property(CENTRAL_YHARNAM)  # type: MSB
    UpperCathedralWard = map_property(UPPER_CATHEDRAL_WARD)  # type: MSB  # and Altar of Despair
    CastleCainhurst = map_property(CASTLE_CAINHURST)  # type: MSB
    NightmareOfMensis = map_property(NIGHTMARE_OF_MENSIS)  # type: MSB
    ForbiddenWoods = map_property(FORBIDDEN_WOODS)  # type: MSB
    Yahargul = map_property(YAHARGUL)  # type: MSB
    # ChaliceDungeon: map_property(CHALICE_DUNGEON)  # type: MSB
    Byrgenwerth = map_property(BYRGENWERTH)  # type: MSB  # and Lecture Building
    NightmareFrontier = map_property(NIGHTMARE_FRONTIER)  # type: MSB
    HuntersNightmare = map_property(HUNTERS_NIGHTMARE)  # type: MSB
    ResearchHall = map_property(RESEARCH_HALL)  # type: MSB
    FishingHamlet = map_property(FISHING_HAMLET)  # type: MSB
