from __future__ import annotations

__all__ = ["AIDirectory"]

import logging
import typing as tp

from soulstruct.ai.base.ai_directory import AIDirectory as _BaseAIDirectory
from soulstruct.maps.bloodborne.maps import ALL_MAPS_NO_CHALICE, get_map

if tp.TYPE_CHECKING:
    from soulstruct.ai.core import LuaBND

_LOGGER = logging.getLogger(__name__)


class AIDirectory(_BaseAIDirectory):
    """TODO: Chalice Dungeons (m29) are currently not supported."""
    MAPS = ALL_MAPS_NO_CHALICE
    GET_MAP = get_map
    EVENT_COMMON_NAME = "eventcommon"

    Common: LuaBND  # scripts loaded in all maps; also contains internal functions that should not be edited
    Event: LuaBND  # internal functions; never processed automatically
    HuntersDream: LuaBND
    AbandonedOldWorkshop: LuaBND
    HemwickCharnelLane: LuaBND
    OldYharnam: LuaBND
    CathedralWard: LuaBND
    CentralYharnam: LuaBND
    UpperCathedralWard: LuaBND  # and Altar of Despair
    CastleCainhurst: LuaBND
    NightmareOfMensis: LuaBND
    ForbiddenWoods: LuaBND
    Yahargul: LuaBND
    # ChaliceDungeon: LuaBND
    Byrgenwerth: LuaBND  # and Lecture Building
    NightmareFrontier: LuaBND
    HuntersNightmare: LuaBND
    ResearchHall: LuaBND
    FishingHamlet: LuaBND
