from __future__ import annotations

__all__ = ["AIDirectory"]

import logging
import typing as tp

from soulstruct.ai.base.ai_directory import AIDirectory as _BaseAIDirectory
from soulstruct.maps.darksouls1.maps import ALL_MAPS, get_map

if tp.TYPE_CHECKING:
    from soulstruct.ai.core import LuaBND

_LOGGER = logging.getLogger(__name__)


class AIDirectory(_BaseAIDirectory):
    ALL_MAPS = ALL_MAPS
    GET_MAP = get_map
    EVENT_COMMON_NAME = "eventCommon"

    Common: LuaBND  # scripts loaded in all maps; also contains internal functions that should not be edited
    Event: LuaBND  # internal functions; never processed automatically
    Depths: LuaBND
    UndeadBurg: LuaBND  # and Undead Parish
    FirelinkShrine: LuaBND
    PaintedWorld: LuaBND
    DarkrootGarden: LuaBND  # and Darkroot Basin
    Oolacile: LuaBND  # and all DLC
    Catacombs: LuaBND
    TombOfTheGiants: LuaBND
    AshLake: LuaBND  # and Great Hollow
    Blighttown: LuaBND
    LostIzalith: LuaBND  # and Demon Ruins
    SensFortress: LuaBND
    AnorLondo: LuaBND
    NewLondoRuins: LuaBND  # and Valley of Drakes
    DukesArchives: LuaBND
    KilnOfTheFirstFlame: LuaBND
    UndeadAsylum: LuaBND
