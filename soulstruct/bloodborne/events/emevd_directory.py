from __future__ import annotations

__all__ = ["EventDirectory"]

import typing as tp

from soulstruct.base.events.emevd_directory import EventDirectory as _BaseEventDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.bloodborne.events.emevd.core import EMEVD
from soulstruct.bloodborne.maps.constants import *


class EventDirectory(_BaseEventDirectory):
    FILE_CLASS: tp.ClassVar = EMEVD
    ALL_MAPS: tp.ClassVar = ALL_MAPS_NO_CHALICE
    GET_MAP: tp.ClassVar = staticmethod(get_map)

    Common = map_property(COMMON)  # type: EMEVD
    HuntersDream = map_property(HUNTERS_DREAM)  # type: EMEVD
    AbandonedOldWorkshop = map_property(ABANDONED_OLD_WORKSHOP)  # type: EMEVD
    HemwickCharnelLane = map_property(HEMWICK_CHARNEL_LANE)  # type: EMEVD
    OldYharnam = map_property(OLD_YHARNAM)  # type: EMEVD
    CathedralWard = map_property(CATHEDRAL_WARD)  # type: EMEVD
    CentralYharnam = map_property(CENTRAL_YHARNAM)  # type: EMEVD
    UpperCathedralWard = map_property(UPPER_CATHEDRAL_WARD)  # type: EMEVD  # and Altar of Despair
    CastleCainhurst = map_property(CASTLE_CAINHURST)  # type: EMEVD
    NightmareOfMensis = map_property(NIGHTMARE_OF_MENSIS)  # type: EMEVD
    ForbiddenWoods = map_property(FORBIDDEN_WOODS)  # type: EMEVD
    Yahargul = map_property(YAHARGUL)  # type: EMEVD
    # ChaliceDungeon: map_property(CHALICE_DUNGEON)  # type: EMEVD
    Byrgenwerth = map_property(BYRGENWERTH)  # type: EMEVD  # and Lecture Building
    NightmareFrontier = map_property(NIGHTMARE_FRONTIER)  # type: EMEVD
    HuntersNightmare = map_property(HUNTERS_NIGHTMARE)  # type: EMEVD
    ResearchHall = map_property(RESEARCH_HALL)  # type: EMEVD
    FishingHamlet = map_property(FISHING_HAMLET)  # type: EMEVD
