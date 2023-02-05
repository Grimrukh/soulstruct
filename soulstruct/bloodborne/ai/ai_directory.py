from __future__ import annotations

__all__ = ["AIDirectory"]

import logging
import typing as tp

from soulstruct.base.ai.ai_directory import AIDirectory as _BaseAIDirectory
from soulstruct.base.game_file_directory import map_property
from soulstruct.bloodborne.maps.constants import *

if tp.TYPE_CHECKING:
    from soulstruct.base.ai.luabnd import LuaBND

_LOGGER = logging.getLogger(__name__)


class AIDirectory(_BaseAIDirectory):
    """TODO: Chalice Dungeons (m29) are currently not supported."""
    ALL_MAPS = ALL_MAPS_NO_CHALICE_WITH_EVENT_COMMON
    GET_MAP = staticmethod(get_map)

    # Scripts loaded in all maps; also contains internal functions that should not be edited.
    Common = map_property(COMMON)  # type: LuaBND
    # Internal functions; never processed automatically.
    Event = map_property(EVENT_COMMON)  # type: LuaBND
    HuntersDream = map_property(HUNTERS_DREAM)  # type: LuaBND
    AbandonedOldWorkshop = map_property(ABANDONED_OLD_WORKSHOP)  # type: LuaBND
    HemwickCharnelLane = map_property(HEMWICK_CHARNEL_LANE)  # type: LuaBND
    OldYharnam = map_property(OLD_YHARNAM)  # type: LuaBND
    CathedralWard = map_property(CATHEDRAL_WARD)  # type: LuaBND
    CentralYharnam = map_property(CENTRAL_YHARNAM)  # type: LuaBND
    UpperCathedralWard = map_property(UPPER_CATHEDRAL_WARD)  # type: LuaBND  # and Altar of Despair
    CastleCainhurst = map_property(CASTLE_CAINHURST)  # type: LuaBND
    NightmareOfMensis = map_property(NIGHTMARE_OF_MENSIS)  # type: LuaBND
    ForbiddenWoods = map_property(FORBIDDEN_WOODS)  # type: LuaBND
    Yahargul = map_property(YAHARGUL)  # type: LuaBND
    # ChaliceDungeon: LuaBND
    Byrgenwerth = map_property(BYRGENWERTH)  # type: LuaBND  # and Lecture Building
    NightmareFrontier = map_property(NIGHTMARE_FRONTIER)  # type: LuaBND
    HuntersNightmare = map_property(HUNTERS_NIGHTMARE)  # type: LuaBND
    ResearchHall = map_property(RESEARCH_HALL)  # type: LuaBND
    FishingHamlet = map_property(FISHING_HAMLET)  # type: LuaBND
